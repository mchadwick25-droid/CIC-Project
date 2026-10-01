"""Password login for the usage dashboard. CIC_API_ADMIN_TOKEN's
bearer-token pattern is built for script and API callers, not as a human
login, so this module adds a second, human-facing credential without
touching that first one: CIC_API_ADMIN_TOKEN still works exactly
as before for a direct API caller (pilot-summary, usage-summary), and now
also serves as the one-time bootstrap credential for setting this
password - see engine.api.app's /api/admin/set-password and
/api/admin/login.

Why a password here can be short (12-20 chars) where CIC_API_ADMIN_TOKEN
needed 32+ (engine.api.config.WeakAdminTokenError): that token is the
ONLY control on its route, checked at engine.api.ratelimit.ADMIN_LIMIT's
loose 10/min - fine for an operator polling an API, not remotely tight
enough to make a short secret safe against a patient guesser. The login
route this module backs gets its own much stricter limiter
(engine.api.ratelimit.ADMIN_LOGIN_LIMIT, 5/15min) precisely so the
password doesn't have to carry that same weight alone - the real defense
here is the lockout, the same way an ordinary website's login works,
not the string's raw entropy.
"""
import hashlib
import hmac
import json
import secrets
import string
import time
from dataclasses import dataclass
from pathlib import Path

PASSWORD_MIN_LENGTH = 12
PASSWORD_MAX_LENGTH = 20
_PBKDF2_ITERATIONS = 600_000  # OWASP's current floor for PBKDF2-HMAC-SHA256 (2023+ guidance)
_SALT_BYTES = 16
_SYMBOLS = set(string.punctuation)

SESSION_COOKIE_NAME = "cic_admin_session"
_SESSION_SEPARATOR = "."
DEFAULT_SESSION_TTL_SECONDS = 60 * 60 * 12  # 12 hours - long enough for one sitting, short enough that a stolen cookie doesn't stay valid indefinitely


class PasswordPolicyError(ValueError):
    """Raised with a plain, specific reason - which rule failed, not just
    'invalid password' - so the dashboard's own client-side check and the
    server's check give the same answer for the same input."""


def validate_password_policy(password: str) -> None:
    if not (PASSWORD_MIN_LENGTH <= len(password) <= PASSWORD_MAX_LENGTH):
        raise PasswordPolicyError(f"password must be {PASSWORD_MIN_LENGTH}-{PASSWORD_MAX_LENGTH} characters, got {len(password)}")
    if not any(c.isupper() for c in password):
        raise PasswordPolicyError("password must contain at least one uppercase letter")
    if not any(c.isdigit() for c in password):
        raise PasswordPolicyError("password must contain at least one number")
    if not any(c in _SYMBOLS for c in password):
        raise PasswordPolicyError("password must contain at least one symbol")


def hash_password(password: str) -> str:
    """Self-describing format (algorithm$iterations$salt$hash, the same
    shape Django's password hashers use) so a future change in iteration
    count or algorithm doesn't invalidate passwords hashed under the old
    one - verify_password reads the parameters back out of the stored
    string rather than assuming today's constants."""
    salt = secrets.token_hex(_SALT_BYTES)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), _PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${_PBKDF2_ITERATIONS}${salt}${digest.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        algorithm, iterations_s, salt, expected_hex = stored_hash.split("$")
        if algorithm != "pbkdf2_sha256":
            return False
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), int(iterations_s))
        return hmac.compare_digest(digest.hex(), expected_hex)
    except (ValueError, TypeError):
        # Malformed stored_hash (corrupt file, wrong format) fails closed,
        # same as anon_cap.verify_token's own "never trust an unparseable
        # credential" rule - never raises past this function.
        return False


@dataclass(frozen=True)
class AdminAuthStore:
    """One small JSON file on the same persistent disk events.db/usage.db
    already live on (Path(settings.events_db_path).parent) - the same
    "one file, one job" pattern engine.m7.scheduler's last_run.json
    already uses, not a new database for one field."""

    path: Path

    def read_password_hash(self) -> str | None:
        if not self.path.exists():
            return None
        try:
            return json.loads(self.path.read_text()).get("password_hash")
        except (OSError, ValueError):
            return None

    def write_password_hash(self, password_hash: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"password_hash": password_hash}, indent=2) + "\n")


def issue_session_token(secret: str, ttl_seconds: int = DEFAULT_SESSION_TTL_SECONDS) -> str:
    """A stateless, self-verifying token - same shape as
    engine.api.anon_cap's issue_token/verify_token, so a session needs no
    server-side store of its own (nothing to clean up, nothing to lose on
    restart - a restart just means every session re-logs-in, the same
    accepted tradeoff anon_cap's own daily counters already make)."""
    expires_at = str(int(time.time()) + ttl_seconds)
    signature = hmac.new(secret.encode(), expires_at.encode(), "sha256").hexdigest()
    return f"{expires_at}{_SESSION_SEPARATOR}{signature}"


def verify_session_token(token: str | None, secret: str) -> bool:
    if not token or _SESSION_SEPARATOR not in token:
        return False
    expires_at, _, signature = token.partition(_SESSION_SEPARATOR)
    if not expires_at or not signature:
        return False
    expected = hmac.new(secret.encode(), expires_at.encode(), "sha256").hexdigest()
    if not hmac.compare_digest(expected, signature):
        return False
    try:
        return int(expires_at) > time.time()
    except ValueError:
        return False
