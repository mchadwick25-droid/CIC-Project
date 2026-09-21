# Tour Experience Module — Technical Build Spec (design only, not a build task yet)

**Status: designed for later implementation, per Mark's direction 2026-07-20** — hold
all Hosted Tour work until token reset (Friday 2026-07-24) and, separately, until
the actual tour content (the first real Tour Manifest, per the strategy doc's Handoff
#2) gets the substantial editing pass it needs. This document fills the one gap left
between the strategy doc's architecture concept (§4.4, explicitly "not a build task")
and actual code: a concrete technical plan a build thread can follow directly once
both gates clear. Nothing here creates a branch, touches `cic-poc`, or should be
built now.

**Reads on top of, and does not re-decide:**
`CiC_Tour_Experience_Module_Strategy_V0_3.md` (concept, per-world evidentiary
verdicts, architecture sketch), `CiC_L4_Tour_Manifest_Template_V1_0.md` (the
construction-side authoring artifact), `CiC_Tour_Eligibility_Gate_V1_0.md` (the
per-world qualification procedure). This document is purely the engineering layer:
data models, API surface, state machine, frontend components.

---

## 1. Gating — when this actually becomes buildable

In order, all required:
1. **Increment 1** (long-form transcript, table bar) merged — the tour view's register
   banner and beat position need the new transcript grammar, not the old bubble UI.
2. **Increment 2** (role selection) merged or explicitly waived for tour scope — not a
   hard technical dependency, but the strategy doc's own Task Board entry blocks TR-14
   on both.
3. **At least one real Tour Manifest exists** — Handoff #2 (PAHC/Justin's Sunday
   gathering, Class A), authored against the L4 template, through the same review
   cycle every construction document gets. The existing standalone demo
   (`Hosted-Tour/Design/CiC_Chloe_Tour_Interactive_Demo.html`) is the draft this
   becomes, not a substitute for it — the demo predates the template and was never
   authored against it.
4. **The validation-suite extension** (Handoff #3 — scene-narration probes:
   Generating-under-narration, register-persistence, refusal-list adherence) exists
   and the first Manifest passes it. A tour must not ship on conversational validation
   alone (strategy doc §4.1).

## 2. Backend data model

### 2.1 `cic-poc/backend/app/tour_manifest.py` — new file, mirrors `world_manifest.py` exactly

Same single-source-of-truth pattern already established for worlds (`WorldManifestEntry`
/ `WORLD_MANIFEST` / `_BY_WORLD_ID` / `get_manifest_entry` / `all_world_ids`) — this
file is that pattern applied to tours, not a new architecture:

```python
@dataclass(frozen=True)
class TourBeat:
    beat_id: str                       # e.g. "arrival", "reading", "collection"
    narration: str                     # the Representative's own-voice narration text
                                        # (or narration bounds, if per-run generation
                                        # stays within them — construction-side choice,
                                        # not this spec's to make)
    sourced_elements: tuple[str, ...]   # Source Identification IDs this beat may draw on
    honest_silence: Optional[str]      # the beat's own named silence, if the sources
                                        # require one (e.g. Desert's synaxis threshold)

@dataclass(frozen=True)
class TourManifest:
    world_id: str
    tour_id: str                       # e.g. "pahc-sunday-gathering"
    anchor_chunk_id: str                # e.g. "pahcstory006" — the manifest may not
                                        # cite outside this chunk + named satellites
    tour_class: str                    # "A" or "B" — governs register_banner_text
    register_banner_text: str           # Article 17's visible-confidence rule, applied
                                        # to a mode: Class A -> "A witness's own
                                        # account..."; Class B -> "A reconstruction of
                                        # typical practice..."
    beats: tuple[TourBeat, ...]
    refusal_list: tuple[str, ...]       # scene-specific Do-Not conditions, inherited
                                        # from the anchor chunk's Do-Not-Retrieve-When
                                        # plus tour-specific additions
    invitation_line: str                # in-voice, surfaced by the Representative
    exit_handback_line: str
    visual_assets: tuple[dict, ...]     # empty until a visual pipeline exists (§2.4
                                        # of the strategy doc) — each entry bound to a
                                        # beat + a Native registry row + a caption +
                                        # its own "what this does not show" line

TOUR_MANIFEST: list[TourManifest] = [
    # one entry per qualified world's tour(s) - starts empty; PAHC/Justin's Sunday
    # gathering is the first real entry once Handoff #2 lands
]

_BY_TOUR_ID = {t.tour_id: t for t in TOUR_MANIFEST}
_BY_WORLD_ID: dict[str, list[TourManifest]] = {...}  # a world may have 0+ tours

def get_tour(tour_id: str) -> TourManifest: ...
def tours_for_world(world_id: str) -> list[TourManifest]: ...  # empty list, not an
                                                                 # error, for a
                                                                 # non-tourable world -
                                                                 # the honest-refusal
                                                                 # line is a frontend
                                                                 # concern (§4 below),
                                                                 # not a backend error
```

### 2.2 `ConversationState` additions (`app/graph/state.py`)

```python
tour_active: bool = False
current_tour_id: Optional[str] = None
current_beat_index: int = 0
```

Three fields, same minimal-footprint style as the existing `closing_stage`/
`current_world_id` fields. No new phase value needed — `phase` stays
`"active_encounter"` throughout a tour; tour-ness is orthogonal to phase, same
relationship `closing_stage` already has to `phase`.

### 2.3 Eligibility surfacing — reuses retrieval, not a new classifier

Unlike the frame-breaker / modern-term / epistemology bridges, tour invitation is
**not** a classify-then-route intercept on the participant's message — per the
strategy doc, the invitation is "surfaced by the Representative in-voice when the
anchor chunk's Retrieve-When conditions fire." Concretely: when normal retrieval for
an ordinary turn returns the anchor chunk above the existing relevance threshold,
attach a `tour_eligible: {tour_id}` flag to that turn's `complete` event, alongside the
existing `citations` field. No new LLM call — this rides the retrieval the turn
already does.

### 2.4 New graph module `app/graph/tour_mode.py`

Three functions, no classifier LLM call in any of them (tour entry/exit are explicit
participant UI actions, not natural-language classification):

- `start_tour(state, tour_id) -> ConversationState` — sets `tour_active=True`,
  `current_tour_id=tour_id`, `current_beat_index=0`. Called only from the explicit
  "accept" action (§3.1), never inferred from a message.
- `stream_tour_beat(state)` — streams beat `current_beat_index`'s narration in the
  Representative's voice, using the **mode overlay over the unchanged Permanent
  Prompt** (§4.3 of the strategy doc) rather than a different prompt. Retrieval is
  pinned to the beat's `sourced_elements` only, not the world's full RAG index — the
  strategy doc's "no-new-texture rule" enforced structurally, not by model goodwill.
  Yields the same token/complete event shape as `stream_representative_turn`, plus a
  `beat_index` and `register_banner_text` field on `speaker_start` so the frontend can
  render them without a second request.
- `exit_tour(state) -> ConversationState` — sets `tour_active=False`, clears
  `current_tour_id`/`current_beat_index`. One action, available at every beat, per
  §4.2 — never framed as abandonment.

### 2.5 Q&A drop-out (`main.py` routing)

Per §4.3.4 ("Q&A drops to ordinary mode... the tour never creates a
*reduced-guardrail* state, only an *additional-structure* one"): when `tour_active` is
True and an incoming message is a real question rather than a
"continue"/"next"/"exit" signal, route it through the **existing, unmodified**
classify-then-route chain (frame-breaker → relational-safety → closing → modern-term
→ epistemology-bridge → normal generation) exactly as today, with `tour_active` simply
along for the ride in state. No new intercept, no reduced checks — this is the one
place the spec is emphatic that nothing new should be invented.

## 3. New API surface (`main.py`)

- `POST /api/session/{id}/tour/start` — body `{tour_id}`. The explicit-acceptance
  action (§4.2's "explicit acceptance is required before any mode shift"). Calls
  `start_tour`, streams beat 0 via SSE (reuses the existing `/message/stream`
  event shape: `speaker_start` / `token` / `speaker_end` / `done`, with the two new
  fields on `speaker_start` per §2.4 above).
- `POST /api/session/{id}/tour/next` — advances `current_beat_index`, streams the next
  beat. No body needed.
- `POST /api/session/{id}/tour/exit` — calls `exit_tour`. Returns to ordinary
  conversation state; the Facilitator's handback line (`exit_handback_line`) streams
  once, Facilitator-voiced, same shape as the existing bridge modules.
- **No changes to `/api/session/{id}/message/stream`** beyond reading `tour_active`
  for the Q&A drop-out in §2.5 — the tour has its own narrow surface rather than
  overloading the general message endpoint.

## 4. Frontend (`cic-poc/frontend/src`)

- **`TourInvitationCard`** — new component, the T3 contextual-card slot's tour variant
  (per the Full UX Design's own T3 priority: safety/close ▸ tour invitation ▸
  next-questions). Renders when a turn's `complete` event carries `tour_eligible`.
  Consent-explicit: "\[Take the tour\] \[Not now\]" — declining is final for the
  session, never re-offered unprompted (§4.2).
- **Tour view additions to `TheTable.tsx`** — three persistent elements once
  `tour_active`: the **register banner** (Class A/B text, per §2.1's
  `register_banner_text`, rendered exactly as designed — never abbreviated, since it
  IS the visible-confidence disclosure), a **beat position indicator**, and an
  **Exit** action always on screen (one action, every beat, per §4.2).
- **World-selection surface** gains the tours-available / honest-refusal line per
  world (`tours_for_world(world_id)` — an empty list renders the honest refusal copy,
  not an absent affordance; the strategy doc treats a thin world's tour-absence as a
  finding to state, not a gap to hide).
- **No new SpeakerName/message-role types needed** — a tour beat is a Representative
  turn like any other; only the two new annotation fields (`beat_index`,
  `register_banner_text`) are additive to the existing `speaker_start` handling
  already in `useConversation.ts`.

## 5. What this spec deliberately does not decide

- The actual beat content for any tour — that's Handoff #2's construction-side work,
  gated on the content-editing pass Mark named, not an engineering question.
- The validation-suite extension's actual probe wording — Handoff #3, a
  Facilitator-governance question, not an architecture one.
- Whether audio ships — already ruled (§2.7 of the strategy doc: performative
  moments only, Syriac decided, others deferred); this spec adds no audio pipeline
  because none is needed yet.
- Visual assets beyond the empty `visual_assets` tuple — Handoff #4, "separate,
  funding-adjacent," per the strategy doc.

## Document Log

- **V0.1 DRAFT (2026-07-20):** first edition, written to close the gap between the
  strategy doc's architecture concept and an actual build plan, explicitly for later
  implementation — no code, no branch, matches the strategy doc's own "not a build
  task" framing for §4.4 but takes it one concrete layer further. Requested by Mark:
  "design for later implementation" while Hosted Tour work overall stays deferred to
  Friday 2026-07-24 and the content-editing project it depends on.
