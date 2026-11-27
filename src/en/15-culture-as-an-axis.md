---
id: culture-as-an-axis
part: 6
number: 15
title: Culture as an axis
stage:
  built: "the law's data on culture, from my rulings of 13 August 2026: Rule 56's clause across cultures, with the condition under which it binds; Rule 64's list of what must not mirror; Rule 122 and the first cultural forbidden pattern; the language's refusal of a colour word where a meaning goes, run on this page"
  designed: "culture as the third axis of *The Second Founding*, put to my ruling: a reading per culture, for which the word `CONVENTION` is proposed; the path from a meaning to its rendering in each culture, on which Rule 56's clause waits; the reading contributed by those who live inside it"
  next: "the proposal's plan: the field of convention and the meeting of medium and culture, after my ruling and once the culture model is built"
status: draft
research: research/ch15.md
fixtures: [unknown-signal, unknown-signal-lawful, signal-unperceivable, signal-unperceivable-lawful]
---

Culture, as an axis of expression, is what a sign means to the person who receives it. Chapter 14 took culture in the law's first sense: a culture of interaction, the way one interface is drawn for its users, Modern or Retro. This chapter takes the reader's reading. A colour, a gesture, a flag mean different things to different readers, and a law for interfaces must say where that difference lives. I show where the law puts it today: the meaning in the declaration, the reading out of it. I show what the law already holds as data, and what *The Second Founding*, a proposal of the project for a new base of the law, designs for the rest.

If you open the book here, a few words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law, and a **finding** is one entry of its report, a refusal when it is an error. **The drawing** is what a medium shows of a declaration.

## The field

The field holds two parts of culture as standards: the direction of writing, and the forms of a locale.

Direction first. W3C's guidance on right-to-left text in HTML says: "Add `dir="rtl"` to the html tag any time the overall document direction is right-to-left (RTL)." And: "Never use CSS to apply the base direction." The direction is a fact of the document. CSS Logical Properties and Values is a W3C Working Draft of December 2025. It gives the means to lay a page out by direction: "These properties are writing-mode relative equivalents of their corresponding physical properties." And the Unicode Standard Annex #9, at Unicode 18.0.0, "describes the algorithm used to determine the directionality for bidirectional Unicode text", where Arabic or Hebrew meets digits and Latin.

A platform says what stays. Apple's Human Interface Guidelines, on right to left: "Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves." And of an icon: "clocks work the same everywhere, so a traditional clock interface icon needs to look the same regardless of language direction."

The forms of a locale come next. The Unicode CLDR project "supplies key information and structures critical for programs", because "Formatting dates, numbers, currencies, and units of measurement is far more complicated across different languages and regions than most people recognize."

The sources were read on 27 November 2026, and Appendix F lists them. So the field standardises the direction a page's text runs in, and how a date is written for a place.

## The principle

**A declaration fixes what a sign means; how a reader reads it belongs to the reader's culture, and some signs are never borrowed at all.**

The proposal adds culture as its third axis. In its words: "A stratum says what an expression does, a medium says where it is carried, and neither says what it *means to the person receiving it*." And it gives the reason in one sentence: "meaning is not a property of the sign. It is a property of the sign *and its reader*."

## Three questions about a sign

The proposal asks three questions of every expression. What does it do: that is its stratum, chapter 11. Where is it carried: that is its medium, Part V. What does it mean to the one who receives it: that is its culture. A status of danger is a signal: that is its stratum, the function it serves; it is carried in colour on a screen and in a tone in a speaker, the medium; and what that colour means to the one who sees it is the culture.

The law already speaks of language. Set 18, *Multilingualism & Dialects*, holds Rules 63, 64 and 122: labels that follow the business's own words, layouts that turn for a script written from right to left, and strings kept in a dictionary per language. The proposal names what the set leaves: "The law has language. It does not have culture."

The word itself is taken. In the law, Article VI uses "culture" for a culture of interaction, a vibe, which chapter 14 tells. The proposal keeps that sense and asks for another word for the reader's reading: "`CONVENTION` is proposed and the naming is the author's." The naming is mine, and the word waits for my ruling. In this chapter "culture" means the reader's reading, and I say so where the two senses meet.

## A meaning, never a reading

Here is the one place the language keeps a culture's reading out of a declaration. A `SCREEN` is a surface the user reads, and `SIGNALS` names the meanings its records carry, from the list of Rule 118: `success`, `warning`, `danger`, `info` and `muted`. Rule 118 splits the colours that speak of a record into two families: these five statuses, `muted` among them, and one quiet style for everything that carries no urgency, which a declaration leaves unmarked. A signal must serve something the user does: `SIGNALS` on a declaration that satisfies no intent is refused, `EXPRESSION_ORPHAN`, as chapter 11 shows. Here is a screen of credit limits, written by someone who reads green as good and red as bad.

::: plate Credit limits, in green and red
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE],
  SIGNALS [green, red]
)
//--> 2 UNKNOWN_SIGNAL credit_limits
```
In words: A screen where the user scans and compares credit limits, and its records are marked green and red.
:::

Refused twice: "A value in SIGNALS is not one of Rule 118's five semantic statuses." Green-for-good is one culture's reading of a colour, and the language has no place to write it. The repair names what each colour was for.

::: plate Credit limits, by meaning
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE],
  SIGNALS [success, danger]
)
//--> clean
```
In words: The same screen; a limit within bounds says success, "OK, valid, under control", and a limit exceeded says danger, "critical, exceeded, incident".
:::

Clean. The language's specification says where the colour went. In its words: "Which colour, timbre or waveform serves `danger` is the rendering's business, per medium and per culture." The project's plan for the axis states the same in its own words: the language is "already culture-safe on that axis by construction". A declaration cannot carry one culture's reading of a colour, because it cannot carry a colour.

## What the law holds

On 13 August 2026 I ruled twelve proposals of the docket in one pass, "Twelve items, twelve rulings", and three of them came from the proposal's section on culture. The docket is the file where changes to the law are proposed and ruled. The three are in the law's data today.

Rule 56 carries the meaning across audiences. Its solution now says that "what a declaration fixes is the meaning, and the rendering is derived per theme, per medium and per culture". I adopted it with a condition. The law states it: "The cultural clause binds once a meaning-to-rendering path exists to obey it." Its reason: "Meaning must survive theming and audience alike, or color was never a signal." The law files Rule 56 under `machine-later`, the tier of a rule whose instrument is to come.

Rule 64 turns a layout for a script written from right to left. Since that pass it says what does not turn: "What must NOT mirror: clocks, media transport controls, the digits within a number, and any progress that encodes a physical direction. Mirroring the layout axis is not mirroring the world." It prescribes the field's own means, "CSS Logical Properties", and its reason is the law's: "Calm that only flows left-to-right is not calm; it is locale bias."

Rule 122 keeps every string in a dictionary per language, so that adding a language means "adding a file and registering a locale, never touching code". Bound to it, the law's list of forbidden patterns gained its first cultural one: "A sovereign sign conscripted as a convenience label". A flag stands for a state, and a language is spoken across states; a menu of languages drawn as flags conscripts the one to label the other. The docket's drafting kept the line exact: "The wording must forbid conscription, not use." On a customs form, a flag is the right sign for a country of registration.

## Who decides

The verifier decides one thing on this axis: the colour word, refused on this page. The rest is judged by a person, or waits for its instrument, as Rule 56 does. The law files Rules 63, 64 and 122 under `judgment`, the tier where a person decides, and the forbidden pattern rests on Rule 122. Here is a menu of languages whose entries are labelled by flags. A `NAV_GRAPH` declares a menu entry, its `LABEL` and the surface it leads to.

::: plate A menu of languages, labelled by flags
```zayn languages.zayn
DEFINE NAV_GRAPH language_menu (
  SATISFIES [SELECT],
  ENTRIES [lang_fr, lang_ar]
)
DEFINE NAV_GRAPH lang_fr (LABEL "Flag of France", TARGET french_pages)
DEFINE NAV_GRAPH lang_ar (LABEL "Flag of Egypt", TARGET arabic_pages)
//--> clean
```
In words: A menu where the user selects a language; the entry for French is labelled by the flag of France, and the entry for Arabic by the flag of Egypt.
:::

Clean, and the law forbids it. The verifier reads a label as words, and the pattern is a matter of what the words stand for. A person reading the menu under Rule 122 refuses it; the lawful menu names each language in its own words, "Français" and "العربية". The declaration carries the label, and a person reads what it stands for.

The proposal separates the two kinds of case. A variance is a meaning that each culture renders its own way, and it can be written as a parameter: the proposal's example is red, for danger in one place and for prosperity in another. A hazard is a sign that must not be used as a label at all. No parameter makes it safe: "A sign that denotes sovereignty, faith or political identity must never be conscripted as a label for something else." Rule 56 serves the first. The forbidden pattern serves the second.

Where does a culture's reading come from? The proposal answers: "A locale formats. A culture interprets." A locale tells a program how a date is written in a place, and a reading of a sign must be contributed by the people who hold it. Part VIII tells the commons, the shared body of such contributions.

## What I refused

**I ruled three amendments from the proposal into the law, one with a condition.** On 13 August 2026 I adopted the cultural forbidden pattern, bound to Rule 122, and Rule 64's list of what must not mirror. I adopted Rule 56 across cultures too, effective once a path from a meaning to its rendering can serve it. The docket had advised the condition because the clause "obliges a derivation path that does not exist yet"; I ruled it so.

**The wider list of hazards waits for those who live inside it.** The docket filed one pattern and held the rest: "The wider hazard class (disputed borders and place names, religious symbols …) is real and is deliberately **not** drafted here. It needs review by people who live inside those readings."

**No closed list of cultures.** A reflection of the project on how the platform senses its user refuses one: "a closed set of five cultures would be both wrong and offensive". It turns the question to "whose reading governs" instead.

**No overloading of a word.** The proposal refuses to stretch Article VI's word over the reader's reading: "Quietly overloading Article VI's term would be the worst option." The word is held for my ruling.

[AUTHOR: the stake of this chapter, in your words: a reading of a sign you have seen read two ways, and why the law keeps the reading out of the declaration.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the refusal the language makes of a colour word. A word outside the five meanings, refused, and its twin, which names a meaning of the list. Beside them, a signal on a medium that cannot carry it, refused, and its twin: a meaning that a medium cannot carry is refused, and chapter 12 runs it. The rules of the reader's culture are judged by a person, and the suite holds no fixture for them.

## Where the field leads

The field leads in direction. Its markup sets a document's direction, its logical properties lay a page out by it, its annex orders text that mixes scripts, and its platforms list what turns and what stays. Rule 64 prescribes the field's logical properties and holds its own list under `judgment`, where a person reads it.

The field leads in locale data. CLDR gives programs the forms of dates, numbers and currencies for a place. The proposal's culture model, which would serve a reading as CLDR serves a format, is designed.

The record states the proposal's own reach: "The cultural claims in §4.6 are examples, not a survey", and it warns: "A chapter on culture written by one culture is the failure it warns about." This chapter tells its examples as the record's.

Zayn leads in what the declaration refuses to carry. A design token, in the field's format, is a name and a value; Zayn's language admits the meaning and refuses the colour, so no declaration fixes one culture's reading of a colour for all. And its law names a hazard that no parameter makes safe.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the law's data from my rulings of 13 August 2026. Rule 56's clause across cultures, with the condition under which it binds. Rule 64's list of what must not mirror. Rule 122 and the first cultural forbidden pattern. The verifier's refusal of a colour word where a meaning goes, run on this page. Designed: culture as the third axis of the proposal, put to my ruling. The word for the reader's reading, for which `CONVENTION` is proposed. The path from a meaning to its rendering in each culture, on which Rule 56's clause waits. Readings contributed by those who live inside them. Next: in the proposal's plan, the field of convention and the meeting of medium and culture, after my ruling and once the culture model is built.

So the declaration holds the meaning. The law holds Rules 56, 64 and 122 and one forbidden pattern as data; a person judges Rules 63, 64 and 122, and Rule 56 waits for its instrument. The reading itself is the designed part of the axis.

## In your hands

Here is a screen of a market's moves, written by someone who reached for the colours their own culture reads. Three findings wait in it. Write what you expect, then open the verifier's answer.

::: plate For you: the market's moves
```zayn markets.zayn
DEFINE SCREEN market_moves (
  SIGNALS [green, red]
)
//--> 2 UNKNOWN_SIGNAL market_moves
//--> EXPRESSION_ORPHAN market_moves
```
In words: A screen of a market's moves, its records marked green and red, and nothing said of what the user does there.
:::

Repair it, and say what you expect. Two lawful repairs follow, and they say different things. Try before you read on.

::: plate The moves, by status
```zayn markets.zayn
DEFINE SCREEN market_moves (
  SATISFIES [SCAN, COMPARE],
  SIGNALS [success, danger]
)
//--> clean
```
In words: The user scans and compares the market's moves; a move reads as success or as danger.
:::

::: plate The moves, without a status
```zayn markets.zayn
DEFINE SCREEN market_moves (
  SATISFIES [SCAN, COMPARE]
)
//--> clean
```
In words: The user scans and compares the market's moves, and the moves carry no status.
:::

Both clean. Is a price that rose a status, "OK, valid, under control", or a fact with no urgency, in Rule 118's quiet family, left unmarked? Rule 118 has a word for a limit exceeded and none for a gain. Whatever you declare, the colour that draws it is the rendering's, in each culture, once the path that Rule 56 waits for exists. Which is a rise, on your screen?

[AUTHOR: is the market's colours the defect you want the reader to repair here, or one from your own work?]

The reader's culture closes the part on who reads an interface. Part VII turns to the law itself, part by part.
