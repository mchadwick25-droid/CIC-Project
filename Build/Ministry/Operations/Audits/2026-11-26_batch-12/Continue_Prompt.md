# Continue batch 12 (era 1 people and the era 1 brief)

You are taking over Church Family Tree batch 12 from an earlier session, whose context ran long. Work on branch `claude/batch12-era1-persons`.

1. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` and `Brief-Kit/kinds/person.md` (and `kinds/era.md` for the era brief).
2. Read `Build/Ministry/Operations/Audits/2026-11-26_batch-12/README.md` in full. Its section "Where each story stands" gives each story's step and next action. Its "Rulings" and "Steps" sections hold Mark's words verbatim. The Decision-Log entries "Batch 12: the slate approved", "Batch 12: hearts and lengths approved" and "Batch 12: lengths measured by the draft" (all 2026-11-27) carry the rulings too.
3. Bring the branch up to date with `main` before anything else; the era 1 card thread edits the same census entries.
4. Mark's rulings that came in at the handover are listed at the end of this file and are already recorded. Go on from the next actions there and in the README.
5. Run each step as the README's "How each step was run" says. Each hand is a fresh agent started from one filled prompt file in the story's folder; the generators are in `_gen/`. Run no more than about twenty hands at once.
6. Stops for Mark go to the coordinator session (`session_01JMNsSDxiDjhkPh1K48BmfL`) with send_message; his words come back verbatim. The remaining stops are a brief that still fails after its one revision, a sibling or shape question, and any length or heart question the ruling does not cover. Pages for Mark reuse a batch 12 artifact, because the account is at its artifact limit.
7. No recording in this batch. Release is one pull request into `main`, merged when CI is green, then check churchfamilytree.com. Open-Gaps entries go at the next free number. Promotion to `live` is Mark's call.

Commit and push as you go.

## Mark's rulings at the handover

Both are already written into the Decision-Log ("Batch 12: the first two briefs approved, and the long stories' lengths", 2026-11-27), the README and each long story's outline ("Length ruling" line). Mark's words: "approve as recommended", answering both pages together.
- Ignatius and Tacitus are approved; their cards come next (Kit step 6), after the others reach the card step or alongside them.
- The fourteen are approved to write in parallel; their `Writer_Prompt.filled.md` files are ready.
- Lengths: Cyprian about 965, Origen about 950, Eusebius about 850, Josephus about 725 (review its draft as written), the era about 730.

Next actions, in order: write the fourteen; review Josephus's 725 draft; apply the named cuts at the outline for Cyprian, Origen, Eusebius and the era, recheck, and draft them. Then review, revise and fresh-read each, run the person reference read once, and go on to cards, second readings and release.
