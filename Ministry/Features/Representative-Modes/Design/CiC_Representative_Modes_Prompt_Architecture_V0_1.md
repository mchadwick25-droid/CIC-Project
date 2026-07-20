# Representative Modes — Prompt Architecture V0.1

**Status:** Draft for Mark's review; implemented on the exploration branch
`claude/representative-modes-exploration` (see the Integration Assessment for the
exact touch surface). Canonical injected text lives in
`cic-poc/backend/app/prompts/role_modes.py` — a versioned, reviewed prompt document
in the same discipline as `table_discourse.py`, not an inline literal. This document
specifies the architecture; that file is the text of record.

---

## 1. The shape in one paragraph

Role is a **session-start parameter** (`role`, optional, one of `general` /
`pastor-teacher` / `academic` / `deconstructing`) that flows: onboarding/selection UI
(or the `role=` URL parameter on the map-handoff contract) → `POST /api/session/start`
→ validated → held on `ConversationState.participant_role` → at every
Representative prompt assembly, resolved to a **facilitation-layer guidance block**
injected as its own segment of the system prompt. The block tells the Representative
**who is listening and what serves them** — it never tells the Representative to
simplify the truth or to be more academic than it is. Omitted role = no block = the
running system's exact current behavior.

This follows the system's own precedent exactly: `table_discourse.py` already proves
that conversation SHAPE is tuned in the prompt-assembly layer, as situation-scoped
guidance identical across representatives, without touching representative identity.
The role block is the same move with a different situational axis: table size there,
listener here.

## 2. Where the role block sits in the prompt (and why)

`build_representative_prompt` currently returns three segments, each with its own
Anthropic prompt-caching role:

1. `static_prompt` — permanent prompt + world capsule + `_HOW_YOU_ENGAGE`;
   byte-identical every turn for a representative; own cache breakpoint.
2. `reactive_guidance_block` — table-discourse guidance; conditionally present;
   byte-identical when present; own cache breakpoint.
3. `dynamic_prompt` — retrieval, reroot, public transcript; changes every call;
   never cached.

The role block becomes a **fourth segment with its own cache breakpoint, inserted
between (1) and (2)**:

```
[ static_prompt | cache ] [ role_block | cache, when role set ] [ reactive block | cache, when present ] [ dynamic ]
```

Reasons, in order of importance:

- **Identity stays pristine.** The block is physically outside the permanent prompt
  and world capsule. Nothing about the Representative's formation is edited per role;
  the diff to what the Representative *is* is zero.
- **Cache-correct.** The block is session-constant and byte-identical per role across
  every representative, every session, every turn — the best possible cache shape.
  Folding it into `static_prompt` would fork that block's cache key per role and cost
  a re-bill of the largest segment for every distinct role in a cache window;
  mixing a sometimes-present block into an always-present one is exactly what the
  existing `_cached_system_message` docstring warns against.
- **Ordering carries meaning.** The Representative reads who it is, the world it
  inhabits, and how it engages *before* it reads who is listening — the listener
  context arrives as situational guidance to an already-formed voice, in the same
  position class as the table-discourse guidance, not as a preamble that could color
  identity.

## 3. What the block is allowed to say (the authoring rules)

Binding on any future edit of `role_modes.py`:

1. **Listener-descriptive, never voice-prescriptive.** Every sentence describes who
   has come and what serves them. Test from the Design Spec §3: "who has come to your
   table" passes; "be more X" fails.
2. **Explicit invariant restatement.** Every block (all four) carries the same closing
   paragraph, verbatim, stating: the same things are true in every mode — claims,
   how certain or uncertain each is, tensions your world never resolved; never
   rounder or more settled than your record; anything the participant asks for —
   depth, sources, plainness — they get, whoever they are; and you remain entirely
   yourself. The invariants are IN the prompt, not only around it.
3. **Scoped to offer-order, examples, pacing.** The block may shape what is offered
   first, which kinds of examples serve, and patience/pacing. It may not name length
   targets (the formation's own measure governs), may not add content rules, and may
   not reference the mode's existence as a thing to mention (a Representative
   narrating "since you are an academic, I will…" is self-narration-adjacent drift;
   the block says the listener context is background, never announced).
4. **The deconstructing block additionally carries** the §8c boundary in listener
   terms (no cumulative tilt toward adoption *or* departure), the no-management rule,
   and the honesty-first order — and explicitly does NOT carry safety instructions,
   which belong to the Facilitator's own triggers (Section 5).

## 4. Backend flow, precisely

- `StartSessionRequest.role: str | None = None`. Validation: unknown value → 400
  listing valid ids (same pattern as invalid `world_id`). `None`/absent → fully
  role-less session, current behavior.
- `ConversationState.participant_role: Optional[str]` — session-constant. Role is a
  starting posture; there is no mid-session role switch in this design (the
  participant never needs one: every depth and register is already reachable by
  asking — invariant 2). If a switch is ever wanted, it is a new session-start-shaped
  decision, not a message-level toggle.
- `_prepare_representative_turn` resolves `get_role_guidance(state.participant_role)`
  → passes it to `build_representative_prompt(role_guidance=...)` → returned as its
  own segment → `_cached_system_message` marks it with its own `cache_control`
  breakpoint. Both the non-streaming and streaming paths share this via the existing
  single assembly helper.
- `StartSessionResponse.role` echoes it back so the frontend state and any transcript
  capture record what posture the session ran under (the pilot transcript logger
  picks it up from the session state).

## 5. Interactions with the rest of the facilitation layer

**Facilitator handoff (threshold voice):** the handoff prompt receives a short
role-calibration note (from `role_modes.py`, Facilitator-facing variant) in the same
"Facilitator-Only Awareness — never voiced" section that already carries the world
cautions. Governance §4 is the source: role calibrates how the Facilitator enters the
room, not what room it enters. The note is explicitly non-verbalized — the
introduction never mentions the role.

**Frame-breaker and relational-safety classifiers: deliberately role-blind in this
design.** These are narrow, live-tested components (ten-of-ten classification record
for the frame-breaker pipeline; the relational-safety classifier live-adversarially
tested through two corrected-design rounds). Injecting role context into a tested
classifier silently invalidates its test record — the exact failure mode the
validation suite exists to prevent. Governance §4's "relational safety attention from
the start" for the deconstructing role is carried in this design by (a) the
Representative-facing block's care-and-honesty posture and (b) the Facilitator handoff
note — not by re-tuning classifier thresholds. If Mark wants role-aware classification
(e.g., a lower Track-B accumulator threshold under `deconstructing`), that is a
separate change gated on its own adversarial re-test — flagged in the decision log,
not built here.

**Drift monitoring: role-blind, permanently.** The monitoring prompt judges the
Representative's output against its formation, and role must never become an excuse a
drifted output can hide behind ("it smoothed because the listener was general-mode").
Content invariance is enforced precisely by keeping the judge blind to the mode.

**Lexicon Level-2 offerings:** unchanged in the pilot UI (highlights render for
everyone — the current build is effectively Mode Two for all). When the Mode One/Mode
Two distinction is implemented as a real toggle, governance §4's default rule applies
mechanically: role selected but no transparency mode chosen → Mode One for `general`
and `deconstructing`, Mode Two for `pastor-teacher` and `academic`; participant
override honored immediately, no comment. Role affects the *default posture* of the
apparatus, never its reachability (Article 30). The role block's academic/pastor
variants additionally make the Representative readier to *name* sources in-voice —
which is offer-order, not new apparatus.

**Citation presentation:** the citations block under each message is unchanged and
identical across roles. Academic mode's "more complete technical explanation" is
carried by (a) in-voice source-naming readiness and (b) the existing click-through
apparatus — not by a role-forked citation renderer. One renderer, one truth.

**Closing resources (designed 2026-07-07, not yet built):** when built, role shapes
the *default register of what is offered* — a pastor/teacher is readier to be offered
study material, a deconstructing participant is offered resources with no
institutional pressure and explicit no-strings framing — while remaining
Facilitator-curated in the moment, responsive to what actually came up, ask-never-push
(Article 34). Role never adds pressure to accept resources and never filters what may
be asked for.

**Map-handoff URL contract:** `role=<general|pastor-teacher|academic|deconstructing>`
rides the contract established by the map thread:
`/?worlds=<id,id>&mode=<interview|table>&role=<...>`. Same one-shot semantics as the
other params (parse at module scope, scrub in an effect — the StrictMode lesson from
the map thread's twenty-fifth pass applies verbatim). Unknown value → ignored (no
role), never an error a participant sees. The map branch and this branch touch
different parse sites today; the contract is reconciled at whichever merge lands
second (map log, twenty-sixth pass).

## 6. Failure modes this architecture forecloses

- **A forked truth per role** — foreclosed structurally: one permanent prompt, one
  capsule, one retrieval pipeline, one monitoring judge, all role-blind; role touches
  only a listener-context segment.
- **Role as gate** — foreclosed structurally: no code path reads role to withhold
  anything; role resolves to prompt text only.
- **Silent invalidation of tested components** — foreclosed by policy stated here:
  classifiers and monitoring take no role input on this branch.
- **Cache-cost regression** — foreclosed by the dedicated breakpoint (Section 2).
- **The mode announcing itself** — authoring rule 3 plus a dedicated validation probe
  (leakage probe, Validation Plan §e).
