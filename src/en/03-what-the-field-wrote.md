---
id: what-the-field-wrote
part: 2
number: 3
title: What the field wrote
stage:
  built: "the rules that keep the field's ground in the law's data, each with its article and its tier; the verifier's refusals of a state shown nowhere, of an act with no undo, of a selection that acts and of a status outside the list, run on this page"
  designed: "the expression fields proposed in the second founding, of which `SIGNALS` is built; the symbol table computed from a project, described in a design document"
  next: "the law of touch feedback, which waits for the devices' evidence"
status: draft
research: research/ch03.md
fixtures: [invisible-state, missing-undo, missing-undo-lawful, select-act-collapse, select-act-lawful, unknown-signal, unknown-signal-lawful, missing-cancel, missing-cancel-lawful]
---

The field of human-computer interaction wrote down what a good interface does: it keeps the user informed, lets the user go back, prevents the error, and keeps one meaning for one sign. In this chapter I read four of its sources and show where Zayn's law keeps each piece: as a numbered rule, under an article, filed at a tier. Where the verifier checks that rule by name, the piece becomes a refusal it prints before anything is drawn. I run those refusals, the offending version before the lawful one. Then I show the ground a declaration leaves to the painted page.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

Two more words serve this chapter. A **heuristic** is a broad rule of thumb that a reviewer judges an interface against; it names no pass or fail. A **tier** is the word under which the law files a rule, for the instrument that owes its check: `machine`, `tool`, `machine-later` or `judgment`. A proposal of the project glosses `judgment` as "a human decides, until an instrument is invented". Chapter 17 reads the four.

## The field

Jakob Nielsen's ten usability heuristics, on a page of the Nielsen Norman Group dated 1994 and last reviewed in 2024, open on "Visibility of System Status". Its sentence: "The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time." The third heuristic is "User Control and Freedom", with a clearly marked "emergency exit" and the tip "Support Undo and Redo." The fourth is "Consistency and Standards". The fifth, "Error Prevention", holds that "the best designs carefully prevent problems from occurring in the first place". The sixth is "Recognition Rather than Recall".

Ben Shneiderman's *Eight Golden Rules of Interface Design*, in the version of the sixth edition of his book (2016), cover the same ground in their own order. Among them are "Strive for consistency", "Offer informative feedback", "Prevent errors", "Permit easy reversal of actions" and "Reduce short-term memory load".

A page of the Nielsen Norman Group gives the origin of the two gulfs: "The terms gulf of evaluation and gulf of execution were invented in 1986 by Ed Hutchins, Jim Hollan, and Don Norman". Evaluation is "Understanding the state of the system"; execution is "Taking action to accomplish a specific goal". Edward Tufte's *The Visual Display of Quantitative Information*, of 1983 with a second edition in 2001, lists among its subjects "The data-ink ratio."

Each of these four sources was read on 21 or 25 November 2026, and Appendix F lists them. My outline of this part names three more pieces of the field: Fitts's law, Hick's law and the Gestalt principles. This chapter shows them through the law's own words, in its rules on the size of a target, the number of choices and grouping. So the field wrote advice: what a good interface does, for a designer to apply and a reviewer to judge.

## The principle

**The field wrote what a good interface does; the law turns into a refusal the part a declaration can state, and leaves the rest to the person who judges the painted page.**

The Zayn site says it in one line: "The heuristic judges what only a person can judge, and the law refuses what a machine can see before a pixel exists." A heuristic and a rule can carry the same knowledge, and they differ in force: a heuristic informs a judgment, and a rule bound to a kind of finding refuses a declaration by name.

## State the user must see

Visibility of system status, seen from the user's side, is the gulf of evaluation. The law's Article III says: "If the system knows something important, the user must see it". And: "Invisible state is a violation." Rule 82, *Perceivable State*, carries it with its reason: "A user who reasons from state they cannot perceive has been harmed by the interface."

A `NAV_GRAPH` declares a navigation, and its `VISIBLE_STATE` names the state the navigation itself must show. To know what the system holds, the verifier reads a symbol table: a small file that lists the system's state, its actors and its entities. A level is how much the verifier is given. Each level adds to the one below. Level 1 reads the file's grammar and words; level 2 adds the checks that need nothing but the file; level 3 adds the checks that need the table. Here a list of orders keeps a filter active and shows only the drafts.

::: plate An active filter shown nowhere
```symbols orders.json
{ "state": ["active_filter", "pending_drafts"] }
```
```zayn orders.zayn level=3 symbols=orders.json
DEFINE NAV_GRAPH orders_nav (
  SATISFIES [LOCATE],
  VISIBLE_STATE [pending_drafts]
)
//--> INVISIBLE_STATE active_filter
```
In words: In the orders, a user goes to an order, and the navigation shows the pending drafts. The system also holds an active filter.
:::

The command names the level and the table:

```shell
$ zayn check orders.zayn --level 3 --symbols orders.json
# exit 1
```

Refused, under Rule 82, Article III and the right to know. The report names the state, `active_filter`, and carries no line number: the state belongs to the system, and no surface of the file declares it. The verifier's messages say operator, the language's word for the person this book calls the user. Without `--symbols`, the verifier skips the checks that need the table. Given no table, the same file runs at level 2.

::: plate The same file, with no table
```zayn orders.zayn level=2
DEFINE NAV_GRAPH orders_nav (
  SATISFIES [LOCATE],
  VISIBLE_STATE [pending_drafts]
)
//--> clean
```
In words: The same navigation, read without the list of what the system holds.
:::

Clean: the check needs to know what the system holds, and chapter 25 shows that silence in a team's build. The repair declares the filter shown, and runs with the table.

::: plate The filter, shown
```zayn orders.zayn level=3 symbols=orders.json
DEFINE NAV_GRAPH orders_nav (
  SATISFIES [LOCATE],
  VISIBLE_STATE [active_filter, pending_drafts]
)
//--> clean
```
In words: The same navigation shows the active filter and the pending drafts.
:::

Clean. Given the table, the verifier refuses a navigation that hides what the system knows, before anything is drawn. Shneiderman's informative feedback, given in time, is the subject of Rule 18: "Actions must acknowledge the user within 100ms". The law files it under `machine-later`, the tier of a rule whose instrument comes later.

## A way back, by name

User control and freedom asks for an emergency exit and for undo, and Shneiderman asks that actions be reversible as much as possible. Rule 79, *The Undo Covenant*, carries both: "Every destructive action (delete, archive, clear) must have instant, one-click undo". An `INTENT_FLOW` is the steps of one intent. Its `SATISFIES` lists the verbs the user performs, and its `ALWAYS_REACHABLE` the verbs kept within reach at every step. Chapter 8 reads this refusal line by line; here it runs once.

::: plate An entry posted with no way back
```zayn ledger.zayn
DEFINE INTENT_FLOW post_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR accountant
)
//--> MISSING_UNDO post_entry
```
In words: An accountant confirms an entry and posts it, with cancel and exit within reach.
:::

Refused, under Rule 79, Article IV and the right to reverse: "What was done can be undone, and what cannot says so before, not after."

::: plate The entry, with undo in reach
```zayn ledger.zayn
DEFINE INTENT_FLOW post_entry (
  SATISFIES [CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR accountant
)
//--> clean
```
In words: The accountant confirms and posts the entry, with undo, cancel and exit within reach.
:::

Clean. The Zayn site draws this link itself: control and freedom, and error prevention, "cover the same ground as the law's undo, cancel and exit rules (Rules 79, 26 and 51)". What Zayn adds, in the site's words: "Refusal."

## Interest before commitment

Error prevention is the fifth heuristic, and Shneiderman's rule asks a designer to shape the interface "so that users cannot make serious errors" as far as possible. One error the law prevents by name is a selection that acts: the user picks an item, and the pick pays. Article II says it in one sentence: "Selection never implies execution; a flow that traps is unconstitutional."

::: plate A choice that pays
```zayn pay.zayn
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR customer
)
//--> SELECT_ACT_COLLAPSE pick_and_pay
```
In words: A customer selects an item, and the selection pays, with undo, cancel and exit within reach.
:::

Refused. The report cites Rule 16, *Intentional Clicks*, and Article II, and no right. Rule 16's words are about affordance: "Every interactive element must have clear visual affordance." The sentence the refusal enforces is Article II's, so a reader who looks for error prevention in Rule 16's text finds it in the article above the rule. The repair puts a step of confirmation between interest and commitment.

::: plate The choice, confirmed before it pays
```zayn pay.zayn
DEFINE INTENT_FLOW pick_and_pay (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR customer
)
//--> clean
```
In words: The customer selects an item, confirms, and it is paid, with undo, cancel and exit within reach.
:::

Clean.

## One meaning for each status

Consistency asks that one sign keep one meaning. Rule 5 asks for "Semantic consistency", with colour as its case: a blue that means action on one page keeps that meaning on the next. Rule 118, *Two Families of Colour*, closes the list of what a status may mean: success, warning, danger, info and muted. Its reason meets recognition over recall, and Shneiderman's short-term memory: "A palette the operator can hold in their head is a language". A declaration names the meaning with `SIGNALS`, which in the specification's words names "the *meaning* a rendering must carry, and never the rendering".

::: plate A status the list does not hold
```zayn overdue.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger, critical]
)
//--> UNKNOWN_SIGNAL overdue_invoices
```
In words: On the list of overdue invoices, a user scans, compares and goes to an invoice. The list signals danger, and a meaning called critical.
:::

Refused under Rule 118, for the word `critical`, on the line where it stands. The check belongs to level 1, and the run at the default level 2 holds it. The law files Rule 118 under `judgment`, and the refusal judges a word of the list, never a colour.

::: plate Two statuses from the list
```zayn overdue.zayn
DEFINE SCREEN overdue_invoices (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger, warning]
)
//--> clean
```
In words: The same list signals danger and warning.
:::

Clean. The colour that serves danger belongs to the drawing; the meaning is the declaration's.

## Where the painted page judges

The rest of what the field wrote lies in how a page is drawn, and a declaration names no rendering. The specification says so: "No `WIDGET`, no layout, no colour." Fitts's law is about the size of a target, and the law holds two rules there. Rule 19 asks for "a minimum hit area of 44x44 pixels" for buttons in business apps, filed under `machine-later`. Rule 69, *The Hand Is Not a Mouse*, asks for "a minimum height of 48px" for every interactive element on a touch surface, filed under `judgment`. Its reason: "Fat fingers are physiology, not user error." Try to declare the size of a target.

::: plate A size the grammar does not hold
```zayn targets.zayn
DEFINE SCREEN invoice_list (
  SATISFIES [SCAN, SELECT],
  TARGET_SIZE [large]
)
//--> UNKNOWN_FIELD TARGET_SIZE
```
In words: On the invoice list, a user scans and selects an invoice, and the declaration asks for large targets.
:::

Refused, and no rule is cited: the grammar holds no field for a target's size, so the finding judges the language's words. The same screen without the field runs.

::: plate The screen, with no size
```zayn targets.zayn
DEFINE SCREEN invoice_list (
  SATISFIES [SCAN, SELECT]
)
//--> clean
```
In words: On the invoice list, a user scans and selects an invoice.
:::

Clean. The pair marks where a declaration ends and the drawing begins.

Hick's law is about the number of choices. Rule 27 limits a horizontal menu to "6-8 primary items maximum", and to five on a reading surface. Rule 24 asks a navigation to answer "Where am I?" The Gestalt principles are about grouping: both rules ask for "semantic grouping". Rule 86 places an error "beside the element that caused it". Tufte wrote about the ink of a chart. Rule 50 names him and carries the reason "Ink that is not data is noise", and Rule 128 states the data-ink ratio "as a general obligation rather than as advice about choosing charts". A person judges each of these rules on the painted page, with its number and its words in hand.

## The map, as I read it

The law names one author of the field, Tufte, in Rule 50, and Rule 128 carries Rule 50's data-ink ratio. Every other link I draw from the field to a rule is my reading of the rule's own words. The record draws two links itself: the Zayn site sets Nielsen's control and freedom, and his error prevention, beside Rules 79, 26 and 51, and a design note sets control and freedom beside the refusal of an act with no undo. Here is the map of what this chapter ran and read, with each rule's tier as the law files that rule.

| The field | The law, as I read it |
|---|---|
| Visibility of status; the gulf of evaluation | Article III; Rule 82 `machine`; Rule 18 `machine-later` |
| Control and freedom; easy reversal | Article IV; Rule 79 `machine`; Rule 26 `machine-later`; Rule 51 `judgment` (Article II) |
| Error prevention | Article II; Rule 16 `judgment` |
| Consistency | Rule 5 `judgment`; Rule 118 `judgment` |
| Recognition; memory load | Rule 118; Rule 42 `judgment`; Rule 106 `machine-later` |
| Target size (Fitts) | Rule 19 `machine-later`; Rule 69 `judgment` |
| Number of choices (Hick) | Rule 27 `judgment`; Rule 24 `judgment` |
| Grouping (Gestalt) | Rules 24 and 27; Rule 86 `machine-later` |
| Data-ink (Tufte, named) | Rule 50 `judgment`; Rule 128 `judgment` |

The gulf of execution needs no rule of its own: a declaration states it, because its `SATISFIES` names what the user means to do, in the law's {{n:law.verbs}} verbs. The verifier's findings cite Rules 82, 79, 26, 51 and 16, and the list of statuses in Rule 118; a person judges the others on the painted page.

A tier and a refusal answer two questions. The tier names the instrument the law owes the whole rule, and in the docket's words it "is honest about which instrument owes the check; it is not a claim that the check runs today". A finding refuses the part of a rule that a declaration states. That holds whatever the rule's tier. Rule 16 is filed under `judgment`, because a person judges whether a control looks clickable, and the verifier still refuses the selection that pays. Rule 26 is filed under `machine-later`, and the verifier refuses a flow with no way to cancel it today. Chapter 17 reads each tier against what refuses it.

## What I refused

**I refused a law of touch feedback before the devices give evidence.** The docket, the file where changes to the law are ruled, made the case: "The title promises a haptic law; the body is 48px touch targets, overscroll bounce and swipe actions." On 13 August 2026 I ruled the docket in one pass, and on this item: "Rule 69 renamed to what it governs; the haptic law waits for device evidence".

**I refused a rule of visible state bound to the screen.** In the same pass Rule 82 became *Perceivable State*: "Rule 82 becomes Perceivable State". Its words now ask that the user perceive what the system knows "in the medium the surface declares". An earlier numbering had cited "Rule 84, Visible State", and the law's data keeps that number out of use: "Reserved, never to be assigned".

**The law keeps one rule of undo, and its reason weighs confirmation.** The law's lineage records a reform of its version 2.0, on 3 August 2026, that retired duplicate rules into their survivors. Rule 33, *Undo over Confirm*, went into Rule 79, whose reason now carries it: "Undo trusts first and interrupts never; confirmation interrupts always and trusts nothing."

**The record keeps taste out of the law.** Its method takes a principle into the law only if a reviewer can say yes or no against it. "Principles that are taste, naming, or product strategy stay in their projects."

[AUTHOR: the stake of this chapter, in your words: why the field's advice should become a law that refuses, and what the law owes the authors whose ground it keeps.]

## The court

The court of this chapter, the fixtures of the suite that judge its claims, proves the refusals run on this page. A state the system holds and no surface shows, at level 3 with its table: the suite proves the refusal, and the lawful plate above is written for the book. An act with no undo, and its twin made lawful. A selection that acts with no confirmation, and its twin. A status outside the list, and its twin. The court adds one pair that this page leaves to it: a flow, an `INTENT_FLOW` or a `WIZARD`, that acts with no way to cancel it, and its twin. It is Rule 26, one of the three rules the site sets beside control and freedom and error prevention.

## Where the field leads

The field leads in reach. A heuristic judges any interface a person can look at, with no declaration and no table. The site says: "Usability testing and heuristic review decide things that nothing in Zayn replaces."

The field leads where the deterioration lives. The project's evidence ledger records two payment surfaces that differ by seven broken rules and whose declarations are the same byte for byte. Both run clean at level 4, and in the ledger's words "the court is silent exactly where the deterioration lives".

And the refusal of a state shown nowhere reads a table that a team supplies today; the record describes a table computed from a project, in a design document.

The law leads in force: where a declaration can state a rule's words, the field's advice becomes a refusal by name, in every file the verifier reads at the level that rule needs.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the rules of this chapter in the law's data at version {{n:law.version}}, each with its article and its tier. The verifier's refusals of a state shown nowhere, of an act with no undo, of a selection that acts with no confirmation and of a status outside the list, with the refusal of a field the grammar does not hold: all run on this page. Designed: the expression fields proposed in *The Second Founding*, the record's design document for the language's next fields, put to ratification: structure, signal, role, motion, message and tempo. `SIGNALS` is built as the first of them. Designed too: the symbol table computed from a project, which a design document describes. Next: the law of touch feedback, which waits for the devices' evidence.

## In your hands

Here is a defect in three pieces of the field at once, run at level 3 with the table of the first plate. Write the findings you expect, by their codes, then open the verifier's answer.

::: plate For you: the invoices
```zayn invoices.zayn level=3 symbols=orders.json
DEFINE NAV_GRAPH invoices_nav (
  SATISFIES [LOCATE],
  VISIBLE_STATE [pending_drafts]
)

DEFINE INTENT_FLOW pay_invoice (
  SATISFIES [SELECT, ACT],
  ALWAYS_REACHABLE [CANCEL, EXIT],
  ACTOR clerk
)
//--> SELECT_ACT_COLLAPSE pay_invoice
//--> MISSING_UNDO pay_invoice
//--> INVISIBLE_STATE active_filter
```
In words: In the invoices, a user goes to an invoice, and the navigation shows the pending drafts. A clerk selects an invoice, and the selection pays it, with cancel and exit within reach. The system also holds an active filter.
:::

Repair it, and say what you expect. Try before you read on.

::: plate The invoices, repaired
```zayn invoices.zayn level=3 symbols=orders.json
DEFINE NAV_GRAPH invoices_nav (
  SATISFIES [LOCATE],
  VISIBLE_STATE [active_filter, pending_drafts]
)

DEFINE INTENT_FLOW pay_invoice (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR clerk
)
//--> clean
```
In words: The navigation shows the active filter and the pending drafts. The clerk selects an invoice, confirms, and it is paid, with undo, cancel and exit within reach.
:::

Clean: three pieces of the field, three refusals, three repairs. Now the question the run leaves to you: can a payment be undone? If it cannot, the lawful form is chapter 8's, a control that declares its act final, and the field's two rules, prevent errors and permit reversal, meet on one button.

The field wrote its knowledge as advice, and it also built instruments that set criteria, measure the painted page and refuse code. The next chapter reads them: the instruments of the field.
