# Who profiles: era 2, batch 4

Nine profiles, one id each: `rufinus-of-aquileia`, `pelagius`, `paulinus-of-milan`, `sulpicius-severus`, `honoratus-of-arles`, `palladius-of-helenopolis`, `john-cassian`, `possidius-of-calama`, `philostorgius`.

These are the next nine era 2 WHO rows of the era 2 Who scan, as cleaned by the 2026-11-12 duplicate clean-up, after era 2 batch 3, ordered by death or last attested year as the scan gives it: Rufinus (411), Pelagius (about 420), Paulinus of Milan (flourished 422), Sulpicius Severus (about 425), Honoratus (429), Palladius (about 431), John Cassian (about 435), Possidius (about 437) and Philostorgius (about 439). These are the scan's years. The cards give the years the held sources give, which differ for some (Rufinus died in 410 by the notes to Fremantle's edition of Jerome and by Richardson's note; Sulpicius about 420 by Roberts or about 410 by Richardson; no held source gives Pelagius's death). The order does not change. Augustine of Hippo falls in the same years and is skipped as a live person entry. The coordinator confirmed the major marks on 2026-11-13, under Mark's full-auto instruction: Pelagius, Rufinus of Aquileia and John Cassian are major; Paulinus of Milan, Sulpicius Severus, Honoratus of Arles, Palladius of Helenopolis, Possidius of Calama and Philostorgius are not. Palladius, Sulpicius, Possidius, Paulinus and Philostorgius are Whos as recorders, the form Auxentius of Durostorum followed in era 2 batch 2.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `label` (outside witness only), `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
