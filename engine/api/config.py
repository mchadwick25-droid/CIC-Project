"""Minimal test-backend config (see /root/.claude/plans/linear-popping-dawn.md).
Env-var-driven, fails loudly on a missing region rather than guessing one -
same discipline as every other --region-required script in this repo
(engine/provider/preflight.py, engine/m4/live_turn_run.py,
engine/m5/safety_script_run.py). AWS credentials themselves are never read
here - engine.provider.bedrock.make_client() already falls through boto3's
standard credential chain; this module only needs to know which region.
"""
import os
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

_DEFAULT_VOICE_MODEL_PATTERN = "us.anthropic.claude-sonnet-4-5"
_DEFAULT_SAFETY_MODEL_PATTERN = "us.anthropic.claude-haiku-4-5"
_DEFAULT_EVENTS_DB = "./cic_api_events.db"
_DEFAULT_USAGE_DB = "./cic_api_usage.db"
_DEFAULT_WORLD_KEY = "fix"


class MissingConfigError(Exception):
    """Raised on a required env var that's absent - never silently defaulted."""


@dataclass(frozen=True)
class Settings:
    region: str
    voice_model_pattern: str
    safety_model_pattern: str
    events_db_path: str
    usage_db_path: str
    worlds_yaml_path: Path
    default_world_key: str

    @classmethod
    def from_env(cls) -> "Settings":
        region = os.environ.get("CIC_API_REGION")
        if not region:
            raise MissingConfigError(
                "CIC_API_REGION is required and has no default - never guess a Bedrock region "
                "(same rule every other live script in this repo follows)"
            )
        worlds_yaml_path = Path(os.environ.get("CIC_API_WORLDS_YAML", str(REPO_ROOT / "records" / "worlds.yaml")))
        return cls(
            region=region,
            voice_model_pattern=os.environ.get("CIC_API_VOICE_MODEL_PATTERN", _DEFAULT_VOICE_MODEL_PATTERN),
            safety_model_pattern=os.environ.get("CIC_API_SAFETY_MODEL_PATTERN", _DEFAULT_SAFETY_MODEL_PATTERN),
            events_db_path=os.environ.get("CIC_API_EVENTS_DB", _DEFAULT_EVENTS_DB),
            usage_db_path=os.environ.get("CIC_API_USAGE_DB", _DEFAULT_USAGE_DB),
            worlds_yaml_path=worlds_yaml_path,
            default_world_key=os.environ.get("CIC_API_DEFAULT_WORLD_KEY", _DEFAULT_WORLD_KEY),
        )
