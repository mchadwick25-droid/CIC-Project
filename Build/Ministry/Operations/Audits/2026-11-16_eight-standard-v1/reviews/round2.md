# Round 2: targeted recheck of the round 1 findings

Reviewer: Opus, the same independent reviewer as round 1. I made no model or API calls and changed no file. I read the diff `497969db..HEAD` on `claude/cft-eight-v1`, which is three commits: 7d3d06ce, 80c1d909 and 59a4afdf. I rechecked only what changed. Every new or changed sentence was checked by hand against `cic/texts/`.

Comparators (drift guard 2): Gregory of Tours, and each brief's own round 1 text.

## Readability of the changed briefs (all pass)

| Brief | Words | Grade (full) | Reading ease (names out) | Words/sentence | Joins/100 |
|---|---|---|---|---|---|
| Athanasius | 390 | 9.0 | 78.6 | 18.6 | 0.8 |
| Constantine | 401 | 8.6 | 76.9 | 17.4 | 0.2 |
| Methodius | 372 | 9.2 | 74.4 | 17.7 | 0.3 |
| Gregory of Nyssa | 390 | 9.2 | 72.2 | 18.6 | 1.0 |
| John Chrysostom | 399 | 9.6 | 69.5 | 19.0 | 0.8 |

Origen, Ephrem, Gregory of Nazianzus, Gregory of Tours and Benedict have no change to their brief text.

## The fixes, one by one

**B1, Gregory of Nyssa: fixed in substance, but the new sentence is not yet in the reader's voice. Still BLOCKING (B1a).**
- The new sentence is "The held sources do not show what came of this teaching in his own day."
- What it says is right. It states the record's limit plainly, as Standard v1 asks, and it does not end on a bare how or why.
- But "held sources" is builder wording. It is the project's own word for what is vendored, and in a listener's ear it reads as process talk (Style Guide 1.11, status-announcement register; checklist item 4). It would also enter the bar that every future brief copies.
- The bar's own model is Gregory of Tours, "his is the only account we have". A fix in that voice: "The sources we have do not show what came of this teaching in his own day."
- This is a two-word change. A round 3 recheck of that one sentence closes it, within the cap.

**B2, John Chrysostom: CLOSED.**
- The new sentence is "... and by this, Socrates says, he brought back to the church's communion the followers who had left it over John's deposition."
- This matches Socrates VII.45 (npnf202 21453-21474): Proclus "brought back to the Church those who had separated themselves from it on account of Bishop John's deposition", and the admirers were "again associated in communion".
- The unsourced "restored him to communion" is gone.

**N14, Chrysostom's tradition: CLOSED, with a non-blocking note.**
- The opening now reads "... a preacher from Antioch in Syria and its plain way of reading Scripture, the tradition the tree calls Antiochene Exegetical Christianity." The census name is `antiochene-exegetical-christianity-chrysostom-ce`, "Antiochene Exegetical Christianity (Chrysostom-centered)", so the name now matches.
- "Plain way of reading Scripture" is supported by Socrates VI.3: Diodore "limited his attention to the literal sense of scripture" (npnf202 17182-17185). That is told again in paragraph 2.
- Note N15 (NON-BLOCKING): the first sentence now runs about 33 words, and it stacks three appositives on "John". "A preacher from Antioch ... and its plain way of reading Scripture" also yokes a city and a method to one "from". A split would read more easily, for example: "... the bishop was John, a preacher from Antioch in Syria. He came from its plain way of reading Scripture, the tradition the tree calls ...". This is a rhythm note only; nothing in it is wrong.
- N13 (NON-BLOCKING, unchanged): "carried John's body home". Constantinople was his see, and the old wording "back to the city" was exact.

**R1: CLOSED.** The `modern` fields for Constantine Q7 and Chrysostom Q18 now hold the rendering only.

**R2 and R3: CLOSED for the eight.**
- Each non-"same" entry in `quotation-originals.json` now carries an `uncertain` note: Q2, Q3, Q8, Q12, Q13, Q15 and Q19.
- Each note matches the comparison's card note word for word in substance, including Ephrem Q8.
- Q6 needs no note, because the brief no longer quotes it.

**R4: CLOSED.**
- Q1 now points to npnf204 19679, where "begotten not made" is printed (checked).
- Q5 now points to npnf201 64594, "that I am your fellow-servant", the letter after Nicaea (checked).
- Q18 now points to Palladius (Moore 1921) 6498-6499, "Glory to God for all things" (checked). It carries a `note` that the renderings were made on the same words in npnf109.

**R5, the Gregory and Benedict cards: CLOSED, with one new release blocker (R8).**
- Gregory of Tours, the new `uncertain` line:
  - It names Dalton's "all", the Latin plural "churches", and "this plan" from "ab hac intentione".
  - "ab hac intentione quievit" is in the MGH Latin (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` 18797). Checked.
  - The G2 `uncertain` note matches the comparison.
- Benedict, the new `uncertain` line on "daily" and "also":
  - "Multa mala facis, multa mala fecisti" is supported by the comparison's check of the held AASS Mart. III.
  - "The 1608 English" is the Gardner edition's translation. Checked.
  - The G9, G11 and G12 notes match the comparison.
- **R8 (BLOCKING for release; the card, not the brief).** Benedict's G10 `uncertain` note says "some manuscripts read 'conversatio' ... and the variant is contested."
  - No held file says this. The held Latin (`benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt` 8569) prints "CONVERSIONE MORUM SUORUM", with no variant note.
  - Gasquet's English carries none either.
  - The manuscript claim comes only from the renderers' memory, in first-renderings and second-renderings ("Many manuscripts read ..."). Elsewhere the comparison itself marks claims of that kind as NOT IN FILE.
  - The claim may be true, but it is a judgment on a manuscript with no held source. Checklist item 1 and `CLAUDE.md`, "never invent", keep it off a card.
  - Fix: cut the variant clause and keep the conversio reading's two renderings. Or vendor an edition that prints the variant, and cite it.
  - Round 1 should have caught this in the comparison's card note. It did not, and I record that miss here.

**Non-blocking fixes**
- Athanasius: "young" is cut. CLOSED. Nothing else changed.
- Methodius: the opening now says "two of Origen's admirers wrote about what he did". CLOSED. It now claims no more than Socrates and Eusebius-via-Jerome carry.
- Constantine: the Milan sentence is split. The new sentence, "They did it so that God in heaven might be kind to them and all they ruled.", keeps the edict's purpose clause (anf07 10684) and adds nothing. CLOSED.

**R6, documents: CLOSED.**
- The pattern's bar paragraph now says that its model passages and figures come from the earlier texts at `4f1b754d`. I checked that this commit exists and that it holds Methodius at 244 words.
- The pattern edit quotes Mark's existing "Revise, then record (Recommended)". The Decision-Log entry quoting it is already on this branch, against `origin/main`, for drift guard 1.
- The bar README's new table matches the tool's output for all ten.

**R7, length: CLOSED as recorded.**
- Ephrem, Nazianzus and Nyssa now have length lines. Nyssa's line says "390 words", which matches.
- All ten now run 372 to 430 words, so the round 1 batch observation stands as a note to the coordinator.

**Other changes in the diff.** Open-Gaps entry 300 was renumbered to 306 (commit 7d3d06ce). Entry 300 was never merged to `main` (checked: `origin/main` has no entries numbered 300 to 309), so the rule that a merged entry's number never changes is not breached.

**Anything new brought in.** Apart from B1a and R8 above, none of the changes adds an unsourced claim, a modern scholar, a quotation or an AI tell.

## Verdicts

| Brief | Bar compared against | Open blocking | Verdict |
|---|---|---|---|
| Origen | Gregory of Tours; its round 1 text (unchanged) | none | CLEARS |
| Methodius of Olympus | Gregory of Tours; its round 1 text | none | CLEARS |
| Constantine the Great | Gregory of Tours; its round 1 text | none | CLEARS |
| Athanasius of Alexandria | Gregory of Tours; its round 1 text | none | CLEARS |
| Ephrem the Syrian | Gregory of Tours; its round 1 text (unchanged) | none (R2 closed) | CLEARS |
| Gregory of Nazianzus | Gregory of Tours; its round 1 text (unchanged) | none | CLEARS |
| Gregory of Nyssa | Gregory of Tours; its round 1 text | B1a ("held sources") | DOES NOT CLEAR |
| John Chrysostom | Gregory of Tours; its round 1 text | none (B2 closed) | CLEARS |
| Gregory of Tours | its round 1 text; old Athanasius | none | CLEARS |
| Benedict of Nursia | its round 1 text; old Athanasius | none on the brief; R8 on the card | CLEARS (brief); release held on R8 |

Round count: this is round 2 of 3 for Gregory of Nyssa. Round 3 needs to recheck only the one Nyssa sentence and the Benedict card's G10 note.
