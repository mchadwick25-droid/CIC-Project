"""Lazy world-package loading (CiC-Program-Spec.md M4: "Worlds load lazily
per conversation"). Builds on engine.m2.loader_stub's hash-verification
contract unchanged - that module's own docstring names lazy loading, LRU
eviction, and mmap'd indexes as M4's job on top of it; this file adds the
lazy/resident/evict shape the stage-5 gate item ("lazy world load/unload
measured") asks for. Full LRU-under-memory-pressure is real multi-world
deployment behavior this build doesn't need to invent yet - the registry
has exactly one built world to load against right now, so what's provable
today is the mechanism (cold load reads and verifies from disk, a resident
world is a cache hit not a second read, unload actually evicts and a
later load is cold again), not eviction policy under real fleet load.
"""
import json
import time
from dataclasses import dataclass
from pathlib import Path

from engine.m2.loader_stub import PackageRefused, verify_package_dict

__all__ = ["LoadedWorld", "LoadTiming", "LazyWorldLoader", "PackageRefused"]


@dataclass(frozen=True)
class LoadedWorld:
    world_key: str
    manifest_hash: str
    prompt_text: str
    capsule_text: str
    repository: dict
    quotes: dict
    figures: dict
    coverage: dict
    frame: dict


@dataclass(frozen=True)
class LoadTiming:
    world_key: str
    cache_hit: bool
    seconds: float


class LazyWorldLoader:
    """One instance is the resident-worlds cache itself - the thing "lazy
    load/unload" measures the behavior of. Nothing is read from disk until
    load() is first called for a given world_key; a second load() for an
    already-resident world is a cache hit, not a second disk read/verify."""

    def __init__(self):
        self._resident: dict[str, LoadedWorld] = {}

    def is_resident(self, world_key: str) -> bool:
        return world_key in self._resident

    def load(self, world_key: str, *, package_dir: Path, expected_manifest_hash: str) -> tuple[LoadedWorld, LoadTiming]:
        start = time.perf_counter()
        cached = self._resident.get(world_key)
        if cached is not None:
            return cached, LoadTiming(world_key=world_key, cache_hit=True, seconds=time.perf_counter() - start)

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
        verify_package_dict(package, expected_manifest_hash)  # PackageRefused on any hash mismatch - refuse, don't serve wrong

        world = LoadedWorld(
            world_key=world_key,
            manifest_hash=expected_manifest_hash,
            prompt_text=package["compiled/prompt.txt"].decode("utf-8"),
            capsule_text=package["compiled/capsule.md"].decode("utf-8"),
            repository=json.loads(package["compiled/repository.json"]),
            quotes=json.loads(package["compiled/quotes.json"]),
            figures=json.loads(package["compiled/figures.json"]),
            coverage=json.loads(package["compiled/coverage.json"]),
            frame=json.loads(package["compiled/frame.json"]),
        )
        self._resident[world_key] = world
        return world, LoadTiming(world_key=world_key, cache_hit=False, seconds=time.perf_counter() - start)

    def unload(self, world_key: str) -> LoadTiming:
        start = time.perf_counter()
        self._resident.pop(world_key, None)
        return LoadTiming(world_key=world_key, cache_hit=False, seconds=time.perf_counter() - start)
