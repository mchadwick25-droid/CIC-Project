## Council profiles, era 7 batch 1, round 2: Part C (Synod of Chanforan 1532)

**Council.** `synod-of-chanforan-1532`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/synod-of-chanforan-1532.brief.txt`, `audio/synod-of-chanforan-1532.audio.txt`, `synod-of-chanforan-1532.entry.json`, `records.json` key `synod-of-chanforan-1532` (now 102 claims, 9 contested claims, 9 absent details), and `README.md` l.11. The scope is `git diff f1f6cd220 HEAD` (branch `claude/cft-councils-era7-batch1`), checked against `R1_review.md` Part C and `R1_changes.md` Part C. The preface's three worker edits touch Worms and Augsburg only; none touches this council.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.87, Flesch 67.27. Longest sentence 25 words ("The articles survive in printings by the Dauphiné pastor Jean-Paul Perrin, the valleys' historians Pierre Gilles and Jean Léger, and the English envoy Samuel Morland."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (exact string match, two tags counted).
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file other than this part was written. No model, network or paid calls were made.

Abbreviations as in round 1 (GIL81, GIL44, PER19, MOR, LEG, MUS, MON, ZEZ, GOLL, COMEN, BEZA1, CRESP1).

## Verdict: REVISE (one blocking, three minor)

Every round 1 finding but C-S4 is closed, and C-S4 is held for the batch's single Open-Gaps entry at merge, as the R1_changes preface says. Every changed or added quote is verbatim, allowing for OCR. The rewritten dissent paragraph keeps each claim with its witness. The deposition is now told in Gilles's frame, and the teaser gives both sides.

One fix carries a new error. The C-B3 wording, "the valleys changed nothing but their view on bearing arms", reads Léger as saying the arms view changed at the Reformation. Léger says the opposite: they still held it in 1560, during Emanuel Philibert's war, and acted otherwise only later (C2-B1). The entry's `uncertain[12]` and records contested claim 3 carry the same reading.

The three minor findings are an editors' year told without the scan reading, an ambiguous "by Crespin's editors" in Gonin's `people` row, and a Perrin line range in claim 95 that does not hold the year it is cited for.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| C-B1 | CLOSED | Brief p.6 now gives Gilles's "some barbes" with their reasons (GIL81 l.2030-2034, "quelques-uns des Barbes ne consentirent pas à toutes les conclusions ... pas totalement nécessaires ... deshonoroit la mémoire"), then the two as "deux des principaux contredisans ... venus de dehors des Valées ... partirent sans congé ... s'en allèrent en Bohême" (l.2046-2052). "Gilles, on the majority's side" is fair to his "prétendues innovations" (l.2053). Blahoslav's envoys "aiunt se ... missos esse a coetu Waldensium" and stay "per integrum semestre unum" and "ad suos in Gallias revertuntur" (GOLL l.7176-7183). Goll's note names "Daniel von Valence und Johannes von Molines, die 'Abgesandten' der Waldenser" and calls the *Summa* Blahoslav's (l.7223-7226); the *Summa* of 1556 is headed at l.6424-6425. The fixer's three corrections to the review's wording are right: "objected" follows "contredisans"; "two of their leaders" follows "deux des principaux". Sentences 2 and 3 carry no "he says", but they follow "Gilles ... says" and precede "The Brethren's chronicle", so the witness is clear. Entry `uncertain[1]`, `uncertain[8]`, `outcome[2]`, `attended[7]`, Valence's `people` row, Gilles's `record` note, records claim 99 and contested claim 5 are in place and right (MUS l.6540-6542, MON l.9152, ZEZ l.11554-11555 read as quoted). "He does not speak of signing" holds (Searches). |
| C-B2 | CLOSED | Brief p.4: "In 1535, he writes, a ducal raid caught a guard keeping watch for ministers at the hamlet of Chanforans." GIL81 l.2327-2330 (the duke's patents to Bersour, 28 August 1535), l.2345-2349 (Bersour's raid at Rocheplate, "y surprit quelques hommes qui y faisoyent la garde"), l.2441-2445 ("l'un des surpris par Bersour faisant la garde ... qui estoyent assemblez en la bourgade des Chanforans"). "Muston puts Farel at this meeting": MUS l.6403-6410. The quote is unchanged and verbatim (l.2446-2447). Entry `attended[4]`-`[5]` and Peiret's `people` row tell the same frame. |
| C-B3 | CLOSED, with a new point | The exception is now in the brief, but the fix's wording misreads it (C2-B1). |
| C-B4 | CLOSED | Teaser: "Two barbes left for Bohemia; the sources differ on whether they walked out or were sent." Both sides are held: GIL81 l.2051 ("partirent sans congé"); PER19 l.6543, MOR l.21815, LEG l.22899, GOLL l.7176-7177, COMEN l.2805-2806. "New" is gone from "articles of faith". |
| C-S1 | CLOSED | Entry `outcome[5]` and `uncertain[6]`, records contested claim 2 and claim 100 are in place. GOLL l.7176-7179 ("ut viderent, an verum sit ... mutationem quandam accidisse in hac Fratrum Bohemorum Unitate. Item ministros, qui ante caelibes vixerant, uxores duxisse") is rendered faithfully as "whether the Brethren had changed and whether their ministers had married". "Told of discord at home" holds for both: "dissidium seu discordiam exortam" (GOLL l.7161-7162) and "a dissensionibus quibusdam domi ortis" (COMEN l.2806-2807, OCR). Comenius's six months: "menses integros sex" (l.2808, OCR). |
| C-S2 | CLOSED, with a new point | Records contested claim 1, claim 101 and `absent_details[5]`; entry `attended[6]`, Gonin's `people` row, the Crespin source and `uncertain[4]` are in place. CRESP1 l.49900-49911 reads as cited. Reading the note's "1552" as 1532 is sound: the same notes misprint 1526 as "IÇ26" (l.49904) and set Saunier's arrest in "février 1550" against "dès le printemps de 1532" (l.49984-49987), and Crespin's own text has Gonin taken in 1536 (l.49944-49962). See C2-M1 on telling that year to the reader, and C2-M2 on the `people` wording. Gonin's 1536 Geneva errand: PER19 l.12165-12170. |
| C-S3 | CLOSED | Peiret's `record` note, `datesNote`, `uncertain[4]`-`[5]`, the retitled `fromThoseThere[0]` and records claims 9, 34, 35 and contested claim 1 are in place. "Avoyent tenu alors leur Synode qui avoit duré six jours. Le procez Latin dit Capitulum" (GIL81 l.2464-2467) is rendered rightly as "had then held a synod that lasted six days". Keeping "participant" with the note was one of the two options round 1 gave. |
| C-S4 | OPEN (held for the batch's Open-Gaps entry at merge) | `Open-Gaps.md` has no Chanforan line yet (searched `chanforan`, case-insensitive). The entry is worded in R1_changes Part C. I checked its four witness points (MUS l.6470-6471, MON l.939-940, PER47 l.16687 and l.5383-5386, PER19 l.11976-11978) and found nothing wrong in it. It must be applied at merge. |
| C-M1 | CLOSED | "Heads of families" (PER19 l.11974-11975; MOR l.7937). "The people were present too" for "eciam dio del populo" (MON l.980-981). |
| C-M2 | CLOSED | "Pastor at Nyons in Dauphiné" (PER19 header l.2). The sentence is 25 words. |
| C-M3 | CLOSED | The thesis sentence is gone. |
| C-M4 | CLOSED | `uncertain[0]`: "printings by Perrin, Léger and Morland ... and in Gilles's summary". |
| C-M5 | CLOSED, with a new point | "Noch 1532" is verbatim (ZEZ l.6304). Morland's "in the year 1530" is at MOR l.21825-21826. The Perrin line range does not hold the year (C2-M3). |

## New findings

### Blocking

**C2-B1. Blocking (a fix's wording reverses a witness: Léger's arms view did not change at the Reformation).**

Locations:
- brief p.8: "Léger wrote in 1669 that the valleys changed nothing but their view on bearing arms." (the C-B3 fix);
- entry `uncertain[12]`: "Léger says they changed nothing but their view on bearing arms." (unchanged, same fault);
- records contested claim 3, Léger's side: "Nothing changed but the view on bearing arms" (unchanged, same fault);
- entry `outcome[17]` and records claim 91, "except on bearing arms": not wrong, but they leave the reader to supply the same misreading.

Evidence. LEG l.23072-23086. Léger's frame is the Reformation contacts: "Bien qu'au tems de la Reformation, les Vaudois ou habitans des Vallées, eussent envoyé des Députés pour conférer avec Bucer, Melanchton, Oecolampade, Zuingle, Luther, Calvin ... touchant les points de Doctrine, & de Discipline" (OCR normalised). Then: "Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement, car ils croyoient qu'il n'appartenoit qu'aus Magistrats de manier l'épée". He goes on: "Ils en étoient même encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert ... bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis." So the arms view was not changed by the Reformation contacts or the meeting. They still held it in 1560 and acted otherwise only later. The brief's sentence, with the thesis line gone, now opens the paragraph on what the meeting changed. A listener hears that the meeting, or the turn to the Reformers, changed their view on arms. Léger says it did not.

Fix:
- Brief p.8: "Léger wrote in 1669 that the valleys changed nothing but, after 1560, their view on bearing arms." (17 words for 15.)
- To stay at 400, brief p.6, sentence 2: "a slight to the leaders before them" becomes "a slight to earlier leaders" (GIL81 l.2034-2036, "deshonoroit la mémoire de ceux qui avoyent ... conduit ces Eglises jusqu'alors"). A scratch copy with both edits: 400 words (wc), FK 6.91, Flesch 66.98, longest sentence 25 words (`/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R2C/fixed.txt`).
- Entry `uncertain[12]`, last sentence: "Léger says they changed nothing. They still held in 1560 that only rulers should bear the sword, and acted otherwise later."
- Entry `outcome[17]`: add "Until at least 1560, he says, they held that only rulers should wield the sword; later they acted otherwise."
- Records contested claim 3, Léger's side: "Nothing changed at the Reformation; the view that only magistrates bear the sword held until at least 1560 and changed later: Léger (leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt l.23072-23086)."
- Records claim 91: add "; the exception is their old view that only magistrates should wield the sword, which they still held in 1560 and later gave up (l.23076-23086)", and widen the witness to l.23072-23086.

### Minor

**C2-M1. Minor (an editors' year told without the scan reading).** Entry `uncertain[4]`: "Muston, the Baum and Cunitz note and Crespin's editors put Farel in the valleys, or at the synod, in 1532." The note reads "En 1552" (CRESP1 l.49905). The reading 1532 is sound (C-S2 row above), and records claim 101 records it. But the entry tells Léger's heading "as our scanned copy reads it" (`datesNote`), and the same care is owed here. Fix, `attended[6]`, last sentence: "Crespin's editors say Martin Gonin and another barbe invited Farel and Saunier from Grandson to the synod of 12 September. Our scan reads 1552, a slip for 1532."

**C2-M2. Minor (an ambiguous witness tag).** Entry `people`, Martin Gonin: "invited Farel and Saunier to the synod, by Crespin's editors". It can be read as the editors doing the inviting. Fix: "Barbe of Angrogna; with another barbe, invited Farel and Saunier to the synod (Crespin's editors); sent to Geneva in 1536 (Perrin)".

**C2-M3. Minor (a line range that does not hold its claim).** Records claim 95: "the held letters date Morel's mission to 1530 (perrin_histoire-des-vaudois-fra_1619.txt l.14134-14143; ...)". PER19 l.14134-14143 tells the mission under "au regne du Roy François premier" with no year. The year is in the heading of Oecolampadius's reply, "escripte en l'annee 1530" (l.14262-14271, OCR). Fix: cite "perrin_histoire-des-vaudois-fra_1619.txt l.14262-14271".

## Verified

- **Changed or added quotes, verbatim (OCR allowed).** "partirent sans congé de l'assemblée" (GIL81 l.2051); "deux des principaux contredisans" (l.2047); "pas totalement nécessaires" (l.2033); "alors" and "Capitulum" (l.2464-2467); "assemblez en la bourgade des Chanforans au milieu d'Angrogne" (l.2444-2445); "M. Farel, qui avoit la barbe rouge, et un beau cheval blanc" (l.2446-2448, OCR "Farel."); "continuoyent de venir" (l.2450); "missos esse a coetu Waldensium" (GOLL l.7176-7177, OCR "haue" for "hanc" in the line before); "per integrum semestre unum" (l.7179); "dissidium seu discordiam" (l.7161); "une faible minorité" (MON l.9152); "noch 1532" (ZEZ l.6304); "Je ne trouve point qu'ils y ayent changé la moindre chose" (LEG l.23074-23075, OCR long s). Translations checked: Blahoslav's purpose clause, Gilles's "alors", Comenius's discord at home, Zezschwitz's "Zwei Geistliche und Führer jener Minorität". None adds anything.
- **Brief, changed sentences, each with its witness.** p.1 (PER19 l.11974-11975; MON l.980-981). p.2 (PER19 header l.2; GIL81 and LEG headers). p.4 (GIL81 l.2327-2349, 2441-2447; MUS l.6403-6410). p.6 (GIL81 l.2030-2052; GOLL l.6424-6425, 7159-7183, 7223-7226; GOLL header l.2, "Jaroslav Goll ... editor"; "Jan Blahoslav", l.3424). p.8 (C2-B1).
- **Teaser, datesNote, record notes, people rows.** As in the table. "From outside the valleys": "venus de dehors des Valées" (GIL81 l.2049-2050).
- **README l.11.** It still holds. Its third reason is now met: the brief tells the chronicle's own account, with the envoys' claim that they were sent.
- **Writing.** No empty contrast, no "X and never Y", no summing-up line, no filler in any changed string. Each changed sentence earns its place; the brief's ceiling is met because the fixes cost more words than the cut freed, not by padding.

## Searches run (absences)

All in `cic/texts/` with case-insensitive `grep`, long s as f allowed for.
- "He does not speak of signing" (entry `uncertain[8]`, records contested claim 5): `sign|soub|souscri|jur[eéè]|serment` in GIL81 l.1880-2200 (only the oath article, "jurer licitement", and "Ne jurez point"); `sign[eé]|soubsign|souscri` in GIL44 (three hits, all on other matters). The absence holds.
- Léger on arms after 1560: read LEG l.23050-23095 in place (C2-B1).
- Perrin's year for the mission: `1530|trente` in PER19 l.14000-14300 (one hit, l.14271).
- Crespin's note years: `Gonin` in CRESP1 (l.49849, 49883, 49923, 50235, 60221, 114326); the OCR year pattern read at l.49900-49911 and l.49980-49986.
- C-S4: `chanforan` in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (none).

## Counts

Round 1: 12 closed (4 of them with a new point), 1 open (C-S4, held for merge). New: Blocking 1 (C2-B1). Substantial 0. Minor 3 (C2-M1 to C2-M3).
