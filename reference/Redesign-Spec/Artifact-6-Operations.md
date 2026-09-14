# Artifact 6 — Non-Functionals, Threat Model, Deployment & Degraded Modes

Companion to `CiC-Program-Spec.md` (Stage 0.5.6). Defaults sized for pilot; every number is a declared target, re-baselined on real measurements (never silently edited — changes are commits with reasons).

## 1. NFR table

| dimension | pilot target | design ceiling | notes |
|---|---|---|---|
| Availability | 99.5% monthly | 99.9% | single-region; a conversation product, not a pager |
| Time-to-first-token | p95 ≤ 3.5 s | ≤ 2.5 s | gate (concurrent, ≤2.5s) + retrieval + generation start |
| Turn completion | p95 ≤ 20 s | — | streaming makes perceived latency the TTFT number |
| Concurrent sessions | 50 | 1,000 | stateless instances + shared store scale horizontally |
| Worlds resident per instance | 8 | 24 | per-world budget ≤ 300 MB (indexes + chunks + prompt); LRU eviction; "idle" = no session activity for 30 min |
| World cold load | p95 ≤ 5 s | ≤ 2 s | pull from S3 + index mmap; a participant seating a cold world sees the doorway meanwhile |
| Transcript store | RPO ≤ 5 min, RTO ≤ 4 h | — | PITR + daily snapshots; quarterly restore test |
| Cache economics | re-measure | — | 16× pooling was measured on the old warm-everything deployment (all six worlds resident); lazy-load changes it; measured at stage 6 on Bedrock, quoted with the band |

## 2. Threat model (one page)

**Assets:** transcripts (intimate, possibly crisis-adjacent), the record corpus (integrity), the fleet's voices (prompt integrity), AWS credentials/spend.

| threat | control |
|---|---|
| Session-code guessing | 128-bit entropy; hashed at rest; constant-time compare; 5/min + 20/day per-IP attempt limits; 401 indistinguishable from unknown session |
| Code shoulder-surfing / shared devices | keep-it-private warning at issuance; `session_resumed` visible in-conversation ("this conversation was reopened") |
| Transcript exfiltration at rest | encryption at rest (RDS/S3 default KMS); no PII index; least-privilege DB roles |
| Prompt injection via participant text | participant text is data everywhere: the gate's schemas are closed-form; directives are code-assembled, never model-composed; retrieval serves corpus-only content; no tool-use in the conversation path |
| Poisoned content via records | the admin plane is **git + CI only** — no runtime write API exists; reviewed commits; package hash chain (Artifact 2) makes tampering post-build detectable at load |
| Model-output injection (voice instructing the client) | client renders text only; citations/glosses come from server-side checks, not model markup |
| Spend attack / runaway cost | per-session turn cap, **10 turns, decided by Mark 2026-08-25** (was `DECIDABLE`, default 40) after a live memory-growth measurement (`engine/m8/live_memory_growth_run.py`) showed real per-turn cost climbing, not flat, as full-session memory accumulates — depth was kept (no history window/truncation), the turn count was capped instead; implemented `engine/m4/turn.py` (`SESSION_TURN_CAP`), graceful redirect via `engine/m4/facilitator_turns.session_cap_turn` (draft text, not yet Mark-approved), session close wired in `engine/api/wiring.py`; per-IP session-creation limits; AWS **Budget Action with a deny policy** (alerts alone don't stop spending) as backstop; per-participant cost attribution (M8) makes anomalies visible |
| Availability attack | provider WAF/rate limits at the edge; no unauthenticated expensive endpoints (session creation is the costliest and is limited) |

**PII posture:** the primary event log holds what participants typed (unavoidably possibly-personal). Access is operator-only, least-privilege, audited. The anonymization pass strips identifiers before ANY derived corpus; derived corpora carry lineage for deletion computation (spec §8). Jurisdiction stance: retention/deletion designed to GDPR-shaped norms (delete-on-request, honest scope) without claiming formal compliance — `DECIDABLE` with counsel before public availability; noted on the methods page.

## 3. Deployment

**Frontend/backend split (spec principle 16):** three deployable pieces. (1) The **public site** (Atlas, landing page with the Representative gallery, program page of world cards) — static, CDN-served, buildable from the open-worlds view; hostable anywhere static assets host. (2) The **interview frontend** — a static SPA talking to the backend only through the Artifact-5 API (CORS-configured; deep links `/world/{key}` from the site and Atlas). (3) The **backend** — the runtime container + Postgres + object storage. No server-side rendering coupling the tiers; the API is the whole contract between them.

**Portability rules:** portable shapes only — OCI container, standard Postgres (no proprietary extensions), S3-compatible object-storage API; IaC so the stack re-creates elsewhere; every provider-proprietary dependency (Bedrock, Budget Actions, CloudFront) is listed here with its exit: Bedrock → any Messages-API provider via the one model seam (preflight required: caching engages, usage fields present, invoice reconciles); Budget Action → provider billing caps + the app's own session caps (primary anyway); CloudFront → any CDN. The model seam normalizes usage accounting so M8's numbers stay comparable across providers — that comparability is what makes a future cost-driven move a decision instead of a project.

- **Topology (current):** AWS, single region. Runtime container (ECS Fargate or App Runner — `DECIDABLE` at stage 5, App Runner default for a solo operator); RDS Postgres; S3 for packages; CloudFront in front; Bedrock for all model calls (Artifact 4 / spec §7 client rules).
- **Environments:** `staging` (fixture world + Alexandria candidate packages) and `prod`. IaC from day one (CDK or Terraform, `DECIDABLE`); no console-clicked resources.
- **CI:** on every commit — schema validate, gates selftest (pass clean fixture, fail every seeded-defect fixture), compiler determinism (twice, byte-identical), package staleness sweep, unit + contract tests (Artifact 5 §4), frontend typecheck. Nightly — reader battery, cost parity check against raw usage shapes. Pre-deploy — the applicable battery for what changed (safety script for gate/safety changes; admission re-runs per Artifact 2 §4).
- **Release:** immutable images; deploy = pointer move; rollback = previous image + registry pin (one step, rehearsed). Gate changes canary-first (Artifact 4 §5). Model/provider switches land **last and alone** (spec principle 11).
- **Ops for one human:** paging only on: two consecutive degraded gate turns, safety-call failure rate > 1%, store unavailability, budget action trip. Everything else is a daily digest. The solo-founder SPOF (Mark's reading as the quality instrument; Mark as operator) is an accepted, stated risk.

## 4. Degraded-mode matrix

| failure | participant experience | system behavior |
|---|---|---|
| Bedrock down | Facilitator chrome: "we're having trouble speaking just now — your conversation is saved; your code will bring you back" | no queueing; turns not committed; health page reflects it |
| Store (Postgres) down | new sessions refused with honest message; in-flight turns complete but cannot commit → participant told to keep their code | no silent data loss; instances hold no authoritative state |
| Gate reader down | conversation continues (pass-through, no directive) | `degraded` flags; priority audit; page on repetition |
| Safety call down | conversation continues; async re-classification; late-fire interjects | stated fail-open + never-silent rule (Artifact 4 §4) |
| One world's package corrupt | that world "temporarily unavailable"; others unaffected | hash-mismatch refusal; page operator |
| S3 down (cold loads only) | warm worlds unaffected; cold worlds unavailable with honest doorway message | retry with backoff |

## 5. Deletion workflow (spec §8, operational form)

`deletion_requested` event → within 72 h: raw events for the session purged (hard delete + backup exclusion note: purged rows fall out of backups at retention horizon, stated honestly on the methods page); lineage index consulted → derived corpus entries from this session either already-anonymized (survive, per ruling) or, if not yet anonymized, purged with the raw. Completion is verifiable by re-presenting the code: `401` as if the session never existed.
