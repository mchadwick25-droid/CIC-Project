"""S1.5 record validator + traceability checker (blueprint S1.5; M1: files-in-git).

A record file is a markdown file whose YAML front matter (between the leading
`---` fences) carries ALL schema fields (long prose as block scalars); any
markdown body after the front matter is commentary and is not validated.
Plain .yaml files are accepted too. Validation dispatches on `record_type`
to the matching $defs entry in records.schema.json for readable errors.

Extra check beyond JSON Schema: the em-dash sentinel. Pass 1 SS3.2's rule is
"empty is a typed null - never an em-dash"; any retrieval-block string that
is exactly an em-dash/dash sentinel is rejected.

Modes (from cic-poc/backend):
  python wrs/schema/validate.py --fixtures          # validate wrs/schema/fixtures/
  python wrs/schema/validate.py --records           # validate wrs/records/**
  python wrs/schema/validate.py --file <path>       # validate one file
  python wrs/schema/validate.py --matrix            # two-direction traceability check

Dependency: jsonschema (installed in the backend venv; not an app runtime
dependency - the app never imports this module).
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
SCHEMA = json.loads((HERE / "records.schema.json").read_text(encoding="utf-8"))
GLOSS_SCHEMA = json.loads((HERE / "confirmed_gloss.schema.json").read_text(encoding="utf-8"))

SENTINELS = {"—", "–", "-", "— ", " —"}


def parse_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".yaml":
        return yaml.safe_load(text)
    if not text.startswith("---"):
        raise ValueError(f"{path}: no front-matter fence")
    parts = text.split("\n---", 2)
    return yaml.safe_load(parts[0][3:])


def sentinel_violations(record):
    """Reject the em-dash-as-empty convention anywhere in a retrieval block."""
    out = []
    r = record.get("retrieval") or {}
    for cond in r.get("retrieve_when") or []:
        if cond.strip() in SENTINELS:
            out.append(f"retrieve_when carries a sentinel string {cond!r} - use an empty list")
    for cond in r.get("do_not_retrieve_when") or []:
        if isinstance(cond, dict) and cond.get("text", "").strip() in SENTINELS:
            out.append(f"do_not_retrieve_when carries a sentinel string - use an empty list")
    return out


def validate_record(record, source=""):
    import jsonschema
    errs = []
    rt = record.get("record_type")
    defs = SCHEMA["$defs"]
    if rt not in defs:
        return [f"{source}: unknown or missing record_type: {rt!r}"]
    sub = {"$defs": SCHEMA["$defs"], **defs[rt]}
    v = jsonschema.Draft202012Validator(sub)
    for e in sorted(v.iter_errors(record), key=lambda e: list(e.absolute_path)):
        errs.append(f"{source}: {'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message[:160]}")
    errs += [f"{source}: {m}" for m in sentinel_violations(record)]
    return errs


def validate_paths(paths):
    n_ok, errs = 0, []
    for p in sorted(paths):
        try:
            rec = parse_front_matter(p)
        except Exception as exc:
            errs.append(f"{p}: parse failure: {exc}")
            continue
        e = validate_record(rec, source=str(p.relative_to(BACKEND)))
        if e:
            errs += e
        else:
            n_ok += 1
    return n_ok, errs


def schema_property_paths():
    """Every $defs/<name>/properties/<prop> leaf the matrix must cover."""
    out = set()
    for name, d in SCHEMA["$defs"].items():
        for prop in (d.get("properties") or {}):
            if prop == "record_type":
                continue
            out.add(f"$defs/{name}/properties/{prop}")
    for prop in GLOSS_SCHEMA["properties"]["glosses"]["items"]["properties"]:
        out.add(f"gloss:properties/{prop}")
    return out


def matrix_check():
    matrix = yaml.safe_load((HERE / "TRACEABILITY.yaml").read_text(encoding="utf-8"))
    rows = matrix["rows"]
    covered = set()
    unresolved = []
    for row in rows:
        sp = row["schema_path"]
        covered.add(sp)
        if sp.startswith("gloss:"):
            node = GLOSS_SCHEMA
            parts = sp.split(":", 1)[1].split("/")
            if parts[0] == "properties":
                parts = ["properties", "glosses", "items"] + parts
            ok = sp in schema_property_paths()
            if not ok:
                unresolved.append(sp)
            continue
        node = SCHEMA
        ok = True
        for part in sp.split("/"):
            if part == "$defs":
                node = node.get("$defs", {})
            elif isinstance(node, dict) and part in node:
                node = node[part]
            else:
                ok = False
                break
        if not ok:
            unresolved.append(sp)
    props = schema_property_paths()
    uncovered = sorted(props - covered)
    extra_rows = sorted(covered - props - {r["schema_path"] for r in rows if "/" not in r["schema_path"].replace("$defs/", "", 1).replace("properties/", "", 1)})
    print(f"matrix rows: {len(rows)}")
    print(f"schema property paths: {len(props)}")
    print(f"direction 1 (Pass 1 field -> schema element): unresolved schema_paths: {len(unresolved)}")
    for u in unresolved:
        print("  UNRESOLVED:", u)
    print(f"direction 2 (schema element -> Pass 1 warrant): uncovered properties: {len(uncovered)}")
    for u in uncovered:
        print("  UNCOVERED:", u)
    return 0 if not unresolved and not uncovered else 1


def validate_gloss_list():
    """VG-1c: real JSON-Schema validation of the LIVE confirmed-gloss data
    against confirmed_gloss.schema.json - the schema was previously loaded
    only for the traceability matrix, never enforced (Voice-Governance
    Addendum SS1.1's finding). Until SS4.3's data move lands (Step 2/3),
    the live data is app/prompts/confirmed_glosses.py's world-keyed
    dataclass module; each entry is projected to the schema's entry shape
    (world_id from the dict key; exact_wording_required True - the
    module's own whitelist discipline, made explicit). Returns exit code."""
    import jsonschema
    sys.path.insert(0, str(BACKEND))
    from app.prompts.confirmed_glosses import CONFIRMED_GLOSSES
    doc = {"schema_version": 1, "glosses": []}
    for world_id, entries in CONFIRMED_GLOSSES.items():
        for g in entries:
            doc["glosses"].append({
                "world_id": world_id, "category": g.category,
                "original": g.original, "gloss": g.gloss,
                "exact_wording_required": True})
    v = jsonschema.Draft202012Validator(GLOSS_SCHEMA)
    errs = [f"{'/'.join(str(x) for x in e.absolute_path) or '<root>'}: "
            f"{e.message[:160]}"
            for e in sorted(v.iter_errors(doc),
                            key=lambda e: list(e.absolute_path))]
    n = len(doc["glosses"])
    by_world = {}
    for g in doc["glosses"]:
        by_world[g["world_id"]] = by_world.get(g["world_id"], 0) + 1
    print(f"gloss entries valid: {n - len(errs)} / {n} "
          f"({', '.join(f'{w} {c}' for w, c in sorted(by_world.items()))})")
    for e in errs:
        print("  ERROR:", e)
    return 1 if errs else 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fixtures", action="store_true")
    p.add_argument("--records", action="store_true")
    p.add_argument("--file")
    p.add_argument("--matrix", action="store_true")
    p.add_argument("--glosses", action="store_true")
    args = p.parse_args()

    if args.matrix:
        sys.exit(matrix_check())

    if args.glosses:
        sys.exit(validate_gloss_list())

    if args.fixtures:
        paths = list((HERE / "fixtures").glob("*.md")) + list((HERE / "fixtures").glob("*.yaml"))
    elif args.records:
        paths = list((BACKEND / "wrs" / "records").rglob("*.md")) + \
                list((BACKEND / "wrs" / "records").rglob("*.yaml"))
    elif args.file:
        paths = [Path(args.file)]
    else:
        p.print_help()
        return

    n_ok, errs = validate_paths(paths)
    print(f"valid: {n_ok} / {n_ok + len(set(e.split(':')[0] for e in errs))} files")
    for e in errs:
        print("  ERROR:", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
