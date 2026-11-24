---
id: the-ai-agent-as-a-user
part: 9
number: 23
title: The AI agent as a user
stage:
  built: "the machine medium, as a row of the media's data and in the verifier's table; the checks this page runs on it; the machine form of a report, the refusal a program reads; the actor model given at level 3, where an AI agent is named as any actor is"
  designed: "the machine medium in the project's proposal for a second founding of the law; the interface through which a person meets an AI agent, in the project's architecture"
  next: "rules for the surfaces where a person approves an AI agent's tool or gives consent; the law served to AI tools while they work"
status: draft
research: research/ch23.md
fixtures: [missing-undo, missing-undo-lawful, projection-machine-cancel, projection-machine-cancel-lawful, hidden-authority, projection-visual-trust, invisible-state, signal-unperceivable, signal-unperceivable-lawful, verb-not-carried, verb-not-carried-lawful]
---

An AI agent as a user is a program, driven by an AI model, that operates an interface to reach a goal: it reads what the interface shows and acts through it. In this chapter I put the AI agent at the end of the interface where a person usually stands. I run one declaration on a screen and on the machine medium, the medium a program consumes, and show the same refusal. I show where Zayn's language names the one who acts, and what the law asks of an interface an AI agent operates. Then I show what the medium changes, read from the data, and what stays a person's judgment.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines that say what a user is doing on a surface, a screen or any other place where a user meets the system. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. Its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field's AI agents meet an interface in three ways. The first reads its pixels. Anthropic's guide to its computer use tool says the tool "provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction". OpenAI's page on its Computer-Using Agent says that screenshots are added to the AI model's context, the input it works from, and that the agent "uses a virtual mouse and keyboard to complete actions".

The second reads the interface's structure. Playwright MCP, a server that lets an AI model drive a browser, says it works "through structured accessibility snapshots, bypassing the need for screenshots". It "Uses Playwright's accessibility tree, not pixel-based input", Playwright being the program that drives the browser. The accessibility tree is W3C's term: WAI-ARIA, the web's standard for accessible controls, defines it as a "Tree of accessible objects that represents the structure of the user interface (UI)". A screen reader, the software that reads an interface aloud to a person who cannot see it, works from that structure, which the browser hands to the operating system: "Assistive technologies use the enhanced information available in an accessibility API."

The third calls the interface's own operations. The Model Context Protocol, the protocol whose letters Playwright MCP carries, connects AI models to tools and data. It gives each tool a name, a description and a schema of its input, a description of the fields the input must have. It also says: "there SHOULD always be a human in the loop with the ability to deny tool invocations".

And the field asks a person to confirm the act that counts. The computer use guide advises "Asking a human to confirm decisions that might result in meaningful real-world consequences". The Computer-Using Agent "seeks user confirmation for sensitive actions, such as entering login details or responding to CAPTCHA forms". Each source was read on 24 November 2026, and Appendix F lists them. So the field's AI agents operate an interface that exists, by its pixels, its structure or its tools, and the field asks a person to confirm the act.

## The principle

**A declaration of an interface that an AI agent operates is checked against the same rules as one a person operates; the medium it names changes what can be carried and what can be shown.**

The law gives the reason in Rule 104: "What a screen reader can operate, an agent can operate and a non-visual medium can render; legibility is one law with three beneficiaries." Rule 104 holds that an interface whose structure is declared serves a person who cannot see it, an AI agent, and a medium with no screen, from the same declaration. The Zayn site draws the consequence: "An interface for an agent is an interface: the agent is the user at the other end". So this chapter puts the AI agent where the user stands, and runs it there.

## One law, three beneficiaries

The law defines its user once, in its preamble, the opening text that says how the rules are read: "the operator and the user name whoever acts through an interface: the user, a person or an agent (Rule 104)". The operator is the law's own word for the user. The same sentence keeps one place for people alone: "where a rule names what is seen, heard, read or felt, it protects the person." Here is the rule it cites.

{{rule:104}}

The law files Rule 104 under `machine-later`, its word for a rule that a program is to check, with that check to come. A medium is a way the interface meets its user. The data that describes them names {{n:media.total}}: `visual`, `auditory`, `voice`, `haptic`, `print`, `luminous`, `signage`, `machine`, `spatial` and `terminal`. The data's row for the medium `machine` is titled "Consumed by a program", and its note calls it "Rule 104's third beneficiary", the medium with no screen that the rule names. On the grid of chapter 13, where the project places each rule on the activities and media it speaks of, Rule 104 is the rule placed on the machine medium. The next section runs a declaration on it.

## The same refusal, two media

A declaration names its medium in `SURFACE_AS`, a field of a `VIBE`, the kind of declaration that states how a surface behaves as a whole: its medium, its density, its motion. Here is a payables desk. On a portal, a clerk schedules a supplier's payment.

::: plate A payment scheduled on a screen
```zayn portal.zayn
DEFINE VIBE payments_portal (
  SURFACE_AS visual
)

DEFINE INTENT_FLOW schedule_payment (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR payables_clerk
)
//--> MISSING_UNDO schedule_payment
```
In words: On the payments portal, a clerk confirms a payment and schedules it. Cancel and exit stay within reach.
:::

Refused under Rule 79: the payment is scheduled, and the declaration keeps no way back. Now the same act through an interface for programs, where an AI agent of the payables desk schedules the payment.

::: plate The same payment, by an AI agent
```zayn payments.zayn envelope
DEFINE VIBE payments_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW schedule_payment (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR payables_agent
)
//--> MISSING_UNDO schedule_payment
```
In words: Through the payments interface for programs, an AI agent confirms a payment and schedules it. Cancel and exit stay within reach.
:::

The same finding, the same rule, the same right: the right to take an act back. The second report is printed twice: once as a person reads it, and once in the machine form, the report's form for a program, on any medium, with each finding's code, its line, and what it cites. This is the form a program reads before the interface exists, an AI model that writes declarations among them. The rule is cited by number, `rule:79`, and the right by its name, `right:reverse`. An AI model that wrote this declaration can read which rule it broke and repair it. The repair is the same on both media: undo within reach.

## Where the user is named

The language leaves who the user is to another place. Here is a declaration that tries to state it.

::: plate A user, declared
```zayn users.zayn
DEFINE USER payables_agent (
  SATISFIES [SCAN, COMPARE]
)
//--> UNSPECIFIED_DECLARATION payables_agent
```
In words: A user of the payables desk, an AI agent, who scans and compares.
:::

A warning, and no refusal: `USER` is not one of the language's {{n:lang.kinds}} kinds of declaration. The parenthesis of the report names the two kinds the language keeps out, `WIDGET` and `USER`. The language's specification says why: it is "a fact about *who*, which Zayn consumes from a symbol table rather than declares". The symbol table is a file given to the verifier beside the declaration, at level 3, that lists what the system holds. When it lists actors, the verifier asks every declaration whose `SATISFIES` holds `ACT` to name an actor; it reads that a name is there, and does not look the name up in the list. On the command line it is named after the file: `zayn check payments.zayn --level 3 --symbols desk.json`. A level is how much the verifier is given. The contract files each kind of finding at one of four levels: level 1 checks that the file is well formed and uses the language's own words, level 2 decides what a single declaration states, level 3 adds a table of what the system holds, and level 4 is the painted page, the page as a browser draws it. A run at a level reports the findings of the levels below it too. A declaration names the one who acts in a field, `ACTOR`, and a person and an AI agent are named the same way. Here is the payment again, at level 3, with the table.

::: plate A payment that names no actor
```symbols desk.json
{
  "actors": ["payables_clerk", "payables_agent"]
}
```
```zayn payments.zayn level=3 symbols=desk.json
DEFINE VIBE payments_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW schedule_payment (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT]
)
//--> HIDDEN_AUTHORITY schedule_payment
```
In words: Through the interface for programs, a payment is confirmed and scheduled, with undo, cancel and exit within reach, and the declaration says nothing of who schedules it.
:::

Refused under Rule 83 and Article V, the law's article on authority: an act that matters names its actor. The verifier needed the table to raise it. Here is the same file at level 2, without the table.

::: plate The same payment, at level 2
```zayn payments.zayn
DEFINE VIBE payments_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW schedule_payment (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT]
)
//--> clean
```
In words: The same payment, checked with the file alone.
:::

The report prints clean: without the table, the check is silent, undecided. The repair names the AI agent.

::: plate The AI agent, named
```zayn payments.zayn level=3 symbols=desk.json
DEFINE VIBE payments_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW schedule_payment (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR payables_agent
)
//--> clean
```
In words: The same payment, and the declaration names the AI agent that schedules it.
:::

Clean. Whether an AI agent should schedule a payment, or only propose one for the clerk to accept, is the subject of chapter 22. The verifier reads that a name is there; a person judges whether it is the right one.

## What the medium changes

A medium changes two things the verifier reads: which verbs it carries, and which statuses it can show. A verb is one of the law's words for what a user does. A status is one of the words a declaration gives in `SIGNALS` for what a value says about its record: success, warning, danger, info and muted. Here is a statement review on a voice line, where a user hears a statement and speaks to it. Before you read the answer, say which verb a voice line cannot carry.

::: plate A statement review, by voice
```zayn statement.zayn
DEFINE VIBE statement_line (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW review_statement (
  SATISFIES [READ, COMPARE, ZOOM],
  SIGNALS [muted]
)
//--> VERB_NOT_CARRIED review_statement
//--> SIGNAL_UNPERCEIVABLE review_statement
```
In words: On a voice line, a user hears a statement, compares its lines and zooms into a month. The statement's one status is muted.
:::

Two refusals. A voice line cannot zoom, and a muted status, on voice, is rendered as nothing at all. The third line of each finding lists what the contract binds to that kind of finding: its rule, an article and a right. So Rule 82 stands under Article II in one finding and Article III in the other, the articles of the two kinds; Rule 82's own article is Article III. The contract calls a verb an intent. The second fires when every status the surface declares is rendered as nothing on its medium. Now the same review through an interface for programs.

::: plate The same review, read by a program
```zayn statement.zayn
DEFINE VIBE statement_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW review_statement (
  SATISFIES [READ, COMPARE, ZOOM],
  SIGNALS [muted]
)
//--> clean
```
In words: Through an interface for programs, a user reads the same statement, compares its lines and zooms into a month. Its one status is muted.
:::

Clean, and the clean holds two different answers. The data has the machine medium carry every verb, so `ZOOM` passes. The statuses are another matter. The data records how a status is rendered for {{n:media.rendered}} media, those with a renderer built, a program that draws a declaration on that medium: visual, auditory and voice. For a medium with no entry the data says: "A medium with no entry is UNDECIDED, not 'perceptible': only channels with a shipped renderer can say." So on the machine medium the verifier decides the verbs and leaves the statuses undecided, and the report prints clean for both. The report has one word for both; a reviewer tells them apart by the medium, whose rendering the data records or leaves open.

## What I refused

**I refused a law of legibility with two beneficiaries.** Rule 104 named two beneficiaries: a person who uses a screen reader, and an AI agent. The docket, the file where changes to the law are ruled, set the change apart for a deliberate ruling, as "the sentence the whole multi-modality argument rests on". In my pass of 13 August 2026 I adopted a third beneficiary as a correction: a medium with no screen.

**I refused a law whose user is a person alone.** On 7 November 2026 I answered "yes to all six" on six recommendations drawn from my remarks on the Zayn site, and one of the six made the law name whoever acts "the user, a person or an agent". It keeps one exception, in the ruling's words: "never where it names human perception". The docket gives the reason "operator" stayed: it "is the law's role word, not a description of a human".

**The record keeps the user out of the language.** The language states what a user does; the list of who may act belongs to the system around it.

**The record refuses to call a status perceptible where no renderer can say.** The machine medium's statuses stay undecided until a renderer for it is recorded.

[AUTHOR: the stake of this chapter, in your words: why an interface an AI agent operates is owed what a person is owed, and where you hold that the person stays apart.]

## The court

The court of this chapter is eleven fixtures of the suite, each a declaration kept with the answer it must get, most in pairs with a twin, the same file made lawful. It holds Rule 79's undo and its twin. It holds Rule 26's cancel under `SURFACE_AS machine`, the suite's own pair on this medium, which chapter 12 showed. It holds the authority check at level 3, once on a file with no medium named and once on a screen, the fixture whose comment says that nothing about the medium "should change the verdict". It holds the state check at level 3. And it holds the two checks a medium changes, verbs and statuses, each with its twin. The comment of the suite's machine pair says what it leaves to a person: whether the way back "means the same thing to an API client as to a person is a judgement no verifier makes", an API client being a program that uses an interface for programs.

## Where the field leads

The field leads on the interface that exists. Its AI agents operate a screen or a page that exists, by its pixels or its accessibility tree, and a protocol's tools with their schemas. Zayn's machine medium is a row that the data calls "derived by reasoning about each medium's properties", and the verifier reads a declaration before any surface exists.

The field leads on the person at the act. Its guides and its protocol ask a person to confirm a consequential act and to be able to deny a tool. Zayn's law holds a neighbouring line in Rule 98, which makes an AI model's output a proposal that a named authority accepts, and in the right to a human, which keeps a person reachable. The rules for the surfaces where a person approves a tool or gives consent are on its roadmap.

Zayn leads before the interface exists. An AI agent that reads pixels works from what the screen shows; one that reads the accessibility tree gets the roles a page exposes. A declaration states the verbs, the way back and the actor before the interface is drawn, and the checks this page ran refuse on the machine medium what they refuse on a screen, with the rule cited in a form a program reads.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The machine medium is built as a row of the media's data and in the verifier's table, and it carries every verb. On it, the checks this page ran refuse what they refuse on a screen: Rule 79's undo, Rule 83's actor and the verb check there, and the suite runs Rule 26's cancel there. The machine form of the report is built, with each finding's code and citations. Who acts is named in `ACTOR`, a person or an AI agent alike, and given at level 3 in the table of actors. The statuses of the machine medium are undecided, and the data names the media whose rendering is recorded. The machine medium in a proposal of the project for a new base of the law, its second founding, which awaits my ruling, and the interface through which a person meets an AI agent, in the project's architecture, are designed. Next are the rules for approval and consent surfaces, and the law served to AI tools through the Model Context Protocol while they work. Whether an interface serves its AI agent well, and what a way back means to a program, is a person's judgment.

## In your hands

Here is an AI agent of a shop's sales desk. Through an interface for programs it lists the orders that are late, filters them by date and scans the list, to chase each customer. The system also holds a limit on how many results the list returns. Run it at level 3 with the table, write the codes you expect, then open the verifier's answer.

::: plate For you: late orders, by an AI agent
```symbols orders.json
{
  "state": ["date_filter", "result_limit"]
}
```
```zayn late.zayn level=3 symbols=orders.json
DEFINE VIBE orders_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW list_late_orders (
  SATISFIES [DISCOVER, FILTER, SCAN],
  ALWAYS_REACHABLE [EXIT],
  VISIBLE_STATE [date_filter]
)
//--> INVISIBLE_STATE result_limit
```
In words: Through an interface for programs, an AI agent discovers the late orders, filters them by date and scans the list. The interface shows the date filter it applied.
:::

Repair it, and say what you expect. Try before you read on.

::: plate The late orders, with the limit shown
```zayn late.zayn level=3 symbols=orders.json
DEFINE VIBE orders_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW list_late_orders (
  SATISFIES [DISCOVER, FILTER, SCAN],
  ALWAYS_REACHABLE [EXIT],
  VISIBLE_STATE [date_filter, result_limit]
)
//--> clean
```
In words: The same list, and the interface shows both the date filter and the limit on the results.
:::

Clean. The system held a limit, and the first interface did not show it: the AI agent chased the customers of a list it could not tell was cut short. Rule 82's reason, under the right to know, says what that costs: "A user who reasons from state they cannot perceive has been harmed by the interface." Now read the preamble's exception again: "where a rule names what is seen, heard, read or felt, it protects the person." Rule 82 asks that the user can perceive the state, and the verifier refused the AI agent's list all the same. Does the right to know protect an AI agent, or only the person it works for? The question is yours too, and it is among this book's requests to the Zayn project, as a question for the law.

An AI agent that operates an interface may also write one. The next chapter reads the grammar that would hold an AI model to a declaration's shape while it writes.
