# The Multi-Voice Table on the New Engine — Ground Truth and Scoping

**Written:** 2026-08-28, opening the Table-build thread. This document does two
things: (1) records what already exists and what is already decided about the
multi-voice Table, with sources, so no prior decision gets re-made by accident;
(2) scopes the actual engineering problem of bringing the Table to the current
engine (`engine/`), naming what is a settled continuation and what is a genuine
open call for Mark. Nothing here is built yet; this is the write-up-before-build
the thread was asked for.

---

## Part 1 — Ground truth: what already exists

### 1.1 The design layer is complete, and live-tested — against the old backend

- **`L3D-Encounter-Methodology/CiC_L3D_The_Table_Design_Document_V2.3.docx`** is
  the governing design document, self-declared "construction-complete as the
  governing design document for the multi-world Table" (§12, Readiness status).
  It specifies the Five Presences (Facilitator, Representatives, Participant,
  Public Transcript, the Worlds), three entry pathways (bypass / build-your-own
  / guided onboarding), facilitator-directed table setting, the encounter arc,
  and the constitutional grounding (Constitution V2.2 Article 3 for context
  isolation, Article 27 for facilitator neutrality, etc.).
- **`L3D-Encounter-Methodology/CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md`**
  is the operational process for the three-Representative table: turn floor 3 /
  cap 6 per round (cap was lowered to 4 during the turn-cap incident, restored
  to 6 on 2026-07-13 after re-test), turn-selector guidance (breadth-of-voice
  preference, no immediate self-repeat), dominance measured as cumulative
  word-share with a 65% single-Representative threshold, and the fully diagnosed
  turn-cap incident (root cause: extended thinking consuming token-capped
  reactive calls; fix: `thinking: {"type": "disabled"}` on every token-capped
  call, verified over eight consecutive trials).
- **`L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`** §8
  (turn allocation is judgment, not rotation) and §10 govern the Facilitator's
  conduct at the table.
- All of this was **live-tested against the old `cic-poc` backend** (V2.3 §12:
  "deployed and live-tested at the three-Representative configuration"). Full
  three-world rounds at the 6-turn cap ran ~150 seconds end to end.

### 1.2 The old implementation is still in the tree — the deletion was frontend-only

The 2026-08-26 front-end decision-log entry
(`Ministry/Technology/CiC_FrontEnd_Decision_Log.md`) says "the old working
component code was deliberately deleted during the engine rebuild." Checked
against the tree, that deletion is **frontend-only**: `LivingTableScene` is gone
(cross-system audit F-18 — `worldIcons.tsx` survives as a dead, inconsistently
keyed asset table). The **backend multi-world implementation is intact** under
`cic-poc/backend/`:

- `app/main.py` — the streaming multi-world round loop: `is_multi_world`,
  `MIN_MULTI_WORLD_TURNS` (floor read from `wrs/parameters.yaml`,
  `turn_floor_multi_world`), `MAX_MULTI_WORLD_TURNS = 6`, per-round
  `check_dominance` / `check_convergence` / drift monitoring, SSE turn events
  (`done {phase, turn_count}` etc.).
- `app/graph/nodes.py` — `build_public_transcript(state, exclude_world_id)`,
  the turn-selector, `get_multi_world_handoff_prompt(world_ids)`, per-voice
  invocation receiving the public transcript as conversation context.
- `backend/scripts/s44a_table_battery.py` plus
  `Ministry/Technology/Pass2/batteries/S4.4a_table_battery*` — a table-specific
  validation battery already existed once.

None of this can be dropped into `engine/` (different architecture: LangGraph
vs. the M4 turn loop; different record store; different safety stack), but it is
the **proven reference implementation** for the conversational mechanics, and
the design documents cite it by line.

### 1.3 The current engine has zero multi-voice scaffolding — confirmed, file by file

The audit-thread handoff's claim ("the current engine has zero multi-world
scaffolding — `mode` is a closed single-value enum at the event-schema level")
is exactly right:

| Where | Single-voice assumption |
|---|---|
| `engine/m4/events.py` | `session_started` requires one `world_key`; allowed values for `mode` are literally `{"interview"}` with the comment "the only mode Phase 1 ships (spec O9: Table is a separate product)" |
| `engine/m4/projection.py` | `SessionState` holds one `world_key`, one `package_manifest_hash`, one `frame` |
| `engine/m4/turn.py` | `run_turn(world: LoadedWorld, ...)` — one compiled prompt, one evidence pass, one grounding-net check, one `voice_event` whose `speaker` is `world.world_key`; `SESSION_TURN_CAP = 10` counted in completed voice turns |
| `engine/api/wiring.py` | `create_session(world_key=...)`; `handle_message` loads exactly one world; `history_from_transcript` pairs each participant message with the single voice reply; `already_told_ids` / `already_bridged_*` are flat single-world sets |
| `engine/api/app.py` | `SessionCreateRequest{world_key}`, one `MessageResponse` per participant message; no streaming transport of any kind (`turn.py`'s own docstring: "no live token-by-token SSE transport exists yet in this codebase") |
| `engine/m4/facilitator_turns.py` | fixed-table facilitator text parameterized by one representative name |
| `engine/m8` | usage attributed per `session_id` + `call_kind`; no per-world dimension |
| `engine/m3` | admission is per-world, single-voice by construction |

What is **not** single-voice, helpfully: M5's safety and reader gate calls take
the participant's message and no world at all — they extend to a table
unchanged. And the spec priced the seams in deliberately (O9): "explicit mode
field, viewer-parameterized transcript projection, per-mode configuration."

### 1.4 Adjacent state worth knowing

- `Redesign-Spec/CiC-Program-Spec.md` §9: the Table "is not a stage — [it is a]
  compile target and module this architecture keeps cheap, added by [its] own
  future spec." That future spec is what Part 2 below begins.
- The website already ships the participant-side seam: "Add to the Table"
  multi-select tray (up to three worlds) handing off with `mode=table` — a URL
  parameter the engine currently reads nowhere (decision log, 2026-08-25 entry;
  audit line on `mode=table`).
- Table visual assets are locked: `Ministry/Communication/Brand-Assets/
  Table-Templates/` (1/2/3-world geometry, V1.0-reviewed icon family).
- `Ministry/Technology/table_phase0/` is **not** Table engine work — it is the
  corpus-acquisition scrubs (texts want-list, per-world scrub findings) that
  were framed as phase 0 of Table readiness.
- All six formation worlds sit at registry `state: built` — none `admitted` or
  `open`. Building the Table does not change launch-readiness sequencing (the
  2026-08-26 decision-log entry's headline finding); it is parallel engineering.

### 1.5 Decisions already made — do not reopen

1. **Three worlds is the permanent table-size ceiling** — Mark, 2026-08-01,
   cost-driven; retires the original design ceiling of five. Recorded in the
   Process doc §7, V2.3 §2/§12, and `cic-poc/backend/wrs/parameters.yaml`
   (`table_size_ceiling`, design_value 5 RETIRED, current 3 permanent).
2. **Public-transcript isolation is constitutional** (Constitution V2.2 Art. 3;
   V2.3 §3, §6): a Representative sees only what the others *said* at this
   table, never their packages, ecology, or records. This is the cross-world
   contamination boundary.
3. **Turn allocation is judgment, not rotation** (Facilitator Governance V3.6
   §8; Process V1.0 §2): no forced round-robin, floor 3 turns per round, a
   round may legitimately exclude a voice.
4. **The turn-cap incident's fix stands**: extended thinking disabled on every
   token-capped call; cap 6 with the fix in place (re-tested), 4 as the
   conservative fallback.
5. **Each world must be individually complete before it comes to the Table**
   (V2.3 §10) — the Table never compensates for a shallow world.
6. **Facilitator neutrality**: the host belongs to no world and holds all of
   them (V2.3 §3, §5; Constitution Art. 27).

---

## Part 2 — The engineering problem on the current engine

### 2.1 Shape of the extension

A Table session is a new **mode** (`session_started.mode: "table"`), exactly the
seam O9 priced in. The single-voice interview path stays byte-identical — no
existing event, test, or admission result is touched. Per module:

**Event schema (M4, `events.py`/`store.py`/`projection.py`).**
`session_started` gains a mode-dependent shape: `mode: "table"` carries
`world_keys: [2..3]` with a per-world `package_manifest_hash` map (each world's
package is still hash-verified at load, per world). `voice_event.speaker`
already carries a world key — multi-speaker transcripts need no change there.
New event type for the turn-selector's decision per voice turn (who spoke, why,
selector reasoning) so the M7 audit surface sees turn allocation, not just its
result. `SessionState` grows `world_keys`, per-world `already_told_ids` /
bridge sets (keyed by world), and round bookkeeping.

**Turn loop (M4, new `engine/m4/round.py` or table-mode path in `turn.py`).**
One participant message triggers a **round**:

1. Gate once — M5 safety + reader calls are message-level and world-agnostic;
   they run exactly once per participant message, not per voice. Routing
   actions that bypass the voice (safety_turn, check_in, system_nature, etic,
   bridge) resolve at the round level: a crisis is a crisis at any table.
2. Turn-select — a new, small model call (new `call_kind`): given the public
   transcript and the participant's message, choose the next speaker or close
   the round. Floor 3 / cap 4-or-6 (see open call C3), no immediate
   self-repeat, breadth-of-voice preference per Process V1.0 §2.
3. Voice turn — for the selected world only, the **existing single-voice
   machinery runs unmodified in its scope**: that world's compiled prompt as
   the cached system prefix, evidence assembled from that world's own coverage
   and repository, grounding-net checked against that world's own records,
   name-bridge and glosses from that world's own package.
4. Repeat 2-3 until the selector closes the round or the cap lands.
5. Round-level governance — dominance (cumulative word-share, 65% threshold)
   and convergence checks, ported from the poc's `check_dominance` /
   `check_convergence` as deterministic-first where possible.

**The grounding-isolation safety property falls out structurally — then gets
tested anyway.** Because step 3 invokes the existing per-world pipeline with
exactly one `LoadedWorld`, alx's voice *cannot* ground a claim in desert's
records: desert's repository is simply never in scope for alx's net, evidence
pass, or prompt. The only cross-world channel is the public transcript entering
as conversation history — which is precisely the designed boundary (V2.3 §6).
The build still adds an explicit regression test: a table session where the net
is asserted to have validated every citation of every turn against the
speaker's own repository and no other, plus a seeded-leak fixture (a record id
from world B planted in world A's output must be withheld by A's net as an
unknown tag). This is the one property the thread must never take on faith.

**History and "what's already been said."** `history_from_transcript` becomes
viewer-parameterized (the O9 phrase): the history handed to a voice is the
public transcript — participant messages plus *all* speakers' surviving text,
each attributed — while `already_told_ids` / `already_bridged_*` stay **per
world** (a story desert told is not "already told" for alx; a figure alx
bridged is not bridged for desert). Facilitator interjections appear in every
voice's history identically.

**API surface (`engine/api/`).** `POST /api/session` accepts `world_keys` (2-3)
alongside the existing single `world_key`; `mode` derived, not client-set
beyond that. The message endpoint is the hard part — see open call C2
(transport): a 3-6-turn round at real latency does not fit the current
one-request/one-response shape.

**M5.** Gate calls unchanged (once per message). `facilitator_turns` texts need
multi-representative variants (they currently name exactly one representative).
The safety-script battery (SS210 discipline) was authored single-message,
single-voice; whether a table-mode safety re-run is owed is open call C5.

**M8.** `record_usage` gains world attribution on voice/turn-selector calls
(session_id alone no longer answers "which world cost what"). New call kinds:
`turn_selector`, per-voice `voice_generation` tagged by world. Cost per
participant message multiplies (up to 4-6 voice calls + selector calls + the
two gate calls); the session cap unit needs re-deciding (open call C4). Per
standing project rule: token counts reportable, no $ figure until reconciled
against an AWS invoice.

**M3.** Unchanged for world admission. Whether the Table itself needs an
admission-style battery before participants sit at it (the poc had S4.4a) is
open call C5.

**M1/M2.** No record or compiler changes required for a first build. The spec
names "Table artifacts" as possible future compile targets (M2), but nothing in
this scoping needs one yet.

### 2.2 What this build does NOT include

- No facilitator free generation beyond what's decided in C1 below — the
  current engine's fixed-script facilitator discipline is a deliberate safety
  stance, not an accident.
- No world-menu/browse pre-encounter portal work (frontend thread's own scope;
  the multi-select tray design is explicitly "the Table thread's own to design
  when it ships" — but that means the participant-facing UI, which should
  follow the engine API, not precede it).
- No raise of the three-world ceiling, ever (decided 2026-08-01).
- No change to single-voice interview behavior — provably, via the existing 13
  CI checks staying green plus the new mode living behind the schema seam.

### 2.3 Open calls — Mark's, before or during the build

- **C1 — The Facilitator's live voice at the Table.** V2.3 gives the
  Facilitator relational introductions, table-setting narration, and curatorial
  transparency ("I've brought two voices who have lived close to your
  question…"). The current engine's Facilitator speaks only fixed, code-owned
  scripts — a deliberate discipline. Options: (a) fixed-template table
  introductions parameterized by the chosen worlds (keeps the discipline,
  loses warmth); (b) a constrained live facilitator call for introductions
  only; (c) defer introductions to the frontend copy. Recommendation: (a) for
  the first engine build, revisit after it works.
- **C2 — Transport.** A full round is 3-6 sequential voice generations
  (~60-150s measured on the poc). The current engine has no SSE. Options:
  (a) build the SSE turn-event transport now (the poc's shape, and the thing
  `turn.py`'s sentence-gating note says the net design already anticipates);
  (b) a polling shape — the round runs server-side, client polls the
  transcript; (c) turn-at-a-time — each HTTP response returns one voice turn
  plus a `round_open` flag and the client re-calls to continue the round.
  Recommendation: (c) first (no new infrastructure, each turn arrives as fast
  as a single-voice turn does today, resumability falls out of the event log),
  with (a) as the known future layer. This is the biggest architectural call in
  the build.
- **C3 — Round cap 4 or 6.** The Process doc restored 6 after re-test but
  itself flags that two trials are lighter evidence than eight, and 6-turn
  rounds ran ~150s. With C2(c) the latency argument weakens (no single long
  request). Recommendation: ship the floor/cap as configuration
  (3/4 default, 6 allowed), decide the default from the first live table runs.
- **C4 — Session-cap and cost units.** `SESSION_TURN_CAP = 10` counts voice
  turns because voice turns drive cost growth. At a table, does a participant
  get 10 exchanges (each costing up to 6 voice turns) or 10 voice turns
  (roughly 2-3 exchanges)? Pure cost/UX call; the memory-growth measurement
  that set 10 was single-voice. Needs Mark plus, eventually, a live measured
  run (which needs his per-run authorization, per standing rule).
- **C5 — What validation gates a Table before participants use it.** The poc
  had a table battery (S4.4a). The new engine's Table presumably owes at
  minimum: the grounding-isolation regression suite (built into CI, §2.1), a
  live table smoke run (authorized spend), and a decision on whether the
  SS210 safety battery needs a table-mode pass. The spec's "added by their own
  future specs" language means the Table's own spec artifact should state its
  gate — proposal: write it as `Redesign-Spec/Artifact-7-Table.md` once C1-C4
  are answered, so the contract precedes the code the way every other module's
  did.
- **C6 — Which pairings sit together.** The design says any 1-3 combination,
  participant-composed or facilitator-directed. For the first live tests
  someone still picks the first configurations. (Low stakes, but Mark may have
  a preference — e.g., the intellectual-textual/ascetic-embodied pairing the
  design document itself keeps reaching for, which maps to alx + desert.)

### 2.4 Proposed build sequence (after C1/C2 land)

1. `Artifact-7-Table.md` — the contract: event shapes, round semantics,
   isolation property, gates. (Mirrors how M1-M8 were each built.)
2. Schema + projection: `mode: "table"`, multi-world `session_started`,
   turn-selector event, per-world state. Tests green with the interview mode
   untouched.
3. Round loop over the existing single-voice turn machinery + deterministic
   governance checks + the isolation regression suite.
4. Turn-selector call (provider seam, mocked in CI like every other live call).
5. API surface per C2, wired to the event log.
6. Live table smoke run — **only with Mark's explicit per-run authorization**.
7. Then the frontend tray/table UI, in the frontend thread's own terms.

---

*Sources for every claim above: `CiC_L3D_The_Table_Design_Document_V2.3.docx`,
`CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md`, `CiC_FrontEnd_Decision_Log.md`
(2026-08-25 and 2026-08-26 entries), `CiC_Cross_System_Consistency_Audit_2026-08-26.md`
(F-15, F-18), `CiC-Program-Spec.md` (O9, §9), `engine/m4/{events,turn,projection}.py`,
`engine/api/{app,wiring}.py`, `cic-poc/backend/app/{main.py,graph/nodes.py}`,
`cic-poc/backend/wrs/parameters.yaml`.*
