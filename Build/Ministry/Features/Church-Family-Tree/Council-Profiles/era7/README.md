# Council profiles: era 7, batch 1

Three major councils, written to `../../Council_Profile_Pattern.md`: `diet-of-worms-1521`, `diet-of-augsburg-1530`, `synod-of-chanforan-1532`. Era 7's twelve major councils go in three batches of four, in date order. The fourth council of batch 1, the Marburg Colloquy (1529), is held back. No held text tells the debate in the room or prints the signed articles, so its profile waits for the colloquy's record, now on the wanted list (`../../../Source-Library/CFT-Wants.md`, "Era 7").

## Why each runs the length it does

The ceiling is 2 minutes 30 seconds, about 400 words, and it is never a target. Each of these three met it because its held sources carry more than the ceiling holds, and each was cut back to fit.

- **Diet of Worms (about 2:30).** Both sides are held in their own voices: the Edict in German, Luther's speech in Foxe's English and his own later account, and the emperor and the papal envoy through Pallavicino. Telling each side from its own witnesses, with the contested Edict date, takes the full length.
- **Diet of Augsburg (about 2:30).** It ran from June to November: the reading of the confession, the Catholic reply, the failed talks, the refused Apology and the final decree. The confessions of Zwingli and the four cities, and the Catholic reply known only through its opponent, each need a sentence.
- **Synod of Chanforan (about 2:30).** The record is indirect: a manuscript quoted by two historians and printings by later writers who disagree on the year. The witness for the meeting's name and for Farel's presence must be placed, and the dissenting barbes' side told from the Bohemian Brethren's chronicle. That takes the full length.

| File | Holds |
|---|---|
| `<id>.brief.txt` | About This Council, the spoken brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.entry.json` | The entry, in the tradition-entry form with `kind` `major-council`. Its fields are listed in the pattern, "The entry". A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `witness_kind`, `formation_confidence`), `contested_claims` (claim, sides, `formation_confidence`) and `absent_details` (detail, note). |
