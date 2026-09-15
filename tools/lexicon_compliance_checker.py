"""
Article 17 confidence-vocabulary compliance checker for deployed lexicon chunks.

Constitution Article 17 requires "a calibrated, visible level of evidential
confidence drawn from a single fixed vocabulary." The Construction Framework
(V7.3) fixes that vocabulary at exactly five terms: Documented, Widely
Accepted, Dominant Modern Reconstruction, Contested, Inferential/Thin.

This script checks for those five terms as capitalized, exact-phrase matches
in each world's Lexicon-Chunks/ directory, and prints the actual matched
snippet so a human can judge whether it's a real label or a false positive
(e.g. "documented tension" is not a confidence rating) rather than trusting a
bare percentage. It also flags Author-Gravity / mediation-risk / Distortion
Risk language separately, since that's a related but distinct requirement.

Usage: py lexicon_compliance_checker.py <worlds/SomeWorld/Lexicon-Chunks>
"""

import re
import sys
from pathlib import Path

CONFIDENCE_TERMS = [
    "Documented",
    "Widely Accepted",
    "Dominant Modern Reconstruction",
    "Contested",
    "Inferential/Thin",
]

GRAVITY_PATTERNS = [
    r"Author[- ]Gravity",
    r"Distortion Risk",
    r"mediation.risk",
]


def find_snippets(text, term, window=25):
    hits = []
    for m in re.finditer(re.escape(term), text):
        start = max(0, m.start() - window)
        end = min(len(text), m.end() + window)
        snippet = text[start:end].replace("\n", " ")
        hits.append(snippet)
    return hits


def check_file(path):
    text = path.read_text(encoding="utf-8")
    confidence_hits = {}
    for term in CONFIDENCE_TERMS:
        hits = find_snippets(text, term)
        if hits:
            confidence_hits[term] = hits
    gravity_hits = []
    for pat in GRAVITY_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            start = max(0, m.start() - 20)
            end = min(len(text), m.end() + 40)
            gravity_hits.append(text[start:end].replace("\n", " "))
    return confidence_hits, gravity_hits


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    d = Path(sys.argv[1])
    files = sorted(d.glob("*.md"))
    if not files:
        print(f"No .md files found in {d}")
        sys.exit(1)

    n_confidence_compliant = 0
    n_gravity_present = 0
    print(f"{'FILE':45} {'CONFIDENCE TERM(S)':45} {'GRAVITY/RISK':10}")
    print("-" * 105)
    for f in files:
        confidence_hits, gravity_hits = check_file(f)
        term_str = ", ".join(confidence_hits.keys()) if confidence_hits else "-- NONE --"
        gravity_str = f"{len(gravity_hits)} hit(s)" if gravity_hits else "-- NONE --"
        print(f"{f.name:45} {term_str:45} {gravity_str:10}")
        if confidence_hits:
            n_confidence_compliant += 1
            for term, snippets in confidence_hits.items():
                for s in snippets[:2]:
                    print(f"      -> [{term}] ...{s}...")
        if gravity_hits:
            n_gravity_present += 1

    print("-" * 105)
    print(f"Confidence-vocabulary compliance: {n_confidence_compliant}/{len(files)}")
    print(f"Author-Gravity/Distortion-Risk language present: {n_gravity_present}/{len(files)}")
    print()
    print("NOTE: a hit above is a literal string match, not a judgment call. Read the")
    print("snippet - a single-word term like 'Documented' or 'Contested' used as an")
    print("ordinary adjective (e.g. 'documented tension', 'contested ground') is a")
    print("false positive, not real Article 17 compliance. This script surfaces")
    print("candidates for a human to confirm; it does not replace that judgment.")


if __name__ == "__main__":
    main()
