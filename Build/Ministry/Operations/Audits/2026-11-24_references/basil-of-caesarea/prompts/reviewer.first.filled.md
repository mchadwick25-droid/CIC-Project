## Batch header

- **Story:** Basil of Caesarea (`basil-of-caesarea`), kind: person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`).
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/`. **Card:** the `card` field of the entry `basil-of-caesarea` in `cic-website/data/world-census.json`.
- **Batch:** a fix to live texts, run as a batch of its own (Kit, Part 3): the three person reference stories brought to the kit of 2026-11-24 (Open-Gaps 406). Job: the person reference for `kinds/person.md`, read by every later person writer for voice. Siblings: as the outline's Sibling field gives them (`gregory-of-nazianzus`, `gregory-of-nyssa`, `macrina-the-younger`).
- **Heart:** The approved heart is the one in `Outline.md` (The heart), essence first: he gave up teaching rhetoric for a life of prayer and shared work; wrote the rules that taught monks to live together and serve one another; built a great lodging for the poor and the sick outside Caesarea; and as its bishop defended the Holy Spirit's place beside the Father and the Son. Shape: Founder or leader, as the outline names it.
- **Length:** The approved length is the outline's: about 4:30 at most (about 675 words by the scorer), aiming at 4:00.
- **Ruling for this batch (Mark, quoted):** "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks." Keep approved wording wherever it passes the kit; change only what fails it.
- **Your step: the first-time visitor's listener read** (the role's second section): no church background, English as a second language. Read only `basil-of-caesarea.brief.txt`, Part 1 and the bar of the kit, and the kind kit; open no source, outline, earlier draft (`.v0` and the like) or other read. Write `Listen_FirstTime.md`.

## Role prompt (`Brief-Kit/roles/reviewer.md`, filled)

# Reviewer

Three fresh hands review each piece about **Basil of Caesarea**, in `Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/`. Each works without the others' reads and without earlier drafts or reviews (files marked `.v1`, `.v2`, and so on). Each reads Part 1 and the bar in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` and the kind kit the batch header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`), and judges against them, not against any earlier brief. The verdict rests on the faults they count, never on an overall impression.

## The trust read

A reader who knows the period, with the sources open. Read `basil-of-caesarea.brief.txt`, then go through it sentence by sentence. For each sentence that states a fact, a summary, a paraphrase or a judgment, find the line in `cic/texts/` it rests on. `Outline.md` and `Source_Sheet.md` point the way, but the check is against the source itself. Quote that line briefly, with its file, and mark the sentence:
- **HELD:** the source says it.
- **SUMMARY HOLDS:** a fair compression, with its meaning and force intact.
- **SOFTENED OR CHANGED:** quote both.
- **ASSUMPTION ADDED:** a motive, cause, reason, connection or date the source does not give.
- **MODERN ONLY:** rests only on a modern editor or historian, or breaks Part 1's date rule.
- **NOT FOUND:** say what you searched.

A quote is often our modern rendering of an old text, so compare its meaning with the original passage.

Then judge whether the heart is the right heart for its subject, from what the sources show, and whether it is told by the end of the first minute (about 150 words, 130 for a council).

Each SOFTENED, ASSUMPTION ADDED, MODERN ONLY or NOT FOUND sentence is BLOCKING, with its exact change: told as the source gives it, or cut. So is a missing or late heart. A sentence the outline does not hold is cut, never written into the outline to match the story. Write `Trust.md`: a count for each mark, then each non-HELD sentence with its evidence.

## The listener reads

Two listeners who see no source, outline or other read: a first-time visitor, with no church background and English as a second language, and an AI skeptic, who knows the habits of machine writing and distrusts it. Each hears `basil-of-caesarea.brief.txt` once and counts, quoting each instance:
1. The lines of the kind kit's test, and each one they cannot fill.
2. The opening: after its first three sentences, what is missing of who, where, when and why there.
3. Each sentence that fails on one hearing, quoted with the meaning lost. A sentence that is merely long or formal, but understood, does not count.
4. Each bare statement (Part 1, Explain it).
5. Each citation read aloud that Part 1 does not call for.
6. Each tell Part 1 names. The AI skeptic also gives each line that sounds machine-made, and why.
7. Each unexplained word, each run of short one-act sentences, and anything that talks down.
8. Whether the opening pulls them in, the sentence where attention first drifts, and whether they would listen to the end.

Then run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/basil-of-caesarea.brief.txt` and `python tools/check_brief_craft.py Build/Ministry/Operations/Audits/2026-11-24_references/basil-of-caesarea/basil-of-caesarea.brief.txt`, and judge each line the second lists by Part 1.

Each unfilled test line, bare statement or tell is BLOCKING, and so is an opening that leaves the listener lost about who or where. A failing sentence is MINOR, and BLOCKING only where it loses the thread of the story. A citation read aloud is MINOR: give the sentence in the narrator's voice. Where attention drifts, say why, for the reviser. Write `Listen_FirstTime.md` or `Listen_Skeptic.md`.

## The verdict

`Review.md` gathers the three reads: the counts; PASS when nothing is BLOCKING, otherwise REVISE; and each finding with its exact change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. There are no scores.

## The fresh read

After the one revision, a new trust reader and a new first-time listener, who have not seen this story's reads, `Revision.md` or any earlier draft, read the final `basil-of-caesarea.brief.txt` in full in the same way. They write `Fresh_Read.md`: the counts, PASS or REVISE, and each finding with its exact change. The fresh read blocks only for what the bar blocks. A MINOR finding there is applied word for word or noted, never the start of another round: the aim is reliable, sound work, not perfection. Once per batch, the same hands read the kind's reference stories in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/reference/` in the same way, without opening `Scores.md`, and `Reference_Read.md` sets their counts beside those in `Scores.md`.

Do not edit the story or commit. Each reply is under 150 words.
