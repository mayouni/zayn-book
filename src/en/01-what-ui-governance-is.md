---
id: what-ui-governance-is
part: 1
number: 1
title: What UI governance is
stage:
  built: "the law as data, {{n:law.rules}} rules at version {{n:law.version}}; the verifier, run on this page; the corpus of {{n:corpus.records}} corrections as data; the audit of the painted page, as a tool of Zayn's repository"
  designed: "the drawing of a declaration on each medium; the path from a user's correction to a numbered rule, with a way to capture it in every application"
  next: "the law served to an AI model while it generates"
status: draft
research: research/ch01.md
fixtures: [role-acts-without-consequence, role-acts-without-consequence-lawful, role-undeclared, role-undeclared-lawful, clean-minimal]
---

UI governance is the governance of interfaces: the rules an interface keeps toward its user, the instrument that checks each rule, the moment it checks, and the way the rules change. In this chapter I say why it is needed now, when AI models draw interfaces and AI agents use them. I show the defect that comes back after it is corrected. Then I set out the three moves of this book, each shown once on a real surface, and I end on the reader's first act.

[AUTHOR: the opening. The Zayn site prints your sentence of 9 November 2026, quoted below in "The defect that comes back"; is it the book's first words?]

Four words carry the book. A **declaration** is a few lines that say what a user is doing on a surface, and nothing of how the surface is drawn. A **user** is whoever acts through an interface: a person, or an AI agent. The **law** is Zayn's constitution for interfaces: {{n:law.rules}} numbered rules, kept as a data file. And the **verifier** is the program that checks a declaration against the law. Its report is a list of findings, and a finding that is an error is a refusal.

## The field

The field governs interfaces with four kinds of instrument. It advises: Jakob Nielsen's ten heuristics of usability are, in their page's words, "broad rules of thumb". It sets criteria: the accessibility guidelines write theirs "as testable criteria for objectively determining if content satisfies them", and a regulation of the United States names one version of them for the web pages and apps of state and local governments. It measures the painted page: the engine axe-core says that with it "you can find on average 57% of WCAG issues automatically", a figure of its own. And it refuses code: a linter, a tool that checks source code against rules, can be set so that a broken rule ends a build, the run that assembles a product.

Each source was read on 21 or 23 November 2026, and Appendix F lists them. So the field advises, sets criteria, measures and refuses, and its instruments read the drawing: the code of a page, or the page itself. W3C's own page on evaluation adds the limit of all of them in one line: "no tool alone can determine if a site meets accessibility standards".

## The principle

**A remark corrects one page, once; a rule kept as data is checked on every declaration an instrument reads.**

The Zayn site states the thesis behind it: "The only correction that keeps pace with a generator is a rule that the generator can be made to check." A generator is a program that writes interfaces, and today it is often an AI model.

## The defect that comes back

On 9 November 2026 I corrected the Zayn site twice for the same defect. At eleven in the morning, a word of two letters stood alone on the last line of a paragraph, and I wrote, as the corpus keeps my typing: "i raise dozens of times before in many projects the issue of visual equilibrium of text lines". At twenty-six past one, the same defect was back on a chart's label that the morning's repair had missed: "how many times I told you to avoid this ugly word taking its own line!!!" An hour later I wrote the sentence that the Zayn site now prints on its page about why it exists: "what makes my fatigue in all my projects is never the more complex technical challenges: it's always UI!"

The corpus is the data file where Zayn keeps such corrections: {{n:corpus.records}} of them, each with its words, its place and its date. {{n:corpus.verbatim}} keep the person's words as typed, and {{n:corpus.repeat}} name an earlier correction of the same defect. Chapter 2 reads it whole.

Why does a defect come back? My answer, on the front page of Zayn's repository: "Interfaces are decaying in the AI era — and not for lack of capable generators." A generator repeats the habits of the interfaces it learned from. On 15 August 2026 I said it to one, in the middle of a correction: "This is the power of dogmatic influence you got from your training data." A remark repairs the page in front of me. The habit stays, and the next page has it again.

## Three moves

This book answers with three moves. Each has its part of the book, and each is shown once here.

**Declare what a user is doing.** A declaration states the user's intent and each control's promise, and says nothing of shape or colour. Here is a dashboard with two totals.

::: plate Two totals, and one of them acts
```zayn dashboard.zayn
DEFINE INTERACTION revenue_total (
  SATISFIES [READ],
  ROLE inert
)

DEFINE INTERACTION overdue_total (
  SATISFIES [SCAN, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE inert
)
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE overdue_total
```
In words: A dashboard shows two totals. The user reads the revenue, and both totals promise only to inform. Touching the overdue total does something, which can be undone.
:::

**Hold it to a law.** Refused! An `INTERACTION` is one control, `SATISFIES` lists what the user does with it, and `ROLE` is its promise: `inert` promises that acting on it does nothing. The overdue total promises to inform and declares that it acts. The report cites Rule 119, *A Card Is Not a Button*, with two other rules, and Article II of the law. A tile that looks like information and behaves like a button is one of the defects that generators repeat, and here the verifier refuses it before anything is drawn. The repair gives the act a control of its own.

::: plate The act, given a control of its own
```zayn dashboard.zayn
DEFINE INTERACTION revenue_total (
  SATISFIES [READ],
  ROLE inert
)

DEFINE INTERACTION overdue_total (
  SATISFIES [SCAN],
  ROLE inert
)

DEFINE INTERACTION send_reminders (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: The two totals only inform: the user reads one and scans the other. A third control sends reminders, and it says that what it does can be taken back.
:::

Clean. The totals inform, and the act is a control whose promise says that it changes what is true and can be undone. The verifier does not say what the control looks like: that is the drawing's business. It is held to its promise.

The user may be an AI agent. Here is the same total, read by a program: a `VIBE` with `SURFACE_AS machine` says that the surface is read by a program, and an AI agent is its actor.

::: plate The same total, for an AI agent
```zayn invoices.zayn
DEFINE VIBE invoices_api (
  SURFACE_AS machine
)

DEFINE INTERACTION overdue_total (
  SATISFIES [SCAN, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE inert,
  ACTOR agent
)
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE overdue_total
```
In words: The surface is read by a program, and an AI agent scans the overdue total; acting on it does something that can be undone, though it promises to inform.
:::

The same refusal. The promise is read the same whoever the user is.

The law has three instruments, and Part VII reads them. The verifier refuses a declaration before anything is drawn. An audit measures the painted page, the interface as a browser draws it: one of its checks finds the word alone on its last line that I corrected twice in one day. And a person judges what no instrument perceives. The Zayn site says it of testing with people: "Nothing replaces it. No instrument here perceives for a person."

**Keep the corrections, so that they become rules.** The law's last article says how it grows: "The law grows only from evidence". A correction that recurs, generalises and can be decided becomes a rule with a number. Part VII tells how, on the record.

## What I refused

**I refused to require a role on every act until the evidence comes.** On 19 August 2026 I ruled that requiring a role is, in the design note's words, "deferred to evidence". A warning was built in its place, and it refuses nothing. The exercise of this chapter ends on it.

**The specification refuses a declaration that names a widget.** A widget is a drawn control, a button or a card. The specification of the language says: "A declaration that needs to say \"card\" has stopped describing intent." The contract, the file that binds each kind of finding to the law, says why the promises of a control were not named after widgets: that "would have produced card, button and table".

**The law refuses a rule of taste.** Its last article: "Trends, fashion, and developer convenience are not grounds."

[AUTHOR: the stake of this chapter, in your words: why the governance of interfaces became your work, and what you want a reader to hold after this page.]

## The court

The court of a chapter is what proves it. In this chapter it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are those of a control's promise: a promise that contradicts the act, with its lawful twin; a file whose controls declare no promise, with its twin; and the smallest lawful file of the suite.

## Where the field leads

The field leads on the person. Usability testing and review decide what no instrument perceives, and the Zayn site says so of itself: "The law judges structure, and usability testing judges the experience."

The field leads on statute. Its criteria are named by regulations, with dates of compliance. Zayn's law is a body of rules for teams and their tools, set beside the guidelines as a body of its own.

The field leads on the painted page, where most of the corrections of the corpus live. The ledger, the dated list of what the project found, records a test of August 2026: two payment surfaces "differing by seven broken laws" were the same declaration, and both ran clean. Zayn's answer is a second instrument on the painted page, and a person.

Zayn leads on the moment. A promise that contradicts the act is refused in the declaration, before a pixel exists, whoever the user is, and the refusal names its rule.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The law is data at version {{n:law.version}}, and every plate of this page was run by the verifier of release {{n:release.version}}. The corpus of corrections is data. The audit of the painted page is a tool of Zayn's repository, and its runs are told in Part VII as recorded. The way a correction becomes a rule is told on the record in chapters 18 and 19, and a way to capture a correction where it is made, in every application, is designed.

## In your hands

Here is a real first draft. An AI agent declared the language switch of a site of the estate, a control that changes the language of the page. Write the finding you expect, by its code, then open the verifier's answer.

::: plate For you: a language switch
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE navigate,
  ACTOR reader
)
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE language_switch
```
In words: A reader uses the language switch, which acts, with undo and cancel within reach; it promises to change only what is shown.
:::

`navigate` promises to change what is shown, never what is true, and the switch declares that it acts. There are two repairs. Try one, then the other, and say what you expect of each.

::: plate Repair A: the reader chooses
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [SELECT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE navigate,
  ACTOR reader
)
//--> clean
```
In words: The reader selects a language, and the switch changes what is shown.
:::

::: plate Repair B: the switch acts, and can be taken back
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible,
  ACTOR reader
)
//--> clean
```
In words: The reader acts, the switch changes what is true, and it can be taken back.
:::

Both clean. The verifier accepts both, and only one is true of the site: does switching the language change what is shown, or what is true? That is a person's reading of the surface, the third instrument, in your hands. Now delete the line `ROLE navigate` from the first draft, and say what you expect.

::: plate The draft, with no promise
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR reader
)
//--> ROLE_UNDECLARED
```
In words: The same switch, and it says nothing of what it promises.
:::

A warning, and the exit code is 0: the contradiction is gone because the promise is gone. Should a control that acts be required to say what it promises? I deferred that question to evidence, and this switch is one piece of it.

The next chapter reads the corrections whole: what {{n:corpus.records}} of them show about the defects a generator repeats.
