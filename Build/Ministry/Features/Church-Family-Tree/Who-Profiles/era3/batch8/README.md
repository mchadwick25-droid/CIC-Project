# Who profiles: era 3, batch 8

Eight profiles, one id each: `john-climacus`, `dionysius-exiguus`, `liberatus-of-carthage`, `marius-of-avenches`, `martin-of-braga`, `brendan-of-clonfert`, `barhadbeshabba-arbaya`, `theopistus`.

These are the last era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`. Batch 7 takes the other eight: Avitus of Vienne, Philoxenus of Mabbug, Boethius, Fulgentius of Ruspe, Eugippius, John of Beth Aphthonia, Ciaran of Clonmacnois and Primasius of Hadrumetum. None of the eight here is a live person entry or was written before. Theopistus was left to the end of the era 3 list, since no held line dates him. The scan row says nothing about the man is held. That is wrong: the History of Dioscorus is told in his own voice, and François Nau gives his reasons for thinking it was reworked after 512. So he is written, at the length his one held source carries (the coordinator's call, 2026-11-14). Many of the years rest on a Library file header or an editor's note, so the cards give the years the held sources give and say whose they are.

The coordinator confirmed the major marks on 2026-11-14: John Climacus and Dionysius Exiguus are major; the other six are not. Liberatus of Carthage, Marius of Avenches, Barhadbeshabba and Theopistus are Whos as recorders and stay at standard length or less, by the rulings for Palladius, John of Ephesus and Gregory of Tours.

Two people named Barhadbeshabba are kept apart, as batch 1's Narsai and Barsauma cards keep them. This profile is the bishop of Halwan who signs the synod that J.-B. Chabot dates to 605 and who wrote the Cause of the Foundation of the Schools. Its display name is "Barhadbeshabba 'Arbaia of Halwan", so that it does not collide with batch 1's "Barhadbeshabba 'Arbaia", the writer of the Ecclesiastical History. Nau's view that the two may be one man is given as his (the coordinator's call, 2026-11-14).

Card traditions are the census's names. Four are the worker's calls, logged in Open-Gaps:
- Dionysius Exiguus reads "Early Benedictine / Italian Monasticism". He was a monk at Rome, and Cassiodorus tells of him in one chapter with Eugippius. The scan's other placings are "The Byzantine Imperial Church (Justinianic)", a movement centered on Constantinople, and "Latin canon law", which is not a census tradition.
- Liberatus of Carthage reads "Latin African Christianity under Byzantium", as Victor of Tunnuna's card does in batch 4.
- Martin of Braga reads "Nicene Visigothic Iberia". The census has no Suevic movement.
- Brendan of Clonfert reads "Insular / Irish Monastic Christianity" only. The scan's Welsh placing comes from W. J. Rees's collection, whose own note says the Lives in that part are of Irish saints, and the census's Medieval Welsh Christianity begins in 768.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
