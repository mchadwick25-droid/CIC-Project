## Batch header

- **Story:** John Chrysostom (`john-chrysostom`), kind: person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`).
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/`. **Card:** the `card` field of the entry `john-chrysostom` in `cic-website/data/world-census.json`.
- **Batch:** a fix to live texts, run as a batch of its own (Kit, Part 3): the three person reference stories brought to the kit of 2026-11-24 (Open-Gaps 406). Job: the third person reference for `kinds/person.md` (Mark: "a, three references, use Chrysostom as the third"), read by every later person writer for voice. Siblings: `epiphanius-of-salamis` (in this batch; it tells the Constantinople visit from Epiphanius's side only) and any the researcher finds on the tree, such as `palladius-of-helenopolis`.
- **Heart:** The approved heart is batch 10's, in `Outline.batch10.md` and the census entry's `why`: a preacher at Antioch and then bishop of Constantinople, who spoke plainly about money, cruelty and the poor, rebuked the powerful, was deposed and exiled, and died on the road into a second exile; his body was later brought back to Constantinople and his followers reconciled.
- **Length:** The approved length is batch 10's: about 3 minutes (about 450 words by the scorer). The person kit allows up to about 675 where the sources and content call for it; the researcher sets the length to Part 2's count, and says if it moves.
- **Ruling for this batch (Mark, quoted):** "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks." Keep approved wording wherever it passes the kit; change only what fails it.
- **Your step: the one revision.** The writer's starting copy is `john-chrysostom.brief.v0.txt`; your backup is `john-chrysostom.brief.v1.txt`. Also add to `Changes.md` a section "## The one revision": each changed sentence, before and after, with its outline line and the finding it answers.

## Role prompt (`Brief-Kit/roles/reviser.md`, filled)

# Reviser

You make the one revision of one Church Family Tree story about **John Chrysostom**, in `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/`. You did not write or review it. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1, and the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`), then `Outline.md`, `Review.md` and `john-chrysostom.brief.txt`. Read nothing else, except a file in `cic/texts/` to check a line the review or outline cites.

1. Before you change anything, copy the brief to the next free backup, `john-chrysostom.brief.v1.txt` (or `.v2.txt` on a craft pass), which is never edited; every change goes into `john-chrysostom.brief.txt`, the live file.
2. Add each Do not say line that `Review.md` gives to `Outline.md`, word for word.
3. Fix every finding in `Review.md`, BLOCKING and MINOR, using only what the outline holds. Where the review gives exact wording, use it word for word. Keep every sentence the review does not touch, word for word. Make the review's cuts, and add only what a finding requires. Keep to the outline's length; never cut the record's force, a credited disagreement or a plain sense to save time.
4. Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt`. It must pass. Hear it once as the listener. Re-read your work for the four faults in Part 1 of the kit. American spelling outside quotes.
5. Write `Revision.md`: each finding and what you did; each new sentence that is neither the outline's nor the old brief's wording, with its outline line; the word at which the essence is complete; the word count and minutes.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
