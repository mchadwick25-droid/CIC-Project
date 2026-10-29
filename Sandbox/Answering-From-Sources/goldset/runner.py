"""Runs one labeller over a labelling stream, under the live-test guard.

A stream line is one thing to label: a natural pool item, a seeded defect or
a control. The labeller is shown only the sentence and its evidence pack; the
line's kind, its key and its origin stay here. Every reply is kept as it came,
with the check's result. A reply the check rejects is asked again once, with
the reason; a second rejection leaves the line unlabelled.

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

MAX_TOKENS = 1200
EXPECTED_OUTPUT_TOKENS = 450
CHARS_PER_TOKEN = 3.5
REGION = "us-east-1"


def stream_line_item(line: dict) -> dict:
    """The fields evidence.build_pack and the prompt need, and nothing else."""
    return {k: line[k] for k in ("item_id", "world", "records_commit", "bindings", "sentence")}


def estimate(lines: list[dict], price) -> dict:
    input_tokens = 0
    for line in lines:
        pack = build_pack(stream_line_item(line))
        input_tokens += (len(SYSTEM_PROMPT) + len(user_message(line["sentence"], pack))) / CHARS_PER_TOKEN
    output_tokens = EXPECTED_OUTPUT_TOKENS * len(lines)
    dollars = None
    if price is not None:
        dollars = input_tokens * price.input_per_token + output_tokens * price.output_per_token
    return {"lines": len(lines), "input_tokens": round(input_tokens), "output_tokens": output_tokens, "estimated_usd": dollars}


def _call(client, model_id: str, system: str, messages: list[dict]) -> tuple[str, dict]:
    response = client.messages.create(model=model_id, max_tokens=MAX_TOKENS, system=system, messages=messages)
    text = "".join(getattr(block, "text", "") for block in response.content)
    usage = response.usage
    return text, {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens}


def label_line(client, model_id: str, line: dict) -> dict:
    pack = build_pack(stream_line_item(line))
    messages = [{"role": "user", "content": user_message(line["sentence"], pack)}]
    attempts = []
    for _attempt in range(2):
        reply, usage = _call(client, model_id, SYSTEM_PROMPT, messages)
        checked = parse_reply(reply, pack)
        attempts.append({"reply": reply, "usage": usage, "check": "ok" if checked["ok"] else checked["why"]})
        if checked["ok"]:
            return {"line_id": line["line_id"], "model_id": model_id, "label": checked["label"], "attempts": attempts, "passage_located": located(pack)}
        messages = messages + [
            {"role": "assistant", "content": reply},
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
    done = {r["line_id"] for r in read_jsonl(args.out) if r.get("label") is not None}
    todo = [line for line in lines if line["line_id"] not in done]
    price = price_for_route("voice_generation", args.model, "bedrock")
    settings = {
        "stream": str(args.stream), "model_id": args.model, "region": REGION, "max_tokens": MAX_TOKENS,
        "temperature": "API default (not set)", "lines_in_stream": len(lines), "already_labelled": len(done),
        "to_label": len(todo), "priced": price is not None, **estimate(todo, price),
        "note": "each rejected reply is asked once more; the estimate counts one call per line",
    }
    print(json.dumps(settings, indent=2), flush=True)
    if args.settings_only:
        return 0
    if price is None:
        print(f"no approved price for {args.model}; a capped run cannot count its spend", file=sys.stderr)
        return 2

    from engine.provider.bedrock import make_client

    client = make_client(REGION)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("a", encoding="utf-8") as out:
        for line in todo:
            try:
                row = label_line(client, args.model, line)
            except guard.LiveTestCapReached as stop:
                print(f"stopped at the cap: {stop}", flush=True)
                break
            row["at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            out.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            out.flush()
    print(json.dumps({"priced_total_usd": guard.priced_total()}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
