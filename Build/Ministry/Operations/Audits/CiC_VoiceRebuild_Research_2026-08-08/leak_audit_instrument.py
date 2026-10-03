"""Leak audit instrument — CiC Voice Rebuild Research stage (2026-08-08).

Executes the app's own serialization path for every lexicon and story chunk
and scans what actually reaches generation context for internal
build-process language. THIS script produces every §4 number in
CiC_VoiceRebuild_Stage1_Research_Findings_2026-08-08.md, in two stages:

  Stage 1 (broad screen): wide pattern classes over serialized bodies —
  deliberately over-matching (it flags e.g. the by-design "modern hearing"
  Distortion Risk language, plus tier meta-language, scholar references,
  see-references). Used ONLY as a candidate pool; its file count (172,
  emitted as broad_screen_files) is NOT a leak count and is not reported
  as one. (The no-Key-Sources-marker fail-open list comes from the
  serialization step itself, not from either pattern stage.)

  Stage 2 (refined classification): the APPARATUS pattern set — gravity
  codes/numbering (incl. Tensional/Primary/Supporting), Doc_/Force
  references, template & assembly language (Final Assembly Instruction,
  L4-Templates, "per Template"), CT tags/Contest Type, Reciprocity Note,
  builder notes / "No brackets", and strand codes — with per-section
  attribution (nearest preceding heading/bold label). Produces
  leak_audit_apparatus_hits.json and the reported counts: files with >=1
  apparatus hit in serialized body (104/178), hits by section, files by
  world with per-world rates.

Run from anywhere; paths are absolute. Requires only the repo (heavy deps
are stubbed; the parsing/stripping code exercised is the app's own).
"""
import importlib.util
import json
import re
import sys
import types
from collections import Counter
from pathlib import Path

BACKEND = Path("/home/user/CIC-Project/cic-poc/backend")
OUT_DIR = Path(__file__).resolve().parent


def _stub(name, **attrs):
    m = types.ModuleType(name)
    for k, v in attrs.items():
        setattr(m, k, v)
    sys.modules[name] = m
    return m


_stub("langchain_community")
_stub("langchain_community.vectorstores", FAISS=object)
_stub("langchain_core")
_stub("langchain_core.documents", Document=object)
_stub("app.config", settings=types.SimpleNamespace(data_dir="", index_dir=""))
_stub("app.rag.embeddings", get_shared_embeddings=lambda *a, **k: None)
_stub("app")
_stub("app.rag")


def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, BACKEND / relpath)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sections = _load("app.rag.sections", "app/rag/sections.py")
indexer_mod = _load("app.rag.indexer", "app/rag/indexer.py")
story_indexer_mod = _load("app.rag.story_indexer", "app/rag/story_indexer.py")

KEY_SOURCES_MARKERS = sections.KEY_SOURCES_MARKERS
QUICK_MEANING_MARKERS = sections.QUICK_MEANING_MARKERS

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

lex_indexer = indexer_mod.LexiconIndexer()
story_indexer = story_indexer_mod.StoryIndexer()


def serialized_lexicon(f, migrated):
    entry = lex_indexer.parse_lexicon_file(f)
    body = entry.content
    no_marker = sections.find_section(body, KEY_SOURCES_MARKERS) is None
    body = sections.truncate_at(body, KEY_SOURCES_MARKERS)
    if migrated:
        body = sections.excise_section(body, QUICK_MEANING_MARKERS)
    return body, no_marker


def serialized_story(f):
    entry = story_indexer.parse_story_file(f)
    return entry.content


# Stage 1: the broad screen (candidate pool only — over-matches by design).
BROAD_PATTERNS = [
    re.compile(r"\b(?:Tensional|Primary|Supporting)\s+gravit|gravit(?:y|ies)\b", re.I),
    re.compile(r"\bDoc[_ ]?0\d|\bDoc_\d"),
    re.compile(r"\btemplate\b|L4-Templates|Final Assembly|per Template", re.I),
    re.compile(r"\bTier[- ][123]\b|\btier justification\b", re.I),
    re.compile(r"\bcandidate\b.{0,80}\btest(?:ed|ing)\b|\btest(?:ed|ing)\b.{0,80}\bcandidate\b", re.I | re.S),
    re.compile(r"\bCT\b(?:\s+(?:tag|Contest))?|Contest Type"),
    re.compile(r"\bbuilder(?:'s)? note|\bno brackets\b|\[TODO|\[NOTE", re.I),
    re.compile(r"\bConfidence:\s*(?:Inferential|Attested|Thin|Reconstructed|Probable)", re.I),
    re.compile(r"Reciprocity Note", re.I),
    re.compile(r"\bFLAG-\d+"),
    re.compile(r"\bSee [A-Z]{2,}\b|see .{0,40}\bbelow\b|see .{0,40}\babove\b", re.I),
    re.compile(r"Construction Framework|Source Ecology|World Identification", re.I),
    re.compile(r"\bscholar(?:s|ship)?\b|\bhistorian|\bacademic\b|\bmodern (?:scholar|historian|reader|hearing|assumption)", re.I),
    re.compile(r"Retrieval Front-Matter|front[- ]matter", re.I),
    re.compile(r"\bomitted\b.{0,60}\b(?:per|instruction)", re.I | re.S),
]

# Stage 2: the refined apparatus classification (the reported measure).
APPARATUS = re.compile(
    r"\bgravity \d|\bgravit(?:y|ies) [A-Z]?\d|\bG0\d\b|\bC\d\b(?= \()"
    r"|Doc_0\d|Force \d[A-C]|\bTensional\b|\bPrimary grav|\bSupporting grav"
    r"|Strand [A-C]\b|Final Assembly Instruction|L4-Templates|per Template"
    r"|CT tag|Contest Type|Reciprocity Note|builder notes?|No brackets")


def section_of(text, pos):
    head = None
    for m in re.finditer(r"^##+ (.+)$|^\*\*([^*]+):\*\*", text[:pos], re.M):
        head = m.group(1) or m.group(2)
    return head or "(top)"


apparatus_hits = {}
broad_screen_files = set()
no_ks_marker = []
fa_files = []
totals = Counter()

def scan_body(fname, wdir, kind, body):
    if any(rx.search(body) for rx in BROAD_PATTERNS):
        broad_screen_files.add(fname)
    if "Final Assembly Instruction" in body:
        fa_files.append(fname)
    secs = Counter(section_of(body, m.start())
                   for m in APPARATUS.finditer(body))
    if secs:
        apparatus_hits[fname] = {"world": wdir, "kind": kind,
                                 "sections": dict(secs)}

for wdir, wid in WORLD_DIRS.items():
    migrated = wid in MIGRATED
    for f in sorted((BACKEND / "data" / wdir / "lexicon_chunks").glob("*.md")):
        totals[("lex", wdir)] += 1
        body, no_marker = serialized_lexicon(f, migrated)
        if no_marker:
            no_ks_marker.append(f.name)
        scan_body(f.name, wdir, "lex", body)
    for f in sorted((BACKEND / "data" / wdir / "story_chunks").glob("*.md")):
        totals[("story", wdir)] += 1
        scan_body(f.name, wdir, "story", serialized_story(f))

sec_counter = Counter()
world_files = Counter()
world_totals = Counter()
for (kind, wdir), n in totals.items():
    world_totals[wdir] += n
for fname, d in apparatus_hits.items():
    world_files[d["world"]] += 1
    for s, n in d["sections"].items():
        sec_counter[s] += n

# Per-section file counts (how many files have >=1 hit in that section),
# alongside raw hit counts — both denominators, per review round 1 P2-9.
sec_files = Counter()
for d in apparatus_hits.values():
    for s in d["sections"]:
        sec_files[s] += 1

lex_total = sum(n for (k, w), n in totals.items() if k == "lex")
story_total = sum(n for (k, w), n in totals.items() if k == "story")

summary = {
    "lexicon_total": lex_total,
    "story_total": story_total,
    "migrated_world_ids": sorted(MIGRATED),
    "broad_screen_files": len(broad_screen_files),
    "apparatus_files": len(apparatus_hits),
    "apparatus_files_lex": sum(1 for d in apparatus_hits.values()
                               if d["kind"] == "lex"),
    "apparatus_files_story": sum(1 for d in apparatus_hits.values()
                                 if d["kind"] == "story"),
    "no_key_sources_marker": no_ks_marker,
    "final_assembly_reaches_model": sorted(fa_files),
    "hits_by_section": dict(sec_counter.most_common()),
    "files_by_section": dict(sec_files.most_common()),
    "per_world": {
        w: {"files_flagged": world_files[w], "files_total": world_totals[w],
            "rate": round(world_files[w] / world_totals[w], 2)}
        for w in sorted(world_totals)
    },
}

(OUT_DIR / "leak_audit_apparatus_hits.json").write_text(
    json.dumps({"summary": summary, "files": apparatus_hits}, indent=1))
print(json.dumps(summary, indent=1))
