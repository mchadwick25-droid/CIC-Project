# Build Instructions for the Sonnet Implementation Thread

Kicked off per `CLAUDE.md` "Scaling the build": self-governing, auto mode
inside anything converged, escalating only for the named categories. Read
`CLAUDE.md` first; it outranks this document. Read `Adjusted-Design.md`
for the reasoning behind each stage; this file is the actionable plan.

## How to work this plan

**Auto mode for every stage marked NOW.** Do not ask step by step inside a
stage. Run the stage's gates, commit on a feature branch, one PR per stage
(or sub-stage where noted), move to the next NOW stage. Package rebuilds
after `records/` edits and CI/infra mechanical fixes are "just do it."

**Stop and escalate — every time — for:**
1. Any Representative identity/title/voice decision (includes editing any
   `voice_craft` field, any participant-facing Facilitator text, any mark
   label/copy).
2. Any cross-world/portfolio decision (fleet thresholds, exemplar choice,
   fleet-wide record edits).
3. Any governance/methodology change (schema field semantics, L4
   templates, `reference/method/*`, gate posture, anything in the sealed
   classifier's prompt or input shape).
4. An unresolved tension (a test that cannot pass without one of the
   above; a bench regression with no clean fix; three revision rounds on
   one artifact).

Hard stops specific to this workstream:
- **Never add a model call, network call, or new retained-state read to
  the ordinary turn path** (`run_gate`, `_run_ordinary_voice_turn`,
  `assemble_evidence`, `apply_net`, `check_output`, the renderer). If a
  task seems to need one, escalate.
- **Never edit a Representative's generated text.** Checks gate
  decoration and reporting, never words.
- **Never change `engine/m5/live_calls.py` prompts/schemas or what
  `run_gate` passes to `call_safety`** without a ruling and a committed
  full-battery tally.
- **Never self-grant a waiver for a new world** in `engine/m9/enforce.py`
  or `engine/m1/cross_world.py ACCEPTED_OPEN`.
- **No fix on a fix.** Back out and redo.
- **Keep live surfaces clean.** Notes go in this workstream folder;
  per-world gaps in `worlds/<code>/Open_Gaps_Tracking.md` (append-only,
  numbered).

**Workstream home:** this directory. `Decision-Log.md` gets one entry per
PR and per ruling. `Rulings-Pending.md` tracks R1–R19 status — update it
when a ruling lands, never before.

**Scope of this pass: Stages 0–4 only.** Stage 5 (Facilitator safety
mechanism) is removed from the plan entirely — see `Decision-Log.md`
entry 3 — never build it regardless of what any other document in this
directory says. Stages 6–9 are blocked (see `Adjusted-Design.md` §5) and
are out of scope until their rulings or Stage 1's own measurement land.
Do not start them.

**Standing gate set** (before every PR; name the ones run in the PR body):
```
python -m pytest engine/m1/tests engine/tests engine/canon/tests engine/m2/tests engine/m3/tests engine/m4/tests engine/m5/tests engine/m8/tests engine/m9/tests engine/api/tests engine/provider/tests -q
python -m engine.m1.cross_world
python -m engine.m9.cli check
python -m engine.m2.cli staleness-check
python -m engine.m2.cli determinism-check <world>   # any stage touching engine/m2 or spoken_fields
python -m engine.m1.selftest                        # any stage adding/changing a gate
python -m engine.canon.check_seal_isolation
cd cic-poc/frontend && npm run build && npm run lint  # any frontend stage
```
Baseline: 567 passing; cross_world and m9 clean.

---

## Stage 0 — Hygiene and twice-confirmed fixes *(NOW)*

**0a. Concurrent gate calls.** Touches `engine/m4/turn.py` `run_gate()`
(~119–124): run `call_safety`/`call_reader` concurrently (two-worker
`ThreadPoolExecutor`); keep 4s timeouts; append usage records in fixed
order (safety, reader). Confirm the Bedrock client is thread-safe
(httpx-based SDK client is); if not, escalate rather than build a second
client per turn. Done: `engine/m4/tests/test_turn.py` proves both calls
invoked and routing byte-identical to sequential for every existing
scenario; table path inherits via `run_gate`; m4/m5/api green.

**0b. Leave never disabled.** Touches `cic-poc/frontend/src/components/
ChatInput.tsx` (Leave at ~73 must not take `disabled`; only Send does),
`screens/Conversation.tsx`, `screens/TableRoom.tsx` (~154). Done: Leave
clickable during in-flight turns and open rounds in both modes; build +
lint clean. (Server-side round close is Stage 8, out of scope this pass.)

**0c. Round-cap copy at the root.** Touches `engine/api/app.py` (additive
`round_cap` on table session-create/transcript), `wiring.py`/
`table_wiring.py` (source from `engine.m4.round.TABLE_SESSION_ROUND_CAP`),
`types/conversation.ts`, `TableRoom.tsx:144` (render, never type). Done:
`test_table_api.py` asserts the field; no literal round count in `src/`.

**0d. Battery tally + model pin.** Touches `engine/m5/safety_script_run.py`
(`--all` runs every committed batch, prints one tally with resolved
`safety_model_id`; never edit an existing batch), `render.yaml`
(`CIC_API_SAFETY_MODEL_PATTERN` = the full profile id the last tally ran
on; document in `engine/api/README.md`). Done: CLI unit-tested with a fake
client; the live tally is by-hand, credentialed, never CI; tally path in
`Decision-Log.md`. Escalate if pinned id ≠ last tally's id.

**0e. `observe_outside_help_guard`.** Touches `engine/m1/cross_world.py` —
OBSERVATION per world: does `voice_craft.guard` carry don's categorical
outside-help prohibition (`records/don/voice_craft/*.md` ~77–79 is the
exemplar). Done: prints; nothing fails; world list filed under R19 in
`Rulings-Pending.md`.

---

## Stage 1 — D1 grounding measurement *(NOW; gates Stages 6, 7 and R9/R16/R18)*

Methodology is `Adjusted-Design.md` §4, exact. New `engine/m4/reports/
grounding_fooling_measure.py` (same discipline as `retrieval_bench.py`),
reading the live-turn/live-table reports; calling
`engine.m4.grounding_net.check_turn`, `engine.prose.grounding_ratio`,
`engine.m1.loader.load_world_records`,
`engine.m4.evidence.repository_records_by_id`. Corpus A (reproduce +
label 55 withheld + ~120 ok-tagged; one-time Sonnet labeling permitted,
prompt in the docstring, request Mark's 20-item spot-check in the
report), Corpus B (constructed fabrications from guard lines,
`honest_limit.statement`, `contested_claim.claim`, `absent_detail`),
Corpus C (one-shared-word mis-tags). Done: `engine/m4/reports/
grounding-fooling-<date>.json` + `D1_Grounding_Measurement.md` in this
directory with rates by path/world/type, list of passing barred claims,
the provenance-not-truth statement. **Do not** change `WITHHOLD_FLOOR`,
`check_turn`, or any threshold. Present to Mark as an Artifact. Escalate
immediately if labeling shows a live fabrication reached a participant.

---

## Stage 2 — Library and build-process foundations *(NOW)*

**2a. Spoken-field registry.** New `engine/m1/spoken_fields.py`
(`SPOKEN_FIELDS = {record_type: {field: role}}`, roles `voice-diet |
evidence-head | participant-label | instruction`). Rewire:
`engine/m2/builders.py build_prompt()`; `engine/m4/evidence.py
_head_text()`; `engine/m4/citation_cards.py _LABEL_FIELDS`;
`engine/m1/gates.py _PERSPECTIVE_FIELDS`, `_ATTRIBUTION_FIELDS`,
`gate_readability`'s list; `engine/m1/cross_world.py _PARTICIPANT_FIELDS`.
Done: AST test in `engine/m1/tests/` fails on any undeclared spoken-field
read; **compiled bytes unchanged** — determinism-check and
staleness-check green with no repin. Any byte change is a finding, not a
repin.

**2b. Bar screen.** New `engine/m1/bar_screen.py` (`python -m
engine.m1.bar_screen <world>`), reusing `engine/m7/instruments.py`
primitives and `engine/m1/fk.py`; writes `worlds/<code>/build/
bar-screen-<date>.json`. Done: runs on all ten; fixture artifact
committed.

**2c. `register-profile` as OBSERVATION (until R6).**
`engine/m1/cross_world.py observe_register_profile`: per world per spoken
field — median words, longest sentence, fragment ratio, dash density —
against *absolute* ceilings you propose from `reference/method/
CiC_Register_Bar_2026-08-29.md` and `StoryMark.tsx`'s layout; alx/hal
exemplar printed as context. Done: prints for all worlds with hal 21 /
cappadocian 25 / don 34 / gallic 43 visible; ceiling proposal filed under
R6 in `Rulings-Pending.md`. Gate promotion (seeded defect in
`fixtures/seeded_defects.yaml`, grandfathered waivers) only after R6.

**2d. Holdings report (report-only, file grain).** New
`engine/m9/holdings.py` reading `cic/corpus-map/<census_id>.yaml`,
`CORPUS-USE.md` tiers, each world's `source` records; one row per
vendored file (`in_scope`, `named_in_records`, `drawn_on`, `disposition`
from the closed vocabulary). Relocate `COVERAGE`/`REGIONS`/`AUTHORS` out
of `engine/m1/cross_world.py` (~386–407) into a library-side file under
`cic/corpus-map/` read via `engine/m9/loader.py`;
`observe_second_hand_sources` reads `cic/texts/AUTHORS.md`/
`AUTHOR-IDS.yaml`. Done: `python -m engine.m9.cli holdings <world>`;
gallic's 19 unopened volumes show `not-yet-assessed`; nothing blocks.
Gate only after R13.

**2e. Golden sets.** New `engine/m4/reports/bench/{cappadocian,don,
gallic,rzg}.json`, 12–20 questions each, **committed before any Stage 4
change** (RETRIEVAL-HINTS rule 2); baselines appended to
`retrieval_bench.py`'s history. Done: bench reports all ten worlds.

Escalate if the AST seal reveals a provenance field read as spoken text,
or a proposed ceiling would fail a world outright.

---

## Stage 3 — Engine-owned Transparency Plan *(engine half NOW; renderer switch-on BLOCKED on R10 + label copy)*

**3a. `transparency_plan.py`.** New `engine/m4/transparency_plan.py` +
tests; called at the end of `_run_ordinary_voice_turn` in `turn.py`;
stored as `voice_event["transparency"]` — **additive; do not add to
`REQUIRED_KEYS`** this stage. Shape per the CE report §3.2 with
`run_start_sentence`/`run_end_sentence` per run (R10 is a flag),
`repeat: true` on separated re-cites, `world_key` everywhere,
`weakest_confidence`/`confidence` on cards (computed, **not rendered**
until Stage 6), `unverified_claims` for internal reporting only. Done:
completeness invariant unit test (`set(references.record_id) ==
set(all record_ids in citations)`); run/repeat, offset, per-world tests;
`apply_net`, `citations`, `_replay_text`, M3 parity untouched (m3 green);
deterministic for identical input.

**3b. API/projection pass-through.** `engine/api/app.py` (optional
`transparency` on VoiceTurn), `wiring.py`/`table_wiring.py`,
`engine/m4/projection.py` if it filters keys. Done: api green;
pre-change transcripts still load (test it).

**3c. Renderer + tests.** `cic-poc/frontend/src/components/
VoiceTurnBody.tsx` (renderer over `anchors`/`references`; delete the
three dedup rules), `GeneralReferences.tsx` (complete list; propose
label, do not invent), `types/conversation.ts`, `StoryMark.tsx`/
`WitnessMark.tsx` (repeat glyph). Add `vitest` + `@testing-library/
react`, a `test` script, and a `frontend-tests` CI job in
`.github/workflows/ci.yml` gated on the existing `frontend` path filter.
Done: fixtures prove `A, A, B, A` and `1,4,7,10` render every verified
citation; an element-count test enforces the N2 house rule; build/lint/
test clean. **Ship behind a flag defaulting to current behavior until
R10 and label copy are ruled.**

**3d. Gloss gating + `gloss_forms`.** `engine/m4/term_glosses.py`
(ordinary-English forms fire only when the sentence cites the term
record; foreign/technical keep the scan), `engine/m1/schemas.py`
(`gloss_forms` on `term`, additive), `test_term_glosses.py`. Done:
gallic "world/power/brethren/elder/disciple" no longer fire uncited;
Logos/hesychia/allegoria still do; authoring rule drafted and **flagged**
(do not edit `reference/L4-Templates/*`).

---

## Stage 4 — Retrieval, real index, guards *(4c–4f NOW; 4a–4b after R11)*

**4a. The split** *(R11 — do not start until ruled)*. `engine/m1/
schemas.py` (`retrieval.prefer_instead`, envelope `claim_guards`,
additive); **first** add `claim_guards` to `engine/prose.py
_NON_PROSE_KEYS` and `engine/m4/evidence.py _FALLBACK_EXCLUDED_KEYS`
with a test asserting both; Haiku migration tool under `tools/` (pattern
`tools/set_source_kind.py`), one world at a time; `python -m
engine.m2.cli build <world>` + repin; new gate
`retrieval-negatives-structured` with seeded defect; riders in
`render_evidence_block` **inside existing `budget_chars`**;
`prefer_instead` demotes, never excludes. Done: gallic first; bench
equal or better; all worlds migrated; staleness green.

**4b. `guard_proximity` family** *(after 4a)*. `engine/m4/output_check.py`
fourth family; `engine/m7/instruments.py` reads it. Reports, never
edits. Feeds R14 — do not start until 4a is ruled and shipped.

**4c. `retrieval.json`** *(NOW)*. `engine/m2/builders.py
build_indexes()` (~631–675) → deterministic lexical index over registry
spoken fields excluding `_FALLBACK_EXCLUDED_KEYS`/`_NON_PROSE_KEYS`;
`evidence.py` Stage B2 fills only empty slots, capped; `world_loader.py`
if it enumerates indexes; manifest hashes change → repin all. Done:
`assemble_evidence` signature unchanged; determinism green; bench on ten
worlds equal or better; per-record retrievability audit printed,
report-only.

**4d. Tier prior** *(NOW, after 2e)*. `evidence.select_cell_candidates`.
Ships only on no-regression across ten golden sets.

**4e. Option C expansions** *(optional, after 4c measured — may be
deferred past this pass)*. `schemas.py` `retrieval.expansions`; one-time
Haiku per world; new fill tier; `gate_readability` grades them.

**4f. Conversation-aware + return-turn queries** *(NOW)*.
`evidence.assemble_evidence` (`history` already a parameter);
`table_wiring._context_prefix`/`run_voice_turn_for_world` at secondary
weight, scoped to own repository. Done: no new input beyond what is in
memory; budget unchanged; bench + `python -m engine.m4.live_table_run`
(by-hand) no-regression; M8 usage shows no per-turn growth on the
fixture session.

Escalate if any step wants a runtime embedding/network call, a bench
regression has no clean fix, or migration reveals a fourth guard
species.

---

## When to stop and ask — quick reference

| About to… | Do |
|---|---|
| Add any call or state read to the ordinary turn path | Stop. Escalate. |
| Change words a participant reads | Propose in the PR; no merge until Mark words it. |
| Touch `live_calls.py` prompts/schemas or `call_safety` inputs | Stop. Ruling + committed `--all` tally. |
| Edit any `voice_craft`, figure name, or date | Stop. Representative-voice category. |
| Set a fleet-wide threshold | Propose with measured numbers; Mark sets it. |
| Promote an observation to a blocking gate | Stop. Governance. |
| Repin after a records edit, add a path-filtered CI job, add a test dependency | Just do it. |
| Third revision round on one artifact | Stop. Unresolved tension. |
| Build any new Facilitator safety machinery (tiers, decay, memory, output-withholding, per-disclosure messages) | Never. Closed, not deferred — `Decision-Log.md` entry 3. |
| Start Stage 6, 7, 8, or 9 | Stop. Out of scope for this pass — check `Rulings-Pending.md` first. |

---

## Critical files for this pass
- `engine/m4/turn.py` — gate concurrency (Stage 0), plan hook (Stage 3)
- `engine/m4/grounding_net.py` (with `engine/prose.py`) — the check Stage
  1 measures; Stage 4 must keep it clean of guard vocabulary
- `engine/m4/evidence.py` — Stage B2, tier prior, riders within budget,
  exclusion lists
- `cic-poc/frontend/src/components/VoiceTurnBody.tsx` — becomes a tested
  renderer over the engine-owned plan (Stage 3c)

Stage 5 (proposed Facilitator safety-mechanism changes) is removed from
this plan entirely, not deferred — see `Decision-Log.md` entry 3. The
Facilitator's mechanism stays exactly what's already shipped: recognize a
signal, check in, encourage the participant to seek real human help.
Nothing about it is this workstream's to redesign.

**Stage 7b queue — one item, not started.** `Rulings-Pending.md` R42
(ruled 2026-09-23) holds one generation-side item until Stage 7b (the
`CIC_API_STREAMING` engine module) merges: a citation-completeness
directive asking the voice to tag any sentence that draws on a record
even when it names no person, number, or quote. Baseline this item
starts from, R42's own measurement (`Rulings-Pending.md`, `Decision-Log.md`
Entry 61, 2026-09-23): 14 of 40 hand-read sentences on a 22-probe run
were true and record-supported but carried no citation tag. `Decision-Log.md`
Entry 73 (2026-09-24) re-confirmed the hold is still correct as of that
date (no code reads `CIC_API_STREAMING` yet, no 7b PR merged). Starts
after 7b merges, as its own item: propose the directive line, re-measure
the same 22-probe/hand-read method, report the before/after counts and
cost. No enforcement follows either way.

Stages 6–9 (confidence display, streaming, table completeness, fleet
cleanup) are specified in full in the Fable design pass's own report —
ask Mark for it when `Rulings-Pending.md` starts clearing, rather than
guessing ahead of the rulings.
