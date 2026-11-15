# Council profiles: era 7, batches 1 and 2

Three major councils, written to `../../Council_Profile_Pattern.md`: `diet-of-worms-1521`, `diet-of-augsburg-1530`, `synod-of-chanforan-1532`. Era 7's twelve major councils go in three batches of four, in date order. The fourth council of batch 1, the Marburg Colloquy (1529), is held back. No held text tells the debate in the room or prints the signed articles, so its profile waits for the colloquy's record, now on the wanted list (`../../../Source-Library/CFT-Wants.md`, "Era 7").

## Why each runs the length it does

The ceiling is 2 minutes 30 seconds, about 400 words, and it is never a target. Each of these three met it because its held sources carry more than the ceiling holds, and each was cut back to fit.

- **Diet of Worms (about 2:30).** Part of the Edict is held in its German text, Luther's speech in Foxe's English with his own later words, and the emperor and the papal envoy through Pallavicino, a Jesuit writing from the envoy's letters. Each side told from its own witnesses, with the dispute over whether the Diet consented to the Edict, takes the full length.
- **Diet of Augsburg (about 2:30).** It ran from June to November: the reading of the confession, the Catholic reply, the failed talks, the refused Apology and the final decree. The confessions of Zwingli and the four cities, and the Catholic reply, known through its opponent and Catholic historians, each need a sentence.
- **Synod of Chanforan (about 2:30).** The record is indirect: a manuscript quoted by two historians and printings by later writers who disagree on the year. The witness for the meeting's name and for Farel's presence must be placed, and the dissenting barbes' side told from the Bohemian Brethren's chronicle. That takes the full length.

## Batch 2

Four more, in date order: `colloquy-of-regensburg-1541`, `council-of-trent`, `diet-of-augsburg-1555`, `colloquy-of-poissy-1561`. `diet-of-augsburg-1555` is the Diet that made the Religious Peace. It is a different gathering from batch 1's `diet-of-augsburg-1530`, which heard the Augsburg Confession, and its brief says so.

### Why each runs the length it does

None was written to the ceiling. Each first draft ran long and was cut back to what the held sources carry and the reader needs.

- **Colloquy of Regensburg (about 2:30).** None of the colloquy's own papers is held, so its story rests on Calvin's dated letters from the city, with Faber's from the Catholic side, set against two rival histories. Each stage (the six named, the book, agreement on justification, the break on the Supper, the recess) needs its own witness, and Rome's doubt on the agreed words needs a sentence.
- **Council of Trent (about 2:30).** Eighteen years and three periods, with the acts held in full. The brief keeps only the closing scene, the calling, the Protestant refusal in its own voices, four decrees, the two disputes the historians fight over, and the reach of the close. Much that is held is left to the entry.
- **Diet of Augsburg 1555 (about 2:30).** The recess's own articles are held, and each of its main clauses (both religions protected, all others shut out, the bishops' reservation, the right to leave) needs a sentence. The room comes only from the Catholic side and Sarpi, and the pope's refusal and the excluded parties need telling through events.
- **Colloquy of Poissy (about 2:30).** The main source names no author and tells the Reformed side, so its standing and the Catholic witnesses must be placed. The scene, Beza's sentence and the uproar, the Catholic replies in their own words, and the prelates' refusal each need a sentence, and so does what came of it, in the crown's, the Catholic historian's and the edict's own words.

| File | Holds |
|---|---|
| `<id>.brief.txt` | About This Council, the spoken brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.entry.json` | The entry, in the tradition-entry form with `kind` `major-council`. Its fields are listed in the pattern, "The entry". A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing paragraph. |
| `records.json` | For each id, `claims` (claim, witness, `witness_kind`, `formation_confidence`), `contested_claims` (claim, sides, `formation_confidence`) and `absent_details` (detail, note). |
