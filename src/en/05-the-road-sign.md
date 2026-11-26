---
id: the-road-sign
part: 2
number: 5
title: The road sign
stage:
  built: "the medium `signage` in Zayn's data, with the verbs a sign carries; the verifier's refusal of a verb a sign cannot carry, of a medium outside the list and of a meaning outside the five, run on this page"
  designed: "how a sign renders each of the five meanings; the statute tier, where an external standard outranks the constitution in a physical medium; the safety standards' support for Rule 118, commissioned and gated on reading their editions; rules written for the signage medium; what a medium carries computed from its properties, so that a new medium is classified by what it is"
  next: "the external standards of physical media read and cited before any rule for them is written"
status: draft
research: research/ch05.md
fixtures: [verb-not-carried, verb-not-carried-lawful, projection-print-promise, projection-print-promise-lawful, unknown-medium, unknown-medium-lawful, unknown-signal, unknown-signal-lawful]
---

The road sign is an interface held by law: a set of shapes, colours and symbols fixed by a treaty, which its parties bind themselves to use and amend together. A driver reads it at speed, in a country whose language they may not speak. In this chapter I read that treaty at its source and say what it carries. Then I show where Zayn makes the same move: a closed list of what a declaration may say, meanings assigned by rule, and a medium for signs, where the verifier refuses what a sign cannot do.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The road sign is an interface the field holds by treaty. The *Convention on Road Signs and Signals* was concluded at Vienna on 8 November 1968. It entered into force on 6 June 1978, and on the day of this book's reading the United Nations counted 75 parties and 35 signatories.

Its text fixes the classes of signs: danger warning signs, regulatory signs, which it divides into priority, prohibitory or restrictive, and mandatory signs, and informative signs. It closes its vocabulary where it speaks. Where the convention prescribes a sign for a rule, the parties undertake "not to use any other sign, symbol or marking for signifying that rule or conveying that information". Where it prescribes none, a party may use a sign of its own, provided that the sign "is not assigned a different meaning in this Convention" and conforms to the system. And the parties prohibit any board or device "which might be confused with signs".

It says why the system has that form. "In order to facilitate international understanding of signs", the system rests on "shapes and colours characteristic of each class of sign and, wherever possible, on the use of graphic symbols rather than inscriptions". A sign may carry words, but only "if this does not make the sign more difficult to understand for drivers who cannot understand the inscription".

And it says how the system changes. Any party may propose an amendment, "accompanied by an explanatory memorandum"; it is deemed accepted unless a third of the parties or more reject it or ask for a conference within twelve months. Parties may depart from the text "for experimental purposes and temporarily", "having regard to the usefulness of carrying out experiments before proposing amendments". The treaty's status page lists amendments from 1994 onward, among them a proposal of May 2025 and an acceptance of May 2026.

Each source was read on 25 November 2026, the text in the *United Nations Treaty Series*, and Appendix F lists them. So the field holds one interface whose signs are fixed in a text, chosen so that a stranger understands them, and changed by its parties on a memorandum and on experiment.

## The principle

**A vocabulary closed by law is one a stranger can learn once and read at speed, and one a program can check.**

The record's founding document for the platform, a design proposed for ratification, calls road signage "the most successful interface standard in human history". My outline of this book's second part describes it in one line: "a closed vocabulary, legislated by treaty, amended on crash evidence, working across languages and literacy for sixty years". The project's evidence ledger, the file that keeps each fact the project relies on with its source, marked that line unchecked clause by clause, and ruled: "Nothing marked `unverified` may be printed as fact without being checked first."

Read at its source, the treaty carries the line at this size. It is a closed vocabulary where it prescribes, and a system that every other sign must conform to. It is legislated by treaty, since 1968. It is amended by its parties, each proposal with a memorandum, and it allows experiments before amendments. It is built for international understanding, on shapes, colours and symbols, and it names the driver "who cannot understand the inscription". That is the move this book makes for interfaces, and the record makes it in data.

## A sign in Zayn's data

Zayn's data holds {{n:media.total}} media, the channels through which a declaration reaches a person, and one of them is `signage`, "Fixed physical marking". Its note in the data says what sets it apart from print: "Distinguished from print by election, not fixity: encountered rather than read, at distance and at speed, by someone who did not choose to read it." A medium carries the law's verbs, the closed list of {{n:law.verbs}} things a user can be doing, natively, at a cost, or not at all; at a cost means degraded, as when an act done in parallel becomes serial. Signage carries three natively: `LOCATE`, `DISCOVER` and `UNDERSTAND`. Every other verb is absent there, and only an absent verb raises a finding.

A declaration names its medium on a `VIBE`, the declaration of an interaction's culture, with the field `SURFACE_AS`. An `INTENT_FLOW` is the steps of one intent; its `SATISFIES` lists the verbs the user performs, and its `ALWAYS_REACHABLE` the verbs kept within reach at every step, such as `UNDO`, `CANCEL` and `EXIT`. Here is a sign in a building's lobby that promises to open the gate.

::: plate A lobby sign that promises to act
```zayn sign-acts.zayn
DEFINE VIBE lobby_sign (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW open_the_gate (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR visitor
)
//--> 4 VERB_NOT_CARRIED open_the_gate
```
In words: A sign in the lobby. Through it, a visitor opens the gate, with a way to undo, to cancel and to leave within reach.
:::

Four refusals, one for each verb a sign cannot carry: the act, and the three ways back it promised. Each cites Rule 82, *Perceivable State*, and Article II. The article on a finding's line is the diagnostic's own, set in the contract, and it can differ from the article the rule sits under: Rule 82 sits under Article III. The contract gives the reason for the rule: Rule 82 is "what made 'the declared medium' a legal concept", since a state must be perceivable in the medium the surface declares, and a promise the medium cannot carry is one the user can never perceive kept. The diagnostic, the kind of finding, states its invariant in the contract, the file that binds each kind of finding to the law: "A new medium adds renderings, never verbs." Here is the same sign, asked only what a sign does.

::: plate The same sign, asked what a sign does
```zayn sign-finds.zayn
DEFINE VIBE lobby_sign (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW find_the_gate (
  SATISFIES [DISCOVER, LOCATE, UNDERSTAND]
)
//--> clean
```
In words: A sign in the lobby. Through it, a visitor discovers the gate, locates it and understands where it is.
:::

Clean. A sign shows where the gate is; the gate's own control opens it.

::: plate A hazard placard that asks to be read
```zayn sign-read.zayn
DEFINE VIBE hazard_placard (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW warn_of_hazard (
  SATISFIES [UNDERSTAND, READ]
)
//--> VERB_NOT_CARRIED warn_of_hazard
```
In words: A placard at a hazard. A passer-by understands the hazard and reads about it.
:::

Refused for `READ`: a sign is encountered, and a paragraph on it is a defect. The founding document says it in one sentence: "A safety sign that requires reading a paragraph has failed; a printed report that requires reading a paragraph has not." Here is the same declaration on paper.

::: plate The same declaration on print
```zayn print-read.zayn
DEFINE VIBE hazard_notice (
  SURFACE_AS print
)

DEFINE INTENT_FLOW warn_of_hazard (
  SATISFIES [UNDERSTAND, READ]
)
//--> clean
```
In words: A printed notice of the hazard. A reader understands the hazard and reads about it.
:::

Clean. In this pair, the line between a sign and a printed page is one verb, `READ`; print also carries `SCAN` and `COMPARE`. One word of medium turns the verdict, and the word is checkable because the list of media and the verbs each carries are data.

## A list that admits no stranger

The treaty prohibits a device that might be confused with a sign. Zayn's list of media is closed in the same way: a medium outside it is refused, and the repair is to name one of the list.

::: plate A medium the list does not hold
```zayn road-medium.zayn
DEFINE VIBE junction_sign (
  SURFACE_AS road_sign
)
//--> UNKNOWN_MEDIUM junction_sign
```
In words: A sign at a junction, declared on a medium called a road sign.
:::

Refused: "SURFACE_AS names a medium outside the ten this language defines." The finding cites no rule, because it judges the language's words, not the law. The repair names a medium of the list.

::: plate The junction sign, on the list
```zayn road-medium.zayn
DEFINE VIBE junction_sign (
  SURFACE_AS signage
)
//--> clean
```
In words: The same sign, declared on the medium of signs.
:::

Clean.

The treaty gives each class of sign its colour and shape. Zayn gives a value five possible meanings, its semantic statuses: success, warning, danger, info and muted, from Rule 118, *Two Families of Colour*. A declaration names the meaning with `SIGNALS`, and in the specification's words it names "a meaning, never a colour". The colour that serves danger belongs to the rendering, medium by medium.

::: plate A placard that carries danger
```zayn sign-signals.zayn
DEFINE VIBE hazard_placard (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW warn_of_hazard (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [danger]
)
//--> clean
```
In words: A placard at a hazard. A passer-by discovers it and understands it, and it signals danger.
:::

Clean, and the verdict judges the word. The verifier judges whether a status can be perceived in a medium whose rendering the data records; of signage the data says that it carries the signal "in principle", and its rendering is at the design stage. So on a sign the verifier checks the meaning as a word of the list and decides nothing about how it is perceived; how a sign draws danger is the design that comes next. A word from outside the list is refused.

::: plate A meaning the list does not hold
```zayn sign-critical.zayn
DEFINE VIBE hazard_placard (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW warn_of_hazard (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [critical]
)
//--> UNKNOWN_SIGNAL warn_of_hazard
```
In words: The same placard, signalling a meaning called critical.
:::

Refused under Rule 118: "A value in SIGNALS is not one of Rule 118's five semantic statuses." A sixth meaning is an amendment of the law, as a new sign is an amendment of the treaty.

## What I refused

**I refused to write the safety standards into the law before their editions are read.** The docket is the record's book of proposed changes to the law, each with its ruling. The founding document holds that the standards for machine indicators and safety signs give colours settled meanings close to Rule 118's five. It proposes to record that support in the rule. On 13 August 2026 I ruled on the proposal, in the docket's words: "Adopted as a commission — the review is authorized; nothing is written into `rules.json` until the IEC 60073 / ISO 3864 / ISO 7010 editions are read and clauses recorded". The founding document had set the same discipline for itself: "Nothing in this project may cite a statute it has not read."

**The record keeps the rules for the signage medium in waiting.** On 3 November 2026 I delegated a pass with the words "close all the pending points on my behalf". In it the docket held rules for five media, signage among them, and the design study of those media, a design document of the record, keeps their text in waiting "until a product that ships in one is named".

**A declaration names no colour and no shape.** The specification says it: "No `WIDGET`, no layout, no colour"; `SIGNALS` names the meaning a rendering must carry, "and never the rendering". A road sign's shape is the treaty's to fix; in Zayn, the meaning is the declaration's, and the shape belongs to the medium's rendering.

[AUTHOR: the stake of this chapter, in your words: why road signage is the proof that a law for interfaces is possible, and what you saw in it.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, proves each closed list this chapter runs. A verb a medium cannot carry is refused, and its twin made lawful: the fixture asks print for a promise it cannot keep, the same refusal this page asked of a sign. A projection to print that promises a way back is refused, and its twin keeps to what paper carries. A medium outside the list is refused, and its twin names one of the list. A meaning outside the five is refused, and its twin takes one of them.

## Where the field leads

The field leads in the reach of its law. The treaty binds 75 parties, and each party undertakes to use the sign it prescribes for that rule. Zayn's law binds whoever adopts it; its edition is pinned by hash, and its author rules its amendments on evidence: a correction made to a real interface, recorded with its date, as chapter 18 tells.

The field leads in what a standard may impose. The founding document designs a tier above the constitution for physical media: "In physical media, the external standard outranks this constitution", and the court's duty there is "to *refuse a conflict*, never to resolve it in our favour". That tier is designed, and the verifier today reads the medium's verbs.

And a closed list has its cost, which the founding document names: "lists go stale — the next channel always arrives". Zayn's data already records six properties for each medium: persistence, seriality, election, bandwidth, mutability and retractability. The founding document designs the next step, what a medium carries computed from those properties, so that a new medium "is classified rather than argued about".

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the medium `signage` in Zayn's data, with its properties and the three verbs it carries. The verifier's refusal of a verb a sign cannot carry, in what a declaration satisfies and in what it keeps within reach; its refusal of a medium outside the list and of a meaning outside the five: all run on this page. Designed: how a sign renders each of the five meanings, and the statute tier, where an external standard outranks the constitution in a physical medium. Also designed: the safety standards' support for Rule 118, commissioned on 13 August 2026 and gated on reading their editions; rules written for the signage medium; and what a medium carries computed from its properties. Next: the external standards of physical media read and cited before any rule for them is written.

## In your hands

Here is a sign in a stairwell that shows the way out, and its declaration promises that leaving stays within reach. Write what you expect the verifier to answer, then open its answer.

::: plate For you: the exit sign
```zayn exit-sign.zayn
DEFINE VIBE stairwell_sign (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW way_out (
  SATISFIES [DISCOVER, LOCATE],
  ALWAYS_REACHABLE [EXIT]
)
//--> VERB_NOT_CARRIED way_out
```
In words: A sign in a stairwell. Through it, a person discovers the way out and locates it, and leaving stays within reach.
:::

Repair it, and say what you expect. Try before you read on.

::: plate The exit sign, repaired
```zayn exit-sign.zayn
DEFINE VIBE stairwell_sign (
  SURFACE_AS signage
)

DEFINE INTENT_FLOW way_out (
  SATISFIES [DISCOVER, LOCATE]
)
//--> clean
```
In words: A sign in a stairwell. Through it, a person discovers the way out and locates it.
:::

Clean. `EXIT` is the user's intent to leave a flow, and a sign that shows the way out serves `LOCATE`: the word on the sign and the verb of the law are two things. The law guards the way out on every surface that acts, and a sign points to it.

The next part turns from the heritage to the inversion: a declaration of intent comes first, and the interface follows it.
