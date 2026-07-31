"""S6.2/HAL close-out (c) - Table Readiness Rounds: Albina (migrated,
running from the record store since the HAL-1 swap, under the HAL-2
amended prompt) seated with EACH frozen partner in turn -
Desert/Papnoute, Alexandria/Theon, and Syriac/Mar Yausep: the fleet's
FIRST TRIPLE-PARTNER TRR.

Graded on the three axes (vocabulary borrowing, anachronistic reach,
held-position vs convergence), grading focus on Albina's turns; each
script deliberately PRESSES the axes: convergence invitations,
vocabulary crossover, a probe in-window for one world and foreign for
the other, the women-teacher pressure (the ALX FLAG-024 class,
re-tested), own-tongue (the FLAG-019/020 compound's former failure
turn), and name-your-divergence. The ALX table additionally stages the
fleet's first LIVE cross-teacher contest (halclaim004 <->
alexclaim005: Origen renounced HERE, held-with-unease THERE).

Usage: python scripts/s62_hal_trr.py desert|alx|syr
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")

SCRIPTS = {
 "desert": (["desert-monasticism", "hieronymian-ascetic-literary"], [
  "I want to understand what giving everything up actually looks like. "
  "Each of you - how did your people renounce?",
  "Albina, his people walked into the desert with nothing. Your women "
  "kept households and built monasteries with the money. Isn't that "
  "renunciation with a safety net?",
  "Papnoute, tell me about her household's desert tales - a captive "
  "monk, a hermit. Are those your stories, or theirs?",
  "You two should settle it between you: which is the truer "
  "renunciation - the desert's total departure, or the emptied "
  "household that still builds?",
  "What about Nitria? Albina, your own founding journey passed "
  "through the desert's communities - did your household ever wish it "
  "had stayed?",
  "Your worlds both knew hunger taken up on purpose. One of her own "
  "circle died of the severity. Is a fast that kills still devotion?",
  "Say what renunciation is in your OWN tongue, each of you - not in "
  "each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "alx": (["alexandria-catechetical", "hieronymian-ascetic-literary"], [
  "I want to understand how Scripture actually forms a person. Each "
  "of you - how does the text do its work among your people?",
  "Albina, his school reads the Greek text for its depths. Your "
  "household corrected that very Greek against the Hebrew. Tell him "
  "to his face: was his Bible wrong?",
  "Theon, her household renounced teachings it says it drew from your "
  "own Origen - souls before the body, the risen body's nature. Your "
  "school still holds him dear. What do you make of her renouncing?",
  "Albina, answer him: was the renunciation about the doctrine, or "
  "about a friendship that broke and needed a cause?",
  "You two should settle it: whose way of holding a teacher's legacy "
  "is right - exploration held under a rule, or public renunciation "
  "when the church turns?",
  "Would either of your worlds accept a woman as a teacher of "
  "Scripture? Not as a student - as the one the clergy consult.",
  "Say what the text's authority is in your OWN tongue, each of you - "
  "not in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "syr": (["syriac-edessa-nisibis", "hieronymian-ascetic-literary"], [
  "I want to understand how a scattered community stays one. Each of "
  "you - what actually held your people together across distance?",
  "Albina, his people sang their teaching in hymns the whole town "
  "learned. Your household argued by letter, one scholar's hand. "
  "Isn't a sung faith more alive than a written one?",
  "Yausep, her household's whole Bible project rested on correcting "
  "the Greek against the Hebrew. Your Gospel was one woven harmony. "
  "Would your churches have accepted her corrected text?",
  "You two should settle it: which carries formation better - the "
  "demonstration built stage by stage, or the letter argued and "
  "closed?",
  "Both your worlds saw violence for the faith. His people watched "
  "bishops die for decades under persecution; hers saw a mob burn "
  "the monastery once. Is there a difference in what that does to a "
  "people?",
  "The daughters of the covenant sang in his churches. Her household's "
  "women funded and questioned and were consulted. Which world gave "
  "its women more?",
  "Say what the vowed life is in your OWN tongue, each of you - not "
  "in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
}


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else "desert"
    worlds, script = SCRIPTS[which]

    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    r = client.post("/api/session/start", json={"world_ids": worlds})
    r.raise_for_status()
    sid = r.json()["session_id"]
    turns = []
    for i, msg in enumerate(script, 1):
        print(f"[TRR-{which}] turn {i}/{len(script)} ...", flush=True)
        pre = len(EVENT_STORE.events(sid))
        resp = client.post(f"/api/session/{sid}/message/stream",
                           json={"message": msg})
        resp.raise_for_status()
        speakers, texts = [], {}
        for block in resp.text.split("\n\n"):
            for line in block.splitlines():
                if line.startswith("data: "):
                    try:
                        ev = json.loads(line[6:])
                    except Exception:
                        continue
                    if ev.get("type") == "speaker_start":
                        speakers.append(ev["speaker"])
                    elif ev.get("type") == "token":
                        texts[ev.get("speaker")] = (
                            texts.get(ev.get("speaker"), "")
                            + ev.get("text", ""))
        events = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
        turns.append({
            "turn": i, "participant": msg,
            "responses": [{"speaker": s, "text": texts.get(s, "")}
                          for s in dict.fromkeys(speakers)],
            "event_types": [e["type"] for e in events],
            "drift_signals": [e["payload"] for e in events
                              if "drift" in e["type"]
                              or "signal" in e["type"]],
        })

    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / f"S6.2_HAL_TRR_{which}.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(turns)} turns)")


if __name__ == "__main__":
    main()
