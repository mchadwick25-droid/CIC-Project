# LPC story tellings: authoring notes (2026-10-27)

Opus authoring pass. Seven `telling` fields were added to `records/lpc/story/`, each placed right after `text:`. No other field was changed, and each file was checked to be byte-identical apart from the inserted line. All seven parse with `yaml.safe_load`. Running the m1 gates over `lpc` found nothing that touches `telling`. Two findings came up on these records, but they are older and not about `telling`: the readability gate scores election `tellable_as` at FRE 58.4, and two `claim_guards` entries fail retrieval-negatives-structured. Both are listed under "Problems found" below.

Grades come from `engine.m1.gates.grade_text`. Every telling clears the gate (FK ≤ 10, FRE ≥ 60). All seven fall below the report-only FK 8 band floor, and below the fleet's usual FK of about 6 to 8 (don 6.2, witt 6.8 to 7.9, cappadocian 7.2). Longer sentences would raise the grade, but they would break the brief's rule of mostly 12 to 20 words and none past about 25. I kept that rule. A reviewer may want to merge a few short sentences.

| Story | FK | FRE | Words | Longest sentence |
|---|---|---|---|---|
| election-of-cyprian | 6.3 | 73.9 | 245 | 23 |
| celerinus-writes-to-lucian | 5.2 | 80.0 | 275 | 22 |
| numidicus | 5.4 | 80.6 | 259 | 24 |
| hundred-thousand-sesterces | 5.9 | 74.4 | 247 | 22 |
| the-plague-and-the-enemies | 5.3 | 78.6 | 268 | 19 |
| the-death-of-cyprian | 6.0 | 75.5 | 288 | 22 |
| the-psalms-on-the-wall | 5.7 | 80.1 | 263 | 21 |

## Per story

**election-of-cyprian**
- Speech is taken from the `modern_rendering` of `lpc.quote.chosen-while-still-a-neophyte` (two sentences, verbatim) and `lpc.quote.ancient-venom-against-my-episcopate` (one clause, verbatim).
- Cyprian stepping back for older men, and the crowd at his door, come from Pontius §5 (anf05, lines 27826-27834). This is the source behind the record's own words "over his reluctance" and "did not want the office".
- The telling states the limits plainly: only Pontius calls him a neophyte; Pontius writes in praise; Pontius does not say how the people showed their favour (that last is a claim guard on the quote record).

**celerinus-writes-to-lucian**
- Speech is taken from the `modern_rendering` of `grieve-with-me-for-my-sister` (verbatim from "Grieve with me…" onward), `shut-up-in-two-cells` (only "But now we have reached the brightness itself"), `the-case-set-before-the-bishop` (final clause verbatim, with the condition paraphrased just before it) and `because-i-am-already-weary`.
- I rendered "So I know she has not sacrificed" myself, from Ep. XX §3 (anf05).
- The telling keeps all of these: the sister is unnamed and none of the three women speaks; Lucian's condition is stated; Candida did not sacrifice; both letters still call the act a great sin.
- Left out: Paulus's own charge to Lucian, the ruling that the women "remain as they are" until a bishop was appointed, and the meaning of "Tria Fata". The only gloss on Tria Fata is an ANF editorial footnote, so it stays unexplained.

**numidicus**
- Speech is taken from the `modern_rendering` of `numidicus-remained-unwillingly` (several sentences verbatim).
- One sentence was added to mark the textual variant: one manuscript and the older printed editions read "unconquered" (inuictus) where Hartel reads "against his will" (inuitus). This comes from the quote record's `divergence_note` and Hartel's apparatus. It is needed because that clause is the story's key point.
- The telling keeps that the place of the search is unknown and that none of the three left any words.

**hundred-thousand-sesterces**
- Speech is taken from the `modern_rendering` of `grief-and-not-without-tears`, `christ-redeemed-in-our-captive-brethren` (Galatians is attributed to Paul) and `a-hundred-thousand-sesterces`.
- The telling gives no conversion into modern money and no outcome. It ends with the money leaving Carthage, as `absent_detail` does.

**the-plague-and-the-enemies**
- Speech is taken from the `modern_rendering` of `a-dreadful-plague-broke-out` and `it-becomes-us-to-answer-to-our-birth` (only the quoted "It is right for us… to live up to our birth").
- The sermon is paraphrased from Pontius §9-10: the tax collector or the pagan, love of enemies, the poor who gave labour, and Tobias.
- I deliberately said only "not only to His own people" and left out "to strangers too". Hartel's critical Latin has only *non suis tantum*; "sed etiam alienis" stands only in the older editions (see the quote record's `divergence_note` and `use_note.not_for`).
- The telling keeps that Pontius is the only witness, that he wrote in praise, that it is unknown whether persecutors were helped, and that no pagan account survives.

**the-death-of-cyprian**
- Speech is taken from the `modern_rendering` of `the-people-kept-watch-at-the-door`, `thanks-be-to-god` and `let-us-too-be-beheaded-with-him`. Paraphrase is used for `a-standard-bearer-of-the-sect`, `o-blessed-people-of-the-church`, `he-covered-his-eyes-with-his-own-hand` and `the-trees-and-the-trembling-executioner`.
- The telling keeps all of these limits:
  - The Acta's compiler is unnamed, and the Acta is not a transcript.
  - Only the Acta gives "Thanks be to God" and the cry.
  - The two texts differ on who tied the cloths, and the telling does not choose.
  - The trees, Zacchaeus and the strengthening "from above" are only how Pontius tells it.
- The date comes from `modern_contrast` and the Acta VI (XVIII Kal. Oct.).
- Left out for length: the young women under guard, the walled-in crowd, the tunic handed to the deacons, the burial procession, and "on the sentence the two texts are not independent witnesses". The telling says "In both texts the sentence…" but does not state that they depend on each other. A reviewer may want that clause back.

**the-psalms-on-the-wall**
- Speech is taken from the `modern_rendering` of `the-psalms-hung-upon-the-wall` (four sentences verbatim) and `he-slept-with-his-fathers` (only the Scripture phrase, attributed to Scripture).
- The siege and the fever "in the third month of the siege" come from Possidius ch. 29 (possidius txt, line 4147). The will and the library come from ch. 31.
- The telling keeps that Possidius is the only witness to the sickroom.

## Problems found in the story records (not fixed)

1. **plague `text`**:
   - It says God shows kindness "to strangers as well as to His own". That rests on "sed etiam alienis", which is only in the older editions and not in Hartel's text, and the story record does not flag this.
   - "Bodies left where they fell" goes a little past the source, which says only that corpses lay over the whole city.
2. **numidicus**: the record carries no note of the inuitus/inuictus variant, though the story's central clause ("against his will") depends on it. The quote record does flag it.
3. **election**:
   - `tellable_as` fails the readability gate (FRE 58.4).
   - The trailer note says the Ep. XXXIX reference is "this record's own addition", but Ep. XXXIX is not listed in `sources` (only Ep. LXVII is).
   - `absent_detail` says Pontius is writing in praise "and he says so himself", but I found no such statement in §5.
4. **celerinus**:
   - `text` says Celerinus "had been imprisoned". Ep. XX itself speaks only of his "purpled" confession. The imprisonment may rest on other letters that are not cited here.
   - The `claim_guards` entry "do not tell Lucian's grant without…" fails the GUARD_MARKERS check in retrieval-negatives-structured.
5. **death-of-cyprian**: the `claim_guards` entry "the two texts differ on who tied the cloths…" fails the same GUARD_MARKERS check.
6. **psalms**: `text` places the siege "by the Vandals". Possidius (ch. 28) names Vandals and Alans with some Goths. This is a minor point.
