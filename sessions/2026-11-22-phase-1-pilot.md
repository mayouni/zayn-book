# 2026-11-22 · Phase 1: the skeleton and the pilot chapter

```
by:        zayn book session | claude-fable-5-2 | 2026-11-22 00:45
subject:   the Zayn book: phase 1 done, the pilot chapter is built; your verdict on the format
why:       you wrote "yes to all three, start phase 1"
did:
  - recorded your three rulings in DECISIONS.md (TITLE-01, READER-01, OUTLINE-01)
  - adapted the Softanza book's tools to Zayn (FORMAT.md): a snapshot of Zayn at v0.2.0, every declaration run through the reference verifier, the reader in the series' format
  - composed the front cover in the series' design; the jar is cropped and scaled, no pixel repainted
  - drafted chapter 8, "The refusal", from research\ch08.md: 8 plates, 7 declarations run, 7 answered as the page expects; its court, 13 fixtures of the suite, all answer as the manifest expects
  - had it read by three fresh readers and fixed it: a verifier (77 claims: 63 verified, 14 corrected), a voice reader, a designer who does not program ("ready after the items above")
  - read five sources of the field at their pages on 2026-11-21 (research\FIELD.md)
state:
  chapter 8:  draft | run 7 of 7 | court 13 of 13 | fresh readers 3 | lint clean | house voice check passes
  reader:     books\zayn-book\en\index.html, one file; preview http://localhost:8740/en/index.html#ch8-the-refusal
  commit:     b39f8b9, local; nothing pushed, nothing public
waiting:
  - you: the verdict on the format: the plate (declaration, "In words", report, sketch), the rule card, the fixed headings, the cover
  - you: two [AUTHOR] markers in chapter 8: the stake of the chapter, and the defect left to the reader
  - you, K-4: length. Recommended: 60,000 to 75,000 words
  - you, K-5: a French edition. Recommended: yes, after you publish the English pages
  - you, K-6: the story. Recommended: none invented; the spine is your corrections and the site under its own law
  - Zayn session: BOOK-ZAYN-03 (README lines against the data), BOOK-ZAYN-04 (a flow whose act cannot be undone), BOOK-ZAYN-05 (a rule's tier against the diagnostics that cite it)
  - house desk: templates\LICENSE.md and the Softanza reader carry the colophon line from before HOUSE-23; I added one preview entry, zayn-book, to the house's local .claude\launch.json
next:
  - you:     the verdict, then the three answers
  - me:      phase 2, the research (the field whole, a brief per chapter), on your verdict; no second chapter before it
note:      BOOK-ZAYN-05 touches the book's strongest page: the 40 diagnostics cite 14 rules, and the law files 7 of those under judgment. Chapter 17 needs the law's own answer first.
```

The memo above is the message sent to the author. What follows is the record behind it.

## What phase 1 wrote (commit b39f8b9)

| File | What it is |
|---|---|
| `DECISIONS.md` | the author's four rulings with his words; fourteen choices taken inside the contract, each with what he may still rule |
| `CLAUDE.md` | the book's rules: the framework version (0.6), the shape of a chapter, the plate, the stage words, the pin, the vocabulary |
| `FORMAT.md`, `README.md`, `LICENSE.md` | the lineage of the reader and the tools, file by file; how to build; the licence from the house's template |
| `src/structure.yaml` | the title block, the ten parts, 26 working chapter titles, the spine proposed, the appendices |
| `tools/` | `book_common.py`, `book_judge.py`, `book_run.py`, `build_book.py`, `make_cover.py`, each with its lineage in its header |
| `reader/`, `assets/` | the series' shell and logo sprite, the typefaces, the logo, the jar, the composed front cover |
| `research/FIELD.md`, `research/ch08.md` | the field's five sources read on 2026-11-21; the brief of the pilot, its probes, what the readers changed |
| `research/verify/`, `voice/`, `read/` | the three fresh readers' reports, as they wrote them |
| `src/en/08-the-refusal.md`, `data/book-run.json`, `en/index.html` | the chapter, its run, the reader |

## The pipeline, proved end to end

1. `tools/book_common.py` exports Zayn at commit `adaecc271dd68e10690eb0166ccb2b1f5d8d1528` into `.cache/` (git archive; nothing
   is run from the Zayn working tree, and nothing was written in that repository).
2. `tools/book_run.py` writes each declaration of a chapter to a file and gives it to `tools/zayn/cli.js` of the snapshot under
   Node v22.20.0, once with `--json` (the findings judged) and once plain (the report printed). A declaration's `//-->` lines
   state the answer its page expects. The chapter's court is run too: each fixture named in the front matter, against the
   suite's manifest.
3. `tools/build_book.py` fills the counts (`{{n:…}}`) and the cards of the law (`{{rule:79}}`, `{{right:reverse}}`) from the data
   at the pin, renders the plates, checks the chapter's shape, the colours and the type scale, and writes one reader file.
4. The run of 2026-11-22 00:21: chapter 8, 7 of 7 declarations, 13 of 13 fixtures. The style lint passes (`--strict`); the
   house's voice check on the reader finds 0 phrases. The reader was opened in the browser: the overview, the chapter, the
   plates, the cards, the court, the invitation and the colophon line word for word; at a phone's width nothing overflows; the
   dark theme switches every colour.

## What the three readers found, in one line each

- **The verifier** (`research/verify/ch08.md`): three statements were wrong (a count of fields; "adding UNDO quiets the verifier";
  a fixture said to be the suite's while it lacked one line), eight said more than the evidence, three had no evidence within
  reach. Each was fixed by the smallest edit, or backed by a run (the exercise's accepted form is now plate 8.8).
- **The voice reader** (`research/voice/ch08.md`): the page gave the first refusal a full reading and the others none; a
  refusal's parts were counted three ways; one refusal in "What I refused" had no run in reach. Fixed; that refusal is cut.
- **The designer who does not program** (`research/read/ch08-designer.md`): "ready after the items above". The sentence that
  stopped the reader most: "a flow of two steps has no exit". Verifier, law, exit code and fixture were used before they were
  said; "promise" had two senses; plate 8.3 had no repair. Fixed; the clearest plate was the repair (8.2).

A second reading by fresh readers of the fixed page is owed before the page is called read by them: the reports above are on
the first draft.

## The requests, in full

To the **Zayn session** (it orders the Zayn desk); the book edited nothing there.

- **BOOK-ZAYN-01** (open since phase 0): the tag `v0.2.0` is on GitHub and absent from the local clone.
- **BOOK-ZAYN-02** (open since phase 0): `README.md:37` names release 0.1.0.
- **BOOK-ZAYN-03, texts against the data or the tree.** (a) `conformance/README.md:114`, `tools/zayn/README.md:202` and
  `doc/language/README.md:159` link `doc/decisions/M3-the-zayn-verifier.md`; the file is `M3-the-zane-verifier.md`.
  (b) `tools/zayn/README.md:20` shows the citation in brackets on a finding's first line; the run prints it on its own line.
  (c) `tools/zayn/README.md:10` names version 0.1.0. (d) `conformance/README.md:46-51` gives 6, 20 and 4 fixtures per level; the
  manifest holds 12, 60 and 5. (e) `conformance/README.md:36` says the id "carries the rule number"; the contract binds a rule
  to 20 of its 40 ids.
- **BOOK-ZAYN-04, a flow whose act cannot be undone.** The second half of the action family's invariant ("or declares why it
  cannot") is expressible on an `INTERACTION` only. A `WIZARD` or an `INTENT_FLOW` that acts must keep `UNDO`; `ROLE` on it is
  `ROLE_MISPLACED`; an `INTERACTION` with `ROLE irreversible` beside it does not lift `MISSING_UNDO` from the flow; the clean
  form moves `ACT` out of the flow, and no field ties the interaction back (`INTENT_FLOW close_account` pointing at a `WIZARD`
  is `UNRESOLVED_INTENT_FLOW`). Probed on 2026-11-21; the runs are in `research/ch08.md`.
- **BOOK-ZAYN-05, a rule's tier and the diagnostics that cite it.** The 40 diagnostics cite 14 rules. In `rules.json` those
  are: `machine` 5 (38, 79, 82, 83, 130), `tool` 1 (116), `machine-later` 1 (26, cited by `MISSING_CANCEL`), `judgment` 7 (16,
  51, 53, 98, 112, 118, 119). Six `machine` rules are cited by no diagnostic (1, 44, 60, 80, 107, 127). A reader who opens
  Rule 16, *Intentional Clicks*, from `SELECT_ACT_COLLAPSE` finds a rule about what a control looks like; the sentence refused
  is Article II's. And Rule 79's reason speaks against confirmation while `SELECT_ACT_COLLAPSE` asks for `CONFIRM`: a designer
  asked which the law wants. Chapter 17 prints which rule sits on which rung.

To the **house desk**; the book edited no tracked file of the house.

- `books/zayn-book` is untracked in the house (as told in phase 0). The proposal to carry on the author's go: `mayouni/zayn-book`,
  a submodule, slug `zayn`, readers at `/books/zayn/en/`.
- `templates/LICENSE.md` ends on the colophon line "code under the library's licence", and the Softanza reader prints the same;
  `OPEN-BOOK.md` line 28 holds the line of HOUSE-23, which this book prints.
- One entry, `zayn-book` (port 8740), was added to `D:\GitHub\ayouni\.claude\launch.json`, the house's local preview file, which
  git ignores. It is the one file outside this folder the session wrote in the house; say the word and it is removed.

## For the author, beyond the three questions

- **The "I" of "What I refused".** Each of its three refusals rests on a file of the Zayn record (the suite's fixture, the
  conformance README, the specification's note on his ruling of 2026-11-02). They are written in his first person; he strikes
  any that is not his.
- **One sentence is my reading, not the record's**: "The verb `CONFIRM` names the user's intent to commit, whatever control
  carries it." It answers the designer's question; he keeps it or gives his own.
- **Names in "The field"** (FIELD-01): ESLint, WCAG 2.2, axe-core, eslint-plugin-jsx-a11y and Jakob Nielsen are named as sources,
  each read at its page. K-9 is about products where the book tells the deterioration; he may rule on both together.
- **A rule's `evidence` field** is not printed by the rule card. Some name projects of the estate. What Appendix A prints of
  them is his call.
- **The executable** was not downloaded (RUN-02): the pages run on the reference. On his word, the book also runs
  `zayn-0.2.0-x86_64-windows.exe` (2,803,712 bytes, from the release page) and prints both.
- **The jar**: is there a larger original, for print? The cover scales the 1024 x 1535 file 1.23 times.
- **Still to ask, three at a time**: K-7 (trim), K-8 (the names Zui and Zane), K-9, K-10 (the live verifier in the reader), K-11
  (the pin), K-12 (the road-signage chapter), K-13 (the jar).

## What the pilot did not exercise

The status page and the agents' form (`book.json`, `llms-book.txt`: phase 5), the PDF (phase 6; the print icon already points
at `../book.pdf`), a figure pair drawn as an image, a level 3 declaration with a symbol table, a recorded run of the audit of
the painted page, an appendix generated from the data. Each comes with the chapter that needs it.
