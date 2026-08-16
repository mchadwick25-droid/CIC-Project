#!/usr/bin/env python3
"""Dump what each OVER_SETTLING path actually said about one turn.

    cd cic/runtime
    PYTHONPATH=. python3 ../../tools/cost/diagnose_over_settling.py --only 48 --reps 3

compare_over_settling.py reports verdicts. When the two paths disagree
stably, the verdict is the one thing that cannot explain the disagreement -
you need the model's own words. This prints them: the screen's candidate
list, the adjudicator's verdicts, and the fold's Phase 1 enumeration and
Phase 2 rulings, in full, for every draw.

The question it exists to answer, on any stable regression:

    did the fold's Phase 1 fail to ENUMERATE the claim the pair found,
    or did it enumerate it and Phase 2 CLEAR it?

Those need opposite fixes. A missed enumeration is a Phase 1 instruction
problem - the claim type is not in the list of what to look for, or it read
as measured in tone. A cleared enumeration is Phase 2 applying the
affirmative test to material that does support the limit, or adjudicating
against different material entirely - which is why this also diffs the
retrieved source block.

HOW IT CAPTURES THE TEXT
------------------------
By wrapping `get_monitoring_llm` inside app.graph.nodes, not by rebuilding
the calls. Every prompt and completion here is the one production sent and
got - the prompt template, evidence gathering, cache boundary and model
config are all the real ones, unmodified. Nothing is reimplemented, so
nothing can drift out of step with what ships.

RETRIEVAL IS PART OF THE ANSWER
-------------------------------
`_gather_world_evidence` runs retrieval fresh on every call - two retrievers,
each with its own guard evaluation - so two draws of the same path can
adjudicate against DIFFERENT source material. That makes source drift a
candidate cause of the instability compare_over_settling.py measured
(29-43% of turns not reproducing), alongside sampling temperature. This
script diffs the `## Retrieved source material` block across every call and
reports how much of it is shared, so the two causes can be told apart:
identical material with different verdicts is the model; different material
is retrieval.

Spends roughly $0.011 per turn per draw, same as the comparison harness.

WHAT IT FOUND (turn 48, 3 draws, temp 0) - see samples/
-------------------------------------------------------
The one stable regression blocking the fold. Answer: Phase 1 enumerates the
claim verbatim, every draw. Phase 2 clears it, every draw, with the same
move - "the representative speaks from inside a household ... does not claim
it as universal".

The cause is visible in the Concern line each path writes for that same
claim. The blind screen, having read no sources, can only say the claim is
stated more firmly than a contested thing should be. The fold, which has
already read the sources, frames its concern as "is this universal across
households?" - a question with a stock answer that always clears. Phase 2
then answers the question Phase 1 asked.

So the screen's contribution is not filtering, it is blindness, and no
instruction restores blindness inside a single forward pass that reads the
sources before it writes.

Retrieval was ruled out here: all six source-fed calls saw 37 of 37 identical
chunks. And with temperature pinned the 1k-token screen was byte-identical
across draws while the 12k-token source-fed calls were not - temperature 0
is not determinism at this context length.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare_over_settling import sessions          # noqa: E402

BOUNDARY = "## Retrieved source material for this world relevant to this response"
# The retrieved material carries its OWN "## " headers ("## Retrieved Lexicon
# Context", "## World Meaning"), so the block cannot be ended at the next
# markdown header - it has to be ended at the named section that follows it.
RETRIEVED_END = "## The representative's response"


class Recorder:
    """Wraps the monitoring LLM and keeps every prompt/completion pair."""

    def __init__(self, real_factory):
        self._real_factory = real_factory
        self.label = "?"
        self.draw = 0
        self.calls: list[dict] = []

    def __call__(self):                       # stands in for get_monitoring_llm()
        return _Proxy(self._real_factory(), self)


class _Proxy:
    def __init__(self, llm, recorder):
        self._llm, self._rec = llm, recorder

    def __getattr__(self, name):
        return getattr(self._llm, name)

    def invoke(self, messages, *a, **kw):
        response = self._llm.invoke(messages, *a, **kw)
        prompt = "\n\n".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for m in messages
            for part in (m.content if isinstance(m.content, list) else [m.content])
        )
        self._rec.calls.append({
            "label": self._rec.label,
            "draw": self._rec.draw,
            "prompt": prompt,
            "retrieved": retrieved_block(prompt),
            "output": (response.content or "").strip(),
        })
        return response


def retrieved_block(prompt: str) -> str:
    """The retrieved-source section of an adjudication prompt, or ''."""
    if BOUNDARY not in prompt:
        return ""
    after = prompt.split(BOUNDARY, 1)[1]
    return after.split(RETRIEVED_END, 1)[0].strip()


def paragraphs(block: str) -> set[str]:
    return {p.strip() for p in block.split("\n\n") if p.strip()}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b) if (a | b) else 1.0


def rule(title: str) -> None:
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default="transcripts/events/*.jsonl")
    ap.add_argument("--only", required=True,
                    help="1-based turn index, as numbered by "
                         "compare_over_settling.py's report")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--out", default="", help="write every prompt and "
                    "completion here as text (large - includes the full "
                    "source material each call saw)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("CIC_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("set CIC_ANTHROPIC_KEY (or ANTHROPIC_API_KEY)")
    os.environ["ANTHROPIC_API_KEY"] = key

    plan = [(w, t) for w, turns in sessions(args.events) for t in turns]
    want = {int(x) for x in args.only.replace(" ", "").split(",") if x}
    picked = [(i, w, t) for i, (w, t) in enumerate(plan, 1) if i in want]
    if not picked:
        sys.exit(f"turn(s) {sorted(want)} not found in {args.events} "
                 f"({len(plan)} turns available)")

    print(f"{len(picked)} turn(s) x {args.reps} draw(s); "
          f"estimated spend ~${len(picked) * args.reps * 0.011:.2f}")
    if args.dry_run:
        print("\n--dry-run: nothing sent.")
        return

    from app.graph import nodes

    recorder = Recorder(nodes.get_monitoring_llm)
    nodes.get_monitoring_llm = recorder

    transcript = []

    for idx, world_id, text in picked:
        rule(f"TURN {idx}  world={world_id}")
        print(text)

        for draw in range(1, args.reps + 1):
            recorder.draw = draw

            recorder.label = "screen"
            screened = nodes._screen_over_settling(text)
            recorder.label = "adjudicate"
            pair = None
            if screened is not None:
                verdict = nodes._adjudicate_over_settling(text, world_id, screened)
                pair = verdict if isinstance(verdict, str) and verdict else None
            recorder.label = "fold"
            outcome = nodes._folded_over_settling(text, world_id)
            fold = outcome[1] if isinstance(outcome, tuple) else None

            rule(f"TURN {idx}  DRAW {draw}   pair={'CONFIRM' if pair else 'clear'}"
                 f"   fold={'CONFIRM' if fold else 'clear'}")
            for call in recorder.calls:
                if call["draw"] != draw:
                    continue
                print(f"\n----- {call['label'].upper()} said -----")
                print(call["output"])

        by_label = {}
        for call in recorder.calls:
            by_label.setdefault(call["label"], []).append(call)

        rule(f"TURN {idx}  DID THE TWO PATHS SEE THE SAME SOURCES?")
        blocks = [(f"{c['label']}/draw{c['draw']}", paragraphs(c["retrieved"]))
                  for c in recorder.calls if c["retrieved"]]
        if len(blocks) < 2:
            print("  only one source-fed call captured - nothing to compare")
        else:
            sizes = ", ".join(f"{n}:{len(p)}" for n, p in blocks)
            print(f"  chunks retrieved per call  {sizes}")
            print(f"\n  {'':22}" + "".join(f"{n:>18}" for n, _ in blocks))
            for name_a, a in blocks:
                row = "".join(f"{jaccard(a, b):>18.2f}" for _, b in blocks)
                print(f"  {name_a:22}{row}")
            union = set().union(*(p for _, p in blocks))
            common = set.intersection(*(p for _, p in blocks))
            print(f"\n  {len(common)} of {len(union)} distinct chunks were seen by "
                  f"EVERY call ({len(common)/len(union):.0%})")
            if len(common) == len(union):
                print("  Identical material every time: the disagreement is the")
                print("  model's ruling, not what it was ruling against.")
            else:
                print("  The calls judged different material. A verdict difference")
                print("  here is not evidence about the prompt - fix retrieval")
                print("  stability before reading anything into the rulings.")

        if args.out:
            transcript.append((idx, world_id, text, list(recorder.calls)))
        recorder.calls = []

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            for idx, world_id, text, calls in transcript:
                fh.write(f"\n{'='*78}\nTURN {idx}  {world_id}\n{'='*78}\n{text}\n")
                for c in calls:
                    fh.write(f"\n{'-'*78}\n{c['label']} draw {c['draw']}\n{'-'*78}\n")
                    fh.write(f"PROMPT:\n{c['prompt']}\n\nOUTPUT:\n{c['output']}\n")
        print(f"\nfull prompts and completions written to {args.out}")


if __name__ == "__main__":
    main()
