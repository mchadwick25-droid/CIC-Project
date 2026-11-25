# Batch header

- **Story:** Marcionism (census name: Marcion / Marcionism) (census id `marcion-marcionism`). **Kind:** tradition (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/tradition.md`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/Card.existing.json` (the census entry's card fields; a tradition has no `card` field).
- **Job on the slate (Mark, 2026-11-25, "Batch 11: the slate approved": "Approve as recommended". This batch only.):** The church Marcion founded, after he left Rome: its congregations, its one Gospel and ten letters, its own martyrs and teachers, and the centuries it lasted. Marcion's own life is the live person story. Half B.
- **Census home and direct line:** Its own entry. No direct line: argued against by the Syriac, Bardaisanite, Tertullian, Greek Apologist and House Church entries.
- **Descent or break:** None.
- **Siblings in the batch:** Latin Apologists (Tertullian's five books: read its outline first). Syriac (Ephrem). Greek Apologists (Justin).
- **Live beside it:** marcion-of-pontus is told within this entry and carries the founding: the gift returned, the two Gods, the Scripture. Split (ruling): this story opens after the break with Rome and tells the community through what the old sources hold of it, such as Marcionite martyrs in Eusebius, Apelles and the later teachers, and the villages a later bishop reports. The founding comes in only as a short essence. Also beside it: tertullian-s-voice, polycarp-of-smyrna, irenaeus-of-lyon, justin-martyr.
- **Heart and length:** approved (Mark, 2026-11-25, "Batch 11: hearts and lengths approved": "Approve as recommended"): the heart as `Outline.md` holds it under "The heart", and **495 words**, as its "Approved heart and length" section records. Every Cut first item goes to the card or Leave out as it is marked. Also kept by that ruling: Theodoret's Marcionite villages. **Length now governs as ruled:** Mark, 2026-11-25 ("Batch 11: lengths, up to 4:30 and cut at the outline", "a"): up to 675 words, and no longer than the heart needs; the approved figure above stands unless a draft runs past 675, when the outline goes back to its researcher. The heart as `Outline.md` now holds it governs, with any wording the outline check corrected.
- **This batch's rulings (Mark, 2026-11-25, "Batch 11: the slate approved": "Approve as recommended". This batch only.):** Quotes: no reuse is planned for this batch. Every quote in the live stories named under Live beside stays barred; a quote another story on the tree uses may be used only where the slate lists it, and the slate lists none. Inside the batch, no quote is shared. A researcher who wants a barred quote asks. Barred: Justin's "There is a certain Marcion, from Pontus…", Tertullian's "Separating the law from the gospel…", Polycarp's "firstborn of Satan", Tertullian's "By what right, Marcion, do you cut my timber?", and every other quote in the stories beside it.

---

# Reviewer

Three fresh hands review each piece about **Marcionism**, in `Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/`. Each works without the others' reads and without earlier drafts or reviews (files marked `.v1`, `.v2`, and so on). Each reads Part 1 and the bar in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` and the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`), and judges against them, not against any earlier brief. The verdict rests on the faults they count, never on an overall impression.

## The trust read

A reader who knows the period, with the sources open. Read `marcion-marcionism.brief.txt`, then go through it sentence by sentence. For each sentence that states a fact, a summary, a paraphrase or a judgment, find the line in `cic/texts/` it rests on. `Outline.md` and `Source_Sheet.md` point the way, but the check is against the source itself. Quote that line briefly, with its file, and mark the sentence:
- **HELD:** the source says it.
- **SUMMARY HOLDS:** a fair compression, with its meaning and force intact.
- **SOFTENED OR CHANGED:** quote both.
- **ASSUMPTION ADDED:** a motive, cause, reason, connection or date the source does not give.
- **MODERN ONLY:** rests only on a modern editor or historian, or breaks Part 1's date rule. A claim about what came of the subject that rests on a reliable later witness who shows it is HELD, with that witness's line.
- **NOT FOUND:** say what you searched.

A quote is often our modern rendering of an old text: where it is rendered from the original language, check it against the original, not an English translation.

Then judge whether the heart is the right heart for its subject, from what the sources show, and whether it is told by the end of the first minute (about 150 words, 130 for a council).

Each SOFTENED, ASSUMPTION ADDED, MODERN ONLY or NOT FOUND sentence is BLOCKING, with its exact change: told as the source gives it, or cut. So is a missing or late heart. A sentence the outline does not hold is cut, never written into the outline to match the story. Write `Trust.md`: a count for each mark, then each non-HELD sentence with its evidence.

**The second trust read.** A second reader who knows the period, who has not seen `Trust.md`, checks the same way every sentence the writer added or changed: in a new brief every sentence, and in a fix the sentences that differ from the approved text. Write `Trust_Second.md`. A finding either read makes is BLOCKING until it is fixed or a third reader, who has seen neither, shows from the source that it holds.

## The listener reads

Two listeners who see no source, outline or other read: a first-time visitor, with no church background and English as a second language, and an AI skeptic, who knows the habits of machine writing and distrusts it. Each hears `marcion-marcionism.brief.txt` once and counts, quoting each instance:
1. The lines of the kind kit's test, and each one they cannot fill.
2. The opening: after its first three sentences, what is missing of who, where, when and why there.
3. Each sentence that fails on one hearing, quoted with the meaning lost. A sentence that is merely long or formal, but understood, does not count.
4. Each bare statement (Part 1, Explain it).
5. Each citation read aloud that Part 1 does not call for.
6. Each tell Part 1 names. The AI skeptic also gives each line that sounds machine-made, and why.
7. Each unexplained word, each run of short one-act sentences, and anything that talks down.
8. Whether the opening pulls them in, the sentence where attention first drifts, and whether they would listen to the end.

Then run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/marcion-marcionism.brief.txt` and `python tools/check_brief_craft.py Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/marcion-marcionism.brief.txt`, and judge each line the second lists by Part 1.

Each unfilled test line, bare statement or tell is BLOCKING, and so is an opening that leaves the listener lost about who or where. A failing sentence is MINOR, and BLOCKING only where it loses the thread of the story. A citation read aloud is MINOR: give the sentence in the narrator's voice. Where attention drifts, say why, for the reviser. Write `Listen_FirstTime.md` or `Listen_Skeptic.md`.

## The verdict

`Review.md` gathers the three reads: the counts; PASS when nothing is BLOCKING, otherwise REVISE; and each finding with its exact change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. There are no scores.

## The fresh read

After the one revision, a new trust reader and a new first-time listener, who have not seen this story's reads, `Revision.md` or any earlier draft, read the final `marcion-marcionism.brief.txt` in full in the same way, and a second trust read checks every sentence the revision added or changed. They write `Fresh_Read.md`: the counts, PASS or REVISE, and each finding with its exact change. The fresh read blocks only for what the bar blocks. A MINOR finding there is applied word for word or noted, never the start of another round: the aim is reliable, sound work, not perfection. Once per batch, the same hands read the kind's reference stories in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/reference/` in the same way, without opening `Scores.md`, and `Reference_Read.md` sets their counts beside those in `Scores.md`.

Do not edit the story or commit. Each reply is under 150 words.
