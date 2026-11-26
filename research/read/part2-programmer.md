# Part II, "The Heritage", read from the programmer's door

Reader: the programmer (exact behaviour: what the command prints, what it exits with, what a field accepts). Pages: chapters 3, 4, 5, as read, in order, twice. Date of the reading: 2026-11-25.

## Chapter 3, What the field wrote

1. **What I remember.** The field's heuristics (Nielsen, Shneiderman, the gulfs, Tufte) map onto numbered rules; where a declaration can state the rule, the verifier refuses by code (INVISIBLE_STATE, MISSING_UNDO, SELECT_ACT_COLLAPSE, UNKNOWN_SIGNAL), and size, count of choices and grouping stay with the painted page. Proof: six refused/clean pairs plus TARGET_SIZE refused as an UNKNOWN_FIELD.
2. **Where I lost the thread.**
   - "Given no table, the same file runs at level 2." (State the user must see): I am never shown how the table is passed. The plate header says `orders.json`, but no command line is printed, so I cannot reproduce plates 3.1 to 3.3 or the exercise. Chapter 4 prints `zayn check notice.zayn --level 4`; chapter 3 needs the same for level 3 with its table.
   - Does `--level 3` with no table fail, warn, or fall back silently? The page says "chapter 25 shows that silence", which tells me it is silent, but not what is printed or exited.
   - The contract lists UNKNOWN_SIGNAL at "level 1"; level 1 is never said (only 2 and 3 are).
3. **Where I doubted.** "The verifier checks Rules 82, 79, 26, 51 and 16 by name" (The map): 26 is shown in the court (MISSING_CANCEL); 51 has no code anywhere on the page. Also the tiers: Rule 16 and Rule 118 are filed "judgment", yet the machine refuses under both. The page explains it for 118 ("judges a word of the list, never a colour"), not for 16.
4. **What was mine.** Exact reports with codes, line numbers, citation lines and exit codes. Got it: I checked every line number against its fence (overdue.zayn:3, invoices.zayn:6) and they hold; the INVISIBLE_STATE line carries no line number, and the page says why.
5. **Verdict:** ready after the items above; the level 3 run cannot be reproduced. Stopped me most: "Given no table, the same file runs at level 2."

## Chapter 4, The instruments of the field

1. **What I remember.** Each field instrument (WCAG criterion, tokens, Storybook, a JSX linter, Playwright screenshots, CLS) reads one object; a declaration is another object, and two drawings alike can carry different promises (ROLE inert vs reversible). The verifier owns the declaration, the audit owns the painted page; level 4 still reads only the declaration.
2. **Where I lost the thread.**
   - Plate 4.3's citation of Rule 112: "Rule 112 lists following a link and opening a panel as acts of that class." I could not reconstruct why a motion rule is cited on a card.
   - "a run at --level 4 runs every check the verifier holds" (Clean, and the drawing still owes): does that include the level 3 checks, and with no table do they skip silently? Same gap as chapter 3.
   - The court's `field-misplaced-lawful.zayn` stands for the notice screen; its name says nothing I was told.
3. **Where I doubted.** Plates 4.3, 4.4 and 4.8: an INTERACTION that ACTs with ALWAYS_REACHABLE [UNDO] and no CANCEL runs clean, while chapter 3's court refuses "a flow that acts with no way to cancel it" (MISSING_CANCEL). I infer MISSING_CANCEL reads INTENT_FLOW only, and SELECT_ACT_COLLAPSE reads both kinds; no page says which check reads which kind of declaration. Also the message on `ROLE navigate` says "A control promising to change nothing", which is inert's promise, not navigate's.
4. **What was mine.** The exit code at level 4 and the scope of "clean". Got it: "That verdict is the declaration's." The exercise (three findings, two lawful repairs that mean different things) is the best exercise in the part.
5. **Verdict:** ready after the items above. Stopped me most: "Rule 112 lists following a link and opening a panel as acts of that class."

## Chapter 5, The road sign

1. **What I remember.** The Vienna Convention closes its vocabulary, explains why (strangers, at speed) and amends by memorandum; Zayn closes its media, verbs and statuses the same way. Proof: signage carries LOCATE, DISCOVER, UNDERSTAND only, so ACT/UNDO/CANCEL/EXIT/READ are refused as VERB_NOT_CARRIED, a medium outside the list is UNKNOWN_MEDIUM, a sixth status is UNKNOWN_SIGNAL.
2. **Where I lost the thread.**
   - How a VIBE binds to an INTENT_FLOW: nothing in plate 5.1 links `lobby_sign` to `open_the_gate`, yet the report says "on signage". I infer the VIBE applies to the whole file; the page (and chapter 4) should say so, and what two VIBEs in one file do.
   - "The verifier judges whether a status can be perceived in a medium whose rendering the data records" (after plate 5.7): I read it three times.
   - "10 media": I am given three (signage, print, visual), never the list.
3. **Where I doubted.** Every VERB_NOT_CARRIED cites "Rule 82 · Perceivable State · Article II"; why a rule on perceivable state refuses an act on a sign is never said.
4. **What was mine.** A closed list checked as data, with one word changing the verdict. Got it: plates 5.3 and 5.4 differ by `signage`/`print` and flip on READ.
5. **Verdict:** ready after the items above. Stopped me most: "Rule 82 · Perceivable State · Article II".

## The part

- **Hand-overs.** Each page hands over cleanly: chapter 3 ends on "the instruments of the field", chapter 4 on "the road sign", chapter 5 on "the inversion".
- **Contradiction.** Chapter 3 prints "Rule 82 · Perceivable State · Article III · the right to know"; chapter 5 prints "Rule 82 · Perceivable State · Article II". If the article on a citation line belongs to the diagnostic and not to the rule, the book never says so; a programmer parsing the report reads it as the rule's article and sees two.
- **Smaller seams.** Clean prints "0 violations", a refusal prints "1 error(s), 0 warning(s)": two words for one count. MISSING_CANCEL's scope (ch3 court) against the clean INTERACTIONs with no CANCEL (ch4).
- **Clearest plate:** 5.3 with 5.4, one medium word flips one verb. **Hardest:** 3.1 to 3.2, because the run that decides the verdict (the table, the level) is the one thing not printed.
- **What I take away.** I could restate the three closed lists (22 verbs, 10 media, 5 statuses) and the four refusal codes of chapter 3 without looking, and I know a clean report at any level speaks for the declaration only. I could not yet run a level 3 check, nor say which checks read an INTERACTION.
