# Built-World Voice Alignment — Decision Log

Dated entries: what was decided (or is still open), the reasoning, and
the next action.

## 2026-09-17 — Workstream opened

Mark's charter: one consistent, human, participant-facing voice across
every touchpoint between browsing the site and a conversation with a
Representative. First concrete task: locate where each of the 8 built
worlds' conversation-opening introduction actually lives — the launch
prompt guessed it was authored per world somewhere under `worlds/<code>/`.

**Finding, not the guess:** there is no per-world opening line. Every
world's literal first conversation line is one shared, hardcoded
Facilitator template (`DOOR` in `engine/m4/facilitator_turns.py`),
deliberately not world-voice ("the Facilitator speaks for the system,
not for a world... a fixed table, never a prompt") and already
Mark-approved (2026-08-25). The real per-world, threshold-facing text
sits one screen earlier: the **Arrival screen**
(`cic-poc/frontend/src/components/Arrival.tsx`), rendering
`doorway_description` and `thinness_statement` straight from each
world's `records/worlds/<code>.yaml`. Touchpoint 4 revised to this.

Full findings and the touchpoint map: artifact `The Fourth Touchpoint`
(https://claude.ai/artifact/7N2wpobk9VbUhLG1VLzJ5u).

## 2026-09-17 (same day) — DOOR's own words didn't align; fixed

Mark's ruling on the DOOR mechanism itself: "it is fine to come from the
facilitator, but the words of the facilitator should align with the text
the world has." Concrete defect found: DOOR's world-name slot was fed
each world's scholarly `display_name` (e.g. "Imperial and Juridical
Christianity"), never the plain `card_name` every other participant-
facing surface uses ("Church and Empire") — a mismatch across 7 of the 8
built worlds. Mark picked the data-source swap (registry `card_name`
over compiled `display_name`, falling back only for the non-participant-
facing `fix` fixture). Shipped same day: `engine/m4/facilitator_turns.py`,
`engine/api/wiring.py`, `engine/api/table_wiring.py`, new regression
coverage in `engine/m4/tests/test_facilitator_turns.py`. Full detail
logged in `Ministry/Technology/CiC_FrontEnd_Decision_Log.md` alongside
DOOR's original approval (git commit on
`claude/amazing-lovelace-coy644`).

## 2026-09-17 (later) — Doctrine field: Atlas-owned, not in scope yet

PR #246 (Atlas/Church Family Tree thread) adds a structured `doctrine`
field (belief-statement objects, not prose) to 6 of the 8 built worlds'
Atlas entries. Asked Mark whether this thread shares ownership of it or
leaves it entirely to the Atlas thread.

**Mark's ruling:** it's an Atlas entry this thread *can* draw on "if
there is a place that it helps the participant in knowing what to ask" —
but "maybe not yet." Reading: `doctrine` stays Atlas-owned data; this
thread doesn't edit or take responsibility for it. A future touchpoint
that helps a participant formulate questions (most plausibly the
Arrival screen's `starters`, or the "More information" page) could draw
on it, but that's not scoped into current work — tracked here as an open
possibility, not a task.

### Next action

Audit touchpoints 1–3 (homepage tile, Atlas panel, tradition page)
across all 8 built worlds against `CiC_Prose_Craft_Analysis.md`'s craft
rules and CLAUDE.md's accessible/rigorous bar. Surface concrete findings
(specific defects with a proposed diff, not vague "could be tighter")
before drafting any replacement copy, per the same divergent-then-rule
pattern touchpoint 4 went through.
