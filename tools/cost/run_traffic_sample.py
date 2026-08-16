#!/usr/bin/env python3
"""Drive N real conversations through the app and capture the cost/decision logs.

Produces the traffic sample the cost review is blocked on:
  * tools/cost/analyze_usage_log.py       -> true $/turn, cache pooling factor
  * tools/cost/analyze_over_settling.py   -> screen fire rate and confirm rate

MUST BE RUN WHERE huggingface.co IS REACHABLE. The retrieval stack needs
all-MiniLM-L6-v2 (embeddings) and cross-encoder/ms-marco-MiniLM-L-6-v2, which
are downloaded on first use and then cached. The Claude Code web sandbox
denies huggingface.co by egress policy, which is why this is a script rather
than a result.

    export CIC_ANTHROPIC_KEY=sk-ant-...          # or ANTHROPIC_API_KEY
    cd cic/runtime
    PYTHONPATH=. python3 ../../tools/cost/run_traffic_sample.py --sessions 17 --out /tmp/sample.log

    python3 ../../tools/cost/analyze_usage_log.py      /tmp/sample.log
    python3 ../../tools/cost/analyze_over_settling.py  /tmp/sample.log

Cost: roughly $0.04 per turn on Sonnet 5, so ~$8 for 200 turns. --dry-run
prints the plan and spends nothing. --max-spend aborts if the running total
passes a ceiling.

Sessions are spread across all six worlds and run back to back, which is what
makes the pooling factor meaningful: several sessions on one world inside the
1h cache window is the production shape a single-session test cannot show.
"""
from __future__ import annotations
import argparse, logging, os, sys, time

# 12 newcomer questions - deliberately ordinary traffic, not seeded defects.
# The confirm rate this measures is only meaningful on questions a real
# visitor would ask.
QUESTIONS = [
    "I don't really know anything about your world. Where should we start?",
    "What did an ordinary week look like for someone in your community?",
    "What did you believe happened after death?",
    "How did someone join you? Was there a moment they became one of you?",
    "What did you argue about among yourselves?",
    "Who held authority, and how did anyone come to have it?",
    "What did you do when someone in the community was dying?",
    "Was there anything about your own community that troubled you?",
    "How did you read your scriptures? What did you look for in them?",
    "What would an outsider have found strangest about you?",
    "How certain are you about the things you've told me?",
    "If I remembered one thing from this conversation, what should it be?",
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", type=int, default=17,
                    help="17 x 12 turns = 204, just over the 200-turn bar")
    ap.add_argument("--turns", type=int, default=12)
    ap.add_argument("--out", default="traffic_sample.log")
    ap.add_argument("--max-spend", type=float, default=15.0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    key = os.environ.get("CIC_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("set CIC_ANTHROPIC_KEY (or ANTHROPIC_API_KEY)")
    os.environ["ANTHROPIC_API_KEY"] = key

    from app.world_manifest import all_world_ids
    worlds = all_world_ids()
    plan = [worlds[i % len(worlds)] for i in range(a.sessions)]
    total = a.sessions * a.turns
    print(f"{a.sessions} sessions x {a.turns} turns = {total} turns")
    print(f"worlds: {', '.join(f'{w}x{plan.count(w)}' for w in worlds)}")
    print(f"estimated spend ~${total * 0.04:.2f} (ceiling ${a.max_spend:.2f})")
    if a.dry_run:
        print("\n--dry-run: nothing sent."); return

    # Capture BOTH structured log streams the analyzers read.
    handler = logging.FileHandler(a.out, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    for name in ("cic.llm_usage", "cic.over_settling_decision"):
        lg = logging.getLogger(name)
        lg.setLevel(logging.INFO)
        lg.addHandler(handler)

    from fastapi.testclient import TestClient
    from app.main import app

    spent_turns = 0
    with TestClient(app) as client:
        for n, world in enumerate(plan, 1):
            r = client.post("/api/session/start", json={"world_id": world})
            if r.status_code != 200:
                print(f"  session {n}: start failed {r.status_code} {r.text[:160]}")
                continue
            body = r.json()
            sid = body["session_id"]
            # /api/session/{id}/message enforces possession of the token minted
            # at start (app/session_auth.py); without the header every turn is
            # a 403 and the run silently measures nothing.
            hdrs = {"X-Session-Token": body.get("session_token", "")}
            print(f"[{n}/{a.sessions}] {world}  session={sid}")
            for q in QUESTIONS[:a.turns]:
                t0 = time.time()
                rr = client.post(f"/api/session/{sid}/message",
                                 json={"message": q}, headers=hdrs)
                spent_turns += 1
                ok = "ok" if rr.status_code == 200 else f"HTTP {rr.status_code}"
                print(f"     {ok:9} {time.time()-t0:5.1f}s  {q[:52]}")
                if rr.status_code != 200:
                    print(f"       {rr.text[:200]}")
                if spent_turns * 0.04 > a.max_spend:
                    print(f"\nSPEND CEILING ${a.max_spend} reached at {spent_turns} turns - stopping.")
                    return
    print(f"\n{spent_turns} turns written to {a.out}")
    print(f"  python3 tools/cost/analyze_usage_log.py {a.out}")
    print(f"  python3 tools/cost/analyze_over_settling.py {a.out}")


if __name__ == "__main__":
    main()
