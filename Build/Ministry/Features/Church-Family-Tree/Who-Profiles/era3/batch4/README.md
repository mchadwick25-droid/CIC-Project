# Who profiles: era 3, batch 4

Ten profiles, one id each: `victor-of-tunnuna`, `theodosius-i-of-alexandria`, `gildas`, `jacob-baradaeus`, `agathias`, `cassiodorus`, `longinus-bishop-of-the-nobadae`, `radegund`, `john-of-ephesus`, `david-of-wales`.

They are the next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 3, in order of death or last attested year as the scan gives it: Victor of Tunnuna (fl. to 566), Theodosius I of Alexandria (567), Gildas (about 570), Jacob Baradaeus (578), Agathias (about 580), Cassiodorus (about 580), Longinus (fl. to about 585), Radegund (587), John of Ephesus (588) and David of Wales (about 589). None is a live person entry or was written before. Many of the scan's years rest on no held line or only on a Library file header, so the order is the scan's, and the cards give the years the held sources give and say whose they are.

The coordinator confirmed the major marks on 2026-11-14, under Mark's full-auto instruction: Theodosius I of Alexandria, Jacob Baradaeus, Cassiodorus and Gildas are major; the other six are not. John of Ephesus is a Who as a recorder at standard length, to match the Palladius ruling, with his work as bishop and missionary in the brief. Victor of Tunnuna is a Who as a recorder. Agathias carries the Outside witness label, and his card's Tradition line reads "Outside the church". Radegund, a queen who became a nun, is judged by what is held in her own words: her letter to the bishops in Gregory of Tours's History is given as hers; the three poems in her voice are Fortunatus's by every held edition, and the brief and card say so. David of Wales is a Who on his following and his Lives, which the brief marks as written centuries after him.

Two names follow the held sources. Longinus has no place in the held sources that identifies him, so his card name gives his role and the people John of Ephesus names, as Julian's did in batch 2. Jacob Baradaeus keeps the census name; John of Ephesus calls him James, and the brief says so.

Card traditions are the scan's placings, in the census's names.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `label` (outside witness only), `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
