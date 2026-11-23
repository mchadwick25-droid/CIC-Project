# Pelagius: craft pass check

Independent check of the craft pass (Decision Log, 2026-11-23, "Batch 10: the fresh read, and the fixes after it", item 1). Compared `pelagius.brief.v2.txt` (before) with `pelagius.brief.txt` (after), by `diff` and by reading each change with its neighbors.

## Verdict: FIX

The paragraph move in fresh-read finding 1 was not made. `Fresh_Read_Applied.md` says the essence paragraph was moved to second place, but in `pelagius.brief.txt` it is still third, after the warning paragraph. The word-level edits of finding 1 were all made. Read in the current order, they break.

## The five points

1. **The two BLOCKING points.**
   - Finding 1 (essence within about 150 words): **not met.** The essence paragraph ends at word 207, about 83 seconds at 150 a minute. With the move made, it ends at word 150, as the fresh read worded it.
   - Finding 2 (Britain by 429): **met.** The sentence is in the brief word for word, after "The sentence held."
2. **Nothing added beyond the fresh read's wording: met.** Every change in the diff is one of the fresh read's exact edits: "a monk named" cut; "Augustine of Hippo"; the reworded warning sentence; "through Augustine and others"; "at Diospolis"; "Then Africa and Rome closed in." and "It did not last." deleted; the Britain sentence inserted. Nothing else changed.
3. **Each change reads correctly on one hearing: not met, because the paragraph was not moved.** In the current order, paragraph 2 is "Writing with a fellow bishop, Augustine even warned Demetrias's mother against the book." Augustine has not been heard before this point. "Even" has nothing to build on, since it was written to follow "answered him book by book". "Augustine of Hippo" then comes one paragraph after the bare "Augustine". The other changes read correctly with their neighbors: "Augustine reports" now opens its paragraph cleanly after the Diospolis paragraph. "On 30 April 418" follows "For a few months, Rome itself took his side" as a plain turn. The Britain sentence sits between "The sentence held." and Cassian, in date order. The move itself tells no event twice. The warning is told only once, as the essence's reach-ahead, and the fresh read already judged the return to "He lived long at Rome" as the kit allows.
4. **The Britain sentence is supported: met.** In `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`, the year "Florentio et Dionysio. a. 429" is at line 54148 and entry 1301 at 54151-54155 reads: "Agricola Pelagianus ... ecclesias Brittaniae dogmatis sui insinuatione corrumpit. sed ... papa Caelestinus Germanum Autisidorensem episcopum vice sua mittit". "A chronicler says", "a Pelagian", "Britain's churches" and "Germanus of Auxerre was sent against it" all hold. This matches Outline.md, What came of them 4.
5. **Length: met.** `python -m engine.m1.profile_readability pelagius.brief.txt`: 674 words, grade 7.4 (names out 5.9), reading ease names out 79.3, longest sentence 28 words, pass. A test copy with the move made scores the same: 674 words, pass.

## The fix

Move the paragraph only, with no change to any word. Current paragraphs 2 and 3 change places:

- **Old order:** (1) "About 413, Pelagius wrote to Demetrias ..." (2) "Writing with a fellow bishop, Augustine even warned Demetrias's mother against the book. ..." (3) "Pelagius, a monk from Britain who taught at Rome, held that ... The teaching that bears his name was ruled out of the church." (4) "He lived long at Rome ..."
- **New order:** (1) "About 413, Pelagius wrote to Demetrias ..." (2) "Pelagius, a monk from Britain who taught at Rome, held that ... The teaching that bears his name was ruled out of the church." (3) "Writing with a fellow bishop, Augustine even warned Demetrias's mother against the book. ..." (4) "He lived long at Rome ..."

After the move, `Fresh_Read_Applied.md`'s line for finding 1 becomes true, and all five points are met.
