---
id: how-to-write-a-rule
part: 7
number: 19
title: How to write a rule
stage:
  built: "a corpus of {{n:corpus.records}} corrections as data, each with its words, its place and its date where it is known; a rule's shape in the law's file, on each of the {{n:law.rules}} rules; the menu remark of 8 November 2026 followed on this page from the sentence to the check, with its fixtures and their lawful twin in the suite; the checks of the painted page, run and recorded in Zayn's repository"
  designed: "the record by which a correction lands on a cell of the grid"
  next: "a way to capture a correction where it is made, so that it reaches the docket with its words and its place"
status: draft
research: research/ch19.md
fixtures: [menu-landing-not-first, menu-label-repeats-parent, menu-label-duplicate, menu-lawful, invisible-state]
---

A rule is a remark that was kept. In this chapter I follow a remark of mine on a menu, and the second remark that its repair called for, from the sentences I typed to a rule with a check. There are seven steps. Each is shown on the record of those remarks, and a team can take the same steps for rules of its own. The chapter ends on a template that you can fill.

If you open the book here, four words are enough to follow. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution for interfaces. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The field has written down what a rule must be, more than once. The page that explains conformance to the accessibility guidelines says that their criteria are "written as testable criteria". ACT, the format for the rules that testers run, asks that each expectation of a rule be "distinct, unambiguous, and be written in plain language". A document of the internet's engineers, a Best Current Practice of 1997, gives the word MUST one meaning, "an absolute requirement of the specification", and adds that such words "must be used with care and sparingly".

Those who keep a body of rules have criteria for a new one. ESLint is a linter, a tool that checks source code against rules. It asks a rule of its core to be atomic, "Rules must function completely on their own", and unique: "No two rules can produce the same warning." The GOV.UK Design System asks a proposed component or pattern to be useful, with evidence, and one that "does not replicate something already in the Design System".

Each source was read on 23 November 2026, and Appendix F lists them. Between them they ask four things of a rule: it can be tested, its words are exact, it stands alone, and it does not say again what is already said.

## The principle

**A remark becomes a rule when it names its cause, is bounded on both sides, and keeps the check that failed on the page as it was.**

A bound is an edge of what the rule allows. The rule states the least and the most, so that a repair stops where it should. Zayn's design study, written from the corpus of its corrections, has the sentence this chapter stands on: "A correction stored as a symptom does not stop the defect; it moves it." The law has its own, in the reason of Rule 78: "A law that cannot be tested at the door will be negotiated in the hallway." A rule is tested at the door by its check.

## Write the remark down

First, keep the remark as it was made. Zayn calls such a remark a correction, and keeps its corrections in a corpus: a data file of {{n:corpus.records}} records. Each record has the words, the page or the file where they were said, the date where it is known, what was wrong, what was asked, and what the remark concerned. {{n:corpus.verbatim}} of them keep the person's words as typed.

Here is mine, of 6 November 2026, on the menu of the Zayn site: "the same menu option in the main and submenu levels (like Try and then Try here)!!!" A section named Try opened on an entry named Try here: the level under a section said the section's name again. The repair that followed deleted that entry, and with it the section's own page left the level under the section. On 8 November I wrote a second remark, and the corpus keeps its typing: "you must bring bakc the frist option but find an other lable for it".

One more field of a record matters here, and it is the one that makes a rule necessary: whether an earlier correction of the same defect exists. {{n:corpus.repeat}} of the {{n:corpus.records}} records say yes. My second remark is one of them, and its record says what the first repair broke.

Here is another section of that menu, Approach, as the second remark found it, written as a declaration. A `NAV_GRAPH` states an entry of a menu: `LABEL` is the name it shows, `TARGET` the page it leads to, `ENTRIES` its children in order. An entry with a target and children is a section, and the page it leads to is its landing page. You repaired a menu like it in chapter 18.

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

Refused: no entry under Approach leads to its page, and the report cites Rule 116. The declaration is written for this book from the sentence of the docket on that menu; the docket is the file where changes to the law are proposed and ruled. The check that answers it is the one the remark produced, and it fails on the page as it was.

## Ask whether it is law already

The second step is a search: look for the rule that already covers the remark. In August 2026 five candidates for a rule came from one surface. Three became rules. Two were refused as new rules, because each was a rule that existed, and each of those rules gained the new case. The docket's sentence on one of the two: "The author's correction and Rule 113 are the same law, reached twice." The law was extended, and its count stayed.

A declaration can ask the question. The other of the two said that a status board must show what it requires of its user. Here is such a board, checked at level 3, where the verifier is given a list of what the system holds.

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

Clean. A search that finds nothing needs a control: a term that you know is in the law. Zayn's ledger, the dated list of what the project found, records a search of the law that returned nothing for every term, the word undo included, in a law that has a rule on undo. Its lesson is in the imperative: "Put a control in every corpus test". A search proves itself on a term it must find.

My remarks on the Zayn site went the same way. In November 2026 a table of them was filed in the docket under the heading "evidence for existing rules, not new rules", most beside the rule they support.

For the menu the answer was yes: Rule 116 has covered the subject since August 2026. So the remark became an amendment of that rule, and took no new number. Here is Rule 116 as amended.

{{rule:116}}

Its last line is the reason: a menu hands its user a map.

## Give it the law's shape

Third, write the rule in the shape that every rule has: what to avoid, as a list; the rule's text; its reason, in a sentence or two; the article, one of the law's statements of principle, that it derives from; and its evidence, which says where the rule comes from. Chapter 16 printed one rule whole. Three things make the rule hold: its cause, its two bounds and its evidence.

The cause. For the menu it was this: the entry of the main menu names a section, and the first entry under it names the section's landing page. The docket's words: "they are two things, so each keeps one name". A cause settles the next case, which a symptom leaves open.

The two bounds. My first remark had one: no repeated label. The repair went past it and deleted the page. The amended rule has both, and its list of what to avoid gained two entries: "A section whose landing page is missing from the level under it, or listed after the pages it leads to", and "A child entry that carries its parent's label, or two entries at one level that carry one label". Here is that first bound, still at work, on the same section.

::: plate The landing page, named as its section
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

Refused, on the other side. Here is the menu with the label that the site's writing rule records for that page, written here as a declaration.

::: plate The landing page, under another label
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

Clean! Between the two refusals, the rule has its room.

The evidence. It is written as it happened. The document of the law's architecture has the sentence for it, "Evidence is never corrected.", and a rule that entered another way says so: the evidence of Rule 130 calls its origin "the reverse of the usual order". What happened is kept as it was told.

## Name the instrument, then the tier

Fourth, ask clause by clause what can decide the rule. An instrument is what makes a check: the verifier, an audit of the painted page, or a person who reads. For Rule 116 there are three answers. A declaration decides three of its demands, and you have just run two of them. The audit of chapter 10 reads the menu, the level under it, the trail and the outline as a browser paints them. And one clause stays with a person: the rule lists, to avoid, "A label that names the author's metaphor and not what the page holds". Here is a menu that the verifier passes and that clause refuses.

::: plate Two labels that only a person can judge
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

Clean, and wrong for a person who reads it: neither label says what its page holds. The verifier judges what a declaration states, and whether a word is a metaphor is a person's to say.

Then the tier. A rule's tier is one word in the law's file, and the card above shows Rule 116's. The docket says of one rule what that word claims: the tier "is honest about which instrument owes the check; it is not a claim that the check runs today". A rule can also point at its instrument, in a field of its own, and the pointer is written when the instrument exists: the docket left one out, because "a pointer to an instrument that does not exist is worse than silence". When Rule 116 gained its checks on a declaration, its tier stayed, and the docket left the question to me: "whether that moves the tier is a ruling, not this desk's". Chapter 17 reads the tiers.

## Place it on the grid

Fifth, place the rule: which activity of the user it protects, and on which media. Chapter 13 gives the grid. The placement reads the activity from the rule's title and its reason, and the medium from the rule's own words; a rule whose check does not look at the medium is placed on every medium. Does the menu's check look at the medium? Here is the defect of the repeated name on a surface that speaks. A `VIBE` declares the surface, here a voice, and the first choice under Orders is the same word without its capital.

::: plate The same defect, on a phone line
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

Refused, on a voice surface as on a screen, and with or without the capital. The repair is the same.

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

Clean. In the grid's data, Rule 116 is placed on the visual medium, under the activity of understanding. The run says that this check answers on a voice surface as on a screen. So an amended rule is to be placed again, and that is one more thing an amendment touches.

## Write the check that fails first

Sixth, write the check so that it fails on the page as it was and passes on the page as corrected, with one change between the two and no other. That is what stops the defect from coming back. The first plate of this chapter and the last plate of the third step are that pair.

Zayn's suite has it as a discipline for its fixtures, the declarations it keeps with the answers they must get: "One fixture, one concern", and for every refused fixture "a lawful twin where the defect is repaired and nothing else changes". The suite's guide gives the twin its reason: it "proves the check is not simply firing on everything". The amendment of Rule 116 brought one fixture for each new kind of finding, and one lawful menu from which each differs by a line. Where only a painted page can decide, the suite keeps no fixture and says why: "A fixture here would be theatre".

The same discipline applies where a check reads files or a painted page. The design study records its checks on the site's files "each shown failing on the pages as they were first", and of one more file check, which reads that a statement is made once on a screen, it gives the count: "35 of the 39 pages failed it". It also records what happens to a check written as a list of the kinds of element it covers: "the defect came back that afternoon on a kind not in the list". A check reads every element. And a check proves itself on the day it fails on the defect it was written for.

## Amend what it touches

Seventh, list what the rule touches, object by object, and change each. Chapter 18 listed them for this remark: the rule's fields, the version and its line of history, the language, the contract, the fixtures, the pins. One more is the nearest: the pages of those who apply the rule. Here is the section of the Zayn site's menu that shows the page Reasoning at the version this book reads, written here with one of its entries left out.

::: plate A section of the site's own menu
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
In words: The section Why opens on its page, named The problem, and Reasoning is one of the entries after it.
:::

Clean. The remark went further than the site: the house that publishes this book adopted the same three kinds of finding for the menu of every book it puts online, this one included.

## The template

Seven steps, and what each one writes.

| Step | What you write |
|---|---|
| 1. The remark | The person's sentence as typed; the page or the file; the date; what was wrong; what was asked; whether an earlier correction of the same defect exists, and what its repair broke |
| 2. Already law? | The rule that covers it, by number, and the case added to that rule; or how you searched, and the control that proved the search works |
| 3. The rule | What to avoid, as a list; the text; the reason; the article; the evidence; the least and the most the rule allows |
| 4. The instrument | Which clause a declaration decides, which a painted page decides, which a person decides; the tier; a pointer when the instrument exists |
| 5. The grid | The activity of the user it protects; the media its own words name, or every medium |
| 6. The check | The page as it was, and the finding expected; the page as corrected, with one change; a case the check must leave alone |
| 7. What it touches | The rule's fields; the version and its line of history; the rules it cites or narrows; the checks and their fixtures; the placement; the pages and the teams to tell |

Row 6 asks one thing more than the plates showed: a case that the check must leave alone, so that it fails for its defect and for nothing else.

## What I refused

**I refused the repair made on my first remark.** It had deleted the landing page from the level under its section. My ruling of 8 November 2026 brought the page back under another label, and the docket says of that ruling that it "reverses the reading of 2026-11-06". A remark with one bound had been read past its bound.

**I refused a rule written to fill a cell.** The grid of chapter 13 has cells that no rule names a medium for. My ruling, as the grid's document keeps it, "forbids writing a rule for them until that is measured". A rule answers a defect that happened; an empty cell is a question.

[AUTHOR: the stake of this chapter, in your words: what you want a team to be able to do on the day after it reads this page.]

## The court

The court of a chapter is what proves it. Here it is Zayn's conformance suite: {{n:fix.total}} fixtures, each a declaration kept with the answer it must get. The fixtures below are the ones the menu remark brought, each refused one beside the lawful menu, and the fixture of the state that no surface shows.

## Where the field leads

The field leads on the form of a rule that a tester runs. The ACT format asks for a rule's applicability and its expectations, with examples that pass, fail and do not apply. A rule of Zayn's law has a list of what to avoid and a text, and the examples live apart from it, in the suite's fixtures.

The field leads on the words of obligation. The engineers' document says exactly what MUST means. Zayn's rules are written in sentences, and what binds in them is the check and its fixture where one exists, a person's judgment elsewhere.

Zayn's part is the path from a remark. A correction is kept with its words and its place; the rule keeps it as evidence; the check fails on the page as it was. The cost is stated too: a rule drawn from one case is as wide as that case, and one of the newest candidates is kept as a candidate until a second site is measured.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the commit named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Each of the seven steps is shown here on a file of Zayn at release {{n:release.version}}, and every declaration was run. The sections of the first three plates are written for this book from the docket's sentence and from the site's writing rule, and the verifier of this page answers them. The checks on the site's files and on its painted pages are told from the design study, with the counts that it records. The template is this book's: it is assembled from the shapes of the corpus, the docket, the law's file, the grid and the suite, and it is written for a team that keeps its rules in a document of its own.

## In your hands

Here is a menu with three defects at once. Before you read its report, write the codes you expect.

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

Three findings, in the order of the checks, not of the lines. The second reads past a leading The: for the verifier, The deliveries and Deliveries are one label. Repair all three: the landing page first, under another label, and one name for each entry. Try before you read on.

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

Clean. The check compares whole labels, and Stock now is a different label from Stock. Read my first remark again: its example was Try, and then Try here. So the check that my second remark produced passes a menu of the shape that my first remark gave as its example. When is a child's label its parent's name said again? That is a bound, and it is yours to set for the rules you write. For Rule 116 the question is open, and I filed it for the law, with this book's requests to Zayn.

The law is written, amended and checked. Part VIII asks who else may write it: a team with its own corrections, and a commons that many teams share.
