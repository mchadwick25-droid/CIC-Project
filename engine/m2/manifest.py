"""manifest.json assembly (Artifact-2 SS2). files{} covers every OTHER file
in the package - manifest.json cannot list its own hash without a
fixed-point problem, so it is the root of trust and the registry stores its
hash externally (Artifact-1 SS2 `package.manifest_hash`), never inside
itself.
"""
from . import canon_summary
from .canonical import canonical_json, sha256_prefixed


def build_manifest(
    *,
    world_key: str,
    package_id: str,
    record_schema_version: int,
    compiler_version: str,
    records_commit: str,
    other_files: dict[str, bytes],
    records: dict,
    fleet: dict,
) -> dict:
    files = {path: sha256_prefixed(content) for path, content in sorted(other_files.items())}
    return {
        "package_schema": 1,
        "package_id": package_id,
        "world_key": world_key,
        "record_schema_version": record_schema_version,
        "built_by": f"cic-m2-compiler {compiler_version}",
        "records_commit": records_commit,
        "files": files,
        "coverage_summary": canon_summary.coverage_summary(records, fleet),
        "floors": canon_summary.declared_floors(records),
        "compat": {
            "min_runtime": None,
            "max_runtime": None,
            "note": "no runtime exists yet (M4 is stage 5); this package predates runtime versioning",
        },
    }


def manifest_hash(manifest: dict) -> str:
    return sha256_prefixed(canonical_json(manifest))
