# Part IV read from the programmer's door

Reader: the programmer. Pages: chapter 10, then chapter 11, as built (`.cache/as-read/`). Read twice, the second time with the brief's questions.

## Chapter 10, What a declaration cannot see

1. **What I remember.** One declaration runs clean under a careful drawing and under one with seven faults, because a declaration names no widget, colour or size. Rules 79 and 119 each split in two: the verifier refuses the half the declaration states (MISSING_UNDO, exit 1), and the painted-page audit (K01 to K37) or a person handles the drawn half.
2. **Where I lost the thread.**
   - "One declaration, two drawings", before the command line: "a check of level 3 also needs a symbol table ... this file needs none". Does `--level 4` skip level 3 checks when there are no symbols, or run them? Then `clean ... at level 4` prints with no sign that the level 4 checks did not run. I cannot tell a level 4 pass from a level 4 skip.
   - "What reads the drawing": "The audit's larger mode runs 32 of them". "Larger mode" is not defined, and the page does not say how the audit is invoked.
   - Line numbers in reports: `approve.zayn:1` (the DEFINE line) for MISSING_UNDO, but `send.zayn:4` (the ROLE line) for IRREVERSIBLE_CLAIMS_UNDO. The page does not say what a report's line points at.
3. **Where I doubted.**
   - "The law is Zayn's constitution of 123 rules", yet the same page cites Rule 129, and chapter 11 cites Rule 125. If the numbering has gaps or runs past the count, the page needs to say so.
   - "measured by the audit's K22": the table files K22 under "the page in time". A layout-displacement kind measured by a timing check needs one clause of explanation.
   - "Five of the seven faults meet a check" is followed by seven check codes, and "Invalid input!" is matched to K19 only by inference. I had to rebuild the pairing myself.
4. **What was mine.** Exact behaviour on the declaration side: report text, exit 0 and 1, codes with level and severity in the court box. I got it for Rules 79 and 119. I did not get what `--level 4` really does.
5. **Verdict.** `ready after the items above`. The run evidence is solid, but the level 4 line and the rule count leave a programmer unsure what was checked. The sentence that stopped me most: "a check of level 3 also needs a symbol table, the list of what the system knows, and this file needs none".

## Chapter 11, The strata of expression

1. **What I remember.** The Second Founding names six strata: structure, signal, role, motion, message, tempo. Two (SIGNALS, ROLE) are built as fields with their own refusals, three are carried by older fields, and tempo is held in the law. Each refusal was run before its repair: UNKNOWN_SIGNAL for `red`, UNKNOWN_ROLE for `button`, EXPRESSION_ORPHAN for a ROLE with no SATISFIES, DECORATIVE_ANIMATION for a MOTION with no REPORTS.
2. **Where I lost the thread.**
   - "Signal: a meaning, never a colour": "five statuses". Only danger and warning are named, so I cannot write the other three.
   - "Message, structure and tempo": "the verifier refuses a word outside it, INVALID_TONE". The TONE list is left to chapter 7. Then Plate 11.10 repairs with `TONE critical`, and the exercise needs that list now. That is not a fair forward pointer.
   - "Motion: the change it reports": `slide` and `shake` pass, and "The proposal designs a closed list of motions". So does MOTION accept any token today? `MOTION banana` would answer the question, and the page does not run it.
   - "Its contract decides three kinds of finding from SIGNALS and seven from ROLE". The ten are not listed. The court shows four, and I could gather others from chapter 10.
   - The levels: the court lists UNKNOWN_SIGNAL and UNKNOWN_ROLE at "level 1", but every report says "at level 2". What the default level is, and whether level 1 runs these checks, is stated nowhere in the part.
3. **Where I doubted.**
   - Rule 112 is "filed under judgment, the tier where a person decides", yet the verifier refuses DECORATIVE_ANIMATION citing Rule 112. Chapter 10's two halves explain it, but this page does not say so.
   - "Each one built refuses what it names" is larger than the motion stratum shows, since a shake is accepted once it reports anything.
   - The INVALID_TONE report has no rule line, and UNKNOWN_ROLE cites only "Article II". Is that deliberate? The page does not say.
4. **What was mine.** Closed vocabularies with exact refusals, and the binding rule (EXPRESSION_ORPHAN) as a real check. I got ROLE fully (five values, each defined). SIGNALS and TONE were only partly given.
5. **Verdict.** `ready after the items above`. The exercise cannot be solved from the page without the TONE list. The sentence that stopped me most: "Its TONE names the register in which the system speaks, from a closed list".

## For the part

- **Hand-over.** Chapter 10's last paragraph hands the drawing's differences to the Second Founding, and chapter 11 opens on it. Chapter 11 hands to Part V. Both bridges hold.
- **Contradiction.** Chapter 10, Plate 10.3: `ROLE reversible` with ACT and no UNDO gets only "MISSING_UNDO approve_payment". Chapter 11's court: "A reversible control that keeps no undo within reach, refused" as ROLE_PROMISE_BROKEN, "A reversible control keeps no reachable UNDO." By that definition Plate 10.3 should also get ROLE_PROMISE_BROKEN, and it does not. Either one finding covers the other when ACT is present, or the fixture differs (no ACT). The book needs to say which, preferably with a plate. That fixture also has no lawful twin in the court.
- **Contradiction.** "123 rules" (both chapters' openings) against Rules 125 and 129.
- **Clearest plates.** 11.3 and 11.4 (`button` refused, `reversible` clean). They show the field's role next to Zayn's in two lines. Next clearest: 10.3 and 10.4.
- **Hardest plate.** 11.10. It needs the TONE list (missing), and it relies on MOTION being an open word today (unstated).
- **What I take away.** I can predict the verifier on undo, roles, signals and orphan expressions, and I know which checks belong to the audit, not the verifier. I cannot yet predict what `--level 4` checks, which TONE and SIGNALS words pass, or why a reversible control without undo gets MISSING_UNDO rather than ROLE_PROMISE_BROKEN.
