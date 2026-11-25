## Batch header

- **Story:** John Chrysostom (`john-chrysostom`), kind: person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`).
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/`. **Card:** the `card` field of the entry `john-chrysostom` in `cic-website/data/world-census.json`.
- **Batch:** a fix to live texts, run as a batch of its own (Kit, Part 3): the three person reference stories brought to the kit of 2026-11-24 (Open-Gaps 406). Job: the third person reference for `kinds/person.md` (Mark: "a, three references, use Chrysostom as the third"), read by every later person writer for voice. Siblings: `epiphanius-of-salamis` (in this batch; it tells the Constantinople visit from Epiphanius's side only) and any the researcher finds on the tree, such as `palladius-of-helenopolis`.
- **Heart:** The approved heart is batch 10's, in `Outline.batch10.md` and the census entry's `why`: a preacher at Antioch and then bishop of Constantinople, who spoke plainly about money, cruelty and the poor, rebuked the powerful, was deposed and exiled, and died on the road into a second exile; his body was later brought back to Constantinople and his followers reconciled.
- **Length:** Batch 10 approved about 450 words. The outline check found the beats need more; the outline now sets about 650 words (4:20), provisional, for Mark's ruling, with a floor of about 580 on its Cut first list. Write to the outline's length.
- **Ruling for this batch (Mark, quoted):** "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks." Keep approved wording wherever it passes the kit; change only what fails it.
- **Your step: revise a live brief.** This is a fix to a live text. Before you change anything, copy `john-chrysostom.brief.txt` to `john-chrysostom.brief.v0.txt`, which is never edited. Read the brief as one more file. Keep its wording wherever a sentence passes Part 1, the kind kit and the outline, its Do not say list included; rewrite only the sentences that fail them, from the outline, and add what the outline's beats carry that the brief lacks. Also write `Changes.md`: each changed, cut or added sentence, before and after, with the outline line it stands on, and one line on what rule the old sentence broke or what beat the new one carries.

## Role prompt (`Brief-Kit/roles/writer.md`, filled)

# Writer

You write one Church Family Tree text about **John Chrysostom**, heard aloud (a connection note is read). Read these files and nothing else in the repository:
- `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Outline.md`
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1 only (the standard)
- the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`)
- the reference stories the kind kit names, each `*.brief.txt` in its folder under `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/reference/`, read once for voice. Do not copy their order, openings, endings or moves.

Write `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt`: plain text, no title, a blank line between paragraphs. Follow the standard and the outline's Do not say list. Use only what the outline holds, and only its quotes, word for word. The length is the outline's, at about 150 words a minute, 130 for a council; to meet it, drop only from its cut-first list, in order, and if it still runs long, stop and say so.

Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt`. It must pass the limits. Run `python tools/check_brief_craft.py Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt` and judge each line it lists by Part 1: fix what breaks a rule, and leave what does not. If the grade is under 8, look for runs of short one-act sentences and link them; never simplify to move the score. Then hear it once as the standard's listener and fix anything that would lose them or talk down. Before you hand on, re-read your own work for the four faults in Part 1 of the kit. Fix what you find, and say in your reply that you checked. Use American spelling outside the outline's quotes.

Do not commit or edit anything else. Reply with the word count, the scorer line, and how you opened and ended.
