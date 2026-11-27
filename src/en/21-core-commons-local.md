---
id: core-commons-local
part: 8
number: 21
title: "Core, commons, local"
stage:
  built: "the parts the tiers would sort, as the law's data: the preamble, {{n:law.articles}} articles, {{n:law.rights}} rights, the invariants of {{n:law.families}} families of verbs, {{n:law.forbidden}} forbidden patterns, and on each of {{n:rule.derived}} rules the article it derives from; the pack of {{n:pack.files}} files pinned by hash, whose check refuses a changed byte; a team's own contract of findings, which the verifier follows; a culture that may not remove a guaranteed verb, run on this page"
  designed: "four tiers of law, statute, core, commons and local, with one rule between them: a local law may be stricter and never looser; the test and the three forms by which a rule is admitted to the commons; a team's local law shipped beside the pinned one"
  next: "the plan's change to the law's file that files every rule under its tier, and the capture loop carried by one real application"
status: draft
research: research/ch21.md
fixtures: [vibe-strips-right, unknown-medium, unknown-medium-lawful, unknown-field]
---

A tier of the law is the level at which a rule is written and kept: for every team, for many teams, or for one. *The Second Founding* is a proposal of the project for a new base of the law, and it awaits my ruling. It designs four tiers: the statutes and binding standards above the law, the core every adopter keeps, the commons many teams contribute to, and the local law of one team. In this chapter I say what each tier is and who may write in it, and how a rule is admitted. Then I show what a team holds today. It holds the law's parts as data, a pin by hash and a contract of its own; and in one place the language already keeps a team's choice from taking away what the core guarantees.

If you open the book here, a few words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law, and a **finding** is one entry of its report, a refusal when it is an error.

## The field

The field keeps its standards in levels, and it says how a thing moves between them.

The Internet's standards process is RFC 2026, of October 1996. It sets levels of maturity: "The entry-level maturity for the standards track is "Proposed Standard"." And it keeps apart the statement that says when a specification applies, which it calls an "Applicability Statement".

Debian, a distribution of free software, keeps its archive in areas. "The main archive area comprises the Debian distribution." Beside it, "The contrib archive area contains supplemental packages intended to work with the Debian distribution".

A tool for checking code lets a team take another's settings. ESLint says: "Shareable configs are simply npm packages that export a configuration object or array." And: "You can publish your shareable config on npm so that others can download and use it in their ESLint projects." A team takes the shared settings into its own project.

And a specification leaves room at its edges. OpenAPI 3.2.1, of September 2026: "The extensions properties are implemented as patterned fields that are always prefixed by `x-`."

The sources were read on 27 November 2026, and Appendix F lists them. So the field matures a standard by levels, keeps a distribution apart from what works with it, shares settings a team may change, and opens named places for extension.

## The principle

**What is true of every person is kept by every team; what is true of one place is set by that place, and it may take away nothing the law guarantees.**

The proposal draws the line in two sentences, first written for culture and then carried into the tiers: "What is non-negotiable is what is true of human beings. What is contributed is what is true of a place." It says which side each thing falls on: "Finite attention, working memory, error recovery and the dignity of undo travel everywhere. Palettes, densities, accents and every colour assignment do not."

## Four tiers

The proposal names "Four tiers, one supremacy rule."

**Statute** is an instrument outside the law that binds a medium, such as a state's rule for road signs, and "that instrument outranks this constitution absolutely". Where the law meets one, the proposal says, its duty is "to *refuse a conflict*, never to resolve it in our favour."

**The core** is the preamble, the {{n:law.articles}} articles, the user's rights, the invariants of the families of verbs and the forbidden patterns: "Amended only by convention, never by contribution."

**The commons** is the rules "contributed, curated, evidence-gated", today's rules of the law and every rule a team adds.

**The local** is "a person's or organisation's own laws, pinned alongside, shipped with the app."

And one rule orders them: "a local law may be *stricter* than the commons and never *looser*; and nothing at any tier may contradict a statute that binds the medium."

The proposal gives the local tier its reason with the case of a ministry, for which "a local law forbidding a sign class" can be "a political necessity, not a taste". A team may hold its interface to more than the commons asks. It may not hold it to less.

## How a rule is admitted

A rule reaches the commons by a test and in three forms.

The test is short: "a proposed rule that derives from no article is inadmissible; one that contradicts the Core is inadmissible; everything else is a question of evidence. No committee of taste is required." Its first half is already data. Each of the {{n:rule.derived}} rules of the law names, in its field `derived_from`, the article it derives from, and each names one of the {{n:law.articles}}.

The three forms are a gotcha, a fixture and evidence: "the Gotchas make an offense *feelable*, the fixtures make it *checkable*, `evidence` makes it *accountable*. A contributed law arrives as all three or not at all." A gotcha is an offense and its lawful twin that a person can play on the Zayn site. A fixture is a declaration kept with the answer it must get, and the suite holds {{n:fix.total}}. The evidence is the field each of the {{n:rule.evidence}} rules carries. All three forms exist today, for some of the law's rules; the evidence is on every one. A path by which a team sends them in is the designed part, and chapter 20 tells its first step, the capture of a remark.

## A place may add, not take away

One check of the language already works as the supremacy rule would, for one case, and it is built. A team's culture of interaction, its `VIBE`, is its own: it names it, sets its density, and may hide verbs. Here is a flow for a field engineer who records a meter's reading, and the crew's own culture beside it.

::: plate A crew's culture that hides the undo
```zayn crew.zayn
DEFINE INTENT_FLOW record_reading (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR field_engineer
)

DEFINE VIBE field_crew (
  SURFACE_AS visual,
  DENSITY compact,
  SUPPRESSES [UNDO]
)
//--> VIBE_STRIPS_RIGHT field_crew
```
In words: A field engineer selects a meter, confirms and records the reading, with undo, cancel and a way out within reach; the crew's culture is compact and hides the undo.
:::

Refused: "A VIBE suppresses an intent another declaration guarantees as ALWAYS_REACHABLE." The check refuses a culture that hides a verb another declaration of the same file keeps within reach under `ALWAYS_REACHABLE`; here the undo, which serves the right to reverse, a right of the core. A verb that no declaration keeps within reach may be hidden. The crew may still choose what is its own.

::: plate The crew's culture, adding only
```zayn crew.zayn
DEFINE INTENT_FLOW record_reading (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR field_engineer
)

DEFINE VIBE field_crew (
  SURFACE_AS visual,
  DENSITY compact,
  SUPPRESSES [ZOOM]
)
//--> clean
```
In words: The same flow; the crew's culture is compact and hides zoom, one of the law's verbs, which no declaration keeps within reach.
:::

Clean. Density is the crew's, and zoom was promised by no one. Chapter 14 runs the same check on the Zayn site's two cultures.

## What a team holds today

**A pin.** The law reaches a team as a pack: {{n:pack.files}} files, the law's data and the suite's, each recorded with its hash in a manifest. A hash is a number computed from a file's bytes; the pack's guide says "A hash says the bytes you have are that edition." A team copies the pack into its project and runs the pack's check in its build. In this book's research, on 27 November 2026, the check was run on such a copy. As copied, it answered "verified — every pinned file matches the manifest", exit 0; with one space added inside a rule's title, it reported that the law's file had "content changed since the manifest was written", exit 1. In the proposal, a team's own law is pinned beside the law, never inside it; the pin already refuses a change inside it. Chapter 25 tells the pack's command.

**A contract of its own.** The verifier reads the contract, the file that gives each kind of finding its severity, its level and its citation, and a team may give it its own with the option `--contract`. The same research ran it both ways. A contract that raised a warning to an error turned a pass with a warning into a refusal, exit 1: stricter. A contract that lowered the culture's refusal above to a warning turned it into a pass, exit 0: looser. The verifier follows the contract a team gives it. So a buyer requires the pinned contract: the supplier runs the verifier with the contract of the pinned pack and no other, and delivers the pack's check with its report. The supremacy rule that would hold a team's contract to "stricter, never looser" is designed. The pack's check refuses a changed byte in the law's own files, and a request that the pack's check also compare a team's contract with the pinned one is filed with Zayn's repository.

**A culture of its own.** A `VIBE` takes any name and any density, and {{n:rule.vibes}} of the law's rules carry a field of notes for named cultures, `vibes`. The place's choices are its own, under the one refusal run above.

## What I refused

**No statute written into the law before it is read.** On 13 August 2026 I ruled that the review of the standards for industrial signs and safety colours goes ahead. I ruled too that "nothing is written into `rules.json`" until their editions are read and their clauses recorded. The tier of statute begins with reading the statute.

**The core is not open to contribution.** The proposal, which awaits my pass, keeps it so: the core is "Amended only by convention, never by contribution". A team's rule enters the commons or stays local.

**No precedence invented under a delegation.** In a pass I delegated in August, the docket met the question of which rule wins when two meet. It left the order unwritten: "inventing one inside a delegated ruling would be exactly the overreach this docket exists to prevent." The law holds no rule of precedence, and the tiers' order waits for my ruling.

**An implementation does not widen a closed list.** The pack's guide says it: "an implementation that adds a verb is not a superset of Zayn, it is a different language that fails the fixtures." A team may name its culture; it may not add a medium or a verb by itself.

[AUTHOR: the stake of this chapter, in your words: where you draw the line between what every team keeps and what a place may add, since the proposal leaves that line to you.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the place's side. A culture for a kiosk that hides an undo its flow guarantees, refused. A medium named outside the list, refused, and its twin with a medium of the list. A field the grammar does not hold, refused. The pin and the contract are shown by the research's recorded runs; the tiers are design, and the suite's fixtures judge declarations.

## Where the field leads

The field leads in practice. Its standards have moved between levels for decades, and its distributions keep a main area apart from what works with it. Zayn's tiers are a design, and its plan names the step that would file every rule under its tier as the change it handles with the most care, because it edits the law's own file.

The field leads in a team's freedom. A shared configuration of ESLint is a package any team can take into its project, and OpenAPI opens named fields for anything a tool wishes to add. Zayn's closed lists keep every implementation speaking one language, and its proposal lets a team add, never loosen.

Zayn's design leads in what admission reads. A rule of the field is admitted by people who weigh it; in the proposal, a rule of Zayn's commons is admitted when it derives from an article, contradicts nothing in the core, and arrives with a gotcha, a fixture and its evidence. Every rule of the law already carries the article and the evidence. And the proposal, written by a session of the project, leaves the line between the tiers to me: "the author has better standing than I do to say where the line actually falls".

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the core's parts in the law's data, and on every rule the article it derives from and its evidence. The pack of {{n:pack.files}} files pinned by hash, whose check refuses a changed byte. A team's own contract of findings, which the verifier follows. A culture that may not remove a guaranteed verb, run on this page. Designed: the four tiers and the rule between them, a local law stricter and never looser; the admission test and its three forms; a team's local law shipped beside the pinned one. Next: the plan's change to the law's file that files every rule under its tier; the capture loop carried by one real application.

So the law's parts are data the tiers would sort, a team's pin and contract are built, and the order of the tiers is the designed part, waiting for my pass.

## In your hands

Here is a team's culture for its night shift. The team named its own medium, for the tablets on its floor, and hid the cancel its flow keeps within reach. Two findings wait. Write what you expect, then open the verifier's answer.

::: plate For you: the night shift
```zayn shift.zayn
DEFINE INTENT_FLOW close_shift (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR supervisor
)

DEFINE VIBE night_shift (
  SURFACE_AS tablet,
  DENSITY compact,
  SUPPRESSES [CANCEL]
)
//--> VIBE_STRIPS_RIGHT night_shift
//--> UNKNOWN_MEDIUM night_shift
```
In words: A supervisor confirms and closes a shift, with undo, cancel and a way out within reach; the night shift's culture is drawn on a tablet, compact, and hides the cancel.
:::

Repair it, and say what you expect. Two lawful repairs follow. Try before you read on.

::: plate The night shift, on a screen
```zayn shift.zayn
DEFINE INTENT_FLOW close_shift (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR supervisor
)

DEFINE VIBE night_shift (
  SURFACE_AS visual,
  DENSITY compact
)
//--> clean
```
In words: The same flow; the night shift's culture is drawn on a screen, compact, and hides nothing.
:::

::: plate The night shift, hiding zoom
```zayn shift.zayn
DEFINE INTENT_FLOW close_shift (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR supervisor
)

DEFINE VIBE night_shift (
  SURFACE_AS visual,
  DENSITY compact,
  SUPPRESSES [ZOOM]
)
//--> clean
```
In words: The same flow; the night shift's culture is drawn on a screen, compact, and hides zoom.
:::

Both clean. A tablet is a screen, and the medium is `visual`. The list of media is the language's, closed: visual, auditory, voice, haptic, print, luminous, signage, machine, spatial and terminal; and a new one is a change of the language or an amendment of the law. If your team needed a channel the list does not hold, which tier would its request enter: your local law, the commons with its three forms, or the core?

[AUTHOR: is the night shift the defect you want the reader to repair here, or one from your own work?]

A team writes its own law, and the core holds for every team. The next part turns to the user the law was written for twice over: the AI agent, which both draws interfaces and uses them.
