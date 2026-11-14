# Who profiles: era 4, batch 1

Eight profiles, one id each: `bede-of-jarrow`, `boniface-of-mainz`, `aidan-of-lindisfarne`, `hild-of-whitby`, `adomnan-of-iona`, `alcuin-of-york`, `dhuoda`, `nennius`.

These are the first era 4 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`, the first batch under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full. None was written before. Bede is a live census person entry. His id is the census id, and his profile agrees with the live entry except where the held lines differ; those points are logged in Open-Gaps for a census fix, and the census is not changed here. Many of the scan's years rest on a Library file header or an editor's reckoning, so the cards give the years the held sources give and say whose they are.

The coordinator marked all eight major on 2026-11-14, as the scan proposed. Seven run 402 to 405 words, about 2:30; the 2:30 is a cap, not a target. Nennius is a recorder with a thin held life, so he keeps the major mark and runs at standard length, about 2:06, by the rulings for Palladius, John of Ephesus and Gregory of Tours (the coordinator's call, 2026-11-14). Bede is a recorder too, but his held life, his list of works and Cuthbert's letter on his death carry the full length.

Names and ids, the worker's calls:
- **Boniface of Mainz.** The card name carries the place, since popes of the name are in the census, and the id follows it: `boniface-of-mainz`. The Royal Frankish Annals call him archbishop of Mainz.
- **Nennius.** The card name is plain "Nennius". The doubt is over who wrote the Historia Brittonum, not over his name, so the attribution is said in the brief, in the card's What is uncertain and in the work's author line, "Nennius (attributed)".
- **Adomnán of Iona**, as the census and the era 3 Columba card spell it.

Card traditions are the census's names. Three are the worker's calls, logged in Open-Gaps:
- Aidan of Lindisfarne reads "Anglo-Saxon Christianity; Insular / Irish Monastic Christianity". His years, 635 to 651 by Bede's counts, fall in both movements, and both name him. His work was the founding of the Northumbrian see, so Anglo-Saxon Christianity goes first.
- Adomnán of Iona reads "Medieval Irish Christianity; Insular / Irish Monastic Christianity". His years as abbot, 679 to 704, fall in Medieval Irish Christianity, which goes first. The Insular movement is kept second because it names him among its people and covers Iona.
- Boniface of Mainz reads "Anglo-Saxon Christianity". His mission and synods fall before 751, when Carolingian Reform Christianity begins.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
