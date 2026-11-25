# Part X, In Practice: read from the door of the builder of tools

Pages, in order, each read twice: ch25 *The command and the gate*, ch26 *A site under its own law* (the part has two pages, not four).

## Chapter 25: The command and the gate

**1. What I remember.** A gate reads one exit code: 1 for a refusal, 0 for none (warnings included), 2 when the command could not read its input; the build goes on at 0 alone. The proof is eleven declarations on a timesheet, one per value, then level 3 with and without a symbol table, and two files that keep their refusal when checked together.

**2. Where I lost the thread.**
- The court's box: "envelope diagnostic-contract v1.2.2 — 59 diagnostics and 77 reports". Envelope, media, catalogue, spec, `VIOLATIONS.md`, `media.json` are never said; "59 diagnostics" and, two lines below, "40 diagnostics" are two counts under one word.
- *The command, as released*: "the first lines of its source list the others." The verbs a plug-in needs are sent to a source I cannot read here.
- *What I refused*: "the two axes of media and statuses, and the proofs": axes and proofs unsaid; I could not name the twelve files.
- Used before said: "suite" (said only in *The court*), "operator" (INVISIBLE_STATE's message, where the book says user), "lexer" (UNEXPECTED_CHARACTER's line), "ledger" (*Where the field leads*).

**3. Where I doubted.**
- "undecidable is silence, never a pass": the run beside it prints clean and exits 0, and at 0 the build goes on. The JSON shown has no field that tells a table-less level 3 from a real clean.
- Plate 25.4 reports `broken.zayn:9`, "at the line where the file ends", on seven lines of declaration. Line 9 holds only if the `//-->` line is in the file read. A second implementation held to "byte for byte what the reference prints" needs that convention.
- "$ zayn check sheet.zayn" prints Node's `ENOENT ... open 'sheet.zayn'`, yet the header says the JavaScript reference ran. Does the native file print Node's text?
- "calls each verifier of the family a court", on the page that calls the fixtures "the court of this chapter".

**4. What was mine.** The contract a tool plugs into. I got the exit codes and the levels: I could restate both without looking, with the symbol file's keys `actors` and `state`. I counted the line numbers in four plates' reports (25.5, 25.9, 26.3, 26.7) and each matches its file. I did not get a finding in the machine form: `--json` is shown on a clean file only, `"diagnostics": []`. And conformance stops at "compares the two sets": sets of codes, or codes with line and subject? That is what my implementation must match.

**5. Verdict.** Ready after the items above: a gate wrapper I could write today, a second verifier not yet. Stopped me most: "the suite's manifest states the findings it must get, and the run compares the two sets."

## Chapter 26: A site under its own law

**1. What I remember.** A site that publishes the law declares its menu and pages, reruns every printed report, and splits its checks over three instruments: the verifier, file checks, a browser audit. The proof is K36, which measured the popup and not the editor in it, while plates 26.3 and 26.4 show the declaration could not have seen the difference.

**2. Where I lost the thread.**
- *The site, declared*: "writes the menu from the registry... fails when the file differs from the registry." Written from it, compared to it: which file is compared?
- Plate 26.1 names `build_family, web_family, audit_family` in ENTRIES, declares none, and runs clean; in ch25 an undeclared flow gets UNRESOLVED_INTENT_FLOW. Which references does the verifier resolve?
- *A remark, a check*: "record what it measured by hand, in a browser": an AI agent, by hand? I could not tell whether K36's figures came from the check's code.

**3. Where I doubted.**
- The principle: each remark "leaves a check, written to fail on the page as it was." The case says "The session changed the page and the check" and never shows the new K36 failing on the old page; *Where it stands* puts fail-first under Designed. The principle is larger than its case.
- 26.3's report cites "Rule 119 ... Rule 112 ... Rule 16 ... Article II": one article, three rules. A parser cannot tell whose article it is.
- MENU_LABEL_REPEATS_PARENT and MENU_LABEL_DUPLICATE: plate 26.7 shows exact equality only. Case? A leading "The" (26.6 has "The rules", "The Reader")? Not on the page.

**4. What was mine.** How to write checks: fail first; an allow list where "an entry that matches no line fails"; each instrument deciding only what it can see; a build that reruns 37 printed reports, "verified, not asserted". I got it, and could build those patterns from this page. From 26.1 and 26.5 I could restate MENU_LANDING_NOT_FIRST: a section's first entry has the section's TARGET.

**5. Verdict.** Ready after the items above: the check-writer's lessons stand; plate 26.1 leaves a resolution rule open. Stopped me most: "It reads the menu with the verifier and fails when the file differs from the registry."

## For the part

**Hand-over.** Ch25's last line, "The last chapter runs it on the Zayn site's own declarations", opens ch26 exactly. Ch26 closes on Appendix A, the law in full, where a builder goes next.

**Contradictions.**
- Level 4. Ch25: "Level 4 is the painted page, the page as a browser draws it", and the suite "conforms at level 4". Ch26: "Undecidable from a declaration: it is a fact about a painted page", decided by "the third instrument", not the verifier. Is level 4 the verifier's, the audit's, or both?
- "Family". Ch25: "every verifier of Zayn's family". Ch26: "a family a group of pages inside a section". I want to know whether my implementation would join the first.
- Silence. Ch25: "the build goes on at 0 alone", and "undecidable is silence, never a pass", over a run that exits 0.

**Clearest plate.** 25.5 with the command line under it: one file, two refusals with the table, clean without; the level contract and the symbol file in one view.
**Hardest.** 26.1: a clean run on a menu that names three entries it never declares, with no word on why.

**What the builder takes away.** I can wire Zayn into a build today: three exit codes, `--json`, `--level`, `--symbols`, the pack's hash check, and the site's discipline for checks. To write a second verifier I still need one finding in the machine form, what the suite compares, how labels compare, which references resolve, and what level 4 asks.
