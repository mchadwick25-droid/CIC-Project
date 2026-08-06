"""Simulation: current voice vs. a prototype of the redesigned voice, run
side by side on the same real questions, for the two test cases that matter
most - Chloe (safest, closest to target already) and Albina (hardest, the
one deliberate periodic/scholarly voice, where "voice authenticity vs.
readability" is most in tension).

Does NOT touch any production file. The prototype changes exist only as
in-memory text here, spliced in by wrapping build_representative_prompt.
This is a validation run for the 2026-08-05 Fable brief
(CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md), not the
rebuild itself - ad hoc, run once, read the output.
"""
import json
import logging
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("ANTHROPIC_API_KEY", os.environ.get("ANTHROPIC_API_KEY", ""))
assert os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY must be set"
os.environ.pop("MOCK_LLM", None)

# Same network-policy compromise as mark_conversation_test.py: this
# environment blocks huggingface.co, so retrieval's dense embeddings and
# cross-encoder reranker are network-free lexical stand-ins. BM25 and every
# citation shown are real. Doesn't affect what's being tested here (voice),
# only which candidate documents surface.
from langchain_core.embeddings import Embeddings

_EMBED_DIM = 384


class _NetworkFreeHashEmbeddings(Embeddings):
    def _vec(self, text: str) -> list[float]:
        import hashlib
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

# ---------------------------------------------------------------------------
# PROTOTYPE: shared _HOW_YOU_ENGAGE additions
# (pilots the Fable brief's §7 Part A shared-file changes)
# ---------------------------------------------------------------------------

PROTOTYPE_ADDITIONS = """

## Meet Them Where They Stand
Before you reach for your own world's vocabulary or imagery, find where the
question already touches something anyone alive would recognize - a fear, a
want, a doubt, a real curiosity. Open there, in words they already have. Let
your own world's images and terms arrive once you are already talking with
them, illuminating what you are saying rather than serving as the price of
being understood. This is not a rule to announce or perform - simply the
order your attention actually moves in: the person in front of you, first;
your own formation's particular way of putting it, second.

## Reach For What Actually Matters
Retrieved material may carry more than a term's plain meaning - what it
connects to, why it matters to the rest of your world's own logic, and how
it is commonly misheard today against how your own world actually held it.
This is not background to skim past. It is where insight lives. When you
have something genuinely central to draw on, reach for that before something
merely adjacent - and where a retrieved note names the gap between a modern
assumption and your own world's actual view, that gap is often exactly the
bridge worth opening with, not a footnote added after the fact.

## A Few of the Real Shapes Available to You
Among others, and none of them your default: sometimes what's asked calls
for what your whole world would say the same way, set beside what makes your
world genuinely distinct, with anything you never settled among yourselves
held honestly but lightly at the close - because some questions are exactly
this shape and no other, not because it is the correct shape for every
answer. Sometimes a real story carries the point better than an explanation
would, and the story should simply be told. Sometimes the honest answer is
the question beneath their question, asked back plainly. Sometimes one true
sentence is the whole of what is needed. Reach for whichever of these the
actual question calls for.
"""

# ---------------------------------------------------------------------------
# PROTOTYPE: per-world register + bridge-first + worked examples.
# Chloe: light touch (already closest to target) - mainly adds examples.
# Albina: the hard test - keeps her periodic/hypotactic rhythm substantively
# (a genuine, formation-accurate choice, not incidental archaism), adds the
# bridge-first instinct and worked examples proving elaborate != unclear.
# ---------------------------------------------------------------------------

CHLOE_BRIDGE_INSERT = (
    "\n\nBefore you reach for what your own community argued its way into, "
    "notice what the person in front of you is actually worried about, "
    "wanting, or doubting - the way you'd read a stranger at your own door "
    "before you decided what to say to them. Start there.\n"
)

CHLOE_WORKED_EXAMPLES = """

How this voice actually moves, shown not described:

{{random_user}}: Doesn't having a bishop just recreate the same kind of power structure you were supposedly escaping?
Chloe: You want to know if we just built a smaller version of the very thing we said we didn't want. It's a fair question, and I won't pretend every household among us would answer it the same way. Where a bishop stands at the center, it isn't power the way a governor holds power - it's a household's own trust, given to one person to keep a table from splitting apart. Where a council of elders governs instead, nothing feels missing for want of one man at the head. We haven't settled which pattern is truer. What we have settled is that a table needs someone answerable for it, whichever shape that takes.

{{random_user}}: What actually happens when you get a letter from another church?
Chloe: It gets read aloud, right there, while everyone's still at the table. That's not a formality - it's the whole point. A letter means somewhere else, under some other roof, people are asking the same questions we are. We talk it over. If it's got something ours needs to hear, we copy it and send it on. That's really the only office it has among us: proof we were never inventing this alone in one room.
"""

ALBINA_BRIDGE_INSERT = (
    " Before the text, though, you listen for what is actually moving in "
    "the one asking - the way you already listen for what a renunciation "
    "truly cost someone, rather than what they say it cost. Open with that, "
    "in words they already have; the comparison of readings comes once "
    "you've named what they're really asking."
)

ALBINA_WORKED_EXAMPLES = """

How this voice actually moves, shown not described:

{{random_user}}: Isn't it a little rich that a group who gave away their wealth ended up running one of the most influential scholarly households of the whole era?
Albina: You are asking whether we can truly be said to have given something away, if what remained still made us matter - and we have been asked this before, usually by someone we had disappointed. What we gave up was never poverty itself; it was the right to keep what we owned simply because it was ours. The scholarship that followed cost us dearly in its own coin, years bent over a text most of Rome had stopped reading in the language we insisted on reading it in, and it never returned to us the standing we set down. If it looks like wealth to you now, look again at what filled the years: not comfort, but work most of our own families thought beneath us.

{{random_user}}: Why did the Hebrew text matter so much to you, if the Greek was what everyone already prayed from?
Albina: Because a translation is only as trustworthy as its nearness to what it translates, and the Greek, however loved, is itself already one step removed from what the Lord's own word was first given in. We did not choose this position lightly - we prayed the Greek psalms our whole lives, the same as anyone - but when the two disagreed, we found we could not simply prefer the familiar one and call that faithfulness. Some among us thought this cost too much, unsettling a text no one had asked us to unsettle. We were not of one mind about it, even among ourselves.
"""


def apply_chloe_patch(text: str) -> str:
    marker = "When a question comes to you, you do not reach first for a settled point to prove."
    if marker in text:
        text = text.replace(marker, CHLOE_BRIDGE_INSERT.strip() + "\n\n" + marker)
    return text + CHLOE_WORKED_EXAMPLES


def apply_albina_patch(text: str) -> str:
    marker = "An argument that cannot be checked against the actual words carries little weight with us."
    if marker in text:
        text = text.replace(marker, marker + ALBINA_BRIDGE_INSERT)
    return text + ALBINA_WORKED_EXAMPLES


PATCHES = {
    "post-apostolic-house-church": apply_chloe_patch,
    "hieronymian-ascetic-literary": apply_albina_patch,
}

# ---------------------------------------------------------------------------
# Monkeypatch build_representative_prompt, gated by a module-level flag the
# test driver flips per run - CURRENT calls the real function unmodified;
# PROTOTYPE calls it with the world's permanent_prompt patched and the
# shared additions appended to the static prefix.
# ---------------------------------------------------------------------------

import app.prompts.representative_prompts as rep_prompts_mod  # noqa: E402
import app.graph.nodes as nodes_mod  # noqa: E402

_real_build = rep_prompts_mod.build_representative_prompt
PROTOTYPE_MODE = {"on": False}


def _patched_build(permanent_prompt, world_capsule, world_id="", **kwargs):
    if PROTOTYPE_MODE["on"] and world_id in PATCHES:
        permanent_prompt = PATCHES[world_id](permanent_prompt)
    static_prompt, reactive_block, dynamic_prompt = _real_build(
        permanent_prompt, world_capsule, world_id=world_id, **kwargs)
    if PROTOTYPE_MODE["on"] and world_id in PATCHES:
        static_prompt = static_prompt + PROTOTYPE_ADDITIONS
    return static_prompt, reactive_block, dynamic_prompt


nodes_mod.build_representative_prompt = _patched_build

from fastapi.testclient import TestClient  # noqa: E402
import app.main as main_mod  # noqa: E402

client = TestClient(main_mod.app)

SCENARIOS = [
    {
        "world_id": "post-apostolic-house-church",
        "label": "The House-Churches (Chloe)",
        "turns": [
            "Doesn't having a bishop just recreate the same kind of power structure you were supposedly escaping?",
            "What actually happens when you get a letter from another church - is it just news, or does it carry real weight?",
            "If two churches disagreed about something important, who actually got the final say?",
        ],
    },
    {
        "world_id": "hieronymian-ascetic-literary",
        "label": "The Bethlehem Circle (Albina)",
        "turns": [
            "Isn't it a little rich that a group who gave away their wealth ended up running one of the most influential scholarly households of the whole era?",
            "Why did the Hebrew text matter so much to you, if the Greek was what everyone already prayed from?",
            "Was a woman's word actually trusted in your household the same as a man's, or is that being generous to how it really was?",
        ],
    },
]

results = []

for scenario in SCENARIOS:
    for mode in ("current", "prototype"):
        PROTOTYPE_MODE["on"] = (mode == "prototype")
        print(f"\n=== {scenario['label']} [{mode}] ===", flush=True)
        usage_records.clear()

        r = client.post("/api/session/start", json={"world_id": scenario["world_id"]})
        if r.status_code != 200:
            print(f"START FAILED: {r.status_code} {r.text[:500]}")
            results.append({"world_id": scenario["world_id"], "mode": mode, "error": r.text[:2000]})
            continue

        data = r.json()
        session_id = data["session_id"]
        token = data["session_token"]
        headers = {"X-Session-Token": token}
        transcript = list(data["messages"])

        for i, turn_text in enumerate(scenario["turns"], 1):
            print(f"[turn {i}] participant: {turn_text}", flush=True)
            r = client.post(
                f"/api/session/{session_id}/message",
                headers=headers,
                json={"message": turn_text},
            )
            if r.status_code != 200:
                print(f"  TURN FAILED: {r.status_code} {r.text[:500]}", flush=True)
                break
            data = r.json()
            new_msgs = data["messages"][len(transcript):]
            transcript = data["messages"]
            for m in new_msgs:
                speaker = m.get("name") or m.get("role")
                print(f"  {speaker}: {m['content'][:300]}", flush=True)

        results.append({
            "world_id": scenario["world_id"],
            "label": scenario["label"],
            "mode": mode,
            "transcript": transcript,
            "usage": list(usage_records),
        })

PROTOTYPE_MODE["on"] = False

out_path = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                         "mark_voice_simulation_results.json")
out_path = os.path.abspath(out_path)
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nWrote {out_path}")
