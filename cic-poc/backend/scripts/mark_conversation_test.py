"""One-off live test: run real multi-turn conversations against three worlds
through the actual HTTP surface (FastAPI TestClient), capturing full
transcripts and every real LLM call's token usage, so the transcripts can be
read for content/flow/readability and the usage log can be turned into a
real per-conversation cost breakdown.

Not a permanent script - ad hoc, run once, read the output files.
"""
import json
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("ANTHROPIC_API_KEY", os.environ.get("ANTHROPIC_API_KEY", ""))
assert os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY must be set"
os.environ.pop("MOCK_LLM", None)

# COMPROMISE, flagged deliberately: this environment's network policy blocks
# huggingface.co, so the real all-MiniLM-L6-v2 dense embedding model can't be
# downloaded. Everything else in the RAG pipeline runs for real - hybrid
# BM25+dense RRF fusion, the Retrieve-When/Do-Not-Retrieve-When filter LLM
# calls, citation resolution - only the dense half of the hybrid search is
# swapped for a network-free hashing/bag-of-words vectorizer instead of the
# real semantic embedding. BM25 (lexical overlap) still runs at full
# fidelity. This can make retrieval less semantically precise than
# production; it does not change Facilitator/Representative voice, tone, or
# turn structure, which is what this test run is primarily evaluating.
import hashlib
import re

from langchain_core.embeddings import Embeddings

_EMBED_DIM = 384


class _NetworkFreeHashEmbeddings(Embeddings):
    def _vec(self, text: str) -> list[float]:
        v = [0.0] * _EMBED_DIM
        for tok in re.findall(r"[a-z0-9]+", text.lower()):
            idx = int(hashlib.sha1(tok.encode()).hexdigest(), 16) % _EMBED_DIM
            v[idx] += 1.0
        norm = sum(x * x for x in v) ** 0.5 or 1.0
        return [x / norm for x in v]

    def embed_documents(self, texts):
        return [self._vec(t) for t in texts]

    def embed_query(self, text):
        return self._vec(text)


import app.rag.embeddings as embeddings_mod  # noqa: E402
import app.rag.indexer as indexer_mod  # noqa: E402
import app.rag.story_indexer as story_indexer_mod  # noqa: E402
_shared = _NetworkFreeHashEmbeddings()
embeddings_mod._embeddings = _shared
embeddings_mod.get_shared_embeddings = lambda: _shared
indexer_mod.get_shared_embeddings = lambda: _shared
story_indexer_mod.get_shared_embeddings = lambda: _shared


# Same compromise, second site: app/rag/cross_encoder.py's reranker also
# downloads a Hugging Face model (cross-encoder/ms-marco-MiniLM-L-6-v2) on
# first use. Stub it with a lexical-overlap score scaled to roughly the
# real model's calibrated range (module docstring: must-docs >= 1.2, noise
# median -10.7, threshold -4.0) so relevance_partition's keep/drop logic
# still does something sensible rather than keeping or dropping everything.
class _NetworkFreeCrossEncoder:
    def predict(self, pairs):
        scores = []
        for query, doc_text in pairs:
            q_toks = set(re.findall(r"[a-z0-9]+", query.lower()))
            d_toks = set(re.findall(r"[a-z0-9]+", doc_text.lower()))
            overlap = len(q_toks & d_toks) / max(len(q_toks), 1)
            scores.append(-10.0 + 13.0 * overlap)
        return scores


import app.rag.cross_encoder as cross_encoder_mod  # noqa: E402
cross_encoder_mod._model = _NetworkFreeCrossEncoder()
cross_encoder_mod._get_model = lambda: cross_encoder_mod._model

usage_records = []


class UsageCapture(logging.Handler):
    def emit(self, record):
        msg = record.getMessage()
        if not msg.startswith("[llm_usage]"):
            return
        fields = {}
        for part in msg[len("[llm_usage] "):].split():
            if "=" in part:
                k, v = part.split("=", 1)
                fields[k] = v
        usage_records.append(fields)


logging.getLogger("cic.llm_usage").addHandler(UsageCapture())

from fastapi.testclient import TestClient  # noqa: E402
import app.main as main_mod  # noqa: E402

client = TestClient(main_mod.app)

# Deep-Interview-style scenarios: one world, a handful of turns that build
# on each other the way a real curious participant would - genuine question,
# natural follow-up, a real pushback/challenge, a closing reflective turn.
SCENARIOS = [
    {
        "world_id": "desert-monasticism",
        "label": "Desert Fathers and Mothers (Papnoute)",
        "turns": [
            "What does it actually mean to \"fight your thoughts\"? That sounds exhausting.",
            "Okay, but practically - if I'm lying awake at 2am spiraling about something, what would one of you actually have me do in that moment?",
            "Isn't that just suppression though? Modern psychology would say naming and expressing the thought is healthier than fighting it.",
            "That's helpful. Is there a story of someone who got this wrong - who fought too hard and it broke them?",
        ],
    },
    {
        "world_id": "post-apostolic-house-church",
        "label": "The House-Churches (Chloe)",
        "turns": [
            "What was it actually like, meeting in someone's house instead of a church building? Did it feel makeshift, or was that the point?",
            "Who got to speak during the meal, and who decided that?",
            "Isn't it convenient that a movement led mostly by wealthy homeowners describes itself as radically inclusive? Whose interests did that structure actually serve?",
            "If I showed up to one of these gatherings as a stranger off the street, what would actually happen to me?",
        ],
    },
    {
        "world_id": "syriac-edessa-nisibis",
        "label": "Syriac Christianity (Mar Yausep)",
        "turns": [
            "Your tradition sits right at the edge between the Roman and Persian worlds. Did that in-between position shape how you thought about faith, or was it mostly a political headache?",
            "What's the Bnay Qyama - the \"sons and daughters of the covenant\"? Is that monasticism, or something else?",
            "A lot of what survives from your world is in a language most people today have never heard of. Doesn't that mean we're only getting a fragment, filtered through whoever bothered to translate it?",
            "What would you want a modern Christian, who's never heard of the Church of the East, to actually understand about your community?",
        ],
    },
]

results = []

for scenario in SCENARIOS:
    print(f"\n=== {scenario['label']} ({scenario['world_id']}) ===", flush=True)
    usage_records.clear()

    r = client.post("/api/session/start", json={"world_id": scenario["world_id"]})
    if r.status_code != 200:
        print(f"START FAILED: {r.status_code} {r.text[:500]}")
        results.append({"world_id": scenario["world_id"], "error": r.text[:2000]})
        continue

    data = r.json()
    session_id = data["session_id"]
    token = data["session_token"]
    headers = {"X-Session-Token": token}

    transcript = list(data["messages"])
    print(f"[start] {len(transcript)} opening message(s)", flush=True)
    for m in transcript:
        speaker = m.get("name") or m.get("role")
        print(f"  {speaker}: {m['content'][:100]}", flush=True)

    turn_errors = []
    for i, turn_text in enumerate(scenario["turns"], 1):
        print(f"\n[turn {i}] participant: {turn_text}", flush=True)
        r = client.post(
            f"/api/session/{session_id}/message",
            headers=headers,
            json={"message": turn_text},
        )
        if r.status_code != 200:
            print(f"  TURN FAILED: {r.status_code} {r.text[:500]}", flush=True)
            turn_errors.append({"turn": i, "error": r.text[:2000]})
            break
        data = r.json()
        new_msgs = data["messages"][len(transcript):]
        transcript = data["messages"]
        for m in new_msgs:
            speaker = m.get("name") or m.get("role")
            print(f"  {speaker}: {m['content'][:300]}", flush=True)

    world_usage = list(usage_records)
    results.append({
        "world_id": scenario["world_id"],
        "label": scenario["label"],
        "transcript": transcript,
        "usage": world_usage,
        "turn_errors": turn_errors,
    })

out_path = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                         "mark_conversation_test_results.json")
out_path = os.path.abspath(out_path)
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nWrote {out_path}")
