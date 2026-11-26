# Part II, read from the door of the AI agent that reads the book as data (second reader)

Pages read, in order, twice: ch3 *What the field wrote*, ch4 *The instruments of the field*, ch5 *The road sign*.

## Chapter 3: What the field wrote

1. **What I remember.** The field's heuristics are advice; where a declaration can state a heuristic's content, the law turns it into a named refusal (INVISIBLE_STATE, MISSING_UNDO, SELECT_ACT_COLLAPSE, UNKNOWN_SIGNAL), and the rest (target size, menu length, grouping, data-ink) is judged on the painted page. Proof: four refused/clean pairs plus an exercise combining three of them.
2. **Lost the thread.** "Without --symbols, the verifier skips the checks that need the table. Given no table, the same file runs at level 2" (State the user must see). I cannot tell whether `--level 3` with no `--symbols` is an error, a silent downgrade, or a pass; plate 3.2's report says "at level 2", so the command used is not shown. Terms used before said: "the docket" in the tier paragraph ("in the docket's words it 'is honest...'") before "What I refused" defines it; "MISSING_CANCEL" and WIZARD appear only in the court.
3. **Doubted.** The tier "machine-later" is glossed "the tier of a rule whose instrument comes later", yet the map files Rule 26 as machine-later and the court runs MISSING_CANCEL, which the page ties to Rule 26 ("It is Rule 26"). A rule whose instrument "comes later" is refused today. The general sentence "it is not a claim that the check runs today" covers judgment-but-refused (Rule 16, 118), not machine-later-but-refused. Also: "The verifier's findings cite Rules 82, 79, 26, 51 and 16": no finding on the page cites Rule 51, so I cannot check it.
4. **What was mine.** Exact codes, levels and the shape of a report line. Mostly got it; the contract box gives UNKNOWN_SIGNAL "level 1" while every UNKNOWN_SIGNAL report says "at level 2", and the page never says that the contract's level is the lowest level at which a code fires and that levels accumulate (the level 3 exercise returning level 2 codes implies it).
5. **Verdict: ready after the items above.** Stopped me most: "Rule 26 machine-later" set against "the tier of a rule whose instrument comes later".

## Chapter 4: The instruments of the field

1. **What I remember.** Each field instrument (criterion, token, story, linter, screenshot, layout-shift measure) decides on its own object; a declaration is a different object, so a drawing that passes them all can still be refused for what it lets the user do. Proof: the checkout refused for SELECT_ACT_COLLAPSE and two alike cards, one refused for ROLE_ACTS_WITHOUT_CONSEQUENCE.
2. **Lost the thread.** The ROLE definitions: "inert promises to change nothing, navigate to change only what is shown". Then the exercise's report fires "A control promising to change nothing" on a `ROLE navigate` tile, and the class rule ("the contract puts inert and navigate in one class") arrives only at the page's last paragraph. The rule I need to generate correctly (ACT is forbidden with inert and with navigate) is stated once, late, as an explanation of a message.
3. **Doubted.** Plate 4.4 and 4.8: `ROLE reversible` with UNDO in reach is clean. The page never says whether reversible *requires* UNDO, or whether an INTERACTION that acts needs CANCEL (ch3's MISSING_CANCEL names INTENT_FLOW and WIZARD only, so I infer INTERACTION is exempt, but no sentence says so). "Clean, and the command answers 0. That verdict is the declaration's": fine, and sized honestly.
4. **What was mine.** The ROLE vocabulary and what it forbids. Got inert/navigate/reversible and one forbidden pair; did not get the full list of ROLE values or reversible's obligations.
5. **Verdict: ready after the items above.** Stopped me most: "inert promises to change nothing, navigate to change only what is shown".

## Chapter 5: The road sign

1. **What I remember.** The Vienna Convention closes its vocabulary, explains its shape by international understanding, and amends by memorandum and experiment; Zayn makes the same move with a closed list of ten media, the verbs each carries, and five statuses. Proof: a sign promising ACT/UNDO/CANCEL/EXIT refused four times; READ refused on signage and clean on print; road_sign refused as a medium; critical refused as a status.
2. **Lost the thread.** Nowhere: the article explanation ("The article on a finding's line is the diagnostic's own... Rule 82 sits under Article III") resolves the only surprise, and it is exactly the rule I need. But it is stated here, in chapter 5, while ch3 already printed Rule 16 with Article II without the rule.
3. **Doubted.** "of signage the data says that it carries the signal 'in principle'": I cannot tell what happens to SIGNALS on a medium that does not carry it (is there a code?). Line anchoring: VERB_NOT_CARRIED for UNDO (on line 7) is reported at `sign-acts.zayn:5`, the DEFINE line, while UNKNOWN_SIGNAL is reported on the line of the word. No sentence says where a finding's line points.
4. **What was mine.** Which verbs each medium carries. Got signage's three (LOCATE, DISCOVER, UNDERSTAND) exactly; print only partly ("also carries SCAN and COMPARE", and UNDERSTAND by inference from plate 5.4).
5. **Verdict: ready after the items above.** Stopped me most: "carries the signal 'in principle', and its rendering is at the design stage".

## The part

- **Hand-over.** Each page closes on the next: ch3 to "the instruments of the field", ch4 to "the road sign", ch5 to Part III. Clean.
- **Disagreements.** (a) ch3: "machine-later, the tier of a rule whose instrument comes later" vs ch3 court/map: Rule 26 machine-later, refused today by MISSING_CANCEL. (b) ch4: "navigate to change only what is shown" vs ch4 report on navigate: "A control promising to change nothing". (c) ch3 levels: "Level 1 reads the file's grammar and words" vs ch5: UNKNOWN_MEDIUM (a word outside a closed list) is "level 2", and ch3's UNKNOWN_FIELD level is never given. Not contradictions of fact, but an agent deriving a level from the description gets UNKNOWN_MEDIUM wrong.
- **Consistent across pages**, checked: 123 rules numbered to 130; 22 verbs; five statuses in the same order; Rule 82 Perceivable State under Article III; Rule 118 Article I; SELECT_ACT_COLLAPSE message identical in ch3 and ch4.
- **Clearest plate:** 5.3 and 5.4, one verb (READ) and one medium word turn the verdict, and I could restate the rule without looking.
- **Hardest plate:** 4.3, a report citing Rules 119, 112, 16 and Article II, where the reason for 112 needs the contract's class rule given only at the end of the page.
- **What I take away.** I could write lawful INTENT_FLOWs for the ACT pattern (SELECT, CONFIRM, ACT with UNDO, CANCEL, EXIT) and SIGNALS from the five. I could not yet write any medium but signage reliably, nor any ROLE but the three shown, because the verb-per-medium table, the ROLE list and the full verb list are not on these pages (forward pointers would do).

## The three items that most need fixing

1. State the tiers once so that machine-later and a running refusal do not collide (Rule 26 / MISSING_CANCEL), or say plainly that a finding refuses part of a rule whatever its tier.
2. State the ROLE class rule (inert and navigate may not ACT) where ROLE is defined in ch4, not after the exercise.
3. Say what `--level 3` without `--symbols` does, and that a code's contract level is its lowest level and levels accumulate; give UNKNOWN_FIELD's level and say where a finding's line number points.
