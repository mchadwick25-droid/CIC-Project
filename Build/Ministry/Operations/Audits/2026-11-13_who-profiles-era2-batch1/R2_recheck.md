# R2 recheck: nine Who profiles, era 2 batch 1

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`, using `git diff 046fd04d HEAD` (the commit that added `R1_review.md`). Unchanged text was not re-reviewed. Every new or changed quotation and every new factual claim brought in by the changes was searched again in its vendored file with `wsfind.py` (whitespace-tolerant, tags stripped, quote marks straightened) and read in context, with the nearby translator's and editor's notes. No drafts were edited. No model calls and no paid calls were made.

Mechanical checks, all nine:
- `records.json` parses. All confidence tags use the five-level vocabulary.
- Each audio script matches its brief word for word once `[calmly]` and `[warmly]` are removed. `[calmly]` opens each one. `[warmly]` now comes right before the closing sentence in all nine, Antony and Hilarion included. No tags appear in the briefs or cards.
- `grade_text` passes for all nine. The highest FK is Pachomius at 8.4. The lowest Flesch is Arius at 60.2, just above the floor.
- Each card's `briefLength` matches its brief. Aetius now reads "about 2 minutes" for 316 words (1:57). Arius now reads "about 2 minutes 30 seconds" for 405 words.
- No narrator sentence in a brief runs past 25 words. Three long sentences are quotation-led: Arius's opening (33 words, mostly Socrates's quote), the Pachomius angel line (28, as in R1), and the new Frumentius letter line (28, 17 of them the emperor's words). One new Pachomius sentence runs 27 words, 7 of them Schodde's quote. Several new card sentences run 26 to 36 words (N8).
- No new "not X but Y" shape appears in a brief.

| Profile | Words | Est. length | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Melitius of Lycopolis | 322 | 1:59 | 7.2 | 60.8 | 324, within |
| Arius (major) | 405 | 2:30 | 7.9 | 60.2 | 405, at the cap |
| Pachomius (major) | 401 | 2:28 | 8.4 | 62.3 | 405, within |
| Antony the Great (major) | 404 | 2:29 | 7.2 | 69.2 | 405, within |
| Frumentius (major) | 401 | 2:28 | 7.9 | 60.4 | 405, within |
| Aetius of Antioch | 316 | 1:57 | 7.8 | 62.7 | 324, within |
| Hilary of Poitiers (major) | 401 | 2:28 | 7.4 | 63.7 | 405, within |
| Lucifer of Cagliari | 320 | 1:58 | 7.5 | 60.8 | 324, within |
| Hilarion of Gaza | 323 | 1:59 | 6.7 | 70.0 | 324, within |

Length assumes 162 words a minute.

## 1. The 9 R1 blocking findings

| Finding | Status | Note |
|---|---|---|
| Arius B1 (Robertson's summary of the prayer given as Athanasius's quote) | RESOLVED | "let me Thy servant depart" and "take off Arius" are exact (letter to Serapion, npnf204 l.70094, l.70097). Macarius as Athanasius's informant matches l.70064–70065. "Swore to Constantine that his faith was right" matches l.70068–70072. "Died suddenly the day before" matches the Sabbath timing (l.70093). "If not" is a fair short form of "but if Thou wilt spare Thy Church". The three views of the death are given "as Robertson reports" (l.4876). That is honest, but Sozomen is held and his own wording differs (N1). |
| Arius B2 (Robertson's statements given to Athanasius) | RESOLVED | Brief: "Robertson says he also taught Scripture" (l.1688–1690). Card: "Robertson reports that he was said to be a native of Libya, and dates his death to 336" keeps "We are told" (l.1676). `place` no longer says "born in Libya". records.json matches. The new card `dates` brings in a small new error (N2). |
| Arius B3 (start of the controversy told as settled) | RESOLVED | "Socrates ... starts the quarrel here" is attributed. Robertson: "The origin of the controversy is obscure. It certainly must be placed as early as 318 or 319" (l.1673–1674). "In Constantine's own letter, it began when Alexander asked his clergy about a passage of Scripture" matches the letter itself in Socrates I.7: "When you, Alexander, inquired of your presbyters what each thought on a certain inexplicable passage of the written Word" (npnf202 l.2474). The card and the new contested_claim give Socrates, Constantine, Philostorgius (Walford l.92) and Robertson. |
| Pachomius B1 (the "forty years" interval) | RESOLVED | The interval and the year 420 are gone from the brief and card. |
| Antony B1 (manuscript note on "poured water" dropped) | RESOLVED | Brief: "In the text he prints, the writer was Antony's attendant ... Robertson notes that some manuscripts make the attendant someone else." The note matches l.31199–31205. The translation is H. Ellershaw's and Robertson is the editor who thanks him (l.31138), so "the text he prints" and "Robertson notes" both stand. The card quotes "requires further sifting", which is exact. New contested_claim added. |
| Frumentius B1 ("Bishop of Auxumis" given to the emperor's letter) | RESOLVED | "Athanasius calls him 'Bishop of Auxumis'" (Apology 29, npnf204 l.36003). The letter's "the Bishop Frumentius" (l.36145) and "was advanced to his present rank ..." (l.36150) are exact. records.json gives each phrase to its owner. |
| Frumentius B2 (card "shipwrecked") | RESOLVED | "Taken as a boy when his ship's company was killed" matches Rufinus (Schwartz-Mommsen l.27307–27311). |
| Aetius B1 (nickname and uproar given to his fellow Arians) | RESOLVED | Brief: Flavian and Diodorus "raised such an uproar" matches Robertson, "raised such a storm" (npnf204 l.6237–6239). "Who led the orthodox party in the city" matches "orthodox Christians, headed by Diodorus and Flavian" (l.5713–5714). Sozomen's "many persons gave him the name of 'Atheist'" is exact (npnf202 l.32010). Card `otherNames` and remembered, and the records.json claim, name Socrates (no namer, l.8393), Sozomen and Athanasius. |
| Hilarion B1 ("the editor of Jerome's works", a role) | RESOLVED | "W. H. Fremantle's English edition of Jerome" fits the preface, where Fremantle says he went through every part and wrote the Prolegomena (npnf206 l.486–527). It names the edition, not the unsigned writer of the introduction, which is accurate. The card's new "religious romance" line drops a hedge (N5). |

**All 9 are resolved.**

## 2. R1 minor findings

**Melitius of Lycopolis**
- M1: fixed. The card carries Bell's full verdict: "excellent authority, probably in part that of Egyptian Bishops banished to Palestine" (Bell l.3157–3159). The brief keeps "good sources" to stay inside 2:00 and above the Flesch floor. The decline reason holds, since the brief has 322 words and a Flesch of 60.8.
- M2: fixed. "Peter wanted to be gentle with them. Melitius wanted to be strict." This matches Epiphanius: "Petri quidem oratio ad clementiam humanitatemque spectabat, Meletii vero ... veritatis ac divini ardoris" (Oehler l.43916–43918). It also matches Bell: Peter "represented the milder" view (l.3191).
- M3 to M9: fixed. "An unbending foe of the Melitians" is a fair rendering of Bell's "uncompromising opponent" (l.3150). The card date "about 306, by H. Idris Bell's dating" keeps Bell's hedge ("probably in 306", l.3205). Socrates I.6 is named on the card and in records.json.

**Arius**
- M1 to M8: fixed. "Has subsisted before time, and before ages, as perfect God" is exact (npnf203 l.6042). The songs "to be sung by sailors, and by millers, and by travellers" are exact (Walford l.114). "Extols Arius to the skies ... yet he asserts that the latter is involved in the most absurd errors" (l.116) supports "found fault with him too". "The mockeries which he utters in it" (npnf204 l.41481) supports "calls the lines that follow mockeries". "Constantine sent Arius into exile and ordered his books burned, Socrates records" matches Socrates I.8 ("an edict of the emperor sent Arius himself into exile", npnf202 l.2965) and Constantine's letter in I.9 (l.3378–3382). The change from "Photius calls him a liar" to the new previous sentence leaves "him" unclear (N3).

**Pachomius**
- M1 to M7: fixed. Gennadius: "founder of the Egyptian monasteries" and "received by angelic dictation" are exact (npnf203 l.42257–42258). Clarke's Pabau note matches note 132 (l.897). "Palladius places Pachomius's own house at Tabennisi" matches XXXII.1 (l.399) with XXXII.7 (l.403). The decline on M4 holds: the Rules stay under "Their own words", and the uncertain line now says nothing held is certainly his. The new Schodde quote on the card is cut short of its own qualifier (N4).

**Antony the Great**
- M1 to M9: fixed. Jerome 88: "sent seven letters in Coptic to various monasteries ... which have been translated into Greek" (npnf203 l.41177–41178). The sidenote there reads "Born 251, died 356", so the brief's "251 to 356" in Richardson's note is exact. Augustine: the officials found "the life of Antony" and meditated "giving up his worldly employments to serve Thee" (npnf101 l.12613–12620). "For I had heard of Antony" (l.13117). Coma "near the Heraclea" is Sozomen's (npnf202 l.27323). "Antony was unmoved" fairly renders "he made nothing very much of the letters" (npnf204 l.33186).

**Frumentius**
- M1: taken, but the fix rests on a mistake in R1, and it brings in a new blocking fault (NB1).
- M2: fixed. Robertson: "the chronology of the story (Gwatkin ...) forbids this altogether, while the letter of Constantius ... is most natural if the consecration ... were then a comparatively recent matter" (npnf204 l.5676–5682).
- M3: fixed. Jackson: "copied or varied by Sozomen, Socrates, and our author, from the version found also in Rufinus" (npnf203 l.7780).
- M4: fixed. "Frumentius was called the Abba Salama of Αὐξούμις (Axum)" is Hartranft (npnf202 l.29919). "The Father of Peace" is inside Jackson's quotation of the Dictionary of Christian Biography (npnf203 l.7767–7768).

**Aetius of Antioch**
- M1 to M7: fixed. "He built arguments, Socrates says, that deceived himself" matches l.8376–8377. "His associates in Arianism pronounced him a heretic" is exact on the card (l.8393). Coele-Syria, poverty and his mother are Philostorgius's (Walford l.178). The death "after the revolt of Procopius" matches IX.6 (l.342). The new line "stop using the word 'substance' at all" matches the creed of 360 in Socrates II.41: "it seemed desirable that it should be wholly abolished, and that in future no mention should be made of substance" (npnf202 l.8586–8587). "Eudoxius, bishop of Antioch" matches Robertson, "Eudoxius, bishop of Germanicia (of Antioch, 358, of CP. 360)" (npnf204 l.6245). The new first mentions of Sozomen and Photius are bare in this brief (N6).

**Hilary of Poitiers**
- M1 to M3: fixed. "Hilary Bishop of Pictavium" is exact in Rufinus (npnf203 l.45533). Watson: "The complaints against Hilary concerned his conduct, not his faith" (npnf209 l.1430). Augustine names Cyprian "loaded when he came out of Egypt", then Lactantius, "And Victorinus, and Optatus, and Hilary" (npnf102 l.51719–51722). "They had all come out of Egypt ... loaded with gold and silver" is a fair rendering.

**Lucifer of Cagliari**
- M1 to M5: fixed. Fremantle: "in company with the priest Pancratius and the deacon Hilarius" (npnf206 l.31422). Theodoret: "The Eustathians, led by Paulinus, a presbyter" (npnf203 l.11568). Fremantle: "according to Jerome's Chronicle, he died in 371" (npnf206 l.31454). Fremantle's "Luciferianism became extinct in the beginning of the following century, if not earlier" (l.31455) supports "had died out by early in the next century". The new opener matches Jerome, who has Lucifer "sent again to Palestine" when he "wrote a book against the emperor Constantius and sent it to be read by him" (npnf203 l.41268–41270). Davies through Jackson is exact (l.11596).

**Hilarion of Gaza**
- M1 to M7: fixed. Sozomen: "It is said that the above-mentioned families were converted through the instrumentality of the monk Hilarion" (npnf202 l.36372–36373). "He answered that he never left his cell" matches Life 14 (npnf206 l.30333). Hartranft: "Hilarion passed away about 371" (npnf202 l.21793). Jerome: "In his eightieth year" (npnf206 l.31055).

## 3. New or changed quotations, checked word for word

All exact:
- Arius: "has subsisted before time, and before ages, as perfect God." (npnf203 l.6042). "let me Thy servant depart." (npnf204 l.70094). "take off Arius." (l.70097).
- Frumentius: "the Bishop Frumentius," (npnf204 l.36145). "Bishop of Auxumis." (l.36003).
- Pachomius, card: "founder of the Egyptian monasteries" and "received by angelic dictation." (npnf203 l.42257–42258). "if not verbatim from his pen, are yet authentic enough" (Schodde l.162), but see N4.
- Antony, card: "requires further sifting." (npnf204 l.31205). "near a hundred and five" (l.33446).
- Lucifer, card: "To what extent he was an actual schismatic remains obscure." (npnf203 l.11596).
- Hilarion, card: "a sort of religious romance" (npnf206 l.30093). "Hilarion passed away about 371" (npnf202 l.21793). "is said" (l.36372).
- Melitius, Aetius and Hilary: no new direct quotations. The changed paraphrases are checked in section 2.

## 4. New faults in changed text

### New blocking

- **NB1 BLOCKING (Frumentius, card legacy and records.json).** "Blomfield Jackson's note to Theodoret, quoting the Dictionary of Christian Biography, says the emperor Constantius later asked the prince of Axum to replace Frumentius with an Arian, Theophilus, without success." The Theophilus sentence is Jackson's own, not the Dictionary's. In Jackson's note the quotation from the Dictionary ends with its citation, "(Dict. of Christ. Biog., Art. Ethiopian Church)". Then Jackson goes on in his own voice, outside the quotation marks: "Constantius afterwards wrote to the Ethiopian Prince to ask him to replace Frumentius by Theophilus, an Arian, but without success (Ath. Ap. ad Const. 31)" (npnf203 l.7768). This gives a writer's own sentence to the document he quotes, which is the witness swap R1 named as the most serious pattern in this batch. R1 M1 caused it: R1 said the Theophilus line came from the Dictionary, and that was wrong. The records.json claim repeats it ("Dictionary of Christian Biography, quoted in Jackson's note"). Jackson's own citation, Apology 31, does not name Theophilus (no "Theophilus" in npnf204 l.35990–36200). Philostorgius does send "Theophilus" to "the Aethiopians who are called Auxumitae" (Walford l.160), but he places the mission under Constantine, and Walford's note there disputes it (l.608). Fix, card: "Blomfield Jackson, in a note to Theodoret, says the emperor Constantius later asked the prince of Axum to replace Frumentius with an Arian, Theophilus, without success. He cites Athanasius's Apology, which does not name Theophilus." In records.json, give the witness as Jackson's own note, and keep "not in Apology 31 itself".

### New minor

- **N1 (Arius, brief and card).** "Sozomen, as Robertson reports, gives three views ... Most people blamed a weak heart." This attribution is honest. But Sozomen is held, and his own words differ from Robertson's summary. Sozomen writes: "Some believed that he died at that very hour, seized by a sudden disease of the heart, or suffering weakness from his joy ...; others imagined that this mode of death was inflicted on him in judgment ... Those who held his sentiments were of opinion that his death was brought about by magical arts" (npnf202 l.30402–30406). "Most people" is Robertson's "the public generally". "Alexander's side" is Robertson's "those of Alexander". Sozomen says "some" and "others". Better to cite the held witness directly: "Sozomen gives three views. Arius's friends blamed magic. Others saw God's judgment, and some blamed a sudden illness of the heart." The contested_claim on the death should match.
- **N2 (Arius, card `dates`).** "Taught at Alexandria from about 318" has no witness. 318 or 319 is Robertson's earliest date for the quarrel (npnf204 l.1674), not the start of Arius's teaching. Write "In dispute with Bishop Alexander from about 318 or 319, by Robertson's dating; died in Constantinople in 336, by the same dating".
- **N3 (Arius, brief, last paragraph).** "Philostorgius praised Arius, but found fault with him too. His history survives only in a hostile summary by Photius ..., who calls him a liar." The last "him" now comes right after a "him" that means Arius, so the listener can hear Photius calling Arius a liar. Photius means Philostorgius. Write "who calls Philostorgius a liar", as the card does.
- **N4 (Pachomius, card uncertain).** The quote "if not verbatim from his pen, are yet authentic enough" stops before Schodde's qualifier: "authentic enough for all practical purposes" (Schodde l.162). Cut there, the line claims more than Schodde does. Quote to the end of his clause.
- **N5 (Hilarion, card uncertain).** "The same edition calls the theory that it was 'a sort of religious romance' without foundation." The edition says the theory "seems destitute of foundation" (npnf206 l.30093). Keep "seems": "says the theory ... seems to have no foundation".
- **N6 (Aetius, brief).** The changes bring in "Sozomen" and "Photius" with no context at first mention. The Arius, Melitius and Hilarion briefs give "Sozomen, the church historian" and "Photius, a patriarch of Constantinople in the 800s". Use the same short context here.
- **N7 (Arius and Frumentius, one name).** The Arius brief and card now say "Theodoret of Cyrus". The Frumentius and Lucifer profiles in this same batch, and the site (`cft-website/index.html`), say "Theodoret of Cyrrhus". npnf203 has each form once. Use one form across the batch. "Cyrrhus" matches the site.
- **N8 (cards, sentence length).** Fourteen new or changed card sentences run past 25 words: Pachomius uncertain (34 and 36), Hilary remembered (33), Frumentius `knownFor`, uncertain and remembered (31, 31, 30), Antony traces (30), Arius remembered and uncertain (27, 27, 27, 26), Aetius remembered and uncertain (26, 27), Hilarion traces (27). The briefs are clean. This is the era 1 batch 2 N8 point again.

## Summary

| Profile | R1 blocking | Resolved | New blocking | New minor | R1 minors partly or not fixed |
|---|---|---|---|---|---|
| Melitius of Lycopolis | 0 | – | 0 | 0 | none (M1 decline holds) |
| Arius | 3 | 3 | 0 | 4 (N1, N2, N3, N7) | none |
| Pachomius | 1 | 1 | 0 | 1 (N4) | none (M4 decline holds) |
| Antony the Great | 1 | 1 | 0 | 0 | none |
| Frumentius | 2 | 2 | 1 (NB1) | 0 | M1 replaced by NB1 |
| Aetius of Antioch | 1 | 1 | 0 | 1 (N6) | none |
| Hilary of Poitiers | 0 | – | 0 | 0 | none |
| Lucifer of Cagliari | 0 | – | 0 | 0 | none |
| Hilarion of Gaza | 1 | 1 | 0 | 1 (N5) | none |
| **Total** | **9** | **9** | **1** | **7 + N8 across cards** | |

All nine R1 blocking findings are resolved. One new blocking finding came in with the changes:
1. NB1 Frumentius: the card and records.json give Blomfield Jackson's own sentence about Theophilus to the Dictionary of Christian Biography he quotes just before it. This error came from R1 M1, which misread the note.

Melitius, Antony, Hilary and Lucifer are clear. Arius, Pachomius, Aetius and Hilarion are clear of blocking faults and have only minors. The fix for NB1 is limited to one card sentence and one records.json witness, so a round 3 can recheck those two lines alone.
