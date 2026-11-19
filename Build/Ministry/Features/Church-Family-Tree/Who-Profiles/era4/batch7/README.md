# Who profiles: era 4, batch 7

Seven profiles, one id each: `symeon-the-new-theologian`, `niketas-stethatos`, `cedd-and-chad`, `elipandus-of-toledo-and-felix-of-urgell`, `paul-the-deacon`, `paulus-emeritanus`, `pisentius-of-coptos-and-john-the-elder`.

These are seven WHO rows of the era 4 table in `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`, built under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full. None is a live census person entry, and none was written before.

The coordinator called Symeon the New Theologian major (2026-11-14), as the scan proposes: the hesychasts of the Philokalia read him. His brief runs 404 words, about 2:30. The other six are not major. Niketas Stethatos, Paul the Deacon and Paulus Emeritanus run 348 to 365 words, about 2:09 to 2:15. Paul the Deacon and Paulus Emeritanus are recorders and stay at standard length, as Palladius, John of Ephesus and Gregory of Tours did. Paulus Emeritanus is a recorder with a thin own life: he never names himself in his book, and everything held of his life is in its first chapter and its close. The three paired profiles run 392 to 400 words, about 2:25 to 2:28, since each tells two lives. That pairs may run to the 2:30 cap, which stays a cap and not a target, was the coordinator's call (2026-11-14). Mark then saw what a 2:00 version of each of the six briefs would drop, and kept the lengths as they are: "keep", and "Pairs up to 2:30 (Recommended)" (2026-11-14). The Decision-Log entry for this batch has his words.

## The pairs

Each pair follows Mark's pairing rule of 2026-11-11: "if two people are tied together in their sources with similar identity its ok to make that a single who".
- **Cedd and Chad.** Brothers, and both bishops. Bede tells their lives together, through Lastingham, the monastery Cedd founded and Chad ruled after him, and he names the monks of Lastingham as his source for both.
- **Elipandus of Toledo and Felix of Urgell.** Two bishops condemned together. The council of Frankfurt in 794 names the heresy as both men's, and the sources tell them together. Their teaching is told from Elipandus's own letters and Felix's confession, and their opponents' reading of it is given as their opponents'.
- **Pisentius of Coptos and John the Elder.** A bishop and the disciple who wrote his Life. John is both the author and a witness inside it. The Life is the one source for John; for Pisentius it is the main one, beside letters to and from a bishop of his name among the Epiphanius papers, the synaxaries and Abu Salih.

## Sources found in drafting

- **Niketas's Life of Symeon** is not held as a text, as the scan says. A long summary of it, with Greek extracts, is held: François Combefis's preface to Manuel Calecas, in Patrologia Graeca 152 (`calecas_opera-omnia-pg152-grc-lat_migne1866.txt`, l.19524-21260). Symeon's life is told from it, with the Philokalia's notice and his own chapters, and with Combefis's own judgments kept apart from the Life's. The coordinator agreed to this use (2026-11-14).
- **Niketas Stethatos** has a held voice outside the Philokalia: his book against the Latins, in Latin, and the envoys' record of his recantation in 1054, both in Cornelius Will's Acta et scripta of 1861.
- **Stephen's Life of Wilfrid**, in Raine's York volume, tells Chad's consecration differently from Bede, and the Cedd and Chad profile gives both.
- **Paulus Emeritanus**: no line of his gives a year. The dates on his card are his editor's reasoning and the Bollandists', and are said to be so.
- **Pisentius**: no held source gives his year of death. The "c. 632" of the Library's file header and of the scan rests on no held line.

## Names and ids, the worker's calls

- **Symeon the New Theologian**, the scan and census form.
- **Niketas Stethatos**, the scan form. The Latin sources call him Nicetas Pectoratus.
- **Cedd and Chad**. Bede's Latin spells Chad Ceadda, and later writers use Cedda for either brother, which the card notes.
- **Elipandus of Toledo and Felix of Urgell**, with the Latin forms on the card.
- **Paul the Deacon**, the census form.
- **Paulus Emeritanus**, the scan form, with "Paul, deacon of Mérida" under other names. Bishop Paul of Mérida, the Greek physician in the same book, is another man.
- **Pisentius of Coptos and John the Elder**. The Life's title calls John the Presbyter; "John the Elder" is Budge's running head and the scan's form.

## Card traditions

The census's names. Four differ from the scan's placing, the worker's calls, to be logged in Open-Gaps:
- **Symeon** and **Niketas** read "The Byzantine Imperial Church (Macedonian Era); Athonite & Comnenian Byzantine Monasticism". The scan's "Byzantine monastic and hesychast tradition" is not a census name. The Macedonian entry, 843 to 1054, covers their years. The Athonite entry names Symeon as a voice and tells Niketas in its story, and its status note places Symeon's corpus in its Constantinople half, as batch 5 placed Athanasios the Athonite.
- **Elipandus and Felix** read "Mozarabic Christianity; Carolingian Reform Christianity". The scan's "Nicene Visigothic Iberia" ends in 711, before their years. Elipandus held Toledo in the Mozarabic entry's years, and Felix was condemned by Frankish councils and kept at Lyon.
- **Paul the Deacon** reads "Carolingian Reform Christianity". The scan's two entries, Early Benedictine Italian Monasticism (to 604) and the Gothic, Vandal and Lombard Homoian entry (to 680), end before he was born. He served at Charlemagne's court, and no era 4 entry covers Italy or Monte Cassino.
- **Pisentius and John** read "The Church of Alexandria and Miaphysite Egypt", the census name for the scan's `cyrilline-miaphysite-egyptian-christianity`. Its window, 328 to 642, covers his consecration, which Budge puts between 570 and 603, and the Persian years of the Life.

Cedd and Chad read "Anglo-Saxon Christianity", and Paulus Emeritanus "Nicene Visigothic Iberia", as the scan places them.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a date, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` at the start of the last paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
