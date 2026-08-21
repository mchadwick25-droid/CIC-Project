"""Deterministic builders: records -> the compiled/ half of a World Package
(Artifact-2 SS1). Every function here is pure - same records in, same bytes
out, no wall clock, no randomness, no network. Content-only; the
`generated-by` header stamping (Artifact-2 SS3) happens once, centrally, in
compiler.py, so it doesn't have to be threaded through every function here.
"""
import hashlib

from engine.m1 import canon

from .canonical import canonical_json

CHUNK_DIR_BY_TYPE = {
    "term": "lexicon",
    "story": "story",
    "ambient": "ambient",
    "doctrinal_witness": "doctrinal_witness",
}


def _by_type(records: dict, record_type: str) -> list[dict]:
    return sorted((r for r in records.values() if r.get("record_type") == record_type), key=lambda r: r["id"])


def _one(records: dict, record_type: str) -> dict | None:
    hits = _by_type(records, record_type)
    return hits[0] if hits else None


# ---- compiled/prompt.txt ----------------------------------------------


def build_prompt(records: dict) -> bytes:
    segments: list[str] = []

    def emit(header: str, body: str | None) -> None:
        if body and body.strip():
            segments.append(f"## {header}\n\n{body.strip()}\n")

    craft = _one(records, "voice_craft")
    if craft:
        emit("Identity", craft.get("identity"))

    core = _one(records, "world_core")
    if core:
        emit("Horizon", core.get("horizon"))
        emit("Formation logic", core.get("formation_logic"))
        emit("Thinness", core.get("thinness"))
        emit("Cautions", core.get("cautions"))

    if craft:
        emit("Guard", craft.get("guard"))
        concerns = craft.get("characteristic_concerns") or []
        if concerns:
            emit("Characteristic concerns", "\n".join(f"- {c}" for c in concerns))
        notes = craft.get("flavor_notes") or []
        if notes:
            emit(
                "Flavor notes",
                "\n".join(f"- [{n.get('segment')}] {n.get('note')}" for n in notes),
            )

    for term in _by_type(records, "term"):
        body = "\n\n".join(filter(None, [term.get("plain_meaning"), term.get("quick_meaning")]))
        emit(f"Term: {term.get('world_word', term['id'])}", body)

    for witness in _by_type(records, "doctrinal_witness"):
        cells = ",".join(witness.get("canon_cells") or [])
        emit(f"Witness ({cells})", witness.get("text"))

    for limit in _by_type(records, "honest_limit"):
        cells = ",".join(limit.get("canon_cells") or [])
        emit(f"Honest limit ({cells})", limit.get("statement"))

    for story in _by_type(records, "story"):
        body = "\n\n".join(filter(None, [story.get("tellable_as"), story.get("text")]))
        emit(f"Story: {story['id']}", body)

    for demo in _by_type(records, "demonstration"):
        exchange = demo.get("exchange") or []
        body = "\n".join(f"{turn['speaker']}: {turn['text']}" for turn in exchange)
        emit(f"Demonstration: {demo['id']}", body)

    return ("\n".join(segments) + "\n").encode("utf-8")


# ---- compiled/capsule.md ------------------------------------------------


def build_capsule(records: dict, registry_entry: dict) -> bytes:
    core = _one(records, "world_core") or {}
    rep = registry_entry.get("representative") or {}
    window = registry_entry.get("time_window") or {}
    lines = [
        f"# {registry_entry.get('display_name', '')}",
        "",
        f"Representative: {rep.get('name', '')} ({rep.get('role_label', '')})",
        f"Time window: {window.get('start')}-{window.get('end')}",
        f"Place: {registry_entry.get('place', '')}",
        "",
        "## Thinness",
        registry_entry.get("thinness_statement", ""),
        "",
        "## Cautions",
        core.get("cautions", ""),
    ]
    return ("\n".join(lines) + "\n").encode("utf-8")


# ---- compiled/chunks/{lexicon,story,ambient,doctrinal_witness}/*.md ----
# Artifact-2 SS1 names chunks/{lexicon,story,ambient}/ explicitly; Artifact-1
# SS3 lists doctrinal_witness as a fourth chunk-feeding (retrieval-block)
# type. Adding a fourth directory that follows the same one-file-per-record
# pattern is the minimal, fully-determined resolution of that gap - DECIDABLE
# (Build-Blueprint.md SS4), not a spec contradiction needing Mark's input.


def _chunk_text(record: dict) -> str:
    record_type = record["record_type"]
    lines = [f"id: {record['id']}", f"canon_cells: {','.join(record.get('canon_cells') or [])}", ""]
    if record_type == "term":
        lines += [record.get("plain_meaning", ""), "", f"world_word: {record.get('world_word', '')}", "", record.get("quick_meaning", "")]
    elif record_type == "story":
        lines += [record.get("tellable_as", ""), "", record.get("text", "")]
    elif record_type == "ambient":
        lines += [record.get("detail", "")]
    elif record_type == "doctrinal_witness":
        lines += [record.get("text", "")]
    return "\n".join(lines) + "\n"


def build_chunks(records: dict) -> dict[str, bytes]:
    out = {}
    for record in records.values():
        record_type = record.get("record_type")
        chunk_dir = CHUNK_DIR_BY_TYPE.get(record_type)
        if chunk_dir is None:
            continue
        out[f"compiled/chunks/{chunk_dir}/{record['id']}.md"] = _chunk_text(record).encode("utf-8")
    return out


# ---- compiled/indexes/{lexicon,story}.faiss -----------------------------
# DECIDABLE placeholder (recorded in the stage-2 commit): a real semantic
# embedding requires a model/provider choice, which spec principle 11 rules
# lands last and alone - not smuggled into compiler infrastructure ahead of
# M4 (stage 5). This is a deterministic, hash-derived pseudo-vector purely so
# the .faiss file/hash pipeline is exercised end-to-end now; it carries no
# semantic meaning and says so in its own "format" field.


def _pseudo_vector(text: str, dim: int = 8) -> list[float]:
    digest = hashlib.sha256((text or "").encode("utf-8")).digest()
    return [digest[i % len(digest)] / 255 for i in range(dim)]


def _index_blob(entries: list[dict]) -> bytes:
    return canonical_json(
        {
            "format": "cic-m2-placeholder-index-v1",
            "dim": 8,
            "note": (
                "deterministic hash-derived placeholder, NOT a semantic embedding - "
                "real retrieval vectors are an M4/stage-5 decision (spec principle 11: "
                "model/provider switches land last and alone)"
            ),
            "entries": entries,
        }
    )


def build_indexes(records: dict) -> dict[str, bytes]:
    lexicon_entries = [
        {"id": r["id"], "vector": _pseudo_vector((r.get("plain_meaning") or "") + (r.get("quick_meaning") or ""))}
        for r in _by_type(records, "term")
    ]
    story_entries = [
        {"id": r["id"], "vector": _pseudo_vector(r.get("text") or "")} for r in _by_type(records, "story")
    ]
    return {
        "compiled/indexes/lexicon.faiss": _index_blob(lexicon_entries),
        "compiled/indexes/story.faiss": _index_blob(story_entries),
    }


# ---- compiled/quotes.json, figures.json, repository.json ----------------


def build_quotes_json(records: dict) -> bytes:
    quotes = [
        {
            "id": q["id"],
            "text": q.get("text"),
            "speaker_or_author": q.get("speaker_or_author"),
            "license": q.get("license"),
            "canon_cells": q.get("canon_cells") or [],
            "sources": q.get("sources") or [],
        }
        for q in _by_type(records, "quote")
    ]
    return canonical_json({"quotes": quotes})


def build_figures_json(records: dict) -> bytes:
    figures = [
        {
            "id": f["id"],
            "names": f.get("names") or [],
            "dates": f.get("dates") or {},
            "narratable": f.get("narratable"),
            "bridge_line": f.get("bridge_line"),
        }
        for f in _by_type(records, "figure")
    ]
    return canonical_json({"figures": figures})


def build_repository_json(records: dict) -> bytes:
    entries = [
        {k: v for k, v in record.items() if not k.startswith("_")}
        for record in sorted(records.values(), key=lambda r: r["id"])
    ]
    return canonical_json({"records": entries})


# ---- compiled/coverage.json ----------------------------------------------

# Analytical record types eligible for the per-cell "analytical" list below.
# Deliberately NOT passed through canon.classify_cell / substantive_types():
# that function is the single spec-mandated implementation of Artifact-1
# SS6's coverage rule ("every open world has >=1 doctrinal_witness/term/
# story/quote OR exactly one honest_limit per cell") - an admission-gate
# question. Whether a gravity/force/contested_claim record can retrieval-
# ground a turn is a different question (M4's evidence assembly, not M1
# admission), and folding these three types into substantive_types() would
# silently let a cell pass SS6 coverage on analytical material alone,
# changing what the gate means. So they get their own field, computed the
# same way (canon_cells membership) but never touching "status" or
# "substantive".
_ANALYTICAL_TYPES = {"gravity", "force", "contested_claim"}


def build_coverage_json(records: dict, fleet: dict) -> bytes:
    out = {}
    for cell in sorted(canon.valid_cells(fleet)):
        classification = canon.classify_cell(cell, records)
        substantive_ids = classification["substantive"]
        figures = sorted(
            {
                records[rid]["speaker_or_author"]
                for rid in substantive_ids
                if records[rid].get("record_type") == "quote" and records[rid].get("speaker_or_author")
            }
        )
        analytical_ids = sorted(
            rid
            for rid, r in records.items()
            if r.get("record_type") in _ANALYTICAL_TYPES and cell in (r.get("canon_cells") or [])
        )
        out[cell] = {
            "status": classification["status"],
            "terms": [rid for rid in substantive_ids if records[rid]["record_type"] == "term"],
            "stories": [rid for rid in substantive_ids if records[rid]["record_type"] == "story"],
            "quotes": [rid for rid in substantive_ids if records[rid]["record_type"] == "quote"],
            "doctrinal_witness": [rid for rid in substantive_ids if records[rid]["record_type"] == "doctrinal_witness"],
            "figures": figures,
            "honest_limit": classification["honest_limit"],
            "gravities": [rid for rid in analytical_ids if records[rid]["record_type"] == "gravity"],
            "forces": [rid for rid in analytical_ids if records[rid]["record_type"] == "force"],
            "contested_claims": [rid for rid in analytical_ids if records[rid]["record_type"] == "contested_claim"],
        }
    return canonical_json(out)


# ---- compiled/frame.json --------------------------------------------------
# O8: only the General/Seeker voice exists through pilot and Phase 1, so
# "frames" carries exactly one key on purpose - not an oversight.


def build_frame_json(records: dict, fleet: dict, registry_entry: dict) -> bytes:
    starters = []
    for cell in sorted(canon.valid_cells(fleet)):
        classification = canon.classify_cell(cell, records)
        if classification["status"] != "substantive":
            continue
        question = next(
            (r for r in fleet.values() if r.get("record_type") == "canon_question" and r.get("cell") == cell),
            None,
        )
        if question:
            starters.append({"cell": cell, "text": question["text"]})

    payload = {
        "representative": registry_entry.get("representative"),
        "display_name": registry_entry.get("display_name"),
        "time_window": registry_entry.get("time_window"),
        "place": registry_entry.get("place"),
        "thinness_statement": registry_entry.get("thinness_statement"),
        "living_tradition_flag": registry_entry.get("living_tradition_flag", False),
        "frames": {"general_seeker": {"starters": starters}},
    }
    return canonical_json(payload)


# ---- media/portrait.svg ----------------------------------------------------
# Deterministic placeholder graphic - no image-generation call, honest about
# what it is (a labeled silhouette), sized/shaped for the doorway card.


def build_media(registry_entry: dict) -> dict[str, bytes]:
    rep = registry_entry.get("representative") or {}
    name, role = rep.get("name", ""), rep.get("role_label", "")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">'
        '<rect width="240" height="240" fill="#e8e2d4"/>'
        '<circle cx="120" cy="95" r="45" fill="#b9ac8f"/>'
        '<rect x="55" y="150" width="130" height="70" rx="20" fill="#b9ac8f"/>'
        f'<text x="120" y="205" font-family="sans-serif" font-size="14" fill="#3a3226" '
        f'text-anchor="middle">{name} - {role}</text>'
        "</svg>\n"
    )
    return {"compiled/media/portrait.svg": svg.encode("utf-8")}
