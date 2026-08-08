"""Leak audit: execute the app's real serialization path for every lexicon and
story chunk, and scan what actually reaches generation context for internal
build-process language. Research-stage instrument for the voice rebuild."""
import json
import re
import sys
from pathlib import Path

BACKEND = Path("/home/user/CIC-Project/cic-poc/backend")
sys.path.insert(0, str(BACKEND))

# Stub the heavy deps the indexer modules import at module level but that
# the parsing path never touches (FAISS, embeddings, settings/pydantic).
import types
def _stub(name, **attrs):
    m = types.ModuleType(name)
    for k, v in attrs.items():
        setattr(m, k, v)
    sys.modules[name] = m
    return m
_stub("langchain_community"); _stub("langchain_community.vectorstores", FAISS=object)
_stub("langchain_core"); _stub("langchain_core.documents", Document=object)
_stub("app.config", settings=types.SimpleNamespace(data_dir="", index_dir=""))
_stub("app.rag.embeddings", get_shared_embeddings=lambda *a, **k: None)

# Bypass app/__init__ and app/rag/__init__ entirely: register empty package
# stubs, then load the three needed modules directly from file.
import importlib.util
_stub("app"); _stub("app.rag")
def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, BACKEND / relpath)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
sections = _load("app.rag.sections", "app/rag/sections.py")
indexer_mod = _load("app.rag.indexer", "app/rag/indexer.py")
story_indexer_mod = _load("app.rag.story_indexer", "app/rag/story_indexer.py")
LexiconIndexer = indexer_mod.LexiconIndexer
StoryIndexer = story_indexer_mod.StoryIndexer
KEY_SOURCES_MARKERS = sections.KEY_SOURCES_MARKERS
QUICK_MEANING_MARKERS = sections.QUICK_MEANING_MARKERS
excise_section = sections.excise_section
find_section = sections.find_section
truncate_at = sections.truncate_at

# Worlds with a world_core record = migrated (repair_classifier._migrated_world_ids
# logic, reimplemented here to avoid importing app.graph's heavy deps)
RECORDS_ROOT = BACKEND / "wrs" / "records"
def migrated_world_ids():
    out = set()
    for p in RECORDS_ROOT.glob("*/world_core/*.md"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^world_id:\s*(\S+)", txt, re.M)
        if m:
            out.add(m.group(1))
    return out

MIGRATED = migrated_world_ids()

WORLD_DIRS = {
    "desert_world": "desert-monasticism",
    "pahc_world": "post-apostolic-house-church",
    "syriac_world": "syriac-edessa-nisibis",
    "alexandria_world": "alexandria-catechetical",
    "imperial_juridical_world": "imperial-juridical-christianity",
    "hieronymian_world": "hieronymian-ascetic-literary",
}

# Pattern classes for internal build-process language. Each: (label, regex).
PATTERNS = [
    ("gravity_apparatus", re.compile(r"\b(?:Tensional|Primary|Supporting)\s+gravit|gravit(?:y|ies)\b", re.I)),
    ("doc_apparatus", re.compile(r"\bDoc[_ ]?0\d|\bDoc_\d")),
    ("template_language", re.compile(r"\btemplate\b|L4-Templates|Final Assembly|per Template", re.I)),
    ("tier_meta", re.compile(r"\bTier[- ][123]\b|\btier justification\b", re.I)),
    ("candidate_tested", re.compile(r"\bcandidate\b.{0,80}\btest(?:ed|ing)\b|\btest(?:ed|ing)\b.{0,80}\bcandidate\b", re.I | re.S)),
    ("ct_tags", re.compile(r"\bCT\b(?:\s+(?:tag|Contest))?|Contest Type", )),
    ("builder_notes", re.compile(r"\bbuilder(?:'s)? note|\bno brackets\b|\[TODO|\[NOTE", re.I)),
    ("confidence_inline", re.compile(r"\bConfidence:\s*(?:Inferential|Attested|Thin|Reconstructed|Probable)", re.I)),
    ("reciprocity_note", re.compile(r"Reciprocity Note", re.I)),
    ("flag_ids", re.compile(r"\bFLAG-\d+")),
    ("see_reference", re.compile(r"\bSee [A-Z]{2,}\b|see .{0,40}\bbelow\b|see .{0,40}\babove\b", re.I)),
    ("construction_framework", re.compile(r"Construction Framework|Source Ecology|World Identification", re.I)),
    ("modern_scholars", re.compile(r"\bscholar(?:s|ship)?\b|\bhistorian|\bacademic\b|\bmodern (?:scholar|historian|reader|hearing|assumption)", re.I)),
    ("front_matter_leak", re.compile(r"Retrieval Front-Matter|front[- ]matter", re.I)),
    ("omitted_per", re.compile(r"\bomitted\b.{0,60}\b(?:per|instruction)", re.I | re.S)),
]

def scan(text, fname, kind, world, extra):
    hits = []
    for label, rx in PATTERNS:
        for m in rx.finditer(text):
            # grab the line containing the match
            start = text.rfind("\n", 0, m.start()) + 1
            end = text.find("\n", m.end())
            line = text[start:end if end != -1 else len(text)].strip()
            hits.append({"pattern": label, "line": line[:220]})
    # dedupe identical (pattern, line) pairs
    seen, out = set(), []
    for h in hits:
        k = (h["pattern"], h["line"])
        if k not in seen:
            seen.add(k)
            out.append(h)
    return {"file": fname, "kind": kind, "world": world, **extra, "hits": out}

results = []
lex_indexer = LexiconIndexer()
story_indexer = StoryIndexer()
lex_count = story_count = 0

for wdir, wid in WORLD_DIRS.items():
    migrated = wid in MIGRATED
    lex_dir = BACKEND / "data" / wdir / "lexicon_chunks"
    for f in sorted(lex_dir.glob("*.md")):
        lex_count += 1
        entry = lex_indexer.parse_lexicon_file(f)
        body = entry.content
        no_ks_marker = find_section(body, KEY_SOURCES_MARKERS) is None
        body = truncate_at(body, KEY_SOURCES_MARKERS)
        if migrated:
            body = excise_section(body, QUICK_MEANING_MARKERS)
        results.append(scan(body, f.name, "lexicon", wdir,
                            {"no_key_sources_marker": no_ks_marker,
                             "serialized_chars": len(body)}))
    story_dir = BACKEND / "data" / wdir / "story_chunks"
    for f in sorted(story_dir.glob("*.md")):
        story_count += 1
        entry = story_indexer.parse_story_file(f)
        body = entry.content
        results.append(scan(body, f.name, "story", wdir,
                            {"serialized_chars": len(body)}))

flagged = [r for r in results if r["hits"] or r.get("no_key_sources_marker")]
summary = {
    "lexicon_total": lex_count,
    "story_total": story_count,
    "migrated_world_ids": sorted(MIGRATED),
    "files_flagged": len(flagged),
    "lexicon_no_key_sources_marker": [r["file"] for r in results
                                      if r["kind"] == "lexicon" and r.get("no_key_sources_marker")],
    "hits_by_pattern": {},
}
for r in results:
    for h in r["hits"]:
        summary["hits_by_pattern"][h["pattern"]] = summary["hits_by_pattern"].get(h["pattern"], 0) + 1

out = {"summary": summary, "flagged": flagged}
outpath = Path("/tmp/claude-0/-home-user-CIC-Project/8bc789e8-47dc-5f6b-b9d5-68f381249a6e/scratchpad/leak_audit_raw.json")
outpath.write_text(json.dumps(out, indent=1))
print(json.dumps(summary, indent=1))
