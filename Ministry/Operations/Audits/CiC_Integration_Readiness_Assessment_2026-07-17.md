# CiC Integration Readiness & Priority Assessment — 2026-07-17

**Scope:** everything different between `main` and the working branch
(`claude/governance-s10-signal-reconciliation`) — 50 commits, 189 files, ~24,700
insertions — plus the feature-branch work still entirely outside this diff
(Representative Modes, Hosted Tour, Front-End Integration Strategy, Guided Questions
live-validation), already tracked separately as the validation queue. This document
answers: what needs testing (feature-level and integration-level) before merge, what
integration work remains, and what actually matters for the Phase 1 experience.

**Convention:** VERIFIED = tested and the record shows how; ASSERTED = claimed in a
commit message or session note but not independently re-confirmed here; NOT TESTED =
explicitly disclosed as untested by the branch's own notes.

---

## Cluster map (main → branch diff)

| # | Cluster | Files (rough) | Test status | Phase 1 value |
|---|---|---|---|---|
| 1 | Prototype/pilot infra (session caps, transcript logging, onboarding, MOCK_LLM, CORS, TS fixes) | `session_cap.py`, `transcript_logging.py`, `OnboardingScreen.tsx`, `RefreshWarningBanner.tsx`, `mock_llm.py` | VERIFIED (transcript logging, normal-turn path, 2026-07-17) + one KNOWN BUG (frame-breaker/relational-safety turns not captured) | **Required** — a pilot cannot ethically run without consent disclosure + session caps + working transcript capture |
| 2 | Frame-breaker classifier | `nodes.py`, `facilitator_prompts.py`, `main.py` | VERIFIED 12/12 (real frame-breakers + adversarial-but-legitimate questions correctly NOT intercepted) | **High** — prevents the Representative getting drawn into "are you an AI" loops |
| 3 | Acute-Distress/Harmful-Dynamic relational safety | `nodes.py`, `facilitator_prompts.py`, `main.py`, `state.py` | VERIFIED 16/16 direct-call + live end-to-end; **two real bugs found and fixed** (first-disclosure routing, compound-tag parsing). NOT TESTED: multi-world tables, frame-breaker/relational-safety interaction boundary, non-streaming `/message` endpoint separately | **Critical** — this is crisis-response code (Article 33 territory); shipping a pilot without it, or with it silently miscarrying, is a real-harm risk, not a quality issue |
| 4 | Drift monitor / FABRICATION fix + Governance V3.7 | `nodes.py`, governance docs | VERIFIED: misattribution battery 8/8 across 4 worlds, SELF_NARRATION 4/4, tiebreak regression 3/3 | **High** — closes the exact fabrication class (misattributing sayings to real named figures) that produced the worst scandals in the market scan |
| 5 | World #9 (Bethlehem Circle/Albina) install + renames (Amma→Chloe, Post-Apostolic→House-Churches, Hieronymian→Bethlehem Circle) + tile copy | `world_manifest.py`, `data/*_world/`, frontend rename touch-points | ASSERTED — tile copy checked against corpus; Amma→Chloe rename direction applied but **explicitly not independently cross-checked** against the original content-repo rename decision's reasoning | **High** — this is the 4th world going live, real content expansion, not a UX feature |
| 6 | Orchestration/retrieval improvements (retrieval short-circuit, governance off critical path, parallelized retrieval, selector-call skip) | `nodes.py`, `main.py`, `rag/retriever.py`, `rag/story_retriever.py` | ASSERTED — described as fixing specific reproduced problems, no formal test count | **Medium-high** — real latency/quality gains, lower stakes than safety-mechanism correctness |
| 7 | Citation UI migration (bottom list → inline hover/click) | `CitationMarker.tsx`, `CitationModal.tsx`, `LexiconHighlight.tsx` | ASSERTED — implemented; not verified against the Front-End Integration Strategy's own conversation-primacy test | **Medium** — this is Increment 1's required first change per the front-end strategy; worth confirming it actually satisfies that spec now that the spec exists |
| 8 | Frontend UX fixes (multi-world lexicon highlighting, scroll behavior) | `useLexicon.ts`, `TheTable.tsx`, `table.css` | Lexicon highlighting: fixed a real StrictMode bug (asserted fixed). **Scroll fix explicitly disclosed as NOT YET CONFIRMED by live testing** — a prior attempt at the same fix was confirmed broken | **Medium** — visibly annoying if broken in a multi-world table, but not safety-relevant |

**Not in this diff at all** (tracked separately as the validation queue, still needs its own gate before it can even be considered for a future merge):
- Representative Modes (needs Battery A — live-model validation, never yet run)
- Hosted Tour (needs the builder machine built, then Chloe manifest + voice sign-off)
- Front-End Integration Strategy Increments 2-4 (role selection, question serving, map merge — only Increment 1's citation piece has any code yet, via cluster 7 above)
- Guided Questions V1.0 (content review + first live-model validation)

---

## What needs to happen before each cluster can merge

### Priority 1 — safety-critical, blocks any real pilot

1. **Fix the transcript-logging gap (already tracked, task #464/#3).** Both the
   frame-breaker (cluster 2) and Acute-Distress (cluster 3) branches skip
   `write_transcript`. For a pilot whose entire safety/stewardship model depends on
   human review of transcripts, a crisis-adjacent turn being the one thing NOT
   captured is backwards. This blocks calling clusters 2 and 3 "pilot-ready" even
   though their own logic is well-tested.
2. **Test the Acute-Distress mechanism at a multi-world table.** Only ever tested
   single-world. Multi-world tables are explicitly part of Prototype 1's design ("both
   modes" per the Gantt's own task 102) — an untested interaction surface for
   crisis-response code is not acceptable to carry into real testers.
3. **Test the frame-breaker / relational-safety boundary.** The two are coded as
   mutually exclusive with frame-breaker taking priority, but no adversarial message
   was ever built to actually test that boundary. Needs one.
4. **Confirm the non-streaming `/message` endpoint's relational-safety branch
   end-to-end** — it received the same code fix and passed the same unit tests as the
   streaming endpoint, but was never separately exercised live. Low effort, real gap.

### Priority 2 — core content and closed governance loops

5. **Cross-check the Amma→Chloe rename** against the original content-repo decision
   doc (`World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Representative_Rename_Amma_to_Chloe_Decision_2026-07-13.md`)
   — same direction was applied here independently, but never verified to match that
   doc's actual reasoning. Quick check, worth doing before this rename is called
   settled everywhere.
6. **Confirm the frontend's manual metadata copies are in sync** with `world_manifest.py`
   — `MessageBubble.tsx`'s `REPRESENTATIVE_INFO` and `types/conversation.ts`'s
   `SpeakerName` union are disclosed as separate, manually-synced copies (TypeScript
   can't read the Python manifest at build time). A drift here would silently
   misrepresent a world/representative in the UI. One pass to confirm they currently
   agree.
7. **Mark's Governance V3.7 authority ruling** (already tracked, task #5) — the code
   is tested; this is a decision, not a test.

### Priority 3 — real value, needs its own verification pass

8. **Re-run an end-to-end pass across all four (soon five) worlds** for the
   orchestration/retrieval changes (cluster 6) — confirm the retrieval short-circuit,
   parallelized retrieval, and selector-call skip haven't regressed anything, since
   none of them carry a formal test count yet, just fix narratives.
9. **Check the citation UI migration against the Front-End Integration Strategy's own
   conversation-primacy test** — the spec that would grade this change didn't exist
   when the change was made. Cheap to check now that it does.

### Priority 4 — polish, lower risk if it slips a few days

10. **Get one clean live confirmation of the scroll-behavior fix** in an actual
    multi-world table — explicitly disclosed as unconfirmed, and a prior attempt at
    the same fix was confirmed broken. Don't trust it silently.

---

## The actual priority order (combining this diff with the already-tracked validation queue)

1. Transcript-logging fix (unblocks calling clusters 2+3 pilot-ready)
2. Acute-Distress multi-world test + frame-breaker boundary test + `/message` endpoint check
3. Representative Modes Battery A (already the top item in the validation queue — highest-cost, highest-value item not yet in this branch at all)
4. Amma→Chloe rename cross-check + frontend manual-copy sync check
5. Mark's Governance V3.7 ruling (cheap — mostly a decision, code already tested)
6. Orchestration/retrieval regression pass + citation-UI-vs-strategy check
7. Scroll-fix live confirmation
8. Everything still outside this branch entirely: Hosted Tour builder machine, Front-End Increments 2-4, Guided Questions live-validation (all already tracked, all gated behind their own work before they're even candidates)

**What this order optimizes for:** get the safety-critical, already-mostly-tested
clusters (1-3) fully pilot-ready first, since they're the closest to done and the
highest-stakes if wrong. Representative Modes' Battery A is the most expensive single
test (real API cost) and the biggest scope decision (a whole new participant-facing
mode), so it's next rather than first. Everything else is real value but lower risk if
it takes a few more days.

---

*Compiled 2026-07-17 by the System Hub thread, from a direct git diff/log audit of
`main` vs `claude/governance-s10-signal-reconciliation`, cross-referenced against
`cic-poc/docs/engineering-notes/SESSION_NOTES_2026-07-13*.md` and the existing
validation-queue tracking. Nothing in this document has been merged or fixed yet —
it's the plan, not the outcome.*
