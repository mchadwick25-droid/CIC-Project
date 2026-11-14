# Who profiles: era 4, batch 4

Eight profiles, one id each: `humbert-of-silva-candida`, `hincmar-of-reims`, `prudentius-of-troyes`, `jonas-of-bobbio`, `braulio-of-zaragoza`, `ildefonsus-of-toledo`, `julian-of-toledo`, `beuno`.

These are eight Latin West WHO rows, the fourth batch under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full. Seven come from `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`. Julian of Toledo comes from `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`. None of the eight is a census person entry or was written before. Braulio, Ildefonsus and Jonas were carried from era 3 to era 4 by the date of their work.

The coordinator marked Humbert of Silva Candida major, as the Roman face of the 1054 break. He first marked the other seven not major. When drafting found Hincmar's church-law writings held, against the scan, the coordinator marked Hincmar major too, a coordinator call Mark may overrule. Humbert's and Hincmar's briefs run about 400 words, about 2:30; the 2:30 is a cap, not a target. The other six run about 330 to 340 words, about 2 minutes. Prudentius of Troyes is a recorder and stays at standard length, under the Palladius, John of Ephesus and Gregory of Tours rulings. Jonas of Bobbio is a recorder with a thin own life, and his card says so. Beuno's record is late, and his brief says so early, under the later-retelling rule.

The held witnesses go well past those the scans list:
- **Humbert.** Cornelius Will's Acta et scripta of 1861 holds the envoys' account, the sentence, the Dialogue and the reply to Nicetas. It also holds the edict of Michael Keroularios's synod, which gives the Greek side, and Keroularios's letters to Peter of Antioch. The scan names only Mirbt.
- **Hincmar.** Beyond the annals, Mansi 15 holds his chapters for his priests, his letters and the date of his ordination. Mansi 16 holds the council of Douzy, the bishops' letter to Pope Hadrian II, his own letter to Hadrian and the writings of both Hincmars. Mansi 17 holds his nephew's own complaint to Pope John VIII, and Mommsen's MGH volume gives his death year. Krusch's MGH volume holds his Life of Remigius. The scan says his canon-law and theological work is not held.
- **Prudentius.** Patrologia Latina 115 holds his own works, among them his treatise against John Scotus Eriugena, with Nicolás Antonio's notice. The scan has only the annals and Hincmar's notice.
- **Jonas.** The Acta Sanctorum for March, volume 3, gives his birth at Susa. His preface to the Life of Columbanus is held in Latin, in Barralis's book of 1613. His Life of John of Réomé, with its opening on his journey of 659, is held in Krusch's MGH volume.
- **Julian.** Toledo XV's answer to the points Pope Benedict had raised, with a section under Julian's name, is held in the Collectio canonum Ecclesiae Hispanae. Felix's notice of his death is held in Patrologia Latina 96.

Many lines of these men are held only in Latin. The briefs tell those lines in modern words, with the source named, and keep quotation marks for held English (Munro's Jonas, Brehaut's Braulio, Rees's Beuno).

Names and ids, the worker's calls:
- **Humbert of Silva Candida**, as the census names him; the census's "Cardinal" is kept among the other names.
- **Braulio of Zaragoza**, as the census spells it; "Braulio of Saragossa", the Library's form, is an other name.
- **Beuno**, as the scan heads him; Rees's English spells "Beino", and the Latin Life of Winefred "Beunonus".

Card traditions are the census's names. Three are the worker's calls:
- Humbert reads "The Latin Papal Church (Gregorian Reform to Innocent III); The Byzantine Imperial Church (Macedonian Era)". Both name him as a voice. The Latin Papal entry begins in 1049 and covers 1054 and 1059, and it is his own church. The Macedonian entry covers the city and the year of the break.
- Beuno reads "British and Welsh Christianity". The scan places him in Medieval Welsh Christianity, but that movement begins in 768. The note in Rees puts his life in the sixth and seventh centuries, with Clynog Fawr founded in 616, which falls in British and Welsh Christianity (451 to 768).
- Jonas of Bobbio reads "Insular / Irish Monastic Christianity". The scan also names Merovingian Gaul, but the census's Merovingian Gallic Christianity ends in 620, before his work of about 640. The Insular movement runs to 664 and covers the Columban houses he wrote of.

The others: Hincmar and Prudentius in "Carolingian Reform Christianity"; Braulio, Ildefonsus and Julian in "Nicene Visigothic Iberia".

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
