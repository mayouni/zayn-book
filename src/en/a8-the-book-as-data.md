---
id: the-book-as-data
appendix: H
number: 108
title: The book as data
status: draft
---

This appendix says how the book is made and where its parts are kept, so that a reader, a person or an AI agent, can check any page against its sources. The book is the public repository `mayouni/zayn-book`.

**The sources.** Each page is a text file in `src/en/`, in the book's own notation. A plate holds a declaration, the line "In words", and the answer the page expects at its foot: a line `//--> CODE name` for each finding the declaration must get, or `//--> clean` for none. The order of the parts, chapters and appendices is `src/structure.yaml`. Each chapter's research, written from Zayn's record before the chapter, is in `research/`, with the register of the field's sources, `research/FIELD.md`, and the reports of the readers who read each page.

**The evidence.** Zayn is read at its release v0.2.0, by the commit's hash. The build copies that commit into a folder of its own and reads nothing else of Zayn. Every count a chapter prints of Zayn's data is read from Zayn's data files at that commit, at each build, and printed in place of a token in the source.

**The run.** At each build every declaration on a page is written to a file and checked by Zayn's reference verifier, as `zayn check FILE --level N` would check it, and the answer is compared with the one the page expects. A declaration is kept when the answer is the one expected. Each chapter's court, the fixtures of Zayn's suite it names, is run the same way. The build fails on any answer that differs. The record of the run is `data/book-run.json`, and the reader, `en/index.html`, prints each report as the run gave it.

The run of this build, page by page:

{{bookdata}}

**The stage of a page.** Every page carries one of three stages in its banner: Draft, In review, Published. Only the author moves a page beyond Draft.
