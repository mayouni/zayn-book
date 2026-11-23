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
- **No page states, as settled, how many of the law's rules a machine refuses.** Chapter 17, *The enforcement ladder*, is drafted
  from the count by citation above, each figure recounted at the pin, with the sentences a ruling would change marked in its
  research file. It is drafted after Part III.
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
