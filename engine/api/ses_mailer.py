"""Amazon SES as the sign-in mail provider.

Implements the accounts `Mailer`: one plain-text message per send, to one
address, through SES's send-email call. Nothing else is configured on the
account side: no configuration set, so no open or click tracking and no event
destination; no message archive. The address and the code are used for the send
and are never logged, and a provider fault is re-raised without the provider's
own text, which can name the recipient.

The SES credentials are this module's own (CIC_ACCOUNTS_SES_*), never botocore's
default chain, so the key that reaches Bedrock cannot send mail and the mail key
can do nothing but send. What the messages say lives in an approved words file,
not here; with no such file the app refuses to start rather than send words
nobody approved.
"""
import re
import string
from dataclasses import dataclass
from pathlib import Path

import yaml

ENV_FROM = "CIC_ACCOUNTS_SES_FROM"
ENV_REGION = "CIC_ACCOUNTS_SES_REGION"
ENV_ACCESS_KEY = "CIC_ACCOUNTS_SES_ACCESS_KEY_ID"
ENV_SECRET_KEY = "CIC_ACCOUNTS_SES_SECRET_ACCESS_KEY"
ENV_WORDS = "CIC_ACCOUNTS_MAIL_WORDS"
DEFAULT_WORDS_PATH = Path(__file__).resolve().parent / "ops" / "accounts-mail.yaml"

_ENV_NAMES = (ENV_FROM, ENV_REGION, ENV_ACCESS_KEY, ENV_SECRET_KEY)
_ADDRESS = re.compile(r"^[^\s<>\r\n,;]+@[^\s<>\r\n,;]+\.[^\s<>\r\n,;]+$")
_SENDER = re.compile(r"^[^\r\n<>]*<[^\s<>\r\n,;]+@[^\s<>\r\n,;]+>$|^[^\s<>\r\n,;]+@[^\s<>\r\n,;]+\.[^\s<>\r\n,;]+$")

# What each message may fill in. A words file that names any other field is refused when it loads.
CODE_FIELDS = frozenset({"code"})
NOTICE_FIELDS = {"recovery_started": frozenset({"cancel_code", "effective_on"})}


class MailConfigError(Exception):
    """A misconfiguration found at startup, never papered over."""


class MailSendError(Exception):
    """A send the provider refused or could not take. Carries no address, code or provider text."""


@dataclass(frozen=True)
class Message:
    subject: str
    body: str


@dataclass(frozen=True)
class MailWords:
    code: Message
    notices: dict[str, Message]

    @classmethod
    def from_file(cls, path: Path) -> "MailWords":
        try:
            data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise MailConfigError(f"the approved sign-in mail words file is missing: {path}") from exc
        except (OSError, yaml.YAMLError) as exc:
            raise MailConfigError(f"the sign-in mail words file cannot be read: {path}") from exc
        return cls.from_data(data)

    @classmethod
    def from_data(cls, data) -> "MailWords":
        if not isinstance(data, dict) or not isinstance(data.get("code"), dict):
            raise MailConfigError("the sign-in mail words need a 'code' section with a subject and a body")
        code = _message(data["code"], "code", CODE_FIELDS, required=CODE_FIELDS)
        raw_notices = data.get("notices") or {}
        if not isinstance(raw_notices, dict):
            raise MailConfigError("the sign-in mail words 'notices' must be a mapping")
        unknown = set(raw_notices) - set(NOTICE_FIELDS)
        if unknown:
            raise MailConfigError(f"the sign-in mail words name notices the service does not send: {sorted(unknown)}")
        missing = set(NOTICE_FIELDS) - set(raw_notices)
        if missing:
            raise MailConfigError(f"the sign-in mail words lack words for: {sorted(missing)}")
        notices = {
            kind: _message(raw_notices[kind], f"notice {kind}", NOTICE_FIELDS[kind], required=NOTICE_FIELDS[kind])
            for kind in NOTICE_FIELDS
        }
        return cls(code=code, notices=notices)


def _message(raw, label: str, allowed: frozenset, *, required: frozenset) -> Message:
    if not isinstance(raw, dict) or not isinstance(raw.get("subject"), str) or not isinstance(raw.get("body"), str):
        raise MailConfigError(f"the sign-in mail words for {label} need a subject and a body, both text")
    subject, body = raw["subject"].strip(), raw["body"].strip()
    if not subject or not body or "\n" in subject or "\r" in subject:
        raise MailConfigError(f"the sign-in mail words for {label}: a subject on one line and a body are both needed")
    used = set()
    for text in (subject, body):
        try:
            used |= {name for _, name, _, _ in string.Formatter().parse(text) if name is not None}
        except ValueError as exc:
            raise MailConfigError(f"the sign-in mail words for {label} have a stray brace") from exc
    if used - allowed:
        raise MailConfigError(f"the sign-in mail words for {label} use fields that are not sent: {sorted(used - allowed)}")
    if not required <= used:
        raise MailConfigError(f"the sign-in mail words for {label} must use {sorted(required - used)}")
    return Message(subject, body)


class SesMailer:
    """The accounts Mailer over an SES client. The client is handed in so tests send nothing."""

    def __init__(self, client, sender: str, words: MailWords):
        if not _SENDER.match(sender or ""):
            raise MailConfigError(f"{ENV_FROM} is not a sender address")
        self._client = client
        self._sender = sender
        self._words = words

    def send_code(self, address: str, code: str) -> None:
        self._send(address, self._words.code, {"code": code})

    def send_notice(self, address: str, kind: str, fields: dict) -> None:
        message = self._words.notices.get(kind)
        if message is None:
            raise MailSendError("no words for this notice")
        self._send(address, message, {name: fields[name] for name in NOTICE_FIELDS[kind]})

    def _send(self, address: str, message: Message, fields: dict) -> None:
        if not _ADDRESS.match(address or ""):
            raise MailSendError("not a sendable address")
        try:
            self._client.send_email(
                FromEmailAddress=self._sender,
                Destination={"ToAddresses": [address]},
                Content={"Simple": {
                    "Subject": {"Data": message.subject.format(**fields), "Charset": "UTF-8"},
                    "Body": {"Text": {"Data": message.body.format(**fields), "Charset": "UTF-8"}},
                }},
            )
        except Exception:  # noqa: BLE001 - the provider's text can name the recipient
            raise MailSendError("the provider did not take the message") from None


def from_env(env: dict) -> SesMailer | None:
    """The mailer for a deploy that sets the SES values, None when none are set (the accounts
    runtime then refuses to start with the flag on). Some set and some missing is a mistake."""
    present = {name for name in _ENV_NAMES if (env.get(name) or "").strip()}
    if not present:
        return None
    if present != set(_ENV_NAMES):
        raise MailConfigError("the SES mail settings are partly set; missing: " + ", ".join(sorted(set(_ENV_NAMES) - present)))
    words = MailWords.from_file(Path(env.get(ENV_WORDS) or DEFAULT_WORDS_PATH))
    import boto3  # local import: keeps this module importable in a boto3-less unit test env

    client = boto3.client(
        "sesv2",
        region_name=env[ENV_REGION].strip(),
        aws_access_key_id=env[ENV_ACCESS_KEY].strip(),
        aws_secret_access_key=env[ENV_SECRET_KEY].strip(),
    )
    return SesMailer(client, env[ENV_FROM].strip(), words)
