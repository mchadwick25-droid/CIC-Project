# Artifact 7 — The Table: Multi-Voice Sessions

Companion to `CiC-Program-Spec.md` — the "own future spec" its §9 promised for
the Table, filling the extension seams O9 priced in (explicit mode field,
viewer-parameterized transcript projection, per-mode configuration). Governed
at the design layer by `CiC_L3D_The_Table_Design_Document_V2.3`,
`CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md`, and
`CiC_L3D_Facilitator_Governance_V3.6` — this artifact is the engine contract
for that design, the way Artifacts 1–6 are contracts for M1–M8. Scoping and
ground truth: `Ministry/Technology/CiC_Table_Engine_Scoping_2026-08-28.md`.

Inherited decisions this artifact builds on and must never weaken:
three-world permanent ceiling (Mark, 2026-08-01); public-transcript isolation
as the constitutional cross-world boundary (Constitution V2.2 Art. 3); turn
allocation as judgment, not rotation (Governance V3.6 §8); extended thinking
disabled on every token-capped call (the turn-cap incident fix); each world
individually complete before it sits at a Table (V2.3 §10).

Decisions taken 2026-08-28 (Mark, this thread): **C1** — the Facilitator's
table introductions are fixed templates parameterized by the seated worlds,
keeping the engine's no-free-generation Facilitator discipline; **C2** —
transport is turn-at-a-time HTTP (each response carries at most one voice
turn plus round state; no SSE dependency); **C3** — round floor/cap ship as
configuration, floor 3 / cap 4 default, 6 allowed.

Still DECIDABLE (Mark): **C4** — the session-cap unit at a table (this
artifact carries the interview cap semantics forward, counted in voice turns,
explicitly provisional); **C5** — whether SS210's safety battery owes a
table-mode pass before participants sit (the CI gates in §8 are this
artifact's own floor, not a substitute for that decision); **C6** — first
live pairings.

---

## 1. Session shape

A Table session is `session_started.mode = "table"`. The interview mode's
events, semantics, and bytes are untouched — every existing test must pass
unmodified, and a `mode: "interview"` log written before this artifact
projects identically after it.

**`session_started` payload, table mode** (mode-dependent keys; the catalog
stays exhaustive and `validate()` learns the mode split):

- `mode: "table"`
- `world_keys`: ordered list of **2 or 3** distinct registry keys. One world
  is an interview, not a table; four is forbidden by schema, not left to
  judgment (the design doc's "no mechanism prevents a fourth world" gap is
  closed here at the log level).
- `package_manifest_hashes`: map `world_key → manifest_hash`, same pin-at-
  creation semantics as the interview's single hash — a mid-session recompile
  of any seated world refuses that session's load.
- `frame`, `code_hash`: unchanged meaning.
- The interview keys `world_key` / `package_manifest_hash` are absent in
  table mode (and `world_keys` / `package_manifest_hashes` absent in
  interview mode) — a payload carrying both shapes fails validation.

`open_session()` (engine.m4.entrance) remains the only writer of
`session_started`, gaining the table shape behind the same seal — the static
grep-guard and the runtime second-writer refusal both still hold.

Session creation appends the table **door turn**: one `facilitator_turn`
(kind `door`), fixed template (C1) naming each seated Representative with its
role label and world display name, in `world_keys` order. Template text is
code-owned in `engine.m4.facilitator_turns` beside the existing door text and
carries its craft note.

## 2. The round

One participant message opens one **round**: the sequence of voice turns that
answers it. Definitions:

- **Round-open**: a `participant_message` whose round has not yet seen
  `round_closed`.
- **Floor / cap**: configuration (C3), floor 3, cap 4 (6 allowed), counted in
  voice turns within the round. The floor binds the selector's close option,
  never forces all voices to speak (Process V1.0 §2: 3 turns does not
  guarantee 3 voices — by design). The cap binds absolutely.
- **No immediate self-repeat**: the same world never takes two consecutive
  turns in a round. Enforced in code, not left to the selector's prompt.

New event types (catalog additions — reviewed change, per Artifact-3 SS2):

- `turn_selected` — `{round_no, position, world_key, reason, degraded}`.
  Written before each voice turn; `world_key` is the chosen speaker;
  `reason` is the selector's stated basis (or the deterministic fallback's,
  with `degraded: true`). This is the M7 audit's view of turn allocation —
  who spoke is never recoverable only from `voice_turn` order.
- `round_closed` — `{round_no, reason, turns}`. `reason` enum:
  `selector_closed` | `cap` | `floor_unmet_exhausted` (the selector wanted to
  close early but eligibility rules left no legal speaker — logged honestly,
  never silently stretched). Exactly one per round; `turn_committed` follows
  it, once per round (a round, not a voice turn, is the committed unit —
  `turn_no` keeps its interview meaning of "participant exchanges").

Gate calls (M5 safety + reader) run **once per round**, on the participant's
message — they are message-level and world-agnostic. Routing resolves at the
round level:

- `safety_turn` (acute), `check_in_turn`, `system_nature_turn`, `etic_turn`:
  the round is the Facilitator's; no voice speaks; `round_closed`
  reason `selector_closed` with `turns: 0` (the floor never forces voices
  into a governed round). Crisis-resource and cap texts gain multi-
  representative template variants (they currently name exactly one).
- `bridge_turn`: the Facilitator speaks the modern sense once, and the
  round proceeds on the underlying subject — every seated voice receives the
  term-free message, same barred-terms discipline per world.
- Ordinary routes: the round runs §3's loop.

Anachronism scope: the fleet-record term set is computed per world (each
world's own `time_window`), and a term is round-anachronistic when it is
anachronistic for **every** seated world; a term inside one seated world's
horizon is not bridged away from a voice that can answer it. (The selector
may then favor that voice; the gate never lies to the others — they simply
were not selected while the term is live.)

## 3. The voice turn — single-voice machinery, single-world scope

Each voice turn invokes the existing per-world pipeline exactly as the
interview does, scoped to the selected world alone:

- that world's compiled prompt as the cached system prefix, byte-identical
  across the session (the cache contract holds per world);
- evidence assembled from that world's own coverage/repository only;
- grounding net checked against that world's own repository only;
- name-bridge, glosses, do-not-voice, output check from that world's own
  package;
- extended thinking disabled on every token-capped call (inherited fix).

**The isolation property (constitutional, tested):** no voice turn's
evidence assembly, grounding check, prompt, or citation resolution may read
any record, chunk, index, or compiled artifact belonging to a world other
than its speaker. The only cross-world channel is the public transcript
(§4). CI enforces this with, at minimum: (a) an assertion suite over a
multi-round table fixture session proving every surviving citation of every
turn resolves within the speaker's own repository; (b) a seeded-leak
fixture — a record id from seated world B planted in world A's raw output
must be withheld by A's net as an unknown tag, and the withholding visible
in the turn's `grounding` result; (c) a static check that the round loop
constructs per-turn scope from exactly one `LoadedWorld`.

Per-world session memory: `already_told_ids`, `already_bridged_figure_ids`,
`already_bridged_gloss_ids` are **per world**, derived from `voice_turn`
events filtered by `speaker`. A story desert told is not "already told" for
alx; a figure alx bridged is not bridged for desert.

## 4. The public transcript as history (viewer-parameterized projection)

The history handed to a voice's generation call is the public transcript
projected for that viewer:

- its **own** prior turns are `assistant` turns, replayed with verified
  citations re-tagged (`_replay_text` semantics unchanged — the anti-
  citation-decay fix applies per voice);
- participant messages and **other voices' surviving text** fold into the
  `user` turns, other voices' speech attributed by representative name and
  world display name (what was *said* at the table — never their records,
  packages, or ecology);
- Facilitator turns are excluded from `assistant` content exactly as the
  interview excludes them; table introductions and governance interjections
  appear (attributed) in the folded `user` content where a voice needs them
  to follow the room;
- roles alternate strictly; consecutive non-self segments concatenate into
  one `user` turn.

Withheld sentences keep their interview-mode treatment: shown text replays,
tags replay only where they verified.

## 5. The turn selector

A new gate-class model call (`call_kind: "turn_selector"`, safety-model
tier), invoked before each voice turn — except two cases decided in code
first:

- **Direct address by name** (Facilitator Governance SS8, the governing
  sentence the poc's S4.4a battery graded against: *"When the participant
  addresses a specific Representative, you route accordingly. Immediately,
  completely, without editorial intervention."*): a participant message
  naming exactly one seated Representative routes that voice at the
  round's opening position with no selector call. Conservative by the
  proven design — two names is ambiguous and falls through to the
  selector; "each/all/both of you" blocks the short-circuit; title-only
  address stays the selector's regime.
- **Forced moves** (below) make no call either.

Otherwise:

- **Input**: the participant's message, the round-so-far and recent public
  transcript, and for each seated world only participant-facing frame data
  (representative name, role label, display name, time window/place) — never
  package internals. Plus eligibility facts computed in code: who spoke
  last, floor/cap state, voices not yet heard this round.
- **Output** (forced JSON): `{"next": world_key | "close", "reason": str}`.
- **Guidance** (prompt): "most directly positioned" judgment with the
  breadth-of-voice preference of Process V1.0 §2 — prefer an unheard voice
  when the question is genuinely open to all, but a voice with a real,
  specific response to what was just said remains selectable.
- **Code-enforced, never model-trusted**: no immediate self-repeat; `close`
  refused below the floor (re-asked once with close removed from the legal
  moves; if the selector still cannot produce a legal speaker,
  `floor_unmet_exhausted`); cap closes the round regardless of the model's
  preference; an unknown `world_key` in the output is a failed call.
- **Forced moves make no call** (added 2026-08-28, both live runs'
  evidence): when closing is off the table and exactly one voice is
  eligible, there is no judgment to exercise — the code selects it and
  writes the honest reason itself. Both live runs showed the model, asked
  anyway, confabulating a justification in the `turn_selected` reason (an
  M7 audit surface), even with the round facts stated in its prompt. At a
  two-seat table this also removes two of every three selector calls.
- **Failure fallback (deterministic)**: on a failed or exhausted-retry
  selector call, the least-recently-spoken eligible voice speaks, and the
  `turn_selected` event carries `degraded: true` with the fallback stated in
  `reason`. A selector outage degrades allocation judgment, never the
  grounding or safety of the turns themselves.

## 6. Transport (C2): turn-at-a-time

No SSE. The client advances a round one voice turn per request:

- `POST /api/session` — accepts `world_keys` (2–3) for a table session;
  single `world_key` keeps creating interviews. Response carries mode and
  the seated worlds.
- `POST /api/session/{id}/message` — opens the round: gates once, resolves
  routing; on an ordinary route runs one selector step and **one** voice
  turn. Response: the turn (or the Facilitator's round, for governed
  routes), plus `round_open: bool` and `round_no`/`position`.
- `POST /api/session/{id}/continue` — advances the open round by one voice
  turn (selector step + voice turn), or reports the close. Calling it with
  no open round is a 409, not an error state. Response shape identical to
  `message`.
- Rounds are resumable by construction: all round state (which round is
  open, who has spoken, floor/cap position) is a projection of the event
  log — a continue served by a different process behind the same store
  continues the same round. Concurrent `continue` calls on one session are
  serialized by the store's per-session seq (Artifact-3 §1); the loser
  re-projects and returns the turn the winner produced rather than
  generating a duplicate.
- The transcript endpoint is unchanged in shape — multi-speaker transcripts
  already fit it (`speaker` is a world key per entry).

A future SSE layer streams the same events; nothing in this artifact
precludes it, and sentence-gating's placement note (engine.m4.turn) is
unchanged.

## 7. Caps and cost (M8)

- Every table-mode model call is attributed: existing kinds unchanged, new
  kind `turn_selector`; voice-generation and selector usage records carry
  the speaking/selected `world_key` (nullable on non-world calls) so
  per-world cost at a shared table is answerable.
- Session cap: **C4 RESOLVED (2026-08-28, Mark's delegation of the full
  C4 range)** — the table unit is **completed rounds**
  (`TABLE_SESSION_ROUND_CAP`, default 5), not voice turns: rounds are what
  a participant actually spends, and a voice-turn cap leaked the cost unit
  into the participant's experience (~3 questions per session). The
  default of 5 sits in the same measured output-token envelope as the
  interview's 10-turn cap (compact-turn rounds ran ~1.8k output tokens;
  live-table-report-2.json), and stays config pending a live long-session
  input-growth measurement — the same discipline the interview cap's own
  memory-growth run established.
- No $ figure is quoted anywhere in this build until measured against a
  reconciled AWS invoice (spec principle 13); token counts are reportable.

## 8. Gates before a participant sits at a Table

**The Table battery (C5, defined 2026-08-28)** — the successor to the
poc's S4.4a battery, implemented in `engine/m4/live_table_battery.py`
(live, by-hand, per-run authorized; every deterministic half is already
CI). Six probes in one session, ordered so probes 1–5 spend the round cap
and probe 6 proves it: **L1** direct address by name (AUTO — FG SS8
routing, zero selector calls), **L2** "each of you" breadth (AUTO — no
short-circuit, ≥2 distinct voices), **L3** crisis at the table (AUTO —
governed round, resources append, turns 0), **L4** no-foreknowledge (a
voice asked directly about another seated world claims only what it heard
here — RECORDED for Mark's read; the isolation sweep stays AUTO), **L5**
cross-voice memory attribution (RECORDED), **L6** the session round cap
close (AUTO). Post-run over the whole session: the isolation sweep, the
per-round governance summaries read back from `round_closed`, and the
convergence check — a conservative model judgment in the poc's own
lineage, RECORDED, never auto-failed. Round-level **dominance** is
deterministic and runs in the engine itself (`engine/m4/table_governance`,
poc thresholds: word-share ≥0.70 min 150 words; turn-share ≥0.50 at 3+
seats min 6 turns), attached to every `round_closed` payload — detected
and audit-visible, never blocking. SS210's sealed safety battery needs
**no** table-mode rerun on this build's evidence: the sealed call's input
is byte-unchanged in table mode (same message-level call, same empty
window/accumulator), and SS210's own trigger is a change to the sealed
call's input — L3 stands as the live table-mode smoke of the governed
path, not a substitute for that reasoning.

This artifact's own floor:

1. The §3 isolation suite green in CI (assertions, seeded leak, static
   scope check).
2. All existing CI checks green unmodified — the interview path provably
   untouched.
3. Round-loop contract tests: floor/cap enforcement, no-self-repeat,
   governed-route rounds, selector fallback, resume mid-round across two
   store instances (the Artifact-3 resume discipline, extended to rounds).
4. A live table smoke run — **only with Mark's explicit per-run
   authorization**, per the standing rule, with its report checked in under
   `engine/m4/reports/`.
5. Registry state gating is out of scope here but recorded: worlds sit at
   `built`; Table sessions inherit whatever state gate the engine applies
   to interviews at the time (currently none — the 2026-08-26 finding), and
   this artifact must not become the reason that gap's fix regresses.
