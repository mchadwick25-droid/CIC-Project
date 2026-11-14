# Council profiles: era 2

Eight major councils, written to `../../Council_Profile_Pattern.md`: `council-of-arles-314`, `council-of-nicaea-325`, `council-of-sardica-343`, `councils-of-ariminum-and-seleucia-359`, `first-council-of-constantinople-381`, `conference-of-carthage-411`, `council-of-ephesus-431`, `council-of-chalcedon-451`.

| File | Holds |
|---|---|
| `<id>.brief.txt` | About This Council, the spoken brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.entry.json` | The entry, in the tradition-entry form with `kind` `major-council`. Its fields are listed in the pattern, "The entry". A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `witness_kind`, `formation_confidence`), `contested_claims` (claim, sides, `formation_confidence`) and `absent_details` (detail, note). |
