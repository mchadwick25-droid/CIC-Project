"""S5.4 - the browsable repository + rights gate + FAIR export (Pass 1 SS5.6).

SS8-objective-3's double duty: the same records the Representative speaks
from, browsable as a real scholarly library - browse/search by domain, by
source, by figure, by contested claim; every record renders its Level 2
and Level 3 faces; `display_permitted` and rights fields gate what text
is shown publicly.

THE RIGHTS GATE (FLAG-013, fail-closed - the load-bearing rule):

  Third-party-derived text renders publicly ONLY when the source record
  it derives from states `display_permitted: true`. Unset is DENIED -
  today no Desert source states it (FLAG-013), so today zero verbatim
  quote text renders publicly; that is the honest state of the rights
  record, not a bug. What withholding looks like: metadata + attribution
  always render (locus, speaker, translation credit) - the road to the
  text is public even when the text is not.

  Gated text class (third-party-derived): `quote.text_translation` /
  `quote.text_original` (a published translation's wording, gated by the
  `translation_used` source row; no translation_used -> provenance
  unestablished -> withheld, uniformly). Project-authored prose (term
  senses, story retellings, gravity/force/claim analysis, voice fields)
  is CiC's own wording, not third-party text - it renders, with its
  apparatus, exactly as the running app already publishes it.

GENERALIZED TO ALL SIX WORLDS (2026-08-09). This builder was hardcoded to
Desert - `WORLD_ID = "desert-monasticism"`, `DATA_DIR = data/desert_world` -
so `data/<world>/repository.json` existed for exactly one world of six. The
app degrades silently on its absence (app/main.py checks `repo_path.exists()`
and moves on), which is why nothing ever surfaced: for five Representatives
the third level of Article 30 transparency - click a term, read the record
and its sources - was not broken, it was never built. Mark found the gap from
the reader's side on the live site the same day.

Nothing about the rights gate or the render layer changes here; `level3.py`
and `plain_explanation.py` were already world-agnostic (they take records as
arguments). Only the scoping moves.

Outputs (generated views, SS3.9 - regenerate, never hand-edit), per world:
  data/<world>/repository.json   browse/search index + per-record faces
  data/<world>/sources.json      FAIR machine-readable source export

Deterministic: same records -> byte-identical outputs. `--check` mode
re-renders and byte-compares without writing (the definitions.json
convention from S4.5).

Usage (from cic-poc/backend):
  python wrs/views/repository.py                 # write all six worlds
  python wrs/views/repository.py --world des     # one world
  python wrs/views/repository.py --check         # verify deployed views current
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
for p in (str(HERE), str(BACKEND)):
    if p not in sys.path:
        sys.path.insert(0, p)

from plain_explanation import render_plain_explanation  # noqa: E402
from level3 import render_level3, _title  # noqa: E402

import yaml  # noqa: E402

# key -> (world_id, records dir, deployed data dir). The records dir name is
# not carried by the world manifest, which is why it is spelled out here; the
# data dir is asserted against the manifest at run time so this table can
# never quietly disagree with what the app reads.
WORLDS = {
    "pahc": ("post-apostolic-house-church", "pahc_world", "pahc_world"),
    "ijc": ("imperial-juridical-christianity", "imperial_juridical_world",
            "imperial_juridical_world"),
    "alx": ("alexandria-catechetical", "alexandria_world", "alexandria_world"),
    "des": ("desert-monasticism", "desert_world", "desert_world"),
    "syr": ("syriac-edessa-nisibis", "syriac_world", "syriac_world"),
    "hal": ("hieronymian-ascetic-literary", "hieronymian_world",
            "hieronymian_world"),
}


def load_records(records_root: Path, subdir: str) -> dict[str, dict]:
    """Records of one type for one world.

    Same parse as chunk_views.load_records, which this replaces: that one
    closes over a module-level Desert RECORDS constant, so importing it was
    the single thing pinning this builder to one world. A missing subdir
    yields {} rather than raising - four of the six worlds carry no `quote`
    records at all, and that absence is a fact about the record set, not an
    error.
    """
    out: dict[str, dict] = {}
    d = records_root / subdir
    if not d.is_dir():
        return out
    for p in sorted(d.glob("*.md")):
        parts = p.read_text(encoding="utf-8").split("---\n")
        rec = yaml.safe_load(parts[1])
        rec["_body"] = "---\n".join(parts[2:])
        out[rec["id"]] = rec
    return out

RECORD_SUBDIRS = (
    "term", "story", "quote", "figure", "gravity", "force",
    "contested_claim", "source", "world_core",
)

WITHHELD_MARKER = (
    "[text withheld from public display - rights not established for the "
    "underlying source (FLAG-013 fail-closed); metadata and attribution "
    "above are the road to it]"
)


# ---------------------------------------------------------------- rights gate

def gated_quote_strings(quotes: dict[str, dict],
                        sources: dict[str, dict]) -> list[str]:
    """The exact third-party-derived strings whose display is not
    permitted - the quote records themselves establish both the wording
    and its provenance. Used to redact EMBEDDED occurrences (a story
    retelling that quotes the saying verbatim carries the same
    translation's wording - caught live on desertstory004, which embeds
    desertq001's Ward rendering). Mechanical detection covers exact
    embeddings only; paraphrase-level review belongs to FLAG-013's
    rights-authoring CO."""
    out = []
    for q in quotes.values():
        src_id = q.get("translation_used")
        src = sources.get(src_id) if src_id else None
        if not (src and src.get("display_permitted") is True):
            for field in ("text_translation", "text_original"):
                text = q.get(field)
                if isinstance(text, str) and text.strip():
                    out.append(text.strip())
    return sorted(out, key=len, reverse=True)


def _redact_embedded(value, gated: list[str]):
    if isinstance(value, str):
        for g in gated:
            if g in value:
                value = value.replace(g, WITHHELD_MARKER)
        return value
    if isinstance(value, list):
        return [_redact_embedded(v, gated) for v in value]
    if isinstance(value, dict):
        return {k: _redact_embedded(v, gated) for k, v in value.items()}
    return value


def display_gate(rec: dict, sources: dict[str, dict],
                 gated: list[str]) -> tuple[dict, dict]:
    """Return (public_copy, rights_note) - the record with gated text
    withheld, plus a machine-readable statement of what was decided.

    Fail-closed: third-party-derived text renders only on an explicit
    display_permitted: true on its provenance source row. The rule
    follows the text wherever it appears: whole fields on the quote
    record itself, exact embedded occurrences everywhere else."""
    rights = {"gated_fields": [], "basis": None}

    if rec.get("record_type") == "quote":
        pub = copy.deepcopy(rec)
        src_id = rec.get("translation_used")
        src = sources.get(src_id) if src_id else None
        if src and src.get("display_permitted") is True:
            rights["basis"] = f"display_permitted: true on {src_id}"
            return pub, rights
        for field in ("text_translation", "text_original"):
            if pub.get(field):
                pub[field] = WITHHELD_MARKER
                rights["gated_fields"].append(field)
        rights["basis"] = (
            f"withheld: {src_id or 'no translation_used row'} states no "
            "display permission (unset is denied - FLAG-013)"
        )
        return pub, rights

    # every other record: redact exact embedded occurrences of gated text
    pub = _redact_embedded(copy.deepcopy(rec), gated)
    if pub != rec:
        rights["gated_fields"].append("embedded-quote-text")
        rights["basis"] = (
            "embedded third-party translation wording redacted "
            "(same fail-closed rule; FLAG-013)"
        )
    return pub, rights


# ------------------------------------------------------------------- indexes

def _search_text(rec: dict, title: str) -> str:
    """Searchable text for one PUBLIC record copy - built after the gate,
    so withheld text can never be found by substring search either."""
    parts = [title, rec.get("id", ""), rec.get("record_type", "")]
    for key in ("term", "aliases", "quick_meaning", "period_sense",
                "modern_sense", "semantic_domain", "title", "text",
                "locus", "claim", "name", "work_author", "work_title",
                "work_locus", "attested_occasion"):
        v = rec.get(key)
        if isinstance(v, str) and v != WITHHELD_MARKER:
            parts.append(v)
        elif isinstance(v, list):
            parts.extend(x for x in v if isinstance(x, str))
    return " ".join(parts).lower()


def build_repository(world_id: str, records_root: Path) -> dict:
    all_records: dict[str, dict] = {}
    by_type: dict[str, dict] = {}
    for sub in RECORD_SUBDIRS:
        recs = load_records(records_root, sub)
        by_type[sub] = recs
        all_records.update(recs)
    sources = by_type["source"]
    gated = gated_quote_strings(by_type["quote"], sources)

    entries = []
    by_domain: dict[str, list[str]] = {}
    by_source: dict[str, list[str]] = {}
    by_figure: dict[str, list[str]] = {}
    by_claim: dict[str, list[str]] = {}

    for rid in sorted(all_records):
        rec = all_records[rid]
        public, rights = display_gate(rec, sources, gated)
        title = _title(public)

        entry = {
            "id": rid,
            "record_type": public.get("record_type"),
            "title": title,
            "rights": rights,
            "level3": render_level3(public, sources, all_records),
            "search_text": _search_text(public, title),
        }
        if public.get("record_type") == "term":
            entry["level2"] = render_plain_explanation(public)
            dom = public.get("semantic_domain")
            if dom:
                by_domain.setdefault(dom, []).append(rid)

        for s in public.get("sources", []) or []:
            sid = s.get("source_id")
            if sid:
                by_source.setdefault(sid, []).append(rid)
        if public.get("translation_used"):
            by_source.setdefault(public["translation_used"], []).append(rid)

        if public.get("record_type") == "story" and public.get("owner_figure_id"):
            by_figure.setdefault(public["owner_figure_id"], []).append(rid)
        if public.get("record_type") == "quote" and public.get("speaker_or_author"):
            by_figure.setdefault(public["speaker_or_author"], []).append(rid)
        if public.get("record_type") == "figure":
            for stid in public.get("story_ids", []) or []:
                by_figure.setdefault(rid, []).append(stid)

        for cid in public.get("contested_claim_ids", []) or []:
            by_claim.setdefault(cid, []).append(rid)

        entries.append(entry)

    claim_note = (
        "truthfully empty: no record in this world populates "
        f"contested_claim_ids, so nothing cross-references the "
        f"{len(by_type['contested_claim'])} claims - they remain browsable as "
        "records in their own right (Desert's FLAG-014 condition)"
    ) if not by_claim else None

    return {
        "view": "repository (S5.4, Pass 1 SS5.6)",
        "world_id": world_id,
        "generated_by": "wrs/views/repository.py - regenerate, never hand-edit",
        "rights_rule": (
            "fail-closed: third-party-derived text renders only on an "
            "explicit display_permitted: true on its provenance source row "
            "(FLAG-013)"),
        "record_count": len(entries),
        "records": entries,
        "browse": {
            "by_domain": {k: sorted(set(v)) for k, v in sorted(by_domain.items())},
            "by_source": {k: sorted(set(v)) for k, v in sorted(by_source.items())},
            "by_figure": {k: sorted(set(v)) for k, v in sorted(by_figure.items())},
            "by_contested_claim": {k: sorted(set(v)) for k, v in sorted(by_claim.items())},
            # present ONLY when the index is empty - the note exists to
            # explain an emptiness, and five of the six worlds do populate
            # contested_claim_ids, so carrying it everywhere would state a
            # falsehood about them.
            **({"by_contested_claim_note": claim_note} if claim_note else {}),
        },
    }


# ---------------------------------------------------------------- FAIR export

def _id_prefix(ids: list) -> str:
    """The shared leading run of the source ids, with the varying tail shown
    as n's - e.g. srcDES001/srcDES002 -> 'srcDESnnn'. Derived rather than
    declared so a world whose ids do not follow the pattern reports what it
    actually has instead of a comfortable fiction."""
    if not ids:
        return "no source records"
    first, last = ids[0], ids[-1]
    i = 0
    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1
    return first[:i] + "n" * (len(first) - i)

def build_sources_json(world_id: str, records_root: Path) -> dict:
    """sources.json - the FAIR export (SS5.6): stable ids, machine-readable,
    external identifiers, stated rights. Beside the existing
    source_registry.json convention, not replacing it."""
    sources = load_records(records_root, "source")
    rows = []
    for sid in sorted(sources):
        s = sources[sid]
        rows.append({
            "id": sid,
            "world_id": world_id,
            "work_author": s.get("work_author"),
            "work_title": s.get("work_title"),
            "work_locus": s.get("work_locus"),
            "edition": s.get("edition"),
            "translation": s.get("translation"),
            "language": s.get("language"),
            "script": s.get("script"),
            "source_type": s.get("source_type"),
            "attribution_status": s.get("attribution_status"),
            "external_ids": s.get("external_ids") or [],
            "transmission_path": s.get("transmission_path"),
            "field_state": s.get("field_state"),
            "discovery": {
                "channel": s.get("discovery_channel"),
                "instrument": s.get("discovery_instrument"),
                "date": s.get("discovery_date"),
            },
            "rights": {
                "rights_status": s.get("rights_status"),
                "license": s.get("license"),
                "display_permitted": s.get("display_permitted"),
                "note": (None if s.get("display_permitted") is not None else
                         "unstated - treated as not permitted for public "
                         "full-text display (FLAG-013 fail-closed)"),
            },
        })
    # the id prefix is READ from the record set, never assumed: the six
    # worlds do not share a scheme (srcDESnnn, srcIJCnn, srcPAHCPnn...).
    prefix = _id_prefix(sorted(rows and [r["id"] for r in rows] or []))
    return {
        "view": "sources.json - FAIR export (S5.4, Pass 1 SS5.6)",
        "world_id": world_id,
        "generated_by": "wrs/views/repository.py - regenerate, never hand-edit",
        "id_scheme": (
            "record ids are stable within this repository "
            f"({prefix}; referenced by every record's sources[] rows)"),
        "source_count": len(rows),
        "sources": rows,
    }


# ----------------------------------------------------------------------- main

def _dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    keys = sorted(WORLDS)
    if "--world" in argv:
        want = argv[argv.index("--world") + 1]
        if want not in WORLDS:
            print(f"unknown world {want!r} - choose from {keys}")
            return 2
        keys = [want]

    # the data dir this writes into must be the one the app reads, or the
    # view lands where nothing looks for it - the exact failure an earlier
    # candidate-tree bug produced by writing alx_* files beside the real
    # alex_* ones and reporting success.
    from app.world_manifest import WORLD_MANIFEST
    manifest = {e.world_id: e.data_dir_name for e in WORLD_MANIFEST}

    outputs: dict[Path, str] = {}
    for key in keys:
        world_id, records_dirname, data_dirname = WORLDS[key]
        expected = manifest.get(world_id)
        if expected != data_dirname:
            print(f"FAIL - {key}: table says data dir {data_dirname!r}, "
                  f"manifest says {expected!r}. Refusing to write a view the "
                  f"app would not read.")
            return 2
        records_root = BACKEND / "wrs" / "records" / records_dirname
        data_dir = BACKEND / "data" / data_dirname
        outputs[data_dir / "repository.json"] = _dump(
            build_repository(world_id, records_root))
        outputs[data_dir / "sources.json"] = _dump(
            build_sources_json(world_id, records_root))

    stale = []
    for path, text in outputs.items():
        if check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != text:
                stale.append(f"{path.parent.name}/{path.name}")
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
            recs = text.count('"id":')
            print(f"written: {path.relative_to(BACKEND)}  ({recs} ids)")
    if check:
        if stale:
            print(f"STALE: {', '.join(stale)} - regenerate with "
                  "python wrs/views/repository.py")
            return 1
        print(f"current: {len(outputs)} views byte-match regeneration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
