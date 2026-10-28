# Handoff — engine: post-draft removal, answer-record quote gate and cell matching, what is left — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSDNWfgSRzVVN7ZYFex (coordinated by session_01JMNsSAkfasNuLhs97dEbmt) · World or workstream: fleet engine (found in `lpc`) · Branch / PR: four pull requests, all merged into `main`: #1217, #1219, #1223, #1230

Supersedes the two engine handoffs of 2026-10-27 (`..._engine-post-draft-sentence-removal-f4-f5.md`, `..._engine-lpc-review-other-items.md`) and the interim `..._engine-post-draft-removal-result.md`; their open items are now OG-98 to OG-104 in `Build/worlds/lpc/Open_Gaps_Tracking.md`. No `lpc` record was changed. No model call, no live test, no paid run in any of the four.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| **The answer record is shown word for word.** It was sent back through the net, which removed every sentence that carried its own quotation marks (the `lpc` suicide witness came back as 6 of 12 sentences, the compassion question gone). `apply_net(answer_record=...)` places it by code (#1217). | Reproduced before, held by `engine/m4/tests/test_post_draft_removal.py`. |
| **A removed cited sentence takes the sentences that lean on it.** A leaning sentence opens with a back-pointing word ("That", "These", "Neither", "But", "So"), cites nothing, names no one and does not open a relative clause; it stops at a paragraph break; a failed quote or story marker counts (#1217, #1219). | 108 recorded drafts from eleven worlds: 5 sentences in 5 turns, all read, all correct. Two Opus review rounds on #1219, findings 1 to 5 fixed. |
| **A reply that lost 40% or more of what it cited is replaced by the answer record**, given at least 3 such sentences and 2 removed; the record is an offered witness; with none offered the reply stands (#1217, #1219). | Counted from the saved `lpc` traces it would fire on safety-4, register-6 and Deep Interview turn 9, all damaged; once on the 108 recorded drafts. |
| **Doubled quotation marks (F24) fixed in the engine** (`grounding_net.quotable_rendering`). | 13 quote records placed with doubled or broken marks before, none after; all 455 still place. |
| **An offline check of every quotation inside a doctrinal answer record** against the vendored sources (`engine/m1/witness_quotations.py`, #1223), as the project lead ruled. | Seeded bad-quote tests; the real corpus held to `engine/m1/witness_quotation_findings.txt`. 87 quotations verify, 3 fail at the gate's scope, 2 more below it. |
| **Cell matching fixed (#1230).** A cell scored as the union of all its `retrieve_when` entries, so it collected shared words from entries that never stand together; the safety-4 question left the suicide witness out of its evidence. A cell now scores as its best single statement, and hint statements compete with the canon ranking on score. | Hint recall 2212/2318 to 2317/2318; each canon question finds its own cell 1176/1176 before and after; table for all twelve worlds in the `lpc` Decision Log. Reproduce with `python engine/m4/reports/cell_match_eval.py out.json` on the base and on a branch. |

Rulings recorded in `Build/worlds/lpc/lpc_Decision_Log.md` and `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`: the answer-record quote check, and retrieval first. Design entries in the `lpc` log: "F4/F5: the engine's design…" and "Cell matching scores a hint as the statement it is".

## 2. Not done

- **The live retest.** Safety-3, safety-4, register-5, register-6 and the Deep Interview. Nothing here proves the live replies now read right; it is proved offline only.
- **The witness-quotation gate is not in `gates.GATES`.** Registering it re-bakes `validation/gates-report.json` in every package (a fleet re-pin) and fails the don, ijc and witt builds until their three records are fixed. Findings: `don.dw.two-churches-in-one-town` (OG-55 in don), `ijc.dw.how-we-read` (entry 46 in ijc), `witt.dw.how-the-promise-reached-us` (OG-85 in witt). Two more below `verified-direct` show in `python -m engine.m1.witness_quotations`.
- **OG-100:** register-4 (the voice paraphrases a quote and writes "These are his own words"; the net has no rule for it), register-5 (the one-quote cap goes to the first marker, so a soft quote can take the slot of the hard teaching), F17 (tag-overlap floor), F23 (the output check reports and never edits).
- **OG-101:** the placed answer record skips the net's thin-topic and unknown-record checks. The quote check covers only its quotations.
- **OG-102:** a hollowed reply can replace a reply whose first sentences have streamed; the client swaps the partial for the finished reply.
- **OG-103:** admission (`engine/m3/generation.py`) calls `apply_net` and never `settle_reply`, so it never grades a replaced reply.
- **OG-104:** Deep Interview turn 7 still reaches F5-I, and `lpc.limit.ordinary-interior-life` rides with it. The canon match there is legitimate; the limit belongs to F5-I only.
- **No ground truth for cells.** The bench counts records, not whether the right cell came back. I judged the questions that moved by reading them.

- **The #1230 review (REVISE, Opus) is open after its merge.** Blocking: statements that need two shared words in one entry lose ground the pooled and other tiers reached; the stem tier is still pooled and appended after hint matches, so matches are not ordered by score; a suicide witness is not offered for "What did your people say about someone who killed themselves?". A follow-up pull request carries the fix.

## 3. Re-check before you trust

- **The 40%, 3 and 2 are judgments.** They come from four `lpc` cases and the decision to exclude a single removal; no recorded draft falls below the minimums.
- **The leaning rule is by opener.** "But the bishops gathered.", "This was hard." and "Those were days." still count as leaning when they follow a removed cited sentence (a test holds it), so a sentence that does not point back can be cut.
- **Hint recall is partly circular.** The questions are the hints; it shows the cell that names a question comes back against competitors, not how unseen questions do. The bench is the independent set, and it counts.
- **The 108 recorded drafts were rebuilt.** `engine/m4/tests/live11_replay.py` puts cut sentences back by a stated rule, so positions are approximate.
- **`retrieval_bench.py` does not list `lpc`** (it is not in the formation registry) though `bench/lpc.json` exists. The `lpc` numbers come from `cell_match_eval.py`, which does.
- **Nine of the 108 recorded turns (six distinct generic prompts) now choose other cells**, ground 815 to 804. They are prompts like "Tell me about someone who lived this out", for which no cell is clearly right.
- **The reviews.** I saw the findings of both rounds on #1219. I did not see the review of #1230 or #1223; the coordinator merged them after it.

## 4. The faults, in one line each

1. After drafting, the net removed sentences one at a time and shipped the rest unread.
2. The fallback to the answer record was damaged by the same step.
3. The evidence for the safety-4 question never held the suicide witness, so the voice cited it from its prompt and typed its quotations; this, not the removal, started F4.
4. Pooled hints let a cell with many entries beat the cell whose one entry names the question.

## 5. Waiting on Mark

- **Name the live retest and its cap** (safety-3, safety-4, register-5, register-6, and the Deep Interview). Retrieval is fixed first, as he ruled.
- **Register the witness-quotation gate, or fix the three records first.** One or the other unblocks it.
- **Later:** whether the one-quote cap should favour a particular quote (register-5), whether a horizon finding should block or redraft (F23), and whether the stream should hold sentences until a reply can no longer be replaced (OG-102).

## 6. Next step

For an engine thread: OG-103, the smallest. Make admission call `settle_reply` so it grades the reply a participant would read, then re-run admission only if the project lead names a capped test. After the live retest, read the traces for `reply_shape.removed` and for `offered_ids` first; those two show whether the removal rules and the evidence did their part. For the `lpc` build thread: the scope of `lpc.limit.ordinary-interior-life` (OG-104). Offline only; any live rerun needs the project lead's named test and cap.

## 7. Spend

Allowance share used: one long session across four pull requests. Metered: none.
