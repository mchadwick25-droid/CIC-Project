# Who profiles: era 3, batch 5

Ten profiles, one id each: `evagrius-scholasticus`, `gregory-of-tours`, `dorotheus-of-gaza`, `columba`, `leander-of-seville`, `venantius-fortunatus`, `reccared`, `henana-of-adiabene`, `augustine-of-canterbury`, `baudonivia`.

They are the next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 4, in order of death or last attested year as the scan gives it: Evagrius Scholasticus (about 594), Gregory of Tours (594), Dorotheus of Gaza (596, by Migne's heading on Andrea Gallandi's notice), Columba (597), Leander of Seville (600), Venantius Fortunatus (about 600), Reccared (601), Henana of Adiabene (about 604), Augustine of Canterbury (604 or 605) and Baudonivia (to about 610). None is a live person entry or was written before. Gregory the Great falls in the same years and is skipped as a live person entry. Many of the scan's years rest on no held line, so the order is the scan's, and the cards give the years the held sources give and say whose they are.

Reccared is a Who on Mark's era 3 ruling for rulers, "Story unless own voice", which names him: his own confession at the Third Council of Toledo is held. The coordinator confirmed the major marks on 2026-11-14, under Mark's full-auto instruction: Columba, Augustine of Canterbury, Leander of Seville and Reccared are major; the other six are not. Gregory of Tours stays at standard length as a recorder, by the coordinator's call on the rulings for Palladius and John of Ephesus. Evagrius Scholasticus, Gregory of Tours and Baudonivia are Whos as recorders. Henana of Adiabene's teaching is known only through his opponents; a pupil's praise of the man survives, and the brief says both.

Card traditions are the scan's placings, in the census's names, with one change. The scan places Evagrius Scholasticus in the Syriac Orthodox church, but he writes for the side that held to Chalcedon, as adviser to Gregory of Antioch; his card reads "The Byzantine Imperial Church (Justinianic)", by the coordinator's call on 2026-11-14. The correction is logged in Open-Gaps.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
