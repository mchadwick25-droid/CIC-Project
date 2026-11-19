"""P2-V: re-verify every evidence quote verbatim, by two independent methods.

1. against the page the researcher saved when the quote was taken;
2. against a fresh fetch of the same URL, made by this script.

Usage: python3 check_quotes.py <results dir> <out.json>
Each results file is result_batch_N.json, with its saved pages under pages/ beside it.
A quote passes only when it is found in the saved page and in the fresh fetch, after
markup is stripped, entities decoded and whitespace and typographic quotes normalized.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path


def text_of(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return norm(html.unescape(raw))


def norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip().lower()


def fetch(url: str) -> str:
    try:
        r = subprocess.run(["curl", "-sSL", "--max-time", "40", "-A", "Mozilla/5.0", url],
                           capture_output=True, timeout=60)
        return r.stdout.decode("utf-8", "replace")
    except Exception:
        return ""


def pdf_text(path: Path) -> str:
    try:
        r = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, timeout=60)
        return norm(r.stdout.decode("utf-8", "replace"))
    except Exception:
        return ""


def main(results_dir: str, out_path: str) -> None:
    rows = []
    for f in sorted(Path(results_dir).glob("*/result_batch_*.json")):
        for entry in json.loads(f.read_text()):
            for i, ev in enumerate(entry.get("evidence") or []):
                if not ev.get("quote"):
                    rows.append({"id": entry["id"], "item": i, "url": ev.get("url"), "saved": None, "fresh": None,
                                 "verified_claim": ev.get("verified"), "note": "no quote"})
                    continue
                q = norm(ev["quote"])
                page = f.parent / ev["page"] if ev.get("page") else None
                saved = None
                if page and page.exists():
                    raw = page.read_bytes()
                    t = pdf_text(page) if raw[:4] == b"%PDF" else text_of(raw.decode("utf-8", "replace"))
                    saved = q in t
                fresh_raw = fetch(ev["url"]) if ev.get("url") else ""
                fresh = None
                if fresh_raw:
                    if fresh_raw.startswith("%PDF"):
                        tmp = Path(out_path).with_suffix(".tmp.pdf")
                        subprocess.run(["curl", "-sSL", "--max-time", "40", "-o", str(tmp), ev["url"]])
                        fresh = q in pdf_text(tmp)
                        tmp.unlink(missing_ok=True)
                    else:
                        fresh = q in text_of(fresh_raw)
                rows.append({"id": entry["id"], "item": i, "url": ev.get("url"), "saved": saved, "fresh": fresh,
                             "verified_claim": ev.get("verified"), "quote": ev["quote"]})
    Path(out_path).write_text(json.dumps(rows, indent=1) + "\n")
    both = sum(1 for r in rows if r["saved"] and r["fresh"])
    print(f"quotes {sum(1 for r in rows if r.get('quote'))}; found by both methods {both}")
    for r in rows:
        if r.get("quote") and not (r["saved"] and r["fresh"]):
            print(f"  {r['id']} item {r['item']}: saved={r['saved']} fresh={r['fresh']} {r['url']}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
