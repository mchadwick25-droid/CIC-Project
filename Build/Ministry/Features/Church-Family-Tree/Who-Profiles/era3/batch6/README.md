# Who profiles: era 3, batch 6

Ten profiles, one id each: `columbanus`, `john-moschus`, `john-of-biclaro`, `babai-the-great`, `isidore-of-seville`, `constantius-of-lyon`, `severinus-of-noricum`, `faustus-of-riez`, `gennadius-of-marseilles`, `ruricius-of-limoges`.

The first five are the last era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 5, in order of death or last attested year as the scan gives it: Columbanus (615), John Moschus (619), John of Biclaro (after 621), Babai the Great (628) and Isidore of Seville (636). Benjamin I of Alexandria, the sixth row, is left to era 4 by the date-of-work rule: the History of the Patriarchs heads his entry 622 to 661, and his patriarchate falls after 622 (the coordinator's call, 2026-11-14). The other five are the first era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` by best held date: Constantius of Lyon, Severinus of Noricum, Faustus of Riez and Gennadius of Marseilles, then Ruricius of Limoges in Benjamin's place. Theopistus is left to the end of the era 3 list, since no held line dates him. None is a live person entry or was written before. Many of the years rest on a Library file header or an editor's note, so the cards give the years the held sources give and say whose they are.

The coordinator confirmed the major marks on 2026-11-14, under Mark's full-auto instruction: Columbanus, Isidore of Seville and Babai the Great are major; the other seven are not. John Moschus, John of Biclaro, Constantius of Lyon and Gennadius of Marseilles are Whos as recorders and stay at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours.

Card traditions are the scan's placings, in the census's names, with one change. The supplement scan places Severinus of Noricum in Early Benedictine / Italian Monasticism and in Gothic, Vandal and Lombard Homoian Christianity. He was Catholic, and the second placing comes only from the Rugians he lived among, so his card reads "Early Benedictine / Italian Monasticism", by the coordinator's call on 2026-11-14. The correction is logged in Open-Gaps.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
