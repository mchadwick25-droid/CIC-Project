# Craft check (shape): The Ebionites and Nazoraeans

This checks the one craft pass made under Mark's ruling "a" (Decision-Log, "Batch 11: the two rebuilt stories ship"). It covers the five changed sentences in `Craft_Pass_Shape.md`, read against `ebionite-nazoraean-current.brief.txt`, `Outline.md`, `Source_Sheet.md`, the cited lines in `cic/texts/`, Kit.md Part 1, and the two shape listeners. No `.v*` file was opened.

## Verdict: FIX

There are three changes, each exact. Change A is BLOCKING. Changes B and C are MINOR.

## Each changed sentence

### 1. Origen and the name (BLOCKING, both listeners): fixed, with one word risk

- **Source:** C2, ANF4 39116–39121: "receiving their very name from the poverty of the law ... for Ebion signifies 'poor'". The new sentence says less than its source. It adds nothing. The scorn stays in the next sentence (C3, ANF4 34023–34025). The listeners' fault is gone, because no "poverty of their Law" is left unexplained.
- **Risk:** "their name came from Ebion" can be heard as a person until the gloss arrives. The outline's Do not say list bars "Ebion, their founder" and says to leave Ebion out of the story (C5). The outline's own wording avoids the risk: "from the Hebrew for 'poor', Origen" ("Who they were").
- **Change B (MINOR):** replace `their name came from Ebion, Hebrew for "poor".` with `their name came from the Hebrew word for "poor".`

### 2. Symmachus (BLOCKING, skeptic): fixed, with one word too many

- **Source:** the new wording holds. Origen set Symmachus's version in his columns (G1, HE 34446–34449). Origen also called them "heretical sects" (ANF4 53781–53783, Against Celsus 5.65). Jerome used Symmachus's renderings (G4, JP 7541, 7553) and wrote of "the heresy of ... Ebion" (D6). The sentence adds no reason why they used it; G2b holds none. It carries the outline's Connection through an act, never through a "this matters because" line, so the skeptic's fault is answered.
- **Overreach:** "the writers" sounds like all of them, and the only one the listener has met is Irenaeus. Nothing held says Irenaeus used Symmachus.
- **Change C (MINOR):** replace `and the writers who called them heretics used his version.` with `and writers who called them heretics used his version.`

### 3. New sentence, "Its words survive only in their opponents' quotations." (BLOCKING, skeptic): barred, cut it

- **Source:** it rests on Source_Sheet line 29, a head note, and on the outline's Connection paragraph. Neither cites a passage. Line 29 is the researcher's summary of what is missing.
- **Part 1:** the sentence only says what is missing: the book is gone, and quotations are what is left. Part 1 bars this ("No sentence that only says what is missing"). It also repeats the one how-we-know statement the brief has already made ("Their own books are lost, so we meet them only through other church writers", paragraph 2). Part 1 allows that statement once, early. The repeat is a point told twice. The outline asks for this connection to be shown "never in a 'this matters because' line", and this sentence does that job without the words. It is also close to the outline's Do not say entry "the only words of their own that survive".
- **Listener fault:** the sentence does not fix what the skeptic named, which was what this gospel was to them. The outline holds only that they used it and let Jerome copy it (F7, F8). That meets the skeptic's own fallback: keep the scene only as far as the outline ties it to them. The paragraph already does this through acts: they let Jerome copy it, he put it into Greek and Latin, and he quotes it. Jerome's closing verdict then shows who kept their book.
- **Change A (BLOCKING):** delete ` Its words survive only in their opponents' quotations.` so that "...and says he put it into Greek and Latin." runs straight on to "In it, after the resurrection...". Without the sentence, "In it" still points plainly to the gospel.

### 4. "They were Jews in everything" (MINOR): holds

- B11, Pan 24955–24968. Epiphanius is credited once, in the paragraph's first sentence. "He says" stays on his own doubt and on the curse. The paragraph reads on one hearing.

### 5. The curse (MINOR): holds

- D3, Pan 25162–25168: "three times a day when they perform their prayers ... they curse them". The new wording, "prayed three times a day that God would curse the Nazoraeans", is the same act, said once. It adds nothing, and the reason given is still Epiphanius's own.

## Around the changes

Each paragraph that was touched reads on one hearing. The connection between the sentences holds. The Symmachus paragraph then the Beroea paragraph then Jerome's verdict show, through acts, that the writers who judged them kept and used their books.

## Count and scorer

- As it stands: `wc -w` **675** (cap 675). `profile_readability`: 672 words, grade 8.2 (names out 7.2), reading ease names out 77.5, longest sentence 33 words. Pass.
- With A, B and C applied (scratch copy only): `wc -w` **667**. `profile_readability`: 664 words, grade 8.3 (names out 7.3), reading ease names out 77.8, longest sentence 33 words. Pass.
- `check_brief_craft.py`: the same five items the listeners judged (s2 is the record's own question; s15, s18 and s23 name a source where Part 1 calls for it; s28 is a split across a closing quotation mark). Nothing new.
