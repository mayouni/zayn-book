# Part IV, The Expression: read from the AI agent's door

Reader: an AI model that will write or check declarations from what the book says. Pages: chapter 10, then chapter 11, as built
(`.cache/as-read/`). Read twice, the second time with the brief's questions. Date of the reading: 2026-11-27.

## Chapter 10, What a declaration cannot see

1. **What I remember.** One clean declaration stands under a careful drawing and under one with seven faults, and the verifier
   answers clean to both, at level 2 and at level 4. Rules 79 and 119 each split: the declaration's half is refused
   (MISSING_UNDO, ROLE_ACTS_WITHOUT_CONSEQUENCE) and the drawing's half belongs to the audit's K-checks or to a person.
2. **Where I lost the thread.**
   - Door paragraph: "Zayn's constitution of 123 rules", then "Rule 129, The Action Is the Last Thing to Go" (The line moves).
     A count of 123 and a rule numbered 129 cannot both be read literally; I cannot tell whether numbers have gaps or the count is old.
   - One rule, two halves, Plate 10.3: a `ROLE reversible` control with no UNDO gets MISSING_UNDO only. Chapter 11's court defines
     ROLE_PROMISE_BROKEN as "A reversible control keeps no reachable UNDO." Plate 10.3 is that case, and that code does not fire. No
     page says which code wins, or when each fires.
   - MISSING_UNDO's contract text: "SATISFIES holds ACT, ALWAYS_REACHABLE lacks UNDO." Plate 10.7 has both conditions and is clean
     because `ROLE irreversible`. The exemption is shown by example only; on this page it is not stated as a rule.
3. **Where I doubted.**
   - "Designed: the contract's kind at level 4, LAYOUT_DISPLACEMENT, measured by the audit's K22." K22 sits in the table of checks
     the audit runs, so I cannot tell whether K22 is built and the finding designed, or both designed.
4. **What was mine.** The boundary: which faults a declaration can carry and which it cannot. I got it: I could list the seven faults
   and say for each whether the verifier, a K-check or a person decides it. I did not get one exact rule for undo across roles.
5. **Verdict: ready after the items above.** The rule count against Rule 129, and MISSING_UNDO against ROLE_PROMISE_BROKEN.
   Stopped me most: "a `ROLE reversible` control ... ALWAYS_REACHABLE [CANCEL]" answered MISSING_UNDO alone (Plate 10.3).

## Chapter 11, The strata of expression

1. **What I remember.** Between the intent and the drawing sit six strata, functions and not appearances: two are language fields
   (SIGNALS, ROLE) with their own refusals and the orphan rule, three are carried by older fields (MOTION/REPORTS, FEEDBACK/TONE,
   NAV_GRAPH/STEPS), and tempo stands only in the law. Each built one is run, refused then repaired.
2. **Where I lost the thread.**
   - Signal: "five statuses, each with the rule's own meaning" names only danger and warning. I could not write a SIGNALS list
     beyond those two from this page.
   - In your hands, Plate 11.10: the repair uses `TONE critical`, but this page gives no value of TONE's closed list. Chapter 7 is
     named, but the exercise needs the list now; an agent would have to guess "critical".
   - The principle: "Every expression declaration traces to an intent, or it is an error." Plates 11.8 and 11.11 are FEEDBACK
     declarations with MOTION or TONE and no SATISFIES, clean. The scope is given later ("The verifier holds two expression fields,
     SIGNALS and ROLE"), but the principle reads wider than the run.
   - Plate 11.9: INVALID_TONE is reported at `purge.zayn:7`, the DEFINE line, while UNKNOWN_ROLE is at line 4 and UNKNOWN_SIGNAL
     at line 3, the field's line. An agent mapping findings to lines needs to know which kinds point at the field and which at the
     declaration.
   - Plate 11.9: nothing says how FEEDBACK `purge_done` is bound to INTERACTION `purge_archive`; they are two declarations in one file.
3. **Where I doubted.**
   - "Its contract decides three kinds of finding from SIGNALS and seven from ROLE." The pages name about six of the ten
     (UNKNOWN_SIGNAL, EXPRESSION_ORPHAN, UNKNOWN_ROLE, ROLE_PROMISE_BROKEN, ROLE_ACTS_WITHOUT_CONSEQUENCE, IRREVERSIBLE_CLAIMS_UNDO,
     ROLE_UNDECLARED, and whether MISSING_UNDO counts is unclear). A list would make the count something I can check.
   - "Zayn's role names the consequence, and the verifier holds the control to it." This is shown for reversible, irreversible and
     inert. No plate shows `navigate` ("never what is true") held to its promise.
4. **What was mine.** The closed lists I write from. ROLE's five values are stated once, exactly, with a meaning each: I could
   write them without looking. SIGNALS (two of five) and TONE (none) are not.
5. **Verdict: ready after the items above.** The two lists the exercise needs, and the ROLE_PROMISE_BROKEN case.
   Stopped me most: "five statuses, each with the rule's own meaning", followed by two of the five.

## For the part

- **Hand-over.** Chapter 10 ends on The Second Founding, which "the next chapter takes ... one by one", and chapter 11 opens on
  it. Chapter 11 ends on Part V. Both hold.
- **Contradictions.**
  - Chapter 10, Plate 10.3 (reversible, no UNDO): "error MISSING_UNDO approve_payment" only. Chapter 11, court: "ROLE_PROMISE_BROKEN
    ... A reversible control keeps no reachable UNDO." Either the precedence is stated, or a plate shows when each code fires.
  - Both chapters: "constitution of 123 rules". Chapter 10: "Rule 129"; chapter 11: "Rule 125 entered the law". Say once how the
    numbers relate to the count.
  - Chapter 10 counts LAYOUT_DISPLACEMENT as designed and "measured by the audit's K22", yet K22 is in the table of checks the
    audit runs. This is a tension rather than a contradiction.
- **Clearest plate:** 11.3 and 11.4. `ROLE button` is refused with "not one of the five promises", and the repair to `reversible`
  follows from the list given three lines above. I could produce the repair without reading it.
- **Hardest plate:** 11.9 and its repairs. Three findings plus a possible fourth, two of them on closed lists the page does not print,
  and a line number that points at the declaration rather than the field.
- **What I take away.** A declaration carries meanings, promises and reported states, never paint or widgets. The verifier refuses
  a colour word in SIGNALS, a widget word in ROLE, an expression field with no intent, motion that reports nothing, and an undo
  that the role makes false. Everything about size, place and colour goes to the audit or to a person. To write declarations from
  these pages alone, I still need the five statuses, the TONE list, the full list of ROLE-derived codes, and the undo rule stated
  once across MISSING_UNDO, ROLE_PROMISE_BROKEN and IRREVERSIBLE_CLAIMS_UNDO.
