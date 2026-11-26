# Fixes from the third batch grade: The Roman Church in the Third Century

Source of the finding: `Grades3/Why_Held.md` section 2 (missing what, weights [2, 1], kept at 2 by the merge), under Mark's ruling (Decision-Log, "Batch 11: third grade and the two small fixes"). Only this one fix was asked. The brief, outline and sheet are not edited here.

## Fix 1. Missing what: lost what

**Finding:** "Almost all that is told of its first decades comes from Hippolytus, a writer of that time who withstood two of Rome's bishops and lost." | missing: what | asks: "Lost what?" | bare statement.

### What the source holds

Hippolytus, *Refutation* IX, ANF 5 (MacMahon, 1886), `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (re-read at the file):

- 13627-13640 (Zephyrinus, led by Callistus): "And we, [note] becoming aware of his sentiments, did not give place to him, but reproved and withstood him for the truth's sake. And he hurried headlong into folly, from the fact that all consented to his hypocrisy—we, [note] however, did not do so—and called us worshippers of two gods". ("worshippers of two gods" stays barred; it is not used.)
- 13955-13956: "And some, under the supposition that they will attain prosperity, concur with them."
- 13957-13958: "that most astonishing Callistus established, whose school continues, preserving its customs and tradition".
- 13951-13952: "they, lost to all shame, attempt to call themselves a Catholic Church!"

In plain words: all but Hippolytus's side went with the bishops, and Callistus's following went on, calling itself the church. **Witness kind:** contemporary, an enemy, and the losing side, admitting it against his own interest. **Confidence:** Documented, as Hippolytus says (sheet Z9, C14; `Source_Sheet.md` line 20 already reads "the losing side" from 13957-13958).

"The church" rather than "most of the church": Hippolytus's own "all ... we, however, did not" sets his side against everyone else, and the sentence already names him as the one who withstood them. No reason for the church's choice is added; none is given beyond Hippolytus's sneer at "prosperity", which stays out.

### Brief change

| | Exact text | Words |
|---|---|---|
| Old (paragraph 2, last sentence) | Almost all that is told of its first decades comes from Hippolytus, a writer of that time who withstood two of Rome's bishops and lost. | 25 |
| New | Almost all that is told of its first decades comes from Hippolytus, a writer of that time. He withstood two of Rome's bishops, but the church sided with them. | 29 (17 + 12) |

Net +4. Split into two sentences, since one would run to 29 words. The one-witness sentence (a Never-cut item) still names him once, early, as the witness; the second sentence answers "lost what". "Them" points to the two bishops.

### Cuts (4 words), and where each goes

All are wording only and drop no claim. None touches the heart, the record's force, a Never-cut line (`Outline.md` line 251: Q1 and the clause after it, Callistus's rule and who came to him, the marriage rule with Hippolytus's charge, and the rest) or a Part 1 explanation (C4 and D1 reasons, the confessor, communion and fallen glosses all stand).

| Paragraph | Old | New | Saves | Goes to |
|---|---|---|---|---|
| 3 | In his own words, as his enemy reports them | In his words, as his enemy reports them | 1 | Leave out ("as his enemy reports them" still marks Q1) |
| 4 | and some whom Hippolytus's side had thrown out | and some Hippolytus's side had thrown out | 1 | Leave out (same shape as "people other groups had refused" just before) |
| 5 | He also let a woman of rank | He let a woman of rank | 1 | Leave out (the new paragraph marks a further rule) |
| 5 | and he called the rule | and called the rule | 1 | Leave out |

**Count:** 675 now; +4 -4 = **675** by `wc -w` on a scratch copy with all five changes applied (at the cap of 675). Each old string occurs once in the live brief.

**Scorer** (`python -m engine.m1.profile_readability <scratch>`):

```
rom.txt: 673 words, grade 8.1 (names out 7.1), reading ease names out 76.2, 18.2 words a sentence, 0.6 joining words per 100, 5% short sentences, longest sentence 35 words - pass
1 brief(s) graded, 0 failing
```

Live brief for comparison: 673 words, grade 8.3, ease 75.7, 18.7 words a sentence. The longest sentence (35) is an existing one, unchanged.

### Outline and sheet lines to change

**`Outline.md` line 9** (the essence):

- Old: `a writer of that time who opposed two bishops and lost (main-witness note; Z9, C3-C4).`
- New: `a writer of that time who opposed two bishops, but the church sided with them (main-witness note; Z9, H 13638-13640, "all consented ... we, however, did not"; C14, H 13957-13958; C3-C4).`

**`Outline.md`, after line 249** (end of the Cut first list, after item 33). Add:

> 34. Third-grade fix (2026-11-25, Fixes_Grade3), wording only, 4, paying for "but the church sided with them" in the essence: "In his own words" to "In his words" (beat 2); "some whom" to "some" (beat 3); "He also let" to "He let" and "and he called" to "and called" (beat 4). All **Leave out**.

**`Source_Sheet.md` line 51** (row Z9), in its last cell:

- Old: `"And we, [note] becoming aware of his sentiments, did not give place to him, but reproved and withstood him for the truth's sake."`
- New: `"And we, [note] becoming aware of his sentiments, did not give place to him, but reproved and withstood him for the truth's sake." 13638-13640: "from the fact that all consented to his hypocrisy—we, [note] however, did not do so". The brief tells this as "but the church sided with them".`
