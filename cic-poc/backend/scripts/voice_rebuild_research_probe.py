"""Voice-rebuild Research-stage probe (2026-08-08).

Runs the §9 Research stage's two ordered checks from the Voice Rebuild brief
(CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md, finding C):

  (a) Mar Yausep FIRST - his permanent prompt already carries a bridge-first
      instruction (syr_...Yausep.txt:45) and a plain-sentence instruction
      (:41), so he answers the PRIOR question: does prose instruction of any
      kind actually hold at generation time?
  (b) Papnoute SECOND - the only world with worked example dialogues, so he
      answers the NARROWER question: do worked examples hold where prose
      alone doesn't?

Probe battery (identical shape for both worlds): eight turns designed to
retrieve term-heavy lexicon/story chunks WITHOUT the participant ever
speaking the world's own technical terms - the exact condition under which
FLAG-018's false "when I said X" / unprompted-sense-clarification openers
were observed live. Turn 7 is a register probe (say it plain); turn 6
invites Distortion Risk material directly (does apparatus language leak).

Measures, per turn: opener classification (automated regex + transcript kept
for manual read), first-sentence technical-term-before-story check
(Yausep's bridge-first instruction), mean words/sentence,
readability_check, and every invisible LLM call's usage record.

Reuses mark_conversation_test.py's network-free embedding/cross-encoder
stand-ins verbatim (this environment blocks huggingface.co; BM25 and all
LLM calls are real).
"""
import json
import logging
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

assert os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY must be set"
os.environ.pop("MOCK_LLM", None)

import hashlib

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

from wrs.gates.core import readability_check  # noqa: E402

client = TestClient(main_mod.app)

# Technical-term inventories for the first-word-vs-story check. Yausep's
# bridge-first instruction (:45) names raza, qyama, Ihidaya specifically.
TECH_TERMS = {
    "syriac-edessa-nisibis": [
        "raza", "raze", "qyama", "ihidaya", "iḥidaya", "bnay", "bnat",
        "madrasha", "madrashe", "shrara", "memra", "ewangeliyon",
    ],
    "desert-monasticism": [
        "logismoi", "logismos", "apatheia", "hesychia", "xeniteia",
        "penthos", "nepsis", "diakrisis", "synaxis", "kellion", "praktike",
        "theoria", "antirrhesis",
    ],
}

# The unprompted-reclarification / false-referent opener patterns finding C
# documents (layer 3's own measured baseline: 1 false opener in 16 turns).
RECLARIFY_PATTERNS = [
    r"when (?:I|we) (?:said|spoke of|used)",
    r"\b(?:I|we) (?:said|meant|used the word)\b.{0,40}\b(?:earlier|before|a moment ago)",
    r"(?:earlier|before|a moment ago).{0,40}\b(?:I|we) (?:said|meant|spoke)",
    r"you asked (?:this|that|me this) before",
    r"the word (?:I|we) (?:used|reached for)",
    r"by [\w'‘’-]+ (?:I|we) (?:mean|meant)",
]

SCENARIOS = [
    {
        "world_id": "syriac-edessa-nisibis",
        "label": "Yausep probe (prose-instruction check, runs FIRST)",
        "turns": [
            "What did it mean in your community to give your whole life to God? Was that for everyone, or only for a few?",
            "How did your community understand baptism? What actually changed for the person?",
            "Why did some people in your world choose never to marry? What was that about?",
            "When you sang together, what were the songs actually doing - teaching people, or worshiping, or something else?",
            "Is there one person from your world whose life shows what all of this looked like when it worked?",
            "What's something people today would completely misunderstand about your community if they only heard the surface of it?",
            "That's a lot to take in. Say it to me the way you'd say it to a farmer's kid who stopped you on the road.",
            "What would you want me to carry away from this conversation?",
        ],
    },
    {
        "world_id": "desert-monasticism",
        "label": "Papnoute probe (worked-examples check, runs SECOND)",
        "turns": [
            "I can't quiet my own head. Does your way of life have anything for someone like me?",
            "What did you actually do all day out there?",
            "Why would anyone choose to grieve on purpose? I heard your people treated sorrow as a good thing.",
            "How did you tell the difference between a thought worth trusting and one that was lying to you?",
            "Is there a story of one of you who failed at all this - who fought too hard and it broke them?",
            "What would people today get most wrong about why you went to the desert?",
            "Tell it to me plain, the way you'd tell a boy who walked out to your cell and asked.",
            "What should I take with me from this?",
        ],
    },
]


def analyze_turn(world_id: str, text: str) -> dict:
    first_para = text.strip().split("\n")[0]
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    words = re.findall(r"[\w'‘’-]+", text)
    first_sentence = sentences[0] if sentences else ""

    reclarify = [p for p in RECLARIFY_PATTERNS
                 if re.search(p, first_para, re.IGNORECASE)]

    lowered = text.lower()
    first_term_pos = None
    first_term = None
    for t in TECH_TERMS.get(world_id, []):
        m = re.search(r"\b" + re.escape(t), lowered)
        if m and (first_term_pos is None or m.start() < first_term_pos):
            first_term_pos, first_term = m.start(), t
    tech_in_first_sentence = bool(
        first_term_pos is not None and first_term_pos < len(first_sentence))

    r = readability_check(text) if len(words) > 30 else {
        "fk_grade": None, "fre": None, "violations": ["too short to score"]}
    return {
        "sentences": len(sentences),
        "words": len(words),
        "words_per_sentence": round(len(words) / max(1, len(sentences)), 1),
        "paragraphs": len([p for p in text.split("\n\n") if p.strip()]),
        "fk_grade": r["fk_grade"],
        "fre": r["fre"],
        "reclarify_opener_patterns": reclarify,
        "first_technical_term": first_term,
        "technical_term_in_first_sentence": tech_in_first_sentence,
        "first_sentence": first_sentence[:300],
    }


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
    headers = {"X-Session-Token": data["session_token"]}
    transcript = list(data["messages"])

    turn_analyses = []
    turn_errors = []
    usage_cursor = 0
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
        turn_usage = usage_records[usage_cursor:]
        usage_cursor = len(usage_records)
        for m in new_msgs:
            speaker = m.get("name") or m.get("role")
            print(f"  {speaker}: {m['content'][:240]}", flush=True)
            if m.get("role") == "assistant" and (m.get("name") or "") not in (
                    "Facilitator",):
                a = analyze_turn(scenario["world_id"], m["content"])
                a["turn"] = i
                a["usage_labels"] = sorted(
                    {u.get("label", "?") for u in turn_usage})
                turn_analyses.append(a)
                print(f"    [analysis] {a['words_per_sentence']} w/s, "
                      f"FK {a['fk_grade']}, reclarify={a['reclarify_opener_patterns']}, "
                      f"tech-first-sentence={a['technical_term_in_first_sentence']}",
                      flush=True)

    results.append({
        "world_id": scenario["world_id"],
        "label": scenario["label"],
        "transcript": transcript,
        "turn_analyses": turn_analyses,
        "usage": list(usage_records),
        "turn_errors": turn_errors,
    })

out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "voice_rebuild_research_probe_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nWrote {out_path}")
