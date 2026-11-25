## Batch header

- **Story:** Basil of Caesarea (`basil-of-caesarea`), kind: person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`).
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/`. **Card:** the `card` field of the entry `basil-of-caesarea` in `cic-website/data/world-census.json`.
- **Batch:** a fix to live texts, run as a batch of its own (Kit, Part 3): the three person reference stories brought to the kit of 2026-11-24 (Open-Gaps 406). Job: the person reference for `kinds/person.md`, read by every later person writer for voice. Siblings: as the outline's Sibling field gives them (`gregory-of-nazianzus`, `gregory-of-nyssa`, `macrina-the-younger`).
- **Heart:** The approved heart is the one in `Outline.md` (The heart), essence first: he gave up teaching rhetoric for a life of prayer and shared work; wrote the rules that taught monks to live together and serve one another; built a great lodging for the poor and the sick outside Caesarea; and as its bishop defended the Holy Spirit's place beside the Father and the Son. Shape: Founder or leader, as the outline names it.
- **Length:** The approved length is the outline's: about 4:30 at most (about 675 words by the scorer), aiming at 4:00.
- **Ruling for this batch (Mark, quoted):** "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks." Keep approved wording wherever it passes the kit; change only what fails it.
- **Your step: the one revision.** The writer's starting copy is `basil-of-caesarea.brief.v0.txt`; your backup is `basil-of-caesarea.brief.v1.txt`. Also add to `Changes.md` a section "## The one revision": each changed sentence, before and after, with its outline line and the finding it answers.

## Role prompt (`Brief-Kit/roles/reviser.md`, filled)

# Reviser

You make the one revision of one Church Family Tree story about **Basil of Caesarea**, in `Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/`. You did not write or review it. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1, and the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`), then `Outline.md`, `Review.md` and `basil-of-caesarea.brief.txt`. Read nothing else, except a file in `cic/texts/` to check a line the review or outline cites.

1. Before you change anything, copy the brief to the next free backup, `basil-of-caesarea.brief.v1.txt` (or `.v2.txt` on a craft pass), which is never edited; every change goes into `basil-of-caesarea.brief.txt`, the live file.
2. Add each Do not say line that `Review.md` gives to `Outline.md`, word for word.
3. Fix every finding in `Review.md`, BLOCKING and MINOR, using only what the outline holds. Where the review gives exact wording, use it word for word. Keep every sentence the review does not touch, word for word. Make the review's cuts, and add only what a finding requires. Keep to the outline's length; never cut the record's force, a credited disagreement or a plain sense to save time.
4. Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/basil-of-caesarea.brief.txt`. It must pass. Hear it once as the listener. Re-read your work for the four faults in Part 1 of the kit. American spelling outside quotes.
5. Write `Revision.md`: each finding and what you did; each new sentence that is neither the outline's nor the old brief's wording, with its outline line; the word at which the essence is complete; the word count and minutes.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
