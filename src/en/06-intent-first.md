---
id: intent-first
part: 3
number: 6
title: Intent first
stage:
  built: "the {{n:law.verbs}} verbs in {{n:law.families}} families, each with its invariant, as data of the law; a word outside them refused from the file alone; an element that answers to no verb refused at level 3, against an inventory the verifier is given, under Rule 130"
  designed: "the tables that say which control follows from which intent in each medium; the inventory of elements computed from a project in place of being given"
  next: "the law served to an AI model while it generates"
status: draft
research: research/ch06.md
fixtures: [clean-minimal, unknown-intent, intent-flow-no-satisfies, intent-orphan, unspecified-declaration, expression-orphan, expression-orphan-lawful]
---

Intent first is the rule Zayn rests on: an interface is declared from what its user is doing, and a control on a screen is what that intent becomes in one medium. In this chapter I write a first declaration, three lines long, and I name the words it is made of. Then I give the verbs, all {{n:law.verbs}} of them, and I show what the verifier answers when a word is outside them, when a flow names no intent, when an element of an interface answers to no verb, and when a declaration starts from a widget.

Three words first. The **law** is Zayn's constitution for interfaces: {{n:law.articles}} articles, and {{n:law.rules}} numbered rules that derive from them, kept as data. The **verifier** is the program that reads a declaration and checks it against the law. A **widget** is a drawn control or container: a button, a card, a table.

## The field

React, for one, builds an interface from the thing drawn. Its Quick Start says that apps "are made out of components", and that a component is a piece of the interface with its own logic and its own appearance. The first word written is the name of a thing on a screen.

The field has also started from the other end. In 2014 a working group of the W3C published a note on task models, which "describe the logical activities" a user carries out to reach a goal, and it built its exchange format on a notation named ConcurTaskTrees. A companion note describes an abstract interface, written with no reference to how it is implemented and independent of any modality, graphical, vocal or haptic. Both are Working Group Notes, and the first says in its own status that the group stopped taking it toward a W3C Recommendation.

So the idea of starting from what the user does is in the field's record. It stands there as a description that tools exchange. Each of these pages was read at its source on 23 November 2026, and Appendix F lists them.

## The principle

**An interface is declared from what its user is doing, in a closed set of verbs: a widget is what an intent becomes in a medium, never where a declaration starts.**

The law holds the inversion as its second article.

{{article:intent}}

The Zayn site says in one sentence what the other starting point costs: "When the unit of declaration is a widget, a tool can check only the widget."

## The first declaration

Here is the home screen of a ledger of invoices, declared.

::: plate A screen, and what its user does there
```zayn invoices.zayn
DEFINE SCREEN invoices_home (
  SATISFIES [DISCOVER, LOCATE]
)
//--> clean
```
In words: On the home screen of invoices, a user finds out which invoices there are, and goes to one they already know.

```sketch
title: Invoices
say: 12 open · 3 overdue
say: 2041 · 1,200.00 · due today
control: Search
control: Open
caption: One drawing among many. The declaration says discover and locate; a list and a search field are one way a screen carries them, and a spoken menu is another.
```
:::

Clean! The verifier found nothing to report, and it handed back the number 0. That number is the exit code, what a command returns when it ends. A team's build, the chain of commands that turns its sources into a product, reads it to know whether to go on.

Read the three lines. `DEFINE` opens every declaration. `SCREEN` is its kind: a place where a user can be. `invoices_home` is its name. Between the parentheses come its fields, and this one has a single field, `SATISFIES`, with the list of what the user does here. Nothing in the three lines says list, table, button or colour.

To run it yourself, save the lines in a file and give the file to the verifier: `zayn check invoices.zayn`. Chapter 25 installs the command, and the testbench of the Zayn site checks a declaration in the browser with nothing installed. The line that begins with `//-->` is a comment, which the verifier skips: it states the answer this page expects, and the book's build fails if the verifier gives another.

A second field carries the rest of the idea.

::: plate A flow, and what stays within reach
```zayn invoices.zayn
DEFINE INTENT_FLOW find_invoice (
  SATISFIES [LOCATE, READ],
  ALWAYS_REACHABLE [EXIT]
)
//--> clean
```
In words: To find an invoice, a user goes to it and reads it. At every step the user can leave.
:::

An `INTENT_FLOW` is a flow: the intents a user goes through, under one name. `SATISFIES` says what the surface lets the user do. `ALWAYS_REACHABLE` says what the user can get to at any step of it. Chapter 8 shows what the verifier does with a flow that acts and keeps nothing within reach.

## The verbs, in their families

The words between the brackets are not free. They are the verbs of the law, and the law holds them in {{n:law.families}} families.

{{families}}

Read the right column. Each family carries one sentence that its verbs must keep true in every declaration: its invariant. Several refusals of this book come from those sentences. A screen that reads and acts breaks the invariant of information. A flow where selecting carries out the act breaks the invariant of selection. Chapter 8 runs the invariants of action and of continuity.

If you come from the Zayn site, you met the same verbs grouped by what a user is busy with: understanding, deciding, acting, recovering. The families are the law's own grouping, and chapter 13 gives the other.

## A word outside the verbs

What happens when a declaration uses a word that is not on the list? Here is a word a first draft reaches for.

::: plate A word a first draft reaches for
```zayn invoices.zayn
DEFINE INTENT_FLOW find_invoice (
  SATISFIES [NAVIGATE, READ],
  ALWAYS_REACHABLE [EXIT]
)
//--> UNKNOWN_INTENT find_invoice
```
In words: To find an invoice, a user navigates and reads it, and can leave at every step.
:::

Refused, and the exit code is 1! The report's first line gives the place, `invoices.zayn:2`, the severity, `error`, the code, `UNKNOWN_INTENT`, and what it is about. Its second line gives the reason. Its third line gives the law: Article II, the one printed above, and no rule, because the law has no numbered rule for this and the verifier claims none.

Why is `NAVIGATE` not a verb? Because it hides two intents. A user who navigates is going to a place they know, which is `LOCATE`, or is finding out which places exist, which is `DISCOVER`. The declaration has to say which, and only its author knows. The second plate of this chapter is the repair for the first case.

I keep the list closed on purpose. A medium is where an interface reaches its user: a screen, a voice, a printed page. A new medium brings new drawings of the same verbs: a voice has no button, and its user still acts. The grammar's own note says of a medium that seems to need a new verb that it "has misread its medium".

## A flow that names no intent

A flow is the one kind of declaration that the verifier asks for its `SATISFIES`. Here is one that says only what stays within reach.

::: plate A flow with a name and no verb
```zayn statement.zayn
DEFINE INTENT_FLOW check_statement (
  ALWAYS_REACHABLE [EXIT]
)
//--> INTENT_FLOW_NO_SATISFIES check_statement
```
In words: A user checks a statement and can leave at every step. The declaration does not say what checking is made of.
:::

A finding, and the exit code is 0. Look at the severity on the first line: `warning`. A warning is a finding that lets the declaration pass. An error is a refusal. The report's second line says it: "An INTENT_FLOW declares no intents." The build goes on. The lawful shape is the second plate of this chapter: a flow with its `SATISFIES`.

## An element with no verb

Now what the inversion asks of every element. Each one answers to a verb, or it has no reason to be there.

A declaration cannot know which elements exist on a screen: it does not draw the screen. So the verifier is told. The list of elements is given to it in a small file, a symbol table, and the check is made at level 3, the first level where the verifier is given more than the declaration. A `COMPONENT` is a second kind of declaration: a part of a surface with a meaning of its own.

::: plate Two elements on the screen, one declared
```zayn statement.zayn level=3 symbols=inventory.json
DEFINE COMPONENT amount_due (
  SATISFIES [READ]
)
//--> INTENT_ORPHAN overdue_mark
```
In words: The amount due is something a user reads. The inventory says that the screen holds a second element, a mark for overdue statements, and no declaration says what a user does with it.

```symbols inventory.json
{
  "elements": ["amount_due", "overdue_mark"]
}
```
:::

Refused, and this time the third line cites a rule: Rule 130. The first line has no line number, because the element is in the inventory and not in the file.

{{rule:130}}

The rule's text gives two repairs: the element "is removed, or the intent it was always meant to serve is declared". Here is the second.

::: plate The mark, asked what it is for
```zayn statement.zayn level=3 symbols=inventory.json
DEFINE COMPONENT amount_due (
  SATISFIES [READ]
)

DEFINE COMPONENT overdue_mark (
  SATISFIES [SCAN]
)
//--> clean
```
In words: The amount due is something a user reads. The overdue mark is something a user scans for, down a list of statements.
:::

Clean. The rule says of this repair that declaring an element "is the moment the element is first asked what it is for".

## A kind for the widget

One more word that a first draft reaches for.

::: plate A declaration that starts from the drawing
```zayn sales.zayn
DEFINE WIDGET sales_card (
  SATISFIES [READ]
)
//--> UNSPECIFIED_DECLARATION sales_card
```
In words: There is a card of sales figures, and a user reads it.
:::

A warning, and the exit code is 0: the language has no kind named `WIDGET`, and the verifier reports the word where it is written. The repair names what the user does with the figures and leaves the card to the drawing.

::: plate The same figures, declared from the user
```zayn sales.zayn
DEFINE COMPONENT sales_figures (
  SATISFIES [READ, COMPARE]
)
//--> clean
```
In words: A user reads the sales figures and compares them.
:::

Clean. Card or table is the drawing's business.

## What I refused

**I refused a kind for the widget.** A widget is a consequence of an intent. A declaration that could name one would start from the drawing, and the language would have two starting points.

**I refused one more verb.** The verbs are a closed list, and `NAVIGATE` is a word it turns away. A closed list is what makes the rest countable: which verbs a medium carries, which rules speak of which verb.

**I refused to leave the founding check outside the law.** The verifier reported an element that answers to no verb before any numbered rule said so. On 2 November 2026 the check was given its rule, number 130, and the law's record says that the order was reversed: the check came first.

## The court

The court of a chapter is what proves it. Here it is a set of fixtures from Zayn's conformance suite: declarations kept with the answer each must get. The build ran each fixture below in the snapshot of Zayn and compared its answer with the suite's manifest, its list of expected answers.

One pair stands in the box, `expression-orphan` and the same file repaired: the same check one layer down, citing Article II and no rule, for a declaration that says how its values should be perceived and says nothing of what its user is doing. The plates of this chapter repair the defects of the other fixtures.

## Where the field leads

The field leads in what a task model can say. The W3C note describes tasks with the order between them and their decomposition into subtasks: one task enables another, two tasks are a choice, one suspends another. A declaration of Zayn lists the intents of a surface and names a wizard's steps. The order between intents is what the task model adds.

And a framework builds the screen. A declaration builds none: a team still draws its interface with the framework it has, and Zayn checks what was declared before the drawing begins.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Starting from intent makes checkable what a declaration states: its verbs, what it keeps within reach, its steps, from the file alone and before anything is drawn. That every element answers to a verb is decided at level 3, when the verifier is given the list of elements. At level 3, an element answers to a verb when a declaration carries its name and satisfies one.

## In your hands

Here is a first draft written in the words of mechanics, with a form that points at its flow, and the inventory of the screen. A `FORM` is a third kind of declaration: a surface where a user enters something.

::: plate For you: a lookup, in the words of mechanics
```zayn exercise lookup.zayn level=3 symbols=screen.json
DEFINE INTENT_FLOW look_up_invoice (
  SATISFIES [SEARCH, NAVIGATE, VIEW]
)

DEFINE FORM search_form (
  INTENT_FLOW look_up_invoice
)
```
In words: To look up an invoice, a user searches, navigates and views. A search form serves that flow.

```symbols screen.json
{
  "elements": ["search_form", "promo_banner"]
}
```
:::

Before you run it, write the codes you expect, and how many times each. Then run it and compare.

Now say each word as a verb of the law, and run it again with the inventory, at level 3: `zayn check lookup.zayn --level 3 --symbols screen.json`. Write what you expect first. Try before you read on.

::: plate The verbs said, and the inventory given
```zayn lookup.zayn level=3 symbols=screen.json
DEFINE INTENT_FLOW look_up_invoice (
  SATISFIES [FILTER, LOCATE, READ]
)

DEFINE FORM search_form (
  INTENT_FLOW look_up_invoice
)
//--> INTENT_ORPHAN search_form
//--> INTENT_ORPHAN promo_banner
```
In words: To look up an invoice, a user filters the list, goes to an invoice and reads it. A search form serves that flow. The screen holds the form and a banner.
:::

Two elements are reported. The banner you expected. The form is the surprise: it names its flow, and the flow is lawful. Go on until the verifier answers clean and every line of your file is true. Do not give the banner a verb it does not serve: the declaration would be untrue.

Here is a form the verifier accepts, with the banner gone from the screen.

::: plate A form the verifier accepts
```zayn lookup.zayn level=3 symbols=screen-kept.json
DEFINE INTENT_FLOW look_up_invoice (
  SATISFIES [FILTER, LOCATE, READ]
)

DEFINE FORM search_form (
  INTENT_FLOW look_up_invoice,
  SATISFIES [FILTER]
)
//--> clean
```
In words: To look up an invoice, a user filters the list, goes to an invoice and reads it. The search form serves that flow, and a user filters with it.

```symbols screen-kept.json
{
  "elements": ["search_form"]
}
```
:::

It is clean, and the form says twice what it is for: once by naming its flow, once by a verb of its own. For the trace, the verifier reads the second. Should an element that names its flow answer through it?

A verb says what a user does. The next chapter gives the {{n:lang.kinds}} kinds of declaration that say where, and the whole grammar on one page.
