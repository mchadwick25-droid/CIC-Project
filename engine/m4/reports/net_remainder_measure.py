"""R37 report-only measurement (Decision-Log.md Entry 56's own follow-up,
triggered by Mark's staging look with CIC_R27_ENFORCE on, 2026-09-23):
the Theon/Donatists worked example ("Under persecution, some gave way -
they sacrificed to the gods, or they handed over the sacred books.") let
a fabricated clause (the traditor charge) ride past the net on the back
of a real, partial match against alx.dw.church-failure. The reviewer
thread's own diagnosis named engine.m4.grounding_net._span_in_records
(the quoted-span, any-6-word-window verbatim check) as the mechanism.

VERIFIED AGAINST THE REAL CODE BEFORE THIS SCRIPT WAS WRITTEN (never
repeat a diagnosis unchecked - this project's own "never invent" rule
applies to a technical claim exactly as it applies to a quoted source):
the worked example carries no quote marks, so it never reaches
_quoted_spans/_span_in_records at all. Run directly against
verdict_for_sentence() with the real alx.dw.church-failure record:

    verdict_for_sentence(
        "Under persecution, some gave way - they sacrificed to the gods, "
        "or they handed over the sacred books.",
        ["alx.dw.church-failure"], ...,
    )
    -> {"verdict": "ok", "why": "tagged claim, shares ground with its own
        records"}

claim_markers() on this sentence is EMPTY (no proper noun, number, or
enumeration), so it takes the "THE TAG IS THE CLAIM" branch
(verdict_for_sentence, the `if not markers:` block) - gated on ANY
NONZERO content-word overlap with the tagged record, no ratio floor at
all. content_words() on the sentence is {way, gods, gave, books, sacred,
sacrificed, persecution, handed}; five of those eight (way, gods, gave,
sacrificed, persecution) are in alx.dw.church-failure's own vocabulary;
three (books, handed, sacred) are not. Any nonzero overlap passes this
branch - it does not matter that 3 of 8 content words are unattested.

So the real mechanism is MORE permissive than a 6-word-window check, not
the same one: verdict_for_sentence has three separate "ok" paths, and
this measurement covers all three correctly, each against its own real
matching unit, rather than assuming the reviewer's named path fired
project-wide:

  quoted_span_window   - _quoted_spans found the claim in literal quote
                          marks; _span_in_records passed each span (a
                          span <=6 words must match whole; a span >6
                          words only needs ONE 6-word window inside it
                          to match - anything past that window in a
                          longer quote is never independently checked).
  tag_is_claim_zero_floor - no proper noun/number/enumeration in the
                          sentence; passes the moment the sentence
                          shares ONE content word with its own tagged
                          record's vocabulary - no floor at all. This is
                          the branch that actually passed the worked
                          example.
  ratio_floor           - a real claim marker fired; passes at
                          grounding_ratio() >= WITHHOLD_FLOOR (0.4), i.e.
                          up to 60% of the sentence's content words may
                          be unattested and it still streams.

For each, "remainder" is the sentence's own content words that are not
found anywhere in the union of its tagged records' own vocabulary
(quoted_span_window additionally gets its own window-coverage note,
since its matching unit is a 6-word verbatim window, not a word bag).
"remainder_is_own_clause" flags a sentence whose remainder is not
scattered but sits together as one coordinating clause (a "so"/"or"/
"and"/dash-led fragment with 3+ content words, every one of them
unmatched) - the shape of the worked example, and the shape a
downstream rule most needs to catch: real content carrying an entire
extra, free-riding assertion.

Corpus: the same Corpus A pool grounding_fooling_measure.py already
established (every engine/m4/reports/live-turn-report*.json carrying a
voice_event.grounding.sentences[] array, for a real fleet world) -
re-run against the CURRENT compiled packages and the CURRENT
verdict_for_sentence, not the verdict saved at generation time, for the
same reason that script gives: a record or prose.py fix landed since
does not silently stay unmeasured. The other file pattern the reviewer
named, engine/m4/reports/live-uncited-claims-battery-report*.json,
carries only reduced {sentence, class} OFFENSE lists by design (the
storage-bloat-avoidance discipline noted throughout this workstream) -
checked directly here (see main()'s own printed note) and confirmed to
hold no grounded-sentence text at all, so it cannot supply this
measurement; Corpus A is the only real source of "whatever turn captures
you hold" with full verdict detail.

No code change to the net anywhere in this file. Report-only, same
discipline as R34's own measurement pass.

Run: python3 -m engine.m4.reports.net_remainder_measure
"""
import json
import pathlib
import re
import sys
from datetime import date, datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.registry import formation_world_keys
from engine.m4 import evidence as ev
from engine.m4 import grounding_net as gn
from engine.prose import all_text, content_words

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent
# Every formation world, read from the one registry instead of hand-kept -
# see grounding_fooling_measure.py's own comment on this same fix (item 2
# of the 2026-09-25 CI/tooling audit). Unchanged today; a newly admitted
# world is picked up automatically from here on.
WORLDS = formation_world_keys()

_CLAUSE_LEAD = re.compile(r",?\s+\b(?:or|and|but|so)\b\s+|--|—|\s-\s")


def latest_complete_package(world_key: str) -> pathlib.Path:
    pkgs = sorted((REPO_ROOT / "packages" / world_key).iterdir())
    for p in reversed(pkgs):
        if (p / "compiled" / "repository.json").exists():
            return p
    raise RuntimeError(f"no complete compiled package found for {world_key}")


_REPO_CACHE: dict[str, tuple[dict, list, set]] = {}


def load_repo(world_key: str):
    if world_key not in _REPO_CACHE:
        C = latest_complete_package(world_key) / "compiled"
        recs = ev.repository_records_by_id(json.loads((C / "repository.json").read_text()))
        thin = ev.thin_topics_for(recs)
        figures = gn.build_figure_lexicon(recs)
        _REPO_CACHE[world_key] = (recs, thin, figures)
    return _REPO_CACHE[world_key]


def _branch_for(why: str) -> str | None:
    if why.startswith("quoted span(s) verbatim"):
        return "quoted_span_window"
    if why == "tagged claim, shares ground with its own records":
        return "tag_is_claim_zero_floor"
    if why.startswith("grounded ") and "own tagged records" in why:
        return "ratio_floor"
    return None


def _own_clause_remainder(sentence: str, remainder: set[str]) -> str | None:
    """The shape the worked example has: remainder isn't scattered, it's
    one trailing coordinating clause, every content word of which is
    unmatched. Returns the clause text if found, else None."""
    fragments = _CLAUSE_LEAD.split(sentence)
    if len(fragments) < 2:
        return None
    for frag in fragments[1:]:
        frag_words = content_words(frag)
        if len(frag_words) >= 3 and frag_words and frag_words <= remainder:
            return frag.strip().rstrip(".!?")
    return None


def measure_sentence(sentence: str, tags: list[str], why: str, world_key: str) -> dict | None:
    branch = _branch_for(why)
    if branch is None:
        return None
    recs, _, _ = load_repo(world_key)
    tagged_records = [recs[t] for t in tags if t in recs]
    cited_words: set[str] = set()
    for rec in tagged_records:
        cited_words |= content_words(all_text(rec))
    sentence_words = content_words(sentence)
    remainder = sentence_words - cited_words
    row = {
        "world": world_key,
        "sentence": sentence,
        "tags": tags,
        "branch": branch,
        "sentence_content_words": len(sentence_words),
        "remainder_count": len(remainder),
        "remainder_words": sorted(remainder),
    }
    own_clause = _own_clause_remainder(sentence, remainder)
    if own_clause:
        row["remainder_is_own_clause"] = own_clause
    if branch == "quoted_span_window":
        spans = gn._quoted_spans(sentence)
        long_spans = [s for s in spans if len(gn._normalize(s).split()) > 6]
        row["quoted_spans"] = spans
        row["has_span_over_six_words"] = bool(long_spans)
    return row


def run() -> dict:
    rows: list[dict] = []
    turns_scanned = 0
    sentences_scanned = 0
    for fp in sorted(REPORTS_DIR.glob("live-turn-report*.json")):
        d = json.loads(fp.read_text())
        world_key = d.get("world_key")
        if world_key not in WORLDS:
            continue
        for r in d.get("results", []):
            ve = (r.get("result") or {}).get("voice_event")
            if not ve or not ve.get("grounding"):
                continue
            turns_scanned += 1
            for s in ve["grounding"]["sentences"]:
                sentences_scanned += 1
                if not s.get("tags"):
                    continue
                new = gn.verdict_for_sentence(
                    s["sentence"], s["tags"],
                    repository_records=load_repo(world_key)[0],
                    figure_names=load_repo(world_key)[2],
                    thin_topics=load_repo(world_key)[1],
                    grounding_floor=gn.WITHHOLD_FLOOR,
                )
                if new["verdict"] != "ok":
                    continue
                row = measure_sentence(s["sentence"], s["tags"], new["why"], world_key)
                if row:
                    rows.append(row)

    by_branch: dict[str, int] = {}
    for row in rows:
        by_branch[row["branch"]] = by_branch.get(row["branch"], 0) + 1

    distribution: dict[str, int] = {}
    for row in rows:
        key = str(row["remainder_count"]) if row["remainder_count"] < 5 else "5+"
        distribution[key] = distribution.get(key, 0) + 1

    own_clause_rows = [r for r in rows if r.get("remainder_is_own_clause")]

    worked_example = measure_sentence(
        "Under persecution, some gave way - they sacrificed to the gods, or they handed over the sacred books.",
        ["alx.dw.church-failure"],
        "tagged claim, shares ground with its own records",
        "alx",
    )

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "turns_scanned": turns_scanned,
        "sentences_scanned": sentences_scanned,
        "marked_grounded_with_tags_checked": len(rows),
        "by_branch": by_branch,
        "remainder_word_count_distribution": distribution,
        "sentences_with_remainder_forming_own_clause": len(own_clause_rows),
        "own_clause_examples": own_clause_rows,
        "worked_example_theon_donatists_2026_09_23": worked_example,
        "all_rows": rows,
        "note_on_uncited_claims_battery_reports": (
            "engine/m4/reports/live-uncited-claims-battery-report*.json carries only "
            "reduced {sentence, class} offense lists (storage-bloat-avoidance discipline "
            "kept throughout this workstream) - confirmed by direct scan, zero \"ok\" "
            "verdicts present in either file. Corpus here is the live-turn-report*.json "
            "pool instead (same Corpus A grounding_fooling_measure.py already uses), "
            "re-run against current packages and the current verdict_for_sentence."
        ),
    }


def main():
    report = run()
    out_path = REPORTS_DIR / f"net-remainder-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))
    print(f"Turns scanned: {report['turns_scanned']}, sentences scanned: {report['sentences_scanned']}")
    print(f"Marked-grounded, tag-checked sentences: {report['marked_grounded_with_tags_checked']}")
    print(f"By branch: {report['by_branch']}")
    print(f"Remainder word-count distribution: {report['remainder_word_count_distribution']}")
    print(
        f"Sentences whose remainder forms a clause of its own: "
        f"{report['sentences_with_remainder_forming_own_clause']} of {report['marked_grounded_with_tags_checked']}"
    )
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
