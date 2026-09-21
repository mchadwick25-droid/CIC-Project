# engine/api — minimal test backend

A thin FastAPI wrapper around `engine/m4`'s turn loop, built to let a real
HTTP client exercise the real pipeline (world load, gate routing, voice
generation, event log, usage log) against a real Bedrock credential. This is
**not** the participant-facing production system — see
`/root/.claude/plans/linear-popping-dawn.md` for what's deliberately out of
scope (SSE streaming, Postgres, rate limiting, deletion workflow, auth
hardening beyond a session-code header, and the full `Artifact-5`/`Artifact-6`
production topology, which stays gated on Mark's own stage-7.5 design pass).

## Running it

Requires `CIC_API_REGION` — no default, this code refuses to guess an AWS
region. AWS credentials are read the standard way (`AWS_ACCESS_KEY_ID`/
`AWS_SECRET_ACCESS_KEY` in the environment, or any other entry in boto3's
normal credential chain) — this code never reads them itself.

```bash
pip install -r engine/api/requirements.txt
CIC_API_REGION=us-west-2 uvicorn engine.api.app:app --reload --port 8000
```

Optional env vars (all have defaults): `CIC_API_VOICE_MODEL_PATTERN` (default
`us.anthropic.claude-sonnet-4-5`), `CIC_API_SAFETY_MODEL_PATTERN` (default
`us.anthropic.claude-haiku-4-5`), `CIC_API_EVENTS_DB` (default
`./cic_api_events.db`), `CIC_API_USAGE_DB` (default `./cic_api_usage.db`),
`CIC_API_WORLDS_YAML` (default `records/worlds`, a directory - one file per
world since the Library Access Gate registry split), `CIC_API_DEFAULT_WORLD_KEY`
(default `fix`; note that since 2026-08-28 a session must NAME its world —
`POST /api/session` with no `world_key` is refused, so the default is no
longer reachable through the API), and `CIC_ENFORCE_ADMISSION` — the
doors-open switch (`"1"` = only admitted/open worlds are listed or seated;
`"0"` = today's declared deferral, see render.yaml's own comment). The
2026-08-28 audit found this one shipped-but-undocumented; this list is the
config surface, so it lives here now.

`CIC_API_ANON_CAP_ENABLED` (2026-09-21, Tech-Readiness P1-Security item 3 —
`engine/api/anon_cap.py`'s own module docstring has the full rationale):
`"1"` turns on a per-visitor daily cap on session creation and conversation
turns, on top of `ratelimit.py`'s per-IP burst limiter. **Off in every
deployment today** (`render.yaml` declares it explicitly as `"0"`, not left
unset, so the switch has a visible, reviewable home once a decision is
made rather than existing only as an undocumented dashboard toggle) — the
mechanism and its default numbers (`CIC_API_ANON_DAILY_SESSION_LIMIT`,
default 5; `CIC_API_ANON_DAILY_TURN_LIMIT`, default 150) are a proposal
from that audit, not yet a decision Mark has made; see the package's own
`Report.md`. Turning it on **requires** `CIC_API_ANON_VISITOR_SECRET`
(any random string — signs the visitor cookie) to already be set — without
it, `create_app` raises at construction time and the process never comes
up at all (not a graceful "feature disabled" fallback). Set both together,
never the flag alone.

## Pinning `CIC_API_SAFETY_MODEL_PATTERN` (Stage 0d, Build-Plan.md)

Left at its code default, `CIC_API_SAFETY_MODEL_PATTERN` is a loose
substring pattern (`us.anthropic.claude-haiku-4-5`) that
`engine.provider.bedrock.resolve_model_id` matches against whatever
inference profiles actually exist in the account at deploy time. That is
right for a pattern nothing has ever validated against a specific dated
profile — but the safety classifier *has*: `engine/m5/safety_script_run.py`
runs a real, credentialed, by-hand battery (`--all` runs every committed
batch and prints one combined tally against the eventual ~19/20 floor;
never run in CI, never automated) and scores it against a reasoned expected
classification per scenario. A loose pattern could silently start
resolving to a newer dated profile between one tally and the next, meaning
production would run a model version the battery never actually scored.

`render.yaml`'s two services (`cic-engine`, `cic-engine-staging`) both pin
`CIC_API_SAFETY_MODEL_PATTERN` to the exact resolved profile id the last
tally ran against instead — `resolve_model_id` still requires exactly one
live match, so an exact id is refused loudly the day it stops existing in
the account, rather than drifting quietly. **Repin only alongside a fresh
`--all` tally**, never on its own: run

```bash
python -m engine.m5.safety_script_run --region us-east-1 --all
```

by hand with a real credential, confirm the printed tally, then update
both `render.yaml` env-var blocks to the run's own `model_id` and log the
tally's report path in `Ministry/Features/Conversation-Transparency-
Engine/Decision-Log.md`. If the currently-pinned id and the last tally's
own `model_id` ever disagree, that is an escalation (Build-Plan.md Stage
0d's own instruction), not something to quietly repin.

## Endpoints

```bash
# Create a session (world_key optional, defaults to "fix")
curl -s -X POST localhost:8000/api/session -H "Content-Type: application/json" \
  -d '{"world_key": "fix"}'
# -> {"session_id": "...", "session_code": "XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XX"}

# Send a message (session_code from above, as the Authorization header)
curl -s -X POST localhost:8000/api/session/<session_id>/message \
  -H "Authorization: Session <session_code>" -H "Content-Type: application/json" \
  -d '{"text": "Who was Jesus to your people?"}'

# Read the transcript so far
curl -s localhost:8000/api/session/<session_id>/transcript \
  -H "Authorization: Session <session_code>"

# Diagnostic only, table sessions: every round_closed event's own payload
# (reason, turns, governance, and selector_reason when the close was a
# genuine model decision rather than the cap or floor_unmet_exhausted)
curl -s localhost:8000/api/session/<session_id>/round-close-reasons \
  -H "Authorization: Session <session_code>"

# Liveness check (no downstream calls)
curl -s localhost:8000/health
```

## Known gaps (see the plan file for the full list and reasoning)

- **Plain JSON responses, not SSE.** `run_turn()` only ever returns
  fully-assembled text — there's no token-level delta transport in this
  codebase yet, so this doesn't fake one.
- **The Facilitator's own turns are placeholder text.** All seven routing
  actions have content, but `engine/m4/facilitator_turns.py` carries a craft
  note saying so plainly: the strings are honest and minimal, and they are
  not finished participant-facing text.
- **Track B does not act on its accumulator.** `safety_state` events are
  written from 2026-08-24 and the accumulator folds and survives resume, but
  no threshold reads it — Track B still fires on a single
  `HARMFUL_DYNAMIC_SIGNAL`, and the sealed safety call is still given an
  empty window and an empty accumulator.
- **This tool bypasses the registry's `built` vs `admitted`/`open`
  distinction** for testing purposes. It must never be treated as, or reused
  as, a participant-facing gate.
