# Part III, from the door of the AI agent

## Chapter 6, Intent first

1. **Remember.** A declaration starts from what its user does, in 22 verbs. Proof: NAVIGATE refused; an inventoried element with no verb refused at level 3.
2. **Lost.** Rule 130's card: "Set" and "Tier" ("machine"), never said.
3. **Doubted.** The verbs, in their families: "must keep true in every declaration"; plate 6.1 is clean and keeps nothing reachable.
4. **Mine.** The closed verb list and the level 3 trace rule: got both, exactly.
5. **Verdict.** `ready after the items above`: the invariants read as checks, and the verifier makes only some. Stopped most: "Pause, resume, and exit are always reachable; a trapped flow is unconstitutional."

## Chapter 7, Ten declarations, one grammar

1. **Remember.** A declaration is DEFINE, kind, name, fields, nothing nested; 10 kinds, 5 closed lists. Proof: five plates refused from the file alone.
2. **Lost.** A field it does not know: "two lines where chapter 8's had three"; chapter 8 is unread. Shown, never said: ACTOR, LABEL, TARGET, DENSITY, MOTION; "in the form it is written".
3. **Doubted.** "It fits on one page, and this chapter is that page": no list of the fields each kind carries. "The other words are yours": `kiosk` is lowercase, and refused.
4. **Mine.** The grammar, once: got five sentences and five lists, not the fields by kind.
5. **Verdict.** `not ready`: without the fields by kind I can write only what a plate showed. Stopped most: "it passes over a kind it does not define, as the exercise below shows."

## Chapter 8, The refusal

1. **Remember.** A refusal is a code, a subject and the law's citation, as report, JSON and exit code. Proof: plate 8.3, four findings in one run.
2. **Lost.** In your hands: "read the refusal you get"; its code is never named.
3. **Doubted.** The principle: "in which declaration, and under which law"; chapter 7's UNKNOWN_FIELD names neither.
4. **Mine.** Each check's exact condition: got it, the report's second line names the fields read.
5. **Verdict.** `ready after the items above`: the most exact of the four. Stopped most: "it covers any feedback that moves or takes a tone and reports nothing."

## Chapter 9, One verdict, two verifiers

1. **Remember.** Findings are filed at four levels; a verifier answers for its own. Proof: one file clean at level 2, refused at level 3; the runner's 77 of 77.
2. **Lost.** VISIBLE_STATE (plate 9.4), never said; "Cross-pillar"; "contract" v1.11 and "diagnostic-contract v1.2.2", undistinguished.
3. **Doubted.** "A consequential act names no actor": consequential is undefined.
4. **Mine.** What conformance asks: got it, "the set of codes it reports equals the expected set, exactly".
5. **Verdict.** `ready after the items above`: two level 3 checks are named and never stated. Stopped most: "One of the two findings has no line number: say why before you read on."

## The part

Each page hands over; chapter 7 alone leans on a later page. Clearest plate: 8.1, whose sentence names both fields read. Hardest: 7.10, clean by assertion. I take away the verbs, the kinds, the closed lists, eight checks and the pass rule; I cannot yet write a kind no plate showed.

## Rules I could state exactly

Chapter numbers in brackets.

Grammar (7)
1. File: declarations and `//` comments to line end.
2. `DEFINE` kind name `(` fields, comma-separated `)`; nothing nests.
3. Field: keyword, then `[names]` or one value (name, quoted text, number, true, false).
4. Field order free; a field once per declaration (DUPLICATE_FIELD); a name once within a kind (DUPLICATE_DECLARATION).
5. Kinds: INTENT_FLOW, FORM, WIZARD, SCREEN, COMPONENT, NAV_GRAPH, WORLD_VIEW, INTERACTION, FEEDBACK, VIBE.
6. Unknown keyword: UNKNOWN_FIELD. Field on a kind that does not carry it: FIELD_MISPLACED.
7. PERSPECTIVE, TONE, SURFACE_AS, SIGNALS, ROLE: the table's values only.

Verbs (6)
8. SATISFIES and ALWAYS_REACHABLE: the 22 verbs only (UNKNOWN_INTENT).
9. INTENT_FLOW without SATISFIES: warning INTENT_FLOW_NO_SATISFIES.

Level 2 (8)
10. ACT in SATISFIES needs UNDO in ALWAYS_REACHABLE (MISSING_UNDO), or ROLE irreversible.
11. ACT needs CANCEL reachable (MISSING_CANCEL).
12. SELECT with ACT needs CONFIRM (SELECT_ACT_COLLAPSE).
13. STEPS needs EXIT reachable (TRAPPED_FLOW).
14. FEEDBACK with TONE needs REPORTS (DECORATIVE_ANIMATION).
15. ROLE irreversible forbids UNDO (IRREVERSIBLE_CLAIMS_UNDO).

Level 3 (6, 9)
16. `zayn check FILE --level 3 --symbols TABLE`; the table is JSON, lists `entities`, `actors`, `state`, `elements`; a check without its list says nothing.
17. Each name in `elements` needs a declaration of that name with SATISFIES (INTENT_ORPHAN).
18. With `actors` given, a consequential act needs ACTOR (HIDDEN_AUTHORITY).

Reports (8, 9)
19. Error refuses, warning passes; every finding in one run; exit 0, 1, and 2 for an unreadable file.
20. Each entry of `diagnostics`: `code`, `severity`, `message`, `span`, `cites`, `language`, `level`, `subject`.
21. A fixture passes when the reported codes equal the expected set; line, wording and order are free.

Not extractable: the fields of each kind; list or single value per field; a name's characters; each code's level; the 14 codes of 40 that no page names.

## One rule, two statements

- Unknown kind. (6) WIDGET is warned, "the verifier reports the word where it is written". (7) SCREN is "passed over, with whatever it holds".
- SATISFIES. (7) "the two fields every kind carries". (6) Asked of "the one kind", the flow.
- FEEDBACK. (7) "it must report a state". (8) Only when it "moves or takes a tone".
- FORM. (7) It points at its flow "in place of saying the flow again". (6) That form is an INTENT_ORPHAN.
- EXIT. (6) "Pause, resume, and exit are always reachable". (8) Asked only of "A multi-step flow".
- List order. (7) "a named sequence of intents". (6) Order "is what the task model adds".
- Report's first line. (8) "the name of the declaration". (6) "what it is about".
