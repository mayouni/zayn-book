# Part II, read from the door of the builder of tools

Pages read, in order: chapter 3 "What the field wrote", chapter 4 "The instruments of the field", chapter 5 "The road sign". Read once whole, then again with the brief's questions.

## Chapter 3: What the field wrote

1. **Remembered.** The field's heuristics live in the law as numbered rules filed at tiers, and the verifier refuses the part a declaration can state (hidden state, no undo, selection that pays, a status off the list). Proof: thirteen plates, each refusal before its repair, and the run's reports.
2. **Lost the thread.**
   - Map, after the table: "The verifier checks Rules 82, 79, 26, 51 and 16 by name". The same table files Rule 26 as machine-later and Rules 51 and 16 as judgment. I took the tier to mean "who owes the check", and here the verifier checks judgment and machine-later rules. Plate 3.8 explains this for Rule 118 alone.
   - The court, codes table: "UNKNOWN_SIGNAL level 1". Level 1 is never defined. Levels 2 and 3 are, and the plate's report says "at level 2".
   - "A symbol table... lists the system's state, its actors and its entities": the plate shows only `state`. I cannot write a reader for the other two keys.
3. **Doubted.** Nothing reads as an advertisement. "The law leads in force" is said at the size shown.
4. **Mine.** The finding's shape: file:line, severity, code, subject, message, citation; the exit codes 0 and 1; and the level at which a check goes silent (plates 3.1 and 3.2). I got it, with one gap. The line number points to the DEFINE line for MISSING_UNDO (`ledger.zayn:1`) and to the field's own line for UNKNOWN_SIGNAL (`overdue.zayn:3`). INVISIBLE_STATE has no line at all. The page explains only the missing line, not the rule for the others.
5. **Verdict:** ready after the items above. The sentence that stopped me most: "The verifier checks Rules 82, 79, 26, 51 and 16 by name". It undoes my reading of what a tier means.

## Chapter 4: The instruments of the field

1. **Remembered.** Each instrument of the field (criterion, token, story, linter, screenshot, layout shift) reads its own object. A declaration is one more object, which Zayn's verifier reads before anything is drawn while its audit reads the drawing. Proof: two cards drawn alike, refused on one word (ROLE), and LAYOUT_DISPLACEMENT left to the audit.
2. **Lost the thread.**
   - "The law names its instruments": "The field is lint, and 18 rules carry it. Its heads name the instrument". "Field" has meant the discipline for two chapters, and here it means a data key. "Heads" is never said. Of all the sections, this one is my door, and I cannot picture the data's shape.
   - The court: `field-misplaced-lawful.zayn` stands for "the screen of overdue invoices with its notice". The name tells me nothing about which claim it proves.
   - Plate 4.8: a tile that ACTs with no CANCEL runs clean. Chapter 3 shows MISSING_CANCEL for "a flow that acts". I infer that MISSING_CANCEL binds INTENT_FLOW and MISSING_UNDO binds INTERACTION too, but no page says which check applies to which kind of declaration. A second implementation needs that.
   - ROLE: is {inert, navigate, reversible} the whole list? The tile refused under "A control promising to change nothing" declares `navigate`. The contract's sentence on Rule 112 covers it, but only after two readings.
3. **Doubted.** "a run at --level 4 runs every check the verifier holds" is useful, and it implies that levels are cumulative. I would like that said once as a rule.
4. **Mine.** Plug-in points: the contract has 40 kinds of finding, one of them at level 4 and given to the audit, and the lint field names the instrument each rule is owed. I got about half. I have the count and five examples, but not the field's values or format, and not what a third-party instrument must emit to answer for a rule.
5. **Verdict:** ready after the items above. The sentence that stopped me most: "The field is lint, and 18 rules carry it."

## Chapter 5: The road sign

1. **Remembered.** The Vienna treaty closes its vocabulary, explains why, and amends by memorandum. Zayn closes its media, verbs and statuses the same way, as data. Proof: one word of medium (signage or print) turns the verdict on READ, and lists outside the data are refused.
2. **Lost the thread.**
   - Plate 5.1: every VERB_NOT_CARRIED cites "Rule 82 · Perceivable State · Article II". Chapter 3's plate 3.1 cites "Rule 82 · Perceivable State · Article III · the right to know", and its prose reads "under Rule 82, Article III". The same rule sits under two articles, and the page gives no reason that a medium's verbs belong to Perceivable State. I would conclude that a kind of finding's citation is set per code in the contract, not derived from the rule. If so, it should be said once.
   - The promise `//--> 4 VERB_NOT_CARRIED`: the count form is used but not said.
   - Locus: VERB_NOT_CARRIED points to the flow's DEFINE line (`:5`) even for a verb in ALWAYS_REACHABLE, while UNKNOWN_SIGNAL points to `:7`, the SIGNALS line. This is the same unstated rule as in chapter 3.
   - Codes table: UNKNOWN_MEDIUM is level 2 and UNKNOWN_SIGNAL is level 1, though both judge a word against a closed list. Level 1 is still undefined.
3. **Doubted.** "the most successful interface standard in human history" is quoted, and the ledger's check that follows sizes it honestly. That paragraph earns trust.
4. **Mine.** The medium-by-verb table as data (native, at a cost, absent; "only an absent verb raises a finding"). I got the rule but not the table: print's verbs are given in passing, and no pointer says where the full table is printed.
5. **Verdict:** ready after the items above. The sentence that stopped me most: "Rule 82 · Perceivable State · Article II".

## For the part

- **Hand-over.** Each page hands over cleanly. Chapter 3 ends on instruments, chapter 4 ends on the road sign, and chapter 5 ends on the inversion.
- **Contradiction.** Chapter 3: "Rule 82 · Perceivable State · Article III · the right to know". Chapter 5: "Rule 82 · Perceivable State · Article II". The tier versus the check, inside chapter 3: Rule 26 is "machine-later, the tier of a rule whose instrument comes later", and yet "The verifier checks Rules 82, 79, 26, 51 and 16 by name", with MISSING_CANCEL in the court.
- **Clearest plate:** 5.3 and 5.4. One word of medium, READ refused or clean, and the data named as the reason.
- **Hardest plate:** 4.3. Four citations in one finding, one of them on motion, and a message about "change nothing" that later fires on `navigate`.
- **What I take away.** I could write a reader for the report format, the exit codes, the closed lists (22 verbs, 10 media, 5 statuses) and the manifest-driven court. I could not yet write a second verifier. Three things are missing: which check binds which kind of declaration; the rule for a finding's line and citation; and what level 1 is. "What conformance asks" is shown by the manifest's fixtures, but no page states it as the test a second implementation must pass.
