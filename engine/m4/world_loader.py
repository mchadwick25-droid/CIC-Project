"""Lazy world-package loading (CiC-Program-Spec.md M4: "Worlds load lazily
per conversation"). Builds on engine.m2.loader_stub's hash-verification
contract unchanged - that module's own docstring names lazy loading, LRU
eviction, and mmap'd indexes as M4's job on top of it; this file adds the
lazy/resident/evict shape the stage-5 gate item ("lazy world load/unload
measured") asks for.

Idle-unload policy (WO-2): at this class's birth the registry
had exactly one built world, so what mattered was proving the mechanism
(cold load reads and verifies from disk, a resident world is a cache hit
not a second read, unload actually evicts and a later load is cold
again) - "full LRU-under-memory-pressure" was deliberately left as real
multi-world deployment behavior the build didn't need to invent yet.
Nine worlds are registered now, so a real deploy carries a real idle
policy: `max_idle_seconds` on `__init__`. Still deliberately not full
LRU-under-memory-pressure - that needs load data this deploy doesn't
have yet (how many worlds are actually touched per hour, real package
sizes in memory) and would be tuning a number nobody has measured
against. A simple idle timeout is the honest amount of policy to add
until that data exists.
"""
import json
import time
from dataclasses import dataclass
from pathlib import Path

from engine.m2.loader_stub import PackageRefused, verify_package_dict
from engine.m10.deployed import assert_compiled_target

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

    def __init__(self, *, max_idle_seconds: float | None = None):
        # max_idle_seconds (WO-2): None keeps every resident
        # world cached for the process's lifetime, the behavior this class
        # always had - the code default stays off, same posture as
        # enforce_admission and admin_token in engine/api/config.py. A real
        # deploy sets CIC_API_WORLD_IDLE_UNLOAD_SECONDS once there is more
        # than one world worth evicting under - at this class's own birth
        # the registry had exactly one built world, so an idle policy had
        # nothing real to act on yet; nine do now. Eviction runs
        # opportunistically from load() (see _evict_idle below) rather than
        # a background thread - unlike engine/m4/idle_close.py's session
        # sweep, which has to fire even with zero traffic (a session can go
        # idle while nobody calls anything), a resident world can only grow
        # stale while something keeps calling load() - the same traffic
        # that already triggers this check for free.
        self._max_idle_seconds = max_idle_seconds
        self._last_accessed: dict[tuple[str, str], float] = {}
        # Keyed by (world_key, expected_manifest_hash), not world_key alone -
        # found live: a bare world_key key means a resident
        # world is returned on ANY later load() for that key regardless of
        # the hash asked for, so a repin lands one of two ways depending on
        # accident of timing - a process that never restarts keeps serving
        # the pre-repin bytes to every session including brand-new ones
        # (silently, since a cache hit skipped verify_package_dict
        # entirely), while a process that does restart between turns loses
        # the cache and reloads against the registry's now-current (post-
        # repin) location/hash, which then refuses every in-flight session
        # still expecting the old hash (PackageRefused -> 503, "world
        # temporarily unavailable"). Neither is what Artifact-2's own
        # promise describes ("open worlds swap by registry pointer, old
        # package retained for rollback"): that promise means the OLD and
        # NEW manifest hashes are both valid, concurrently, for as long as
        # any session is still pinned to the old one - which requires both
        # to be independently resident and independently verified, not one
        # cache slot per world_key. Paired with wiring.py's package_dir
        # override (session-pinned, not registry-current) so an old
        # in-flight session's load() call asks for its own hash against its
        # own still-on-disk directory (old packages are never deleted - see
        # Artifact-2 SS2) and a new session's load() call asks for the
        # current one; both cache under their own key.
        self._resident: dict[tuple[str, str], LoadedWorld] = {}

    def is_resident(self, world_key: str) -> bool:
        return any(k[0] == world_key for k in self._resident)

    def load(self, world_key: str, *, package_dir: Path, expected_manifest_hash: str) -> tuple[LoadedWorld, LoadTiming]:
        if self._max_idle_seconds is not None:
            self._evict_idle()
        start = time.perf_counter()
        cache_key = (world_key, expected_manifest_hash)
        cached = self._resident.get(cache_key)
        if cached is not None:
            self._last_accessed[cache_key] = time.monotonic()
            return cached, LoadTiming(world_key=world_key, cache_hit=True, seconds=time.perf_counter() - start)

        assert_compiled_target(package_dir / "compiled" / "prompt.txt")
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
        self._resident[cache_key] = world
        self._last_accessed[cache_key] = time.monotonic()
        return world, LoadTiming(world_key=world_key, cache_hit=False, seconds=time.perf_counter() - start)

    def unload(self, world_key: str) -> LoadTiming:
        # Evicts every hash-variant resident for this world_key - callers
        # unload by world identity, not by a specific pin.
        start = time.perf_counter()
        for key in [k for k in self._resident if k[0] == world_key]:
            del self._resident[key]
            self._last_accessed.pop(key, None)
        return LoadTiming(world_key=world_key, cache_hit=False, seconds=time.perf_counter() - start)

    def _evict_idle(self) -> list[str]:
        """Unloads every resident (world_key, hash) pin last accessed more
        than max_idle_seconds ago. Called from load() itself, not a
        background thread (see __init__'s own note on why that's enough
        here) - so the actual eviction moment is "the next time someone
        asks to load anything", not exactly max_idle_seconds after the
        fact. Returns the evicted world_keys, for a caller that wants to
        log what happened; LoadTiming has no field for "why a load was
        briefly a cold load" so this stays a separate, optional return
        rather than overloading that dataclass."""
        now = time.monotonic()
        stale = [k for k, last in self._last_accessed.items() if now - last > self._max_idle_seconds]
        for key in stale:
            del self._resident[key]
            del self._last_accessed[key]
        return [k[0] for k in stale]
