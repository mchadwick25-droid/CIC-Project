# Change order: gold set, calibration half, world-core and story items (2026-10-31)

Coordination-level, AI-reviewed (not Mark's). Mark's pacing ruling applies (one reader per review, a second read only where the first disagrees with the existing label; Decision-Log 41).

## Why

The gold labels for items bound to a world-core or story record were made with the old judge evidence pack, which left out fields the voice is shown (a world-core record's horizon, thinness, cautions and living traditions; a story's tellings and absent_detail). The fix is PR #1383. A 30-item spot sample found the fixed-pack judges disagreeing with 6 of 13 gold-unsupported labels (the sample was 30 items, not the 34 here) on these types (Early_Pass_Report.md; OG-126).

## Scope

- Calibration half only. The held-out half, its seals (`canon/gold_set/seals.yaml`) and its labels are untouched. No held-out number is quoted for world-core or story types until that half is relabelled the same way.
- 34 calibration items bind a world-core or story record and carry a supported or unsupported label. 4 of them are constructed items whose label comes from the construction and are not relabelled. 30 natural items were relabelled by a reader.

## Method

The specialist labeller prompt (`goldset/labeller.py`), unchanged, with the fixed evidence pack (`goldset/evidence.py`), through the in-plan route (`goldset/inplan.py`): no metered call. One reader per item. One reply needed a retry because its quoted evidence words were not found verbatim in the pack; the retry was accepted by the same check. Where the reader's verdict differed from the existing label, a second read of the same prompt was taken. A label changes only where both reads give the new verdict and the Opus review of this order finds the new label right.

## Result

| Existing label | Outcome | Items |
|---|---|---|
| supported | reader agrees | 17 |
| unsupported | reader agrees | 6 |
| unsupported | both reads say supported, and the Opus review of this order agrees | 4 |
| unsupported | both reads say supported, the Opus review does not agree; label stays | 2 |
| unsupported | first read supported, second read cannot_judge; label stays | 1 |

The 4 changed items, all unsupported to supported (item id, bound record, why the old label was wrong):

- gs-3684b2df4d2e (gallic core): the cautions say the two groups never wrote of each other and one must not be said to have known the other.
- gs-3a2c786bd048 (witt core): living_traditions states both points almost word for word. This label was previously agreed by two labellers; the fixed pack shows the field they did not see.
- gs-ccdd354f9269 (don core): the horizon states "no unbroken line to any church of today is on record at any point."
- gs-d6a54d0d70ef (gallic core and cautions): the record dates the Rule of Benedict nearly a century after the span. The sentence's "So does" refers to something the item does not show; the label's record_concern says so, and `gallic.cautions` is not a record in its own right. The verdict covers the dating only. Borderline, and stated here.

In each case the old label, made without these fields, said the record did not state the sentence. The new label carries the reader's evidence words, copied from the pack.

The 3 items that keep their label:

- gs-f918e15ed5c9 (lpc core): both reads said supported. The Opus review found that the record holds the 258-391 silence as Contested, in three places, because nine Morin sermons are still unread, while the sentence states it flatly. The reader's own reason admits this. A contested point stated as settled is stronger than the record, so the label stays unsupported. The old reason ("the record says nothing about Donatist sources") was also wrong; the reason is not rewritten here.
- gs-3630bab97450 (ijc story): both reads said supported, because the absent_detail says what survives is entirely Ambrose's own account. The Opus review noted that the record's own telling uses "the bishop" for the local bishop of Callinicum, whose account does not survive, so "the bishop" in the sentence has no clear referent without the conversation. The label stays unsupported.
- gs-1d362f894065: the first read says supported, the second says cannot_judge ("two years earlier" depends on a later event the pack does not name). The label stays unsupported. It needs a third read or Mark's call only if the item matters to a score.

## Changed in the repository

`canon/gold_set/calibration.jsonl`: the 4 items above, each with the new `label`, `label_source` set to `relabelled_fixed_pack`, and a `relabel` record (from, to, reads, pack, this change order). The `relabel` record is provenance data on the item, not prose; whether it belongs in a canon file is for the project lead to confirm. Nothing else in the file changes. `goldset/tests`: 37 passed.

## Not done

- The held-out half.
- No judge was re-scored against the new labels. Judge recall and false-alarm numbers on the calibration half change with these labels and have not been recomputed.
- The 4 constructed items.
