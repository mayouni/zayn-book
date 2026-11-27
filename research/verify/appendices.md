# Fresh verification: appendices B, D, E, G, H

Read: `.cache/as-read/app-{b,d,e,g,h}*.txt`, sources `src/en/a2, a4, a5, a7, a8`, `tools/build_book.py` (the eleven table functions), `tools/book_common.py` (`closed_lists`, `fields_by_kind`, `pack.files`), the snapshot `.cache/zayn-adaecc271/`, `data/book-run.json`, and chapters 1, 2, 6, 8, 9, 10, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23, 25 where the glossary points. Nothing run.

## 1. Count

`appendices B, D, E, G, H · claims checked: 148 · verified 140 · wrong 3 · unsupported 1 · overclaim 4`

Generated tables, all matching their sources at the pin: grammar (three `ebnf` blocks of `doc/language/GRAMMAR.md`, word for word, headings stripped of their numbers); families and invariants (`constitution/rules.json` 3.17); fields by kind (`VIOLATIONS.md`:278-285); closed lists (`DECLARATIONS.md` §5); levels and the per-level counts 10/25/4/1 (`conformance/violations.json` 1.11, 40 kinds); the 37 checks (`DESIGN-SYSTEM.md` §7, columns 1-4; the painted/files split matches `SYS_CHECKS` in `tools/ui-audit.html`:743, which leaves K18-K21 and K30 to the files, so 32 + 5); activities (`coverage-count.js`:23); media counts and the sole-carrier column (`conformance/media.json`, every row recomputed); carriage lists; grid closed cells (recomputed for haptic, print, luminous, signage) and the auditory, voice, print and machine counts (`coverage-placement.json`); the declarations column of Appendix H (`book-run.json`, all 26 rows). I did not recount the visual row of the grid, or the court and command columns of H, by hand.

## 2. Items

- a7:13 · "AI model. ... Chapter 1." · wrong (pointer) · ch01 never defines it; ch22:17 does ("a program that writes text, a declaration among others, from what it is asked") · point to chapter 22 and use its words.
- a7:11 · "acts on its own on a person's behalf ... and it may also draw interfaces" · overclaim · ch22:17 and ch23:15: "driven by an AI model, that acts for a user"; ch01:15 gives drawing to AI models ("AI models draw interfaces and AI agents use them") · use the ch22 definition and drop "may also draw interfaces".
- a7:41 · "0 when the file passes, 1 when it is refused. Chapters 1 and 25." · wrong (incomplete) · ch08:192 and ch25:7 ("its three exit codes"), ch25:136 `# exit 2` · add "2 when it could not read the file".
- a7:35 · "Diagnostic ... Chapter 8" · unsupported · ch08 never uses the word as a term; searched src/en for "diagnostic": 12 hits, none a definition · point to Appendix C alone, or define it where the chapters say "kind of finding".
- a7:23 and a7:87 · "the core ..., the commons ..., and a team's own local law"; "The tiers of law, core, commons and local" · wrong · ch21:15, 41: the proposal designs four tiers, the statute first · name the statute as the fourth tier.
- a7:21 · "One of the numbered measures of the painted page, K01 to K37" · overclaim · Appendix D:9 and ch10:151: five of them read the site's files · "the numbered checks of Zayn's design system, K01 to K37, most read on the painted page".
- a7:65 · "the pack is the 12 files of the law and the suite" · overclaim · `protocol/MANIFEST.json`: the 12 include the language specification (README, GRAMMAR, DECLARATIONS, VIOLATIONS), the contract and its schema, media and signal data, and only the suite's manifest · "the files a team pins: the law, the language, the contract and the suite's manifest".
- a8:13 · "Every count a page prints is read from Zayn's data files ...; no count is typed." · overclaim · a2 types "the ten declarations" (title) and "the four levels" (line 9); a7 types "K01 to K37"; H's own table counts the book's run, not Zayn's data · "every count of Zayn's data a page prints is read from it ...".

Source lines: the fields and lists tables say only "the language specification, version 1.7". Name `VIOLATIONS.md` and `DECLARATIONS.md`, as the grammar and checks lines name their files.

## 3. Reading problems

- a2:19 / Appendix B fields table · "beyond those every kind carries": the four are never named. The source names them (`VIOLATIONS.md`:271: `SATISFIES`, `ALWAYS_REACHABLE`, `SIGNALS`, `ACTOR`). Add them in one clause.
- Appendix E · perceive and trust print empty verb cells, and the legend says "closed means that the medium carries none of the verbs the activity owns", which is vacuously true of an activity with no verbs, yet no P or T cell is closed. The reason is in ch13:35 and `coverage-count.js`:21, 46. Add one sentence.
- Appendix H table · "Declarations run, kept": "kept" (the promise kept) is not explained on the page.

The glossary also leaves out words that the chapters use as terms: generator, widget, manifest, machine form, lawful twin, culture (Modern and Retro). Operator (a7:61) and painted page (a7:63) name no chapter (ch14:43, ch10:17).

## 4. Rules

- Appendix D, K23 prints the record's id "ZANE-READER-MENUPOS-01", the language's former name. It is not on the withheld list (`tools/withheld.json`), but the vocabulary rule says "The name is Zayn". Consider describing the id in brackets, as the build does for withheld names.
- No withheld name, no person named, no forbidden word found. The design system's "(from Zin, section 5.1)" stays out because the build drops column 5.
