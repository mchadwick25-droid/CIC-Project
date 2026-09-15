"""S4.4a deterministic fixture half of the L table battery.

The live half (scripts/s44a_table_battery.py) proves the wired behavior
through the real streaming endpoint; THIS half proves the deterministic
mechanisms themselves, including on text the live half cannot force -
most importantly the PART II Round-2 adjacency verbatim-adapted (the
blueprint's named test case, sourced from
`git show CiC-Fable-Experiment:World-Builds/Cross_World_Roundtable_Validation.md`).

Every expected-behavior line carries the governance it is graded
against. FG §8: "When the participant addresses a specific
Representative, you route accordingly. Immediately, completely, without
editorial intervention."

Deterministic; double-run must be byte-identical.

Usage (from cic-poc/backend):
  python <repo>/Ministry/Technology/Pass2/gates/S4.4a_deterministic_fixtures.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[4] / "cic-poc" / "backend"
sys.path.insert(0, str(BACKEND))

W3 = ["post-apostolic-house-church", "desert-monasticism",
      "syriac-edessa-nisibis"]


def run_once() -> dict:
    from langchain_core.messages import AIMessage, HumanMessage
    from app.graph.nodes import (
        TRANSCRIPT_RECENT_WINDOW,
        TRANSCRIPT_STABLE_PREFIX,
        build_public_transcript,
        detect_direct_address,
        detect_rep_to_rep_address,
        outstanding_first_pair_parts,
    )
    from app.graph.state import ConversationState
    import app.main as m

    checks: dict[str, bool] = {}

    # --- direct address (FG §8: route accordingly, immediately,
    # completely, without editorial intervention) ---
    checks["participant_names_one_rep"] = (
        detect_direct_address(
            "Chloe, what did your house-church actually eat at the meal?",
            W3) == "post-apostolic-house-church")
    checks["each_of_you_blocks_short_circuit"] = (
        detect_direct_address("Chloe and each of you - how did you pray?",
                              W3) is None)
    checks["two_names_ambiguous_falls_through"] = (
        detect_direct_address("Chloe or Papnoute, either of you?", W3) is None)
    checks["no_name_falls_through"] = (
        detect_direct_address("How did your communities fast?", W3) is None)
    checks["flag006_economic_question_no_false_address"] = (
        detect_direct_address("Who paid for all this work of yours?", W3)
        is None)

    # --- Rep -> Rep: the PART II Round-2 adjacency, adapted to seated
    # names (original: KIMON to Cordus - "But tell me this, presbyter:
    # does your sign work on a heart still full of thoughts?"). The
    # title-only address ("presbyter") is deliberately below this cheap
    # check's line - adapted here to the named form the detector owns;
    # title-address remains the holistic selector's regime. ---
    part2_adapted = (
        "You speak of a sign that binds. I do not doubt it works as you "
        "say it works, for I was formed differently. But tell me this, "
        "Mar Yausep: does your covenant hold a heart still full of "
        "thoughts? Among us the water only began the war.")
    checks["part2_adjacency_routes_to_addressee"] = (
        detect_rep_to_rep_address(part2_adapted, "desert-monasticism", W3)
        == "syriac-edessa-nisibis")
    checks["statement_only_turn_no_route"] = (
        detect_rep_to_rep_address("We held the fast. It was our way.",
                                  "desert-monasticism", W3) is None)

    # --- outstanding first pair parts (Pass 1 §6.2 item 4) ---
    msgs = [
        HumanMessage(content="How did each of you understand prayer?"),
        AIMessage(content=("Prayer was the church's breath. Chloe, was it "
                           "so among your houses?"), name="papnoute"),
        AIMessage(content="It was. We prayed the meal itself.", name="chloe"),
        AIMessage(content="And the psalms held us. What drew you to ask this?",
                  name="mar_yausep"),
    ]
    out = outstanding_first_pair_parts(msgs, W3)
    checks["answered_in_round_does_not_stack"] = (
        len(out) == 1 and out[0]["addressee"] == "participant")
    checks["participant_reply_resolves"] = (
        outstanding_first_pair_parts(
            msgs + [HumanMessage(content="Just curiosity.")], W3) == [])

    # --- block truncation with stable prefix ---
    short = build_public_transcript(
        ConversationState(messages=msgs, world_ids=W3))
    checks["short_conversation_rendered_whole"] = "not shown" not in short
    long_msgs = [HumanMessage(content="Opening frame question?"),
                 AIMessage(content="First answer.", name="chloe")]
    long_msgs += [AIMessage(content=f"Turn {i}.", name="papnoute")
                  for i in range(14)]
    t = build_public_transcript(
        ConversationState(messages=long_msgs, world_ids=W3))
    lines = t.split("\n\n")
    checks["stable_prefix_pinned"] = (
        lines[0].startswith("Participant: Opening frame")
        and lines[1].startswith("Chloe: First answer"))
    checks["elision_marker_counts_hidden_turns"] = (
        "[... 4 earlier turn(s) not shown ...]" in lines[2])
    checks["window_shape_exact"] = (
        len(lines) == TRANSCRIPT_STABLE_PREFIX + 1 + TRANSCRIPT_RECENT_WINDOW)

    # --- F9: the floor read from wrs/parameters.yaml (M3 pending ->
    # value 2, the per-round floor still in force) ---
    checks["floor_read_from_parameters_yaml"] = (
        m._multi_world_turn_floor() == 2
        and m._TURN_FLOOR_MULTI_WORLD == 2)

    return {"checks": checks,
            "gate": "PASS" if all(checks.values()) else "FAIL"}


def main() -> int:
    r1, r2 = run_once(), run_once()
    s1, s2 = (json.dumps(r, sort_keys=True) for r in (r1, r2))
    print(json.dumps(r1, indent=1))
    print(f"\ndouble-run byte-identical: {s1 == s2}")
    print(f"GATE: {r1['gate']}")
    return 0 if (r1["gate"] == "PASS" and s1 == s2) else 1


if __name__ == "__main__":
    sys.exit(main())
