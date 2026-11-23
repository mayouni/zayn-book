# The metaphor register (framework C5: one metaphor at a time)

Opened 2026-11-23, before Part III is drafted, so that the names are stable from the first chapter written. The contract (section E)
names this subject's ruling metaphors: **the law**, **the court**, **the constitution**. They are the subject's own words: the Zayn
repository calls its rules a constitution, with articles and rights, and amends it on a docket. The book did not choose them; it
keeps them, maps each once where it starts, and adds none. The author rules on every row (the choice of a ruling metaphor is his,
framework section 4); under DELEGATE-01 the register is applied as written until he changes it.

## Table 1. The ruling metaphors, term by term

| Term in the book | What it names, in the record | Where the record holds it | Where the book maps it |
|---|---|---|---|
| **the law** | the interface constitution and nothing wider: never business rules, workflow or the governance of an organisation (the author, 2026-08-08, as the contract records it) | `constitution/rules.json` | chapter 1; and in one sentence at the door of any chapter on the spine (chapter 8 does it) |
| **the constitution** | the law's own name for itself: its preamble, articles, rights, forbidden patterns and numbered rules, kept as one data file with a version | `rules.json` `metadata`, `preamble`, `articles`, `rights`, `forbidden`, `set1` to `set31` | chapter 16 |
| **an article** | one of the principles every rule derives from (`derived_from`) | `rules.json` `articles` | chapter 16; named with its numeral where a refusal cites one (chapter 8) |
| **a rule** | one numbered entry of the law, with its title, what to avoid, the solution, the reason, its article, its tier and its evidence | `rules.json`, the sets | chapter 16; printed by the rule card wherever a page opens one |
| **a right** | what a user is owed, stated in one sentence, with the rules that enforce it | `rules.json` `rights` | chapter 16; printed by the right card |
| **the court** | what proves a chapter: the conformance suite (fixtures with the findings each must get) and the run of the book's own declarations | `conformance/manifest.json`, `conformance/fixtures/`; `data/book-run.json` | chapter 9 in full; one sentence in each chapter's section *The court* |
| **a verdict** | the set of findings a verifier gives on one file; two verifiers agree when their sets of codes are equal | `conformance/README.md`, "What conformance means" | chapter 9 |
| **a finding**, **a refusal** | one entry of the verifier's report; a refusal is a finding whose severity is `error` | `conformance/violations.json`; the report | chapter 8 |
| **the contract** | the list of every kind of finding a verifier can report, each bound to what it cites in the law | `conformance/violations.json` | chapter 8 |
| **the docket**, **an amendment** | the record of proposed changes to the law and of what was ruled on each; a change to the law, made on evidence (Article VII) | `doc/AMENDMENT-DOCKET.md`; `rules.json` `metadata.lineage` | chapter 18 |
| **the stage words** (built, designed, next) | the three words that say how far a thing has come, carried from data and code | the house's HOUSE-24; each chapter's front matter | chapter 1; one sentence under each *Where it stands* until the preface says it once |

## Used once and put down, never sustained

**The lawful twin** (a refused fixture's repaired pair: the suite's own word); **the ladder** (the law's tiers side by side: kept
for chapter 17, where it is drawn, and written out as "three instruments" elsewhere); **the door** (a kind of reader: the series'
word, used in the preface and nowhere in a chapter's argument).

## Refused, by name

- **The police, the judge who punishes.** A verifier refuses a declaration before anything is drawn; nobody is punished, and words
  name states, never people (the estate's rule).
- **The linter's "smell", "lint", "nit".** A finding cites a numbered rule or says that it cites none; it is never a matter of taste.
- **Construction and the factory** (the first book refuses them by name; this book does not reopen them).

## One thing, one word (from the pilot's fresh readers)

| The thing | The book's word | Words it does not use for it |
|---|---|---|
| one entry of the verifier's report | a finding (a refusal, when it is an error) | a violation (the tool's own word, kept inside its quoted report), an issue, a defect of the tool |
| what is wrong in the declaration | a defect | a bug, a smell |
| a kind of finding in the contract | a diagnostic, with its code | a check, a rule (a rule is the law's) |
| what a medium shows of a declaration | the drawing; in a browser, the painted page | the rendered page, the render, the UI |
| the page's own check of a run | the answer this page expects | the promise (a promise is what a declaration owes its user) |
| the person or the AI agent an interface serves | the user | the operator (the law's word, kept inside quotations and inside a declaration's own names) |
