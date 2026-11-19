"""Run the segmenter over the union of the built worlds' shelves.

  python -m answering_library.run [--out DIR] [--workers N] [--only FILE ...]

Writes <out>/passages/<file-stem>.jsonl for every source file and
<out>/manifest.json. Two passes: the first builds the word vocabulary the OCR
score needs, the second segments and writes. Both are deterministic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import re
import subprocess
import time
from collections import Counter
from pathlib import Path

from . import markup as mu
from . import curation, ocr, passages, plain, segment
from .langscript import _latin_choice
from .textio import Source
from .union import REPO_ROOT, UnionEntry, build_union

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "out"
_VOCAB: ocr.Vocabulary | None = None
_OUT: Path | None = None
_TOKEN = re.compile(r"[^\W\d_]+", re.UNICODE)


def _token_language(token: str, latin_lang: str) -> str | None:
    c = token[0]
    o = ord(c)
    if 0x370 <= o < 0x400 or 0x1F00 <= o < 0x2000:
        return "grc"
    if 0x400 <= o < 0x530:
        return "rus"
    if o < 0x250 or 0x1E00 <= o < 0x1F00:
        return latin_lang
    return None


def vocab_task(entry: UnionEntry) -> tuple[str, dict[str, Counter]]:
    src = Source.read(entry.path)
    raw = src.text
    text = re.sub(r"<[^>]*>", " ", raw) if (entry.suffix == ".xml" or mu.looks_like_markup(raw)) else raw
    codes = segment.codes_for(entry.filename, raw)
    latin_codes = [c for c in codes if c not in ("grc", "rus", "chu", "ara", "syr", "heb", "hye", "gez", "cop")] or ["eng"]
    latin_lang = _latin_choice(text[:20000], latin_codes)
    out: dict[str, Counter] = {}
    for tok, n in ocr.token_counts(text).items():
        lang = _token_language(tok, latin_lang)
        if lang:
            out.setdefault(lang, Counter())[tok] = n
    return entry.filename, out


def _verify(path: Path, records_n: int, summary: dict, src_bytes: bytes, markup_mode: bool) -> dict:
    lines = path.read_bytes().split(b"\n")
    if lines and lines[-1] == b"":
        lines.pop()
    rows = [json.loads(x) for x in lines]
    words_field = sum(r["word_count"] for r in rows)
    words_text = sum(len(r["text"].split()) for r in rows)
    per_div_n: Counter = Counter()
    by_div_words: dict[str, int] = {}
    for r in rows:
        by_div_words[r["division_locus"]] = by_div_words.get(r["division_locus"], 0) + r["word_count"]
        per_div_n[r["division_locus"]] += 1
    count_mismatch = 0
    for loc, w in by_div_words.items():
        expected = max(1, math.ceil(w / passages.MAX_WORDS))
        if per_div_n[loc] != expected:
            count_mismatch += 1
    exact = with_suppressed = bad = 0
    if not markup_mode:
        for r in rows:
            seg = src_bytes[r["byte_start"]:r["byte_end"]].decode("utf-8", errors="surrogateescape").split()
            own = r["text"].split()
            if seg == own:
                exact += 1
            else:
                it = iter(seg)
                if all(tok in it for tok in own):
                    with_suppressed += 1
                else:
                    bad += 1
    gap = None
    if markup_mode:
        w = words_field
        gap = 0 if summary["independent_word_count_lower"] <= w <= summary["independent_word_count"] else (
            w - summary["independent_word_count"] if w > summary["independent_word_count"]
            else w - summary["independent_word_count_lower"])
    else:
        gap = summary["independent_word_count"] - summary["furniture_words"] - words_field
    return {
        "lines_on_disk": len(rows),
        "lines_equal_records": len(rows) == records_n,
        "words_by_field": words_field,
        "words_by_text_resplit": words_text,
        "words_gap_to_independent": gap,
        "divisions_with_count_mismatch": count_mismatch,
        "verbatim_exact": exact,
        "verbatim_with_suppressed_furniture": with_suppressed,
        "verbatim_mismatch": bad,
    }


def segment_task(entry: UnionEntry) -> dict:
    t0 = time.time()
    src = Source.read(entry.path)
    records, summary = segment.segment(entry, _VOCAB, src)
    out_path = _OUT / "passages" / (Path(entry.filename).stem + ".jsonl")
    h = hashlib.sha256()
    with open(out_path, "wb") as fh:
        for r in records:
            line = (json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8", errors="replace")
            h.update(line)
            fh.write(line)
    markup_mode = summary["mode"] == "markup"
    check = _verify(out_path, len(records), summary, src.data, markup_mode)
    scores = sorted(r["ocr_score"] for r in records)
    body = [r for r in records if not r["apparatus"]]
    summary.update({
        "file": entry.filename,
        "worlds": entry.worlds,
        "row_count": len(entry.row_ids),
        "authors": entry.authors,
        "passages": len(records),
        "passages_non_apparatus": len(body),
        "words": sum(r["word_count"] for r in records),
        "words_non_apparatus": sum(r["word_count"] for r in body),
        "output_sha256": h.hexdigest(),
        "output_path": str(out_path.relative_to(_OUT.parent)) if _OUT.parent in out_path.parents else str(out_path),
        "checks": check,
        "ocr_scores": scores,
        "speaker_words": {k: sum(r["word_count"] for r in records if r["speaker"]["state"] == k)
                          for k in ("known", "mixed", "unknown")},
        "script_words": dict(Counter({s: sum(r["word_count"] for r in records if r["script"] == s)
                                      for s in {r["script"] for r in records}})),
        "language_words": dict(Counter({s: sum(r["word_count"] for r in records if r["language"] == s)
                                        for s in {r["language"] for r in records}})),
        "passage_words": [r["word_count"] for r in records],
        "seconds": round(time.time() - t0, 2),
    })
    return summary


def git_hash() -> str:
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "Sandbox/answering-library/answering_library"],
                               cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
        return head + ("+uncommitted" if dirty else "")
    except OSError:
        return "unknown"


def parameters() -> dict:
    return {
        "passage_words": [passages.MIN_WORDS, passages.MAX_WORDS],
        "oversize_division_words": plain.OVERSIZE_WORDS,
        "subsplit_division_words": plain.SUBSPLIT_WORDS,
        "tiny_division_words": plain.TINY_WORDS,
        "clean": {"min_divisions": segment.CLEAN_MIN_DIVISIONS, "max_oversize_share": segment.CLEAN_MAX_OVERSIZE,
                  "min_cover": segment.CLEAN_MIN_COVER, "min_sequentiality": segment.CLEAN_MIN_SEQUENTIALITY},
        "curated": {"min_cover": curation.CURATED_MIN_COVER, "max_division_words": curation.CURATED_MAX_DIVISION_WORDS},
        "ocr": {"w_unknown": ocr.W_UNKNOWN, "w_symbol": ocr.W_SYMBOL, "w_short": ocr.W_SHORT,
                "w_mixed": ocr.W_MIXED, "w_hyphen": ocr.W_HYPHEN, "known_min_count": ocr.KNOWN_MIN_COUNT,
                "known_min_files": ocr.KNOWN_MIN_FILES},
    }


def main(argv=None) -> int:
    global _VOCAB, _OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--workers", type=int, default=max(1, mp.cpu_count()))
    ap.add_argument("--only", nargs="*")
    args = ap.parse_args(argv)

    started = time.time()
    entries = build_union()
    stems = [Path(e.filename).stem for e in entries]
    assert len(stems) == len(set(stems)), "file stems must be unique"
    try:
        curations = curation.load_all([e.filename for e in entries])
    except curation.CurationError as exc:
        print(f"curation error: {exc}")
        return 2
    if args.only:
        entries = [e for e in entries if e.filename in set(args.only)]
    _OUT = args.out
    (args.out / "passages").mkdir(parents=True, exist_ok=True)

    ctx = mp.get_context("fork")
    vocab = ocr.Vocabulary()
    t_vocab = time.time()
    with ctx.Pool(args.workers) as pool:
        for _, per_lang in pool.imap_unordered(vocab_task, entries, chunksize=1):
            for lang, counts in per_lang.items():
                vocab.add(lang, counts)
    vocab.freeze()
    vocab_seconds = time.time() - t_vocab
    _VOCAB = vocab

    t_seg = time.time()
    summaries = []
    with ctx.Pool(args.workers) as pool:
        for s in pool.imap_unordered(segment_task, entries, chunksize=1):
            summaries.append(s)
    seg_seconds = time.time() - t_seg
    summaries.sort(key=lambda s: s["file"])
    for s in summaries:
        s["ocr_score_quantiles"] = _quantiles(s.pop("ocr_scores"))
    manifest = {
        "code_git_hash": git_hash(),
        "parameters": parameters(),
        "files": len(summaries),
        "curation_files": len(curations),
        "curations_sha256": curation.digest(curations),
        "passages": sum(s["passages"] for s in summaries),
        "words": sum(s["words"] for s in summaries),
        "vocabulary_seconds": round(vocab_seconds, 1),
        "segmentation_seconds": round(seg_seconds, 1),
        "elapsed_seconds": round(time.time() - started, 1),
        "workers": args.workers,
        "per_file": [{k: v for k, v in s.items() if k != "passage_words"} for s in summaries],
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (args.out / "passage_words.json").write_text(
        json.dumps({s["file"]: s["passage_words"] for s in summaries}, separators=(",", ":")), encoding="utf-8")
    print(f"{manifest['files']} files, {manifest['passages']} passages, {manifest['words']} words, "
          f"{manifest['elapsed_seconds']} s")
    return 0


def _quantiles(values: list[float]) -> dict:
    if not values:
        return {}
    return {q: values[min(len(values) - 1, int(p * (len(values) - 1)))]
            for q, p in (("min", 0), ("p05", 0.05), ("p25", 0.25), ("p50", 0.5), ("p75", 0.75), ("max", 1))}


if __name__ == "__main__":
    raise SystemExit(main())
