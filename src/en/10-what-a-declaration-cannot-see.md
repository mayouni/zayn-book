---
id: what-a-declaration-cannot-see
part: 4
number: 10
title: What a declaration cannot see
stage:
  built: "the verifier's reading of a declaration at the levels it holds, run on this page; the declaration's half of Rule 79 and of Rule 119, refused and repaired; the numbered checks of the painted page, {{n:audit.checks}} in Zayn's design system: {{n:audit.paint}} run by the audit on the page at {{n:audit.widths}} widths in two cultures, the others read in the site's files; a menu's structure moved from the drawing into the declaration"
  designed: "the contract's one kind of finding at level 4, `LAYOUT_DISPLACEMENT`, as a refusal; today the audit's K22 measures what it names; an audit that reads the drawing while it is painted, in a renderer that Softanza owns; the strata of expression as a proposal of the project states them, beyond the fields that chapter 11 runs"
  next: "the second half of Rule 129, which the audit decides once a declaration names the column that must survive; rules moved up the enforcement ladder as their instruments are built"
status: draft
research: research/ch10.md
fixtures: [missing-undo, missing-undo-lawful, role-acts-without-consequence, role-acts-without-consequence-lawful, menu-landing-not-first, menu-lawful, field-misplaced, field-misplaced-lawful]
---

A declaration sees what a user is doing: the verbs the user performs, what stays within reach, the promise a control makes, the meaning a status carries. It names no widget, no layout and no colour, by design. In this chapter I draw the line where its sight ends. I take one clean declaration and put two drawings under it, one of them carrying the seven faults the record names. Then I take two of those rules and show each split in two: the half the verifier refuses in the declaration, and the half that only the drawing shows. Last, I show what reads the drawing, and the line moving.

If you open the book here, a few words come first. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law, and a **finding** is one entry of its report, a refusal when it is an error. **The drawing** is what a medium shows of a declaration: a screen, a voice, a printed page. The painted page is the drawing in a browser.

## The field

The field holds two objects apart, and it has a name for each.

The first is the interface before any medium. A Working Group Note of W3C of April 2014, *Abstract User Interface Models*, describes an abstract user interface, and says that it "is said to be independent of any interaction modality (e.g., graphical, vocal, haptic, 3D)". The same Note asks that the abstract model make no reference to the concrete user interface, the level where a modality and its controls are chosen.

The second is the product, as drawn. W3C's methodology for evaluating a product against its accessibility guidelines is WCAG-EM 2.0, a Group Note of July 2026. It evaluates "a representative sampling" of a digital product, and asks the evaluator to "Select a sample set that is representative of the target product to be evaluated." It says what tools add: "While most accessibility checks are not fully automatable, evaluation tools can significantly assist evaluators".

And some criteria exist only on the drawing. WCAG 2.2's Success Criterion 1.4.10, *Reflow*, at Level AA, asks that content "can be presented without loss of information or functionality, and without requiring scrolling in two dimensions", for text read downwards "at a width equivalent to 320 CSS pixels". A width is a fact of the screen, and a person or a program measures it there.

The sources were read on 26 November 2026, and Appendix F lists them. So the field describes an interface free of any medium on one side, and measures a drawn product, page by page, with people and tools, on the other.

## The principle

**A declaration says what a user is doing, never how it is drawn; one declaration stands under many drawings, and a rule broken only in the drawing leaves it clean.**

The language's specification puts the line in its list of what a declaration may not do: "No `WIDGET`, no layout, no colour. A declaration that needs to say "card" has stopped describing intent." A widget is a drawn control: a button, a card, a tile. The specification adds one field that comes close to the drawing and keeps to the meaning: `SIGNALS` "names the *meaning* a rendering must carry, and never the rendering". A rendering is the record's word for a drawing in any medium.

So the declaration and the drawing are two objects, as in the field. The difference is that Zayn's law reads both: the verifier reads the declaration, and the audit of the painted page reads the drawing.

## One declaration, two drawings

Here is the approval of a payment from chapter 8. An `INTENT_FLOW` is the steps of one intent; `SATISFIES` lists the verbs the user performs, from the law's closed list of {{n:law.verbs}}, and `ALWAYS_REACHABLE` lists the verbs kept within reach at every step.

::: plate The approval, drawn with care
```zayn payments.zayn
DEFINE INTENT_FLOW approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
//--> clean
```
In words: The user selects a payment, confirms, and approves it, with a way to undo and a way to cancel within reach at every step.
```sketch
title: Payments to approve
say: Office supplies · 420.00 · due today
control: Review
control: Approve
control: Cancel
caption: One main control, a short label, text at reading size; after approval a notice offers Undo for a few seconds.
```
:::

Clean. Now a second drawing of the same file. The ledger, the dated list of what the project found, records the case: on 12 August 2026 two payment surfaces "differing by seven broken laws" were written as the same declaration, and both ran clean. The record names the seven. Cards look like information, against Rule 119. Three main buttons compete, against Rule 8. One red serves the brand and danger, against Rules 3, 87 and 117. A message reads "Invalid input!", against Rule 40. The undo is buried in a menu, against Rule 79. The body text is 11 pixels high, against Rule 105. And a wall of text stands against Rule 123.

::: plate The same approval, drawn with seven faults
```zayn payments.zayn
DEFINE INTENT_FLOW approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL]
)
//--> clean
```
In words: The same declaration, word for word: select, confirm, approve, with undo and cancel within reach.
```sketch
title: PAYMENTS
say: Invalid input! · a paragraph of terms at 11 pixels, in the brand's red
control: Office supplies 420.00 | Rule 119
control: Approve | Rule 8
control: Export | Rule 8
control: Schedule | Rule 8
control: More ▾ (Undo inside) | Rule 79
caption: Every fault here is a fact of the drawing; the declaration under it is the same file, and the verifier gives the same answer.
```
:::

Clean again, and it must be. The declaration says that an undo is within reach, and the drawing put it in a menu. The declaration names no card, no button, no colour, no size and no sentence, so the faults of those belong to the drawing. The ledger's test ran on the law and the language of that August. This book runs the declaration at the release named under its title, and the answer is the same.

The level does not change it. A level is a stage of what a check needs to read: level 2 needs the file alone, level 3 a table of what the system knows, level 4 a painted page. The verifier holds no painted page, so at level 4 it runs the checks it holds, and on this file each of them reads the declaration alone:

```shell
$ zayn check payments.zayn --level 4
# exit 0
```

Clean at level 4, the declaration's verdict. Chapter 4 explains the run; here it shows the line. The seven faults sit past it.

## One rule, two halves

The line does not fall between rules. It falls inside them. Take Rule 79, *The Undo Covenant*, whose avoid list names "Undo buried in menus or requiring multiple steps". An `INTERACTION` is one control, and its `ROLE` is the control's promise about what it changes; `reversible` promises that what it changes can be taken back. Here is the approve control with the undo dropped.

::: plate The approve control, with no way back
```zayn approve.zayn
DEFINE INTERACTION approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE reversible
)
//--> MISSING_UNDO approve_payment
```
In words: The user selects, confirms and approves a payment, with a way to cancel within reach and none to undo, and the control promises that the approval can be taken back.
:::

Refused: "An act declares no way back: SATISFIES holds ACT, ALWAYS_REACHABLE lacks UNDO." The finding cites Rule 79, Article IV and the right to reverse. That an undo exists is the half of Rule 79 that a declaration states, and the verifier refuses its absence. One defect gets one finding. Here `ACT` is declared, so the finding is `MISSING_UNDO`. A reversible control that declares only a selection, and no act, and keeps no undo gets `ROLE_PROMISE_BROKEN` instead; an irreversible control that offers an undo gets `IRREVERSIBLE_CLAIMS_UNDO`, as the exercise below shows. The contract, the file that binds each kind of finding to the law, keeps the three apart, so that a defect is reported once. The repair is one word.

::: plate The approve control, with undo
```zayn approve.zayn
DEFINE INTERACTION approve_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)
//--> clean
```
In words: The same control, with a way to undo and a way to cancel within reach.
:::

Clean. Where the undo sits is the other half: in a toast for a few seconds, as the rule's solution puts it, or three levels down a menu, as its avoid list refuses. The declaration says it is within reach, and the drawing decides how far the hand must go. A design note of the project met the same split when it designed the roles. It withdrew a check it had planned, because "the declaration cannot see the defect": a step of review and the modal dialog Rule 79 refuses "are the same declaration with two renderings".

Rule 119, *A Card Is Not a Button*, splits the same way. Its avoid list names "Clickable tiles styled like information cards". The declaration's half is the promise: a control that acts may not promise to change nothing, and chapter 4 runs that refusal on two cards of a dashboard. Here is the payment card with an honest promise.

::: plate The payment card, honest about its act
```zayn card.zayn
DEFINE INTERACTION payment_card (
  SATISFIES [SCAN, ACT],
  ALWAYS_REACHABLE [UNDO],
  ROLE reversible
)
//--> clean
```
In words: A card on which the user scans a payment and acts on it, with undo within reach, and which says that what it does can be taken back.
```sketch
title: Payments to approve
control: Office supplies · 420.00 · due today
caption: Drawn as a quiet card of information, it hides that a tap acts. The declaration is honest; the drawing is the fault Rule 119 names.
```
:::

Clean. The promise is honest and the drawing can still dress the card as information. Whether a container reacts under the pointer is a fact of the painted page, and the audit reads it.

## What reads the drawing

The audit of the painted page is a page of Zayn's repository, `tools/ui-audit.html`, that opens a page in a browser and measures what is drawn. Zayn's own design system numbers its checks K01 to K37, {{n:audit.checks}} in all. The audit's larger mode runs {{n:audit.paint}} of them on the painted page, at {{n:audit.widths}} widths from 320 to 1900 pixels, in both of the site's cultures, the two ways it draws the same interface. The other {{n:audit.files}} read the site's files, the words and the markup, in the tool that builds the site. The design system gives the principle in italics: "*The painted page is the instrument.*"

Each check reads one property of every element that has it. Here they are grouped by what they read; the grouping is mine, and the design system files each by the cause of the corrections it answers, which chapter 2 tells:

| What a check reads | Checks |
|---|---|
| the size and contrast of every text | K01, K02 |
| lines of text and of code | K03, K11, K27, K28 |
| boxes: size, fill, distance, room | K04, K05, K06, K12, K17, K23, K24, K35 |
| ink: lines, emphasis, colours, cues | K07, K08, K09, K10, K25, K29, K31 |
| scroll, overlap and the flow of regions | K13, K14, K26, K34 |
| what reacts under the pointer | K15, K16 |
| the page in time: loading, acting, answering | K22 |
| what loaded: a photograph, an image | K32, K33 |
| an editor driven: maximised, dragged | K36, K37 |
| the files: words, register, markup | K18, K19, K20, K21, K30 |

Five of the seven faults meet a check. K16 SHAPE reads a card that reacts under a link. K09 PALETTE and K10 ONE_CRITICAL read the colours. K01 TYPE_SCALE reads the size of the text and K02 TEXT_CONTRAST its contrast. K03 MEASURE reads the length of a line, and K19 the register of the words in the files. The pairing is mine. The other two are read by a person: the three main buttons that compete, and where the undo sits. Chapter 17 gives the audit's recorded runs.

## The line moves

The line between the two objects is a ruling, and it has moved.

It moved into the declaration. On 8 November 2026 I read a menu whose section had lost its first entry, and I ruled that "you must add this as an issue that is statically checked in Zayn". The language gained `NAV_GRAPH`, a declaration of a menu. The docket, the file where changes to the law are proposed and ruled, records the division: "the verifier now decides three of its demands from a declaration, and the UI audit the rest on a painted page". Chapters 18 and 19 run it.

And the record, the files of Zayn's repository at the release this book reads, shows where it will move again, the other way. Rule 129, *The Action Is the Last Thing to Go*, asks that the column a user acts on be the last a narrow screen gives up. The docket says of its second half: "An auditor can prove nothing is clipped; proving *the actionable column* survived needs the surface to say which column that is." The audit reads the drawing, and it needs the declaration to say what to look for. The two instruments divide one rule between them.

## What I refused

**A widget in the language.** The specification excludes `WIDGET` "on constitutional grounds", because admitting it "would let a declaration name a rendering". The inversion it protects is Article II's: widgets are consequences of intent, never primitives.

**A check the declaration could not hold.** The design of the roles planned a check that a reversible act must not ask for confirmation. It was withdrawn before it was built, with the reason quoted above: "Rule 79's dialog clause is a fact about a rendering, not about a declaration". It went to the audit's side of the line, recorded with its reason.

**Silence on a field that nothing reads.** A field placed on a kind of declaration that does not read it, a `TONE` on a `SCREEN`, did nothing, and the verifier said nothing. The contract's note on the finding that closed it says of whoever wrote the field: "the author believed it was honoured. That silence was the defect". Since then the verifier refuses it, `FIELD_MISPLACED`, and chapter 7 runs it. A declaration that the verifier accepts says only what it reads.

**A rule for a column, where a rule already stood.** The corrections made to a status dashboard of the platform, gathered as evidence, proposed a rule: a status row ends in the action it requires. The docket refused it as new law, because Rule 82 already held the demand: "The *column* does not; a surface may express an obligation any way it likes." What the law keeps is that an obligation is perceived; how it is drawn stays the drawing's.

[AUTHOR: the stake of this chapter, in your words: what you saw in the two drawings of one declaration, and why the law must reach the drawing as well as the intent.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, holds the declaration's side of the line. An act with no undo, refused, and its twin with one. A card that promises to change nothing and acts, refused, and its twin made reversible. A menu whose landing entry comes second, refused, and a lawful menu: the line moved by a ruling. A field on a kind that does not read it, refused, and its twin with the field in its place. Beside them the manifest of the suite lists `LAYOUT_DISPLACEMENT` apart, the one kind of finding it gives to the painted page.

## Where the field leads

The field leads in the drawing's breadth. Its methodology samples a whole product, its criteria fix widths and ratios on the screen, and its tools, as WCAG-EM says, "can significantly assist evaluators". Zayn's audit reads the pages of one site, Zayn's own, against its own design system. For a product of your own, the declaration can be required of a supplier and refused by the verifier; the drawing answers to the instruments of the painted page the project adopts, and to a person's review.

The field leads in time, too. The record's reflection on a renderer that Softanza owns says that level 4 is reached today by the audit, on a page served from the audit's own site, "after the fact". The verifier reads the declaration before anything is drawn; the audit reads the drawing after.

And a person reads what neither instrument reads. The Zayn site says it in one sentence: "A declaration cannot say whether a page *looks* right, or whether a person understood it." The design system keeps the last gate for people: "the perceptual row is the gate no check replaces".

Zayn leads in the division. The field keeps its abstract interface as a model and its drawn product as the object of conformance. Zayn binds both to one law: a rule's half that a declaration states is refused before the drawing exists, and a rule's half that the drawing shows is measured on the painted page where a check reads it, and judged by a person for the rest.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the verifier's reading of the declaration at the levels it holds, run on this page. The declaration's half of Rules 79 and 119, refused and repaired. The numbered checks of the painted page, {{n:audit.checks}} in the design system: {{n:audit.paint}} run by the audit on the page at {{n:audit.widths}} widths in both cultures, and the others read in the site's files. A menu's structure decided from a `NAV_GRAPH` declaration. Designed: the contract's kind at level 4, `LAYOUT_DISPLACEMENT`, as a refusal; the audit's K22 measures what it names today. An audit that reads the drawing while a renderer that Softanza owns paints it. The strata of expression as a proposal states them, beyond the fields that chapter 11 runs. Next: the second half of Rule 129, once a declaration names the column the audit must find; rules moved up the enforcement ladder as their instruments are built.

So a clean declaration says that what a user is doing keeps every rule the verifier checks. The drawing answers to the checks of the painted page, and to a person for the rest.

## In your hands

Here is the payment once more, this time sent to the bank, where a sent payment cannot be called back. The first draft still promises an undo. Write what you expect the verifier to answer, then open its answer.

::: plate For you: sending the payment
```zayn send.zayn
DEFINE INTERACTION send_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE irreversible
)
//--> IRREVERSIBLE_CLAIMS_UNDO send_payment
```
In words: The user selects a payment, confirms and sends it, the control says the send cannot be taken back, and an undo is within reach.
:::

Repair it, and say what you expect. Two lawful repairs follow, and they say different things. Try before you read on.

::: plate The send that cannot be undone
```zayn send.zayn
DEFINE INTERACTION send_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL],
  ROLE irreversible
)
//--> clean
```
In words: The user selects, confirms and sends; the send cannot be taken back, and a way to cancel stays within reach until it is sent.
:::

::: plate The send that can be recalled
```zayn send.zayn
DEFINE INTERACTION send_payment (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)
//--> clean
```
In words: The user selects, confirms and sends; the send can be taken back, with undo and cancel within reach.
:::

Both clean. Which is true depends on the bank: whether it can recall a payment is a fact of the system, and the declaration states it. Once you have chosen, the rest is the drawing's: whether the confirmation is a step of review or the dialog Rule 79 refuses, and where the cancel sits on the screen. Which of the two is true of your bank, and how will the drawing show it?

[AUTHOR: is the payment that cannot be recalled the defect you want the reader to repair here, or one from your own work?]

The two drawings of this chapter differ in things the language leaves to the drawing. *The Second Founding*, a proposal of the project for a new base of the law, which awaits my ruling, designs words for them, and the next chapter takes them one by one.
