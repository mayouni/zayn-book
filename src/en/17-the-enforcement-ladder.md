---
id: the-enforcement-ladder
part: 7
number: 17
title: The enforcement ladder
stage:
  built: "a tier on each of the {{n:law.rules}} rules, in the law's own words; the verifier, whose kinds of finding cite {{n:cite.verifier}} rules, each kind with its fixture; the audit of the painted page, which names {{n:cite.ui}} rules for its checks and whose runs are recorded; the checker of a screenshot's facts, run on its example"
  designed: "the audit of a screenshot as a whole, from the picture to the verdict; an audit that refuses at the moment of painting"
  next: "rules moved up the ladder as their instruments are built"
status: draft
research: research/ch17.md
fixtures: [intent-orphan, missing-undo, missing-undo-lawful, irreversible-claims-undo, irreversible-claims-undo-lawful, proposal-commits, proposal-commits-lawful, missing-cancel, missing-cancel-lawful, multiple-violations, unknown-signal, unknown-signal-lawful]
---

The enforcement ladder is the law's word for how its rules are held: each rule is filed under one word that names the instrument it is owed. In this chapter I read those words. Then I set beside them what answers today: the verifier, which refuses a declaration; the audits, which measure a page; and a person, who judges. I show each at work on one surface, a help desk where an AI agent answers a customer, and I count which rules each instrument names, with the definition of the count printed beside every number.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field knows that its instruments reach part of a rule. The accessibility guidelines write their criteria "as testable criteria for objectively determining if content satisfies them", and their page on conformance adds that testing "would involve a combination of automated testing and human evaluation". W3C's page on evaluation says it plainly: "no tool alone can determine if a site meets accessibility standards".

The tools say the same of themselves. axe-core, an engine that tests a page in a browser, says that with it "you can find on average 57% of WCAG issues automatically", a figure of its own, and that it returns an element as "incomplete" where "manual review is needed". A linter for the markup of one framework says that it "only catches errors in static code", and sends its reader to a second tool for the page as rendered.

And the field gives a rule a force. ESLint, a linter for code, lets its user set a rule to "warn", which "doesn't affect exit code", or to "error", whose "exit code is 1 when triggered": a build that stops.

So the field has instruments at two moments, before rendering and after, a force set per rule, and a person beside them. Each source was read on 21 or 23 November 2026, and Appendix F lists them.

## The principle

**A tier names the instrument a rule is owed; a citation shows the instrument that answers today.**

The law's site calls it a ladder: "Each rule declares one rung of an enforcement ladder, and rules climb as instruments are invented." A rung is a tier, and a climb is an amendment, which chapter 18 tells. The docket, the file where changes to the law are ruled, says what a tier claims, in a sentence on one rule: it "is honest about which instrument owes the check; it is not a claim that the check runs today".

## Four words, as the law files them

Every rule has a field named `enforcement`, and its value is one of {{n:law.tiers}} words. Here they are, with the rules filed under each, and beside them the count by citation that the rest of this chapter explains.

{{tiers}}

Read the first two columns as the law's filing, and nothing more. The founding document of the project gives the meaning of the largest rung in its own table: `judgment`, "a human decides, until an instrument is invented". The other columns come from the instruments.

## Three instruments

The architecture of the law puts its instruments at two moments: "The constitution is enforced twice, at two different moments." Before rendering, the verifier reads a declaration and refuses it. After rendering, an audit measures the painted page, the interface as a browser draws it. And at every moment a person can read a rule, judge a surface against it, and cite its number.

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

Refused, under Rule 130, which the law files under `machine`. The verifier needed the inventory: from the file alone it cannot know what the screen holds. The rule names two repairs, to remove the element or to declare the intent it serves. Here is the second.

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

Clean. The verifier read that an intent is declared. Whether a ticker of news serves a customer who came for help is a person's to judge: one rule, and two instruments for its two halves.

**One clause of a rule.** The verifier often reads one clause of a rule and leaves the others to the other instruments. Here is a message that a support agent deletes.

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

Clean, and it still holds `CONFIRM` on a common deletion. The first thing Rule 79 lists to avoid is "Confirmation dialogs for every deletion". Here is the same act as a control that confirms and can be undone.

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

Clean. Is the confirmation a dialog that interrupts, or a step of review? A declaration does not say, and a design note of the project gives the reason: "Rule 79's dialog clause is a fact about a rendering, not about a declaration". That clause goes to the painted page, and to a person.

**The audit measures.** The audit of the painted page is a page of Zayn's repository that opens another page in the browser and measures what is drawn: sizes, contrast, the menu, the trail, the room before a scrollbar. Its title names the rules it measures against: "Rules 105, 107, 108 and 114–116". Its larger mode runs numbered checks, and one of them, K22, reads whether something on the page moves because something else appeared: that is Rule 38, Zero Displacement. The contract, the file that binds each kind of finding to the law, has a kind for it, `LAYOUT_DISPLACEMENT`, and says where its answer comes from: "Measured today by tools/ui-audit.html, which is the enforcement ladder working as designed."

This page cannot run a browser on another page, so the audit is told from its recorded runs. The project's record of its second milestone gives two full runs, before and after a change of the stylesheet: "38 pages, five widths, both cultures: 380 renders each", read on 10 November 2026. A culture, or vibe, is a way of drawing the same interface, and chapter 15 is about them. On both runs, K22 found nothing to report.

A second audit reads a screenshot, once a writer has reduced the picture to facts: the lines of text, their size, their contrast. Its checker gives three answers per line, "fail, pass, not_decided", and it keeps one of them out of reach for size: "A size is never `pass`." It runs on an example made by hand, and the site files it as designed. Together the two audits name {{n:cite.audit}} rules for a check.

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

Refused: the law's verbs say what a user does, and reaching a person is none of them. Then as a field.

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

Refused again: the grammar has no field for it. The closed vocabulary that lets a machine decide the other rules has no word for this one, so a person holds it. The rule's first line of what to avoid says what that person looks for: "Support mazes that end at a bot".

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

::: plate The proposal, accepted by an agent
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

::: plate The proposal, accepted by its author
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

Clean as well. The verifier reads that an authority is named. Whether that authority may accept its own proposal is the clause of Rule 98 that a person reads.

## Where the citations fall

Here is the count, with its definition. A rule is counted for the verifier when a kind of finding that the verifier raises cites it in the contract. A rule is counted for an audit when a file of that audit names it for a check. A citation shows that an instrument reads the rule. It does not say that the instrument reads every clause, and the plates above showed clauses on both sides.

{{ladder}}

By that definition, the verifier's kinds of finding cite {{n:cite.verifier}} rules, the audits name {{n:cite.audit}}, and {{n:cite.both}} rule, Rule 116, is named by both: {{n:cite.union}} rules in all. The audit of the painted page names {{n:cite.ui}} of them and the screenshot's checker {{n:cite.shot}}. Read the tier column beside the two others. The rules filed under `judgment` that the verifier cites are rules whose one clause a declaration can state. Every rule filed under `machine`, and most filed under `tool`, names in a field of its own, `lint`, the instrument it is owed. A person judges every rule, with its number and its words in hand.

## What I refused

**I refused a tier that no instrument could serve.** In my pass of 13 August 2026 a draft proposed to file Rule 62, on contrast, under `machine`. A declaration holds no colours, so the verifier could never read it. I adopted the move to `tool`, and the docket keeps the reason: the draft "would have placed a rule in a tier no instrument could serve".

**I deferred a requirement until it has evidence.** A design note proposed to require a role on every control that acts. On 19 August 2026 I ruled that requiring a role is, in the note's words, "deferred to evidence", and a warning took its place: it tells the author of a declaration that a role is missing, and refuses nothing.

**The record refuses a census typed by hand.** The ledger, the dated list of what the project found, has the rule for counts like the ones on this page: "Counts and tier tables belong in code that reads `rules.json`". Every count of this chapter is read from the files at each build.

[AUTHOR: the stake of this chapter, in your words: why a law should say of each rule what answers for it, and what you want a team to do with the rules that a person holds.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below hold the verifier's side of this chapter: Rule 130 against an inventory, Rule 79's undo, Rules 98 and 83 in one finding, Rule 26 and Rule 118, filed under `machine-later` and `judgment`, and one file that cites rules of two tiers in one report. The audit's side has no fixture, and the suite gives its reason for `LAYOUT_DISPLACEMENT`: "A fixture here would be theatre".

## Where the field leads

The field leads on its tools' account of themselves. An engine that tests a page in a browser publishes the share of issues it finds, and returns what it cannot decide as incomplete, for a person. The audits of Zayn give the same three answers, and the screenshot's checker keeps one of them, a pass on size, out of its own reach.

The field leads on force. A linter's user sets each rule to warn or to error. In Zayn the contract fixes the severity of each kind of finding, the same for every team: a team gains one meaning of a refusal, and gives up a setting.

Zayn's law leads on saying, for every rule, which instrument it is owed, and on citing the rule by number wherever an instrument answers. The ledger records where the verifier's reach ends, in a test of August 2026: two payment surfaces that differed by seven broken laws were written as the same declaration, and both ran clean. Its own words: "the court is silent exactly where the deterioration lives". That is why the record answers with a second instrument on the painted page, and designs a third, an audit that refuses at the moment of painting.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Every rule of the law is filed under one of {{n:law.tiers}} words, and the file says which. By citation, the verifier's kinds of finding cite {{n:cite.verifier}} rules, each kind with a fixture, and this page ran those it shows. The audit of the painted page names {{n:cite.ui}} rules for its checks, and its runs are told here as recorded, with their date, widths and cultures. The checker of a screenshot's facts names {{n:cite.shot}} and runs on its example; the audit of a screenshot as a whole, from the picture to the verdict, is designed. Each instrument reads the clauses it can read, and this chapter names the clause for each rule it shows. A person judges every rule, and holds alone the rules whose subject no declaration and no measure states, such as the right to a human.

## In your hands

Here is the help desk's refund, as first written. Before you read the report, write the codes you expect.

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

Four findings, five rules. Open each rule's card in Appendix A, read its tier, and say which instrument has just answered for it. Then repair the selection and the undo, and say what you expect.

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

Clean. Which rules of the law has the report read, and which wait for the audit and for a person? The tone is one of them: whether a celebration fits a refund is a person's call. And should a rule's card say what answers for it today? That question is filed for the law.

A rule climbs the ladder by an amendment. The next chapter tells how the law changes.
