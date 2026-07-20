# Two design gaps closed — session recovery and the world-count ceiling

**Status: designed for later implementation**, per Mark's direction (same instruction
as the Tour Build Spec — real design work now, no code until later). Both items came
off the Full UX Feature Checklist's "Still needs design work" bucket for Section 9.

---

## 1. Session recovery — narrower and better-understood than the checklist said

**Correction to the checklist's own framing first:** "session data persistence" was
listed as though no persistence design exists at all. That's not quite right — read
directly, `cic-poc/backend/app/transcript_logging.py` already has a real, considered
design: every completed round is upserted to Supabase (`sessions` table: phase,
turn_count, status; `messages` table: append-only, self-healing against partial
writes). It's a no-op only because it's gated behind `settings.pilot_logging_enabled`
and `supabase_configured()` — same root gate as the Accounts/sign-in item, not a
separate open question.

**What's actually still missing:** that module is **write-only**. It builds a durable
audit trail of what happened, but nothing reads it back. The live, in-memory
`sessions: dict[str, ConversationState] = {}` in `main.py` is the only thing that
makes a conversation *continuable* — and it is lost completely on any server restart
or crash, mid-pilot or not. A durable record would survive; the ability for that
participant to keep talking would not. That's the real gap: **session recovery**, not
persistence in general.

**Design (for later implementation):**
1. On a lookup miss in `sessions[session_id]` (currently an immediate 404), attempt a
   rehydration read from Supabase's `sessions`/`messages` tables before failing —
   reconstruct a `ConversationState` from the stored phase/turn_count/world_ids and
   replay `messages` back into LangChain message objects (the inverse of
   `_serialize_message`).
2. Gate this identically to `write_transcript` (`pilot_logging_enabled` +
   `supabase_configured()`) — where those are off, today's behavior (404, start over)
   is unchanged and correct; this is additive, not a rewrite.
3. Rehydration is best-effort and fails open to today's 404 — a participant restarting
   a lost conversation is a worse UX than a 404, never the other way around.
4. **Explicitly out of scope:** recovering *mid-stream* (a connection dropped
   mid-token) — that's a frontend reconnect/retry question, not a backend storage one,
   and the frontend already has its own retry affordance on the input line per the
   design doc.

## 2. The Table's world-count ceiling — a real, still-open policy question

**Confirmed in code, still true today:** `world_ids = request.world_ids[:3]` in
`start_session` caps how many worlds can be *seated in one conversation* — that part
is enforced. What's *not* enforced is the separate, larger claim from the Table
Design Document: that the whole **live portfolio** stays capped (today: 5 deployed
worlds — House-Churches, Syriac, Desert, Bethlehem Circle, Alexandria). Nothing in
code stops a sixth `WorldManifestEntry` from being added to `world_manifest.py`
without a deliberate decision that the ceiling itself should move. Today this is held
entirely by curatorial discipline (Mark's own review before adding an entry), not by
the codebase.

**Design (for later implementation) — mirrors a discipline this codebase already
uses on itself:** `world_manifest.py`'s own docstring names the exact failure category
this is: "a hand-synced list falling out of sync with its own source... exactly the
class of silent bug." The fix pattern that already works elsewhere in this file
(one source of truth instead of five) suggests the same medicine here:

```python
# in world_manifest.py, alongside WORLD_MANIFEST
LIVE_WORLD_CEILING = 5  # bump this deliberately, in the same commit that adds a world

assert len(WORLD_MANIFEST) <= LIVE_WORLD_CEILING, (
    f"WORLD_MANIFEST has grown to {len(WORLD_MANIFEST)} entries without "
    f"LIVE_WORLD_CEILING being deliberately raised - bump the constant in "
    f"the same commit as the new world, or this isn't ready to ship."
)
```

A one-line assertion, run at import time (same place `_BY_WORLD_ID` is already built),
costs nothing and turns "did we mean to do this" into a required, visible decision
instead of a silent one. Not a hard technical limit on the product (the ceiling number
itself is a curatorial/business call, entirely Mark's), just a guarantee that crossing
it is never an accident.

**Alternative considered and not recommended:** a heavier governance gate (e.g.,
requiring a completed Step 0 record before a world can be added to the manifest at
all). Rejected as over-engineering for what is fundamentally a one-line
"did-you-mean-to" check — Step 0 completion is already a real, separate discipline
upstream of this file; duplicating its enforcement here would be redundant, not
additive.

## Document Log

- **V0.1 DRAFT (2026-07-20):** first edition. Both items requested as "design for
  later implementation," same instruction as the Tour Build Spec written earlier the
  same session. No code changes made — this is the plan, not the patch.
