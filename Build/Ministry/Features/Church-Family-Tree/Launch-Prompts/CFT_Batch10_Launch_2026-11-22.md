# Church Family Tree, batch 10 (era 2: Antioch to Chalcedon and the edges of the empire): launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 10 end to end on the brief kit. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. The kit and its role prompts in `Brief-Kit/roles/` hold every standing rule. Each agent gets its role prompt filled in with the batch header the kit describes, and nothing else.

**The group.** Era 2's Antioch to Chalcedon and the edges of the empire, as Mark approved in the batch 8 slate (Decision-Log, "Batch 8: the slate approved", item 3). John Chrysostom and Ephrem the Syrian, approved and recorded before the kit, are reviewed in this batch (Kit, Part 4, step 0); their earlier work is in `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/final/` and `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/drafts/`. Before the slate, run `python tools/list_story_status.py --write` and read era 2 in `Story-Ledger.md`.

**Where things go.** The batch folder is `Build/Ministry/Operations/Audits/<date>_batch-10/`, with a README that carries each story's step, the open items and this batch's rulings, so a fresh session can pick up from it. `Build/Ministry/Operations/Audits/2026-11-21_batch-9` shows what each step's records look like.

**Step 0, then stop for Mark.** One page (an Artifact): each story's job in one line, its half, its census home, its siblings, and the live stories it sits beside. Name each quote already used elsewhere on the tree, and any reuse the kit's quote rule would allow. Run `python tools/check_tree_overlap.py` once on the old texts. Research starts only after Mark approves.

**Stops for Mark:** the slate; the hearts and lengths page; a brief that still fails after its one revision; a sibling or shape question; and the recording approval, in his own words with a credit cap.

**Recording.** The settings in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md`, each passed on the command. Run one story per command.

**Release.** One pull request into `main`, merged when CI is green, then check churchfamilytree.com. Open-Gaps entries at the next free number. Promotion to `live` is Mark's call. Do not write the next batch's launch prompt unless Mark asks; when he does, fill in this template.
