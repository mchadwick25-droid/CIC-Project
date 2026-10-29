"""Runs one labeller over a labelling stream, under the live-test guard.

A stream line is one thing to label: a natural pool item, a seeded defect or
a control. The labeller is shown only the sentence and its evidence pack; the
line's kind, its key and its origin stay here. Every reply is kept as it came,
with the check's result. A reply the check rejects is asked again once, with
the reason; a second rejection leaves the line unlabelled, and a resumed run
does not ask it again. One output file holds one model's labels.

Settings, counts and the estimated cost print before any call. With
--settings-only the run stops there and makes no call. Without an approved
live test (--live-test "<name>" --cap-usd <n>) the guard refuses the client.

  python -m goldset.runner --stream <stream.jsonl> --model <inference profile id> \\
      --out <labels.jsonl> --settings-only
  python -m goldset.runner ... --live-test "<name>" --cap-usd <n>
"""
import argparse
import json
import sys
import time
from pathlib import Path

from goldset.common import read_jsonl
from goldset.evidence import build_pack, located
from goldset.labeller import SYSTEM_PROMPT, parse_reply, user_message
from engine.provider.guard import LiveTestCapReached

MAX_TOKENS = 1200
EXPECTED_OUTPUT_TOKENS = 450
REASONING_MAX_TOKENS = 12_000
REASONING_EXPECTED_OUTPUT_TOKENS = 3_000
REASONING_FIELDS = {"reasoning": {"effort": "high"}}
CHARS_PER_TOKEN = 3.5
REGION = "us-east-1"


def is_claude(model_id: str) -> bool:
    return ".anthropic." in model_id or model_id.startswith("anthropic.")


def call_settings(model_id: str) -> dict:
    """A Claude model through the Messages seam at the default effort; any
    other vendor through the Converse seam with reasoning at high effort
    (the specialist runs slow and strong), its reasoning billed as output."""
    if is_claude(model_id):
        return {"seam": "engine.provider.bedrock (Messages API)", "max_tokens": MAX_TOKENS, "expected_output_tokens": EXPECTED_OUTPUT_TOKENS, "extra": {}}
    return {"seam": "engine.provider.bedrock_converse (Converse API)", "max_tokens": REASONING_MAX_TOKENS,
            "expected_output_tokens": REASONING_EXPECTED_OUTPUT_TOKENS, "extra": {"additional_model_request_fields": REASONING_FIELDS}}


def make_client_for(model_id: str, region: str = REGION):
    if is_claude(model_id):
        from engine.provider.bedrock import make_client
    else:
        from engine.provider.bedrock_converse import make_client
    return make_client(region)


def stream_line_item(line: dict) -> dict:
    """The fields evidence.build_pack and the prompt need, and nothing else."""
    return {k: line[k] for k in ("item_id", "world", "records_commit", "bindings", "sentence")}


def estimate(lines: list[dict], price, expected_output_tokens: int = EXPECTED_OUTPUT_TOKENS) -> dict:
    input_tokens = 0
    for line in lines:
        pack = build_pack(stream_line_item(line))
        input_tokens += (len(SYSTEM_PROMPT) + len(user_message(line["sentence"], pack))) / CHARS_PER_TOKEN
    output_tokens = expected_output_tokens * len(lines)
    dollars = None
    if price is not None:
        dollars = input_tokens * price.input_per_token + output_tokens * price.output_per_token
    return {"lines": len(lines), "input_tokens": round(input_tokens), "output_tokens": output_tokens, "estimated_usd": dollars}


def _call(client, model_id: str, system: str, messages: list[dict]) -> tuple[str, dict]:
    settings = call_settings(model_id)
    response = client.messages.create(model=model_id, max_tokens=settings["max_tokens"], system=system, messages=messages, **settings["extra"])
    text = "".join(getattr(block, "text", "") for block in response.content)
    usage = response.usage
    return text, {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens}


def label_line(client, model_id: str, line: dict) -> dict:
    pack = build_pack(stream_line_item(line))
    messages = [{"role": "user", "content": user_message(line["sentence"], pack)}]
    attempts = []
    for attempt in range(2):
        try:
            reply, usage = _call(client, model_id, SYSTEM_PROMPT, messages)
        except LiveTestCapReached:
            if attempt == 0:
                raise
            return {"line_id": line["line_id"], "model_id": model_id, "label": None, "attempts": attempts, "passage_located": located(pack), "stopped_at_cap": True}
        checked = parse_reply(reply, pack)
        attempts.append({"reply": reply, "usage": usage, "check": "ok" if checked["ok"] else checked["why"]})
        if checked["ok"]:
            return {"line_id": line["line_id"], "model_id": model_id, "label": checked["label"], "attempts": attempts, "passage_located": located(pack)}
        messages = messages + [
            {"role": "assistant", "content": reply or "(empty reply)"},
            {"role": "user", "content": f"That reply cannot be used: {checked['why']}. Reply again with one JSON object, copying evidence words exactly from the named block."},
        ]
    return {"line_id": line["line_id"], "model_id": model_id, "label": None, "attempts": attempts, "passage_located": located(pack)}


def main(argv: list[str] | None = None) -> int:
    from engine.m8.price_tables import price_for_route
    from engine.provider import guard

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--model", required=True, help="the exact inference profile id")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=None, help="label only the first N lines (a sample)")
    parser.add_argument("--settings-only", action="store_true")
    guard.add_arguments(parser)
    args = parser.parse_args(argv)

    lines = read_jsonl(args.stream)[: args.limit]
    existing = read_jsonl(args.out)
    other_models = sorted({r["model_id"] for r in existing} - {args.model})
    if other_models:
        print(f"{args.out} already holds labels from {other_models}; one file per model", file=sys.stderr)
        return 2
    done = {r["line_id"] for r in existing if not r.get("stopped_at_cap")}
    todo = [line for line in lines if line["line_id"] not in done]
    price = price_for_route("voice_generation", args.model, "bedrock")
    call = call_settings(args.model)
    settings = {
        "stream": str(args.stream), "model_id": args.model, "region": REGION, "seam": call["seam"],
        "max_tokens": call["max_tokens"], "request_fields": call["extra"].get("additional_model_request_fields"),
        "temperature": "API default (not set)", "lines_in_stream": len(lines), "already_labelled": len(done),
        "to_label": len(todo), "priced": price is not None,
        "price_per_million": None if price is None else {"input": round(price.input_per_token * 1e6, 4), "output": round(price.output_per_token * 1e6, 4)},
        **estimate(todo, price, call["expected_output_tokens"]),
        "note": "each rejected reply is asked once more; the estimate counts one call per line",
    }
    print(json.dumps(settings, indent=2), flush=True)
    if args.settings_only:
        return 0
    if price is None:
        print(f"no approved price for {args.model}; a capped run cannot count its spend", file=sys.stderr)
        return 2

    client = make_client_for(args.model)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("a", encoding="utf-8") as out:
        for line in todo:
            try:
                row = label_line(client, args.model, line)
            except LiveTestCapReached as stop:
                print(f"stopped at the cap: {stop}", flush=True)
                break
            row["at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            out.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            out.flush()
            if row.get("stopped_at_cap"):
                print("stopped at the cap during a retry", flush=True)
                break
    print(json.dumps({"priced_total_usd": guard.priced_total()}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
