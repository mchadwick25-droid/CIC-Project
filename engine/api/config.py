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
    """Raised on a set-but-too-short CIC_API_ADMIN_TOKEN (2026-09-21,
    closing adversarial review of Tech-Readiness P1-Security). The route
    this token gates is now rate-limited (engine/api/ratelimit.py,
    ADMIN_LIMIT), but that limiter's whole job is making a short, weak
    token infeasible to brute-force in a reasonable time by slowing an
    attacker down - a token short enough to guess outright makes the
    limiter irrelevant, not redundant-but-safe. 32 chars is a floor, not
    a target: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
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
    # Anonymous per-visitor daily cap (Tech-Readiness P1-Security item 3,
    # 2026-09-21) - OFF by default everywhere, including a real deploy that
    # hasn't opted in yet. See engine.api.anon_cap's own module docstring:
    # the mechanism and the two numbers below are the PROPOSED default from
    # that package's report, not yet a decision Mark has made. Flipping
    # this on with no secret set is a hard failure (below), not a silent
    # skip - same "never guess" posture as region/admin_token above.
    anon_cap_enabled: bool
    anon_visitor_secret: str | None
    anon_daily_session_limit: int
    anon_daily_turn_limit: int
    # R27 build item 5 (Decision-Log.md Entry 56/Rulings-Pending.md R36,
    # 2026-09-23): OFF by default, everywhere, including a real deploy -
    # Mark flips this after his own staging look at item 5's own live
    # battery (the reviewer thread's own explicit instruction: "stop for
    # Mark's staging look before the flag is flipped anywhere"). When on,
    # a wholly_uncited_paragraph or neighbour_named offense regenerates
    # once, then hands the turn to the Facilitator if it survives that -
    # see engine.m4.turn._run_ordinary_voice_turn's own docstring for the
    # full shape. inherited_ungrounded stays report-only regardless of
    # this flag (R36's own scope decision, not something this flag
    # widens).
    r27_enforce: bool

    # R38 (Rulings-Pending.md, RULED 2026-09-23) - self-revision at
    # generation on other_tradition-routed turns, unconditional unlike
    # r27_enforce above (this is generation, not enforcement: no
    # withhold, no Facilitator, no flag-gated staging rollout needed
    # before it can run for real). Default ON - the kill-switch exists
    # for cost or incident use only, the opposite default sense from
    # r27_enforce/CIC_R27_ENFORCE, since Mark's own ruling is to ship
    # this, not stage it behind an off-by-default flag.
    self_revision_enabled: bool

    # Stage 7b (Decision-Log.md Entry 53, "Shape B"): the engine's own
    # sentence-buffered streaming module (engine.m4.streaming). OFF by
    # default, everywhere, same staging discipline as r27_enforce above -
    # "flag-gated, default off, flipped only after Mark's own staging
    # look." Streaming does not ship to participants before R27-A's own
    # enforcement is on (Decision-Log Entry 54/62) - CIC_R27_ENFORCE is
    # itself off today by ruling (R42), so this flag has no live
    # deployment path yet regardless of its own value; it exists so the
    # module can be built and tested against a real setting rather than
    # a hypothetical one.
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
            streaming_enabled=os.environ.get("CIC_API_STREAMING", "") in ("1", "true", "yes"),
        )
