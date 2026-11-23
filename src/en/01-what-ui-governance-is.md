---
id: what-ui-governance-is
part: 1
number: 1
title: What UI governance is
stage:
  built: "the law as data, {{n:law.rules}} rules at version {{n:law.version}}; the verifier, run on this page; the corpus of {{n:corpus.records}} corrections as data; the audit of the painted page, as a tool of Zayn's repository"
  designed: "the path from a user's correction to a numbered rule, with a way to capture it in every application; the drawing of a declaration on each medium, written as data that each project's renderer reads"
  next: "the law served to an AI model while it generates"
status: draft
research: research/ch01.md
fixtures: [role-acts-without-consequence, role-acts-without-consequence-lawful, role-undeclared, role-undeclared-lawful, clean-minimal]
---

UI governance holds an interface to rules: the rules it keeps toward its user, the instrument that checks each rule, the moment it checks, and the way the rules change. In this chapter I say why it is needed now, when AI models draw interfaces and AI agents use them. I show a defect that comes back after it is corrected. Then I set out the three moves of this book, each shown once on a declaration that runs, and I end on the reader's first act.

[AUTHOR: the opening. The Zayn site prints your sentence of 9 November 2026, quoted below in "The defect that comes back"; is it the book's first words?]

Zayn is the subject of this book: a language of declarations, a law for interfaces kept as data, and the instruments that hold an interface to that law. Four words carry the book. A **declaration** is a few lines that say what a user is doing on a surface, and nothing of how the surface is drawn. A **user** is whoever acts through an interface: a person, or an AI agent. The **law** is Zayn's constitution for interfaces: {{n:law.rules}} numbered rules, kept as a data file. And the **verifier** is the program that checks a declaration against the law. Its report is a list of findings, and a finding that is an error is a refusal.

## The field

The field governs interfaces with four kinds of instrument. It advises: Jakob Nielsen's ten heuristics of usability are, in their page's words, "broad rules of thumb". It sets criteria: the accessibility guidelines, WCAG, from W3C, the body that writes the web's standards, are written "as testable criteria for objectively determining if content satisfies them", and a regulation of the United States names one version of them for the web pages and apps of state and local governments. It measures the painted page, the interface as a browser draws it: the engine axe-core says that with it "you can find on average 57% of WCAG issues automatically", by its own count. And it refuses code: a linter, a tool that checks source code against rules, can be set so that a broken rule ends a build, the run that assembles a product.

Each source was read on 21 or 23 November 2026, and Appendix F lists them. W3C's page on evaluation says of every tool, in one line: "no tool alone can determine if a site meets accessibility standards". So the field advises, sets criteria, measures and refuses, and its instruments read how a page is drawn: its code, or the page itself.

## The principle

**A remark corrects one page, once; a rule kept as data is checked on every declaration an instrument reads.**

The Zayn site states the thesis behind it: "The only correction that keeps pace with a generator is a rule that the generator can be made to check." A generator is a program that writes interfaces, and today it is often an AI model.

## The defect that comes back

On 9 November 2026 I corrected a site of mine twice for the same defect. At eleven in the morning, a word of two letters stood alone on the last line of a paragraph, and I wrote, as the corpus keeps my typing: "i raise dozens of times before in many projects the issue of visual equilibrium of text lines". At twenty-six past one, the same defect was back on a chart's label that the morning's repair had missed: "how many times I told you to avoid this ugly word taking its own line!!!" Two remarks, one defect, one day. An hour later I wrote the sentence that the Zayn site now prints on its page about why Zayn exists: "what makes my fatigue in all my projects is never the more complex technical challenges: it's always UI!"

The corpus is Zayn's file of corrections: {{n:corpus.records}} of them, each with its words, its place and its date. {{n:corpus.verbatim}} keep the person's words as typed, and {{n:corpus.repeat}} name an earlier correction of the same defect. Chapter 2 reads it whole.

Why does a defect come back? The front page of Zayn's repository, the store of its files and their history, answers: "Interfaces are decaying in the AI era — and not for lack of capable generators." The Zayn site gives the reason in one sentence: "A model repeats the habits of the interfaces it learned from, at machine speed and under any instruction." On 15 August 2026 I said it to an AI model, in the middle of a correction: "This is the power of dogmatic influence you got from your training data." A remark corrects the page in front of me. The habit stays, and the next page has it again.

## Three moves

This book answers with three moves, and each is shown once here.

**Declare what a user is doing.** A declaration states the user's intent and each control's promise, and says nothing of shape or colour. An `INTERACTION` is one control. `SATISFIES` lists what the user does with it, and `ALWAYS_REACHABLE` what the user can always get to, such as undo. `ROLE` is the control's promise: `inert` promises that acting on it changes nothing. Here is a dashboard with two totals.

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

**Hold it to the law.** Refused! The overdue total promises to inform and declares that it acts. The report cites three rules, Rule 119 first, and Article II of the law. Rule 119 was written from this defect, a tile that looks like information and behaves like a button, corrected in the interface of a banking product in April 2026. Here the verifier refuses it before anything is drawn. The repair gives the act a control of its own.

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
In words: The two totals only inform: the user reads one and scans the other. A third control sends reminders, and it says that what it does can be undone.
:::

Clean. The totals inform, and the act is a control whose promise says that it changes what is true (here, the reminders are sent) and can be undone. The verifier does not say what the control looks like: that is the drawing's business. The control is held to its promise.

The user can be an AI agent. Here is the same total, read by a program. A `VIBE`, the kind of declaration that names a medium, says so with `SURFACE_AS machine`, and `ACTOR agent` names an AI agent as the one who acts.

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

Part VII reads the three ways the law is held. The verifier refuses a declaration before anything is drawn. An audit measures the painted page: one of its checks finds a short last line in a paragraph of running text, the defect I corrected twice in one day. And a person judges what only a person perceives; the Zayn site says of testing with people: "Nothing replaces it. No instrument here perceives for a person."

**Keep the corrections, so that they become rules.** The law's last article says how it grows: "The law grows only from evidence". A correction that happened, was corrected, holds beyond its project and can be decided can become a rule with a number. Chapters 18 and 19 tell how, on the record.

## What I refused

**I deferred requiring a promise on every control that acts, until the evidence comes.** On 19 August 2026 I ruled that requiring a role is, in the design note's words, "deferred to evidence". A warning was built in its place, and it refuses nothing. The exercise of this chapter ends on it.

**The specification refuses a declaration that names a widget.** A widget is a drawn control, a button or a card. The specification of the language says: "A declaration that needs to say \"card\" has stopped describing intent." So a promise names what happens when the user acts, and never what the control looks like. The contract, the file that binds each kind of finding to the law, gives the reason the promises were not named after widgets: that "would have produced card, button and table".

**The law refuses a rule of taste.** Its last article: "Trends, fashion, and developer convenience are not grounds." A rule comes from a defect that happened.

[AUTHOR: the stake of this chapter, in your words: why the governance of interfaces became your work, and what you want a reader to hold after this page.]

## The court

The court of a chapter is what proves it. In this chapter it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are those of a control's promise: a promise that contradicts the act, with its lawful twin; a file whose controls declare no promise, with its twin; and the smallest lawful file of the suite.

## Where the field leads

The field leads on the person. The Zayn site says it of itself: "The law judges structure, and usability testing judges the experience." Usability testing and review decide what no instrument perceives.

The field leads on regulation. Its criteria are named by a regulation of the United States, with dates of compliance. Zayn's law is a body of rules for teams and their tools.

The field leads on the painted page, where the corrections of the corpus are seen. The ledger, the dated list of what the project found, records a test of 12 August 2026, made before a control could state its promise: two payment surfaces "differing by seven broken laws" were the same declaration, and both ran clean. Zayn's answer is a second instrument on the painted page, and a person.

Zayn leads on the moment. A promise that contradicts the act is refused in the declaration, before a pixel exists, whoever the user is, and the refusal names its rule.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The law is data at version {{n:law.version}}, and every plate of this page was run by the verifier of release {{n:release.version}}. The corpus of corrections is data. The audit of the painted page is a tool of Zayn's repository, and its runs are told in Part VII as recorded. The way a correction becomes a rule is told on the record in chapters 18 and 19, and a way to capture a correction where it is made, in every application, is designed.

## In your hands

Here is a real first draft, printed on the Zayn site: the language switch of a site of mine, a control that changes the language of the page, read by hand into a declaration. Write the finding you expect, by its code, then open the verifier's answer.

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
In words: A user acts on the language switch, with undo and cancel within reach; the switch promises to change only what is shown.
:::

The same kind of finding as the dashboard's: a control whose promise and act disagree, whatever the control is, so the report cites the same rules. `navigate` promises to change what is shown, never what is true, and the switch declares that it acts. There are two repairs. Try one, then the other, and say what you expect of each.

::: plate Repair A: the user chooses
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [SELECT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE navigate,
  ACTOR reader
)
//--> clean
```
In words: The user selects a language, and the switch changes what is shown.
:::

::: plate Repair B: the switch acts, and can be undone
```zayn language.zayn
DEFINE INTERACTION language_switch (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible,
  ACTOR reader
)
//--> clean
```
In words: The user acts, the switch changes what is true, and it can be undone.
:::

Both clean. The verifier accepts both, and only one is true of the site: does switching the language change what is shown, or what is true? That is a person's reading of the surface, the third way the law is held, in your hands. On the site, the switch changes what is shown and nothing that is true, so repair A is the true one, and it is the site's own. Now delete the line `ROLE navigate` from the first draft, and say what you expect.

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

A warning, and the exit code, the number the command returns (0 when the file passes, 1 when it is refused), is 0: the contradiction is gone because the promise is gone. Should a control that acts be required to say what it promises? I deferred that question to evidence, and this switch is one piece of it.

The next chapter reads the corrections whole: what {{n:corpus.records}} of them show about the defects a generator repeats.
