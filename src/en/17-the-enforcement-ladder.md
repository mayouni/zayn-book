---
id: the-enforcement-ladder
part: 7
number: 17
title: The enforcement ladder
stage:
  built: "a tier on each of the {{n:law.rules}} rules, in the law's own words; the verifier, whose kinds of finding cite {{n:cite.verifier}} rules, each kind with its fixture; the audit of the painted page, which names {{n:cite.ui}} rules and whose runs are recorded; the checker of a screenshot's facts, run on its example"
  designed: "the audit of a screenshot as a whole, from the picture to the verdict; an audit that refuses at the moment of painting"
  next: "rules moved up the ladder as their instruments are built"
status: draft
research: research/ch17.md
fixtures: [intent-orphan, missing-undo, missing-undo-lawful, irreversible-claims-undo, irreversible-claims-undo-lawful, proposal-commits, proposal-commits-lawful, missing-cancel, missing-cancel-lawful, multiple-violations, unknown-signal, unknown-signal-lawful]
---

The enforcement ladder is the phrase the law's site uses for how its rules are held: each rule is filed under one word, its tier, which names the instrument the rule is owed. In this chapter I read those words. Then I set beside them what answers today: the verifier, which refuses a declaration; the audits, which measure a page; and a person, who judges. I show the verifier and the person at work on one surface, a help desk where an AI agent answers a customer, and the audits on their recorded runs. And I count which rules each instrument names, with the definition of the count printed beside every number.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field knows that its instruments reach part of a rule. The accessibility guidelines, WCAG, are published by W3C, the body that writes the web's standards. Their page on conformance says that the criteria are written "as testable criteria for objectively determining if content satisfies them", and adds that testing them "would involve a combination of automated testing and human evaluation". W3C's page on evaluation says it in one line: "no tool alone can determine if a site meets accessibility standards".

The tools say the same of themselves. axe-core, an engine that tests a page in a browser, says that with it "you can find on average 57% of WCAG issues automatically", a figure of its own, and that it returns an element as "incomplete" where "manual review is needed". A linter is a tool that checks source code against rules. One linter for the markup of a framework, the code that a browser draws a page from, says that it "only catches errors in static code", and sends its reader to a second tool for the page once it is drawn.

And the field gives each rule a severity. ESLint, a linter for code, lets its user set a rule to "warn", which "doesn't affect exit code", or to "error", whose "exit code is 1 when triggered". The exit code is the number a command returns when it ends, and a build, the program that assembles and checks a product, stops on 1.

Each source was read on 21 and 23 November 2026, and Appendix F lists them. So the field has instruments at two moments, before a page is drawn and after, a severity set rule by rule, and a person beside them.

## The principle

**A tier names the instrument a rule is owed; a citation shows the instrument that answers today.**

The law's site calls the tiers a ladder: "Each rule declares one rung of an enforcement ladder, and rules climb as instruments are invented." A rung is a tier. The foot of the ladder is `judgment`, and the roadmap moves a rule up toward `tool` and `machine` as its instrument is built. A move up is a promotion, a change of the law that I rule. The docket, the file where changes to the law are ruled, says what a tier claims, in a sentence on Rule 127: it "is honest about which instrument owes the check; it is not a claim that the check runs today". A citation, the other half of the principle, is a rule named by number in what an instrument reports.

## The four tiers, as filed

Every rule has an entry named `enforcement`, and its value is one of {{n:law.tiers}} words. Here they are, with how many rules the law files under each, and beside them the count by citation that the rest of this chapter explains.

{{tiers}}

Read the first two columns as the law's filing. The record gives each word its meaning in a table of a proposal of the project, *The Second Founding*: `judgment`, "a human decides, until an instrument is invented"; `machine-later`, "the law's own admission that the instrument is missing"; `machine`, "a declaration checker refuses it"; `tool`, "measured by a runnable instrument". From the foot of the ladder the rungs go `judgment`, then `machine-later`, then `tool` and `machine`, the two rungs whose instrument is named, side by side at the top.

The other columns are what the instruments name at this version, and they follow the filing in part. Rules 38 and 107, filed under `machine`, are named by the audit of the painted page. Several rules filed under `judgment` are cited by the verifier for one clause. That is the docket's sentence at work: a tier says which instrument owes the check, and a citation says which one answers today. Whether the filing should follow the instruments is a question filed for the law.

## Three instruments

The document that sets the law's architecture puts its instruments at two moments: "The constitution is enforced twice, at two different moments." Before a page is drawn, the verifier reads a declaration and refuses it. After, an audit measures the painted page, the interface as a browser draws it. And at every moment a person can read a rule, judge a surface against it, and cite its number.

**The verifier refuses.** Here is the help desk's home screen, checked at level 3, where the verifier is given an inventory: the list of the elements on the screen.

::: plate A ticker that no one asked for
```zayn help.zayn level=3 symbols=elements.json
DEFINE SCREEN help_home (
  SATISFIES [DISCOVER, READ]
)

DEFINE COMPONENT answer_card (
  SATISFIES [READ]
)
//--> INTENT_ORPHAN news_ticker
```
In words: On the help desk's home a user discovers and reads, and an answer card is something the user reads. The inventory says the screen also holds a ticker of news.

```symbols elements.json
{
  "elements": ["help_home", "answer_card", "news_ticker"]
}
```
:::

Refused, under Rule 130, which the law files under `machine`. Rule 130 has an entry named `lint`, which names the instrument the rule is owed, and it describes this very check: "a declared element that traces to no intent, decided against an element inventory". The verifier needed the inventory, given on the command line: `zayn check help.zayn --level 3 --symbols elements.json`. The file alone does not say what the screen holds. The rule names two repairs, to remove the element or to declare the intent it serves. Here is the second.

::: plate The ticker, given an intent
```zayn help.zayn level=3 symbols=elements.json
DEFINE SCREEN help_home (
  SATISFIES [DISCOVER, READ]
)

DEFINE COMPONENT answer_card (
  SATISFIES [READ]
)

DEFINE COMPONENT news_ticker (
  SATISFIES [SCAN]
)
//--> clean
```
In words: The same screen, and the ticker is something a user scans.
:::

Clean. The verifier read that an intent is declared, and a person judges whether that intent fits: a ticker of news, for a customer who came for help.

The verifier often reads one clause of a rule and leaves the others to the audit and to a person. Here is a message that a support agent, a person at the help desk, deletes.

::: plate A deletion with no way back
```zayn messages.zayn
DEFINE INTENT_FLOW delete_message (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT]
)
//--> MISSING_UNDO delete_message
```
In words: A user confirms, and a message is deleted. Cancel and exit stay within reach.
:::

Refused under Rule 79, which the law files under `machine`. The clause the verifier read is in the rule's list of what to avoid: "No way to reverse common destructive actions". The repair keeps undo within reach.

::: plate A deletion that can be undone
```zayn messages.zayn
DEFINE INTENT_FLOW delete_message (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT]
)
//--> clean
```
In words: The same deletion, and undo stays within reach.
:::

Clean, and it still declares `CONFIRM` on a common deletion. The first thing Rule 79 lists to avoid is "Confirmation dialogs for every deletion". Here is the same act written as one control, an `INTERACTION`, that confirms and can be undone: its `ROLE`, `reversible`, is its promise that the act can be taken back.

::: plate A control that confirms what it can undo
```zayn messages.zayn
DEFINE INTERACTION delete_message (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)
//--> clean
```
In words: A control deletes a message after the user confirms. The act can be undone, and the control says so.
:::

Clean. Is the confirmation a dialog that interrupts, or a step of review? A design note of the project gives the reason a declaration leaves it open: "Rule 79's dialog clause is a fact about a rendering, not about a declaration". On the painted page, a person judges that clause.

**The audit measures.** The audit of the painted page is a page of Zayn's repository that opens another page in the browser and measures what is drawn: sizes, contrast, the menu, the trail of links that shows where a page sits, the room before a scrollbar. Its title names the rules it measures against: "Rules 105, 107, 108 and 114–116". Its larger mode runs numbered checks, and one of them, K22, reads whether something on the page moves while the page loads: that is Rule 38, Zero Displacement. The contract, the file that binds each kind of finding to the law, has a kind of finding for it too, `LAYOUT_DISPLACEMENT`, which the verifier never raises; the audit's check for it is K22 LAYOUT_STILL, and the contract's note sends the reader there: "Measured today by tools/ui-audit.html, which is the enforcement ladder working as designed." So Rule 38, filed under `machine`, is answered by the audit.

The audit runs in a browser, and this page gives it from its recorded runs. The record of the second milestone of Zayn's design system gives two full runs of the larger mode on the Zayn site's own pages, before and after a change of the stylesheet, the file that sets how the pages look: "38 pages, five widths, both cultures: 380 renders each". The widths run from 375 to 1900 pixels, the cultures are Modern and Retro, and the runs were made on 10 November 2026, before the version this book reads. A culture is a way of drawing the same interface; chapters 14 and 15 are about cultures. K22 counted zero findings on both runs.

A second audit reads a screenshot, once a separate program has reduced the picture to facts: the lines of text, their size, their contrast. Its checker gives three answers per line, "fail, pass, not_decided", and for the size of text it never answers pass, because a size read from a picture is only an upper bound: "A size is never `pass`." The checker runs on an example made by hand, and the site files the whole audit as designed.

**A person judges.** Here is the help desk's assistant, an AI agent that answers the customer.

::: plate An assistant with an exit
```zayn assistant.zayn
DEFINE INTENT_FLOW ask_assistant (
  SATISFIES [DISCOVER, UNDERSTAND, READ],
  ALWAYS_REACHABLE [EXIT]
)
//--> clean
```
In words: A customer discovers, understands and reads what the assistant answers, and can leave at any moment.
:::

Clean. Can the customer reach a person? The law has a right for that.

{{right:human}}

One rule enforces it, Rule 102, and the law files it under `judgment`. Try to declare the path to a person, first as a verb.

::: plate A person, written as a verb
```zayn assistant.zayn
DEFINE INTENT_FLOW ask_assistant (
  SATISFIES [DISCOVER, UNDERSTAND, READ],
  ALWAYS_REACHABLE [EXIT, HUMAN]
)
//--> UNKNOWN_INTENT ask_assistant
```
In words: The same assistant, and the customer can also reach a human at any moment.
:::

Refused: the law's verbs say what a user does, and reaching a person is none of them. Then as a field, a named line of the declaration.

::: plate A person, written as a field
```zayn assistant.zayn
DEFINE INTENT_FLOW ask_assistant (
  SATISFIES [DISCOVER, UNDERSTAND, READ],
  ALWAYS_REACHABLE [EXIT],
  HUMAN_PATH support_agent
)
//--> UNKNOWN_FIELD HUMAN_PATH
```
In words: The same assistant, and a field names the support agent as the human path.
:::

Refused again: the grammar, the set of rules that says what a declaration may be made of, has no field for it. The rule's first line of what to avoid says what a person looks for: "Support mazes that end at a bot". The closed vocabulary that lets the verifier decide the rules it cites has no word for this one, so Rule 102 stays with a person.

## One finding, two tiers

A tier belongs to a rule, and a finding can cite several rules. Here the help desk's assistant proposes a refund and carries it out.

::: plate A proposal that acts alone
```zayn refund.zayn
DEFINE INTERACTION suggest_refund (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal
)
//--> PROPOSAL_COMMITS suggest_refund
```
In words: The assistant proposes a refund, and the refund is made. Undo and cancel stay within reach.
:::

Refused, and the third line cites two rules: Rule 98, Proposals, Not Commits, which the law files under `judgment`, and Rule 83, filed under `machine`. One verifier, one finding, two tiers. The repair names who accepts the proposal.

::: plate The proposal, accepted by a support agent
```zayn refund.zayn
DEFINE INTERACTION suggest_refund (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal,
  ACTOR support_agent
)
//--> clean
```
In words: The assistant proposes a refund, and a support agent makes it.
:::

Clean. Now name the assistant itself as the one who accepts.

::: plate The proposal, accepted by the one who made it
```zayn refund.zayn
DEFINE INTERACTION suggest_refund (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal,
  ACTOR assistant
)
//--> clean
```
In words: The assistant proposes a refund, and the assistant makes it.
:::

Clean as well. The verifier reads that an authority is named. Rule 98 opens on a sentence that a person reads: "Intelligence advises; execution decides." An assistant that accepts its own proposal advises and decides at once, and a person sees it.

## Where the citations fall

Here is the count, with its definition. A rule is counted for the verifier when a kind of finding that the verifier raises cites it in the contract. A rule is counted for an audit when the audit's title, the table of checks of its larger mode, or the screenshot checker's file of decisions names it. A rule that one finding mentions in passing is not counted: a finding of the trail check names Rules 60 and 104 beside Rule 108. A citation shows that an instrument reads the rule, and the plates above showed both a clause the verifier reads and a clause left to a person.

{{ladder}}

By that definition, the verifier's kinds of finding cite {{n:cite.verifier}} rules, the audits name {{n:cite.audit}}, and Rule 116 is named by both: {{n:cite.union}} rules in all. The audit of the painted page names {{n:cite.ui}} of them and the screenshot's checker {{n:cite.shot}}, Rules 105 and 107 by both. Read the tier column beside the two others. Most of the rules filed under `judgment` that the verifier cites have a clause that a declaration can state; Rule 16 is reached through the forbidden pattern that names it. Every rule filed under `machine`, and most filed under `tool`, name in their `lint` entry the instrument they are owed: for some a check of this repository, like Rule 130's; for others a lint of HTML, which the record leaves to the projects that use the law. A person can judge every rule, with its number and its words in hand, and in this repository the other {{n:cite.rest}} rules are answered by a person.

## What I refused

**I refused a tier that no instrument could serve.** In my pass of 13 August 2026 a draft proposed to file Rule 62, on contrast, under `machine`. A declaration states no colours, so the verifier could never read it. I adopted the move to `tool`, an instrument that measures, and the docket keeps the reason: the draft "would have placed a rule in a tier no instrument could serve". Rule 38, on displacement, is filed under `machine` and answered by the audit: the filing and the instruments follow each other in part, and whether they should agree is a question filed for the law.

**I deferred a requirement until it has evidence.** A design note asked whether the law should require a role on every declaration that acts. On 19 August 2026 I ruled that requiring a role is, in the note's words, "deferred to evidence". A warning, `ROLE_UNDECLARED`, took its place: when no interaction of a file states a role, it tells whoever writes the declaration, and it refuses nothing. A run that holds only that warning ends with exit code 0.

**The record refuses a count typed by hand.** The ledger, the dated list of what the project found, has a line for counts like the ones on this page: "Counts and tier tables belong in code that reads `rules.json`". Every count of this chapter is computed at each build: from the law, the contract and the verifier's code, and for the audits from a list of citations that the build checks against each file.

[AUTHOR: the stake of this chapter, in your words: why a law should say of each rule what answers for it, and what you want a team to do with the rules that a person holds.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below hold the verifier's side of this chapter: Rule 130 against an inventory, Rule 79's undo, Rules 98 and 83 in one finding, Rule 26 and Rule 118, filed under `machine-later` and `judgment`, and one file that cites rules of two tiers in one report. The audit's side stands on its recorded runs, and the suite gives its reason for keeping no fixture for `LAYOUT_DISPLACEMENT`: "A fixture here would be theatre". A fact about the painted page is proved on the painted page.

## Where the field leads

The field leads on its tools' account of themselves. An engine that tests a page in a browser publishes the share of issues it finds, and returns what it cannot decide as incomplete, for a person. The screenshot's checker in Zayn also gives an answer for what it cannot decide, and keeps a pass on size out of its own reach.

The field leads on severity. A linter's user sets each rule to warn or to error. In Zayn the contract fixes the severity of each kind of finding, the same for every team: a team gains one meaning of a refusal, and gives up a setting.

Zayn's law leads on saying, for every rule, which instrument it is owed, and on citing the rule by number in every finding of the verifier that binds a rule, and in most of the audit's. The ledger records where the verifier's reach ends, in a test of 12 August 2026: two payment surfaces "differing by seven broken laws" were the same declaration, byte for byte, and both ran clean. Its own words: "the court is silent exactly where the deterioration lives". The project answers with the audit of the painted page, and designs one more instrument: an audit that refuses at the moment of painting.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Every rule of the law is filed under one of {{n:law.tiers}} words, and the file says which. By citation, the verifier's kinds of finding cite {{n:cite.verifier}} rules, each kind with a fixture, and this page ran those it shows. The audit of the painted page names {{n:cite.ui}} rules, and its runs are told here as recorded, with their date, widths and cultures. The checker of a screenshot's facts names {{n:cite.shot}} and runs on its example; the audit of a screenshot as a whole, from the picture to the verdict, is designed. For Rules 130, 79 and 98 this chapter named the clause the verifier reads. A person can judge every rule, and holds alone the rules whose subject no declaration and no measure states, such as Rule 102, which enforces the right to a human.

## In your hands

Here is the help desk's refund, as first written. A `FEEDBACK` is a message of the system; it names in `REPORTS` the state it reports. Write the codes you expect, then open the verifier's answer.

::: plate For you: a refund, granted on a click
```zayn grant.zayn
DEFINE INTERACTION grant_refund (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE proposal
)

DEFINE FEEDBACK refund_sparkle (
  TONE celebratory
)
//--> SELECT_ACT_COLLAPSE grant_refund
//--> MISSING_UNDO grant_refund
//--> PROPOSAL_COMMITS grant_refund
//--> DECORATIVE_ANIMATION refund_sparkle
```
In words: The assistant proposes a refund; choosing it grants it, with cancel within reach. Then the system answers in a celebrating tone.
:::

Four findings, five rules. Open each rule's card in Appendix A, read its tier, and say which instrument has just answered for it. Then repair the selection and the undo, and say what you expect. Try before you read on.

::: plate The selection confirmed, the undo within reach
```zayn grant.zayn
DEFINE INTERACTION grant_refund (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal
)

DEFINE FEEDBACK refund_sparkle (
  TONE celebratory
)
//--> PROPOSAL_COMMITS grant_refund
//--> DECORATIVE_ANIMATION refund_sparkle
```
In words: The assistant proposes a refund; a user selects it and confirms, and it is granted, with undo and cancel within reach.
:::

Two remain. Go on until the verifier answers clean and every line of your file is true. Try before you read on.

::: plate A refund that a person grants, and a message that reports
```zayn grant.zayn
DEFINE INTERACTION grant_refund (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal,
  ACTOR support_agent
)

DEFINE FEEDBACK refund_granted (
  TONE celebratory,
  REPORTS [refund_status]
)
//--> clean
```
In words: The assistant proposes a refund, and a support agent grants it after selecting and confirming. The message that follows reports the refund's status.
:::

Clean. Which rules of the law has the report read, and which wait for the audit and for a person? The tone is one case: whether a celebration fits a refund is a person's call. And should a rule's card say what answers for it today? That question is filed for the law.

A rule climbs the ladder by a promotion, a change of the law like an amendment. The next chapter tells how the law changes.
