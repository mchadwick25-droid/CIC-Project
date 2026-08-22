# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: all seven worlds built; the M4 live-generation pipeline is implemented end-to-end

2026-08-22, this thread. Two large bodies of work, both real, both
verified against real compiled data (never a live model call unless
named below), neither a numbered stage in the original build order
(CiC-Program-Spec.md §9) because neither was foreseen at that table's
own writing - the first is six more worlds' worth of the table's own
stage-7 work, done in parallel across sibling sessions rather than
sequentially in one; the second is new engineering Mark's own review of
the fleet exemplar transcript ("is this being generated out of our
system only... we need the system doing 100 percent of the work")
called into being mid-build.

### All seven worlds now `built` on `build/phase-1`

Alexandria (`alx`), Post-Apostolic House-Church (`pahc`), Hieronymian
Ascetic-Literary (`hal`), Syriac (`syr`), Imperial-Juridical (`ijc`), and
Desert Monasticism (`desert`) all merged into this branch and ran the
real step-6 compile pipeline (`determinism-check` → `build` →
stub-loader verify → registry update → `staleness-check`) - `state:
built` for all six, same mechanical, gates-green semantics `fix`'s own
entry has always carried. The "Alexandria is a separate track on a
separate branch" framing immediately below this section is now
obsolete, kept only as historical record of how that thread's work
reached this one - see the closing note appended to it.

Two real defects found and fixed during these merges, worth keeping
named:
- **A genuinely stale Alexandria package.** `world/alexandria` predated
  this session's own M4 compiler changes (the fleet preamble, demo
  tagging - both below); merging it in without recompiling would have
  shipped a compiled prompt missing both. Caught by the M2 staleness
  sweep before it was committed, not after.
- **`records/worlds.yaml`/`cic/texts/README.md` merge conflicts** on
  every one of these merges except Desert's own (its thread had already
  merged `build/phase-1` in ahead of its PR) - resolved by keeping every
  world's own registry block side by side and regenerating the README
  via its own generator (`cic/engine/texts_registry.py
  --write-readme`), never hand-merged.

Desert's own build additionally closed a real, honestly-named gap before
merging: Doc_09c §4 had flagged a living-tradition-differentiation review
(does the compiled content ever conflate this world's 320-430 CE
reconstruction with present-day Coptic Orthodox/other living monastic
practice?) as required and unperformed. This thread ran that check
directly against every compiled-facing field - clean, zero genuine
instances - and Desert's own build thread independently re-ran the
identical check against their own branch and got the same result before
merging. Doc_09c's own text was corrected via a dated addendum, not
rewritten, per this build's own standing convention. External Scholarly
Review (Doc_09c §4's other named freeze-eligibility gate) remains open -
needs an actual patristics/late-antique-monasticism specialist, not
something any thread can substitute for.

### The M4 Live-Generation Design - designed, signed off, fully implemented

Design doc: `engine/m4/LIVE-GENERATION-DESIGN.md` (written on
`claude/cic-design-assignment-ecoxh2` against the real alx package,
merged into this branch's own history via the implementation below). Its
own four forks (sentence-gated streaming; in-voice honest-limit
degradation; lexical-first retrieval; report-only ratio-floor
promotion) are **signed off, final** (§9.5) - checked against real,
populated data across all five worlds built at the time, not just alx's
own original test case. §9.6 (model tiering: Haiku for
safety/reader, Sonnet for voice generation carrying in-band citation
tags, the old separate citations call eliminated) is explicitly
**provisional/TEST**, Mark's own empirical call pending real cost/quality
measurement - not locked the way §9.5 is.

Every row of the design's own §7 build map is now built:

- **`engine/m4/grounding_net.py`** - the deterministic per-sentence
  citation-tag verifier (promoted from the design's own prototype) plus
  `scope_completion` (the tension-record anti-conflation walk - the
  door-line fabrication's systemic fix, not just a patch).
- **`engine/m4/evidence.py`** - Stages A-E of evidence assembly (asks →
  canon cells → ranked candidates → tension completion → thin-topic
  riders → session exclusion), verified against real IJC/PAHC data: a
  real authority-contest question correctly matches its cells, pulls in
  the right gravity/quote/story records, and a genuinely off-canon
  message correctly resolves to an empty block rather than a forced
  nearest-cell match.
- **`records/_fleet/fleet_voice/`** - the new fleet-owned record
  (register statements, pronoun rule, citation contract, limit
  discipline) that lets `engine/m2/builders.py` compile one fleet
  preamble segment into every world's prompt, replacing what was
  duplicated six times across each world's own `voice_craft`.
- **`engine/m4/generation.py` + `engine/m4/turn.py`** - the old two-call
  shape (stream, then guess citations after the fact) is gone. One call
  now carries its own inline `[[record.id]]` tags; the real net checks
  them before any of the turn's text is treated as the answer;
  withheld sentences degrade to the matched cell's own honest_limit
  statement (or a fleet floor line, same "appended by code" precedent as
  `crisis_resources.py`) rather than ever regenerating or being
  human-edited.
- **`engine/m3/generation.py`** - `LiveModelAnswerer` is real now, not
  the `NotImplementedError` seam it was: the identical evidence-
  assembly + one-call + net pipeline, pointed at a sealed probe instead
  of a live participant message, safety/routing skipped outright (a
  sealed probe already IS the ask). `engine/m3/harness.py`'s
  `run_battery` gained an `answerer=` param so a real one can run
  through the same battery/masking/grading pipeline once someone with
  spend authorization builds and passes one - **nothing in this build
  has yet made a real call through this path**, matching the same
  spend-authorization discipline the safety script and generation
  calls above were run under.
- **Demonstration citation tagging** (`engine/m2/builders.py`) - the
  design's own §5.3 assumed tags could be derived from a demo's
  `sources` field; a real-record check found that field points to
  bibliographic editions, never the records a demo actually draws on.
  Built the direct alternative the design itself recommends elsewhere
  for this shape of gap: score each demo sentence against its own
  cell's candidate records, tag only what clears the floor. **A real
  false positive found and fixed before this shipped**: an early version
  scored against a record's full text (including its own uncompiled
  provenance/analysis prose) and mistagged a martyrdom sentence to an
  unrelated term purely from incidental word overlap in that trailing
  text - fixed by scoring against compiled-facing head text only, plus a
  minimum-shared-word floor; locked in with a committed regression test.

A real layering bug surfaced and fixed mid-build, worth naming the way
this file already names the entrance-seal false-positive and the
never-requested-caching bug above: moving the quote-aware sentence
splitter and a new lexical-overlap scorer down into
`engine/m1/gates_experimental.py` (so both M2's compile-time demo
tagging and M4's live evidence ranking could use them without M2
importing M4, which would reverse the pipeline's real dependency
direction) picked a name, `_grounding_ratio`, that collided with a
pre-existing, differently-shaped function already living in that file -
silently shadowing it and breaking every caller of the real one. Caught
by the test suite immediately, renamed before anything using the real
function could regress.

Full engine test suite: 172/172 passing (up from 123 at the top of the
stage-6 entry below). No live model call anywhere in this body of work -
every verification ran against fake/synthetic clients or real *compiled*
data, never a real API call.

### The glossary/story/quote retrofit - designed, now ENFORCED

`Redesign-Spec/Glossary-Story-Quote-Template.md`: the standard every
world thread retrofits its `term`/`story`/`quote`/`gravity`/`force`
records against, once every world clears its own content canon - that
condition is now met for all seven. Mark authorized flipping the switch
(2026-08-22): `engine/m1/gates.py` gained `distortion_risk`/
`modern_contrast`/`modern_lens_note`/`classification`/`matrix_cell` in
`COMPLETION_REQUIRED`, plus a dedicated `gate_glossary_retrofit_complete`
for the two fields a flat completion list can't express correctly
(`false_friend`'s own typed-empty-list "none identified" state; the
nested `senses.translational` path). `fix` (the CI fixture) is already
retrofitted directly - engineering-owned, not one of the six content
threads' own work. Every other world now honestly shows its real,
current retrofit scope in its own compiled `validation/gates-report.json`
(alx 62, hal 67, pahc 52, ijc 59, syr 55, desert 56 findings) - not a
regression, the real remaining task. **The task itself is drafted and
ready to send to all six threads but has not yet been dispatched** - the
one concrete next action this file should flag for whoever picks this up
next.

## Also: this thread now owns Alexandria from step 5(e) forward

2026-08-21, authorized by Mark: the Alexandria world-build thread
(branch `world/alexandria`, a sibling session) handed off Alexandria's
build to this thread once its own steps 1-5(a-d) closed (source ecology,
ecology reconstruction, canon answered 28/28, voice-craft foundation).
Full detail lives on that branch, not here - see `world-build-docs/alx/
HANDOFF-TO-BUILD-THREAD.md` (the authoritative handoff doc, still
accurate for steps 1-5(a-d) and Mark's four recorded rulings) and this
thread's own follow-on commits on `world/alexandria`: `6d9ce55`
(texts_registry.py ported, README regenerated for real), `5c2fcea`
(census_id set - verified against the real Atlas frontend's actual
deep-link code, not the spec's own illustrative example format), `6f857cb`
(step 6 official compile: determinism-twice, real package built and
stub-loader-verified, `state: building -> built`).

Still open on that branch, in order: the fleet exemplar transcript (a
fleet-wide voice-craft artifact, not Alexandria-specific - flagged for
Mark's steer before drafting, not started); step 5(e) voice validation +
step 7 admission (needs the M3 harness on a live model - real spend,
paced with Mark same as the safety script, not started). This thread's
own stage work (M1-M8 above) and Alexandria are two separate tracks on
two different branches - this section exists so a reader of this file
alone knows the second track exists at all.

**SUPERSEDED, 2026-08-22 - kept as historical record, not current
state.** The fleet exemplar transcript this section names as "not
started" was drafted (`fleet-voice/EXEMPLAR-TRANSCRIPT.md`) and became
the direct occasion for the M4 Live-Generation Design (see the top
section of this file) - Mark's own read of it ("is this being generated
out of our system only... we need the system doing 100 percent of the
work") is §0 of that design doc, verbatim. `world/alexandria` itself
merged into `build/phase-1` and ran the real step-6 compile - see the
top section; it is no longer a separate track on a separate branch.
Step 7 admission for Alexandria (and every other world) is still real,
unstarted, live-model-spend work reserved for Mark's own go-ahead -
that part of this section is still accurate.

## Previously: stage 6 DONE — M8 cost & observability, all four gate items proven with real evidence (parity vs. raw usage shapes; zero unattributed calls; cache economics re-measured and recorded with the band; a lapsed cache window visible in the numbers)

**Stage 6 (M8: cost & observability) — done, commits `dad8448` +
`075f09e`.** `engine/m8/`. The stage-6 gate (CiC-Program-Spec.md §9): *"parity
against raw usage shapes; a lapsed cache window visible in the numbers;
zero unattributed calls; cache economics re-measured and recorded with the
band."* All four, real evidence:

1. **Parity against raw usage shapes** — `engine/m8/parity.py`
   (`check_parity`/`assert_parity`), wired *inline* into
   `engine.m4.turn`'s attribution path rather than run as a separate
   occasional check: every real call this session's turn loop makes is
   parity-tested at the moment its usage is logged, so a provider
   response-shape drift would raise immediately on any real turn, not
   surface later as a quietly-wrong number.
2. **Zero unattributed calls** — `engine/m8/usage.py` (`UsageRecord`
   requires a real `session_id` at construction; `SYSTEM_SESSION_ID` is
   the explicit tag for non-session/evidence calls, never a blank
   fallback) + `engine/m8/log_store.py` (SQLite, same idempotent-append/
   any-instance-serves-any-session pattern as `engine.m4.store.Store`).
   Live evidence: `engine/m8/reports/live-attribution-report.json` — a
   real ordinary turn through the actual M4 turn loop, 4 calls (safety,
   reader, voice generation, citations), `zero_unattributed_calls: true`.
3. **Cache economics re-measured and recorded with the band** —
   `engine/m8/cache_economics_measure.py`, real Bedrock run:
   `engine/m8/reports/cache-economics-report.json` — a cache write of 4202
   tokens, then 3/3 repeated reads identically 4202 tokens (deterministic,
   `mechanism_confirmed: true`). Re-confirms the write/read caching
   mechanism itself still engages correctly under the new lazy-loading
   architecture (the old 16× pooling figure was explicitly flagged as
   stale — Artifact-6 §1 — this is that re-measurement, at the token
   level; no dollar figure computed, principle 13).
4. **A lapsed cache window visible in the numbers** —
   `engine/m8/lapsed_cache_window_measure.py`, two real phases 71.7
   minutes apart (genuinely past Bedrock's 1h ephemeral TTL, not asserted
   from the documented value): `engine/m8/reports/lapsed-cache-window-
   report.json` — the check call, reusing the identical saved system
   prompt, shows a *fresh* cache write (6002 tokens again, same as the
   original write) with `cache_read_input_tokens: 0` — a miss, not a hit.
   `window_lapsed: true`.

**Real finding, fixed as part of building this instrumentation:**
`engine/m4/generation.py`'s `stream_voice_turn` never actually requested
prompt caching at all — `system` was passed as a plain string, not the
structured `cache_control` shape `engine/provider/preflight.py` had
already proven works. Stage 5's turn loop was silently paying full
input-token price on every call; "zero cache fields" would have read as
"nothing to instrument" rather than "caching was never requested." Fixed
(structured system block + `cache_control: ephemeral`) and confirmed live
— the fixture world's own compiled prompt now shows a real 1168-token
cache write on an ordinary turn (`live-attribution-report.json`).

**Also landed:** `engine/m5/failure.py`'s `CallOutcome` gained an optional
`raw_usage` field (backward compatible) so every real call's SDK usage
object is carried through, not re-derived; `engine/m8/cost.py` defines the
$/turn unit's *structure* (`PriceTable` + `estimate_cost`) but ships no
default price table and no dollar figure — principle 13 stays intact,
`estimate_cost` returns `priced: False` until a Mark-approved, sourced
table is supplied (the AWS invoice reconciliation preflight's third leg
still names as pending). `TURNS_PER_HOUR_CONVENTION = 12` defined once.
CI: new `m8-cost-observability` job, mocked-only (24 hermetic tests:
usage, log store, parity, cost, summary), same no-live-call discipline as
`provider-seam-unit-tests`. `engine/m4/requirements.txt` gained `boto3`
(`turn.py` now pulls in `engine.m8.parity` → `engine.provider.bedrock`
transitively).

Full engine suite: 123/123 passing.

## Previously: stage 5 DONE — all five gate items proven with real evidence (resume across two processes; entrance-seal test; live safety script ≥19/20; crisis append incl. empty-stream; lazy load/unload measured)

**Bedrock preflight — done, commit `7cfeda7`.** `engine/provider/` (seam +
preflight, commit `bde1ea7`) run for real against Mark's live account
(468683594478, us-east-1, `cic-bedrock-dev` IAM user scoped to 5 `bedrock:`
actions only). All three required legs green:
`engine/provider/reports/preflight-report.json` - model resolved (not
guessed) to `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, cache write
confirmed (4202 tokens), cache read confirmed on the very next call (same
4202 tokens, not rewritten), streaming usage shape confirmed carrying cache
fields too (the specific silent-absence risk spec SS10 names). Invoice
reconciliation (the preflight's third leg) still pending - AWS billing data
lags; no $/token figure exists or is quoted anywhere yet, per spec
principle 13.

Credential handling note for whoever picks this up: the AWS access key was
pasted directly in chat (after two other delivery paths - session env vars,
a `.env` file created outside this container - failed to actually reach
this session's filesystem/process). It lives in a local, gitignored `.env`
here, never committed, never printed by any script. Mark was advised to
rotate/delete this key once live-model dev work is further along, since a
chat-pasted credential is a weaker channel than the ones tried first.

**Live safety script — s1-s23 run for real across 6 batches, commits
`b3d54a5`..`691473d`.** `engine/m5/live_calls.py` (Call A/B, forced tool-use,
Haiku-class) + `engine/m5/safety_script_run.py` (BATCH_1..BATCH_6, paced 2-5
scenarios per run at Mark's explicit request, each batch immutable once run
- a later fix re-verifies under new scenario ids rather than editing an
earlier batch's graded record). Reports: `engine/m5/reports/safety-script-
run-{1..8}.json` (runs 1-2 were infrastructure-blocked, see below; 3-8 are
real graded batches).

Three real findings, each found by live testing, reported to Mark with
options, fixed only after his ruling, then reverified under new scenario
ids (never by silently patching and re-grading the same scenario):
1. **`acute_level` bleeding into non-`ACUTE_DISTRESS` signals** + reader
   `system_nature` over-firing on relational statements — both prompt-
   clarity fixes, batch 2 (commit `0a3c87c`), reverified 5/5 same batch.
2. **Routing gap:** `AMBIGUOUS_LOW_CONFIDENCE` fell through to ordinary
   routing instead of any safety-aware handling (batch 2 scenario s9, an
   adversarial hypothetical-framed disclosure). Mark's ruling: a new
   `check_in_turn` route, ranked above `system_nature`/bridge/etic, below
   the two hard `ACUTE_SIGNALS` (commit `75b794c`). `Artifact-4-Gate-
   Contracts.md` §3 updated to match.
3. **`risk_subject` missing from Call A's schema:** a third-party crisis
   disclosure ("my brother has been talking about not wanting to be here
   anymore") was scored `ACUTE_DISTRESS` as if it were the participant's own
   risk (batch 3 scenario s12). Mark's ruling: add `risk_subject` ("self" |
   "third_party" | "not_applicable") to Call A's schema (commit `665885f`);
   doesn't change routing, carried into the routing reason for the eventual
   safety-turn content and audit trail. `Artifact-4-Gate-Contracts.md` §1
   updated.
4. **`HARMFUL_DYNAMIC_SIGNAL` over-triage on enthusiasm alone:** a message
   describing the conversations as enjoyable but explicitly *alongside*
   real other supports (therapy, friends) still fired the dependency signal
   (batch 5 scenario s20). Mark's ruling: tighten the prompt so stated other
   supports weigh against the signal, as a weigh not an override - an
   adversarial re-check (mentions a therapist AND real confidant-exclusivity
   language) confirms real dependency still fires (commit `691473d`).

Net: the original s1-s20 run graded 18/20; both misses (s12, s20) are now
root-caused, fixed, and reverified (batch 4's s16/s18, batch 6's s21/s22/s23)
- **current code clears the spec's ≥19/20 floor.** No outstanding safety-
script findings as of this note.

**Real generation call, crisis-append, lazy load/unload — done, commit
`230a331`.** The last two stage-5 gate items, proven with real evidence:

- `engine/m4/world_loader.py` (`LazyWorldLoader`): lazy on first `load()`,
  a resident world is a cache hit not a second disk read, `unload()`
  actually evicts. `engine/m4/lazy_load_measure.py` run against the real
  committed fixture package: cold load 1.8ms, warm (cache hit) 0.0008ms,
  unload ~1μs, cold reload 1.6ms (proves unload wasn't a no-op). No model
  call - `engine/m4/reports/lazy-load-report.json`, `mechanism_proven:
  true`. Fixture-scope only (312K total) - proves the mechanism, not
  production latency at real-world scale.
- `engine/m4/generation.py` (real Sonnet-class streaming voice call +
  forced-tool-use citations follow-up) + `engine/m4/grounding.py`
  (deterministic, explicitly-narrow grounding checks - same discipline as
  `engine.m3.grading`'s `register_check` - plus an independent hard check
  that a do-not-voice-licensed quote never appears verbatim) +
  `engine/m4/crisis_resources.py` (`append_crisis_resources_turn` - a PURE
  function, no client, whose output never depends on stream content, only
  on signal; the literal hermetic proof point for "crisis append asserted
  including the empty-stream case") + `engine/m4/turn.py` (wires M5's
  already-proven gate/routing/failure onto real generation; only
  `voice_with_directive`/`voice_pass_through` and `safety_turn` for
  `ACUTE_DISTRESS` get full content - every other routing outcome raises
  `UnhandledRoutingAction`, a named, deliberate seam, same pattern as
  `engine.m3.generation.LiveModelAnswerer`).
- `engine/m4/live_turn_run.py` run against real Bedrock + the real fixture
  package: an ordinary turn (real citations - one correctly demoted to
  `consulted` when the model's paraphrase didn't literally contain a
  record's own words, the grounding check working as designed), a crisis
  turn with a real non-forced stream, and the forced-empty-stream case for
  direct comparison. `engine/m4/reports/live-turn-report.json`:
  `crisis_append_proven: true` on both. Non-blocking observation for
  Mark: the voice model independently recalled similar crisis resources
  unprompted in the real-stream case - not a violation (the code-owned
  append is the actual guarantee, present either way), just worth knowing.
- CRAFT NOTE carried in `crisis_resources.py` itself: the resource text
  (988, Crisis Text Line) is a real, standard, publicly-published baseline,
  explicitly flagged as a placeholder pending Mark's craft/legal review
  before any world that actually opens ships this literal text.
- Hermetic tests (fake client / no client at all, no live call):
  `test_world_loader.py`, `test_crisis_resources.py`, `test_grounding.py`,
  `test_turn.py` (includes a genuinely-empty-stream case via a fake client
  yielding zero chunks, not only the `force_empty_stream` test hook).
  `engine/m4/requirements.txt` (new) + CI: `m4-event-log` job now installs
  it instead of `m1`'s, since `test_turn.py` pulls in `anthropic`
  transitively via `engine.m5.live_calls`.

**Deliberately out of scope, not stage-5 gate items:** Track B's own
`safety_turn` content (`HARMFUL_DYNAMIC_SIGNAL`), `check_in_turn`/
`system_nature_turn`/`bridge_turn`/`etic_turn` generation content, and the
full HTTP/SSE API layer (Artifact-5 - M6's job, a separate module). Each is
a real, tested routing outcome with no Facilitator-authored turn content
built yet - `UnhandledRoutingAction` names the gap loudly rather than
hiding it.

Spend note: this required real, repeated Bedrock spend - checked pace/scope
with Mark before running it, same as the safety script. The AWS Budget
Action (deny-policy backstop) still isn't in place; Mark's earlier call to
proceed on the $20 alert-only budget + free-plan credit ceiling stands.

**Credential rotation still outstanding:** the AWS access key
(`cic-bedrock-dev`, account `468683594478`) is still the one pasted directly
in chat (see below) - now well into live use across the preflight and six
safety-script batches. Rotating/deleting it once this phase of dev work
slows down is still the right move, recorded here again so it isn't
forgotten now that "further along" has actually arrived.

**Stage 0.6 — done, commit `75278a2`.** Fixture world, fixture-scope 8-cell
canon subset, `fixtures/seeded_defects.yaml`.

**Stage 1 (M1: schema, registry, gates) — done, commit `440cc15`.**
`engine/m1/`. Evidence: `engine/m1/reports/selftest-report.json`.

**Stage 2 (M2 compiler) — done, commits `dcac649` + `159044c`.**
`engine/m2/`. `records/worlds.yaml` fix entry: `building → built`.

**Stage 3 (Canon v1 + sealed admission paraphrases) — done, commits
`db1925b` + `2846d53`.** `records/_fleet/canon_question/` (86 records, 28
cells), `canon/sealed_probes/` (28 sealed paraphrases + isolation guard).

**Stage 4 (M3 admission harness) — done, this commit:**
- `engine/m3/protocol.py` — the battery: the 28 sealed probes, center-first
  draw order (canon maintenance rule 5).
- `engine/m3/masking.py` — the blind-protocol boundary: a `MaskedTranscript`
  TypedDict is the only shape any grading check accepts; `assert_blind()`
  raises on anything carrying `world_key` or `paraphrase_of`.
- `engine/m3/generation.py` — `FixtureRecordAnswerer`, a deterministic,
  no-model stand-in that answers a cell from the fixture's own records
  (demonstration first, then the coverage-gate's own substantive/
  honest_limit classification); citations are the *union* of every
  demonstration/substantive/honest_limit record's sources for that cell,
  not just whichever one supplies the answer text — otherwise the
  fabrication-defect scenario (a bad citation on a *quote* record) would
  never surface for a cell where a *demonstration* happens to answer.
  `LiveModelAnswerer` is a named, deliberately-`NotImplementedError` seam.
- `engine/m3/grading.py` — `source_boundedness_check` (mechanical, reliable:
  every citation must resolve to a real source record) and
  `register_check` (an explicitly narrow heuristic — one metaphor-as-
  definition regex, grounded-in-a-real-quote check — built and tested
  against exactly the one seeded register defect this stage's gate names,
  *not* offered as a general register grader; spec module M3 itself says
  Mark's reading is the real register instrument).
- `engine/m3/harness.py` + `results.py` — orchestration and
  `validation/admission/results.json`'s shape (`sealed-key refs`: results
  reference `probe_id`, never the sealed plaintext wording).
- `engine/m3/selftest.py` — stage-4 gate, confirmed:
  `engine/m3/reports/selftest-report.json` shows the clean fixture battery
  all-pass (28/28) and both M3-layer `fixtures/seeded_defects.yaml` entries
  caught (`admission-register-invented-aphorism`,
  `admission-fabricated-source`).
- **Deliberately reverted mid-stage:** `engine/m2/validation.py` briefly
  imported `engine.m3` to embed real admission results into a compiled
  package, then was walked back — `canon/sealed_probes/README.md` and
  `engine/canon/check_seal_isolation.py` both name M2 as a code path barred
  from the sealed plaintext, and M3 reads that plaintext, so M2 must never
  import M3 even transitively "just to build a package." Real admission
  evidence stays at `engine/m3/reports/selftest-report.json`, deliberately
  never routed through a package. Recorded here so nobody "fixes" this
  apparent gap the same way again without re-deriving why it isn't one.
- CI: `m3-admission-harness` (module name, not the stage-3 job — see
  `.github/workflows/ci.yml`'s own comment on the near-collision between
  "M3 the module" and "stage 3").

Stage 4 gate reached: *"catches a seeded register defect and a seeded
fabrication on the fixture world."*

**Stage 5 (M4+M5), non-model half — done, this commit:**
- `engine/m4/store.py` — the session event log (Artifact-3 SS1): SQLite-
  backed for dev/test (DECIDABLE, same pattern as M2's FAISS placeholder;
  real deployment is managed Postgres per Artifact-6 SS3 topology). Append
  is idempotent on `event_uuid` (a retried append is a silent success, never
  a duplicate row), ordered per-session via `seq`, with bounded (3×) retry
  on a concurrent-writer collision. `Store` holds no session state itself -
  that's what makes "any instance can serve any session" literally true.
- `engine/m4/events.py` — the event catalog (Artifact-3 SS2): required-key
  and closed-vocabulary validation per type; `guidance_*` is accepted as a
  reserved family but `validate()` refuses to ever pass one (spec principle
  2: no live guidance exists).
- `engine/m4/projection.py` — `project_fresh()`: folds the log into a fresh
  `SessionState` every call, never a cached/shared instance. The safety
  accumulator folds as "take the latest `safety_state` event per track,"
  never a manual re-summation - each event already carries its own full
  current value, so resume-safety is a property of the log, not the fold.
- `engine/m4/session_code.py` — 128-bit CSPRNG, Crockford base32 (26 chars,
  grouped), SHA-256 hashed at rest, constant-time compared.
- `engine/m4/entrance.py` — the entrance seal, enforced twice:
  `open_session()` refuses a second `session_started` for the same
  `session_id` at runtime (the real guarantee), and
  `find_second_writer_violations()` greps the rest of `engine/` for a
  session_started *write site* as defense-in-depth. **Found and fixed a
  false-positive on the first real run**, worth remembering: a plain
  substring grep for `"session_started"` flagged `events.py` (a schema
  declaration) and `projection.py` (a read/fold) as "violations" - neither
  is a write. Narrowed to a regex matching only the keyword-argument write
  shape (`event_type="session_started"`, excluding `==` reads) before
  trusting the guard - the same "don't ship a guard that flags legitimate
  code" lesson as stage 3's isolation guard, hit fresh here because it's a
  different guard.
- `engine/m4/tests/test_resume_across_processes.py` — the literal gate item:
  two independent `Store` instances sharing nothing but a file path
  reconstruct identical, full-fidelity state (including a safety
  accumulator that was updated *after* the simulated resume) from the log
  alone.
- `engine/m5/anachronism.py` — anachronism computed per world from its own
  `time_window` against fleet `modern_term.origin_year` data - no world
  identifier in the code (law 4).
- `engine/m5/routing.py` + `failure.py` — the deterministic routing merge
  (Artifact-4 SS3, priority order proven by test: safety > system_nature >
  anachronistic bridge > later_age/other_tradition press-state > ordinary)
  and the fail-open/degraded semantics (SS4: reader failure forces
  pass-through regardless of safety's own outcome; safety failure alone
  fails open but reader-based routing still applies; two consecutive
  degraded turns is the page-the-operator condition). Both take
  already-resolved call outcomes (`CallOutcome`) as input - they never make
  or await a model call themselves, which is exactly what makes this half
  buildable and testable today.
- CI: `m4-event-log`, `m5-gate-routing`. Evidence at the time:
  `engine/m4/reports/pytest-output.txt` (22/22),
  `engine/m5/reports/pytest-output.txt` (25/25), full suite 60/60. (Grew
  substantially since - see the turn-loop entry below; full suite is 97/97
  as of commit `230a331`.)

**Stage 5, model half — decision resolved, live, and in active use.** The
Bedrock account came up, credentials were provided (see the credential
handling note above), the preflight passed for real, and Mark has since
directed and paced real spend across the safety script (six batches, s1-s23,
findings 1-4 above). The "decision, not a guess" section immediately below
is kept as the historical record of that decision being raised and made -
it is no longer an open gate; nothing here is currently blocked pending it.

## Before the model half of stage 5: a decision, not a guess (RESOLVED — kept as historical record)

Stage 5's remaining gate items — *"live safety script ≥19/20 vs fixture
world; crisis append asserted incl. empty-stream; lazy load/unload
measured"* — every one needs a **real conversational turn** (resume and the
entrance seal, the other two gate items, are already done above without
one). The live safety script alone is 20-ish adversarial conversations
against the fixture world. That means:

1. **A model provider must be chosen and configured** (spec principle 11:
   provider switches land last and alone — meaning this is exactly the kind
   of decision that shouldn't be made implicitly by whichever thread happens
   to need a model call first). Spec §7 names Bedrock as the pilot's target,
   but "Bedrock preflight — blocked on the live AWS account" is explicitly
   listed as an unresolved risk (spec §10), and no AWS account has been
   wired into this build environment.
2. **Real spend.** Even a cheap Haiku-class gate call, run ~20+ times for
   the safety script alone, is real API cost. Build-Blueprint.md §4 reserves
   "spending beyond the budget envelope" as Mark's decision, not this
   thread's.

Stage 4 deliberately avoided both by building `FixtureRecordAnswerer` (no
model call) instead of wiring a live one. The live safety script and a real
generation call can't avoid it — that IS the remaining stage-5 work. **This
is the decision to raise with Mark before writing that code**, not a guess
to make and correct later: which provider/model to call (Bedrock, once
actually live, or a cheaper interim path for dev-time iteration before the
real Bedrock preflight), and confirmation that the near-term spend (dev
iteration + the safety script's ~20+ calls) is within an approved envelope.
Mark has since said the Bedrock account is provisioning and should be
available in a couple of hours - noted above; still not a green light to
spend against it until it's actually live and the choice is confirmed.

**Already done without that decision** (at the time of writing): the event
log/store, session projection, session codes, the entrance seal,
resume-across-two-processes, and the Facilitator gate's routing/failure
logic — see the "non-model half" list above. Everything else this section
once listed as needing the live call — the classification calls, the live
safety script, crisis-append-on-empty-stream, lazy load/unload timing — is
now done too; see the entries above. Stage 5 is closed out as of commit
`230a331`.

## Open decisions still outstanding

- `gravity`/`force` record field shape — ratified as-is at stage 1,
  unchanged, now with two structured additions (`classification`,
  `matrix_cell` - the glossary retrofit, top section) on top of it.
- FAISS placeholder vectors (`engine/m2/builders.py`) — still a
  deterministic hash-derived stand-in. **Resolved in direction, not yet
  in code:** the M4 design's Fork 3 (signed off, §9.5) rules
  lexical-first retrieval as the live path — real embeddings are
  admittable later, per the design's own §3.4 threshold (measured recall
  on real transcripts), not foreclosed, but nothing pays for a provider
  anywhere until that evidence exists. The placeholder vectors themselves
  are simply unused by the actual retrieval path now (`engine/m4/
  evidence.py` scores lexically, direct off compiled record JSON) —
  removing them outright is a minor cleanup, not a blocked decision.
- Sealing mechanism (`canon/sealed_probes/README.md`) — commit-reveal +
  access-discipline guard; real secrets infra is a later, non-urgent call.
- `engine/m3`'s register heuristic — explicitly narrow; real register
  grading needs either Mark's read or a configured model. Partially
  addressed by the model-tiering call below (Sonnet carries voice
  generation, the one call actually responsible for register), but the
  heuristic itself is unchanged and still narrow.
- **Model tiering for live turns (`engine/m4/LIVE-GENERATION-DESIGN.md`
  §9.6) — TEST, not locked.** Haiku for safety/reader, Sonnet for voice
  generation (now the only generation call - citations are in-band).
  Mark's own empirical call from prior usage elsewhere in this project;
  explicitly flagged as provisional pending real cost/quality
  measurement, unlike §9.5's four signed-off forks.
- **The glossary/story/quote retrofit task is drafted, the gate is live,
  but the task itself has not been sent to the six content threads** -
  the single most concrete unstarted action as of this note (top
  section).
- **Desert's External Scholarly Review** (Doc_09c §4's other named
  freeze-eligibility gate, distinct from the living-tradition-
  differentiation review this thread already closed) — needs an actual
  patristics/late-antique-monasticism specialist. Not blocking anything
  currently in flight; blocking Frozen status whenever that's raised.
- **Credential rotation still outstanding** (carried forward from the
  stage-6 entry below, still true): the AWS access key
  (`cic-bedrock-dev`, account `468683594478`) is still the one pasted
  directly in chat, now in even wider live use across this session's own
  real Bedrock calls (M4 turn-loop evidence, M8 instrumentation).
  Rotating/deleting it is still the right move once this phase of dev
  work actually slows down.

## Currently blocked

**Nothing in this engineering thread is blocked on a missing decision -
everything genuinely open now needs either Mark's own action or someone
this thread cannot substitute for, not more engineering judgment:**

1. **Send the retrofit task.** Drafted, ready, not yet dispatched to the
   six content threads (top section) - the one item on this whole list
   that's pure "someone needs to press send," not a design or spend call.
2. **Step 7 (admission) and M7 (transcript audit)**, for every world -
   both need real live-model spend/data and both stay explicitly reserved
   for Mark's own go-ahead, the same discipline this file has held since
   the stage-5 safety script and every Bedrock call since. Nothing in
   this thread's own work has made or triggered one.
3. **Desert's External Scholarly Review** and **Alexandria's own older,
   still-possibly-open source gaps** (Stromateis III, Origen's Homilies,
   Didymus's Tura commentaries, the Letter to Marcellinus - four
   genuine not-found texts; the Philocalia acquisition and the *On
   Prayer*/Curtis-CCEL provenance question flagged for Mark's own
   judgment) - carried forward from this section's own prior text below,
   **not independently re-verified as of this update** - worth checking
   fresh rather than assuming either way before treating either as
   closed or as blocking.
4. **Stage 7.5 (experience design)** is still Mark's own design pass, not
   code; **M6 (the participant surface, stage 8)** is still explicitly
   gated on 7.5's approved screens - "no surface code before approval"
   remains true, so M6 is still not a task any thread should pick up
   unprompted even though the M4 turn loop it would sit behind is now
   considerably more complete than when this section was first written.

The two things this thread built that touch M6/M5 territory but were
flagged as deliberately out of scope for stages 5-6 (not silently
skipped): Track B's own `safety_turn` content (`HARMFUL_DYNAMIC_SIGNAL`),
and the other routing actions' generation content (`check_in_turn`/
`system_nature_turn`/`bridge_turn`/`etic_turn`) - real, tested routing
outcomes (`engine.m5.routing`) with `UnhandledRoutingAction` raised loudly
wherever their content isn't built yet. These become real work once M6
(stage 8) actually starts, not before.
