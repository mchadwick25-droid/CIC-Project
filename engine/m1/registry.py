"""The ONE world registry (Artifact-1 SS2): records/worlds/<code>.yaml, one
file per world. No world identifier belongs anywhere else in code or config
(spec principle 4) - this module is the sole reader.

Split from a single records/worlds.yaml into this directory (Library Access
Gate D3 SS6.4/SS7 increment 1) to retire records/worlds.yaml as a cross-branch
merge-conflict point - two worlds' registry commits no longer touch the same
file. A world's file is named by its registry code (the old top-level key)
and holds that world's entry directly, with no wrapping "worlds:"/"<code>:"
keys - the filename already is the key.
"""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_DIR = REPO_ROOT / "records" / "worlds"


def load_registry(path: Path = REGISTRY_DIR) -> dict:
    registry = {}
    for world_file in sorted(path.glob("*.yaml")):
        with open(world_file, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        registry[world_file.stem] = data
    return registry


def get_world(world_key: str, registry: dict | None = None) -> dict:
    registry = registry if registry is not None else load_registry()
    if world_key not in registry:
        raise KeyError(f"world_key {world_key!r} is not in the registry (records/worlds/{world_key}.yaml)")
    return registry[world_key]


def world_keys(registry: dict | None = None) -> list[str]:
    registry = registry if registry is not None else load_registry()
    return sorted(registry.keys())


# A world's kind, not its state. `state` tracks how far a world has come
# (built -> admitted -> open); `kind` says whether it is a formation world
# at all. The fixture is the harness's own negative control - synthetic,
# seeded with the defects the gates must catch (spec stage 0.6) - and it
# was being counted and reported beside the six real worlds, which is how
# "seven worlds" kept appearing in output that should have said six.
KIND_FIXTURE = "fixture"
KIND_FORMATION = "formation"


def kind_of(entry: dict) -> str:
    return entry.get("kind", KIND_FORMATION)


def is_fixture(entry: dict) -> bool:
    return kind_of(entry) == KIND_FIXTURE


# States a world reaches once it has a compiled package. A world registered at
# the Library handoff (state: candidate) has an entry and no package yet.
BUILT_STATES = frozenset({"built", "admitted", "open"})


def is_built(entry: dict) -> bool:
    return entry.get("state") in BUILT_STATES


def formation_world_keys(registry: dict | None = None) -> list[str]:
    """The worlds a participant could ever speak to: formation worlds that
    have a compiled package. Everything that lists, counts or reports worlds
    should use this; build and test paths that need the fixture, or a world
    still at the Library stage, ask for it by name."""
    registry = registry if registry is not None else load_registry()
    return sorted(k for k, v in registry.items() if not is_fixture(v) and is_built(v))


# The project lead sets this yes/no field on a world's registry entry at the
# Library handoff: True when the Representative's material sits near
# self-harm, abuse, or another safety-sensitive subject. The full-validation
# trigger reads it. Only a YAML boolean counts.
SAFETY_ADJACENT_KEY = "safety_adjacent"


def safety_adjacent(entry: dict | None) -> bool | None:
    """The entry's safety_adjacent value, or None when it is absent or not a boolean."""
    value = (entry or {}).get(SAFETY_ADJACENT_KEY)
    return value if isinstance(value, bool) else None
