# Requests the book has filed, and where each stands

What the book needs from another repository is a numbered request, never an edit. Each is filed in a memo (`sessions/`) and in one
line of `D:\GitHub\softanza\dashboard\CONCLUSIONS.md`. This file keeps their state in one place. A status is written with its date
and with who gave it; the book checks what it can check itself, read only, and says so.

## To the Zayn session (it orders the Zayn desk)

| Id | Filed | What | State |
|---|---|---|---|
| BOOK-ZAYN-01 | 2026-11-21 | The tag `v0.2.0` was on GitHub and absent from the local clone | **Done 2026-11-21 22:21** (the Zayn session). Checked by the book on 2026-11-22 19:25: `git -C D:\GitHub\zayn rev-parse v0.2.0^{commit}` answers `adaecc271dd68e10690eb0166ccb2b1f5d8d1528`. The book goes on reading by the commit's sha, which the tag names |
| BOOK-ZAYN-02 | 2026-11-21 | `README.md:37` names release 0.1.0 | **Confirmed and widened** (the Zayn session, 2026-11-22 19:22): `site/tour.html:207,216`, `site/ports.html:126` and `tools/zayn/README.md:10-12` name it too. Ordered to the Zayn desk as ZAYN-SITE-RELEASE-NAMED-01, with a check that fails first; the desk's commit had not landed when the machine restarted on 2026-11-22 01:06. The pin keeps its lines: the fix lands on `main`, after the tag |
| BOOK-ZAYN-03 | 2026-11-22 | README lines against the data or the tree, parts (a) to (e) | **Confirmed, in the same order to the desk** (the Zayn session, 2026-11-22 19:22). One more file carries the dead link of part (a): `ROADMAP.md:25`. Part (b) confirmed by its own run |
| BOOK-ZAYN-04 | 2026-11-22 | A flow whose act cannot be undone has no form of its own | **Routed** to the Zayn desk as ZAYN-LAW-BOOK-READ-01: a read and a proposal. Nothing of the law or the language changes without the author's ruling |
| BOOK-ZAYN-05 | 2026-11-22 | A rule's tier and the diagnostics that cite it tell two stories | **Routed** with 04. The Zayn session recounted the figures on the data at `adaecc2` and they stand: 40 diagnostics, 20 cite a rule, 14 rules cited (machine 5, tool 1, machine-later 1, judgment 7), 6 of the 11 `machine` rules with no diagnostic |

## What the open requests hold back in the book

- **No page states, as settled, how many of the law's rules a machine refuses.** The contract's "18 of 123" is the tier field's
  count (`machine` 11 and `tool` 7), which is a count of how the law files its rules, not of what an instrument refuses today
  (the Zayn session, 2026-11-22, on BOOK-ZAYN-05; the book's own note in `research/ch08.md` says the same). Chapter 17, *The
  enforcement ladder*, is drafted after the desk's read and the author's ruling. The pilot chapter states no such count: it
  gives Rule 79's own tier and the number of diagnostics that cite a rule, both read from the data.
- **The exercise of chapter 8** leaves the question of BOOK-ZAYN-04 in the reader's hands. If the author rules on it, the
  exercise follows his ruling.

## To the house desk

| Filed | What | State |
|---|---|---|
| 2026-11-21 | `books/zayn-book` is an untracked local repository in the house; proposed later as `mayouni/zayn-book`, a submodule, slug `zayn`, on the author's go | told; waits for the author |
| 2026-11-22 | `templates/LICENSE.md` and the Softanza reader carry the colophon line from before HOUSE-23 | told; no answer yet |
| 2026-11-22 | One preview entry, `zayn-book` (port 8740), added to the house's local `.claude/launch.json`, which git ignores | told; removed on a word |
