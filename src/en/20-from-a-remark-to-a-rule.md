---
id: from-a-remark-to-a-rule
part: 8
number: 20
title: From a remark to a rule
stage:
  built: "a corpus of {{n:corpus.records}} corrections as data, each kept with its words, its date, its cause and whether its source names an earlier correction; records followed on this page to Rules 105, 106 and 112, and one of them to a refusal with its fixtures; the law's own dated lineage of each rule"
  designed: "a capture of a remark in every application, where it is made, with its surface, the intent it served and its medium; the design study's amendment that writes the loop into Article VII"
  next: "the capture carried by one real application, feeding a team's own law and the commons"
status: draft
research: research/ch20.md
fixtures: [decorative-animation, decorative-animation-lawful, menu-label-repeats-parent, menu-lawful]
---

A remark is what a person says about an interface in front of them: this is too small, this moved, I cannot tell what this button does. Zayn's law grows from such remarks, and its repository keeps them as data, in a corpus of corrections. Chapter 2 counted that corpus by cause, and chapters 18 and 19 followed one remark about a menu to a rule and its checks. In this chapter I show the practice under them: what a record keeps, how records are gathered, and where two records and one cause led. Then I show the loop as it is designed, a remark taken where it is made, in every application.

If you open the book here, a few words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of its report, a refusal when it is an error. **The record** is the files of Zayn's repository at the release this book reads.

## The field

The field writes its failures down, and it has forms for it.

Google's book on site reliability engineering gives one. In its words, "A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve it, the root cause(s), and the follow-up actions to prevent the incident from recurring." The book adds: "Blameless postmortems are a tenet of SRE culture."

A standard keeps its own errors. The page of errata of WCAG 2.2 opens: "This document records all known errors in the Web Content Accessibility Guidelines (WCAG) 2.2 specification." Its latest entries are dated 17 August 2026.

And a proposal keeps its dissent. Python's PEP 1 says that "A PEP is a design document providing information to the Python community", and that "The PEP author is responsible for building consensus within the community and documenting dissenting opinions."

The sources were read on 27 November 2026, and Appendix F lists them. So the field records an incident with its cause, an error of a standard, and a proposal with the voices against it.

## The principle

**A remark becomes evidence when it is kept with its words, its date, its place and its cause; a rule is written from that evidence.**

Article VII of the law, *Amendment*, sets the condition: "The law grows only from evidence: real usage, operator feedback, documented failure analysis." The corpus is that feedback, kept as data.

## What a record keeps

A record of the corpus is one correction. It keeps the same fields every time. There are the remark's words, what was wrong and what was required. There is the sense it touched, sight or touch or hearing, and its cause, the default that produced the defect. There are its date, the decision it led to, under `ruling`, and two marks.

The first mark is `verbatim`. My own words are kept with their typing, "typing kept" in the corpus page's words. A record whose source holds only a session's wording is a paraphrase, and the field says which. {{n:corpus.verbatim}} of the {{n:corpus.records}} records are my words, and a page that quotes me quotes those.

The second mark is `repeat`: "{{n:corpus.repeat}} of the {{n:corpus.records}} name an earlier correction of the same defect." The mark says what the record's source says: that this remark was made before. It is set by the source, and the record names the earlier one in its words where the source did.

The records were gathered by reading the files where remarks were made, in sweeps: "Four read-only sweeps on 2026-11-09, merged by hand, then classified by root cause", and further sweeps since. A remark found again in another file is listed under the first record, {{n:corpus.relays}} times in all, and counted once. And a row that looks like an answered remark, whose source does not quote or name the author, is kept apart: {{n:corpus.candidates}} such rows are "left out of every count".

## Two records and a cause

Here are two records and one cause, each followed from its words to where it led.

**The smooth scroll.** On 3 August 2026, a record notes, in its paraphrase, that "the reader scrolled smoothly when a set was chosen from its menu". What was wrong: "animation nobody asked for between a click and its answer". What was required: "motion only to report; the jump is instant". Two days later the law gained Rule 112, *Motion Reports, It Never Decorates*, which allows movement "only when it reports a change the operator caused and might otherwise miss". The rule reached the verifier. A `FEEDBACK` tells the user of a state; its `MOTION` names how it moves and its `REPORTS` the state it tells.

::: plate A menu choice that glides
```zayn reader.zayn
DEFINE FEEDBACK set_chosen (
  MOTION glide
)
//--> DECORATIVE_ANIMATION set_chosen
```
In words: When the user chooses a set from the menu, the page glides to it, and the glide tells of nothing.
:::

Refused: "Motion or feedback that reports no state." The finding cites Rule 112 by its number. The check reads three fields of a feedback: a `TONE` or a `MOTION` with nothing in `REPORTS` is refused, whatever the motion, and the names in `REPORTS` are taken as written. The operator, in the rule's words, is the law's word for its user. Here is the record's repair, as it asked.

::: plate A menu choice that jumps
```zayn reader.zayn
DEFINE FEEDBACK set_chosen (
  MOTION none,
  REPORTS [current_set]
)
//--> clean
```
In words: When the user chooses a set, the page jumps to it at once, and tells the user which set is current.
:::

Clean. The same defect came back on 22 September and on 1 October 2026, in other projects, after the rule existed; the records say so in their words, and both carry `repeat` false, because their sources name no earlier correction. The verifier refuses what a declaration states; in a project with no declaration, the rule is met on the painted page, by a person who reads it.

**The toggle.** On 15 October 2026 I wrote of a book's reader, where one button switched between two views and named the view it would open. My words, as the record keeps them: "this button is confusing, never use it like that, make the two states visible in sliding button or in a combo box." The docket, the file where changes to the law are proposed and ruled, found that Rule 106, *The Verb on the Button*, allowed the button as written, because its label began with a verb. So the rule was amended on 3 November: "A control with exactly two states shows both, as a segmented switch or a select". This record's path ends at the rule.

::: plate The two views of a reader
```zayn reader.zayn
DEFINE INTERACTION spine_toggle (
  SATISFIES [SELECT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: A control with which the user selects one of two views of a book, with undo within reach, and which says that its change can be taken back.
:::

Clean, because a declaration states what the user does, and the label on the button is the drawing's. The law files Rule 106 under `machine-later`, its word for a rule that a machine is to check once the instrument is built, and the rule's `lint` field, where the law names that instrument, is empty: a person reads the button.

**The size of type.** Of the corpus's causes, type comes back most often. The design study of Zayn's site says why. In its words, "20 of its 28 corrections name an earlier one, because a reading size is undone every time a template or a new project starts from the web's defaults." Rule 105, *The Legibility Floor*, asks that "Main reading text is at least 1rem", and the audit of the painted page reads every text against a floor of 16 pixels. The design study proposes, from those records, that "the floor becomes 18 px for every text". That amendment waits for my ruling.

So a record can lead to a refusal with fixtures, to a rule that a person reads, or to a proposal that waits. Each of the three is in the data.

## The records behind the rules

The law holds {{n:law.above104}} rules numbered above 104, and each carries its evidence. {{n:corpus.law_cited}} records of the corpus name one of them in their `ruling`. They name {{n:corpus.law_rules}} rules, Rules 105 to 116; the first evidence of each is a remark on the framework's own site. Rule 116 gathered five records over three months before its checks were written; chapter 19 follows it.

The other rules above 104 came from other evidence, and their evidence says which: the practice of a product of banking supervision, a decision of a sibling project, a measurement, a dashboard built by an AI agent session. The corpus is one source of the law among several, and each rule's own evidence names its source.

## The capture, designed

Today the records are gathered after the fact, by reading the files where remarks were made. *The Second Founding*, a proposal of the project for a new base of the law, which awaits my ruling, designs the loop from its first step:

> an operator meets a pain, in the app, at the moment it hurts
> capture: the surface, the intent it served, the medium it was in

From the capture, the loop runs to a local law binding on the team's own application, then to a proposal for the commons, then to a numbered rule. Its reason is one sentence: "The person who feels the pain has never had a channel to the person who decides." It adds a field that the corpus keeps today in free words: "Note the added field: **the medium** — without it the corpus would go on writing law for the eye." Chapter 21 tells the tiers that loop runs through.

## What I refused

**Remarks kept as evidence, not as rules.** In a pass of the docket in November, the site's remarks of 4 to 6 November were documented, each beside the rule it supports. The pass says: "Each remark below is documented as evidence; the rule it supports already says enough." It made six recommendations, and I ruled on 7 November: "yes to all six". The law gained evidence and one amendment, and no new number.

**A remark that became a check of the site and no rule.** On 6 November I said this of the site's tooltips: "avoid info bulles altogethor because they complexify the redaing by a volatile additional layer!" The site's guide to writing gained a rule of its own, and the site's build now refuses a tooltip in its pages. No rule of the law was written for it: the instrument that could hold it was the site's own build.

**The design study's amendments wait.** The study wrote its amendments from the corpus. One amends Article VII itself: "a correction enters the law as its cause, bounded on both sides, with a check on the painted result by default for every element". Its own rule holds them: "nothing here enters `rules.json` before that", before my ruling.

[AUTHOR: the stake of this chapter, in your words: the remark you made most often, and what it cost before it became a rule.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the records whose rules reached the verifier. A feedback that speaks and reports no state, refused, and its twin: Rule 112, from the smooth scroll. A menu whose child repeats its parent's label, refused, and a lawful menu: Rule 116, from the remarks on the site's menus.

## Where the field leads

The field leads in its channels. A standard takes comments and keeps errata in public; a postmortem is written by the team that met the incident; a proposal records the voices against it. Zayn's capture in every application is designed, and the plan of the project says: "One real app must carry it or the loop is theatre."

The field leads in its many voices. Its standards gather remarks from many people; the corpus is the record of one person's corrections, mine, across my projects. The proposal's commons is where other voices would enter.

Zayn leads in what a record keeps. The field records the error and the change to the text. The corpus keeps the remark under it, with its date, its cause and the rule it led to: in the words it was said in where the source kept them, and in a marked paraphrase where it did not. And the law keeps its own dated lineage in its file, so each of the {{n:corpus.law_rules}} rules the corpus names can be traced back to its remarks.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the corpus of {{n:corpus.records}} corrections as data, each with its words, its date, its cause, its two marks and the decision it led to. Two records and a cause followed on this page: to Rule 112 and its refusal, run here with its fixtures; to Rule 106, amended; to Rule 105 and the audit's floor. The law's lineage, dating each rule. Designed: the capture of a remark in every application, with its surface, its intent and its medium; the design study's amendment that writes the loop into Article VII. Next: the capture carried by one real application, feeding a team's own law and the commons.

So the loop runs today on records read after the fact. It has closed in days: the smooth scroll of 3 August became Rule 112 on 5 August, and the menu remark of 8 November had its checks the same day.

## In your hands

Here is a record of 1 October 2026, in its paraphrase: "decoration (gradients, glides, a covered photo) competed with the content". What it required: "no animation while navigating". A page arrives, and its author made it glide in. Write what you expect, then open the verifier's answer.

::: plate For you: the page that arrives
```zayn pages.zayn
DEFINE FEEDBACK page_arrives (
  TONE celebratory,
  MOTION glide
)
//--> DECORATIVE_ANIMATION page_arrives
```
In words: When a page arrives, it glides in, in a celebratory tone, and tells of nothing.
:::

Repair it, and say what you expect. Two lawful repairs follow. Try before you read on.

::: plate The page that arrives, as the record asked
```zayn pages.zayn
DEFINE FEEDBACK page_arrives (
  TONE informational,
  MOTION none,
  REPORTS [current_page]
)
//--> clean
```
In words: When a page arrives, it appears at once, and tells the user which page is current, in an informational tone.
:::

::: plate The page that still glides
```zayn pages.zayn
DEFINE FEEDBACK page_arrives (
  TONE informational,
  MOTION glide,
  REPORTS [current_page]
)
//--> clean
```
In words: When a page arrives, it glides in and tells the user which page is current.
:::

Both clean, and only the first is what the record asked. The verifier checks that a motion reports; Rule 112 lists "Fades, slides, and reveals when content arrives" among what it avoids, and a person judges the glide. Now write the record yourself, in the corpus's fields: the words, what was wrong, what was required, the sense, the cause. Would you mark it a repeat?

[AUTHOR: is the arriving page the defect you want the reader to repair here, or one from your own work?]

A remark that a team keeps becomes a rule of that team first. The next chapter takes the tiers a rule passes through: the team's own, the commons many teams share, and the core every one keeps.
