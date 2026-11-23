---
id: how-to-write-a-rule
part: 7
number: 19
title: How to write a rule
stage:
  built: "a corpus of {{n:corpus.records}} corrections as data, each with its words, its place and its date; a rule's shape in the law's file, on each of the {{n:law.rules}} rules; the menu remark of 8 November 2026 followed on this page from the sentence to the check, with its fixtures and their lawful twin in the suite"
  designed: "the checks of the painted page that the site's study specifies, each shown failing on the pages as they were; the record by which an issue lands on a cell of the grid"
  next: "a way to capture a correction where it is made, so that it reaches the docket with its words and its place"
status: draft
research: research/ch19.md
fixtures: [menu-landing-not-first, menu-label-repeats-parent, menu-label-duplicate, menu-lawful, invisible-state]
---

A rule is a remark that was kept. In this chapter I follow one remark of mine from the sentence I typed to a rule with a check, in seven steps. Each step is shown on the record of that remark, and a team can take the same steps with no tool installed. The chapter ends on a template that you can fill.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution for interfaces. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field has written down what a rule must be, more than once. An accessibility standard says of its criteria that they are "written as testable criteria". The format for the rules that testers run, ACT, asks that each expectation of a rule be "distinct, unambiguous, and be written in plain language". The convention that the standards of the internet use for their own wording gives the word MUST one meaning, "an absolute requirement of the specification", and adds that such words "must be used with care and sparingly".

Those who keep a body of rules have criteria for a new one. ESLint, a linter, which is a tool that checks source code against rules, asks that a rule of its core be atomic, "Rules must function completely on their own", and unique: "No two rules can produce the same warning." The GOV.UK Design System asks of a proposal that it be useful, with evidence, and that it "does not replicate something already in the Design System".

So the field agrees on four things: a rule can be tested, its words are exact, it stands alone, and it does not say again what another rule says. Each source was read on 23 November 2026, and Appendix F lists them.

## The principle

**A remark becomes a rule when it names its cause, is bounded on both sides, and keeps the check that failed on the page as it was.**

The study of the Zayn site, written from its corrections, has the sentence this chapter stands on: "A correction stored as a symptom does not stop the defect; it moves it." And the law has its own, in the reason of Rule 78: "A law that cannot be tested at the door will be negotiated in the hallway."

## Write the remark down

The first step is to keep the remark as it was made. Zayn keeps its corrections in a corpus: a data file of {{n:corpus.records}} records. Each record holds the words, the page or the file where they were said, the date, what was wrong, what was asked, and the sense that noticed it. {{n:corpus.verbatim}} of them keep the person's words as typed.

Here is mine, of 6 November 2026, on the menu of the Zayn site: "the same menu option in the main and submenu levels (like Try and then Try here)!!!" A section named Try opened on an entry named Try here: the level under a section said the section's name again. The repair that followed deleted that entry, and with it the section's own page left the level under the section. Two days later, looking at a section whose first place stood empty, I wrote a second remark: bring the page back, under another label.

A record has one more field, and it is the one that makes a rule necessary: whether an earlier correction of the same defect exists. {{n:corpus.repeat}} of the {{n:corpus.records}} records say yes. My second remark is one of them, and its record says what the first repair broke. Here is the section as that second remark found it, written as a declaration. A `NAV_GRAPH` states an entry of a menu: `LABEL` is the name it shows, `TARGET` the page it leads to, `ENTRIES` its children in order.

::: plate The section, as the remark found it
```zayn band.zayn
DEFINE NAV_GRAPH site_menu (
  SATISFIES [LOCATE],
  ENTRIES [approach]
)

DEFINE NAV_GRAPH approach (
  LABEL "Approach",
  TARGET thinking,
  ENTRIES [the_grid, channels, comparison, claims]
)

DEFINE NAV_GRAPH the_grid (LABEL "The grid", TARGET grid)
DEFINE NAV_GRAPH channels (LABEL "Channels", TARGET media)
DEFINE NAV_GRAPH comparison (LABEL "Comparison", TARGET positioning)
DEFINE NAV_GRAPH claims (LABEL "Claims", TARGET innovation)
//--> MENU_LANDING_NOT_FIRST approach
```
In words: The site's menu has a section, Approach, which leads to a page. Under it the menu shows four entries, and none of them is that page.
:::

Refused. The declaration is written today from the docket's sentence on that menu, and the check that answers it is the one the remark produced: it fails on the page as it was. The docket is the file where changes to the law are proposed and ruled.

## Ask whether it is law already

The second step costs the least and saves the most: look for the rule that already holds the remark. In August 2026 five candidates came from one surface. Two were refused as new rules, because each was a rule that existed, and each of those rules gained the new case. The docket's sentence on one of them: "The author's correction and Rule 113 are the same law, reached twice."

A declaration can ask the question. One of those two candidates said that a status board must show what it requires of its user. Here is such a board, checked at level 3, where the verifier is given a list of what the system holds.

::: plate A board that keeps the next action to itself
```zayn board.zayn level=3 symbols=board.json
DEFINE SCREEN status_board (
  SATISFIES [SCAN, LOCATE],
  VISIBLE_STATE [open_count, blocked_count]
)
//--> INVISIBLE_STATE next_action
```
In words: On the status board a user scans and goes to an item. The board shows two counts: what is open and what is blocked.

```symbols board.json
{
  "state": ["open_count", "blocked_count", "next_action"]
}
```
:::

Refused, and the citation is the answer: Rule 82. The candidate has a number already. The repair is the board's, and the law stays as it is.

::: plate The same board, showing the next action
```zayn board.zayn level=3 symbols=board.json
DEFINE SCREEN status_board (
  SATISFIES [SCAN, LOCATE],
  VISIBLE_STATE [open_count, blocked_count, next_action]
)
//--> clean
```
In words: The same board, and it now shows a third thing: the next action.
:::

Clean. A search that finds nothing needs a control: a term that you know is in the law. The ledger, the dated list of what the project found, records a search of the law that returned nothing for every term, the word undo included, in a law whose Rule 79 is named The Undo Covenant. Its lesson is in the imperative: "Put a control in every corpus test".

For the menu the answer was yes. Rule 116, The Menu Tells the Truth About the Tree, held the subject since August 2026. So the remark became an amendment of that rule, and took no new number.

## Give it the law's shape

The third step writes the rule in the shape that every rule has: what to avoid, as a list; the rule's text; its reason, in a sentence; the article it derives from; and its evidence, which says what happened, where and when. Chapter 16 printed one rule whole.

Three things make the text hold. It names the cause. Mine was this: the entry of the main menu names a section, and the first entry under it names the section's landing page. The docket's words: "they are two things, so each keeps one name". A cause settles the next case, which a symptom leaves open.

It is bounded on both sides. My first remark had one bound: no repeated label. The repair went past it and deleted the page. The amended rule has both, and its list of what to avoid gained two entries: "A section whose landing page is missing from the level under it, or listed after the pages it leads to", and "A child entry that carries its parent's label, or two entries at one level that carry one label". Here is the second bound at work, on the same section.

::: plate The page back, under the section's name
```zayn band.zayn
DEFINE NAV_GRAPH site_menu (
  SATISFIES [LOCATE],
  ENTRIES [approach]
)

DEFINE NAV_GRAPH approach (
  LABEL "Approach",
  TARGET thinking,
  ENTRIES [landing, the_grid, channels, comparison, claims]
)

DEFINE NAV_GRAPH landing (LABEL "Approach", TARGET thinking)
DEFINE NAV_GRAPH the_grid (LABEL "The grid", TARGET grid)
DEFINE NAV_GRAPH channels (LABEL "Channels", TARGET media)
DEFINE NAV_GRAPH comparison (LABEL "Comparison", TARGET positioning)
DEFINE NAV_GRAPH claims (LABEL "Claims", TARGET innovation)
//--> MENU_LABEL_REPEATS_PARENT landing
```
In words: The section's page is back, first under the section, and under the section's name: Approach.
:::

Refused, on the other side. And here is the menu as it was corrected.

::: plate The page back, under another label
```zayn band.zayn
DEFINE NAV_GRAPH site_menu (
  SATISFIES [LOCATE],
  ENTRIES [approach]
)

DEFINE NAV_GRAPH approach (
  LABEL "Approach",
  TARGET thinking,
  ENTRIES [landing, the_grid, channels, comparison, claims]
)

DEFINE NAV_GRAPH landing (LABEL "Reasoning", TARGET thinking)
DEFINE NAV_GRAPH the_grid (LABEL "The grid", TARGET grid)
DEFINE NAV_GRAPH channels (LABEL "Channels", TARGET media)
DEFINE NAV_GRAPH comparison (LABEL "Comparison", TARGET positioning)
DEFINE NAV_GRAPH claims (LABEL "Claims", TARGET innovation)
//--> clean
```
In words: The section Approach opens on its page, named Reasoning, and then shows its four other entries.
:::

Clean! And the third thing: the evidence is written as it happened. The record's rule for it has four words, "Evidence is never corrected.", and a rule that entered another way says so: the evidence of Rule 130 calls its own origin "the reverse of the usual order".

## Name the instrument, then the tier

The fourth step asks, clause by clause, what can decide the rule. For Rule 116 there are three answers. A declaration decides three of its demands, and you have just run two of them. The painted page, which is the menu as a browser draws it, is read by the audit of chapter 10. And one clause stays with a reader: the rule tells its reader to avoid "A label that names the author's metaphor and not what the page holds".

::: plate Two labels that only a reader can judge
```zayn menu.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [orders, customers]
)

DEFINE NAV_GRAPH orders (
  LABEL "Orders",
  TARGET order_board,
  ENTRIES [orders_today, returns, refunds]
)

DEFINE NAV_GRAPH orders_today (LABEL "The pulse", TARGET order_board)
DEFINE NAV_GRAPH returns (LABEL "Returns", TARGET return_list)
DEFINE NAV_GRAPH refunds (LABEL "Refunds", TARGET refund_list)
DEFINE NAV_GRAPH customers (LABEL "Depth", TARGET customer_list)
//--> clean
```
In words: The section Orders opens on a page named The pulse, and the menu's second entry, which leads to the customers, is named Depth.
:::

Clean, and wrong for a reader: neither label says what its page holds. The verifier judges what a declaration states, and whether a word is a metaphor is a reader's to say.

The tier follows from the instrument, and it is filed as the instrument stands. The docket's sentence on one rule says what a tier claims: it "is honest about which instrument owes the check; it is not a claim that the check runs today". A rule's pointer to its instrument is written when the instrument exists: for one rule the docket left the pointer out, because "a pointer to an instrument that does not exist is worse than silence". When Rule 116 gained its three checks on a declaration, its tier stayed where it was, and the docket left the question to me: "whether that moves the tier is a ruling, not this desk's". Chapter 17 reads the tiers.

## Place it on the grid

The fifth step places the rule: which activity of the user it protects, and on which media. Chapter 13 gives the grid. The placement reads the activity from the rule's title and its reason, and the medium from the rule's own words; a rule whose check does not look at the medium is placed on every medium. Does the menu's check look at the medium? Run it on a surface that speaks: a `VIBE` declares the surface, and here it is a voice.

::: plate The same fault, on a phone line
```zayn phone.zayn
DEFINE VIBE phone_line (
  SURFACE_AS voice
)

DEFINE NAV_GRAPH orders (
  LABEL "Orders",
  TARGET order_board,
  ENTRIES [orders_today, returns]
)

DEFINE NAV_GRAPH orders_today (LABEL "orders", TARGET order_board)
DEFINE NAV_GRAPH returns (LABEL "Returns", TARGET return_list)
//--> MENU_LABEL_REPEATS_PARENT orders_today
```
In words: On a phone line, the menu says Orders, and the first choice under it is said with the same word: orders.
:::

Refused, on a voice surface as on a screen: a label is compared without its capitals. The repair is the same.

::: plate The first choice, under another word
```zayn phone.zayn
DEFINE VIBE phone_line (
  SURFACE_AS voice
)

DEFINE NAV_GRAPH orders (
  LABEL "Orders",
  TARGET order_board,
  ENTRIES [orders_today, returns]
)

DEFINE NAV_GRAPH orders_today (LABEL "Today", TARGET order_board)
DEFINE NAV_GRAPH returns (LABEL "Returns", TARGET return_list)
//--> clean
```
In words: The menu says Orders, and the first choice under it is said as Today.
:::

Clean. In the grid's data, Rule 116 is placed on the visual medium, under the activity of understanding. The run says that three of its checks answer on any medium. So a rule that is amended is placed again, and that is one more thing an amendment touches.

## Write the check that fails first

The sixth step is the one that keeps the remark from coming back. A check is written to fail on the page as it was, and to pass on the page as corrected, with one change between the two and no other. The first plate of this chapter and the last plate of the third step are that pair.

Zayn's suite states it as a rule for its fixtures, the declarations it keeps with the answers they must get: "One fixture, one concern", and for every refused fixture "a lawful twin where the defect is repaired and nothing else changes". The suite's guide gives the twin its reason: it "proves the check is not simply firing on everything". The amendment of Rule 116 brought one fixture for each new kind of finding, and one lawful menu from which each differs by a line.

The same discipline holds where the check reads files or a painted page. The site's study records its file checks "each shown failing on the pages as they were first", and one of them with its count: of a check that a statement is made once on a screen, "35 of the 39 pages failed it". A check proves itself on the day it fails on the defect it was written for.

## Amend what it touches

The seventh step lists what the rule touches, object by object, and changes each. Chapter 18 counted them for this remark: the rule's fields, the version and its line of history, the language, the contract, the fixtures, the pins. The last on the list is the nearest: the pages of those who hold the rule. Here is the same section in the Zayn site's own menu, as the site declares it at the version this book reads.

::: plate The site's own section, as declared
```zayn site-menu.zayn
DEFINE NAV_GRAPH whyzayn (
  LABEL "Why",
  TARGET why,
  ENTRIES [why, case, thinking, innovation]
)

DEFINE NAV_GRAPH why (LABEL "The problem", TARGET why)
DEFINE NAV_GRAPH case (LABEL "The case", TARGET case)
DEFINE NAV_GRAPH thinking (LABEL "Reasoning", TARGET thinking)
DEFINE NAV_GRAPH innovation (LABEL "Claims", TARGET innovation)
//--> clean
```
In words: The section Why opens on its page, named The problem, and then shows three more entries.
:::

Clean. The remark went further than the site: the house that publishes this book adopted the same three refusals for the menu of every book's reader, this one included.

## The template

Seven steps, and what each one writes.

| Step | What you write |
|---|---|
| 1. The correction | The person's sentence as typed; the page or the file; the date; what was wrong; what was asked; whether an earlier correction of the same defect exists, and what its repair broke |
| 2. Already law? | The rule that holds it, by number, and the case added to that rule; or how you searched, and the control that proved the search works |
| 3. The rule | What to avoid, as a list; the text; the reason, in a sentence; the article; the evidence; the least and the most the rule allows |
| 4. The instrument | Which clause a declaration decides, which a painted page decides, which a reader decides; the tier; a pointer when the instrument exists |
| 5. The grid | The activity of the user it protects; the media its own words name, or every medium |
| 6. The check | The page as it was, and the finding expected; the page as corrected, with one change; a case the check must leave alone |
| 7. What it touches | The rule's fields; the version and its line of history; the rules it cites or narrows; the checks and their fixtures; the placement; the pages and the teams to tell |

## What I refused

**I refused the repair made on my first remark.** It had deleted the landing page from the level under its section. My ruling of 8 November 2026 brought the page back under a label of its own, and the docket says of that ruling that it "reverses the reading of 2026-11-06". A remark with one bound had been read past its bound.

**I refused a rule written to fill a cell.** The grid of chapter 13 has cells that no rule names a medium for. My ruling, as the grid's document keeps it, "forbids writing a rule for them until that is measured". A rule answers a defect that happened; an empty cell is a question.

**A remark that the law already covers stays evidence.** In November 2026 a table of my remarks on the Zayn site was filed under the heading "evidence for existing rules, not new rules", each beside the rule it supports, and I ruled on what the docket recommended for them.

**The suite refuses a fixture it cannot judge.** One kind of finding is a fact about a painted page, and the suite's manifest gives its reason for keeping no fixture for it: "A fixture here would be theatre".

**A check is never a list of kinds.** The site's study records a correction that was kept as a list of the kinds of element it applied to, and what followed: "the defect came back that afternoon on a kind not in the list". The study asks of a check that it read every element.

[AUTHOR: the stake of this chapter, in your words: what you want a team to be able to do on the day after it reads this page.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the ones the menu remark brought, each refused one beside the lawful menu, and the fixture of the state that no surface shows.

## Where the field leads

The field leads on the form of a rule that a tester runs. The ACT format asks for a rule's applicability and its expectations, with examples that pass, fail and do not apply. A rule of Zayn's law has a list of what to avoid and a text, and the examples live apart from it, in the suite's fixtures.

The field leads on the words of obligation. A standard of the internet says exactly what MUST means. Zayn's rules are written in sentences, and what binds in them is the check and its fixture where one exists, a reader's judgment elsewhere.

Zayn leads on the path from a remark. A correction is kept with its words, its place and its date; the rule keeps it as evidence; the check fails on the page as it was. And the cost is stated: a rule drawn from one case is of the size of that case, and several of the newest candidates are kept as candidates until a second case comes.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

The seven steps are the record's: each is shown here on a file of Zayn at release {{n:release.version}}, and every declaration was run. The section of the first plate is written today from the docket's sentence, and it is refused by today's verifier. The checks on the site's files and on its painted pages are told from the site's study, with the counts that it records. The template is this book's: it is assembled from the shapes of the corpus, the docket, the law's file, the grid and the suite, and it holds for a team that keeps its rules in a document of its own.

## In your hands

Here is a menu with three faults at once.

::: plate For you: a stock menu, three times wrong
```zayn stock.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [stock, suppliers]
)

DEFINE NAV_GRAPH stock (
  LABEL "Stock",
  TARGET stock_levels,
  ENTRIES [deliveries, stock_now, counts]
)

DEFINE NAV_GRAPH deliveries (LABEL "Deliveries", TARGET delivery_list)
DEFINE NAV_GRAPH stock_now (LABEL "Stock", TARGET stock_levels)
DEFINE NAV_GRAPH counts (LABEL "The deliveries", TARGET count_sheet)
DEFINE NAV_GRAPH suppliers (LABEL "Suppliers", TARGET supplier_list)
//--> MENU_LABEL_REPEATS_PARENT stock_now
//--> MENU_LABEL_DUPLICATE counts
//--> MENU_LANDING_NOT_FIRST stock_now
```
In words: The section Stock leads to the stock levels. Under it the menu shows Deliveries, then Stock, then The deliveries.
:::

Cover the report under the declaration, write the codes you expect, then compare. Three findings, and they come in the order of the checks, which is another order than the lines'. Repair all three: the landing page first, under a label that is its own, and one name for each entry. Try before you read on.

::: plate The stock menu, repaired
```zayn stock.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [stock, suppliers]
)

DEFINE NAV_GRAPH stock (
  LABEL "Stock",
  TARGET stock_levels,
  ENTRIES [stock_now, deliveries, counts]
)

DEFINE NAV_GRAPH stock_now (LABEL "Levels", TARGET stock_levels)
DEFINE NAV_GRAPH deliveries (LABEL "Deliveries", TARGET delivery_list)
DEFINE NAV_GRAPH counts (LABEL "Counts", TARGET count_sheet)
DEFINE NAV_GRAPH suppliers (LABEL "Suppliers", TARGET supplier_list)
//--> clean
```
In words: The section Stock opens on its page, named Levels, and then shows Deliveries and Counts.
:::

Clean. Now give the landing page a label that keeps the section's word, Stock now, and say what you expect.

::: plate The section's word, kept in the label
```zayn stock.zayn
DEFINE NAV_GRAPH main_menu (
  SATISFIES [LOCATE],
  ENTRIES [stock, suppliers]
)

DEFINE NAV_GRAPH stock (
  LABEL "Stock",
  TARGET stock_levels,
  ENTRIES [stock_now, deliveries, counts]
)

DEFINE NAV_GRAPH stock_now (LABEL "Stock now", TARGET stock_levels)
DEFINE NAV_GRAPH deliveries (LABEL "Deliveries", TARGET delivery_list)
DEFINE NAV_GRAPH counts (LABEL "Counts", TARGET count_sheet)
DEFINE NAV_GRAPH suppliers (LABEL "Suppliers", TARGET supplier_list)
//--> clean
```
In words: The section Stock opens on a page named Stock now.
:::

Clean. The check compares whole labels, and Stock now is another label than Stock. Read my first remark again: its example was Try, and then Try here. So the check that my remark produced passes the example that my remark gave. When is a child's label its parent's name said again? That is the second bound of a rule, and it is yours to set for the rules you write. For this one it is a remark for the law, filed with the book's findings.

The law is written, amended and checked. Part VIII asks who else may write it: a team with its own corrections, and a commons that many teams share.
