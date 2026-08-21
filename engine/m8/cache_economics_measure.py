"""Stage-6 gate item: "cache economics re-measured and recorded with the
band." The spec's own cache facts (~17.8k token static prefix at 0.1x read,
1h TTL write at 2x, pooling previously measured 16x) are explicitly
flagged as needing re-measurement under the new lazy-loading architecture
("16x pooling was measured on the old warm-everything deployment... does
not carry, re-measure" - Artifact-6 SS1). This script re-confirms the
underlying MECHANISM (write once, read repeatedly off the same static
prefix) still engages correctly on Bedrock post-redesign, and records the
observed token-level band across repeated reads - it never computes a
dollar figure (principle 13: no $/token quoted until invoice-reconciled;
Anthropic's stated 2x/0.1x multipliers are a published rate STRUCTURE, not
a measured amount, and are unaffected by this run).

Real, billed Bedrock calls - like engine/provider/preflight.py and
engine/m5/safety_script_run.py, a by-hand, credentialed run, not CI.
"""
import argparse
import json
import sys
from pathlib import Path

from engine.m8.parity import assert_parity
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPORT_PATH = Path(__file__).resolve().parent / "reports" / "cache-economics-report.json"

# Same padding technique as engine/provider/preflight.py - comfortably over
# Anthropic's ~1024-token Sonnet-class cache-eligibility floor, so a real
# engine decides whether caching engages, not a coin-flip on prompt length.
_CACHE_PADDING_UNIT = "This is a cache-economics re-measurement filler sentence for Church in Conversation stage 6. "
_SYSTEM_PROMPT = _CACHE_PADDING_UNIT * 200


def _call(client, model_id: str):
    system = [{"type": "text", "text": _SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": "Reply with exactly one word: OK"}]
    response = client.messages.create(model=model_id, max_tokens=16, system=system, messages=messages)
    normalized = normalize_usage(response.usage)
    assert_parity(response.usage, normalized)  # every real call in this file is parity-checked, not just logged
    return normalized


def run(region: str, samples: int = 3) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)  # the voice model - the one that actually carries a world's static prefix in production
    client = make_client(region)

    write_call = _call(client, model_id)  # first call this run: expect a cache WRITE
    read_samples = [_call(client, model_id) for _ in range(samples)]  # same prefix, repeated: expect cache READS

    report = {
        "model_id": model_id,
        "region": region,
        "write_call": {"cache_creation_input_tokens": write_call.cache_creation_input_tokens, "input_tokens": write_call.input_tokens},
        "read_samples": [{"cache_read_input_tokens": s.cache_read_input_tokens, "input_tokens": s.input_tokens} for s in read_samples],
        "band": {
            "cache_write_engaged": write_call.cache_creation_input_tokens > 0,
            "cache_read_tokens_min": min((s.cache_read_input_tokens for s in read_samples), default=0),
            "cache_read_tokens_max": max((s.cache_read_input_tokens for s in read_samples), default=0),
        },
        "note": (
            "Token counts only - no $/token figure computed here (principle 13). What this run confirms is that "
            "the underlying MECHANISM (write once, read repeatedly off the same static prefix) still engages "
            "correctly on Bedrock under the lazy-loading architecture; invoice-based dollar reconciliation is a "
            "separate, later step (engine/provider/preflight.py's still-pending third leg)."
        ),
    }
    report["mechanism_confirmed"] = write_call.cache_creation_input_tokens > 0 and all(
        s.cache_read_input_tokens == write_call.cache_creation_input_tokens for s in read_samples
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    parser.add_argument("--samples", type=int, default=3)
    args = parser.parse_args()

    report = run(args.region, args.samples)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["mechanism_confirmed"] else 1


if __name__ == "__main__":
    sys.exit(main())
