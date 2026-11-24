"""How a declaration is judged against its promise.

Lineage: the Softanza book's tools/book_judge.py (softanza-book a9e3812) judged a Haro block against the output it promised on
`#-->` lines. This book's blocks are Zayn declarations, and what a declaration promises is the verifier's finding, so the
judge is new and the rule it applies is the conformance suite's own (Zayn conformance/README.md, "What conformance means"):
a set of findings is compared, never line numbers, message wording or order. The words under a block (WORDS) keep the
Softanza book's shape.

A promise line is a Zayn comment, so the file runs exactly as the page prints it:

    //--> MISSING_UNDO approve_payment     one finding the block promises: its code, then the declaration it is about
    //--> ROLE_UNDECLARED                  a finding the verifier reports on the whole file, with no name
    //--> clean                            the block promises that the verifier finds nothing
    //--> 10 SYNTAX_ERROR                  the same finding, as many times as the number says (a count before the code)

The verifier's `subject` is the declaration's name for most findings and a phrase for some ("irreversible purge_archive
declares UNDO"). The promise names the declaration; it is kept when that name is a word of the subject, so the wording of
a phrase is never pinned, as the suite does not pin it.
"""
import re

PROMISE = re.compile(r"^[ \t]*//[ \t]*-->[ \t]*(.*?)[ \t]*$")


def parse(text):
    """The promises a block carries, as a sorted list of (code, subject or None); 'clean' is the empty list.
    Returns (promises, stated): stated is False when the block carries no promise line at all."""
    out, stated, clean = [], False, False
    for line in text.replace("\r", "").split("\n"):
        m = PROMISE.match(line)
        if not m:
            continue
        stated = True
        words = m.group(1).split()
        if not words:
            continue
        if words[0].lower() == "clean":
            clean = True
            continue
        if words[0].isdigit() and len(words) > 1:
            out.extend([(words[1], words[2] if len(words) > 2 else None)] * int(words[0]))
            continue
        out.append((words[0], words[1] if len(words) > 1 else None))
    if clean and out:
        raise SystemExit("a block promises both 'clean' and a finding")
    return sorted(out, key=lambda p: (p[0], p[1] or "")), stated


def verdict(promises, diagnostics):
    """True when the findings reported equal the findings promised: the same codes, each as many times, and every
    promised name found as a word of its finding's subject. Severity, line and wording are not compared."""
    got = [(d.get("code"), d.get("subject") or "") for d in diagnostics]
    if sorted(c for c, _ in promises) != sorted(c for c, _ in got):
        return False
    left = list(got)
    # the promises that name a declaration choose their finding first
    for code, name in sorted(promises, key=lambda p: p[1] is None):
        match = next((g for g in left if g[0] == code and (name is None or name in re.findall(r"\w+", g[1]))), None)
        if match is None:
            return False
        left.remove(match)
    return True


WORDS = {
    "en": {
        "kept": "run: the verifier gave the answer this page expects",
        "kept_clean": "run: the verifier found nothing, as this page expects",
        "differs": "run: the verifier gave another answer than this page expects; here it is",
        "unpromised": "run: this page states no expected answer; here is the verifier's answer",
        "exercise": "exercise: written for you to run and repair",
        "not-run": "shown as written: {why}",
        "exit": "exit code {n}",
        "report": "The verifier's report",
        "envelope": "The same answer, as a machine reads it",
        "grammar": "the grammar for generation, on the same lines without those that state the expected answer: {answer}",
        "grammar_yes": "a sentence of it",
        "grammar_no": "not a sentence of it",
        "shell_label": "At the command line",
        "shell_kept": "run: the command returned the exit code this page states",
        "shell_differs": "run: the command returned another exit code than this page states",
        "in_words": "In words",
    },
}
