# Second Readings (references, REF-01 to REF-02)

## Method

For each id I set our wording (`Second_Reading_Key.md`, as it stands in the brief) beside the blind rendering (`Second_Readings_Blind_A.md`). I first confirmed that each key wording stands word for word in `john-chrysostom/john-chrysostom.brief.txt` and equals its card entry's `modern` in `john-chrysostom/john-chrysostom.card.json`: both do. The one change in `john-chrysostom/Card_Check.md` touches only Q1's `uncertain` and no rendering. Where the readings differed, I opened the cited lines in `cic/texts/` and read the card's `quotationOriginals` entry (`printed`, `uncertain`). Where the card's English is made from a Greek the Library holds, I read that Greek.

- **SAME**: same meaning.
- **MINOR**: a small difference a listener would not take differently.
- **MEANING**: a listener would understand something different.

## Verdicts

| id | piece | verdict | reason |
|---|---|---|---|
| REF-01 | john-chrysostom | SAME | The blind reader follows Stephens's English; ours follows the Greek (PG52 822-827), as the card's `uncertain` records: *παριδόντων* "ignored", *ὑπὸ τὰ παραπετάσματα* "behind her curtains", *βασιλικὴν ὀργὴν* "the emperor's anger", *μῖσος ἀφόρητον* "unbearable hatred". |
| REF-02 | john-chrysostom | SAME | Ours keeps Prevost's order; the blind reader moves the "do not" onto the pairing. Both forbid honoring him here in silk while neglecting him outside. |

Counts: SAME 2, MINOR 0, MEANING 0.

## Card changes needed

`john-chrysostom.card.json`:

- `quotationOriginals[0].secondReading`: "same"
- `quotationOriginals[1].secondReading`: "same"

No `original` to correct. Neither entry carries an `original`: Q1 prints English alone because the Greek scan is damaged, and Q2's Greek is not held.
