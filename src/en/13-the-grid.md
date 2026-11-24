---
id: the-grid
part: 5
number: 13
title: The grid
stage:
  built: "the grid as data and as a page: {{n:grid.cells}} cells, {{n:grid.closed}} closed and {{n:grid.live}} open, of which {{n:grid.ruled}} hold a rule and {{n:grid.empty}} are empty, with {{n:grid.placed}} of the {{n:law.rules}} rules placed; the projection fixtures, which apply a rule under a declared medium, run on this page; a declaration that lands on a closed cell refused by name"
  designed: "the record by which a defect found in use lands on a cell"
  next: "the projection of the rules that name no medium into haptic, luminous, signage, spatial and terminal; rules written for those media once a product that ships in one is named; a person's perception of each medium"
status: draft
research: research/ch13.md
fixtures: [projection-auditory-undo, projection-auditory-undo-lawful, projection-voice-select-act, projection-voice-select-act-lawful, projection-machine-cancel, projection-machine-cancel-lawful, projection-print-motion, projection-print-motion-lawful, projection-print-promise, projection-print-promise-lawful, projection-visual-perceive, projection-visual-understand, projection-visual-decide, projection-visual-act, projection-visual-recover, projection-visual-trust]
---

The grid is a map of what the law covers, drawn from what a user does with an interface. In this chapter I draw it: the media crossed with the activities of the user, the cells that no rule can hold, the cells that hold one and the cells that wait for one. I show how each rule finds its place. Then I run a rule on a cell where no rule is written, to see whether it answers there.

If you open the book here, four words are enough to follow, and an `INTENT_FLOW`, on the plates, is a flow: what a user does to reach one goal. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces. The **verifier** is the program that checks a declaration against the law. A **medium** is the way an interface meets its user: a screen, a sound, a voice, a printed page, a program that reads it. The Zayn site and chapter 12 also call it a channel, and chapter 12 gives the {{n:grid.media}} media of the law.

## The field

The field has drawn maps of its rules. The accessibility guidelines are organised around "four principles", with their guidelines under them: one axis, the user's perception and use, with a tree beneath it.

The field has also separated what a user does from how it is drawn. W3C's Note on task models says that they "describe the logical activities that have to be carried out in order to reach the user's goals". Its Note on abstract interfaces describes an interface "independent of any interaction modality (e.g., graphical, vocal, haptic, 3D)".

Each source was read on 23 November 2026, and Appendix F lists them. So the field has a tree of principles, a model of the user's activities, and an interface held apart from its medium.

## The principle

**A cell holds a rule when a rule is written for it, so every empty cell shows where the law is projected today and where its next rule will stand.**

To project a rule is to apply a rule that names no medium in one medium. The grid's page on the Zayn site says what an empty cell is: "an empty cell is a visible gap in the law, not a hidden one". The design document behind the page counts only the rules written for a cell, and gives the reason: a rule's projection into a cell is "a claim that the rule *can* be projected there". So the count shows what is written, and every empty cell stays in view.

## Activities and media

The activities are what a user does: perceive, understand, decide, act, recover, trust. Each is a question the user asks of an interface, and none is named after a defect. The law's verbs, its words for what a user does, are shared among them, each verb once: understand owns the verbs of finding and reading; decide, those of choosing; act, `ACT` and `CONFIRM`; recover, those of the way back and of time. Perceive and trust own no verb, and the design document gives the reason for perceive: "Giving perceive the verb READ would have called a lit lamp unperceivable." So no medium is closed to perceiving or to trusting.

The media are the ten of the law, and one more, `any`: in the document's words, "the law stated without a medium, before it is projected into one". Here is the grid, counted from the data each time this book is built. It has a medium on each row and an activity in each column, as the site draws it. In the table, `visual` is the screen, `auditory` is sound that is not speech, `voice` is speech, and `machine` is a program that reads the interface.

{{grid}}

Read the table by its kinds of cell. A closed cell is one that no rule can hold: the medium carries none of the verbs the activity owns. Every other cell is open. A number is the count of rules written for that activity in that medium, and a zero is an empty cell, where the next rule will stand. The grid has {{n:grid.cells}} cells: {{n:grid.closed}} are closed, and of the {{n:grid.live}} open ones, {{n:grid.ruled}} hold a rule and {{n:grid.empty}} are empty.

Two rows carry most of the law. Of the {{n:grid.placed}} rules placed, {{n:grid.visual}} sit on the screen, {{n:grid.free}} name no medium, and Rule 125 sits on sound alone. A rule counts once in these figures, and once in each cell of the table where it is placed. The law is written for a screen, and the row `any` holds the rules stated for every medium.

## How a rule finds its place

A rule's activities are read from its title and its reason. Its medium is found in three steps. First, a medium that its own words name. If none, no medium at all, when the kind of finding that enforces it ignores the medium, or when its text speaks of no screen. If neither, the screen. Rule 79, the undo rule, takes the second step: its finding is the same on every medium. {{n:grid.off}} rules are placed on no cell, and the file gives each a reason: one is a checklist applied to the other rules, and one concerns what a generator, a program that writes interfaces, ships.

The placement is a reading, and it was measured as one. On 3 November 2026 I ruled that it "be measured, not changed", and two readers, each of whom had not seen the placement, placed a sample of the rules again. They agreed on the medium more often than on the exact activities, and the design document draws the lesson: "The medium-free column is stable where a diagnostic is bound and soft where none is." The same day I ruled how a medium is named: "a rule sits on a medium only where its own words name it". The placements of Rules 60, 104, 123 and 125 changed.

## A rule on an empty cell

The row `any` stands for every medium, so a rule that names no medium is projected onto the empty cells of its activity in every medium. Does it answer there? Here is Rule 79, which the placement puts on no medium, on a surface heard as sound.

::: plate An alert heard as sound, with no way back
```zayn alert.zayn
DEFINE VIBE alert_audio (
  SURFACE_AS auditory
)

DEFINE INTENT_FLOW dismiss_alert (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR operator
)
//--> MISSING_UNDO dismiss_alert
```
In words: The surface is heard as sound. An operator confirms and an alert is dismissed, with cancel and exit within reach.
:::

Refused, under Rule 79, on a sound surface as on a screen. The declaration lands on recover by auditory, an empty cell, and the rule answers there. The lawful twin, the same declaration with the defect repaired, keeps undo within reach.

::: plate The same alert, with undo
```zayn alert.zayn
DEFINE VIBE alert_audio (
  SURFACE_AS auditory
)

DEFINE INTENT_FLOW dismiss_alert (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR operator
)
//--> clean
```
In words: The same alert, and undo stays within reach.
:::

Clean. The rule fired on the defect and stayed quiet on its twin. Zayn has two verifiers: the reference that this page runs, and a second one built from another declaration of the language, which chapter 9 describes. When both agree on such a pair, the design document records that the rule "applies". Zayn's conformance suite, its set of fixtures, which are declarations kept with the answers they must get, holds such pairs for sound, voice, a program and print. Here is one more empty cell, recover by voice, measured on this page by a declaration of its own.

::: plate A voicemail, deleted for good
```zayn voicemail.zayn
DEFINE VIBE phone_assistant (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW delete_voicemail (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR mailbox_owner
)
//--> MISSING_UNDO delete_voicemail
```
In words: The surface speaks and listens. The owner of a mailbox selects a voicemail, confirms, and it is deleted, with cancel and exit within reach.
:::

Refused. The lawful twin keeps undo within reach.

::: plate A voicemail that can come back
```zayn voicemail.zayn
DEFINE VIBE phone_assistant (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW delete_voicemail (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR mailbox_owner
)
//--> clean
```
In words: The same deletion, and undo stays within reach.
:::

Clean. The run measured one more empty cell, and the grid's count stayed where it was, because the count is of the rules written for a cell, and this run wrote none. The design document says the same of the first projection fixtures: "No rule, diagnostic or verifier changed." The cell is measured, and it stays empty for its next rule.

## A closed cell, refused

A closed cell is drawn on the grid, and the verifier refuses what lands there: it refuses each verb that a medium cannot carry, and on a closed cell none of the activity's verbs is carried. Print carries no verb of the way back. Here is a printed ledger that promises one.

::: plate A printed ledger that promises a way back
```zayn ledger.zayn
DEFINE VIBE ledger_print (
  SURFACE_AS print
)

DEFINE INTENT_FLOW read_ledger (
  SATISFIES [READ],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR auditor
)
//--> VERB_NOT_CARRIED read_ledger
//--> VERB_NOT_CARRIED read_ledger
//--> VERB_NOT_CARRIED read_ledger
```
In words: The surface is a printed page. An auditor reads the ledger, and undo, cancel and exit are promised within reach.
:::

A refusal for each promised verb that print cannot carry. Each cites Rule 82, the rule of perceivable state, which the contract's note says "is what made 'the declared medium' a legal concept". This kind of finding, `VERB_NOT_CARRIED`, once read only what a declaration satisfies, and a promise like this one passed. On 2 November 2026 I ruled that it was, in the design document's words, "silence hiding an error, so the verifier changes". The repair promises nothing that paper cannot keep.

::: plate A printed ledger, read
```zayn ledger.zayn
DEFINE VIBE ledger_print (
  SURFACE_AS print
)

DEFINE INTENT_FLOW read_ledger (
  SATISFIES [READ],
  ACTOR auditor
)
//--> clean
```
In words: The surface is a printed page, and an auditor reads the ledger.
:::

Clean.

## A rule satisfied on paper

A rule that names no medium can be satisfied in a medium where it has nothing to act on. Here is a printed notice that declares a motion.

::: plate A printed notice that moves
```zayn notice.zayn
DEFINE VIBE printed_notice (
  SURFACE_AS print,
  MOTION fade
)
//--> DECORATIVE_ANIMATION printed_notice
```
In words: The surface is a printed page, and the notice fades.
:::

Refused under Rule 112: motion that reports nothing is decoration. Now give the motion something to report.

::: plate A printed notice that moves and reports
```zayn notice.zayn
DEFINE VIBE printed_notice (
  SURFACE_AS print,
  MOTION fade,
  REPORTS [save_state]
)
//--> clean
```
In words: The same printed notice, and its fading reports that the work was saved.
:::

Clean, and print has no time in which to fade. The design document records it as a gap of projection: "The rule is satisfied in a medium where it cannot apply". On 2 November 2026 the same ruling left it unchanged, because it hides no error. It stays, in the document's words, "open as a fact and closed as a question".

## What I refused

**I refused a rule written to fill an empty cell.** My ruling of 2 November 2026, as the grid's document keeps it, "forbids writing a rule for them until that is measured": until the projection of the rules that already reach those cells is measured. The measurement came first, with the projection fixtures of this chapter.

**I refused to change the placement when it was doubted.** I ruled that it be measured instead, and then ruled how a medium is named.

**The design document refused to count a projection as coverage.** A rule that names no medium is projected onto every empty cell of its activity, and the count leaves those cells empty, so that each stays in view.

**The design document keeps back rule text** for haptic, luminous, signage, spatial and terminal, until a product that ships in one of them is named.

[AUTHOR: the stake of this chapter, in your words: why an empty cell is shown on the public page, and what a team should do with one.]

## The court

The court of a chapter is what proves it. In this chapter it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the projection fixtures, which apply a rule that already exists under a declared medium: ten in pairs, a refusal beside its lawful twin, and six on the screen, one for each activity.

## Where the field leads

The field leads on people. W3C's page on evaluation says that "Knowledgeable human evaluation is required to determine if a site is accessible." The grid's projection is measured by instrument, and the design document says so: the fixtures are "projected by instrument, not as verified by a person". A person's perception of each medium is next.

The field leads on the media themselves. What a medium carries is, in Zayn's data, "derived by reasoning about each medium's properties, not by rendering anything", and chapter 12 reads it.

Zayn leads on a map that is finite and counted. The verbs are a fixed list, and so are the media, so the grid has a fixed number of cells, a declaration that lands on a closed cell is refused, and an empty cell is printed on the public page with its count.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The grid on this page is counted at each build from the placement of the rules, the media and the verbs each activity owns, and its figures equal those of the Zayn site. The projection fixtures show that rules which name no medium answer on sound, voice, a program and print as on a screen, and one projection on print is recorded as a gap of projection. The placement is a reading, measured by two readers and ruled on. Each of the {{n:grid.empty}} empty cells is projected onto by a rule that names no medium. A rule for each is for my ruling, after its projection is measured.

## In your hands

This exercise is written for the book. Here an AI agent is the user: it orders stock through a supplier's interface for programs. A `VIBE` with `SURFACE_AS machine` says that the surface is read by a program. Write the finding you expect, by its code, then open the verifier's answer.

::: plate For you: an order placed on a choice
```zayn reorder.zayn
DEFINE VIBE supplier_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW reorder_stock (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR purchasing_agent
)
//--> SELECT_ACT_COLLAPSE reorder_stock
```
In words: Through a supplier's interface for programs, an AI agent selects a product and the order is placed. It can undo, cancel or leave at every step.
:::

Now place it on the grid. The report cites Rule 16, and the grid's placement puts Rule 16 on decide, act and trust, with no medium named. The `VIBE` says the medium is a program. A declaration lands on the cells of the activities its findings' rules are placed on, in the medium its `VIBE` names. So this one lands on the row `machine`, in the columns D, A and T, decide, act and trust: look at the table, and each of those cells is empty. Repair the declaration. Try before you read on.

::: plate The order, confirmed
```zayn reorder.zayn
DEFINE VIBE supplier_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW reorder_stock (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR purchasing_agent
)
//--> clean
```
In words: The AI agent selects a product, confirms, and the order is placed.
:::

Clean. What is a confirmation when the user is an AI agent reading a surface made for programs? Zayn's data on the machine medium says: "What a screen reader can operate, an agent can operate". Whether that holds for a confirmation is the question that the next rule for decide, act or trust by machine will answer, and the grid keeps those cells empty for it.

A cell is a place where a rule can stand. Part VI asks who reads the interface that the rules describe: two cultures, under one law.
