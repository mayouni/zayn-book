---
id: amendment-from-evidence
part: 7
number: 18
title: Amendment from evidence
stage:
  built: "Article VII as data; a lineage of {{n:law.lineage}} dated entries inside the law's own file; {{n:law.retired}} retired and {{n:law.burned}} reserved numbers; an evidence field on each of the {{n:law.rules}} rules; three amendments answered by the verifier on this page; {{n:pin.files}} data files that record the version of the law they were checked against, and a pack of {{n:pack.files}} files held by their hashes"
  designed: "a law in tiers, with a core that every interface keeps and a commons that a team adds to; the test and the record by which a contributed rule is admitted; a check for two rules that legislate one subject"
  next: "rules moved up the ladder as their instruments are built, and a law fed by the corrections of the people who use it"
status: draft
research: research/ch18.md
fixtures: [unknown-signal, unknown-signal-lawful, intent-orphan, field-misplaced, field-misplaced-lawful, menu-landing-not-first, menu-label-repeats-parent, menu-label-duplicate, menu-lawful]
---

An amendment is a change to what the law requires. In this chapter I tell how Zayn's law changes. I read its history in its own file, entry by entry. I tell three cases from the record: a correction that turned out to be law already, two rules that contradicted each other, and a check that ran for months before a rule was written for it. Then I count what moves when one rule moves.

If you open the book here: a declaration is a few lines that say what a user is doing on a surface; the law is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; the verifier is the program that checks a declaration against it; and a finding is one entry of the verifier's report, a refusal when it is an error.

## The field

The field amends its standards by versions. The Web Content Accessibility Guidelines are at version 2.2, a W3C Recommendation. Its page lists the success criteria that are new in 2.2, and W3C's page on what is new says that the criteria of 2.0 and 2.1 are "essentially the same in 2.2, with one exception": criterion 4.1.1, which is "obsolete and removed". The standard prints the reason under the criterion's number: assistive technology "no longer has any need to directly parse HTML". The number stays on the page, with its note.

The W3C Process Document says how a Recommendation changes after it is published. It names a correction and an addition, and calls the two together "candidate amendments".

A statute can then name one version. The fact sheet of the United States rule on the web content of state and local governments names "Version 2.1, Level AA" as its technical standard, with dates of compliance in April 2027 and April 2028.

A design system grows by criteria. The GOV.UK Design System asks of a proposal that there be evidence it would be "useful for many teams or services", and that it be unique. A linter does the same for its rules: ESLint lists guidelines for a core rule, and says that since 2020 it accepts only rules "related to new ECMAScript features".

And the field has a convention for what a version number promises. Semantic Versioning gives the first number to "incompatible API changes", the second to added functionality, the third to fixes.

Each of these was read at its source on 23 November 2026, and Appendix F lists them.

## The principle

**The law changes only on evidence, and every change stays on the record: its date, its cause, and what it replaced.**

The law says so itself, in its last article.

{{article:amendment}}

The article sets two burdens. To add a protection, the harm must be shown. To remove one, the harm must be shown to be gone. It names what is not a ground. And its last sentence is about numbers: a rule's number is a name, and a name that is given twice means two things.

## The lineage, entry by entry

The law carries its history in its own file. The lineage is one dated entry for each state of the law: {{n:law.lineage}} entries, from version 2.0 on 3 August 2026 to version {{n:law.version}} on 12 November 2026. Most entries canonize a rule, which means that they give it a number and a place in a set. Some amend a rule and add none. Three are corrections. Three change a word or a name.

What tells an amendment from a correction? One question, which the record calls the substance test: "does any interface that was lawful before become unlawful after — or must any conforming implementation change anything it does?" If the answer is no, the change is a correction, "however much prose changed". The entry of 6 August 2026 is the first of them: two pointers named a file that had moved, and no requirement moved with them.

The numbers keep their own history. The rules are numbered up to {{n:law.highest}}, and the law holds {{n:law.rules}}: {{n:law.unused}} numbers are out of use. {{n:law.retired}} are retired: each was a duplicate, folded into the rule that survives it, and the survivor says which number it absorbed. {{n:law.burned}} are reserved for good, because older documents had cited them for something else. A number proposed for a rule is checked the same way. Rule 126 was first written as 125, and the docket had kept 125 for another rule. The docket is the file where changes to the law are proposed together and ruled item by item, and its own words for that lesson are: "a proposed number is not a free number".

Each of the {{n:rule.evidence}} rules carries a field named `evidence`: what happened, where and when. An amended rule keeps its first evidence and gains a dated clause after it. The record's rule for that field is short: "Evidence is never corrected."

## A correction that was already law

In August 2026 a session that had not opened the law built a status dashboard for me. I rejected two versions and corrected the third. The ledger, which is the dated list of the project's findings, says what those corrections were worth: "Every correction he made was already law."

The first version was a grid of tiles, then cards with coloured meters. My words, as the ledger keeps them: "use a classical table format not cards, it's more direct and less stressing to me". Two rules already forbade the cards. The second showed two red blocks, one under the other. Mine again: "having two red divs one under the other means we are not focusing on one critical thing." That was a rule too. Then every table was wrapped in a container that scrolls sideways, which one rule forbids, and when that was removed each row was stacked into a block, which another rule forbids.

So what did the episode add to the law? Five candidates were put to the docket on 15 August 2026. Two were refused as new law, because each was a rule that existed, and each of those rules was extended by a sentence. Three were canonized. One of them is Rule 129, and the docket says what was new in it: "which column survives when width genuinely runs out". On a narrow screen the column that was hidden had carried the user's next action.

Why is this evidence, and not compliance? Because the law was closed while it happened. The ledger: "Nobody consulted `rules.json` while it happened". It also states the size of the case, and so do I: "one surface, one operator, one implementer".

## Two rules that contradicted each other

On 16 August 2026 two rules were put side by side for the first time, Rule 3 and Rule 118. Both speak of colour. Rule 3 kept the colour of danger for a failure of the system. Rule 118 gives `danger` to a value that is critical or exceeded. So a credit limit that is exceeded, coloured as danger, obeyed one rule and broke the other.

Which rule wins? The law has no rule that says so, and the ledger records it in one line: "The constitution has no precedence mechanism at all." I had delegated that pass, and the docket records it as a delegation. It did not choose a winner. It amended both rules until they no longer overlapped: "Rule 3 owns chrome. Rule 118 owns what a colour means about a record." Chrome is the frame of an interface: its bars, its borders, its controls. Each rule now points at the other, in a field named `see_also`, and {{n:rule.see_also}} rules carry such a pointer.

The language took Rule 118's five statuses the same day, as the closed list of the field `SIGNALS`. Here is a screen that uses two words of chrome as statuses.

::: plate Two words of chrome, as statuses
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger, neutral, accent]
)
//--> UNKNOWN_SIGNAL credit_limits
//--> UNKNOWN_SIGNAL credit_limits
```
In words: On the screen of credit limits a user scans, compares and goes to a limit. Its values carry three statuses: danger, neutral and accent.
:::

Two refusals, and both cite Rule 118. The word `danger` passes. The other two belong to the frame, and the frame is Rule 3's.

{{rule:118}}

::: plate An exceeded limit, said as danger
```zayn limits.zayn
DEFINE SCREEN credit_limits (
  SATISFIES [SCAN, COMPARE, LOCATE],
  SIGNALS [danger]
)
//--> clean
```
In words: The same screen. Its values carry one status, danger: here, a limit that is exceeded.
:::

Clean! The docket says what the amendment did for this declaration: what "was forbidden by one rule and required by another" is now lawful. By the substance test it is still an amendment, because a tool that conforms had to change what it does.

## A check that became a rule

The usual order is a defect, then a rule, then a check. Once the order was reversed. The check `INTENT_ORPHAN` had run since the first version of the language and cited Article II alone: no numbered rule stood behind it. On 2 November 2026 Rule 130 was written for it, and the law went to version 3.12.

::: plate An element the inventory holds
```zayn balance.zayn level=3 symbols=screen.json
DEFINE COMPONENT balance_card (
  SATISFIES [READ]
)
//--> INTENT_ORPHAN export_button
```
In words: The balance is something a user reads. The inventory of the screen holds a second element, an export button, and no declaration says what a user does with it.

```symbols screen.json
{
  "elements": ["balance_card", "export_button"]
}
```
:::

Refused, and the third line of the report cites Rule 130. Before version 3.12 the same file got the same refusal, and its third line cited the article alone: that sentence is told from the record, because the verifier of this page is today's. The lineage says what the amendment changed: "the refusal now cites a rule". Rule 130's own evidence says how it entered, and what it does not claim: "Canonized v3.12 from an existing check, which is the reverse of the usual order and is stated as such."

::: plate The button, asked what it is for
```zayn balance.zayn level=3 symbols=screen.json
DEFINE COMPONENT balance_card (
  SATISFIES [READ]
)

DEFINE INTERACTION export_button (
  SATISFIES [ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL],
  ROLE reversible
)
//--> clean
```
In words: A user reads the balance. With the button a user acts; the act can be undone or cancelled, and the button says that it can be taken back.
:::

Clean. Two other checks cite an article and no rule, and the ruling of the same day left them so: a citation is a claim, and a rule is written when there is one to write.

## What moves with one rule

On 8 November 2026 I looked at a menu of the Zayn site and wrote a remark. Rule 116 was amended that day, and the law went to version 3.16. Chapter 19 follows that remark from my sentence to the check. Here I count what moved.

The law's file moved first: the rule's text, then the version, the date and one more entry of the lineage. The language moved: three fields entered it, so that a declaration can state a menu with levels. The contract moved: it is the data file that binds each kind of finding to the law it cites, and it gained three kinds, which makes {{n:diag.total}}. The suite moved: one fixture for each new kind and one lawful menu, which makes {{n:fix.total}}. The Zayn site moved, because its own menu is a declaration that the same three checks read.

Then the pins moved. A pin is the version of the law that a file records as the one it was checked against. At the commit this book reads, {{n:pin.files}} data files carry a pin, and {{n:pin.agree}} of them name version {{n:law.version}}. A pin moves by an act of its own, after the suite has run against the new law. The ledger tells why that act is watched: in August 2026 the suite's manifest was found pinned three versions behind the law it had passed against, "by grepping for the field, not by any check".

A version is a name, and a name can be kept while the text under it changes. So the files a consumer relies on are also held by their hashes. A hash is a fingerprint computed from a file's bytes. The pack is the set of {{n:pack.files}} files that a participant pins, each with its hash, and its document says what each of the two is for: "A version number says which edition you meant. A hash says the bytes you have are that edition."

One change in this chapter's record moved the language and left the law's version where it was. Chapter 7 showed it: a field on a kind that does not carry it is refused since language 1.4, and that finding cites Article II and no rule.

## What I refused

**I refused a sixth status.** In my pass of 13 August 2026 a draft proposed to add a value to Rule 118's five. The ruling adopted the proposal without the value: "the closed set stays at five". The data file of the vocabulary says what a sixth would be: "a constitutional amendment, not an implementation choice".

**I refused a rule with no evidence behind it.** The same pass was asked for a rule on haptic feedback. No device had been measured, so the rule was renamed for what it governs, and the docket's line is: "the haptic law waits for device evidence".

**I refused a rule drawn from one page.** In November 2026 a candidate came from one page of one site. It was written up and left unenacted: "it would want a second site before a ruling". Another, from one author's reading of one site, was held with these words: "not a measurement".

**I refused to make an ornament a rule.** One remark of the same pass asked the law to legislate an ornament. The answer keeps it where the law already puts such choices: "an ornament is a culture's choice under Article VI".

**I refused to rewrite the record.** The ledger opens on its rule: "Append, never rewrite." An entry that is later found false keeps its text and gains a correcting entry. One section of the ledger holds the corrections the project made to itself, and it gives its reason: a project "that argues about drift and hides its own errors has refuted itself".

The pass I delegated refused one thing more: it invented no rule of precedence between two rules, and left that question to me.

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the ones that the three amendments of this chapter brought or changed: the closed list of statuses, the check that Rule 130 now backs, the field on the wrong kind, and the menu of version 3.16 with its lawful form.

## Where the field leads

The field leads on the width of its evidence. A criterion of an accessibility standard is reviewed in public before it enters, and a design system asks for evidence from many teams. Several of Zayn's newest rules rest on one surface, and the docket says so of each. It also names the risk of a law fed case by case: "Three new numbers from one surface is a lot, and the risk is corpus inflation."

The field leads on procedure. The W3C Process says who reviews a change and at which stage. Zayn's docket has one author who rules, and it records each pass that he delegated as a delegation.

Zayn's law leads on the trace. Every rule carries its evidence, every change is a dated entry in the law's own file, and a number is never given twice: the pack's document says of one rule that it "means the same thing in ten years". And an amendment reaches the tools the same day: a rule that changes on a morning is refused by the verifier that afternoon, with its fixtures.

Both sides know the cost of a pin. A statute that names version 2.1 goes on naming it when the standard is at 2.2. A file pinned at one version of Zayn's law goes on reading that version, and the record says of a consumer that it "moves its pin deliberately".

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The history told here is data of the law's own file at version {{n:law.version}}, and the three amendments were answered on this page by the verifier of release {{n:release.version}}. What was lawful before a version is told from the record: this page runs one verifier, today's. Two rules that touch one subject are reconciled by amending both, and the reconciliation is found by a person who puts them side by side; a rule of precedence, or a check for two rules on one subject, is a question the docket has filed for me. The evidence behind a rule is of the size its field states: a corpus for some, one surface for others, a decision or a check for two, and each rule says which.

## In your hands

Here is the menu that the Zayn site held from 6 to 8 November 2026, written small. A `NAV_GRAPH` is the kind of declaration that states an entry of a menu. `LABEL` is the name the menu shows, `TARGET` is the page the entry leads to, and `ENTRIES` lists its children in order. An entry with children is a section, and the page it leads to is its landing page.

::: plate For you: a section and its two pages
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [invoices, payments]
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LANDING_NOT_FIRST billing
```
In words: The main menu has one section, Billing, which leads to the billing home. Under it the menu shows two entries, Invoices and Payments.
:::

Cover the report under the declaration, write the code you expect, then compare. The section leads to a page that its own level does not show. Put the page back under the section's name, and say what you expect.

::: plate The page back, under the section's name
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [billing_page, invoices, payments]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Billing",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LABEL_REPEATS_PARENT billing_page
```
In words: The same menu, and the section's own page is now its first entry, under the same name as the section: Billing.
:::

Refused again, for the name. This is the menu I had refused in my remark: a reader meets the section's title, then finds the same title among its entries. Give the page a label of its own, and put it last.

::: plate A label of its own, in last place
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [invoices, payments, billing_page]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Overview",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> MENU_LANDING_NOT_FIRST billing
```
In words: The section's page is now named Overview, and it is the third entry of three.
:::

Refused for the place. The report's first line counts it for you: entry 3 of 3. Here is the lawful form.

::: plate The landing page first, under its own label
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  TARGET billing_home,
  ENTRIES [billing_page, invoices, payments]
)

DEFINE NAV_GRAPH billing_page (
  LABEL "Overview",
  TARGET billing_home
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> clean
```
In words: The section Billing opens on its own page, named Overview, and then shows Invoices and Payments.
:::

Clean. Now go back to the first plate, the menu with its landing page absent, and delete one line: `TARGET billing_home`. Change nothing else, and say what you expect.

::: plate The same defect, with one line less
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [billing]
)

DEFINE NAV_GRAPH billing (
  LABEL "Billing",
  ENTRIES [invoices, payments]
)

DEFINE NAV_GRAPH invoices (
  LABEL "Invoices",
  TARGET invoice_list
)

DEFINE NAV_GRAPH payments (
  LABEL "Payments",
  TARGET payment_list
)
//--> clean
```
In words: The section Billing says no longer where it leads. Under it the menu shows Invoices and Payments.
:::

Clean. The specification calls an entry with children and no target a bar, like the main menu, and a bar has no landing page. So the section passes once it stops saying where it leads. Should an entry that carries a label and leads nowhere be read as a bar? That is a finding, and the law grows from findings: it is filed where the next pass will read it.

A rule enters the law from a remark that someone wrote down. The next chapter writes one, field by field, from the sentence to the check.
