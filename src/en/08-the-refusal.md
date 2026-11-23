---
id: the-refusal
part: 3
number: 8
title: The refusal
stage:
  built: "the refusal in three forms, all run on this page: the report a person reads, the machine form a tool reads and the exit code a build reads; a contract of {{n:diag.total}} kinds of finding, {{n:diag.cite_rule}} of them citing a rule of the law by its number; the role `irreversible`, with which an act says that it cannot be taken back"
  designed: "the screen, the voice line or the machine surface drawn from a declaration: the verifier judges the declaration, and its drawing for each medium is designed"
  next: "the law served to an AI model while it generates, so that a generated surface cites the rules it kept"
status: draft
research: research/ch08.md
fixtures: [missing-undo, missing-undo-lawful, missing-cancel, missing-cancel-lawful, select-act-collapse, select-act-lawful, trapped-flow, trapped-flow-lawful, decorative-animation, decorative-animation-lawful, multiple-violations, irreversible-claims-undo, irreversible-claims-undo-lawful]
---

A refusal is the verifier's answer to a declaration it does not accept: a finding that is an error. Chapter 7's refusals were for the grammar. In this chapter I make the verifier refuse for the law. I give it a declaration, I print its answer as the run gave it, and I read that answer one line at a time: what it found and where, why, and under which law. Then I repair the declaration and run it again.

If you open the book here, three words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface, with {{n:law.verbs}} verbs and no others, and that say nothing of how the surface is drawn. The **law** is Zayn's constitution for interfaces: {{n:law.rules}} numbered rules, kept as data, under {{n:law.articles}} articles and {{n:law.rights}} rights of the user. The **verifier** is the program that reads a declaration and checks it against the law. Chapter 6 gives the verbs, chapter 7 the {{n:lang.kinds}} kinds of declaration, and Part VII the law.

## The field

The field refuses program code, and it has given the refusal a shape. A linter is a program that reads source code and reports what breaks its rules: it has named rules, and a severity for each. ESLint's documentation lists three severities, off, warn and error, and says of the last that the "exit code is 1 when triggered". An exit code is the number a command hands back when it ends. A build, the chain of commands that turns a team's sources into a product, reads that number and stops.

For the interface, the field speaks in three other ways, each at its own moment.

It advises. The third of Jakob Nielsen's ten heuristics, User Control and Freedom, asks for a clearly marked "emergency exit" from an unwanted action, and its tips ask for undo and redo. The page calls the ten items broad rules of thumb. A rule of thumb is read by a person and applied by judgment.

It sets criteria. WCAG 2.2, a W3C Recommendation, has a criterion, 3.3.4, for the page that commits its user to a payment or to a legal act: the submission is reversible, or it is checked, or it is confirmed. A page meets the criterion or fails it, once the page exists.

It measures. axe-core describes itself as an "accessibility testing engine" for websites, and its README puts the share of WCAG issues it finds automatically at 57 per cent on average. One step earlier, eslint-plugin-jsx-a11y checks the source of the markup before a browser renders it, and tells whoever installs it to add a tool that tests the page once rendered.

So the field refuses code by a name and an exit code. For the interface it advises, sets criteria and measures, and what its checkers read is the drawing: the markup, or the page once painted. Each of these pages was read at its source on 21 November 2026, and Appendix F lists them.

## The principle

**A refusal names what it refuses and in which declaration, and it cites every rule, article and right that the law holds for its code.**

It does not say that something is bad practice. Where the law speaks of the defect, the refusal points at its sentence. So a refusal that cites the law has two answers and no third: repair the declaration, or amend the law with evidence. A refusal for the grammar alone, like chapter 7's unknown field, cites nothing and has one answer: the repair.

The specification of the language says why this matters: an opinion, in its words, gets "negotiated in the hallway". A finding that cites a numbered rule is settled where it can be checked: in the declaration, or in the law.

## An act with no way back

Here is a payment approval as a first draft declares it. `SATISFIES` lists what the user does on this surface: select a payment, confirm, act. To run it yourself, save the three lines in a file and give the file to the verifier: `zayn check payments.zayn`. Chapter 25 installs the command, and the testbench of the Zayn site checks a declaration in the browser with nothing installed.

::: plate An act, and nothing kept within reach
```zayn payments.zayn
DEFINE INTENT_FLOW approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT]
)
//--> MISSING_UNDO approve_payment
//--> MISSING_CANCEL approve_payment
```
In words: To approve a payment, a user selects it, confirms, and the payment is sent. The declaration keeps nothing within reach once the user has begun.

```sketch
title: Approve a payment
say: Payment 3 of 12 · 1,200.00 · due today
control: Approve
missing: Cancel | Rule 26
missing: Undo | Rule 79
caption: One control, and it goes forward. The two dashed outlines are the controls the verifier asked for, each with the rule it cited.
```
:::

Two refusals, and the exit code is 1! That number is what the command hands back when it ends, and 1 means that the verifier refused. The two lines that begin with `//-->` are comments, which the verifier skips. They state the answer this page expects, and the book's build fails if the verifier gives another.

Read the first refusal one line at a time.

**The first line** is made to be scanned. It gives the file and the line, `payments.zayn:1`; the severity, `error`; the code, `MISSING_UNDO`; and the subject of the finding, here the name of the declaration, `approve_payment`. The code is the stable part. Zayn's conformance suite compares the codes a verifier reports and nothing else: the line number, the wording and the order stay outside its comparison.

**The second line** is the sentence. The declaration satisfies `ACT`, and `UNDO` is not among the intents it keeps reachable. The sentence names the two fields the verifier read, so you know where the repair goes.

**The third line** is the law: Rule 79, Article IV, the right to reverse. Three citations, and each one can be opened. Here is the rule, printed from the law's own data.

{{rule:79}}

And here is the right.

{{right:reverse}}

The rule gives its reason in one line and the right says what a user is owed. The card also names the three kinds of finding that cite this rule. The verifier checked the part of Rule 79 that a declaration states: an act, and the undo that stays within reach of it.

The second refusal has the same three lines. `MISSING_CANCEL` cites Rule 26, Article IV again, and another right: the right to leave. Why two refusals for one missing field? Because they protect two different moments, and the specification says which in one line: "undo reverses what was done, cancel abandons what is being done."

The last line of the report counts: two errors, no warning, one file, level 2. An error is a refusal; a warning is a finding that lets the declaration pass. Level 2 is what a verifier decides from the file alone, and chapter 9 gives the four levels.

## The repair

The report said where to write: `ALWAYS_REACHABLE`, the field that lists what stays within the user's reach at every step.

::: plate The same act, with its two ways back
```zayn payments.zayn
DEFINE INTENT_FLOW approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
//--> clean
```
In words: To approve a payment, a user selects it, confirms, and the payment is sent. At every step the user can cancel, and can undo what was done.

```sketch
title: Approve a payment
say: Payment 3 of 12 · 1,200.00 · due today
control: Approve
restored: Cancel | Rule 26
restored: Undo | Rule 79
caption: The same surface with the two controls the declaration now promises. Where each one sits is the drawing's business; that both are there is the declaration's.
```
:::

Clean, and the exit code is 0. The report's last words give the version of the law it checked against, {{n:law.version}}. I added one line. It does not say where the Cancel control sits or what the Undo looks like. It says that both stay within reach at every step.

## Every finding, in one run

What does the verifier do with a declaration that breaks the law in several places? It reports every finding. Its two declarations are those of a fixture of Zayn's conformance suite. A fixture is a file kept with the answer it must get. This one has a wizard that deletes in bulk, and a message that celebrates.

::: plate One file, four findings
```zayn ledger.zayn
DEFINE WIZARD bulk_delete (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [CANCEL],
  STEPS [choose, apply],
  ACTOR operator
)

DEFINE FEEDBACK delete_flourish (
  TONE celebratory
)
//--> SELECT_ACT_COLLAPSE bulk_delete
//--> MISSING_UNDO bulk_delete
//--> TRAPPED_FLOW bulk_delete
//--> DECORATIVE_ANIMATION delete_flourish
```
In words: In two steps, an operator selects records and they are deleted, with cancel within reach and nothing else. Then the system answers in a celebrating tone, and says nothing of what changed.
:::

Four findings in one run. Read the second line of each: it says what the verifier found.

`SELECT_ACT_COLLAPSE` read `SATISFIES`, which lists `SELECT` and `ACT` with no `CONFIRM`: choosing a record carries out the act. The verb `CONFIRM` names the user's act of confirming, whatever carries it: a review step and a dialog are two drawings of the same declaration. Rule 79's sentence on confirmation is about one drawing, the dialog that interrupts, and it keeps that dialog for acts that cannot be undone.

`MISSING_UNDO` is the refusal of plate 8.1.

`TRAPPED_FLOW` read `STEPS` and `ALWAYS_REACHABLE`. A declaration with steps is a flow of several steps, and this one keeps `CANCEL` within reach and no `EXIT`. Cancel abandons the act in progress. Exit leaves the flow. A user of this wizard can drop the deletion and stay caught in its two steps.

`DECORATIVE_ANIMATION` stands on the message. The verifier read its `TONE` and looked for `REPORTS`, the field that says which state a message reports. It found none. The code says animation, and it covers any feedback that moves or takes a tone and reports nothing.

Now look at the third line of each. The citations are not the same length. `SELECT_ACT_COLLAPSE` cites a rule and an article, and no right. `TRAPPED_FLOW` cites two rules. `DECORATIVE_ANIMATION` cites a rule and Article I. A citation is as long as the law is: the verifier prints the rules, articles and rights its contract binds to that code, and adds nothing. The contract is the list of everything the verifier can report. Of its {{n:diag.total}} kinds of finding, {{n:diag.cite_rule}} cite a rule by its number, {{n:diag.cite_article}} cite an article alone, and {{n:diag.cite_none}} cite nothing, because where the law has no rule the verifier claims none. A finding that cites nothing has one answer: the repair.

Here is the repair of all four.

::: plate The same file, repaired
```zayn ledger.zayn
DEFINE WIZARD bulk_delete (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  STEPS [choose, apply],
  ACTOR operator
)

DEFINE FEEDBACK delete_report (
  TONE informational,
  REPORTS [deleted_count]
)
//--> clean
```
In words: In two steps, an operator selects records, confirms, and they are deleted. At every step the operator can undo, cancel or leave. Then the system says, in an informing tone, how many records were deleted.
:::

Clean. Three verbs were added to the wizard, and the message now reports a state.

## An act that cannot be undone

Some acts cannot be taken back, and purging an archive is one. Does the law ask for an undo all the same? It asks for one of two things, in the sentence that binds the {{n:law.family.action}} verbs of action, `ACT`, `CONFIRM`, `CANCEL` and `UNDO`: every act has a reachable undo, or declares why it cannot.

The language has a word for the second half. A declaration of the kind `INTERACTION` stands for one control, and it can state the control's role. One of its roles is `irreversible`. Here is a first draft that states the role and keeps the habit.

::: plate A control that says irreversible, and promises an undo
```zayn archive.zayn envelope
DEFINE INTERACTION purge_archive (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE irreversible,
  ACTOR administrator
)
//--> IRREVERSIBLE_CLAIMS_UNDO purge_archive
```
In words: An administrator confirms, and the archive is purged. The control says that this cannot be taken back, and the declaration still promises an undo.
:::

Refused, under the same Rule 79! The declaration promises a way back that the act does not have, and a user who trusts that promise learns the truth at the one moment it matters.

Under the report, the plate prints the same answer as a machine reads it, for the tools that read reports in place of people. The command gives this form when it is asked with `--json`. It is one object: the level, the versions of the contract and of the law, the files, the counts, and a list named `diagnostics` with one entry for each finding. In the entry, `code` is the stable name. `span` gives the file and the line. `cites` gives the law as three keys: `rule:79`, `article:reversibility`, `right:reverse`. `subject` says what the finding is about, and `level` says at which level it was decided. A build needs less than that. It reads the exit code: 0 when the verifier refused nothing, 1 when it refused, 2 when it could not read the file.

The repair removes the promise and keeps the right that still holds.

::: plate The same control, saying only what is true
```zayn archive.zayn
DEFINE INTERACTION purge_archive (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible,
  ACTOR administrator
)
//--> clean
```
In words: An administrator confirms, and the archive is purged. At every step the user can cancel. The control says that the purge cannot be taken back.
:::

Clean. So an act has two lawful forms: it keeps an undo within reach, or it says that it has none. Saying nothing is refused, as plate 8.1 showed. Saying both is refused, as plate 8.5 showed.

## What I refused

**I refused a verifier that stops at the first finding.** A file with four defects gets four findings in one run, as plate 8.3 shows. The suite carries that file as a fixture, and a verifier passes it only by reporting all four.

**I refused to compare wording.** The suite that keeps two verifiers to one verdict compares the codes they report and nothing else: the line number, the order and the sentence are free. Between the reference and its own port the bar is higher, and chapter 9 gives it. The contract binds each code to the law it cites, and the sentence may be written in whatever language its reader reads.

**I refused a citation that the law does not back.** A finding that cites a rule is answered by a repair or by an amendment, so a citation is a claim. The ruling of 2 November 2026 left two kinds of finding, `EXPRESSION_ORPHAN` and `VIBE_STRIPS_RIGHT`, citing an article and no rule.

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get, and a manifest that lists those answers. The build ran each fixture below in the snapshot of Zayn and compared its answer with the manifest.

Of the fixtures, {{n:fix.clean}} must get no finding, because a check that fires on everything proves nothing. Among them are the lawful twins: for a refused declaration, a second fixture where the defect is repaired. The box below sets a refused fixture beside its twin wherever the suite has one.

## Where the field leads

The field leads on the painted page. A checker such as axe-core reads the interface a browser has built: the contrast of a text against its background, the name a button exposes to a screen reader. Its rule list had 105 rules on 21 November 2026, each with its impact and its tags. A declaration of Zayn has no colour and no widget: both belong to the drawing. Chapter 10 measures the painted page.

And WCAG's criterion reaches the page as a user meets it, where a declaration states what every drawing of it must keep. A team keeps both: the refusal before anything is drawn, and the measurement of what was drawn.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Every run on this page was made by the verifier's JavaScript reference, at Zayn's release {{n:release.version}}, against the law at version {{n:law.version}}. A refusal covers what a declaration states: on this page, what its fields say of intents, reach, steps, tone and role. The rules it cites say more than a declaration can state, and Part VII sets the law's three instruments side by side: the verifier, the audit of the painted page and a person's judgment. A clean verdict covers the declaration and what it states. Whether the declaration is true of the screen that is delivered is measured on the painted page, in chapter 10.

## In your hands

Here is a wizard that closes an account, and a closed account stays closed.

::: plate For you: a wizard that closes an account
```zayn close-account.zayn
DEFINE WIZARD close_account (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [CANCEL],
  STEPS [choose, review, close]
)
//--> SELECT_ACT_COLLAPSE close_account
//--> MISSING_UNDO close_account
//--> TRAPPED_FLOW close_account
```
In words: In three steps, a user selects an account and it is closed, with cancel within reach and nothing else.
:::

Write the codes you expect, then open the verifier's answer under the plate and compare.

Now repair it. Adding `UNDO` silences `MISSING_UNDO` and makes the declaration untrue: nothing reopens the account. The true word is `irreversible`. Write it on the wizard, and say what you expect.

::: plate The true word, written on the wizard
```zayn close-account.zayn
DEFINE WIZARD close_account (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  STEPS [choose, review, close],
  ROLE irreversible
)
//--> ROLE_MISPLACED close_account
```
In words: In three steps, a user selects an account, confirms, and it is closed, with cancel and exit within reach. The wizard says that this cannot be taken back.
:::

Refused, for the place of the word: a role belongs to an interaction. Go on until the verifier answers clean and every line of your file is true. Try before you read on.

Here is a form the verifier accepts.

::: plate A form the verifier accepts
```zayn close-account.zayn
DEFINE WIZARD close_account (
  SATISFIES [SELECT, CONFIRM],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  STEPS [choose, review, close]
)

DEFINE INTERACTION close_for_good (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible,
  ACTOR account_holder
)
//--> clean
```
In words: In three steps, a user selects an account and confirms, and can cancel or leave at every step. One control closes the account: the account holder confirms, can cancel at every step before, and the control says that the closing cannot be taken back.
:::

It is clean, and it has two declarations: the wizard, which no longer says that it acts, and an interaction that acts and says `irreversible`. The act had to move: `irreversible` is a role, and only an interaction states a role. The two stand side by side, and the file leaves their order to its reader. Should a flow be able to say that its own act cannot be undone? Or is one interaction for each such act the right grain?

A refusal is worth what the court behind it is worth. The next chapter gives the four levels, runs the suite, and tells how a second verifier, the command, is kept to the reference's verdict.
