"""What the book's tools share: the sources, their declarations, and the Zayn snapshot they run against.

Lineage: adapted from the Softanza book's tools/book_common.py (softanza-book a9e3812). Kept as they were: ROOT, SRC, DATA,
CACHE, FENCE, now, stamp, read_source, sources, structure, block_hash, load_json, save_json. Changed: the library snapshot with
its engine binaries is replaced by a snapshot of the Zayn repository at the pin. It needs no binary, because the reference
verifier is JavaScript (tools/zayn/cli.js) and Node runs it.

Zayn is never run in its working checkout: other sessions write that tree every day. The runner exports the tree at the pinned
commit into .cache/ (git archive, which reads the repository's history and writes nothing in it) and runs there. Every number
the book prints about the law is read from the snapshot's data files by law_facts(), never typed.
"""
import csv, hashlib, json, re, subprocess, pathlib, datetime
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DATA = ROOT / "data"
CACHE = ROOT / ".cache"
ZAYN_REPO = pathlib.Path("D:/GitHub/zayn")            # the Zayn repository, read only
# THE PIN: the commit the release v0.2.0 of Zayn names (the tag v0.2.0 on GitHub, 2026-11-21). A commit, never a branch:
# main moves past the release. Moving the pin is a decision with a row in DECISIONS.md, followed by a full run.
PIN = "adaecc271dd68e10690eb0166ccb2b1f5d8d1528"
PIN_TAG = "v0.2.0"
GH_BLOB = "https://github.com/mayouni/zayn/blob/{tag}/{path}"

FENCE = re.compile(r"(?ms)^```([^\n]*)\n(.*?)^```[ \t]*$")
CODE_TAG = "zayn"


def now():
    """One reading of the clock, never composed."""
    return datetime.datetime.now().astimezone()


def stamp(t):
    """A clock reading as the book prints it: date, minute and the offset from UTC."""
    z = t.strftime("%z")
    return t.strftime("%Y-%m-%d %H:%M ") + "UTC" + (z[:3] + ":" + z[3:] if z else "")


def read_source(path):
    """Front matter (a dict) and body (Markdown) of one chapter file."""
    text = path.read_text(encoding="utf-8").replace("\r", "")
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: no front matter")
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm) or {}
    for key in ("id", "number", "title", "status"):
        if key not in meta:
            raise SystemExit(f"{path}: front matter has no '{key}'")
    return meta, body.lstrip("\n")


def sources(lang):
    """The chapter files of one language, in book order."""
    d = SRC / lang
    if not d.exists():
        return []
    out = [(p, *read_source(p)) for p in sorted(d.glob("*.md"))]
    return sorted(out, key=lambda r: r[1]["number"])


def structure():
    return yaml.safe_load((SRC / "structure.yaml").read_text(encoding="utf-8"))


def block_hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def symbol_tables(body):
    """The symbol tables a chapter writes for its level 3 declarations: one ```symbols <name.json> fence each.
    A symbol table is what a declaration cannot know about the system around it: its entities, actors, state, elements."""
    out = {}
    for m in FENCE.finditer(body):
        info = m.group(1).strip().split()
        if info and info[0].lower() == "symbols":
            out[info[1] if len(info) > 1 else "symbols.json"] = m.group(2).rstrip("\n")
    return out


def code_blocks(body):
    """Every Zayn fence of a chapter, in order. The info string after `zayn` holds, in any order: a file name
    (`payments.zayn`, the name the report prints), `level=N` (default 2), `symbols=<name.json>` (a symbol table written
    on the same page in a ```symbols fence), and the flags `exercise` and `envelope`. A block's hash covers what its
    run depends on: its text, its level when it is not 2, and its symbol table."""
    out = []
    tables = symbol_tables(body)
    for m in FENCE.finditer(body):
        info = m.group(1).strip().split()
        if not info or info[0].lower() != CODE_TAG:
            continue
        name, level, flags, symbols = None, 2, [], None
        for w in info[1:]:
            lw = w.lower()
            if lw.endswith(".zayn"):
                name = w
            elif lw.startswith("level="):
                level = int(w.split("=", 1)[1])
            elif lw.startswith("symbols="):
                symbols = w.split("=", 1)[1]
            else:
                flags.append(lw)
        text = m.group(2).rstrip("\n")
        table = tables.get(symbols) if symbols else None
        key = text + (f"\n@level {level}" if level != 2 else "") + (f"\n@symbols {table}" if symbols else "")
        out.append({"flags": flags, "name": name, "level": level, "symbols": symbols, "table": table, "text": text,
                    "hash": block_hash(key), "start": m.start(), "end": m.end()})
    return out


# --------------------------------------------------------------------------- Zayn, pinned

def git(*args):
    return subprocess.run(["git", "-C", str(ZAYN_REPO), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=True).stdout.strip()


def snapshot(commit=None):
    """The Zayn tree at one commit, exported once into .cache/. Returns (path, provenance dict)."""
    sha = git("rev-parse", (commit or PIN) + "^{commit}")
    short = sha[:9]
    base = CACHE / f"zayn-{short}"
    prov_file = base / "provenance.json"
    if not (base / "constitution" / "rules.json").exists():
        base.mkdir(parents=True, exist_ok=True)
        archive = subprocess.Popen(["git", "-C", str(ZAYN_REPO), "archive", sha], stdout=subprocess.PIPE)
        subprocess.run(["tar", "-x", "-C", str(base)], stdin=archive.stdout, check=True)
        archive.wait()
    if not prov_file.exists():
        prov = {
            "commit": sha, "short": short, "tag": PIN_TAG if sha == PIN else None,
            "commit_date": git("show", "-s", "--format=%ci", sha),
            "exported": stamp(now()),
            "how": "git archive of the commit into .cache/; nothing is run from the Zayn working tree",
        }
        prov_file.write_text(json.dumps(prov, indent=1), encoding="utf-8")
    return base, json.loads(prov_file.read_text(encoding="utf-8"))


def _rules(law):
    out = []
    for key in sorted((k for k in law if re.fullmatch(r"set\d+", k)), key=lambda k: int(k[3:])):
        s = law[key]
        for r in (s.get("rules") or []):
            out.append({**r, "_set": key, "_set_title": s.get("title", "")})
    return out


def law_data(snap):
    """The law and the contract as the snapshot holds them: rules by number, articles, rights, diagnostics, fixtures."""
    law = json.loads((snap / "constitution" / "rules.json").read_text(encoding="utf-8"))
    contract = json.loads((snap / "conformance" / "violations.json").read_text(encoding="utf-8"))
    manifest = json.loads((snap / "conformance" / "manifest.json").read_text(encoding="utf-8"))
    rules = _rules(law)
    diags = contract["diagnostics"] if isinstance(contract["diagnostics"], list) else list(contract["diagnostics"].values())
    return {"law": law, "rules": {str(r["number"]): r for r in rules}, "rule_list": rules,
            "articles": law.get("articles", {}), "rights": {r["id"]: r for r in law.get("rights", [])},
            "contract": contract, "diagnostics": {d["id"]: d for d in diags}, "diag_list": diags,
            "manifest": manifest, "fixtures": {f["file"]: f for f in manifest.get("fixtures", [])}}


def law_facts(snap):
    """Every count the pages may print, read from the snapshot's data files. A fact that cannot be read is None,
    and the builder prints it as `null` and fails. The keys are the tokens a page writes as {{n:key}}."""
    d = law_data(snap)
    law, rules, diags, fixtures = d["law"], d["rule_list"], d["diag_list"], d["manifest"].get("fixtures", [])
    meta = law.get("metadata", {})
    tiers = {}
    for r in rules:
        tiers[r.get("enforcement")] = tiers.get(r.get("enforcement"), 0) + 1
    cite_rule = sum(1 for x in diags if x.get("rules"))
    cite_article = sum(1 for x in diags if not x.get("rules") and x.get("articles"))
    spec = (snap / "doc" / "language" / "README.md").read_text(encoding="utf-8")
    m_spec = re.search(r"(?m)^# .*Specification v([\d.]+)", spec)
    grammar = (snap / "doc" / "language" / "GRAMMAR.md").read_text(encoding="utf-8")
    m_kinds = re.search(r"decl-kind\s*=(.*?);", grammar, re.S)
    families = law.get("intents", {}).get("families", {})
    zon = (snap / "build.zig.zon").read_text(encoding="utf-8")
    m_rel = re.search(r'\.version\s*=\s*"([^"]+)"', zon)
    facts = {
        "law.version": meta.get("version"),
        "law.rules": len(rules) or None,
        "law.sets": len([k for k in law if re.fullmatch(r"set\d+", k)]) or None,
        "law.articles": len(law.get("articles", {})) or None,
        "law.rights": len(law.get("rights", [])) or None,
        "law.forbidden": len(law.get("forbidden", [])) or None,
        "law.highest": max((int(r["number"]) for r in rules), default=None),
        "law.tier.machine": tiers.get("machine"),
        "law.tier.tool": tiers.get("tool"),
        "law.tier.machine-later": tiers.get("machine-later"),
        "law.tier.judgment": tiers.get("judgment"),
        "law.verbs": sum(len(f.get("verbs", [])) for f in law.get("intents", {}).get("families", {}).values()) or None,
        "law.families": len(law.get("intents", {}).get("families", {})) or None,
        "diag.total": len(diags) or None,
        "diag.errors": sum(1 for x in diags if x.get("severity") == "error"),
        "diag.warnings": sum(1 for x in diags if x.get("severity") == "warning"),
        "diag.cite_rule": cite_rule,
        "diag.cite_article": cite_article,
        "diag.cite_none": len(diags) - cite_rule - cite_article,
        "diag.level1": sum(1 for x in diags if x.get("level") == 1),
        "diag.level2": sum(1 for x in diags if x.get("level") == 2),
        "diag.level3": sum(1 for x in diags if x.get("level") == 3),
        "diag.level4": sum(1 for x in diags if x.get("level") == 4),
        "contract.version": d["contract"].get("metadata", {}).get("version"),
        "fix.total": len(fixtures) or None,
        "fix.level1": sum(1 for f in fixtures if f.get("level") == 1),
        "fix.level2": sum(1 for f in fixtures if f.get("level") == 2),
        "fix.level3": sum(1 for f in fixtures if f.get("level") == 3),
        "fix.clean": sum(1 for f in fixtures if not f.get("expect_ids")),
        "fix.twins": sum(1 for f in fixtures if f.get("file", "").endswith("-lawful.zayn")),
        "fix.unfixtured": len(d["manifest"].get("unfixtured", [])) or None,
        "law.family.action": len(families.get("action", {}).get("verbs", [])) or None,
        "lang.version": m_spec.group(1) if m_spec else None,
        "lang.kinds": len(re.findall(r'"[A-Z_]+"', m_kinds.group(1))) if m_kinds else None,
        "release.version": m_rel.group(1) if m_rel else None,
        "pin.tag": PIN_TAG,
    }
    facts.update(_record_facts(snap))
    return facts


def _record_facts(snap):
    """Counts read from three records of the snapshot: the list of the differences of the evaluator forged from the Haro
    declaration, the rows its judge last wrote, and the record the browser proof compares with. A file that is not
    there gives None, and the page that asks for it fails."""
    out = {"haro.rows": None, "haro.other_code": None, "haro.not_refused": None, "haro.court_only": None,
           "haro.judged": None, "proof.fixtures": None, "proof.answers": None, "wasm.bytes": None}

    def rows(path):
        lines = [l for l in path.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
        r = list(csv.reader(lines))
        return r[0], [x for x in r[1:] if len(x) == len(r[0])]

    twin = snap / "haro" / "twin-expected.csv"
    if twin.exists():
        head, body = rows(twin)
        k = head.index("class")
        out.update({"haro.rows": len(body), "haro.other_code": sum(1 for x in body if x[k] == "other-code"),
                    "haro.not_refused": sum(1 for x in body if x[k] == "not-refused"),
                    "haro.court_only": sum(1 for x in body if x[k] == "court-only")})
    judged = snap / "haro" / "judge-rows.csv"
    if judged.exists():
        out["haro.judged"] = len(rows(judged)[1])
    proof = snap / "tools" / "zayn" / "wasm-proof.json"
    if proof.exists():
        fx = json.loads(proof.read_text(encoding="utf-8")).get("fixtures", [])
        out["proof.fixtures"] = len(fx) or None
        out["proof.answers"] = sum(len(f.get("expect") or []) for f in fx) or None
    wasm = snap / "site" / "zayn.wasm"
    if wasm.exists():
        out["wasm.bytes"] = wasm.stat().st_size
    return out


def load_json(name, default):
    p = DATA / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save_json(name, obj):
    DATA.mkdir(exist_ok=True)
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
