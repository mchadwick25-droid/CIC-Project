# Card check: Columba

**Verdict: FIX** (two references).

Base: the census card for `columba`. Diffed field by field: only `briefReferences` and `quotationOriginals` differ, as `Card_Edits.md` lists.

## 1. Edits justified

Every listed edit checks against its evidence. Re-read: AD 2224-2225, 7610-7613, 10622-10627, 10785-10789, 10801-10803, 10866-10877, 7894-7897; BEDE 5745-5752, 5862, 5866-5869, 5884-5885, 8122-8123, 8227-8233, 14983-14989; BEDL 18879, 18882-18885.

## 2. Nothing else moved

Confirmed. Every other field is word for word.

## 3. References

Rule applied: remove what the brief does not tell, but keep a date that grounds one of the brief's "about" dates.

FIX 1. `briefReferences[1]`. The brief does not give his forty-second year or the battle.
- Old: `Adomnán, second preface: born of noble parentage; the voyage in his forty-second year, two years after the battle, \"to make a pilgrimage for Christ\".`
- New: `Adomnán, second preface: born of noble parentage; the voyage \"to make a pilgrimage for Christ\".`

FIX 2. `briefReferences[5]`. The brief gives "an older Irish table of dates" and not the moons.
- Old: `Bede III.3: Aidan, a monk of Iona, sent to Oswald in 635, at the king's request for a bishop; his see on Lindisfarne; the English taught the monks' rule by Irish monks; Aidan's Easter by the custom of his country, from the fourteenth to the twentieth moon.`
- New: `Bede III.3: Aidan, a monk of Iona, sent to Oswald in 635, at the king's request for a bishop; his see on Lindisfarne; the English taught the monks' rule by Irish monks; Aidan's Easter by the custom of his country.`

These stay as they are:
- [0] the last day.
- [2] the twelve disciples.
- [3] Brude, the interpreter and the household.
- [4] Bede III.4.
- [6] Whitby.
- [7] "715 or 716" grounds "about 716".
- [8] "562" grounds "about 563".
- [9] the census.

## 4. Census rules

Pass.
- Only allowed keys, and no `briefLength`.
- There are seven quoted spans in the brief and seven entries, with none left over.
- Each `printed` and `original` stands at its lines, and every cited file is in `sources`.
- The quotation marks in the references are verbatim in the brief.
- No audit, review or ruling is named.
- The spelling is American.

Four entries have no `secondReading` yet. That is expected: second readings come at step 7.

## 5. Not found, and left in

The edit list has no "not found" claims. Nothing clearly wrong was left in.

Note, not a fix: the reference to the Annals of Ulster has no `sources` entry, although `annals-of-ulster_annala-uladh-v1-431-1056-gle-lat-eng_hennessy1887.txt` is held. The reference came from the starting card unchanged.
