# Part IV, read from the door of the builder of tools

Read: ch10 then ch11, as built (`.cache/as-read/`), twice. I asked of each page whether I could write a second verifier, or plug my audit in, from what it says.

## Chapter 10, What a declaration cannot see

1. **What I remember.** A declaration names no widget, so one clean file stands under a careful drawing and a drawing with seven faults; Rule 79 and Rule 119 each split into a half the verifier refuses and a half only the painted page shows. The proof is plate 10.1 and 10.2 giving the same clean report, then MISSING_UNDO refused and repaired.
2. **Where I lost the thread.**
   - "One rule, two halves" and the court: plate 10.3 is ROLE reversible with no UNDO, and it gets only MISSING_UNDO. Chapter 11's contract says ROLE_PROMISE_BROKEN is "A reversible control keeps no reachable UNDO." Why that code is not also reported here (suppression, precedence, or a condition on ACT) is stated nowhere. A second implementation would report two findings and fail the suite.
   - The exercise's code IRREVERSIBLE_CLAIMS_UNDO is in no court box and no contract line; I get its words from the report alone.
   - "What reads the drawing": "Five of the seven faults meet a check" lists six checks against five faults, and K02 pairs with no named fault. I want one row per fault.
3. **Where I doubted.**
   - "clean — 1 file(s), 0 violations at level 4": the page says the verifier "holds none" of a rendered surface. A report that says clean at a level it cannot read is the conformance question I came with: must my tool print the same, or say the level was partly read?
   - Designed: "LAYOUT_DISPLACEMENT, measured by the audit's K22". Measured reads as built; the stage says designed. Its shape (subject, line, level) is not given, so I cannot emit it.
   - "the law is Zayn's constitution of 123 rules", then Rule 129 on the same page (and 125 in ch11). Numbering beyond the count is not explained.
4. **What was mine.** The boundary of the contract: which findings a declaration tool owes, and which kind it hands to a drawing tool. I got the boundary (LAYOUT_DISPLACEMENT is the one kind given to the painted page; the K01 to K37 table, which I could sum to 37), not the interface between the two.
5. **Verdict:** ready after the items above. The missing ROLE_PROMISE_BROKEN on plate 10.3 is a fault a second implementer meets on the first run. Stopped me most: "at level 4 it runs the checks it holds, and each reads the declaration".

## Chapter 11, The strata of expression

1. **What I remember.** Between the intent and the drawing sit six functions: structure, signal, role, motion, message, tempo. SIGNALS and ROLE are built fields with their own refusals, three are carried by older fields, tempo is held in the law. The proof is red refused as UNKNOWN_SIGNAL, button refused as UNKNOWN_ROLE, a lone ROLE refused as EXPRESSION_ORPHAN, each repaired.
2. **Where I lost the thread.**
   - "Signal: a meaning": "five statuses, each with the rule's own meaning". Two are named (danger, warning). I cannot write the enumeration.
   - "In your hands": the repair uses TONE critical; the TONE list is never printed on this page ("chapter 7 runs that refusal"). The exercise needs it now.
   - "decides three kinds of finding from SIGNALS and seven from ROLE": the ten are not named. I can find UNKNOWN_SIGNAL, EXPRESSION_ORPHAN, UNKNOWN_ROLE, ROLE_PROMISE_BROKEN, ROLE_ACTS_WITHOUT_CONSEQUENCE, IRREVERSIBLE_CLAIMS_UNDO, ROLE_UNDECLARED, and cannot tell whether EXPRESSION_ORPHAN counts on both sides.
   - Line anchoring: UNKNOWN_ROLE sits on the ROLE line (`purge.zayn:4`), UNKNOWN_SIGNAL on the SIGNALS line (`:3`), but INVALID_TONE on the DEFINE line (`purge.zayn:7`, TONE is line 8) and DECORATIVE_ANIMATION on `:1`. The rule for which line a finding carries is not stated, and the court's "compares the two sets" does not say whether line and subject are compared.
3. **Where I doubted.** "Every expression declaration traces to an intent, or it is an error." Plates 11.8, 11.10 and 11.11 are FEEDBACK declarations with MOTION or TONE and no SATISFIES, and they are clean. The page settles it later ("The verifier holds two expression fields, SIGNALS and ROLE"), but the principle reads wider than the code; a scope line under EXPRESSION_ORPHAN would close it.
4. **What was mine.** The five roles, stated once, each with its promise: I could restate them without looking. The stage table of the six strata is the conformance map I wanted. Got it, short of the two enumerations above.
5. **Verdict:** ready after the items above. The exercise asks for a word from a list the page does not give. Stopped me most: "five statuses, each with the rule's own meaning".

## For the part

- **Hand-over.** Ch10 ends on The Second Founding and "the next chapter takes them one by one"; ch11 opens on it. Ch11 ends on Part V and its channels. Both hold.
- **Contradictions.**
  - Ch10 plate 10.3 reports only "MISSING_UNDO approve_payment" for a reversible control lacking UNDO; ch11's contract line: "ROLE_PROMISE_BROKEN ... A reversible control keeps no reachable UNDO."
  - Ch10 and ch11: "constitution of 123 rules"; ch10: "Rule 129, The Action Is the Last Thing to Go".
  - Ch10 Where it stands: LAYOUT_DISPLACEMENT "designed"; the same line: "measured by the audit's K22".
- **Clearest plate:** 11.3 and 11.4, archive as a button then as a promise: one field, one code, one repair, and the five promises stated just above.
- **Hardest plate:** 11.9, three findings on two declarations, two of them anchored to a line I could not predict, and a repair whose TONE word I had to take from the answer.
- **What I take away.** I could write the declaration side of the expression layer from these pages: the five roles, the binding rule's scope, the finding codes with their contract sentences, the fixtures by name. To pass the suite I still need the five statuses, the TONE list, the rule for a finding's line, and whether ROLE_PROMISE_BROKEN yields to MISSING_UNDO. To plug an audit in, I need the shape of LAYOUT_DISPLACEMENT.
