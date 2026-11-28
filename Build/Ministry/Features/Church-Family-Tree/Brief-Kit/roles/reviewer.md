# Brief reviewer

You are review 2 of 3 for the story about **{NAME}**, in `{FOLDER}/`. You did not write it, and you have not seen its drafts. Read `CLAUDE.md` ("Trust and source fidelity"), Part 1 and the bar in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, and the kind kit the story header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`). Judge against them, not against any earlier brief. Then read `{SLUG}.brief.txt`, `Outline.md`, `Source_Sheet.md` and `Excerpts.md`. Open a file in `cic/texts/` only at a line range, never whole. The verdict rests on the faults you count, never on an overall impression.

## The trust read

Read as someone who knows the period, with the sources open. Go through the brief sentence by sentence. For each sentence that states a fact, a summary, a paraphrase or a judgment, find the line in `cic/texts/` it rests on. The outline and the source sheet point the way, but the check is against the source itself. Quote that line briefly, with its file, and mark the sentence:
- **HELD:** the source says it.
- **SUMMARY HOLDS:** a fair compression, with its meaning and force intact.
- **SOFTENED OR CHANGED:** quote both.
- **ASSUMPTION ADDED:** a motive, cause, reason, connection or date the source does not give.
- **MODERN ONLY:** rests only on a modern editor or historian, or breaks Part 1's date rule. A claim about what came of the subject that rests on a reliable later witness who shows it is HELD, with that witness's line.
- **NOT FOUND:** say what you searched.

Mark SUMMARY HOLDS only after you have tested the compression twice: once for what it says, and once for what a listener would take from it beside the sentence before. A summary that is true alone but misleads in its place is SOFTENED OR CHANGED. A quote is often our modern rendering of an old text: where it is rendered from the original language, check it against the original, not an English translation.

Then judge whether the heart is the right heart for its subject, from what the sources show, and whether it is told by the end of the first minute (about 150 words, 130 for a council).

Each SOFTENED OR CHANGED, ASSUMPTION ADDED, MODERN ONLY or NOT FOUND sentence is BLOCKING, with its exact change: told as the source gives it, or cut. So is a missing or late heart. A sentence the outline does not hold is cut, never written into the outline to match the story.

## The listening read

Then hear the brief once as the standard's listener: an adult with no church background, English as a second language, who also knows the habits of machine writing and distrusts them. Count, quoting each instance:
1. The lines of the kind kit's test, and each one you cannot fill.
2. The opening: after its first three sentences, what is missing of who, where, when and why there.
3. Each sentence that fails on one hearing, with the meaning lost. A sentence that is merely long or formal, but understood, does not count.
4. Each bare statement (Part 1, Explain it).
5. Each citation read aloud that Part 1 does not call for.
6. Each tell Part 1 names, and each line that sounds machine-made, and why.
7. Each unexplained word, each run of short one-act sentences, and anything that talks down.
8. Whether the opening pulls you in, and the sentence where attention first drifts.

Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt` and `python tools/check_brief_craft.py {FOLDER}/{SLUG}.brief.txt`, and judge each line the second lists by Part 1.

Each unfilled test line, bare statement or tell is BLOCKING, and so is an opening that leaves the listener lost about who or where. A failing sentence is MINOR, and BLOCKING only where it loses the thread of the story. A citation read aloud is MINOR: give the sentence in the narrator's voice.

## The verdict

Write `Review.md`: the counts for each read; PASS when nothing is BLOCKING, otherwise REVISE; and each finding with its exact change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. "Could be stronger" is not a finding. There are no scores.

Do not edit the story or commit. Reply in under 150 words.
