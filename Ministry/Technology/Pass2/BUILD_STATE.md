# Pass 2 Build-State Ledger

**Read this first, every session** (Session Contract rule 1 — see `SESSION_CONTRACT.md`).
All state lives here and in commits; no session relies on memory of a previous session.

- **Blueprint:** `Ministry/Technology/CiC_System_Redesign_Pass2_Blueprint_2026-07-26.md` (settled input — defects in it are FLAGS.md entries, never in-place edits)
- **Current step:** S2.9 - register written (change_orders/S2.9_CO_Register.md, 11 COs); CO-P2-01 (swap decision) PRESENTED to Mark, awaiting his call; no CO applied. Non-dependent next work while M pends: Phase 3 (S3.x, operates on today's chunk formats via the compatibility rule).
- **Last completed checkpoint:** S2.8 (`gates/S2.8_three_parities.md` - render 0-unclassified, retrieval 0-regressions, probe 6/7 with the divergence characterized; NO swap: presented to Mark at S2.9)
- **Parked items:** none

## Mark's decision points (M checkpoints — presented singly, recorded in the Decision Log before dependent steps proceed)

| ID | Decision | Needed before | Status |
|---|---|---|---|
| M1 | Record-store physical form (Pass 1 §12.2) | S1.5 | **decided 2026-07-26: files-in-git** (`decisions/M1_record_store_form.md`) |
| M2 | First migration world (§12.5) | S2.1 | **decided 2026-07-26: Desert** (`decisions/M2_first_migration_world.md`) |
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
| S1.3 | done | G | `gates/S1.3_seeded_defects.md` | `wrs/gates/` + `wrs/metrics/parroting.py`: 6 gates (referential, reciprocity, completion w/ backfill profile, narratability, quote-recording, sentinel) + readability instrument + F7's coverage-parity & parroting instruments; self-test green (all clean pass, 13/13 seeds caught, byte-identical double run); F5 annex: gate run on the six deployed prompts finds exactly the documented Marius drift (FK 11.5/FRE 59.8) and nothing else. **Gate-integrity rule in force from here** |
| S1.4 | done | G + R | `gates/S1.4_schema_valid.md`, `reviews/S1.4_value_sources.md` | `wrs/parameters.yaml`: 13 parameters (all traced — 2 governing-doc values re-verified verbatim, 10 from code, 1 TBD per §11-D) + 14 §10 metric records; no governing-doc edits; no runtime consumer yet (F9 → S4.4a) |
| S1.5 | done | G + R | `gates/S1.5_validator_fixtures.md`, `reviews/S1.5_traceability_matrix.md` | M1 = files-in-git; `wrs/schema/`: envelope + 13 record types + gloss list (draft 2020-12, unevaluatedProperties:false), validator (+ em-dash sentinel rule), 13/13 fixtures valid, seeded-invalid fails with 6 named errors, traceability 143/143 both directions (blueprint-origin elements named: world_core.pairing_guidance/cautions per S2.7a) |

### Phase 2 — First world migration (world per M2)

| Step | Status | Checkpoint(s) | Notes |
|---|---|---|---|
| S2.1 | done | G + R | Desert: 16 source records + world_core from Doc_02/Doc_01 prose via `wrs/migrate/source_rows_from_doc02.py` (the declared mapping); backfill rule verbatim (4 fields coarse, instrument/date never set — grep 0 hits); 17/17 validate, gates green (backfill profile), migration byte-deterministic; R sample (seed 20260726: srcDES004/006/007/012) caught 2 mapping deviations, fixed in-step |
| S2.1a | done | G | `gates/S2.1a_discovery_sweep.md` + `wrs/migrate/s21a_discovery_sweep.py` (the sweep log): 8 rows added with REAL discovery data (srcDES017–024; 4 were load-bearing in Doc_02's prose but row-less incl. Bartelink SC 400 verified at sourceschretiennes.org), 4 exclusions logged; search_record srcDESsearch001 (STARLITE, migration-time scope, BIBP/L'Année logged as coverage limits); 26/26 valid, gates green |
| S2.1b | done | R | `reviews/S2.1b_coverage_check.md`: relative recall 9/10 (miss: Cassian — no row anywhere); PRESS answered with 3 named works (Cassian; Butler's Lausiac History edition; Guy SC editions); all routed to S2.9/pre-freeze re-sweep, no records edited (per Touches) |
| S2.2 | done | G + P + R | 9 term records via `wrs/migrate/lexicon_chunk_split.py` (mechanical, parses the real chunks); coverage parity 9/9 full (instrument caught a real parser bug first run — 5/9 failing, fixed); drops = exactly the legal classes, logged (2 retired cross-world + 5 em-dash sentinels, matching Touches prediction); EF parked in world_meaning per FLAG-002; 35/35 valid, gates green |
| S2.3 | done | G + R×2 | All 9 terms: four senses (prior senses not in build docs marked UNVERIFIED, never asserted), voice_surface (plain register, ~60-word measure), semantic_domain, 3-axis confidence, 24 typed reciprocal field_relations absorbing EF (FLAG-002 parking removed; chunk EF verbatim on first edge for parity); coverage 9/9; reciprocity 0 violations; Round 1 caught P1 invented-aphorism class in 5 voice_surfaces (fixed); Round 2 clear (P2s only); known staged gap: world_core.gravities → S2.5 |
| S2.4 | done | G + R | 8 story + 3 quote + 12 figure records (58/58 valid). Narratability gate's first real run fires 4× (Syncletica/Theodora/Poemen/Sisoes — prompt-named, unnarratable; routed to S2.9). Quote fidelity PERFORMED: Moses/Sarah verified vs Ward rendering (translation_used srcDES021); Arsenius matches no published translation → translation_used honestly unset, gate red documented, license paraphrase-only. FLAG-003 filed (Tier-4 composite owner requiredness). Occasions re-derived for 4-story sample — the Amma-Sarah wrong-occasion class is now data |
| S2.5 | done | G + R | 10 gravity (named six tests, Doc_04 corrections preserved, softest-Primary flag carried) + 12 force records (3 cited layers + NEW Layer 4: 8 elaborations, 4 argued stasis cases); reciprocity 0 across whole graph; validator caught tension-with->competing enum fix (8 edges); world_core.gravities closed; 6 mirrored cross-cell force pairs; 80/80 valid |
| S2.6 | done | G + R | 6 records (one per Primary gravity, SS11 floor); all 5 SS3.7 fields non-empty on each; 7 held_against entries all traced to real contested material (Sarah/elders, Moses/council, tombs assault, Pachomian office model, zeal-vs-moderation, embeddedness record, in-world systematic mode); divergence_partners mapped from the 5 partner Doc_04s read directly; six-shapes probe found+fixed 2 defects in-round (claim003 strand-flattening P1, claim001 undocumented-exchange phrasing P2); 86/86 valid, no new gate violations |
| S2.7 | done | G + R | desertvoice001 (8-field SPEAKING model, 5-trait rubric w/ 12 intensity cells, avoid_traits from documented failures, register evidence = Doc_06 1.8 genre w/ Doc10's DMR caveat verbatim, native measure = runtime 60-word ceiling as data) + 3 demonstrations (the template-required Doc10 S4 exchanges, machine-verified verbatim incl. restored koinonia macron, {{random_user}} convention, honestly scored: all partial on terse economy at 146/164/168 words vs 60); CO-015 checked both directions; coverage gap (5 of 12 cells undemoed) routed to S2.9; 90/90 valid |
| S2.7a | done | G + R | 5 pairing_guidance (Alexandria/scripture, HAL/'ascetic' surface word, IJ/authority w/ the desert's own office-model-inside honesty, Syriac/where-asceticism-lives, boundary-energy w/ Doc_07's pending-confirmation flag preserved) + 6 cautions (2 unperformed freeze-gate reviews, recruitment risk, thin domains, 4-vetted-sayings boundary, logismoi/clinical adjacency); every guidance entry evidence-linked (schema-enforced minItems 1); idempotent in-place world_core update; P3 (Donatism mention at Brief-render) routed to S2.8; 90/90 valid |
| S2.8 | done (no swap) | G+P+P | 6 views staged (chunks near/full round-trip, temporary prompt w/ 19/19 completeness map + 2 GAP COs, capsule section-classified, Brief populated from S2.7a records); render parity 25 classified/0 unclassified; retrieval parity 0 regressions (after FLAG-004 measurement+parking); probe parity 6/7 blind two-trial (FLAG-005 found+fixed via norms completion; claim-laundering divergence = deployed prompt vs its own Doc10 record, routed to S5.2); swap decision deferred to Mark at S2.9 |
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
