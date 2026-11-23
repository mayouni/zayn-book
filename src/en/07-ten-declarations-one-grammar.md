---
id: ten-declarations-one-grammar
part: 3
number: 7
title: "Ten declarations, one grammar"
stage:
  built: "a grammar of {{n:lang.kinds}} kinds of declaration and {{n:lang.lists}} closed lists of values, specified at version {{n:lang.version}}; the grammar's own refusals, decided from the file alone: a field it does not know, a field on a kind that does not carry it, a field or a declaration written twice, a value outside a closed list"
  designed: "the grammars of motion, message and tempo, the fields of expression that follow `SIGNALS` and `ROLE`"
  next: "the law served to an AI model while it generates"
status: draft
research: research/ch07.md
fixtures: [clean-full, comments-and-formatting, unknown-field, field-misplaced, field-misplaced-lawful, field-misplaced-read-anywhere, duplicate-field, duplicate-declaration, invalid-tone, invalid-perspective, unknown-medium, unknown-medium-lawful, unknown-signal, unknown-signal-lawful, unknown-role, unknown-role-lawful, foreign-pillar-ignored]
---

The grammar of Zayn is the set of rules that say what a declaration may be made of. It fits on one page, and this chapter is that page. I give the grammar in five sentences. I show each of the {{n:lang.kinds}} kinds of declaration once, in files the verifier accepts. Then I make the grammar refuse: a field it does not know, a field in the wrong place, a field written twice, a value from outside a closed list.

Chapter 6 gave the verbs and two of the fields every kind carries, `SATISFIES` and `ALWAYS_REACHABLE`. The verifier is the program that checks a declaration against the law, Zayn's constitution for interfaces.

## The field

The field has written languages that describe an interface above the widget, and it has written them for a long time. XForms, a W3C Recommendation of 2009, describes a form with an architecture that "separates presentation, purpose and content", and names its controls by purpose: an input, a choice of one, a trigger. UIML, an OASIS specification of the same year, calls itself a meta-language "for describing user interfaces". SCXML, a W3C Recommendation of 2015, is a language of state machines: what state a system is in, and which events move it.

More recently the field is writing names for the values of a drawing. The Design Tokens format, a draft report of its community group, defines a token as information with "a human readable name", and its types include a colour, a dimension and a font family.

Each of these is a description that a tool reads. Each was read at its source on 23 November 2026, and Appendix F lists them.

## The principle

**A declaration is made of two sorts of words: the names its author chooses, and the words the language holds. The second sort is a closed list, and each word of it has its place.**

The verifier's contract gives the reason in one clause: "a vocabulary that anyone may extend cannot be checked".

## The grammar, in five sentences

A file is a list of declarations, and of comments that begin with `//` and run to the end of the line.

A declaration is the word `DEFINE`, a kind, a name, and its fields between parentheses, separated by commas.

A field is a keyword followed by a list of names between square brackets, or by one value: a name, a text between quotes, a number, `true` or `false`.

The order of the fields is free, a field appears once in a declaration, and a name is used once within a kind.

Nothing nests: the value of a field is never another declaration.

That is all of it. The words in capitals belong to the language and are written in capitals. The other words are yours, except the values of the closed lists, which this chapter gives further down.

## The kinds, in three files

Three kinds say how a user moves.

::: plate A flow, a form, a wizard
```zayn payments.zayn
DEFINE INTENT_FLOW approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR approver
)

DEFINE FORM payment_form (
  INTENT_FLOW approve_payment
)

DEFINE WIZARD onboarding (
  SATISFIES [UNDERSTAND, CONFIRM],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  STEPS [identity, contact, review]
)
//--> clean
```
In words: An approver selects a payment, confirms, and it is sent, with undo and cancel within reach. A form serves that flow. A newcomer is taken through three steps, identity, contact and review, and can cancel or leave at each one.
:::

An `INTENT_FLOW` is a flow: the intents a user goes through, under one name. The verifier reads the list as a set: which verbs it holds. A `FORM` is a surface where a user enters something, and it points at the flow it serves in place of saying the flow again. A `WIZARD` is a flow with named steps in order.

Four kinds say where a user is.

::: plate A screen, a component, a menu entry, a map
```zayn places.zayn
DEFINE SCREEN payments_home (
  SATISFIES [DISCOVER, LOCATE, SCAN]
)

DEFINE COMPONENT balance_card (
  SATISFIES [READ]
)

DEFINE NAV_GRAPH payments_entry (
  SATISFIES [LOCATE],
  LABEL "Payments",
  TARGET payments_home
)

DEFINE WORLD_VIEW branch_map (
  SATISFIES [DISCOVER, LOCATE],
  PERSPECTIVE top_down,
  VISIBLE_ENTITIES [branch, payment]
)
//--> clean
```
In words: On the home of payments a user discovers, locates and scans. A part of it shows the balance, which a user reads. A menu entry labelled Payments leads there. A map shows branches and payments from above, for a user who discovers and locates.
:::

A `SCREEN` is a place a user can be. A `COMPONENT` is a part of a surface with a meaning of its own: it says what a user does with it, and never what it looks like. A `NAV_GRAPH` says how surfaces connect. In a menu, each entry is one `NAV_GRAPH`, and chapter 26 declares a whole menu. A `WORLD_VIEW` is a space with things in it, seen from a stated point.

The last three kinds are a control, a message and a culture.

::: plate A control, a message, a culture
```zayn answers.zayn
DEFINE INTERACTION confirm_gesture (
  SATISFIES [CONFIRM],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)

DEFINE FEEDBACK payment_sent (
  TONE informational,
  REPORTS [transfer_state]
)

DEFINE VIBE operator_dense (
  DENSITY compact,
  SURFACE_AS terminal
)
//--> clean
```
In words: One control confirms, and it promises that what it does can be taken back. One message, in an informing tone, reports the state of the transfer. One culture is dense, and it is drawn on a terminal.
:::

An `INTERACTION` stands for one control and can state its role, the promise the control makes. A `FEEDBACK` is what the system says back, and one that takes a tone or moves must report a state. A `VIBE` is a culture of use: how dense, on which medium, with what motion. Chapter 14 is about cultures.

Three files, {{n:lang.kinds}} kinds, and the verifier accepts all three!

## A field it does not know

Now the refusals. The first is the plainest: a keyword that is not the language's.

::: plate A colour, written into a message
```zayn deploy.zayn
DEFINE FEEDBACK deploy_result (
  TONE neutral,
  COLOR red,
  REPORTS [deploy_state]
)
//--> UNKNOWN_FIELD COLOR
```
In words: A message reports the state of a deployment, in a neutral tone, and it is red.
:::

Refused, at line 3. The finding has two lines: what was found, and why. It cites no law, because no rule of the law is needed to say that a word is not in the grammar. The repair is to take the line out. A declaration has no word for a colour: red is the drawing's business, and what red would mean is said another way, which the last refusal of this chapter shows.

## A field in the wrong place

A known field can sit on a kind that does not carry it. Every kind carries `SATISFIES`, `ALWAYS_REACHABLE`, `SIGNALS` and `ACTOR`. Beyond those, each kind has its own fields.

{{fields}}

::: plate A tone, written on a screen
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE],
  TONE cautionary
)
//--> FIELD_MISPLACED overdue_invoices
```
In words: On the screen of overdue invoices a user scans and compares, and the tone is cautionary.
:::

Refused, and the finding says where the field belongs: `TONE` is a message's field. A tone is how the system speaks, and a screen does not speak. The repair gives the tone to a message.

::: plate The tone, given to a message
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE]
)

DEFINE FEEDBACK overdue_notice (
  TONE cautionary,
  REPORTS [overdue_count]
)
//--> clean
```
In words: On the screen of overdue invoices a user scans and compares. A message, in a cautionary tone, reports how many invoices are overdue.
:::

Clean. Before this check existed, a field on the wrong kind was read by nothing and reported by nothing, and its author believed it was working. A few fields are read on any kind, and so pass anywhere: `STEPS`, `INTENT_FLOW`, `VISIBLE_STATE` and `VISIBLE_ENTITIES`.

## A field written twice

::: plate One field, two lists
```zayn statement.zayn
DEFINE INTENT_FLOW ambiguous_flow (
  SATISFIES [READ],
  ALWAYS_REACHABLE [EXIT],
  SATISFIES [SCAN]
)
//--> DUPLICATE_FIELD ambiguous_flow
```
In words: A user reads, and can leave at every step, and scans.
:::

Refused, at the second copy. The verifier does not merge the two lists and does not keep the last one. Which of the two did the author mean? It asks. The repair writes the list once.

::: plate One field, one list
```zayn statement.zayn
DEFINE INTENT_FLOW ambiguous_flow (
  SATISFIES [READ, SCAN],
  ALWAYS_REACHABLE [EXIT]
)
//--> clean
```
In words: A user reads and scans, and can leave at every step.
:::

Clean.

## A value outside a closed list

Beside the verbs, {{n:lang.lists}} fields take their value from a closed list. Here they are, with every value each one admits.

{{lists}}

A word outside a list is refused, however reasonable it sounds.

::: plate A kiosk, declared as a medium
```zayn lobby.zayn
DEFINE VIBE lobby_kiosk (
  SURFACE_AS kiosk,
  MOTION none
)
//--> UNKNOWN_MEDIUM lobby_kiosk
```
In words: The culture of the lobby is drawn on a kiosk, with no motion.
:::

Refused. A kiosk is a screen that its user did not choose to stand in front of. That is a property of a surface, and the list holds media. The repair names a medium of the list.

::: plate The kiosk, as a visual surface
```zayn lobby.zayn
DEFINE VIBE lobby_kiosk (
  SURFACE_AS visual,
  MOTION none
)
//--> clean
```
In words: The culture of the lobby is drawn on a visual surface, with no motion.
:::

Clean.

Two of the lists look alike, and they are kept apart on purpose.

::: plate The same word, in two lists
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger]
)

DEFINE FEEDBACK overdue_notice (
  TONE danger,
  REPORTS [overdue_count]
)
//--> INVALID_TONE overdue_notice
```
In words: The screen of overdue invoices carries values that mean danger. A message reports how many are overdue, in a tone of danger.
:::

One finding, on the message. On the screen, `danger` passes: `SIGNALS` says what a value means about a record. On the message it is refused: `TONE` is the register in which the system speaks, and the repair takes the tone `critical`. Two subjects, two lists, and a word of one is refused in the other. This is also where the red of the first refusal went: a declaration says that a value means danger, and a medium decides how danger is shown.

## What I refused

**I refused nesting.** A field holds a value or a list of names. The grammar gives the reason: nesting "is where widget trees creep back into an intent language".

**I refused to let any word be a medium.** `SURFACE_AS` once accepted any name, and `kiosk` passed. A closed list of media is what makes a table of verbs against media finite, and a kiosk is a property of one of them.

**I refused one vocabulary for the tone and the signal.** The specification draws the line: one subject with two vocabularies is a defect, which the law corrected in itself, and "two subjects with two vocabularies is correct", provided the border is written down.

**I refused silence on a misplaced field.** Since version 1.4 of the language, on 1 November 2026, a known field on a kind that does not carry it is refused. A file that carried one was accepted the day before.

## The court

The court of this chapter is a set of fixtures from Zayn's conformance suite, declarations kept with the answer each must get. The first one holds the {{n:lang.kinds}} kinds in one lawful file. The build ran each fixture below in the snapshot of Zayn and compared its answer with the suite's manifest.

## Where the field leads

The field leads in what its descriptions can compute. SCXML describes a machine of states and of the events that move it. `ALWAYS_REACHABLE` states what stays within reach, and it describes no machine.

And the design tokens name what a declaration leaves to the drawing: colours, dimensions, typefaces. A team that declares in Zayn still needs those names, and the token format is where the field is writing them.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The grammar refuses what this chapter showed: a field, a place, a second copy, a value. It reads the {{n:lang.kinds}} kinds it defines, it reports the words `WIDGET` and `USER` with a warning, and it passes over any other kind as another language's. Appendix B gives the grammar in full, with the form each field takes.

## In your hands

Here is a declaration that the verifier accepts, and that holds four defects.

::: plate For you: clean, and wrong four times
```zayn invoices.zayn
DEFINE SCREN overdue_invoices (
  SATISFIES [SCAN, COMPARE],
  TONE danger,
  SIGNALS [critical]
)
//--> clean
```
In words: On the screen of overdue invoices a user scans and compares, the tone is danger, and the values carry a critical signal.
:::

Clean! Now read the first line again, letter by letter, and repair what you find. Before you run it again, write down the codes you expect. Try before you read on.

::: plate The kind spelt right
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE],
  TONE danger,
  SIGNALS [critical]
)
//--> FIELD_MISPLACED overdue_invoices
//--> UNKNOWN_SIGNAL overdue_invoices
```
In words: The same four lines, with the kind spelt as the language spells it.
:::

Two refusals, and a third defect waits behind the first: the tone is on the wrong kind, and its word comes from the other list. Repair each one, and go on until the verifier answers clean and every line of your file is true.

::: plate A form the verifier accepts
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE],
  SIGNALS [danger]
)

DEFINE FEEDBACK overdue_notice (
  TONE critical,
  REPORTS [overdue_count]
)
//--> clean
```
In words: On the screen of overdue invoices a user scans and compares, and the values carry a signal of danger. A message, in a critical tone, reports how many invoices are overdue.
:::

The first draft was clean because the verifier read nothing of it: `SCREN` is not a kind of this language, and a kind of another language is passed over, with whatever it holds. A file may hold declarations of several languages, and the verifier judges only its own. So how is it to tell a misspelt kind of its own from a kind that belongs to someone else? The record holds two answers. The verifier passes such a kind over. The evaluator of chapter 9, forged from a second declaration of the language, refuses every kind it does not know.

A declaration that the grammar accepts can still break the law. The next chapter makes the verifier refuse one, and reads the refusal line by line.
