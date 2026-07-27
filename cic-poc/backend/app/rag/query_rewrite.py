"""S3.5 - conversational query rewriting (Pass 1 R9). MODULE ONLY as of
2026-07-27: authored while the API usage limit blocks live verification
(resets 2026-08-01 00:00 UTC); NOT yet wired into any live path, so main
stays deployable. The wiring plan below executes at the reset, with the
step's G (reactive cases), the safety rerun, and B-RETR-POST-P3.

What R9 replaces (both are the same defect - a retrieval query polluted
with text written for no world in particular or for a different world):

1. The reactive-turn concatenation (`nodes.py`,
   `_prepare_representative_turn`): today a reactive turn's retrieval
   query is `f"{participant_msg}\\n\\n{other_rep_name} just said:
   {other_rep_msg}"` - another world's full turn drives this world's
   vector search. Measured consequence (S3.4 gate artifact): must-docs
   score at cross-encoder noise level on these queries; the interim
   reactive-marker lenient floor in cross_encoder.py exists solely
   because of this shape and dies with it.
2. The bridges' query replacement (`modern_term_bridge.py` and
   `epistemology_bridge.py` - two of the three classify-then-route
   intercepts, same pattern per F8): a false-positive bridge currently
   searches the world's lexicon against reframe text written for no
   world in particular.

The rewrite: ONE Haiku call producing a standalone, world-appropriate
retrieval query - what is this participant actually asking, in terms
this world's own material would be indexed under - replacing the
concatenation/replacement at those three call sites.

WIRING PLAN (executes at the API reset - kept here so the resuming
session needs no archaeology):
- nodes.py `_prepare_representative_turn`: replace the
  `retrieval_query = f"..." ` concatenation with
  `rewrite_query(...)`; on rewrite failure the fallback below returns
  the old concatenation unchanged (fail-open to today's behavior).
- modern_term_bridge.py / epistemology_bridge.py: at the point each
  substitutes its reframe text as the retrieval query, pass the
  original participant message + reframe through rewrite_query instead.
- cross_encoder.py: after wiring, the reactive-marker lenient floor is
  retired (the marker no longer occurs); harness re-run must show the
  reactive-turn class recovering (Alexandria/Desert MRR cells - the
  named targets).
- Harness: reactive golden cases get fixture rewrites generated ONCE
  live and committed (fixture-from-live), so the harness stays
  deterministic; the fixtures are data, the rewrite path is code.
- Checkpoint: G (reactive cases) + safety rerun (bridges + endpoint
  body per F8) + B-RETR-POST-P3 committed as the post-Phase-3 baseline.
"""
from __future__ import annotations

from app.usage_logging import log_llm_usage

_REWRITE_MODEL = "claude-haiku-4-5-20251001"

REWRITE_PROMPT = """Rewrite this conversational moment as ONE standalone retrieval query.

The query will search a historical world's own indexed material (terms, stories). It must:
- name the actual subject being asked about, in plain topical words
- carry any key vocabulary the participant themselves used
- include the specific angle the immediately-preceding speaker raised ONLY if the participant is engaging it
- contain NO speaker names, no "just said", no meta-language about the conversation

Participant's message: {participant}

{reactive_block}

Respond with the standalone query only - one line, no quotes, no commentary."""

REACTIVE_BLOCK = """Another representative spoke immediately before ({other_name}): {other_msg}

The participant may be responding to that turn - fold its TOPIC (not its wording) into the query only where the participant is engaging it."""


def rewrite_query(llm, participant_msg: str,
                  other_rep_name: str | None = None,
                  other_rep_msg: str | None = None) -> str:
    """One Haiku call -> a standalone retrieval query. Fail-open: any
    error returns the legacy concatenation so retrieval behavior
    degrades to exactly today's, never to nothing."""
    legacy = participant_msg
    if other_rep_msg:
        legacy = (f"{participant_msg}\n\n{other_rep_name} just said: "
                  f"{other_rep_msg}")
    try:
        reactive = ""
        if other_rep_msg:
            reactive = REACTIVE_BLOCK.format(other_name=other_rep_name or "another representative",
                                              other_msg=other_rep_msg[:600])
        response = llm.invoke(REWRITE_PROMPT.format(
            participant=participant_msg, reactive_block=reactive))
        log_llm_usage("query_rewrite", response, _REWRITE_MODEL)
        text = response.content if isinstance(response.content, str) else str(response.content)
        text = text.strip().splitlines()[0].strip().strip('"')
        return text if 3 <= len(text.split()) <= 60 else legacy
    except Exception:
        return legacy
