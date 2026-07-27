# Pass 2 Build-State Ledger

**Read this first, every session** (Session Contract rule 1 — see `SESSION_CONTRACT.md`).
All state lives here and in commits; no session relies on memory of a previous session.

- **Blueprint:** `Ministry/Technology/CiC_System_Redesign_Pass2_Blueprint_2026-07-26.md` (settled input — defects in it are FLAGS.md entries, never in-place edits)
- **Current step:** S1.4 next (S1.3+S1.5 are one unit gated on M1 — presented to Mark, pending)
- **Last completed checkpoint:** S1.2 G + B + R (`gates/S1.2_determinism.md`, `baselines/retrieval_baseline.json`, `reviews/S1.2_golden_case_verification.md`)
- **Parked items:** none

## Mark's decision points (M checkpoints — presented singly, recorded in the Decision Log before dependent steps proceed)

| ID | Decision | Needed before | Status |
|---|---|---|---|
| M1 | Record-store physical form (Pass 1 §12.2) | S1.5 | pending |
| M2 | First migration world (§12.5) | S2.1 | pending |
| M3 | `MIN_MULTI_WORLD_TURNS` floor retirement (§12.7) | S4.4b | pending |
| M4 | Lens spine adoption (§12.8) | S6.1 | pending |
| M5 | Streaming vs. selective buffering (§12.1) | never blocks; standing open item reviewed after S4.2 | pending |
| M6 | Appendix B governance-defect sweep (§12.6) | S6.4 | pending |

Additional per-item M checkpoints arise inside S2.9 (each schema Change Order), S5.5/S6.1/S6.4 (each governing-document wording), and S6.6 (threshold adoption).

## Step ledger

Statuses: `pending` / `in-progress` / `done` (done = checkpoint artifact exists, is committed, and re-runs green — rule 5, never the session's say-so). Every step ID below was enumerated mechanically from the blueprint (`grep -oE '\bS[1-6]\.[0-9]+[ab]?\b' | sort -uV`): 44 step-ID tokens, of which `S4.4b` is the blueprint's named sub-step of S4.4 — so 43 distinct steps, ledgered with S4.4 as one row carrying a gated half. (`S4.4a` is this ledger's own label for the sub-step the blueprint writes as "(a)"; the blueprint never spells "S4.4a".)

### Phase 1 — Measure and pin

| Step | Status | Checkpoint(s) | Artifact(s) | Notes |
|---|---|---|---|---|
| S1.0 | done | R | `reviews/S1.0_contract_ledger_review.md` | P1 (off-by-one in ledger's own count) caught and fixed in-step |
| S1.1a | done | G | `gates/S1.1a_instrumentation_completeness.md` (+ `S1.1a_gate_failure_proof.md`, gate script beside it) | 19 sites instrumented → 30/30 total; gate AST-based, deterministic (double-run byte-identical), proven non-vacuous against pre-step code |
| S1.1 | done | B + R-lite | `baselines/cost_baseline_2026-07.md` (+ raw JSONL, run notes, R-lite rerun log), `reviews/S1.1_token_recount.md` | B-COST: 40 live turns, 689 calls, $6.62 std / $0.165 per turn; cache-TTL pause measured (15,737-token prefix re-paid post-pause); C4 hit `CONVERSATION_TURN_CAP=20` at its turns 9–10 (real system behavior, see run notes); R-lite under FLAG-001 reading (exact recomputation + live shape re-verification) |
| S1.2 | done | G + B + R | `gates/S1.2_determinism.md`, `baselines/retrieval_baseline.json`, `reviews/S1.2_golden_case_verification.md` | R0/B-RETR: 105 golden cases across 6 worlds (all categories, 12–20 each), harness deterministic (byte-identical double run), LLM vote bracketed [retrieve/skip]; findings: dead-guard class generalizes (Tier-1 top-2 bypasses DNRW; all 45 ALX chunks are Tier 1), composite-Term de-dup gap is deterministic in every world, reactive-turn dilution measured (rank 6/4 burials), 2 genuine thematic embedding misses |
| S1.3 | pending | G | `gates/S1.3_seeded_defects.md` | gates + content-coverage parity program + parroting metric (F7); one unit with S1.5, schema first |
| S1.4 | pending | G + R | `gates/S1.4_schema_valid.md`, `reviews/S1.4_value_sources.md` | parameters file; no governing-doc edits |
| S1.5 | pending | G + R | `gates/S1.5_validator_fixtures.md`, `reviews/S1.5_traceability_matrix.md` | **after M1** |

### Phase 2 — First world migration (world per M2)

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S2.1 | pending | G + R | **after M2**; world_core + source records, backfill rule verbatim |
| S2.1a | pending | G | migration-time discovery sweep (§11-A per F2) |
| S2.1b | pending | R | reviewer coverage check (§11-B), PRESS question |
| S2.2 | pending | G + P + R | term records, mechanical half; runs S1.3's coverage instrument |
| S2.3 | pending | G + R | term records, new authoring; two-round minimum first batch |
| S2.4 | pending | G + R | story/quote/figure; narratability gate live for the first time |
| S2.5 | pending | G + R | gravity/force + Layer 4 |
| S2.6 | pending | G + R | contested_claim; partners from unmigrated worlds' documents (F1 withdrawn) |
| S2.7 | pending | G + R | voice_profile + demonstration; CO-015 lesson both directions |
| S2.7a | pending | G + R | Facilitation Brief human-judgment records on world_core |
| S2.8 | pending | P ×3 (render, probe, retrieval) | swap commit only after all three parities green |
| S2.9 | pending | M (per CO) + G | migration retrospective → Change Orders |

### Phase 3 — Retrieval rebuild

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S3.1 | pending | G + B + R-lite | R1/R2; truncation report |
| S3.2 | pending | G | R3 + R8; BM25/RRF hybrid |
| S3.3 | pending | G + safety rerun | R4/R5; conversation-state trigger applies |
| S3.4 | pending | G + B-COST delta + L-lite | R6; cross-encoder |
| S3.5 | pending | G + safety rerun + B | R9; both bridges (F8); commits B-RETR-POST-P3 |

### Phase 4 — Governance engine (safety rerun every step)

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S4.1 | pending | P (replay-parity) + safety rerun | recorded real classifier responses, not mock_llm defaults |
| S4.2 | pending | P + G (race fixture) + safety rerun | then A.4 re-diagnosis, filed |
| S4.3 | pending | G + L + safety rerun | 17 signal types; queue; FABRICATED split |
| S4.4 | pending | L + safety rerun + B-COST delta | (a) shippable now — first runtime consumer of parameters.yaml (F9); (b) **after M3** |
| S4.5 | pending | L + safety rerun | "what is faith" battery |
| S4.6 | pending | L + safety rerun + B | pushback battery; held/concession rates first computed |
| S4.7 | pending | L + safety rerun | multi-world battery; PART II cases via `git show CiC-Fable-Experiment:...` |

### Phase 5 — Voice, parroting, R7, access

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S5.1 | pending | G + B | B-PARROT; probe defs in wrs/probes/; RCF .docx edit belongs to S6.1 (open ambiguity noted in blueprint) |
| S5.2 | pending | P + G + B-PARROT rerun + B-COST delta + R | assembly; swap after all pass |
| S5.3 | pending | G + B-COST delta + L-lite | R7; tolerance per F3 |
| S5.4 | pending | G + R | Levels 2/3 + repository; rights fixtures |
| S5.5 | pending | M (per document) | Brief render live; parameters pointers |
| S5.6 | pending | L ×2 + gate report | representative-freeze, first migrated world (§11-C) |

### Phase 6 — Process and fleet

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S6.1 | pending | M (per document) + R | **after M4**; Completion Standard V1.0 |
| S6.2 | pending | per-world full pipeline | 5 worlds, order per Mark; includes companion-index deletions |
| S6.3 | pending | G + R-lite | divergence enrichment |
| S6.4 | pending | M (per item) | **after M6**; Appendix B sweep |
| S6.5 | pending | full regression | compatibility layer retirement — last, deliberately |
| S6.6 | pending | R + M | verdict report; thresholds adopted from real numbers |

## Standing rules in force

- **Safety regression rule** (blueprint §1): any step touching the intercept chain, `main.py` endpoint bodies, conversation state, or the public transcript ends with a full live safety script rerun; 19/20 floor; A.4 re-diagnosed at S4.2, not tinkered with before.
- **Retrieval regression rule** (blueprint §1): any step touching indexing/retrieval/ranking/query construction ends with a harness run diffed against the committed baseline (B-RETR through Phase 3; B-RETR-POST-P3 after S3.5); `do_not_retrieve_when` violations must be 0.
- **Gate-integrity rule** (from S1.3 onward): gate code changes are their own steps; never edit a gate in the session that must pass it.
