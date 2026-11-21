# Card edits: Tacitus

Card writer, batch 6, 2026-11-19, per `Card_Prompt.md` and `Brief-Kit/roles/card.md`. The existing card (`Card.existing.json`, the same as the census `card` object for `tacitus`) is kept word for word; every field it had is unchanged. Result: `tacitus.card.json`.

## New

1. **`quotationOriginals`** (new key; the census card had none). One entry per quoted span in the brief, three in all. Each is new, so none carries a `secondReading`.
   - Q1. Modern, as the brief has it: "Christus, from whom the name came, was put to death in the reign of Tiberius by one of our governors, Pontius Pilatus." Printed: "Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus". Evidence: `cic/texts/tacitus_annals-15-44_church-brodribb1876.txt` line 68 (s7), re-read.
   - Q3. Modern: "that same Cornelius Tacitus, who truly talks more lies than anyone," Printed (the Latin the rendering is made from): "At enim idem Cornelius Tacitus, sane ille mendaciorum loquacissimus", `cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt` lines 17915–17916 (split "Cor- / nelius" at the line end), re-read. English printed beside it: "the said Cornelius Tacitus (the very opposite of tacit in telling lies)", `cic/texts/anf03_tertullian.xml` lines 2583–2584 (the `<i>` tag around "tacit" aside), re-read.
   - Q2. Modern: "So even for criminals who deserved to be punished harshly, as an example to all, a feeling of pity arose. For it seemed they were being destroyed not for the public good, but to feed one man's cruelty." Printed: "Hence, even for criminals who deserved extreme and exemplary punishment, there arose a feeling of compassion; for it was not, as it seemed, for the public good, but to glut one man's cruelty, that they were being destroyed." Evidence: TAC line 68 (s12), re-read.
2. **`briefReferences`** (new key): seven entries, one for each source the brief draws on (Annals 15.44; McGiffert's notes to Eusebius 2.25; Schanz, Duchesne and McGiffert on the verdict; Tertullian, Apology 16; Sulpicius Severus 2.29; the 1876 debate; Yonge's preface for the date). No quotation marks. Evidence: `Source_Sheet.md` M1–M7, I1–I3, D1–D3, S3; the outline's Quotes and beat 7.
3. **`sources.about`**: four entries added after the existing five, for files the brief draws on that the card did not cite:
   - Tertullian, Apology 16 in Latin (Oehler), `cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt`: the original of Q3.
   - Schanz, Hosius and Krüger (1922), `cic/texts/schanz-hosius-krueger_geschichte-der-roemischen-litteratur-teil3-deu_3e-aufl1922.txt`: "Historians a century ago read that to mean the inquiry proved them Christians" (lines 24300–24304).
   - Louis Duchesne (1907), `cic/texts/duchesne_histoire-ancienne-de-leglise-tome1-fra_3e-ed1907.txt`: the same reading (lines 2385–2386).
   - Bradlaugh and Roberts debate (1876), `cic/texts/roberts-bradlaugh_is-the-bible-divine-six-nights-discussion_1876.txt`: "In an 1876 debate, a speaker arguing that the Bible was not divine said the passage was open to challenge" (lines 3162–3164).

## Clearly wrong

None. Re-read against the held sources: Sulpicius "born in Aquitania about 363" (`npnf211_…xml` 349–351); Rolfe's "no follower until Ammianus Marcellinus" (`suetonius_…rolfe1914.txt` 375–376); Yonge's "where Tacitus and Suetonius end" (`ammianus-marcellinus_…yonge1862.txt` 758–759); "most loquacious in falsehood" (`anf03_tertullian.xml` 10094); McGiffert on Gibbon, Schiller and Josephus (`npnf201_…xml` 13849–13857). None contradicts the brief.

## Not found

None.

## Not added

- `briefLength`: the census card allows no such key (`tools/validate-census.mjs`, `CARD_KEYS`). The brief is 526 words, about 3 minutes 30 (`Revision.md`).

## Awaiting second reading

All three spans are new; `secondReading` is left out of each:
- "Christus, from whom the name came, was put to death in the reign of Tiberius by one of our governors, Pontius Pilatus."
- "that same Cornelius Tacitus, who truly talks more lies than anyone,"
- "So even for criminals who deserved to be punished harshly, as an example to all, a feeling of pity arose. For it seemed they were being destroyed not for the public good, but to feed one man's cruelty."
