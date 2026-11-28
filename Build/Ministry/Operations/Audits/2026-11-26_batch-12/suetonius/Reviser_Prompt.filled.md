# Batch header

- **Story:** Suetonius (census id `suetonius`). **Kind:** person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/suetonius/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/suetonius/Card.existing.json` (the census `card` field as it stood when this prompt was made; the era 1 card thread may be rewriting it in the census).
- **Job on the slate (Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended". This batch only.):** Two short lines in the lives of the emperors: Claudius expels Jews stirred up by "Chrestus", and Nero punishes the Christians. The story tells how little the lines say, and how later readers used them. Part A. Shape proposed on the slate: Outside witness; the record decides the order.
- **Census home and direct line:** none (an outside witness).
- **Descent or break:** None.
- **Siblings:** `tacitus` (this batch; read its outline first): the fire is told there; Nero's punishment is a clause here.
- **Live beside it:** `pliny-the-younger` (his friend: a link only), `josephus`.
- **Heart and length (Mark, 2026-11-27, "Batch 12: hearts and lengths approved": "approve as recommended". This batch only.):** the heart as `Outline.md` gives it, and the section "Approved heart and length" at its end: Mark, 2026-11-27 ("Batch 12: hearts and lengths approved", "approve as recommended"): the heart above, and **500 words** (the independent count in `Length_Count.md`, rounded up to the next 25, capped at 675). If the outline, less its Cut first list, runs past 500, it is cut back at the outline by its researcher and checked; the heart and the record's force are not cut, and a story that cannot fit without cutting its heart goes back to Mark. Every Cut first item goes to the card or Leave out as it is marked. Ruinart (1689) goes to the card; the story's later readers are the old ones (ruling 3). The heart is revised to match before the outline check.
- **This batch's rulings (Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended". This batch only.):**
  - The live wording is not kept (slate decision 2). Do not open `suetonius.brief.live.txt` in your folder, any other version of the live story, or the census `longDescription` for this entry.
  - Quotes: no reuse in this batch. Every quote in the live stories named under Live beside stays barred, and no quote is shared inside the batch. A researcher who wants a barred quote asks. Barred: every quote in `pliny-the-younger`, and every quote the Tacitus outline uses.
  - No census change. A descent or break named above is told as the old sources give it, crediting each witness.

- **Heart wording (this batch):** a review finding that changes wording the approved essence or heart holds is applied as the review gives it, and goes to Mark as a report with the brief. Fixes the review needed at the outline are already in `Outline.md` (`Fixes_Review.md`, `Recheck_Review.md`, `Recheck_Review_Applied.md` where present): use the outline as it now stands.
- **Length:** the ceiling is 675 words (Mark, 2026-11-27, "Batch 12: lengths measured by the draft"). If the review's fixes take it past the ceiling, say so with the count; do not cut what the review did not name.
- **Length note:** the review-fix recheck asked for two new cuts to reach 500; under the lengths ruling the ceiling is 675, so those cuts were not applied (`Recheck_Review_Applied.md`).

---

# Reviser

You make the one revision of one Church Family Tree story about **Suetonius**, in `Build/Ministry/Operations/Audits/2026-11-26_batch-12/suetonius/`. You did not write or review it. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1, and the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`), then `Outline.md`, `Review.md` and `suetonius.brief.txt`. Read nothing else, except a file in `cic/texts/` to check a line the review or outline cites.

1. Before you change anything, copy the brief to the next free backup, `suetonius.brief.v1.txt` (or `.v2.txt` on a craft pass), which is never edited; every change goes into `suetonius.brief.txt`, the live file.
2. Add each Do not say line that `Review.md` gives to `Outline.md`, word for word.
3. Fix every finding in `Review.md`, BLOCKING and MINOR, using only what the outline holds. Where the review gives exact wording, use it word for word. Keep every sentence the review does not touch, word for word. Make the review's cuts, and add only what a finding requires. Keep to the outline's length; never cut the record's force, a credited disagreement or a plain sense to save time.
4. Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-26_batch-12/suetonius/suetonius.brief.txt`. It must pass. Hear it once as the listener. Re-read your work for the four faults in Part 1 of the kit. American spelling outside quotes.
5. Write `Revision.md`: each finding and what you did; each new sentence that is neither the outline's nor the old brief's wording, with its outline line; the word at which the essence is complete; the word count and minutes.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
