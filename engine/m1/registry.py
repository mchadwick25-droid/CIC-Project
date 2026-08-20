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
