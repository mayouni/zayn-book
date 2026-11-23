---
id: the-constitution-part-by-part
part: 7
number: 16
title: The constitution, part by part
stage:
  built: "the law as one data file at version {{n:law.version}}: a preamble, {{n:law.articles}} articles, {{n:law.rights}} rights, {{n:law.forbidden}} forbidden patterns and {{n:law.sets}} sets of {{n:law.rules}} rules; citations made of the file's own numbers and names, run on this page; a page that shows the whole law, drawn from the file; the file held by its hash in a pack of {{n:pack.files}} files"
  designed: "a law in four parts, from a core that every interface keeps to a commons that teams add to; a field on a rule that records the sources which corroborate it"
  next: "the law served to AI tools as they work, and rules moved to an instrument as each instrument is built"
status: draft
research: research/ch16.md
fixtures: [missing-undo, missing-undo-lawful, trapped-flow, trapped-flow-lawful, signal-unperceivable, signal-unperceivable-lawful, select-act-collapse, select-act-lawful, verb-not-carried, verb-not-carried-lawful]
---

The constitution of Zayn is one file. In this chapter I open that file and read it part by part: what it says of itself, its articles, its sets, one rule field by field, the rights of the user and the rules that enforce each, the patterns it forbids. Then I make the verifier refuse three declarations, and I follow each citation back into the file.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution for interfaces. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field writes its rules as documents, in layers. The Web Content Accessibility Guidelines are organised around "four principles", with "a total of 13 guidelines" under them, and under each guideline come success criteria, numbered like 3.3.4 and "written as testable criteria". A classic of the field is a list: ten heuristics of usability, each a name and a paragraph, which their page calls "broad rules of thumb".

For the people who test a page, the ACT Rules Format says what a test rule must state. Two of its parts are the applicability, "what parts of the test subject are tested", and the expectations, each of which is "an assertion about a test target".

And the field keeps some of its decisions as data. The Design Tokens format defines a token as information with "a human readable name": a colour, a dimension, a typeface. Those are values of the drawing.

So the field has documents in layers, lists of advice, a format for a rule that a tester runs, and data for the values of a drawing. Each source was read on 21 or 23 November 2026, and Appendix F lists them.

## The principle

**The law is one file: the page that shows it, the count that sizes it and the refusal that cites it all read it there.**

The file is named `rules.json`. It is written in a notation for data, names and values between braces, and a designer reads the law on a page that is drawn from it, never in the notation. The verifier reads the same file at each run: the title of a rule and the numeral of an article in a report are looked up there. Every count on this page is read from it by the book's build. Appendix A prints it in full.

## What the file says of itself

The file opens on its title, its version and its lineage, the dated list of its changes that chapter 18 reads. Then comes a preamble. It says what the law is for: "non-negotiable principles for business interfaces", which it wants "framework-agnostic, trend-resistant, and machine-checkable". It names its subject once: "the operator and the user name whoever acts through an interface: the user, a person or an agent". And it closes on four sentences, of which the last is "Undo is dignity."

The word philosophy names two things in the file. One is a line of four phrases, each of the form "X Over Y": calm over power, intent over mechanics, visible over hidden, business over technology. {{n:law.axioms}} of the articles carry one of them as their axiom. The other is a part of {{n:law.principles}} principles, which stand before the articles and outside the count of rules.

## The articles

An article is a sentence of principle, and every rule derives from one article: each of the {{n:rule.derived}} rules names it in a field, `derived_from`. Here are the articles, with the number of rules that derive from each.

{{articles}}

The counts are uneven, and that is information. Most rules protect calm, visible state and the culture of the people who use an interface. Reversibility needs few rules, and the article on amendment fewest of all.

## The sets, by subject

A set is a subject: menus, forms, accessibility, time. The file holds {{n:law.sets}} of them.

{{sets}}

Read the last column. A set's numbers are not a range, because a number is given once, in the order in which rules entered the law, and a rule goes to the set of its subject. The rules are numbered up to {{n:law.highest}} and the law holds {{n:law.rules}}: {{n:law.unused}} numbers are out of use, and the file lists them with what became of each.

## One rule, field by field

Every rule has the same shape. Here is Rule 105, whole, as the file holds it.

{{anatomy:105}}

{{n:rule.fields.all}} fields are on every rule. `id` is a handle, and `number` is what a citation carries. `title` is the name printed after the number in a report. `avoid` is a list of defects, and `solution` is the text of the rule: together they make a rule something a reviewer can decide, yes or no. `why` is the reason in a sentence or two. `derived_from` is the article. `enforcement` is one of four words, the rule's tier, and chapter 17 is about them. `evidence` says what earned the rule its number; the site in Rule 105's evidence is the one that carried the law at the time.

{{n:rule.fields.some}} fields are on some rules. `invariant` is a mark, the value `true`, on {{n:rule.invariant}} rules: the page that shows the law prints it as the badge "vibe-invariant", and Article VI uses the same word of rights: "Vibe-invariant rights never flex." A vibe is a culture of interaction, and chapter 15 is about it. `lint` is a sentence that names a check or an instrument, on {{n:rule.lint}} rules. `vibes` holds a note for one culture or another, on {{n:rule.vibes}}. `see_also` points at a neighbouring rule, on {{n:rule.see_also}}. `absorbs` names the retired number that a rule took in, on {{n:rule.absorbs}}.

## The rights, and their rules

A right is a sentence about the user, and it lists the rules that enforce it.

{{rights}}

A refusal can cite a right: {{n:diag.cite_right}} of the {{n:diag.total}} kinds of finding do. Here is a flow that posts an entry to a ledger.

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

Refused! Read the third line of the report: a rule, an article, a right. Now follow each into the file. Rule 79 is the rule whose `number` is 79, in set 26. Its `derived_from` says `reversibility`, and that is the name of Article IV. And the right to reverse lists 79 among the rules that enforce it.

{{right:reverse}}

Nothing in that line was typed into the verifier. The contract, which is the data file that binds each kind of finding to the law, says which rule, article and right this kind cites; the title and the numeral come from the law's file at the run. The repair is one word.

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

Refused, and the citation names two rules: Rule 51 and Rule 53, both derived from Article II, and both in the list of the right to leave. One finding may cite several rules.

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

Clean. A third, under Article III and the right to know. A `VIBE` declares the culture of a surface, and here the surface is heard: a queue monitor that speaks.

::: plate A status that a listener cannot hear
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
In words: The surface is heard. On the queue monitor a user discovers and understands the queue, and its values carry one status: muted.
:::

Refused: Rule 82, Article III, the right to know. On a surface that is heard, the status `muted` is rendered as silence, and a silence tells a listener nothing. The repair gives the surface a status that the medium can carry.

::: plate A status the medium carries
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
In words: The same monitor, and its values now carry two statuses: muted and danger.
:::

Clean. Three refusals, three articles, three rights, and each word of each citation is a name or a number that the file holds.

## The patterns the law forbids

The law also names what it forbids, in the words a designer already uses for it. A forbidden pattern is a title and the rules it breaks.

{{forbidden}}

A few kinds of finding are bound to a pattern. The report that a person reads prints the rule, the article and the right. The pattern travels in the machine form, the same answer written as data for a tool. Here is a flow where choosing a row carries out the act, with both forms.

::: plate Selecting is acting
```zayn pick.zayn envelope
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR operator
)
//--> SELECT_ACT_COLLAPSE pick_and_pay
```
In words: An operator selects an invoice and it is paid. Undo, cancel and exit stay within reach.
:::

Refused under Rule 16 and Article II. Look at the machine form, at the list named `cites`: after the rule and the article it holds a third entry, `pattern:select-silently-acts`. That is the pattern "Selection that silently executes" of the table above. The repair puts a confirmation between the choice and the act.

::: plate A confirmation between the two
```zayn pick.zayn
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR operator
)
//--> clean
```
In words: An operator selects an invoice, confirms, and it is paid.
:::

Clean.

## What I refused

**The law refuses a second use of a number.** Article VII ends on it: "Retired numbers are never reused." Two numbers that an earlier numbering had used for other things are marked in the file with these words: "Reserved, never to be assigned". A citation of Rule 79 names the same rule in every version of the law.

**An amended rule keeps its number.** When Rule 116 was first amended, on 5 August 2026, the lineage wrote: "No new number: the same rule, stated whole." A rule that changes is the same rule, with its history in its evidence.

**I refused to cite a standard before reading it.** In my pass of 13 August 2026 a proposal asked to add to a rule the standards that corroborate it. I adopted it as a commission, and the docket, the file where changes to the law are ruled, keeps the condition: "nothing is written into `rules.json`" until the editions of those standards are read and their clauses recorded.

**I kept the law's role word.** The law says operator where this book says user. On 7 November 2026 I ruled that the law's prose names its subject as the user, a person or an agent. The word operator stayed in the rules and in the title of Article VI, and the docket says why: "it is the law's role word, not a description of a human". One definition in the preamble now makes every use of it mean the user.

[AUTHOR: the stake of this chapter, in your words: why the law had to be a file that tools read, and what you saw when it was prose.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the declarations of this page as the suite keeps them, each refused one beside its lawful twin. The suite proves the codes. The citations are the contract's data, and this page followed them into the law by hand.

## Where the field leads

The field leads on what stands behind a criterion. The criterion read for chapter 8 has a page of its own, which states its intent, and every criterion is "written as testable". Zayn's oldest rules share one line of evidence, and the rules canonized since version 2.1 each carry their own event.

Zayn's law leads on being read by tools. A count, a citation and a page all come from one file, so a rule's number means one thing wherever it is printed. The cost is on the other side of the file: a text written by hand beside it can differ from it, and the ledger, the dated list of what the project found, says so in one line: "a number in prose is attached to nothing that can contradict it". This book takes the remedy that the ledger gives: its counts are read from the file at each build.

And a list has no order of rank. Two rules can speak of one subject, and chapter 18 tells how one such pair was reconciled.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Every table of this page was printed from the law's file at version {{n:law.version}}, and every citation was run. What reads the file at that version is the verifier, for the titles and the numerals of a report; the page that shows the law, for every part; the site, for its figures; and the pack, for the hash. The rights' lists name rules up to number 102, and whether a newer rule joins a list is a question for a pass, a sitting where changes to the law are ruled. A report prints the article that its kind of finding is bound to, which for most is the article of the rule it cites.

## In your hands

Here is a printed ledger that promises an act. The `VIBE` says that the surface is paper.

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

Cover the report under the declaration, write the codes you expect and how many, then compare. Four findings of one code: a printed page carries none of the four verbs. The first repair most readers try is to change the act into reading. Say what you expect.

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

Clean. Now do what this chapter did: follow the citation of the first report into the file. The report says Rule 82 and Article II, and names no right. In the file, Rule 82 derives from Article III, and the right to know lists it. So when a refusal cites a rule, does it answer to that rule's article and to the right the rule serves, or to an article of its own? The contract binds this kind of finding to Article II, and its note says why it cites Rule 82: that rule "is what made 'the declared medium' a legal concept". It is a remark for the law, filed with the book's findings.

A rule's card names its tier in one word. The next chapter reads those four words, and counts which rules an instrument refuses.
