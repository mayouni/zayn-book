---
id: the-ai-agent-under-the-law
part: 9
number: 22
title: The AI agent under the law
stage:
  built: "Article V and Set 31 as data, each rule with its reason, its article and its tier word; the role `proposal` and the check that refuses a proposal that acts with no authority named, each with its fixture; the verifier, which judges a declaration by what it states, whoever wrote it and whoever acts; its machine form, which an AI model can read"
  designed: "the loop of the Zayn site in which an AI model declares, the verifier refuses by rule, and the model corrects: a procedure a person runs"
  next: "the law served to AI tools while they generate; rules for a conversation with an AI agent and for the surfaces of approval and consent"
status: draft
research: research/ch22.md
fixtures: [proposal-commits, proposal-commits-lawful, hidden-authority, projection-visual-trust, missing-undo, missing-undo-lawful, role-undeclared, role-undeclared-lawful, unknown-role, unknown-role-lawful]
---

An AI agent under the law is an AI agent that the law counts as an actor: named in a declaration as a person who acts is named, and held to the same rules. In this chapter I read the law's article on authority and its set of rules for AI agents, rule by rule, each with its reason. I run declarations that show the verifier judging what a declaration states, whoever wrote it and whoever acts. I show the set's one check, on a proposal, where its reach ends, and what a person reads in its place. And I say how an AI model works with the law today, while it writes.

If you open the book here, six words come first, and every other word is said where it first appears. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. Its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error. An **AI model** is a program that writes text, a declaration among others, from what it is asked. An **AI agent** is a program, driven by an AI model, that acts for a user.

## The field

The field, the practice and the texts outside Zayn, governs the AI agent from three sides. The first side is guidance for design. Microsoft's *Guidelines for Human-AI Interaction* number eighteen, G1 to G18, among them "G8: Support efficient dismissal.", "G9: Support efficient correction.", "G11: Make clear why the system did what it did." and "G16: Convey the consequences of user actions."

The second side is statute. The European Union's Artificial Intelligence Act, Regulation (EU) 2024/1689, asks that the people who talk with an AI system are "informed that they are interacting with an AI system" (Article 50(1)). It asks that what such systems generate is "marked in a machine-readable format and detectable as artificially generated or manipulated" (Article 50(2)). And for the systems it calls high-risk, it asks that a person can "disregard, override or reverse the output" (Article 14(4)(d)).

The third side is protocol, the rules by which programs talk while an AI agent works. The Model Context Protocol, MCP, connects an AI application, which it calls the host, to servers, programs that offer it data, prepared messages and tools, each tool "Functions for the AI model to execute". Its overview says that "Hosts must obtain explicit user consent before invoking any tool", that is, before calling it. A2UI, a format for interfaces that an AI agent composes, "Streams declarative JSON data with two-way bindings — never executable code": the AI agent sends a description of the interface as data, and the application draws it from parts it registered. "Agents place only components you registered."

Each source was read on 24 November 2026, and Appendix F lists them. So the field advises at design, binds by statute in use, and asks for consent while the AI agent works.

## The principle

**An AI agent acts under the same law as a person, and a declaration is judged by what it states, whoever wrote it.**

The law says it in its fifth article, the one on authority.

{{article:authority}}

An actor is whoever performs an act. An authority above the law would be an actor whose acts the law does not judge. The set of rules written for AI agents opens on the same line, "an AI is an actor under the constitution, never an authority above it", and closes on what it asks, in three parts: "Same norms, same audit, same dignity."

## Set 31, rule by rule

The law gathers its rules into sets, and Set 31, *Intelligence Under Law*, holds the rules written for AI agents. Rules 97 to 104 entered the law with its version 2.0, on 3 August 2026, and Rules 121 and 124 with version 3.7. Here they are, each with the reason it gives, the article it derives from, and its tier: the word under which the law files the rule, naming what is to check it. A proposal of the project for a new base of the law, its second founding, which awaits my ruling, glosses the two tiers of this set: `judgment`, "a human decides, until an instrument is invented", and `machine-later`, "the law's own admission that the instrument is missing". A tier names what a rule is owed; a check may read one clause of the rule before then, as `PROPOSAL_COMMITS` reads Rule 98's, and chapter 17 counts which. The last column gives the kinds of finding of the contract that cite the rule. The contract is the file that ties each kind of finding to the rules it cites, and a kind of finding is named by a code in capitals, such as `MISSING_UNDO`.

{{set:31}}

Read the reasons first: they are the law's own case for each rule. Each rule also gives a solution, which the table leaves out. Rule 97's makes the AI agent an actor, "named in the step, subject to the same validations, norms, signatures, and audit trail as any human". Rule 98's makes an AI model's output a proposal, which "becomes a commit only through an authority the declaration names". A commit is the act that changes what is true in the records. Rule 99's asks that what a machine wrote is marked as such, Rule 102's that a person is always reachable.

Then read the last column: what the verifier reads of the set is `PROPOSAL_COMMITS`, for Rule 98. Article V is cited as well by `HIDDEN_AUTHORITY`, for Rule 83: the check that, at level 3, asks every act to name its actor. A level is how much the verifier is given. The contract files each kind of finding at one of four levels: level 1 checks that the file is well formed and uses the language's own words, level 2 decides what a single declaration states, level 3 adds a table of what the system holds, and level 4 is the painted page, the page as a browser draws it. A run at a level reports the findings of the levels below it too. At level 3 the table lists the system's actors, and every declaration whose `SATISFIES` holds `ACT` must name an actor. Chapter 9 runs `HIDDEN_AUTHORITY`. Article V and Rule 83 bear the same title.

## Whoever wrote it, whoever acts

Here is a reconciliation desk in accounts. An AI agent matches the lines of a bank statement to invoices, and an accountant answers for the books. Say an AI model wrote the first declaration of the desk, and left a comment on its first line, which the verifier skips. An `INTENT_FLOW` is a flow, what a user does to reach one goal: `SATISFIES` lists the verbs it carries out, `ALWAYS_REACHABLE` the verbs that stay within reach at every step, and `ACTOR` names who acts.

::: plate Written by an AI model
```zayn matches.zayn
// written by an AI model, which says it kept Rule 79
DEFINE INTENT_FLOW apply_matches (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR matching_agent
)
//--> MISSING_UNDO apply_matches
```
In words: An AI agent applies the matches after a confirmation; cancel and exit stay within reach. An AI model wrote the declaration and says it kept Rule 79.
:::

Refused, under Rule 79, the rule the comment says was kept: the act keeps no undo. The report ends on the exit code, the number the command returns: 1 when it refuses, 0 when it accepts. Now the same flow as a person would write it, for the accountant to apply.

::: plate Written by a person
```zayn matches.zayn
// written by a person, for the accountant
DEFINE INTENT_FLOW apply_matches (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR accountant
)
//--> MISSING_UNDO apply_matches
```
In words: The accountant applies the matches after a confirmation; cancel and exit stay within reach. A person wrote the declaration.
:::

The writer changed and the actor changed, and the report did not: the same refusal, the same rule, the same right, to reverse. The verifier reads the fields, never the writer, and holds the AI agent's act to Rule 79 as it holds the accountant's. The repair is one word for both.

::: plate The matches, with a way back
```zayn matches.zayn
DEFINE INTENT_FLOW apply_matches (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR matching_agent
)
//--> clean
```
In words: An AI agent applies the matches after a confirmation; undo, cancel and exit stay within reach.
:::

Clean. A claim to have kept a rule is a comment, and the verifier's answer is the run.

## A proposal and its authority

Rule 98 has a word in the language: the role `proposal`. A role is the promise a control makes about what happens when it is used. A control is an `INTERACTION`, and its role is one of these words: `inert`, `navigate`, `reversible`, `irreversible` and `proposal`. `proposal` promises that the control "commits nothing until an authority accepts". Here the AI agent proposes a match, and a user previews and selects it.

::: plate A proposal that advises
```zayn reconcile.zayn
DEFINE INTERACTION suggest_reconciliation (
  SATISFIES [PREVIEW, SELECT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE proposal
)
//--> clean
```
In words: The AI agent proposes a match; a user previews it and selects it, and nothing is committed.
:::

Clean: a proposal that does not act commits nothing, and the law asks no authority of it. Now the proposal acts.

::: plate A proposal that commits itself
```zayn reconcile.zayn envelope
DEFINE INTERACTION suggest_reconciliation (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal
)
//--> PROPOSAL_COMMITS suggest_reconciliation
```
In words: The AI agent's match is applied as soon as it is proposed; undo and cancel stay within reach.
:::

Refused, under Rules 98 and 83 and Article V, and the third line of the report says so. Rule 98 lists this case among what to avoid: "Auto-applied AI corrections". The report is printed a second time as data, its machine form: this is what a person, or a tool, hands back to an AI model that writes declarations, with each rule cited by number. The repair names the authority.

::: plate The accountant accepts the proposal
```zayn reconcile.zayn
DEFINE INTERACTION suggest_reconciliation (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal,
  ACTOR accountant
)
//--> clean
```
In words: The AI agent proposes a match, and the accountant applies it.
:::

Clean. Chapter 17 runs the same pair at a help desk, and one step more: the AI agent named as the authority of its own proposal, which is clean as well. The verifier reads that an authority is named. A person reads who it is.

## Where a person reads

Rule 98 lists another case to avoid: "Agent-triggered irreversible operations". Here an AI agent purges the bank lines that matched nothing.

::: plate An AI agent's irreversible act
```zayn purge.zayn
DEFINE INTERACTION purge_unmatched (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible,
  ACTOR cleanup_agent
)
//--> clean
```
In words: An AI agent confirms, and the unmatched lines are purged; the control says this cannot be taken back.
:::

Clean: the verifier passes the case that Rule 98 lists to avoid. The role `irreversible` keeps no undo, by its promise, and chapter 8 tells why that is lawful. And `ACTOR` is a name: the verifier reads a person's name and an AI agent's alike. Here is the same purge, split as Rule 98 asks.

::: plate The purge, split as Rule 98 asks
```zayn purge.zayn
DEFINE INTERACTION propose_purge (
  SATISFIES [PREVIEW, SELECT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE proposal,
  ACTOR cleanup_agent
)

DEFINE INTERACTION purge_unmatched (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible,
  ACTOR accountant
)
//--> clean
```
In words: The AI agent proposes the purge for review; the accountant confirms and purges, knowing it cannot be taken back.
:::

Both files are clean, and the difference between them is the one Article V cares about. "Never an authority above it" is held here by a person who reads the names, when the declarations are reviewed, with the rule in hand. The verifier reads the shape of the authority; a person reads who it is.

## While an AI model writes

An AI model works with the law today through the verifier's command. The command checks the files named after it, `zayn check orders.zayn`, and with the option `--json` it prints the machine form above. The Zayn site describes a loop: give the law to an AI model, ask it to declare each surface before it draws it, run the verifier, and hand it the findings by rule number. In the site's words: "This loop is a procedure: the model declares, the verifier refuses by name, and the model corrects until the declaration is lawful." A refusal by rule, the page says, "lets a generator be told *which* law it broke instead of being told only that it was wrong". The loop ends on what the verifier reads: the exercise below shows a declaration that reaches a pass by the role it chooses, and a person reads that choice.

The roadmap names the next step: "An MCP surface serving the law to AI tools", so that AI models can consult the law while they generate. And chapter 24 shows the grammar written for a decoder, which would hold an AI model to a declaration's shape, in a form of its own.

## What I refused

**I deferred requiring a role on every act until evidence asks for it.** On 19 August 2026 I ruled that requiring a role is, in the words of the design note on roles, "deferred to evidence"; chapter 17 tells it. It bears on this chapter: the check of Rule 98 reads the role `proposal`, and a file in which no control states a role passes it with a warning.

**The record refuses a role that names a widget.** The roles are promises about what an act does and who decides it, and the contract says the vocabulary was "Deliberately NOT sourced from Set 13, Widget Selection, whose rules prescribe widgets". The design note on roles says it in five words: "Nothing here names a widget." A `proposal` is a promise about who decides, never a chat bubble or a side panel.

**The record refuses to merge the two authority checks.** `PROPOSAL_COMMITS` and `HIDDEN_AUTHORITY` both ask for an actor, and the contract keeps both: the first "Overlaps HIDDEN_AUTHORITY in spirit and not in reach". The first is decided from the file alone, at level 2, because the role has said the act was advisory. The second needs the list of actors, at level 3. Given that list, both fire on one missing actor, each citing Rule 83, and a request of this book to the Zayn project names this double finding.

[AUTHOR: the stake of this chapter, in your words: why an AI agent is an actor under the law and never an authority above it, and what you have seen happen where it was the second.]

## The court

The court of this chapter is these fixtures of the suite, each a declaration kept with the answer it must get, most of them in pairs with a twin, the same file made lawful. A proposal that acts with no authority named, and its twin that names the accountant. An act that names no actor at level 3, on a file with no medium named and on a screen; a medium is where the interface meets its user, a screen, a voice line or a program. An act with no undo, and its twin. The warning a file gets when none of its controls states a role, and its twin. And a role outside the five, and its twin. Of Set 31, the fixtures name Rule 98; a person reads the set's other rules, with each rule's number and words in hand.

## Where the field leads

The field leads while the AI agent works. The Model Context Protocol sits beside the AI agent as it runs: its host "must obtain explicit user consent before invoking any tool", and a person "SHOULD" be able to deny a tool's call. A2UI goes further on the drawing, with parts the application registered. Zayn's service for that moment, the law served to AI tools while they work, is on its roadmap.

The field leads over time. Its guidelines speak of an AI system over many interactions: "G13: Learn from user behavior.", "G14: Update and adapt cautiously.", "G18: Notify users about changes." A declaration states one surface, and those guidelines stay with the team.

Zayn's law leads on the act. It names the AI agent as an actor. It asks each proposal that acts to name its authority, from the file alone, and each act to name its actor, at level 3, given the list of actors. The verifier refuses the declaration that breaks it before any interface is drawn, with the rule cited by number in a form the AI model that wrote it can read. Where the statute asks that a person can override or reverse a system's output, the law asks a way back on every act not declared irreversible, and a named authority on every proposal that acts; whether that authority is a person, a person reads. Where the statute asks that generated output be marked, Rule 99 asks the same of an interface, and the law files it under `machine-later`: a person checks the mark.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The law sets every AI agent under Article V, and Set 31 gives its rules, each with its reason and its tier word, as data. The verifier answers for Rule 98 through `PROPOSAL_COMMITS`, together with Rule 83, on any control that calls itself a proposal and acts; at level 3, given the actors, it answers for Rule 83 on every act. It judges a declaration by what it states, whoever wrote it and whoever acts, and this page ran it with both changed. An AI model works with the law today through the command and its machine form, in a loop that a person runs, which the Zayn site describes. The law served to AI tools while they generate, and rules for a conversation with an AI agent and for approval and consent, are next on the roadmap. The verifier reads the shape of the authority; a person reads who it is, and whether an AI agent stands where the law asks for a person, as in Rule 102.

## In your hands

Here is the reconciliation desk as an AI model might write it: the AI agent's suggested match, and a message that warns. A `FEEDBACK` is a message of the system: its field `TONE` sets how it speaks, and its field `REPORTS` names the state it reports. Rule 112 counts a message that reports no state as decoration. Write what you expect the verifier to refuse, rule by rule, then open its answer.

::: plate For you: the desk as written
```zayn desk.zayn
DEFINE INTERACTION apply_suggested_match (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [CANCEL]
)

DEFINE FEEDBACK match_nudge (
  TONE cautionary
)
//--> MISSING_UNDO apply_suggested_match
//--> DECORATIVE_ANIMATION match_nudge
//--> ROLE_UNDECLARED
```
In words: The AI agent's suggested match is applied, with cancel within reach. Then the system warns, in a cautionary tone, and says nothing of what it warns about.
:::

The match keeps no undo, the message reports nothing, and no control of the file states a role. Repair the two refusals, and say what you expect. Try before you read on.

::: plate Undo, and a message that reports
```zayn desk.zayn
DEFINE INTERACTION apply_suggested_match (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)

DEFINE FEEDBACK match_nudge (
  TONE cautionary,
  REPORTS [unmatched_lines]
)
//--> ROLE_UNDECLARED
```
In words: The AI agent's suggested match is applied, with undo and cancel within reach, and the message reports the lines still unmatched.
:::

The file passes, with a warning: its exit code is 0, the number a command returns when it accepts. The match is still applied by the AI agent, and the file names no one who accepted it. Now write the control's true role, and say what you expect. Try before you read on.

::: plate The true role, written
```zayn desk.zayn
DEFINE INTERACTION apply_suggested_match (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal
)

DEFINE FEEDBACK match_nudge (
  TONE cautionary,
  REPORTS [unmatched_lines]
)
//--> PROPOSAL_COMMITS apply_suggested_match
```
In words: The same match, and the control now says that it is the AI agent's proposal.
:::

Writing the truth turned a pass into a refusal! Name the authority.

::: plate The accountant accepts the match
```zayn desk.zayn
DEFINE INTERACTION apply_suggested_match (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE proposal,
  ACTOR accountant
)

DEFINE FEEDBACK match_nudge (
  TONE cautionary,
  REPORTS [unmatched_lines]
)
//--> clean
```
In words: The AI agent proposes a match, and the accountant applies it, with undo and cancel within reach; the message reports the lines still unmatched.
:::

Clean. Now write the other role that is true of the match: it can be undone.

::: plate The other true role
```zayn desk.zayn
DEFINE INTERACTION apply_suggested_match (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)

DEFINE FEEDBACK match_nudge (
  TONE cautionary,
  REPORTS [unmatched_lines]
)
//--> clean
```
In words: The AI agent's match is applied and can be undone, and the control says so; no one is named who accepts it.
:::

Clean as well, with no authority named. A control states one role. Which should this one state, and should a control whose act an AI agent proposes be required to say so? The first half is a question filed with the Zayn project, and the second is my ruling of 19 August 2026, put to you.

The AI agent acts under the law. It also uses interfaces, as a person does, and the next chapter takes up that side.
