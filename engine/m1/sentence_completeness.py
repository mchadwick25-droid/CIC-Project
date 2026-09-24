"""Does every sentence of a quote record's `modern_rendering` stand as a
whole sentence - a main clause with its own subject and its own finite
verb? The process doc's fragment rule (`reference/method/
CiC_Record_Native_World_Build_Process_V1.5.md`, Phase B, V1.6): a rendering
may be split into shorter sentences only where each resulting sentence has
its own subject and verb and carries one whole thought of the original - a
fragment is never an acceptable rendering, whatever the grader or the FK
score says.

`rendering_fidelity.py`'s grader cannot see this: it grades meaning, not
grammar, and passed every fragment the R43 human read later caught (P3
Decision-Log Entries 20, 25 and 26 - e.g. "Of his Deity, by his miracles
during the three years after his baptism."). This module checks grammar
only, never meaning.

REPORT-ONLY. Not registered in gates.GATES, and never fails a run. Mark's
R39, in his own words: "our goal is to generate the right conversation,
not correct it. it fine to have checks, but idealiy they are not used
because the engine is generating it correctly." A rendering this check
flags is read by a person against the fragment rule; the parser's verdict
is never the ruling on its own.

WHAT IS FLAGGED - per sentence, judged on the sentence's MAIN clause (its
parse root), never on whether some verb appears anywhere in it: a verb
inside a relative clause ("...those objections which might be made...")
does not make the sentence around it whole.
  - `no_finite_verb`: the main clause has no finite verb - its root is not
    a verb at all ("Of his Deity, ..."; "In the third, to penance."), or
    is a participle or infinitive with no finite auxiliary.
  - `no_subject`: the main clause has a finite verb but no subject, and is
    not an imperative. An imperative ("Love your enemies.", "Do not
    reason with yourself this way.") is a whole sentence with an
    understood subject, and a subjunctive ("To you be the glory
    forever.") has its own subject; neither is ever flagged.

PARSERS: two spaCy English dependency parsers, `en_core_web_lg` and
`en_core_web_sm`, versions pinned in
`engine/m1/requirements-sentence-completeness.txt`. That file is separate
from `engine/m1/requirements.txt` on purpose: the m1 test suite runs
hermetically in CI with no network model fetch (see `engine/m1/fk.py` and
the ci.yml comment on the m1 test step), so
`engine/m1/tests/test_sentence_completeness.py` exercises the
classification rules against hand-built parse trees, and the real parsers
are exercised by this CLI's own calibration step instead - every run first
checks them against KNOWN_CASES (the real R43 fragments, their accepted
fixes, and whole-sentence shapes) and refuses to report if any case
misclassifies.

A statistical parser misreads some whole sentences (a verb tagged as a
noun, an inverted question), so a sentence is flagged only when NO reading
finds a whole main clause: each parser, on the sentence as written and on
the sentence without an opening connective ("For", "And", "But", ...) or
a dialogue label ("Question:", "Answer:"), which the parser can otherwise
take as the head of the clause. One parse correction, found on KNOWN_CASES:
the parser sometimes labels a modal as the subject ("might" in the
relative-clause case above). A modal is never a subject, so a modal child
is always read as a finite auxiliary. Measured precision on main at the
time of writing is in the P3 Fidelity-Gate Decision-Log.md
(sentence-completeness entry, 2026-09-24); the parser's call is never the
ruling on its own.

Usage: `python -m engine.m1.sentence_completeness` - writes
`engine/m1/reports/sentence-completeness-report-<date>.json` and prints a
per-world summary.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

from engine.m1.loader import load_world_records

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = Path(__file__).resolve().parent / "reports"

SPACY_MODELS = ("en_core_web_lg", "en_core_web_sm")

FINITE_TAGS = frozenset({"VBD", "VBP", "VBZ", "MD"})
SUBJECT_DEPS = frozenset({"nsubj", "nsubjpass", "expl", "csubj", "csubjpass"})
AUX_DEPS = frozenset({"aux", "auxpass"})

NO_FINITE_VERB = "no_finite_verb"
NO_SUBJECT = "no_subject"

# A sentence ends at . ! ? (or a run of them, e.g. an ellipsis), with any
# closing quotes or brackets (up to two) kept with it, when the next sentence opens
# with a capital letter or an opening quote.
_CLOSE = "[\"'\u201d\u2019)\\]]"
_SENTENCE_BREAK = re.compile(
    rf"(?:(?<=[.!?])|(?<=[.!?]{_CLOSE})|(?<=[.!?]{_CLOSE}{_CLOSE}))\s+(?=[\"'\u201c\u2018(\[]?[A-Z])"
)

# The real R43 fragments the human read caught (P3 Decision-Log Entries 20,
# 25, 26), each with the accepted fix, plus whole-sentence shapes the check
# must never flag. The CLI's calibration step runs these through the real
# parser before every report.
KNOWN_CASES: tuple[tuple[str, str | None], ...] = (
    ("Of his Deity, by his miracles during the three years after his baptism.", NO_FINITE_VERB),
    ("Of his humanity, during the thirty similar years before his baptism.", NO_FINITE_VERB),
    ("In the third, to penance.", NO_FINITE_VERB),
    ("In the fourth, to standing...", NO_FINITE_VERB),
    (
        "Not for argument's sake, but to learn the answers to those objections "
        "which might, as she saw, be made to my statements.",
        NO_SUBJECT,
    ),
    ("He showed his Deity by his miracles during the three years after his baptism.", None),
    ("He showed his humanity in the thirty similar years before his baptism.", None),
    ("Love your enemies.", None),
    ("Always let the bridegroom delight with you.", None),
    ("Time will fail me if I attempt to recount the rest.", None),
    ("He has gone to the Lord.", None),
    ("There is one God.", None),
    ("To you be the glory forever.", None),
    ("Do not reason with yourself this way.", None),
    ("For the heart is a deep gulf.", None),
    ("For us and for our salvation, he came down from heaven.", None),
    ("Question: Should a woman who has just given birth keep the Paschal fast?", None),
    ("Answer: No.", NO_FINITE_VERB),
    ("Praise to God.", NO_FINITE_VERB),
)


def split_sentences(text: str) -> list[str]:
    text = " ".join((text or "").split())
    if not text:
        return []
    return [s for s in _SENTENCE_BREAK.split(text) if s.strip()]


def classify_root(root) -> str | None:
    """The fragment category for one sentence's parse root, or None if the
    main clause is whole. `root` needs only spaCy's Token surface this
    reads: `.tag_`, `.dep_`, `.lower_`, `.children`."""
    children = list(root.children)
    modal_children = [c for c in children if c.tag_ == "MD"]
    finite_aux = [c for c in children if c.dep_ in AUX_DEPS and c.tag_ in FINITE_TAGS]
    finite = root.tag_ in FINITE_TAGS or bool(finite_aux) or bool(modal_children)
    subjects = [c for c in children if c.dep_ in SUBJECT_DEPS and c.tag_ != "MD"]
    infinitive = any(c.dep_ in AUX_DEPS and c.tag_ == "TO" for c in children)

    if root.tag_ == "VB" and not infinitive:
        if subjects and not finite:
            return None  # subjunctive: "To you be the glory", "Thy kingdom come"
        do_support = [c for c in finite_aux if c.lower_ == "do"]
        if not subjects and (not finite or do_support):
            return None  # imperative, incl. "Do not say...": an understood subject
    if not finite:
        return NO_FINITE_VERB
    if not subjects:
        return NO_SUBJECT
    return None


# Words that head a sentence without being part of its main clause's
# grammar: a dialogue label, or an opening connective.
_SPEAKER_LABEL = re.compile(r"^(?:Question|Answer)\s*:\s*")
_LEADING_CONNECTIVE = re.compile(r"^(?:For|And|But|So|Or|Yet|Now|Then|Still|Therefore|Thus)\b,?\s+(?=\S)")


def readings(sentence: str) -> list[str]:
    unlabeled = _SPEAKER_LABEL.sub("", sentence)
    out = [sentence, unlabeled, _LEADING_CONNECTIVE.sub("", unlabeled)]
    return list(dict.fromkeys(out))


def classify_doc(doc) -> str | None:
    roots = [t for t in doc if t.dep_ == "ROOT"]
    if not roots:
        return NO_FINITE_VERB
    # The parser can read a single written sentence as more than one; the
    # written sentence is whole if any main clause the parser found is.
    categories = [classify_root(r) for r in roots]
    if any(c is None for c in categories):
        return None
    return categories[0]


def classify_sentence(parsers, sentence: str) -> str | None:
    """None if any parser finds a whole main clause in any reading of the
    sentence; otherwise the first parser's category on the sentence as
    written."""
    first = None
    for reading in readings(sentence):
        for parse in parsers:
            category = classify_doc(parse(reading))
            if category is None:
                return None
            first = first or category
    return first


def check_rendering(parsers, rendering: str) -> list[dict]:
    flagged = []
    for sentence in split_sentences(rendering):
        category = classify_sentence(parsers, sentence)
        if category is not None:
            flagged.append({"sentence": sentence, "category": category})
    return flagged


def calibrate(parsers) -> list[str]:
    failures = []
    for sentence, expected in KNOWN_CASES:
        got = classify_sentence(parsers, sentence)
        if got != expected:
            failures.append(f"{sentence!r}: expected {expected}, got {got}")
    return failures


def sweep_world(world_key: str, parsers, load=load_world_records) -> dict:
    records = load(world_key)
    quotes = {rid: r for rid, r in records.items() if r.get("record_type") == "quote"}
    findings = []
    checked = 0
    sentences = 0
    for rid, rec in sorted(quotes.items()):
        rendering = rec.get("modern_rendering")
        if not rendering:
            continue
        checked += 1
        sentences += len(split_sentences(rendering))
        flagged = check_rendering(parsers, rendering)
        if flagged:
            findings.append({"id": rid, "flagged_sentences": flagged})
    category_counts = {NO_FINITE_VERB: 0, NO_SUBJECT: 0}
    for f in findings:
        for s in f["flagged_sentences"]:
            category_counts[s["category"]] += 1
    return {
        "world": world_key,
        "total_quotes": len(quotes),
        "renderings_checked": checked,
        "sentences_checked": sentences,
        "renderings_flagged": len(findings),
        "sentences_flagged": sum(category_counts.values()),
        "category_counts": category_counts,
        "findings": findings,
    }


def fleet_report(parsers, worlds) -> dict:
    per_world = {w: sweep_world(w, parsers) for w in worlds}
    keys = ("total_quotes", "renderings_checked", "sentences_checked", "renderings_flagged", "sentences_flagged")
    totals = {k: sum(w[k] for w in per_world.values()) for k in keys}
    totals["category_counts"] = {
        c: sum(w["category_counts"][c] for w in per_world.values()) for c in (NO_FINITE_VERB, NO_SUBJECT)
    }
    return {"parsers": list(SPACY_MODELS), "worlds": per_world, "totals": totals}


def load_parsers():
    try:
        import spacy
    except ImportError:
        sys.exit("spaCy is not installed: pip install -r engine/m1/requirements-sentence-completeness.txt")
    return [spacy.load(m) for m in SPACY_MODELS]


def main(argv: list[str] | None = None) -> int:
    from engine.m1.quote_verbatim import REPORT_WORLDS

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=REPORTS_DIR / f"sentence-completeness-report-{date.today().isoformat()}.json")
    args = parser.parse_args(argv)

    parsers = load_parsers()
    failures = calibrate(parsers)
    if failures:
        print("calibration failed - the parser misreads a known case; no report written:")
        for f in failures:
            print(f"  {f}")
        return 1

    report = fleet_report(parsers, REPORT_WORLDS)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    t = report["totals"]
    print(
        f"sentence-completeness sweep: {t['renderings_flagged']}/{t['renderings_checked']} renderings flagged, "
        f"{t['sentences_flagged']}/{t['sentences_checked']} sentences, categories={t['category_counts']}"
    )
    for w in report["worlds"].values():
        print(
            f"  {w['world']:12} renderings={w['renderings_checked']:4} flagged={w['renderings_flagged']:3} "
            f"sentences_flagged={w['sentences_flagged']:3} {w['category_counts']}"
        )
    print(f"\nfull report written to {args.out}")
    return 0  # report-only: never fails the run on findings


if __name__ == "__main__":
    sys.exit(main())
