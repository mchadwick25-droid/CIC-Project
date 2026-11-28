# Church Family Tree story: {NAME} ({KIND}, era {ERA}): launch

Paste this as the first message of a new session. One story per session.

---

Run the Church Family Tree story for **{NAME}** end to end on the brief kit. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. The kit and its role prompts in `Brief-Kit/roles/` hold every standing rule. You do the research, writing, revision and release yourself, on Opus. The card is written by a Sonnet hand. The three reviews (outline check, brief review, final check) are each a fresh Opus hand, given its role prompt filled in with the story header the kit describes and nothing else. There are no other reviews.

**The story.** {SLUG}, its census home {TRADITION}, its card file {CARD}. {THE DECISION-LOG ENTRY WHERE MARK APPROVED IT.} {"APPROVED BEFORE THE KIT AND REVIEWED HERE", OR "NEW".} Run `python tools/list_story_status.py --write` and read era {ERA} in `Story-Ledger.md` first.

**Where things go.** The story folder is `Build/Ministry/Operations/Audits/<date>_{SLUG}/`, with a README that carries the story's step, the open items and its rulings, so a fresh session can pick up from it.

**Stops for Mark:** the slate check (step 0), on one page; the heart and length; a BLOCKING outline finding not applied; a blocking fault the final check cannot settle; the finished brief before release; a sibling or shape question; and any recording, in his own words with a credit cap.

**Release.** One pull request into `main` for the story, merged when CI is green, then check churchfamilytree.com. Open-Gaps entries at the next free number. Promotion to `live` is Mark's call. Report the story's cost from this session's record in the release. Do not start another story in this session.
