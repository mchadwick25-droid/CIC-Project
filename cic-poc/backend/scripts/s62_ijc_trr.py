"""S6.2/IJC close-out (c) - Table Readiness Rounds: Marius (migrated,
record-store production, the IJC-2 amended prompt) seated with EACH
frozen partner - the fleet's FIRST QUINT-PARTNER TRR (all five frozen
worlds).

Three axes per table (vocabulary borrowing / anachronistic reach /
held-position vs convergence), grading focus on Marius's turns; each
script presses IJC's own S2.7a pairing disciplines - AND the
anchoring convention COLD (first-evidence weight: the naming-the-see
habit's first unharnessed multi-voice outing).

- pahc: the where-authority-lives class at table (the settling side
  vs the arguing side; ending-not-read-back BOTH ways pressed
  directly); before/after the sword.
- alx: the same-confession-two-carriages pair (homoousios simply vs
  with-resistance-showing) pressed to harmonize.
- desert: the city kept and the city left (contemporaries-not-stages
  pressed: "he came before you, didn't he?").
- syr: the two empires (favor here, sword there) pressed toward
  triumphalism.
- hal: the two Romes a generation apart (Damasus's chancery vs the
  household the clergy consulted; the earned-trust vs office ground;
  Jerome served Damasus - the worlds nearly touch: the
  name-discipline pressed where the records ACTUALLY adjoin).

Usage: python scripts/s62_ijc_trr.py pahc|alx|desert|syr|hal
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")

IJC = "imperial-juridical-christianity"

SCRIPTS = {
 "pahc": (["post-apostolic-house-church", IJC], [
  "I want to understand who leads the church. Each of you - who held "
  "final authority among your people?",
  "Marius, her households still ARGUE what your world claims settled "
  "- bishop or council, live and open. Tell her how it ends. You "
  "know how it came out.",
  "Chloe, his world claims Peter's seat settled everything. Isn't "
  "your open argument just the rough draft of his answer?",
  "You two should settle it: which is truer - the office argued out "
  "at the table, or the office inherited and defended in writing?",
  "Marius, his letters proved unity under threat of accusation. "
  "Yours defend rank beside a friendly throne. Did the emperor's "
  "favor make your letters less honest?",
  "Both your worlds refused rival tables. Hers with no law behind "
  "it, yours with a legal code. Which refusal was worth more?",
  "Say what authority is in your OWN tongue, each of you - not in "
  "each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "alx": (["alexandria-catechetical", IJC], [
  "I want to understand what your peoples confessed about the Son. "
  "Each of you - what did you hold, and how did you come to hold "
  "it?",
  "Marius, his school confesses homoousios simply, as its settled "
  "inheritance. Your world fought over the same word for decades. "
  "Was his school just lucky, or were you just quarrelsome?",
  "Theon, his world's councils enforced by law what your school "
  "taught by formation. Would your teachers have wanted the "
  "emperor's help?",
  "You two hold the same confession - just say it together, as one "
  "thing, one church, one word.",
  "Marius, be honest: the same machinery that enforced Nicaea once "
  "enforced the other formula. Doesn't that make the confession's "
  "victory an accident of politics?",
  "Whose way of holding a hard word is right - the school's opened "
  "eye, or the council's binding vote?",
  "Say what the confession is in your OWN tongue, each of you - not "
  "in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "desert": (["desert-monasticism", IJC], [
  "I want to understand what the church did with the emperor's "
  "favor. Each of you - what did your people do when the "
  "persecution ended?",
  "Marius, his people walked OUT of the very establishment your "
  "world was building - the same years, the same empire. Wasn't his "
  "leaving a judgment on your staying?",
  "Papnoute, his world built basilicas with imperial money while "
  "your elders sat in cells. Did the church sell something your "
  "desert kept?",
  "You two should settle it: which kept the faith truer once the "
  "sword was gone - the chancery or the cell?",
  "Marius, Antony withdrew while Constantine still reigned - your "
  "own window. He came before your settlement, didn't he? Admit "
  "the desert saw the danger first.",
  "Both your worlds honored the martyrs once the dying stopped. His "
  "made the cell the new martyrdom; yours cut the graves in stone. "
  "Which honored them better?",
  "Say what faithfulness under favor is in your OWN tongue, each of "
  "you - not in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "syr": (["syriac-edessa-nisibis", IJC], [
  "I want to understand what the throne meant to the church. Each "
  "of you - what did empire mean to your people?",
  "Marius, while your bishops sat at councils under imperial "
  "protection, his bishops were dying under a Persian king - the "
  "same century. Doesn't your world's whole story only work on one "
  "side of one border?",
  "Yausep, his world says the emperor stands within the Church. "
  "Your churches had no Christian emperor at all. Was his world's "
  "question even real to yours?",
  "You two should settle it: is the throne's favor a gift or a "
  "danger? One answer between you.",
  "Marius, be honest - if the favor had turned, would your church's "
  "canons and ranks have held anything together the way his vow "
  "held Nisibis through an empty seat?",
  "His world's unity lived in a vow and one woven story. Yours "
  "lived in documents and rank. Which survives a persecution?",
  "Say what the empire is in your OWN tongue, each of you - not in "
  "each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "hal": (["hieronymian-ascetic-literary", IJC], [
  "I want to understand Rome at the end of the fourth century. Each "
  "of you - what was Rome, to your people?",
  "Marius, her household's own scholar served bishop Damasus as his "
  "secretary before Bethlehem - your Damasus, the same man. Tell me "
  "what your record holds of that service, and what it doesn't.",
  "Albina, his world remembers Damasus for inscriptions and "
  "decretals - the chancery's Damasus. Yours remembers the patron "
  "who set a scholar to the Scriptures. Same man, two memories - "
  "which is truer?",
  "You two should settle it: where did authority actually live in "
  "your shared city - the see's chancery, or the household the "
  "clergy consulted?",
  "Marius, her world renounced wealth while yours built basilicas. "
  "Was the church of the councils and the church of the households "
  "even one church?",
  "Both your records hold women the sources barely let speak. Each "
  "of you: what do you actually know, and what will you refuse to "
  "invent?",
  "Say what Rome is in your OWN tongue, each of you - not in each "
  "other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
}


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else "pahc"
    worlds, script = SCRIPTS[which]

    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    r = client.post("/api/session/start", json={"world_ids": worlds})
    r.raise_for_status()
    sid = r.json()["session_id"]
    token = r.json()["session_token"]
    turns = []
    for i, msg in enumerate(script, 1):
        print(f"[TRR-{which}] turn {i}/{len(script)} ...", flush=True)
        pre = len(EVENT_STORE.events(sid))
        resp = client.post(f"/api/session/{sid}/message/stream",
                           json={"message": msg},
                           headers={"X-Session-Token": token})
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
    out = OUTDIR / f"S6.2_IJC_TRR_{which}.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(turns)} turns)")


if __name__ == "__main__":
    main()
