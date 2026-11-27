# Appendices B, D, E, G, H read from the door of the AI agent that reads the book as data

Read 2026-11-27, from `.cache/as-read/` (build of 2026-11-27 22:19). Read once whole, then again entry by entry, every list counted.

## Appendix B: The grammar and the ten declarations

1. **What I remember.** The grammar in EBNF, 22 verbs in six families, 10 kinds with their own fields, five closed lists, four levels holding 10, 25, 4 and 1 kinds of finding. The verbs sum to 22 and the ten SURFACE_AS words match Appendix E's ten media.
2. **Lost the thread.** "The fields it carries, beyond those every kind carries": I'm never told which fields every kind carries. By elimination the grammar's keys left over are SATISFIES, ALWAYS_REACHABLE, INTENT_FLOWS, SIGNALS and ACTOR. The page should state that list, not leave me to infer it.
3. **Doubted.** "A declaration names verbs from these lists". The page never says *in which field*, and no field in the grammar takes a verb. "a keyword may not be an identifier": are the verbs keywords? If they are, `ref-items = identifier` cannot hold them. DENSITY and MOTION are missing from the closed lists, so I can't tell whether they are open, numeric or closed.
4. **What was mine.** A grammar I could generate against. Mostly yes: I could write a well-formed file. I could not write a well-placed field.
5. **Verdict: ready after the items above.** Stopped most by: "The fields it carries, beyond those every kind carries".

## Appendix D: The checks of the painted page

1. **What I remember.** 37 checks, K01 to K37. 32 are read on the painted page and five on the site's files (K18, K19, K20, K21, K30: I counted five). Each has what it reads, when it fails and its causes.
2. **Lost the thread.** "The causes are the letters of the corpus of corrections, as chapter 2 gives them." Thirteen letters (T S I E F X B L H N W M P) go undecoded here. Appendix E then reuses P and T for *perceive* and *trust*, so the same letter means two things across two adjacent appendices.
3. **Doubted.** A failure condition I can't evaluate: K01 "a size outside the six tokens" (the tokens are not given); K09 "the culture's tokens"; K18 "the menu's three faults"; K19 "a paragraph over about 70 words"; "at six widths" with only 375 and 768 named. The record IDs (Z391, Z432, ZANE-READER-MENUPOS-01) are unexplained, and "ZANE" reads as a typo for ZAYN. Appendix B gives level 4 one kind of finding, yet the audit runs 32 checks: how checks map to findings is not said.
4. **What was mine.** A checklist I could apply. Half: the conditions with numbers (K02 7:1, K17 48 by 48 px, K24 24 px) yes; the ones that point to tokens or faults kept elsewhere, no.
5. **Verdict: ready after the items above.** Stopped most by: "The causes are the letters of the corpus of corrections, as chapter 2 gives them."

## Appendix E: The grid as data

1. **What I remember.** Six activities own the 22 verbs (perceive and trust own none). Ten media carry each verb fully, at a cost or not at all. The grid counts the rules placed on each cell. I recounted every medium's lists against its three numbers, and all ten agree.
2. **Lost the thread.** The row "any" is not one of the ten media and is not in SURFACE_AS; the page never says what it is.
3. **Doubted.** "closed means that the medium carries none of the verbs the activity owns." Perceive and trust own no verbs, so by this sentence every medium's P and T cells are closed, yet all of them hold numbers. The rule as written contradicts its own table. The visual row alone holds 128 placements against a law of 123 rules (Appendix G), so a rule can be placed on several cells; the page should say so. "May carry a surface alone" is a column with no definition and no consequence.
4. **What was mine.** Which verb a medium refuses, and so when VERB_NOT_CARRIED fires. Yes, exactly and completely.
5. **Verdict: ready after the items above.** Stopped most by: "closed means that the medium carries none of the verbs the activity owns."

## Appendix G: Glossary

1. **What I remember.** About forty terms, each in one or two sentences with its chapter. The lists in it (media, roles, rights, strata) match Appendices B and E word for word.
2. **Lost the thread.** "Level. A stage of what a check needs to read". Two entries up, "Check" is K01 to K37, which are all level 4, so the word means two things. Terms missing that these appendices use: *activity*, *family* (of verbs), *kind* (of declaration), *cause*, *token*, *suite*, *severity*.
3. **Doubted.** "Tier. Two senses." For a reader that maps one word to one thing, this is the fault the glossary should remove, not record. Symbol table: "its entities, actors and states", where Appendix B says "entities, actors, state and elements". Exit code "0 when the file passes, 1 when it is refused": a file with warnings only is not placed. "Culture" in Appendix D ("both of the site's cultures") is not the "Culture of interaction, vibe" here.
4. **What was mine.** One meaning per term. Mostly yes; there are two collisions (check, tier) and seven gaps.
5. **Verdict: ready after the items above.** Stopped most by: "Level. A stage of what a check needs to read".

## Appendix H: The book as data

1. **What I remember.** The sources (src/en, structure.yaml, research/), the pin, the run against the reference verifier, and the record data/book-run.json. Every page's declarations and fixtures all answered as expected.
2. **Lost the thread.** "Declarations run, kept": the word *kept* is never defined. I take it to mean "answered as the page promised", but the page should say so.
3. **Doubted.** "the answer the page expects at its foot": the notation of that answer (`//-->`) is not given, and neither is the verifier's command or its level flag. I could not re-run one plate from this page alone. It says Zayn is read "by the commit's hash" but prints only "adaecc271".
4. **What was mine.** Enough to check a page against its sources myself. In part: I learn where everything is, but not how to run it.
5. **Verdict: ready after the items above.** Stopped most by: "the answer the page expects at its foot."

## For the part

- **Hand-over.** B leads to E through SURFACE_AS = the ten media, and B's level 4 leads to D's audit (both name tools/ui-audit.html). G closes the vocabulary and H closes the method.
- **Contradictions.** E: "closed means ... none of the verbs the activity owns" against its own P and T columns. B "entities, actors, state and elements" against G "entities, actors and states". D's cause letters P and T against E's columns P and T. B's level 4 "Kinds of finding: 1" against D's 32 painted checks, with no line joining them.
- **Clearest:** E's media lists. All ten rows sum to 22 and agree with their counts. **Hardest:** B's kinds table, because of its unstated "every kind" fields.
- **What I take away:** I can write a well-formed declaration and predict VERB_NOT_CARRIED exactly. I can't yet place every field on its kind, name where a verb goes, or decode a check's causes without leaving the appendices.
