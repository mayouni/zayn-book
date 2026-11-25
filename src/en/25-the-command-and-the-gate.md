---
id: the-command-and-the-gate
part: 10
number: 25
title: The command and the gate
stage:
  built: "the reference command, four of its options and its three exit codes, run on this page; its machine form, in the shape the family's Diagnostic Contract sets; the zayn command of release {{n:release.version}}, one file for each operating system, told as its release notes record it"
  designed: "the gate's step and the pack's check written into a team's build service, as the record's guides set them out"
  next: "the symbol table computed from a project, which the record names as the work that follows; rules moved from a person's judgment to a program as the programs that check them are built; the law served to AI tools while they work"
status: draft
research: research/ch25.md
fixtures: [read-act-collapse, read-act-lawful, unresolved-intent-flow, role-undeclared, role-undeclared-lawful, hidden-authority, invisible-state, role-promise-broken, unexpected-character, clean-minimal]
---

The command is the verifier as a program a team runs by typing its name, and the gate is the step of a team's build where it runs, so that a declaration that breaks the law stops the build. A build is the chain of commands that turns a team's files into a product. It stops when one command ends with any number but 0, and that number is the command's exit code. In this chapter I read the command as the record, Zayn's repository at its release, holds it. I run the reference command on the three values of that number, and I describe the release, the command's published files, as its notes record it. Then I show what a team chooses: the level of the check, the table of what the system holds, and the files.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

A declaration names its kind and its name, then lists its clauses. The kinds on this page are a `SCREEN`, an addressable surface; a `FORM`, a conversation with the system; an `INTENT_FLOW`, the steps of one intent, such as submitting a week; and an `INTERACTION`, an act bound to an object, such as a control. `SATISFIES` lists the law's verbs that the user performs there, such as `READ`, `SELECT`, `CONFIRM` and `ACT`. `ALWAYS_REACHABLE` lists the verbs kept within reach at every step, such as `UNDO` and `CANCEL`. `ROLE` states the promise a control makes about acting on it, in one of five words: `inert`, it informs; `navigate`, it changes what is shown; `reversible`, it changes what is true and can be taken back; `irreversible`, it changes what is true for good; `proposal`, it commits nothing until an authority accepts it. A plate is a declaration shown with its run, and its lines that begin `//-->` are comments the verifier skips.

## The field

The field's gates read one number. Git, the program that records a team's changes, runs a hook, a script of the team's, before each change is recorded. Its documentation says of the `pre-commit` hook: "Exiting with a non-zero status from this script causes the git commit command to abort before creating a commit." The same hook "can be bypassed with the --no-verify option". The pre-commit project, "A framework for managing and maintaining multi-language pre-commit hooks", gives the reason teams use them: "Git hook scripts are useful for identifying simple issues before submission to code review." So the first gate stands before a change is recorded.

A shared copy of a project can stop a change in the same way. Continuous integration, CI, is a service that runs a team's build on every change sent to that shared copy. GitHub's documentation says of a protected branch with required checks: "all required status checks must pass before collaborators can merge changes into the protected branch". And of an action, one step of such a build, an exit code of 0 means "The action completed successfully and other tasks that depend on it can begin"; "Any other exit code indicates the action failed." The second gate stands before a change joins the others.

The tools decide what their number means. ESLint, a program that checks code, gives "error" an exit code of 1 and lets "warn" leave it untouched, and a team can go further with `--max-warnings`, which "can be used to force ESLint to exit with an error status if there are too many warning-level rule violations". And the field shares one format for findings. SARIF, a standard of the OASIS consortium, "defines a standard format for the output of static analysis tools", and "GitHub can parse SARIF files produced by third-party tools to display code scanning alerts in repositories."

Each source was read on 21 and 24 November 2026, and Appendix F lists them. So the field's gate stops on a number, and the tool behind it decides which findings move the number.

## The principle

**A gate reads one number: 1 when the verifier refused a declaration, 0 when it refused none, even with warnings, and 2 when it could not open what it was given; the build goes on at 0 alone.**

The reference command's own guide says it in two lines: "Exit codes: 0 clean · 1 violations found · 2 usage or read error. That is all a CI gate needs." A gate set to read a table of what the system holds needs one thing more, that table, as the section on a team's choices shows. Zayn belongs to a family of languages built the same way, each with its own law and its own verifier, which the family calls a court. The family's Diagnostic Contract sets the shape every one of them gives a finding, and gives each severity, error or warning, its meaning. An `error` means "the artifact is unlawful; a build must fail"; a `warning` means "lawful but suspect, or undecidable without more input". The report is for a person; the machine form, the same findings printed for a program, is for a tool; and the number is for the build.

## The command, as released

The command has two programs in the record. The reference is a program in JavaScript, run with Node, the program that runs JavaScript outside a browser, as `node tools/zayn/cli.js check` in a copy of the repository. This book runs it on every plate, and it answers one verb, `check`. The `zayn` command is the same verifier written again as one file for each operating system, written to print byte for byte what the reference prints, which a script of the record compares. The command lines of this page run the reference under the command's name, and a file it cannot read is told in the reference's own words.

A verb of the command is the first word after its name, and an option, a word that begins with two hyphens such as `--level 3`, changes how the verb works. The first lines of the command's source list its verbs. `check` is the verifier. `conformance` runs the suite: the declarations the record keeps, each with the answer it must get, which are called its fixtures. `pack` writes or checks the manifest of the files a team pins, that is, records by their hash, so that it uses one edition. `cross-medium` compares one declaration's renderings in two media. `audit-facts` reads the facts of the audit of screenshots, `serve` serves the site and its audit, `site` runs the site's own checks, and `version` names the editions of the law, the language and the contract that the command carries; the option `--version` names the release.

The release {{n:release.version}} carries the law at version {{n:law.version}}, the language at {{n:lang.version}}, and the contract at {{n:contract.version}}. The contract is the file that binds each kind of finding to the law and places it at a level; the family's Diagnostic Contract is another file, the shape of a finding. The release notes list its files.

{{release}}

A file's name says the system it runs on: `x86_64` and `aarch64` name the two families of processor, and SHA-256 is the kind of hash, a long number computed from a file's bytes. The `.wasm` file is the verifier built for a browser, the one the Zayn site runs on its pages. The notes say how to know a file: "The hash is how to know a file is the one built here." The same bytes give the same number. And they say what to do when the check of a file's hash fails: "A file that prints FAILED is not the one built here: do not run it." This book runs the reference command in its build, and tells the release's files as their notes record them.

## One number, three values

The gate's one number has three values, the command's answers to a build: 1, 0 and 2. Here each is run on a timesheet desk, where an employee enters the hours of the week and submits them, and a manager reviews the team's weeks. A change to its declarations reaches the gate.

::: plate A screen that reads and submits
```zayn week.zayn
DEFINE SCREEN timesheet_week (
  SATISFIES [READ, ACT],
  ALWAYS_REACHABLE [UNDO]
)
//--> READ_ACT_COLLAPSE timesheet_week
```
In words: On the week's timesheet, a user reads the hours, and the same screen submits them; undo stays within reach.
:::

Refused, under Rule 16: a screen the user reads also acts. The contract states the invariant: "A read surface that silently acts is an intent violation." The command answers 1, and the build stops. A tool reads the same refusal in the machine form, with the option `--json`:

```shell
$ zayn check week.zayn --json
# exit 1
```

Each finding is one object under `diagnostics`: its `code`, its `severity`, its `message`, its `span`, the file and the line where it stands, and what it `cites`, the rule by its number and the article by its name, which the person's report prints as a numeral. Then its `language`, its `level`, the level the contract gives its kind, and the `subject`, the name it judges. The repair puts the act on a flow of its own: the week is read on one screen, and submitting it opens steps of its own, where the user selects, confirms, and can go back.

::: plate The week, read on one surface and submitted on another
```zayn week.zayn
DEFINE SCREEN timesheet_week (
  SATISFIES [READ, FILTER]
)

DEFINE INTENT_FLOW submit_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
//--> clean
```
In words: On the week's timesheet, a user reads and filters the hours. To submit the week, the user selects it, confirms, and it is submitted, with undo and cancel within reach at every step.
:::

Clean, and the command answers 0. In the machine form the answer is the same object with no finding in it. With `--quiet` the command prints a person's report, findings only, and a clean run prints nothing. Here are both:

```shell
$ zayn check week.zayn --json
$ zayn check week.zayn --quiet
# exit 0
```

In the machine form a clean run still prints its list of findings, under `diagnostics`, empty. The family's Diagnostic Contract requires it: "*Clean* and *no output* are different facts". Now a finding that is a warning.

::: plate A form whose flow is elsewhere
```zayn entry.zayn
DEFINE FORM week_entry (
  INTENT_FLOW submit_week,
  SATISFIES [SELECT, CONFIRM]
)
//--> UNRESOLVED_INTENT_FLOW week_entry
```
In words: The week's entry form serves the flow that submits the week; the user selects and confirms. The flow is declared in another file.
:::

A warning, and the command answers 0. The build goes on, and its log, the text the build prints as it runs, keeps the warning for a person to read. The flow is declared in the file of the second plate. Here are the two files checked in one run:

```shell
$ zayn check week.zayn entry.zayn
# exit 0
```

The warning stays: the verifier judges each file on its own, and the next section shows what that means for a project. Now a file the verifier reads and cannot parse.

::: plate A parenthesis lost
```zayn broken.zayn
DEFINE INTENT_FLOW submit_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)

DEFINE SCREEN timesheet_week (
  SATISFIES [READ, FILTER]
//--> SYNTAX_ERROR timesheet_week
```
In words: The flow that submits the week, then the timesheet screen, whose closing parenthesis was lost.
:::

A syntax error, at the line where the file ends, and the command answers 1. A file the verifier reads and cannot parse, that is, cannot read in the language's grammar, is a refusal. Here is a file name with no file behind it:

```shell
$ zayn check sheet.zayn
# exit 2
```

2: the command could not open what it was given, a read error in its own words. So the gate's one number has three values, and each is a different message: 1, a declaration broke the law or the language's grammar; 0, none did; 2, the gate itself was set wrong.

## What a team chooses

A team chooses the level, the table and the files the gate checks. A level is how much the verifier is given. The contract places each kind of finding at one of four levels. Level 1 checks that the file is well formed and uses the language's own words. Level 2 decides what the file alone states, its declarations read together. Level 3 adds a table of what the system holds. Level 4 is the painted page, the page as a browser draws it. The contract places {{n:diag.level4}} kind of finding there, content that "reserves no space and shoves the reading when it lands". Its note gives that kind to the audit of the painted page, a program that measures the page in a browser, which chapter 26 shows. A run at a level reports the findings of the levels below it too, so a run at level 4 runs every check the verifier holds. The command runs at level 2 unless it is told another.

The symbol table, the table for short, is a small file, given with `--symbols`, that lists what the system around a declaration holds under four keys, named `entities`, `actors`, `state` and `elements`. The two checks of this chapter read two of them: `actors` for an act's actor, and `state` for what a surface must show. A team writes the table by hand today; a table computed from the project is the work the record names next. Here is the second plate's file, word for word, at level 3 with the project's table.

::: plate The same week, at level 3
```symbols project.json
{
  "actors": ["employee", "manager"],
  "state": ["week_status"]
}
```
```zayn week.zayn level=3 symbols=project.json
DEFINE SCREEN timesheet_week (
  SATISFIES [READ, FILTER]
)

DEFINE INTENT_FLOW submit_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
//--> HIDDEN_AUTHORITY submit_week
//--> INVISIBLE_STATE week_status
```
In words: The same timesheet and the same flow. The project's table says that the system knows two actors, an employee and a manager, and holds one state the user must know: the status of the week.
:::

Two refusals where level 2 found none: the act names no actor, and the status of the week is shown nowhere. The verifier's messages say operator, the language's word for the person this book calls the user. The level a team sets changes what its gate stops. Here is the same file at level 3, with no table:

```shell
$ zayn check week.zayn --level 3
# exit 0
```

Clean, and the command answers 0. Without the table, the checks of level 3 have nothing to read, and they say nothing. The command's own help says it: "undecidable is silence, never a pass". The silence is the verifier's, and the 0 is the gate's: the report and the machine form of this run are those of a clean file, and a gate reads them as a pass. So a gate set at level 3 is given its table on the same command line. Here is the repair, checked with the project's table, as the plate before was.

::: plate The week, repaired at level 3
```zayn week.zayn level=3 symbols=project.json
DEFINE SCREEN timesheet_week (
  SATISFIES [READ, FILTER],
  VISIBLE_STATE [week_status]
)

DEFINE INTENT_FLOW submit_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR employee
)
//--> clean
```
In words: The timesheet shows the status of the week. To submit the week, the employee selects it, confirms, and it is submitted, with undo and cancel within reach.
:::

Clean. Now the files. A project keeps its declarations in several files, and the record's build step checks them in one run: `zayn check specs/*.zayn`, where the star stands for any name, every `.zayn` file in the folder `specs`. Here are two files of the project, the screens and the flows, each checked at level 3 with the project's table.

::: plate The project's screens
```zayn screens.zayn level=3 symbols=project.json
DEFINE SCREEN timesheet_week (
  SATISFIES [READ, FILTER],
  VISIBLE_STATE [week_status]
)
//--> clean
```
In words: The project's file of screens: the timesheet, where a user reads and filters the hours and sees the status of the week.
:::

::: plate The project's flows
```zayn flows.zayn level=3 symbols=project.json
DEFINE INTENT_FLOW submit_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR employee
)
//--> INVISIBLE_STATE week_status
```
In words: The project's file of flows: the employee submits the week. The screen that shows the week's status is in the other file.
:::

The flows file is refused for a state that the screens file shows. Here are the two checked together, in one run:

```shell
$ zayn check screens.zayn flows.zayn --level 3 --symbols project.json
# exit 1
```

Each file keeps the answer it gets alone: the screens clean, the flows refused. At level 3 the verifier reads each file with the whole system's table: the table speaks for the project, and the file for itself. So a team that gates at level 3 keeps a flow and the screen that shows its state in one file, as the repaired week does, and the gate passes. Which the gate should read, one file or the project's declarations together, is a question this book puts to the Zayn project.

## What I refused

**I refused the law a web address until someone outside asks to cite it; until then its hash names it.** On 18 August 2026 I ruled, in the words the pack's guide records: "The pack stays content-addressed. Buy a domain when the first outside citation is asked for." Content-addressed means named by its hash. The pack is the set of files a team pins. The law is one file and the language four. The contract is one, and the family's Diagnostic Contract two, with the file of its shape. Two files hold the media an interface can be rendered in and what each medium carries, and two hold the proof: the suite's manifest and the cases of the comparison across media. That is {{n:pack.files}} files, with a manifest of the pack, `MANIFEST.json`, the list that gives each file's hash. The guide tells a team what to do with it: "Vendor the twelve files, record `MANIFEST.json` beside them, and make `zayn pack --check` a step in your build." To vendor is to copy the files into the team's own project. "A version number says which edition you meant. A hash says the bytes you have are that edition."

**The record refuses a manifest that rewrites itself when the files change.** "The manifest never regenerates itself": the pack's tool writes it only when asked, "because a manifest that follows the tree automatically pins nothing". The tree is the folder of files the manifest lists.

**The record refuses a third severity.** The family's Diagnostic Contract ranks its two severities as rungs, and a court in its words is one verifier of the family: "A third rung is a substance change to this contract, never a court's private extension." A gate has two answers about the law, a refusal or a pass.

[AUTHOR: the stake of this chapter, in your words: why a refusal should stop a build, and what you want a team to do with the log that names the rule.]

## The court

In this book, the court of a chapter is the fixtures that judge its claims. Here they are these fixtures of the suite, each a declaration kept with the answer it must get, and their twins, the same files made lawful. A screen that reads and acts, and its twin. A form whose flow is elsewhere, a warning. The warning a file gets when none of its controls states a role, which leaves the number at 0, and its twin. The two checks of level 3, an act with no actor and a state shown nowhere. A control that promises a way back and keeps none, for the exercise. A file with a stray character, which the lexer, the part of the verifier that splits a file into its words, has no word for: a refusal at level 1. And the smallest clean file. The suite itself runs at every build of this book, at each level, and here is its run at level 4, which takes in every fixture.

{{suite:4}}

The box's first lines name the files the run reads. The line `envelope` counts the findings the fixtures produced, each checked against the family's shape, and the reports, one for each fixture. The lines `media` and `catalogue` check that two files saying one thing agree: the verifier and the file of media, and the contract and its prose, whose count is the contract's kinds of finding. The suite compares the codes a fixture gets with the codes it must get, "by diagnostic id only — never line numbers, wording or order".

## Where the field leads

The field leads in the display. GitHub reads SARIF files from other tools and shows their findings as alerts in a repository. Zayn's machine form is the one format its family of verifiers shares, which the family's Diagnostic Contract gives as "one CI gate, one editor plugin, one dashboard". A gate reads its number, a tool its machine form, and a person its report, in the log, where the rule is named.

The field leads in the team's control of the number. ESLint lets a team fail its build on warnings above a number. Zayn's family fixes two severities, and the contract the release carries places each kind of finding under one, so a team that keeps that contract gets the same meaning of a refusal in every build. A team can give the command another contract with `--contract`, and its gate then follows that file. A team that pins the pack and gives its gate the pinned contract keeps the release's meaning, since the pack's check compares each pinned file with its hash.

And the field's number says pass or stop, as Zayn's 0 and 1 do, and leaves the rest to the report. The record's evidence ledger, the file that keeps each finding of the project with its date, its source and whether it was verified, says it of the verb `cross-medium`, which compares one declaration's renderings in two media. Print has no instrument of its own, so a difference between the visual page and print stays undecided, and the run answers 1: an instrument "reporting a gap it cannot close is not the same as a gap somebody forgot to fill", and "the exit code cannot tell them apart". Its report says which. So each instrument sets what its number says of what it cannot decide: a check of level 3 with no table says nothing, a warning lets the build go, and the comparison across media stops it.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the reference command and its three exit codes, run on this page on every plate and every command line, with four of its options: `--json`, `--quiet`, `--level` and `--symbols`. The machine form is built, in the shape the family's Diagnostic Contract sets. The suite at level 4 is run by this book's build. The `zayn` command {{n:release.version}}, one file for each operating system, is built and described as its release notes record it: the Windows file was run there with `--version`, the suite, a check and the pack's check.

Designed: the gate's step and the pack's check written into a team's build service, as the record's guides set them out; this page runs the command those steps call. Next: the symbol table computed from a project, which the record names as the work that follows; rules checked by a person, moved to a program as the programs that check them are built, so that what a gate refuses grows; and the law served to AI tools while they work.

## In your hands

Here is a change to the manager's review of the team's weeks. Look for three faults: a selection that acts with no step to confirm it, an act with no way back within reach, and a control whose role promises a way back that it does not keep. Write the faults you expect, and the number the gate reads, then open the solution.

::: plate For you: the review, as changed
```zayn review.zayn
DEFINE SCREEN team_review (
  SATISFIES [SCAN, SELECT, ACT]
)

DEFINE INTERACTION mark_reviewed (
  SATISFIES [MARK],
  ROLE reversible
)
//--> SELECT_ACT_COLLAPSE team_review
//--> MISSING_UNDO team_review
//--> ROLE_PROMISE_BROKEN mark_reviewed
```
In words: On the team's review, a manager scans the weeks, and selecting one approves it. A control marks a week as reviewed, and says the mark can be taken back.
:::

Repair it, and say what you expect. Try before you read on.

::: plate The review, repaired
```zayn review.zayn
DEFINE SCREEN team_review (
  SATISFIES [SCAN, SELECT]
)

DEFINE INTENT_FLOW approve_team_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)

DEFINE INTERACTION mark_reviewed (
  SATISFIES [MARK],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: On the team's review, a manager scans and selects a week. To approve it, the manager selects, confirms, and it is approved, with undo and cancel within reach. The mark of review can be taken back.
:::

The gate passes at level 2, the command's default. At level 3, with the project's table, the review owes what the week owed there: an actor for the approval, the manager, and a surface that shows the status of the week. Now a shorter repair of the mark, which a hurried team might write: say that the mark cannot be taken back. Say what you expect. Try before you read on.

::: plate The mark, said to be final
```zayn review.zayn
DEFINE SCREEN team_review (
  SATISFIES [SCAN, SELECT]
)

DEFINE INTENT_FLOW approve_team_week (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)

DEFINE INTERACTION mark_reviewed (
  SATISFIES [MARK],
  ROLE irreversible
)
//--> clean
```
In words: The same review, and the control says that the mark of review cannot be taken back.
:::

Clean as well: the gate reads 0 for both repairs. A control that says it is final owes no way back, and the verifier reads what the control says. Can a manager's mark of review be taken back? The gate reads what the control says, and a person on the team knows what the mark does. Who reads that difference before the change ships?

The command runs on a team's declarations. The last chapter runs it on the Zayn site's own declarations, a site held to the law it publishes.
