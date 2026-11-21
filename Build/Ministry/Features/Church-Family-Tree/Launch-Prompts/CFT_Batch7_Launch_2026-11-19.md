# Church Family Tree, batch 7: launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 7 end to end on the brief kit, `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, with its role prompts in `Brief-Kit/roles/`. This finishes era 1 (Mark, 2026-11-19: "Let's focus in finishing era one then two"). Read `CLAUDE.md` first, then the kit, then the Decision-Log entries of 2026-11-19 headed "Batch 6" and "Change order: the stories approved before the kit go through review in their era's batch", and Open-Gaps 335 and 336.

**Batch 6 is the working model.** `Build/Ministry/Operations/Audits/2026-11-19_batch-6/` holds its README, every prompt it used (researcher, checker, fix, recheck, reviewer, reviser, story recheck, card, card check, card apply, new card), its hearts page, its originals ruling and its release record. Copy its prompts into `Build/Ministry/Operations/Audits/<date>_batch-7/` and change only the batch number, the rulings named and the jobs. Records go to that folder, with no shared scratch file between agents.

**The thirteen.** Rewrite eleven on the kit, and review two on it:
- Carthage: `tertullian-s-voice`, `cyprian-of-carthage`, `pontius-the-deacon`, `novatian`, `councils-of-rome-and-carthage-251` (council).
- Origen's line: `pamphilus-of-caesarea`, `eusebius-of-caesarea`, `dionysius-of-alexandria`.
- Alexandria to the Great Persecution: `peter-of-alexandria`, `anatolius-of-alexandria-and-laodicea`.
- Latin, under Diocletian: `lactantius`.
- **Approved before the kit, reviewed in this batch** (Open-Gaps 336): `origen` and `methodius-of-olympus`. Their Standard v1 texts (`Who-Profiles/bar/`) are live and recorded. They join at review, as Polycarp did in batch 6: approved wording is kept wherever it passes, and a fix touches only what fails. They are re-recorded only if a fix changes their text.

Tertullian, Cyprian, Lactantius and Pamphilus have no census card, so each gets a new card, checked. Tertullian's old recording is replaced.

**Step 0 first, then stop for Mark.** One page (an Artifact): each story's job in one line, with its siblings and links. Include the batch 6 stories that are now live (Pliny and Tertullian's answer to Trajan; Hermas, which Tertullian rejected; Hippolytus and Novatian; Josephus, Eusebius and Origen; Valentinus and Tertullian), and the live new-kit stories (Justin, Clement, Marcion, Antony, Athanasius, Arius, Nicaea). Name every quote barred because another story already uses it, and run `python tools/check_tree_overlap.py` once briefs exist. Siblings are researched after the story they depend on: Cyprian before Pontius, Novatian and the 251 councils; Eusebius before Pamphilus; Dionysius after Origen's live text is read. Research starts only after Mark approves the slate and the jobs.

**Batch 6's lessons, kept:**
- Mark, 2026-11-19: "ok we want it right, if two sorces say different things recognize that remember we are not pursuint perfection but high scholory acceptance". Where held sources differ, the story or card credits each.
- Originals on a card stand only as the page prints them. A scan fault is allowed only when a held print confirms the reading, or when it is a stray mark (`Batch_Originals_Ruling.md`). The census check drops Greek letters (Open-Gaps 335), so Greek is checked by hand.
- A quoted span may not hide a cut. Close the quote and reopen it, or tell the dropped part in narration.
- Length is a pressure, not a cap. When a reviewed story runs well past its approved heart, ask Mark, as batch 6 did for Irenaeus and Bardaisan.

**Stops for Mark:** the slate, the hearts page, a brief that fails after one revision, a sibling or shape question, a length well past the approved heart.

**Recording** is a paid run. It waits for Mark's approval and a credit cap, records one item first for his ear, prints its settings, and checks the balance after. Use batch 6's voice and settings (`2026-11-19_batch-6/recording/` logs).

**Release.** One pull request: a draft first, then merge the latest `main` in. Push once after the local checks pass: census validator, atlas-check, live commentary, American spelling, readability, tool tests and `tools/check_standard_lock.py`. Mark it ready, and merge it when CI is green. At release, take each released story off `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml` where it is listed, then refresh the ledger with `python tools/list_story_status.py --write`. Write Open-Gaps entries for what is open. Promotion to `live` is Mark's call. At the end, write the launch prompt for the first era 2 batch into `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/`, carrying the ledger step and the era 2 stories approved before the kit (Open-Gaps 336).
