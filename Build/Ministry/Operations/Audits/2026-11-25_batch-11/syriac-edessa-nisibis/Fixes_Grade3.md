# Fixes from the third batch grade: Syriac Christianity

Source of the finding: `Grades3/Why_Held.md` section 3 (missing what, weights [2, 2]), under Mark's ruling (Decision-Log, "Batch 11: third grade and the two small fixes"). Only this one fix was asked. The brief, outline and sheet are not edited here.

## Fix 1. Missing what: what the envoy did

**Finding:** "A Roman envoy, a bishop, came to a later Persian king. Through his work, the king ordered the churches his fathers had torn down to be rebuilt." | missing: what | asks: "What did the envoy do?" | bare statement. The second-grade fix named "his work" and left it empty.

### What the source holds

- **The acts of the synod of 410**, `cic/texts/synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` 16227-16231 (re-read at the file): "par la diligence et par les soins de l'apôtre, messager de paix, que Dieu dans ses miséricordes envoya en Orient, le Père sage, le chef honorable, Mar Marouta®), évèque, qui fut le médiateur de la paix et de la concorde entre l'Orient et l'Occident, qui s'applhiqua à consolider les églises du Seigneur Christ". The grant itself (16155-16166) follows "après que la paix et la tranquillité furent rétablies pour les églises du Seigneur" (16155-16156). In plain words: Marutha, a bishop, was the go-between who made peace and concord between East and West.
- **Witness kind:** contemporary (the synod's own acts, Chabot's French of 1902). **Confidence:** Documented, as the synod's account.
- "Roman envoy" still rests on Socrates VII.8, `npnf202_socrates-sozomen-ecclesiastical-histories.xml` 19135-19141 (later, about 30 years; Documented as his account), as `Recheck_Grade2.md` found. The wonders (19151-19191) stay out.
- "East and West" is kept as the acts give it. The acts do not settle whether they mean the two empires or the two churches; the same clause goes on to the Western canons (16231-16234). The brief does not turn it into "the two empires".
- The king's own reason is not held in his own words (sheet line 130). That is the record's limit. The brief does not mention it, and no gap-only clause is added.

### Brief change

| | Exact text | Words |
|---|---|---|
| Old (paragraph 9, first sentence) | A Roman envoy, a bishop, came to a later Persian king. | 11 |
| New | A Roman envoy, a bishop who made peace between East and West, came to a later Persian king. | 18 |

Net +7. One sentence of 18 words; the next sentence ("Through his work, ...", 16 words) is unchanged, and "his work" now points back to the peace just named.

### Cuts (7 words), and where each goes

All are wording only and drop no claim. None touches the heart, the record's force, a Never-cut line (`Outline.md` line 204) or a Part 1 explanation (the Magi's gloss, the refrain's gloss, the bow's gloss and the synod's gloss all stand).

| Paragraph | Old | New | Saves | Goes to |
|---|---|---|---|---|
| 1 | and destroyed the church of the Christians. | and destroyed the Christians' church. | 2 | Leave out (same claim; chronicle 53, "the church of the Christians") |
| 5 | In his hymn for a siege by a Persian army, | In his hymn for a Persian siege, | 3 | Leave out (same claim) |
| 6 | in number, and this angered the Magi | in number, which angered the Magi | 1 | Leave out (the anger stays) |
| 6 | in his own days many declared | in his day many declared | 1 | Leave out (Aphrahat 27988-27991, "in our days", still told) |

**Count:** 654 now; +7 -7 = **654** by `wc -w` on a scratch copy with all five changes applied (at the cap of 654). Each old string occurs once in the live brief.

**Scorer** (`python -m engine.m1.profile_readability <scratch>`):

```
syr.txt: 647 words, grade 7.5 (names out 6.6), reading ease names out 80.0, 18.0 words a sentence, 0.3 joining words per 100, 3% short sentences, longest sentence 38 words - pass (note: grade 7.5 is under 8: the listener read checks it is not flat)
1 brief(s) graded, 0 failing
```

Same profile as the live brief (647, grade 7.5, ease 80.0). The longest sentence (38) is the existing covenant-practices line, unchanged.

### Outline and sheet lines to change

**`Outline.md` line 61** (beat 6):

- Old: `Through the work of a bishop sent as the Roman envoy (the acts,`
- New: `Through the work of a bishop sent as the Roman envoy, told as "a bishop who made peace between East and West" (the acts, 16229-16230, "médiateur de la paix et de la concorde entre l'Orient et l'Occident"; keep "East and West" as the acts give it, never "the two empires"; the acts,`

**`Outline.md`, after line 201** (end of the Cut first list, after item 31). Add:

> 32. Third-grade fix (2026-11-25, Fixes_Grade3), wording only, 7, paying for what the envoy did in beat 6: "the church of the Christians" to "the Christians' church"; "a siege by a Persian army" to "a Persian siege"; "and this angered" to "which angered"; "in his own days" to "in his day". All **Leave out**.

**`Outline.md` line 87** (By role): no change; the envoy stays unnamed.

**`Source_Sheet.md` line 130**, at its end:

- Old: `No held line gives the king's own reason in his own words.`
- New: `No held line gives the king's own reason in his own words. The brief tells the envoy as "a bishop who made peace between East and West" (16229-16230); the acts do not say whether East and West are the empires or the churches (the clause runs on to the Western canons, 16231-16234), so the wording stays theirs.`
