# Part X, *In Practice*, read from the programmer's door

Pages, in order: `ch25-the-command-and-the-gate.txt`, `ch26-a-site-under-its-own-law.txt` (the part has two). Each read once whole, then again with the brief's questions.

## Chapter 25, The command and the gate

1. **Remembered.** The gate reads one number: 1 for a refusal (a syntax error too), 0 for none even with warnings, 2 when the command cannot read its input. Plates 25.1 to 25.4 and two command lines run each value, and Plate 25.5 shows level 3 with a table adding two refusals that level 2 missed.

2. **Lost the thread.**
   - The command, as released: "the first lines of its source list the others". I am sent to a source I cannot open, for the verbs I came for.
   - "the contract at 1.11" (The command, as released) is used before "The contract, the file that binds each kind of finding" (What a team chooses), beside "the family's Diagnostic Contract" (v1.2.2 in the court's run). Two contracts, one word.
   - "fixtures" is used in the command section and only said in The court.
   - The court's run: "59 diagnostics and 77 reports" beside "40 diagnostics". Neither count is explained.
   - The verifier's "the operator must know": the book's word is user.

3. **Doubted.**
   - "undecidable is silence, never a pass", beside a printed "clean ... 0 violations at level 3" and exit 0, which a gate reads as a pass. The same page quotes a warning as "undecidable without more input". So a gate set to `--level 3` without `--symbols` passes everything, with no warning, and the page does not reconcile its three sentences.
   - "$ zayn check week.zayn --json": Where it stands says the reference ran every command line, and the missing-file line is Node's ("ENOENT: no such file or directory"). The prompt names a program the page never ran, and the page does not say how to start the reference for `check`.
   - "or reads the refusal with that in mind": an exit of 1 stops the build whatever a person reads.
   - Plate 25.3 promises "the next section shows what that means for a project", but the run over several files shows only INVISIBLE_STATE. Whether `zayn check entry.zayn week.zayn` clears UNRESOLVED_INTENT_FLOW is never run.
   - `--contract` and `pack --check` are named as steps of a gate, with no output or exit code on the page. The machine form is shown only empty, without the fields of a finding.

4. **Mine.** Exact exit behaviour. I got it: I could restate 0, 1 and 2, warnings leaving 0, level 2 by default, and `--quiet` printing nothing on a clean run, all without looking.

5. **Verdict.** `ready after the items above`. The exit codes are run and exact; the silent pass at level 3 and the question across files are only half-run. Stopped me most: "Clean: without the table, its checks are silent."

## Chapter 26, A site under its own law

1. **Remembered.** The Zayn site checks itself with three instruments: the verifier on its declarations (a menu of 57 entries, eight pages that declare themselves, 37 declarations run again against what each page prints), its build's checks on its files, and a browser audit, K01 to K37, on the painted page. The proof is the chain of 15 to 17 November, where K36 measured the popup in place of the editor, and Plates 26.4 and 26.6, which are clean while the defect stands.

2. **Lost the thread.**
   - A remark, a check: "One of its pages is left out, and the headings of its first page are nested under that page." Which page is left out, and is "that page" the first or the missing one? The plate shows neither.
   - "The corpus keeps each remark of mine": corpus is not said, and "the record" is not said on this page for a reader who opens here.
   - Where it stands: "checks that count their cases today begin to fail". I guess a mode that only reports, but the page does not say it.
   - "the site's eight redesigned pages" and "Eight of the site's pages declare themselves": are they the same eight?

3. **Doubted.**
   - Within the page: "K36 fails when the popup is under 98 percent of the window either way", then "K36 now measures the editor's own box". The first is in the present tense, and K36's threshold for the editor is never stated.
   - The principle: "each remark made on it leaves a check, written to fail on the page as it was". No K check is shown failing on an old page; the sentence about Milestone 2 quotes a rule, not a failing run.
   - Plate 26.1, "word for word", lists `build_family`, `web_family` and `audit_family`, declared nowhere, and runs clean. Chapter 25 warns on an INTENT_FLOW that resolves to nothing; an entry of ENTRIES that resolves to nothing gets no finding, and the page does not remark it.
   - "In the verifier's words, the role navigate 'changes what is shown, never what is true'": the printed report holds no such words.
   - "fails when the file differs from the registry" and "verified, not asserted" are told, with no script, exit code or failing run.

4. **Mine.** How a build wires the verifier into a site. I got half: which instrument decides what, and the landing rule, which I could infer (the first entry's TARGET equals its parent's). I could not rebuild the site's gate.

5. **Verdict.** `ready after the items above`. The plates run, and the exercise teaches what the verifier cannot see; the site's own gate is told and never run. Stopped me most: "K36 fails when the popup is under 98 percent of the window either way".

## For the part

- **Hand-over.** Chapter 25 closes on "Who reads that difference before the change ships?", and chapter 26 answers it: "Each remark of this chapter's chain was a person's." Chapter 25's bridge says the next chapter runs the command "on the Zayn site's own declarations". Chapter 26 runs plates, never a command line of the kind chapter 25 taught.
- **Contradictions.** Chapter 25: "designed the gate's step and the pack's check as steps of a team's build". Chapter 26: "built the Zayn site's menu ... written by its build and checked there". A gate step is built in one build and designed in the other, and neither page says how the two differ. Within chapter 25, the pack's instrument "answers 1 while a difference stays undecided", while the verifier at level 3 without a table answers 0.
- **Clearest plate.** 25.5 with the command line under it: one file, the table the only difference, two refusals and then a clean run.
- **Hardest.** 26.5: the defect it shows is not in the declaration, and the declaration runs clean.
- **What I take away.** A gate on 0, 1 and 2 that I could wire tomorrow at level 2. At level 3, I would pass `--symbols` on every line and keep each surface in the same file as the state it shows. And a check earns trust only after it has failed on what it is meant to see.
