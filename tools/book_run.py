#!/usr/bin/env python3
"""Run every Zayn declaration of every chapter through the reference verifier, and judge each against its promise.

Lineage: adapted from the Softanza book's tools/book_run.py (softanza-book a9e3812). Kept: one record per block in book
order, a verdict per block, nothing a block prints stored in a source file (the answers go to data/book-run.json and the
page shows them from there), an `exercise` fence recorded as the reader's to run, exit status 1 when a chapter's blocks
do not all keep their promise. Changed: a block is a .zayn file, and the runtime is the reference verifier of the pinned
snapshot, `node <snapshot>/tools/zayn/cli.js check <file> --level N`, run twice: with --json for the findings that are
judged, and without for the report a person reads, which the page prints as the run printed it.

The chapter's court is run too: each fixture a chapter names in its front matter is checked in the snapshot against the
verdict the suite's manifest expects for it (the set of diagnostic ids, compared exactly).

    python tools/book_run.py                 # Zayn at the pin
    python tools/book_run.py --commit <sha>  # Zayn at a named commit, to see what moving the pin would do
"""
import json, re, shutil, subprocess, sys
from book_common import (sources, code_blocks, block_hash, snapshot, law_data, law_facts, now, stamp, save_json,
                         gbnf_regex, shell_blocks, symbol_tables, CACHE, PIN)
import shlex
from book_judge import parse, verdict, PROMISE

NODE = shutil.which("node") or "node"


def check(cli, cwd, name, level, as_json, symbols=None):
    cmd = [NODE, str(cli), "check", name, "--level", str(level)]
    if as_json:
        cmd.append("--json")
    if symbols:
        cmd += ["--symbols", symbols]
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    return p.returncode, (p.stdout or "").replace("\r", ""), (p.stderr or "").replace("\r", "")


def run_block(cli, work, k, b, grammar=None):
    promises, stated = parse(b["text"])
    rec = {"hash": b["hash"], "name": b["name"] or f"declaration-{k + 1}.zayn", "level": b["level"],
           "symbols": b.get("symbols"), "flags": b["flags"], "promise": [list(p) for p in promises], "stated": stated}
    if "gbnf" in b["flags"] and grammar is not None:
        # the flag asks for the grammar for generation's answer too, on the lines that are not promises
        bare = "\n".join(l for l in b["text"].replace("\r", "").split("\n") if not PROMISE.match(l)).strip("\n") + "\n"
        rec["grammar"] = bool(grammar.fullmatch(bare))
    if "exercise" in b["flags"]:
        rec.update(verdict="exercise", report="", diagnostics=[])
        return rec
    d = work / f"{k + 1:02d}"
    d.mkdir(parents=True)
    (d / rec["name"]).parent.mkdir(parents=True, exist_ok=True)
    (d / rec["name"]).write_text(b["text"] + "\n", encoding="utf-8", newline="\n")
    symbols = None
    if b.get("symbols"):
        if b.get("table") is None:
            rec.update(verdict="not-run", why=f"the symbol table {b['symbols']} is not written on the page", report="",
                       diagnostics=[])
            return rec
        try:
            json.loads(b["table"])
        except json.JSONDecodeError as e:
            rec.update(verdict="not-run", why=f"the symbol table {b['symbols']} is not JSON ({e})", report="", diagnostics=[])
            return rec
        (d / b["symbols"]).write_text(b["table"] + "\n", encoding="utf-8", newline="\n")
        symbols = b["symbols"]
    code, out, err = check(cli, d, rec["name"], b["level"], True, symbols)
    try:
        env = json.loads(out)
    except json.JSONDecodeError:
        rec.update(verdict="not-run", why="the verifier did not answer in its machine form", report=(out + err).strip()[-2000:],
                   diagnostics=[], exit=code)
        return rec
    diags = [{"code": x.get("code"), "severity": x.get("severity"), "subject": x.get("subject"),
              "line": (x.get("span") or {}).get("line"), "cites": x.get("cites") or [], "level": x.get("level"),
              "message": x.get("message")} for x in env.get("diagnostics", [])]
    code2, report, _ = check(cli, d, rec["name"], b["level"], False, symbols)
    if not stated:
        v = "unpromised"
    else:
        v = "kept" if verdict(promises, diags) else "differs"
    rec.update(verdict=v, exit=code2, report=report.rstrip(), diagnostics=diags, envelope=out.rstrip(),
               contract=env.get("contract"))
    return rec


def run_shell(cli, work, k, sb, files, tables):
    """One ```shell fence: each `$ zayn …` line run by the reference command in a folder holding the chapter's files so far.
    The arguments are split as a shell would split them, and no pattern is expanded: the command reads each as a path."""
    d = work / f"shell-{k + 1:02d}"
    d.mkdir(parents=True)
    for name, text in files.items():
        (d / name).parent.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(text + "\n", encoding="utf-8", newline="\n")
    for name, table in tables.items():
        (d / name).write_text(table + "\n", encoding="utf-8", newline="\n")
    parts, last = [], None
    for c in sb["commands"]:
        argv = shlex.split(c)
        if not argv or argv[0] != "zayn":
            raise SystemExit(f"a shell fence runs the zayn command only: {c}")
        p = subprocess.run([NODE, str(cli)] + argv[1:], cwd=d, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=120)
        out = ((p.stdout or "") + (p.stderr or "")).replace("\r", "")
        out = out.replace(str(d) + "\\", "").replace(str(d) + "/", "").replace(str(d), ".")
        parts.append({"command": c, "output": out.rstrip("\n"), "exit": p.returncode})
        last = p.returncode
    kept = sb["exit"] is not None and last == sb["exit"]
    return {"hash": sb["hash"], "runs": parts, "exit": last, "promise": sb["exit"], "verdict": "kept" if kept else "differs"}


def run_court(cli, snap, law, names, work):
    """Each named fixture, checked in the snapshot against the manifest's expected ids."""
    out = []
    for name in names or []:
        file = name if name.endswith(".zayn") else name + ".zayn"
        fx = law["fixtures"].get(file)
        if not fx or not (snap / "conformance" / "fixtures" / file).exists():
            out.append({"file": file, "exists": False})
            continue
        symbols = None
        if fx.get("symbols"):
            work.mkdir(parents=True, exist_ok=True)
            sp = work / (file + ".symbols.json")
            sp.write_text(json.dumps(fx["symbols"]), encoding="utf-8")
            symbols = str(sp)
        _, raw, _ = check(cli, snap, f"conformance/fixtures/{file}", 4, True, symbols)
        try:
            got = sorted({x.get("code") for x in json.loads(raw).get("diagnostics", [])})
        except json.JSONDecodeError:
            got = None
        want = sorted(set(fx.get("expect_ids", [])))
        out.append({"file": file, "exists": True, "level": fx.get("level"), "expect_ids": want, "got_ids": got,
                    "pass": got == want})
    return out


def run_suite(snap):
    """The conformance suite, run by its own runner in the snapshot, at each of the four levels. The page that tells the
    suite prints this run; its counts become facts ({{n:suite.4.pass}})."""
    out = {}
    for level in (1, 2, 3, 4):
        p = subprocess.run([NODE, "tools/zayn/conformance.js", "--level", str(level)], cwd=snap, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=300)
        text = (p.stdout or "").replace("\r", "").strip("\n")
        m = re.search(r"pass (\d+) \S+ fail (\d+) \S+ skipped (\d+)", text)
        out[str(level)] = {"command": f"node tools/zayn/conformance.js --level {level}", "exit": p.returncode,
                           "output": text, "pass": int(m.group(1)) if m else None,
                           "fail": int(m.group(2)) if m else None, "skipped": int(m.group(3)) if m else None}
    return out


def main():
    commit = sys.argv[sys.argv.index("--commit") + 1] if "--commit" in sys.argv else PIN
    snap, prov = snapshot(commit)
    cli = snap / "tools" / "zayn" / "cli.js"
    law = law_data(snap)
    node_v = subprocess.run([NODE, "--version"], capture_output=True, text=True).stdout.strip() or None
    grammar = gbnf_regex(snap) if (snap / "haro" / "zayn.gbnf").exists() else None
    started = now()
    result = {"run": {"date": stamp(started), "zayn": prov, "law": law_facts(snap), "node": node_v,
                      "verifier": "tools/zayn/cli.js, the reference verifier, in the snapshot"}, "chapters": {}}
    suite = run_suite(snap)
    result["run"]["suite"] = suite
    for level, rec in suite.items():
        for key in ("pass", "fail", "skipped", "exit"):
            result["run"]["law"][f"suite.{level}.{key}"] = rec[key]
    failed = []
    work_root = CACHE / "run"
    shutil.rmtree(work_root, ignore_errors=True)
    for path, meta, body in sources("en"):
        key = f"en/{path.stem}"
        work = work_root / path.stem
        t0 = now()
        cbs = code_blocks(body)
        records = [run_block(cli, work, k, b, grammar) for k, b in enumerate(cbs)]
        shells = []
        tables = symbol_tables(body)
        for k, sb in enumerate(shell_blocks(body)):
            files = {}
            for b in cbs:
                if b["end"] <= sb["start"] and b.get("name"):
                    files[b["name"]] = b["text"]
            shells.append(run_shell(cli, work, k, sb, files, tables))
        court = run_court(cli, snap, law, meta.get("fixtures"), work / "court")
        runnable = [r for r in records if r["verdict"] != "exercise"]
        kept = sum(1 for r in runnable if r["verdict"] == "kept")
        ch = {"id": meta["id"], "blocks": records, "kept": kept, "runnable": len(runnable),
              "exercises": len(records) - len(runnable), "court": court, "shell": shells, "ran": stamp(t0)}
        result["chapters"][key] = ch
        line = f"{key}: {kept} of {len(runnable)} declarations kept their promise"
        bad_court = [c["file"] for c in court if not c.get("exists") or not c.get("pass")]
        if court:
            line += f"; court: {len(court) - len(bad_court)} of {len(court)} fixtures answer as the manifest expects"
        if shells:
            line += f"; command lines: {sum(1 for s in shells if s['verdict'] == 'kept')} of {len(shells)} as stated"
        bad_shell = [f"shell {i + 1}" for i, s in enumerate(shells) if s["verdict"] != "kept"]
        if (runnable and kept < len(runnable)) or bad_court or bad_shell:
            failed.append(key)
            line += "  <- FAILS: " + ", ".join(sorted({r["verdict"] for r in runnable if r["verdict"] != "kept"}) + bad_court + bad_shell)
        print(line, flush=True)
    bad_suite = [level for level, rec in suite.items() if rec["exit"] != 0]
    if bad_suite:
        failed.append("the suite's own runner, at level " + ", ".join(bad_suite))
    print("suite: " + "; ".join(f"level {l}: pass {r['pass']}, fail {r['fail']}, skipped {r['skipped']}" for l, r in suite.items()))
    result["run"]["failed"] = failed
    save_json("book-run.json", result)
    shutil.rmtree(work_root, ignore_errors=True)
    print(f"Zayn at {prov['short']} ({prov.get('tag') or 'no tag'}), law {result['run']['law']['law.version']}, "
          f"Node {node_v} -> data/book-run.json")
    if failed:
        print(f"FAILED: {len(failed)} chapter(s) did not keep all their promises")
        sys.exit(1)


if __name__ == "__main__":
    main()
