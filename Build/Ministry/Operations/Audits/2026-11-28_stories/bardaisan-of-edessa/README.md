# Bardaisan of Edessa (`bardaisan-of-edessa`): the rebuild of 2026-11-28

Branch `claude/cft-story-bardaisan`. One story, run on the brief kit (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`) by one thread. It reports to the CFT project manager session (session_01JMNsSEFT3XBAJcDh8uPC1s), which relays Mark's rulings.

## The story header

- **Name:** Bardaisan of Edessa. **Slug:** `bardaisan-of-edessa`. **Kind:** person (`kinds/person.md`), era 1. **Shape:** Teacher or thinker.
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-28_stories/bardaisan-of-edessa/`. **Card file:** the `card` of `bardaisan-of-edessa` in `cic-website/data/world-census.json` (the starting card); the new card is written to `bardaisan-of-edessa.card.json` in this folder.
- **Job on the slate:** a Christian teacher at Edessa around 200 who taught that people are free and not ruled by the stars; the dialogue a pupil tells; Eusebius on his pupils and his writing against Marcion's followers; the later witnesses who called him a heretic and disagree why; his followers' songs, which Ephrem answered. Told within `bardaisanite-current` ("the Bardaisanites").
- **Siblings:** `bardaisanite-current` (a thin tradition, done later: Open-Gaps 417 and 437; its documented story opens on the same scene), `ephrem-the-syrian`, `valentinus`, `marcion-of-pontus`, `eusebius-of-caesarea`, `epiphanius-of-salamis`, `jerome` (each job in `Outline.md`, Sibling).
- **Approved heart:** Decision-Log, "2026-11-19 — Batch 6 hearts approved; Josephus told with what is held (Mark)", and the Bardaisan paragraph in `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Hearts.md`.
- **Length:** about 5:15, up to about 790 words, for this story only (Mark, 2026-11-28, relayed by the manager: the option "Allow about 5:15 (Recommended)"; "as with Tertullian"). This replaces the batch 6 "about 4:30" for this story.
- **Rulings for this story alone (Mark):** the length above (2026-11-28); logged in the Decision-Log at release. The heart's "the only text in his voice" is not told; the story's wording ("comes down to us as one of his pupils, Philip, tells it") stands for review 2 to test (manager, 2026-11-28). Standing: new work passes at B or with Mark's sign-off (2026-11-28).

## Why it is rebuilt

The live text was approved before the kit. It grades C on the whole-text method (`Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/Calibration_Whole.json`: rigor B, craft D) and D on the 25 Nov readers (`2026-11-25_person-council-grades/Grades.json`: two modern-opinion findings; opening missing where and when; Ephrem's soul-and-body charge bare; a sentence that only says what is missing; Ephrem's curse on "the Seven" lost the listener; the Eusebius sentence drifts out of the scene).

## Step

1. Research: done. `Source_Sheet.md` (the batch 6 sheet, brought up to the kit: E14, E15, X1–X3 added), `Outline.md` (new, to Part 2: the essence said once, the dialogue told once in its own order, the witnesses in time order, Cut first list), `Excerpts.md`.
2. Review 1, the outline check: FIX (2 BLOCKING, 6 MINOR), all applied (`Fixes.md`: none set aside). B1 brought in four held texts the sweep had missed, above all Eusebius's long Greek quotation of the dialogue (*Preparation for the Gospel* VI.10); B2 recounted the beats at about 845 words and added Cut first items 7–11.
3. Write: draft written, every Cut first item dropped, wording tightened with nothing further cut: 784 words, about 5:14 (readability pass: grade 8.8, names out 7.9; reading ease names out 75.3). The essence is complete at word 135. `check_tree_overlap.py`: clear. **Stopped for the length** (writer role: "if it still runs long, stop and say so"); Mark ruled (a): about 5:15, up to about 790 words, this story only.
4. Review 2, the brief review: REVISE (3 BLOCKING, 3 MINOR), all applied word for word, no wording of my own (`Revision.md`); its four Do not say lines added to `Outline.md`. 795 words, about 5:18; grade 9.0 (names out 8.1), reading ease names out 75.0: pass. The essence ends at word 135. Backup `bardaisan-of-edessa.brief.v1.txt`.
5. Card (Sonnet hand): `bardaisan-of-edessa.card.json`, `Card_Edits.md` (timeline in 12 periods, briefSources, shortDescription, Q3 trimmed to the brief's span, Gwynn and Smith moved to `modernWorks`; entry-field changes listed for release; none not found). The card hand's note: on a scratch census copy the validator shows two errors only, `tools/quote_renderings.json` lacking the new Q3 and holding the old one; release replaces that listing.
6. Review 3 set up: `Second_Reading_Requests.md` and `Second_Reading_Key.md` written (3 spans, all read blind). **Next: the final check**, a fresh Opus hand given `roles/final-check.md` filled in with the story header above and nothing else.

## Open items

- Decision-Log entry for the length ruling: at release.

## Handover (2026-11-28, context past 150,000 tokens)

This session stopped after the card with context about 285,000 tokens and cost $14.80 of its $20 cap. A fresh session picks up from this README:
1. Review 3, the final check (`roles/final-check.md`, the header above). Apply its exact changes word for word; a blocking fault it cannot settle goes to the manager.
2. The grade (Stage Two Kit section 5). `Grade/` already holds copies, unchanged, of `grade.py`, `grade_whole.py`, `score_this.py` and `Listener_Prompt.md` from `../tertullian-s-voice/Grade_2/`, and in `Grade/scans/` the reader, modern-reader and third-read prompts and `merge.py` from `../tertullian-s-voice/Grade/scans/`. Still to make: `Grade/Set.json`, `Grade/packets/S01.md` and `L01.md` (the final brief, in the Tertullian packets' format), then two bare readers, one modern reader, `merge.py`, a third read if needed, the listener and `score_this.py`. Note: the copied `merge.py` writes the era1-new-grades packet path into the third-read header; point the third reader at `Grade/packets/S01.md`. The grade passes at B, or with Mark's sign-off.
3. The blind check: three fresh Opus readers, one each against the Basil, Epiphanius and Chrysostom reference briefs, using the prompt in `../tertullian-s-voice/Grade/blind_pairs_inputs/pairs/p01/prompt.txt` with only the paths changed, X and Y drawn at random. It passes when 2 of 3 give B− or better and none says clearly worse.
4. One Artifact page: the brief, the card, the three reviews' counts, the grade with its findings, and the blind result. Send the manager the link and stop. No release, pull request or recording.

Review counts so far: outline check FIX, 2 BLOCKING, 6 MINOR; brief review REVISE, 3 BLOCKING, 3 MINOR.

## Cost (from `get_session`)

- After the outline check and fix pass: $6.10 (`get_session` `usage.cost_usd`, list-rate telemetry, not a bill; read again after writing, still $6.10, last updated 09:16 UTC).
- After review 2 and the revision: $12.05 (13:14 UTC).
- After the card: $14.80 (13:20 UTC).
