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
`CIC_API_WORLDS_YAML` (default `records/worlds.yaml`), `CIC_API_DEFAULT_WORLD_KEY`
(default `fix`; note that since 2026-08-28 a session must NAME its world —
`POST /api/session` with no `world_key` is refused, so the default is no
longer reachable through the API), and `CIC_ENFORCE_ADMISSION` — the
doors-open switch (`"1"` = only admitted/open worlds are listed or seated;
`"0"` = today's declared deferral, see render.yaml's own comment). The
2026-08-28 audit found this one shipped-but-undocumented; this list is the
config surface, so it lives here now.

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
