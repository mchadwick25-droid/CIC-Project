"""Review-file header contract (check f)."""
from __future__ import annotations

import re
from pathlib import Path

from .common import PLACEHOLDER, REPO_ROOT, Finding, read_text, rel

SIMULATED_REVIEW_LABEL = "Simulated review — informational only, not an Article 31 substitute."
REVIEWER_MODEL_ID = "claude-opus-5-5"

FIELD_REVIEWER_MODEL = "Reviewer model"
FIELD_DRAFTER_MODEL = "Drafter model"
FIELD_REVIEWER_AGENT = "Reviewer agent"
FIELD_DRAFTER_AGENT = "Drafter agent"
DRAFTER_WITHHELD = "withheld until the mapping is revealed"

FIELD_ROUND = "Round"
FIELD_TRUNCATION_METHOD_1 = "Truncation check, method 1"
FIELD_TRUNCATION_METHOD_2 = "Truncation check, method 2"

HEADER_FIELDS = (
    FIELD_REVIEWER_MODEL,
    FIELD_DRAFTER_MODEL,
    FIELD_REVIEWER_AGENT,
    FIELD_DRAFTER_AGENT,
    FIELD_ROUND,
    FIELD_TRUNCATION_METHOD_1,
    FIELD_TRUNCATION_METHOD_2,
)

HEADER_LINES = 30
_DASHES = re.compile(r"[‒–—―-]+")
_FILENAME_ROUND = re.compile(r"Round_?(\d+)", re.IGNORECASE)
_MODEL = re.compile(r"(?:claude[-\s]*)?(opus|sonnet|haiku|fable)[-\s]*(\d+)[-.\s](\d+)", re.IGNORECASE)


def model_id(value: str) -> str | None:
    """A model name in any common spelling ("Opus 5.5", "Claude Opus 5.5",
    "claude-opus-5-5") as one id, or None when it is not a model name."""
    m = _MODEL.fullmatch(value.strip().strip("`*").strip())
    return f"claude-{m.group(1).lower()}-{m.group(2)}-{m.group(3)}" if m else None


def _same_agent(a: str, b: str) -> bool:
    key = lambda v: re.sub(r"[\W_]+", "", v).lower()  # noqa: E731
    return key(a) == key(b)


def _withheld(value: str | None) -> bool:
    return value is not None and value.strip().rstrip(".").lower() == DRAFTER_WITHHELD


def _canonical(line: str) -> str:
    line = line.strip().strip("*_#> ").strip()
    line = _DASHES.sub("-", line)
    return re.sub(r"\s+", " ", line).rstrip(".").lower()


def _field_value(lines: list[str], name: str) -> str | None:
    pattern = re.compile(
        rf"^\s*(?:[-*]\s*)?\**{re.escape(name)}\**\s*:\s*\**\s*(.*?)\s*\**\s*$", re.IGNORECASE
    )
    for line in lines:
        m = pattern.match(line)
        if m:
            return m.group(1).strip()
    return None


def check_review_file(path: Path, root: Path = REPO_ROOT) -> list[Finding]:
    where = rel(path, root)
    if not path.is_file():
        return [Finding(where, "reviewfile-exists", "review file does not exist")]
    lines = read_text(path).splitlines()
    findings: list[Finding] = []

    def bad(check: str, reason: str) -> None:
        findings.append(Finding(where, check, reason))

    first = lines[0] if lines else ""
    if _canonical(first) != _canonical(SIMULATED_REVIEW_LABEL):
        bad("reviewfile-label", f"first line must be the simulated-review label {SIMULATED_REVIEW_LABEL!r}")

    header = lines[1 : HEADER_LINES + 1]
    values = {name: _field_value(header, name) for name in HEADER_FIELDS}
    for name, value in values.items():
        if value is None:
            bad("reviewfile-field", f"header field '{name}' is missing from the first {HEADER_LINES} lines")
        elif PLACEHOLDER.match(value):
            bad("reviewfile-field", f"header field '{name}' is empty or a placeholder")

    def filled(name: str) -> str | None:
        value = values[name]
        return value if value and not PLACEHOLDER.match(value) else None

    reviewer, drafter = filled(FIELD_REVIEWER_MODEL), filled(FIELD_DRAFTER_MODEL)
    if reviewer and model_id(reviewer) != REVIEWER_MODEL_ID:
        bad("reviewfile-reviewer", f"reviewer model is {reviewer!r}; it must be {REVIEWER_MODEL_ID}")
    reviewer_agent, drafter_agent = filled(FIELD_REVIEWER_AGENT), filled(FIELD_DRAFTER_AGENT)
    model_withheld, agent_withheld = _withheld(drafter), _withheld(drafter_agent)
    if drafter and drafter_agent and model_withheld != agent_withheld:
        bad("reviewfile-drafter", "the drafter model and the drafter agent must both be withheld, or neither")
    if drafter and not model_withheld and model_id(drafter) is None:
        bad("reviewfile-drafter", f"drafter model {drafter!r} is not a recognized model name")
    if reviewer_agent and drafter_agent and not agent_withheld and _same_agent(reviewer_agent, drafter_agent):
        bad("reviewfile-independence", "the reviewer agent and the drafter agent are the same; the reviewer is never the drafter")

    m1, m2 = values[FIELD_TRUNCATION_METHOD_1], values[FIELD_TRUNCATION_METHOD_2]
    if m1 and m2 and not PLACEHOLDER.match(m1) and not PLACEHOLDER.match(m2):
        if re.sub(r"\W+", " ", m1).strip().lower() == re.sub(r"\W+", " ", m2).strip().lower():
            bad("reviewfile-truncation", "the two truncation-check methods are identical; they must be independent methods")

    round_value = values[FIELD_ROUND]
    if round_value and not PLACEHOLDER.match(round_value):
        m = re.fullmatch(r"(\d+)\b.*", round_value.strip("`"))
        if not m or int(m.group(1)) < 1:
            bad("reviewfile-round", f"round must be a whole number of 1 or more, found {round_value!r}")
        else:
            named = _FILENAME_ROUND.search(path.name)
            if named and int(named.group(1)) != int(m.group(1)):
                bad("reviewfile-round", f"header round {m.group(1)} does not match round {named.group(1)} in the file name")
    return findings
