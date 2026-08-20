"""The stub loader (Artifact-2 SS2): recomputes the manifest hash and
spot-verifies every file hash a package claims. Mismatch => refuse to serve
that world ("temporarily unavailable"); this is the named availability
decision - a wrong world is worse than an absent one. A stub because the
real M4 loader (stage 5) adds lazy loading, LRU eviction, and mmap'd
indexes; the hash-verification contract itself is exactly this, unchanged.
"""
import json
from pathlib import Path

from .canonical import sha256_prefixed
from .manifest import manifest_hash as compute_manifest_hash


class PackageRefused(Exception):
    """Raised with a human-readable reason - never a silent failure."""


def verify_package_dict(package: dict[str, bytes], expected_manifest_hash: str) -> None:
    manifest = json.loads(package["manifest.json"])
    actual_hash = compute_manifest_hash(manifest)
    if actual_hash != expected_manifest_hash:
        raise PackageRefused(
            f"manifest hash mismatch: registry expects {expected_manifest_hash}, package computes {actual_hash}"
        )
    for path, expected_file_hash in manifest["files"].items():
        if path not in package:
            raise PackageRefused(f"manifest lists {path!r} but the package does not contain it")
        actual_file_hash = sha256_prefixed(package[path])
        if actual_file_hash != expected_file_hash:
            raise PackageRefused(
                f"file hash mismatch on {path!r}: manifest expects {expected_file_hash}, actual {actual_file_hash}"
            )


def verify_package_dir(package_dir: Path, expected_manifest_hash: str) -> None:
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.exists():
        raise PackageRefused(f"no manifest.json under {package_dir}")
    package = {"manifest.json": manifest_path.read_bytes()}
    manifest = json.loads(package["manifest.json"])
    for path in manifest["files"]:
        file_path = package_dir / path
        if not file_path.exists():
            raise PackageRefused(f"manifest lists {path!r} but it is missing on disk under {package_dir}")
        package[path] = file_path.read_bytes()
    verify_package_dict(package, expected_manifest_hash)
