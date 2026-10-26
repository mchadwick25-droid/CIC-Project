# P2 Pass Recheck (round 2) — lpc, branch `claude/lpc-p2-pass-2026-10-25`

- **Scope.** A targeted recheck of findings R1–R12 in `P2_Pass_Review_2026-10-25.md`, against the changes since that review: `git diff b575918b`, now committed as `03861b0d`. Only what changed was checked.
- **Reviewer.** Opus 5.5. No model API was called. No file was edited except this one.
- **Date.** 2026-10-25.

## Findings from round 1

| id | status | evidence |
|---|---|---|
| R1 (P1) | **Fixed** | `lpc.source.tertullian-de-pudicitia` no longer claims a licence. The body says "Cited for one passage, as comparandum evidence", and both the body and `rights_status` say "Registry row 29 is Excluded and licenses nothing from Tertullian." The boundary question stays open with the project lead (OG-70, carried). |
| R2 | Fixed | `edition` says "lines 9550-9659". anf04 line 9659 is `</div3>`, and XXIII opens at 9661. |
| R3 | Fixed | `divergence_note` adds the upper bound. anf03 line 62 reads "Tertullian (c. 160-c.  230)", from the CCEL catalogue metadata. Line 4763 reads "Tertullian deceased (extreme surmise) 240.", in the editor's chronology. So "about 230 … 240 at the latest on the editor's furthest surmise" holds. The inference that the treatise comes before 250 holds: it was written no earlier than 208 and before its author's death by 240 at the latest. |
| R4 | Fixed | "Knopf lines 5632-5639". Line 5639 ends "memoriae relinqueremus.", and II opens at 5641. |
| R5 | Fixed | Record and `wb_lpc_s28.py` both say "lines 14147-14168 and 14185-14195". npnf101 line 14168 closes IX.10's speech ("what do I here?”"), and line 14195 closes IX.11's last words ("be.”"). |
| R6 | Fixed | The 34-word sentence is split, at 19 and 16 words. The change is in the generator and the record. |
| R7 | Fixed | The witness `positions` sentence is now 14 + 18 words. It is a hand-kept record, so no generator applies. The gravity sentence is now 6 + 16 + 8 words, in `wb_lpc_s25.py` and the record. |
| R8 | Fixed | "sinners who ask imprisoned martyrs for peace", in `wb_lpc_s25.py` and the record. This matches the force record `lpc.force.decian-persecution-libelli-system` (line 62) and both `sources[]` loci. |
| R9 | Fixed | §4 now applies "one bishop writing" to the letters only. It also keeps Doc_04's bound: "Within what Doc_04 validly read … the *Gesta* was not validly read for the question (§4a)." (24 words.) |
| R10 | Fixed (routed) | The corpus map was not edited. A Library flag sits in `NEEDS-RULING.md`, and OG-71 logs it with the Library thread as owner. That follows the default actions table. |
| R11 | Fixed | The `wb_lpc_s21.py` docstring now names both records as "Not emitted here, and kept by hand". |
| R12 | Fixed | The parenthetical ruling pointer is gone from the precedent header. As round 1 advised, the wider header narrative was left for the project lead. |

## Checks

- **Sentence length.** Every participant-facing sentence edited in this pass is 25 words or fewer. The longest is 19.
- **Live-file commentary.** `tools/check_live_commentary.py --base b575918b` shows no REWRITE or ROUTE line. The new `wb_lpc_s21.py` docstring lines describe what the script does and does not emit. They are not process notes.
- **Regeneration.** I made a detached worktree of `03861b0d` under the scratchpad. The branch tree was clean, so it holds the full diff. I ran `wb_lpc_s21.py`, `wb_lpc_s25.py` and `wb_lpc_s28.py` there, with all three exiting 0. They emitted 245 records, including the two edited gravities and the edited honest limit. I parsed the front matter and body of each one and compared it with the branch: 0 differ and 0 are missing. 38 files differ in bytes only, from line wrapping. The worktree was then removed.
- **Tracking.** OG-71 is appended with a new number. It closes OG-70's second carried item by subject, and OG-70 itself is unedited.

## New findings

None at P1 or P2.

One note, not graded. The new `divergence_note` sentence in `lpc.source.tertullian-de-pudicitia` runs 32 words with its two citations. It is source-record metadata, not spoken text, so the 25-word bar does not bind it. If a later pass touches the field, splitting it at "so the practice…" would cost nothing.

## Verdict

**Approved to proceed.** All twelve findings are fixed: R1, the P1, and R2–R12. The regeneration check is clean, and this pass adds no P1 or P2. The question of a licence for Tertullian chapter XXII (OG-70) is still open with the project lead. The *City of God* date in the corpus map (R10) is still open with the Library thread.
