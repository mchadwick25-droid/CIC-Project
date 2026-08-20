# Artifact 3 — Session Event Log: Catalog, Store, Guarantees

Companion to `CiC-Program-Spec.md` (Stage 0.5.3). Session state is an append-only event log; all state is a projection (proven pattern — "an append has no read-modify-write cycle at all").

## 1. Store — DECIDED (default)

**Managed Postgres** (single primary, PITR enabled). One table:

```sql
CREATE TABLE session_events (
  session_id  uuid        NOT NULL,
  seq         integer     NOT NULL,          -- per-session, monotonic from 1
  event_uuid  uuid        NOT NULL UNIQUE,   -- idempotency key (client/worker supplied)
  event_type  text        NOT NULL,
  payload     jsonb       NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (session_id, seq)
);
```

- **Ordering guarantee:** per-session total order via `(session_id, seq)`; append = `INSERT` with the next seq; a unique-violation on seq means a concurrent writer — re-read and retry (bounded, 3×). No cross-session ordering is promised or needed.
- **Idempotency:** retried appends carry the same `event_uuid`; a duplicate insert is a silent success.
- **Horizontal scaling:** any instance can serve any session (the 404-on-second-instance failure is designed out). No process-local session state beyond caches that rebuild from the log.
- Rate limiting also moves to shared state (same store or Redis) — "the fix is the same fix, at the same time."

## 2. Event catalog (v1 — exhaustive; adding a type is a reviewed change)

| type | payload (required keys) | notes |
|---|---|---|
| `session_started` | world_key, mode(`interview`), frame(type or null), code_hash, package_manifest_hash | the ONLY writer of world/mode — the entrance contract; a test fails on a second writer |
| `participant_message` | text, client_msg_id | words never rewritten |
| `gate_decision` | asks[], register, out_of_scope{class,pressed}, modern_terms[], safety{signal,confidence}, route, directive, degraded(bool) | one per message; `degraded:true` when a gate call failed/timed out (audit flag) |
| `facilitator_turn` | kind(`door`\|`threshold`\|`safety`\|`bridge`\|`close`), text | visible turns only; the seam never silent-edits |
| `voice_turn` | speaker, text, citations[], glosses[], quote_offers[], attempts_meta | the answer as streamed |
| `retrieval_surfaced` | chunk_ids[] | feeds session exclusion (Q4 non-repetition) |
| `safety_state` | track, level, accumulator{...} | **accumulator lives here — resume-safe by construction** |
| `guidance_… ` | — | (reserved; no live guidance exists post-Q1) |
| `turn_committed` | turn_no | closes a round |
| `session_resumed` | device_hint | resume by code (Q5a) |
| `deletion_requested` | — | starts the deletion workflow (Artifact 6 §4) |
| `session_closed` | reason(`participant`\|`idle`\|`cap`) | close is a bonus, never a container |

Projection (`get_state`) folds the log into a fresh state object per request — never a shared mutable instance. `project_fresh` from the store alone must reconstruct any session (tested in stage 5: resume across two processes).

## 3. Session code

- 128-bit CSPRNG, Crockford base32 (26 chars, grouped for humans: `XXXX-XXXX-XXXX-XXXX-XXXX-XX`). Shown from turn one (P3).
- Stored **hashed** (SHA-256; codes are high-entropy so no slow hash needed). Possession = resume + transcript + deletion; the UI carries the keep-it-private warning.
- Rate limits on code attempts: 5/min/IP, 20/day/IP; constant-time compare; failures indistinguishable from unknown-session.

## 4. Durability & the transcript store

- The event log IS the transcript of record (the promise of durability kept — no write-only mirror, no second source of truth).
- Backups: PITR + daily snapshots; **RPO ≤ 5 min, RTO ≤ 4 h** (Artifact 6 NFRs); restore is tested quarterly (a restore never tested is a backup that doesn't exist).
- The audit (M7) and learning corpus read from the log via the anonymization pass; derived corpora record their source `(session_id, seq)` ranges so deletion scope (Q9) is computable.
