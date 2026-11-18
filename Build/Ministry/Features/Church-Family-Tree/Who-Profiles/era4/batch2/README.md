# Who profiles: era 4, batch 2

Eight profiles, one id each: `maximus-the-confessor`, `martin-i-of-rome`, `benjamin-i-of-alexandria`, `jacob-of-edessa`, `timothy-i-of-baghdad`, `dionysius-of-tel-mahre`, `photius-of-constantinople`, `gregory-of-narek`.

These are the eastern majors of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`, the second batch under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full. Benjamin I of Alexandria comes from the era 3 scan and was moved to era 4 by the date of his work (Decision-Log, era 3 batch 6). His brother Mennas is a separate STORY row and has no profile here. None of the eight is a census person entry or was written before. Many of the scan's years rest on a Library file header or an editor's reckoning, so the cards give the years the held sources give and say whose they are.

The coordinator marked all eight major on 2026-11-14. Each brief runs 404 or 405 words, about 2:30; the 2:30 is a cap, not a target. Dionysius of Tel Mahre is a recorder, but his held life carries the full length, as Bede's did in batch 1. Bar Hebraeus gives his election in his own words, his two journeys to Egypt, his hearing before al-Ma'mun and his death, and Michael the Syrian keeps his own preface.

Much of what these men wrote or said is held only in Latin, French or Italian. The briefs tell those lines in modern words, with the source named, and keep quotation marks for held English.

Names and ids, the worker's calls, accepted by the coordinator:
- **Martin I of Rome**, `martin-i-of-rome`, in the form of the era 3 bishops of Rome (`vigilius-of-rome`). The ordinal keeps him apart from Martin of Tours and Martin of Braga.
- **Timothy I of Baghdad**, `timothy-i-of-baghdad`. "Timothy I" alone would collide with Timothy I of Alexandria, Timothy II of the Church of the East and Timothy Aelurus. Assemani has the patriarchs' seat at Baghdad, and Mari and Amr bury Timothy at Kelilisho in Baghdad. He was enthroned at Seleucia, and the card says so.
- **Photius of Constantinople**, `photius-of-constantinople`. Census texts already call him so, and the census and the Library also hold other men named Photius.

Card traditions are the census's names. Three are the worker's calls, accepted by the coordinator:
- Maximus the Confessor reads "The Byzantine Imperial Church (Heraclian & Iconoclast Eras); Latin African Christianity under Byzantium". His trials, sentence and death fall in the first, which names him as a voice. The second lists him among its people, and his dispute with Pyrrhus was held in Africa.
- Martin I of Rome reads "The Byzantine Imperial Church (Heraclian & Iconoclast Eras)". The scan places him in "Heraclian; Roman", but no era 4 census movement is Roman. The Heraclian entry names him as a voice, and his synod, trial and exile fall in its years.
- Benjamin I of Alexandria reads "Coptic Christianity under Early Islam; The Church of Alexandria and Miaphysite Egypt". His return under 'Amr and most of his patriarchate fall after 642. His election and flight fall in the older movement, whose voice line also names him.

The others: Timothy I in "The Church of the East on the Silk Road" (the Abbasid movement begins about 845, after his death); Photius in "The Byzantine Imperial Church (Macedonian Era)"; Jacob of Edessa and Dionysius of Tel Mahre in "Syriac Orthodox Christianity under Islam"; Gregory of Narek in "Bagratid Armenian Christianity".

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
