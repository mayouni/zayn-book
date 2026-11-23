# CLAUDE.md: Zayn (the book)

**Read this first.** This folder holds the Zayn book, the third of the AYOUNI books (AYOUNI Press). It is a local git repository with
no remote. Nothing here is pushed and nothing is public: creating a public repository, a first push and publication are the author's
acts, prepared by the house desk and done on his explicit "go".

```
Zayn
UI Governance in the Agentic Era
Declare what a user is doing. The law refuses the rest.
```

**Author:** Mansour Ayouni · **Imprint:** AYOUNI · **Series:** third of the AYOUNI books, after *Softanza* (`../softanza-book/`) and
*Refinement-Oriented Programming* (`../refinement-book/`). The title block is the author's ruling of 2026-11-21 (`DECISIONS.md`, TITLE-01).

## The contract

`D:\GitHub\softanza\prompts\72-zayn-book.md`, sections 0 to K. Read it whole before touching a file. Where it and a repository
disagree, the repository is right: report the divergence, do not force the prompt. The author's rulings are in `DECISIONS.md` and
override anything below that disagrees. The house's rules (`../../CLAUDE.md`, `../../OPEN-BOOK.md`) bind this folder.

## What the book is, and who reads first

The site shows what Zayn is; the book says why, and it is the reference a practitioner keeps open on how an interface is held to
rules when AI models draw interfaces and AI agents use them. **The designer who does not program reads first** (READER-01). Six doors:
the designer who does not program, the programmer, the decision-maker who commissions software, the builder of tools, the educator,
the AI agent that reads the book as data.

## The outline (OUTLINE-01)

The author's ten parts, in his order: I The Deterioration, II The Heritage, III The Inversion, IV The Expression, V The Senses,
VI The Readers, VII The Law, VIII The Commons, IX Under Generation, X In Practice. About 26 chapters of 2,000 to 3,000 words;
appendices A to H generated at build; the preface last, and his. The contents as data: `src/structure.yaml`. Chapter titles and the
spine there are working proposals until he rules (TITLES-01).

## The shape of a chapter (SHAPE-01, PLATE-01)

Front matter: `id`, `part`, `number`, `title`, `stage` (`built`, `designed`, `next`: carried from data and code, never from
documents), `status` (`draft`; only the author moves a page, HOUSE-18), `research`, `fixtures` (the court: fixtures of Zayn's
conformance suite, by name). Then, in order, with these headings reused exactly:

1. an opening in the first person that says what the chapter does, in a few sentences; its first sentence says what the subject is;
2. `## The field`: the field read at its sources, each in `research/FIELD.md` with the date of the reading;
3. `## The principle`: one bold sentence, then what it means;
4. sections that show a declaration, run it, quote the verifier's answer and read it, the offending version before the lawful one;
   titled freely, six words at most;
5. `## What I refused`: from the docket, the ledger and the decisions of the Zayn repository, never invented;
6. `## The court`: the fixtures that prove the chapter; the build runs each against the suite's manifest and prints the box;
7. `## Where the field leads`: the loss printed beside the win;
8. `## Where it stands`: Built, Designed, Next from the front matter, then the claim's true size in affirmative sentences;
9. `## In your hands`: a real defect, a declaration the reader repairs, in a `zayn exercise` fence;
10. a closing bridge to the next chapter, never a summary.

**The plate.** A declaration never stands alone. `::: plate <title>` … `:::` holds the ```` ```zayn ```` fence, then a line
`In words: …` that says what the declaration states for the reader who does not program, then where it helps a ```` ```sketch ````
fence (`title`, `say`, `control`, `missing: Label | Rule N`, `restored: Label | Rule N`, `caption`). The build adds the verdict, the
exit code and the report from the run. A fence's info string holds a file name (`payments.zayn`), `level=N`, and the flags
`exercise` and `envelope`.

**The promise (RUN-01).** `//--> CODE name` for each finding the declaration must get, `//--> clean` for none, at the foot of the
fence. **Numbers and the law's words (TOKEN-01).** A count is `{{n:key}}` (the keys are in `tools/book_common.py`, `law_facts`);
`{{rule:79}}` and `{{right:reverse}}` print a card from the law's data. Never type a count, a rule's title or a right's sentence.

## The evidence and the run

- Zayn is pinned at its release v0.2.0, commit `adaecc271dd68e10690eb0166ccb2b1f5d8d1528` (PIN-01; K-11 open). The tag is on GitHub;
  read by the commit's sha. `tools/book_common.py` exports it once into `.cache/zayn-adaecc271/` with `git archive`.
- **Never edit `D:\GitHub\zayn`, never run from its working tree, never run `zig`.** The data files and the run are the authority
  for every number: a README of that repository is never a source of a count.
- `python tools/build_book.py` runs every declaration through the reference verifier of the snapshot (`node
  .cache/zayn-<sha>/tools/zayn/cli.js check <file> --level N`), runs the court, writes `data/book-run.json` and `en/index.html`, and
  fails on a broken promise or a broken shape. No output is stored in a source file.
- Research per chapter in `research/chNN.md`, written from the record before the chapter, every block probed against the snapshot.
- What runs only in a browser (the audit of the painted page) is shown from a recorded run, with its date, widths and culture.
- To look at the reader: the preview server `zayn-book` (the house's local `.claude/launch.json`, port 8740).

## The voice (the AYOUNI Writing Framework, `../../writing-framework/FRAMEWORK.md`, version 0.6)

First person; "you" is the reader with a declaration open; the tool is "it"; a question is a beat answered on the page; an
exclamation only after a run or a reveal, one or two per thousand words; a long sentence, then a short verdict; the colon, not the
dash; plain words a non-native reader parses; one metaphor at a time. A title is six words at most and names its subject; the first
sentence under a title says what the thing is. No particular (name, date, place, memory, sentence of the author's) that the record
or the author did not give: a hole is `[AUTHOR: …]`, three per chapter at most. The stake of a chapter (C10) and the defect left to
the reader (C2) are the author's: propose, mark, never compose his conviction. The record's own words are evidence, not prose to
copy. The lint: `python ../../writing-framework/tools/style_lint.py src/en --strict`. Then a fresh verifier
(`briefs/fresh-verifier.md`, report in `research/verify/`), the voice reader (`briefs/voice-reader.md`, `research/voice/`), the
fixer (`briefs/fixer.md`), and fresh readers by door (`research/read/`), who answer "ready" or "not ready" with the sentence that
stopped them.

## The vocabulary

- **The name is Zayn.** StzZui appears once in the book, where it says what Zayn is inside Softanza. The language of the first book
  is Haro; the former host language is named nowhere. Two products of the estate are never named (the contract's section F); the
  Zayn record names both, and those names stay out of every page.
- **The subject of Zayn is the user, and a user is a person or an AI agent.** "Person" alone only where a statement is true of
  people alone. "AI model" and "AI agent" where the bare word is ambiguous.
- **"The law"** is the interface constitution and nothing wider. **"The court"** is what proves a chapter: the conformance suite and
  the run. Map a ruling metaphor once, term by term, where it starts (`research/METAPHORS.md`, opened in phase 2).
- One thing, one word, fixed as fresh readers read the chapters (the pilot's readers found six words for a finding and three for
  the drawn interface): **a finding** is one entry of the verifier's report; **a refusal** is a finding that is an error;
  **a diagnostic** is a kind of finding in the contract, with its code; **the drawing** is what a medium shows of a declaration, and
  **the painted page** is the drawing in a browser.
- "Crafter" is the person, never "maker" outside "decision-maker"; "programmer", never "developer"; no "substrate"; none of the
  framework's listed inflations. Words name states, never people.
- Stage words: **built**, **designed**, **next**. Public pages say what the work is and does at its true size, in affirmative
  sentences; what is unmeasured stays in `research/`, the decisions and the memos.

## Rules that bind

- Stage files by explicit path, never `git add -A`. Commit here, never in the house for this folder. **Never push.** Hand a commit
  over to the house desk in a memo.
- Never move a page beyond `draft`. When the author moves one, send the desk the page id, the stage and his words first.
- Never background a heavy command. A secret appears only as `$env:NAME`. Every stamp is read from the clock.
- What the book needs from another repository is a numbered request (`BOOK-ZAYN-01` onward) in a memo and one line in
  `D:\GitHub\softanza\dashboard\CONCLUSIONS.md`, never an edit. A finding against the law is filed the same way: it is a gift to it.
- Every substantive report to the author is a memo (`../../writing-framework/templates/memo.md`), filed in `sessions/` and appended
  to `D:\GitHub\softanza\memos\YYYY-MM-DD.md`.
- `SITE-LESSONS.md` at the root is written at the end of each part, never before its fresh readers have read (the contract's
  section I). It is for the Zayn session; this book never edits the site.

## Working state

- 2026-11-21: phase 0 (the read) done; the first memo and its three questions (`sessions/2026-11-21-phase-0.md`). The author
  answered the same day: "yes to all three, start phase 1".
- 2026-11-22: phase 1 (the skeleton and the pilot) done: the tools adapted (`FORMAT.md`), the front cover composed, chapter 8
  drafted from `research/ch08.md`, run and built into the reader; read by a fresh verifier, a voice reader and a fresh reader
  from the designer's door, and fixed. Memo: `sessions/2026-11-22-phase-1-pilot.md`. **Stopped for the author's verdict on the
  format before a second chapter.**
- 2026-11-23: the author delegated ("decide on my behalf and continue", DELEGATE-01); the decisions are in `DECISIONS.md`
  (ORDER-01: the book is researched, drafted and read part by part). **Part III is drafted, run and read**: chapters 6 to 9,
  37 declarations and 49 court fixture runs answering as expected; a verifier and a voice reader per chapter, six doors for the
  part; `SITE-LESSONS.md` (Part III); memo `sessions/2026-11-23-part-3.md`. Owed: a second fresh reading of the fixed pages.
  Requests and the rulings that wait for the author: `research/REQUESTS.md` (BOOK-ZAYN-01 to 06).
- What the pilot's and Part III's readers settled, for every chapter to come: every declaration on a page is run, the steps of
  an exercise included ("Cover the report, write the codes you expect, then compare"); a technical word is said in a clause
  at its first use; a sentence of the record is quoted with its source, never reused as prose; a recorded result is told as
  recorded, a run as run; no count is typed (tokens `{{n:…}}`, and the tables `{{families}}`, `{{levels}}`, `{{lists}}`,
  `{{fields}}`, the cards `{{rule:N}}`, `{{right:id}}`, `{{article:id}}`, the run `{{suite:N}}`); a level 3 plate takes
  `level=3 symbols=<name.json>` and a `symbols` fence; no page says how many of the law's rules a machine refuses before the
  author's ruling (the count by citation is in `research/REQUESTS.md`).
- Next: Part VII (chapters 16, 18, 19, then 17), then Parts I, V, IX and X, then II, IV, VI and VIII. For each chapter:
  `research/BRIEF.md` to a research session, the draft, `python tools/build_book.py`, the lint, a fresh verifier and a voice
  reader, then the six doors for the part with `research/READER-BRIEF.md` and `python tools/as_read.py`.
- Session notes: `sessions/YYYY-MM-DD-topic.md`.
