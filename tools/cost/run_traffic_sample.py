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
    PYTHONPATH=. python3 ../../tools/cost/run_traffic_sample.py --out /tmp/sample.log

    python3 ../../tools/cost/analyze_usage_log.py      /tmp/sample.log
    python3 ../../tools/cost/analyze_over_settling.py  /tmp/sample.log

Cost: roughly $0.04 per turn on Sonnet 5, so ~$2 for the 48-turn default.
--dry-run prints the plan and spends nothing. --max-spend aborts if the
running total passes a ceiling.

WHY 48 TURNS AND NOT 200
------------------------
The bar is not a round number, it is whatever separates the fire rate from
the 60% break-even. At a rate near 78% a 48-turn sample already excludes 60%
(95% CI roughly 65%-87%); the per-turn cost and token shape converge far
sooner than that. Only a rate sitting close to the threshold needs hundreds
of turns - and analyze_over_settling.py now says so itself, reporting the
interval and the n that would resolve it rather than enforcing a fixed bar.
Run the default, read the verdict, extend only if it comes back INCONCLUSIVE.

WHY THE SESSIONS CONCENTRATE ON TWO WORLDS
------------------------------------------
The cache pools on the prompt prefix, which is per-world. Spreading four
sessions over six worlds would measure four cold caches and prove nothing
about pooling. Two worlds x two back-to-back sessions inside the 1h window
is the smallest shape where the second session shows the pooled read.
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


def preflight() -> None:
    """Load the two retrieval models before spending anything.

    They are fetched from huggingface.co on first use and cached. If that
    host is unreachable the failure otherwise lands mid-run, after turns
    have already been billed, as a bare httpx.ProxyError from inside the
    graph. Paying for a partial sample and then throwing it away is the
    worst outcome available, so buy the check up front - it is free, and
    on a warm cache it costs a second.
    """
    # Import every app module first. Several deps are imported lazily inside
    # functions (app/rag/hybrid.py's rank_bm25 is imported inside
    # candidate_search), so app boot, /health and /api/session/start all pass
    # without them and the failure lands on the first real turn - after the
    # session started and the facilitator calls were billed.
    print("preflight: importing app modules ...", flush=True)
    import importlib, pkgutil, pathlib
    app_dir = pathlib.Path(__file__).resolve().parents[2] / "cic/runtime/app"
    missing = []
    for mod in pkgutil.walk_packages([str(app_dir)], prefix="app."):
        try:
            importlib.import_module(mod.name)
        except ModuleNotFoundError as exc:
            missing.append(f"{mod.name}: {exc}")
        except Exception:
            pass          # import-time errors that are not missing deps are
                          # the app's business, not this check's
    if missing:
        sys.exit("preflight FAILED - missing dependencies:\n  "
                 + "\n  ".join(missing)
                 + "\n\npip install -r cic/runtime/requirements.txt"
                   "\nNothing was spent.")

    print("preflight: loading retrieval models ...", flush=True)
    try:
        from app.rag.embeddings import get_shared_embeddings
        get_shared_embeddings().embed_query("preflight")
        from app.rag.cross_encoder import score_candidates  # noqa: F401
        from sentence_transformers import CrossEncoder
        CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2").predict(
            [("preflight", "preflight")])
    except ModuleNotFoundError as exc:
        sys.exit(f"preflight FAILED: {exc}\n"
                 "Run from cic/runtime with PYTHONPATH=. and the deps in\n"
                 "cic/runtime/requirements.txt installed. Nothing was spent.")
    except Exception as exc:
        sys.exit(
            f"preflight FAILED: {type(exc).__name__}: {exc}\n\n"
            "The retrieval stack needs all-MiniLM-L6-v2 and\n"
            "cross-encoder/ms-marco-MiniLM-L-6-v2 from huggingface.co.\n"
            "A 403 here means the network policy denies that host - run this\n"
            "where HF is reachable, or warm the cache there once and copy\n"
            "~/.cache/huggingface across. Nothing was spent."
        )
    print("preflight: OK\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", type=int, default=4,
                    help="4 x 12 turns = 48; enough to separate a ~78%% fire "
                         "rate from the 60%% break-even (see module docstring)")
    ap.add_argument("--turns", type=int, default=12)
    ap.add_argument("--worlds", default=None,
                    help="comma-separated world ids to cycle through. "
                         "Default: the first two, so sessions pool on a warm "
                         "cache instead of measuring cold prefixes.")
    ap.add_argument("--out", default="traffic_sample.log")
    ap.add_argument("--max-spend", type=float, default=15.0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    key = os.environ.get("CIC_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("set CIC_ANTHROPIC_KEY (or ANTHROPIC_API_KEY)")
    os.environ["ANTHROPIC_API_KEY"] = key

    preflight()

    from app.world_manifest import all_world_ids
    known = all_world_ids()
    if a.worlds:
        worlds = [w.strip() for w in a.worlds.split(",") if w.strip()]
        unknown = [w for w in worlds if w not in known]
        if unknown:
            sys.exit(f"unknown world id(s): {', '.join(unknown)}\n"
                     f"known: {', '.join(known)}")
    else:
        worlds = known[:2]
    # Consecutive sessions on the SAME world, not round-robin: the pooled
    # cache read only shows up when the second session starts inside the
    # first's 1h window on the same prefix.
    per_world = -(-a.sessions // len(worlds))
    plan = [w for w in worlds for _ in range(per_world)][:a.sessions]
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
