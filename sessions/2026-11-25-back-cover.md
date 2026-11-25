```yaml
by:        zayn book session · claude-opus-5-5 · 2026-11-25 11:45

subject:   the back cover, drawn and in the reader, as the author ruled it (BACK-01); commit a567314

why:       the author, relayed by the StzZui D1 session: "Add the back cover of the book"; then his two remarks on its text in
           this session, and his choice: "No second line"

did:
  - tools/make_cover.py draws the back (assets/cover/back.png) on the front's dark ground, in its faces and on its column:
    the tagline alone at its top, a description that opens on the problem, says what the book is about (UI governance, and
    Zayn, which enforces it the way a compiler enforces a language, as the interface layer of Softanza's AI governance
    stack) and who it is for, the line that every declaration was run, his portrait and note, the imprint, the free
    reader's address with its QR code (decoded and checked), the shelf and the licence; every count is read from the book's
    data; the tool fails rather than let two blocks touch; the front is redrawn byte for byte the same
  - rewrote the description twice on his remarks: the first draft was vague on the problem; the second told his own
    corrections, as if the book were a report on them
  - the reader turns the cover over on a click, with Front and Back named under it, as the first two books' readers do;
    checked in the browser at desktop and at 375 px
  - recorded BACK-01 in DECISIONS.md with his words; FORMAT.md follows
  - recorded the Zayn desk's answer to BOOK-ZAYN-09 in research/REQUESTS.md (relayed by the Zayn session): (a) confirmed,
    ten new rows for the author, five parts joined to rows already with him

state:
  book:      local commits a567314 and the memo commit that holds this file, the tip named in the hand-over, ahead of
             origin/main (a6daf3e, published by the desk, house f45b430); never pushed
  back:      assets/cover/back.png, sessions/2026-11-25-back-cover/front-and-back.jpg

waiting:
  - DESK-PIN-BACK: verify the book at the tip named in the hand-over, ask the author's go, pin it; the house's own card
             of the book may show the back -> the house desk   [routed by this memo]   class: outward

next:
  - me:      no commit after the tip until the desk answers; then Parts II, IV, VI and VIII

note:      the author's note on the back keeps the facts of the first book's back cover and ends "He designed Softanza, and he
           rules the changes to Zayn's law."; he may replace any line in src/structure.yaml (back_*)
```
