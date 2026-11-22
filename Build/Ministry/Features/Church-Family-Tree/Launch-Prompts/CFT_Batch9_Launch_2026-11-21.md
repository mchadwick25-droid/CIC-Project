# Church Family Tree, batch 9 (era 2: the Greek East and the Nicene century): launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 9 end to end on the brief kit. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. The kit and its role prompts in `Brief-Kit/roles/` hold every standing rule (Decision-Log, "The brief kit: one kit, one prompt per step", 2026-11-21). Each agent gets its role prompt filled in with the batch header the kit describes, and nothing else: no copied batch prompts, no rule text, no Decision-Log entries to read.

**The group.** Era 2's Greek East and the Nicene century, as Mark approved in the batch 8 slate (Decision-Log, "Batch 8: the slate approved", item 3). Gregory of Nazianzus and Gregory of Nyssa, live and recorded, are reviewed in this batch as stories approved before the kit (Kit, Part 4, step 0); their earlier research is in `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/`. Before the slate, run `python tools/list_story_status.py --write` and read era 2 in `Story-Ledger.md`.

**Where things go.** The batch folder is `Build/Ministry/Operations/Audits/<date>_batch-9/`, with a README that carries each story's step, the open items and this batch's rulings, so a fresh session can pick up from it (Kit, Part 4). Batch 8's folder, `2026-11-21_batch-8/`, shows what each step's records look like.

**Step 0, then stop for Mark.** One page (an Artifact): each story's job in one line, its half, its census home, its siblings, and the live stories it sits beside (Constantine, Ambrose, Jerome and Leo from batch 8; Eusebius, Peter of Alexandria and the Melitian stories from batch 7). Name each quote already used elsewhere on the tree, and any reuse the kit's quote rule would allow. Run `python tools/check_tree_overlap.py` once on the old texts. Research starts only after Mark approves.

**Stops for Mark:** the slate; the hearts and lengths page; a brief that still fails after its one revision; a sibling or shape question; and the recording approval, in his own words with a credit cap.

**Recording.** Batch 8's settings (`2026-11-21_batch-8/recording/`): people in `onegjDE2z0mQtp1g0HK7`, `eleven_v4`; councils in `onwK4e9ZLuTAKqWW03F9`, `eleven_multilingual_v2`; both `mp3_44100_64`, stability 0.95, similarity 0.68, style 0, speaker boost on. Run one story per command.

**Release.** One pull request into `main`, merged when CI is green, then check churchfamilytree.com. Open-Gaps entries at the next free number. Promotion to `live` is Mark's call. Do not write the next batch's launch prompt unless Mark asks.
