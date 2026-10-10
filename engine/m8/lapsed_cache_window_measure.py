"""Stage-6 gate item: "a lapsed cache window visible in the numbers."
Bedrock's ephemeral cache_control TTL is 1h - the only honest way to prove
a lapsed window is to actually wait past it and make a real follow-up call
with the identical system prompt, not to assert it from the documented TTL
value alone. Two phases, run as two separate invocations with a real gap
between them:

  --phase write   makes the initial call (expect a cache WRITE), saves the
                   exact system prompt text + timestamp + observed usage to
                   a small state file so phase 2 can reuse the identical
                   prompt (a re-derived or re-padded prompt could hash
                   differently and this would prove nothing).
  --phase check   (run >=65 minutes later) makes the follow-up call with
                   the SAME saved prompt text. cache_read_input_tokens==0
                   and cache_creation_input_tokens>0 is the lapsed-window
                   proof (a fresh write, not a read); cache_read_input_
                   tokens>0 would mean the window was still live at check
                   time - a real, reportable finding, not something to
                   paper over.

Real, billed Bedrock calls - by-hand, credentialed, not a CI job.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from engine.m8.parity import assert_parity
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

STATE_PATH = Path(__file__).resolve().parent / "reports" / "lapsed-cache-window-state.json"
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "lapsed-cache-window-report.json"

_PADDING_UNIT = "This is a lapsed-cache-window filler sentence for Church in Conversation stage 6, invocation {tag}. "
_PROMPT_REPEAT = 200


def _call(client, model_id: str, system_text: str):
    system = [{"type": "text", "text": system_text, "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": "Reply with exactly one word: OK"}]
    response = client.messages.create(model=model_id, max_tokens=16, system=system, messages=messages)
    normalized = normalize_usage(response.usage)
    assert_parity(response.usage, normalized)
    return normalized


def phase_write(region: str) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    client = make_client(region)
    system_text = (_PADDING_UNIT.format(tag="lapsed-window-probe") * _PROMPT_REPEAT)

    usage = _call(client, model_id, system_text)
    state = {
        "model_id": model_id,
        "region": region,
        "system_text": system_text,
        "write_at": datetime.now(timezone.utc).isoformat(),
        "write_usage": {"cache_creation_input_tokens": usage.cache_creation_input_tokens, "cache_read_input_tokens": usage.cache_read_input_tokens},
    }
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return state


def phase_check(region: str) -> dict:
    if not STATE_PATH.exists():
        raise SystemExit(f"no write-phase state at {STATE_PATH} - run --phase write first")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    client = make_client(region)

    write_time = datetime.fromisoformat(state["write_at"])
    elapsed_minutes = (datetime.now(timezone.utc) - write_time).total_seconds() / 60

    usage = _call(client, state["model_id"], state["system_text"])

    report = {
        "model_id": state["model_id"],
        "region": region,
        "write_at": state["write_at"],
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_minutes": round(elapsed_minutes, 1),
        "write_usage": state["write_usage"],
        "check_usage": {"cache_creation_input_tokens": usage.cache_creation_input_tokens, "cache_read_input_tokens": usage.cache_read_input_tokens},
    }
    report["window_lapsed"] = usage.cache_read_input_tokens == 0 and usage.cache_creation_input_tokens > 0
    report["still_within_window"] = usage.cache_read_input_tokens > 0
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--phase", required=True, choices=["write", "check"])
    args = parser.parse_args()

    if args.phase == "write":
        state = phase_write(args.region)
        print(json.dumps(state, indent=2))
        return 0

    report = phase_check(args.region)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["window_lapsed"] else 1


if __name__ == "__main__":
    sys.exit(main())
