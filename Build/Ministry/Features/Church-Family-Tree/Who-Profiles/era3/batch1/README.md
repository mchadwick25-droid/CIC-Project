# Who profiles: era 3, batch 1

Ten profiles, one id each: `vardan-mamikonian`, `dioscorus-of-alexandria`, `euthymius-the-great`, `timothy-aelurus`, `elishe`, `victor-of-vita`, `moses-of-khoren`, `barsauma-of-nisibis`, `narsai`, `lazar-parpetsi`.

They are the first ten era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, in order of death or last attested year as the scan gives it: Vardan Mamikonian (451), Dioscorus of Alexandria (deposed 451), Euthymius the Great (473), Timothy Aelurus (477), Elishe (about 480), Victor of Vita (about 484), Moses of Khoren (by the traditional date, about 490), Barsauma of Nisibis (after 491) and Narsai (about 503), then Lazar Parpetsi, whose row gives no year ("late 5th-early 6th c."). Patrick and Peter the Iberian fall in the same years and are skipped as live person entries. The scan's ninth row, Vakhtang I Gorgasali (499), was rescored STORY by the coordinator on 2026-11-14 under Mark's era 3 ruling "Story unless own voice", since no words of his own are held; Lazar Parpetsi took his place. Several of the scan's years rest on no held line, so the order is the scan's, and the cards give the years the held sources give and say whose they are.

The coordinator confirmed the major marks on 2026-11-13, under Mark's full-auto instruction: Dioscorus of Alexandria, Timothy Aelurus, Barsauma of Nisibis, Narsai and Vardan Mamikonian are major; the other five are not. Elishe, Victor of Vita, Moses of Khoren and Lazar Parpetsi are Whos as recorders. Euthymius the Great is known through Cyril of Scythopolis's Life, which the brief marks as hagiography. Moses of Khoren's date stays Contested.

Narsai and Lazar Parpetsi keep their census names and ids, `narsai` and `lazar-parpetsi`, since an existing id is never renamed. Lazar's brief and card add "also called Lazar of Pharp", the form the earlier batches use. Narsai's and Barsauma's briefs give "Narsai of Nisibis" at first mention because the held files name other men called Narsai.

One card tradition is the scan's and names a record the person appears in, not a church he belonged to: Victor of Vita "Gothic, Vandal & Lombard Homoian Christianity", the church that persecuted his own. It is to be settled with the placing.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `label` (outside witness only), `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
