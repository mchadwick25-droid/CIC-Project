"""Builds a world's sub-question sidecar from the Question-Coverage maps.

The sidecar lists, for every sub-question in the repository's sub-question file,
its label and cluster, and for the one world named, the records of that world
that the coverage maps list for it. A record id the world's compiled repository
does not hold is left out and counted.

  python tools/build_answers_sidecar.py --world lpc \
      --repository packages/lpc/<stamp>/compiled/repository.json \
      --out Build/worlds/lpc/build/lpc_Answers_Sidecar.yaml

Reads Build/Ministry/Features/Question-Coverage/{Repository/07-subquestions.yaml,
Coverage-Maps/C*-coverage.json}. No model call.
"""
import argparse
import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE = REPO_ROOT / "Build" / "Ministry" / "Features" / "Question-Coverage"
RENDERED_LAYERS = ("RENDERED", "R*")


def _record_ids(entry: dict) -> list[str]:
    found = []
    for item in entry.get("records") or []:
        rid = item.get("id") if isinstance(item, dict) else item
        if isinstance(rid, str):
            found.append(rid.split(" (", 1)[0])
    return found


def build(world: str, repository_records: dict[str, dict]) -> tuple[dict, list[str], list[str]]:
    catalogue = yaml.safe_load((COVERAGE / "Repository" / "07-subquestions.yaml").read_text(encoding="utf-8"))["subquestions"]
    sub_questions = {s["id"]: {"cluster": s["c"], "label": s["label"], "records": []} for s in catalogue}
    unknown_ids: list[str] = []
    unheld_records: list[str] = []
    for path in sorted(COVERAGE.glob("Coverage-Maps/C*-coverage.json")):
        cluster = re.match(r"(C\d+)-coverage", path.name).group(1)
        entries = (json.loads(path.read_text(encoding="utf-8")).get("worlds") or {}).get(world) or {}
        for key, entry in entries.items():
            if not isinstance(entry, dict) or not re.fullmatch(r"S\d+", key):
                continue
            sid = f"{cluster}.{key}"
            if sid not in sub_questions:
                unknown_ids.append(sid)
                continue
            if entry.get("layer") not in RENDERED_LAYERS:
                continue
            for rid in _record_ids(entry):
                if rid not in repository_records:
                    unheld_records.append(f"{sid} {rid}")
                elif rid not in sub_questions[sid]["records"]:
                    sub_questions[sid]["records"].append(rid)
    return {"world": world, "subquestions": sub_questions}, sorted(set(unknown_ids)), sorted(set(unheld_records))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--world", required=True)
    parser.add_argument("--repository", required=True, type=Path, help="the world's compiled repository.json")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    repository = {r["id"]: r for r in json.loads(args.repository.read_text(encoding="utf-8"))["records"]}
    result, unknown, unheld = build(args.world, repository)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    held = sum(1 for s in result["subquestions"].values() if s["records"])
    print(json.dumps({"sub_questions": len(result["subquestions"]), "with_records": held, "unknown": unknown, "unheld_records": unheld}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
