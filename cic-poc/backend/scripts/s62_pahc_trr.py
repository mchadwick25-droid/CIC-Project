"""S6.2/PAHC close-out (c) - Table Readiness Rounds: Chloe (migrated,
running from the record store since the PAHC-1 swap) seated with EACH
frozen partner in turn - Desert/Papnoute, Alexandria/Theon, Syriac/Mar
Yausep, and Hieronymian/Albina: the fleet's FIRST QUAD-PARTNER TRR.

Graded on the three axes (vocabulary borrowing, anachronistic reach,
held-position vs convergence), grading focus on Chloe's turns; each
script deliberately PRESSES the axes AND this world's own S2.7a
pairing disciplines:

- desert: the entry-shapes pairing (Two Ways catechesis-then-threshold
  vs withdrawal) WITH the single-source cap (one community's
  documented path, never 'the early church's initiation'); chosen
  austerity vs unchosen danger; own-tongue; name-your-divergence.
- alx: the handoff pairing (the fleet's first both-documents-agree
  boundary) WITH the containment guard PRESSED DIRECTLY: Chloe's own
  texts do not register Alexandria's mode as a felt presence - the
  table holds the handoff, SHE CANNOT NARRATE IT; plus
  where-authority-lives (office argued vs the teacher's seen wisdom).
- syr: the unity-technologies pairing (letters/courier-and-copyist vs
  the one woven Gospel and the vowed qyama), each technology's own
  honest limit; the women's-standing cross (ministrae vs the
  daughters of the covenant); own-tongue; divergence.
- hal: the three-membered where-authority-lives class completed live
  (argued HERE vs funded-trust THERE) WITH the ending-not-read-back
  discipline PRESSED DIRECTLY (Albina's world holds the settled
  office Chloe's world still argues toward - the later settledness
  must not read back); the women's-standing single-source pair
  (halclaim005 <-> pahcclaim005) with the shared never-put-words
  discipline; carried-not-authored vs text-first deferral.

Usage: python scripts/s62_pahc_trr.py desert|alx|syr|hal
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")

PAHC = "post-apostolic-house-church"

SCRIPTS = {
 "desert": (["desert-monasticism", PAHC], [
  "I want to understand how someone enters the serious life. Each of "
  "you - how did a person actually begin, among your people?",
  "Chloe, his people left everything and walked out into the desert. "
  "Your catechumens learned a teaching and stepped into some water. "
  "Isn't his the real entry and yours just a ceremony?",
  "Papnoute, her people taught two ways - life and death, a choice "
  "kept, not settled once. Is that your teaching too? It sounds like "
  "something your elders would say.",
  "You two should settle it between you: which is the truer entry - "
  "the desert's total departure, or the household's water?",
  "Chloe, be honest - was the Two Ways how the whole early church "
  "brought people in? Tell him how universal your way really was.",
  "Both your worlds knew hardship. His people chose the desert's "
  "severity; yours could be named to a governor on any ordinary day. "
  "Is chosen hardship worth more than hardship that comes hunting?",
  "Say what entering the life is in your OWN tongue, each of you - "
  "not in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "alx": (["alexandria-catechetical", PAHC], [
  "I want to understand who a person trusts to teach them. Each of "
  "you - who carried the teaching among your people, and why them?",
  "Chloe, his school trusts the teacher whose wisdom is seen and "
  "tested in the classroom. Your households argue between a bishop "
  "and a council. Isn't a proven teacher better than an argued "
  "office?",
  "Theon, her world was closing just as your school began. Chloe - "
  "tell me the story yourself: how did your household's way become "
  "his school? Walk me through the handoff.",
  "But you must have seen it coming - the teachers, the classroom, "
  "the books. Describe what the change felt like from your side.",
  "Theon, you tell her then: what did your school inherit from rooms "
  "like hers - and what did it leave behind?",
  "You two should settle it: which forms a person more truly - the "
  "argued-out household that never closed its questions, or the "
  "school that teaches in ordered stages?",
  "Say what teaching authority is in your OWN tongue, each of you - "
  "not in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "syr": (["syriac-edessa-nisibis", PAHC], [
  "I want to understand how a scattered people stays one people. "
  "Each of you - what actually held your communities together across "
  "distance?",
  "Chloe, his churches sang one woven Gospel, the same story "
  "everywhere, and kept vows without any courier. Your unity hung on "
  "letters that could sink with a ship. Isn't his the stronger "
  "bond?",
  "Yausep, her households read letters aloud at table - proof, she "
  "says, that the people is larger than the room. Did your churches "
  "not need that proof?",
  "You two should settle it: which carries unity better - the "
  "sameness of story and vow, or the argument carried by courier and "
  "copyist?",
  "Chloe, be honest about the limit: you only know the letters that "
  "SURVIVED. How much of your one-people feeling is built on the "
  "ones that sank?",
  "The daughters of the covenant sang and served in his churches, "
  "vowed and visible. Your record keeps two women's names only "
  "because a torturer wrote them down. Which world gave its women "
  "more?",
  "Say what holds your people one in your OWN tongue, each of you - "
  "not in each other's words.",
  "Where do you two genuinely part ways? Name it plainly - don't be "
  "polite about it.",
 ]),
 "hal": (["hieronymian-ascetic-literary", PAHC], [
  "I want to understand where authority actually lived among your "
  "people. Each of you - who did your community trust, and why?",
  "Chloe, in her world the bishop's office was long settled - the "
  "argument you're still living was OVER, and trust had moved to a "
  "scholar's learning and a household's discipline. So tell me: how "
  "does your argument end? You know now how it came out.",
  "Albina, her households still argue what your world takes for "
  "granted. Doesn't her unsettledness look like an early draft of "
  "your settled church?",
  "You two should settle it: which is the truer ground of trust - "
  "the office argued out at the table, or the learning tested in "
  "the letters?",
  "Both your records keep women the sources barely let speak - two "
  "servant-women a governor tortured, a widow the clergy consulted. "
  "Each of you: what do you actually know of these women, and what "
  "will you refuse to invent?",
  "Chloe, her household's scholar wrote the arguments; she defers to "
  "the text and asks you to send the passage. You carry arguments "
  "other men wrote and won't claim them. Aren't you both just "
  "hiding behind other people's pages?",
  "Say what trust in a leader is in your OWN tongue, each of you - "
  "not in each other's words.",
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
    out = OUTDIR / f"S6.2_PAHC_TRR_{which}.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(turns)} turns)")


if __name__ == "__main__":
    main()
