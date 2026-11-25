# FORMAT: what this book's reader and tools took from the first two books, file by file

The contract (section D) asks that the Softanza book's tools be copied and adapted, with the lineage in each header, as the
Softanza book's own `FORMAT.md` did for the Refinement book. This file is that record. Written 2026-11-21, phase 1.

## The sources

| Book file | Taken from | How |
|---|---|---|
| `reader/shell.refine.html` | the Softanza book's `reader/shell.refine.html` at softanza-book a9e3812, which is the Refinement book's `web/shell.template.html` as it stood on 2026-10-08 (sha256 `58d6be2e…4ca29df4`, the hash the Softanza book's `FORMAT.md` records) | copied unchanged; sha256 `58d6be2eba53d97b1d2c3de7374d7ba68a3c1b6b1e553030889374bd4ca29df4` |
| `reader/logo-sprite.html` | the Softanza book's `reader/logo-sprite.html` (the AYOUNI logo as an SVG symbol, with its red dot, HOUSE-17) | copied unchanged; sha256 `47457781…ccf5152` |
| `assets/fonts/` (three typefaces and their OFL files) | the Softanza book's `assets/fonts/` | copied unchanged |
| `assets/cover/source/ayouni-logo.svg`, `.png` | the house's `site-src/assets/ayouni-logo.svg` (the same sha256, `d8faf2a9…417e21ab4`) and the Softanza book's rasterised copy | copied unchanged |
| `assets/cover/source/jar.webp` | `D:\GitHub\softanza\vision\zayn-book\cover-art.webp`, the image the author supplied | copied unchanged; sha256 `88dde241d7b208784f304db2ca815a291e0b293e972a8c310a3486dec456253a`, checked by `tools/make_cover.py` at every run |
| `tools/book_common.py` | the Softanza book's `tools/book_common.py` | the sources, the fences, the clock and the data files kept; the library snapshot replaced by a snapshot of Zayn at the pin; `law_data` and `law_facts` added |
| `tools/book_judge.py` | the Softanza book's `tools/book_judge.py` (the words under a block) | the judge is new: a declaration promises findings, compared as the conformance suite compares them |
| `tools/book_run.py` | the Softanza book's `tools/book_run.py` | one record per block, a verdict per block, exit 1 on a broken promise kept; the runtime is Zayn's reference verifier under Node; the chapter's court is run against the suite's manifest |
| `tools/build_book.py` | the Softanza book's `tools/build_book.py` | the shell edits, the colour sets, the type scale and its check, the Markdown reading, the navigation, the proof line, the banner and the invitation kept; the additions below |
| `tools/make_cover.py` | the Softanza book's `tools/make_cover.py`, function `make` | the same design, positions, faces and sizes; the figure is the jar |

**Not taken in phase 1, and when each comes:** `book_guards.py` (this book's court is the conformance suite, run by `book_run.py`);
`book_audit.py` and `release.py` (phase 4, with the first verified part); `book_schema.py`, the status page and the agents' files
(`book.json`, `llms-book.txt`, `agents/`: phase 5); `print_book.py` and `epub_book.py` (phase 6, the press edition); `check_fr.py`
(a French edition, if ruled). The back cover is drawn by `make_back` of the cover tool and turns in the reader (BACK-01).

## What is the same as the first two books

The page (an overview with the cover and the title block, then the chapters as cards or as a list; a chapter view with the whole
contents in a sidebar); hash routing, previous and next, the arrow keys; EB Garamond for reading at 24px with seven steps, Inter
for headings and labels; search; light and dark themes with every colour behind a variable, checked at build; the type scale
(`TYPE` in `tools/build_book.py`) with its check; the page stage and its banner (Draft, In review, Published); the proof line under
the title; the AYOUNI logo once, in the header, linking home; the print icon opening the book's PDF; the standing invitation and the
colophon line at the end of the last chapter, word for word from the house's `OPEN-BOOK.md`.

## What this book adds

| Addition | Where | Why |
|---|---|---|
| the **plate**: declaration, "In words", verdict and exit code, the report from the run, a sketch; one numbered figure | `convert_body`, `code_cell`; `::: plate` in a source | the author's rulings for the Zayn site (2026-11-14): never two blocks in a row; an "In words" sentence beside every declaration |
| the declaration's lines numbered, and the line a finding cites marked | `numbered` | the site's plate (Zayn `doc/design/DESIGN-SYSTEM.md`) |
| the **sketch**, labelled "Illustration", missing controls dashed with their rule, restored ones with theirs | `sketch_html`; ```` ```sketch ```` in a source | the site's sketch: Zayn checks the declaration and does not draw the screen |
| the **rule card** and the **right card**, printed from `constitution/rules.json` at the pin | `rule_card`, `right_card`; `{{rule:79}}`, `{{right:reverse}}` | no word of the law is typed in a page |
| every count as a **token** read at build | `fill_tokens`; `{{n:diag.total}}` | numbers are read, never composed; an unread number is `null` and fails the build |
| the **court** as fixtures run against the suite's manifest | `book_run.run_court`, `court_box`; `fixtures:` in the front matter | the book's court is the conformance suite |
| the chapter's **fixed headings**, checked | `check_shape` | the shape is the same in every chapter and language |
| four colour variables (`--code-field`, `--code-verb`, `--code-cited`, `--code-cited-rule`) | `LIGHT`, `DARK` | the plate's tones, behind variables like every other colour |

## What changed in the shell, and why

The Softanza book's named edits, each asserted to apply exactly once, with three differences: the title and the breadcrumb say Zayn;
the keys kept in the browser are `zayn-theme` and `zayn-spine`; the header has no language toggle, because this book has one language
until a French edition is ruled.
