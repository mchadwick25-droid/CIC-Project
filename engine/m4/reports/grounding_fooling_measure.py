"""Build-Plan.md STAGE 1 - D1 grounding measurement (Adjusted-Design.md
Section 4, "The D1 measurement - methodology"). Read-only: measures how
often engine.m4.grounding_net.verdict_for_sentence (check_turn()'s own
per-sentence logic, factored out for exactly this stage - see that
function's own docstring) can be fooled by a plausible fabricated claim,
and how often it withholds honest prose. Deterministic, mostly zero model
calls - the one deliberate exception is documented below. Never changes
WITHHOLD_FLOOR, check_turn, or any threshold; this stage only measures the
mechanism as it already exists.

Three corpora, per the design doc:

CORPUS A - real logged turns. Every engine/m4/reports/live-turn-report*.json
file that carries a voice_event.grounding.sentences[] array (a turn that
actually reached voice generation, not one that safety-routed away) is the
pool. Each saved (sentence, tags) pair is re-run through
verdict_for_sentence() against the CURRENT compiled package for that
world - not the verdict saved at generation time - so a record or prose.py
fix landing since the report was generated shows up as a reproduction
delta, exactly as the design doc asks ("verdicts should reproduce, shifting
slightly for guard-bearing records post-prose.py fix"). The design doc
cites "36 turns / 546 sentences / 55 withheld" from when it was written;
the real, current pool measured here is smaller - a small, believable
drift (one report regenerated, one outcome changed), not force-fit to
match: see the printed count vs. cited count below.

Package note: several worlds' newest packages/ timestamp on disk in this
sandbox carries only manifest.json, not a full compiled/ directory (a
pre-existing, already-documented gap - Build-Plan.md Stage 0c's own
finding). latest_complete_package() walks backward past any such
incomplete timestamp rather than assuming pkgs[-1] is usable, the same
problem retrieval_bench.py's own pkgs[-1] would hit unmodified.

CORPUS B - constructed fabrications (deterministic). For every
contested_claim.claim (68 fleet-wide) - itself already phrased as a flat,
uncontested-sounding over-claim - the flat assertion is the field verbatim,
tagged to its own record: zero transformation, zero risk of the
construction itself corrupting the measurement.

For the guard lines: each record's claim_guards entries - R11's
honesty-guard half of the old do_not_retrieve_when field, which also
carried 701 ordinary retrieval-scoping redirects that were never a barred
proposition at all (keyword-matched apart by engine.prose.GUARD_MARKERS:
"does not say", "must not supply", "not attested", "do not invent",
"must not"). The fleet's 13 guard lines are hand-authored below into flat
assertions of the specific barred proposition each one names - small
enough (13) to read and phrase correctly by hand rather than risk a regex
mis-extracting a barred proposition from free prose. Brictio
(gallic.story.brictio-in-the-courtyard) is row one, per the design doc.

For honest_limit.statement (50) and story absent_detail (120): both fields
are free-form, multi-sentence, often rhetorical first-person prose, not
clean propositions - a mechanical regex negation-flip risked producing
grammatically broken or semantically confused test sentences, which would
corrupt this measurement with construction artifacts rather than real
signal about the checker. Per the design doc's own explicit allowance
("template first; optional one-time Sonnet phrasing"), these 170 flat
assertions were authored in a one-time pass (a background agent working
from the same raw record data, spot-checked before use here) rather than
templated - no live/billed model call, the same zero-additional-cost
authoring this document's own text already requires. See
corpus_b_flat_assertions.json alongside this file.

CORPUS C - the one-shared-word hole. For every world, every sentence drawn
from a record's own text (claim_markers() == [] - no proper noun, no
number, no repeated-phrase marker, so the ONLY thing that could ground it
is a tag) is paired against every OTHER record in the same world; a pair
qualifies if they share EXACTLY ONE content word and the sentence's own
words include no figure name. The sentence is then tagged to the WRONG
record (never its true source) and run through verdict_for_sentence() -
measuring how often the "tag is the claim" branch (zero-shared-content-word
is its one hard line, per that function's own docstring) still says "ok"
on a single incidental word in common.

Deliverable: engine/m4/reports/grounding-fooling-<date>.json + this
docstring's own structural statement, unchanged from the design doc:
provenance, not truth; mitigations are upstream (riders, guards,
honest-limit records) and reporting; any UI element implying per-sentence
truth verification overclaims. No thresholds self-set here; numbers go to
Mark as an Artifact.

PER-WORLD GUARD COVERAGE (--world <code>). Corpus B for one world, built
or not yet admitted, run after the world's contested-claim records exist:
a report-only list of barred claims that pass the grounding check and
that no claim_guards entry covers, for a person to decide which ones get
a guard (each guard renders as a MUST NOT ASSERT rider inside the
record's evidence budget_chars, so guarding everything crowds out
evidence). Differences from the fleet run:

- The repository is compiled in memory from the world's CURRENT records/
  (engine.m2.builders.build_repository_json, the same builder a package
  uses) - no package, registry entry or admission needed, and records
  authored since the last package build are measured, not missed.
- Rows are built by walking the world's records, so every contested_claim,
  honest_limit, story absent_detail and claim_guards entry is accounted
  for. A contested_claim.claim is used verbatim. The other three need a
  phrased flat assertion; one comes from, in order: the world's own
  worlds/<code>/build/corpus-b-flat-assertions.json (same shape as
  corpus_b_flat_assertions.json, plus "guard": {id: [one assertion per
  claim_guards entry, in order]}), then the fleet's
  corpus_b_flat_assertions.json and GUARD_FLAT_ASSERTIONS. A field with
  no phrased assertion is never skipped silently: it is listed under
  "unphrased" with its own source text, and the run is incomplete until
  that list is empty.
- This script never calls a model. Phrasing is template first, as the
  design doc asks; where a template would produce a broken sentence (the
  regex negation-flip problem above), the assertion comes from a one-time,
  build-time phrasing pass (a person, or a single Sonnet pass whose output
  a person spot-checks) written into that world's file. Nothing on the
  runtime turn path reads that file or this output.

"Covers" means exactly what the runtime would enforce: an assertion is
covered when engine.m4.output_check's guard_proximity family fires on it
cited to its own record - that record carries a claim_guards entry whose
barred proposition (_guard_proposition: guard markers, boilerplate and
proper nouns stripped) shares at least _GUARD_PROXIMITY_MIN_SHARED_WORDS
content words with the assertion. A guard on a different record never
counts. "needs_decision" lists every row whose verdict is "ok" and that
is not covered.

Output: worlds/<code>/build/guard-coverage-<date>.json - the world's own
build output. Measurement only: WITHHOLD_FLOOR, check_turn,
verdict_for_sentence and every threshold are unchanged.

Run: python3 -m engine.m4.reports.grounding_fooling_measure
     python3 -m engine.m4.reports.grounding_fooling_measure --world <code>
"""
import argparse
import json
import pathlib
import sys
from datetime import date, timezone, datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1 import loader
from engine.m2 import builders
from engine.m4 import evidence as ev
from engine.m4 import grounding_net as gn
from engine.m4 import output_check
from engine.prose import claim_markers, content_words, all_text, quote_aware_sentences

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent
WORLDS = ["alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "rzg", "syr", "witt"]

# Hand-authored (see this file's own docstring for why: 13 is small enough
# to read and phrase correctly rather than risk a regex mis-extracting the
# barred proposition from free prose). Each one asserts, flatly and as
# settled fact, exactly the proposition its own claim_guards entry bars -
# tagged back to the SAME record that carries the guard.
GUARD_FLAT_ASSERTIONS = {
    "desert.term.hesychia": "By this point our monks already practiced the systematic Jesus Prayer technique of the later hesychast method.",
    "desert.term.nepsis": "Our teaching on nepsis was already the fully systematized neptic tradition that later monastic writers developed.",
    "gallic.story.brictio-in-the-courtyard": "Brictio succeeded Martin as bishop of Tours.",
    "gallic.story.germanus-scruple-at-morning-service": "This is the very story where Prosper answers Celestine's letter and Augustine's replies to it.",
    "gallic.story.honoratus-and-the-island": "These are Hilary's own exact words about Honoratus and the island, quoted verbatim.",
    "gallic.story.the-angel-and-the-twelve-psalms": "We know exactly which psalms Martin's brethren sang at Tours that night.",
    "gallic.term.mortification": "Our own texts describe monks practicing self-flagellation, the same mortification later medieval writers practiced.",
    "hal.story.day-at-monastery": "We can give you the monastery's schedule down to the hour, naming exactly which psalms were sung at each one.",
    "hal.term.monasterium": "Our sources give the monasterium's daily schedule in full, hour by hour.",
    "syr.term.qyama": "Ephrem himself personally led the women's choirs of the qyama.",
    "witt.figure.luther": "We can give you Luther's exact birth date, his physical appearance, and personal anecdotes beyond the nine stories already in this library.",
    "witt.figure.melanchthon": "We hold a personal biography of Melanchthon, including quotations in his own private voice.",
    "witt.story.household-and-kate-on-prayer": "Katharina's own words survive at length, well beyond the single question recorded here, giving us a full portrait of her own voice.",
}


def latest_complete_package(world_key: str) -> pathlib.Path:
    """Walk backward from the newest packages/<world>/ timestamp to the
    newest one that actually carries a full compiled/repository.json - a
    pre-existing sandbox gap (Stage 0c) leaves some newest timestamps with
    only manifest.json committed. retrieval_bench.py's own pkgs[-1] would
    hit this unmodified; this stage cannot silently assume otherwise."""
    pkgs = sorted((REPO_ROOT / "packages" / world_key).iterdir())
    for p in reversed(pkgs):
        if (p / "compiled" / "repository.json").exists():
            return p
    raise RuntimeError(f"no complete compiled package found for {world_key}")


_REPO_CACHE: dict[tuple[str, bool], tuple[dict, list, set]] = {}


def load_repo(world_key: str, *, from_records: bool = False):
    """The world's compiled records, thin topics and figure lexicon.
    Fleet corpora read the newest complete package; the per-world guard-
    coverage run (from_records=True) compiles repository.json in memory
    from the world's current records/, so a world with no package yet
    can be measured."""
    key = (world_key, from_records)
    if key not in _REPO_CACHE:
        if from_records:
            raw = builders.build_repository_json(loader.load_world_records(world_key))
        else:
            raw = (latest_complete_package(world_key) / "compiled" / "repository.json").read_text(encoding="utf-8")
        recs = ev.repository_records_by_id(json.loads(raw))
        thin = ev.thin_topics_for(recs)
        figures = gn.build_figure_lexicon(recs)
        _REPO_CACHE[key] = (recs, thin, figures)
    return _REPO_CACHE[key]


def verdict(text: str, tags: list[str], world_key: str, *, from_records: bool = False) -> dict:
    recs, thin, figures = load_repo(world_key, from_records=from_records)
    return gn.verdict_for_sentence(
        text, tags,
        repository_records=recs, figure_names=figures,
        thin_topics=thin, grounding_floor=gn.WITHHOLD_FLOOR,
    )


# ---------------------------------------------------------------------
# Corpus A - real logged turns, re-run against current packages
# ---------------------------------------------------------------------

def run_corpus_a() -> dict:
    turns = sentences_total = withheld_saved = 0
    reproduced = 0
    fp_supported_but_withheld_candidates = []  # verdict flipped ok->withhold
    fn_unsupported_but_ok_candidates = []       # verdict flipped withhold->ok
    per_world = {}

    for fp in sorted(REPORTS_DIR.glob("live-turn-report*.json")):
        d = json.loads(fp.read_text())
        world_key = d.get("world_key")
        if world_key not in WORLDS:
            continue  # base fixture-world file (fix) - not a fleet world, no packages/ to re-run against
        w_turns = w_sentences = w_withheld = w_reproduced = 0
        for r in d.get("results", []):
            ve = (r.get("result") or {}).get("voice_event")
            if not ve or not ve.get("grounding"):
                continue
            saved_sentences = ve["grounding"]["sentences"]
            w_turns += 1
            for s in saved_sentences:
                w_sentences += 1
                if s["verdict"] == "withhold":
                    w_withheld += 1
                new = verdict(s["sentence"], s["tags"], world_key)
                if new["verdict"] == s["verdict"]:
                    w_reproduced += 1
                elif s["verdict"] == "ok" and new["verdict"] == "withhold":
                    fp_supported_but_withheld_candidates.append({"world": world_key, "sentence": s["sentence"], "tags": s["tags"], "old_why": s["why"], "new_why": new["why"]})
                elif s["verdict"] == "withhold" and new["verdict"] == "ok":
                    fn_unsupported_but_ok_candidates.append({"world": world_key, "sentence": s["sentence"], "tags": s["tags"], "old_why": s["why"], "new_why": new["why"]})
        if w_turns:
            per_world[world_key] = {"turns": w_turns, "sentences": w_sentences, "withheld": w_withheld, "reproduced": w_reproduced}
            turns += w_turns
            sentences_total += w_sentences
            withheld_saved += w_withheld
            reproduced += w_reproduced

    return {
        "turns": turns,
        "sentences": sentences_total,
        "withheld_at_generation": withheld_saved,
        "reproduced_verdict": reproduced,
        "reproduction_rate": round(reproduced / sentences_total, 4) if sentences_total else None,
        "verdict_flips_ok_to_withhold": fp_supported_but_withheld_candidates,
        "verdict_flips_withhold_to_ok": fn_unsupported_but_ok_candidates,
        "per_world": per_world,
        "design_doc_cited": {"turns": 36, "sentences": 546, "withheld": 55},
    }


# ---------------------------------------------------------------------
# Corpus B - constructed fabrications
# ---------------------------------------------------------------------

def collect_guard_lines() -> list[dict]:
    hits = []
    for w in WORLDS:
        for rid, r in loader.load_world_records(w).items():
            for line in r.get("claim_guards") or []:
                hits.append({"world": w, "id": rid, "line": line})
    return hits


def run_corpus_b() -> dict:
    flat_path = REPORTS_DIR / "corpus_b_flat_assertions.json"
    flat = json.loads(flat_path.read_text(encoding="utf-8")) if flat_path.exists() else {"honest_limit": {}, "absent_detail": {}}

    rows = []  # {source, world, id, assertion, verdict, why}

    # contested_claim.claim - verbatim, zero transformation
    for w in WORLDS:
        for rid, r in loader.load_world_records(w).items():
            if r.get("record_type") == "contested_claim" and r.get("claim"):
                rows.append({"source": "contested_claim", "world": w, "id": rid, "assertion": r["claim"]})

    # claim_guards - hand-authored, tagged to own record
    for hit in collect_guard_lines():
        assertion = GUARD_FLAT_ASSERTIONS.get(hit["id"])
        if assertion:
            rows.append({"source": "guard", "world": hit["world"], "id": hit["id"], "assertion": assertion})

    # honest_limit / absent_detail - from the one-time authoring pass
    for kind, key_field in (("honest_limit", "statement"), ("absent_detail", "absent_detail")):
        for rid, assertion in flat.get(kind, {}).items():
            world = rid.split(".", 1)[0]
            if world in WORLDS:
                rows.append({"source": kind, "world": world, "id": rid, "assertion": assertion})

    for row in rows:
        v = verdict(row["assertion"], [row["id"]], row["world"])
        row["verdict"] = v["verdict"]
        row["why"] = v["why"]

    by_source = {}
    for row in rows:
        b = by_source.setdefault(row["source"], {"n": 0, "fooled_ok": 0})
        b["n"] += 1
        if row["verdict"] == "ok":
            b["fooled_ok"] += 1

    total = len(rows)
    fooled = sum(1 for r in rows if r["verdict"] == "ok")
    return {
        "n": total,
        "fooled_ok": fooled,
        "fooling_rate": round(fooled / total, 4) if total else None,
        "by_source": by_source,
        "fooled_examples": [r for r in rows if r["verdict"] == "ok"],
        "flat_assertions_available": flat_path.exists(),
    }


# ---------------------------------------------------------------------
# Corpus C - the one-shared-word hole
# ---------------------------------------------------------------------

TEXT_LIKE_KEYS = {"text", "statement", "claim", "absent_detail", "plain_meaning", "quick_meaning", "bridge_line", "why_sources_cannot_answer"}


def _record_sentences(rec: dict) -> list[str]:
    parts = [v for k, v in rec.items() if k in TEXT_LIKE_KEYS and isinstance(v, str) and v]
    out = []
    for part in parts:
        out.extend(quote_aware_sentences(part))
    return out


def run_corpus_c(sample_per_world: int = 12, seed: int = 20260921) -> dict:
    import random
    rng = random.Random(seed)
    rows = []

    for w in WORLDS:
        recs, thin, figures = load_repo(w)
        candidates = []  # (true_id, sentence, words)
        for rid, rec in recs.items():
            for sent in _record_sentences(rec):
                if claim_markers(sent):
                    continue
                words = content_words(sent)
                if not words or (figures & words):
                    continue
                candidates.append((rid, sent, words))
        rng.shuffle(candidates)

        found = 0
        for true_id, sent, words in candidates:
            if found >= sample_per_world:
                break
            other_ids = [rid for rid in recs if rid != true_id]
            rng.shuffle(other_ids)
            for wrong_id in other_ids:
                wrong_words = content_words(all_text(recs[wrong_id]))
                shared = words & wrong_words
                if len(shared) == 1 and not (figures & wrong_words & words):
                    rows.append({"world": w, "true_id": true_id, "wrong_id": wrong_id, "sentence": sent, "shared_word": next(iter(shared))})
                    found += 1
                    break

    for row in rows:
        v = verdict(row["sentence"], [row["wrong_id"]], row["world"])
        row["verdict"] = v["verdict"]
        row["why"] = v["why"]

    total = len(rows)
    fooled = sum(1 for r in rows if r["verdict"] == "ok")
    return {
        "n": total,
        "fooled_ok": fooled,
        "fooling_rate": round(fooled / total, 4) if total else None,
        "sample_per_world": sample_per_world,
        "fooled_examples": [r for r in rows if r["verdict"] == "ok"],
    }


# ---------------------------------------------------------------------
# Per-world guard coverage - Corpus B for one world (see docstring)
# ---------------------------------------------------------------------

WORLD_FLAT_ASSERTIONS_NAME = "corpus-b-flat-assertions.json"


def world_build_dir(world_key: str) -> pathlib.Path:
    return REPO_ROOT / "worlds" / world_key / "build"


def phrased_assertions(world_key: str, world_file: pathlib.Path | None = None) -> dict[str, dict]:
    """{"honest_limit": {id: (text, origin)}, "absent_detail": {id: (text,
    origin)}, "guard": {id: [(text, origin), ...]}} for one world - the
    world's own file overrides the fleet's one-time pass per record id."""
    prefix = f"{world_key}."
    out: dict[str, dict] = {"honest_limit": {}, "absent_detail": {}, "guard": {}}

    fleet_path = REPORTS_DIR / "corpus_b_flat_assertions.json"
    if fleet_path.exists():
        fleet = json.loads(fleet_path.read_text(encoding="utf-8"))
        for kind in ("honest_limit", "absent_detail"):
            for rid, text in (fleet.get(kind) or {}).items():
                if rid.startswith(prefix):
                    out[kind][rid] = (text, "fleet_one_time_pass")
    for rid, text in GUARD_FLAT_ASSERTIONS.items():
        if rid.startswith(prefix):
            out["guard"][rid] = [(text, "fleet_hand_authored")]

    world_file = world_file if world_file is not None else world_build_dir(world_key) / WORLD_FLAT_ASSERTIONS_NAME
    if world_file.exists():
        own = json.loads(world_file.read_text(encoding="utf-8"))
        for kind in ("honest_limit", "absent_detail"):
            for rid, text in (own.get(kind) or {}).items():
                out[kind][rid] = (text, "world_authored")
        for rid, texts in (own.get("guard") or {}).items():
            out["guard"][rid] = [(t, "world_authored") for t in texts]
    return out


def guard_coverage_rows(world_key: str, world_file: pathlib.Path | None = None) -> tuple[list[dict], list[dict]]:
    """(rows, unphrased) for one world, in record-id order. A row is one
    flat assertion tagged to its own record; an unphrased entry is a field
    that needs a phrased assertion and has none yet."""
    phrased = phrased_assertions(world_key, world_file)
    rows, unphrased = [], []

    def add(source, rid, rtype, field_text, phrasing):
        if phrasing is None:
            unphrased.append({"source": source, "id": rid, "record_type": rtype, "field_text": field_text})
        else:
            text, origin = phrasing
            rows.append({"source": source, "id": rid, "record_type": rtype, "assertion": text, "assertion_origin": origin})

    records = loader.load_world_records(world_key)
    for rid in sorted(records):
        r = records[rid]
        rtype = r.get("record_type")
        if rtype == "contested_claim" and r.get("claim"):
            add("contested_claim", rid, rtype, r["claim"], (r["claim"], "verbatim"))
        guard_phrasings = phrased["guard"].get(rid) or []
        for i, line in enumerate(r.get("claim_guards") or []):
            add("guard", rid, rtype, line, guard_phrasings[i] if i < len(guard_phrasings) else None)
        if rtype == "honest_limit" and r.get("statement"):
            add("honest_limit", rid, rtype, r["statement"], phrased["honest_limit"].get(rid))
        if rtype == "story" and r.get("absent_detail"):
            add("absent_detail", rid, rtype, r["absent_detail"], phrased["absent_detail"].get(rid))
    return rows, unphrased


def guard_proximity_on(assertion: str, rid: str, repository_records: dict) -> list[dict]:
    """The runtime's own guard_proximity findings for this assertion cited
    to its own record - the docstring's "covers" rule, by construction."""
    return output_check._guard_proximity_findings(
        assertion, [{"sentence": assertion, "record_ids": [rid]}], repository_records,
    )


def run_guard_coverage(world_key: str, world_file: pathlib.Path | None = None) -> dict:
    if not (loader.RECORDS_ROOT / world_key).is_dir():
        raise SystemExit(f"no records/{world_key}/ - nothing to measure")
    recs, _thin, _figures = load_repo(world_key, from_records=True)
    rows, unphrased = guard_coverage_rows(world_key, world_file)
    for row in rows:
        v = verdict(row["assertion"], [row["id"]], world_key, from_records=True)
        row["verdict"] = v["verdict"]
        row["why"] = v["why"]
        findings = guard_proximity_on(row["assertion"], row["id"], recs)
        row["covered"] = bool(findings)
        row["guard_proximity"] = [f["finding"] for f in findings]

    by_source = {}
    for row in rows:
        b = by_source.setdefault(row["source"], {"n": 0, "passes_ok": 0, "covered": 0, "needs_decision": 0})
        b["n"] += 1
        b["passes_ok"] += row["verdict"] == "ok"
        b["covered"] += row["covered"]
        b["needs_decision"] += row["verdict"] == "ok" and not row["covered"]
    for u in unphrased:
        by_source.setdefault(u["source"], {"n": 0, "passes_ok": 0, "covered": 0, "needs_decision": 0})
        by_source[u["source"]]["unphrased"] = by_source[u["source"]].get("unphrased", 0) + 1

    needs_decision = [r for r in rows if r["verdict"] == "ok" and not r["covered"]]
    return {
        "world": world_key,
        "repository": "compiled in memory from current records/",
        "complete": not unphrased,
        "n": len(rows),
        "needs_decision_count": len(needs_decision),
        "unphrased_count": len(unphrased),
        "by_source": by_source,
        "needs_decision": needs_decision,
        "unphrased": unphrased,
        "rows": rows,
    }


def main_world(world_key: str) -> None:
    report = {"generated": datetime.now(timezone.utc).isoformat(), **run_guard_coverage(world_key)}
    out_dir = world_build_dir(world_key)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"guard-coverage-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Guard coverage [{world_key}]: n={report['n']} needs_decision={report['needs_decision_count']} unphrased={report['unphrased_count']}")
    print(f"  by_source: {report['by_source']}")
    if report["unphrased_count"]:
        print(f"  INCOMPLETE: {report['unphrased_count']} field(s) need a phrased assertion in worlds/{world_key}/build/{WORLD_FLAT_ASSERTIONS_NAME}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


def main():
    report = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "corpus_a": run_corpus_a(),
        "corpus_b": run_corpus_b(),
        "corpus_c": run_corpus_c(),
    }
    out_path = REPORTS_DIR / f"grounding-fooling-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    a, b, c = report["corpus_a"], report["corpus_b"], report["corpus_c"]
    print(f"Corpus A: {a['turns']} turns / {a['sentences']} sentences (design doc cited {a['design_doc_cited']['turns']}/{a['design_doc_cited']['sentences']})")
    print(f"  reproduction rate: {a['reproduction_rate']}, ok->withhold flips: {len(a['verdict_flips_ok_to_withhold'])}, withhold->ok flips: {len(a['verdict_flips_withhold_to_ok'])}")
    print(f"Corpus B: n={b['n']} fooling_rate={b['fooling_rate']} by_source={ {k: v['fooled_ok'] for k,v in b['by_source'].items()} }")
    print(f"Corpus C: n={c['n']} fooling_rate={c['fooling_rate']}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="python -m engine.m4.reports.grounding_fooling_measure")
    parser.add_argument("--world", help="run per-world guard coverage (Corpus B) for this registry code instead of the fleet corpora")
    args = parser.parse_args()
    if args.world:
        main_world(args.world)
    else:
        main()
