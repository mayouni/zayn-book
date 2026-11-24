---
id: a-grammar-for-generation
part: 9
number: 24
title: A grammar for generation
stage:
  built: "a grammar for constrained decoding, as a file of {{n:gbnf.rules}} grammar rules written by a program from the language's second declaration, and compared on every run of the record's script with a fresh copy; a translation from the language's form into the grammar's; the verifier, which reads the language's form"
  designed: "the generate workflow of the Zayn site: a grammar for the shape and the verifier for the meaning, in a loop that a person runs with an AI model; the second declaration's places for the menu fields of language 1.6"
  next: "a decoder that holds an AI model to the grammar; the law served to an AI model while it writes; the ruling on which written form that decoder writes"
status: draft
research: research/ch24.md
fixtures: [unknown-intent, role-misplaced, comments-and-formatting, missing-cancel, missing-cancel-lawful]
---

A grammar for generation is a file of rules that says which texts are declarations, so that an AI model can be held to them while it writes one. Zayn's record has one, `zayn.gbnf`, written by a program from the language's second declaration: the language itself declared a second time, as data, in Haro, the language of this series' first book, which chapter 9 described; it declares the language, not a surface. In this chapter I read the file beside the language's own grammar. I run one declaration in each of the two forms the record writes it in: the language's form, which the verifier reads, and the grammar's form, which a decoder would write. Then I show where the record joins the two forms, and the question that join leaves open.

If you open the book here, five words come first, and every other word is said where it first appears. A **declaration** is a few lines that say what a user is doing on a surface. The **law** is Zayn's constitution of {{n:law.rules}} rules for interfaces, kept as a data file. Its rules are numbered to {{n:law.highest}}, because a number taken out of use is never given again. The **verifier** is the program that checks a declaration against the law. A **finding** is one entry of the verifier's report, and a refusal when it is an error. An **AI model** is a program that writes text, here a declaration, from what it is asked.

## The field

Constrained decoding is the field's name for holding an AI model to a form while it writes. A model writes its text a piece at a time, and the decoder is the part of the program that picks each next piece. A constrained decoder picks only the pieces that keep the text inside a grammar, a set of rules that says which texts are allowed, or a schema, a description of the fields a piece of data must have.

The llama.cpp project reads such grammars in a notation it calls GBNF: "a format for defining formal grammars to constrain model outputs". Its guide says that with it "you can use it to force the model to generate valid JSON", a common format for data. A rule is written `name ::= ...`, and "the `root` rule always defines the starting point of the grammar".

The providers of AI models do it with schemas. OpenAI's guide says its Structured Outputs hold a model's output "to your supplied JSON Schema", and adds that an application must still "validate any business rules that the schema does not express". Anthropic's guide says its structured outputs "guarantee schema-compliant responses through constrained decoding", and "guarantee schema compliance in most cases".

Research gives the method its measure. A paper of 2023 shows how to guide generation "with regular expressions and context-free grammars", and says it "adds little overhead": little extra work for each piece the model writes. Another, at a conference of the same year, says grammar-constrained decoding guarantees "that the output follows a given structure". A study of 2024 measured a cost: "a significant decline in LLMs reasoning abilities under format restrictions", LLMs being the large language models the field writes with.

Each source was read on 24 November 2026, and Appendix F lists them. So the field holds the shape while an AI model writes, and leaves what the text means to the program that receives it.

## The principle

**A grammar fixes the shape an AI model can write; what the shape means stays with the verifier.**

The Zayn site says of this file: "The grammar narrows what a generator can say, and it does not make what the generator says lawful." The file's own header says it in five words: "the decoder holds the shape". The shape is a declaration's frame: a kind, a name, and the fields that kind may carry. The meaning is what the law judges: whether a verb, one of the law's words for what a user does, is the law's, and whether an act keeps its way back.

A design note of Zayn's corrected an earlier claim that said more. That claim was that the grammar makes every word that breaks the law impossible to write. The note says it "overstates what the grammar holds", and draws the line where this chapter draws it: "a misplaced field and a malformed shape are unemittable". Unemittable means that a decoder held to the grammar cannot write such a text. Every other refusal stays with the verifier.

## The file and its form

The file has {{n:gbnf.rules}} grammar rules in GBNF. Of these, {{n:gbnf.kinds}} each allow one kind of declaration, and each kind has a grammar rule for the fields it may carry, which the grammar calls clauses. The grammar rule `root`, where the grammar starts, takes one declaration or more. Every declaration the file allows has one form: `DEFINE`, the kind, a name, the word `AS`, the clauses in parentheses, then `RATIONALE` and a reason in quotation marks. The reason is the declaration's account of why it exists. Two of the file's grammar rules are short enough to read here:

```
ident ::= [a-z_] [a-z0-9_]*
ws ::= ([ \t\r\n] | "--" [^\n]* "\n")*
```

The first says that a name, and every word in a list, opens on a small letter or an underscore, and goes on in small letters, digits and underscores. The second says what may stand around parentheses and commas, and between declarations: spaces, tabs, line ends, and a comment that opens on two hyphens. The file's header names its form: "-- comments, double-quoted strings, UPPER_SNAKE keywords, lower_snake identifiers, trailing commas". A keyword is a word of the language, such as `DEFINE`, and UPPER_SNAKE means written in capitals joined by underscores; an identifier is a name the writer chooses, and lower_snake is the same in small letters; a trailing comma is a comma after the last field.

Chapter 7 gave the language's own grammar, which the verifier reads; in it a declaration is written another way. The parentheses open right after the name, with no `AS`. A declaration carries no `RATIONALE`. A comment opens on two slashes. And the law's verbs are written in capitals: the language's specification matches them "case-sensitively in their uppercase form". So the record keeps two forms of one language: the language's form, which the verifier reads, and the grammar's form, which a decoder held to this file would write.

A program writes the file from the second declaration. The same program makes the forged evaluator: a second program that judges declarations as the verifier does, made from the second declaration with no hand in between. The script of chapter 9 compares the verifier with the forged evaluator. It also writes this file again on every run, and fails when the copy kept in Zayn's repository differs.

## One screen, two forms

Here is a screen of an order desk, a wholesaler's page where a clerk scans and filters the orders of the day, in the language's form. Under the plates of this section the build that makes this book prints two answers: whether the text is a sentence of the grammar, and the verifier's report.

::: plate The order list, in the language's form
```zayn orders.zayn gbnf
DEFINE SCREEN order_list (
  SATISFIES [SCAN, FILTER]
)
//--> clean
```
In words: On the order list, a clerk scans the orders of the day and filters them.
:::

Clean for the verifier, and not a sentence of the grammar. A sentence of a grammar is a whole text that the grammar accepts, from its first character to its last. Here the grammar meets a parenthesis where it wants `AS`, and the verbs are in capitals. Now the same screen in the form the grammar allows.

::: plate The order list, in the grammar's form
```zayn orders.zayn gbnf
DEFINE SCREEN order_list AS (
  SATISFIES [scan, filter]
) RATIONALE "A clerk scans and filters the orders of the day"
//--> 12 SYNTAX_ERROR
```
In words: The same screen, with the reason it gives for itself: a clerk scans and filters the orders of the day.
:::

A sentence of the grammar, and twelve refusals from the verifier! It read `DEFINE`, the kind and the name, met `AS` where the language's grammar wants a parenthesis, and from there answered one syntax error for the parenthesis it expected, then one for each word and sign it could not place. A syntax error is the verifier's finding when a text is not written in the language's form. The contract, Zayn's file of every kind of finding the verifier may give, each bound to the law, cites no rule for it: "It is a failure to read the declaration, so no law applies". The grammar accepts one form of the screen, the verifier the other. The join comes after what each one refuses.

## What the shape lets through

The grammar's lists take any name in small letters. Here is the order desk's home screen, in the grammar's form, with a verb its writer chose.

::: plate A verb of the writer's own, in the grammar's form
```zayn home.zayn gbnf
DEFINE SCREEN order_home AS (
  SATISFIES [navigate]
) RATIONALE "A clerk opens the order desk"
//--> 10 SYNTAX_ERROR
```
In words: On the home screen of the order desk, a clerk navigates.
:::

A sentence of the grammar: the grammar rule `ident` above takes `navigate`. Write the same declaration in the language's form, and the verifier reads it.

::: plate The same verb, in the language's form
```zayn home.zayn
DEFINE SCREEN order_home (
  SATISFIES [NAVIGATE]
)
//--> UNKNOWN_INTENT order_home
```
In words: On the home screen of the order desk, a clerk navigates.
:::

Refused: `NAVIGATE` is not one of the law's {{n:law.verbs}} verbs; `navigate` is the name of a control's role, not a verb. A decoder held to the grammar can write this verb, and the verifier refuses it once the declaration stands in the language's form. The repair uses the law's words.

::: plate The law's verbs
```zayn home.zayn
DEFINE SCREEN order_home (
  SATISFIES [DISCOVER, LOCATE]
)
//--> clean
```
In words: On the home screen, a clerk discovers what the desk offers and locates an order.
:::

Clean. A field in the wrong place is the opposite case: the grammar refuses it too. The grammar gives each kind its own grammar rule of clauses, and here is a screen's:

```
clause_SCREEN ::= "SATISFIES" sp namelist | "ALWAYS_REACHABLE" sp namelist | "SIGNALS" sp namelist | "ACTOR" sp ident
```

`sp` is one or more spaces and `namelist` a list of names in brackets; `ROLE` is not in it. A role is the promise a single control, an `INTERACTION`, makes about what acting on it does.

::: plate A role on a screen
```zayn orders.zayn
DEFINE SCREEN order_list (
  SATISFIES [SCAN, FILTER],
  ROLE inert
)
//--> ROLE_MISPLACED order_list
```
In words: The order list, and a role on the screen itself: acting on it changes nothing.
:::

Refused. Now the same declaration in the grammar's form.

::: plate The same role, in the grammar's form
```zayn orders.zayn gbnf
DEFINE SCREEN order_list AS (
  SATISFIES [scan, filter],
  ROLE inert
) RATIONALE "A clerk scans and filters the orders of the day"
//--> 15 SYNTAX_ERROR
```
In words: The same screen and its role, written in the grammar's form.
:::

Not a sentence of the grammar, for the role alone: a decoder held to the grammar cannot write it. The verifier answers the form, as before.

A screen's clauses have no place for a role. Here the grammar and the verifier agree, the grammar by its shape and the verifier by its refusal. That is the design note's line: a misplaced field cannot be written, and the unknown verb stays the verifier's to refuse. The repair gives the role to the control it describes.

::: plate The role, on its control
```zayn orders.zayn
DEFINE SCREEN order_list (
  SATISFIES [SCAN, FILTER]
)

DEFINE INTERACTION open_order (
  SATISFIES [SELECT, READ],
  ROLE inert
)
//--> clean
```
In words: The order list, where a clerk scans and filters; opening an order is a control that selects and reads, and acting on it changes nothing.
:::

Clean.

## Where the two forms meet

The record has a translation between the two forms, in the script of chapter 9. Its comment says what it does: a declaration "is translated MECHANICALLY" into the grammar's form. The script writes `AS` before the parenthesis, writes the words of every list in small letters, deletes the comments, and closes each declaration with `RATIONALE "none given"`, because a declaration in the language's form gives no reason. The translated text goes to the forged evaluator, and the verifier reads the original. The second plate above is the first, translated, with a reason of its own in place of "none given".

So the record joins the two forms in one direction, from the language's form to the grammar's. A declaration that a decoder would write in the grammar's form must be written in the language's form before the verifier can judge it, and the exercise below takes that step by hand. Which form a decoder is to write, and which program takes a declaration from one form to the other, is a ruling the language awaits.

## What I refused

**A reason in the language's form.** The grammar's form asks every declaration for a reason, and the second declaration says what adopting it in the language would be: "a language change, not a translation". The Zayn site records that I ruled on this difference. The second declaration dates the ruling 31 October 2026 and gives its words: "RATIONALE stays mandatory in the agent's grammar", the agent's grammar being the record's name for this file. A declaration in the language's form reaches the forged evaluator with the words "none given".

**A grammar that claims more than the shape.** The design note of 3 November 2026, read under the principle, is that refusal. The script says the same of the verbs: "The verbs are an identifier list and the semantic refusals stay the court's." The court, in that line, is the script's word for the forged evaluator; in this book the court is the suite.

**A grammar file that drifts from its source.** The script of chapter 9 refuses it, as read above: on every run it writes the file again and fails on a difference.

[AUTHOR: the stake of this chapter, in your words: why an AI model should be held to the shape of a declaration while it writes, and what you want the reason it gives to become.]

## The court

The court of this chapter is five fixtures of the suite, each a declaration kept with the answer it must get. Two are the refusals the plates met: an unknown verb and a role on a screen. Two are a flow that acts and its lawful twin, which the exercise meets. The contract files each kind of finding at one of four levels: level 1 checks that the file is well formed and uses the language's own words, level 2 decides what a single declaration states, level 3 adds a table of what the system holds, and level 4 is the painted page, the page as a browser draws it. A run at a level reports the findings of the levels below it too. The unknown verb is a word outside the law's, so level 1 refuses it; every report on this page is at level 2. The last shows the language's form at its loosest, with comments on two slashes, a comma after the last field and an empty body, and the verifier accepts it.

The suite pins the language and leaves syntax errors to each verifier, with its reason: "Recovery is not part of the language." Recovery is what a verifier reports after the first word or sign it cannot place. So the counts of syntax errors on this page are this verifier's.

## Where the field leads

The field leads in the decoder. Its grammars and schemas are read by decoders that run, in the programs that run AI models and in the providers' services. The field's decoders read GBNF, the notation of this file; a decoder that holds an AI model to it within Zayn's own loop is next.

Zayn leads in the second layer, the meaning. OpenAI's guide leaves what a schema does not express to the application, which must "validate any business rules". For an interface, Zayn names those rules: a law, a verifier that refuses by the rule or the article it cites, and a court of fixtures against which the verifier's refusals are proved. An AI model can read the verifier's report on the language's form, and chapter 22 describes the Zayn site's loop, a procedure a person runs, in which one does.

And the field measures the price of a held form. The study of 2024 found that reasoning declined under format restrictions, and, in reasoning tasks, generally more as the format tightens. That is the loss beside the win: a form held while an AI model writes can cost some of what it writes, and the field measures it.

## Where it stands

Built means that it ran on this page or runs in Zayn's repository at the release named under the title. Designed means that it is specified, and that its build comes after. Next names the direction.

Built: the grammar for generation, as a file of {{n:gbnf.rules}} grammar rules. A program writes it from the language's second declaration, and the script of chapter 9 writes it again and compares it on every run, where the Haro forge, the program that makes an evaluator and this file from the second declaration, is installed. The same script has the translation from the language's form to the grammar's. The verifier reads the language's form, and this page ran every plate on it.

Designed: the generate workflow of the Zayn site, the grammar for the shape and the verifier for the meaning, in a loop that a person runs with an AI model. The language has versions of its own, and its specification in this release is at version {{n:lang.version}}. The second declaration names version 1.4 of the language, and the grammar written from it carries the {{n:gbnf.kinds}} kinds and their clauses as of that version; the menus of version 1.6 are written in the language's form, and their places in the second declaration are designed.

Next: a decoder that holds an AI model to the grammar, the law served to an AI model while it writes, and the ruling on which form that decoder writes.

## In your hands

This exercise is written for the book: a declaration in the grammar's form, as a decoder held to the grammar would write it for the order desk. It releases an order for shipping. Say what you expect from the verifier, and why, then open its answer.

::: plate For you: an order released, in the grammar's form
```zayn release.zayn gbnf
DEFINE INTENT_FLOW release_order AS (
  SATISFIES [select, confirm, act],
  ALWAYS_REACHABLE [undo, exit],
  ACTOR clerk
) RATIONALE "A clerk releases an order once it is confirmed"
//--> 24 SYNTAX_ERROR
//--> INTENT_FLOW_NO_SATISFIES release_order
```
In words: A clerk selects an order, confirms it and releases it, with undo and exit within reach. The reason it gives says the same.
:::

A sentence of the grammar. The verifier read the name, answered the syntax errors, then a warning that the flow lists no verbs: it judged the declaration as a name with no fields. Every line of the report is about the form. Write the declaration in the language's form, keep the reason in a comment, and run it again. Try before you read on.

::: plate The release, in the language's form
```zayn release.zayn
// A clerk releases an order once it is confirmed
DEFINE INTENT_FLOW release_order (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, EXIT],
  ACTOR clerk
)
//--> MISSING_CANCEL release_order
```
In words: The same release, written in the language's form, with its reason in a comment.
:::

Now the law speaks. Repair it, and say what you expect. Try before you read on.

::: plate The release, with cancel within reach
```zayn release.zayn
// A clerk releases an order once it is confirmed
DEFINE INTENT_FLOW release_order (
  SATISFIES [SELECT, CONFIRM, ACT],
  ALWAYS_REACHABLE [UNDO, CANCEL, EXIT],
  ACTOR clerk
)
//--> clean
```
In words: A clerk selects an order, confirms it and releases it; undo, cancel and exit stay within reach.
:::

Clean. The first form is the grammar's, and the verifier's report on it is about the form; the verifier judged the law on the second and the third. Which form would you have a decoder write, and where would its reason live once the declaration stands in the language's form?

The verifier is a command, and a team can run it at the gate where its work is checked before it ships. Part X starts there.
