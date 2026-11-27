---
id: two-cultures-one-law
part: 6
number: 14
title: Two cultures, one law
stage:
  built: "Article VI and the declaration `VIBE`, with the verifier's refusal of a culture that hides a way back that another declaration keeps within reach, run on this page; the Zayn site's two cultures, Modern and Retro, each setting {{n:culture.tokens}} of the stylesheet's named values, chosen by the reader and drawn before the first paint; the exhibit that draws one screen in both at once; the audit of the painted page in both cultures; Set 18 and the forbidden pattern bound to Rule 122, read by a person"
  designed: "a culture's vocabulary of interaction, Retro keyboard-first with instant feedback and Modern pointer-first; a rule that a culture owns every default of its controls; culture as the reader's reading, chapter 15"
  next: "the reading of a sign per culture, chapter 15's axis"
status: draft
research: research/ch14.md
fixtures: [vibe-strips-right, clean-full, field-misplaced, field-misplaced-lawful]
---

An interaction culture is the way one interface presents itself to a community of users: its colours, its type, its density, its pace. The law calls it a vibe. In this chapter I show the two cultures the Zayn site is drawn in, Modern and Retro, and what the law lets each change. Then I declare two cultures over one flow, run them, and make one of them hide a way back the flow promised. Last, I name the law a reader's language keeps.

If you open the book here, a few words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law, and a **finding** is one entry of its report, a refusal when it is an error. **The drawing** is what a medium shows of a declaration, and the painted page is the drawing in a browser.

## The field

The field draws one page in more than one way, and it names the switch.

Media Queries Level 5 is a W3C Working Draft of February 2026. It defines a feature a page reads: "The prefers-color-scheme media feature reflects the user's desire that the page use a light or dark color theme." Its values are `light` and `dark`. The person's system holds the choice, and the page follows it.

And the field holds text and controls to a floor of contrast. WCAG 2.2's Success Criterion 1.4.3, *Contrast (Minimum)*, at Level AA: "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1", with named exceptions. Success Criterion 1.4.11, *Non-text Contrast*, at Level AA, asks the same of controls: "The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s)", for the parts of a control and for graphics.

The sources were read on 27 November 2026, and Appendix F lists them. So the field switches a page between a light and a dark theme, and measures the contrast of what it draws.

## The principle

**A culture changes how an interface looks to its users; it never takes away what the interface keeps within their reach.**

Article VI of the law, *Operator Primacy and Vibes*, says it in one sentence. The contract carries it word for word: "Vibe-invariant rights never flex." The site's exhibit of the two cultures gives the division: "the vibe owns *how* the screen looks, and it has no freedom over *what* the screen shows."

## Two cultures, one site

The Zayn site is drawn in two cultures, and its reader chooses one with a menu in the bar at the top of the site's pages, or with the key F2. In the exhibit's words, a culture's palette is "indigo and rose, or phosphor on black", and its typeface "proportional prose, or the terminal's mono". The law's notes on its rules name the two `curator` and `guardian`: Modern and Retro, in that order. They are names in the law's notes; a `VIBE` takes any name, and its `DENSITY` and `MOTION` take any word.

A culture is built as a set of named values. Zayn's design system says it: "**Fixed** tokens hold in both cultures; **culture** tokens are set by Modern and Retro (Article VI), always under the same name and meaning." A token is a named value the stylesheet uses. Each culture sets {{n:culture.tokens}} of them. They are the typeface, the colours of the frame, the colours of the five statuses of Rule 118 and the one quiet colour it keeps for everything else, the radius of a corner and its shadow, and the measure of a line of reading. The names and their meanings stay; the values change.

The design system's list of what a page may vary, and what it may not, keeps the meaning fixed: never "the meaning of a colour; a sixth status colour; a hue outside the tokens". The meaning of `danger` is fixed; its red is Modern's or Retro's.

The site's exhibit draws one screen of operations in both cultures side by side. Both come from one shared state: "An action in either pane changes the other pane, because the truth is shared and only the projection differs." The law calls its user the operator, and gives the operator {{n:law.rights}} rights: to understand, to reverse, to know, to leave, to act without fear and to reach a human. The exhibit's list of what a culture cannot touch begins with "The six operator rights" and "The undo window and every declared way back (Article IV)". And it says why both are measured: "a page can be lawful in one palette and unlawful in the other." The audit of the painted page runs its checks of the painted page in both cultures; chapter 17 tells its recorded runs.

## A culture, declared

In the language, a culture is a declaration, `VIBE`: in the specification's words, "Article VI made declarable: a culture, not a skin". It may set `DENSITY`, a word for how close things sit, `SURFACE_AS`, the medium it is drawn in, and `MOTION` with what the motion `REPORTS`. A motion that reports no state is refused as decoration, `DECORATIVE_ANIMATION`, under Rule 112: the verifier checks that a motion reports, and a person judges whether its way of moving fits. And it may hide verbs with `SUPPRESSES`; the specification calls them intents, and says the field is "Legal only for intents no declaration guarantees". To guarantee a verb is to list it under `ALWAYS_REACHABLE`, the verbs kept within reach at every step.

Here is a flow to delete an invoice, and the site's two cultures beside it. An `INTENT_FLOW` is the steps of one intent; `SATISFIES` lists the verbs the user performs, from the law's closed list of {{n:law.verbs}}, and `ACTOR` names who acts.

::: plate One flow, two cultures
```zayn invoices.zayn
DEFINE INTENT_FLOW delete_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR clerk
)

DEFINE VIBE modern (
  SURFACE_AS visual,
  DENSITY comfortable,
  MOTION none
)

DEFINE VIBE retro (
  SURFACE_AS visual,
  DENSITY compact,
  MOTION none
)
//--> clean
```
In words: A clerk selects an invoice, confirms, and deletes it, with undo and cancel within reach; the screen is drawn in two cultures, one comfortable and one compact, neither moving.
:::

Clean, at level 2, the verifier's default, where each check needs only the file; a level is a stage of what a check needs to read. One declaration of what the clerk does, two cultures beside it. They differ in density and agree on everything the flow keeps within reach. Now let the compact culture be made quicker by someone who thought the undo was clutter.

::: plate Retro, with the way back hidden
```zayn invoices.zayn
DEFINE INTENT_FLOW delete_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR clerk
)

DEFINE VIBE modern (
  SURFACE_AS visual,
  DENSITY comfortable,
  MOTION none
)

DEFINE VIBE retro (
  SURFACE_AS visual,
  DENSITY compact,
  MOTION none,
  SUPPRESSES [UNDO]
)
//--> VIBE_STRIPS_RIGHT retro
```
In words: The same flow and cultures; the compact culture hides the undo.
:::

Refused: "A VIBE suppresses an intent another declaration guarantees as ALWAYS_REACHABLE." The finding cites Article VI and no rule: the law's sentence on cultures is an article, and the finding enforces it. A file is lawful only when every culture in it is. Modern alone does not save the file, because a clerk in Retro would delete with no way back. The check reads the declarations of one file, so a project keeps its cultures in the file of the flow they draw. A culture kept in a file of its own answers clean beside a flow in another; a request to read every file of a run is with Zayn's own repository. A team that keeps its cultures in a design system apart from its screens declares them beside each flow for the check to hold.

The court's fixture holds a payment flow and a culture for a kiosk that hides the undo the flow guarantees, and it is refused the same way. A culture may hide a verb that no declaration keeps within reach: remove the `SUPPRESSES` line, or name such a verb in it, and the file is clean.

## What a culture may not carry

A culture sets the look. The register in which the system speaks is the message's, and it is declared on a feedback, not on a culture.

::: plate A culture that speaks
```zayn retro.zayn
DEFINE VIBE retro (
  SURFACE_AS visual,
  TONE critical
)
//--> FIELD_MISPLACED retro
```
In words: A culture drawn on a screen, which sets the tone in which the system speaks.
:::

Refused: "A field is declared on a kind that does not declare it." The report names the kind it belongs to, `FEEDBACK`. Chapter 7 runs the same finding on a screen.

## The law a reader's language keeps

A reader brings a language as well as a culture, and the law holds three rules for it, in Set 18, *Multilingualism & Dialects*. Rule 63 lets each part of a business use its own word for the same person, "Client" here, "Debtor" there. Rule 64 turns a layout for a script read from right to left, and says what never turns: clocks, the controls of a player, the digits of a number. Rule 122 keeps every string in a dictionary per language, and its reason is the law's: "the next operator's mother tongue should cost a file, not a fork". Bound to Rule 122, the law's list of {{n:law.forbidden}} forbidden patterns holds its first cultural one: "A sovereign sign conscripted as a convenience label", a flag used to name a language.

The law files all three under `judgment`, the tier where a person decides, and the verifier holds no kind of finding for them. A person reads them on the drawing. Chapter 15 takes them further, with the reader's own reading of a sign.

## What I refused

**A platform's default inside a culture.** Of the site's Theme menu, open, I said that its selected line "should embrace the current theme (retro or modern) not the standard browser them (that ugly blue)". My ruling on that remark entered the law with its version 3.15, as Article VI's evidence: "a culture owns every state of its controls, the open one included, and none is left to the platform's default". I said the same later of the checkboxes: "checkboxes should be in green not blue in this retro mode!" That sentence is Article VI's evidence in the law; the rule the design system proposes with the same aim, that a culture owns its defaults, is designed.

**The other culture in the first instant.** I said it of the site's pages: "when a page is clicked in the menu in retro the modern them is displayed slightly before the retro them is establsihed!!" The culture is now set in the page's head, before anything is painted.

**A citation the law does not hold.** The finding on a culture cites Article VI alone. A ruling of 2 November 2026, made under my delegation and recorded in the docket, kept it so: the law holds no numbered rule for it, and the finding cites the article it enforces.

**The word kept for the interaction.** A note of the docket, left for my ruling, keeps "culture" for a culture of interaction, and asks a word of its own for the reader's reading; chapter 15 tells it.

[AUTHOR: the stake of this chapter, in your words: why the site is drawn in two cultures, and what Retro is for.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the culture's side. A culture for a kiosk that hides an undo its flow keeps within reach, refused. A file of {{n:lang.kinds}} kinds of declaration, among them a dense culture drawn in a terminal, clean. A field on a kind that does not read it, refused, and its twin with the field in its place.

## Where the field leads

The field leads in the person's own choice. A page reads `prefers-color-scheme` and follows the theme the person's system asks for. The Zayn site gives the choice to its reader inside the page, by a menu and a key, and the law keeps a rule against knobs, Rule 44, *Strong Defaults Over Customization*.

The field leads in the floor of contrast. The Zayn site writes the contrast of its main colours beside them in the stylesheet, in each culture, and the audit reads contrast on the painted page in both.

Zayn leads in what a culture may never touch. A theme of the field changes colours, and its criteria measure each colour. A culture of Zayn is declared beside the flow it draws. The verifier refuses the culture that hides a way back the flow keeps within reach; in the exhibit's words, declaring a culture "lets a compiler check that no culture has quietly dropped a right". It reads the guarantees of one file at a time.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: Article VI and the declaration `VIBE`, with the verifier's refusal of a culture that hides a way back another declaration keeps within reach, run on this page. The Zayn site's two cultures, Modern and Retro, each setting {{n:culture.tokens}} named values, chosen by the reader and drawn before the first paint. The exhibit of one screen in both cultures from one state. The audit of the painted page in both. Set 18 and the forbidden pattern bound to Rule 122, read by a person. Designed: a culture's vocabulary of interaction, Retro keyboard-first with instant feedback and Modern pointer-first; a rule that a culture owns every default of its controls, proposed in the design system; culture as the reader's reading, chapter 15. Next: that reading, in chapter 15.

So a declared culture is refused when it hides a way back, and the site's two cultures, drawn by its stylesheet, are measured on the painted page.

## In your hands

Here is the flow to delete an invoice once more. Its second culture was written by someone who wanted Retro quick and bare. Three findings wait in it. Write what you expect, then open the verifier's answer.

::: plate For you: a quick Retro
```zayn invoices.zayn
DEFINE INTENT_FLOW delete_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR clerk
)

DEFINE VIBE modern (
  SURFACE_AS visual,
  DENSITY comfortable,
  MOTION none
)

DEFINE VIBE retro (
  SURFACE_AS visual,
  DENSITY compact,
  MOTION blink,
  SUPPRESSES [UNDO, CANCEL]
)
//--> DECORATIVE_ANIMATION retro
//--> 2 VIBE_STRIPS_RIGHT retro
```
In words: The flow and two cultures; the compact one blinks, and hides both the undo and the cancel.
:::

Repair it, and say what you expect. Two lawful repairs follow. Try before you read on.

::: plate Retro, still and whole
```zayn invoices.zayn
DEFINE INTENT_FLOW delete_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR clerk
)

DEFINE VIBE modern (
  SURFACE_AS visual,
  DENSITY comfortable,
  MOTION none
)

DEFINE VIBE retro (
  SURFACE_AS visual,
  DENSITY compact,
  MOTION none
)
//--> clean
```
In words: The flow and two cultures, neither moving, and nothing hidden.
:::

::: plate Retro, blinking with a reason
```zayn invoices.zayn
DEFINE INTENT_FLOW delete_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ACTOR clerk
)

DEFINE VIBE modern (
  SURFACE_AS visual,
  DENSITY comfortable,
  MOTION none
)

DEFINE VIBE retro (
  SURFACE_AS visual,
  DENSITY compact,
  MOTION blink,
  REPORTS [invoice_state]
)
//--> clean
```
In words: The flow and two cultures; the compact one blinks to report the invoice's state, and hides nothing.
:::

Both clean. The second blinks, and the verifier accepts it, because the blink now reports a state. The verifier checks the part of Rule 112 a declaration states: that the motion reports. Whether a blink is a fit way to report is a person's to judge, and the site's own design system forbids blinking in both of its cultures. Would your Retro blink?

[AUTHOR: is the quick Retro the defect you want the reader to repair here, or one from your own work?]

A culture of interaction is chosen by the reader. The next chapter turns to the culture the reader brings: what a sign means to the one who reads it.
