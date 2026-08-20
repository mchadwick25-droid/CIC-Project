# Artifact 5 — Runtime API

Companion to `CiC-Program-Spec.md` (Stage 0.5.5). One product per endpoint; the entrance is a contract with a test that fails on a second writer. All endpoints JSON over HTTPS; errors are RFC-9457 problem+json; the session code travels as `Authorization: Session <code>` where required.

## 1. Endpoints

### Worlds & records (public, read-only)
- `GET /api/worlds` → open worlds from the registry: `[{world_key, display_name, period, place, representative, thinness_statement, living_tradition_flag}]`
- `GET /api/worlds/{key}/doorway` → frame data: starters (per participant type), disclosure texts (P1), methods-page link
- `GET /api/records/{record_id}` → tier-3 record view (repository.json-backed; plain explanation + sources + confidence axes). 404 for non-open worlds.
- `GET /api/methods` → the methods/limitations page content (P9, H1 statement)

### Session lifecycle
- `POST /api/session` `{world_key, participant_type?}` → `201 {session_id, session_code, opening: [facilitator_turns…]}`
  - `world_key` only. Any plural/other product field ⇒ `400` with a plain-text contract message (the single-voice seal, carried). `participant_type` optional, frame-only.
- `POST /api/session/{id}/resume` `{}` + code header → `200 {transcript: [...], state: {...}}` (accumulator restored from the log — never zeroed)
- `POST /api/session/{id}/message` `{text, client_msg_id}` + code header → **SSE stream** (below)
- `GET  /api/session/{id}/transcript` + code header → transcript with speakers + cited sources; `?variant=teaching` (P4) expands citations to edition+section and adds the provenance note
- `POST /api/session/{id}/delete` + code header → `202` starts the deletion workflow (raw purged; derivatives statement returned honestly, spec §8)

## 2. The message stream (SSE)

Event sequence per turn (order guaranteed):

```
event: gate        data: {route}                      # only when a Facilitator turn replaces/precedes the voice
event: speaker     data: {speaker: "facilitator"|"<rep name>"}
event: delta       data: {text: "…"}                  # token deltas; streaming from first token (no buffering — spec principle 1)
event: citations   data: {drawn_on: [...], consulted: [...]}   # after text completes; the badge number is a promise
event: glosses     data: {terms: [...], figures: [...]}
event: offer       data: {quote_offers: [...]}        # licensed sayings offerable this turn (canon offerability)
event: done        data: {turn_no}
```

- Post-`done` there is nothing the participant waits for (no post-turn governance exists, spec principle 2). Wind-down/closing content, when it applies, arrives before `done`.
- Client disconnect mid-stream: the turn still commits from the server side (the answer already generated is real — degraded-round lesson); resume shows it.
- Deterministic grounding checks run before `citations` is emitted (they gate decoration, not text).

## 3. Errors & limits

| condition | response |
|---|---|
| bad/absent session code | `401` (indistinguishable from unknown session; constant-time) |
| unknown session | `401` (same shape) |
| world not open | `409 {title: "world not available"}` |
| package hash mismatch at load | `503 {title: "world temporarily unavailable"}` (Artifact 2 §2 refusal) |
| message cap reached | `200` — a Facilitator turn says so gracefully (never an error to the participant) |
| rate limits | `429`; limits per Artifact 3 §3 + per-session turn pacing (`≥1 in-flight turn per session` rejected with `409`) |
| provider (Bedrock) failure | one silent retry; then a Facilitator apology turn, turn not committed, participant may resend |

## 4. Contract tests (ship with the API)

- Entrance seal: exactly one writer of `session_started`; plural-world request 400s; AST/route test fails on any new writer or field.
- Stream grammar: every turn emits the sequence above; `citations.drawn_on` ⊆ text-grounded set.
- Resume: two processes, same session, full fidelity incl. accumulator.
- Deletion: raw gone, derivatives statement accurate against the corpus lineage index.
