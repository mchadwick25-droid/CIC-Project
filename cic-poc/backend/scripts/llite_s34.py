"""S3.4 L-lite mini-battery + B-COST call-count measurement.

One scripted live conversation per world (real API, plain endpoint, the
full pipeline incl. the cross-encoder and the retained guard vote), two
turns each, with an expected-behavior column per world - committed as a
battery, not a free-form spot check. Desert's second turn is the
DES-TH-06 shape on purpose: the harness's pessimistic bracket cannot
show the guard vote doing its job (it assumes all votes retrieve), so
the live run is where the beyond-Sarah guard's real behavior is proven.

B-COST delta: a logging handler captures every log_llm_usage record
during the run and counts calls per label per turn - the measured (not
asserted) replacement for the 2 removed relevance-filter calls per
world per turn: `retrieval_filter_lexicon/story` should be ZERO, and
`negative_condition_lexicon/story` appears only when a relevance-kept
candidate actually carries an evaluable guard.
"""
from __future__ import annotations

import json
import logging
import sys
import threading
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from fastapi.testclient import TestClient

from app.main import app

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else BACKEND / "llite_s34.jsonl"

# (world_id, [(turn_label, message, expected_behavior)])
BATTERY = [
 ("post-apostolic-house-church", [
   ("PAHC-1", "What happened when your communities gathered for the meal?",
    "In-character answer drawing on the eucharistic-gathering material "
    "(their Primary gravity G07); no Facilitator intercept."),
   ("PAHC-2", "Say more about that shared meal - was it the same everywhere?",
    "Continues on the meal WITHOUT re-injecting the identical chunk "
    "(session exclusion set holds); names variation honestly (G07 is "
    "variation-and-convergence)."),
 ]),
 ("syriac-edessa-nisibis", [
   ("SYR-1", "What is the qyama?",
    "Verbatim-term hit: defines the covenant (qyama) in-voice - the "
    "lexical path working on a native term."),
   ("SYR-2", "Did you sing your teaching? Tell me about the madrasha.",
    "The madrasha term (force_llm_vote flagged, guard-carrying) "
    "retrieves when genuinely on-topic - the guard vote retrieving, "
    "not skipping, on a direct ask."),
 ]),
 ("desert-monasticism", [
   ("DES-1", "Why did you leave ordinary village life for the desert?",
    "Anachoresis material in-voice; withdrawal-as-formation, not "
    "escape."),
   ("DES-2", "Were there women living this life in the desert too?",
    "THE TH-06 PROOF CASE: the vetted Sarah story surfaces (her answer "
    "to the elders may be told); the two allusion-only amma records are "
    "guard-SKIPPED by the live vote (their own beyond-Sarah scope) - "
    "honest thinness named, no invented texture."),
 ]),
 ("hieronymian-ascetic-literary", [
   ("HAL-1", "Why translate from the Hebrew instead of the Greek?",
    "Hebraica veritas material in-voice; the translation-principle "
    "answer."),
   ("HAL-2", "Who paid for all this work of yours?",
    "Patronage material (their Primary G3) - the world's own "
    "authority-structure honesty."),
 ]),
 ("alexandria-catechetical", [
   ("ALX-1", "What is theosis?",
    "Verbatim-term hit on theosis; in-voice definition (deification "
    "without dissolution register)."),
   ("ALX-2", "Is allegorical reading legitimate, or just arbitrary?",
    "Allegory/rule-of-faith material; the school's own answer to the "
    "arbitrariness charge."),
 ]),
 ("imperial-juridical-christianity", [
   ("IJC-1", "Why did the emperor get involved in church disputes at all?",
    "Church-state alliance material (Primary 2) in-voice."),
   ("IJC-2", "Could a bishop ever say no to the emperor?",
    "Episcopal-independence material (Supporting 4, the Ambrose shape) "
    "- the limits side of the alliance."),
 ]),
]


class UsageCounter(logging.Handler):
    def __init__(self):
        super().__init__()
        self._records_lock = threading.Lock()  # never shadow Handler.lock
        self.counts: list[dict] = []
        self.current: dict[str, int] | None = None

    def start_turn(self):
        with self._records_lock:
            self.current = {}
            self.counts.append(self.current)

    def emit(self, record):
        msg = record.getMessage()
        if "label=" not in msg:
            return
        label = msg.split("label=")[1].split()[0]
        with self._records_lock:
            if self.current is not None:
                self.current[label] = self.current.get(label, 0) + 1


def main() -> None:
    counter = UsageCounter()
    logging.getLogger("cic.llm_usage").addHandler(counter)

    client = TestClient(app)
    with OUT.open("w", encoding="utf-8") as f:
        for wid, turns in BATTERY:
            r = client.post("/api/session/start", json={"world_id": wid})
            r.raise_for_status()
            sid = r.json()["session_id"]
            print(f"[{wid}] session {sid[:8]}")
            for label, msg, expected in turns:
                counter.start_turn()
                resp = client.post(f"/api/session/{sid}/message",
                                   json={"message": msg})
                resp.raise_for_status()
                data = resp.json()
                msgs = data["messages"]
                idx = max(i for i, m in enumerate(msgs) if m["role"] == "user")
                new = [{"name": m.get("name"), "content": m["content"][:2000]}
                       for m in msgs[idx + 1:]]
                rec = {"world": wid, "label": label, "sent": msg,
                       "expected": expected, "responses": new,
                       "llm_calls": dict(counter.current or {})}
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
                calls = ", ".join(f"{k}={v}" for k, v in
                                   sorted((counter.current or {}).items()))
                print(f"  {label}: calls[{calls}]")
    print(f"battery transcript: {OUT}")


if __name__ == "__main__":
    main()
