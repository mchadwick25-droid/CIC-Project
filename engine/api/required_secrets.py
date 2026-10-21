"""The secrets each switch needs before the engine will start, in one list.

Three readers share it:
- the production start-up (engine.api.app._build_real_app) refuses to start
  with every missing secret named in one message, not one per deploy;
- engine/api/tests/test_required_secrets.py fails when render.yaml turns a
  switch on without declaring the secrets that switch needs;
- `python -m engine.api.required_secrets --service cic-engine` prints the
  hand-set values to confirm in the Render dashboard.

A secret is a value render.yaml marks `sync: false`: it is typed into the
Render dashboard by hand and never committed. Declaring it in render.yaml
does not give it a value.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ON_VALUES = ("1", "true", "yes")
MIN_KEY_LENGTH = 32


@dataclass(frozen=True)
class Need:
    name: str
    min_length: int = 1
    # True when `name` is a switch that must itself be on, not a secret.
    switch: bool = False


@dataclass(frozen=True)
class Problem:
    name: str
    because: str

    def __str__(self) -> str:
        return f"{self.name} ({self.because})"


# switch -> what it needs while on. Mirrors the refusals already raised by
# engine.api.app.create_app (MissingAnonCapSecret) and
# engine.api.deeper_routes.build_runtime (DeeperConfigError).
NEEDS: dict[str, tuple[Need, ...]] = {
    "CIC_API_ANON_CAP_ENABLED": (Need("CIC_API_ANON_VISITOR_SECRET"),),
    "CIC_DEEPER_ENABLED": (
        Need("CIC_DEEPER_WEBHOOK_SECRET"),
        Need("CIC_DEEPER_FREE_KEY", min_length=MIN_KEY_LENGTH),
        Need("CIC_API_ANON_CAP_ENABLED", switch=True),
    ),
}

# Needed on Render whatever the switches say: start-up looks the models up on
# Bedrock with these. Not part of check(), because off Render the same
# credentials can come from any source in botocore's chain.
ALWAYS_ON_RENDER = ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")

# Optional values that refuse start-up when set too short.
MIN_LENGTH_IF_SET: dict[str, int] = {"CIC_API_ADMIN_TOKEN": MIN_KEY_LENGTH}


class MissingSecrets(Exception):
    def __init__(self, problems: list[Problem]):
        self.problems = problems
        super().__init__(
            "refusing to start; set these in the Render dashboard (Settings -> Environment): "
            + "; ".join(str(p) for p in problems)
        )


def is_on(value: str | None) -> bool:
    return (value or "") in ON_VALUES


def problems_in(env: dict) -> list[Problem]:
    """Every start-up refusal the environment would trigger, all at once."""
    problems: list[Problem] = []
    for switch, needs in NEEDS.items():
        if not is_on(env.get(switch)):
            continue
        for need in needs:
            value = env.get(need.name)
            if need.switch:
                if not is_on(value):
                    problems.append(Problem(need.name, f"must be on (1, true or yes) while {switch} is on"))
            elif not value:
                problems.append(Problem(need.name, f"unset; {switch} is on"))
            elif len(value) < need.min_length:
                problems.append(Problem(need.name, f"shorter than {need.min_length} characters; {switch} is on"))
    for name, min_length in MIN_LENGTH_IF_SET.items():
        value = env.get(name)
        if value and len(value) < min_length:
            problems.append(Problem(name, f"set but shorter than {min_length} characters"))
    return problems


def check(env: dict) -> None:
    if problems := problems_in(env):
        raise MissingSecrets(problems)


def service_env(render_yaml: Path, service: str) -> list[dict]:
    blueprint = yaml.safe_load(render_yaml.read_text())
    for entry in blueprint.get("services", []):
        if entry.get("name") == service:
            return entry.get("envVars", [])
    raise KeyError(f"no service named {service!r} in {render_yaml}")


def declared_gaps(env_vars: list[dict]) -> list[Problem]:
    """What render.yaml itself gets wrong for one service: a switch it turns
    on, with a needed secret it never declares or a needed switch it leaves
    off."""
    values = {v["key"]: v.get("value") for v in env_vars if "value" in v}
    hand_set = {v["key"] for v in env_vars if v.get("sync") is False}
    gaps: list[Problem] = []
    for switch, needs in NEEDS.items():
        if not is_on(values.get(switch)):
            continue
        for need in needs:
            if need.switch:
                if not is_on(values.get(need.name)):
                    gaps.append(Problem(need.name, f"render.yaml leaves it off while {switch} is on"))
            elif need.name not in hand_set:
                gaps.append(Problem(need.name, f"not declared sync: false while {switch} is on"))
    return gaps


def checklist(env_vars: list[dict]) -> tuple[list[str], list[str]]:
    """(needed to start, other hand-set values) for one service."""
    values = {v["key"]: v.get("value") for v in env_vars if "value" in v}
    hand_set = [v["key"] for v in env_vars if v.get("sync") is False]
    needed = set(ALWAYS_ON_RENDER) | {
        need.name
        for switch, needs in NEEDS.items() if is_on(values.get(switch))
        for need in needs if not need.switch
    }
    return [k for k in hand_set if k in needed], [k for k in hand_set if k not in needed]


def _cli(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.api.required_secrets")
    parser.add_argument("--service", required=True, help="a service name in render.yaml, e.g. cic-engine")
    parser.add_argument("--render-yaml", default=str(Path(__file__).resolve().parents[2] / "render.yaml"))
    args = parser.parse_args(argv)
    env_vars = service_env(Path(args.render_yaml), args.service)
    gaps = declared_gaps(env_vars)
    needed, other = checklist(env_vars)
    print(f"{args.service}: confirm each value is set in Render -> {args.service} -> Environment.")
    print("Needed to start (the deploy fails without them):")
    for key in needed:
        print(f"  [ ] {key}")
    print("Other hand-set values (the engine starts without them):")
    for key in other:
        print(f"  [ ] {key}")
    if gaps:
        print("render.yaml itself is wrong:")
        for gap in gaps:
            print(f"  {gap}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
