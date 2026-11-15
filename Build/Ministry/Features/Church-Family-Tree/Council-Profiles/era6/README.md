# Council profiles: era 6

Two major councils, written to `../../Council_Profile_Pattern.md`: `council-of-constance-1414`, `council-of-basel-ferrara-florence-1431`.

The councils scan joins Basel, Ferrara and Florence in one row, and this folder follows it with one profile. The council opened at Basel in 1431. Eugenius IV moved it to Ferrara to meet the Greeks, then to Florence and later to Rome. Those who stayed at Basel deposed him and elected Felix V, and they ended at Lausanne in 1449. The entry tells the joins in `issue`, `datesNote` and `outcome`, each with its witness. The Council of Pisa (1409) is told inside the Constance profile, as background to its issue, as the scan rules.

| File | Holds |
|---|---|
| `<id>.brief.txt` | About This Council, the spoken brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.entry.json` | The entry, in the tradition-entry form with `kind` `major-council`. Its fields are listed in the pattern, "The entry". A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `witness_kind`, `formation_confidence`), `contested_claims` (claim, sides, `formation_confidence`) and `absent_details` (detail, note). |
