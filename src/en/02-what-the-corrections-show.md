---
id: what-the-corrections-show
part: 1
number: 2
title: What the corrections show
stage:
  built: "the corpus of {{n:corpus.records}} corrections as data, each filed under the cause that produced it, and its page rendered from the data; the verifier's refusal of two of its defects, run on this page; the checks of the painted page written from the Zayn site's corrections, with their recorded runs"
  designed: "the design study's amendments to the law, written from the corpus and held for the author's ruling"
  next: "the law served to an AI model while it generates, so that a generator consults the rules before it draws"
status: draft
research: research/ch02.md
fixtures: [decorative-animation, decorative-animation-lawful, invisible-state, menu-label-duplicate, menu-lawful]
---

A correction is a remark a person makes about an interface: this text is too small, this space is empty, this button does something no one asked for. In this chapter I read {{n:corpus.records}} of mine as one body of data. I count them, and I file each under the default of the generator that produced it. Then I follow three chains in which a repair moved a defect instead of stopping it, and I show what changes when a correction becomes a rule and a check.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution for interfaces, kept as a data file. The **verifier** is the program that checks a declaration against the law. A **generator** is a program that writes interfaces, and today it is often an AI model.

## The field

The field has its own ways of finding defects in an interface. Its heuristics of usability are, in their page's words, "broad rules of thumb", applied by a reviewer. Its testing engines measure the painted page, the interface as a browser draws it: axe-core says that it finds "on average 57% of WCAG issues automatically", by its own count, and returns what it cannot decide as "incomplete" where "manual review is needed". And W3C says of every tool: "no tool alone can determine if a site meets accessibility standards".

Each source was read on 21 or 23 November 2026, and Appendix F lists them. So the field finds defects by review and by measure, one page at a time, and it keeps the person in the loop.

## The principle

**A defect that comes back is a default of the generator, and it stays away only where a rule names the default and an instrument checks every case.**

Zayn's design study, written from the corpus, says what a cause is: "A root cause is the default that produced the defect: the thing the generator does when nothing stops it." A remark corrects a page. A default writes the next one.

## The corpus, counted

The corpus is one data file, and a page of Zayn's repository is rendered from it. It holds {{n:corpus.records}} corrections of something a person sees, touches or hears, made in {{n:corpus.projects}} projects. Each record has the person's words, the page or file, the date, what was wrong, what was asked, and the cause. {{n:corpus.verbatim}} keep my words as I typed them. {{n:corpus.repeat}} name an earlier correction of the same defect, and {{n:corpus.verbatim_repeat}} do both. On one day alone, 9 November 2026, I made {{n:corpus.oneday}}.

The words say it before the counts do. "I told you a thousand times", on text set too small, in September. And on 9 November at half past three: "the same issue of text and space and bad line cuts AGAIN and AGAIN and AGAIN!!!!!!!!!!"

Each correction is filed under a cause, and each cause is a default. The design study names them: type sized for the web and not for reading, a box that takes its container's width, emphasis added to every element, a line broken wherever the width ends. Here are the causes, in their groups, counted from the data.

{{causes}}

Read the last column against the third. Where a cause comes back most, a person's eye judged first: the size of type, the width of a block, the balance of a line. These are the defaults a generator carries from the interfaces it learned from. On 15 August 2026 I said it to an AI model, as the corpus keeps my words: "This is the power of dogmatic influence you got from your training data."

## Three chains

A chain is a defect that a repair moved somewhere else. Here are three, each on the record with its date.

**The hero panel of the Zayn site, 5 November 2026.** The first remark: "the space to the right is not necessary! Space is a functional communication tool that we must use with care". The repair made the panel a tall, narrow box. The second remark: "I'm tired of talking to you of visual equlibrium! the hero zone must be rectangyular and you have space : put the title on one line and strech the text to the right!" The next repair stretched the box over the photograph. The third: "npw it is so larg and hides the door!" Three remarks, one defect, three places.

**A news-watching site of the estate, 9 November 2026.** At a quarter to one: "use the wider space of the page ... we are in a sort of workstation site, not a tight textual web site". The repair stretched the cards. At one o'clock: "making best use of the space does not mean creating divs as large as this making the text hardly readable". Each correction had one bound, and the repair went past it on the other side.

**The photograph of the Zayn site, 14 November 2026.** A review that I had asked for moved the photograph of the front page off its first screen. My remark: "(b) I never asked you to remove the photo or to move it in the bottom of ther page!!!!" That remark became a check of the painted page, K32, which fails when the front page's first screen paints no photograph. Its first recorded find was in the audit itself, and the audit's code says so: "found by K32 and K33 on the front page, 2026-11-15".

The design study puts the three chains in one sentence: "A correction stored as a symptom does not stop the defect; it moves it."

## A correction, as a declaration

Some corrections can be stated as a declaration, and then the verifier refuses them before anything is drawn. Smooth scrolling is one: a page that glides to its place when a user picks a section from its menu. I corrected it on 3 August 2026, and Rule 112 entered the law two days later with smooth scrolling first in its list of what to avoid. It was corrected again in two other projects, on 22 September and 1 October. A `VIBE` is the kind of declaration that states a culture of interaction, and its field `MOTION` says how the surface moves.

::: plate A reader that glides
```zayn reader.zayn
DEFINE VIBE reader_culture (
  SURFACE_AS visual,
  MOTION smooth_scroll
)
//--> DECORATIVE_ANIMATION reader_culture
```
In words: On a screen, the reader moves by smooth scrolling.
:::

Refused, under Rule 112: motion that reports nothing is decoration. The record's own repair is that "the jump is instant".

::: plate A reader that jumps
```zayn reader.zayn
DEFINE VIBE reader_culture (
  SURFACE_AS visual,
  MOTION none
)
//--> clean
```
In words: On a screen, the reader does not move: a choice jumps to its place.
:::

Clean. A filter the user cannot see is another. On 24 October 2026, in an organisation-chart editor of the estate, an active filter left nothing on the screen to say it was active, and it was corrected twice that day, the second time after my third look. At level 3 the verifier is given what the system holds, its state, in a small file, and checks that a surface shows it.

::: plate A chart with a filter it does not show
```zayn chart.zayn level=3 symbols=chart.json
DEFINE SCREEN people_chart (
  SATISFIES [LOCATE, SCAN]
)
//--> INVISIBLE_STATE active_filter
```
In words: On the chart, a user goes to a person and scans the chart. The system holds an active filter.

```symbols chart.json
{
  "state": ["active_filter"]
}
```
:::

Refused, under Rule 82 and the right to know. The repair declares that the chart shows the filter.

::: plate A chart that shows its filter
```zayn chart.zayn level=3 symbols=chart.json
DEFINE SCREEN people_chart (
  SATISFIES [LOCATE, SCAN],
  VISIBLE_STATE [active_filter]
)
//--> clean
```
In words: The same chart, and it shows the active filter.
:::

Clean. Other corrections belong to a person. On 10 November 2026 I wrote of the Zayn site's menu: "Use and Try are very simular lettting the navigation be cofusing." A `NAV_GRAPH` states an entry of a menu, and its `LABEL` is the name the menu shows.

::: plate Two labels a reader confuses
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [use, try]
)

DEFINE NAV_GRAPH use (LABEL "Use", TARGET use_home)
DEFINE NAV_GRAPH try (LABEL "Try", TARGET try_home)
//--> clean
```
In words: The main menu shows two entries, Use and Try.
:::

Clean. The verifier refuses two entries that carry one label, and two labels that a reader confuses are a person's to judge. So the corpus holds three kinds of correction: those a declaration can state, those a measure of the painted page can read, and those a person reads.

## The site, corrected under its own law

The Zayn site was built by AI models under the law it publishes, and I corrected it remark by remark. On 5 November 2026 I asked that every remark be kept: "ALL THSE REMARKS MUST BE DOCUMENTED TO BE INCLUDED IN THE CONSTITUION". Each remark of that pass went into the docket, the file where changes to the law are ruled, with its defect, its repair and the check that now holds it.

The checks of the painted page grew from those remarks. The audit, a page of Zayn's repository that measures another page in a browser, has numbered checks, and each of the later ones names the remark or the ruling it was written for. The design system records two full runs of them on the site, before and after its stylesheet changed: "38 pages, five widths, both cultures: 380 renders each", read on 10 November 2026. And it records what no check replaces: "No counter can say the site reads well; the Principal looks at it in both cultures". The Principal is the record's word for me.

## What I refused

**A correction that the law already holds is not a new rule.** On 15 August 2026 two of five candidates were refused as new law, and the docket gives the line: "The author's correction and Rule 113 are the same law, reached twice."

**The corpus refuses a record that does not name or quote me.** Such records are kept apart, and the corpus says why: "their source does not name or quote the Principal, so they are kept here and left out of every count".

**The design study refuses a check written as a list of kinds.** A check that covers the kinds of element someone thought of lets the defect back on the next kind, and the study asks of every check that it read "the painted page, by default, for every element".

**The design study's amendments wait for my ruling.** Its proposals to the law are written from the corpus, and its own line is: "nothing here enters `rules.json` before that".

[AUTHOR: the stake of this chapter, in your words: what the corrections cost you, and what a team gains when its corrections become data.]

## The court

The court of a chapter is what proves it. In this chapter it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below hold the corrections that this page states as declarations: motion that reports nothing, with its twin; a state the system holds and no surface shows; and the menu's labels, refused when two entries share one and clean when each has its own.

## Where the field leads

The field leads on the person. Its heuristics are applied by a reviewer, and its engines leave to a person what they cannot decide. The corpus agrees: its corrections are a person's, and the design study keeps a person's look as the last check of the site.

The field leads on measuring the painted page, where most of these defects are seen. The ledger, the dated list of what the project found, records a test of 12 August 2026: two payment surfaces "differing by seven broken laws" were the same declaration, and both ran clean. The answer of the record is the audit of the painted page, whose later checks were each written from a remark.

Zayn leads on keeping the corrections as data. Each one has its words, its date and its cause, so a team can count which default comes back, write the rule that names it, and check every case.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The corpus is data, and every count of this page is read from it at each build; its page in Zayn's repository is rendered from the same file. The verifier refused, on this page, two defects that the corpus records. The checks of the painted page are tools of the repository, and their runs are told here as recorded. The design study's amendments, written from the corpus, wait for my ruling before any of them enters the law.

## In your hands

Here is a stop button on the control panel of a local server of the estate, as first built. Two corrections fell on it on 22 August 2026: the stop killed the panel, leaving nothing to start again, and the browser's own confirmation box asked before it did. Write the findings you expect, by their codes, then open the verifier's answer.

::: plate For you: a stop button
```zayn server.zayn
DEFINE INTERACTION stop_server (
  SATISFIES [CONFIRM, ACT],
  ACTOR operator
)
//--> MISSING_UNDO stop_server
//--> ROLE_UNDECLARED
```
In words: An operator confirms, and the server stops.
:::

A refusal and a warning: the act has no way back, and the control states no promise. One word silences the refusal. Write `ROLE irreversible`, and say what you expect.

::: plate The word that silences the refusal
```zayn server.zayn
DEFINE INTERACTION stop_server (
  SATISFIES [CONFIRM, ACT],
  ROLE irreversible,
  ACTOR operator
)
//--> clean
```
In words: An operator confirms, the server stops, and the control says that this cannot be taken back.
:::

Clean, and untrue: the correction asked that the server can be started again. Write the form the record asks for. Try before you read on.

::: plate A stop that can be undone
```zayn server.zayn
DEFINE INTERACTION stop_server (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible,
  ACTOR operator
)
//--> clean
```
In words: An operator stops the server, and can start it again: the control says that the stop can be taken back.
:::

Clean, and true. Starting again is the undo, and the confirmation is gone: Rule 79 keeps confirmation for acts that cannot be undone. The verifier accepted the untrue form as well. Which form is true is a fact of the server, and a person reads it.

The corrections show what a generator does when nothing stops it. Part II reads what the field wrote to stop it.
