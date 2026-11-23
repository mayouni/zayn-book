#!/usr/bin/env python3
"""Build the Zayn book: run it, then write the reader.

    python tools/build_book.py                # run every declaration and every court fixture, then render
    python tools/build_book.py --render-only  # render from data/ as it stands (no run)

Writes:
  en/index.html   the reader, one self-contained file (the series' choice)
  index.html      opens the English reader

Lineage: adapted from the Softanza book's tools/build_book.py (softanza-book a9e3812), which ported the Refinement book's
web/build.py. Kept, word for word unless marked: the shell and its named edits (apply_shell), the colour sets, the font
faces, the type scale and its check, inline / plain / render_table, the cover on the overview, the navigation, the proof
line, the page stages and their banner, the standing invitation. FORMAT.md lists what is kept, what changed and why.

What this book adds, on the author's rulings for the Zayn site (2026-11-14), which a reference keeps:
  - a PLATE: a declaration, the sentence that says it in words, the verifier's report from the run and, where the chapter
    shows what a user meets, a sketch labelled as an illustration, as one numbered figure, never two blocks in a row;
  - the declaration's lines numbered, and the line a finding cites marked;
  - a RULE CARD and a RIGHT CARD, printed from the law's own data at the pin, so no word of the law is typed in a page;
  - every count a page states written as a token, {{n:law.rules}}, and filled from the run's reading of the data files.

The build FAILS (exit status 1) when: a chapter's declarations did not all keep their promise; a declaration changed since
its last run; a court fixture is missing or answers otherwise than the suite's manifest expects; a chapter lacks one of
the fixed headings, or holds a declaration outside a plate or without its "In words" line; a token cannot be read; a colour
sits outside the variables; the type scale is out of order. It still writes the page first, so the failure can be seen.
"""
import html, json, re, subprocess, sys
from book_common import (ladder, pin_files, ROOT, sources, structure, code_blocks, block_hash, load_json, now, stamp, snapshot, law_data,
                         closed_lists, fields_by_kind, GH_BLOB, PIN_TAG)
from book_judge import WORDS

ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

# The fixed headings of a chapter, in order (the book's CLAUDE.md, "The shape of a chapter"). Sections that show and run
# declarations sit between "The principle" and "What I refused", titled freely.
SHAPE = ["The field", "The principle", "What I refused", "The court", "Where the field leads", "Where it stands",
         "In your hands"]

# ============================================================================ UI words
UI = {
  "en": {
    "lang": "en", "part": "Part", "chapter": "Chapter", "preface": "Preface",
    "spine": "Spine", "spine_title": "One of the spine chapters: they carry the whole argument and can be read alone",
    "spine_group": "Which chapters to show", "opt_all": "Every chapter", "opt_spine": "The spine: {n} chapters",
    "draft": "Draft", "review": "In review", "published": "Published",
    "draft_title": "Written, its declarations run and judged, read by fresh readers; awaiting the author's review",
    "review_title": "The author is reviewing this page; his remarks are being applied",
    "published_title": "Approved by the author: this is the book's text",
    "missing": "Missing · the source is awaited",
    "proof": "Run on {d} by the reference verifier of the zayn command, release {tag} (commit {sha}), against the law at version {law}: the verifier gave the expected answer on {k} of {n} declarations.",
    "proof_none": "This page has no declaration to run.",
    "proof_data": "Printed at build on {d} from the files of Zayn at release {tag} (commit {sha}), and from the book's own registers.",
    "proof_how": "Each declaration on this page was checked as a file by the verifier's JavaScript reference, the one the zayn command is held to, under Node {node}. Every report printed below is the one that run gave. The lines that begin with //--> state the answer the page expects, and the build fails on any other.",
    "stale": "This page's declarations changed after their last run; their reports appear with the next run.",
    "contents": "Contents", "not_drafted": "in writing", "words": "words",
    "decision": "The decision, and what was refused",
    "court_head": "Run in the Zayn snapshot at commit {sha} on {d}. Each fixture is a declaration of the conformance suite; the suite's manifest states the findings it must get, and the run compares the two sets.",
    "court_ok": "answers as the manifest expects", "court_bad": "answers otherwise", "court_missing": "this fixture is not in the suite at the pin",
    "court_clean": "no finding",
    "court_codes": "The codes above, in the words of the verifier's contract",
    "court_level": "level", "court_error": "error", "court_warning": "warning",
    "stage": {"built": "built", "designed": "designed", "next": "next"},
    "plate": "Plate", "illustration": "Illustration", "symbols": "Symbol table", "run_label": "Run",
    "families_h": ["Family", "Its verbs", "What its verbs keep true"],
    "levels_h": ["Level", "Its name", "What the verifier is given", "What it decides", "Kinds of finding"],
    "lists_h": ["Field", "On", "The values it admits, and no others"],
    "fields_h": ["Kind", "The fields it carries, beyond those every kind carries"], "fields_none": "none of its own",
    "spec_src": "Printed from the language specification, version {v}.",
    "contract_src": "Printed from the verifier's contract, version {v}.",
    "suite_ran": "run at this build by the suite's own runner, in the snapshot of Zayn",
    "rule": "Rule", "article": "Article", "set": "Set", "tier": "Tier", "why": "Why", "right_label": "A right of the user",
    "cited_by": "Cited by", "cited_none": "no diagnostic of the verifier's contract",
    "law_src": "Printed from the law's data, version {v}.",
    "diag_h": ["Code", "Level", "Severity", "The contract's sentence", "What it cites"],
    "diag_none": "nothing", "avoid": "Avoid", "rights_h": ["Right", "Its sentence", "Rules that enforce it"],
    "forbidden_h": ["Forbidden pattern", "Rules it breaks"],
    "retired_h": ["Number", "Its title", "Where it went"], "retired_into": "merged into Rule {n}", "burned": "reserved, never assigned",
    "sources_h": ["Id", "The source", "What the page is", "Read on", "Used in"],
    "articles_h": ["Article", "Its title", "Its sentence", "Rules derived from it"],
    "sets_h": ["Set", "Its title", "Rules", "Their numbers"],
    "tiers_h": ["Tier, in the law's word", "Rules filed under it", "Cited by a kind of finding the verifier raises", "Named by an audit for a check"],
    "ladder_h": ["Rule", "Tier", "The verifier: kinds of finding that cite it", "The audits: checks that name it"],
    "ladder_src": "Counted by citation at this build, from the contract, the verifier's code and the files of the two audits; each audit citation is checked against its file. A citation shows that an instrument reads the rule. Which clauses it reads is said rule by rule in the chapter.",
    "inst_ui": "painted page", "inst_shot": "screenshot",
    "anatomy_h": ["Field, as the file names it", "What this rule holds"],
    "pins_h": ["A data file of Zayn", "The version of the law it records"],
    "pins_src": "Read from each file at the version of Zayn this book reads.",
    "sources_src": "Printed from the book's register of sources, research/FIELD.md.",
    "prev": "← Previous", "next": "Next →",
    "series": "Third of the AYOUNI books",
    "cover_alt": "Zayn, book cover",
    "description": "Zayn, UI Governance in the Agentic Era: declare what a user is doing, the law refuses the rest. By Mansour Ayouni. Third of the AYOUNI books.",
    "theme": "Light or dark",
    "zoom_label": "View the cover large", "close_label": "Close",
    "home_label": "AYOUNI Press: home", "home_url": "https://mayouni.github.io/ayouni/",
    # the open book (house OPEN-BOOK.md, lines 27 and 28): the invitation and the colophon line, word for word
    "invite": "If this book is useful to your organisation, I work with organisations on its subjects: paper copies in quantity, workshops and training, talks, consulting and the building of solutions. Write to ",
    "invite_mail": "kalidianow@gmail.com", "offer_link": "How these books are offered",
    "colophon": "Copyright © 2026 Mansour Ayouni. Free to read and share under CC BY-NC-ND 4.0; code under the MIT licence.",
    "offer_url": "https://mayouni.github.io/ayouni/offer/", "licence_url": "https://mayouni.github.io/ayouni/licence/",
    "pdf_public": "../book.pdf", "pdf_local": "../print/zayn-en.pdf",
    "appendix": "Appendix", "appendices": "Appendices",
  },
}

# ============================================================================ colours: every one a variable
# The Softanza book's two sets, kept; four variables added for the plate (the cited line, the field and verb tones).
LIGHT = {
  "--ink": "#17140f", "--ink-soft": "#2a241b", "--soft": "#6b6358", "--soft-2": "#9a9078",
  "--paper": "#ffffff", "--bg": "#fbfaf6", "--rule": "#e3ddc9", "--rule-strong": "#1a1612",
  "--hover-bg": "#f3eedf", "--hover-bg-soft": "#fcfaf5", "--card-bg": "#ffffff", "--sidebar-bg": "#f5f0e2",
  "--bookmark": "#E96A1A", "--bookmark-text": "#b3480a",
  "--shadow-cover": "rgba(40, 30, 18, 0.16)", "--shadow-soft": "rgba(40, 30, 18, 0.08)",
  "--shadow-side": "rgba(0, 0, 0, 0.12)", "--scrim": "rgba(26, 22, 18, 0.45)", "--scrim-search": "rgba(26, 22, 18, 0.42)",
  "--shadow-panel": "rgba(26, 22, 18, 0.28)", "--shadow-pill": "rgba(26, 22, 18, 0.18)",
  "--mark": "rgba(233, 106, 26, 0.20)", "--mark-strong": "rgba(233, 106, 26, 0.25)",
  "--flash": "rgba(233, 106, 26, 0.22)", "--flash-0": "rgba(233, 106, 26, 0)", "--print-bg": "#ffffff",
  "--code-bg": "#211c15", "--code-rule": "#35302a", "--code-ink": "#e8e1d1", "--code-kw": "#f0914f",
  "--code-str": "#a9c795", "--code-num": "#82c0ae", "--code-com": "#8d8471", "--code-promise": "#d8c3a5",
  "--code-label": "#a39a88", "--code-field": "#82c0ae", "--code-verb": "#e8e1d1",
  "--code-cited": "rgba(233, 106, 90, 0.20)", "--code-cited-rule": "#e99484",
  "--ok": "#2f6b3f", "--ok-bg": "#e8f0e6", "--bad": "#a3392b", "--bad-bg": "#f6e5e0",
  "--neutral": "#5d564b", "--neutral-bg": "#eee9dc", "--designed": "#2f5d7c", "--designed-bg": "#e3ecf2",
  "--decision-bg": "#f3eee2", "--cover-bg": "#1a1612", "--cover-ink": "#fbfaf6", "--cover-soft": "#bdb4a2",
  "--cover-accent": "#E96A1A",
}
DARK = {
  "--ink": "#ece6da", "--ink-soft": "#cfc6b4", "--soft": "#a39a88", "--soft-2": "#7d7565",
  "--paper": "#1d1a16", "--bg": "#14120f", "--rule": "#3a342b", "--rule-strong": "#ece6da",
  "--hover-bg": "#2a251e", "--hover-bg-soft": "#221e19", "--card-bg": "#1d1a16", "--sidebar-bg": "#191612",
  "--bookmark": "#ef7a2e", "--bookmark-text": "#f4a066",
  "--shadow-cover": "rgba(0, 0, 0, 0.55)", "--shadow-soft": "rgba(0, 0, 0, 0.35)",
  "--shadow-side": "rgba(0, 0, 0, 0.5)", "--scrim": "rgba(0, 0, 0, 0.6)", "--scrim-search": "rgba(0, 0, 0, 0.58)",
  "--shadow-panel": "rgba(0, 0, 0, 0.6)", "--shadow-pill": "rgba(0, 0, 0, 0.5)",
  "--mark": "rgba(239, 122, 46, 0.28)", "--mark-strong": "rgba(239, 122, 46, 0.34)",
  "--flash": "rgba(239, 122, 46, 0.26)", "--flash-0": "rgba(239, 122, 46, 0)", "--print-bg": "#ffffff",
  "--code-bg": "#0f0d0b", "--code-rule": "#2e2923", "--code-ink": "#e8e1d1", "--code-kw": "#f0914f",
  "--code-str": "#a9c795", "--code-num": "#82c0ae", "--code-com": "#8d8471", "--code-promise": "#d8c3a5",
  "--code-label": "#8d8471", "--code-field": "#82c0ae", "--code-verb": "#e8e1d1",
  "--code-cited": "rgba(233, 148, 132, 0.18)", "--code-cited-rule": "#e99484",
  "--ok": "#8cc79a", "--ok-bg": "#1f2d22", "--bad": "#e99484", "--bad-bg": "#3a211c",
  "--neutral": "#b9b0a0", "--neutral-bg": "#2a261f", "--designed": "#8fb7d3", "--designed-bg": "#1d2a33",
  "--decision-bg": "#1f1b16", "--cover-bg": "#0f0d0b", "--cover-ink": "#f3eee3", "--cover-soft": "#a39a88",
  "--cover-accent": "#ef7a2e",
}


def css_vars(d):
    return " ".join(f"{k}: {v};" for k, v in d.items())


# ============================================================================ the shell, transformed
# Each edit: (name, old, new). Applied in order; each must match exactly once in the Refine shell.
FONT_FACES = """@font-face { font-family: 'EB Garamond'; font-style: normal; font-weight: 400 800; font-display: swap;
  src: local('EB Garamond'), local('EBGaramond-Regular'), url('../assets/fonts/EBGaramond-normal.woff2') format('woff2'); }
@font-face { font-family: 'EB Garamond'; font-style: italic; font-weight: 400 800; font-display: swap;
  src: local('EB Garamond Italic'), local('EBGaramond-Italic'), url('../assets/fonts/EBGaramond-italic.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 400 800; font-display: swap;
  src: local('Inter'), local('Inter-Regular'), url('../assets/fonts/Inter-normal.woff2') format('woff2'); }
@font-face { font-family: 'Archivo Black'; font-style: normal; font-weight: 400; font-display: swap;
  src: local('Archivo Black'), local('ArchivoBlack-Regular'), url('../assets/fonts/ArchivoBlack-normal.woff2') format('woff2'); }
"""


def shell_edits(ui):
    return [
        ("html lang", '<html lang="en">', f'<html lang="{ui["lang"]}">'),
        ("title", "<title>Refinement-Oriented Programming — AYOUNI</title>", "<title>Zayn — AYOUNI</title>"),
        ("description",
         '<meta name="description" content="A discipline for software in the agentic era. By Mansour Ayouni. First book from the AYOUNI imprint.">',
         f'<meta name="description" content="{html.escape(ui["description"])}">\n'
         '<script>try{var t=localStorage.getItem("zayn-theme");if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}</script>'),
        ("no CDN: the fonts are local files, with the same families and the same fallbacks",
         '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n',
         ""),
        ("font faces", "<style>\n:root {", "<style>\n" + FONT_FACES + ":root {"),
        ("the overview shows one view at a time: the cards, or the contents as text",
         "    chapterGrid.classList.remove('list-mode');\n",
         "    chapterGrid.classList.remove('list-mode');\n    document.body.classList.remove('vm-list');\n    vmGrid.setAttribute('aria-pressed', 'true'); vmList.setAttribute('aria-pressed', 'false');\n"),
        ("the list view is the contents",
         "    chapterGrid.classList.add('list-mode');\n",
         "    chapterGrid.classList.add('list-mode');\n    document.body.classList.add('vm-list');\n    vmList.setAttribute('aria-pressed', 'true'); vmGrid.setAttribute('aria-pressed', 'false');\n"),
        ("the default reading size is 24px: a Garamond reads small", "  --font-size: 22px;", "  --font-size: " + str(TYPE["body_px"]) + "px;"),
        ("the reading size control starts on 24px", "  let currentSizeIdx = 2;", "  let currentSizeIdx = 3;"),
        ("the AYOUNI logo, once, as a symbol", "<body>", "<body>\n" + (ROOT / "reader" / "logo-sprite.html").read_text(encoding="utf-8")),
        ("the logo is the way home, at the top of every page", '<div class="hdr-section hdr-left">',
         '<div class="hdr-section hdr-left">\n    <a class="ayouni-home" href="' + ui["home_url"] + '" aria-label="' + html.escape(ui["home_label"]) + '"><svg viewBox="0 0 2095 518" aria-hidden="true" focusable="false"><use href="#ayouni-logo"/></svg></a>'),
        ("the print icon opens the book's PDF, never a page the browser generates (OPEN-BOOK, HOUSE-11)",
         "  btnPrint.addEventListener('click', () => window.print());",
         f"  btnPrint.addEventListener('click', () => {{ const served = /\\/books\\/[^/]+\\/(en|fr)\\/(index\\.html)?$/.test(location.pathname); "
         f"window.open(served ? '{ui['pdf_public']}' : '{ui['pdf_local']}', '_blank', 'noopener'); }});"),
        ("the menu keeps the current page at its top", "    // Scroll to top of content\n    window.scrollTo({ top: 0, behavior: 'instant' });", "    // Scroll to top of content\n    window.scrollTo({ top: 0, behavior: 'instant' });\n\n    // the current page is underlined in the menu and brought to its top (the menu is visible now)\n    const sbEl = document.querySelector('.chapter-sidebar');\n    const cur = sbEl && sbEl.querySelector('.sidebar-link.active');\n    if (cur) { sbEl.scrollTo({ top: Math.max(0, cur.getBoundingClientRect().top - sbEl.getBoundingClientRect().top + sbEl.scrollTop - 24), behavior: 'instant' }); }"),
        ("colours: hero shadow", "box-shadow: 0 16px 48px rgba(40, 30, 18, 0.16), 0 4px 12px rgba(40, 30, 18, 0.08);",
         "box-shadow: 0 16px 48px var(--shadow-cover), 0 4px 12px var(--shadow-soft);"),
        ("colours: card shadow", "box-shadow: 0 8px 20px rgba(40, 30, 18, 0.08);", "box-shadow: 0 8px 20px var(--shadow-soft);"),
        ("colours: sidebar shadow", "box-shadow: 4px 0 20px rgba(0,0,0,0.12);", "box-shadow: 4px 0 20px var(--shadow-side);"),
        ("colours: backdrop", "background: rgba(26, 22, 18, 0.45);", "background: var(--scrim);"),
        ("colours: search scrim", "background: rgba(26, 22, 18, 0.42);", "background: var(--scrim-search);"),
        ("colours: search panel", "box-shadow: 0 18px 50px rgba(26, 22, 18, 0.28);", "box-shadow: 0 18px 50px var(--shadow-panel);"),
        ("colours: search hover", ".search-hit:hover { background: #fcfaf5; }", ".search-hit:hover { background: var(--hover-bg-soft); }"),
        ("colours: search mark", "background: rgba(233, 106, 26, 0.20);", "background: var(--mark);"),
        ("colours: term mark", "background: rgba(233, 106, 26, 0.25);", "background: var(--mark-strong);"),
        ("colours: pill shadow", "box-shadow: 0 6px 24px rgba(26, 22, 18, 0.18);", "box-shadow: 0 6px 24px var(--shadow-pill);"),
        ("colours: flash",
         "0%   { background: rgba(233, 106, 26, 0.22); box-shadow: 0 0 0 6px rgba(233, 106, 26, 0.22); }\n  100% { background: transparent; box-shadow: 0 0 0 6px rgba(233, 106, 26, 0); }",
         "0%   { background: var(--flash); box-shadow: 0 0 0 6px var(--flash); }\n  100% { background: transparent; box-shadow: 0 0 0 6px var(--flash-0); }"),
        ("colours: print", "body { background: white; font-size: 11pt; }", "body { background: var(--print-bg); font-size: 11pt; }"),
        ("breadcrumb: the book's name", '<a href="#" class="bc-book" id="bcBook">Refinement-Oriented Programming</a>',
         '<a href="#" class="bc-book" id="bcBook">Zayn</a>'),
        ("header: theme",
         '  <div class="hdr-section hdr-right">\n',
         '  <div class="hdr-section hdr-right">\n'
         f'    <button class="circle-btn" id="btnTheme" aria-label="{ui["theme"]}" title="{ui["theme"]}">'
         '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>\n'),
        ("script: theme, spine",
         "  // Initial route\n  handleHash();",
         "  // THEME (book): light and dark as first-class themes; the reader's choice is kept\n"
         "  const btnTheme = document.getElementById('btnTheme');\n"
         "  function currentTheme() {\n"
         "    const t = root.getAttribute('data-theme');\n"
         "    if (t) return t;\n"
         "    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';\n"
         "  }\n"
         "  btnTheme.addEventListener('click', () => {\n"
         "    const next = currentTheme() === 'dark' ? 'light' : 'dark';\n"
         "    root.setAttribute('data-theme', next);\n"
         "    try { localStorage.setItem('zayn-theme', next); } catch (e) {}\n"
         "  });\n"
         "  // SPINE (book): the chapters that carry the argument alone\n"
         "  const spineOpts = Array.from(document.querySelectorAll('.spine-opt'));\n"
         "  function applySpine(on) {\n"
         "    document.body.classList.toggle('spine-only', on);\n"
         "    spineOpts.forEach(b => b.setAttribute('aria-pressed', (b.dataset.spine === '1') === on ? 'true' : 'false'));\n"
         "    try { localStorage.setItem('zayn-spine', on ? '1' : '0'); } catch (e) {}\n"
         "  }\n"
         "  spineOpts.forEach(b => b.addEventListener('click', () => applySpine(b.dataset.spine === '1')));\n"
         "  try { if (localStorage.getItem('zayn-spine') === '1') applySpine(true); } catch (e) {}\n\n"
         "  // Initial route\n  handleHash();"),
    ]


def apply_shell(ui):
    shell = (ROOT / "reader" / "shell.refine.html").read_text(encoding="utf-8").replace("\r", "")
    for name, old, new in shell_edits(ui):
        n = shell.count(old)
        if n != 1:
            raise SystemExit(f"shell edit '{name}' matched {n} times; the Refine shell changed, re-read it")
        shell = shell.replace(old, new)
    # the theme variables: the Refine :root block is replaced by the book's light set, then dark is added
    root_block = re.search(r":root \{\n(.*?)\n\}", shell, re.S)
    fonts_and_sizes = "\n".join(l for l in root_block.group(1).split("\n") if not re.search(r"#[0-9a-fA-F]{3,6}", l))
    themed = (":root {\n" + fonts_and_sizes + "\n  " + css_vars(LIGHT) + "\n}\n"
              ":root[data-theme=\"dark\"] { " + css_vars(DARK) + " color-scheme: dark; }\n"
              "@media (prefers-color-scheme: dark) { :root:not([data-theme=\"light\"]) { " + css_vars(DARK) + " color-scheme: dark; } }\n"
              "@media print { :root, :root[data-theme=\"dark\"], :root:not([data-theme=\"light\"]) { " + css_vars(LIGHT) + " } }")
    shell = shell[:root_block.start()] + themed + shell[root_block.end():]
    shell = shell.replace("</style>", BOOK_CSS + type_css() + "\n</style>", 1)
    OV = "<!-- ============ OVERVIEW VIEW ============ -->"
    # the reader's own script is the first <script> after the overview marker (the theme script in the head comes before it)
    return shell[:shell.index(OV)], shell[shell.index("<script>", shell.index(OV)):]


def check_colours(page):
    """Every colour behind a variable: no literal colour outside the variable sets (the mask's #000 is an alpha mask)."""
    css = "\n".join(re.findall(r"<style>(.*?)</style>", page, re.S))
    css = re.sub(r":root[^{]*\{[^}]*\}", "", css)
    css = re.sub(r"@media \((?:prefers-color-scheme|print)[^{]*\{\s*:root[^{]*\{[^}]*\}\s*\}", "", css)
    css = css.replace("#000 70%", "")
    return sorted(set(re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\bwhite\b(?!-space)", css)))


# ============================================================================ the book's own CSS
BOOK_CSS = """
/* ---- from the Refine build's additions (web/build.py EXTRA_CSS), through the Softanza book, colours as variables ---- */
.ch-lede{font-style:italic;color:var(--soft);font-size:1.04em;line-height:1.55;margin:0 0 1.7em;padding-bottom:1.1em;border-bottom:1px solid var(--rule);}
h4.subsubsection-h{font-family:var(--sans);font-weight:700;font-size:0.76em;letter-spacing:0.05em;text-transform:uppercase;color:var(--ink-soft);margin:2em 0 0.5em;line-height:1.4;}
.chapter-page ul,.chapter-page ol{margin:1.1em 0 1.1em 1.3em;padding:0;}
.chapter-page li{margin:0.4em 0;line-height:1.6;}
blockquote{margin:1.5em 0;padding:0.3em 0 0.3em 1.3em;border-left:3px solid var(--rule-strong);color:var(--ink-soft);font-style:italic;}
.book-table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:0.74em;line-height:1.45;margin:1.7em 0;}
.book-table th,.book-table td{border:1px solid var(--rule);padding:7px 10px;text-align:left;vertical-align:top;}
.book-table th{background:var(--sidebar-bg);font-weight:700;color:var(--ink);}
pre{background:var(--code-bg);border:1px solid var(--code-rule);border-radius:10px;padding:1.1em 1.3em;overflow-x:visible;margin:1.5em 0;font-size:0.7em;line-height:1.65;}
.chapter-page pre code{font-family:ui-monospace,'Cascadia Code','SF Mono',Consolas,Menlo,monospace;font-size:1em;white-space:pre-wrap;overflow-wrap:anywhere;word-break:normal;color:var(--code-ink);background:none;padding:0;border-radius:0;font-variant-ligatures:none;font-feature-settings:"liga" 0,"calt" 0;}
pre .c-kw{color:var(--code-kw);font-weight:600;}
pre .c-string{color:var(--code-str);}
pre .c-number{color:var(--code-num);}
pre .c-comment{color:var(--code-com);font-style:italic;}
pre .c-promise{color:var(--code-promise);}
pre .c-field{color:var(--code-field);}
pre .c-verb{color:var(--code-verb);font-weight:600;}
.chapter-page code{font-family:var(--sans);font-size:0.82em;background:var(--sidebar-bg);padding:0.05em 0.35em;border-radius:4px;font-variant-ligatures:none;font-feature-settings:"liga" 0,"calt" 0;}

/* ---- the Softanza book's additions, kept ---- */
.chapter-page p.proof,.chapter-page p.proof-engine,.chapter-page .code-cell p,.chapter-page .court p,.chapter-page .plate p,.chapter-page .law-card p{text-indent:0;text-align:left;hyphens:none;-webkit-hyphens:none;font-feature-settings:normal;}
.status-banner{display:inline-block;font-family:var(--sans);font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:5px 10px;border-radius:4px;margin:0 0 14px;border:1px solid var(--rule);color:var(--soft);background:var(--sidebar-bg);}
.status-banner.st-draft{border-color:var(--bookmark);color:var(--bookmark-text);background:transparent;}
.status-banner.st-review{border-color:var(--designed);color:var(--designed);background:var(--designed-bg);}
.status-banner.st-published{border-color:var(--ok);color:var(--ok);background:var(--ok-bg);}
.status-banner.st-missing{border-color:var(--bad);color:var(--bad);background:transparent;}
.spine-badge{display:inline-block;font-family:var(--sans);font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--paper);background:var(--ink);border-radius:3px;padding:2px 7px;margin-left:10px;vertical-align:2px;}

.proof{font-family:var(--sans);line-height:1.55;color:var(--soft);margin:0 0 6px;}
.proof strong{color:var(--ink);font-weight:600;}
.proof.fails strong{color:var(--bad);}
.proof-engine{font-family:var(--sans);line-height:1.5;color:var(--soft);margin:0 0 8px;font-variant-ligatures:none;font-feature-settings:"liga" 0,"calt" 0;}

.code-cell{margin:1.6em 0;}
.code-cell pre{margin:0;border-radius:10px 10px 0 0;}
.code-cell .cell-label{font-family:var(--sans);font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--code-label);background:var(--code-bg);border:1px solid var(--code-rule);border-bottom:none;border-radius:10px 10px 0 0;padding:8px 1.3em 0;}
.code-cell .cell-label .cl-file{letter-spacing:0;text-transform:none;font-weight:500;margin-left:10px;}
.code-cell .cell-label + pre{border-top:none;border-radius:0;padding-top:0.5em;}
.code-cell .ran{font-family:var(--sans);line-height:1.5;margin:0;padding:8px 14px;border:1px solid var(--rule);border-top:none;background:var(--neutral-bg);color:var(--neutral);}
.code-cell .ran::before{font-weight:700;margin-right:7px;}
.code-cell .ran.nv-kept{background:var(--ok-bg);color:var(--ok);}
.code-cell .ran.nv-kept::before{content:"\\2713";}
.code-cell .ran.nv-differs,.code-cell .ran.nv-not-run,.code-cell .ran.nv-unpromised{background:var(--bad-bg);color:var(--bad);}
.code-cell .ran.nv-differs::before,.code-cell .ran.nv-not-run::before,.code-cell .ran.nv-unpromised::before{content:"\\2717";}
.code-cell .ran.nv-exercise{border-radius:0 0 10px 10px;}
.code-cell .ran.nv-exercise::before{content:"\\270E";}
.code-cell .ran .exit{float:right;font-weight:600;}
.code-cell .ran-out{border-radius:0;margin:0;border-top:none;}
.code-cell.aux-cell{margin-top:10px;}
.code-cell.aux-cell pre{border-radius:0 0 10px 10px;}
.code-cell.run-cell .ran{border-radius:0 0 10px 10px;}
.plate .code-cell + .code-cell{margin-top:10px;}
.code-cell .ran-out:last-child{border-radius:0 0 10px 10px;}
.code-cell .ran-sub{font-family:var(--sans);margin:0;padding:7px 14px;border:1px solid var(--rule);border-top:none;background:var(--sidebar-bg);color:var(--ink-soft);}

.stage-list{list-style:none;margin:0 0 1.2em !important;padding:0;}
.stage-list li{display:flex;gap:12px;align-items:baseline;margin:0.45em 0;}
.stage{display:inline-block;flex:0 0 auto;font-family:var(--sans);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:3px 8px;border-radius:3px;border:1px solid currentColor;min-width:86px;text-align:center;}
.stage.s-built{color:var(--ok);background:var(--ok-bg);}
.stage.s-designed{color:var(--designed);background:var(--designed-bg);}
.stage.s-next{color:var(--neutral);background:var(--neutral-bg);}

.decision{background:var(--decision-bg);border-left:4px solid var(--ink);border-radius:0 6px 6px 0;padding:6px 26px 22px;margin:44px -26px 36px -30px;}
.decision > .subsection-h{margin-top:26px;}
.decision-tag{font-family:var(--sans);font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--bookmark-text);margin-top:18px;}

.court{border:1px solid var(--rule);border-radius:6px;padding:14px 18px;margin:1.4em 0;background:var(--card-bg);font-family:var(--sans);}
.chapter-page .court p.court-head{line-height:1.5;color:var(--soft);margin:0 0 10px;font-family:var(--sans);}
.court ul{list-style:none;margin:0 !important;padding:0;}
.court li{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;padding:7px 0;border-top:1px dotted var(--rule);margin:0 !important;line-height:1.45;}
.court li:first-child{border-top:none;}
.court .g-name code{font-family:ui-monospace,'Cascadia Code',Consolas,monospace;background:none;padding:0;color:var(--ink);}
.court .g-name a{border-bottom:1px solid var(--rule);}
.court .g-name a:hover{border-bottom-color:var(--ink);}
.court .g-count{font-weight:700;color:var(--ink);}
.court .g-path{color:var(--soft);}
.court .g-what{flex-basis:100%;color:var(--ink);}
.chapter-page .court p.court-codes{margin:16px 0 6px;padding-top:10px;border-top:1px solid var(--rule);}
.court .g-ok{color:var(--ok);font-weight:600;}
.court .g-missing{color:var(--bad);font-weight:600;}

.author-q{font-family:var(--sans);font-size:0.72em;font-weight:600;color:var(--bookmark-text);border:1px dashed var(--bookmark);border-radius:4px;padding:1px 6px;}

/* ---- this book's additions: the plate, the sentence in words, the sketch, the cards of the law ---- */
.plate{border:1px solid var(--rule);border-radius:12px;margin:2.2em -14px;padding:16px 14px 14px;background:var(--card-bg);}
.plate-h{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;font-family:var(--sans);margin:0 4px 12px;}
.plate-n{font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--bookmark-text);}
.plate-h{font-style:normal;}
.plate-t{font-weight:600;color:var(--ink);line-height:1.3;}
.plate .code-cell{margin:0;}
.plate .code-cell + .sketch{margin-top:14px;}
pre.numbered code{counter-reset:ln;display:block;}
pre.numbered .cl{display:block;counter-increment:ln;padding-left:3.1em;text-indent:-3.1em;border-left:3px solid transparent;margin:0 -1.3em;padding-right:1.3em;}
pre.numbered .cl::before{content:counter(ln);display:inline-block;width:2.2em;margin-right:0.9em;text-align:right;color:var(--code-com);text-indent:0;}
pre.numbered .cl.cited{background:var(--code-cited);border-left-color:var(--code-cited-rule);}
.chapter-page .code-cell p.in-words{font-family:var(--serif);line-height:1.5;margin:0;padding:11px 16px 12px;border:1px solid var(--rule);border-top:none;background:var(--paper);color:var(--ink);}
.in-words .iw-label{display:block;font-family:var(--sans);font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--soft);margin-bottom:2px;}
.sketch{border:1px solid var(--rule-strong);border-radius:10px;padding:12px 16px 14px;background:var(--paper);font-family:var(--sans);}
.sketch .sk-label{font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--soft);margin-bottom:8px;}
.sketch .sk-title{font-weight:700;color:var(--ink);margin-bottom:4px;}
.chapter-page .sketch p.sk-say{font-family:var(--sans);line-height:1.45;margin:2px 0;color:var(--ink);}
.sketch .sk-controls{display:flex;flex-wrap:wrap;gap:10px 12px;align-items:center;margin-top:12px;}
.sketch .sk-ctl{display:inline-flex;align-items:baseline;gap:8px;border:1.5px solid var(--ink);border-radius:7px;padding:5px 13px;font-weight:600;color:var(--ink);line-height:1.3;}
.sketch .sk-ctl.sk-missing{border-style:dashed;border-color:var(--bad);color:var(--bad);}
.sketch .sk-ctl.sk-restored{border-color:var(--ok);color:var(--ok);}
.sketch .sk-rule{font-weight:500;}
.chapter-page .sketch p.sk-caption{font-family:var(--sans);line-height:1.45;margin:12px 0 0;color:var(--ink-soft);}
.book-table.families td:first-child{white-space:nowrap;}
.book-table.diag td:first-child{white-space:normal;word-break:normal;overflow-wrap:normal;}
.book-table td code{overflow-wrap:anywhere;}
@media (max-width:640px){.book-table{table-layout:fixed;}.book-table th,.book-table td{overflow-wrap:anywhere;padding:6px 7px;}.book-table.families td:first-child{white-space:normal;}}
.book-table.sources td{word-break:break-word;}
.book-table.families code{background:none;padding:0;font-family:ui-monospace,'Cascadia Code',Consolas,monospace;font-size:0.92em;}
.chapter-page p.table-src{font-family:var(--sans);color:var(--soft);margin:-1.1em 0 1.6em;text-indent:0;text-align:left;}
.law-card{border:1px solid var(--rule);border-left:4px solid var(--ink);border-radius:0 8px 8px 0;margin:1.6em 0;padding:12px 18px 12px;background:var(--card-bg);font-family:var(--sans);}
.law-card .lc-head{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline;margin-bottom:6px;}
.law-card .lc-num{font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--bookmark-text);}
.law-card .lc-title{font-weight:700;color:var(--ink);}
.law-card dl{margin:0;display:grid;grid-template-columns:max-content 1fr;gap:3px 14px;line-height:1.45;}
.law-card dt{font-weight:600;color:var(--soft);}
.law-card dd{margin:0;color:var(--ink);}
.law-card dd code{background:none;padding:0;font-family:ui-monospace,'Cascadia Code',Consolas,monospace;font-size:0.92em;}
.chapter-page .law-card p.lc-quote{font-family:var(--serif);font-style:italic;line-height:1.5;margin:2px 0 4px;color:var(--ink);}
.chapter-page .law-card p.lc-src{margin:8px 0 0;color:var(--soft);line-height:1.4;}

/* navigation: parts, the spine, the chapters in writing */
.sb-part{font-family:var(--sans);font-weight:700;text-transform:uppercase;color:var(--ink);}
.sidebar-link .sl-spine{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ink);margin-right:8px;vertical-align:2px;}
.sidebar-link:not(.is-spine) .sl-spine{background:transparent;border:1px solid var(--soft-2);}
.sidebar-link.active .sl-text{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:5px;}
.sidebar-link.is-absent{color:var(--soft-2);cursor:default;}
.hero-cover{flex-direction:column;align-items:center;}
.cover-wrap{position:relative;display:block;width:100%;line-height:0;}
@media (max-width: 900px){.cover-wrap{max-width:280px;margin:0 auto;}}
.cover-zoom{position:absolute;right:14px;bottom:14px;width:46px;height:46px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--paper);color:var(--ink);display:flex;align-items:center;justify-content:center;cursor:zoom-in;padding:0;box-shadow:0 2px 10px var(--shadow-soft);}
.cover-zoom svg{width:22px;height:22px;}
.cover-zoom:hover{background:var(--ink);color:var(--paper);}
.cover-lightbox{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1000;background:var(--scrim);display:flex;flex-direction:column;gap:16px;align-items:center;justify-content:center;padding:24px;cursor:zoom-out;}
.cover-lightbox[hidden]{display:none;}
.cover-lightbox img{max-width:calc(100vw - 48px);max-height:calc(100vh - 112px);width:auto;height:auto;background:var(--paper);box-shadow:0 8px 40px var(--shadow-cover);}
.cover-close{position:absolute;top:14px;right:18px;width:46px;height:46px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--paper);color:var(--ink);font-size:28px;line-height:1;cursor:pointer;padding:0;}
.the-invite{margin:3.2em 0 1em;padding:1.6em 0 0;border-top:1px solid var(--rule);}
.the-invite p{text-indent:0;text-align:left;hyphens:none;}
.the-invite .invite-line{font-style:italic;}
.the-invite a{border-bottom:1px solid var(--rule-strong);}
.the-invite .invite-more,.the-invite .colophon-line{font-family:var(--sans);color:var(--soft);line-height:1.5;}
.sidebar-link.is-absent .sl-text{font-style:italic;}
.sidebar-link.is-absent:hover .sl-text{font-weight:400;}
.spine-switch{display:inline-flex;border:1px solid var(--rule-strong);border-radius:20px;overflow:hidden;margin:0 0 8px;}
.spine-opt{font-family:var(--sans);font-size:15px;font-weight:600;border:0;background:var(--paper);color:var(--ink);padding:9px 16px;cursor:pointer;line-height:1.2;}
.spine-opt + .spine-opt{border-left:1px solid var(--rule-strong);}
.spine-opt:hover{background:var(--hover-bg);}
.spine-opt[aria-pressed="true"]{background:var(--ink);color:var(--paper);cursor:default;}
body.spine-only .sidebar-link:not(.is-spine),body.spine-only .chapter-card:not(.is-spine),body.spine-only .ce-row:not(.is-spine){display:none;}
.chapter-card.is-spine .card-bookmark{background:var(--ink);}

.hero-series{font-family:var(--sans);color:var(--soft);letter-spacing:1.5px;text-transform:uppercase;margin:-14px 0 26px;}
.hero-tagline{font-family:var(--serif);color:var(--ink-soft);margin:-8px 0 22px;line-height:1.45;}

.overview-contents{max-width:760px;margin:72px auto 0;}
body:not(.vm-list) .overview-contents{display:none;}
body.vm-list .chapter-grid{display:none;}
body.vm-list .overview-contents{margin-top:24px;}
.overview-contents h2{font-family:var(--sans);font-weight:800;letter-spacing:-0.3px;margin-bottom:6px;color:var(--ink);}
.contents-listing .ce-row.is-absent .ce-title{color:var(--soft-2);}
.contents-listing .ce-row a.ce-title:hover{text-decoration:underline;}
.contents-listing .ce-spine{font-family:var(--sans);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--paper);background:var(--ink);border-radius:3px;padding:1px 6px;margin-left:8px;}

@media (max-width: 600px) {
  .decision{margin-left:-16px;margin-right:-16px;padding:4px 16px 18px;}
  .plate{margin-left:-10px;margin-right:-10px;padding:12px 8px 10px;}
}
@media print {
  .plate, .court, .decision, .law-card { break-inside: avoid; }
  .spine-switch, .cover-zoom, #btnTheme { display: none !important; }
  body.spine-only .sidebar-link, body.spine-only .chapter-card, body.spine-only .ce-row { display: initial; }
}
"""


# ============================================================================ the type scale
# One scale, and a check (the author's rule, repeated: the size of a text follows its level. A part is above a chapter,
# a chapter above a section, a section above the body text it heads; a label is never smaller than 14px). The Softanza
# book's scale, kept; the plate, the sketch and the cards of the law take their sizes here and nowhere else.
TYPE = {
    # the reader's navigation, in px
    "sidebar_book": 24, "sidebar_part": 20, "sidebar_link": 18.5,
    "contents_h2": 36, "contents_part": 27, "contents_row": 22, "contents_num": 16, "contents_pg": 15, "contents_badge": 14,
    "card_title": 21, "card_words": 15,
    # inside a chapter page, in em of the reading size (so it follows the font control)
    "section_h3": 1.3, "subsection_h4": 1.12, "body": 1.0, "stage_li": 0.92, "in_words": 0.92,
    # labels and notes, in px
    "body_px": 24, "card_preview": 18, "hero_subtitle": 24, "hero_tagline": 22, "hero_author": 20, "hero_label": 14, "micro": 14,
    "eyebrow": 14, "decision_tag": 14, "proof": 15, "proof_engine": 14.5, "ran": 15, "banner": 14, "court_li": 15, "court_head": 14, "court_path": 14,
    "invite_note": 14.5, "plate_title": 18, "plate_label": 14, "sketch": 16, "sketch_note": 14.5, "law_card": 15.5, "law_card_label": 14,
}


def check_type_scale():
    T, bad = TYPE, []
    def above(hi, lo):
        if not T[hi] > T[lo]:
            bad.append(f"the type scale: {hi} ({T[hi]}) must be larger than {lo} ({T[lo]})")
    above("sidebar_book", "sidebar_part"); above("sidebar_part", "sidebar_link")
    above("contents_h2", "contents_part"); above("contents_part", "contents_row"); above("contents_row", "contents_num")
    above("section_h3", "subsection_h4"); above("subsection_h4", "body")
    above("plate_title", "plate_label"); above("plate_title", "sketch"); above("sketch", "sketch_note")
    above("law_card", "law_card_label")
    for k in ("sidebar_link", "contents_num", "contents_pg", "contents_badge", "card_words", "eyebrow", "decision_tag", "proof", "proof_engine", "ran", "banner",
              "court_li", "court_head", "court_path", "invite_note", "micro", "hero_label", "plate_label", "sketch_note", "law_card_label"):
        if T[k] < 14:
            bad.append(f"the type scale: {k} ({T[k]}px) is below the 14px floor for any label or note")
    if T["body_px"] < 20:
        bad.append(f"the type scale: the default reading size ({T['body_px']}px) is below 20px")
    for k in ("card_preview", "hero_subtitle", "hero_tagline", "hero_author"):
        if T[k] < 18:
            bad.append(f"the type scale: {k} ({T[k]}px) is below 18px")
    r, g, b = (int(LIGHT["--ink"][i:i + 2], 16) for i in (1, 3, 5))
    if 0.299 * r + 0.587 * g + 0.114 * b > 0.299 * 0x17 + 0.587 * 0x14 + 0.114 * 0x0f + 0.5:
        bad.append("the type scale: the body ink is lighter than #17140f")
    for k in ("stage_li", "in_words"):
        if T[k] < 0.85:
            bad.append(f"the type scale: {k} is below 0.85 of the body text")
    return bad


def type_css():
    T = TYPE
    return (
        "\n/* ---- the type scale (TYPE in build_book.py): generated, checked at build ---- */\n"
        f".sidebar-book-title{{font-size:{T['sidebar_book']}px;margin-bottom:22px;}}\n"
        f".sb-part{{font-size:{T['sidebar_part']}px;letter-spacing:0;font-weight:600;text-transform:none;margin:30px 0 6px;line-height:1.3;}}\n"
        f".sidebar-link,.sidebar-link.is-absent{{font-size:{T['sidebar_link']}px;line-height:1.32;padding:11px 0;}}\n"
        ".sidebar-link .sl-spine{width:9px;height:9px;margin-right:10px;vertical-align:1px;}\n"
        f".contents-listing .ce-part{{font-size:{T['contents_part']}px;font-weight:600;text-transform:none;letter-spacing:0;line-height:1.25;margin:44px 0 12px;}}\n"
        f".contents-listing .ce-row{{font-size:{T['contents_row']}px;padding:11px 0;}}\n"
        f".contents-listing .ce-num{{font-size:{T['contents_num']}px;width:46px;}}\n"
        f".contents-listing .ce-pg{{font-size:{T['contents_pg']}px;}}\n"
        f".contents-listing .ce-spine{{font-size:{T['contents_badge']}px;}}\n"
        f".overview-contents h2{{font-size:{T['contents_h2']}px;}}\n"
        f".chapter-card .card-title{{font-size:{T['card_title']}px;}}\n"
        f".chapter-card .card-words{{font-size:{T['card_words']}px;}}\n"
        f".chapter-page .subsection-h{{font-size:{T['section_h3']}em;font-weight:600;text-transform:none;letter-spacing:0;line-height:1.3;}}\n"
        f".chapter-page h4.subsubsection-h{{font-size:{T['subsection_h4']}em;font-weight:600;text-transform:none;letter-spacing:0;}}\n"
        f".chapter-page .ch-eyebrow{{font-size:{T['eyebrow']}px;}}\n"
        f".decision-tag{{font-size:{T['decision_tag']}px;}}\n"
        f".chapter-page p.proof{{font-size:{T['proof']}px;}}\n"
        f".chapter-page p.proof-engine{{font-size:{T['proof_engine']}px;}}\n"
        f".chapter-page .code-cell p.ran,.chapter-page .code-cell p.ran-sub{{font-size:{T['ran']}px;line-height:1.5;}}\n"
        f".status-banner{{font-size:{T['banner']}px;}}\n"
        f".stage-list li{{font-size:{T['stage_li']}em;}}\n"
        f".court li{{font-size:{T['court_li']}px;}}\n"
        f".chapter-page .court p.court-head{{font-size:{T['court_head']}px;}}\n"
        f".court .g-path{{font-size:{T['court_path']}px;}}\n"
        f".the-invite .invite-more,.the-invite .colophon-line{{font-size:{T['invite_note']}px;}}\n"
        f".card-preview{{font-size:{T['card_preview']}px;line-height:1.55;color:var(--ink);max-height:340px;}}\n"
        f".hero-subtitle{{font-size:{T['hero_subtitle']}px;color:var(--ink);}}\n"
        f".hero-tagline{{font-size:{T['hero_tagline']}px;color:var(--ink);}}\n"
        f".hero-author{{font-size:{T['hero_author']}px;}}\n"
        f".hero-series,.search-clear-hl{{font-size:{T['hero_label']}px;}}\n"
        f".spine-badge,.code-cell .cell-label,.stage,.aside-h,.cnb-dir,.court .g-name code{{font-size:{T['micro']}px;}}\n"
        f".plate-t{{font-size:{T['plate_title']}px;}}\n"
        f".plate-n,.in-words .iw-label,.sketch .sk-label,.sketch .sk-rule{{font-size:{T['plate_label']}px;}}\n"
        f".chapter-page .code-cell p.in-words,.chapter-page .law-card p.lc-quote{{font-size:{T['in_words']}em;}}\n"
        f".sketch .sk-title,.chapter-page .sketch p.sk-say,.sketch .sk-ctl{{font-size:{T['sketch']}px;}}\n"
        f".chapter-page .sketch p.sk-caption{{font-size:{T['sketch_note']}px;}}\n"
        f".law-card .lc-title,.law-card dd{{font-size:{T['law_card']}px;}}\n"
        f".law-card .lc-num,.law-card dt,.chapter-page .law-card p.lc-src,.chapter-page p.table-src{{font-size:{T['law_card_label']}px;}}\n"
        ".ayouni-home{display:inline-flex;align-items:center;}\n"
        ".top-header .ayouni-home{height:38px;margin-right:6px;}\n"
        ".top-header .ayouni-home svg{height:22px;width:auto;aspect-ratio:2095/518;}\n"
        "@media (max-width: 900px){.top-header .ayouni-home svg{height:16px;}}\n"
        "@media (max-width: 900px){.sb-part{font-size:19px;}.sidebar-link{font-size:18px;}.contents-listing .ce-part{font-size:23px;}.contents-listing .ce-row{font-size:20px;}}\n"
    )


# ============================================================================ Markdown, as the Refine build reads it
def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    codes = []
    def _stash(m):
        codes.append(m.group(1)); return f"\x00C{len(codes)-1}\x00"
    text = re.sub(r"`([^`]+)`", _stash, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\x00C(\d+)\x00", lambda m: "<code>" + codes[int(m.group(1))] + "</code>", text)
    # the author's open questions stay visible on the page until answered
    text = re.sub(r"\[AUTHOR:(.*?)\]", r'<span class="author-q">[AUTHOR:\1]</span>', text)
    return text


def plain(text):
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


KINDS = "INTENT_FLOW|FORM|WIZARD|SCREEN|COMPONENT|NAV_GRAPH|WORLD_VIEW|INTERACTION|FEEDBACK|VIBE"
FIELDS = ("SATISFIES|ALWAYS_REACHABLE|VISIBLE_ENTITIES|VISIBLE_STATE|INTENT_FLOWS|STEPS|REPORTS|SUPPRESSES|SIGNALS|ENTRIES|"
          "PERSPECTIVE|TONE|SURFACE_AS|DENSITY|MOTION|ROLE|LABEL|TARGET|ACTOR")
ZAYN_TOKEN = re.compile(rf"""
   (?P<promise>//[ \t]*-->[^\n]*)
 | (?P<comment>//[^\n]*)
 | (?P<string>"[^"\n]*")
 | (?P<kw>\bDEFINE\b|(?<=DEFINE\ )(?:{KINDS})\b)
 | (?P<field>\b(?:{FIELDS}|INTENT_FLOW)\b)
 | (?P<verb>\b[A-Z][A-Z_]+\b)
 | (?P<number>(?<![\w.])-?\d+(?:\.\d+)?(?![\w.]))
""", re.X)


def highlight_line(src):
    out, pos = [], 0
    for m in ZAYN_TOKEN.finditer(src):
        out.append(html.escape(src[pos:m.start()], quote=False))
        out.append(f'<span class="c-{m.lastgroup}">{html.escape(m.group(0), quote=False)}</span>')
        pos = m.end()
    out.append(html.escape(src[pos:], quote=False))
    return "".join(out)


def numbered(text, cited=()):
    """The declaration with its lines numbered, each line apart; the lines a finding cites are marked."""
    rows = []
    for k, line in enumerate(text.split("\n"), 1):
        cls = "cl cited" if k in cited else "cl"
        rows.append(f'<span class="{cls}">{highlight_line(line) or "&#8203;"}</span>')
    return '<pre class="numbered"><code>' + "".join(rows) + "</code></pre>"


def render_table(rows, cls="book-table", head=None):
    th = "".join(f"<th>{c}</th>" for c in head) if head else ""
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}">' + (f"<thead><tr>{th}</tr></thead>" if th else "") + f"<tbody>{trs}</tbody></table>"


def code_cell(block, rec, in_words, ui):
    """One declaration: as written, said in words, then the verifier's answer from the run."""
    w = WORDS[ui["lang"]]
    name = (rec or {}).get("name") or block.get("name") or ""
    cited = {d.get("line") for d in (rec or {}).get("diagnostics", []) if d.get("line")}
    label = '<div class="cell-label">Zayn' + (f'<span class="cl-file">{html.escape(name)}</span>' if name else "") + "</div>"
    parts = ['<div class="code-cell">', label, numbered(block["text"], cited)]
    if in_words:
        parts.append(f'<p class="in-words"><span class="iw-label">{w["in_words"]}</span>{inline(in_words)}</p>')
    if rec is None:
        parts.append(f'<p class="ran nv-not-run">{html.escape(w["not-run"].format(why="this declaration has no run on record"))}</p>')
    else:
        v = rec["verdict"]
        if v == "exercise":
            parts.append(f'<p class="ran nv-exercise">{html.escape(w["exercise"])}</p>')
        else:
            if v == "kept":
                text = w["kept_clean"] if not rec.get("diagnostics") else w["kept"]
            elif v == "not-run":
                text = w["not-run"].format(why=rec.get("why", ""))
            else:
                text = w[v]
            exit_note = f'<span class="exit">{html.escape(w["exit"].format(n=rec["exit"]))}</span>' if rec.get("exit") is not None else ""
            parts.append(f'<p class="ran nv-{v}">{exit_note}{html.escape(text)}</p>')
            if rec.get("report"):
                parts.append(f'<pre class="ran-out report"><code>{html.escape(rec["report"])}</code></pre>')
            if "envelope" in block["flags"] and rec.get("envelope"):
                parts.append(f'<p class="ran-sub">{html.escape(w["envelope"])}</p>')
                parts.append(f'<pre class="ran-out envelope"><code>{html.escape(rec["envelope"])}</code></pre>')
    parts.append("</div>")
    return "\n".join(parts)


def sketch_html(lines, ui):
    """A sketch of what a user meets, drawn with real words and one ink line; it opens on its label, "Illustration",
    because Zayn checks the declaration and does not draw the screen (the Zayn site's design, DESIGN-SYSTEM.md, `sketch`).
    A missing control is a dashed outline with its rule; a restored one carries its rule too."""
    title, says, ctls, caption = "", [], [], ""
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        key, _, val = s.partition(":")
        key, val = key.strip().lower(), val.strip()
        if key == "title":
            title = val
        elif key == "say":
            says.append(val)
        elif key in ("control", "missing", "restored"):
            text, _, rule = (x.strip() for x in val.partition("|"))
            ctls.append((key, text, rule))
        elif key == "caption":
            caption = val
        else:
            raise SystemExit(f"sketch: unknown line '{s}'")
    out = ['<div class="sketch">', f'<div class="sk-label">{ui["illustration"]}</div>']
    if title:
        out.append(f'<div class="sk-title">{inline(title)}</div>')
    out += [f'<p class="sk-say">{inline(x)}</p>' for x in says]
    if ctls:
        out.append('<div class="sk-controls">')
        for kind, text, rule in ctls:
            cls = "sk-ctl" + ("" if kind == "control" else f" sk-{kind}")
            tag = f'<span class="sk-rule">{html.escape(rule)}</span>' if rule else ""
            out.append(f'<span class="{cls}">{html.escape(text)}{tag}</span>')
        out.append("</div>")
    if caption:
        out.append(f'<p class="sk-caption">{inline(caption)}</p>')
    out.append("</div>")
    return "\n".join(out)


def rule_card(number, law, ui, version):
    r = law["rules"].get(str(number))
    if not r:
        raise SystemExit(f"rule card: the law at the pin has no rule {number}")
    art = law["articles"].get(r.get("derived_from") or "", {})
    set_n = r["_set"][3:]
    set_t = re.sub(r"^Set \d+:\s*", "", r.get("_set_title", ""))
    tier = r.get("enforcement") or "null"
    # what the pin measures, and no more: the tier is the law's own word for the rule; the diagnostics are the ones
    # whose binding in the contract names this rule (what a tier means is a ruling the law's author has before him)
    citing = [d["id"] for d in law["diag_list"] if str(number) in [str(x) for x in (d.get("rules") or [])]]
    cited = " ".join(f"<code>{html.escape(c)}</code>" for c in citing) if citing else html.escape(ui["cited_none"])
    rows = [(ui["article"], f'{art.get("numeral", "null")} · {art.get("title", "null")}'),
            (ui["set"], f"{set_n} · {set_t}"),
            (ui["tier"], f"<code>{html.escape(tier)}</code>"),
            (ui["cited_by"], cited),
            (ui["why"], html.escape(r.get("why") or "null"))]
    dl = "".join(f"<dt>{html.escape(k)}</dt><dd>{v}</dd>" for k, v in rows)
    return (f'<aside class="law-card" id="rule-{number}"><div class="lc-head"><span class="lc-num">{ui["rule"]} {number}</span>'
            f'<span class="lc-title">{html.escape(r.get("title", ""))}</span></div><dl>{dl}</dl>'
            f'<p class="lc-src">{html.escape(ui["law_src"].format(v=version))}</p></aside>')


def right_card(rid, law, ui, version):
    r = law["rights"].get(rid)
    if not r:
        raise SystemExit(f"right card: the law at the pin has no right '{rid}'")
    return (f'<aside class="law-card" id="right-{rid}"><div class="lc-head"><span class="lc-num">{html.escape(ui["right_label"])}</span>'
            f'<span class="lc-title">{html.escape(r.get("title", ""))}</span></div>'
            f'<p class="lc-quote">{html.escape(r.get("statement", ""))}</p>'
            f'<p class="lc-src">{html.escape(ui["law_src"].format(v=version))}</p></aside>')


def article_card(aid, law, ui, version):
    a = law["articles"].get(aid)
    if not a:
        raise SystemExit(f"article card: the law at the pin has no article '{aid}'")
    return (f'<aside class="law-card" id="article-{aid}"><div class="lc-head"><span class="lc-num">{ui["article"]} {html.escape(a.get("numeral", ""))}</span>'
            f'<span class="lc-title">{html.escape(a.get("title", ""))}</span></div>'
            f'<p class="lc-quote">{html.escape(a.get("statement", ""))}</p>'
            f'<p class="lc-src">{html.escape(ui["law_src"].format(v=version))}</p></aside>')


def families_table(law, ui, version):
    """The verbs in their families, each with its invariant, as the law's data holds them."""
    fams = (law["law"].get("intents") or {}).get("families") or {}
    if not fams:
        raise SystemExit("families: the law at the pin holds no intent families")
    rows = [[f"<strong>{html.escape(name)}</strong>",
             " ".join(f"<code>{html.escape(v)}</code>" for v in f.get("verbs", [])),
             html.escape(f.get("invariant", ""))] for name, f in fams.items()]
    return (render_table(rows, "book-table families", ui["families_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def levels_table(law, ui):
    """The four levels of checking as the contract's data files them, with the kinds of finding at each."""
    levels = law["contract"].get("levels") or {}
    if not levels:
        raise SystemExit("levels: the contract at the pin holds no levels")
    rows = []
    for n in sorted(levels, key=int):
        lv = levels[n]
        count = sum(1 for d in law["diag_list"] if str(d.get("level")) == str(n))
        rows.append([f"<strong>{html.escape(str(n))}</strong>", html.escape(lv.get("name", "")), html.escape(lv.get("requires", "")),
                     html.escape(lv.get("decides", "")), str(count)])
    v = (law["contract"].get("metadata") or {}).get("version", "null")
    return (render_table(rows, "book-table levels", ui["levels_h"])
            + f'<p class="table-src">{html.escape(ui["contract_src"].format(v=v))}</p>')


def fields_table(law, ui):
    """Which fields each kind carries beyond the ones every kind carries."""
    rows_in = law.get("fields_by_kind") or []
    if not rows_in:
        raise SystemExit("fields: the specification at the pin tables no fields by kind")
    rows = [[" ".join(f"<code>{html.escape(k)}</code>" for k in kinds),
             " ".join(f"<code>{html.escape(f)}</code>" for f in fields) if fields else html.escape(ui["fields_none"])]
            for kinds, fields in rows_in]
    return (render_table(rows, "book-table families", ui["fields_h"])
            + f'<p class="table-src">{html.escape(ui["spec_src"].format(v=law.get("spec_version") or "null"))}</p>')


def lists_table(law, ui):
    """The closed lists of the language: the field, the kind that carries it, and every value it admits."""
    lists = law.get("closed_lists") or []
    if not lists:
        raise SystemExit("lists: the specification at the pin tables no closed list")
    rows = [[f"<code>{html.escape(field)}</code>", html.escape(on.lower()) if on.lower().startswith("any") else f"<code>{html.escape(on)}</code>",
             " ".join(f"<code>{html.escape(v)}</code>" for v in values)] for field, on, values in lists]
    return (render_table(rows, "book-table families", ui["lists_h"])
            + f'<p class="table-src">{html.escape(ui["spec_src"].format(v=law.get("spec_version") or "null"))}</p>')


def _cites(d, law):
    parts = []
    if d.get("rules"):
        parts.append(", ".join(f"Rule {html.escape(str(n))}" for n in d["rules"]))
    if d.get("articles"):
        parts.append(", ".join("Article " + html.escape((law["articles"].get(a) or {}).get("numeral", a)) for a in d["articles"]))
    if d.get("rights"):
        parts.append(", ".join(html.escape((law["rights"].get(r) or {}).get("title", r)) for r in d["rights"]))
    return "; ".join(parts)


def diagnostics_table(law, ui):
    """Appendix C: every kind of finding of the verifier's contract, in the contract's order within each level."""
    rows = []
    for d in sorted(law["diag_list"], key=lambda d: int(d.get("level") or 0)):
        rows.append(['<code>' + html.escape(d["id"]).replace("_", "_<wbr>") + '</code>', html.escape(str(d.get("level", ""))), html.escape(d.get("severity", "")),
                     html.escape(d.get("summary", "")), _cites(d, law) or html.escape(ui["diag_none"])])
    v = (law["contract"].get("metadata") or {}).get("version", "null")
    return (render_table(rows, "book-table families diag", ui["diag_h"])
            + f'<p class="table-src">{html.escape(ui["contract_src"].format(v=v))}</p>')


def constitution_full(law, ui, version):
    """Appendix A: the law as its data holds it: the preamble, the articles, the rights, the forbidden patterns, then
    every set with its rules. Printed fields: a rule's number, title, tier, article, text ("solution"), what it tells
    the reader to avoid, and its reason. Nothing is typed here."""
    L = law["law"]
    out = []
    pre = (L.get("preamble") or {}).get("text") or ""
    for para in [p.strip() for p in pre.split("\n") if p.strip()]:
        out.append(f"<p>{html.escape(para)}</p>")
    for aid in law["articles"]:
        out.append(article_card(aid, law, ui, version))
    rights = [[html.escape(r.get("title", "")), html.escape(r.get("statement", "")),
               ", ".join(html.escape(str(n)) for n in r.get("enforced_by") or [])] for r in L.get("rights", [])]
    out.append(render_table(rights, "book-table", ui["rights_h"]))
    forb = [[html.escape(f.get("title", "")), ", ".join(html.escape(str(n)) for n in f.get("violates") or [])] for f in L.get("forbidden", [])]
    out.append(render_table(forb, "book-table", ui["forbidden_h"]))
    sets = sorted((k for k in L if re.fullmatch(r"set\d+", k)), key=lambda k: int(k[3:]))
    for k in sets:
        st = L[k]
        title = re.sub(r"^Set \d+:\s*", "", st.get("title", ""))
        out.append(f'<h3 class="subsection-h" id="law-{k}">{html.escape(ui["set"])} {k[3:]} · {html.escape(title)}</h3>')
        if st.get("description"):
            out.append(f"<p>{html.escape(st['description'])}</p>")
        for r in st.get("rules", []):
            art = law["articles"].get(r.get("derived_from") or "", {})
            rows = [(ui["article"], f'{html.escape(art.get("numeral", "null"))} · {html.escape(art.get("title", "null"))}'),
                    (ui["tier"], f'<code>{html.escape(r.get("enforcement") or "null")}</code>')]
            if r.get("avoid"):
                rows.append((ui["avoid"], html.escape("; ".join(r["avoid"]))))
            rows.append((ui["why"], html.escape(r.get("why") or "null")))
            dl = "".join(f"<dt>{html.escape(a)}</dt><dd>{b}</dd>" for a, b in rows)
            out.append(f'<aside class="law-card" id="law-rule-{html.escape(str(r["number"]))}"><div class="lc-head">'
                       f'<span class="lc-num">{ui["rule"]} {html.escape(str(r["number"]))}</span>'
                       f'<span class="lc-title">{html.escape(r.get("title", ""))}</span></div>'
                       f'<p class="lc-quote">{html.escape(r.get("solution", ""))}</p><dl>{dl}</dl></aside>')
    gone = [[html.escape(str(n)), html.escape(v.get("title", "")), html.escape(ui["retired_into"].format(n=v.get("into", "")))]
            for n, v in (L.get("retired") or {}).items()]
    gone += [[html.escape(str(n)), "", html.escape(ui["burned"])] for n in (L.get("burned") or {})]
    if gone:
        out.append(render_table(sorted(gone, key=lambda r: int(r[0])), "book-table", ui["retired_h"]))
    out.append(f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')
    return "\n".join(out)


def sources_table(ui):
    """Appendix F: the register of the field's sources, as research/FIELD.md keeps it: the source, what its page calls
    itself, the date it was read, and where the book uses it. The reading notes stay in the register."""
    path = ROOT / "research" / "FIELD.md"
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(F-\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 6:
            continue
        src = re.sub(r"<(https?://[^>]+)>", r"[\1](\1)", cells[0])
        date = re.search(r"\d{4}-\d{2}-\d{2}", cells[2])
        rows.append([html.escape(m.group(1)), inline(src), inline(cells[1]), html.escape(date.group(0) if date else "null"), inline(cells[5])])
    if not rows:
        raise SystemExit("sources: research/FIELD.md holds no source row")
    return (render_table(rows, "book-table sources", ui["sources_h"])
            + f'<p class="table-src">{html.escape(ui["sources_src"])}</p>')


def _rule_num(r):
    return int(re.sub(r"\D", "", str(r["number"])) or 0)


def articles_table(law, ui, version):
    rows = []
    for aid, a in law["articles"].items():
        n = sum(1 for r in law["rule_list"] if r.get("derived_from") == aid)
        rows.append([html.escape(a.get("numeral", "")), html.escape(a.get("title", "")), html.escape(a.get("statement", "")), str(n)])
    return (render_table(rows, "book-table", ui["articles_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def rights_table(law, ui, version):
    rows = [[html.escape(r.get("title", "")), html.escape(r.get("statement", "")),
             ", ".join(html.escape(str(n)) for n in r.get("enforced_by") or [])] for r in law["law"].get("rights", [])]
    return (render_table(rows, "book-table", ui["rights_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def forbidden_table(law, ui, version):
    rows = [[html.escape(f.get("title", "")), ", ".join(html.escape(str(n)) for n in f.get("violates") or [])]
            for f in law["law"].get("forbidden", [])]
    return (render_table(rows, "book-table", ui["forbidden_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def sets_table(law, ui, version):
    L = law["law"]
    rows = []
    for k in sorted((k for k in L if re.fullmatch(r"set\d+", k)), key=lambda k: int(k[3:])):
        st = L[k]
        nums = sorted(_rule_num(r) for r in st.get("rules", []))
        rows.append([k[3:], html.escape(re.sub(r"^Set \d+:\s*", "", st.get("title", ""))), str(len(nums)), ", ".join(str(n) for n in nums)])
    return (render_table(rows, "book-table", ui["sets_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def tiers_table(law, ui, version):
    """The law's own filing of each rule under a tier, beside the count by citation (law["ladder"]): how many rules of
    the tier a kind of finding that the verifier raises cites, and how many an audit names. Counted, never glossed."""
    lad = law.get("ladder") or {}
    order, by = [], {}
    for r in law["rule_list"]:
        tr = r.get("enforcement") or "null"
        if tr not in by:
            by[tr] = []; order.append(tr)
        by[tr].append(r)
    def cell(nums):
        return (f"{len(nums)}: " + ", ".join(str(n) for n in nums)) if nums else "0"
    rows = []
    for tr in order:
        ver = sorted(_rule_num(r) for r in by[tr] if (lad.get(str(r["number"])) or {}).get("codes"))
        aud = sorted(_rule_num(r) for r in by[tr] if (lad.get(str(r["number"])) or {}).get("audits"))
        rows.append([f"<code>{html.escape(tr)}</code>", str(len(by[tr])), cell(ver), cell(aud)])
    return (render_table(rows, "book-table", ui["tiers_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))} {html.escape(ui["ladder_src"])}</p>')


def ladder_table(law, ui):
    lad = law.get("ladder") or {}
    if not lad:
        raise SystemExit("ladder: no citation counted at the pin")
    rows = []
    for n in sorted(lad, key=lambda x: int(x)):
        r = law["rules"].get(n) or {}
        codes = " ".join("<code>" + html.escape(c).replace("_", "_<wbr>") + "</code>" for c in lad[n]["codes"]) or "none"
        auds = "; ".join(f'{html.escape(chk)} ({html.escape(ui["inst_" + inst])})' for inst, chk in lad[n]["audits"]) or "none"
        rows.append([f"<strong>{html.escape(n)}</strong> {html.escape(r.get('title', ''))}",
                     f"<code>{html.escape(r.get('enforcement') or 'null')}</code>", codes, auds])
    return (render_table(rows, "book-table families diag", ui["ladder_h"])
            + f'<p class="table-src">{html.escape(ui["ladder_src"])}</p>')


def anatomy_table(number, law, ui, version):
    """One rule printed whole, field by field, under the names its file gives them."""
    r = law["rules"].get(str(number))
    if not r:
        raise SystemExit(f"anatomy: the law at the pin has no rule {number}")
    rows = []
    for k, v in r.items():
        if k.startswith("_"):
            continue
        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, list):
            v = "; ".join(str(x) for x in v) if v else "[]"
        elif isinstance(v, dict):
            v = json.dumps(v, ensure_ascii=False)
        rows.append([f"<code>{html.escape(k)}</code>", html.escape(str(v))])
    return (render_table(rows, "book-table families", ui["anatomy_h"])
            + f'<p class="table-src">{html.escape(ui["law_src"].format(v=version))}</p>')


def pins_table(law, ui):
    rows = [[f"<code>{html.escape(p)}</code>", html.escape(v)] for p, v in law.get("pins") or []]
    if not rows:
        raise SystemExit("pins: no data file of the pin records a version of the law")
    return (render_table(rows, "book-table families", ui["pins_h"])
            + f'<p class="table-src">{html.escape(ui["pins_src"])}</p>')


def suite_cell(level, suite, ui, where, errors):
    """The conformance suite's own run at one level, as the snapshot's runner printed it at this build."""
    rec = (suite or {}).get(str(level))
    if not rec:
        errors.append(f"{where}: the suite has no run on record at level {level}")
        return ""
    ok = rec.get("exit") == 0
    return ('<div class="code-cell run-cell"><div class="cell-label">' + html.escape(ui["run_label"])
            + f'<span class="cl-file">{html.escape(rec["command"])}</span></div>'
            + f'<pre class="ran-out"><code>{html.escape(rec["output"])}</code></pre>'
            + f'<p class="ran nv-{"kept" if ok else "differs"}"><span class="exit">{html.escape(WORDS[ui["lang"]]["exit"].format(n=rec["exit"]))}</span>'
            + html.escape(ui["suite_ran"]) + "</p></div>")


TOKEN = re.compile(r"\{\{n:([a-z0-9_.\-]+)\}\}")


def fill_tokens(text, facts, where, errors):
    """Every count a page states is a token read from the run's reading of the data files."""
    def sub(m):
        key = m.group(1)
        if key not in facts:
            errors.append(f"{where}: the token {{{{n:{key}}}}} names no fact the build reads")
            return "null"
        if facts[key] is None:
            errors.append(f"{where}: the fact {key} could not be read from the snapshot")
            return "null"
        return str(facts[key])
    return TOKEN.sub(sub, text)


def convert_body(body, meta, ui, run_rec, law, version, errors, where, suite=None):
    """The Refine build's Markdown reading, with this book's chapter shape: the plate, the decision (boxed), the court
    (fixtures run at build), the stage words at the head of "Where it stands"."""
    lines = body.split("\n")
    out, para, n = [], [], len(lines)
    blocks = (run_rec or {}).get("blocks", [])
    src_blocks = code_blocks(body)
    k_code, k_plate = 0, 0
    current, decision_open, in_plate = None, False, False
    number = meta.get("appendix") or meta["number"]

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    def close_section():
        nonlocal decision_open
        flush()
        if current == "The court":
            out.append(court_box(meta, ui, run_rec, law))
        if decision_open:
            out.append("</section>"); decision_open = False

    i = 0
    while i < n:
        s = lines[i].strip()
        if s == "":
            flush(); i += 1; continue
        if s.startswith(":::"):
            flush()
            rest = s[3:].strip()
            if rest.lower().startswith("plate"):
                if in_plate:
                    errors.append(f"{where}: a plate opens inside a plate")
                k_plate += 1
                in_plate = True
                title = rest[5:].strip()
                out.append(f'<figure class="plate" id="plate-{number}-{k_plate}"><figcaption class="plate-h">'
                           f'<span class="plate-n">{ui["plate"]} {number}.{k_plate}</span>'
                           f'<span class="plate-t">{inline(title)}</span></figcaption>')
            elif rest == "":
                if not in_plate:
                    errors.append(f"{where}: ':::' closes a plate that was not opened")
                in_plate = False
                out.append("</figure>")
            else:
                errors.append(f"{where}: unknown block '{s}'")
            i += 1; continue
        if s.startswith("## "):
            close_section()
            if in_plate:
                errors.append(f"{where}: the plate before '{s}' is not closed")
            head = s[3:].strip()
            current = head
            if head == "What I refused":
                out.append(f'<section class="decision"><div class="decision-tag">{ui["decision"]}</div>'); decision_open = True
            out.append(f'<h3 class="subsection-h">{inline(head)}</h3>')
            if head == "Where it stands" and meta.get("stage"):
                items = "".join(f'<li><span class="stage s-{k}">{ui["stage"].get(k, k)}</span><span>{inline(str(v))}</span></li>'
                                for k, v in meta["stage"].items())
                out.append(f'<ul class="stage-list">{items}</ul>')
            i += 1; continue
        if s.startswith("### "):
            flush(); out.append(f'<h4 class="subsubsection-h">{inline(s[4:].strip())}</h4>'); i += 1; continue
        if s == "---":
            flush(); out.append('<div class="divider">· · ·</div>'); i += 1; continue
        if s == "{{families}}":
            flush(); out.append(families_table(law, ui, version)); i += 1; continue
        if s == "{{levels}}":
            flush(); out.append(levels_table(law, ui)); i += 1; continue
        if s == "{{lists}}":
            flush(); out.append(lists_table(law, ui)); i += 1; continue
        if s == "{{fields}}":
            flush(); out.append(fields_table(law, ui)); i += 1; continue
        if s == "{{diagnostics}}":
            flush(); out.append(diagnostics_table(law, ui)); i += 1; continue
        if s == "{{constitution}}":
            flush(); out.append(constitution_full(law, ui, version)); i += 1; continue
        if s == "{{sources}}":
            flush(); out.append(sources_table(ui)); i += 1; continue
        if s == "{{articles}}":
            flush(); out.append(articles_table(law, ui, version)); i += 1; continue
        if s == "{{rights}}":
            flush(); out.append(rights_table(law, ui, version)); i += 1; continue
        if s == "{{forbidden}}":
            flush(); out.append(forbidden_table(law, ui, version)); i += 1; continue
        if s == "{{sets}}":
            flush(); out.append(sets_table(law, ui, version)); i += 1; continue
        if s == "{{ladder}}":
            flush(); out.append(ladder_table(law, ui)); i += 1; continue
        if s == "{{pins}}":
            flush(); out.append(pins_table(law, ui)); i += 1; continue
        if s == "{{tiers}}":
            flush(); out.append(tiers_table(law, ui, version)); i += 1; continue
        m_an = re.match(r"^\{\{anatomy:(\d+)\}\}$", s)
        if m_an:
            flush(); out.append(anatomy_table(m_an.group(1), law, ui, version)); i += 1; continue
        m_card = re.match(r"^\{\{(rule|right|suite|article):([a-z0-9-]+)\}\}$", s)
        if m_card:
            flush()
            if m_card.group(1) == "suite":
                out.append(suite_cell(m_card.group(2), suite, ui, where, errors))
            elif m_card.group(1) == "article":
                out.append(article_card(m_card.group(2), law, ui, version))
            else:
                out.append(rule_card(m_card.group(2), law, ui, version) if m_card.group(1) == "rule"
                           else right_card(m_card.group(2), law, ui, version))
            i += 1; continue
        if s.startswith("```"):
            flush()
            info = s[3:].strip().split()
            i += 1; code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            tag = info[0].lower() if info else ""
            if tag == "zayn":
                block = src_blocks[k_code]
                rec = blocks[k_code] if k_code < len(blocks) else None
                k_code += 1
                # the sentence in words follows the declaration: "In words: ..."
                j = i
                while j < n and lines[j].strip() == "":
                    j += 1
                in_words = None
                if j < n and re.match(r"(?i)^in words:\s*", lines[j].strip()):
                    words = [re.sub(r"(?i)^in words:\s*", "", lines[j].strip())]
                    j += 1
                    while j < n and lines[j].strip() and not lines[j].strip().startswith(("```", ":::", "#")):
                        words.append(lines[j].strip()); j += 1
                    in_words = " ".join(words)
                    i = j
                else:
                    errors.append(f"{where}: the declaration '{block.get('name') or k_code}' has no \"In words\" line")
                if not in_plate:
                    errors.append(f"{where}: the declaration '{block.get('name') or k_code}' stands outside a plate")
                out.append(code_cell(block, rec, in_words, ui))
            elif tag == "sketch":
                if not in_plate:
                    errors.append(f"{where}: a sketch stands outside a plate")
                out.append(sketch_html(code, ui))
            elif tag == "symbols":
                if not in_plate:
                    errors.append(f"{where}: a symbol table stands outside a plate")
                name = info[1] if len(info) > 1 else "symbols.json"
                out.append('<div class="code-cell aux-cell"><div class="cell-label">' + html.escape(ui["symbols"])
                           + f'<span class="cl-file">{html.escape(name)}</span></div>'
                           + f"<pre><code>{html.escape(chr(10).join(code))}</code></pre></div>")
            else:
                out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            continue
        if s.startswith(">"):
            flush(); bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("<blockquote>" + "<br>".join(inline(x) for x in bq) + "</blockquote>"); continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            flush(); tbl = [s]; j = i + 1
            while j < n and lines[j].strip().startswith("|"):
                tbl.append(lines[j].strip()); j += 1
            rows = [[inline(c.strip()) for c in r.strip("|").split("|")] for r in tbl]
            out.append(render_table(rows[2:], head=rows[0])); i = j; continue
        if re.match(r"^[-*]\s+", s) and not s.startswith("**"):
            flush(); items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip())); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if re.match(r"^\d+\.\s+", s):
            flush(); items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        para.append(s); i += 1
    close_section()
    if in_plate:
        errors.append(f"{where}: the last plate is not closed")
    return "\n".join(out)


def court_box(meta, ui, run_rec, law=None):
    court = (run_rec or {}).get("court") or []
    if not court:
        return ""
    items = []
    for c in court:
        name = c["file"]
        if not c.get("exists"):
            items.append(f'<li><span class="g-name"><code>{html.escape(name)}</code></span><span class="g-missing">{ui["court_missing"]}</span></li>')
            continue
        url = GH_BLOB.format(tag=PIN_TAG, path=f"conformance/fixtures/{name}")
        want = ", ".join(c["expect_ids"]) if c["expect_ids"] else ui["court_clean"]
        verdict = (f'<span class="g-ok">{ui["court_ok"]}</span>' if c.get("pass")
                   else f'<span class="g-missing">{ui["court_bad"]}: {html.escape(", ".join(c.get("got_ids") or []) or ui["court_clean"])}</span>')
        items.append(f'<li><span class="g-name"><a href="{url}" target="_blank" rel="noopener"><code>{html.escape(name)}</code></a></span>'
                     f'<span class="g-count">{html.escape(want)}</span>{verdict}</li>')
    # each code the fixtures expect, once, with its level and the contract's own sentence (violations.json, "summary")
    seen, glosses = [], []
    diags = (law or {}).get("diagnostics", {})
    for c in court:
        for code in c.get("expect_ids") or []:
            if code in seen or code not in diags:
                continue
            seen.append(code)
            d = diags[code]
            sev = ui["court_error"] if d.get("severity") == "error" else ui["court_warning"]
            glosses.append(f'<li class="g-gloss"><span class="g-count">{html.escape(code)}</span>'
                           f'<span class="g-path">{ui["court_level"]} {html.escape(str(d.get("level", "")))}, {sev}</span>'
                           f'<span class="g-what">{html.escape(d.get("summary", ""))}</span></li>')
    gloss = (f'<p class="court-head court-codes">{ui["court_codes"]}</p><ul>{"".join(glosses)}</ul>' if glosses else "")
    return f'<div class="court"><p class="court-head">{{COURT_HEAD}}</p><ul>{"".join(items)}</ul>{gloss}</div>'


def words_of(body):
    no_code = re.sub(r"(?ms)^```.*?^```", "", body)
    no_code = re.sub(r"(?m)^(#+\s.*|:::.*|\{\{.*\}\})$", "", no_code)
    return len(re.findall(r"\b\w+\b", plain(no_code)))


def check_shape(body, meta, where, errors):
    """The fixed headings, each once and in order; at most three questions to the author."""
    if meta.get("appendix") or not meta.get("number"):
        return
    heads = [h.strip() for h in re.findall(r"(?m)^## (.+)$", re.sub(r"(?ms)^```.*?^```", "", body))]
    found = [h for h in heads if h in SHAPE]
    if found != SHAPE:
        missing = [h for h in SHAPE if h not in found]
        errors.append(f"{where}: the chapter's fixed headings must be {SHAPE}, each once, in this order"
                      + (f"; missing: {missing}" if missing else f"; found in the order {found}"))
    if not re.search(r"(?ms)^## The principle\s*\n+\*\*[^\n]+\*\*\s*$", body):
        errors.append(f"{where}: 'The principle' must open on one bold sentence")
    q = re.findall(r"\[AUTHOR:", body)
    if len(q) > 3:
        errors.append(f"{where}: {len(q)} questions to the author; three at most")


# ============================================================================ the cover
COVER_ZOOM_JS = ("(function(){var w=document.querySelector('.cover-wrap'),z=document.querySelector('.cover-zoom'),lb=document.getElementById('coverLightbox');"
    "if(!w||!z||!lb)return;var src=w.querySelector('img'),big=lb.querySelector('img'),x=lb.querySelector('.cover-close');"
    "function open(){big.src=src.src;big.alt=src.alt;lb.hidden=false;document.body.style.overflow='hidden';x.focus();}"
    "function close(){lb.hidden=true;big.removeAttribute('src');document.body.style.overflow='';z.focus();}"
    "z.addEventListener('click',function(e){e.stopPropagation();open();});"
    "lb.addEventListener('click',function(e){if(e.target===lb||e.target===x)close();});"
    "document.addEventListener('keydown',function(e){if(!lb.hidden&&e.key==='Escape')close();});})();")


def cover_html(ui):
    """The front cover, embedded so the reader stays one file."""
    import base64, io
    from PIL import Image
    img = ROOT / "assets" / "cover" / "cover.png"
    if not img.exists():
        raise SystemExit("assets/cover/cover.png does not exist: run python tools/make_cover.py")
    buf = io.BytesIO()
    Image.open(img).convert("RGB").save(buf, "JPEG", quality=86, optimize=True)
    data = base64.b64encode(buf.getvalue()).decode("ascii")
    return (f'<img class="cover-img" src="data:image/jpeg;base64,{data}" width="1097" height="1434" '
            f'alt="{html.escape(ui["cover_alt"])}">')


# ============================================================================ the names gate
def _withheld():
    p = ROOT / "tools" / "withheld.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"replace": [], "never": []}


def withhold(fragment):
    """The book's copy of the law: a withheld name becomes its description in square brackets."""
    for a, b in _withheld()["replace"]:
        fragment = fragment.replace(a, html.escape(b, quote=False))
    return fragment


def check_names(text, where, errors):
    for name in _withheld()["never"]:
        if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", text):
            errors.append(f"{where}: prints a name the book leaves out ({name[0]}…, see tools/withheld.json)")


# ============================================================================ pages
def chapter_part(st, number):
    for p in st["parts"]:
        for num, _ in p["chapters"]:
            if num == number:
                return p
    return None


def preview_of(body):
    txt = ""
    for ln in body.split("\n"):
        s = ln.strip()
        if not s or s.startswith(("#", ">", "-", "|", "`", "[", ":", "{")):
            continue
        txt += (" " if txt else "") + plain(s)
        if len(txt) > 230:
            break
    if len(txt) > 250:
        txt = txt[:250].rsplit(" ", 1)[0] + "…"
    return html.escape(txt, quote=False)


def build_pages(st, en_src, runs, law, ui, errors):
    pages = []
    facts = runs.get("run", {}).get("law", {})
    version = facts.get("law.version") or "null"
    run = runs.get("run", {})
    court_head = html.escape(ui["court_head"].format(sha=(run.get("zayn") or {}).get("short", ""), d=run.get("date", "")))
    for path, meta, body in en_src:
        number = meta["number"]
        appendix = meta.get("appendix")
        key = f"en/{path.stem}"
        where = key
        if appendix:
            slug = f"app-{str(appendix).lower()}-{meta['id']}"
            eyebrow = f'{ui["appendix"]} {appendix}'
            spine = False
        else:
            slug = "preface" if number == 0 else f"ch{number}-{meta['id']}"
            part = chapter_part(st, number)
            spine = number in st["spine"]
            eyebrow = ui["preface"] if number == 0 else f'{ui["part"]} {ROMAN[part["number"]]} · {ui["chapter"]} {number}'
        check_shape(body, meta, where, errors)
        check_names(body, where + " (source)", errors)
        run_rec = runs.get("chapters", {}).get(key)
        filled = fill_tokens(body, facts, where, errors)
        meta = {**meta, "stage": {k: fill_tokens(str(v), facts, where, errors) for k, v in (meta.get("stage") or {}).items()}}
        body_html = withhold(convert_body(filled, meta, ui, run_rec, law, version, errors, where,
                                          run.get("suite")).replace("{COURT_HEAD}", court_head))
        check_names(body_html, where, errors)
        pages.append(dict(key=key, slug=slug, meta=meta, number=number, title=meta["title"], eyebrow=eyebrow, spine=spine,
                          body_html=body_html, run=run_rec, words=words_of(body), preview=preview_of(filled), appendix=appendix))
    for k, p in enumerate(pages):
        p["prev"] = pages[k - 1]["slug"] if k > 0 else ""
        p["next"] = pages[k + 1]["slug"] if k < len(pages) - 1 else ""
    return pages


def proof_html(p, runs, ui, stale):
    run = p["run"]
    r = runs.get("run", {})
    zayn = r.get("zayn", {})
    if stale:
        return f'<p class="proof fails"><strong>{html.escape(ui["stale"])}</strong></p>'
    if not run or not run.get("runnable"):
        if p.get("appendix"):
            z = (runs.get("run", {}).get("zayn") or {})
            return '<p class="proof">' + html.escape(ui["proof_data"].format(d=runs.get("run", {}).get("date", ""), tag=z.get("tag") or "", sha=z.get("short", ""))) + "</p>"
        return f'<p class="proof">{ui["proof_none"]}</p>' if p["number"] else ""
    line = ui["proof"].format(d=run.get("ran", ""), tag=zayn.get("tag") or "", sha=zayn.get("short", ""),
                              law=(r.get("law") or {}).get("law.version", "null"), k=run["kept"], n=run["runnable"])
    fails = run["kept"] < run["runnable"]
    out = f'<p class="proof{" fails" if fails else ""}"><strong>{html.escape(line)}</strong></p>'
    out += f'<p class="proof-engine">{html.escape(ui["proof_how"].format(node=(r.get("node") or "null").lstrip("v")))}</p>'
    return out


def the_invitation(ui):
    """The open book's standing invitation to organisations and the colophon line, once, at the end of the reader
    (house OPEN-BOOK.md, lines 27 and 28): word for word, no payment."""
    col = html.escape(ui["colophon"]).replace("CC BY-NC-ND 4.0", f'<a href="{ui["licence_url"]}">CC BY-NC-ND 4.0</a>')
    mail = ui["invite_mail"]
    return (f'<section class="the-invite"><p class="invite-line">{html.escape(ui["invite"])}<a href="mailto:{mail}">{mail}</a>.</p>'
            f'<p class="invite-more"><a href="{ui["offer_url"]}">{html.escape(ui["offer_link"])}</a></p>'
            f'<p class="colophon-line">{col}</p></section>\n')


STAGES = ("draft", "review", "published")      # a page's life (HOUSE-18): only the author moves a page beyond draft


def status_banner(meta, ui):
    st = meta.get("status", "draft")
    label = ui.get(st, st) if st in STAGES or st == "missing" else st
    title = ui.get(f"{st}_title", "")
    return f'<div class="status-banner st-{st}" title="{html.escape(title)}">{html.escape(label)}</div>'


def render_reader(st, pages, runs, stale_keys):
    ui = UI["en"]
    head, script = apply_shell(ui)
    by_number = {p["number"]: p for p in pages if not p["appendix"]}

    cards, articles = [], []
    last_chapter = max((p["number"] for p in pages if not p["appendix"]), default=0)
    for p in pages:
        sp = " is-spine" if p["spine"] else ""
        meta_line = p["eyebrow"] + f' · {p["words"]} {ui["words"]}'
        cards.append(f'<a class="chapter-card{sp}" href="#{p["slug"]}">\n<span class="card-bookmark"></span>'
                     f'<div class="card-preview"><p>{p["preview"]}</p></div>\n'
                     f'<div class="card-meta"><h3 class="card-title">{html.escape(p["title"], quote=False)}</h3>'
                     f'<p class="card-words">{html.escape(meta_line)}</p></div>\n</a>')
        stale = p["key"] in stale_keys
        spine_badge = f'<span class="spine-badge" title="{html.escape(ui["spine_title"])}">{ui["spine"]}</span>' if p["spine"] else ""
        articles.append(
            f'<article class="chapter-page" id="page-{p["slug"]}" data-slug="{p["slug"]}" '
            f'data-title="{html.escape(p["title"], quote=True)}" data-prev="{p["prev"]}" data-next="{p["next"]}">\n'
            f'<div class="ch-eyebrow">{html.escape(p["eyebrow"])}{spine_badge}</div>\n'
            f'<h1 class="ch-title">{html.escape(p["title"], quote=False)}</h1>\n'
            f'{status_banner(p["meta"], ui)}\n{proof_html(p, runs, ui, stale)}\n'
            f'<div class="ch-rule"></div>\n{p["body_html"]}\n{the_invitation(ui) if p["number"] == last_chapter and not p["appendix"] else ""}</article>')

    # the navigation: the whole book, parts and chapters; a chapter in writing is shown and not linked
    side, rows = [], []
    if 0 in by_number:
        side.append(f'<a class="sidebar-link is-spine" href="#preface"><span class="sl-text" data-t="{ui["preface"]}">'
                    f'<span class="sl-spine"></span>{ui["preface"]}</span><span class="sl-leader"></span></a>')
        rows.append(f'<div class="ce-row is-spine"><span class="ce-num"></span><a class="ce-title" href="#preface">{ui["preface"]}</a></div>')
    for part in st["parts"]:
        ptitle = f'{ui["part"]} {ROMAN[part["number"]]} · {part["title"]}'
        side.append(f'<div class="sb-part">{html.escape(ptitle)}</div>')
        rows.append(f'<div class="ce-part">{html.escape(ptitle)}</div>')
        for num, ctitle in part["chapters"]:
            sp = num in st["spine"]
            cls = " is-spine" if sp else ""
            p = by_number.get(num)
            label = f"{num} · {html.escape(p['title'] if p else ctitle, quote=False)}"
            spine_mark = f'<span class="ce-spine">{ui["spine"]}</span>' if sp else ""
            if p:
                side.append(f'<a class="sidebar-link{cls}" href="#{p["slug"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span><span class="sl-leader"></span></a>')
                rows.append(f'<div class="ce-row{cls}"><span class="ce-num">{num}</span><a class="ce-title" href="#{p["slug"]}">{html.escape(p["title"])}</a>{spine_mark}</div>')
            else:
                side.append(f'<span class="sidebar-link is-absent{cls}" title="{ui["not_drafted"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span></span>')
                rows.append(f'<div class="ce-row is-absent{cls}"><span class="ce-num">{num}</span><span class="ce-title">{html.escape(ctitle)}</span>{spine_mark}<span class="ce-pg">{ui["not_drafted"]}</span></div>')
    by_letter = {str(p["appendix"]): p for p in pages if p.get("appendix")}
    if st.get("appendices"):
        side.append(f'<div class="sb-part">{html.escape(ui["appendices"])}</div>')
        rows.append(f'<div class="ce-part">{html.escape(ui["appendices"])}</div>')
        for letter, atitle in st["appendices"]:
            p = by_letter.get(letter)
            label = f"{letter} · {html.escape(p['title'] if p else atitle, quote=False)}"
            if p:
                side.append(f'<a class="sidebar-link" href="#{p["slug"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span><span class="sl-leader"></span></a>')
                rows.append(f'<div class="ce-row"><span class="ce-num">{letter}</span><a class="ce-title" href="#{p["slug"]}">{html.escape(p["title"])}</a></div>')
            else:
                side.append(f'<span class="sidebar-link is-absent" title="{ui["not_drafted"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span></span>')
                rows.append(f'<div class="ce-row is-absent"><span class="ce-num">{letter}</span><span class="ce-title">{html.escape(atitle)}</span><span class="ce-pg">{ui["not_drafted"]}</span></div>')
    spine_btn = (f'<div class="spine-switch" role="group" aria-label="{html.escape(ui["spine_group"])}">'
                 f'<button type="button" class="spine-opt" data-spine="0" aria-pressed="true">{html.escape(ui["opt_all"])}</button>'
                 f'<button type="button" class="spine-opt" data-spine="1" aria-pressed="false">{html.escape(ui["opt_spine"].format(n=len(st["spine"])))}</button>'
                 f'</div>')

    overview = f"""<!-- ============ OVERVIEW VIEW ============ -->
<div class="view view-overview active" id="viewOverview">
<div class="overview-container">

<section class="book-hero">
<div class="hero-cover">
<div class="cover-wrap">{cover_html(ui)}<button type="button" class="cover-zoom" aria-label="{html.escape(ui["zoom_label"])}" title="{html.escape(ui["zoom_label"])}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><line x1="15.5" y1="15.5" x2="21" y2="21"/><line x1="10.5" y1="7.5" x2="10.5" y2="13.5"/><line x1="7.5" y1="10.5" x2="13.5" y2="10.5"/></svg></button></div>
</div>
<div class="cover-lightbox" id="coverLightbox" role="dialog" aria-modal="true" aria-label="{html.escape(ui["zoom_label"])}" hidden><button type="button" class="cover-close" aria-label="{html.escape(ui["close_label"])}">&times;</button><img alt="{html.escape(ui["cover_alt"])}"></div>
<script>{COVER_ZOOM_JS}</script>
<div class="hero-info">
<p class="hero-series">{html.escape(st["series"])}</p>
<h1 class="hero-title">{html.escape(st["title"])}</h1>
<p class="hero-subtitle">{html.escape(st["subtitle"])}</p>
<p class="hero-tagline">{html.escape(st["tagline"])}</p>
<p class="hero-author">Mansour Ayouni</p>
{spine_btn}
<div class="view-mode-toggle" role="group" aria-label="View mode">
<button class="vm-list" id="vmList" aria-label="List view">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><circle cx="4" cy="6" r="1.2"/><circle cx="4" cy="12" r="1.2"/><circle cx="4" cy="18" r="1.2"/></svg>
</button>
<button class="vm-grid active" id="vmGrid" aria-label="Grid view">
<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>
</button>
</div>
</div>
</section>

<section class="chapter-grid" id="chapterGrid">
{chr(10).join(cards)}
</section>

<section class="overview-contents">
<h2>{ui["contents"]}</h2>
<div class="contents-listing">
{chr(10).join(rows)}
</div>
</section>

</div><!-- /overview-container -->
</div><!-- /view-overview -->

<!-- ============ CHAPTER VIEW ============ -->
<div class="view view-chapter" id="viewChapter">
<div class="chapter-container">

<aside class="chapter-sidebar" id="chapterSidebar">
<h2 class="sidebar-book-title"><a href="#">{html.escape(st["title"])}</a></h2>
{spine_btn}
<nav class="sidebar-nav" id="sidebarNav">
{chr(10).join(side)}
</nav>
</aside>

<main class="chapter-main">

{chr(10).join(articles)}

<nav class="ch-nav" id="chapterNav" aria-label="Chapter navigation">
<a class="ch-nav-btn" id="cnPrev" href="#">
<span class="cnb-dir">{ui["prev"]}</span>
<span class="cnb-title">—</span>
</a>
<a class="ch-nav-btn next" id="cnNext" href="#">
<span class="cnb-dir">{ui["next"]}</span>
<span class="cnb-title">—</span>
</a>
</nav>

</main>

</div><!-- /chapter-container -->
</div><!-- /view-chapter -->

"""
    return head + overview + script


def main():
    if "--render-only" not in sys.argv:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "book_run.py")])
        if r.returncode not in (0, 1):
            raise SystemExit(f"book_run.py could not run (exit {r.returncode})")
    built = stamp(now())
    st = structure()
    runs = load_json("book-run.json", {})
    snap, _ = snapshot((runs.get("run", {}).get("zayn") or {}).get("commit"))
    law = law_data(snap)
    law["closed_lists"] = closed_lists(snap)
    law["fields_by_kind"] = fields_by_kind(snap)
    law["pins"] = pin_files(snap)
    law["ladder"], law["instruments"] = ladder(snap)
    law["spec_version"] = (runs.get("run", {}).get("law") or {}).get("lang.version")
    en_src = sources("en")
    errors = []

    errors.extend(check_type_scale())
    stale_keys = set()
    for path, m, body in en_src:
        key = f"en/{path.stem}"
        r = runs.get("chapters", {}).get(key)
        hashes = [b["hash"] for b in code_blocks(body)]
        if hashes and (not r or [b.get("hash") for b in r["blocks"]] != hashes):
            stale_keys.add(key); errors.append(f"{key}: its declarations changed since their last run (or never ran)")
        elif r and r["runnable"] and r["kept"] < r["runnable"]:
            errors.append(f"{key}: {r['kept']} of {r['runnable']} declarations kept their promise")
        for c in (r or {}).get("court", []):
            if not c.get("exists"):
                errors.append(f"{key}: the fixture {c['file']} is not in the suite at the pin")
            elif not c.get("pass"):
                errors.append(f"{key}: the fixture {c['file']} answers {c.get('got_ids')}, the manifest expects {c.get('expect_ids')}")
        if m.get("status", "draft") not in STAGES:
            errors.append(f"{key}: status '{m.get('status')}' is not one of {STAGES}")

    pages = build_pages(st, en_src, runs, law, UI["en"], errors)
    page = render_reader(st, pages, runs, stale_keys)
    left = check_colours(page)
    if left:
        errors.append(f"en/index.html: colours outside the variables: {left}")
    for word in ("substrate",):
        if word in page.lower():
            errors.append(f"en/index.html: the word '{word}' appears")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page, encoding="utf-8", newline="\n")
    (ROOT / "index.html").write_text('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
                                     '<meta http-equiv="refresh" content="0; url=en/index.html"><title>Zayn — AYOUNI</title></head>'
                                     '<body><a href="en/index.html">Zayn</a></body></html>\n', encoding="utf-8", newline="\n")
    print(f"built {built}: en/index.html ({len(page):,} characters), {len(pages)} page(s)")
    if errors:
        print("BUILD FAILED:\n  " + "\n  ".join(dict.fromkeys(errors)))
        sys.exit(1)
    print("build passed")


if __name__ == "__main__":
    main()
