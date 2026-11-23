---
id: the-grid
part: 5
number: 13
title: The grid
stage:
  built: "the grid as data and as a page: {{n:grid.cells}} cells, {{n:grid.closed}} closed, {{n:grid.live}} live, {{n:grid.ruled}} holding a rule and {{n:grid.empty}} open to the next rules, with {{n:grid.placed}} of the {{n:law.rules}} rules placed; the projection fixtures, which apply a rule under a declared medium, run on this page; a closed cell refused by the verifier by name"
  designed: "the record by which a defect found in use lands on a cell; the projection of the rules that name no medium into the media that have no fixture yet"
  next: "rules written for the media that have none, once a product that ships in one is named; a person's perception of each medium"
status: draft
research: research/ch13.md
fixtures: [projection-auditory-undo, projection-auditory-undo-lawful, projection-voice-select-act, projection-voice-select-act-lawful, projection-machine-cancel, projection-machine-cancel-lawful, projection-print-motion, projection-print-motion-lawful, projection-print-promise, projection-print-promise-lawful, projection-visual-perceive, projection-visual-understand, projection-visual-decide, projection-visual-act, projection-visual-recover, projection-visual-trust]
---

The grid is a map of what the law covers, drawn from what a user does with an interface. In this chapter I draw it: the activities of the user crossed with the media, the cells that no rule can hold, the cells that hold one and the cells that wait for one. I show how each rule finds its place. Then I run a rule where no rule is written for its cell, to see whether it answers there.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces. The **verifier** is the program that checks a declaration against the law. A **medium** is where an interface reaches its user: a screen, a sound, a voice, a printed page, a program that reads it. Chapter 12 gives the {{n:grid.media}} media of the law.

## The field

The field has drawn maps of its rules. The accessibility guidelines are organised around "four principles", with their guidelines under them: one axis, the reader's perception and use, with a tree beneath it.

The field has also separated what a user does from how it is drawn. W3C's Note on task models says that they "describe the logical activities that have to be carried out in order to reach the user's goals". Its Note on abstract interfaces describes an interface "independent of any interaction modality (e.g., graphical, vocal, haptic, 3D)".

So the field has a tree of principles, activities written for each application, and an interface held apart from its modality. Each source was read on 23 November 2026, and Appendix F lists them.

## The principle

**A cell is held when a rule is written for it, so every empty cell shows where the law reaches by projection and where its next rule will stand.**

The grid's page on the Zayn site says it in one line: "an empty cell is a visible gap in the law, not a hidden one". The design document behind the page keeps its count strict. It does not count a rule's reach as coverage, because then "the honest gap would read 0".

## Six activities, ten media

The rows are what a user does: perceive, understand, decide, act, recover, trust. Each is a question the user asks of an interface, and none is named after a defect. The law's verbs are shared among them, each verb once. Understand owns the verbs of finding and reading, decide those of choosing, act owns `ACT` and `CONFIRM`, recover those of the way back and of time. Perceive and trust own no verb, and the design document gives the reason for perceive: "Giving perceive the verb READ would have called a lit lamp unperceivable."

The columns are the media, and one more, `any`: in the document's words, "the law stated without a medium, before it is projected into one". Here is the grid, counted from the data at this build. The site draws it the same way, with a medium on each row.

{{grid}}

Read the table by its three kinds of cell. A number is the count of rules written for that activity in that medium. A closed cell is one that no rule can hold: the medium carries none of the verbs the activity owns. A zero is an open cell that no rule names yet. The grid has {{n:grid.cells}} cells: {{n:grid.closed}} are closed, and of the {{n:grid.live}} live ones, {{n:grid.ruled}} hold a rule and {{n:grid.empty}} are open to the next rules.

Two columns carry most of the law. Of the {{n:grid.placed}} rules placed, {{n:grid.visual}} sit on the screen and {{n:grid.free}} name no medium. The law was written for a screen first, and the column `any` holds what is true of every medium.

## How a rule finds its place

A rule's activities are read from its title and its reason. Its medium is found in three steps: a medium its own words name; otherwise no medium at all, when the check that enforces it ignores the medium or its text speaks of no screen; otherwise the screen. {{n:grid.off}} rules are placed on no cell, and the file gives each a reason: one is a checklist applied to the other rules, and one concerns what a generator ships.

The placement is a reading, and it was measured as one. I ruled that the placement "be measured, not changed", and a second reader placed a sample of the rules without seeing the first reader's work. The two agreed on the activities more often than on the medium, and the design document draws the lesson: "The medium-free column is stable where a diagnostic is bound and soft where none is." On 3 November 2026 I ruled how a medium is named: "a rule sits on a medium only where its own words name it". The placements of Rules 60, 104, 123 and 125 changed that day.

## A rule where no rule is written

The column `any` reaches every row, so a rule that names no medium reaches the open cells of its row in every medium. Does it answer there? Here is Rule 79, the undo rule, which names no medium, on a surface heard as sound.

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

Refused, under Rule 79, on a sound surface as on a screen. The declaration lands on the cell recover by auditory, where no rule is written. The lawful twin keeps undo within reach.

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

Clean. The rule fired on the defect and stayed quiet on its twin: the design document calls that "applies". The suite holds such pairs for sound, voice, a program and print, and one fixture for each row on the screen. Here is one more empty cell, recover by voice, which no fixture of the suite reaches.

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

Refused. The lawful form keeps undo within reach.

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

Clean. The run measured one more empty cell by projection, and the grid's count did not move: the count holds the rules written for a cell, and this run wrote none. The design document says it of the whole measurement: "No rule, diagnostic or verifier changed."

## A closed cell, refused

A closed cell is drawn on the grid, and the verifier refuses it too. Print carries no verb of the way back. Here is a printed ledger that promises one.

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

Three refusals, one for each verb that print cannot carry. This check once read only what a declaration satisfies, and a promise like this one passed. I ruled on 2 November 2026 that it was, in the design document's words, "silence hiding an error, so the verifier changes". The repair promises nothing that paper cannot keep.

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

## A rule satisfied where it cannot apply

A rule that names no medium is not always projectable into every medium. Here is a printed notice that declares a motion.

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

Clean, and print has no time in which to fade. The rule is satisfied in a medium where it cannot apply. The design document records it as a gap of projection, and I ruled that nothing changes for it: it hides no error. It stays, in the document's words, "open as a fact and closed as a question".

## What I refused

**I refused a rule written to fill a cell.** The empty cells are reached only by rules that name no medium, and my ruling of that time, as the grid's document keeps it, "forbids writing a rule for them until that is measured". The measurement came first: the projection fixtures of this chapter.

**I refused to change the placement when it was doubted.** I ruled that it be measured instead, by a second reader, and then ruled the one principle the measurement showed was needed: a rule sits on a medium only where its own words name it.

**The grid does not count reach as coverage.** A rule that names no medium reaches every open cell of its row, and the document's count leaves that reach out, because a claim that a rule can be projected is "not a statement that anyone has done it".

**The design document holds rule text for the media that no rule names yet**, haptic, luminous, signage, spatial and terminal, until a product that ships in one is named.

[AUTHOR: the stake of this chapter, in your words: why an empty cell is shown on the public page, and what a team should do with one.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the projection fixtures: each applies a rule that already exists under a declared medium, beside its twin, and the six on the screen give one fixture to each row.

## Where the field leads

The field leads on people. A team that tests a service with a screen reader, or a spoken interface with its users, perceives each medium. The grid's projection is measured by instrument, and the document says so: the fixtures are "projected by instrument, not as verified by a person". A person's perception of each medium is the gate that comes after.

The field leads on the medium's own standards. What a medium carries is, in Zayn's data, "derived by reasoning about each medium's properties, not by rendering anything", and chapter 12 reads it.

Zayn leads on a map that is finite and counted. The verbs are closed and the media are closed, so the grid has a fixed number of cells, a closed cell is refused by the verifier, and an empty cell is printed on the public page with its count.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The grid on this page is counted at each build from the placement of the rules, the media and the verbs each activity owns, and its figures equal those of the Zayn site. The projection fixtures show that rules which name no medium answer on sound, voice, a program and print as on a screen, and one projection on print is recorded as a gap of fact. The placement is a reading, measured by a second reader and ruled on. The {{n:grid.empty}} empty cells are each within reach of a rule that names no medium, and the next rules will be written for them once their projection is measured and a product that ships in their medium is named.

## In your hands

Here an AI agent is the user: it orders stock through a supplier's interface for programs. A `VIBE` with `SURFACE_AS machine` says that the surface is read by a program. Write the code you expect, then open the verifier's answer.

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

Now place it on the grid. The report cites Rule 16, and the law's placement puts Rule 16 on decide, act and trust, with no medium named. The `VIBE` says the medium is a program. So the declaration lands on decide, act and trust by machine: look at the table, and you will find three empty cells. Repair the declaration. Try before you read on.

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

Clean. What is a confirmation when the user is an AI agent reading a surface made for programs? The data of the medium says of it: "What a screen reader can operate, an agent can operate". Whether that holds for a confirmation is a question the clean run does not settle, and the grid's count says the same: no rule is written yet for decide by machine.

A cell is a place where a rule can stand. Part VI asks who reads the interface that the rules describe: two cultures, under one law.
