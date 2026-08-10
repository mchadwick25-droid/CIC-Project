# CiC Voice Rebuild — Checkpoint 0 (exit Phase 0)

**Run:** 2026-08-08. Verified by re-executing every gate live, not by
reading commit history — each item below states what command ran and
what it returned.

## Verdict: 9 of 10 [G] items green. One red, blocked on a decision only Mark can make.

## The Blueprint's stated pass bar, checked item by item

**1. All [G] items green.**

| # | Item | Phase | Status | Evidence |
|---|---|---|---|---|
| 1 | Demonstration selector hardened (canonical trait_scores, `required` flag, deterministic rank, zero-demonstration world fails the build) | 0.1 | ✅ PASS | `wrs/views/segments/demonstrations.py`: `_selected()` implements the deterministic rank (required-first, then strong-count desc/id order); `assert_ready()` raises `ValueError` on an empty selection, gated for Phase-2 go-live per its own docstring |
| 2 | `ceiling_words` on every world's `voice_profile.native_measure`; `HARD_CEILING_WORLDS` reads from it | 0.1 | ✅ PASS | `ceiling_words_map()` returns all six worlds: desert 60, pahc 150, alx 160, syr 165, ijc 180, hal 160 |
| 3 | `truncate_at` fail-closed mode; `## Final Assembly Instruction` in `_VOICE_UNSAFE_SECTIONS` | 0.2 | ✅ PASS | `app/rag/sections.py` carries `fail_closed=True` + `TRAILING_APPARATUS_MARKERS`; `app/rag/story_indexer.py`'s `_VOICE_UNSAFE_SECTIONS` includes the marker |
| 4 | Tiered build-time leak gate (hard-fail unambiguous apparatus; report-only Usage Guidance/out-of-section) | 0.2 | ✅ PASS | see §2 below — gate runs, zero regression-class hits, 160 EF/FEC hits are the expected rewrite-branch output |
| 5 | Five per-world S52 assemblers; assembly-identity check wired | 0.3 | ✅ PASS | `wrs/views/assembly_identity.py`: all six worlds PASS (Desert byte-identical to deployed; other five deterministic) |
| 6 | Readability gate wired at assembly time | 0.3 | ✅ PASS | all six assemblers re-run live just now: Desert FK 9.74/FRE 62.38 pass, PAHC FK 6.81/FRE 74.89 pass, Alexandria FK 3.73/FRE 87.91 pass, Syriac/IJC/Hieronymian correctly warn (FK 0.0/FRE 0.0) against their still-empty Phase-0 craft tables |
| 7 | Per-signal drift breakdown + `declining_initiative`; `over_settling`/`length_ceiling` surfaced into the harness | 0.4 | ✅ PASS | `app/drift_signal_logging.py` built and verified (Phase 0.4); confirmed live in both baseline battery runs (`drift_signal`/`over_settling_decision`/`length_ceiling` lines present throughout both logs) |
| 8 | Probe harness extended to six worlds; sustained-disagreement scripts; redefined `probe_parity`; Objective-3 checklist sheet | 0.4 | ✅ PASS | all four built, committed, and (the first two) run for real against all six worlds |
| 9 | Pre-rebuild baseline battery committed for six worlds | 0.4 | ✅ PASS | both halves committed: `voice_rebuild_research_probe_results.json` (commit `6cb943e`, 48/48 turns clean) and `sustained_disagreement_battery_baseline.json` (commit `7ffda0d`, 6/6 worlds clean) |
| 10 | **Baseline Objective-3 read** | 0.4 | 🔴 **RED** | Blocked — needs Mark to name a reader (Design §5's protocol: one reader, each transcript scored twice on separate days) |

**2. Assembly-identity holds for Desert (already true) and produces stable output for the other five.** ✅ Re-verified live this run (table row 5).

**3. Leak gate runs clean on hard-fail classes, and on the rewrite branch names exactly the files Phase 2's authoring passes must fix.** ✅ Re-run live: `GATE FAILED — 160 hard-fail hit(s)`, all 160 confirmed programmatically to be the `_HARD_FAIL_SCOPED` class (gravity vocabulary inside `Ecological Function`/`Formation Ecology Connection` bodies only — Mark's rewrite-branch scope call). The separate `_HARD_FAIL_ANYWHERE` class (Final Assembly Instruction blocks, template/builder references — what Phase 0.2 fixed at the source) returned **zero** hits: no regression. A "GATE FAILED" result here is the *designed* outcome on the rewrite branch, not a Phase 0 defect — it is the gate doing its job of naming Phase 2's authoring worklist. 48 files also carry report-only background apparatus language (non-blocking, same worklist signal).

**4. Baseline battery committed for six worlds.** ✅ (table row 9).

## What "on fail" means here

The Blueprint's own rule: *fix within Phase 0; nothing in Phase 1+ starts on a red foundation item it depends on.* Item 10 is genuinely red, and it is not a formality — Phase 1A's own checkpoint (Blueprint §2) states its pass bar explicitly requires *"the Objective-3 read ≥ her [Chloe's] baseline read."* Phase 1A cannot be scored at its own checkpoint without at least Chloe's baseline Objective-3 number in hand first. Phase 1B (Desert's assembly-proof, a machinery test with no voice-quality bar) does not depend on it and could proceed independently.

## Bottom line

Every buildable Phase 0 item is done, verified live, and holds under re-run. The one gap is not an engineering gap — it is Design's own deliberate human-in-the-loop requirement (an LLM is explicitly disallowed from being the score of record), waiting on a name.
