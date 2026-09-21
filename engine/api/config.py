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


def _float_or_none(raw: str | None) -> float | None:
    if not raw:
        return None
    return float(raw)


@dataclass(frozen=True)
class Settings:
    region: str
    voice_model_pattern: str
    safety_model_pattern: str
    events_db_path: str
    usage_db_path: str
    worlds_yaml_path: Path
    default_world_key: str
    # THE ADMISSION GATE (stage-10 enforcement; 2026-08-28). The spec is
    # plain - a world "becomes selectable when it passes Admission" - and
    # the 2026-08-26 audit's headline finding was that the running engine
    # never checked: create_session served any `built` world. The gate now
    # exists; this flag is when it BITES: only admitted/open worlds are
    # listed or seated, interview and table alike. The code default stays
    # off (local dev and tests construct their own stages), but the
    # DEPLOYED value is "1": the doors are open,
    # the same day all six worlds were admitted - render.yaml carries the
    # flip and its record; the
    # declared deferral this flag was born with is ended.
    enforce_admission: bool
    # Gates /api/admin/pilot-summary (2026-09-05: "how many pilot
    # id/transcripts have been generated" had no answer from outside the
    # service - no admin surface existed at all). None (unset) disables the
    # route entirely rather than defaulting to some guessed secret; a real
    # deploy sets its own random value in the Render dashboard, same
    # sync: false pattern as the AWS keys - never committed here.
    admin_token: str | None
    # WO-2 idle-world unload (2026-09-16): None keeps every resident world
    # cached for the process's lifetime - LazyWorldLoader's own long-
    # standing default, unchanged unless a deploy opts in. See that
    # class's own docstring for why this is a plain idle timeout rather
    # than full LRU-under-memory-pressure.
    world_idle_unload_seconds: float | None
    # WO-1 (2026-09-16): where to cache a package object storage had to
    # fetch, so a redeploy/restart doesn't re-fetch it. Object storage
    # itself (bucket, endpoint, credentials) is read directly from env
    # vars by engine.m4.object_storage, not carried on Settings - that
    # module already fails loudly if CIC_API_PACKAGE_BUCKET is set
    # without its endpoint/keys, the same "never guess, fail loudly"
    # rule region already follows above, so duplicating those fields
    # here would just be a second place for them to drift.
    package_cache_dir: Path

    @classmethod
    def from_env(cls) -> "Settings":
        region = os.environ.get("CIC_API_REGION")
        if not region:
            raise MissingConfigError(
                "CIC_API_REGION is required and has no default - never guess a Bedrock region "
                "(same rule every other live script in this repo follows)"
            )
        worlds_yaml_path = Path(os.environ.get("CIC_API_WORLDS_YAML", str(REPO_ROOT / "records" / "worlds")))
        return cls(
            region=region,
            voice_model_pattern=os.environ.get("CIC_API_VOICE_MODEL_PATTERN", _DEFAULT_VOICE_MODEL_PATTERN),
            safety_model_pattern=os.environ.get("CIC_API_SAFETY_MODEL_PATTERN", _DEFAULT_SAFETY_MODEL_PATTERN),
            events_db_path=os.environ.get("CIC_API_EVENTS_DB", _DEFAULT_EVENTS_DB),
            usage_db_path=os.environ.get("CIC_API_USAGE_DB", _DEFAULT_USAGE_DB),
            worlds_yaml_path=worlds_yaml_path,
            default_world_key=os.environ.get("CIC_API_DEFAULT_WORLD_KEY", _DEFAULT_WORLD_KEY),
            enforce_admission=os.environ.get("CIC_ENFORCE_ADMISSION", "") in ("1", "true", "yes"),
            admin_token=os.environ.get("CIC_API_ADMIN_TOKEN") or None,
            world_idle_unload_seconds=_float_or_none(os.environ.get("CIC_API_WORLD_IDLE_UNLOAD_SECONDS")),
            package_cache_dir=Path(os.environ.get("CIC_API_PACKAGE_CACHE_DIR", str(REPO_ROOT / "packages"))),
        )
