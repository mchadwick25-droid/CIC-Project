# Card check: Cyril of Jerusalem (`cyril-of-jerusalem`)

**Verdict: FIX** (two changes; everything else holds).

## Checks

1. Edits against evidence: every listed edit re-read at its lines (G, SS, TJ, JW, JC, RU, EP, EG, EB). All hold except the two below.
2. Unlisted fields: a field-by-field diff of `Card.existing.json` against the new card shows only the edits `Card_Edits.md` lists. Nothing else moved.
3. `briefReferences`: all twenty name what the brief tells. Entry 7 also names the old garden (outline, "For the card, not the story"), and says so. Holds.
4. Census rules: allowed keys only; no `briefLength`; five `quotationOriginals`, one per quoted span, none extra. Each `printed` and the two Greek `original` entries stand at their lines (validator run on a scratch census with this card and brief in place: no print or original errors; only the pending `secondReading` values and `quote_renderings.json` entries that release sets). Every cited file is in `sources`. No audit named. American spelling.
5. "checked at card": none (all five are six words or more).
6. Not found and clearly wrong: see below.

## FIX

1. `legacy.traces[5]`. The note is at the end of the Procatechesis (G 6190-6196 sit in div `ii.iv`, the Procatechesis; Lecture 1 begins at G 6201). The card's own `briefReferences` says Procatechesis.
   - Old: "A note at the end of the first lecture lets copies be lent"
   - New: "A note at the end of the Procatechesis lets copies be lent"
2. `uncertain[13]`. Rufinus's *sacerdotio ... suscepto* "post Maximum" (RU 28378-28379) is Cyril's taking the see after the bishop Maximus. "Priesthood" here misleads, and sits against `uncertain[0]`, where Jerome has him give up the priesthood to become bishop.
   - Old: "Cyril took up the priesthood after Maximus"
   - New: "Cyril took up the bishop's office after Maximus"

## The two items left in as not found

- `uncertain[1]`, "Sozomen, who says he looked into why Acacius deposed him". Leave it. "And on inquiry I find these to be the facts" (SS 34730) is followed by "It is said that...", hearsay about the next matter. So "these" most naturally points back to the Cyril account just told. That supports the card. The paragraph break in this print is not enough to call it wrong.
- `uncertain[2]`, "Sozomen says he had once followed Macedonius". Leave it. Sozomen's own words, that Cyril "renounced the tenets of the Macedonians which he previously held" (SS 40794-40795), support it in substance, and Zenos's note (SS 15086-15088) reads him the same way. This is found, not unsupported.

## Note (no change required)

`uncertain[8]` says the Munich note "equates" 352 with 360. In Gifford's quotation (G 20590-20604), that sentence sits inside Rupp's quoted words after the note's text, so the equation may be Rupp's rather than the note's. The reading is unclear, not clearly wrong.
