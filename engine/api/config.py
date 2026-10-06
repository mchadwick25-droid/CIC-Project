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
_DEFAULT_ANON_DAILY_SESSION_LIMIT = 5
_DEFAULT_ANON_DAILY_TURN_LIMIT = 150


class MissingConfigError(Exception):
    """Raised on a required env var that's absent - never silently defaulted."""


class WeakAdminTokenError(Exception):
    """Raised on a set-but-too-short CIC_API_ADMIN_TOKEN. The route this
    token gates is rate-limited (engine/api/ratelimit.py, ADMIN_LIMIT),
    but that limiter's whole job is making a short, weak token infeasible
    to brute-force in a reasonable time by slowing an attacker down - a
    token short enough to guess outright makes the limiter irrelevant, not
    redundant-but-safe. 32 chars is a floor, not a target:
    `python -c "import secrets; print(secrets.token_urlsafe(32))"`
    comfortably clears it."""


_MIN_ADMIN_TOKEN_LENGTH = 32


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
    # THE ADMISSION GATE: a world "becomes selectable when it passes
    # Admission." This flag is when that gate BITES: only admitted/open
    # worlds are listed or seated, interview and table alike. The code
    # default stays off (local dev and tests construct their own stages),
    # but the deployed value is "1": the doors are open, and render.yaml
    # carries that value.
    enforce_admission: bool
    # Gates /api/admin/pilot-summary. None (unset) disables the route
    # entirely rather than defaulting to some guessed secret; a real
    # deploy sets its own random value in the Render dashboard, same
    # sync: false pattern as the AWS keys - never committed here.
    admin_token: str | None
    # Idle-world unload: None keeps every resident world cached for the
    # process's lifetime - LazyWorldLoader's own long-standing default,
    # unchanged unless a deploy opts in. See that class's own docstring
    # for why this is a plain idle timeout rather than full
    # LRU-under-memory-pressure.
    world_idle_unload_seconds: float | None
    # Where to cache a package object storage had to fetch, so a
    # redeploy/restart doesn't re-fetch it. Object storage itself (bucket,
    # endpoint, credentials) is read directly from env vars by
    # engine.m4.object_storage, not carried on Settings - that module
    # already fails loudly if CIC_API_PACKAGE_BUCKET is set without its
    # endpoint/keys, the same "never guess, fail loudly" rule region
    # already follows above, so duplicating those fields here would just
    # be a second place for them to drift.
    package_cache_dir: Path
    # Anonymous per-visitor daily cap - code default OFF (a fresh/local/
    # test app opts in explicitly), but both real deploys turn it on
    # (render.yaml). See engine.api.anon_cap's own module docstring: the
    # cap numbers below are still the PROPOSED default, not independently
    # re-tuned as part of Mark's on/off decision. Flipping this on with no
    # secret set is a hard failure (below), not a silent skip - same
    # "never guess" posture as region/admin_token above.
    anon_cap_enabled: bool
    anon_visitor_secret: str | None
    anon_daily_session_limit: int
    anon_daily_turn_limit: int
    # Off by default. When on, a wholly_uncited_paragraph or
    # neighbour_named offense regenerates once, then hands the turn to
    # the Facilitator if it survives that - see
    # engine.m4.turn._run_ordinary_voice_turn's own docstring for the
    # full shape. inherited_ungrounded stays report-only regardless of
    # this flag.
    r27_enforce: bool

    # Self-revision at generation on other_tradition-routed turns.
    # Default on; the kill-switch exists for cost or incident use only.
    # Unlike the enforcement flag above, this is generation, not enforcement - no
    # withhold, no Facilitator handoff.
    self_revision_enabled: bool

    # Verified citation attachment after each voice turn (engine.m4.
    # citation_attach): adds a citation to an uncited claim sentence only
    # when a check call confirms the record carries it; never changes text.
    # Default off.
    citation_attach_enabled: bool

    # The anonymous quality-control store (engine.m7.qc_store): a separate
    # SQLite file, sharing no key with the event log or the usage log.
    qc_db_path: str

    # Lets a client that asks for an event stream (Accept: text/event-stream)
    # read a reply, an interview's or a Table seat's, sentence by sentence while it is written
    # (engine.api.app._stream_turn). Off by default.
    streaming_enabled: bool

    @classmethod
    def from_env(cls) -> "Settings":
        region = os.environ.get("CIC_API_REGION")
        if not region:
            raise MissingConfigError(
                "CIC_API_REGION is required and has no default - never guess a Bedrock region "
                "(same rule every other live script in this repo follows)"
            )
        worlds_yaml_path = Path(os.environ.get("CIC_API_WORLDS_YAML", str(REPO_ROOT / "records" / "worlds")))
        admin_token = os.environ.get("CIC_API_ADMIN_TOKEN") or None
        if admin_token is not None and len(admin_token) < _MIN_ADMIN_TOKEN_LENGTH:
            raise WeakAdminTokenError(
                f"CIC_API_ADMIN_TOKEN is set but only {len(admin_token)} chars - "
                f"needs at least {_MIN_ADMIN_TOKEN_LENGTH} (e.g. secrets.token_urlsafe(32))"
            )
        return cls(
            region=region,
            voice_model_pattern=os.environ.get("CIC_API_VOICE_MODEL_PATTERN", _DEFAULT_VOICE_MODEL_PATTERN),
            safety_model_pattern=os.environ.get("CIC_API_SAFETY_MODEL_PATTERN", _DEFAULT_SAFETY_MODEL_PATTERN),
            events_db_path=os.environ.get("CIC_API_EVENTS_DB", _DEFAULT_EVENTS_DB),
            usage_db_path=os.environ.get("CIC_API_USAGE_DB", _DEFAULT_USAGE_DB),
            worlds_yaml_path=worlds_yaml_path,
            default_world_key=os.environ.get("CIC_API_DEFAULT_WORLD_KEY", _DEFAULT_WORLD_KEY),
            enforce_admission=os.environ.get("CIC_ENFORCE_ADMISSION", "") in ("1", "true", "yes"),
            admin_token=admin_token,
            world_idle_unload_seconds=_float_or_none(os.environ.get("CIC_API_WORLD_IDLE_UNLOAD_SECONDS")),
            package_cache_dir=Path(os.environ.get("CIC_API_PACKAGE_CACHE_DIR", str(REPO_ROOT / "packages"))),
            anon_cap_enabled=os.environ.get("CIC_API_ANON_CAP_ENABLED", "") in ("1", "true", "yes"),
            anon_visitor_secret=os.environ.get("CIC_API_ANON_VISITOR_SECRET") or None,
            anon_daily_session_limit=int(
                os.environ.get("CIC_API_ANON_DAILY_SESSION_LIMIT", _DEFAULT_ANON_DAILY_SESSION_LIMIT)
            ),
            anon_daily_turn_limit=int(os.environ.get("CIC_API_ANON_DAILY_TURN_LIMIT", _DEFAULT_ANON_DAILY_TURN_LIMIT)),
            r27_enforce=os.environ.get("CIC_R27_ENFORCE", "") in ("1", "true", "yes"),
            self_revision_enabled=os.environ.get("CIC_SELF_REVISION", "1") not in ("0", "false", "no"),
            citation_attach_enabled=os.environ.get("CIC_CITATION_ATTACH", "") in ("1", "true", "yes"),
            qc_db_path=os.environ.get("CIC_API_QC_DB", "./cic_api_qc.db"),
            streaming_enabled=os.environ.get("CIC_API_STREAMING", "") in ("1", "true", "yes"),
        )
