# Batch header

- **Story:** Josephus (census id `josephus`). **Kind:** person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/Card.existing.json` (the census `card` field as it stood when this prompt was made; the era 1 card thread may be rewriting it in the census).
- **Job on the slate (Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended". This batch only.):** A Jewish priest and commander who went over to Rome and wrote his people's history. The story tells his lines on John the Baptist, James and Jesus, and how Christian writers kept them and argued over the passage on Jesus. Part A. Shape proposed on the slate: Outside witness; the record decides the order.
- **Census home and direct line:** none (an outside witness).
- **Descent or break:** None.
- **Siblings:** None in the batch. Links: `eusebius-of-caesarea` quoted him; `origen` said he did not believe in Jesus as the Christ. Each is a clause.
- **Live beside it:** `eusebius-of-caesarea`.
- **Heart and length (Mark, 2026-11-27, "Batch 12: hearts and lengths approved": "approve as recommended". This batch only.):** the heart as `Outline.md` gives it, and the section "Approved heart and length" at its end: Mark, 2026-11-27 ("Batch 12: hearts and lengths approved", "approve as recommended"): the heart above, and **675 words** (the independent count in `Length_Count.md`, rounded up to the next 25, capped at 675). If the outline, less its Cut first list, runs past 675, it is cut back at the outline by its researcher and checked; the heart and the record's force are not cut, and a story that cannot fit without cutting its heart goes back to Mark. Every Cut first item goes to the card or Leave out as it is marked.
- **This batch's rulings (Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended". This batch only.):**
  - The live wording is not kept (slate decision 2). Do not open `josephus.brief.live.txt` in your folder, any other version of the live story, or the census `longDescription` for this entry.
  - Quotes: no reuse in this batch. Every quote in the live stories named under Live beside stays barred, and no quote is shared inside the batch. A researcher who wants a barred quote asks. Barred: every quote in `eusebius-of-caesarea` as it stands live.
  - No census change. A descent or break named above is told as the old sources give it, crediting each witness.



- **Redraft (Mark, 2026-11-27, "Batch 12: lengths measured by the draft": "approve as recommended". This batch only.):** the first draft ran 1,004 words; the outline has since been cut back with that draft in hand (`Fixes_Length.md`, `Recheck_Length.md`) to an expected draft of about 673. Write a fresh draft from the outline as it now stands; do not open the first draft. The ceiling is 675 words: if it still runs past 675 with every Cut first item out, stop and say so.

---

# Writer

You write one Church Family Tree text about **Josephus**, heard aloud (a connection note is read). Read these files and nothing else in the repository:
- `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/Outline.md`
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1 only (the standard)
- the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`)
- the reference stories the kind kit names, each `*.brief.txt` in its folder under `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/reference/`, read once for voice. Do not copy their order, openings, endings or moves.

Write `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/josephus.brief.txt`: plain text, no title, a blank line between paragraphs. Follow the standard and the outline's Do not say list. Use only what the outline holds, and only its quotes, word for word. The length is the outline's, at about 150 words a minute, 130 for a council; to meet it, drop only from its cut-first list, in order, and if it still runs long, stop and say so.

Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/josephus.brief.txt`. It must pass the limits. Run `python tools/check_brief_craft.py Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/josephus.brief.txt` and judge each line it lists by Part 1: fix what breaks a rule, and leave what does not. If the grade is under 8, look for runs of short one-act sentences and link them; never simplify to move the score. Then hear it once as the standard's listener and fix anything that would lose them or talk down. Before you hand on, re-read your own work for the four faults in Part 1 of the kit. Fix what you find, and say in your reply that you checked. Use American spelling outside the outline's quotes.

Do not commit or edit anything else. Reply with the word count, the scorer line, and how you opened and ended.
