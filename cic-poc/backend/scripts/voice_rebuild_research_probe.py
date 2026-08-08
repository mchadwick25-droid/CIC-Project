"""Voice-rebuild probe harness (2026-08-08, extended to the full fleet in
Phase 0.4).

Originated as the §9 Research stage's two ordered checks from the Voice
Rebuild brief (CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md,
finding C):

  (a) Mar Yausep FIRST - his permanent prompt already carries a bridge-first
      instruction (syr_...Yausep.txt:45) and a plain-sentence instruction
      (:41), so he answers the PRIOR question: does prose instruction of any
      kind actually hold at generation time?
  (b) Papnoute SECOND - the only world with worked example dialogues, so he
      answers the NARROWER question: do worked examples hold where prose
      alone doesn't?

Voice Rebuild Phase 0.4 (Blueprint 0.4, Design §5's per-world checkpoint):
extended to the remaining four worlds (Chloe/PAHC, Theon/Alexandria,
Marius/IJC, Albina/Hieronymian) so the harness covers the full fleet, not
just the two Research-stage probe worlds - the instrument every per-world
checkpoint after this runs against, not a one-off Research artifact.

Probe battery (identical shape for all six worlds): eight turns designed to
retrieve term-heavy lexicon/story chunks WITHOUT the participant ever
speaking the world's own technical terms - the exact condition under which
FLAG-018's false "when I said X" / unprompted-sense-clarification openers
were observed live. Turn 7 is a register probe (say it plain); turn 6
invites Distortion Risk material directly (does apparatus language leak).

Measures, per turn: opener classification (automated regex + transcript kept
for manual read), first-sentence technical-term-before-story check
(Yausep's bridge-first instruction, generalized to TECH_TERMS per world),
mean words/sentence, readability_check, every invisible LLM call's usage
record, and (Phase 0.4) the over_settling confirmed-rate and length_ceiling
outcome breakdown for the scenario's turns.

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

# Voice Rebuild Phase 0.4 (Design §3/Blueprint 0.4): surface
# over_settling_logging's confirmed-rate and length_ceiling_logging's
# regeneration events into this harness, the same way usage_records already
# surfaces [llm_usage] lines - both loggers were previously observation-only
# with no committed artifact ever reading them back.
over_settling_records = []
length_ceiling_records = []


class _TaggedLogCapture(logging.Handler):
    """Generic [tag] key=value line capture, same parsing convention as
    UsageCapture above - shared here rather than duplicated per tag."""

    def __init__(self, tag: str, sink: list):
        super().__init__()
        self._prefix = f"[{tag}] "
        self._sink = sink

    def emit(self, record):
        msg = record.getMessage()
        if not msg.startswith(self._prefix):
            return
        fields = {}
        for part in msg[len(self._prefix):].split():
            if "=" in part:
                k, v = part.split("=", 1)
                fields[k] = v
        self._sink.append(fields)


logging.getLogger("cic.over_settling_decision").addHandler(
    _TaggedLogCapture("over_settling_decision", over_settling_records))
logging.getLogger("cic.length_ceiling").addHandler(
    _TaggedLogCapture("length_ceiling", length_ceiling_records))


def summarize_over_settling(records: list[dict]) -> dict:
    screened = [r for r in records if r.get("screened") == "True"]
    confirmed = [r for r in screened if r.get("confirmed") == "True"]
    return {
        "total_signal_calls": len(records),
        "screened": len(screened),
        "confirmed": len(confirmed),
        "confirmed_rate_of_screened": (
            round(len(confirmed) / len(screened), 3) if screened else None),
    }


def summarize_length_ceiling(records: list[dict]) -> dict:
    by_outcome = {}
    for r in records:
        outcome = r.get("outcome", "unknown")
        by_outcome[outcome] = by_outcome.get(outcome, 0) + 1
    return {"total_ceilinged_turns": len(records), "by_outcome": by_outcome}

from fastapi.testclient import TestClient  # noqa: E402
import app.main as main_mod  # noqa: E402

from wrs.gates.core import readability_check  # noqa: E402

client = TestClient(main_mod.app)

# Technical-term inventories for the first-word-vs-story check. Yausep's
# bridge-first instruction (:45) names raza, qyama, Ihidaya specifically.
#
# Voice Rebuild Phase 0.4 (Blueprint 0.4 "extend the probe harness's
# scenarios to all six worlds"): the four added entries below draw each
# world's own untranslated loanwords from its term records
# (wrs/records/<world>/term/*.md), the same kind of list Yausep's and
# Papnoute's already used - not the English glosses those records also
# carry, since an English concept word ("bishop", "fasting") is not the
# unprompted-technical-term signal this check is built to catch.
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
    "post-apostolic-house-church": [
        "episkopos", "presbyteros", "presbyteroi", "ekklesia",
        "eucharistia", "diakonos", "diakonoi", "presbyterion",
        "prophetes", "baptisma", "hetaeria", "pertinacia",
    ],
    "alexandria-catechetical": [
        "logos", "gnosis", "theosis", "nous", "autexousia", "hamartia",
        "photismos", "mysterion", "oikonomia", "arete", "metanoia",
        "apokatastasis", "didaskaleion", "homoousios", "logikos",
    ],
    "imperial-juridical-christianity": [
        "primatus", "presbeia", "homoios", "communio", "homoousios",
        "concilium", "synodos", "haeresis", "tomus", "martyrium",
    ],
    "hieronymian-ascetic-literary": [
        "hebraica veritas", "renuntiatio", "virginitas", "patrocinium",
        "epistula", "matrona", "grammaticus", "praefatio", "nosocomium",
        "monachus",
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
    # Voice Rebuild Phase 0.4 (Blueprint 0.4): the four worlds added to
    # extend this harness to the full fleet, same eight-turn shape as the
    # two Research-stage scenarios above - retrieve term-heavy lexicon/
    # story chunks without the participant ever speaking the world's own
    # technical terms (TECH_TERMS above), closing with the same register
    # probe (turn 7) and takeaway close (turn 8).
    {
        "world_id": "post-apostolic-house-church",
        "label": "Chloe probe (PAHC, fleet extension)",
        "turns": [
            "What held your community together when you didn't have one leader everyone agreed on?",
            "How would you know if a stranger who showed up at your door claiming to speak for God was telling the truth?",
            "Why would you trust a letter from a church in another city you'd never even seen?",
            "What did eating together actually mean to your community - was it just a meal, or something more?",
            "Is there someone from your community whose life shows what it looked like when all of this really worked?",
            "What's something people today would get completely wrong about your community if they only knew the surface of it?",
            "Say that to me plain, the way you'd explain it to someone who just wandered in off the street.",
            "What would you want me to carry away from this conversation?",
        ],
    },
    {
        "world_id": "alexandria-catechetical",
        "label": "Theon probe (Alexandria, fleet extension)",
        "turns": [
            "What does it actually mean to be taught by God, in your world? What does that experience feel like?",
            "How is reading scripture different from reading any other old book, for your community?",
            "Why would something like fasting have anything to do with what happens in a person's mind?",
            "Does everyone reach the same depth of understanding, or do some people get further than others? What does that path look like?",
            "Is there someone from your community whose life shows what all of this looked like when it worked?",
            "What would people today get most wrong about your community if they only saw the surface of it?",
            "Say that to me plain, the way you'd explain it to someone who just walked in off the street.",
            "What would you want me to take away from this conversation?",
        ],
    },
    {
        "world_id": "imperial-juridical-christianity",
        "label": "Marius probe (IJC, fleet extension)",
        "turns": [
            "When several great cities all claimed a voice, how did your church decide who actually had the authority to speak for everyone?",
            "What really happened when two churches stopped recognizing each other? What did that actually break?",
            "Why would an emperor's soldiers matter to a religious argument at all?",
            "Was there ever a time your own church held a position that later got treated as a mistake?",
            "Is there a moment or a person whose story shows what was really at stake in these disputes?",
            "What would people today get most wrong about your world if they only heard the outside of it?",
            "Say that to me plain, the way you'd tell it to a traveler who stopped you on the road.",
            "What should I take away from this conversation?",
        ],
    },
    {
        "world_id": "hieronymian-ascetic-literary",
        "label": "Albina probe (Hieronymian, fleet extension)",
        "turns": [
            "What did it mean for a woman of your standing to give up everything she had?",
            "How did your household actually spend its days - what did the work look like?",
            "Why would studying old texts closely matter as much as prayer, in your world?",
            "What happened when your household disagreed sharply with people you'd once been close to?",
            "Is there someone in your household whose life shows what all of this looked like when it was lived out fully?",
            "What would people today get most wrong about women like you if they only knew the surface of it?",
            "Say that to me plain, the way you'd tell it to a girl who just arrived at your door.",
            "What would you want me to carry away from this conversation?",
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
    over_settling_records.clear()
    length_ceiling_records.clear()

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

    over_settling_summary = summarize_over_settling(over_settling_records)
    length_ceiling_summary = summarize_length_ceiling(length_ceiling_records)
    print(f"  [over_settling] screened={over_settling_summary['screened']} "
          f"confirmed={over_settling_summary['confirmed']} "
          f"rate={over_settling_summary['confirmed_rate_of_screened']}",
          flush=True)
    print(f"  [length_ceiling] {length_ceiling_summary['by_outcome']}",
          flush=True)

    results.append({
        "world_id": scenario["world_id"],
        "label": scenario["label"],
        "transcript": transcript,
        "turn_analyses": turn_analyses,
        "usage": list(usage_records),
        "over_settling": over_settling_summary,
        "over_settling_records": list(over_settling_records),
        "length_ceiling": length_ceiling_summary,
        "length_ceiling_records": list(length_ceiling_records),
        "turn_errors": turn_errors,
    })

out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "voice_rebuild_research_probe_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nWrote {out_path}")
