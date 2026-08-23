"""The ONE world registry (Artifact-1 SS2): records/worlds.yaml. No world
identifier belongs anywhere else in code or config (spec principle 4) - this
module is the sole reader.
"""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "records" / "worlds.yaml"


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("worlds", {})


def get_world(world_key: str, registry: dict | None = None) -> dict:
    registry = registry if registry is not None else load_registry()
    if world_key not in registry:
        raise KeyError(f"world_key {world_key!r} is not in the registry (records/worlds.yaml)")
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


def formation_world_keys(registry: dict | None = None) -> list[str]:
    """The worlds a participant could ever speak to. Everything that lists,
    counts or reports worlds should use this; build and test paths that
    need the fixture ask for it by name."""
    registry = registry if registry is not None else load_registry()
    return sorted(k for k, v in registry.items() if not is_fixture(v))
