# Card check applied: Pontius the Deacon

All changes are in `pontius-the-deacon.card.json`.

1. timeline "257, the first day at Curubis", third line, `text`: applied. The sentence "The judge's face seems moved, and the young man signals" became "From the judge's calm face, he senses that the request has moved him, and the young man signals". The rest of the line is unchanged.
2. timeline "257 to 258", fifth line (the messenger):
   - `text`: applied, now "A messenger comes to Cyprian from Rome with word about its bishop, whom Pontius calls a most blessed martyr."
   - `reference`: applied, with the Latin file and lines 41141-41142 added after the English lines.
   - `note`: applied, added as a new field after `reference`.
3. timeline "September 258", sixth line (the trial), `text`: applied, now "Brought before the governor and asked his name, Cyprian answers that he is Cyprian, Pontius writes. That was all that was said."
4. timeline period `when` "September 258": applied, now "258, to 14 September". Only the period's own `when` was changed. The `when` of the individual lines is untouched.

Entry fields: the check gives no change to an entry field, so nothing was written to `Card_Edits.md`.

Not applied: none. Every old text was found once, as quoted.

JSON check: `python -m json.tool pontius-the-deacon.card.json` passed.

Readability score: not run. `Card_Edits.md` names the command but not the plain file of running text it was run on.
