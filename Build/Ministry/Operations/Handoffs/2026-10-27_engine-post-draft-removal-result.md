# Handoff — engine: post-draft sentence removal (F4/F5, F24) — result — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSAkfasNuLhs97dEbmt (coordinating); this thread's work is on branch `engine-post-draft-removal-f4-f5` · World or workstream: fleet engine (found in `lpc`) · Branch / PR: `engine-post-draft-removal-f4-f5` into `main`; the number is in the report to the coordinating session

Takes the two engine handoffs of 2026-10-27 (`..._engine-post-draft-sentence-removal-f4-f5.md`, `..._engine-lpc-review-other-items.md`). No `lpc` record changed. No model call, no live test, no paid run.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| **The answer-record fallback ships the record word for word.** `settle_reply` sent the record's text back through the net, which removed every sentence carrying the record's own quotation marks. `apply_net(answer_record=...)` now places the record's sentences by code and verifies each against the record (`grounding_net._placed_answer_verdict`). | Reproduced before: the suicide witness came back as six of its twelve sentences, the compassion question gone. After: all twelve. `test_post_draft_removal.py`. |
| **A removed cited sentence takes the sentences that lean on it.** The run just after it, in its paragraph, that opens by pointing back, cites no record and names no one ("That…", "Neither…", "But…") goes with it; a sentence with its own citation never does (`grounding_net.leans_on_previous`; in `apply_net`, `place_quotes`, `place_stories`). | 108 recorded drafts, eleven worlds: 5 sentences in 5 turns, all five read and all five leaned on a removed sentence. Unit tests. |
| **A reply that lost 40 percent or more of the sentences it rested on records for (failed markers and leaning cuts count) is replaced by the answer record**, given at least 3 such sentences and 2 removed (`HOLLOWED_SHARE`, `settle_reply`). The record is the offered witness the draft cited. With no record to show, the reply stands. | 38 lpc drafts, counted from the removals and kept sentences in their saved traces (the raw drafts were not saved): would fire on safety-4 (5 cited removed, 6 kept), register-6 and Deep Interview turn 9, all damaged. 108 recorded drafts, rebuilt and replayed: fires once (witt Q1, already a fallback). Unit tests. |
| **F24 fixed in the engine.** A rendering wrapped in quotation marks is set with each mark once; a quotation inside a rendering takes single marks (`grounding_net.quotable_rendering`). No record change, no change to the fleet rule on renderings. | Reproduced before: `““Lay this body anywhere...””`. Before the change 13 quote records placed with doubled or broken marks; after, none. All 455 quote records still place (`test_every_quote_record_in_the_fleet_places_word_for_word`). |
| **Findings F17, F18, F23 checked and sorted** (below). | Offline reproduction and reading. |

Run locally before the push: m4, m5, m1 (300), canon (5) and api (1074) suites, all passing; `tools/check_live_commentary.py --enforce --base origin/main` (exit 0); `tools/check_paths.py --baseline tools/check_paths_baseline.txt` (exit 0).

## 2. What the handoffs got wrong, or only half right

- **F4 did not start in the removal.** The evidence block for safety-4 never offered the suicide witness or its paired quote. Cell matching chose C-I and F5-I on common words (0.484 each); F6-T, whose witness lists this question word for word, was third at 0.337. The voice cited the witness from its system prompt and typed the quotations, and the net removed them. Reproduced offline. Registered as OG-99; not fixed here.
- **F18 has the same cause.** `lpc.limit.ordinary-interior-life` is in F5-I only; the off-topic questions reached F5-I on common words. Reproduced for safety-3 and Deep Interview turn 7. OG-99.
- **Register-4 is not a removal.** No quote was removed; the voice paraphrased it and wrote "These are his own words". OG-100.
- **Register-5's hard teaching was lost to the one-quote cap**, not to a guard the net ignored. OG-100.
- **The review's root-cause line ("removes sentences without reading the guards") is only partly right.** Guards are prose and the net cannot read them. What the engine can read is how much of the cited material it removed (`HOLLOWED_SHARE`).

## 3. Not done, and why

- **Safety-4's inversion is caught only through the hollowed-reply rule.** If the share had been under 40 percent, the remainder would have shipped. The threshold comes from four cases and is a judgment.
- **Silent omission of a hard teaching is not closed.** A cut reply can still leave out a teaching without dangling. Closing that needs a reader of the remainder (a model call) or a redraft. Neither can be proved offline.
- **A blanket cut was tried and measured out.** Cutting everything after a removed cited sentence turned full replies into one-sentence stubs (30 of 108 turns, about 12 percent of shipped sentences). Stopping at any removal would have hit 51 of 108 turns.
- **F17, F23, register-4's label, register-5's cap, retrieval.** OG-99 and OG-100.
- **Review round 1 (Opus, PR #1217), recorded and not fixed:** the answer record skips the net's claim checks (OG-101); a replaced reply can follow streamed sentences (OG-102); admission never calls `settle_reply` (OG-103).
- **Admission is not re-run.** The M3 live path calls the same `apply_net`; its grading of the reply a participant would read changes with this PR. Not run (model spend).

## 4. How often the fault can occur (offline)

Source: the 108 recorded drafts of 13 and 14 October (eleven worlds) and the 38 lpc single-turn drafts of 27 October. The recorded drafts predate the lpc prompt; counts are for the engine's removal step, not for judged damage, which only the `lpc` review made.

| Count | lpc (38 drafts) | Eleven worlds (108 drafts) |
|---|---|---|
| Turns with at least one removal | 22 | 51 (alx 6/12, cappadocian 4/6, desert 7/12, don 1/6, gallic 5/6, hal 7/12, ijc 8/12, pahc 2/12, rzg 1/12, syr 4/12, witt 6/6) |
| Turns with a removed sentence that cites a record | 11 | 36 |
| Turns that cite a record the evidence did not offer | 15 | 73 |
| Turns with a cited removal on an unoffered record | 4 of 11 | 21 of 36 |
| Cut as leaning, by the new rule | n/a (no draft order saved) | 5 turns, 5 sentences |
| Replaced as hollowed, by the new rule | 3 (damaged), counted from the traces | 1 |

The removal step runs on every reply of every world. The damage it can do (a changed meaning, a dangling remainder) needs a cited sentence removed, so it is a fleet matter, and it is likeliest where the voice cites from its prompt and not from the evidence block (OG-99).

## 5. Waiting on Mark

- **Live retest.** Safety-3, safety-4, register-5, register-6 and the Deep Interview, as a named test with a cap. His to name. Until then the fix is proved offline only.
- **One question to answer first:** should the retrieval defect (OG-99) be fixed before the retest? Recommendation: yes. It is the cause of safety-4's draft and of the off-topic limit; a retest before it measures the voice against evidence it was never given. Shown as an Artifact.
- **Later, no hurry:** F23 (report or block), the one-quote cap order (register-5), F25.

## 6. Next step

A retrieval thread, held to the leave-one-out and sixty-question instruments, to give the record whose `retrieve_when` names the question a place in the evidence: `engine/m4/evidence.py` `match_asks_to_cells` and the `canon` hint ranking. Reproduce with `evidence.match_asks_to_cells(message="What did Augustine teach about suicide in the City of God?", ..., top_n=4)` over the `lpc` records.

## 7. Spend

Allowance share used: one long session. Metered: none.
