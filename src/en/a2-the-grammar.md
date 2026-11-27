---
id: the-grammar
appendix: B
number: 102
title: The grammar and the ten declarations
status: draft
---

This appendix gives the language as its specification states it at the pin, version {{n:lang.version}}. It holds the grammar in its notation and the {{n:law.verbs}} verbs a declaration may name. It holds the {{n:lang.kinds}} kinds of declaration with their fields, the closed lists of words, and the levels of checking. Chapters 6 and 7 teach them; this appendix is where a reader looks one up.

The grammar is written in a notation for grammars. `=` defines a name and `|` gives a choice. `{ }` repeats zero or more times, and `[ ]` is optional. A word in quotes is written as it stands, and `(* *)` holds a comment.

{{grammar}}

The verbs, by the families of the law. A declaration names verbs from these lists and from no other.

{{families}}

The kinds of declaration and the fields each carries. Every kind also carries four fields: `SATISFIES` and `ALWAYS_REACHABLE`, which take verbs from the families above, `SIGNALS`, which takes a status from its closed list, and `ACTOR`, which names who acts. A field marked as an identifier, such as `DENSITY` or `MOTION`, takes any word.

{{fields}}

The closed lists: each field that takes one word from a list, and every word the list admits.

{{lists}}

The levels: what each needs to read, what it decides, and how many kinds of finding it holds.

{{levels}}
