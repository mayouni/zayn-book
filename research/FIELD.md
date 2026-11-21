# The field, read at its sources

Every source the book cites about the field is in this register: the page, what the page calls itself, the date it was read,
how it was read, and the sentence the book relies on. Nothing about the field is written from memory. A source read for one
chapter is re-read on its own date before another chapter leans on it for a different sentence.

**How a source is read.** The page is opened in a browser by the book's session and the sentence is taken from the page's own
text. Where a fetching agent read the page first, the sentence was then checked in the browser, and the entry says so.
A quotation in a chapter is a few words, attributed; the rest is said in the book's words.

**The two axes** on which the book places an instrument of the field (the contract's section C, item 1): **when it acts**
(before the interface exists; on the painted page; in use) and **with what force** (advice; measurement; refusal).

Phase 1 opened the register with the five sources the pilot chapter (8, *The refusal*) uses. Phase 2 extends it to the whole
field: the Zayn site's sixteen items of 4 November 2026, re-read; the classics; the accessibility standards and the laws that
cite them; the platform guidelines; design systems and tokens; the linters; the model-based interface languages; the rules on
deceptive patterns; the guidelines for human and AI interaction; the protocols by which AI agents render or operate interfaces.

| Id | Source | What the page is | Read | The sentence relied on | When it acts · force | Used in |
|---|---|---|---|---|---|---|
| F-01 | *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C. <https://www.w3.org/TR/WCAG22/> ; the criterion's text on <https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html> | "W3C Recommendation", dated "12 December 2024" on the page | 2026-11-21. Title, status and date by a fetching agent from the first page; the criterion's text by the session, in the browser, from the second | Success Criterion 3.3.4, *Error Prevention (Legal, Financial, Data)*, Level AA: for pages "that cause legal commitments or financial transactions", "at least one of the following is true", and the three items are named *Reversible*, *Checked* and *Confirmed*. Its intent says it is "not the intent to require a confirmation for each save command" | on the painted page · a criterion, met or failed | ch. 8 |
| F-02 | Jakob Nielsen, *10 Usability Heuristics for User Interface Design*, Nielsen Norman Group. <https://www.nngroup.com/articles/ten-usability-heuristics/> | dated "April 24, 1994 · Last reviewed Jan. 30, 2024" on the page | 2026-11-21, by a fetching agent, then by the session in the browser | Heuristic 3 is named "User Control and Freedom"; its text says users need a clearly marked "emergency exit" "to leave the unwanted action"; its tips include "Support Undo and Redo."; the page calls the ten "broad rules of thumb" | at design and at review · advice | ch. 8 |
| F-03 | axe-core, Deque Labs: `README.md` and `doc/rule-descriptions.md`, branch `develop`. <https://github.com/dequelabs/axe-core> | the project's own README and rule list | 2026-11-21, by a fetching agent, then the README's sentences by the session in the browser | "Axe is an accessibility testing engine for websites and other HTML-based user interfaces."; "you can find on average 57% of WCAG issues automatically"; the rule list's columns are Rule ID, Description, Impact, Tags, Issue Type, ACT Rules; it held 105 rule rows on the day (counted by the agent), among them `color-contrast` and `button-name` | on the painted page · measurement, a refusal when a build reads it | ch. 8 |
| F-04 | ESLint documentation: *Configure Rules* and *Command Line Interface Reference*. <https://eslint.org/docs/latest/use/configure/rules>, <https://eslint.org/docs/latest/use/command-line-interface> | the documentation's "latest" pages; the version switcher showed v10.15.0 and v9.39.5 on the day | 2026-11-21, by a fetching agent, then the severities by the session in the browser | a rule's severity is "off", "warn" or "error"; "warn" "doesn't affect exit code"; "error": "exit code is 1 when triggered". Exit codes 0, 1 and 2 are listed, 2 for "a configuration problem or an internal error" | on program code, before it runs · refusal | ch. 8 |
| F-05 | eslint-plugin-jsx-a11y: `README.md`, branch `main`. <https://github.com/jsx-eslint/eslint-plugin-jsx-a11y> | the project's own README | 2026-11-21, by a fetching agent, then by the session in the browser | "Static AST checker for accessibility rules on JSX elements."; "Because it only catches errors in static code, use it in combination with @axe-core/react to test the accessibility of the rendered DOM."; its list of supported rules held 39 rows on the day (counted by the agent) | on the markup's source, before it is rendered · refusal | ch. 8 |

## What the register does not hold yet

The items of section C, item 2 of the contract that phase 2 reads: they are listed in the paragraph above. Until an item is
in this table with its date, no page states anything about it.
