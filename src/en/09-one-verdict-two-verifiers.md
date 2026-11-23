---
id: one-verdict-two-verifiers
part: 3
number: 9
title: "One verdict, two verifiers"
stage:
  built: "four levels of checking, filed as data; a conformance suite of {{n:fix.total}} fixtures, run on this page at each level; the level 3 checks, decided when a symbol table is supplied; the `zayn` command and its build for the browser, held to the JavaScript reference byte for byte in the runs their release notes record"
  designed: "the symbol table computed from the project around a declaration, in place of being written by hand; the evaluator forged from the Haro declaration judged against the command as well as against the reference"
  next: "the suite run by verifiers written by other hands, each stating its level and its differences"
status: draft
research: research/ch09.md
fixtures: [hidden-authority, invisible-state, intent-orphan, unresolved-entity, projection-visual-trust, clean-minimal, unknown-intent, unspecified-declaration, multiple-violations, duplicate-field, role-undeclared, foreign-pillar-ignored]
---

A verdict is the set of findings a verifier gives on one file. This chapter asks what keeps that verdict the same when the verifier changes. I give the four levels of checking and what each one needs. I run the conformance suite, which is a set of declarations kept with the answers they must get. Then I tell how two verifiers, written in two languages, are kept to one verdict, and how a third evaluator, made another way, names each place where it differs.

If you open the book here: a declaration is a few lines that say what a user is doing on a surface; the law is Zayn's constitution of {{n:law.rules}} rules for interfaces; the verifier is the program that checks a declaration against it; and a finding is one entry of the verifier's report, a refusal when it is an error.

## The field

The field knows how to keep several implementations of one standard to one result: it writes a shared suite of tests. The web-platform-tests project calls itself "a cross-browser test suite for the Web-platform stack", and it archives the results of an array of browsers, run on a regular basis. Test262 is, in its own words, "the implementation conformance test suite" for the specification of ECMAScript.

For interfaces, the field has taken the same step for the instruments that test a page. The W3C's format for accessibility test rules, a Recommendation of 5 February 2026, asks that each rule be published with examples whose outcome is known: passed, failed, and inapplicable. Its abstract gives the purpose: the harmonization of testing methods, the ones built into test tools among them.

So the instrument is known: cases with known answers, published, and run by every implementation. Each of these pages was read at its source on 23 November 2026, and Appendix F lists them.

## The principle

**A verdict belongs to the suite: a fixture is a declaration kept with the answer it must get, and every verifier, in whatever language it is written, is held to that answer at the level it can see.**

The page of Zayn's suite says what this is for: with it, an implementation can "prove agreement rather than assert it".

## Four levels of seeing

A verifier decides only what it is given enough to see. The contract files every kind of finding at one of four levels.

{{levels}}

Levels 1 and 2 need the file alone. Every plate of chapter 8 was decided there. Level 3 needs something a declaration cannot hold: what the system around it contains. Here is a flow that posts an entry to a ledger, at level 2.

::: plate A flow that acts, seen from the file alone
```zayn ledger.zayn
DEFINE INTENT_FLOW post_ledger_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT]
)
//--> clean
```
In words: To post an entry, a user confirms and the entry is posted. At every step the user can undo, cancel or leave.
:::

Clean. From the file alone, nothing says who may post the entry, and nothing says that anyone must.

Now the verifier is given one more thing: a symbol table, a small file that lists what the system holds. This one says that the system has two actors.

::: plate The same flow, with the system's actors given
```zayn ledger.zayn level=3 symbols=actors.json
DEFINE INTENT_FLOW post_ledger_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT]
)
//--> HIDDEN_AUTHORITY post_ledger_entry
```
In words: The same flow, word for word. The table beside it says that the system knows two actors, an accountant and an auditor.

```symbols actors.json
{
  "actors": ["accountant", "auditor"]
}
```
:::

Refused! The same file, the same verifier, and one more input. The finding cites Rule 83 and Article V: an act with consequences names who performs it. The repair is one field.

::: plate The same flow, naming its actor
```zayn ledger.zayn level=3 symbols=actors.json
DEFINE INTENT_FLOW post_ledger_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR accountant
)
//--> clean
```
In words: To post an entry, an accountant confirms and the entry is posted. At every step the accountant can undo, cancel or leave.
:::

Clean, at level 3. A table has four lists: entities, actors, state and elements. Each level 3 check waits for its own list, and a check whose list is not given says nothing. So read the words "clean at level 3" with the table in mind: they say that nothing was refused among the checks the table made possible.

## The suite, run on this page

A fixture is a declaration kept with the answer it must get. The suite is {{n:fix.total}} fixtures and a manifest, the list that gives each fixture its level and the codes it must receive. The build of this book ran the suite's own runner in the snapshot of Zayn. Here is what it printed.

{{suite:4}}

Read it from the bottom. Every fixture passed. The manifest says what a pass is: a run passes a fixture when the set of codes it reports equals the expected set, exactly. The line number, the wording of a message and the order of the findings stay outside the comparison, as chapter 8 said.

The three lines above the count are agreements the runner checks beside the fixtures. Every finding and every report has the shape of the machine form. The media the verifier knows are the ones the data lists. The contract's {{n:diag.total}} kinds of finding are the ones the specification catalogues. Each of these is one truth kept in two places, and the runner fails when the two places differ.

Now the same runner, asked for level 2.

{{suite:2}}

{{n:suite.2.pass}} passed and {{n:suite.2.skipped}} were skipped. The skipped ones are the fixtures of level 3, and a skip is not a failure: a verifier that reads the file alone has nothing with which to decide who an actor is. It states its level, and the suite holds it to that level.

Of the {{n:fix.total}} fixtures, {{n:fix.clean}} must get no finding, and {{n:fix.twins}} of those are lawful twins of a refused fixture. And {{n:fix.unfixtured}} kinds of finding have no fixture at all, each with its reason written in the manifest. One is the finding of level 4, which is a fact about a painted page. The other two are failures to parse: what a parser reports after its first failure differs from one parser to the next, and a fixture would bind every verifier to one parser's habits.

The suite holds no fixture above level 3, so its last line at level 4 says what a run at level 3 says. Level 4 needs a painted page, and chapter 10 measures one.

## Two verifiers, one answer

The verifier that ran every page of this book is written in JavaScript. It is the reference.

The verifier a team installs is the `zayn` command, one file, written in another language. It is a port of the reference, and its bar is set above the suite's. The suite compares codes. The gate between the command and the reference compares every byte: what each prints, what each prints on failure, and the exit code, on every fixture and on a corpus of inputs that a generator makes from the fixtures. The gate's own head states its rule: "There are NO allowed differences."

Why bytes, when the suite asks only for codes? Because a port that agrees on the code and changes the sentence has changed what a person reads.

I asked for that command in these words, which the design keeps as I typed them: "We should not depend on Node or any other thing!"

The release notes record the runs. Those of release 0.1.0 record the gate's full run with no difference to the byte. Those of release {{n:release.version}} record the Windows file passing the suite, {{n:fix.total}} fixtures of {{n:fix.total}}, and the files for the other systems as built.

The same core is also compiled for the browser, {{n:wasm.bytes}} bytes, so that a page can check a declaration with nothing installed. A proof page runs every fixture at every level through it and compares each answer with the command's: the record it compares with holds {{n:proof.answers}} answers for {{n:proof.fixtures}} fixtures.

The gate says in its own head what it proves, and I keep the sentence beside the result: parity is sameness. A command that agrees with the reference on every input carries every mistake of the reference.

## A third evaluator, and its differences

Two verifiers that share a design can share a blind spot. So Zayn was also declared a second time, in Haro, the language for declaring languages of this series' first book, from the data of the law alone. An evaluator is forged from that declaration, and it shares no code with the verifier. The record calls it the forged court.

It does not agree everywhere, and that is its use. Its judge ran it against the reference on {{n:haro.judged}} fixtures, and the list of its differences holds {{n:haro.rows}} rows, four of them added on 8 November 2026 for the menu fixtures and written by expectation. Each row names the fixture, what each of the two says, and the class of the difference. In {{n:haro.other_code}} rows both refuse and speak different codes. In {{n:haro.court_only}} rows the forged evaluator refuses a file the verifier accepts. In {{n:haro.not_refused}} rows the verifier refuses or warns and the forged evaluator says clean, and the five fixtures of level 3 are among them.

The list is a ratchet. The judge fails when a difference appears that is not on it, when a listed row changes, and when a listed difference now agrees and is still listed. A difference can leave the list only by being repaired and removed.

## What I refused

**I refused to choose where the verifier lives before there was evidence.** The fixtures and the specification were written first, on 6 August 2026, before a verifier could pass them. Once a suite exists, two implementations that drift apart are a failing run.

**I refused to fail a fixture that a verifier cannot see.** A fixture above a verifier's level is skipped. A verifier that pretended to decide it would be claiming a level it does not have.

**I refused a fixture for what a declaration cannot show.** The finding of level 4 is a fact about a painted page. The manifest says of a fixture for it that it "would be theatre".

**I refused a table that the verifier computes.** A verifier that stands alone accepts the symbol table as an input. What the system around a declaration holds is that system's to say.

## The court

The court of this chapter is the suite itself, and the box below holds the fixtures this page leans on. The five fixtures of level 3 carry their own symbol tables in the manifest, and the build ran each with its table.

## Where the field leads

The field leads in the number of hands. The web's suite is run by many browser projects, and their results are published side by side. Zayn's record holds one reference, one port of it in two builds, and one evaluator made another way, whose judge runs where the Haro forge is installed. The direction is the field's: more verifiers, written by other hands, each stating its level and listing its differences.

The field also has a third outcome that Zayn's suite names a skip. A rule for testing accessibility is published with cases where it does not apply, and a tool that meets one says so.

And a suite proves agreement. Whether what the verifiers agree on is right is the law's business, and Part VII's.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Two things ran on this page: the reference verifier and the suite's runner, both in the snapshot. The command, its build for the browser and the forged evaluator are told from their own records, each as its record states it. The symbol tables of this chapter were written by hand: a table is an input, and the project around a declaration is where it comes from.

## In your hands

Here is a refund desk: a screen and a flow. From the file alone it is clean. Beside it is the table of the system around it.

::: plate For you: a refund desk, and the system around it
```zayn exercise refunds.zayn level=3 symbols=desk.json
DEFINE SCREEN refund_desk (
  SATISFIES [READ, FILTER],
  VISIBLE_STATE [open_refunds]
)

DEFINE INTENT_FLOW issue_refund (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
```
In words: At the refund desk, a user reads the refunds and filters them, and the screen shows which refunds are open. To issue a refund, a user selects one, confirms, and the refund is issued, with undo and cancel within reach at every step.

```symbols desk.json
{
  "actors": ["cashier", "supervisor"],
  "state": ["open_refunds", "active_filter"]
}
```
:::

Run it at level 2, then at level 3 with the table: `zayn check refunds.zayn --level 3 --symbols desk.json`. Before the second run, write the codes you expect and what each will be about. One of the two findings has no line number: say why before you read on.

Repair it until the verifier answers clean at level 3 and every line of your file is true.

::: plate A form the verifier accepts
```zayn refunds.zayn level=3 symbols=desk.json
DEFINE SCREEN refund_desk (
  SATISFIES [READ, FILTER],
  VISIBLE_STATE [open_refunds, active_filter]
)

DEFINE INTENT_FLOW issue_refund (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR cashier
)
//--> clean
```
In words: At the refund desk, a user reads the refunds and filters them, and the screen shows which refunds are open and which filter is active. To issue a refund, a cashier selects one, confirms, and the refund is issued, with undo and cancel within reach at every step.
:::

It is clean. Now write `ACTOR intern`, a name the table does not hold, and run it again. The verifier asked that an actor be named. Should the actor also be one the system knows, as an entity that a view shows must be?

Every level so far reads a declaration or a table. Level 4 reads a painted page, and a declaration does not hold one. Part IV begins there, with what a declaration cannot see.
