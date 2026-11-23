# Part III, read from the programmer's door

## Chapter 6

1. **Remember.** A declaration lists what a user does, in 22 verbs and no others; a widget is never a kind. Proof: `NAVIGATE` gets `UNKNOWN_INTENT`, error, line 2, exit 1; an inventory element with no declaration gets `INTENT_ORPHAN` at level 3.
2. **Lost the thread.** A kind for the widget: the report's parenthesis (quoted in 5) is never read. Does the warning fire on those two words only? Used before said: "level 2" (plate 6.1; the default level is stated nowhere), "Set" and "Tier" (Rule 130's card).
3. **Doubted.** "one sentence that its verbs must keep true in every declaration: its invariant" (The verbs). Flows with no EXIT, PAUSE or RESUME pass clean in plates 7.1, 8.2 and 9.5; which part the verifier enforces is unsaid.
4. **Mine.** The exact answer to a word outside the list: code, severity, line, exit code. Got it, with the warning that exits 0 (plate 6.4).
5. **Verdict: ready after the items above.** The behaviour on an unknown kind is half stated. Stopped me most: "A .zayn declaration kind outside the ten this language defines (WIDGET, USER)."

## Chapter 7

1. **Remember.** The grammar is five sentences: `DEFINE`, a kind, a name, each field once, nothing nested; ten kinds, five closed lists. Proof: `COLOR` gets `UNKNOWN_FIELD`, `TONE` on a screen gets `FIELD_MISPLACED`, `kiosk` gets `UNKNOWN_MEDIUM`, each with exit 1.
2. **Lost the thread.** "the report has two lines where chapter 8's had three" (A field it does not know): chapter 8 is ahead of me; chapter 6 showed the three lines. The reported line is the field's in plates 7.4, 7.5, 7.7 and the `DEFINE` line in 7.8, 7.9; unsaid.
3. **Doubted.** "It fits on one page, and this chapter is that page." No table says which field sits on which kind, though `FIELD_MISPLACED` reads one; DENSITY and MOTION have no stated values. "Run it. Clean!" (plate 7.10): the chapter's most surprising behaviour has no printed run.
4. **Mine.** What a field accepts. Got the five closed lists exactly: I could write TONE's five values unaided. Not the fields of each kind, nor whether `TARGET` must name an existing declaration.
5. **Verdict: ready after the items above.** Two chapters answer the unknown kind two ways. Stopped me most: "it passes over a kind it does not define, as the exercise below shows".

## Chapter 8

1. **Remember.** A refusal is a stable code, a declaration's name and the law's citations, in three forms: report, JSON, exit code. Proof: plate 8.1 gets `MISSING_UNDO` and `MISSING_CANCEL`, exit 1; one added line gives exit 0.
2. **Lost the thread.** No flag or command on the page prints the machine form (sentence quoted in 5). "2 when it could not read the file": a missing file, or a parse failure, which chapter 9 counts as a finding? The key `language` is not read.
3. **Doubted.** "the wizard, which no longer says that it acts" (plate 8.8): removing ACT quiets the check, the move the page had just refused for UNDO. The page asks the question itself.
4. **Mine.** What a build and a tool read. Got it: "The code is the stable part", the exit codes 0, 1 and 2, the object's keys.
5. **Verdict: ready after the items above**, all small. Stopped me most: "Under the report, the plate prints the same answer as a machine reads it".

## Chapter 9

1. **Remember.** The suite owns the verdict: 77 fixtures, a pass is the exact set of codes, at the level a verifier states. Proof: the runner prints 77 pass at level 4, 72 pass and 5 skipped at level 2; plate 9.2 refuses the same file once `actors.json` is given.
2. **Lost the thread.** A third evaluator (quoted in 5): which menu fixtures, and are those rows unrun? Used before said: "forged", "its judge", "the gate's own head", "Cross-pillar". Plate 9.4: `VISIBLE_STATE` and the check behind `INVISIBLE_STATE` never get a sentence, yet I must predict the code.
3. **Doubted.** "held to the JavaScript reference byte for byte in the runs their release notes record" (Where it stands). The body records the byte run for release 0.1.0; for 0.2.0, the release this book runs, a suite pass on Windows and the other files "as built".
4. **Mine.** The levels, the pass rule, a command to run. Got it: I can restate the table (10, 25, 4 and 1 kinds) and "a check whose list is not given says nothing".
5. **Verdict: ready after the items above.** The command's parity is told, the rest is run. Stopped me most: "four of them added on 8 November 2026 for the menu fixtures and written by expectation".

## The part

**Hand-overs.** 6 to 7 and 7 to 8 hold. 8 to 9: chapter 8 says the next "gives the same declarations to two verifiers, the reference and the command"; chapter 9 says "The command, its build for the browser and the forged evaluator are told from their own records". One verifier ran.

**Contradictions.** Chapter 6: "the language has no kind named WIDGET, and the verifier reports the word where it is written". Chapter 7: "it passes over a kind it does not define". Also chapter 7: "the two fields every kind carries"; chapter 6: "A flow is the one kind of declaration that the verifier asks for its SATISFIES."

**Clearest plate:** 9.2, the same file, one more input, another exit code. **Hardest:** 7.10, clean by assertion and against plate 6.7.

**Takeaway.** A declaration gets stable codes, a severity and an exit code; 77 fixtures hold any verifier to those codes at its level. I will watch three things: a warning exits 0, a misspelt kind passes in silence, level 3 checks tables written by hand.
