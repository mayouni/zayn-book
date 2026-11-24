# Interfaces Under Law: the Zayn book

*Interfaces Under Law · UI governance for people and AI agents, using the Zayn language · Declare what a user is doing. The law refuses the rest.* By Mansour Ayouni. The third of the
AYOUNI books.

This book runs. Every Zayn declaration in it is checked by Zayn's reference verifier at a named commit and judged against the
findings it promises on its `//-->` lines. A chapter whose declarations do not all keep their promise fails the build, and every
report a page prints is the one the run gave.

## Build

```bash
python tools/build_book.py
```

This runs every declaration and every court fixture (`tools/book_run.py`), then writes `en/index.html`, one self-contained reader.
It exits 1 when a promise is broken, a declaration changed since its last run, a fixture answers otherwise than the suite's manifest
expects, a chapter lacks one of its fixed headings, a count cannot be read from the data, or a colour sits outside the variables.
To re-render from `data/` without running: `python tools/build_book.py --render-only`.

The first run exports Zayn at the pinned commit into `.cache/` with `git archive` (4.6 MB, ignored by git). It needs Python 3 with
PyYAML and Pillow, `git`, `tar`, Node, and the Zayn repository at `D:/GitHub/zayn` (`tools/book_common.py`, `ZAYN_REPO` and `PIN`).
The cover: `python tools/make_cover.py`. The style lint: `python ../../writing-framework/tools/style_lint.py src/en --strict`.

## Layout

| Path | What |
|---|---|
| `src/structure.yaml` | the contents: the title block, the ten parts, the chapters, the spine |
| `src/en/NN-slug.md` | one chapter per file, with front matter (`stage`, `status`, `research`, `fixtures`) |
| `research/` | `FIELD.md` (the field, read at its sources, with the date of each reading); `chNN.md` per chapter; `verify/`, `voice/`, `read/` for the fresh readers' reports |
| `data/book-run.json` | what each declaration got from the verifier, and the court; written by the run, read by the build |
| `tools/` | `book_common.py`, `book_judge.py`, `book_run.py`, `build_book.py`, `make_cover.py` |
| `reader/`, `assets/` | the series' reader shell, the logo, the typefaces, the cover and its sources |
| `en/index.html`, `index.html` | the built reader |
| `sessions/` | the memos, one per phase or topic |
| `CLAUDE.md`, `DECISIONS.md`, `FORMAT.md`, `LICENSE.md` | the book's rules, its decisions, the lineage of its format, its licence |

## Stage

Every page is a **Draft**: written, its declarations run and judged. Only the author moves a page to **In review** or **Published**.
The edition is a proof copy until every page is published.
