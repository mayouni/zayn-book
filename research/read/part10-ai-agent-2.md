# Part X, In Practice: the AI agent that reads the book as data, second reading

Read in order: chapters 25, 26.

## Chapter 25, The command and the gate

1. **Remembered.**
   - Exit codes of `zayn check`: 1 when any finding is an error, 0 when none is (warnings included), 2 when the command cannot read its input ("Exit codes: 0 clean · 1 violations found · 2 usage or read error"). Proved by plate 25.1 (1), 25.2 (0), 25.3 (a warning, 0), 25.4 (a syntax error, 1) and the `sheet.zayn` line (2).
   - A file that does not parse gives 1 (`SYNTAX_ERROR`, plate 25.4); a file that cannot be read at all gives 2 (`ENOENT`, the `sheet.zayn` line).
   - The person's report has this form: `file:line  severity  CODE  detail`, then the message, then the citation line; then `N error(s), M warning(s) across K file(s) at level L`. A clean run prints `clean — K file(s), 0 violations at level L against Zayn v3.17` (plates 25.1, 25.2).
   - `--json` prints an object with `level`, `contract{version, constitution}`, `files`, `counts{errors, warnings}`, `diagnostics[]`. Each diagnostic has `code`, `severity`, `message`, `span{file, line}`, `cites[]`, `language`, `level`, `subject` (the JSON runs under 25.1 and 25.2). A clean run keeps `"diagnostics": []`.
   - `--quiet` prints nothing on a clean run (the run under 25.2).
   - The default level is 2 (every plain run prints "at level 2"). `--level N` sets it, and a run at a level also reports the findings of the levels below it.
   - Level 3 without `--symbols` returns clean with exit 0 ("undecidable is silence, never a pass"). A level-3 gate must pass the table on the same command line (the `--level 3` run before plate 25.6).
   - The symbol table is JSON; `actors` and `state` hold arrays of names (plate 25.5).
   - At level 3 with the table: an act with no `ACTOR` gives `HIDDEN_AUTHORITY`, and a table state that no surface lists in `VISIBLE_STATE` gives `INVISIBLE_STATE`. Both are errors (plates 25.5, 25.6).
   - Each file is judged on its own, even when several files are checked in one run. A flow declared in another file still gives `UNRESOLVED_INTENT_FLOW` (the two-file run under 25.3), and a state shown in another file still gives `INVISIBLE_STATE` (the run under 25.8).
   - The level-2 codes and when they fire: `READ_ACT_COLLAPSE` (SATISFIES holds READ and ACT), `SELECT_ACT_COLLAPSE` (SELECT and ACT without CONFIRM), `MISSING_UNDO` (ACT with no UNDO in ALWAYS_REACHABLE), `ROLE_PROMISE_BROKEN` (ROLE reversible with no reachable UNDO). An irreversible role owes no UNDO (plates 25.1, 25.9, 25.10, 25.11).
   - Gate command: `zayn check specs/*.zayn`, with `--level 3 --symbols <file>` added for a level-3 gate.
   - The suite compares codes "by diagnostic id only — never line numbers, wording or order".

2. **Lost the thread.**
   - "which the family calls a court" against "In this book, the court of a chapter is the fixtures that judge its claims." One word names both a verifier and a chapter's fixtures. When "a court's private extension" is quoted, I cannot tell which of the two is meant.
   - "Each finding is one object under diagnostics" names every field except `"language": "zayn"` and the diagnostic's own `"level": 2`. Both levels are 2 in the only example, so I cannot tell whether a diagnostic's `level` is the run's level or the level of the code's kind.
   - `"article:intent"` against "Article II": the mapping from an article id in `cites` to its numeral is shown once and never stated, so I cannot map any other article.
   - The fourth column of the report is the subject in "READ_ACT_COLLAPSE  timesheet_week" but a phrase in "submit_week referenced by week_entry", while the promise names "week_entry". I have to infer that the JSON `subject` is `week_entry`, because the JSON for that finding is not shown.
   - The rule for which line a finding points at is given only by example. It is the declaration's line in "week.zayn:5" and the ROLE clause's line in "review.zayn:7", and `INVISIBLE_STATE` has no line at all: "week.zayn  error  INVISIBLE_STATE  week_status". "at the line where the file ends" gives `broken.zayn:9` for an eight-line plate. I would need the `span` of a line-less finding in JSON and the end-of-file count before I could parse these reliably.
   - "lists under four keys what the system around a declaration holds: its entities, its actors, its state and its elements": only `actors` and `state` appear as keys. The exact names of the other two keys, and "A table gives the keys its checks need" (which check reads which key), are left to guessing.
   - The opening defines the clauses SATISFIES, ALWAYS_REACHABLE and ROLE. `ACTOR employee` (a bare name), `VISIBLE_STATE [week_status]` (a list) and `INTENT_FLOW submit_week` inside a FORM appear only in plates and their In words. "A consequential act names no actor" does not say which verbs or kinds count as consequential, so I cannot tell whether `MARK` on an INTERACTION would need an actor.

3. **Doubted.**
   - "Plate 25.6 The week, repaired at level 3" shows no symbol table, and the paragraph just before it says: "Without the table, the checks of level 3 have nothing to read, and they say nothing." From the page alone, its clean result cannot be told apart from the silent clean, so the repair is not proved on the page.
   - "Level 2 decides what a single declaration states." Yet `UNRESOLVED_INTENT_FLOW` is "level 2, warning", and it judges one declaration against the other declarations of its file.
   - "1 when the verifier refused a declaration" is the gate's rule. On the same page, for cross-medium, "a difference stays undecided, and the run answers 1", while elsewhere undecidable is a warning ("or undecidable without more input", exit 0) or silence (level 3 with no table, exit 0). The page gives the same exit code to different events, depending on the verb.
   - "That is 12 files, with a manifest, the list that gives each file's hash." The list before it names four files, two axis files and "the proof", which is an unstated number of files. I cannot list the twelve files to vendor, and the suite's manifest (one of the twelve) and `MANIFEST.json` (beside them) are two different manifests.
   - "version names the editions the command carries" (a verb) against "built and run: --version" (an option). I do not know which form to type.

4. **Mine.** I came for the exit codes, the shape of the machine form, the levels and the gate command line, and I got all four in exact, runnable form. I did not get a complete rule for the symbol table (two key names, which check reads which key), for `span.line`, or for the diagnostic's `level` field. Those are the parts a tool that parses the output or writes the table needs most.

5. **Verdict.** `ready after the items above`. Stopped most by: "The symbol table, the table for short, is a small file, given with --symbols, that lists under four keys what the system around a declaration holds: its entities, its actors, its state and its elements."

## Chapter 26, A site under its own law

1. **Remembered.**
   - NAV_GRAPH syntax: `LABEL "<text>"`, `TARGET <page>`, `ENTRIES [<nav_graph names>]`; one line or several (plate 26.1).
   - An entry that names no declared NAV_GRAPH is not judged and gets no finding. The page contrasts this with the flow warning, quoting the specification (plate 26.1).
   - `MENU_LABEL_REPEATS_PARENT`: a child's label equals its parent's. It is a level-2 error under Rule 116, and the report points at the child's line: `law.zayn:16 ... "Design system" of design repeats "Design system" of design_family` (plate 26.7). Changing the child's label clears it (plate 26.8).
   - `MENU_LANDING_NOT_FIRST` and `MENU_LABEL_DUPLICATE` are level-2 errors (the contract table). Labels compare ignoring case, the spaces around them and a leading "The".
   - A menu with levels is lawful (plate 26.5). Declared pages that no menu reaches are not refused by the verifier (plate 26.6).
   - `ROLE_ACTS_WITHOUT_CONSEQUENCE`: `ROLE navigate` with `ACT` in SATISFIES is a level-2 error, reported at the ROLE line and citing Rules 119, 112 and 16 (plate 26.3). Dropping `ACT` (and the UNDO it no longer needs) clears it (plate 26.4).
   - The size of what is drawn belongs to the browser audit (K34 to K37), not to the declaration (plates 26.4, 26.5 and the text after them).

2. **Lost the thread.**
   - "A section is a group of the main menu, and a family a group of pages inside a section." The landing rule then speaks of "a section whose first entry is not its landing page", while the contract says "A section with children". The exercise asks for a family "with its landing first", but no run shows whether the code fires on a family or on a deeper level.
   - "the entry whose TARGET is the section's own": in plate 26.5 three entries share `TARGET positioning`, so "the" entry is not unique. The page never says what happens when no entry carries the parent's TARGET.
   - "The report says the control promised "to change nothing": for navigate, that means nothing true." `inert` also promises to change nothing true, and the page does not say whether `ROLE inert` with `ACT` gets the same code.
   - "Rule 119 · A Card Is Not a Button · Rule 112 · Motion Reports, It Never Decorates · Rule 16 · Intentional Clicks · Article II": three rules with one article. I cannot tell which rule the article belongs to, or how `cites` lists three rules in JSON.
   - `MENU_LANDING_NOT_FIRST` and `MENU_LABEL_DUPLICATE` are never run on a plate, so their report line and detail form are unknown. The label comparison ("Invoices" and "The invoices" are one name) is stated, and no plate exercises it.

3. **Doubted.**
   - "A flow that a form names and no file declares gets a warning, as chapter 25 shows." Chapter 25's two-file run keeps the warning while `week.zayn`, in the same run, declares the flow. The warning fires when the flow is not declared in the same file, which is a different condition from "no file declares" it.
   - "They refuse a page the registry does not list, and a phrase that lists what the project lacks." Against this, Where it stands describes "checks that today count the pages they would refuse, owed by a later step". The page does not say which of the site's checks refuse today and which only count.
   - "Its Adopt section ran clean on this page." Yet of plate 26.1 the page says: "In this excerpt they are names with no declaration." Three of the section's five entries were not judged, so the run shows less than the claim.
   - The principle has each remark leave "a check, written to fail on the page as it was". For the chain's own checks, the page records only passing measurements (96 percent, 33 flat lists, 1596 by 930), and for K36 it records "The session changed the page and the check." It does not show the rewritten check failing first.

4. **Mine.** I came for the three menu codes, the NAV_GRAPH syntax and what the verifier leaves to other instruments, and I got the syntax, the label comparison, the non-judging of undeclared entries and one menu code run end to end. The landing rule, the code I would apply most, is given in prose only, with its scope (section or family) and its multiple-target case open.

5. **Verdict.** `ready after the items above`. Stopped most by: "The verifier refuses three codes of a menu: a label that repeats its parent's; a section whose first entry is not its landing page, the entry whose TARGET is the section's own; and two siblings with one label."

## For the part

**Hand-over.** Yes. Chapter 25 ends with "The last chapter runs it on the Zayn site's own declarations, a site held to the law it publishes", and chapter 26's first sentence defines exactly that. Chapter 26 closes with an open question and a pointer to the law's data in Appendix A. For an AI agent that pointer is the right last line, because it says where the full rule set lives. Both chapters still carry a visible `[AUTHOR: ...]` line for the stake.

**Contradictions.**
- Ch. 26: "A flow that a form names and no file declares gets a warning, as chapter 25 shows." Ch. 25: "The warning stays: the verifier judges each file on its own" (after a run where another file declares the flow).
- Ch. 25: "Level 2 decides what a single declaration states." Ch. 26: "MENU_LABEL_REPEATS_PARENT level 2, error A menu entry's label repeats the label of the entry it sits under." (This level-2 code relates two declarations.)

**Clearest plate / Hardest plate.**
- Clearest: plate 25.1 with its `--json` run. It shows one fault, one code, the person's report and the machine form side by side, and the exit code. The JSON is complete enough to write a parser from.
- Hardest: plate 25.6. It is titled as a level-3 repair, it shows no table, and it follows the sentence that says level 3 with no table is silent and clean. The reader cannot tell from the page whether its clean proves the repair.

**What the agent takes away.**
- The rules I would apply:
  - Gate on exit code: 0 pass, 1 stop, 2 fix the gate.
  - Read findings from `--json` `diagnostics`, keyed by `code`.
  - Run at level 2 by default. Never run level 3 without `--symbols`.
  - Keep a flow and the screen that shows its state in one file.
  - Every ACT needs CONFIRM after SELECT and UNDO within reach. `reversible` needs UNDO, and `navigate` must not ACT.
  - In a menu, give the first entry the parent's TARGET and a label that differs from the parent's, give siblings distinct labels, and remember that undeclared entries are not judged.
- What I would still have to guess:
  - the names of the `entities` and `elements` keys, and which check reads which key;
  - what `span.line` holds for a finding with no line;
  - whether a diagnostic's `level` is the run's level or the kind's;
  - how an article id maps to its numeral;
  - whether `inert` plus ACT is refused;
  - whether the landing rule binds families and what it does with several or no entries on the parent's TARGET;
  - what `--level 4` adds beyond level 3;
  - what `--quiet` prints when there are findings;
  - which twelve files to vendor;
  - whether `version` is a verb or `--version` an option.
