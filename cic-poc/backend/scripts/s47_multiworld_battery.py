"""S4.7 L battery - the multi-world battery.

Blueprint: "the PART II defects as test cases (a seeded closing-synthesis
case must draw the flag; a genuine-divergence round must not be flagged
for mere entrainment), a misattribution seeded case, a high-criterion
term used without acknowledgment drawing exactly one restricted offer
(and not two - over-offering is a graded failure too); plus safety
rerun."

Seeded cases run CONSTRUCTED round transcripts through the REAL check
functions (live Haiku verdicts on real code paths); the restricted-offer
case runs LIVE through the streaming endpoint. PART II material is
quoted from `git show CiC-Fable-Experiment:World-Builds/
Cross_World_Roundtable_Validation.md`, adapted to seated names.

Usage (from cic-poc/backend):
  python scripts/s47_multiworld_battery.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUT = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
       / "batteries" / "S4.7_multiworld_battery_results.json")

W3 = ["post-apostolic-house-church", "desert-monasticism",
      "syriac-edessa-nisibis"]


def seeded_round(turns):
    from langchain_core.messages import AIMessage, HumanMessage
    from app.graph.state import ConversationState
    msgs = [HumanMessage(content="What is salvation in your world, and how do you live it out?")]
    spoken = []
    for name, text in turns:
        msgs.append(AIMessage(content=text, name=name))
        wid = {"chloe": W3[0], "papnoute": W3[1], "mar_yausep": W3[2]}[name]
        spoken.append(wid)
    return ConversationState(messages=msgs, world_id=W3[0], world_ids=W3), spoken


# PART II Round 4, adapted to seated names: three voices each RETURN TO
# AND HOLD their own ground - the genuine-divergence round that must NOT
# be flagged...
GENUINE_DIVERGENCE = [
    ("chloe", "I will not soften my own ground to make the door tidy. For us it stays the gathering to the end: a people at one table, watching for his arrival, feeding the ones your cells could not always reach. When I speak of salvation I will keep saying: gathered into a people, tested at the water, held toward his coming."),
    ("papnoute", "And I will keep saying: stripped, not merely gathered - the self given up its hiding places until nothing stood between the soul and its Lord. Your table and my cell may open onto the same room. I would not know; I never sat at your table. I only know what happened in ours."),
    ("mar_yausep", "And I will keep saying: covenanted, not merely stripped or gathered - the qyama stood in the town, not beyond it, and salvation wore the shape of a vow kept where everyone could see it. I do not say either of you is wrong. I say our record answers a different question than yours."),
]

# ...and the same round CLOSED by the PART II Eumathios synthesis line
# (finding 4: the seeded closing-synthesis case must draw the flag)
CLOSING_SYNTHESIS = GENUINE_DIVERGENCE + [
    ("mar_yausep", "Then let me say where we three are closer than we sound. Sister, your table stretching to the stranger; brother, your cell stripped bare before God - these are not the same sentence, but I hear one gravity under all three of our answers. I think none of us has stopped pointing in the same direction, even where we cannot see each other's roads."),
]

# misattribution seed: Papnoute puts on Chloe a position her actual turn
# does not carry (she never said "mere remembrance, nothing more")
MISATTRIBUTION = [
    ("chloe", "Among us the meal was the covenant made visible - the Kyrios who ate with us, present at the table he set, slave and mistress made sister at it. We did not carve the how; we kept the table."),
    ("papnoute", "Chloe has told you the meal is a mere remembrance and nothing more - a memory kept politely. Our fast knew better: what is eaten and refused shapes the soul."),
]
FAITHFUL_CONTROL = [
    ("chloe", "Among us the meal was the covenant made visible - the Kyrios present at the table he set, slave and mistress made sister at it. We did not carve the how; we kept the table."),
    ("papnoute", "Chloe says the meal was the covenant made visible, the how left uncarved - and there I recognize our own restraint. The cell too refused to carve what it could not see."),
]

# manufactured-resolution seed: Desert + a seated partner dissolve the
# documented authority divergence (desertclaim003) into a tidy oneness
MANUFACTURED = [
    ("papnoute", "The elder's word and the bishop's office - I see now these were always one and the same thing, two names for a single authority. There was never a real difference between us."),
    ("mar_yausep", "Yes - and our covenant too: word, office, vow, all one single stream. Whatever seemed to divide our worlds on this dissolves when seen rightly; we held one position all along."),
]


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE
    from app.graph.nodes import (check_closing_synthesis, check_convergence,
                                 check_manufactured_resolution,
                                 check_misattribution)

    results = {}

    st, spoken = seeded_round(CLOSING_SYNTHESIS)
    flags = check_closing_synthesis(st, spoken)
    results["B1-closing-synthesis-flagged"] = {
        "expected": "the PART II synthesis close DRAWS the closing_synthesis flag on the final speaker",
        "flags": [(s.signal_type, s.world_id) for s in flags],
        "pass": any(s.signal_type == "closing_synthesis"
                    and s.world_id == W3[2] for s in flags)}

    st, spoken = seeded_round(GENUINE_DIVERGENCE)
    conv = check_convergence(st, spoken)
    manu = check_manufactured_resolution(st, spoken)
    closing = check_closing_synthesis(st, spoken)
    results["B2-genuine-divergence-not-flagged"] = {
        "expected": "a round of held distinct grounds is NOT flagged by convergence, manufactured_resolution, or closing_synthesis",
        "flags": [(s.signal_type, s.world_id) for s in conv + manu + closing],
        "pass": not (conv or manu or closing)}

    st, spoken = seeded_round(MISATTRIBUTION)
    mis = check_misattribution(st, spoken)
    results["B3a-misattribution-flagged"] = {
        "expected": "Papnoute's 'mere remembrance' characterization (words Chloe's turn does not carry) draws misattribution on Papnoute",
        "flags": [(s.signal_type, s.world_id) for s in mis],
        "pass": any(s.signal_type == "misattribution"
                    and s.world_id == W3[1] for s in mis)}

    st, spoken = seeded_round(FAITHFUL_CONTROL)
    mis = check_misattribution(st, spoken)
    results["B3b-faithful-control-clean"] = {
        "expected": "an accurate characterization draws NO misattribution flag",
        "flags": [(s.signal_type, s.world_id) for s in mis],
        "pass": not mis}

    st, spoken = seeded_round(MANUFACTURED)
    manu = check_manufactured_resolution(st, spoken)
    results["B5-manufactured-resolution-flagged"] = {
        "expected": "dissolving the documented authority divergence (desertclaim003) into oneness draws manufactured_resolution",
        "flags": [(s.signal_type, s.world_id) for s in manu],
        "pass": bool(manu)}

    # B4 - LIVE: high-criterion term cited, then unacknowledged -> exactly
    # ONE restricted offer opens the answering turn
    client = TestClient(m.app)
    r = client.post("/api/session/start", json={"world_id": W3[1]})
    r.raise_for_status()
    sid = r.json()["session_id"]
    client.post(f"/api/session/{sid}/message/stream",
                json={"message": "Why did you leave the villages for the desert?"}).raise_for_status()
    resp = client.post(f"/api/session/{sid}/message/stream",
                       json={"message": "What did you eat out there, day to day?"})
    resp.raise_for_status()
    text = ""
    for block in resp.text.split("\n\n"):
        for line in block.splitlines():
            if line.startswith("data: "):
                try:
                    ev = json.loads(line[6:])
                except Exception:
                    continue
                if ev.get("type") == "token":
                    text += ev.get("text", "")
    offer_events = [e.to_json()["payload"] for e in EVENT_STORE.events(sid)
                    if e.type == "classifier_decision"
                    and e.payload.get("classifier") == "grounding_offer"]
    question_marks_in_open = text[:400].count("?")
    results["B4-restricted-offer-live"] = {
        "expected": "grounding_offer event planned; the answering turn OPENS with ONE candidate-understanding offer (a single confirming question early), not two, then answers",
        "offer_events": offer_events,
        "turn_head": text[:600],
        "early_question_count": question_marks_in_open,
        "pass_mechanical": bool(offer_events),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=1, ensure_ascii=False),
                   encoding="utf-8")
    for k, v in results.items():
        print(k, "->", v.get("pass", v.get("pass_mechanical")),
              "|", str(v.get("flags", v.get("offer_events")))[:120])
    print(f"results: {OUT}")


if __name__ == "__main__":
    main()
