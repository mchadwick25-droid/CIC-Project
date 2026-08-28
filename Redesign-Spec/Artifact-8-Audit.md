# Artifact 8 — The Transcript Audit (M7)

**Status:** contract for the stage-9 build, written 2026-08-28 at the start
of that build (the same pattern as Artifact-7: the contract precedes the
code, and the code cites the contract). Governed by CiC-Program-Spec.md M7
("owns: quality after the door") and §Instruments; ops posture from
Artifact-6 (PII, deletion lineage, cadence).

## §1 What M7 is, and is not

M7 is the offline batch reader of everything the runtime already writes.
It runs over the durable event log at batch rates, computes the instrument
suite per session and per fleet, and produces **findings that route to the
world build and to admission re-runs — never to live patches** (spec:
"a quality problem is always fixed in the world build, never patched
live"). It creates no new runtime path, makes no live-conversation
decision, and holds no state the event log doesn't already hold.

M7 is also the module that pays a standing debt: four safety/audit
outputs have been computed on every live turn and read by nothing —
`voice_turn.grounding` (per-sentence net verdicts),
`voice_turn.do_not_voice_violation` (content licensing),
`voice_turn.output_defects`, and `round_closed.governance`. The 2026-08-28
foundation audit named them ("dead code that looks like a safety check is
worse than no code at all") and ruled they stay because M7 was coming.
This artifact is where they acquire their reader.

## §2 Inputs

One input: the M4 event log (`engine.m4.store.Store`), read-only, plus the
registry for world metadata. The audit never talks to a model provider in
phase 1 (see §5) and never writes to the event log. `Store.list_session_ids`
is added for the batch sweep; `--since` filters on the log's own
`created_at`, which is what makes a daily cadence a query, not a scheme.

## §3 The instrument suite — phase 1 (deterministic, report-only)

Principle 10 governs everything here: **report-only instruments stay
report-only until data earns them a bar.** Phase 1 instruments are
deterministic — no model calls, no spend, safe at any cadence. Each
finding carries a severity from a three-word vocabulary: `defect`
(something the build must fix), `review` (something Mark or a build
thread should read), `info` (a tracked tendency).

1. **Unread-output surfacing** — every `do_not_voice_violation` (defect),
   every `output_defects` entry (review), every net-withheld sentence and
   `degraded_by_net` turn (info, with the implicated record tags), read
   from the events where they have always been written.
2. **Fabrication / isolation surface** — a citation whose world prefix is
   not its speaker's world (defect; the battery's isolation sweep, now
   running over every real session), and unresolvable-tag counts from the
   net verdicts (info).
3. **Register, mechanical half** — per voice turn: Flesch-Kincaid grade
   and Flesch Reading Ease (the spec's two-move split is reported
   whole-turn in phase 1; the split itself needs the plain/grounding
   boundary, a phase-2 refinement), first-sentence-answers-first-ask as a
   content-word overlap ratio (spec: "first sentence answers the first
   ask" — mechanical check), and turn length. All info; short segments
   report as `unscored`, never as clean (spec §Instruments).
4. **Ask-coverage** — each reader ask vs the responding turn(s), as
   content-word overlap; asks that drew no coverage are review findings.
5. **Repetition** — repeated 8-grams across one voice's turns within a
   session (info; a tendency count, not a bar).
6. **Safety review** — every safety turn is listed; the specific pattern
   the spec names — **intervention followed by abandonment** (a safety
   turn after which the participant never speaks again and the session
   was not closed by cap) — is a review finding, always.
7. **Story/quote offer rates** — per session and fleet, from citation
   record types (the id's own type segment), the per-cell half deferred
   to phase 2 with the cell attribution it needs.
8. **Encounter-openings** — personal_wound-register messages counted,
   with what followed (voice turn / safety turn / abandonment) (info).
9. **Governance rollup** — dominance flags and round-close reasons from
   `round_closed.governance` across all table sessions; selector
   `degraded` counts (review when nonzero).
10. **Question-canon growth** — reader asks, normalized and counted
    across sessions; recurring asks become canon candidates for Mark
    (spec stage 9: "a real question enters the canon"). Participant-
    authored text: operator-only file, never in the fleet rollup (§4).

## §4 Outputs, PII, deletion lineage

Three outputs per run, all under an output directory the operator names:

- `sessions/<session_id>.json` — the full per-session audit (operator-only:
  contains participant text by necessity, same access posture as the event
  log itself, per Artifact-6).
- `fleet-rollup.json` + `fleet-digest.md` — aggregates and findings with
  **no participant text**: session ids, world keys, voice-text excerpts and
  record ids only. This is the shareable/reviewable layer.
- `canon-candidates.json` — recurring participant asks (operator-only).

**Deletion lineage** (spec §8): every derived file names the session_ids
it was computed from, so a deletion request is a grep, not an
archaeology. Deleting a session = delete its events (the store's own
path, still to be built in the retention stage), delete
`sessions/<id>.json`, and re-run the rollup — the rollup's lineage list
proves the recomputation covered it.

## §5 Deferred to phase 2, deliberately (declared, not hidden)

- **Model-assisted instruments** — register judgment beyond mechanics,
  distinctness drift, batch convergence in the battery's lineage. Each is
  real spend under Mark's per-run authorization, and each threshold waits
  on phase-1 baselines (principle 10). The battery's own convergence
  check (engine/m4/live_table_battery.py) is the seed.
- **The two-move readability split and per-cell offer rates** — both need
  attribution phase 1 doesn't compute (plain/grounding boundary; ask→cell
  mapping). Reported whole in phase 1, split in phase 2.
- **The learning corpus and vetted-answer bank** — spec keeps the goal and
  bars a runtime serving path in Phase 1; nothing here builds one.
- **Retention/TTL and the deletion writer** — scheduled with the Postgres
  stage (foundation audit move 6), not here; §4's lineage is written so
  that stage has something to compute over.

## §6 Cadence and routing

Daily, over sessions since the last run (`--since`), plus on-demand over
everything. A `defect` finding opens a record fix in the world build and —
when the fix lands and the world's records materially change — the
existing staleness/admission machinery already forces the re-run
(Artifact-2 §4); M7 adds nothing to that path except the finding itself.
Findings name record ids wherever the evidence does, so the route from
finding to fix is a lookup, not a search.
