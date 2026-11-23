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
| BOOK-ZAYN-06 | 2026-11-23 | Ten findings of Part III's research, parts (a) to (j), below | **Filed 2026-11-23 10:17**; each part with its runs and its lines in `research/ch06.md`, `ch07.md` and `ch09.md`, section 12 |
| BOOK-ZAYN-07 | 2026-11-23 | Findings of Part VII's research and of Part III's second readings, in parts, below | **Filed 2026-11-23**, with Part VII's memo; each part with its runs and its lines in `research/ch16.md` to `ch19.md`, section 12. Three of them are the open questions that chapters 16, 18 and 19 leave to their reader |

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
| LAW-TIER-REFUSED-01 | what a tier means, and what the site prints | the tier keeps the docket's meaning, and each rule gains a field naming what refuses it today |
| LAW-TIER-CHECK-01 | a check that a tier and the instruments agree | |
| LAW-SELECT-CONFIRM-01 | Rule 16's text, and the meaning of `CONFIRM` in the specification | |
| LANG-FLOW-REFERENCE-01 | a reference may name a `WIZARD`; `MISSING_UNDO` reads `ROLE` on an `INTERACTION` only | |

If they are ruled, they land after the pin; the Zayn session tells the book which release carries them.

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
