---
id: a-site-under-its-own-law
part: 10
number: 26
title: A site under its own law
stage:
  built: "the Zayn site's menu as a declaration of {{n:site.menu}} entries, written by its build and checked there for the three menu codes; {{n:site.declared}} pages that declare themselves; {{n:site.pairs}} declarations its build runs again against what each page prints; the checks of its files; the audit of its painted page, in the browser"
  designed: "a closing part that declares the page on every page of the site; the next steps of the site's redesign, where checks that count what they will refuse begin to refuse it"
  next: "the lessons of this book's fresh readers taken to the site, one remark at a time, each with a check written to fail first"
status: draft
research: research/ch26.md
fixtures: [role-acts-without-consequence, role-acts-without-consequence-lawful, menu-lawful, menu-label-repeats-parent, menu-landing-not-first, menu-label-duplicate]
---

A site under its own law is a site that publishes a law for interfaces and holds its own pages to it. Its pages declare themselves, its build checks them, and a remark made on one of its pages leaves a check behind. The Zayn site is that case. In this chapter I run the site's own declarations, its menu and a page, and show the three instruments that check them. Then I follow one chain of my remarks, from 15 to 17 November 2026, each from the words I typed to the check that keeps it; one of those checks measured the wrong box. This book reads Zayn at the commit, the recorded change of its repository, that answered the last of those remarks.

If you open the book here, four words come first, and every other word is said where it first appears. A **declaration** is a few lines of Zayn, a language for interfaces, that say what a user is doing on a surface, and nothing of how the surface is drawn. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file; its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error.

## The field

The bodies that write the field's standards hold their own sites to them, and say so in a statement. WCAG, the web's accessibility guidelines, are W3C's, and W3C's guide to an accessibility statement lists what one holds: "A commitment to accessibility for people with disabilities", "The accessibility standard applied, such as WCAG 2.2", and "Contact information in case users encounter problems". W3C states it of its own pages, AA and AAA being two of the guidelines' levels of conformance: "Content must meet WCAG 2.1 AA, and should meet AAA as feasible." It measures them itself: "WAI assessed the accessibility of the WAI website by self-evaluation."

A government can require the statement. The United Kingdom's guidance says: "Public sector bodies must publish an accessibility statement and review it regularly", under regulations of 2018. The GOV.UK Design System's statement says its website "is fully compliant with the Web Content Accessibility Guidelines (WCAG) version 2.2 AA standard". It "was last audited for accessibility issues by an external group in July 2024", and its team keeps the failures it finds in a public list.

And the field checks the parts before the whole. Storybook is a tool where each state of a component is kept apart as a story. It says: "When you navigate to a story, automated accessibility checks are run and the results are reported in the Accessibility addon panel." Each source was read on 24 November 2026, and Appendix F lists them. So the field states a site's conformance to a published standard, measures it by audit and by tools on its parts, and dates the statement.

## The principle

**A site that publishes a law holds its own pages to it: its pages declare themselves, its build checks them, and each remark made on it leaves a check, written to fail on the page as it was.**

A check is trusted once it has failed on what it is meant to see, and a rule is kept once it is written down and checked. The site's rule on how its pages are written says why it was written down rather than promised. I had asked more than once that its pages say what their subject is, in plain and full descriptive sentences. "It drifted back each time because it lived only in a promise, so it is written here and part of it is checked". To drift is to slide back, one page at a time, from what was asked. The ledger, the dated list of what the project found, keeps its own errors in view: "a project that argues about drift and hides its own errors has refuted itself."

## The site, declared

The site's menu is a declaration of {{n:site.menu}} entries. The site's build, the scripts that write and check its pages, renders the menu from the registry, the one file that lists the site's pages, and writes that menu as a declaration, the file `site/menu.zayn`. At each build it fails when that file differs from the menu it renders, and it reads the file with the verifier.

A section is a group of the main menu, and a family a group of pages inside a section. A `NAV_GRAPH` is an entry of a menu. The word after `NAV_GRAPH` is the entry's name, which other entries list; its `LABEL` is the word a visitor sees, its `TARGET` the page it opens, and its `ENTRIES` the entries under it, which are siblings. An entry with `ENTRIES` and no `TARGET` is a bar, such as the main menu. An entry with both, a section or a family, has a landing page: the page its own `TARGET` opens. The verifier refuses three codes of a menu. A label that repeats its parent's. An entry with a landing page whose first child is not the one that leads there, or that has no such child. And two siblings with one label. Labels compare ignoring case, the spaces around them and a leading "The", so "Invoices" and "The invoices" are one name. Chapter 19 follows those three codes from my remark. Here is the section of the menu where a visitor goes to adopt Zayn, and the family of pages for designers, word for word.

::: plate The Adopt section of the site's menu
```zayn menu.zayn
DEFINE NAV_GRAPH use (
  LABEL "Adopt",
  TARGET adopt,
  ENTRIES [adopt, designers_family, build_family, web_family, audit_family]
)
DEFINE NAV_GRAPH adopt (LABEL "Start", TARGET adopt)

DEFINE NAV_GRAPH designers_family (
  LABEL "Designers",
  TARGET designers,
  ENTRIES [designers, testbench]
)
DEFINE NAV_GRAPH designers (LABEL "Overview", TARGET designers)
DEFINE NAV_GRAPH testbench (LABEL "Testbench", TARGET testbench)
//--> clean
```
In words: The Adopt section opens on its Start page, then lists four families; the Designers family opens on its overview, then the testbench.
:::

Clean. In the site's file the section's own entry, `use`, is listed by the main menu, and its other three families are declared further on. In this excerpt they are names with no declaration. The language's specification says what the verifier does with them: "An entry that names no declared `NAV_GRAPH` is not judged, since its label is not in the file." A flow that a form names and its own file does not declare gets a warning, as chapter 25 shows; a menu's entry gives the verifier a label to judge only where its file declares it.

{{n:site.declared}} of the site's pages declare themselves as well: each ends on a closing part, "This page, declared", that shows the page's own declaration and the verifier's answer. The testbench is the page where a visitor writes a declaration and reads the verifier's report beside it, in the browser. Here is its declaration, as the page prints it.

::: plate The testbench, as it declares itself
```zayn testbench.zayn
DEFINE SCREEN testbench (
  SATISFIES [SELECT, COMPARE, UNDERSTAND],
  ALWAYS_REACHABLE [EXIT]
)
//--> clean
```
In words: On the testbench, a visitor selects an example, compares the answers and understands them, and can always leave.
:::

Clean, as the page says. Writing a declaration, the visitor's act on this page, has no verb among the law's, and the page declares what the law's verbs can say; the question is with the Zayn project. The site's build does not take a page's word for it. It runs again every declaration that any page of the site shows beside its report, {{n:site.pairs}} of them, and compares what the verifier prints with what the page prints. A report "copied from a real run" is then, in the script's words, "verified, not asserted".

## Three instruments

Three instruments check the site's pages, each deciding what it can see. The verifier decides a declaration. The checks of the site's build decide a file: its text and its markup. They refuse a tooltip, which I ruled out on 6 November 2026 as a passing layer over the reading, so that a label says it instead. They refuse a link that carries a right arrow, a dash that can start a line, and a size or a colour outside the design's named sizes and colours. They refuse a page the registry does not list, and a phrase that lists what the project lacks. And they refuse a band of more than five entries, a band being the row of a section's pages under the main menu. On the site's eight redesigned pages, the eight that declare themselves, they also refuse a title of more than six words; on the other pages that check counts the titles it will refuse. One script keeps a rule of its own: "every figure on the site has a file, or it is not on the page", a figure being a number. Each check's comment names the remark, the ruling or the document it was written for.

The record keeps how these checks were first shown failing. On the pages as they were, the check that no link carries a right arrow counted 29 failures. The check that every page the site links is one the registry lists failed once, on the live site: the Why page linked the samples of the design system, which were a file outside the menu. They are now the page Samples, under Law, in the family Design system. A failure found that way stays in the record with its date, and the page is repaired.

The third instrument runs in a browser. The audit of the painted page, the page as a browser draws it, measures what is drawn. Its code lists six widths, from 320 to 1900 pixels, and the site's two cultures, Modern and Retro, two ways of drawing the same interface. It numbers its checks, K01 to K37. And a check of the build may excuse a line, through an allow list whose entries each give their reason; the excuse is checked too, for "an entry that matches no line fails, so the list cannot outlive what it excuses".

The audit's newer checks were built under the rule this chapter's principle states. "Milestone 2 builds the new checks and shows each one failing on today's pages first, with its count." Milestone 2 is the second step of the site's redesign.

## A remark, a check

Here is one chain of my remarks, told from the record: Zayn's repository at the commit this book reads, and the memos of the session that builds the site. The corpus, a file of the repository, keeps each remark of mine with its date. The session is an AI agent's, and its memos record what it measured in a browser on each commit.

On 15 November 2026 I asked for a testbench of the language in the browser, an editor with the code on the left and the verifier's report on the right, and the session built it.

On 16 November I asked that the testbench take the whole page, to give the code room. The audit's K35 now fails when the editor spans less than 90 percent of the window at 1085 pixels and wider; the memo of that day records it at 96 percent at 1440. A side list stands at the side of a page and lists the pages of its family and the headings of the page; I asked that the side lists hold no hierarchy. K34 fails on a list inside an entry, and the memo records all 33 pages with a side list kept flat. I asked for a button that maximises the editor in a popup. K36 then failed when the popup was under 98 percent of the window either way, when Escape left it open, or when the code typed before was gone. Later the same day I asked that the border between the code and the report be movable. K37 fails when the border moves less than 95 percent of a drag, or when a pane's change differs from the border's by more than 10 pixels. The next day's memo records a drag of 150 pixels in the page: the code's pane lost 149 and the report's gained 150, within the check's 10 pixels. The thresholds are the checks' own figures.

On 17 November, looking at the Designers page, I wrote: "not maximised on all the page". The check had measured the popup, not the editor in it. The editor filled 935 pixels of a popup 1596 pixels wide: the box was right, and the thing in it was not. The session changed the page and the check. K36 now measures the editor's own box, "the IDE's own box", in the record's words, "never the dialog's", the popup's. An IDE is an editor with its tools. K36 fails when the editor is under 98 percent of the window either way. It still fails when Escape leaves the popup open or the code typed before is gone. The memo records the editor at 1596 by 930 in a window of 1596 by 930, on the commit this book reads. Each of K34 to K37 was ordered to fail first, and the memos keep the measure each passed on the repaired page.

What does a declaration say about a button like that? A role is the promise a control makes about what acting on it does, one of five: `inert`, `navigate`, `reversible`, `irreversible` and `proposal`. `FOCUS`, `ACT` and `UNDO` are three of the law's verbs. Here is the testbench with its Maximise control, said wrongly.

::: plate Maximise, said as an act
```zayn testbench.zayn
DEFINE SCREEN testbench (
  SATISFIES [SELECT, COMPARE, UNDERSTAND],
  ALWAYS_REACHABLE [EXIT]
)

DEFINE INTERACTION maximise_ide (
  SATISFIES [FOCUS, ACT],
  ALWAYS_REACHABLE [UNDO, EXIT],
  ROLE navigate
)
//--> ROLE_ACTS_WITHOUT_CONSEQUENCE maximise_ide
```
In words: The testbench, and a control that maximises the editor: its role says it only changes what is shown, and its verbs say it acts.
:::

Refused. In the language's table of roles, `navigate` "changes what is shown, never what is true", and this control declares that it acts. The finding cites the three rules its contract binds, under Article II. Rule 112 lists opening a panel among the changes of what is shown. Rule 119 says that a card is not a button: a thing that promises to inform must not act, and this finding is that defect said in a declaration. Rule 16 is on intentional clicks. A control whose role is `inert`, which only informs, gets the same refusal when it acts. The report says the control promised "to change nothing": for `navigate`, that means nothing true. Here it is said as what it does: with `ACT` gone there is nothing true to undo, and `UNDO` goes with it.

::: plate Maximise, said as what it does
```zayn testbench.zayn
DEFINE SCREEN testbench (
  SATISFIES [SELECT, COMPARE, UNDERSTAND],
  ALWAYS_REACHABLE [EXIT]
)

DEFINE INTERACTION maximise_ide (
  SATISFIES [FOCUS],
  ALWAYS_REACHABLE [EXIT],
  ROLE navigate
)
//--> clean
```
In words: The testbench, and a control that brings the editor into focus, changes only the view, and can always be left.
:::

Clean, and it was true on the commit where the editor filled 935 pixels of 1596. The declaration states the focus and the way out; how large the editor is drawn belongs to the painted page, and K36 reads it. Each remark of the chain landed on the instrument that can decide it.

A side list with a level inside it shows the same division. Here is the Comparison family's list as it stood before my remark, written as a declaration for this book, with the family's third page, Frameworks and languages, left out for length. Its defect is the level, by my remark of 16 November that a side list holds no hierarchy, a rule of the site: the headings of the first page sit nested under that page's entry.

::: plate A side list with a level inside it
```zayn comparison.zayn
DEFINE NAV_GRAPH comparison (
  LABEL "Comparison",
  TARGET positioning,
  ENTRIES [overview, practices]
)
DEFINE NAV_GRAPH overview (
  LABEL "Overview",
  TARGET positioning,
  ENTRIES [the_claim, two_pages, corrections]
)
DEFINE NAV_GRAPH the_claim (LABEL "The claim", TARGET positioning)
DEFINE NAV_GRAPH two_pages (LABEL "The two pages", TARGET positioning)
DEFINE NAV_GRAPH corrections (LABEL "Corrections", TARGET positioning)
DEFINE NAV_GRAPH practices (LABEL "Practices", TARGET practices)
//--> clean
```
In words: The Comparison family opens on its overview, whose three headings sit one level down, then lists Practices.
:::

Clean. A menu with levels is lawful, and Rule 116, on how a menu's levels name each other, governs them. Whether the side list beside a page draws that level is a fact of the painted page: the same declaration can be drawn flat, and K34 reads the drawing.

## What I refused

**A public page that lists what the project lacks.** On 8 November 2026 I wrote, about the site: "Avoid this role of transparency that hurts the project image (negative markeing)!", spelled as the corpus keeps it. A page states what the work is and does; a failure found stays in the record with its date, as this chapter's chain does. The site's rule on writing now keeps the ruling, and a check of its files refuses such a phrase, with an allow list whose entries give their reasons. The house that publishes this book holds this book's web edition to the same rule.

**A figure typed by hand.** The ledger keeps the error that taught it, on 13 August 2026: "The site drifted under a heading claiming it could not." A census of the law, a count of its rules under a title that said it was computed from its file, had been typed by hand. Every figure of the site is now read from a file, and so is every count of the law in this book.

**A check that measures the container in place of the thing.** The chain above is its case: since my remark of 17 November, K36 measures the editor inside the popup.

[AUTHOR: the stake of this chapter, in your words: why a site that publishes a law holds its own pages to it, and what you want a team to keep from the chain of remarks; and whether the question that closes the exercise is the one you leave.]

## The court

The court of this chapter is these fixtures of the suite, each a declaration kept with the answer it must get. A control whose role promises to change nothing and that acts, with its twin, the same file made lawful. A lawful menu with levels. And the three codes of a menu that the site's build refuses on its own menu. The suite keeps no fixture for the one kind of finding at level 4, content that shoves the reading when it lands, and says why: it is "Undecidable from a declaration: it is a fact about a painted page." The checks K34 to K37 run in a browser, and this chapter gives what the record measured on the painted page, dated.

## Where the field leads

The field leads in the statement. Its sites state their conformance to a published standard and date the statement; GOV.UK's names an external audit and keeps its failures in a public list. The Zayn site states what its declared pages declare and runs each, and its checks are its own: "They are not part of the standard; they are this site's build." The audit is one page of the record, `tools/ui-audit.html`, which runs in a browser.

The field leads in the person. Its statements give a visitor a way to report a barrier, and its audits are made by a group, outside or its own. The Zayn site's record says it in its own words: "No counter can say the site reads well; the Principal looks at it in both cultures." The Principal is the record's name for me. Each remark of this chapter's chain was a person's.

And one site's evidence is one site's. The docket, where changes to the law are ruled, keeps a rule drawn from the site's pages as a proposal, because "it would want a second site before a ruling". This book's web edition is held to one rule of the same law, Rule 116, and to the site's rule on phrases of lack: the house that publishes it refuses both on every page.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that it is built after. Next names the direction.

Built: the site's menu as a declaration of {{n:site.menu}} entries, written by its build and checked there for the three codes of a menu. An excerpt of its Adopt section ran clean on this page. {{n:site.declared}} pages declare themselves, and the testbench's ran here. The site's build runs {{n:site.pairs}} declarations again against what each page prints, and checks the site's files. The audit of the painted page runs in a browser, K34 to K37 among its checks, and this chapter gives what the record measured there, dated. Designed: the closing part "This page, declared" on every page of the site, and the next steps of the site's redesign, where checks that count what they will refuse begin to refuse it. Next: the lessons of this book's fresh readers, who read each part before it is published, kept in the book's file of site lessons, taken to the site one remark at a time, each with a check written to fail first.

## In your hands

Here is a real defect from the site's record, of 14 November 2026. The design system's principles and its samples stood on the site, reached only from a sentence of one page, and no menu reached them; I asked that they be part of the site's menu, "not external auxiliary pages like that!". This exercise is written for the book from the record, with the Law section shortened and the two pages declared beside it. Write what you expect the verifier to answer, then open its answer.

::: plate For you: the Law section, and two pages beside it
```zayn law.zayn
DEFINE NAV_GRAPH law (
  LABEL "Law",
  TARGET rules,
  ENTRIES [rules, reader, violations, vibes]
)
DEFINE NAV_GRAPH rules (LABEL "The rules", TARGET rules)
DEFINE NAV_GRAPH reader (LABEL "The Reader", TARGET reader)
DEFINE NAV_GRAPH violations (LABEL "Violations", TARGET gotchas)
DEFINE NAV_GRAPH vibes (LABEL "Two cultures", TARGET vibes)

DEFINE NAV_GRAPH design (LABEL "Principles", TARGET design)
DEFINE NAV_GRAPH samples (LABEL "Samples", TARGET samples)
//--> clean
```
In words: The Law section opens on the rules and lists four entries; two more entries, the principles and the samples, are declared under no section.
:::

If you wrote clean, you read it right, and the defect is in the site: two pages that no menu reaches, which this file shows as two entries that no section lists. The site's build reads that on its files, against the registry, and its check of the registry found the samples so on the live site, as told above. Now add a family for the two pages to the section, with its landing first, and give its first page the family's own label. Say what you expect. Try before you read on.

::: plate The family added
```zayn law.zayn
DEFINE NAV_GRAPH law (
  LABEL "Law",
  TARGET rules,
  ENTRIES [rules, reader, violations, vibes, design_family]
)
DEFINE NAV_GRAPH rules (LABEL "The rules", TARGET rules)
DEFINE NAV_GRAPH reader (LABEL "The Reader", TARGET reader)
DEFINE NAV_GRAPH violations (LABEL "Violations", TARGET gotchas)
DEFINE NAV_GRAPH vibes (LABEL "Two cultures", TARGET vibes)

DEFINE NAV_GRAPH design_family (
  LABEL "Design system",
  TARGET design,
  ENTRIES [design, samples]
)
DEFINE NAV_GRAPH design (LABEL "Design system", TARGET design)
DEFINE NAV_GRAPH samples (LABEL "Samples", TARGET samples)
//--> MENU_LABEL_REPEATS_PARENT design
```
In words: The Law section gains a family, Design system, whose first page is labelled Design system as well, then the samples.
:::

Repair it, and say what you expect. Try before you read on.

::: plate The site's own form
```zayn law.zayn
DEFINE NAV_GRAPH law (
  LABEL "Law",
  TARGET rules,
  ENTRIES [rules, reader, violations, vibes, design_family]
)
DEFINE NAV_GRAPH rules (LABEL "The rules", TARGET rules)
DEFINE NAV_GRAPH reader (LABEL "The Reader", TARGET reader)
DEFINE NAV_GRAPH violations (LABEL "Violations", TARGET gotchas)
DEFINE NAV_GRAPH vibes (LABEL "Two cultures", TARGET vibes)

DEFINE NAV_GRAPH design_family (
  LABEL "Design system",
  TARGET design,
  ENTRIES [design, samples]
)
DEFINE NAV_GRAPH design (LABEL "Principles", TARGET design)
DEFINE NAV_GRAPH samples (LABEL "Samples", TARGET samples)
//--> clean
```
In words: The Law section's fifth entry is the Design system family, which opens on its Principles, then the Samples.
:::

Clean, and it is the site's own form. The first file was clean as well, with two pages no menu reached. Should a declaration be able to say that every page it names is reached by a menu, so that the first file is refused before the site's build sees it?

The law is printed in full in Appendix A, from its data, for the reader who will hold a site of their own to it.
