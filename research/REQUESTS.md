# Requests the book has filed, and where each stands

What the book needs from another repository is a numbered request, never an edit. Each is filed in a memo (`sessions/`) and in one
line of `D:\GitHub\softanza\dashboard\CONCLUSIONS.md`. This file keeps their state in one place. A status is written with its date
and with who gave it; the book checks what it can check itself, read only, and says so.

## To the Zayn session (it orders the Zayn desk)

| Id | Filed | What | State |
|---|---|---|---|
| BOOK-ZAYN-01 | 2026-11-21 | The tag `v0.2.0` was on GitHub and absent from the local clone | **Done 2026-11-21 22:21** (the Zayn session). Checked by the book on 2026-11-22 19:25: `git -C D:\GitHub\zayn rev-parse v0.2.0^{commit}` answers `adaecc271dd68e10690eb0166ccb2b1f5d8d1528`. The book goes on reading by the commit's sha, which the tag names |
| BOOK-ZAYN-02 | 2026-11-21 | `README.md:37` names release 0.1.0 | **Committed in the Zayn repository** (`4a91b9d`, and the Audit page's line in `32e6d33`), verified by the Zayn session, waiting for the author's push (its message of 2026-11-23 09:26). Wider than filed: `site/tour.html:207,216`, `site/ports.html:126` and `tools/zayn/README.md:10-12` named it too. The pin keeps its lines: the fix is on `main`, after the tag |
| BOOK-ZAYN-03 | 2026-11-22 | README lines against the data or the tree, parts (a) to (e) | **Committed with 02**, verified, waiting for the push. One more file carried the dead link of part (a): `ROADMAP.md:25` |
| BOOK-ZAYN-04 | 2026-11-22 | A flow whose act cannot be undone has no form of its own | **Answered 2026-11-23 09:26**: the four readings confirmed by the Zayn desk and by the Zayn session, on the reference and on the built command. One correction, one addition (below). A ruling on the language waits for the author: LANG-FLOW-REFERENCE-01 |
| BOOK-ZAYN-05 | 2026-11-22 | A rule's tier and the diagnostics that cite it tell two stories | **Answered 2026-11-23 09:26**: the figures stand, and a count by citation is given (below). Three rulings on the law wait for the author: LAW-TIER-REFUSED-01, LAW-TIER-CHECK-01, LAW-SELECT-CONFIRM-01 |
| BOOK-ZAYN-06 | 2026-11-23 | Ten findings of Part III's research, parts (a) to (j), below | **Answered 2026-11-23 19:54** (the Zayn session): all ten confirmed at the pin by the Zayn desk, 27 runs on the reference and on the built command, identical; full text in the Zayn repository's `.central/outbox.md`, NOTE of 2026-11-23 19:34. Six rulings go to the author (below). Part (i)'s texts are rewritten in Zayn's `ce58575`, after the pin |
| BOOK-ZAYN-07 | 2026-11-23 | Findings of Part VII's research and of Part III's second readings, in parts, below | **Answered 2026-11-24**: all ten parts confirmed by the Zayn desk (its NOTE of 2026-11-24 00:47 in the Zayn repository's outbox), checked by the Zayn session (01:14). Five rows are with the author: LAW-MENU-READINGS-01 (a, b), LAW-CONTRACT-BINDINGS-01 (c, found wider: nine bindings cite an article or a right that the cited rule does not hold), GRID-116-PLACEMENT-01 (d), LAW-CORRECTIONS-3171-01 (e, f, g: a correction pass 3.17.1), LAW-ARTICLE-VII-RECURRING-01 (h). (i): the texts outside the law corrected in the Zayn repository after the pin (d01d322, local); (j) confirmed. Chapter 17's findings, owed to this request, are filed as BOOK-ZAYN-09 (u) | Routed by the Zayn session to the desk as ZAYN-LAW-BOOK-READ-03 (2026-11-23 19:54); none of the five rows ruled yet
| BOOK-ZAYN-08 | 2026-11-23 | Findings of the research of Parts I and V, in parts, below | **Filed 2026-11-23**, with the memo of Parts I and V; parts added as chapters 1, 2, 12 and 13 are drafted. Two parts are the open questions that chapters 12 and 13 leave to their reader |
| BOOK-ZAYN-09 | 2026-11-24 | Findings of the research of Part IX, in parts, below | **Answered 2026-11-25**: the Zayn desk's NOTE of 2026-11-25 07:58 (the Zayn repository's outbox, lines 5718 to 5944), checked by the Zayn session against the code. (a) confirmed: the confirmation relayed for BOOK-ZAYN-06 (g) was wrong and is withdrawn. `haro/judge-zayn-court.js` translates from the `.zayn` form to the grammar's, and its output feeds the forged court alone; the verifier reads the original; nothing translates the other way. The desk's probe: 0 of 77 fixtures are sentences of the grammar, 66 of 77 translations are, and the verifier answers `SYNTAX_ERROR` on all 77 translations. The desk withdraws its recommendation for LANG-RECORD-GAPS-01 (c), which rested on the withdrawn line. The other 21 parts are confirmed as stated; of (c), "33 errors" stands in no tracked file of the repository, the desk's own count on one probe file. Texts corrected after the pin, local commits on d01d322, not pushed: 1408405 (a: the pages say which form each reader reads, held by a check FORMS_SAID that found 4 problems before the fix and 0 after), 7e32c0e (h, m, u 8 and 10), 45da235 (g, s, u 15 and 17), 02be560 (r's comments). Ten new rows go to the author, and five parts join rows already with him (table below). The sentences of Part IX that hang on a ruling stay as they are until he rules | Routed by the Zayn session to the desk as ZAYN-LAW-BOOK-READ-04 (2026-11-24 23:30); none of the rows ruled yet |
| BOOK-ZAYN-10 | 2026-11-24 | Findings of the research of Part X, in parts, below | **Filed 2026-11-24**, with the memo of Part X. Two parts are the open questions that chapters 25 and 26 leave to their reader |
| BOOK-ZAYN-11 | 2026-11-26 | Findings of the research and the readings of Part II, in parts, below | **Filed 2026-11-26**, with the memo of Part II |

## What the answers say, and what the book checked at its own pin

**On BOOK-ZAYN-04** (the Zayn session, 2026-11-23):

- `ROLE irreversible` on a `WIZARD` or an `INTENT_FLOW` gives `ROLE_MISPLACED` alone: the misplaced `ROLE` also silences `MISSING_UNDO`
  on that declaration (`tools/zayn/zayn.js:486` reads `ROLE` on any kind). Take the line off and `MISSING_UNDO` appears.
- With an `INTENT_FLOW` (not a `WIZARD`), the act moved into an `INTERACTION` can be tied back by a field `INTENT_FLOW <name>`, and the
  file is clean. So "no field ties the two" holds for a `WIZARD` only: the verifier resolves a reference against `INTENT_FLOW`
  declarations (`zayn.js:414`) while it counts a `WIZARD` a flow for `MISSING_CANCEL` (`zayn.js:133`). Chapter 8's exercise is a
  `WIZARD`, so its sentence stands.

**On BOOK-ZAYN-05** (the Zayn session, 2026-11-23; the lines marked *checked* were read or counted by the book at `adaecc2` on 2026-11-23):

- "A machine refuses 18 of 123 rules" is **not printable**: 18 is the census of two tiers, `machine` 11 and `tool` 7.
- Counted by citation, from files of the pin: instruments that run in the repository refuse **20 of the 123 rules**. The verifier
  refuses 13 from a declaration (16, 26, 51, 53, 79, 82, 83, 98, 112, 116, 118, 119, 130): *checked*, counted from
  `conformance/violations.json` with `LAYOUT_DISPLACEMENT` set aside, which no verifier raises (`manifest.json`, `unfixtured`). The
  audits refuse 8 on a painted page (38, 62, 105, 107, 108, 114, 115, 116), Rule 116 in both: the Zayn session's count, from
  `doc/design/audit/decides.json`, `tools/ui-audit.html` and `doc/design/DESIGN-SYSTEM.md` section 7; the book recounts it when it
  drafts chapter 17.
- The desk splits the 20 into 8 refused "in whole" and 12 "in part". That split is the desk's reading of each rule and is not ruled:
  if printed, it is printed with its definition and whose reading it is. For a chapter: say, for each rule discussed, which clause
  the diagnostic refuses.
- Of the 18 rules marked `machine` or `tool`, 6 are refused by nothing in the repository (1, 44, 60, 80, 127, 129). 8 rules marked
  `judgment` or `machine-later` are refused in part by the verifier (16, 51, 53, 98, 112, 118, 119 and 26).
- What a tier means, in the record: the tier "is honest about which instrument owes the check; it is not a claim that the check runs
  today" (`doc/AMENDMENT-DOCKET.md:591-592`, on Rule 127: *checked*). `site/rules.html:111` says of `machine` that a conforming
  compiler or linter refuses it today, which holds for 4 of the 11: that sentence is not quoted as the meaning of `machine` before
  the ruling.
- Rule 16: `SELECT_ACT_COLLAPSE` enforces Article II's sentence; it reaches Rule 16 only through the forbidden pattern
  `select-silently-acts`. Rule 16's text is about what a control looks like.
- Rule 79 beside `CONFIRM`: the record answers the pilot's designer in `doc/ROLE-DESIGN.md:127-133` (*checked*): "`CONFIRM` in
  `SATISFIES` means *the operator confirms*, which covers both a review step and Rule 79's forbidden modal — and those are the same
  declaration with two renderings", and "Rule 79's dialog clause is a fact about a rendering, not about a declaration". It is a
  design note, not the law or the specification, and no check of the audit reads a confirmation dialog.

## Rulings that wait for the author (outside the book's delegation: the law and the language)

| Id (the Zayn session's) | What it would settle | Recommended there |
|---|---|---|
| LAW-TIER-REFUSED-01 | what a tier means, and what the site prints (09 (u) 1, 2, 9, 11 and 13 join it) | the tier keeps the docket's meaning, and each rule gains a field naming what refuses it today |
| LAW-TIER-CHECK-01 | a check that a tier and the instruments agree | |
| LAW-SELECT-CONFIRM-01 | Rule 16's text, and the meaning of `CONFIRM` in the specification | |
| LANG-FLOW-REFERENCE-01 | a reference may name a `WIZARD`; `MISSING_UNDO` reads `ROLE` on an `INTERACTION` only | |
| LANG-LEVEL-SKIPPED-01 | what a run prints when a level 3 check has no table (BOOK-ZAYN-06 (a)) (09 (u) 7 and (r)'s statuses join it) | |
| LANG-FOREIGN-KIND-01 | a misspelt kind of Zayn, beside another language's kinds, which the verifier ignores by the ruling of 2026-10-31 (06 (b)) | |
| LANG-TRACE-01 | an element traced through `INTENT_FLOW`; the fixture `clean-full.zayn` answers `INTENT_ORPHAN payment_form` at level 3 with that element listed (06 (c)) | |
| LANG-SATISFIES-EMPTY-01 | `SATISFIES` called required and read for presence only (06 (d)) | |
| LANG-LEVEL3-LAWFUL-01 | the level 3 checks from the lawful side: an actor's name never looked up (06 (e)) | |
| LANG-RECORD-GAPS-01 | (a) and (b) three clauses of the families' sentences carried by no diagnostic, `MISSING_CANCEL` filed under continuity; (c) which form a decoder writes; (d) where the election of a surface is stated (06 (f), (g), (j)) |(c), since 2026-11-25: a decoder grammar of the `.zayn` form, written from the verifier's own tables; the alternatives are a translator from the grammar's form into the `.zayn` form, or a verifier that reads both forms (language 1.8). The earlier recommendation is withdrawn with the line it rested on |
| LAW-MENU-READINGS-01 | a section with entries and no `TARGET` under a bar; a child label that begins with its parent's whole label (BOOK-ZAYN-07 (a), (b)) | (a) `MENU_LANDING_NOT_FIRST` refuses it, a reading of the specification; (b) an amendment, 3.18 |
| LAW-CONTRACT-BINDINGS-01 | a finding's article or right against its rule's (07 (c)) (09 (u) 18 joins it) | a check that compares each binding with the law |
| GRID-116-PLACEMENT-01 | Rule 116 on the grid, after v3.16 (07 (d)) | |
| LAW-CORRECTIONS-3171-01 | the law's history against itself, the names corrections did not reach, a design note's count (07 (e), (f), (g)) (09 (u) 6 and 12 join it) | a correction pass 3.17.1, with four questions only the author answers |
| LAW-ARTICLE-VII-RECURRING-01 | how "real and recurring" reads for rules that entered before a defect (07 (h)) | | (09 (i) joins it)
| LANG-SYNTAX-RECOVERY-01 | after a syntax error, the verifier judges the declaration it kept with no field (09 (b)) |  |
| LANG-GRAMMAR-FILE-01 | the smaller differences of the grammar for generation against the language (09 (d)) |  |
| LANG-ROLE-AXES-01 | one role per control, and two axes in the roles (09 (e)) |  |
| LANG-AUTHORITY-OVERLAP-01 | one missing actor gives two errors at level 3 (09 (f)) |  |
| LANG-ACTOR-SEAT-01 | where `ACTOR` may stand (09 (j)) |  |
| LANG-AGENT-PARTIES-01 | provenance with no field; one proposal, two parties, one field; nothing says that a user is an AI agent (09 (k), (n), (o)) |  |
| LAW-AGENT-RIGHTS-01 | the preamble's exception and the right to know; `INVISIBLE_STATE` citing the pattern of active filters for any state (09 (p), (q)) |  |
| LANG-CITES-OBEYED-01 | "cite the rules you obeyed" (09 (l)) |  |
| SUITE-MACHINE-PAIR-01 | the machine medium in the court (09 (t)) |  |
| LANG-MISSING-UNDO-SENTENCE-01 | a finding's sentence against its check (09 (v)) |  |

If they are ruled, they land after the pin; the Zayn session tells the book which release carries them. The six rulings added on 2026-11-23 19:54 each carry the Zayn desk's recommendation, in the outbox note named above.

## What the open rulings hold back in the book, and the sentences a ruling would change

- **The rule card** prints a rule's tier as the law's own word (`machine`, `tool`, `machine-later`, `judgment`) with no gloss, and
  beside it the diagnostics of the contract that cite the rule: both are data of the pin. It said "Enforced by the verifier, on the
  declaration" until 2026-11-23; that was the book's gloss of a tier, and it is gone (LAW-TIER-REFUSED-01).
- **No page states, as settled, how many of the law's rules a machine refuses.** Chapter 17, *The enforcement ladder*, was
  drafted on 2026-11-23 from the count by citation, recounted at the pin by the build itself (`tools/book_common.py`, `ladder`;
  the audits' citations in `data/audit-citations.json`, each checked against its file at build): the verifier's kinds of finding
  cite 13 rules, the audits name 8, Rule 116 is in both, 20 in all. The definition is printed beside every number. **Sentences
  of chapter 17 that a ruling would change:**
  - LAW-TIER-REFUSED-01: the principle, "A tier names the instrument a rule is owed; a citation shows the instrument that
    answers today", and the closing question of the exercise ("should a rule's card say what answers for it today?"). The
    principle rests on the docket's sentence (`doc/AMENDMENT-DOCKET.md:591-592`), which the Zayn session recommends keeping.
  - LAW-TIER-REFUSED-01: "Read the first two columns as the law's filing, and nothing more", and the reading of the tiers
    table ("The rules filed under `judgment` that the verifier cites are rules whose one clause a declaration can state").
  - LAW-TIER-CHECK-01: "Every rule filed under `machine`, and most filed under `tool`, names in a field of its own, `lint`,
    the instrument it is owed" (11 of 11 and 4 of 7, counted at the pin).
  - LAW-SELECT-CONFIRM-01: the plate on Rule 79's dialog clause rests on `doc/ROLE-DESIGN.md:133-134`, a design note.
  - LANG-FLOW-REFERENCE-01 changes none of chapter 17's plates (each `ROLE` sits on an `INTERACTION`).
- **Chapter 8, plate 8.3's reading**: "The verb `CONFIRM` names the user's act of confirming, whatever carries it: a review step and
  a dialog are two drawings of the same declaration." It now rests on `doc/ROLE-DESIGN.md:127-133` (LAW-SELECT-CONFIRM-01 would move
  it into the specification).
- **Chapter 8, the exercise's closing question** ("Should a flow be able to say that its own act cannot be undone?") is
  LANG-FLOW-REFERENCE-01 put to the reader. If the author rules, the exercise follows his ruling.
- **Chapter 6, the exercise's closing question** ("Should an element that names its flow answer through it?") is a finding of
  `research/ch06.md` (section 12, finding 9), filed with Part III's memo.

## To the house desk

| Filed | What | State |
|---|---|---|
| 2026-11-21 | `books/zayn-book` is an untracked local repository in the house; proposed later as `mayouni/zayn-book`, a submodule, slug `zayn`, on the author's go | told; waits for the author |
| 2026-11-22 | `templates/LICENSE.md` and the Softanza reader carry the colophon line from before HOUSE-23 | told; no answer yet |
| 2026-11-22 | One preview entry, `zayn-book` (port 8740), added to the house's local `.claude/launch.json`, which git ignores | told; removed on a word |

## BOOK-ZAYN-06, in parts (filed 2026-11-23 10:17)

Found while researching chapters 6, 7 and 9, each probed on the reference verifier of the pin. A finding against the law or the
language is a gift to it; the book edits nothing there.

- **(a) "clean" at level 3 with no table.** Asked for `--level 3` with no `--symbols`, or with a table that lacks a check's list, the
  report prints `clean … at level 3`, exit 0, and the machine form says `"level": 3` with an empty list. Three texts say "undecidable
  is silence, never a pass" (`research/ch09.md`, section 12, finding 1; `research/ch06.md`, finding 8).
- **(b) A kind outside the ten is passed over whole.** `WIDGET` and `USER` get a warning; any other word (`SCREN`, `BUTTON`, a kind
  in lower case) answers `clean`, with whatever the declaration holds, an act with no undo included (`research/ch07.md`, finding
  F1; `research/ch06.md`, finding 16). Chapter 7's exercise is built on it.
- **(c) The trace of an element reads its own `SATISFIES` only.** A `FORM` bound to a lawful flow by `INTENT_FLOW` is an
  `INTENT_ORPHAN` once an inventory lists it; the grammar's own complete example carries such a form. Two files checked against
  one inventory are each blamed for the other's elements (`research/ch06.md`, findings 9 to 13). Chapter 6's exercise asks it.
- **(d) `SATISFIES` marked required, and its absence.** `SATISFIES []` on a flow passes with no finding; a `WIZARD` with no
  `SATISFIES` is clean (`research/ch06.md`, findings 5 and 6).
- **(e) The level 3 checks from the lawful side.** `HIDDEN_AUTHORITY` uses the list of actors as a switch: `ACTOR visitor`, a name
  the table does not hold, is clean. `INVISIBLE_STATE` is counted file by file. No level 3 fixture has a lawful twin
  (`research/ch09.md`, finding 2). Chapter 9's exercise asks the first.
- **(f) The family invariants and the checks.** Three clauses of the six invariants have no diagnostic; `MISSING_CANCEL` is filed
  under the continuity invariant while `CANCEL` is a verb of action (`research/ch06.md`, findings 19 and 20).
- **(g) The grammar file.** `haro/zayn.gbnf` writes another form of declaration (`AS ( … ) RATIONALE`), which the verifier answers
  with `SYNTAX_ERROR` (`research/ch07.md`, section 12). Chapter 24 needs to know which form a decoder is to produce.
- **(h) The forged evaluator's count.** The site's "55 of 77 agree, 22 named differences" adds 73 judged fixtures and four rows
  written by expectation; the judge counts agreement on the first code, so `multiple-violations.zayn` agrees with one code of four
  (`research/ch09.md`, finding 3). Chapter 9 gives the judged count and the judge's rule.
- **(i) Texts against the data**, listed with their lines in the three research files: among them `doc/language/README.md:106-107`
  ("Every diagnostic it raises cites a numbered rule"; the contract binds a rule to 20 of 40) and `:147-158` ("No implementation is
  at Level 2 today"), and `doc/ARCHITECTURE.md:72` (a count of verbs the specification corrected).
- **(j) A kiosk.** `SURFACE_AS visual` carries `election: elected` in `conformance/media.json`, so the property that makes a kiosk
  (a surface its user did not choose) has no place to be stated (`research/ch07.md`, section 12).

## BOOK-ZAYN-07, in parts (filed 2026-11-23)

Found while researching chapters 16 to 19 and in the second readings of Part III. Each was probed on the reference verifier of
the pin or counted from its files. The book edits nothing in Zayn; a finding against the law is a gift to it.

- **(a) A section that stops saying where it leads passes.** Take a section whose landing page is absent from the level under it
  (`MENU_LANDING_NOT_FIRST`) and delete its `TARGET`: the file is clean. The specification calls an entry with `ENTRIES` and no
  `TARGET` a bar; a labelled child of the main menu with children and no page of its own is judged by neither reading
  (`research/ch18.md`, finding 13). Chapter 18's exercise asks it.
- **(b) The first remark's own example passes its check.** A section labelled "Try" whose first child is labelled "Try here" is
  clean: labels are compared whole (`research/ch19.md`, finding 1; the corpus record of 2026-11-06). Chapter 19's exercise asks
  when a child's label is its parent's name said again.
- **(c) A finding's article is not always its rule's.** `VERB_NOT_CARRIED` cites Rule 82 with Article II; Rule 82 derives from
  Article III and stands in the right to know, which the finding does not cite. `ROLE_ACTS_WITHOUT_CONSEQUENCE` cites Rule 112
  under Article II; the rule derives from Article I. Two findings cite Rule 83 and no right, while a right lists 83
  (`research/ch16.md`, finding 13). Chapter 16's exercise asks it.
- **(d) The amendment of version 3.16 did not reach the grid.** Rule 116 is placed on `visual`; its three diagnostics ignore the
  medium (run on a voice surface, chapter 19). The grid's figures are those of 73 fixtures; the manifest holds 77
  (`research/ch19.md`, findings 2 and 3).
- **(e) The law's history, against itself.** Two entries of the lineage bear version 3.8; `lastUpdated` says 2026-11-08 and the
  last entry is dated 2026-11-12; the docket's header says "three passes" and "v3.13" over seven ruled sections and a law at
  3.17, and `protocol/README.md:127` repeats it in a pinned file; who ruled D6 (Rule 130) is said two ways; the second pass names
  no ruler (`research/ch18.md`, findings 1 to 5).
- **(f) Names the corrections of versions 3.7.2 and 3.7.3 did not reach.** In normative parts of the law: a product in the
  description of Set 30, a store in Rules 79, 83 and 98, the language's former name in Rule 44's `lint` and in `intents.note`;
  in 101 of the 123 `evidence` values, a product or a project; in the lineage, the law's first home and two former names
  (`research/ch16.md`, section 2k and finding 9; `research/ch18.md`, finding 14). One quotation dated 2026-11-08 carries the name
  the language took on 2026-11-12 (`research/ch19.md`, finding 3). The book's copy of the law gives a description in square
  brackets (`DECISIONS.md`, WITHHELD-01).
- **(g) The law's data, read closely.** No right's list names a rule above 102; `invariant` is a mark on a rule, a sentence on a
  family and a field of a diagnostic; `philosophy` names a line of axioms and a section of principles; Rule 5's `avoid` is empty;
  the pattern `decorative-animation` names Rules 1 and 17 and its diagnostic cites Rule 112; two ids keep a former title's words;
  Rule 105's evidence says "Amended in v2.1" where the lineage says canonized (`research/ch16.md`, findings 3 to 11).
- **(h) "Real and recurring."** Article VII asks proof that a harm is real and recurring; Rules 126 and 130 entered without an
  observed defect and say so, and several rules rest on one surface or one measurement. The record is open about each; the
  article's word has no stated reading for them (`research/ch18.md`, finding 8).
- **(i) Texts against the data**, with their lines in the research files: `README.md:13` (every rule above 104 "from a defect an
  AI produced") against the evidence of Rules 125, 126 and 130; `doc/ARCHITECTURE.md:53` (three values of `enforcement`; the file
  holds four); the law's reader ("Visible State (Rule 82)", "cites article numbers", `lint` shown for one tier only, a set's
  numbers printed as a range); `site/rules.html:143-144` (two horizontal levels given to version 3.16); `ROADMAP.md:7` and `:106`;
  a fixture's comment against its run (`verb-not-carried.zayn:8-10`).
- **(j) From Part III's second readings.** The contract's sentence for level 2 says "a single declaration"; several checks of
  that level read the whole file. Article II's sentence lists "recover", which is in no list of verbs.

Chapter 17's findings are added to this request when the chapter is drafted.

## BOOK-ZAYN-08, in parts (filed 2026-11-23)

Found while researching chapters 1, 2, 12 and 13, each probed on the reference verifier of the pin or counted from its files.

- **(a) A medium declared in a file applies to every declaration of it, and `soleCarrier` is read by nothing.** A lamp beside a
  screen in one file refuses the screen's verbs on the lamp; a file whose only medium is a lamp, which the data says should never
  carry a surface alone, passes. Nothing in a declaration says which media carry it together (`research/ch12.md`, finding 2).
  Chapter 12's exercise asks it.
- **(b) "clean" means two things for statuses.** Where a rendering is recorded (screen, sound, voice), clean is decided; elsewhere
  `SIGNAL_UNPERCEIVABLE` has nothing to read, and the report prints the same word (`research/ch12.md`, finding 3).
- **(c) Renderers.** The data records renderings for three media, while `protocol/README.md:186-187` says "Two of the ten media
  have an implementation" (`research/ch12.md`, finding 1).
- **(d) The grid's table and its fixtures.** The understand by `any` cell counts 12 fixtures where `COVERAGE.md:98` prints 8: four
  are Rule 116's menu fixtures, on a cell where Rule 116 is not placed; `COVERAGE.md:363` says D5 showed Rule 79 on voice and
  machine, which its fixtures do not; figures that the ruling of 3 November moved (34 to 35 empty cells) stand in several lines
  (`research/ch13.md`, findings 1 to 3).
- **(e) A rule's finding on a closed cell.** On print, `SELECT_ACT_COLLAPSE` (Rule 16) is raised beside `VERB_NOT_CARRIED` for the
  same verbs, on cells the grid calls closed (`research/ch13.md`, finding 6). Chapter 13's exercise asks what a confirmation is
  for an AI agent on the machine medium.
- **(f) The hand-set placements** are said to be listed in `coverage-placement.json` and are not; "empty" names two things in
  the record (`research/ch13.md`, findings 5 and 10).

## BOOK-ZAYN-09, in parts (filed 2026-11-24)

Found while researching chapters 22, 23 and 24, each probed on the reference verifier of the pin or counted from its files; the
book's build checks the flagged plates of chapter 24 against `haro/zayn.gbnf` itself (`tools/book_common.py`, `gbnf_regex`,
fourteen controls read off the grammar, all as read). A finding against the law or the language is a gift to it.

- **(a) The grammar for generation and the verifier share no file, and the translation runs one way.** Every declaration of
  `haro/zayn.gbnf` needs `AS` after its name and `RATIONALE` after its body, with lists in small letters; the verifier answers
  `SYNTAX_ERROR` on any word but `(` after a name, and reads verbs in capitals only. Of the 77 fixtures, none is a sentence of the
  grammar as written; translated by `translate()` (`haro/judge-zayn-court.js:27-46`), 66 are, and all 77 translations answer
  `SYNTAX_ERROR` on the verifier (`research/ch24.md`, block 4 and the batch). The translation runs from the language's form to the
  grammar's, and its output goes to the forged evaluator while the verifier reads the original (`:61-65`, `:73`). **The
  confirmation relayed for BOOK-ZAYN-06 (g), that the verifier reads a decoder's output after the translation that
  `haro/judge-zayn-court.js` applies, does not match the code in that direction.** Texts that this bears on:
  `site/generate.html:112-113`, `:82-87`, `:105-106`; `site/haro.html:157`; `site/tour.html:185`; `index.html:351-360`. Chapter 24
  says which form each reader accepts, and files which form a decoder writes (LANG-RECORD-GAPS-01 (c)).
- **(b) After a syntax error, the verifier judges the declaration it kept with no field.** A lawful wizard in the grammar's form
  gets `TRAPPED_FLOW`, citing Rules 51 and 53 and the right to leave; over the 77 translations, `INTENT_FLOW_NO_SATISFIES` on 28,
  `ROLE_UNDECLARED` on 13, `TRAPPED_FLOW` on 4, where the contract says of `SYNTAX_ERROR` "no law applies" (`research/ch24.md`,
  F4). Chapter 24's exercise shows the warning on a flow in the grammar's form. Recovery is outside the suite (`manifest.json:598`).
- **(c) "33 errors" is one file's count.** The number of `SYNTAX_ERROR` is one plus the words after the name: 8 to 183 over the 77
  translations, 33 on four of them (`research/ch24.md`, F5).
- **(d) Smaller differences of the grammar file.** `translate()` leaves names unchanged, so a name in capitals is clean on the
  verifier and not a sentence once translated; the grammar is written from a second declaration that names language 1.4 (no
  `LABEL`, `TARGET` or `ENTRIES` on a `NAV_GRAPH`; the contract counted "(37)"; "the 57 fixtures"); a string has no escape;
  `number` and `stringlist` are used by no rule; the comment at `judge-zayn-court.js:28` names a rewrite of comments where the next
  line deletes them; the refusal message of `zayn.stzu:1164-1166` describes the language's form (`research/ch24.md`, F6 to F10).
- **(e) One role per control, and two axes.** `proposal` says who decides; `reversible` and `irreversible` say what can be taken
  back. A control states one role, so an AI agent's applied match that can be undone, written `reversible`, is clean at level 2
  with no authority named, and `PROPOSAL_COMMITS` never reads it (`research/ch22.md`, finding 1; `doc/ROLE-DESIGN.md:248-249`
  foresaw it). Chapter 22's exercise asks it.
- **(f) One missing actor, two errors, at level 3.** With an `actors` table, a proposal that acts with no actor gets
  `PROPOSAL_COMMITS` and `HIDDEN_AUTHORITY`, both citing Rule 83, where the contract says they overlap "in spirit and not in
  reach" (`research/ch22.md`, finding 2).
- **(g) Set 31 in a design note.** `doc/ROLE-DESIGN.md:247` says that Set 31 has three rules, all `judgment`; the data holds ten,
  and files 99, 100 and 104 under `machine-later`.
- **(h) "Agent surface" in two senses, and the machine channel's rules.** `site/beyond.html:146` and `site/conformance.html:167`
  give Rules 121 and 124 as the only rules the law has for agent surfaces, in a section on `SURFACE_AS machine`; the grid places
  Rule 104 alone on `machine`, Rule 121 on `visual`, Rule 124 off the grid; `doc/ARCHITECTURE.md:66-68` uses the phrase for the
  interface through which a person meets an AI agent (`research/ch22.md`, finding 4; `research/ch23.md`, finding 3).
- **(i) Set 31's evidence.** Rules 97 to 104 carry one evidence sentence, the same in all eight, naming two products of the
  estate; Article VII asks that a harm be "real and recurring" (adds to BOOK-ZAYN-07 (f), (h)).
- **(j) Where `ACTOR` may stand.** `doc/language/DECLARATIONS.md:214-215` admits it where `SATISFIES` holds `ACT`; `:38`,
  `VIOLATIONS.md:271` and the verifier carry it on every kind, and a reading `SCREEN` with an `ACTOR` is clean.
- **(k) Provenance has no field.** Rule 99 is filed `machine-later`; `PROVENANCE` is `UNKNOWN_FIELD`, and `REPORTS [machine_made]`
  is accepted as any name and read by nothing, while `site/generate.html:142-143` says what an AI agent produces is marked as
  machine-made.
- **(l) "Cite the rules you obeyed."** The loop of `site/generate.html:123` asks the model for its citations, and nothing checks
  them: a clean run's machine form cites nothing.
- **(m) Stage words for M5.** `site/conformance.html:166` files the AI-interaction jurisdiction "designed"; `ROADMAP.md:94-100`
  lists M5 with no item done, and the founding folds its MCP surface into M12. The book carries the MCP surface as next.
- **(n) One proposal, two parties, one field.** Rule 98 asks for "an authority the declaration names"; `ACTOR` is "who performs
  the act"; the AI agent that proposed may name itself and the file is clean, and the grammar has no seat for a second party (a
  list is `UNKNOWN_FIELD`, a second line `DUPLICATE_FIELD`) (`research/ch23.md`, finding 1).
- **(o) Nothing in a declaration says that its user is an AI agent.** In data and code the machine medium equals the screen: the
  same six properties, the same carriage, the same verdicts (`research/ch23.md`, finding 2).
- **(p) The preamble's exception and the right to know.** The preamble keeps for the person every rule that names what is seen,
  heard, read or felt; `index.html:337` says an AI agent keeps the rights a person has; the verifier raises `INVISIBLE_STATE` for
  an AI agent on the machine medium under Rule 82, whose word is "perceive". Which of the six rights an AI agent keeps, the record
  does not say (`research/ch23.md`, finding 4). Chapter 23's exercise asks it.
- **(q) `INVISIBLE_STATE` cites the pattern of invisible active filters for any state** (`research/ch23.md`, finding 5).
- **(r) Statuses on the machine medium print "clean"** (kin of BOOK-ZAYN-08 (b)); `zayn.js:61-62` says two channels are listed
  where `signal.json:197` records three.
- **(s) A document behind the code.** `doc/THE-SECOND-FOUNDING.md:853-855` says no instrument would refuse a voice flow that
  mishears, acts and cannot be interrupted or reversed; at the pin the verifier refuses it, citing Rules 16, 79 and 26.
- **(t) The machine medium in the court.** No fixture puts the authority or state checks under `SURFACE_AS machine`; a pair for
  `PROPOSAL_COMMITS` there would put chapter 23's contract row in the suite (`research/ch23.md`, finding 9).

- **(u) Chapter 17's findings, owed to BOOK-ZAYN-07** (`research/ch17.md`, section 12, findings 1 to 18). The phrase "the
  enforcement ladder" names the four tiers on the site and the `machine-later` rules alone in the law's reader (1); `machine` is
  glossed "the declaration checker refuses it" while 7 of the 11 rules filed under it name another instrument in their `lint` (2);
  a count by citation has two roads, the `rules` lists and the forbidden patterns a finding cites, which reach Rules 1, 17, 18
  and 96 besides (3); one finding of the UI audit names Rules 60 and 104 in its tag (4); some checks of the audits and of the
  site's shell read what a rule legislates and cite no rule (5); for three of the four rules whose `lint` names a declaration
  lint, the `lint` names another check than the diagnostic that cites the rule, Rule 79's naming a withheld product (6); `--level 4`
  prints `clean … at level 4` (7, kin of BOOK-ZAYN-06 (a)); the reader's badge says "checked by the UI audit" on all seven `tool`
  rules (8); the site prints the census of `machine` as a count of refusals (9); "six rules" for the UI audit, which also reads
  Rule 38 (10); "judgment-tier" said of three rules the data files otherwise (11); who ruled D6 (12, in BOOK-ZAYN-07 (e)); Rule
  107's road to `machine` (13); the founding's table measured at v3.11 (14); per-level fixture counts and "Fourteen of those 20"
  (15, the first in BOOK-ZAYN-03); `site/rules.html:144` on v3.16 (16); K22 reads the page while it loads (17); the rights
  `understand` and `human` are cited by no diagnostic (18).

- **(v) A finding's sentence and its check.** The contract's sentence for `MISSING_UNDO` ("An act declares no way back: SATISFIES holds ACT, ALWAYS_REACHABLE lacks UNDO.") leaves out the role `irreversible`, under which the check does not fire (`zayn.js:486`); a verifier built from the contract's sentences alone would refuse chapter 22's lawful purge. Found by the builder of tools' door (`research/read/part9-tool-builder.md`).

**Sentences of Part IX that a ruling would change.** LANG-RECORD-GAPS-01 (c): chapter 24's "Which form a decoder is to write, and
where the step from one form to the other stands, is a question filed for the language", its exercise's closing question, its
front matter's `next` and the last sentence of its "Where it stands". Part (e), if ruled: chapter 22's exercise and its closing
question. Part (p), if ruled: chapter 23's closing question. LAW-TIER-REFUSED-01: chapter 22 quotes, at the table of Set 31, the record's glosses of `judgment` and
`machine-later`, as chapter 17 does; chapters 23 and 24 print the tier word only.

## BOOK-ZAYN-10, in parts (filed 2026-11-24)

Found while researching chapters 25 and 26 and in their verifiers' runs, each probed on the reference verifier of the pin or read
in its files. A finding against the law or the language is a gift to it.

- **(a) What a gate at level 3 reads: one file, or the project's declarations together.** The record's own build steps check
  several files in one run (`site/adopt.html:149-150`; `site/build.html:166-167`; at level 3, `tools/zayn/README.md:65`). In such a
  run a reference to a flow declared in another file is a warning, a state that another file shows is refused in each file that
  does not show it, an element declared in another file is refused the same way, and two files that declare one name pass
  (`research/ch25.md`, R5, R6; kin of BOOK-ZAYN-06 (c), (e)). Chapter 25 shows the state case and puts the question to its reader.
- **(b) `--contract` with a missing path changes the exit code, and the two verifiers take two courses.** The reference warns and
  goes on, and every finding then falls back to an error at level 1 with no citation, so a file with only a warning exits 1
  (`tools/zayn/cli.js:88-101`, `:158-163`); the Zig command answers 2 (`zig/src/main.zig:224-228`, read). Parity holds no case for
  `--contract`, an unreadable file or an unreadable table (`tools/zayn/parity.js:346-347`). `tools/zayn/README.md:80-81` says that
  without the contract the verifier "just cites less".
- **(c) Level 3 with a misspelt table prints "clean … at level 3"** (kin of LANG-LEVEL-SKIPPED-01): `site/commands.html:116` says the
  skipped checks "say so"; the run says nothing of a skip.
- **(d) A gate's run over several files.** One unreadable file among several exits 2 and prints none of the readable files'
  findings; the command expands no pattern, so a literal `specs/*.zayn` exits 2; an empty file is clean; a file in UTF-16 gives a
  hundred and more `UNEXPECTED_CHARACTER` errors (`research/ch25.md`, R2, R4, R10).
- **(e) Texts against the run** (`research/ch25.md`, section 12, items 8 to 17): `site/refusal.html:129-139` shows `--json` printing
  one finding where the run prints the outer object; `doc/design/BINARY.md:25`, `:131` say `zayn version` prints hashes, which
  `main.zig:284-296` does not; `doc/diagnostic-contract.md:81-82` "exits non-zero exactly when errors exist" (a read error exits 2);
  `tools/zayn/README.md:26` "0 clean" (a run with warnings exits 0); `site/commands.html:195` "One entry per refusal" (warnings are
  entries); `site/calling.html:116-120` prints "refused" for a read error; `site/adopt.html:101-103` and the release's file names;
  `doc/EVIDENCE-LEDGER.md:287` against the ruling of 2026-08-18; the notes of 0.2.0 name no file for their `check` run.
- **(f) A page that no menu reaches, and a band's width, pass the verifier.** A declared `NAV_GRAPH` that no `ENTRIES` lists gets no
  finding, and a band of six or seven entries gets none; the site's build refuses both on its files (`tools/site-shell.js:981-1001`,
  `:222`). Chapter 26's exercise asks whether a declaration should be able to say that every page it names is reached by a menu.
- **(g) The audit's widths and the design study's counts.** `tools/ui-audit.html:734-735` says "five widths" and lists six;
  `doc/design/DESIGN-SYSTEM.md:760` says 32 new checks and 5 extended where its table marks 29 and 8, `:25` 28 checks against 37,
  `:22` 26 components against 28, `:827` 449 and 160 corrections against 489 and 174 in the corpus; `CORPUS.md:6` "between April and
  November" where seven records are dated February and March (`research/ch26.md`, section 12, items 1 to 3).
- **(h) Requests of the corpus carry no `verbatim` field.** E42 to E46 are words of the author kept in quotation marks with no mark
  either way; the book quotes only records marked verbatim, and tells those five in paraphrase (`research/ch26.md`, item 5).
- **(i) K36's blind spot, and the fail-first runs of K34 to K37.** The memo says the check "reads the testbench only"; the code and
  the corpus say it measured the dialog, not the editor; neither the snapshot nor the memos record the failing runs that each new
  check was ordered to show first (`research/ch26.md`, items 6, 7).
- **(j) The language and the site's controls.** A layer opened over a page has no kind, and its way out is read on the painted page
  only: Maximise names Rules 51 and 53, whose diagnostic fires on a multi-step flow (`site/try.js:91`; `zayn.js:493-496`). A
  `navigate` control that declares `ACT` and keeps no `UNDO` gets two findings for one defect, where the specification scoped
  `ROLE_PROMISE_BROKEN` away from `MISSING_UNDO` as noise (`doc/language/VIOLATIONS.md:347-350`). The law's verbs hold none for
  entering or editing text, which the testbench's page names as its visitor's act (`site/testbench.html:157`). A heading of a page
  has no form of its own in a menu (`research/ch26.md`, items 8 to 12, 14).
- **(k) "This page, declared" stands on eight pages**, the redesigned ones; the ruling it comes from asks for every page (corpus
  Z261), and no check of the build requires it. Chapter 26 gives it as designed.

**Sentences of Part X that a ruling would change.** Part (a), if ruled: chapter 25's last paragraph of *What a team chooses*. Part
(f), if ruled: chapter 26's closing question.

## BOOK-ZAYN-11, in parts (filed 2026-11-26)

Found while researching chapters 3, 4 and 5, in their verifiers' reports and in the readings of the six doors, each read in the
files of the pin or run on its reference verifier. A finding against the law or the language is a gift to it.

- **(a) Lint heads that name an instrument the pin does not hold.** `constitution/rules.json` gives an `html lint` head to Rules 1,
  38, 60, 80, 107 and 127, and a `manifest lint` head to Rule 44; no `.js` or `.py` file of the pin holds either. The docket says a
  tier "is not a claim that the check runs today" (`doc/AMENDMENT-DOCKET.md:591-592`); the `lint` head carries no such word.
  Chapter 4 says "names [...] owed to read". A field saying whether the named instrument is built would let a page say it.
- **(b) `--level 4` prints "clean — 1 file(s), 0 violations at level 4"** (`tools/zayn/cli.js:225`) while the language's table says
  level 4 "requires a rendered surface" (`doc/language/README.md:128`) and the verifier holds none. Two doors read the line as a
  pass at level 4. Chapter 4 now says the verifier runs every check it holds there. Kin of BOOK-ZAYN-10 (c).
- **(c) One measure, two names.** The contract's `LAYOUT_DISPLACEMENT` (Rule 38) and the audit's check K22 LAYOUT_STILL measure
  the same displacement; no file of the pin joins the two names.
- **(d) Two target sizes.** Rule 19 asks "a minimum hit area of 44x44 pixels" for buttons in business apps (`machine-later`); Rule
  69 asks "a minimum height of 48px" on a touch surface (`judgment`); the audit's K17 cites WCAG 2.5.8 (24 by 24 CSS pixels). Which
  governs where, is the law's to say.
- **(e) No fixture on `signage`.** The suite proves `VERB_NOT_CARRIED` on print; a pair on signage (`SATISFIES [ACT]` refused,
  `[DISCOVER, LOCATE, UNDERSTAND]` clean) would prove chapter 5's claim in the court. The book runs it on its page.
- **(f) The statute tier is in documents only.** `doc/THE-SECOND-FOUNDING.md` designs a tier where "the external standard outranks
  this constitution" in physical media; the law's data holds no field for it.
- **(g) `ALWAYS_REACHABLE [EXIT]` on a sign is refused** (`VERB_NOT_CARRIED`). Chapter 5's exercise rests on it: the sign serves
  `LOCATE`, and `EXIT` is the user's intent to leave a flow. If the law means a sign may never promise the way out, a sentence of
  the specification could say so.
- **(h) A finding's article and its rule's.** `VERB_NOT_CARRIED` cites Rule 82 and Article II (`conformance/violations.json`,
  `articles: ["intent"]`); Rule 82 derives from `visible`, Article III. All six doors stopped on it. Chapter 5 now says that the
  article is the diagnostic's; the site's pages that print a citation could say it once.
- **(i) The roadmap and the docket on Rule 118.** `ROADMAP.md:75-77` says the second founding "records the strongest support Rule
  118 has ever had"; the docket's C-2 holds that "nothing is written into `rules.json` until the IEC 60073 / ISO 3864 / ISO 7010
  editions are read and clauses recorded" (`doc/AMENDMENT-DOCKET.md:40`). Chapter 5 states the commission and its gate.
- **(j) Tiers against today's refusals.** Rule 26 is `machine-later` and `MISSING_CANCEL` refuses it today; Rules 16 and 51 are
  `judgment` and refused in part. Five doors stopped on it. Joins LAW-TIER-REFUSED-01.
- **(k) `ROLE_ACTS_WITHOUT_CONSEQUENCE` says "A control promising to change nothing declares that it acts" for `ROLE navigate`
  too.** The contract's reason puts `inert` and `navigate` in one class; the message names only the first. The AI agent stopped on it.
- **(l) Which declarations a check reads.** `MISSING_CANCEL` reads flows (`INTENT_FLOW`, `WIZARD`); an `INTERACTION` that acts with no
  `CANCEL` runs clean. Three doors asked where this is said; the contract's entry could name the kinds each check reads.

**Sentences of Part II that a ruling would change.** Part (a): chapter 4's *The law names its instruments*. Part (d): chapter 3's
*Where the painted page judges*. Part (g): chapter 5's exercise. Part (j): chapter 3's paragraph on a tier and a refusal.
