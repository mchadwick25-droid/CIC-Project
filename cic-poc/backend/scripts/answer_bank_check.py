#!/usr/bin/env python
"""SH-11 verification: the answer bank (app/answer_bank.py) wired into the
real /message and /message/stream endpoints via FastAPI's TestClient.

No live API key, no network call: MOCK_LLM=true stands in for the LLM (same
as every other check script in this repo), and the lexicon/story retrievers
for the test world are pre-seeded with a fake that skips FAISS/HuggingFace
entirely - real retrieval correctness is redesign_battery.py's job, not
this script's; this script's job is proving the bank's own hit/miss/
fallthrough wiring is correct end to end against the real app.

  python scripts/answer_bank_check.py
"""

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MOCK_LLM", "true")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f" - {detail}" if detail else ""))


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


WORLD = "post-apostolic-house-church"

# ---------------------------------------------------------------------------
section("A. setup - fake retrievers (no FAISS/HuggingFace), a real bank file")
# ---------------------------------------------------------------------------
import app.graph.nodes as nodes_mod  # noqa: E402


class _FakeRetriever:
    def get_context_for_response(self, *a, **kw):
        return "", [], []


nodes_mod._retrievers[WORLD] = _FakeRetriever()
nodes_mod._story_retrievers[WORLD] = _FakeRetriever()
check("fake retrievers seeded for the test world", True)

from app.config import settings  # noqa: E402

BANK_QUESTION = "Walk me through an ordinary day among your people - from waking to sleeping."
BANK_ANSWER = "This is the precomputed answer this test expects to see served verbatim."
bank_path = settings.data_base_path / "answer_bank" / f"{WORLD}.json"
bank_path.parent.mkdir(parents=True, exist_ok=True)
_had_existing = bank_path.exists()
_original_bytes = bank_path.read_bytes() if _had_existing else None
bank_path.write_text(json.dumps({"entries": [{
    "role": "general", "set_id": "general-ordinary-day", "question_order": 1,
    "question_text": BANK_QUESTION, "answer_text": BANK_ANSWER,
    "representative_name": "chloe", "citations": [{"term": "test", "key_sources": "n/a"}],
    "retrieval_audit": None, "glosses_used": [],
}]}, indent=2), encoding="utf-8")
check("bank file written for the test world", bank_path.exists())

from fastapi.testclient import TestClient  # noqa: E402

import app.main as main_mod  # noqa: E402

client = TestClient(main_mod.app)
start = client.post("/api/session/start", json={"world_id": WORLD})
check("session start succeeds", start.status_code == 200, f"HTTP {start.status_code}")
body = start.json()
sid, token = body["session_id"], body["session_token"]
headers = {"X-Session-Token": token}

# ---------------------------------------------------------------------------
section("B. non-streaming /message - hit, miss, and ordinary-traffic fallthrough")
# ---------------------------------------------------------------------------
r_hit = client.post(f"/api/session/{sid}/message", headers=headers, json={
    "message": BANK_QUESTION,
    "curriculum_ref": {"role": "general", "set_id": "general-ordinary-day", "question_order": 1},
})
check("bank-hit request succeeds", r_hit.status_code == 200, f"HTTP {r_hit.status_code}")
hit_new = r_hit.json()["messages"][-1]
check("bank-hit response's newest message is the exact precomputed answer",
      hit_new.get("content") == BANK_ANSWER, f"got: {hit_new.get('content')!r}")
check("bank-hit response carries the precomputed citations",
      bool(hit_new.get("citations")))

r_ref_mismatch = client.post(f"/api/session/{sid}/message", headers=headers, json={
    "message": "This is not the question the bank entry was stored for.",
    "curriculum_ref": {"role": "general", "set_id": "general-ordinary-day", "question_order": 1},
})
check("text-mismatched curriculum_ref falls through to live (mock) generation, 200 not error",
      r_ref_mismatch.status_code == 200, f"HTTP {r_ref_mismatch.status_code}")
# .messages is the WHOLE session transcript, not just this turn - the
# earlier bank-hit answer legitimately still appears in it. Only the
# newest message (this turn's actual response) is the thing being tested.
mismatch_new = r_ref_mismatch.json()["messages"][-1]
check("...and does NOT serve the bank answer for a mismatched question",
      mismatch_new.get("content") != BANK_ANSWER, f"got: {mismatch_new.get('content')!r}")

r_free = client.post(f"/api/session/{sid}/message", headers=headers, json={
    "message": "Whatever a real participant might type on their own.",
})
check("ordinary free-typed message (no curriculum_ref) -> 200, live path unaffected",
      r_free.status_code == 200, f"HTTP {r_free.status_code}")
free_new = r_free.json()["messages"][-1]
check("...and never accidentally serves the bank answer",
      free_new.get("content") != BANK_ANSWER, f"got: {free_new.get('content')!r}")

# ---------------------------------------------------------------------------
section("C. streaming /message/stream - same hit/miss contract, token-by-token")
# ---------------------------------------------------------------------------
start2 = client.post("/api/session/start", json={"world_id": WORLD})
sid2, token2 = start2.json()["session_id"], start2.json()["session_token"]
headers2 = {"X-Session-Token": token2}

with client.stream("POST", f"/api/session/{sid2}/message/stream", headers=headers2, json={
    "message": BANK_QUESTION,
    "curriculum_ref": {"role": "general", "set_id": "general-ordinary-day", "question_order": 1},
}) as r_stream:
    check("streaming bank-hit request succeeds", r_stream.status_code == 200,
          f"HTTP {r_stream.status_code}")
    chunks = [json.loads(line[len("data: "):]) for line in r_stream.iter_lines()
              if line.startswith("data: ")]

token_events = [c for c in chunks if c.get("type") == "token"]
reassembled = "".join(c["text"] for c in token_events)
check("streamed tokens reassemble to exactly the precomputed answer",
      reassembled == BANK_ANSWER, f"got: {reassembled!r}")
check("a real token stream happened (more than one chunk), not one instant dump",
      len(token_events) > 1, f"{len(token_events)} token events")

# ---------------------------------------------------------------------------
section("D. cleanup")
# ---------------------------------------------------------------------------
if _had_existing:
    bank_path.write_bytes(_original_bytes)
else:
    bank_path.unlink(missing_ok=True)
check("test bank file removed / restored, no artifact left behind",
      (bank_path.exists() == _had_existing))

# ---------------------------------------------------------------------------
n_pass = sum(1 for _, p, _ in RESULTS if p)
print(f"\n{'=' * 72}\nRESULT: {n_pass}/{len(RESULTS)} checks passed\n{'=' * 72}")
sys.exit(0 if n_pass == len(RESULTS) else 1)
