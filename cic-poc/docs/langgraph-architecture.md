# Backend Architecture

*Replaces a previous version of this document that described a conversation
loop the code has never executed — verified wrong in nearly every particular
by the 2026-08-05 full-system review (Engineering, finding P0-4), and
confirmed independently line-by-line while writing this replacement. If
anything below and the code disagree, the code is right; open an issue
against this file rather than trusting it blindly, the same lesson that
produced it.*

## The one true fact: the LangGraph graph is not the conversation

`app/graph/builder.py` defines a `StateGraph` with six nodes and a docstring
diagram showing a `wait_for_input → representative_engages →
facilitator_monitors → {reroot, wait, close}` loop. That loop **has never
run**. The real edges compiled into the graph are:

```
START → facilitator_receives → facilitator_handoff → END
```

`facilitator_handoff` edges straight to `END` (`builder.py:80`) — the
handoff never routes into `representative_engages` or anything else. The
other four nodes (`representative_engages`, `facilitator_monitors`,
`facilitator_reroots`, `facilitator_closes`) are registered in the graph but
have no path into them from the edges the graph actually compiles.

The graph is invoked **exactly once per session**, at session start
(`app/main.py:402-403`, inside session creation): it produces the opening
welcome and the Representative's handoff line, then returns. Every
subsequent participant turn — the entire live conversation — is orchestrated
by hand-written endpoint logic in `main.py`, not by `graph.invoke()` again.
`builder.py:12` still imports `route_after_input`; nothing in the file calls
it.

**Practical upshot for a new engineer:** don't go looking in the graph for
how a turn works. `langgraph` remains a dependency and the graph still runs
once for the welcome message, but the actual control flow is below.

## What actually runs a turn

Two FastAPI endpoints in `app/main.py` handle live conversation (session
start, and each subsequent message). Both endpoints share the same
per-turn machinery through `app/graph/governance.py`, which used to be
duplicated inline in each endpoint and was extracted into one module — a
record/replay parity harness (`app/graph/replay/`) exists specifically to
prove that extraction was behavior-preserving.

Per turn, roughly:

1. **Governance pre-turn checks** (`governance.py`) — the intercept chain:
   relational-safety (Acute Distress / Harmful Dynamic), frame-breaking,
   and other pre-turn interrupts that can pre-empt normal generation.
2. **Generation** (`app/graph/nodes.py`) — speaker selection among worlds at
   the table, retrieval-augmented response generation, and, after a
   response, table-check signal detection (`governance.run_table_checks`).
   17+ distinct signal types are emitted here (drift categories, repair
   triggers, closing-synthesis flags, and more) — the old doc's list of
   seven is stale.
3. **Post-round governance** (`governance.run_post_round_governance`) —
   folds any queued guidance and signals into state for the next turn.
4. **Event log** (`app/graph/events.py`) — an append-only event store is
   the actual state-projection mechanism (`project()`/`project_fresh()`),
   replacing an earlier hand-patched read-modify-write pattern. Not
   mentioned at all in the old version of this doc.

None of this is graph-node dispatch; it's plain function calls from the
endpoint bodies through `governance.py` into `nodes.py`.

## `ConversationState`

`app/graph/state.py`, `@dataclass class ConversationState` — **28 declared
fields** (counted directly from the AST while writing this, not carried over
from any other document's count). Includes the full relational-safety block
(`track_a_active`, `track_a_severity`, `track_b_active`,
`relational_safety_tags`, `relational_safety_deescalation_count`),
`closing_stage`, `pending_guidance`, `surfaced_chunk_ids`,
`private_directive`, `register_note`, and `session_token` — none of which
existed in the 11-field version this document used to describe.

## Retrieval

`app/rag/pipeline.py` is the one candidate-to-decision pipeline both the
lexicon and story retrievers run (a 2026 fix that collapsed two ~95-line
near-duplicates into one, after that duplication caused a real bug that had
to be fixed twice). The stack, in order:

BM25 + dense retrieval → weighted RRF → one-hop `Related-Terms` graph
expansion → adaptive relevance floor → MMR → a **local, zero-API-cost
cross-encoder** (`app/rag/cross_encoder.py`) for final relevance scoring →
one Haiku call only for the residual guard cases the cross-encoder can't
resolve on its own.

There is no per-candidate LLM evaluation loop. That pattern (an LLM call in
a loop over every retrieved candidate) is two generations obsolete — it was
batched, then replaced by the local cross-encoder — and the old version of
this document's RAG diagram described exactly that retired loop as current.

## Module map

| Module | Owns |
|---|---|
| `app/main.py` | The two live-conversation endpoints; session start; the SPA catch-all |
| `app/graph/events.py` | The append-only event log and state projection |
| `app/graph/governance.py` | The intercept chain, table-check signals, post-round folding |
| `app/graph/nodes.py` | Generation, speaker selection, signal detection |
| `app/graph/builder.py` | The vestigial welcome-only graph (see above) |
| `app/rag/pipeline.py` | The shared retrieval pipeline |
| `app/prompts/` | Facilitator and Representative prompt templates |
| `app/world_manifest.py` | The single source of truth for the six live worlds |

Six worlds are live today (`app/world_manifest.py`), not the one this
document used to name as an example.

## If you're extending this document

Prefer adding a short, verifiable fact over a diagram — the previous version
of this file was a detailed, professional-looking diagram that was wrong
almost everywhere it could be checked, and its polish is exactly what let it
go unquestioned for weeks. A plain module map with real line references is
harder to make convincingly wrong.
