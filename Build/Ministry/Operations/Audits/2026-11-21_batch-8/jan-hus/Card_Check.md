# Card check: Jan Hus

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. Read: `jan-hus.brief.txt` (and `brief.v1.txt`, to see what the final brief dropped), `jan-hus.card.json`, `Card_Edits.md`, and each quoted line in its file. There is no starting card: Hus has no census entry yet.

**Verdict: FIX** (three changes below).

## 1. Each field is justified

Every field was checked against the evidence `Card_Edits.md` gives. Spot re-reads:
- datesNote, the birth and the death: Lützow's birth discussion (LUT 3007-3016) and Peter's date for the death (REL 17086-17089) stand.
- placeNote: Lützow says Hus "was born in the village of Husinec near the small town of Prachatice, which is not far from the frontiers of Bavaria" (LUT 3018-3020). He does not say "southern Bohemia". `Card_Edits.md` takes those words from the outline, but the card credits them to Lützow. See FIX 2.
- uncertain[9], the death and the stake: Peter's Latin at REL 17380-17387 is as the entry describes it.

## 2. Nothing else moved

Not applicable: new card, no starting card, no existing entry. The tradition-entry conflicts `Card_Edits.md` lists (Sigismund called emperor, the commended soul) belong to the tradition entry; the card follows the held texts on both.

## 3. References

The final brief dropped the date 2 September 1415 from the lords' letter. briefReferences[9] keeps it only as the name of the letter, which is the source of a told claim, so that part stands. One part names something the brief does not tell.

**FIX 1.** `briefReferences[9]`
- Old: "The lords' letter of 2 September 1415 (Palacký, Documenta): the seals, the verdict on Hus and the vow. World census, the Hussite and Bohemian Brethren movement: the cup as its emblem, the movement as a national one, and his story as its first voice."
- New: "The lords' letter of 2 September 1415 (Palacký, Documenta): the seals, the verdict on Hus and the vow. World census, the Hussite and Bohemian Brethren movement: the cup as its emblem, and the movement as a national one."
- Why: the brief does not tell that his story is the movement's first voice.

References kept as they stand: [0] to [8] and [10]. Each names what the brief tells, or the source a told claim comes from (Gregory XII's bull for the houses and hidden corners, Cerretanus for the papal official, Workman and Pope's note for the decree on the cup). [0] carries pass, stay, remain and return freely without quotation marks; those words stand verbatim in the brief, so marks would also be allowed.

## 4. Census rules

Only allowed keys; no `briefLength`; no `label`. The brief has five quoted spans (paragraphs 1, 11, 13, 15 and 17); the card has five entries, each `modern` word for word as the brief has it. "return freely." in paragraph 17 has its own entry, separate from the six-word span in paragraph 1. Each `printed` stands at its lines (re-read): DOC 13102-13103; DOC 15246-15249; WP 13341-13345; DOC 30155-30157; DOC 13103. Every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. The four spans of six words or more carry no `secondReading` yet, as the new-card prompt asks.

**Checked at card: "return freely."** "redire libere" (DOC 13103) is "return freely". The rendering is right.

**FIX 3. American spelling.** `uncertain[11]`
- Old: "ordered the Bethlehem Chapel, which it called a nest of heretics, destroyed and levelled to the ground"
- New: "ordered the Bethlehem Chapel, which it called a nest of heretics, destroyed and leveled to the ground"
- The words are the card's paraphrase of Lützow, not a quotation, so the spelling is the card's own.

## 5. Originals

- The safe-conduct, the Wyclif answer and the lords' letter each print Palacký's Latin, and each stands clean at its lines.
- The words at the stake. The outline renders them from Peter's Latin (REL 17380-17387). The card leaves the Latin out, and that is right under the batch 6 ruling. Some marks could be read as margin letters set into the line ("qp eccatis", "qmraedicavi", "1 aetanter"). But "mnihi" (17382), "wel" (17384) and "bomines" (17384) are misreads inside the words, and no other held file has the passage. The printed wording is Workman and Pope's English of the same speech (WP 13341-13345), and the entry's `uncertain` records where it differs from the Latin. Not a FIX.

## 6. Not found, and anything clearly wrong left in

**FIX 2.** `placeNote`
- Old: "Husinec, near the small town of Prachatice in southern Bohemia, by Lützow;"
- New: "Husinec, near the small town of Prachatice, not far from the frontiers of Bavaria, by Lützow;"
- Why: the card credits Lützow with words he does not print (LUT 3018-3020). Southern Bohemia is true, but it is the outline's phrase, and the brief does not use it.

Rulings on the points `Card_Edits.md` raises:
- "Dead since 1384" for Wyclif is the brief's, not the card's. The card does not repeat it. No card change.
- The bull's date of 15 May 1408 (uncertain[12]) is reckoned from "Idib. Maji, pontificatus nostri anno sacundo" for Gregory XII (DOC 18233). The ides of May is the fifteenth, and Gregory, elected at the end of 1406, was in his second year from late 1407, so 1408 is right. It stands, but it is a reckoning, not printed.
- legacy.remembered[0], the Czech public holiday, comes from the tradition entry and from no held text. It is true and it does not contradict the brief. Ruling: keep it.

Nothing else in the card is clearly wrong.
