---
id: amendment-from-evidence
part: 7
number: 18
title: Amendment from evidence
stage:
  built: "Article VII as data; a lineage of {{n:law.lineage}} dated entries inside the law's file; {{n:law.retired}} retired and {{n:law.burned}} reserved numbers; an evidence field on each of the {{n:law.rules}} rules; the amendments of versions 3.11, 3.12 and 3.16 answered by the verifier on this page; {{n:pin.files}} data files that record the version of the law they were checked against, and a pack of {{n:pack.files}} files, each with its hash"
  designed: "a law in four layers: statute, core, commons and local; the test and the record by which a contributed rule is admitted"
  next: "rules moved to an instrument as each instrument is built, and a law fed by the corrections of the people who use it"
status: draft
research: research/ch18.md
fixtures: [unknown-signal, unknown-signal-lawful, intent-orphan, field-misplaced, field-misplaced-lawful, menu-landing-not-first, menu-label-repeats-parent, menu-label-duplicate, menu-lawful]
---

An amendment is a change to what the law requires. In this chapter I tell how Zayn's law changes. I read its history in the file that holds it. I give three cases from the record: a remark on a screen that turned out to be law already, two rules that contradicted each other, and a check that ran before a rule was written for it. Then I list what moves when one rule moves.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field amends its standards by versions. The Web Content Accessibility Guidelines are at version 2.2, a W3C Recommendation. Its page lists the success criteria that are new in 2.2, and W3C's page on what is new says that the criteria of 2.0 and 2.1 are "essentially the same in 2.2, with one exception": criterion 4.1.1, which is "obsolete and removed". The standard prints the reason under the criterion's number: assistive technology "no longer has any need to directly parse HTML". The number stays on the page, with its note.

The W3C Process Document says how a Recommendation changes after it is published. It names a correction and an addition, and calls the two together "candidate amendments".

A regulation can then name one version. The fact sheet of the United States rule on the web content of state and local governments names "Version 2.1, Level AA" as its technical standard, with dates of compliance in April 2027 and April 2028.

A design system grows by criteria. The GOV.UK Design System asks of a proposal that there be evidence it would be "useful for many teams or services", and that it be unique. A linter, which is a tool that checks source code against rules, does the same for its rules: ESLint lists guidelines for a rule of its core, and says that since 2020 it accepts a new one only for a new feature of the language it checks.

And the field has a convention for what a version number promises. Semantic Versioning moves the first number when a change breaks what relied on the version before, the second for what is added, the third for a fix.

So the field amends by versions, admits by criteria, and keeps a removed number on its page. Each source was read on 23 November 2026, and Appendix F lists them.

## The principle

**The law changes only on evidence, and every change stays on the record: its date, its cause, and what it replaced.**

The law says so itself, in its last article.

{{article:amendment}}

The article sets two burdens. To add a protection, the harm must be shown. To remove one, the harm must be shown to be gone. It names what is not a ground. And its last sentence is about numbers: a rule's number is a name, and a name that is given twice means two things.

## The law's history, in its file

The law carries its history with it. The lineage is a list of dated entries, one for each state of the law: {{n:law.lineage}} entries, from version 2.0 on 3 August 2026 to version {{n:law.version}} on 12 November 2026. Most entries canonize a rule, which means that they give it a number and a place in a set. Some amend a rule and add none. Some are corrections of wording. Some change a word or a name.

What tells an amendment from a correction of wording? One question. The document that sets the law's architecture calls it the substance test: "does any interface that was lawful before become unlawful after — or must any conforming implementation change anything it does?" A conforming implementation is a tool that keeps to the law. If the answer is no, the change is a correction of wording, "however much prose changed". The first entry of 6 August 2026 is one: two lines of the law named a file that had moved, and no requirement moved with them.

The numbers have a history too. The rules are numbered up to {{n:law.highest}} and the law holds {{n:law.rules}}, so {{n:law.unused}} numbers are out of use. {{n:law.retired}} are retired: each was a duplicate, folded into the rule that survives it, and the survivor says which number it absorbed. {{n:law.burned}} are reserved for good, because an earlier numbering had given them to what are now Rules 82 and 83. A number that is only proposed can be taken too. The docket is the file where changes to the law are proposed together and ruled item by item, in sittings that it calls passes. Rule 126 was first written under the number 125. The docket had already kept 125 for another candidate, so the new rule took 126. The docket's lesson: "a proposed number is not a free number".

Each of the {{n:rule.evidence}} rules carries a field named `evidence`: what happened, where and when. Since version 3.13, an amended rule keeps its first evidence and gains a dated clause after it. The architecture document gives the rule for that field in four words: "Evidence is never corrected." What happened stays as it was written.

## A remark that was already law

In August 2026 an AI agent that was not consulting the law built a status dashboard for me. I rejected two versions and corrected the third. The ledger is the dated list of what the project found, and it says what those corrections were worth: "Every correction he made was already law."

The first version was a grid of tiles, and the second was cards with coloured meters. My words, as the ledger keeps them: "use a classical table format not cards, it's more direct and less stressing to me". Rule 119 and Rule 94 already forbade both. Then came two red blocks, one under the other. Mine again: "having two red divs one under the other means we are not focusing on one critical thing." That was Rule 87. Then every table was wrapped in a container that scrolls sideways, which Rule 14 forbids. When that was removed, each row was stacked into a block, which is the first thing that Rule 95, a rule of the culture the law calls `field`, tells its reader to avoid.

So what did the episode add to the law? Five candidates were put to the docket on 15 August 2026. Two were refused as new law, because each was a rule that existed, and each of those rules was extended by a sentence. Three were canonized, and Rule 129 is one of them. The column that the scrollbar hid had carried my next action. The law forbade the scrollbar. It did not say "which column survives when width genuinely runs out", and that is the whole of the new rule.

{{rule:129}}

Why is this evidence, and not compliance? Because the law stayed shut while it happened. The ledger's sentence names the law's file: "Nobody consulted `rules.json` while it happened". The docket gives the size of the case, "one surface, one operator, one implementer", and I print it at that size.

## Two rules that contradicted each other

On 16 August 2026 Rule 3 and Rule 118 were put side by side: for the first time, by the ledger's account. Both speak of colour. Rule 3 kept the colour of danger for a failure of the system. Rule 118 gives `danger` to a value that is critical or exceeded. So a credit limit that is exceeded, coloured as danger, obeyed one rule and broke the other.

Which rule outranks the other? Neither: the ledger records that the law has "no precedence mechanism at all". I had delegated that pass to an AI agent, and the docket records it as a delegation. The pass invented no rule of precedence. On the colour of danger it gave the subject to Rule 118, "on the merits, not by seniority", and it amended both rules until they no longer overlapped: "Rule 3 owns chrome. Rule 118 owns what a colour means about a record." Chrome is the frame of an interface: its bars, its borders, its controls. Each rule now points at the other in a field named `see_also`, and {{n:rule.see_also}} rules carry such a pointer.

The language took Rule 118's statuses the same day, as the closed list of the field `SIGNALS`: success, warning, danger, info and muted. Here is a screen that uses two words of chrome as statuses.

::: plate Two words of chrome, as statuses
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger, neutral, accent]
)
//--> UNKNOWN_SIGNAL credit_limits
//--> UNKNOWN_SIGNAL credit_limits
```
In words: On the screen of credit limits a user scans, compares and goes to a limit. Its values carry three statuses: danger, neutral and accent.
:::

Two refusals, and both cite Rule 118. The word `danger` passes. The other two belong to the frame, and the frame is Rule 3's. Here is Rule 118 as it stands after the amendment.

{{rule:118}}

Its tier is the law's word, and chapter 17 reads it. The card's last line is the reason for a closed list: a palette small enough to hold in one's head. Here is the same screen with Rule 118's word alone.

::: plate An exceeded limit, said as danger
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger]
)
//--> clean
```
In words: The same screen. Its values carry one status, danger: here, a limit that is exceeded.
:::

Clean! Before the amendment this colouring was, in the docket's words, "forbidden by one rule and required by another". The record counts the change an amendment: two rules changed what they require.

## A check that became a rule

The usual order is a defect, then a rule, then a check. In one case the order was reversed. The verifier's check for an element that answers to no intent, whose code is `INTENT_ORPHAN`, had run since the first version of the language. Its findings cited Article II alone, with no numbered rule behind them. On 2 November 2026 Rule 130 was written for it, and the law went to version 3.12.

Here is a screen with one declaration, and its inventory: the list of the elements of the screen, which the verifier is given in a small file.

::: plate An element the inventory holds
```zayn balance.zayn level=3 symbols=screen.json
DEFINE COMPONENT balance_card (
  SATISFIES [READ]
)
//--> INTENT_ORPHAN hide_button
```
In words: The balance is something a user reads. The inventory of the screen holds a second element, a button that hides the balance, and no declaration says what a user does with it.

```symbols screen.json
{
  "elements": ["balance_card", "hide_button"]
}
```
:::

Refused. Read the third line of the report: it cites Rule 130. The record says that before version 3.12 the same file got the same refusal, citing the article alone, and the lineage sums up the amendment: "the refusal now cites a rule". No verdict moved. Rule 130's evidence says how it entered, and what it does not claim: "Canonized v3.12 from an existing check, which is the reverse of the usual order and is stated as such." Then: "No defect in a shipped interface is cited and none is claimed."

The repair gives the button a declaration.

::: plate The button, asked what it is for
```zayn balance.zayn level=3 symbols=screen.json
DEFINE COMPONENT balance_card (
  SATISFIES [READ]
)

DEFINE INTERACTION hide_button (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)
//--> clean
```
In words: A user reads the balance. With the button a user hides it; the act can be undone or cancelled, and the button says that it can be taken back.
:::

Clean. The ruling of that day weighed two more of the kinds of finding that cite an article only, and left them so.

## What moves with one rule

On 8 November 2026 I looked at a menu of the Zayn site and wrote a remark. Rule 116 was amended that day, and the law went to version 3.16. Chapter 19 follows that remark from my sentence to the check. Here is what moved.

The law's file moved first: the rule's text, then the version, the date and one more entry of the lineage. The language moved: fields entered it, so that a declaration can state a menu with levels. The contract moved: it is the data file that binds each kind of finding to the law it cites, and with the kinds that judge a menu it holds {{n:diag.total}}. The suite moved. The suite is Zayn's set of fixtures, and a fixture is a declaration kept with the answer it must get: one came for each new kind of finding, and one for a lawful menu, which makes {{n:fix.total}}. The Zayn site moved, because its menu is a declaration too, and the new kinds of finding judge it.

Then the pins moved. A pin is the version of the law that a file records as the one it was checked against.

{{pins}}

At the version of Zayn this book reads, {{n:pin.files}} data files carry a pin; counted at this build, {{n:pin.agree}} of them name version {{n:law.version}}. A pin moves by a separate act, after the suite has run against the new law. The ledger tells what that act guards against. In August 2026 the suite's manifest, the file that lists the fixtures and their answers, was found pinned three versions behind the law it had passed against. It was found "by grepping for the field, not by any check": by a search through the files, made by hand.

A version is a name, and a name can be kept while the text under it changes. So each file that a team or a tool relies on also carries a hash. A hash is a fingerprint computed from a file's bytes. The pack is the set of {{n:pack.files}} files that a user of the law pins, each with its hash, and its document sets the two side by side: "A version number says which edition you meant. A hash says the bytes you have are that edition." The version names; the hash proves.

One change in this chapter's record moved the language and left the law's version where it was. Chapter 7 showed it: a field on a kind of declaration that does not carry it has been refused since version 1.4 of the language, which numbers its versions apart from the law, and that finding cites Article II and no rule.

## What I refused

**I refused a sixth status.** In my pass of 13 August 2026 a draft proposed to add a value to the statuses of Rule 118. The ruling adopted the proposal without the value: "the closed set stays at five". The data file of the vocabulary says what a sixth would be: "a constitutional amendment, not an implementation choice".

**I refused a title that promised more than its rule.** Rule 69's title promised a law for haptic feedback, the answer a device gives by touch, and its text governed touch targets and swipes. The same pass renamed the rule for what it governs. The docket's line is: "the haptic law waits for device evidence".

**A rule waits for a second case.** On 3 November 2026 a pass that I had delegated met a candidate rule: one subject, one page. It kept the candidate open, with these words: "The evidence is one author's reading of one site, not a measurement; it is not ratified now." Four days later another candidate, drawn from one site, was written up and kept as a candidate: "it would want a second site before a ruling". One case shows that a defect exists. Article VII asks that a harm be "real and recurring", and the docket states the size of every case it admits: Rule 129 rests on one surface, and its record says so.

**The record refuses to be rewritten.** The ledger opens on its rule: "Append, never rewrite." An entry that is later found false keeps its text and gains a correcting entry. One section of the ledger lists the corrections the project made to itself, and gives its reason: a project "that argues about drift and hides its own errors has refuted itself". Drift is a text that no longer matches the data it describes.

[AUTHOR: the stake of this chapter, in your words: what a law that changes only on evidence protects, and from whom.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below belong to the amendments of versions 3.11, 3.12 and 3.16, and to the one change of the language: the closed list of statuses, the check that Rule 130 now backs, the menu with its lawful form, and the field on the wrong kind.

## Where the field leads

The field leads on how many cases stand behind a rule. A design system asks for evidence from many teams. The W3C Process asks for wide review of a change, with the aim that the web community, "including the general public", has had notice of it. Several of Zayn's newest rules rest on one surface, and the docket says so of each. It also names the risk of a law that takes its rules one case at a time: "Three new numbers from one surface is a lot, and the risk is corpus inflation." A corpus is a body of recorded cases.

The field leads on procedure. The W3C Process is a document of its own, with its terms for a correction, an addition and a review. On Zayn's docket I rule alone, and the docket records each pass I delegated as a delegation.

Zayn's law leads on what it keeps of each change. Every rule carries its evidence, every change is a dated entry in the law's file, and a number is never given twice: the pack's document promises of one rule that it "means the same thing in ten years". And an amendment reaches the tools at once: on 16 August and on 8 November 2026 the language took an amendment on the day it was ruled.

Both sides know the cost of a pin. A regulation that names version 2.1 goes on naming it when the standard is at 2.2. A file pinned at one version of Zayn's law goes on reading that version, and the docket says of a user of the law that it "moves its pin deliberately". Zayn's law numbers its versions its own way: one of its first two numbers moves when its substance moves, the second from 3.1 to 3.17, and a third, as in 3.7.1, marks a correction of wording. So version 3.16, which added three refusals of a menu, is a step of the second number, where Semantic Versioning would ask for the first; a team that keeps its pin keeps the law it checked against.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The history told here is data of the law's file at version {{n:law.version}}, and the amendments of versions 3.11, 3.12 and 3.16 were answered on this page by the verifier of release {{n:release.version}}. What was lawful before a version is told from the record: this page runs one verifier, today's. Two rules that touch one subject are reconciled by amending both, and the pair is found by whoever puts them side by side; a rule of precedence, or a check for two rules on one subject, is a question that the docket has filed for me. The evidence behind a rule is of the size its field states: a body of recorded corrections for some, one surface for others, a decision or a check for two, and each rule says which. The law in four layers, with its commons, is a design: it is written, and it waits for my pass, section by section.

## In your hands

Here is the menu that the Zayn site had from 6 to 8 November 2026, written small. A `NAV_GRAPH` is the kind of declaration that states an entry of a menu. `LABEL` is the name the menu shows, `TARGET` is the page the entry leads to, and `ENTRIES` lists its children in order. An entry with a target and children is a section, and the page it leads to is its landing page.

::: plate For you: a section and its two pages
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [invoices, payments]
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LANDING_NOT_FIRST billing
```
In words: The main menu has one section, Billing, which leads to the billing home. Under it the menu shows two entries, Invoices and Payments.
:::

Write the code you expect, then open the verifier's answer. The section leads to a page that the level under it does not show. Put the page back under the section's name, and say what you expect.

::: plate The page back, under the section's name
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [billing_page, invoices, payments]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Billing",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LABEL_REPEATS_PARENT billing_page
```
In words: The same menu, and the section's page is now its first entry, under the same name as the section: Billing.
:::

Refused again, for the name. This is the defect my first remark named, in its plainest form: a reader meets the section's title, then finds it again among its entries. Chapter 19 gives that remark's own example. Give the page another label, and put it last.

::: plate Another label, in last place
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [invoices, payments, billing_page]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Overview",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LANDING_NOT_FIRST billing
```
In words: The section's page is now named Overview, and it is the third entry of three.
:::

Refused for the place. The report's first line counts it for you: entry 3 of 3. Repair it. Try before you read on.

::: plate The landing page first, under its label
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [billing_page, invoices, payments]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Overview",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> clean
```
In words: The section Billing opens on its page, named Overview, and then shows Invoices and Payments.
:::

Clean. Now go back to the first menu of this exercise, the one with its landing page absent, and delete one line: `TARGET billing_home`. Change nothing else, and say what you expect.

::: plate The same defect, with one line less
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  ENTRIES [invoices, payments]
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> clean
```
In words: The section Billing no longer says where it leads. Under it the menu shows Invoices and Payments.
:::

Clean. The specification of the language calls an entry with children and no target a bar, like the main menu, and a bar has no landing page. So the section passes once it stops saying where it leads. Should an entry that carries a label and leads nowhere be read as a bar? That is a remark for the law, and the law grows from remarks: this one is filed with the book's findings, for the next pass.

The usual order begins with a remark that someone wrote down. The next chapter follows one, field by field, from the sentence to the check.
