---
id: one-declaration-ten-channels
part: 5
number: 12
title: "One declaration, ten channels"
stage:
  built: "the media as data: {{n:media.total}} media, each described by {{n:media.properties}} properties and by what it does with each of the law's verbs; the verifier's refusal of a promise that the declared medium cannot carry, of a status that it renders as nothing, and of a medium outside the list, each with its fixtures; the renderings of a status recorded for {{n:media.rendered}} media"
  designed: "the rendering of one declaration on each medium; a field that declares how a user on a passing medium asks again"
  next: "the media of voice, print, light and signs taken in turn, and the law served to AI agents through the machine medium"
status: draft
research: research/ch12.md
fixtures: [verb-not-carried, verb-not-carried-lawful, signal-unperceivable, signal-unperceivable-lawful, unknown-medium, projection-machine-cancel, projection-machine-cancel-lawful, projection-print-promise, projection-print-promise-lawful]
---

A medium is the way an interface meets its user: a screen, a sound, a voice, a printed page, a lamp, a program that reads it. The Zayn site calls it a channel. In this chapter I write one declaration once, with no medium named, and check it on several media. Each medium is a row of data, and the verifier reads that row to refuse what the medium cannot carry.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces. The **verifier** is the program that checks a declaration against the law. A **verb** is one of the law's {{n:law.verbs}} words for what a user does: discover, read, select, act, undo, and the others.

## The field

The field adapts one document to several media. The W3C's Media Queries let an author write one stylesheet per medium: `print` "Matches printers, and devices intended to reproduce a printed display", and `screen` "Matches all devices that aren't matched by print." The specification also keeps a list of media types it has retired, speech among them, which a browser "must make … match nothing".

And the field asks that meaning never rest on one sense. The accessibility guidelines say that instructions "do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound", and that colour "is not used as the only visual means of conveying information".

Each source was read on 23 November 2026, and Appendix F lists them. So the field styles one document for each medium, and guards each meaning against a single sense.

## The principle

**A declaration is written once, for every medium; the medium it names decides which of its promises can be kept, and the verifier refuses those that the medium cannot keep at all.**

The contract, the file that binds each kind of finding to the law, gives the rule behind it in one sentence: "A new medium adds renderings, never verbs." The verbs stay the same on every medium, and each medium says which of them it can carry.

## Ten media, as data

Each medium is a row of Zayn's data of the media. Six properties describe it: how long what it shows lasts, whether it shows things one after another or all at once, whether the user chose to look at it, how much it can carry at a time, whether it can change, and whether it can take back what it showed. And for each of the law's verbs, the row says whether the medium carries it natively, carries it at a cost, or does not carry it at all.

{{media}}

The last column is the data's field `soleCarrier`: a medium marked no should never carry a surface on its own. The data's note on sound gives the reason: "sound is the first thing switched off". Across the ten rows, {{n:media.cells}} pairs of a medium and a verb: {{n:media.native}} carried, {{n:media.degraded}} carried at a cost and {{n:media.absent}} not carried. The data says why the media are a list and not a matter of taste: "a new channel is classified rather than argued about."

## The same declaration, on four media

Here is a review of overdue invoices, written with no medium named.

::: plate A review of overdue invoices, on no medium
```zayn invoices.zayn
DEFINE INTENT_FLOW review_overdue_invoices (
  SATISFIES [DISCOVER, LOCATE, SCAN, COMPARE, READ],
  SIGNALS [danger, warning, muted]
)
//--> clean
```
In words: A user discovers the overdue invoices, goes to one, scans them, compares them and reads one. The values carry three statuses: danger, warning and muted.
:::

Clean. With no medium named, the declaration is checked by the law that holds on every medium. A `VIBE` is the kind of declaration that names a medium, in its field `SURFACE_AS`. Here is the same review, shown by a lamp.

::: plate The review, shown by a lamp
```zayn invoices.zayn
DEFINE VIBE invoices_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW review_overdue_invoices (
  SATISFIES [DISCOVER, LOCATE, SCAN, COMPARE, READ],
  SIGNALS [danger, warning, muted]
)
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
```
In words: The same review, and the surface is a lamp.
:::

Refused, once for each verb a lamp cannot carry: a lamp lets a user discover that something is wrong, and it cannot be scanned, compared or read. The declaration is the same; the medium decides. Here is the same review on a voice line.

::: plate The review, on a voice line
```zayn invoices.zayn
DEFINE VIBE invoices_voice (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW review_overdue_invoices (
  SATISFIES [DISCOVER, LOCATE, SCAN, COMPARE, READ],
  SIGNALS [danger, warning, muted]
)
//--> clean
```
In words: The same review, and the surface speaks and listens.
:::

Clean, though the data records that a voice carries scanning, going to an item and comparing at a cost. The cost is for the designer to read in the data, and it raises no finding. The data's own line on it: "Only 'absent' raises a diagnostic." Now two media in one file: a screen and the lamp beside it.

::: plate A screen, and a lamp beside it
```zayn invoices.zayn
DEFINE VIBE invoices_screen (
  SURFACE_AS visual
)

DEFINE VIBE invoices_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW review_overdue_invoices (
  SATISFIES [DISCOVER, LOCATE, SCAN, COMPARE, READ],
  SIGNALS [danger, warning, muted]
)
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
//--> VERB_NOT_CARRIED review_overdue_invoices
```
In words: The same review, drawn on a screen and shown by a lamp.
:::

The same four refusals. Every medium that a file names applies to every declaration of the file, so the screen does not carry what the lamp cannot.

## A medium the law does not know

The list of media is closed. Here is a lamp named in a word of its own.

::: plate A lamp, in a word of its own
```zayn desk.zayn
DEFINE VIBE desk_lamp (
  SURFACE_AS lamp
)

DEFINE INTENT_FLOW notice_overdue_invoices (
  SATISFIES [DISCOVER, READ]
)
//--> UNKNOWN_MEDIUM desk_lamp
```
In words: The surface is a lamp, named in a word the law does not have, and a user discovers and reads the overdue invoices.
:::

Refused: the medium is outside the list. The data's name for a lamp is `luminous`, "Indicator light, lamp, beacon". Here is the same file with the law's word.

::: plate The lamp, named as the law names it
```zayn desk.zayn
DEFINE VIBE desk_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW notice_overdue_invoices (
  SATISFIES [DISCOVER, READ]
)
//--> VERB_NOT_CARRIED notice_overdue_invoices
```
In words: The same lamp, named by the law's word, and a user discovers and reads the overdue invoices.
:::

Named rightly, the lamp brings its own refusal: it cannot be read. The repair asks of a lamp what a lamp can do.

::: plate What a lamp can do
```zayn desk.zayn
DEFINE VIBE desk_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW notice_overdue_invoices (
  SATISFIES [DISCOVER, UNDERSTAND]
)
//--> clean
```
In words: The lamp lets a user discover that invoices are overdue, and understand it.
:::

Clean.

## A status that sounds like nothing

A medium also renders the statuses of a declaration, the five words of `SIGNALS`. On a voice line, `muted` is rendered as silence. Here is a queue that a user hears, whose only status is that one.

::: plate A queue whose only status is silence
```zayn queue.zayn
DEFINE VIBE queue_line (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW hear_queue_status (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [muted]
)
//--> SIGNAL_UNPERCEIVABLE hear_queue_status
```
In words: The surface speaks and listens. A user discovers and understands the state of a queue, and its values carry one status: muted.
:::

Refused, under Rule 82 and the right to know: every status the surface declares is rendered as nothing on this medium. Silence is the right rendering of `muted`, and the contract says so: "silence is the CORRECT rendering of 'waiting, inactive'". The defect is a surface that has nothing else to say. The repair gives it a status that sounds.

::: plate A queue with a status that sounds
```zayn queue.zayn
DEFINE VIBE queue_line (
  SURFACE_AS voice
)

DEFINE INTENT_FLOW hear_queue_status (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [warning, muted]
)
//--> clean
```
In words: The same queue, and its values carry two statuses: warning and muted.
:::

Clean. The data records how {{n:media.rendered}} media render each status: the screen, sound and voice. On the other media the check answers clean, because the data holds no rendering for it to read.

## The machine medium

One medium is read by a program: `machine`, "Consumed by a program". Its user can be an AI agent. The data's note on it ties three kinds of user together: "What a screen reader can operate, an agent can operate and a non-visual medium can render." Here is a batch that a program submits.

::: plate A batch submitted by a program, with no way to abandon it
```zayn batch.zayn
DEFINE VIBE ledger_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW submit_batch (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, EXIT],
  ACTOR integration
)
//--> MISSING_CANCEL submit_batch
```
In words: The surface is read by a program. An integration confirms and a batch is submitted; undo and exit stay within reach.
:::

Refused: a flow that acts must keep cancel within reach, and the rule holds for a program as for a person. The repair keeps it there.

::: plate The batch, with cancel within reach
```zayn batch.zayn
DEFINE VIBE ledger_api (
  SURFACE_AS machine
)

DEFINE INTENT_FLOW submit_batch (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR integration
)
//--> clean
```
In words: The same batch, and cancel stays within reach too.
:::

Clean. Part IX reads this medium at length, where the user is an AI agent.

## What I refused

**I made the medium a part of the law.** In my pass of 13 August 2026 Rule 82 became *Perceivable State*: a state the system knows must be perceivable "in the medium the surface declares". The docket, the file where changes to the law are ruled, calls it "the load-bearing amendment of the medium axis."

**I refused a haptic rule without a device.** In the same pass a rule whose title promised a law of touch was renamed for what it governs, and the docket's line is: "the haptic law waits for device evidence".

**I refused a promise the medium cannot keep.** A promise of the way back on a printed page once passed, because the check read only what a declaration does and not what it keeps within reach. On 2 November 2026 I ruled that it was "silence hiding an error, so the verifier changes".

**The data refuses a medium by taste.** A medium enters the list by its properties, and the data names one word it kept out: "ambient is deliberately NOT a medium."

[AUTHOR: the stake of this chapter, in your words: why one declaration must hold on every medium, and what changes for a team that ships on more than a screen.]

## The court

The court of a chapter is what proves it. In this chapter it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are those of the media: a verb the medium cannot carry, a status rendered as nothing, a medium outside the list, the machine medium, and a printed promise of the way back, each refused one beside its lawful twin where the suite has one.

## Where the field leads

The field leads on what runs. Its standards for a medium come from surfaces that exist and are drawn. Zayn's data of the media says of itself that it is "a first cut", "derived by reasoning about each medium's properties, not by rendering anything".

The field leads on the cost of a medium. Its guidelines for voice and for touch say how much a user can hold in mind or in hand. In Zayn a cost is data for the designer and raises no finding, and the data marks the lines that will move first: those of sound, voice and touch.

Zayn leads on refusing before the surface exists. A promise the declared medium cannot carry is refused in the declaration, on every medium the file names, with the rule that makes the medium a legal concept.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The media are data at version {{n:media.version}} of their file, and the verifier reads that data on every run; its own copy of the carriage is held equal to the data by the suite's runner. Each plate of this page was run. The renderings of a status are recorded for the screen, sound and voice, in a library of the estate. A user on a passing medium, such as a voice, keeps a right by being able to ask again, and the data names the field that would declare it as a language change that "deserves its own decision".

## In your hands

Here is a build lamp on a team's wall, and the work it asks for. A build is the run that assembles a team's product; when it breaks, the lamp turns red. Write the findings you expect, by their codes, then open the verifier's answer.

::: plate For you: a lamp that asks for a repair
```zayn build.zayn
DEFINE VIBE build_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW repair_broken_build (
  SATISFIES [DISCOVER, UNDERSTAND, RETRY],
  ALWAYS_REACHABLE [CANCEL],
  SIGNALS [danger, success]
)
//--> VERB_NOT_CARRIED repair_broken_build
//--> VERB_NOT_CARRIED repair_broken_build
```
In words: The surface is a lamp. A user discovers that the build is broken, understands it and retries it, with cancel within reach. The statuses are danger and success.
:::

A lamp cannot retry or cancel. The repair that comes to mind is to add the console where the build is repaired, in the same file. Say what you expect.

::: plate The lamp, and the console beside it
```zayn build.zayn
DEFINE VIBE build_lamp (
  SURFACE_AS luminous
)

DEFINE VIBE build_console (
  SURFACE_AS terminal
)

DEFINE INTENT_FLOW repair_broken_build (
  SATISFIES [DISCOVER, UNDERSTAND, RETRY],
  ALWAYS_REACHABLE [CANCEL],
  SIGNALS [danger, success]
)
//--> VERB_NOT_CARRIED repair_broken_build
//--> VERB_NOT_CARRIED repair_broken_build
```
In words: The same repair, on a lamp and on a console.
:::

The same refusals: the lamp's medium applies to every declaration of the file. Give each medium its own file and its own work. Try before you read on.

::: plate The lamp's file
```zayn build-lamp.zayn
DEFINE VIBE build_lamp (
  SURFACE_AS luminous
)

DEFINE INTENT_FLOW notice_broken_build (
  SATISFIES [DISCOVER, UNDERSTAND],
  SIGNALS [danger, success]
)
//--> clean
```
In words: The lamp lets a user discover that the build is broken, and understand it.
:::

::: plate The console's file
```zayn build-console.zayn
DEFINE VIBE build_console (
  SURFACE_AS terminal
)

DEFINE INTENT_FLOW repair_broken_build (
  SATISFIES [DISCOVER, UNDERSTAND, RETRY],
  ALWAYS_REACHABLE [CANCEL],
  SIGNALS [danger, success]
)
//--> clean
```
In words: On the console a user discovers the broken build, understands it and retries it, with cancel within reach.
:::

Both clean. Now look at the lamp's file alone. The data says a lamp should never carry a surface by itself, and the file passes. Nothing in the two files says that the lamp and the console are one surface. Should a declaration name the media that carry it together? That is a remark for the law, filed with this book's requests to Zayn.

The next chapter crosses the media with what a user does, and counts where the law's rules stand.
