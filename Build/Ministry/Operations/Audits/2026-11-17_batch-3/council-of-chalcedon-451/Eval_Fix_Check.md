# Council of Chalcedon (451): check of the evaluation fix

Independent check, 2026-11-18, of the targeted correction ordered in the Decision-Log entry "Batch 3: four-reader evaluation; five pieces fixed before recording" (2026-11-18). Compared: `council-of-chalcedon-451.brief.pre-eval.txt` against `council-of-chalcedon-451.brief.txt`.

## Verdict on content (length aside): PASS

There are three small notes. None of them blocks (see points 2, 3 and 8).

## One hearing (read once, as a newcomer)

1. The dispute: Dioscorus's side would say Christ was "from two natures", one nature formed from two. The council said "in two natures", two natures kept distinct in one person, and to Dioscorus's side that split Christ.
2. Why it divided the churches: Leo's legates and the emperor's officials pushed "two natures" into the Definition and deposed Dioscorus. Egypt, Syria and later Armenia refused the council, condemned Eutyches too, and kept Dioscorus as a martyr.
3. What happened on the ground: Alexandria broke communion and there was killing on both sides. Palestine's monks chose their own bishop, and Dioscorus died in exile at Gangra.

The seeker's FAIL is cleared. The stake is said in plain words in paragraph 2. Five names are now given by role (Flavian, Anatolius, Proterius, Theodosius, Juvenal). "Their chronicle" is now "the Syriac chronicle" and "the same chronicle". The piece ends on Dioscorus's death and memory, not on a stray line. "Made it their fourth" is now "counted it their fourth general council". The narrator's "not 'from two' but 'in two'" is gone.

## Points

1. **The new lines trace to the outline and say only what their sources say.** The two-formula sentences come from Outline beat 5 and the Connection note (B14, B14a, B15, B20, E4). "Robbers" is in Leo's Letter XCV, npnf212 8640, verbatim (B4). Eutyches's "two natures before the union" is in Perry 23842–23844 (B1). "Kept his name as a faithful priest" is in Zachariah III.2 (E2). "One of their own" is Evagrius 3408–3420, a monk (E3). "Kept its Definition among its synods" is Wigram 14626–14638 (E7). "A new emperor and empress" and "Constantinople's new bishop" are role descriptions of A1, A4 and B12. Pass.
2. **Each side's claim is credited to that side.** "'Two' split Christ" is given to Dioscorus's side, "not for the faith" to the new bishop, the hand saying to the Syriac chronicle, and the riots to Priscus. Pass. Note: "The other side opposed Eutyches" can sound, by ear, as if Dioscorus's side did not. Paragraph 8 corrects this ("All three later condemned Eutyches"). The merge in the length section below removes the problem.
3. **The deposition grounds.** "And other charges" was dropped, so the three grounds now sound like the whole list. Outline beat 4 gives more charges. What is left is true, but it is narrower than the sentence. A minor note.
4. **No must-tell item or force was lost.** The trial, the guards and the absent officials, the legates' threat, "Leo or Dioscorus?", the Definition, the ban on other creeds, canon 28 and Leo's annulment, the emperors setting the council aside, the Serapeum burning, the abuse by the troops, the altar killings, both sides claiming Cyril, the refusers condemning Eutyches, Severus, the robe, and the Coptic martyr line are all still there. Pass.
5. **"Peter has spoken thus through Leo" was cut.** Nothing essential is lost. The outline asks for beat 3 to be given as "the Tome and its acclaim only". The acclaim that carries a must-tell point (both sides claimed Cyril) is "Leo and Cyril taught the same thing", and it stays. The Peter cry adds Roman authority, which the Connection note does not require. Pass.
6. **Quotations are otherwise unchanged.** A sort-and-diff of every quoted string shows: one cut (Peter), one addition ("not of judges but of robbers", verified), the formula labels moved into paragraph 2, and the "from two / in two" pair taken out of the narrator's contrast. Each kept quotation is unchanged, word for word. Pass.
7. **The last two paragraphs stay in the council's own time.** They cover Alexandria after Proterius (451 onward), Palestine's monks (451–452), and Gangra and Dioscorus's death (454). Pass.
8. **Final sentence.** In Zachariah, Dioscorus's name was proclaimed while he lived. "He died there, and his people kept his name" reads as after his death. "Kept" covers both, so this stays a minor note.
9. **Not taken (should-fix items, outside this fix).** These were not acted on: the Historian's point about 449 violence (only partly met, by "robbers"), Juvenal's restoration (Evagrius 3405–3450), and the seeker's point that "Every other creed was banned" may sound as if it includes Nicaea.
10. **`python -m engine.m1.profile_readability`:** 586 words, grade 8.6, reading ease 67.4 (names out), 14.0 words a sentence, longest sentence 31 words. Pass, with 0 failing.

## Length

The brief is 586 words, about 4:17 at 137 words a minute. Mark's 560 words would be about 4:05 in Daniel's voice. His "about 3:45" was worked out at 150 words a minute.

Cuts that lose nothing:

| Sentence | Change | Saves |
|---|---|---|
| P2 "The other side opposed Eutyches, a monk who said…" + P3 "Constantinople's bishop had condemned Eutyches." | Merge: "Constantinople's bishop had condemned Eutyches, a monk who said Christ had two natures before the union and one after." This also fixes note 2. | ~6 |
| P4 "…to Chalcedon, across the water from Constantinople." | Drop "across the water from Constantinople". | 5 |
| P8 "…by synod early in the sixth century." | Drop "early in the sixth century" and keep "by synod". | 5 |
| P8 "claimed Cyril of Alexandria" | "claimed Cyril" | 2 |

These cuts bring it to **about 568 words, about 4:09**.

Cuts with a cost (to reach 560 or below):

| Sentence | Cost | Saves |
|---|---|---|
| P3 "Leo of Rome called it a meeting 'not of judges but of robbers'." | It undoes the only step taken toward the Historian's point about 449. Leo is then introduced in P4 instead ("Leo of Rome sent legates…"). | ~10 |
| P7 "The Church of the East kept its Definition among its synods." | Drops outline impact 7, which should be carried in a single sentence. | 11 |
| P10 "…and his people kept his name as a faithful priest." | It partly repeats the Coptic martyr line, but it weakens the ending the seeker asked for. | 9 |

With the robbers cut as well: **about 558 words, about 4:04**. With the Church of the East cut too: **about 547 words, about 3:59**.
