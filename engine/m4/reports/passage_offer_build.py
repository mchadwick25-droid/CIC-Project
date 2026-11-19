"""Build the passage offer file for a world from Library's reviewed passage seed and the passage index.

  python -m engine.m4.reports.passage_offer_build --seed SEED.yaml --db INDEX.sqlite --out OFFER.json

The seed (Build/worlds/<world>/build/<world>_Passage_Seeds.yaml) names passages by index passage_id with
their byte span, voice, role, window, shelf binding, author, work, work date, fit and rank. This builder
reads each passage's text and marks from the index and writes the offer file the engine reads
(engine.m4.passage_offer). A seed made against another index version is refused. What is left out is
counted in the report:
  not_in_lens       the seed's shelf_binding is missing or is not "row narrowed ...": the file is on the
                    world's shelf but the work may not be, so the passage is not in the world's lens
  unresolved        the passage_id or its byte span differs from the index
  not_english       no English reading (nothing is rendered live)
  apparatus         an editor's note or heading
  no_source_label   no author and no work is named, so the voice could not say who writes
A passage is voiceable only when the seed says so, the seed's role is own, the index's one row role for
the world is tradition, the speaker is known, and the seed's window is inside; otherwise it is offered etic.
No model call.
"""
import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

import yaml

LENS_BINDING = "row narrowed"
_SMALL_WORDS = frozenset({"of", "the", "and", "de", "du", "von", "van", "in", "on", "to"})


def tag_for(world: str, passage_id: str) -> str:
    """The id a sentence cites a passage by. The citation grammar takes only [a-z0-9_.-], and an index passage id holds
    ':' and '#', so the passage is cited under a world-prefixed record-style id; the record keeps its index passage_id."""
    return f"{world}.passage.{hashlib.sha1(passage_id.encode()).hexdigest()[:12]}"


def _set(value) -> str | None:
    """A seed field's value, or None when the seed marks it unresolved or unset."""
    return value if isinstance(value, str) and value.strip() and not value.startswith(("unresolved", "unset", "unknown")) else None


def _name(slug: str | None) -> str | None:
    if not slug:
        return None
    words = slug.replace("-", " ").split()
    return " ".join(w if i and w in _SMALL_WORDS else w.capitalize() for i, w in enumerate(words))


def _date_text(date) -> str | None:
    """The work's date with its formation confidence, or None when the seed gives no dated window."""
    if not isinstance(date, dict) or date.get("start") is None or not date.get("formation_confidence"):
        return None
    years = str(date["start"]) if date.get("start") == date.get("end") else f"{date['start']} to {date['end']}"
    return f"{years}, {date['formation_confidence']}"


def build_offer(seed: dict, db_path: Path, seed_bytes: bytes | None = None) -> tuple[dict, dict]:
    header = seed.get("header") or {}
    world = header["world"]
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    meta = dict(connection.execute("SELECT key, value FROM meta"))
    if header.get("index_version") != meta.get("version"):
        raise SystemExit(f"the seed was made against index {str(header.get('index_version'))[:8]}, this index is {str(meta.get('version'))[:8]}; "
                         f"the offer is not built from a mismatched index")
    out: dict[str, list[dict]] = {}
    tags: dict[str, str] = {}
    report = {"seeds": 0, "offered": 0, "not_in_lens": 0, "unresolved": [], "not_english": 0, "apparatus": 0, "no_source_label": 0, "duplicates": 0}
    for sid, entry in (seed.get("subquestions") or {}).items():
        seen = set()
        for hit in entry.get("seeds") or []:
            report["seeds"] += 1
            if not str(hit.get("shelf_binding") or "").startswith(LENS_BINDING):
                report["not_in_lens"] += 1
                continue
            row = connection.execute("SELECT * FROM passages WHERE passage_id = ?", (hit["passage_id"],)).fetchone()
            if row is None or (row["byte_start"], row["byte_end"]) != (hit.get("byte_start"), hit.get("byte_end")):
                report["unresolved"].append([sid, hit["passage_id"]])
                continue
            if row["language"] != "eng":
                report["not_english"] += 1
                continue
            if row["apparatus"]:
                report["apparatus"] += 1
                continue
            if row["passage_id"] in seen:
                report["duplicates"] += 1
                continue
            speaker = hit.get("speaker") or {}
            author = _name(_set(speaker.get("name")) or _set(hit.get("author")))
            work = _set(hit.get("work"))
            if not author and not work:
                report["no_source_label"] += 1
                continue
            seen.add(row["passage_id"])
            roles = {r["role"] for r in connection.execute("SELECT role FROM passage_rows WHERE passage_id = ? AND world = ?", (row["passage_id"], world))}
            voiceable = (hit.get("voice") == "voiceable" and hit.get("role") == "own" and roles == {"tradition"} and row["speaker_state"] == "known"
                         and str(hit.get("window") or "").startswith("inside"))
            tag = tag_for(world, row["passage_id"])
            if tags.setdefault(tag, row["passage_id"]) != row["passage_id"]:
                raise SystemExit(f"passage tag collision on {tag}")
            out.setdefault(sid, []).append({
                "tag": tag, "passage_id": row["passage_id"], "file": row["file"], "text": row["text"], "word_count": row["word_count"],
                "locus": " ".join(x for x in (row["division_locus"], row["division_title"]) if x) or None,
                "speaker_state": row["speaker_state"], "ocr_score": row["ocr_score"], "role": hit.get("role"),
                "work": work, "author_name": author, "date": _date_text(hit.get("work_date")), "window": hit.get("window"),
                "fit": hit.get("fit"), "rank": hit.get("rank"), "voiceable": voiceable,
                "byte_start": row["byte_start"], "byte_end": row["byte_end"],
            })
            report["offered"] += 1
    connection.close()
    offer = {
        "world": world, "index_version": meta.get("version"), "seed_phase": header.get("phase"),
        "seed_sha256": hashlib.sha256(seed_bytes if seed_bytes is not None else yaml.safe_dump(seed, sort_keys=True).encode()).hexdigest(),
        "subquestions": out,
    }
    report["sub_questions_with_passages"] = len(out)
    return offer, report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--seed", type=Path, required=True)
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)
    raw = args.seed.read_bytes()
    offer, report = build_offer(yaml.safe_load(raw), args.db, raw)
    args.out.write_text(json.dumps(offer, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
