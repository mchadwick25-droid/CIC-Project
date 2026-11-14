# Who profiles: era 4, batch 3

Eight profiles, one id each: `theodore-of-tarsus`, `willibrord`, `leoba`, `muirchu`, `tirechan`, `cogitosus`, `wilfrid-of-york`, `cuthbert-of-lindisfarne`.

These are eight Insular WHO rows. Six come from `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: Theodore of Tarsus, Willibrord, Leoba, Muirchu maccu Machtheni, Tirechan and Cogitosus. Two come from `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`: Wilfrid of York and Cuthbert of Lindisfarne. They are built under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full. None is a live census person entry, and none was written before.

None is marked major. The coordinator ruled on 2026-11-14 that Anglo-Saxon Christianity already has its four majors in Bede, Boniface, Aidan and Hild, and Insular Irish has Adomnán. All eight run 337 to 344 words, about 2:05. Tirechan, Cogitosus and Muirchu are recorders and stay at standard length, as Palladius, John of Ephesus and Gregory of Tours did. Leoba's held record is one letter of hers and three letters to her. Her brief runs to what those and Edward Kylie's introduction carry, and says which part is Kylie's.

Names and ids, the worker's calls:
- **Theodore of Tarsus.** The census has many Theodores, so the card name carries the place Bede gives, and the id follows it.
- **Wilfrid of York.** Bede and Stephen make him bishop of York, and the supplement scan names him so. "Wilfrid of Ripon" is kept under other names. The id keeps him apart from Wilfrid II of York, Hild's pupil, who is named only in the records.
- **Cuthbert of Lindisfarne**, as the supplement scan names him. Cuthbert, Bede's pupil, who wrote the letter on Bede's death, is a different man and is named only in the records.
- **Muirchu maccu Machtheni**, the form Newport White gives from the note at the end of the first book. The id is `muirchu`.
- **Leoba**, the census spelling. Kylie and the Roman Breviary spell her Lioba, which the card keeps under other names.
- **Willibrord**, **Tirechan** and **Cogitosus** stand without a place; no other person of those names is in the census or the held sources used.

Card traditions are the census's names. Four are the worker's calls, to be logged in Open-Gaps:
- Muirchu and Tirechan read "Medieval Irish Christianity". Every held dating of their work falls after 664, where that movement begins: White's 664 to about 670 and Stokes's 683 for Tirechan, and the 690s for Muirchu.
- Cogitosus reads "Medieval Irish Christianity; Insular / Irish Monastic Christianity". His date is disputed. Basnage thought him much later than Brigid, White's reading puts him before about 700, and Stokes gives 800 to 835, so Medieval Irish goes first. The Insular movement is kept second because Migne prints him under 591 and the era 3 Brigid card sits there.
- Cuthbert of Lindisfarne reads "Anglo-Saxon Christianity" only. He was trained at Melrose under men of the Irish mission. Most of his held life falls after 664, and the Insular movement does not name him.
- Leoba and Willibrord read "Anglo-Saxon Christianity". The census names Leoba among that movement's people and voices, and Willibrord in its long description. Leoba's last years may fall after 751, when Carolingian Reform Christianity begins, but no held line gives her death.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
