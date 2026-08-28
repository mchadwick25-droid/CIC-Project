#!/usr/bin/env python3
"""The corpus map: which works belong to which Atlas entry.

Mark, 2026-08-26: *"lets keep this separate from the built worlds with clear
buckets that align, then we can figure out how best to integrate this into
each world after we do the parsing and organizing."*

So this lives at `cic/corpus-map/`, outside `records/` entirely - beside the
texts it describes and the tooling that reads them, and touched by nothing in
the compile path. `records/_fleet/` would NOT have been separate: compile_world()
loads the fleet records on every build (build_coverage_json,
build_canon_map_json, and the manifest), so anything there moves all seven
package hashes.

ONE FILE PER ATLAS ENTRY, NAMED FOR THE CENSUS ID. That is what "clear buckets
that align" means concretely - the filename IS the key, so alignment is
structural rather than something anyone keeps in sync, and integration later is
a join on a key that already matches:

    cic/corpus-map/desert-monasticism.yaml
    cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml

Three rulings are enforced here rather than left to memory:

  PER WORK (Mark, 2026-08-26). Not per volume - anf02 holds five authors
      belonging to different traditions. Not per author either - Athanasius'
      Vita Antonii belongs to desert while his Against the Arians belongs to
      Alexandria. The unit is the work.

  NON-EXCLUSIVE. A work may appear in as many entries as need it. desert's
      most important source is the Vita, whose author is Alexandria's - an
      exclusive partition would silently destroy desert's evidential base
      while looking tidy. A validator that demanded uniqueness would be
      enforcing a bug.

  ROLE: TRADITION | CONTEXT | ANTECEDENT | TRANSMISSION.

      `transmission` was added 2026-08-26 on Mark's ruling, after three works
      in the Syriac pile turned out to be saying the same thing in different
      words: `syr` was marking WHERE A TEXT WAS PRESERVED, not whose voice it
      is. The Ambrose hypomnemata is a Greek apology that survives only
      because Syriac scribes copied it. The Testaments of the Twelve
      Patriarchs, the Life of Adam and Eve and the Narrative of Zosimus are
      Jewish works that survive only because Christian scribes went on copying
      them after Judaism had let them go.

      THE RELATION IS CUSTODY. Not authorship, not opposition, not authority.
      An assignment is `transmission` when the work ORIGINATES OUTSIDE the
      entry and the entry's people are why we still have it.

      THE BOUNDARY, which is the whole reason this was measured before it was
      added. A scan for preservation language returned 25 rows, and reading
      them showed it conflating three different relations. Only the first
      belongs here:

        transmission   this tradition preserved a work that is not its voice.
        embedded voice an opponent's words survive INSIDE a work of this
                       tradition - Celsus inside Origen's refutation, Petilian
                       inside Augustine's, Mani inside Augustine's. The
                       containing work is the tradition's own; the quoted
                       voice has no separate custody relation, and marking one
                       would make every polemic a transmission.
        attested-by    a lost work survives as fragments quoted by a later
                       author - Alexander of Jerusalem via Eusebius. That is a
                       fact about the source record, not a relation between an
                       entry and a work.

      A work the tradition COMPOSED is `tradition`, however widely it was
      later copied. And an entry whose whole subject is preserved material -
      `apocryphal-and-pseudepigraphal-literature` - holds that material as
      `tradition`, because there it is the content rather than the custody:
      the Testaments are `tradition` in the apocrypha entry and
      `transmission` in `post-apostolic-house-church`, whose scribes kept them.

      `antecedent` was added 2026-08-26 for a relation the first two cannot
      express. The Donatists claimed Cyprian as their charter authority - his
      rebaptism practice, his purity-of-clergy ecclesiology, the Carthage
      council of 256. He is not a Donatist, so `tradition` is false. He died
      fifty years before the schism began, so `context` - describing a
      movement from outside - is false too. He is the authority the movement
      argued FROM, and both sides did: Augustine's *On Baptism, Against the
      Donatists* names him 306 times in ninety thousand words.

      THE RULE THAT STOPS THIS EXPLODING, and it needs one. If "a later
      movement claimed him" were sufficient, Augustine would be assigned to
      every Reformation entry and Origen to everything after him, and the map
      would say nothing. So: an `antecedent` assignment requires that the
      entry's OWN VENDORED SOURCES ARGUE FROM THE TEXT - that reading this
      entry means reading that work. Demonstrable in the corpus, not asserted
      from what the tradition later said about itself. Admiration and descent
      are not enough; the argument has to run through the words.

      A contemporary opponent is `context`, not `antecedent`. Cyprian is
      antecedent to `donatism` and context for `novatianism`, whose schism he
      lived through and argued against - the same author, two relations, which
      is the point of having the field at all.

  ROLE: TRADITION | CONTEXT (Mark, 2026-08-26: "it carries a context marker
      for that world"). Julian, Porphyry, Libanius and Ammianus are assigned
      to the entry they SURROUND, marked context. They are the view from
      outside, which no Christian source can supply. The half of that ruling
      this file can check is structural; the other half - that no `register:
      emic` record ever cites a context work - becomes checkable at
      integration, and is named in the brief so it is not forgotten.

INTEGRATION IS DELIBERATELY NOT DESIGNED HERE. How a world's records come to
draw on this map is a later decision, made with the map in hand.

    python cic/engine/corpus_map.py            # validate + report
    python cic/engine/corpus_map.py --coverage # also list unassigned sources
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
MAP_DIR = REPO_ROOT / "cic" / "corpus-map"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
CENSUS = REPO_ROOT / "cic-website" / "data" / "world-census.json"

ROLES = {"tradition", "context", "antecedent", "transmission"}
CONFIDENCES = {"assigned", "provisional", "needs-ruling"}
REQUIRED = ("work", "author", "source_file", "role", "confidence")

# Pre-Survey Candidate entries ARE valid targets - Mark, 2026-08-26. 215 of the
# census's 274 movements sit in eras whose Step 0 survey has not run, and
# material plainly belonging to one of them should be placed there rather than
# held back. Placing a source is not a claim that the era's survey has run.
_ANY_STATUS = True


def census_ids() -> dict[str, str]:
    """movement id -> status. Read fresh; the census grows."""
    if not CENSUS.is_file():
        return {}
    data = json.loads(CENSUS.read_text(encoding="utf-8"))
    return {m["id"]: m.get("status", "") for m in data.get("movements", [])}


def load() -> dict[str, dict]:
    """atlas_id -> the parsed file. Missing directory is not an error - the
    map does not exist until the assignment thread starts."""
    import yaml

    out: dict[str, dict] = {}
    if not MAP_DIR.is_dir():
        return out
    for path in sorted(MAP_DIR.glob("*.yaml")):
        if path.name == "UNATTRIBUTED.yaml":      # a ruling list, not a bucket
            continue
        out[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return out


def validate() -> list[str]:
    findings: list[str] = []
    ids = census_ids()
    if not ids:
        return [f"cannot read the census at {CENSUS}"]
    vendored = {p.name for p in TEXTS_DIR.iterdir() if p.suffix in (".xml", ".txt")} if TEXTS_DIR.is_dir() else set()

    sys.path.insert(0, str(HERE))
    from corpus_authors import build_index

    known_authors = set(build_index()[0])
    # Authors CCEL's markup does not supply, ruled on with evidence by the
    # assignment thread and collected by corpus_map_merge.py. Without this the
    # Didache and the Pastor of Hermas have no legal `author` value at all,
    # and §6.4 of the brief makes them first-class - so the escape has to
    # exist. It is narrow on purpose: a slug is legal because a RULING exists,
    # never because a session was confident.
    unattributed = MAP_DIR / "UNATTRIBUTED.yaml"
    if unattributed.is_file():
        import yaml
        declared = (yaml.safe_load(unattributed.read_text(encoding="utf-8")) or {}).get("authors") or {}
        known_authors |= set(declared)

    for atlas_id, doc in load().items():
        where = f"{atlas_id}.yaml"
        if atlas_id not in ids:
            findings.append(f"{where}: filename is not a census movement id")
        if doc.get("atlas_id") != atlas_id:
            findings.append(f"{where}: atlas_id {doc.get('atlas_id')!r} does not match the filename")
        works = doc.get("works")
        if not isinstance(works, list) or not works:
            findings.append(f"{where}: no works listed")
            continue
        seen: set[tuple] = set()
        for i, entry in enumerate(works):
            tag = f"{where}[{i}]"
            if not isinstance(entry, dict):
                findings.append(f"{tag}: not a mapping")
                continue
            for field in REQUIRED:
                if not str(entry.get(field) or "").strip():
                    findings.append(f"{tag}: missing {field!r}")
            if entry.get("role") not in ROLES | {None}:
                findings.append(f"{tag}: role {entry.get('role')!r} not in {sorted(ROLES)}")
            if entry.get("confidence") not in CONFIDENCES | {None}:
                findings.append(f"{tag}: confidence {entry.get('confidence')!r} not in {sorted(CONFIDENCES)}")
            source_file = entry.get("source_file")
            if source_file and vendored and source_file not in vendored:
                findings.append(f"{tag}: source_file {source_file!r} is not in cic/texts/")
            author = entry.get("author")
            if author and known_authors and author not in known_authors:
                findings.append(f"{tag}: author {author!r} is not in the corpus author index "
                                "(cic/texts/AUTHORS.md) - if it is a genuinely anonymous or "
                                "pseudonymous work, that needs its own ruling, not a guess")
            # Per-work, per-entry: the same work twice in ONE atlas entry is a
            # duplicate. The same work in SEVERAL entries is expected and
            # correct - see the module docstring on non-exclusivity.
            key = (str(entry.get("work")).strip().lower(), str(entry.get("source_file")))
            if key in seen:
                findings.append(f"{tag}: {entry.get('work')!r} listed twice in this entry")
            seen.add(key)
    return findings


def report(show_coverage: bool = False) -> int:
    findings = validate()
    docs = load()
    works = [(a, w) for a, d in docs.items() for w in (d.get("works") or []) if isinstance(w, dict)]
    ids = census_ids()

    if not docs:
        print(f"no corpus map yet at {MAP_DIR.relative_to(REPO_ROOT)}/ - nothing to validate.")
        return 0

    by_role: dict[str, int] = {}
    by_confidence: dict[str, int] = {}
    for _, w in works:
        by_role[w.get("role", "?")] = by_role.get(w.get("role", "?"), 0) + 1
        by_confidence[w.get("confidence", "?")] = by_confidence.get(w.get("confidence", "?"), 0) + 1

    print(f"corpus map: {len(works)} work assignment(s) across {len(docs)} Atlas entry(ies)")
    print(f"  role      : {by_role}")
    print(f"  confidence: {by_confidence}")
    statuses: dict[str, int] = {}
    for atlas_id in docs:
        statuses[ids.get(atlas_id, "unknown")] = statuses.get(ids.get(atlas_id, "unknown"), 0) + 1
    print(f"  entries by census status: {statuses}")

    if show_coverage and TEXTS_DIR.is_dir():
        assigned = {w.get("source_file") for _, w in works}
        unassigned = sorted({p.name for p in TEXTS_DIR.iterdir() if p.suffix in (".xml", ".txt")} - assigned)
        print(f"\n  {len(unassigned)} vendored file(s) with no work assigned from them yet:")
        for name in unassigned:
            print(f"    {name}")

    if findings:
        print(f"\n{len(findings)} finding(s):")
        for f in findings:
            print(f"  {f}")
        return 1
    print("\nvalid.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python cic/engine/corpus_map.py")
    parser.add_argument("--coverage", action="store_true", help="also list vendored files with nothing assigned")
    return report(parser.parse_args(argv).coverage)


if __name__ == "__main__":
    sys.exit(main())
