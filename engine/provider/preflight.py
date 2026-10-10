"""The Bedrock preflight (spec SS7): "nothing is trusted until the preflight
runs against the live account - caching engages, both usage shapes report
cache fields, $/token reconciled against the real AWS invoice." This script
does the first two; the third (invoice reconciliation) can't happen in one
run - AWS invoices lag - so it logs exact token counts for that to be done
against the real bill once it's available, rather than guessing a price.

Never quotes a $/turn or $/token figure - spec principle 13: "no figure
quoted onward until measured on the billing provider." This script measures
tokens, not dollars.
"""
import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from .bedrock import ModelResolutionError, make_client, normalize_usage, resolve_model_id

REPORT_PATH = Path(__file__).resolve().parent / "reports" / "preflight-report.json"

# Cacheable system prompt must clear Anthropic's minimum cacheable-length
# threshold (1024 tokens for Sonnet-class) or cache_control is silently a
# no-op - padded well past that so a real engine, not a coin-flip, decides
# whether caching engages.
_CACHE_PADDING_UNIT = (
    "This is preflight filler text for the Church in Conversation Bedrock cache-engagement check. "
)
_SYSTEM_PROMPT = _CACHE_PADDING_UNIT * 200  # ~1600+ words, comfortably over the cache-eligibility floor


def _call(client, model_id: str, *, stream: bool):
    system = [{"type": "text", "text": _SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": "Reply with exactly one word: OK"}]
    if not stream:
        response = client.messages.create(model=model_id, max_tokens=16, system=system, messages=messages)
        return normalize_usage(response.usage)
    final_usage = None
    with client.messages.stream(model=model_id, max_tokens=16, system=system, messages=messages) as s:
        for _ in s.text_stream:
            pass
        final_message = s.get_final_message()
        final_usage = final_message.usage
    if final_usage is None:
        raise RuntimeError("streaming response never reported a final usage object - exactly the silent-absence risk spec SS10 names")
    return normalize_usage(final_usage)


def run(model_pattern: str, region: str) -> dict:
    model_id = resolve_model_id(model_pattern, region)
    client = make_client(region)

    write_call = _call(client, model_id, stream=False)  # first call: expect a cache WRITE
    read_call = _call(client, model_id, stream=False)  # second call, same prefix: expect a cache READ
    stream_call = _call(client, model_id, stream=True)  # confirm the streaming usage shape also carries cache fields

    report = {
        "model_id": model_id,
        "region": region,
        "calls": {
            "non_streaming_first (expect cache write)": asdict(write_call),
            "non_streaming_second (expect cache read)": asdict(read_call),
            "streaming (expect cache read)": asdict(stream_call),
        },
        "cache_engaged": {
            "write_call_wrote_to_cache": write_call.cache_creation_input_tokens > 0,
            "read_call_read_from_cache": read_call.cache_read_input_tokens > 0,
            "streaming_shape_reports_cache_fields": stream_call.cache_creation_input_tokens > 0 or stream_call.cache_read_input_tokens > 0,
        },
        "note": (
            "No $/token or $/turn figure is computed here - spec principle 13 forbids quoting a cost "
            "figure onward until it is measured on the billing provider. These raw token counts are "
            "what a later pass reconciles against the real AWS invoice once it's available (invoices "
            "lag; this preflight cannot do that reconciliation in one run)."
        ),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-pattern", required=True, help="substring/name fragment to resolve to exactly one inference profile")
    parser.add_argument("--region", required=True)
    args = parser.parse_args()

    try:
        report = run(args.model_pattern, args.region)
    except ModelResolutionError as e:
        print(json.dumps({"pass": False, "error": str(e)}, indent=2))
        return 1

    all_engaged = all(report["cache_engaged"].values())
    report["pass"] = all_engaged
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if all_engaged else 1


if __name__ == "__main__":
    sys.exit(main())
