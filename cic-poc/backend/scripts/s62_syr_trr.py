"""S6.2/SYR close-out (c) - Table Readiness Rounds: Mar Yausep (now
migrated, running from the record store since the SYR-1 swap) seated
with EACH frozen partner in turn - Desert/Papnoute and
Alexandria/Theon (the first world to TRR against TWO frozen partners).

Graded on the three axes (vocabulary borrowing, anachronistic reach,
held-position vs convergence), grading focus on Yausep's turns; each
script deliberately PRESSES the axes: convergence invitations (turns
2, 4), vocabulary crossover (turn 3), a probe in-window for one world
and foreign for the other (turn 5), the women-teacher / martyr-value
pressure (turn 6, the ALX FLAG-024 class re-tested on a new table),
own-tongue (turn 7 - the ALX FLAG-019/020 compound's exact former
failure turn), and name-your-divergence (turn 8).

Usage: python scripts/s62_syr_trr.py desert|alx
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")

SCRIPTS = {
 "desert": (["desert-monasticism", "syriac-edessa-nisibis"], [
  "I want to understand the serious vowed life. Each of you - where "
  "does it actually happen for your people?",
  "Papnoute, his covenant people stayed home with their families. "
  "Isn't that just ordinary life with extra rules? The desert costs "
  "everything.",
  "Yausep, tell me about the thoughts. Your companion's people watch "
  "their thoughts like enemies at a gate - do yours as well?",
  "You two should settle it between you: which is the truer askesis - "
  "leaving the world, or refusing it from within?",
  "What about Antony? He heard the Gospel read and left everything. "
  "Did his story reach your towns, Yausep?",
  "Your worlds both watched believers die for the faith. Is a "
  "martyr's death worth more than a long life of prayer?",
  "Say what the vow is in your OWN tongue, each of you - not in each "
  "other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "alx": (["alexandria-catechetical", "syriac-edessa-nisibis"], [
  "I want to understand how Scripture actually forms a person. Each "
  "of you - how does the reading do its work among your people?",
  "Yausep, his answer sounds like it could be yours - you both read "
  "for hidden depths, don't you?",
  "Theon, tell me about singing. Your companion's people sang their "
  "doctrine - did yours as well?",
  "Settle it between you: which is the truer way to read - the symbol "
  "bound to its truth, or the ascent through the text's depths?",
  "What about the Diatessaron - one Gospel woven from four. Theon, "
  "would your school have accepted such a text?",
  "The daughters of the covenant sang Ephrem's hymns in the churches. "
  "Would either of your worlds accept a woman as a teacher?",
  "Say what formation is in your OWN tongue, each of you - not in "
  "each other's words.",
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
        print(f"[TRR-{which}] turn {i}/{len(script)} ...")
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
    out = OUTDIR / f"S6.2_SYR_TRR_{which}.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(turns)} turns)")


if __name__ == "__main__":
    main()
