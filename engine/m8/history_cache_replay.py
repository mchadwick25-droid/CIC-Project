"""Offline replay of a recorded one-voice session through the two request
shapes. Makes no API call and spends nothing.

Reads a live-memory-growth report (per-turn token counts) and prices each
turn twice at the approved rate card:

  before: the directive sits in the system block after the world prompt's
          breakpoint, so the whole session history is billed as fresh input
          every turn.
  after:  the history carries a second breakpoint (engine.m4.voice_request),
          so each turn reads the previous turn's cached history and writes
          only the newest user/assistant pair.

The report stores one uncached-input count per turn, not history alone. History
size is taken as that count minus turn 0's (message, evidence and directive
only), which assumes those stay roughly constant. The directive frame adds
FRAME_TOKENS of fresh input to every turn after the change.
"""
import argparse
import json
from pathlib import Path

from engine.m8.price_tables import SONNET_4_5_PRICE_TABLE as PRICES

FRAME_TOKENS = 28
DEFAULT_REPORT = Path(__file__).resolve().parent / "reports" / "live-memory-growth-report.json"


def _price(fresh: int, write: int, read: int, output: int) -> float:
    return (
        fresh * PRICES.input_per_token + write * PRICES.cache_write_per_token
        + read * PRICES.cache_read_per_token + output * PRICES.output_per_token
    )


def replay(turns: list[dict]) -> list[dict]:
    base = turns[0]["voice_call_input_tokens"]
    rows, prev_history = [], 0
    for t in turns:
        history = max(t["voice_call_input_tokens"] - base, 0)
        system_write, system_read = t["voice_call_cache_write_tokens"], t["voice_call_cache_read_tokens"]
        output = t["voice_call_output_tokens"]
        before = _price(t["voice_call_input_tokens"], system_write, system_read, output)
        cached_read = prev_history
        new_write = history - prev_history
        after = _price(
            t["voice_call_input_tokens"] - history + FRAME_TOKENS, system_write + new_write, system_read + cached_read, output,
        )
        rows.append({"turn": t["turn_index"], "history_tokens": history, "before": before, "after": after})
        prev_history = history
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    rows = replay(json.loads(parser.parse_args().report.read_text(encoding="utf-8"))["turns"])
    print("turn  history_tokens   before    after   saved")
    for r in rows:
        print(f"{r['turn']:>4}  {r['history_tokens']:>14}  ${r['before']:.4f}  ${r['after']:.4f}  {1 - r['after'] / r['before']:>5.0%}")
    before, after = sum(r["before"] for r in rows), sum(r["after"] for r in rows)
    print(f"total                    ${before:.4f}  ${after:.4f}  {1 - after / before:>5.0%}")


if __name__ == "__main__":
    main()
