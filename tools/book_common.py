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


def closed_lists(snap):
    """The fields whose value comes from a closed list, as the language specification tables them (DECLARATIONS.md,
    "Enumerations, complete"): [(field, on which kind, [values])]. Read from the snapshot, never typed."""
    text = (snap / "doc" / "language" / "DECLARATIONS.md").read_text(encoding="utf-8")
    m = re.search(r"(?ms)^## 5\. Enumerations, complete\s*$(.*?)^###? ", text)
    out = []
    for line in (m.group(1) if m else "").splitlines():
        row = re.match(r"^\|\s*`(\w+)`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if row:
            out.append((row.group(1), row.group(2).replace("`", ""), re.findall(r"`([a-z_]+)`", row.group(3))))
    return out


def fields_by_kind(snap):
    """Which fields each kind carries beyond the ones every kind carries, as the specification tables it (VIOLATIONS.md,
    the note on FIELD_MISPLACED): [(kinds, fields)]. Read from the snapshot, never typed."""
    text = (snap / "doc" / "language" / "VIOLATIONS.md").read_text(encoding="utf-8")
    out = []
    for line in text.splitlines():
        row = re.match(r"^\|\s*\*\*([A-Z_, ]+)\*\*\s*\|\s*(.+?)\s*\|\s*$", line)
        if row:
            out.append(([k.strip() for k in row.group(1).split(",")], re.findall(r"`([A-Z_]+)`", row.group(2))))
    return out


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
        "lang.lists": len(closed_lists(snap)) or None,
        "release.version": m_rel.group(1) if m_rel else None,
        "pin.tag": PIN_TAG,
    }
    facts.update(_record_facts(snap))
    facts.update(_history_facts(snap, law, rules, diags))
    return facts


def pin_files(snap):
    """The data files that record which version of the law they were checked against: [(path, version)]."""
    out = []
    for folder in ("conformance", "protocol"):
        for p in sorted((snap / folder).rglob("*.json")):
            try:
                doc = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(doc, dict):
                continue
            for holder in (doc.get("metadata"), doc.get("versions")):
                if isinstance(holder, dict) and holder.get("constitution"):
                    out.append((p.relative_to(snap).as_posix(), str(holder["constitution"])))
                    break
    return out


def ladder(snap):
    """The count by citation (chapter 17). The verifier's side: the rules that the contract binds to a kind of finding
    whose code the reference verifier raises (the code occurs in tools/zayn/zayn.js). The audits' side: the citations of
    data/audit-citations.json, each checked against the snapshot. Returns {rule: {"codes": [...], "audits": [(inst, check)]}}
    and the instruments' names. A citation shows that an instrument reads a rule, never that it decides the whole rule."""
    contract = json.loads((snap / "conformance" / "violations.json").read_text(encoding="utf-8"))
    diags = contract["diagnostics"] if isinstance(contract["diagnostics"], list) else list(contract["diagnostics"].values())
    verifier = (snap / "tools" / "zayn" / "zayn.js").read_text(encoding="utf-8")
    out = {}
    for d in diags:
        if d.get("rules") and re.search(r"['\"]" + re.escape(d["id"]) + r"['\"]", verifier):
            for n in d["rules"]:
                out.setdefault(str(n), {"codes": [], "audits": []})["codes"].append(d["id"])
    data = json.loads((DATA / "audit-citations.json").read_text(encoding="utf-8"))
    for c in data["citations"]:
        f = snap / c["file"]
        if not f.exists() or c["needle"] not in f.read_text(encoding="utf-8"):
            raise SystemExit(f"audit-citations.json: '{c['needle']}' is not in {c['file']} at the pin")
        out.setdefault(str(c["rule"]), {"codes": [], "audits": []})["audits"].append((c["instrument"], c["check"]))
    return out, data.get("instruments", {})


ACT_LETTERS = {"P": "perceive", "U": "understand", "D": "decide", "A": "act", "R": "recover", "T": "trust"}


def grid(snap):
    """The grid of chapter 13, counted from the data as Zayn's own script counts it: six activities of the user, each owning
    some of the 22 verbs (the constant VERBS of doc/design/coverage-count.js, the one place the map is written), by the ten
    media of conformance/media.json and one more column, "any". A cell is closed when its activity owns verbs and the medium
    marks every one of them absent. A rule sits on the cells of its activities, in its media (coverage-placement.json)."""
    src = (snap / "doc" / "design" / "coverage-count.js").read_text(encoding="utf-8")
    m = re.search(r"const VERBS = \{(.*?)\};", src, re.S)
    verbs = {k: re.findall(r"'([A-Z]+)'", v) for k, v in re.findall(r"(\w+):\s*\[(.*?)\]", m.group(1), re.S)}
    acts = list(verbs)
    media = json.loads((snap / "conformance" / "media.json").read_text(encoding="utf-8"))["media"]
    law = json.loads((snap / "constitution" / "rules.json").read_text(encoding="utf-8"))
    all22 = {v for f in law["intents"]["families"].values() for v in f["verbs"]}
    absent = {}
    for md in media:
        car = md.get("carries") or {}
        if car.get("default") == "absent":
            absent[md["id"]] = all22 - set(car.get("native") or []) - set(car.get("degraded") or [])
        else:
            absent[md["id"]] = set(car.get("absent") or [])
    cols = ["any"] + [md["id"] for md in media]
    place = json.loads((snap / "doc" / "design" / "coverage-placement.json").read_text(encoding="utf-8"))
    cells = {(a, col): {"closed": False, "rules": []} for a in acts for col in cols}
    for a in acts:
        for md in media:
            if verbs[a] and all(v in absent[md["id"]] for v in verbs[a]):
                cells[(a, md["id"])]["closed"] = True
    for n, r in place["rules"].items():
        for letter in r["activities"]:
            a = ACT_LETTERS[letter]
            for col in (["any"] if r["media"] == "any" else r["media"]):
                cells[(a, col)]["rules"].append(int(n))
    rules = place["rules"]
    live = [k for k, v in cells.items() if not v["closed"]]
    ruled = [k for k in live if cells[k]["rules"]]
    empty = [k for k in live if not cells[k]["rules"]]
    anyrows = {a for a in acts if cells[(a, "any")]["rules"]}
    facts = {
        "grid.activities": len(acts), "grid.media": len(media), "grid.cells": len(cells),
        "grid.closed": sum(1 for v in cells.values() if v["closed"]), "grid.live": len(live),
        "grid.ruled": len(ruled), "grid.empty": len(empty),
        "grid.reach": sum(1 for (a, _) in empty if a in anyrows),
        "grid.placed": len(rules), "grid.off": len(place.get("off") or {}),
        "grid.visual": sum(1 for r in rules.values() if r["media"] != "any" and "visual" in r["media"]),
        "grid.visualonly": sum(1 for r in rules.values() if r["media"] == ["visual"]),
        "grid.free": sum(1 for r in rules.values() if r["media"] == "any"),
        "grid.named": sum(1 for r in rules.values() if r["media"] != "any" and r["media"] != ["visual"]),
        "grid.norule": sum(1 for md in media if not any(cells[(a, md["id"])]["rules"] for a in acts)),
    }
    return {"acts": acts, "cols": cols, "cells": cells, "titles": {md["id"]: md.get("title", "") for md in media}}, facts


def _history_facts(snap, law, rules, diags):
    """The law's history and anatomy as its own file holds them, and what pins it. Counted, never typed."""
    meta = law.get("metadata", {})
    lineage = meta.get("lineage") or ""
    entries = re.findall(r"v\d+\.\d+(?:\.\d+)?\s*\(\d{4}-\d{2}-\d{2}\)", lineage)

    def carry(field):
        return sum(1 for r in rules if r.get(field) not in (None, "", [], {}))

    out = {
        "law.lineage": len(entries) or None,
        "law.retired": len(law.get("retired") or {}) or None,
        "law.burned": len(law.get("burned") or {}) or None,
        "law.unused": (len(law.get("retired") or {}) + len(law.get("burned") or {})) or None,
        "rule.evidence": carry("evidence") or None,
        "rule.derived": carry("derived_from") or None,
        "rule.invariant": carry("invariant") or None,
        "rule.lint": carry("lint") or None,
        "rule.vibes": carry("vibes") or None,
        "rule.see_also": carry("see_also") or None,
        "rule.absorbs": carry("absorbs") or None,
    }
    names = {}
    for r in rules:
        for k in r:
            if not k.startswith("_"):
                names[k] = names.get(k, 0) + 1
    out["rule.fields.all"] = sum(1 for k, n in names.items() if n == len(rules)) or None
    out["rule.fields.some"] = sum(1 for k, n in names.items() if n < len(rules)) or None
    out["law.principles"] = len((law.get("philosophy") or {}).get("rules") or []) or None
    out["law.axioms"] = sum(1 for a in (law.get("articles") or {}).values() if a.get("axiom")) or None
    out["diag.cite_right"] = sum(1 for d in diags if d.get("rights")) or None
    lad, _ = ladder(snap)
    out["cite.verifier"] = sum(1 for v in lad.values() if v["codes"]) or None
    out["cite.audit"] = sum(1 for v in lad.values() if v["audits"]) or None
    out["cite.ui"] = sum(1 for v in lad.values() if any(i == "ui" for i, _ in v["audits"])) or None
    out["cite.shot"] = sum(1 for v in lad.values() if any(i == "shot" for i, _ in v["audits"])) or None
    out["cite.union"] = len(lad) or None
    out["cite.both"] = sum(1 for v in lad.values() if v["codes"] and v["audits"]) or None
    out["cite.rest"] = (len(rules) - len(lad)) if rules and lad else None
    out.update(grid(snap)[1])
    out["law.tiers"] = len({r.get("enforcement") for r in rules if r.get("enforcement")}) or None
    listed = [int(n) for r in (law.get("rights") or []) for n in (r.get("enforced_by") or []) if str(n).isdigit()]
    out["right.max"] = max(listed) if listed else None
    # the corpus of corrections, as its data file holds it
    out.update({"corpus.records": None, "corpus.verbatim": None, "corpus.repeat": None, "corpus.causes": None, "corpus.groups": None})
    corpus = snap / "doc" / "design" / "corpus" / "corpus.json"
    if corpus.exists():
        c = json.loads(corpus.read_text(encoding="utf-8"))
        recs = c.get("records") or []
        out.update({"corpus.records": len(recs) or None,
                    "corpus.verbatim": sum(1 for x in recs if x.get("verbatim")) or None,
                    "corpus.repeat": sum(1 for x in recs if x.get("repeat")) or None,
                    "corpus.causes": len(c.get("causes") or []) or None,
                    "corpus.groups": len(c.get("groups") or []) or None})
    # the files that record which version of the law they were checked against (metadata.constitution)
    pins = []
    for folder in ("conformance", "protocol"):
        for p in sorted((snap / folder).rglob("*.json")):
            try:
                doc = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(doc, dict):
                continue
            for holder in (doc.get("metadata"), doc.get("versions")):
                if isinstance(holder, dict) and holder.get("constitution"):
                    pins.append(str(holder["constitution"]))
                    break
    out["pin.files"] = len(pins) or None
    out["pin.agree"] = sum(1 for v in pins if v == str(meta.get("version")))
    pack = snap / "protocol" / "MANIFEST.json"
    out["pack.files"] = None
    if pack.exists():
        out["pack.files"] = len(json.loads(pack.read_text(encoding="utf-8")).get("pinned") or []) or None
    # the rules that a diagnostic of the contract cites, and the rules of the two instrument tiers that none cites
    cited = {str(n) for d in diags for n in (d.get("rules") or [])}
    out["cite.rules"] = len(cited) or None
    # ... and those cited by a diagnostic that a verifier decides from a declaration (levels 1 to 3 of the contract)
    declared = {str(n) for d in diags if int(d.get("level") or 0) <= 3 for n in (d.get("rules") or [])}
    out["cite.declaration"] = len(declared) or None
    return out


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
