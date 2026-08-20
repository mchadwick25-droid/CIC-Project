# CiC Build Blueprint — the handoff charter

**Status: DRAFT for Mark's redline, 2026-08-20.** This is the document a fresh build thread launches from. It tells that thread what to build, in what order, under what laws, with what freedom, and when to stop and ask. The design record it executes is `CiC-Program-Spec.md` + Artifacts 1–6, all in this folder, all on branch `claude/cic-redesign-spec-fcjzz6`.

---

## 1. What you are building — and not

You are building the redesigned Church in Conversation: the single-voice interview product — one participant, one Representative voice of an early-Christian world, a Facilitator at door/thresholds/close — on the clean architecture specified here. Purpose above all (O0): *the system exists to reveal Jesus through the witness of his church across history* — as witness, never recruitment.

You are **not** building: the multi-voice Table (separate product, separate thread — you only keep it cheap: mode field, projection-shaped transcripts, per-mode config); voice-position variants (build-time compile targets later); any answer-serving bank (goal kept, mechanism dropped); anything from `cic-poc/` or `cic/` by copying — **the old trees are evidence, never dependencies**. The existing world records are raw material that must pass through the new schema, gates, and canon (nothing grandfathered).

## 2. Reading order (before any code)

1. `CiC-Program-Spec.md` — front to back. §1 (outcomes) and §2 (design principles) bind everything; the full decision history lives in the branch's git log.
2. Artifacts 1–6 — the contracts you implement.
3. Appendix A — Canon v1 (approved seed; scholarly vetting pending).

## 3. The laws (violating any of these is a stop-and-ask, never a judgment call)

1. **Length is observed, never enforced.** No caps, no retries-for-length, no buffering that breaks streaming.
2. **No per-turn quality police.** The live turn = gate + retrieval + generation + deterministic checks + stream. Quality lives in the build and the offline audit.
3. **Prompt = how to speak; records = what's true.** The per-world half of any prompt is a record, never code.
4. **One registry; everything derived.** No world identifier in code. No hand-synced lists, anywhere, ever.
5. **Safety is sealed.** Its call shares nothing with iterated machinery; any change to it triggers the full live safety rerun (19/20 floor). Crisis resources appended by code, never model-recalled.
6. **Fail open toward the pre-guard state, with the direction stated per check — and never silently** (degraded flags, async re-classification for safety).
7. **The participant's words are never rewritten;** directives are code-assembled from schemas, never model-composed.
8. **Honest thinness beats invented depth, absolutely.** Honest-limit answers are the voice's own; the identity-collision framing rule (spoken non-judgment) is canon law.
9. **Generated artifacts verify against their source**: determinism twice in CI, regenerate-and-diff staleness, load-time hash refusal. No hand edits of compiled files.
10. **Thresholds come from baselines, never invented** (Goodhart rule); report-only instruments stay report-only until data earns them a bar; Mark's reading is the register instrument.
11. **Risky substitutions land last and alone** (model/provider switches especially); gate changes go canary-first.
12. **Gate-integrity rule:** a session that needs a gate changed to pass files a flag and stops. Changes to gates are their own reviewed steps.
13. **Cost discipline:** engineered in $/turn; every LLM call attributed to its session; no figure quoted onward until measured on the billing provider (Bedrock today; portability per spec principle 16).
14. **Every commit message carries its reasoning** — this project's commit log is its decision record; keep it that way.

*(Numbering note: laws 1–13 mirror spec principles 1–13; spec principles 14–16 — witness/transparency, scholarly-review aspiration, portability — bind through §1 and the spec directly; law 14 is blueprint-only. Cite "spec principle N" vs "law N" explicitly.)*

## 4. Decision rights

- **The build thread decides freely:** anything marked `DECIDABLE` in Artifacts 1–6 (hosting service, IaC tool, exact re-admission trigger list, jurisdiction counsel timing), library and implementation choices, test structure — each with a recorded reason in the commit.
- **Mark decides (stop and ask):** anything touching §1–§2 or any decided design in the spec; the four world touchpoints (identity, living-tradition, freeze, admission read); canon changes beyond mechanical fixes; anything participant-facing that changes what is promised or disclosed; spending beyond the budget envelope; safety behavior of any kind.
- **Spec amendments:** if reality contradicts the spec, the spec is amended by recorded ruling — never silently worked around. The spec stays the living source of truth through the build.

## 5. The work plan (executes spec §9; acceptance gates verbatim from there)

| stage | deliverable | gate before next |
|---|---|---|
| 0.6 | Fixture world (synthetic, exercises every gate + admission + safety script) | seeded defects enumerated and mapped to the gates that must catch them; the firing and harness proofs land in stages 1 and 4 |
| 1 | M1: schema, registry, gates (Artifact 1) | selftest: pass clean fixture, fail every seeded-defect fixture; inertness reporting fires |
| 2 | M2: compiler (Artifact 2) | determinism twice; staleness CI green; manifest hash verified by stub loader |
| 3 | Canon v1 as records (`_fleet.canon.*` from Appendix A) + sealed held-out admission paraphrases | every cell has sealed probes before any world answers it |
| 4 | M3: admission harness (blind protocol, masked grading, sealed keys) | catches a seeded register defect and a seeded fabrication on the fixture world |
| 5 | M4+M5: runtime core, gate, safety (Artifacts 3–5) | resume across two processes incl. accumulator; entrance-seal test; live safety script ≥19/20 vs fixture world; crisis append asserted incl. empty-stream; lazy load/unload measured |
| 6 | M8: cost instrumentation, on Bedrock first | parity vs raw usage shapes; lapsed-cache-window visible; zero unattributed calls; re-measured cache economics recorded with the band |
| 7 | **Alexandria** through the full world-build process (spec §4) | Mark's four touchpoints; admission passed; build cost + defect list recorded. Then Desert (the honest-limit proof) |
| 7.5 | **Experience design (the pass we almost skipped).** Flows and mockups for the participant journey — the three access points (landing page with the scrolling Representative gallery; the "Start an interview" program page of detailed world cards; Atlas deep-link arrival), the detailed world card/doorway (portrait, disclosure, thinness, starters, launch), conversation view (stream, status line, code), the three-tier transparency interactions on desktop *and* touch, the safety turn as it looks and feels, the close, the methods page; plus the visual identity decision (align with the existing public site or its own). Designed as screens, mobile-first, before any M6 code. Runs in parallel with stages 5–7. | Mark approves the screens — the experience gets the same redline discipline as the spec; nothing in M6 is invented while coding |
| 8 | M6: participant surface built to the approved designs (spec §6 content + stage 7.5 screens), including the **Atlas connection**: census_id in the registry, the open-worlds view/API for the public site, "speak with this world" deep links from Atlas entries to world doorways, honest "not yet built" state for unbuilt entries | every §6 item demonstrable; screens match the approved designs; an Atlas entry deep-links into a doorway end-to-end; Artifact 5 contract tests green |
| 9 | M7: transcript audit pipeline (priced; daily cadence; lineage index for deletion) | full suite runs over pilot transcripts at batch rates; a finding routes to a record fix; a real question enters the canon |
| 10 | Doors open: pilot with informed testers (spec §8 pilot rules: informed, adult, prototype status disclosed) | public availability waits on the two safety gates (live adversarial trials; clinician read) |

Progress discipline: one stage at a time; a stage's gate is evidence in the repo (reports, transcripts, measurements), not an assertion. Status to Mark at every stage boundary and every stop-and-ask.

## 6. Landmines (the archaeology's top recurrences — treat these as tests to write)

Silent relabeling (an unknown enum value mapped to a default) · hand-synced lists drifting (see law 4) · a permanently-red guard everyone scrolls past (a red check must block or be deleted) · a guard pointed at the wrong tree · a builder with a `--check` nobody runs (regenerate-and-diff instead) · a 0% fire rate read as health without a deployed-since check · instruments measuring the path that doesn't ship (test the streaming path) · discarding half a graded judgment (keep NOT_USED with its reason) · a stale comment claiming coverage that doesn't exist · duplicated logic fixed in one copy · cost split by model name instead of call label · streaming usage fields silently absent (Bedrock client rules, spec §7).

## 7. Handoff mechanics

- Work on a fresh branch cut from `claude/cic-redesign-spec-fcjzz6` (e.g. `build/phase-1`); the spec folder travels with it; spec amendments happen in the same PRs as the reality that forced them.
- Mark's operational roles: source-request manifests (fetching archive texts), the four touchpoints per world, stop-and-ask rulings, budget approvals.
- The project's governance documents (the L0–L4 folders and Ministry/ in the repo) and the old code trees remain read-only context; the containment discipline applies: state a past incident's general lesson when useful, never its internal identifiers (world, defect, revision), so fresh review threads stay unprimed.

**Definition of done for this charter:** stage 10 reached — Alexandria and Desert open to informed pilot testers, every gate green, cost measured and attributed on Bedrock, the audit loop demonstrably feeding fixes back into a world build.
