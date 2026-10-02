# Known gaps at `baseline/pilot-2026-08-24`

Routed out of `engine/BASELINES.md` during the "hoarder house" live-surface
cleanup (`tools/check_live_commentary.py`) — this is provenance about the
pinned baseline commit, not current engine behavior.

At commit `8b23f46e` ("Give the four dead routes an answer"), two wiring
gaps were live and deliberately left in place:

1. **`bridge_turn` was unreachable.** The reader prompt told the model to
   invent `term_id`; `engine/m5/routing.py` matched those against fleet
   record ids. Nothing mapped between them.
2. **`etic_turn` was unreachable.** `escalation_pressed` was declared in
   `engine/m4/events.py` and folded in `engine/m4/projection.py`, but
   appended by nothing — so `SessionState.pressed` was permanently `{}`.

Both were wiring, not turn content; both were proven live at this
baseline's state, and both were fixed after it, not in it. (As of this
routing pass, `engine/m5/routing.py` does return `bridge_turn` for
anachronistic-modern-term routing, confirming gap 1 is resolved.)
