# Part III, from the door of the builder of tools

My question: could I write a second verifier, or plug mine in?

## Chapter 6 · Intent first

1. **Remember.** A declaration is made from 22 verbs in 6 families, a closed list, with no kind for a widget. Proof: `NAVIGATE` gets `UNKNOWN_INTENT` and exit 1; an inventoried element with no verb gets `INTENT_ORPHAN` at level 3.
2. **Lost.** "The first line has no line number, because the element is in the inventory and not in the file." (An element with no verb): in plate 6.10 `search_form` is in the file and has none either. Terms before they are said: "level 2", "Set", "Tier", "layer", "wizard".
3. **Doubted.** "A screen that reads and acts breaks the invariant of information.": not run, and no code named.
4. **Mine.** The vocabulary as data, and level 3's input. Got: the table, the symbol table's shape, the matching rule ("a declaration carries its name and satisfies one"). Not: the file that holds the verbs.
5. **Verdict: ready after the items above.** The verbs are exact; the rule for an unknown kind is not. Stopped most: "the language has no kind named WIDGET, and the verifier reports the word where it is written".

## Chapter 7 · Ten declarations, one grammar

1. **Remember.** A declaration is `DEFINE`, a kind, a name and fields; a field holds a bracketed list or one value, and nothing nests. Proof: 10 kinds accepted in three files, then five refusals, from `UNKNOWN_FIELD` to `INVALID_TONE`.
2. **Lost.** "the report has two lines where chapter 8's had three" (A field it does not know): chapter 8 is unread; chapter 6's had three. Plate 7.10, "write down the two codes you get": is a misplaced `TONE`'s value judged too? The codes are never printed. Terms: "contract", "pillar".
3. **Doubted.** "It fits on one page, and this chapter is that page." No table says which fields each kind carries, so `FIELD_MISPLACED` cannot be rebuilt from the page.
4. **Mine.** The grammar, to write a parser. Got: five sentences, five lists with every value. Not: the kind-by-field table, each field's value type, what a name is made of.
5. **Verdict: ready after the items above.** I could write the parser, not the field checks. Stopped most: "That is all of it."

## Chapter 8 · The refusal

1. **Remember.** A refusal is a code, a subject and the citations the contract binds to that code, as a printed report, a JSON object and an exit code. Proof: `MISSING_UNDO` and `MISSING_CANCEL` on a three-line flow, and the object under plate 8.5.
2. **Lost.** "The same answer, as a machine reads it" (An act that cannot be undone): no flag is given to ask for it. "2 when it could not read the file": chapter 9 files two findings as "failures to parse"; exit 1 or 2? The principle says "a code, a name"; the object has no key for the declaration's name.
3. **Doubted.** "The contract is the list of everything the verifier can report.": chapter 9's runner names a second, `diagnostic-contract v1.2.2`.
4. **Mine.** The machine form and the exit codes: got both. Not the flag, nor `span` for a finding with no line.
5. **Verdict: ready after the items above.** I could restate the object's keys and the three exit codes. Stopped most: "2 when it could not read the file".

## Chapter 9 · One verdict, two verifiers

1. **Remember.** The suite owns the verdict: 77 fixtures, a manifest of levels and codes, a pass when the sets of codes are equal, a skip above the verifier's level. Proof: the runner's two printed runs and plate 9.2.
2. **Lost.** "four of them added on 8 November 2026 for the menu fixtures and written by expectation" (A third evaluator): were they run? "Each level 3 check waits for its own list": the four pairs are never written, nor what triggers `INVISIBLE_STATE` and `UNRESOLVED_ENTITY`.
3. **Doubted.** "held to the JavaScript reference byte for byte in the runs their release notes record": the byte gate's recorded run is release 0.1.0's; 0.2.0 records the suite passing.
4. **Mine.** What conformance asks. Got: the pass rule, the skip rule, the four levels, codes for the suite, bytes for a port. Not: each code's level, the manifest's shape, what my verifier hands the runner.
5. **Verdict: ready after the items above.** I know what a pass is, not how mine is judged. Stopped most: "every verifier, in whatever language it is written, is held to that answer at the level it can see".

## The part

**Handover.** 6 to 7 and 7 to 8 hold. 8 to 9 promises more than 9 runs: "gives the same declarations to two verifiers, the reference and the command", while in chapter 9 the command is "told from their own records".

**Contradictions.**

- Chapter 6: "the verifier reports the word where it is written" (`WIDGET` warns). Chapter 7: "it passes over a kind it does not define" (`SCREN` is clean). The report's "(WIDGET, USER)" hints at a list of two words; no page says so.
- Chapter 8: "compares the codes a verifier reports and nothing else". Chapter 9, on the envelope, media and catalogue lines: "the runner fails when the two places differ". Do those bind a second verifier?

**Plates.** Clearest: 9.2, one more input and another verdict. Hardest: 6.10, where a form in the file is an orphan until 6.11 explains.

**Takeaway.** I could start a level 2 verifier: parser, verbs, closed lists, exit codes, the object's keys, the pass rule. I count 26 of the 40 codes named. To finish it, or to plug mine in, I need the kind-by-field table, each code's trigger and level, and the manifest.
