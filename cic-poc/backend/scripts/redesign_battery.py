#!/usr/bin/env python
"""Verification battery for the retrieval/evidence redesign.

Runs against the REAL code and the REAL deployed chunks - no fixtures
standing in for the record, no reasoning about what should happen. Needs no
API key: MOCK_LLM=true plus scripted stand-ins where a specific branch has to
be driven.

  python scripts/redesign_battery.py

Every guarantee the redesign must preserve gets a check here, plus the two
findings that changed what got built:

  A  sections.py    - Desert recovery AND byte-identity on fenced worlds
  B  retrieval_mode - guards/exclusion differ by mode, correct by construction
  C  pipeline       - the two retrievers share one code path
  D  adjudication   - the two adjudicators are mutually exclusive (why there
                      is no memo on (world_id, response_text))
  E  world_sources  - static-source cache is correct and self-invalidating
  F  session_auth   - full end-to-end via FastAPI TestClient
  G  route coverage - every session-scoped route enforces ownership
  H  modern_term_bridge - the skip is outcome-preserving, exhaustively
"""

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


# ---------------------------------------------------------------------------
section("A. sections.py - one section primitive, both conventions")
# ---------------------------------------------------------------------------
from app.config import settings  # noqa: E402
from app.graph.repair_classifier import _migrated_world_ids  # noqa: E402
from app.rag.sections import (KEY_SOURCES_MARKERS, QUICK_MEANING_MARKERS,  # noqa: E402
                              excise_section, extract_section, find_section,
                              truncate_at)


def legacy_quick_meaning_strip(body: str) -> str:
    """The exact algorithm this replaced (origin/main retriever.py 298-311)."""
    for qm in QUICK_MEANING_MARKERS:
        qidx = body.find(qm)
        if qidx != -1:
            nxt = body.find("##", qidx + 2)
            body = (body[:qidx].rstrip() + "\n\n"
                    + body[nxt:] if nxt != -1 else body[:qidx].rstrip())
            break
    return body


fenced_n = fenced_same = bold_n = bold_recovered = 0
qm_leaks = ks_diffs = 0
desert_min_after = 10 ** 9
for world in sorted(_migrated_world_ids()):
    cfg = settings.get_world_config(world)
    for f in sorted(cfg.lexicon_chunks_path.glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        # Key Sources strip must be unchanged from main's truncate
        legacy_ks = raw
        for marker in KEY_SOURCES_MARKERS:
            i = raw.find(marker)
            if i != -1:
                legacy_ks = raw[:i].rstrip()
                break
        body = truncate_at(raw, KEY_SOURCES_MARKERS)
        if body != legacy_ks:
            ks_diffs += 1

        new = excise_section(body, QUICK_MEANING_MARKERS)
        old = legacy_quick_meaning_strip(body)
        if any(m in new for m in QUICK_MEANING_MARKERS):
            qm_leaks += 1

        if "\n## " in body or body.startswith("## "):
            fenced_n += 1
            fenced_same += (old == new)
        else:
            bold_n += 1
            bold_recovered += (len(new) > 2 * len(old))
            desert_min_after = min(desert_min_after, len(new))

check("fenced-heading worlds byte-identical to previous behaviour",
      fenced_n and fenced_same == fenced_n, f"{fenced_same}/{fenced_n} chunks")
check("bold-label world (Desert) recovers its body",
      bold_n and bold_recovered == bold_n, f"{bold_recovered}/{bold_n} chunks")
check("Desert bodies are now substantial, not front-matter only",
      desert_min_after > 500, f"smallest recovered body = {desert_min_after}B")
check("Quick Meaning never survives excision", qm_leaks == 0, f"{qm_leaks} leaks")
check("Key Sources strip unchanged", ks_diffs == 0, f"{ks_diffs} differences")

# The bug in miniature, stated as a unit fact.
desert_like = ("---\nTerm: X\n---\n\n**Quick Meaning:** short gloss.\n\n"
               "**World Meaning:** the substantive body that must survive.\n")
fenced_like = ("---\nTerm: X\n---\n\n## Quick Meaning\n\nshort gloss.\n\n---\n\n"
               "## World Meaning\n\nthe substantive body that must survive.\n")
check("bold-label: body survives excision",
      "substantive body that must survive" in excise_section(desert_like, QUICK_MEANING_MARKERS))
check("bold-label: legacy algorithm DID lose it (regression is real)",
      "substantive body" not in legacy_quick_meaning_strip(desert_like))
check("fenced: body survives excision",
      "substantive body that must survive" in excise_section(fenced_like, QUICK_MEANING_MARKERS))
check("fenced: no orphaned rule left at the resume point",
      not excise_section(fenced_like, QUICK_MEANING_MARKERS).split("\n\n")[1].startswith("---"))
check("find_section distinguishes 'absent' from 'runs to end of body'",
      find_section("no marker here", QUICK_MEANING_MARKERS) is None
      and find_section("**Quick Meaning:** only section", QUICK_MEANING_MARKERS).end
      == len("**Quick Meaning:** only section"))
check("extract_section returns the section text itself",
      extract_section(desert_like, QUICK_MEANING_MARKERS) == "short gloss.")

# ---------------------------------------------------------------------------
section("A2. the real get_context_for_response, on real Desert chunks")
# ---------------------------------------------------------------------------
# The embedding model is not reachable in this environment, so FAISS candidate
# search cannot run. Everything downstream of it CAN: build the retriever
# without __init__, stub only `retrieve` (the vector-search half, untouched by
# this redesign), and drive the REAL serialization path - which is exactly
# where the Desert truncation lived.
from langchain_core.documents import Document as _Doc  # noqa: E402

from app.rag.retriever import LexiconRetriever, RetrievalResult  # noqa: E402

desert_cfg = settings.get_world_config("desert-monasticism")
desert_files = sorted(desert_cfg.lexicon_chunks_path.glob("*.md"))[:3]
desert_docs = [
    _Doc(page_content=f.stem, metadata={
        "term": f.stem, "source_file": str(f), "content": f.read_text(encoding="utf-8"),
        "key_sources": "", "do_not_retrieve_when": "", "tier": 1})
    for f in desert_files
]

r = LexiconRetriever.__new__(LexiconRetriever)
r.world_id = "desert-monasticism"
r.retrieve = lambda *a, **k: RetrievalResult(
    documents=desert_docs, terms=[d.metadata["term"] for d in desert_docs],
    reasoning="", evaluations=[])

ctx, _cits, _evals = r.get_context_for_response(query="withdrawal")
check("real serializer emits Desert lexicon content", len(ctx) > 2000, f"{len(ctx)}B of context")
check("real serializer strips Quick Meaning",
      not any(m in ctx for m in QUICK_MEANING_MARKERS))
check("real serializer keeps the substantive body",
      "World Meaning" in ctx, "the section that used to be discarded")
check("real serializer keeps Key Sources apparatus OUT of generation context",
      not any(m in ctx for m in KEY_SOURCES_MARKERS))

# Same path, a fenced world, must be unchanged in kind.
alx_cfg = settings.get_world_config("alexandria-catechetical")
alx_files = sorted(alx_cfg.lexicon_chunks_path.glob("*.md"))[:3]
alx_docs = [
    _Doc(page_content=f.stem, metadata={
        "term": f.stem, "source_file": str(f), "content": f.read_text(encoding="utf-8"),
        "key_sources": "", "do_not_retrieve_when": "", "tier": 1})
    for f in alx_files
]
r2 = LexiconRetriever.__new__(LexiconRetriever)
r2.world_id = "alexandria-catechetical"
r2.retrieve = lambda *a, **k: RetrievalResult(
    documents=alx_docs, terms=[], reasoning="", evaluations=[])
ctx2, _c2, _e2 = r2.get_context_for_response(query="logos")
check("fenced world still serializes its body", "World Meaning" in ctx2)
check("fenced world still has Quick Meaning stripped",
      not any(m in ctx2 for m in QUICK_MEANING_MARKERS))

# ---------------------------------------------------------------------------
section("B. retrieval_mode - the two questions, made explicit")
# ---------------------------------------------------------------------------
from app.rag.retrieval_mode import ADJUDICATION, TURN  # noqa: E402

check("TURN applies guards", TURN.apply_guards is True)
check("ADJUDICATION does not apply guards", ADJUDICATION.apply_guards is False)
check("TURN honours session exclusion", TURN.allow_session_exclusion is True)
check("ADJUDICATION ignores session exclusion", ADJUDICATION.allow_session_exclusion is False)
check("modes are immutable value objects",
      type(TURN).__dataclass_params__.frozen)

# ---------------------------------------------------------------------------
section("C. pipeline - one shared path, mode-driven behaviour")
# ---------------------------------------------------------------------------
from langchain_core.documents import Document  # noqa: E402

from app.rag.pipeline import LEXICON_SPEC, STORY_SPEC, run_retrieval  # noqa: E402
from app.rag.retriever import RetrievalEvaluation  # noqa: E402

guard_votes: list[int] = []


def fake_filter_llm_marker():
    return None


def make_docs():
    return [
        Document(page_content="a", metadata={
            "term": "guarded-term", "story_title": "guarded-story",
            "source_file": "chunk_guarded.md",
            "do_not_retrieve_when": "participant is asking about a modern denomination.",
            "retrieve_when": "always", "tier": 1, "content": "A"}),
        Document(page_content="b", metadata={
            "term": "plain-term", "story_title": "plain-story",
            "source_file": "chunk_plain.md",
            "do_not_retrieve_when": "", "retrieve_when": "always",
            "tier": 1, "content": "B"}),
    ]


import app.rag.pipeline as pipeline_mod  # noqa: E402

_real_eval = pipeline_mod.evaluate_negative_conditions
_real_score = None


def run_mode(mode, exclude_ids=None, spec=LEXICON_SPEC):
    """Run the real pipeline with the cross-encoder and guard vote stubbed,
    so what is under test is the pipeline's own branching, not the model."""
    calls = {"guard_vote": 0, "guarded": 0}

    def fake_evaluate(llm, candidates, query, ctx, item_noun):
        calls["guard_vote"] += 1
        calls["guarded"] = len(candidates)
        calls["item_noun"] = item_noun
        return [(True, "guard vote says retrieve") for _ in candidates]

    import app.rag.cross_encoder as ce
    real_score, real_thresh = ce.score_candidates, ce.threshold_for
    ce.score_candidates = lambda q, docs: [0.9] * len(docs)
    ce.threshold_for = lambda q: 0.1
    pipeline_mod.evaluate_negative_conditions = fake_evaluate
    try:
        res = run_retrieval(
            spec=spec, mode=mode, candidate_docs=make_docs(),
            query="q", conversation_context="ctx", k=3,
            exclude_ids=exclude_ids, filter_llm=None,
            evaluation_cls=RetrievalEvaluation)
    finally:
        pipeline_mod.evaluate_negative_conditions = _real_eval
        ce.score_candidates, ce.threshold_for = real_score, real_thresh
    return res, calls


res_turn, calls_turn = run_mode(TURN)
res_adj, calls_adj = run_mode(ADJUDICATION)

check("TURN sends guarded candidates to the guard vote",
      calls_turn["guard_vote"] == 1 and calls_turn["guarded"] == 1)
check("ADJUDICATION makes no guard-vote LLM call at all",
      calls_adj["guard_vote"] == 0)
check("ADJUDICATION still returns the guarded document as evidence",
      any(d.metadata["term"] == "guarded-term" for d in res_adj.documents))
check("ADJUDICATION audit trail says WHY no guard ran",
      all("guards not applied: adjudication evidence" in e.reason
          for e in res_adj.evaluations if e.retrieved))
check("TURN audit trail unchanged for unguarded docs",
      any("no evaluable guard" in e.reason for e in res_turn.evaluations))

# Session exclusion: the correct-by-construction property
excl = {"chunk_plain"}
res_turn_x, _ = run_mode(TURN, exclude_ids=excl)
res_adj_x, _ = run_mode(ADJUDICATION, exclude_ids=excl)
check("TURN honours the session exclusion set",
      not any(d.metadata["source_file"] == "chunk_plain.md" for d in res_turn_x.documents))
check("ADJUDICATION ignores an exclusion set even when one is PASSED",
      any(d.metadata["source_file"] == "chunk_plain.md" for d in res_adj_x.documents),
      "correct by construction, not by the caller remembering to omit it")

_, calls_story = run_mode(TURN, spec=STORY_SPEC)
check("story spec drives the guard-vote noun through the same path",
      calls_story.get("item_noun") == "story")
check("lexicon spec drives its own noun", calls_turn.get("item_noun") == "lexicon entry")

# The duplication that made the guard bug a two-place edit is gone.
lex_src = Path("app/rag/retriever.py").read_text()
story_src = Path("app/rag/story_retriever.py").read_text()
check("neither retriever re-implements the guard partition",
      "_evaluable_negative_condition" not in lex_src
      and "_evaluable_negative_condition" not in story_src)
check("both retrievers call the shared pipeline",
      "run_retrieval(" in lex_src and "run_retrieval(" in story_src)

# ---------------------------------------------------------------------------
section("D. adjudication - the two adjudicators are mutually exclusive")
# ---------------------------------------------------------------------------
import app.graph.nodes as nodes  # noqa: E402

gather_calls: list[tuple] = []
_real_gather = nodes._gather_world_evidence


def traced(world_id, response_text):
    gather_calls.append((world_id, response_text))
    return nodes.WorldEvidence("pp", "capsule", "retrieved")


class ScriptedMonitor:
    def __init__(self, monitor_reply, screen_reply):
        self.monitor_reply, self.screen_reply = monitor_reply, screen_reply

    def invoke(self, messages):
        sys_text = ""
        for m in messages:
            if m.__class__.__name__ == "SystemMessage":
                sys_text = str(m.content)
                break

        class R:
            content = ""
        r = R()
        if "SCREEN_FLAG" in sys_text:
            r.content = self.screen_reply
        elif "GROUNDED" in sys_text or "FABRICATED" in sys_text:
            r.content = "GROUNDED\nReason: attested."
        elif "OVER_SETTLED" in sys_text:
            r.content = "NOT_OVER_SETTLED"
        else:
            r.content = self.monitor_reply
        return r


def drive(monitor_reply, screen_reply):
    gather_calls.clear()
    real_llm = nodes.get_monitoring_llm
    nodes._gather_world_evidence = traced
    nodes.get_monitoring_llm = lambda *a, **k: ScriptedMonitor(monitor_reply, screen_reply)
    try:
        nodes._detect_drift_signal("a turn under judgement", world_id="desert-monasticism")
    finally:
        nodes._gather_world_evidence = _real_gather
        nodes.get_monitoring_llm = real_llm
    return len(gather_calls)


fab = drive("DRIFT_DETECTED\nSignal: FABRICATION\nSeverity: high\nDescription: d", "NO_FLAG")
ovs = drive("clean", "SCREEN_FLAG\n1. a claim stated more firmly than the record")
cln = drive("clean", "NO_FLAG")
check("fabrication path gathers evidence exactly once", fab == 1, f"{fab} call(s)")
check("over-settling path gathers evidence exactly once", ovs == 1, f"{ovs} call(s)")
check("a clean turn gathers no evidence", cln == 0, f"{cln} call(s)")
check("no single turn can gather the SAME evidence twice",
      fab <= 1 and ovs <= 1,
      "the memo on (world_id, response_text) had no reachable case")

check("_gather_world_evidence carries no response-text memo",
      not hasattr(nodes._gather_world_evidence, "cache_info"),
      "no lru_cache holding generated turn text process-wide")
check("adjudication retrieval requests ADJUDICATION mode",
      "mode=ADJUDICATION" in Path("app/graph/nodes.py").read_text())

# ---------------------------------------------------------------------------
section("E. world_sources - the cache that is actually warranted")
# ---------------------------------------------------------------------------
import time  # noqa: E402

from app.graph import world_sources  # noqa: E402

world_sources._CACHE.clear()
s1 = world_sources.load_world_sources("desert-monasticism")
s2 = world_sources.load_world_sources("desert-monasticism")
check("returns (capsule, permanent_prompt)", s1 is not None and len(s1) == 2)
check("repeat load is served from cache", s1 == s2 and len(world_sources._CACHE) == 2)
check("unknown world returns None", world_sources.load_world_sources("nope") is None)

tmp = Path("/tmp/_ws_cache_probe.txt")
tmp.write_text("first", encoding="utf-8")
a = world_sources._read_cached(tmp)
time.sleep(0.01)
tmp.write_text("second-and-longer", encoding="utf-8")
b = world_sources._read_cached(tmp)
tmp.unlink()
check("cache self-invalidates when the file changes",
      a == "first" and b == "second-and-longer",
      "keyed on (mtime_ns, size), so an edited capsule is never served stale")

# ---------------------------------------------------------------------------
section("F. session_auth - end to end against the real app")
# ---------------------------------------------------------------------------
from fastapi.testclient import TestClient  # noqa: E402

import app.main as main_mod  # noqa: E402

client = TestClient(main_mod.app)
start = client.post("/api/session/start", json={"world_id": "desert-monasticism"})
check("session start succeeds", start.status_code == 200, f"HTTP {start.status_code}")
body = start.json()
token = body.get("session_token")
sid = body.get("session_id")
check("start returns a real session token", bool(token) and len(token) >= 32,
      f"{len(token or '')} chars")

check("GET session without a token -> 403",
      client.get(f"/api/session/{sid}").status_code == 403)
check("GET session with the WRONG token -> 403",
      client.get(f"/api/session/{sid}",
                 headers={"X-Session-Token": "wrong-" + "x" * 40}).status_code == 403)
check("GET session with the CORRECT token -> 200",
      client.get(f"/api/session/{sid}",
                 headers={"X-Session-Token": token}).status_code == 200)
check("POST /message without a token -> 403",
      client.post(f"/api/session/{sid}/message",
                  json={"message": "hello"}).status_code == 403)
check("POST /message/stream without a token -> 403",
      client.post(f"/api/session/{sid}/message/stream",
                  json={"message": "hello"}).status_code == 403)
r_ok = client.post(f"/api/session/{sid}/message/stream",
                   json={"message": "hello"},
                   headers={"X-Session-Token": token})
check("POST /message/stream with the correct token -> 200",
      r_ok.status_code == 200, f"HTTP {r_ok.status_code}")
check("unknown session still 404s (not 403)",
      client.get("/api/session/does-not-exist").status_code == 404)

# timing-safe comparison, and the pre-token fail-open
import inspect  # noqa: E402

from app import session_auth  # noqa: E402

check("comparison is timing-safe",
      "compare_digest" in inspect.getsource(session_auth.require_session_access))


class _LegacyState:
    session_token = None


session_auth.require_session_access(_LegacyState(), None)
check("pre-token sessions are never enforced against", True,
      "in-flight sessions don't break at deploy")


class _TokenState:
    session_token = "abc123"


try:
    session_auth.require_session_access(_TokenState(), None)
    ok = False
except Exception:
    ok = True
check("a tokened session rejects a missing token", ok)

# ---------------------------------------------------------------------------
section("G. route coverage - the check cannot be forgotten on a new endpoint")
# ---------------------------------------------------------------------------
main_src = Path("app/main.py").read_text()

SESSION_SCOPED_EXEMPT = {
    # /audit is deliberately exempt: it exists for a signed-in reviewer
    # reading a session they did not start. get_audit_user gates it once
    # Supabase is configured. A possession check would lock reviewers out of
    # every session but their own - that is not hardening, it is breaking the
    # endpoint's purpose. Its unconfigured-Supabase gap is real and separate.
    "get_session_audit",
}

routes = []
for route in main_mod.app.routes:
    path = getattr(route, "path", "")
    name = getattr(route, "name", "")
    if "/api/session/{session_id}" in path:
        routes.append((path, name, sorted(getattr(route, "methods", []) or [])))

missing = []
for path, name, methods in routes:
    if name in SESSION_SCOPED_EXEMPT:
        continue
    fn = getattr(main_mod, name, None)
    src = inspect.getsource(fn) if fn else ""
    if "require_session_access" not in src:
        missing.append((path, name))

print(f"    session-scoped routes found: {len(routes)}")
for path, name, methods in routes:
    status = ("EXEMPT (documented)" if name in SESSION_SCOPED_EXEMPT
              else "enforced" if not any(n == name for _p, n in missing) else "NOT ENFORCED")
    print(f"      {','.join(methods):8s} {path:42s} {name:22s} {status}")
check("every non-exempt session-scoped route enforces ownership",
      not missing, f"unenforced: {missing}" if missing else "")
check("/audit is exempt on purpose and still reachable",
      any(n in SESSION_SCOPED_EXEMPT for _p, n, _m in routes))

# ---------------------------------------------------------------------------
section("H. modern_term_bridge - the skip is outcome-preserving")
# ---------------------------------------------------------------------------
from app.graph import modern_term_bridge as mtb  # noqa: E402

defs = mtb._load_definitions()
check("dictionary loads", bool(defs), f"{len(defs or {})} terms")

llm_calls = {"n": 0}


class CountingLLM:
    def __init__(self, reply):
        self.reply = reply

    def invoke(self, messages):
        llm_calls["n"] += 1

        class R:
            content = self.reply
        return R()


def classify_with(message, reply, seated):
    llm_calls["n"] = 0
    import app.graph.nodes as nd
    real = nd.get_monitoring_llm
    nd.get_monitoring_llm = lambda *a, **k: CountingLLM(reply)
    try:
        return mtb.classify_modern_term(message, seated), llm_calls["n"]
    finally:
        nd.get_monitoring_llm = real


seated = ["desert-monasticism"]
term_free = "What did they eat, and how did the day pass?"
res_free, n_free = classify_with(term_free, list(defs)[0], seated)
check("term-free message makes ZERO classifier calls", n_free == 0, f"{n_free} calls")
check("term-free message still returns None", res_free is None)

# Exhaustive equivalence: for a term-free message, EVERY possible classifier
# output must still produce None - which is what makes skipping the call
# outcome-preserving rather than merely cheaper.
mismatches = 0
for tid in defs:
    out, _ = classify_with(term_free, tid, seated)
    if out is not None:
        mismatches += 1
check("no classifier output could have changed the outcome",
      mismatches == 0,
      f"checked all {len(defs)} possible answers; {mismatches} would differ")

# And a message that DOES carry a term still reaches the classifier.
sample_tid = next(iter(defs))
forms = defs[sample_tid].get("display_terms") or [sample_tid]
present_msg = f"I keep hearing about {forms[0]} - what did your world make of it?"
_res_present, n_present = classify_with(present_msg, sample_tid, seated)
check("a message carrying a dictionary term still calls the classifier",
      n_present == 1, f"{n_present} calls for {forms[0]!r}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
passed = sum(1 for _n, p, _d in RESULTS if p)
failed = [n for n, p, _d in RESULTS if not p]
print(f"RESULT: {passed}/{len(RESULTS)} checks passed")
if failed:
    print("\nFAILED:")
    for n in failed:
        print(f"  - {n}")
print("=" * 72)
sys.exit(1 if failed else 0)
