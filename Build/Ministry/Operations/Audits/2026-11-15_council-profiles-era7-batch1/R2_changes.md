# Round 2 changes: era 7 council profiles, batch 1 (2026-11-15)

Before the fixer, the worker applied four fixes in the brief and README. Worms: A2-B1 in the brief ("Charles produced a paper in his own hand"), A2-M1 ("published by John Wesley in 1778") and A2-M3 in the README ("Part of the Edict is held in its German text"). Chanforan: the brief sentence of C2-B1, in the worker's own wording after reading LEG l.23072-23086 in context: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, except that later they took up arms." It is paid for by "a slight to earlier leaders" and "in quotations by Alexis Muston". One fresh Opus fixer then applied the rest of the three round 2 rechecks, after re-opening each cited line. It checked that the worker's edits were in place and did not redo them. It did not edit `records.json`, `README.md`, `Open-Gaps.md` or `R1_changes.md`. All six JSON files pass `python -m json.tool`. No entry sentence runs past 25 words (script check). `mkaudio.py` regenerated the audio; only Augsburg's changed.

## Part A (Diet of Worms 1521)

Files changed by the fixer: `diet-of-worms-1521.entry.json` and `working/records_diet-of-worms-1521.json`. The brief is the worker's.

### Blocking

**A2-B1 (who read Charles's paper).** Applied in corrected form. The brief's "Charles produced a paper in his own hand" is the worker's edit, in place. Records `claims[60]` now reads: "Charles brought before the electors and princes a paper in his own hand, a full sheet long, later read in consistory at Rome. The held OCR ('£ « legger') leaves unclear whether he read it himself or had it read. He would hear Luther no more ...". Why corrected: PALL1 l.10137-10142 reads "voler'egli prima esporre l'opinion sua: £ « legger vna scrittura". The review reads the blob as "E fè legger" (he had it read). But "voler" can also govern "legger" (he wished to set out his view and read a paper). The held line cannot settle it. The review's own brief fix, "produced", is neutral for that reason, so the records stay neutral too, rather than asserting "had ... read".

### Substantial

**A2-S1 (Sarpi gives no arrival date).** Applied. SARPI l.9605-9617 re-read: "the ſeventeenth of 4pril" with no day of arrival. Records `contested_claims[2]` sides, entry `uncertain[4]` and entry `datesNote` replaced as the review gives them. The brief's "17 April" stands on all three.

**A2-S2 (the Table Talk's first hearing).** Applied. TT l.3547-3563 re-read: Luther's answer to the emperor, "for that end I desire respite of time", then "one day and one night". Entry `uncertain[2]` replaced as the review gives it.

### Minor

**A2-M1 (the printer).** Applied by the worker, in the worker's wording: "Herrnschmid's Life of Luther, published by John Wesley in 1778" (ARM l.2-3: Wesley the editor, R. Hawes the printer).

**A2-M2 (the Aleander hits).** Applied. Records `absent_details[3]` gains: "The Loyola letters' editors annotate him (ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt l.9858, 11088-11090). Mirbt cites Kalkoff's edition of the dispatches, not held (mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt l.15592)." Lines checked: Loyola v22 l.9858 and l.11088-11090 (Aleander annotated); MIRBT l.15592 "Kalk off. Die Depeschen d. Nuntius Alexander".

**A2-M3 (the README on the Edict).** Applied by the worker, as the review gives it.

### The brief's figures

399 words, 2:29 at 160 wpm, FK 7.12, Flesch 67.17, longest sentence 23 words.

### README text proposed

None beyond A2-M3, already applied.

### For Open-Gaps

None new.

## Part B (Diet of Augsburg 1530)

Files changed: `diet-of-augsburg-1530.brief.txt`, `diet-of-augsburg-1530.entry.json`, `audio/diet-of-augsburg-1530.audio.txt` (regenerated) and `working/records_diet-of-augsburg-1530.json`.

### Substantial

**B2-S1 (the translator).** Applied. BOC l.1466-1471 re-read: "carefully prepared by a Joint Committee of The General Council, The General Synod, The United Synod of the South, and the Joint Synod of Ohio ... The words in brackets are inserted from the German Editio Princeps." Entry `record[0].note` replaced as the review gives it. The witness label "H. E. Jacobs's Book of Concord" stays, since he edited the volume.

### Minor

**B2-M1 ("two other confessions").** Applied. Brief p.2: "and two other confessions." ZW2 l.1972-1977 (the Tetrapolitana) and l.1990-1994 (Zwingli's) re-read.

**B2-M2 (Buchheim's gapped sentence).** Applied. Brief p.8: "Waterworth puts the term in a September draft. Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November." Entry: the review cites `issue[3]`, but the Buchheim sentence is `issue[4]`; changed there to "Buchheim, writing on Luther's side in 1885, quotes the writ's aim ...". The entry's `record` note on Buchheim ("An 1885 historian on Luther's side") is a label, not a spoken sentence, and is left as it is.

**B2-M3 (Bensow's "säkerligen").** Applied. BENS l.31339-31341 re-read: "hvilken säkerligen betydligt afviker från den i Augsburg upplästa". Entry `uncertain[0]`: "the printed German surely differs considerably". Records `claims[107]`: "Bensow judges that the printed German text surely differs considerably ...", the rest unchanged.

**B2-M4 (no "September" in Pallavicino).** Applied. Entry `traditions[0].note`: "They refused the Catholic reply (Melanchthon) and the first terms of the decree (Waterworth's September draft; Pallavicino's first recess)."

**B2-M5 (Waterworth gives no date for the commission).** Applied. WAT l.2440-2446 re-read: the commission is told, then "On the I3th of July the reply ... was completed". Records `contested_claims[13]`, side one: "Told before the 13 July draft of the reply, with no date given: Waterworth (council-of-trent_canons-and-decrees_waterworth1848.txt l.2440-2446)".

**B2-M6 (the Exhortation in the Coburg absence).** Applied. LW4 l.15631-15671 re-read: the Exhortation and C. M. Jacobs's introduction (signed l.15723), "He began work on the Exhortation as soon as he was settled in the castle. On April 29 he wrote to Melanchthon that the work was growing under his hands." Records `absent_details[5]`, first two sentences replaced as the review gives them; the rest of the note unchanged.

**B2-M7 (the R1_changes preface miscounts the worker's cuts).** Not applied to `R1_changes.md`, which stays as written. Recorded here instead: the worker cut three words, not one, to keep the Augsburg brief at 400 in round 1: "two" in paragraph 2, Waterworth's "J." and "church" before "council at Uppsala". With B2-M1 applied, `R1_changes.md` Part B's line on "the two other confessions" is true again of the brief.

### The brief's figures

400 words, 2:30 at 160 wpm, FK 7.91, Flesch 60.26, longest sentence 25 words (the unchanged opening). This matches the reviewer's scratch figures.

### README text proposed

None.

### For Open-Gaps

None new. B-M10 (census differences) is still held for the batch's single entry at merge, worded in `R1_changes.md` Part B.

## Part C (Synod of Chanforan 1532)

Files changed by the fixer: `synod-of-chanforan-1532.entry.json` and `working/records_synod-of-chanforan-1532.json`. The brief is the worker's.

### Blocking

**C2-B1 (Léger on arms).** Applied in corrected form. LEG l.23070-23087 re-read. In talks with Bucer, Melanchthon, Oecolampadius and the others, "Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement", holding "qu'il n'appartenoit qu'aus Magistrats de manier l'épée". They still held it in 1560, during Emanuel Philibert's war, "bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis". Corrected: the brief sentence is the worker's (see the preface), not the review's, and the entry and records now match that reading:
- Entry `uncertain[12]`: "Léger says nothing changed in their dealings with the reformers. Their near-Anabaptist view, that only magistrates bear the sword, held until at least 1560. Only later, after the Maccabees' example, did they act otherwise."
- Entry `outcome[17]`: after the quote, "He names one exception: they were nearly Anabaptists on arms, holding that only magistrates should wield the sword. They still held this in 1560, in Emanuel Philibert's war, and acted otherwise only later."
- Records `contested_claims[3]`, Léger's side: "Nothing changed in their dealings with the reformers; their near-Anabaptist view that only magistrates bear the sword held until at least 1560, in Emanuel Philibert's war, and only later, after the Maccabees' example, did they act otherwise: Léger (... l.23072-23086)."
- Records `claims[91]`: the same reading, "acted otherwise only later" for Léger's "en ayent uzé autrement" (the review's "gave up" says more than he does); witness widened to l.23072-23086.

### Minor

**C2-M1 (the scan's 1552).** Applied. CRESP1 l.49905 "En 1552" re-read. Entry `attended[6]` ends: "Our scan reads 1552, a slip for 1532."

**C2-M2 (Gonin's witness tag).** Applied. Entry `people`, Martin Gonin: "Barbe of Angrogna; with another barbe, invited Farel and Saunier to the synod (Crespin's editors); sent to Geneva in 1536 (Perrin)".

**C2-M3 (Perrin's line range).** Applied. PER19 l.14134-14136 has no year; l.14271 has "escripte en l'annee 1530". Records `claims[95]` now cites perrin_histoire-des-vaudois-fra_1619.txt l.14262-14271.

### The brief's figures

400 words, 2:30 at 160 wpm, FK 6.93, Flesch 66.84, longest sentence 25 words.

### README text proposed

None.

### For Open-Gaps

None new. C-S4 is still held for the batch's single entry at merge, worded in `R1_changes.md` Part C.

## Counts

- Part A: 5 applied (two of them, A2-M1 and A2-M3, by the worker), 1 in corrected form (A2-B1), 0 not applied.
- Part B: 7 applied, 0 in corrected form, 1 not applied (B2-M7, recorded here).
- Part C: 3 applied, 1 in corrected form (C2-B1), 0 not applied.
