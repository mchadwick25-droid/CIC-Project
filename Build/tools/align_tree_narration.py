"""Paragraph start times for the Church Family Tree's recorded briefs.

The map's "Read the brief" fold lets a visitor tap a paragraph to play the brief from there, and marks
the paragraph being spoken. That needs the second at which each paragraph starts in its recording.
This tool finds them by running a speech-recognition model locally over the existing recordings and
matching the words it hears to the brief's own text. Nothing is re-recorded and no paid service is
called.

A brief gets times only when every paragraph's opening is matched in order. Otherwise it gets none,
and the map shows its text without jumps. Times are stored with the text hash they were made from,
so a brief rewritten or re-recorded later never shows stale times.

Run (faster-whisper must be installed; the model downloads once):
    python Build/tools/align_tree_narration.py            # every multi-paragraph recorded brief
    python Build/tools/align_tree_narration.py --only id1,id2
    python Build/tools/align_tree_narration.py --check    # report entries whose times are stale
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "cft-website" / "index.html"
AUDIO = ROOT / "cft-website" / "audio" / "tree"
MANIFEST = AUDIO / "manifest.json"
TIMES = AUDIO / "paragraph-times.json"
MARKER = "const DATA = "

MODEL = "base.en"
MIN_MATCH_RATIO = 0.85
MAX_LEAD_WORDS = 2
LEAD_IN = 0.15


def load_entries(page: Path = PAGE) -> dict:
    html = page.read_text(encoding="utf-8")
    at = html.index(MARKER) + len(MARKER)
    data, _ = json.JSONDecoder().raw_decode(html, at)
    return {m["id"]: m for m in data["movements"]}


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def norm(word: str) -> str:
    return re.sub(r"[^a-z0-9]", "", word.lower())


def paragraphs(text: str) -> list[str]:
    return text.split("\n\n")


def words_of(text: str) -> list[str]:
    return [w for w in (norm(t) for t in text.split()) if w]


def paragraph_starts(text: str, heard: list[tuple[str, float]]) -> list[float] | None:
    """Seconds at which each paragraph starts, or None when any start can't be placed surely.

    heard is the recognized words in order, each with its start second.
    """
    paras = paragraphs(text)
    if len(paras) < 2:
        return None
    ref, first = [], []
    for p in paras:
        first.append(len(ref))
        ref.extend(words_of(p))
    hyp = [w for w, _ in heard]
    matcher = difflib.SequenceMatcher(a=ref, b=hyp, autojunk=False)
    if matcher.ratio() < MIN_MATCH_RATIO:
        return None
    ref_to_hyp = {}
    for block in matcher.get_matching_blocks():
        for k in range(block.size):
            ref_to_hyp[block.a + k] = block.b + k
    starts = [0.0]
    for p_index in first[1:]:
        hit = next((ref_to_hyp[p_index + j] for j in range(MAX_LEAD_WORDS + 1) if p_index + j in ref_to_hyp), None)
        if hit is None:
            return None
        t = max(0.0, heard[hit][1] - LEAD_IN)
        if t <= starts[-1]:
            return None
        starts.append(round(t, 2))
    return starts


def decode(mp3: Path):
    """The recording as 16 kHz mono samples, decoded by ffmpeg."""
    import subprocess

    import numpy as np

    raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(mp3), "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def transcribe(model, mp3: Path) -> list[tuple[str, float]]:
    segments, _ = model.transcribe(decode(mp3), language="en", word_timestamps=True, beam_size=5, vad_filter=False)
    out = []
    for seg in segments:
        for w in seg.words or []:
            n = norm(w.word)
            if n:
                out.append((n, float(w.start)))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--only", help="comma-separated entry ids")
    ap.add_argument("--check", action="store_true", help="list stored times whose text has changed")
    args = ap.parse_args(argv)

    entries = load_entries()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    store = json.loads(TIMES.read_text(encoding="utf-8")) if TIMES.exists() else {}

    if args.check:
        stale = [i for i, v in store.items() if i not in entries or text_hash(entries[i].get("longDescription", "")) != v["text_sha256"]]
        print("\n".join(stale) if stale else "no stale paragraph times")
        return 1 if stale else 0

    ids = [i for i, rec in manifest.items()
           if i in entries and entries[i].get("longDescription")
           and len(paragraphs(entries[i]["longDescription"])) > 1
           and rec.get("text_sha256") == text_hash(entries[i]["longDescription"])]
    if args.only:
        wanted = set(args.only.split(","))
        ids = [i for i in ids if i in wanted]

    from faster_whisper import WhisperModel  # imported here so --check runs without it

    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    placed = skipped = 0
    for n, i in enumerate(ids, 1):
        text = entries[i]["longDescription"]
        starts = paragraph_starts(text, transcribe(model, AUDIO / manifest[i]["file"]))
        if starts:
            store[i] = {"text_sha256": text_hash(text), "starts": starts}
            placed += 1
        else:
            store.pop(i, None)
            skipped += 1
        print(f"[{n}/{len(ids)}] {i}: {'placed' if starts else 'no sure match'}", flush=True)
        TIMES.write_text(json.dumps(dict(sorted(store.items())), indent=1) + "\n", encoding="utf-8")
    print(f"model {MODEL}: {placed} briefs placed, {skipped} left without times")
    return 0


if __name__ == "__main__":
    sys.exit(main())
