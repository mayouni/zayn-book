---
id: the-instruments-of-the-field
part: 2
number: 4
title: The instruments of the field
stage:
  built: "the verifier's refusal of a selection that acts and of a control that promises to change nothing and acts, at level 2, run on this page; a run at level 4, which reads the declaration; the audit of the painted page, whose check K22 reads layout shift; the `lint` field, which names an instrument on {{n:rule.lint}} rules; a menu's structure decided from a declaration"
  designed: "the contract's one kind of finding at level 4, `LAYOUT_DISPLACEMENT`, whose measure its note gives to the audit of the painted page; an audit that refuses at the moment of painting"
  next: "rules moved up the enforcement ladder, from a person's judgment toward a machine's check, as the instruments that answer for them are built"
status: draft
research: research/ch04.md
fixtures: [select-act-collapse, select-act-lawful, projection-visual-decide, role-acts-without-consequence, role-acts-without-consequence-lawful, projection-visual-understand, field-misplaced-lawful]
---

An instrument of the field is anything that reads an interface and decides something about it: a written criterion, a set of design tokens, a catalogue of components, a linter, a visual test, a measure of movement. In this chapter I take them one by one and say what each reads and what each decides. Then I show a different object, a declaration of what a user is doing, and run two interfaces whose drawing can be in order for each instrument, and which the law refuses. Last, I show the other half: what only a drawing shows stays with the instrument that reads the drawing.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

Each instrument of the field reads one object, and its sources say which.

A criterion reads the painted page, the interface as a browser draws it. WCAG 2.2, the accessibility guidelines of W3C, sets in Success Criterion 2.5.8, at Level AA, that a target for a pointer "is at least 24 by 24 CSS pixels", with named exceptions. A person or a program measures the drawn target against that number.

A design token reads nothing: it is read. The Design Tokens format, a draft report of a W3C community group, defines a token as information with a name, "at minimum a name/value pair": a colour, a size, a typeface, kept as data so that tools share it.

A catalogue of components reads each part apart from the whole. Storybook keeps each state of a component as a story, and "A story captures the rendered state of a UI component." Its accessibility addon, in its own words, "is built on top of Deque's axe-core library", the engine that tests a drawn page.

A linter reads the source. eslint-plugin-jsx-a11y, a plugin for the linter ESLint, does in its README's words "a static evaluation of the JSX", the markup written inside a program's source, before any browser draws it. The same README asks that its user "Consider these tools just as one step of a larger a11y testing process".

A visual test reads pixels against pixels. Playwright's documentation says: "On first execution, Playwright test will generate reference screenshots." Then "Subsequent runs will compare against the reference." It decides one thing: the same as before, or not.

And a measure of movement reads the page while it loads. The Layout Instability API, a draft of a W3C community group, defines a page's layout shift value as the share of the screen that moved, multiplied by how far it moved. Cumulative Layout Shift, CLS, is the score built on it, and the guide on web.dev sets a threshold: "Good CLS values are 0.1 or less."

Each source was read on 24 or 25 November 2026, and Appendix F lists them. So the field reads the criterion's target, the token's value, the component's rendered state, the source's markup, the screenshot's pixels and the page's motion, and it decides on each object where it reads it.

## The principle

**Each instrument of the field reads one object and decides there; a declaration is another object, and the law refuses it for what it lets a user do.**

Article II of the law, *Intent*, says where the object starts. Interaction starts "from what the human is trying to do", and "widgets are consequences of intent, never primitives. Selection never implies execution". A widget is a drawn control: a button, a card, a tile. The field's instruments read widgets, their values and their drawing. A declaration reads the intent the widget serves. Two surfaces drawn from the same tokens, the same component and the same markup can let a user do different things, and only a declaration says which.

The record's comparison of practices puts it at the true size. Of WCAG it says that Zayn adds "Intent and rights beyond access: a flow with no exit, an act with no undo." Of design tokens: "Data for the intent and the rights, not for the look." Of Storybook: "A place to say what a user, a person or an agent, is doing with a component." Each instrument keeps its object. The declaration adds one.

## A selection that pays

Here is a checkout drawn on a screen. A `VIBE` is the declaration of an interaction's culture, and its field `SURFACE_AS` names the medium, here `visual`, the screen. An `INTENT_FLOW` is the steps of one intent; `SATISFIES` lists the verbs the user performs, from the law's closed list of {{n:law.verbs}}, and `ALWAYS_REACHABLE` the verbs kept within reach at every step.

::: plate A checkout where choosing pays
```zayn checkout.zayn
DEFINE VIBE screen_surface (
  SURFACE_AS visual
)

DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR operator
)
//--> SELECT_ACT_COLLAPSE pick_and_pay
```
In words: On a screen, an operator picks a plan and pays for it, with a way to undo, to cancel and to leave within reach.
```sketch
title: Choose a plan
say: Basic · Standard · Premium
control: Standard
missing: Confirm | Rule 16
caption: A tap on a plan charges for it. The dashed outline is the step the verifier asked for.
```
:::

Refused: "Selection has become execution: SATISFIES holds SELECT and ACT without CONFIRM." The finding cites Rule 16, *Intentional Clicks*, and Article II, whose sentence it enforces.

Now hold the drawing of this screen to each instrument of the field. The tokens give the plan cards their colour and size. The story renders the card, and the addon tests it as drawn. The linter reads the markup of each control, and the visual test compares the screenshot with its reference. Each decides on its object, and each object can be in order. The objects they read describe the card: its values, its rendered state, its markup, its pixels. The declaration states what a tap on it does, so the verifier refuses it.

Naming the screen changed nothing: the court's fixture `select-act-collapse` holds the same flow with no `VIBE` and gets the same finding, because the check judges the intent, whatever draws it. Here is the repair.

::: plate The checkout, with a step to confirm
```zayn checkout.zayn
DEFINE VIBE screen_surface (
  SURFACE_AS visual
)

DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR operator
)
//--> clean
```
In words: On a screen, an operator picks a plan, confirms, and pays, with a way to undo, to cancel and to leave within reach.
```sketch
title: Choose a plan
say: Basic · Standard · Premium
control: Standard
restored: Confirm | Rule 16
caption: The tap selects; a separate step commits. How the step is drawn is the drawing's business.
```
:::

Clean. One verb restored the boundary between interest and commitment, and no pixel of the drawing was named.

## Two cards drawn alike

A dashboard shows two cards. A design system draws them alike: one token for the surface, one for the corner, one component. An `INTERACTION` is one control, and its `ROLE` is the control's promise about what it changes: `inert` promises to change nothing, `navigate` to change only what is shown, `reversible` to change something that can be taken back. A control that promises `inert` or `navigate` may not act: both promise that what is true stays as it is.

::: plate Two cards, one that acts
```zayn cards.zayn
DEFINE INTERACTION revenue_card (
  SATISFIES [READ],
  ROLE inert
)

DEFINE INTERACTION overdue_card (
  SATISFIES [SCAN, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE inert
)
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE overdue_card
```
In words: Two cards on a dashboard. The user reads the first. The second lets the user scan the overdue invoices and act on them, with undo within reach, and it promises to change nothing.
:::

Refused: "A control promising to change nothing declares that it acts." The revenue card beside it passes: the check reads each card's promise, and the revenue card keeps its own. The finding cites Rule 119, *A Card Is Not a Button*, Rule 16 and Article II. It also cites Rule 112, on motion, and the contract gives the reason: "inert informs and navigate changes what is shown, never what is true", and Rule 112 lists following a link and opening a panel as acts of that class.

The two cards are one drawing and two promises. The token reads the same value on both; the story renders the same component. The difference lives in one word of the declaration.

::: plate The second card, honest about its act
```zayn cards.zayn
DEFINE INTERACTION revenue_card (
  SATISFIES [READ],
  ROLE inert
)

DEFINE INTERACTION overdue_card (
  SATISFIES [SCAN, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: The same two cards. The second now says that what it changes can be taken back.
:::

Clean. The drawing may still show both cards alike, and the law leaves that to the drawing. What a design system decides next, a cue that one card acts, is the design's to choose.

## Clean, and the drawing still owes

Here is the other half. A screen of overdue invoices, and a notice that reports their count. A `SCREEN` is a surface the user reads; a `FEEDBACK` reports a state, and its `TONE` says how.

::: plate A screen and its notice
```zayn notice.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE]
)

DEFINE FEEDBACK overdue_notice (
  TONE cautionary,
  REPORTS [overdue_count]
)
//--> clean
```
In words: A screen where the user scans and compares the overdue invoices, and a notice, in a cautionary tone, that reports how many are overdue.
:::

Clean at level 2, the verifier's default. A level is a stage of what a check needs to read: level 4, in the language's table, is "Projection", and it requires "a rendered surface". The verifier holds no rendered surface, so at level 4 it runs every check it holds, and each reads the declaration. Here is the same file at level 4:

```shell
$ zayn check notice.zayn --level 4
# exit 0
```

Clean, and the command answers 0. That verdict is the declaration's.

The painted page has its own instrument. The audit of the painted page is a page of Zayn's repository, `tools/ui-audit.html`, that opens another page in a browser and measures what is drawn. The contract is the file that binds each kind of finding to the law. It holds {{n:diag.total}} kinds, and it places {{n:diag.level4}} of them at level 4: `LAYOUT_DISPLACEMENT`, for Rule 38, *Zero Displacement*. Its note gives the measure to the audit: "undecidable from a declaration. Measured today by tools/ui-audit.html, which is the enforcement ladder working as designed." The enforcement ladder is the law's order of instruments, from a person's judgment up to a machine's check; chapter 17 climbs it.

Rule 38 asks a page to avoid "Errors that push content down". Whether the notice, when it lands, shoves the table of invoices down the screen is a fact of the painted page. The declaration says that a notice reports a count; the drawing decides where it lands. The audit holds the check for it, K22 LAYOUT_STILL. It reads the browser's own record of movement, the `layout-shift` entries of the API the field defines. Chapter 17 tells that audit and its recorded runs.

The audit also reads a criterion of the field. Its check K17 TARGET sets a size for a target, and its source code says why one target passes: "a link inside a sentence is exempt, as WCAG 2.5.8 exempts it". So Zayn holds two instruments, one for each object: the verifier for the declaration, the audit for the drawing.

## The law names its instruments

A rule of the law can name the instrument that answers for it. In the law's data such a rule carries an entry named `lint`, and {{n:rule.lint}} rules carry one. Each entry opens with a head, the name of an instrument, followed by what it reads. For Rule 130 it names a `declaration lint`, built in the verifier, which reads a declared element that traces to no intent. For Rule 105 it names the UI audit, which measures size and contrast. For Rule 3 it names an instrument of Softanza, the platform Zayn belongs to: its graphics plane, which resolves a meaning to a colour. For Rule 44 it names a `manifest lint`, owed to read the profile a project's manifest names. And for Rule 38 it names an `html lint`, owed to read an image declared "without width+height", which "reserves no space": the field's own kind of instrument, a linter of markup, named by the law as the one this rule is owed.

That entry is the bridge between a rule and the field's instruments. A rule states what a user must be able to do; its `lint` names the object where an instrument can check it, and the instrument that reads that object. A project that adopts the law reads, on each rule that carries the field, which of its own instruments owes which check.

## What I refused

**I moved a menu's structure from the drawing to the declaration.** On 8 November 2026, reading a menu whose section had lost its first entry, to avoid repeating its name one level down, I ruled that "you must add this as an issue that is statically checked in Zayn". The language gained `NAV_GRAPH`, a declaration of a menu, and the verifier refuses a broken menu from it. The docket records the division: "the verifier now decides three of its demands from a declaration, and the UI audit the rest on a painted page".

**The suite proves the painted page through the audit.** A fixture is a declaration kept with the answer it must get. The suite's manifest lists `LAYOUT_DISPLACEMENT` apart, with the kinds it holds no fixture for, gives the measure to the audit, and "says so rather than pretending coverage". Chapter 17 gives the whole sentence.

**The verifier keeps to its object.** Its README leaves `LAYOUT_DISPLACEMENT` to the audit, for good: the painted page is the audit's.

**The law asks what the user can do, and WCAG keeps its own claim.** The rules, in the comparison's words, "do not cite WCAG, and this page does not claim they implement it". The law asks what the user can do; WCAG keeps its own criteria and its own claim.

**A rule names an instrument with care.** When the docket put instrument pointers on the rules of colour, one rule received none, and the note says why: "a pointer to an instrument that does not exist is worse than silence."

[AUTHOR: the stake of this chapter, in your words: why an interface that passes every instrument of the field can still be refused, and what that taught you about where a rule for interfaces must be read.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the verifier's side. A selection that acts, refused, and its lawful twin. The same selection on a screen, refused the same way. A card that promises nothing and acts, refused, and its twin made reversible; the same card on a screen, refused the same way. And the screen of overdue invoices with its notice, clean. Beside them, the manifest lists `LAYOUT_DISPLACEMENT` apart, a fact measured on the painted page by the audit.

## Where the field leads

The field leads in what it reads on the painted page. The record's comparison of practices says the UI audit measures "a much narrower set than axe-core's", and that the field ships its checks inside design tools; its page on frameworks says they ship them in the tests of the frameworks that build screens.

The field leads in what people decide. The same comparison says: "Usability testing and heuristic review decide things that nothing in Zayn replaces."

The field leads in the drawing, where a generator errs. The record's founding document for the platform says of a court that checks intent alone: "generators rarely misdeclare intent". An AI model that draws an interface errs in the drawing, and Part IV turns to what a declaration leaves to it.

Zayn leads in the moment. Its law is data that a tool loads, and a declaration is refused, in the comparison's words, "before the interface exists". The instruments of the field read the interface after it is drawn; the verifier reads the intent before.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the verifier's refusal of a selection that acts and of a control that promises to change nothing and acts, at level 2, run on this page; a run at level 4, which reads the declaration with every check the verifier holds. The audit of the painted page, whose check K22 reads layout shift, told in chapter 17. The `lint` field on {{n:rule.lint}} rules, naming the instrument each is owed. A menu's structure decided from a `NAV_GRAPH` declaration. Designed: the contract's kind at level 4, `LAYOUT_DISPLACEMENT`, whose measure its note gives to the audit; and an audit that refuses at the moment of painting. Next: rules moved up the enforcement ladder as the instruments that answer for them are built.

So a clean report at level 4 says that the declaration keeps every rule the verifier checks. The painted page answers to the audit, and the rest of the law to a person.

## In your hands

Here is a tile on a dashboard of projects. It opens a project, and its declaration was written by someone who also wanted a tap to archive the project. Three findings wait in its few lines. Write what you expect the verifier to answer, then open its answer.

::: plate For you: the project tile
```zayn tile.zayn
DEFINE INTERACTION project_tile (
  SATISFIES [SELECT, ACT],
  ROLE navigate
)
//--> SELECT_ACT_COLLAPSE project_tile
//--> MISSING_UNDO project_tile
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE project_tile
```
In words: A tile for a project. Selecting it acts on the project, and the tile promises only to change what is shown.
:::

Repair it, and say what you expect. Two lawful repairs follow, and they say different things. Try before you read on.

::: plate The tile that only opens
```zayn tile.zayn
DEFINE INTERACTION project_tile (
  SATISFIES [SELECT],
  ROLE navigate
)
//--> clean
```
In words: A tile for a project. Selecting it opens the project, and it changes only what is shown.
:::

::: plate The tile that archives
```zayn tile.zayn
DEFINE INTERACTION project_tile (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: A tile for a project. The user selects it, confirms, and the project is archived, with undo within reach, and the tile says the act can be taken back.
:::

Both clean. The finding on the role says "change nothing" of a tile that navigates too: the contract puts `inert` and `navigate` in one class, which changes what is shown, never what is true. The two tiles may be drawn alike, and an instrument that reads the drawn tile sees one tile. Which one is true of your tile?

The next chapter reads an interface the field has held by law for decades, read at speed by strangers: the road sign.
