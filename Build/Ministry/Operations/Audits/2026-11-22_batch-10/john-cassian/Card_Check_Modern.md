# John Cassian: card check, the modern pass (2026-11-23)

Checked `john-cassian.card.json` against `Card.pass3.json`, the section **Fourth pass: no modern opinion (2026-11-23)** of `Card_Edits.md`, and `john-cassian.brief.txt` as it now stands (compared with `john-cassian.brief.v4.txt`). Role: `Brief-Kit/roles/card.md`, check pass. Every cited line opened.

**Verdict: FIX** (seven changes).

## What holds

- **Nothing else moved.** A JSON diff with `Card.pass3.json` shows only the five new `uncertain` entries and `briefReferences[0]`, `[1]`, `[7]`, `[8]`, `[9]`, `[10]`, `[12]`, each listed in the edit list.
- **The five new `uncertain` entries.** Each is credited by name and marked as modern.
  - Hunter Blair: RB 132-150 ("from the solitude of Monte Cassino,*" ... "* About 535 a. d."); RB 6839 ("legat unus Collationes").
  - Gibson on the Conferences: N211 15544-15569 ("completed shortly after the death of Castor in 426"; "Honoratus died in January, 429"; "between the years 426 and 428").
  - Gibson on the letter: N211 15724-15726 (Hilary "had just succeeded Honoratus"; "fixes the date of the correspondence as 429").
  - Gibson on Nestorius and On the Incarnation: N211 48516-48517 ("consecrated Bishop of Constantinople in a.d. 428"); 15599-15603.
  - Gibson on Prosper's book: N211 15905-15907 (not earlier than 432; Celestine died in April); 15780-15781 ("never once names him directly"); MOM 42762-42764 ("contra Cassiani 'presbyteri libruni qui titulo de protectione dei praenotatur").
- **`briefReferences` edits.**
  - `[0]`: N211 36737-36745 names the Institutes for Castor and the ten Conferences.
  - `[8]`: N211 48475-48487 holds the near-silence and Leo.
  - `[9]`: N202 20520-20556 holds "Nestorius was brought from Antioch" and "Being ordained".
  - `[10]`: MOM 42762-42764 and N211 37475-37479 ("On the Protection of God.").
  - `[1]`, `[7]` and `[12]` are trims: the brief no longer gives 426-428, 429 or 535.
- **Quotations.** The brief still quotes four spans and the card has four `quotationOriginals`, unchanged. Each `printed` is verbatim: N211 38028-38030, 15774-15775 ("Contra Collatorem"), 25949-25952; N203 43669-43671. "The Conferencer", marked "checked at card", is a fair English for "Contra Collatorem", and its note explains it.
- **Other rules.** No audit is named, spelling is American, and the keys are allowed. Nothing in the edit list is not found.

## FIX

### Modern views not credited, or not marked as modern

1. **`datesNote`.** Gibson's dates are credited to him but not marked as modern.
   - Old: `Born about 360 and in Egypt between about 380 and 400, both by Edgar Gibson's reckoning; died at Marseilles in the reign of Theodosius and Valentinian, by Gennadius of Marseilles, which Gibson places not long after 432`
   - New: `Born about 360 and in Egypt between about 380 and 400, both by the modern reckoning of Edgar Gibson, his translator; died at Marseilles in the reign of Theodosius and Valentinian, by Gennadius of Marseilles, which Gibson's modern reckoning places not long after 432`
2. **`uncertain[3]`.** Bright is named but not marked as modern. N211 15637-15638 gives "with an Introduction by William Bright, D.D. (Oxford), 1889".
   - Old: `Gibson, and William Bright whom he quotes, call this teaching Semi-Pelagian.`
   - New: `Gibson, and William Bright, a modern scholar whom he quotes, call this teaching Semi-Pelagian.`
3. **`uncertain[5]`.** The year 450 comes from the translator's endnote (N203 43243, "Johannes Cassianus died 450."), and the entry does not mark it as modern.
   - Old: `Ernest Cushing Richardson's note gives 450.`
   - New: `Ernest Cushing Richardson, the modern translator of Gennadius, gives 450 in a note.`
4. **`uncertain[7]`.** The eighth-century authorship is Warren's own judgment (BANG 1581, "The author of the statement is an eighth century continental Scotic monk"), and the entry does not mark it as modern.
   - Old: `A tract on the Irish cursus, which Frederick Warren says was written by`
   - New: `A tract on the Irish cursus, which Frederick Warren, a modern editor, says was written by`

### `briefReferences` naming what the brief does not tell

5. **`briefReferences[1]`.** The brief gives no birth year and no years for Egypt; its early life comes "from his own books". Gibson's reckonings stay in `datesNote`.
   - Old: `Gibson, Prolegomena: born about 360; Bethlehem with Germanus; the two visits to Egypt placed between 380 and 400; ordained deacon at Constantinople by John Chrysostom.`
   - New: `Gibson, Prolegomena: Bethlehem with Germanus; ordained deacon at Constantinople by John Chrysostom.`
6. **`briefReferences[3]`.** The brief says only "a later priest of Marseilles". "About fifty years" is an uncredited modern reckoning, resting on the editor's "Died 496." (N203 43968). Gennadius's own text gives "later" (he reports the death, N203 43268-43272) and "a presbyter of Marseilles" (N203 43968-43969).
   - Old: ` Gennadius is later by about fifty years and lived at Marseilles.`
   - New: ` Gennadius is later and lived at Marseilles.`

### Rule 4: cited files missing from `sources`

7. **`sources.about`.** Three held files cited in `briefReferences` (Palladius in `[4]`, Goldbacher in `[7]`, Cassiodorus in `[13]`) are not in `sources`. The gap carries over from earlier passes. Add at the end:
   - Old: (none)
   - New:
     - `{"title": "Dialogue on the Life of Chrysostom", "author": "Palladius", "date": null, "language": "English translation", "file": "cic/texts/palladius_dialogue-life-of-chrysostom_moore1921.txt"}`
     - `{"title": "Letter to Augustine, Epistle 225 among Augustine's letters, edited by Alois Goldbacher", "author": "Prosper of Aquitaine", "date": null, "language": "Latin", "file": "cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt"}`
     - `{"title": "Institutions, book I, chapter 29, in Migne, Patrologia Latina 70", "author": "Cassiodorus", "date": null, "language": "Latin", "file": "cic/texts/cassiodorus_opera-institutiones-pl70-lat_migne1847.txt"}`

No other change. After the fix, run `node tools/validate-census.mjs --skip-quotes` on a scratch census again.
