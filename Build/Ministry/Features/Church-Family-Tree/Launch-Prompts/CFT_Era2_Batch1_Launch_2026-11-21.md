# Church Family Tree, era 2, first batch (batch 8): launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 8, the first era 2 batch, end to end on the brief kit, `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, with its role prompts in `Brief-Kit/roles/`. Era 1 is finished (batch 7). Mark, 2026-11-19: "Let's focus in finishing era one then two." Read `CLAUDE.md` first, then the kit, then the Decision-Log entries of 2026-11-20 and 2026-11-21 headed "Batch 7: …", and the Open-Gaps entries for batch 7 and for "The stories approved before the kit: reviewed in their era's batch".

**Batch 7 is the working model.** `Build/Ministry/Operations/Audits/2026-11-20_batch-7/` holds its README, every prompt it used (researcher, checker, fix, recheck, writer notes, reviewer, reviser, story recheck, card, new card, card check, card apply, release), its hearts page, its originals ruling, its second readings and its release record. Copy its prompts into `Build/Ministry/Operations/Audits/<date>_batch-8/` and change only the batch number, the rulings named and the jobs. Records go to that folder, with no shared scratch file between agents.

**The ledger.** Before the slate, run `python tools/list_story_status.py --write` and read era 2 in `Build/Ministry/Features/Church-Family-Tree/Story-Ledger.md`: 12 on the kit, 64 to do when batch 7 closed. Era 2 is several batches. At Step 0, propose to Mark how era 2 splits into batches of about twelve, by region and theme, with siblings kept together and researched in order. Mark decides the split.

**The stories approved before the kit** (Open-Gaps, "The stories approved before the kit: reviewed in their era's batch"): Constantine the Great, Ephrem the Syrian, Gregory of Nazianzus, Gregory of Nyssa and John Chrysostom are live and recorded at Standard v1 (`Who-Profiles/bar/`). Each joins the review of the era 2 batch its siblings are in, as Origen and Methodius did in batch 7: approved wording is kept wherever it passes, a fix touches only what fails, and it is re-recorded only if a fix changes its text. Their research is in `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/`.

**Step 0 first, then stop for Mark.** One page (an Artifact): the proposed era 2 split, then for this batch each story's job in one line, with its siblings and links, including the live stories it sits beside (batch 7's Eusebius, Lactantius, Peter of Alexandria and the Melitian stories reach into era 2). Name every quote barred because another story already uses it, and run `python tools/check_tree_overlap.py` on the old texts once to find shared quotes. Research starts only after Mark approves the slate and the jobs.

**Batch 7's lessons, kept:**
- Length (Mark, 2026-11-20: "we need to keep to 4 maybe 4:30 max"): a story aims at about 4:00 and never runs past about 4:30 (person about 675 words, council about 585, by the scorer). In batch 7 the outlines planned five to seven minutes of beats even after counting; the writers compressed to 4:30. Researchers should plan to 4:00 from the start, with firm "for the card, not the story" sections.
- Where held sources differ, the story or card credits each (Mark, 2026-11-19). A quoted span may not hide a cut. Originals stand only as the page prints them (`2026-11-19_batch-6/Batch_Originals_Ruling.md`, `2026-11-20_batch-7/Batch_Originals_Ruling.md`). The census check compares Greek (Open-Gaps 337); Greek is also checked by hand.
- The census check allows `disputed` only under a card's `sources.ownWords`, not `about`.
- Writers, revisers and card writers sometimes exceed a count by a few words or skip a minor fix to hold it; the story recheck catches it.

**Stops for Mark:** the slate and the era 2 split, the hearts page, a brief that fails after one revision, a sibling or shape question, a length past 4:30.

**Recording** is a paid run. It waits for Mark's approval and a credit cap, records one item first for his ear, prints its settings, and checks the balance after. Use batch 7's voices and settings (`2026-11-20_batch-7/recording/` logs): people in `onegjDE2z0mQtp1g0HK7`, `eleven_v4`; councils in Daniel, `onwK4e9ZLuTAKqWW03F9`, `eleven_multilingual_v2`; both `mp3_44100_64`, stability 0.95, similarity 0.68, style 0, speaker boost on.

**Release.** One pull request: a draft first, then merge the latest `main` in as the last step before the push. Push once after the local checks pass: census validator, census tests, atlas-check, live commentary, American spelling, readability, tool tests and `tools/check_standard_lock.py`. Mark it ready, and merge it when CI is green. At release, take each released story off `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml` where it is listed, then refresh the ledger with `python tools/list_story_status.py --write`. Write Open-Gaps entries for what is open. Promotion to `live` is Mark's call. At the end, write the launch prompt for the next era 2 batch into `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/`.
