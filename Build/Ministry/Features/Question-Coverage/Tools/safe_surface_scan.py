"""Scan the surfaces that reach a visitor or the voice for method-of-death and
traitor words, in records that may fire on a suicide or bereavement question.

Read-only. No model calls. For each record it checks the spoken fields, the
use-note lines sent to the voice, each source's locus as the engine's
display_locus filter shows it on the citation card, and the divergence note.
With --prompt it also scans a compiled prompt file whole.

  python Build/Ministry/Features/Question-Coverage/Tools/safe_surface_scan.py \
      [--prompt packages/<world>/<id>/compiled/prompt.txt] [record.md ...]

Exit status 1 if any hit is found.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO))
from engine.prose import display_locus  # noqa: E402

DEFAULT = [
    "records/don/honest_limit/don.limit.fate-of-those-who-end-their-own-lives.md",
    "records/alx/honest_limit/alx.limit.faith-alone-later-frame.md",
    "records/pahc/honest_limit/pahc.limit.assurance-and-the-dead.md",
    "records/don/contested_claim/don.contested.augustine-precipice-charge.md",
]
WORDS = re.compile(
    r"\b(cliffs?|precipices?|precipitat\w*|jump\w*|hang\w*|hung|rope|noose|"
    r"thr(?:ow|ew|own)\w*|headlong|summits?|strangl\w*|drown\w*|Judas|traitors?)\b",
    re.I,
)
SPOKEN = ("statement", "claim", "held_against", "concedes")


def flat(v):
    return " ".join(map(str, v)) if isinstance(v, list) else str(v)


def surfaces(path):
    d = yaml.safe_load((REPO / path).read_text().split("---")[1])
    for k in SPOKEN:
        if k in d:
            yield f"{d['id']} {k}", flat(d[k])
    un = d.get("use_note") or {}
    yield f"{d['id']} use_note.means", flat(un.get("means", ""))
    for i, line in enumerate(un.get("not_for") or [], 1):
        yield f"{d['id']} use_note.not_for[{i}]", flat(line)
    for s in d.get("sources") or []:
        yield f"{d['id']} card locus ({s['source_id']})", display_locus(s.get("locus") or "")
    dn = (d.get("confidence") or {}).get("divergence_note")
    if dn:
        yield f"{d['id']} confidence.divergence_note", flat(dn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("records", nargs="*")
    ap.add_argument("--prompt")
    a = ap.parse_args()
    hits = 0
    for rec in a.records or DEFAULT:
        for name, text in surfaces(rec):
            for m in WORDS.finditer(text):
                hits += 1
                s = max(0, m.start() - 50)
                print(f"HIT  {name}: ...{text[s:m.end() + 50]!r}")
    if a.prompt:
        text = (REPO / a.prompt).read_text()
        for m in WORDS.finditer(text):
            hits += 1
            line = text.count("\n", 0, m.start()) + 1
            s = max(0, m.start() - 60)
            print(f"HIT  {a.prompt} line {line}: ...{text[s:m.end() + 60]!r}".replace("\\n", " "))
    print(f"{hits} hit(s)")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
