# Story header

- **Story:** Josephus. **Slug:** `josephus`. **Kind:** person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`), era 1. **Folder:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/Card.existing.json` (the census `card` of `josephus` as it stands; identical to the census today).
- **Job on the slate (Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended"):** A Jewish priest and commander who went over to Rome and wrote his people's history. The story tells his lines on John the Baptist, James and Jesus, and how Christian writers kept them and argued over the passage on Jesus. Shape: Outside witness.
- **Census home:** none (an outside witness; `toldWithin` null). **Siblings:** none. Links: `eusebius-of-caesarea` quoted him; `origen` said he did not believe in Jesus as the Christ; `jerome` gave the passage in Latin.
- **Approved heart:** as `Outline.md`, "The heart", states it (Mark, 2026-11-27, "Batch 12: hearts and lengths approved": "approve as recommended").
- **Approved length:** 778 words, as the brief stands, with its heart timing (Mark, 2026-11-28, "Batch 12: three hearts, the era's heart timing and five lengths": "follow recommendations on all"; item 5, "Five lengths accepted as they stand: Josephus 778 (and its heart timing)").
- **Rulings for this story (batch 12 only):**
  - "Batch 12: the full cards for its twenty people" (Mark, 2026-11-27: "a"): "Batch 12 writes the full new card for each of its twenty people at its card step ..., after each new brief: every section of the card the kit approves, Timeline included, under `roles/card.md`." The card sections and the timeline are in `Build/Ministry/Features/Church-Family-Tree/Stage-Two-Kit/Kit.md`, sections 1 to 3.
  - "Batch 12: the slate approved", decision 3: no census change; decision 6: no quote reuse.

---

# Final checker

You are review 3 of 3, the last, for the story about **Josephus**, in `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/`. You have not seen its drafts or its earlier reviews: do not open `Outline_Check.md`, `Review.md`, any `*.v1.txt` or other backup, or the census `longDescription`. Read `CLAUDE.md` ("Trust and source fidelity"), Part 1 and the bar in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, the kind kit the story header names, and the card role, `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md`. Open a file in `cic/texts/` only at a line range, never whole. Work in this order.

## 1. The blind renderings

Before you read the brief or the card, read `Second_Reading_Requests.md`. For each id, open the named file at the lines given and render the passage into plain modern English, from the original language where the request names one. Render every clause; add nothing. Where the scan is damaged, say what you read and what is unclear. Write these renderings into `Final_Check.md` under **Blind renderings** before you go on.

## 2. The quotes

Now read `Second_Reading_Key.md`, `josephus.brief.txt` and `josephus.card.json`. For each id, confirm our wording stands word for word in the brief and equals its card entry's `modern`. Set it beside your rendering. Where they differ, open the cited lines and the card's `quotationOriginals` entry. Give each id SAME (same meaning), MINOR (a difference a listener would not take differently) or MEANING (a listener would understand something different, with the corrected rendering), and a one-line reason. Each quotation marked "checked at card" is checked against its original and print. Every quote's `printed` wording is checked verbatim at its file and lines.

## 3. What changed

Read `Revision.md`. Read every sentence the revision added or changed, and every sentence of the thread's own wording it lists, against the sources, the way the brief reviewer's trust read does (`roles/reviewer.md`): the same marks, the same BLOCKING faults, each with its exact change. Read the sentences on either side of each one. Then hear the whole final brief once as the standard's listener, and count only what is BLOCKING under the bar.

## 4. The card

Check the card as the card role's check list below gives it, with `Card_Edits.md` and the starting card if there is one.

1. Each edit or field is justified by its evidence, and each item the outline or review sends to the card is on it. No modern opinion, date or identification is stated as content anywhere on the card; a modern work appears only in `modernWorks`, its `note` saying what it covers, never what it argues.
2. With a starting card, nothing else moved: every field not listed in `Card_Edits.md` is word for word.
3. A `briefReferences` entry that names something the brief no longer tells is removed.
4. The census rules in the card role: allowed keys, one `quotationOriginals` entry per quoted span and none for a dropped one, each cited file in `sources`, no audit named, American spelling. Where the outline renders from a held original, the card carries it.
5. Each claim listed as not found, and anything clearly wrong left in.
6. A census entry: each field against its source, no `atlasId` already in use.
7. Timeline lines and headlines, where the card has them, each against its source.

## The verdict

`Final_Check.md` holds the blind renderings, the quote table with its counts and each card change it needs (each `secondReading` as "same", "minor" or "changes meaning", and any `original` to correct), the marks for each changed sentence, and the card findings. Give PASS, or FIX with each change exact (the file, the old text, the new text). A finding is BLOCKING only under the bar; a MINOR one is given as an exact change or noted, never a reason for another round. If a BLOCKING fault cannot be settled by an exact change, say so plainly: the story then goes to Mark. "Could be stronger" is not a finding.

Edit nothing else and do not commit. Reply in under 150 words.
