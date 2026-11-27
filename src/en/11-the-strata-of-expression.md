---
id: the-strata-of-expression
part: 4
number: 11
title: The strata of expression
stage:
  built: "two strata as fields of the language, run on this page with their kinds of finding and fixtures: `SIGNALS`, a meaning from Rule 118's list of {{n:signal.values}}, and `ROLE`, a control's promise among {{n:lang.roles}}; the layer's binding rule, that every expression serves an intent, refused on both; motion asked what state it reports, through the field `MOTION`; message carried by `FEEDBACK`, its `TONE` and its `REPORTS`; a menu's levels and a flow's steps as structure; the law's rules on time, and among them Rule 125, which entered the law in my ruling on the proposal"
  designed: "the strata as *The Second Founding* states them, put to my ruling section by section: closed lists of words for structure and motion; a message that names its cause, its remedy and its actor; tempo as a declared class of time"
  next: "the proposal's order of work: signal in sound; then message; then structure, motion and tempo"
status: draft
research: research/ch11.md
fixtures: [unknown-signal, unknown-signal-lawful, expression-orphan, expression-orphan-lawful, unknown-role, unknown-role-lawful, role-promise-broken, decorative-animation, decorative-animation-lawful, invalid-tone, menu-landing-not-first, menu-lawful]
---

A stratum of expression is one function by which an intent is made perceivable: a meaning, a promise, a change, a message, an order, a pace. It sits between what a user is doing and how one medium draws it. *The Second Founding*, a proposal of the project for a new base of the law, which awaits my ruling, names six: structure, signal, role, motion, message and tempo. In this chapter I take them one by one. For each, I say what the proposal asks, and what stage it has reached in the language. Two are the proposal's fields, built with their own refusals; three are carried by other fields of the language, with their own checks; and tempo is held in the law. I run each one that is built, the refusal first and the repair after.

If you open the book here, five words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law, and a **finding** is one entry of its report, a refusal when it is an error. **The drawing** is what a medium shows of a declaration.

## The field

The field has expression, and it names it by the widget, the setting and the clock.

By the widget. WAI-ARIA 1.2, a W3C Recommendation of June 2023, gives the roles with which a page conveys its controls "to assistive technologies", the programs that read a page aloud or by touch. Its section on widget roles opens: "The following roles act as standalone user interface widgets or as part of larger, composite widgets." The list begins `button`, `checkbox`, `gridcell`, `link`. A role in the field names the kind of control.

By the person's setting. Media Queries Level 5 is a W3C Working Draft of February 2026. It defines a feature a page can read: "The prefers-reduced-motion media feature is used to detect if the user has requested the system minimize the amount of non-essential motion it uses." Its value `reduce` says that the user prefers an interface that "removes or replaces the types of motion-based animation" that trouble some people.

By the clock. In 1993 Jakob Nielsen wrote that "0.1 second is about the limit for having the user feel that the system is reacting instantaneously", and he set limits at one second and at ten. WCAG 2.2's Success Criterion 2.2.1, *Timing Adjustable*, is at Level A. It opens: "For each time limit that is set by the content, at least one of the following is true:", and its first three answers are to turn the limit off, to adjust it, and to extend it.

The sources were read on 26 November 2026, and Appendix F lists them. So the field names a control's kind, honours a person's setting for motion, and measures time in fractions of a second.

## The principle

**An expression says what a meaning, a promise or a change is for, never how it looks, and it always serves something a user is doing.**

The proposal puts it in four words: "Expression is not appearance." A declaration of expression "names a **meaning, a promise, or a relation**", never a pixel, a colour or a waveform. And one rule binds the whole layer: "Every expression declaration traces to an intent, or it is an error." The contract, the file that binds each kind of finding to the law, carries that sentence word for word as the invariant of a finding, `EXPRESSION_ORPHAN`. The verifier binds it today on its two expression fields, `SIGNALS` and `ROLE`; the older fields of a feedback answer to their own checks.

## Six functions in the middle

The proposal draws three layers. At the bottom, the intent: what the user is trying to do, in the law's closed list of {{n:law.verbs}} verbs. At the top, the projection: how one medium draws it, replaceable. Between them, the expression, which the proposal calls "THE MISSING MIDDLE": the founding architecture of the platform ran from the intent "straight to pixels".

The proposal's first version named six strata and defined three of them in visual terms: signal as colour, motion as animation, structure as layout. Its current version, the fourth, corrects that: "The strata are functions. The media are channels." Sound, it says, "is the same function in a different channel". A signal is a meaning, carried in colour on a screen and in a tone in a speaker; the stratum says the meaning, and the medium carries it.

Here are the six, in the proposal's words. Structure is "what is grouped, subordinate, ordered, dense, deep". Signal is "a meaning bound to a perceptible quality". Role is "the promise a control makes". Motion is "change that reports state". Message is what the system owes the user "when it speaks: cause, remedy, actor — not the wording". Tempo is "budgets, interruption, resumption".

## Signal: a meaning, never a colour

A `SCREEN` is a surface the user reads. Its field `SIGNALS` lists the meanings the screen's records carry, from the list of Rule 118, *Two Families of Colour*: {{n:signal.values}} statuses, each with the rule's own meaning: `success`, "OK, valid, under control"; `warning`, "watch this"; `danger`, "critical, exceeded, incident"; `info`, "in progress, neutral"; and `muted`, "waiting, inactive". Here is a screen of overdue invoices, written by someone who named the paint.

::: plate Overdue invoices, in red
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [red]
)
//--> UNKNOWN_SIGNAL overdue_invoices
```
In words: A screen where the user scans, compares and finds overdue invoices, and its records are marked red.
:::

Refused: "A value in SIGNALS is not one of Rule 118's five semantic statuses." Red is a colour, and the stratum holds meanings. The repair names what the red was for.

::: plate Overdue invoices, by meaning
```zayn invoices.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger, warning]
)
//--> clean
```
In words: The same screen; its records say danger for an invoice past its limit and warning for one to watch.
:::

Clean. Each medium chooses how to carry `danger`: a colour on a screen, a pattern in print. The data file of the signals, `signal.json`, states its own rule: "EXTRACTED, NOT DESIGNED: every value and every meaning below is quoted from Rule 118". Chapter 12 carries a signal across the media.

## Role: a promise, never a widget

An `INTERACTION` is one control, and its `ROLE` is the control's promise about what happens when the user acts. The language holds {{n:lang.roles}}. `inert` informs and does nothing; `navigate` changes what is shown, never what is true; `reversible` changes something that can be taken back; `irreversible` changes something that cannot; `proposal` advises and commits nothing until an authority accepts it. Here is a control to archive an invoice, written in the field's word.

::: plate Archive, as a button
```zayn archive.zayn
DEFINE INTERACTION archive_invoice (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE button
)
//--> UNKNOWN_ROLE archive_invoice
```
In words: A control on which the user archives an invoice, with undo within reach, and its role is a button.
:::

Refused: "A ROLE value is not one of the five promises this language defines." The contract states the invariant behind it: "A declaration may not name a widget; it may name a promise." That sentence is the proposal's answer to an old exclusion: the language has no `WIDGET`, and `ROLE` names what the control owes the user without one.

::: plate Archive, as a promise
```zayn archive.zayn
DEFINE INTERACTION archive_invoice (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: The same control; archiving can be taken back, and undo stays within reach.
:::

Clean. A `reversible` control may be drawn as a button, a swipe or a key; the promise holds in each. The project's design note on roles, a design pass revised as the roles were built, found its best argument there: "`ROLE irreversible` is Rule 79's escape clause, made expressible for the first time." Rule 79 asks for an undo on every act, or a reason there is none; the role is that reason, and chapter 8 runs it.

The layer's binding rule runs on roles too. Here is a control with a role and no intent.

::: plate A role that serves nothing
```zayn open.zayn
DEFINE INTERACTION open_invoice (
  ROLE navigate
)
//--> EXPRESSION_ORPHAN open_invoice
```
In words: A control that promises to change only what is shown, and says nothing of what the user does with it.
:::

Refused: "An expression field is declared on a declaration that satisfies no intent." A promise is a promise about an act; with no act declared, it promises about nothing.

::: plate The role, with its intent
```zayn open.zayn
DEFINE INTERACTION open_invoice (
  SATISFIES [LOCATE],
  ROLE navigate
)
//--> clean
```
In words: A control with which the user finds an invoice, and which changes only what is shown.
:::

Clean. The verifier holds {{n:lang.expression}} expression fields, `SIGNALS` and `ROLE`, and the binding rule runs on both. Its contract decides {{n:diag.signal}} kinds of finding from `SIGNALS` and {{n:diag.role}} from `ROLE`, each with its fixtures in the suite.

## Motion: the change it reports

Motion is older in the language than the proposal. A `FEEDBACK` tells the user of a state, and its field `MOTION` names how it moves, if it does; its field `REPORTS` names the state it tells. The verifier's first checks, of 6 August 2026, already held one on motion, from Rule 112, *Motion Reports, It Never Decorates*. Here is a row that slides when it is saved.

::: plate A saved row that slides
```zayn saved.zayn
DEFINE FEEDBACK row_saved (
  MOTION slide
)
//--> DECORATIVE_ANIMATION row_saved
```
In words: When a row is saved, the user sees it slide, and the slide tells of nothing.
:::

Refused: "Motion or feedback that reports no state." Rule 112 allows movement "only when it reports a change the operator caused and might otherwise miss", and ends: "If motion would look the same whether or not anything changed, it is decoration; remove it." The operator is the record's word for the person at the controls.

::: plate A saved row that reports
```zayn saved.zayn
DEFINE FEEDBACK row_saved (
  MOTION slide,
  REPORTS [row_state]
)
//--> clean
```
In words: When a row is saved, it slides, and the slide tells the user the row's new state.
:::

Clean. The motion stratum as built asks one question of a motion: what state it reports. `MOTION` takes any word, and the verifier reads whether a report goes with it. Which motion is fit to report it, a slide or a pulse, is the drawing's choice, and Rule 112 is filed under `judgment`, the tier where a person decides. The proposal designs a closed list of motions, for every medium that moves, sound among them.

## Message, structure and tempo

Message is carried today by the `FEEDBACK` declaration. Its `TONE` names the register in which the system speaks, from a closed list: `celebratory`, `cautionary`, `critical`, `neutral` and `informational`. The verifier refuses a word outside it, `INVALID_TONE`; chapter 7 runs that refusal and shows why `TONE` and `SIGNALS` keep two lists. Its `REPORTS` names what the message tells. The proposal extends `FEEDBACK` rather than replacing it, toward a message that names its cause, its remedy and its actor.

Structure is carried by a menu's levels and by a flow's steps. A `NAV_GRAPH` declares a menu entry and names its children, and the verifier refuses a section whose landing entry is not first, under Rule 116; chapters 18 and 19 run it. A flow declares its `STEPS`, and the verifier refuses a flow that traps the user, as chapter 8 shows. "Subordinate" and "ordered", two of the proposal's words for structure, are decided on menus: a child sits under its section, and the landing comes first. The rest of its words, grouping, density and depth, are designed.

Tempo stands in the law. Rule 18, *The Speed of Thought*, asks that "Actions must acknowledge the user within 100ms", and the law files it under `machine-later`, the tier for a rule a machine is to check once its instrument is built; chapter 17 climbs the tiers. Rule 125, *Sound Corroborates, It Does Not Acknowledge*, entered the law in my ruling on the proposal, from a measurement made by the part of Softanza that plays sound: "An act is acknowledged in a channel that can meet Rule 18's hundred milliseconds." Rule 81 holds how a wait is shown, and Rule 91 time as the business counts it: deadlines, periods, cutoffs. In the language, tempo is the proposal's: a declared class of time, so that a declaration can say which acts owe the hundred milliseconds.

## What I refused

**I ruled parts of the proposal into the law.** On 13 August 2026 I ruled twelve items in one pass, "Twelve items, twelve rulings", and the docket, the file where changes to the law are proposed and ruled, records them. Among them: Rule 82 became *Perceivable State*, so that a state may be heard as well as seen; and Rule 125 entered the law, "narrowed to channels that demonstrably cannot meet Rule 18's budget". On 18 August I adopted the proposal's amendment to the reference design of Softanza, the platform Zayn belongs to, its plan of layers: the layer of the law now holds the vocabulary of interfaces as data too. The rest of the proposal waits for my pass, section by section.

**I deferred the requirement of a role to evidence.** On 19 August 2026 I ruled that requiring a role of each control waits for evidence. The contract's note gives the reason: requiring a vocabulary before real surfaces have tried it buys "a declared role rather than an accurate one". In its place the verifier reports, as a warning that never refuses, a surface whose controls declare no role: `ROLE_UNDECLARED`, run in chapter 22.

**A role that would declare the defect.** The design note refused the proposal's own example, a role for a binary state: "A vocabulary that let a declaration say `ROLE binary_state` would let it declare the defect as its intent."

**A word in the wrong stratum.** The proposal listed `instant` as a role. The design note moved it: "It is a `TEMPO` word, not a `ROLE` word — it says how fast, not what happens."

**The language computes no colour.** The proposal's plan keeps the drawing out of the language's home: "The moment this repository computes a colour or a waveform, the split that makes the vision safe is gone." A stratum names the meaning; a renderer draws it.

[AUTHOR: the stake of this chapter, in your words: why the middle layer, and what you will rule first when you take *The Second Founding* section by section.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the built strata. A colour where a meaning goes, refused, and its twin. A signal on a declaration that serves no intent, refused, and its twin. A widget's name where a promise goes, refused, and its twin. A reversible control that selects, declares no act and keeps no undo, refused under its own code, `ROLE_PROMISE_BROKEN`. Chapter 10 shows the act that gets `MISSING_UNDO` instead. A feedback that speaks and reports no state, refused, and its twin. A tone outside its list, refused. And for structure, a menu whose landing comes second, refused, beside a lawful menu.

## Where the field leads

The field leads in the person's own setting. A page reads `prefers-reduced-motion` and removes or replaces its motion for the person who asked. Zayn's law speaks to whoever designs the interface: each motion reports a state, or it goes.

The field leads in measured time. Nielsen's limits have stood since 1993, in seconds a person feels. The law holds the hundred milliseconds in Rule 18, filed `machine-later`, and Rule 125 reaches the channels that cannot meet it.

The field leads in its roles' reach. ARIA's roles are a W3C Recommendation that pages use to reach assistive technologies. Zayn's {{n:lang.roles}} roles are built and run on declarations, and requiring them waits for the evidence of real surfaces, as I ruled.

Zayn leads in what a role says. The field's role names the control's kind, and a `button` may archive, delete or do nothing. Zayn's role names the consequence, and the verifier holds the declaration to it.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

- **Signal**, `SIGNALS` with its refusals: built.
- **Role**, `ROLE` with its refusals: built.
- **Motion**, `MOTION` and `REPORTS`: built, as the older check.
- **Message**, `FEEDBACK`, `TONE`, `REPORTS`: built, as the older fields.
- **Structure**, `NAV_GRAPH` levels, `STEPS`: built for menus and flows.
- **Tempo**, Rules 18 and 125 in the law: designed in the language.

Built: `SIGNALS` and `ROLE`, the {{n:lang.expression}} expression fields of the verifier, with the layer's binding rule run on both. The motion check of Rule 112. `FEEDBACK` with its tone and its reports. A menu's levels and a flow's steps. Rules 18 and 125 in the law. Designed: the rest of each stratum as the proposal states it, put to my ruling section by section. Next: in the proposal's order, signal in sound; then message; then structure, motion and tempo.

So two of the six are the language's own fields today, three are carried by other fields of the language, and tempo is held in the law. Each one built refuses what it names.

## In your hands

Here is a control to purge an archive, and the notice that follows. Whoever wrote it reached for a widget's word, a signal's word where a tone goes, and a shake. Three findings wait in it. Write what you expect, then open the verifier's answer.

::: plate For you: the purge
```zayn purge.zayn
DEFINE INTERACTION purge_archive (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE danger_button
)

DEFINE FEEDBACK purge_done (
  TONE danger,
  MOTION shake
)
//--> UNKNOWN_ROLE purge_archive
//--> INVALID_TONE purge_done
//--> DECORATIVE_ANIMATION purge_done
```
In words: The user confirms and purges an archive, with undo and cancel within reach, through a control whose role is a danger button; then a notice in a danger tone shakes.
:::

Repair it, and say what you expect. When the role is true, a fourth finding may appear: a purge that cannot be undone and still offers an undo. Two lawful repairs follow. Try before you read on.

::: plate The purge that cannot be undone
```zayn purge.zayn
DEFINE INTERACTION purge_archive (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible
)

DEFINE FEEDBACK purge_done (
  TONE critical,
  MOTION shake,
  REPORTS [archive_state]
)
//--> clean
```
In words: The user confirms and purges the archive, which cannot be taken back, with a way to cancel; a notice in a critical tone shakes and tells the archive's state.
:::

::: plate The purge that can be undone
```zayn purge.zayn
DEFINE INTERACTION purge_archive (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)

DEFINE FEEDBACK purge_done (
  TONE critical,
  REPORTS [archive_state]
)
//--> clean
```
In words: The user confirms and purges the archive, which can be taken back, with undo and cancel within reach; a notice in a critical tone tells the archive's state.
:::

Both clean. The first still shakes, and the verifier accepts it, because the notice now reports a state. Whether a shake is the right way to report a purge is a person's judgment under Rule 112 today, and the proposal's closed list of motions is designed for it. And whether the purge can be taken back is a fact of your system. Which is it?

[AUTHOR: is the purge the defect you want the reader to repair here, or one from your own work?]

Each stratum says what an expression does, and a medium carries it. Part V turns to the media: one declaration, carried in {{n:media.total}} channels.
