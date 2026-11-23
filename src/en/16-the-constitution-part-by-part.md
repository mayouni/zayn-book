---
id: the-constitution-part-by-part
part: 7
number: 16
title: The constitution, part by part
stage:
  built: "the law as one data file at version {{n:law.version}}: a preamble, {{n:law.articles}} articles, {{n:law.rights}} rights, {{n:law.forbidden}} forbidden patterns and {{n:law.sets}} sets of {{n:law.rules}} rules; citations made of the file's numbers and names, run on this page; a reader that shows every part of the law, made from the file; the file identified by its hash in a pack of {{n:pack.files}} files"
  designed: "a law in four layers: statute, core, commons and local; a field on a rule that records the sources which support it"
  next: "the law served to AI agents as they work, and rules moved to an instrument as each instrument is built"
status: draft
research: research/ch16.md
fixtures: [missing-undo, missing-undo-lawful, trapped-flow, trapped-flow-lawful, signal-unperceivable, signal-unperceivable-lawful, select-act-collapse, select-act-lawful, verb-not-carried, verb-not-carried-lawful]
---

The constitution of Zayn is one file. In this chapter I open that file and read it part by part: what it says of itself, its articles, its sets, one rule field by field, the rights of the user with the rules that enforce each, the patterns it forbids. On the way I make the verifier refuse four declarations, and I follow a citation back into the file.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface: a screen, a voice, a printed page. The **law** is Zayn's constitution for interfaces. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field writes its rules as documents. The Web Content Accessibility Guidelines are organised around "four principles", with "a total of 13 guidelines", and their success criteria are numbered, like 3.3.4, and "written as testable criteria". A classic of the field is a list: the ten usability heuristics of Jakob Nielsen, which their page calls "broad rules of thumb".

For the people who test a page, the ACT Rules Format says what a test rule must state. Two of its parts are the applicability, "what parts of the test subject are tested", and the expectations, each of which is "an assertion about a test target".

And the field keeps some of its decisions as data. The Design Tokens format defines a token as information with "a human readable name": a colour, a dimension, a typeface. Those are values of the drawing.

So the field has documents, lists of advice, a format for a rule that a tester runs, and data for the values of a drawing. Each source was read on 21 or 23 November 2026, and Appendix F lists them.

## The principle

**The law is one file: the page that shows it and the count that sizes it read it there, and every refusal cites it by its numbers and its names.**

The file is named `rules.json`. It is written in a notation for data, names and values between braces. A designer reads the law in its reader, a page made from the file, and never in the notation. The verifier reads the same file at each run: the title of a rule and the numeral of an article in a report are looked up there. Every count of the law on this page is read from the file by the book's build, the program that makes these pages. Appendix A prints the law, set by set.

## What the file says of itself

The file opens on its title, its version and its lineage, the dated list of its changes that chapter 18 reads. Then comes a preamble. It says what the law is for: "non-negotiable principles for business interfaces", which it wants "framework-agnostic, trend-resistant, and machine-checkable". In plain words: bound to no toolkit and to no fashion, and written so that a machine can check it. The preamble names its subject once: "the operator and the user name whoever acts through an interface: the user, a person or an agent". And it closes on short sentences, of which the last is "Undo is dignity." Article IV opens on the same words.

The word philosophy names two things in the file. One is a line of phrases, each of the form "X Over Y": calm over power, intent over mechanics, visible over hidden, business over technology. {{n:law.axioms}} of the articles have one of them as their axiom, the phrase an article stands on. The other is a section of {{n:law.principles}} principles, on the absence of pain, on empty space and on what lasts. The law's reader prints them before the articles, and they are outside the count of rules.

## The articles

An article is a statement of principle, and every rule derives from one article. Each of the {{n:rule.derived}} rules names its article in a field, which is a name with its value: `derived_from`. Here are the articles, with the number of rules that derive from each.

{{articles}}

The counts are uneven, and that is information. Most rules protect calm, visible state and the culture of an interface's users. Reversibility needs few rules, and the article on amendment fewest of all.

## The sets, by subject

A set is a subject: menus, forms, accessibility, time. The file holds {{n:law.sets}} of them.

{{sets}}

Read the last column. Why are a set's numbers not a range? Because a number is given once and never again, and a rule goes to the set of its subject. The rules are numbered up to {{n:law.highest}} and the law holds {{n:law.rules}}: {{n:law.unused}} numbers are out of use, and the file lists them with what became of each.

## One rule, field by field

Every rule has the same shape. Here is Rule 105, whole, as the file holds it.

{{anatomy:105}}

Every rule has {{n:rule.fields.all}} fields. `id` is a handle, and `number` is what a citation names. `title` is printed after the number in a report. `avoid` is a list of defects and `solution` is the text of the rule: the list shows the rule broken, the text states it kept. `why` is the reason, in a sentence or two.

`derived_from` is the article, by its name in the file: here `operator`, which is Article VI. `enforcement` is the rule's tier: one of {{n:law.tiers}} words, here `tool`, and chapter 17 reads them. `evidence` says where the rule comes from. Rule 105's is printed as written, and the site it speaks of is the one that showed the law at the time.

Some rules have more: {{n:rule.fields.some}} other fields exist. `invariant` is a mark, the value `true`, on {{n:rule.invariant}} rules. The law's reader prints it as the badge "vibe-invariant", and Article VI uses the same word of rights: "Vibe-invariant rights never flex." A vibe is a culture of interaction, and chapters 14 and 15 are about cultures. `lint` is a sentence that names a check or an instrument, the tool that makes a check, on {{n:rule.lint}} rules. `vibes` is a note for one culture or another, on {{n:rule.vibes}}. `see_also` points at a neighbouring rule, on {{n:rule.see_also}}. `absorbs` names the retired number that a rule took in, on {{n:rule.absorbs}}.

## The rights, and their rules

A right is what the user is owed, in one sentence, with the rules that enforce it. The file holds {{n:law.rights}}; here they are.

{{rights}}

A rule can stand in two lists: Rule 79 enforces the right to reverse and the right to act without fear. And a refusal can cite a right: {{n:diag.cite_right}} of the {{n:diag.total}} kinds of finding do. Here is a flow, which is a sequence of what a user does, that posts an entry to an accountant's ledger.

::: plate An act with no way back
```zayn ledger.zayn
DEFINE INTENT_FLOW post_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR accountant
)
//--> MISSING_UNDO post_entry
```
In words: An accountant confirms and an entry is posted. At every step the accountant can cancel or leave.
:::

Refused! The report ends on the level, here 2, which means that the verifier was given the file alone, and on the exit code, the number the command returns: 1 for a refusal, 0 for a file that passes. Read the third line of the report: a rule, an article, a right. Now follow each into the file. Rule 79 is the rule whose `number` is 79. Its `derived_from` says `reversibility`, and that is the name of Article IV. And the right to reverse lists 79 among the rules that enforce it. Here is that right, as the file states it.

{{right:reverse}}

No rule, article or right in the report's third line was typed into the verifier. The contract, which is the data file that binds each kind of finding to the law, says which rule, article and right this kind cites; the title and the numeral come from the law's file at the run. The repair is one word.

::: plate The same act, with undo within reach
```zayn ledger.zayn
DEFINE INTENT_FLOW post_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR accountant
)
//--> clean
```
In words: The same flow, and at every step the accountant can also undo.
:::

Clean. A second refusal, under another article and another right: a wizard, which is a flow with named steps.

::: plate Three steps, and no exit
```zayn opening.zayn
DEFINE WIZARD account_opening (
  SATISFIES [UNDERSTAND, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  STEPS [identity, funding, review],
  ACTOR applicant
)
//--> TRAPPED_FLOW account_opening
```
In words: In three steps, an applicant understands, confirms, and an account is opened. At each step the applicant can undo or cancel.
:::

Refused, and the citation names two rules: Rule 51 and Rule 53, both derived from Article II, and both in the list of the right to leave. One finding may cite several rules. The repair is again one word.

::: plate The same wizard, with an exit
```zayn opening.zayn
DEFINE WIZARD account_opening (
  SATISFIES [UNDERSTAND, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  STEPS [identity, funding, review],
  ACTOR applicant
)
//--> clean
```
In words: The same three steps, and at each one the applicant can also leave.
:::

Clean. A third, under Article III and the right to know. A `VIBE` declares the culture of a surface and its medium, the channel through which it reaches its user. Here the medium is sound: a queue monitor that a user hears. Its field `SIGNALS` lists the statuses that its values carry, from a closed list of five.

::: plate A monitor whose only status is silence
```zayn queue.zayn
DEFINE VIBE queue_audio (
  SURFACE_AS auditory
)

DEFINE SCREEN queue_monitor (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [muted]
)
//--> SIGNAL_UNPERCEIVABLE queue_monitor
```
In words: The surface is heard. On the queue monitor a user discovers and understands the queue, and its values have one status: muted.
:::

Refused: Rule 82, Article III, the right to know. In sound, `muted` is rendered as silence, and that is right for `muted`. The defect is that it is the only status the monitor declares: its user hears nothing at all. The repair declares a status that sounds.

::: plate A status that sounds
```zayn queue.zayn
DEFINE VIBE queue_audio (
  SURFACE_AS auditory
)

DEFINE SCREEN queue_monitor (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [muted, danger]
)
//--> clean
```
In words: The same monitor, and its values now have two statuses: muted, and danger for a queue that is stuck.
:::

Clean. Three refusals, three articles, three rights, and each rule, article and right in a citation is a name or a number that the file holds.

## The patterns the law forbids

The law also names what it forbids. A forbidden pattern is a title and the rules it breaks, and the file holds {{n:law.forbidden}}.

{{forbidden}}

The first column is a name that a team can say in a review, and the second says which rules stand behind it. Some kinds of finding are bound to a pattern. The report that a person reads prints the rule, the article and the right. The pattern is printed in the machine form, the same answer written as data for a tool. Here is a flow where choosing a row carries out the act, with both forms.

::: plate Selecting is acting
```zayn pick.zayn envelope
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR clerk
)
//--> SELECT_ACT_COLLAPSE pick_and_pay
```
In words: A clerk selects an invoice and it is paid. Undo, cancel and exit stay within reach.
:::

Refused under Rule 16 and Article II. The command that prints the machine form is `zayn check pick.zayn --json`. Look at the machine form, at the list named `cites`: after the rule and the article it has a third entry, `pattern:select-silently-acts`. That is the pattern "Selection that silently executes" of the table above. The repair puts a confirmation between the choice and the act.

::: plate A confirmation between the two
```zayn pick.zayn
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR clerk
)
//--> clean
```
In words: A clerk selects an invoice, confirms, and it is paid.
:::

Clean. Four refusals, and the fourth takes a pattern's name to the tool that reads it.

## What I refused

**The law refuses a second use of a number.** Article VII ends on it: "Retired numbers are never reused." Two numbers that an earlier numbering had given to what are now Rules 82 and 83 are marked in the file with these words: "Reserved, never to be assigned". Under Article VII, a citation of Rule 79 names the same rule in every version of the law, and the rule's evidence says what changed in it.

**An amended rule keeps its number.** When Rule 116 was first amended, on 5 August 2026, the lineage wrote: "No new number: the same rule, stated whole." A rule that changes is the same rule, with its history in its evidence.

**No standard is cited before it is read.** A proposal of August 2026 asked that a rule name the standards that support it, and set its own condition. In my pass of 13 August, a sitting where I ruled the proposals one by one, I accepted it as work to do. The docket, the file where changes to the law are proposed and ruled, keeps the condition: "nothing is written into `rules.json`" until the editions of those standards are read and their clauses recorded.

**The law kept its role word.** The law says operator where this book says user. On 7 November 2026 I answered yes to six recommendations of the docket, and one was that the law's prose name its subject as the user, a person or an AI agent. The word operator was left in the rules and in the title of Article VI, and the docket says why: "it is the law's role word, not a description of a human". Its remedy is one sentence of the preamble, which, in the docket's words, "makes every use of it mean the user, a person or an agent".

[AUTHOR: the stake of this chapter, in your words: why the law had to be a file that tools read, and what you saw when it was prose.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the declarations of this page as the suite keeps them, each refused one beside its lawful twin. The suite proves the codes, the names of the kinds of finding. The citations are the contract's data, and I followed them into the law by hand.

## Where the field leads

The field leads on what stands behind a criterion. The criterion of the accessibility guidelines that chapter 8 read has a page of its own, which states its intent, and every criterion is "written as testable". Zayn's oldest rules share one line of evidence, and the rules that entered since version 2.1 each have their own.

Zayn's law leads on being read by tools. A count, a citation and a page all come from one file, so a rule's number means one thing wherever it is printed. The cost is beside the file: a text written by hand can differ from it, and Zayn's own ledger, the dated list of what the project found, says so in one line: "a number in prose is attached to nothing that can contradict it". This book takes the remedy that the same ledger gives: its counts of the law are read from the file at each build.

And the law's rules are equal in rank: when two speak of one subject they are reconciled, and chapter 18 tells one case.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Every table of this page was printed from the law's file at version {{n:law.version}}, and each citation on it comes from a run. What reads the file at that version is the verifier, for the titles and the numerals of a report; the law's reader, for its parts; the Zayn site, for its figures; and the pack, the set of files that a user of the law keeps together, each identified by a fingerprint of its bytes. The highest rule number in a right's list is {{n:right.max}}, and whether a newer rule joins a list is a question for a pass. The law in four layers is a design: a statute above, a core that every interface keeps, a commons that teams add to, and a local layer of their own.

## In your hands

Here is a printed ledger that promises an act. The `VIBE` says that the surface is paper. A printed page carries the verbs of finding and reading, `DISCOVER`, `UNDERSTAND`, `LOCATE`, `READ`, `SCAN` and `COMPARE`, and on paper every other verb is absent. Write the codes you expect, and how many, then open the verifier's answer under the plate.

::: plate For you: an approval, on paper
```zayn paper.zayn
DEFINE VIBE printed_record (
  SURFACE_AS print,
  MOTION none
)

DEFINE INTENT_FLOW approve_on_paper (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR auditor
)
//--> VERB_NOT_CARRIED approve_on_paper
//--> VERB_NOT_CARRIED approve_on_paper
//--> VERB_NOT_CARRIED approve_on_paper
//--> VERB_NOT_CARRIED approve_on_paper
```
In words: The surface is a printed page. On it an auditor acts, with undo, cancel and exit within reach.
:::

Four findings of one code: a printed page carries none of the four verbs this declaration names. A verb is one of the law's words for what a user does. The first repair that comes to mind is to change the act into reading. Say what you expect.

::: plate The act, changed into reading
```zayn paper.zayn
DEFINE VIBE printed_record (
  SURFACE_AS print,
  MOTION none
)

DEFINE INTENT_FLOW approve_on_paper (
  SATISFIES [READ],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR auditor
)
//--> VERB_NOT_CARRIED approve_on_paper
//--> VERB_NOT_CARRIED approve_on_paper
//--> VERB_NOT_CARRIED approve_on_paper
```
In words: On the printed page an auditor reads, with undo, cancel and exit within reach.
:::

Three stay: a page cannot keep within reach what it cannot carry. Go on until the verifier answers clean and every line of your file is true. Try before you read on.

::: plate What a printed ledger is for
```zayn paper.zayn
DEFINE VIBE printed_record (
  SURFACE_AS print,
  MOTION none
)

DEFINE INTENT_FLOW read_the_ledger (
  SATISFIES [READ, SCAN, COMPARE]
)
//--> clean
```
In words: On the printed page a user reads the ledger, scans it and compares its lines.
:::

Clean. Now do what this chapter did: take the report of this exercise's first plate, and follow its citation into the file. Try before you read on.

The report says Rule 82 and Article II, and names no right. In the file, Rule 82 derives from Article III, and the right to know lists it. A report prints the article that its kind of finding is bound to in the contract, which for most kinds is the article of the rule they cite. For this one the contract's note says why it cites Rule 82: that rule "is what made 'the declared medium' a legal concept". So is a refusal's article the article of its rule, or one of its own? The question is open, and it is filed as a remark for the law, with this book's requests to Zayn.

Rule 105's tier is one of {{n:law.tiers}} words. The next chapter reads them.
