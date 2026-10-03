# engine/api — minimal test backend

A thin FastAPI wrapper around `engine/m4`'s turn loop, built to let a real
HTTP client exercise the real pipeline (world load, gate routing, voice
generation, event log, usage log) against a real Bedrock credential. This is
**not** the participant-facing production system — see
`/root/.claude/plans/linear-popping-dawn.md` for what's deliberately out of
scope (SSE streaming, Postgres, rate limiting, deletion workflow, auth
hardening beyond a session-code header, and the full `Artifact-5`/`Artifact-6`
production topology, which is not yet built).

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
(default `fix`; note that a session must NAME its world —
`POST /api/session` with no `world_key` is refused, so the default is not
reachable through the API), and `CIC_ENFORCE_ADMISSION` — the
doors-open switch (`"1"` = only admitted/open worlds are listed or seated;
`"0"` = today's declared deferral, see render.yaml's own comment). This is
the config surface for the running service; it lives here so it stays
documented.

`CIC_API_ANON_CAP_ENABLED` (`engine/api/anon_cap.py`'s own module
docstring has the full rationale):
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
tally's report path with the feature notes in
`Build/Ministry/Features/Conversation-Transparency-Engine/`. If the currently-pinned id and the last tally's
own `model_id` ever disagree, escalate to the project lead; do not repin
quietly.

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

# The same message as an event stream (needs CIC_API_STREAMING on)
curl -sN -X POST localhost:8000/api/session/<session_id>/message \
  -H "Authorization: Session <session_code>" -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" -d '{"text": "Who was Jesus to your people?"}'
# -> event: sentence / data: {"index", "lead", "text", "text_start", "text_end", "elements", "cards"}
#    event: done     / data: {...}           (the finished turn)

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

## Streaming

By default a message returns one JSON response. With `CIC_API_STREAMING` on,
a client that sends `Accept: text/event-stream` gets a `sentence` event for
each sentence as the voice finishes it (`engine/m4/sentence_stream.py`), then a
`done` event carrying the same body the JSON response would have. A sentence
event carries the display text before it (`lead`), its own text and offsets in
the finished reply, and the quote and story marks the finished plan gives it,
with their source cards. Term and figure marks, the mark cap, and citations
added by attachment arrive in `done`, whose plan is authoritative. A failure
after the stream began is an `error` event: `{code, status, detail}`, where
`detail` is the string the JSON response would carry and `code` is stable
(`invalid_session`, `session_closed`, `message_too_long`, `round_open`,
`advance_in_flight`, `duplicate_message`, `world_unavailable`,
`provider_failed`, `internal`).

Only interview turns answered by the voice stream. A Facilitator turn, a table
session, a bridge turn, a first other-tradition ask with self-revision on, and
any turn with an enforcement flag on return whole.

## What to know when testing

- **The Facilitator's own turns are placeholder text.** All seven routing
  actions have content, but `engine/m4/facilitator_turns.py` carries a craft
  note saying so plainly: the strings are honest and minimal, and they are
  not finished participant-facing text.
- **Track B does not act on its accumulator.** `safety_state` events are
  written and the accumulator folds and survives resume, but
  no threshold reads it — Track B still fires on a single
  `HARMFUL_DYNAMIC_SIGNAL`, and the sealed safety call is still given an
  empty window and an empty accumulator.
- **This tool bypasses the registry's `built` vs `admitted`/`open`
  distinction** for testing purposes. It must never be treated as, or reused
  as, a participant-facing gate.
