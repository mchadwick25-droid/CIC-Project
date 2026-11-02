"""Build the passage offer file for a world from a seed, the passage index and the vendored texts.

  python -m engine.m4.reports.passage_offer_build derive-seed --world lpc --out SEED.yaml
  python -m engine.m4.reports.passage_offer_build build --world lpc --seed SEED.yaml --db INDEX.sqlite --out OFFER.json

derive-seed reads the coverage maps' structured file-and-line hits and writes a seed marked
`status: derived-unreviewed`; Library's reviewed seed replaces it. build resolves each seed hit
to the one passage whose byte span holds that line, checks the seed's snippet against that
passage, and writes the offer file with the index version, the seed's hash and a report of what
resolved. A hit that does not resolve, or whose snippet is not in its passage, is listed in the
report and left out. A reviewed seed whose shelf_binding is not "row narrowed ..." (the file is on the world's
shelf but its work may not be) is not in the world's lens and is not offered; one outside the world's window is
offered etic. No model call.

Seed shape:
  world: lpc
  status: derived-unreviewed | reviewed
  subquestions:
    C5.S1:
      passages:
        - {file: x.xml, line: 68817, snippet: "...", layer: LOADED, role: own, voice_of: null, note: "..."}
        - {file: y.xml, ref: "Rom 5:12"}      # optional scripture-reference seed (not resolved here)
"""
import argparse
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
TEXTS = REPO_ROOT / "cic" / "texts"
STAGING = REPO_ROOT / "cic" / "corpus-map" / "_staging"
COVERAGE = REPO_ROOT / "Build" / "Ministry" / "Features" / "Question-Coverage" / "Coverage-Maps"
_WS = re.compile(r"\s+")


def tag_for(world: str, passage_id: str) -> str:
    """The id a sentence cites a passage by. The citation grammar takes only [a-z0-9_.-], and an index passage id holds
    ':' and '#', so the passage is cited under a world-prefixed record-style id; the record keeps its index passage_id."""
    return f"{world}.passage.{hashlib.sha1(passage_id.encode()).hexdigest()[:12]}"


def _norm(text: str) -> str:
    return _WS.sub(" ", re.sub(r"<[^>]*>", " ", text)).strip().lower()


def derive_seed(world: str) -> dict:
    subs: dict[str, dict] = {}
    prose_only = 0
    for path in sorted(COVERAGE.glob("C*-coverage.json")):
        cluster = path.name.split("-")[0]
        worlds = json.loads(path.read_text(encoding="utf-8")).get("worlds")
        cells = worlds.get(world) if isinstance(worlds, dict) else None
        if not isinstance(cells, dict):
            continue
        for sid, cell in cells.items():
            if not isinstance(cell, dict) or not re.fullmatch(r"S\d+", sid):
                continue
            passages = []
            for hit in cell.get("source_hits") or []:
                if isinstance(hit, dict) and hit.get("file") and hit.get("line"):
                    entry = {"file": Path(hit["file"]).name, "line": int(hit["line"]), "layer": cell.get("layer")}
                    if hit.get("snippet"):
                        entry["gloss"] = hit["snippet"]
                    passages.append(entry)
                else:
                    prose_only += 1
            if passages:
                subs[f"{cluster}.{sid}"] = {"passages": passages}
    return {"world": world, "status": "derived-unreviewed", "prose_only_hits_not_used": prose_only, "subquestions": subs}


def _line_offset(path: Path, line: int, cache: dict) -> int | None:
    if path not in cache:
        data = path.read_bytes()
        cache[path] = [0] + [m.end() for m in re.finditer(rb"\n", data)]
    starts = cache[path]
    return starts[line - 1] if 1 <= line <= len(starts) else None


def _staging_rows(file_name: str) -> dict[str, dict]:
    path = STAGING / (Path(file_name).stem + ".yaml")
    if not path.exists():
        return {}
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {r["row_id"]: r for r in doc.get("assignments") or [] if r.get("row_id")}


def _date_text(date) -> str | None:
    if isinstance(date, dict) and date.get("start") is not None:
        return str(date["start"]) if date.get("start") == date.get("end") else f"{date['start']} to {date['end']}"
    return None


def _file_work(staging: dict) -> str | None:
    """The work of a file when every row in it names the same one; None when the rows disagree."""
    works = {r.get("work") for r in staging.values() if r.get("work")}
    return next(iter(works)) if len(works) == 1 else None


def _label(slug: str | None) -> str | None:
    return slug.replace("-", " ").title() if slug else None


def build_offer(seed: dict, db_path: Path) -> tuple[dict, dict]:
    world = seed.get("world") or (seed.get("header") or {}).get("world")
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    meta = dict(connection.execute("SELECT key, value FROM meta"))
    header = seed.get("header") or {}
    if header.get("index_version") and header["index_version"] != meta.get("version"):
        raise SystemExit(f"the seed was made against index {header['index_version'][:8]}, this index is {str(meta.get('version'))[:8]}; the offer is not built from a mismatched index")
    offsets: dict = {}
    staging_cache: dict = {}
    out: dict[str, list[dict]] = {}
    report = {"hits": 0, "resolved": 0, "unresolved": [], "snippet_missing": [], "not_english": 0, "apparatus": 0, "duplicates": 0}
    for sid, entry in (seed.get("subquestions") or {}).items():
        seen = set()
        for hit in entry.get("seeds") or entry.get("passages") or []:
            if hit.get("shelf_binding") is not None and not str(hit["shelf_binding"]).startswith("row narrowed"):
                report["not_in_lens"] = report.get("not_in_lens", 0) + 1
                continue
            if hit.get("passage_id"):
                report["hits"] += 1
                row = connection.execute("SELECT * FROM passages WHERE passage_id = ?", (hit["passage_id"],)).fetchone()
                if row is None or (row["byte_start"], row["byte_end"]) != (hit.get("byte_start"), hit.get("byte_end")):
                    report["unresolved"].append([sid, hit["passage_id"], "id or byte span differs from the index"])
                    continue
                file_name = row["file"]
            else:
                if not hit.get("line"):
                    continue
                report["hits"] += 1
                file_name = Path(hit["file"]).name
                offset = _line_offset(TEXTS / file_name, int(hit["line"]), offsets) if (TEXTS / file_name).exists() else None
                row = None if offset is None else connection.execute(
                    "SELECT * FROM passages WHERE file = ? AND byte_start <= ? AND byte_end > ? ORDER BY byte_start LIMIT 1", (file_name, offset, offset)).fetchone()
                if row is None and offset is not None and (TEXTS / file_name).read_bytes()[offset:offset + 4] == b"<div":
                    row = connection.execute("SELECT * FROM passages WHERE file = ? AND byte_start >= ? ORDER BY byte_start LIMIT 1", (file_name, offset)).fetchone()
                if row is None:
                    report["unresolved"].append([sid, file_name, hit["line"]])
                    continue
                if hit.get("snippet") and _norm(hit["snippet"])[:80] not in _norm(row["text"]):
                    report["snippet_missing"].append([sid, file_name, hit["line"], row["passage_id"]])
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
            seen.add(row["passage_id"])
            rows = [dict(r) for r in connection.execute("SELECT row_id, role FROM passage_rows WHERE passage_id = ? AND world = ?", (row["passage_id"], world))] or [
                dict(r) for r in connection.execute("SELECT row_id, role FROM shelf_files WHERE file = ? AND world = ?", (file_name, world))]
            roles = {r["role"] for r in rows}
            role = next(iter(roles)) if len(roles) == 1 else "mixed"
            staging = staging_cache.setdefault(file_name, _staging_rows(file_name))
            detail = staging.get(rows[0]["row_id"], {}) if len(rows) == 1 else {}
            speaker = row["speaker_voice"] if row["speaker_state"] == "known" else None
            reviewed = "voice" in hit
            voiceable = hit["voice"] == "voiceable" if reviewed else role == "tradition" and row["speaker_state"] == "known"
            if voiceable and str(hit.get("window") or "").startswith("outside"):
                voiceable = False
            if voiceable and (row["speaker_state"] != "known" or row["apparatus"]):
                report["voiceable_but_index_disagrees"] = report.get("voiceable_but_index_disagrees", 0) + 1
                voiceable = False
            work = detail.get("work") or _file_work(staging)
            out.setdefault(sid, []).append({
                "tag": tag_for(world, row["passage_id"]), "passage_id": row["passage_id"], "file": file_name, "text": row["text"], "word_count": row["word_count"],
                "locus": " ".join(x for x in (row["division_locus"], row["division_title"]) if x) or None,
                "speaker_state": row["speaker_state"], "speaker": speaker, "ocr_score": row["ocr_score"], "role": role,
                "row_id": rows[0]["row_id"] if len(rows) == 1 else None, "work": work, "rank": hit.get("rank"),
                "author_name": _label(detail.get("author") or speaker), "date": _date_text(detail.get("date")),
                "voiceable": voiceable, "window": hit.get("window"), "seed_origin": "reviewed" if reviewed else "derived",
                "byte_start": row["byte_start"], "byte_end": row["byte_end"], "seed_line": hit.get("line"),
            })
            report["resolved"] += 1
    connection.close()
    seed_text = yaml.safe_dump(seed, sort_keys=True)
    offer = {
        "world": world, "index_version": meta.get("version"), "seed_status": seed.get("status") or (f"reviewed, phase {header.get('phase')}" if header else None),
        "seed_sha256": hashlib.sha256(seed_text.encode()).hexdigest(), "subquestions": out,
    }
    report["sub_questions_with_passages"] = len(out)
    return offer, report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("derive-seed")
    d.add_argument("--world", required=True)
    d.add_argument("--out", type=Path, required=True)
    b = sub.add_parser("build")
    b.add_argument("--world", required=True)
    b.add_argument("--seed", type=Path, required=True)
    b.add_argument("--db", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)
    if args.cmd == "derive-seed":
        seed = derive_seed(args.world)
        args.out.write_text(yaml.safe_dump(seed, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(f"seed {args.out}: {len(seed['subquestions'])} sub-questions, {sum(len(v['passages']) for v in seed['subquestions'].values())} hits, "
              f"{seed['prose_only_hits_not_used']} prose-only hits not used")
        return 0
    seed = yaml.safe_load(args.seed.read_text(encoding="utf-8"))
    offer, report = build_offer(seed, args.db)
    args.out.write_text(json.dumps(offer, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
