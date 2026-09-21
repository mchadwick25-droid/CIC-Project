#!/usr/bin/env python3
"""Runner for probes.yaml (Tech-Readiness P1-Security item 4).

Sends every probe in probes.yaml into a real engine/api instance over HTTP
and records the response excerpt, one JSON report line per probe. Probes
sharing a `thread` value are sent in order into the SAME session (a
follow-up conversation); every other probe gets its own fresh session.

This script makes real API calls and, against a real Bedrock-backed
deployment, real model calls that cost real money - it does NOT enforce
the $5 cost ceiling itself (this process can't see Bedrock billing), so
whoever runs it against a live-model target is responsible for stopping
if that ceiling is at risk (40 probes x a few short turns each, against
Haiku/Sonnet-classed models, is expected to land well under $5, but this
is a design expectation, not a metered guarantee).

Usage:
    python run_probes.py --base-url http://localhost:8000 --world fix \
        --out results.json [--admin-token TOKEN]

Against the local dev server (engine/api/dev_server.py, a fixed
FakeBedrockClient - see its own module docstring), every response is the
SAME canned string regardless of probe content. That makes this run
"structural only": it proves the probe harness itself (session creation,
auth, threading, transcript capture) works end-to-end - it proves NOTHING
about whether a real model resists any of these probes. Report it as such;
never present a fake-client run as a security finding either way.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

PROBES_PATH = Path(__file__).parent / "probes.yaml"


def _post(base_url: str, path: str, body: dict, session_code: str | None = None) -> tuple[int, dict]:
    req = urllib.request.Request(
        f"{base_url}{path}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", **({"Authorization": f"Session {session_code}"} if session_code else {})},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read() or b"{}")


def _voice_excerpt(response_body: dict, limit: int = 400) -> str:
    voice = response_body.get("voice") or {}
    facilitator = response_body.get("facilitator")
    text = (voice.get("text") if isinstance(voice, dict) else None) or ""
    fac_text = ""
    if isinstance(facilitator, dict):
        fac_text = facilitator.get("text") or ""
    elif isinstance(facilitator, list):
        fac_text = " | ".join(f.get("text", "") for f in facilitator if isinstance(f, dict))
    combined = " ".join(p for p in (fac_text, text) if p)
    return combined[:limit]


def run(base_url: str, world: str, out_path: Path) -> None:
    probes = yaml.safe_load(PROBES_PATH.read_text())["probes"]
    threads: dict[str, dict] = {}
    results = []

    for probe in probes:
        thread_key = probe.get("thread")
        if thread_key and thread_key in threads:
            session = threads[thread_key]
        else:
            status, body = _post(base_url, "/api/session", {"world_key": world})
            if status != 201:
                results.append({**probe, "error": f"session creation failed: {status} {body}"})
                continue
            session = {"session_id": body["session_id"], "session_code": body["session_code"]}
            if thread_key:
                threads[thread_key] = session

        status, body = _post(
            base_url, f"/api/session/{session['session_id']}/message", {"text": probe["text"]}, session_code=session["session_code"],
        )
        results.append(
            {
                "id": probe["id"],
                "category": probe["category"],
                "thread": thread_key,
                "text": probe["text"],
                "expect": probe["expect"],
                "http_status": status,
                "routing_action": body.get("routing_action"),
                "routing_reason": body.get("routing_reason"),
                "response_excerpt": _voice_excerpt(body) if status == 200 else json.dumps(body)[:400],
            }
        )
        print(f"{probe['id']:8s} status={status} routing={body.get('routing_action')}", file=sys.stderr)

    out_path.write_text(json.dumps(results, indent=2))
    print(f"\n{len(results)} probes run, written to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--world", default="fix")
    parser.add_argument("--out", type=Path, default=Path("probe_results.json"))
    args = parser.parse_args()
    run(args.base_url, args.world, args.out)
