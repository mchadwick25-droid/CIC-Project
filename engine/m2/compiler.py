"""compile_world(): the pure orchestration function. Same world_key +
records tree content + package_id + records_commit + compiler_version in =>
byte-identical package (a dict of relative_path -> bytes) out, every time
(Artifact-2 SS3, the stage-2 gate). No filesystem writes happen in here -
that's cli.py's job - so the determinism check can call this twice and diff
dicts in memory, no disk I/O race possible.
"""
import json
from pathlib import Path

from engine.m1.loader import REPO_ROOT as RECORDS_REPO_ROOT
from engine.m1.loader import RECORDS_ROOT, load_fleet_records, load_world_records, package_records, voiced_records
from engine.m1.registry import get_world, is_fixture, load_registry

from . import builders, validation
from .canonical import canonical_json
from .manifest import build_manifest, manifest_hash

RECORD_SCHEMA_VERSION = 2

# registry_entry (records/worlds.yaml) feeds build_capsule/build_frame_json
# even though it lives outside records/<world_key>/ - so `records_commit`
# only truthfully describes what this package was built from when it names
# a commit where the registry and the world's records were BOTH already
# committed. Building against a dirty working tree (registry edited after
# the records, before either is committed) will compile fine but silently
# go stale the moment you check - discovered exactly this way while wiring
# stage 2/3 evidence: rebuild after the registry settles, never before.

# Files whose bytes are (or become) live model input: no generated-by header
# is stamped into these, ever, because that text would corrupt what the
# runtime later sends to a model. Their provenance is carried by the
# manifest's file-hash entry instead (DECIDABLE, recorded in the stage-2
# commit).
_NO_STAMP_PREFIXES = ("compiled/prompt.txt", "compiled/capsule.md", "compiled/chunks/")


def _frozen_records_copy(world_key: str, records: dict[str, dict], records_root: Path = RECORDS_ROOT) -> dict[str, bytes]:
    """The files of exactly the records given (each record's own _path),
    never a fresh glob, so a stray non-record file beside them is never
    copied."""
    world_dir = records_root / world_key
    out = {}
    for record in records.values():
        path = RECORDS_REPO_ROOT / record["_path"]
        rel = f"records/{path.relative_to(world_dir).as_posix()}"
        out[rel] = path.read_bytes()
    return out


def _stamp(path: str, content: bytes, provenance: str) -> bytes:
    if path.startswith("records/") or path.startswith(_NO_STAMP_PREFIXES):
        return content
    if path.endswith(".svg"):
        return f"<!-- generated-by: {provenance} -->\n".encode("utf-8") + content
    # every remaining compiled file is canonical_json output (dict-shaped)
    obj = json.loads(content)
    return canonical_json({"_generated_by": provenance, **obj})


def unstamp(path: str, content: bytes) -> bytes:
    """The inverse of _stamp: a compiled file's content without its
    generated-by provenance."""
    if path.startswith("records/") or path.startswith(_NO_STAMP_PREFIXES):
        return content
    if path.endswith(".svg"):
        first, _, rest = content.partition(b"\n")
        return rest if first.startswith(b"<!-- generated-by:") else content
    obj = json.loads(content)
    obj.pop("_generated_by", None)
    return canonical_json(obj)


def compile_world(
    *,
    world_key: str,
    package_id: str,
    records_commit: str,
    compiler_version: str,
    records_root: Path = RECORDS_ROOT,
) -> dict[str, bytes]:
    registry = load_registry()
    registry_entry = get_world(world_key, registry)
    fleet = load_fleet_records()
    records = load_world_records(world_key, records_root=records_root)
    voiced = voiced_records(records)

    provenance = f"cic-m2-compiler {compiler_version} from records_commit {records_commit}"

    compiled: dict[str, bytes] = {
        "compiled/prompt.txt": builders.build_prompt(voiced, registry_entry),
        "compiled/capsule.md": builders.build_capsule(voiced, registry_entry),
        "compiled/quotes.json": builders.build_quotes_json(voiced),
        "compiled/figures.json": builders.build_figures_json(voiced),
        "compiled/repository.json": builders.build_repository_json(voiced),
        "compiled/coverage.json": builders.build_coverage_json(voiced, fleet),
        "compiled/frame.json": builders.build_frame_json(voiced, fleet, registry_entry),
        "compiled/indexes/canon-map.json": builders.build_canon_map_json(fleet),
    }
    compiled.update(builders.build_chunks(voiced))
    compiled.update(builders.build_indexes(voiced))
    compiled.update(builders.build_media(registry_entry))

    validation_files = {
        "validation/gates-report.json": validation.build_gates_report(records, fleet, registry),
        "validation/admission/results.json": validation.build_admission_results(world_key),
        "validation/signoffs.json": validation.build_signoffs(
            world_key, is_fixture=is_fixture(registry_entry), state=registry_entry.get("state", "built")
        ),
    }

    frozen_records = _frozen_records_copy(world_key, package_records(world_key, records, records_root), records_root=records_root)

    other_files = {**compiled, **validation_files, **frozen_records}
    other_files = {path: _stamp(path, content, provenance) for path, content in other_files.items()}

    manifest = build_manifest(
        world_key=world_key,
        package_id=package_id,
        record_schema_version=RECORD_SCHEMA_VERSION,
        compiler_version=compiler_version,
        records_commit=records_commit,
        other_files=other_files,
        records=records,
        fleet=fleet,
    )
    manifest_bytes = canonical_json(manifest)

    package = {"manifest.json": manifest_bytes, **other_files}
    return package


def compile_and_hash(**kwargs) -> tuple[dict[str, bytes], str]:
    package = compile_world(**kwargs)
    manifest = json.loads(package["manifest.json"])
    return package, manifest_hash(manifest)
