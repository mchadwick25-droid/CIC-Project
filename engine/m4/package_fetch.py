"""The seam between object storage (engine.m4.object_storage) and
LazyWorldLoader (WO-1, 2026-09-16). ensure_package_local() is the only
thing engine/api/wiring.py needs to call before world_loader.load() -
it guarantees a package's files are on local disk somewhere, but does
NOT verify their content is correct. That stays load()'s own,
unchanged job (verify_package_dict against the expected manifest
hash), on purpose: a wrong or corrupted fetch here is still refused
downstream, exactly as if a locally-baked file had been tampered with.
This module never imports LazyWorldLoader and world_loader.py never
imports this module - the mechanism (verify) and the seam (find bytes
to verify) stay independently testable.
"""
from __future__ import annotations

from pathlib import Path

from . import object_storage


def ensure_package_local(*, package_dir: Path, cache_dir: Path, key_prefix: str) -> Path:
    """Returns a directory load() can read package_dir/manifest.json from.

    If package_dir already has a manifest.json - baked into the image at
    build time, or already fetched by an earlier call in this same
    process's lifetime - it's returned unchanged, no object-storage call
    at all. This is the common case for every world that existed at the
    last deploy; WO-1 only changes behavior for a world installed (or
    repinned) since.

    Otherwise, if object storage is configured, the package is fetched
    into cache_dir/key_prefix and that path is returned instead.
    cache_dir is expected to be the persistent disk in a real deploy
    (CIC_API_PACKAGE_CACHE_DIR, defaulting under render.yaml's own
    /data mount) - a redeploy or restart does not lose the fetch, but a
    disk-less local/test run still works, it just re-fetches every
    process start.

    If object storage isn't configured either, package_dir is returned
    unchanged despite not existing - load()'s own "no manifest.json
    under {package_dir}" PackageRefused already says exactly what's
    wrong; duplicating that message here would be a second place for it
    to drift out of sync with the first."""
    if (package_dir / "manifest.json").is_file():
        return package_dir
    if not object_storage.is_configured():
        return package_dir
    local = cache_dir / key_prefix
    if not (local / "manifest.json").is_file():
        object_storage.download_package_dir(key_prefix, local)
    return local
