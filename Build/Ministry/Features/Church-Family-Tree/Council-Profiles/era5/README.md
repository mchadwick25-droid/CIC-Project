# Council profiles: era 5

Three major councils, written to `Archive/Superseded-Method/Church-Family-Tree-Patterns-2026-11-17/Council_Profile_Pattern.md` (since archived; the kit is `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/`): `council-of-clermont-1095`, `fourth-lateran-council-1215`, `second-council-of-lyon-1274`.

| File | Holds |
|---|---|
| `<id>.brief.txt` | About This Council, the spoken brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.entry.json` | The entry, in the tradition-entry form with `kind` `major-council`. Its fields are listed in the pattern, "The entry". A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `witness_kind`, `formation_confidence`), `contested_claims` (claim, sides, `formation_confidence`) and `absent_details` (detail, note). |
