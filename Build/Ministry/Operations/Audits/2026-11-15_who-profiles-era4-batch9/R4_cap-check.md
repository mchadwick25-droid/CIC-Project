# R4 cap check: era 4 batch 9

A fresh Opus agent did this check at full effort. It had not seen the drafting or the earlier rounds. This is the one targeted check under Mark's cap ruling of 2026-11-15, "Write it + one check (Recommended)", and it does not count toward the cap. It covers only three things. The first is the strings changed by round 3's fixes, in the batch's briefs, cards, `records.json` and README and in Open-Gaps 269. The second is the two new Decision-Log entries. The third is Open-Gaps 269's reference to the batch entry. No repo file was edited except this one. No paid calls were made.

**Verdict: NOT CLEAR. 0 blocking, 14 minor (R4-M1 to R4-M14).** Every round 3 fix was applied as R3_review.md words it, and none of them adds a wrong fact, misquote or wrong date. The minor points are three new unclear references or long sentences in the briefs, line ranges and record wording, a near-miss in an absence statement, and gaps in the two Decision-Log entries. The batch entry and the cap ruling entry also need the verdict of this check added, as earlier cap ruling entries have it.

## Findings

### Briefs

**R4-M1 (Theodore brief, para 3: "his" can be heard as Fabricius's own birth).**
- Text: "The bibliographer Johann Fabricius dates his birth in the city to 759."
- The sentence before ends on Angelo Mai, and this sentence names Fabricius before "his". A listener can hear Fabricius's own birth. The old wording ("He was born in the city in 759") had Theodore as subject.
- Source: PG99 l.351-352, "Theodorus Studites ... natus in eadem urbe est a. C. 759".
- Replacement: "The bibliographer Johann Fabricius dates Theodore's birth in the city to 759."
- Tested: 405 words, FK 7.20, Flesch 67.92. Rebuild the audio script.

**R4-M2 (Anskar brief, para 2: "his Life" can be heard as Rimbert's own Life).**
- Text: "Rimbert, his disciple and successor, wrote his Life with help from a fellow disciple."
- After the change to active voice, the second "his" sits right after Rimbert. This batch also holds a Life of Rimbert, so the reading is a real one. The old passive wording had no such reading.
- Source: WAITZ l.4790-4794, "libellus gestorum praefati pontificis ab ipso Rimberto alioque condiscipulo eius editus".
- Replacement: "Rimbert, his disciple and successor, wrote Anskar's Life with help from a fellow disciple."
- Tested: 405 words, FK 6.12, Flesch 77.62. Rebuild the audio script.

**R4-M3 (Clement brief, para 2: R3-M11 makes a 26-word sentence, with "he ... him" at the end).**
- Text: "The scholar Franz Miklosich argued that a Bulgarian disciple of Clement wrote it in the tenth century, and its narrator says he was always with him."
- The two added words take the sentence past about 25 words. Its close, "he was always with him", has two men to point to.
- Source: PG126 l.96738, "auctorem ejus S. Clementi, mortuo 916, convixisse".
- Replacement: "The scholar Franz Miklosich argued that a Bulgarian disciple of Clement wrote it in the tenth century. Its narrator says he was always with Clement."
- Tested: 370 words, FK 6.01, Flesch 73.04. Rebuild the audio script.

### records.json and Open-Gaps 269

**R4-M4 (John, `records.json`: the new Le Quien range still stops short of "728").**
- Text: "PG94 l.32054-32068, l.32111-32115; THEO l.73562, l.73735-73739"
- The claim quotes "hoc anno 727, aut subsequenti 728". In the file, l.32066 reads "Lentavit. Atque adeo hoc anno 727, aut sub-". L.32067-32068 are blank. L.32069 reads "sequenti 728, Joannem nostrum pro tuendis ima-", and l.32070 ends "scribere incepisse censeo." R3-M3 counted the blank lines as text. This is graded minor, as R3-M3 graded the same kind of range error.
- Replacement: "PG94 l.32054-32070, l.32111-32115; THEO l.73562, l.73735-73739"

**R4-M5 (Cyril and Methodius, `records.json`: the Life's line for A.M. 6393 is damaged, and Ginzel supplies the year).**
- Text: "Life of Methodius: 6 April, A.M. 6393 (GIN l.12536-12541); Ginzel works the year out as 885 and defends the date (GIN l.6170-6205)"
- Source: GIN l.12538-12539, "requievit sexta die mensis Aprilis tertia indictione appo / fi^ j*^ ... millesimo trecentesimo nonagesimo t ertio". The word "sexies" cannot be read in the OCR. Ginzel, at GIN l.6199-6205, says Dümmler's Latin reads "anno millesimo trecentesimo nonagesimo tertio" with "sexies" dropped. He restores 6393 from Šafařík's edition and all its manuscripts. The claim is right, but its witness should show where 6393 is read.
- Replacement: "Life of Methodius: 6 April, A.M. 6393 (GIN l.12536-12541, where the year is damaged in the scan; Ginzel gives 6393 from Šafařík's edition, l.6199-6205); Ginzel works the year out as 885 and defends the date (GIN l.6170-6205)"

**R4-M6 (Open-Gaps 269, census bullet: "printed" makes the claim about the printed page that R3-M1 took off the card).**
- Text: "(PG 94 l.32111-32115, printed "750", tied to Germanus's deposition)"
- R3-M1 changed the card to "the copy used here reads 750", since only an OCR text is held and the records read the 750 as a misread 730. This round edited the same parenthesis and left "printed".
- Source: PG94 l.32114, "præstitit anno Christi 750. quo Germanus solio de-".
- Replacement: "(PG 94 l.32111-32115, where the scan reads "750", tied to Germanus's deposition)"

**R4-M7 (Open-Gaps 269 and README: "of Sirmium" is literally absent, but a held note ties Methodius's diocese to Sirmium).**
- Text (Open-Gaps 269, added this round): "no held line names Methodius's jailer or calls him "of Sirmium"." The README carries the same sentence.
- Source: GIN l.13166-13173, an editor's note to the Salzburg account (Kopitar's edition, l.13135-13136): "Metbodii dioecesin pro antiqua Sirmiensi libenter instaurasse et amplificasse". R1 reports a search for "Sirm* near Methodi*", but this line has both words. The literal claim still holds, so this is minor. A reader of the re-score corrections should still know the note is there.
- Replacement (Open-Gaps 269): "; no held line names Methodius's jailer or calls him "of Sirmium", though an editor's note to the Salzburg account says John VIII restored his diocese in place of the old see of Sirmium (Ginzel l.13166-13173)."
- The same addition fits the README's Cyril and Methodius correction line.

### README

**R4-M8 (README, "John of Damascus, the live entry": nested parentheses).**
- Text: "(the scan reads 750; Le Quien ties it to Germanus's fall, which Theophanes puts in the year of the world 6221 (729/30))."
- The R3-M13 wording leaves one parenthesis inside another. Also, the held Theophanes heading (THEO l.73562) pairs A.M. 6221 with Goar's own Christian year, which the OCR gives as "A. C. 724" (the headings next to it run 719, 720, 722, 723). So 729/30 comes from the records' reckoning, not from a held line. The records already give the same figure, so this is left as it is.
- Replacement: "(the scan reads 750). Le Quien ties it to Germanus's fall, which Theophanes puts in the year of the world 6221, that is 729/30."

### Decision-Log entries (l.3393-3433)

**R4-M9 (cap ruling entry: Part 2's reviewer covered three profiles, not all seven).**
- Text: "Part 2's reviewer found no wrong fact, quotation or date in the briefs or cards, and no contested point told as settled."
- Source: R3_review.md l.271, Part 2: "No blocking content error remains in the three briefs or cards." Part 1 (l.9) found "no blocking finding" for the other four.
- Replacement: "Neither part's reviewer found a wrong fact, quotation or date in any brief or card, or a contested point told as settled."

**R4-M10 (cap ruling entry: the check's verdict and "the cap ruling is met" are missing).**
- The entries for era 4 batch 8 (l.3108) and era 6 batch 2 (l.3320) each give the check's verdict, what was done with its points, and that the cap ruling is met. This entry stops at "This entry and the batch entry below resolve R3-B1."
- Replacement, to add after that sentence once this check's points are handled: "Its verdict was NOT CLEAR, with no blocking point: every round 3 fix held against its source. It found 14 minor points: three unclear references or long sentences in the Theodore, Anskar and Clement briefs; two line ranges or witnesses in the records; "printed" and an absence note in Open-Gaps 269; nested parentheses in the README; and four points in these two entries and R3_changes.md. [Say which were applied.] As in the earlier cap rulings, the ruling is treated as met, since a minor finding needs no further round."

**R4-M11 (cap ruling entry: the check's scope is given as Mark's order, which the held record does not show).**
- Text: "run one targeted Opus check of only the changed strings, the new entry and Open-Gaps 269's reference to it, by an agent that had not seen the drafting or the earlier rounds."
- Source: R3_changes.md l.3 gives Mark's order as "run one targeted Opus check of only the changed strings". The new entries and the Open-Gaps reference were added to the check by the brief it was given. The entry has two new entries, not one.
- Replacement: "run one targeted Opus check of only the changed strings, by an agent that had not seen the drafting or the earlier rounds. The check also read the two new Decision-Log entries and Open-Gaps 269's reference to the batch entry."

**R4-M12 (batch entry, "Review": round 2's fixes were not all applied as reported).**
- Text: "Round 2, a targeted recheck in two parts, found 7 blocking and 34 minor points, all applied except two, which round 3 took up."
- Source: R3_review.md l.50-54 (R3-M2): the records half of R2-M2 was not applied, though R2_changes.md said it was. R3_changes.md l.10 completes it.
- Replacement: "Round 2, a targeted recheck in two parts, found 7 blocking and 34 minor points. All were applied except two that were left, and the records half of one that was missed; round 3 took up all three."

**R4-M13 (batch entry, "Review": Anskar's birth sits under "On the Kyiv card").**
- Text: "On the Kyiv card, a contested point was told as settled, and Robinson was misread on Anskar's birth."
- Source: R1_changes.md l.43 (C-K1, Kyiv) and l.53 (N-B2, the Anskar card's dates). These are two cards.
- Replacement: "On the Kyiv card, a contested point was told as settled. On the Anskar card, Robinson was misread on his birth."

### R3_changes.md

**R4-M14 (R3_changes.md, R3-M14: the fix does not say what the line says it does).**
- Text: "Applied through Part 2's R3-M11, which rewrites the same sentence and also says the additions are counted by their cards."
- The Open-Gaps 269 sentence now reads: "By the census Who rows, Greek East & Orthodoxy era 4 held five majors and Latin West & Catholicism ten. John of Damascus, Theodore, and Cyril and Methodius make the Greek East eight, and Anskar makes the Latin West eleven." It says nothing about cards. Part 2's R3-M11 gives the point only as its reason (R3_review.md l.392).
- Replacement: "Applied through Part 2's R3-M11, which rewrites the same sentence."

## Checked and passed

- **Each round 3 fix against R3_review.md.** Part 1 R3-M1 to R3-M13 and R3-M16, and Part 2 R3-M1 to R3-M12, are applied word for word. R3-M11 (Clement) was taken. R3-M14 went in through Part 2's R3-M11, and R3-M15 is the same range as R3-M3.
- **Each changed string against its source, read in context:**
  - Le Quien's 750 is at PG94 l.32114, and his sentence starts at l.32111 ("Alteram / posthac composuit").
  - Fabricius's "quod avus ejus ita diceretur" is at PG94 l.566-568.
  - Meyer's "mit geringen Abänderungen" and "Can. 1—5 ... fast wörtlich" are at MEYER l.1044-1047.
  - Codinus is at PG99 l.831-832, "Theodorum Studitam et Josephum (episcopum Thessalonicensem), ejus fratrem, laudat Codinus, Origg. C Pol.", and "ut ferunt" is at PG99 l.10267.
  - Rastislav's request is at GIN l.11396-11401.
  - Ginzel's working of 885 from the third indiction and Easter is at GIN l.6182-6199.
  - "canticis tertiæ horz decantatis" is at PG126 l.98437-98438, and the houses at Devol stay on the card, as at PG126 l.99117-99119.
  - "philologum clarissimum" (Miklosich) is at PG126 l.96732.
  - ROB l.2697-2699 has "he repeated again and again the words of Job". Adam's books 1-2 are dated perhaps 1074 at ADAM l.3551-3557.
  - The Life of Rimbert's rule is at WAITZ l.4794-4797 and ROB l.4269-4274. Schmeidler's margin "V. Rimb. c. 24." sits beside "positio est III idus Iunii" at ADAM l.6783.
  - The Arsenian redaction of 1406 is item 1 of the appendices at PAT l.162-166.
  - On who chose the prior, who built the monastery and the Studite rule, the Paterik's founding account agrees with the Chronicle (PAT l.1169-1170, 1219-1223, 1230-1233).
  - Cross's "Who ... your prior" runs from l.11853 to l.11860, with the running head at l.11856 and "‘your" at l.11860. "cloakf" is at ROB l.2652.
  - Mark's rule "each name sits at the point matching the dates the person was active" is at Decision-Log l.2031-2032.
- **Quotations.** No quotation in quotation marks was changed. The two the changed README line describes were checked in their files, as above.
- **Writing.** The other changed strings have no AI tell, no "not X but Y" turn, no colon reveal and no tail. Apart from R4-M1 to R4-M3, none has an unclear reference or a sentence past about 25 words, and the new identifiers ("the historian", "the scholar", "the bibliographer") fit their men.
- **Scores.** `grade_text` (FK ceiling and FRE floor 60): Theodore 405 words, FK 7.14, Flesch 68.34; Cyril and Methodius 406, 7.42, 67.53; Clement 371, 6.13, 72.94; Anskar 405, 6.09, 77.84. All pass, and they match R3_changes.md.
- **Audio.** All seven `audio/<id>.audio.txt` files equal the brief with "[calmly] " before the first paragraph and "[warmly] " before the last, two tags each, with the brief's final newline.
- **Decision-Log, checked against the record:**
  - The counts are right: round 1 had 14 blocking and 66 minor, round 2 had 7 and 34, and round 3 had 1 and 29.
  - The round 1 examples match R1_changes.md: A-B1, T-B1, B-K1, B-K3, C-K1, N-B2 and D-B1.
  - The round 2 examples match R2_review.md and R2_changes.md: five from round 1's wording, including "their own time" for Gauderich.
  - The batch plan of nine, with Stephen the Younger and Nikephoros I in one PG 100 volume, matches Rescore.md l.100.
  - The 400k handover matches Handover.md l.3.
  - Mark's Clement pick matches R1_changes.md l.5. PG 111's anonymous Life of "circa medium seculum X" is at PG111 l.241-244 and 36942-36947.
  - The majors, the lengths (405 to 406; 365 and 371), the Kyiv placing with 1062 and both traditions, the river counts and the ids all match the README and Open-Gaps 269.
  - "None was written before" holds, since no other Who profile for these seven was found.
  - The shape follows the batch 8 and era 6 batch 2 entries, except as R4-M10 notes.
- **Open-Gaps 269's reference.** "Decision-Log, "Who profiles, era 4 batch 9" (2026-11-15)" matches the entry heading "2026-11-15 — Who profiles, era 4 batch 9: ...". The README's Clement line cites it the same way, in the short-title form other Open-Gaps entries use (for example 235 to 244). The entry's own "What is still open" cites Open-Gaps 269, "Era 4 Who batch 9" (2026-11-15), which matches.

## Files and ranges opened

- The round 3 word diff (scratchpad `r3_diff.txt`), whole.
- The audit folder: R3_review.md l.1-62, 80-105, 125-143, 160-233, 267-425; R3_changes.md and Handover.md, whole; R1_review.md (grep for verdicts and "N-B2"); R1_changes.md l.1-60; R2_changes.md, whole; R2_review.md (grep for "their own", "fall", "two princes").
- Decision-Log.md l.2016-2042 (grep), 3095-3145, 3160-3168, 3310-3355, 3385-3433. Open-Gaps.md (grep for the Decision-Log citations and "Era 4 Who batch 9", l.3516). Rescore.md l.100 (grep "batch 9").
- Batch 9: all seven briefs and audio scripts; the clement card's `place`; the anskar card (grep); `records.json` (top).
- `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` l.552-580, 940-944, 1286-1299, 32050-32118 (grep "726", "727", "728", "750").
- `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` l.73558-73566, 73730-73742 (grep "A. M. 62").
- `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` l.348-356, 822-836, 10262-10269.
- `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` l.1040-1048.
- `ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt` l.6168-6208, 11392-11404, 12520-12545, 13125-13176, 13876-13880, 13980-13984 (grep "sexies", "Sirmi", jailer names).
- `theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt` l.96728-96760, 98428-98446, 99095-99122.
- `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt` l.241-246, 36940-36948.
- `rimbert_anskar-the-apostle-of-the-north_robinson1921.txt` l.2650-2653, 2690-2702, 4262-4282.
- `rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt` l.4786-4802.
- `adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt` l.3545-3560, 6774-6792.
- `kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt` l.150-175, 1160-1172, 1214-1242.
- `russian-primary-chronicle_cross1930.txt` l.11851-11861.
- `engine/m1/gates.py` (grep `grade_text`, the floors).
