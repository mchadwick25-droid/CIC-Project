# Representative Modes — Integration Assessment V0.1

In the map thread's style: what was built, the exact touch surface, merge tiers, and
the standing caution. Branch: **`claude/representative-modes-exploration`**, cut from
`claude/cic-poc-backend-facilitator-upgrade`. The running branches are untouched.

## What was built and verified

Role as a session-start posture, end to end: an optional four-role selector on the
world-selection screen (plus `role=` URL preselection per the map-handoff contract) →
`role` on `POST /api/session/start` (validated; absent = today's exact behavior) →
`ConversationState.participant_role` → at prompt assembly, a listener-guidance block
from the new `role_modes.py` injected as its own prompt-cache segment between the
Representative's static identity block and the table-discourse block, plus a
never-voiced calibration note in the Facilitator's handoff prompt. Role is recorded
in pilot transcripts. Nothing reads role to gate, retrieve, classify, or monitor.

**Verified live against the dev servers (2026-07-16, mock-LLM mode for the app
mechanics; `.env` restored after):** role echo on single- and multi-world session
start; invalid role → 400; no-role baseline unchanged; `/?role=deconstructing`
preselects the pill and scrubs the URL (module-scope parse — the map thread's
StrictMode lesson applied); full UI flow world-select → begin → streamed round with
role in session state, no console/network errors. **Verified directly:** a
prompt-assembly assertion script (scratchpad `test_role_modes.py`) proving the
no-role prompt is byte-identical to pre-feature, each role's block is exactly one
cache-marked segment, static identity is byte-identical across all arms, and all
four blocks end with the identical invariants paragraph. `tsc --noEmit` clean;
backend `py_compile` clean.

## Touch surface

~178 insertions / 10 deletions across 8 modified files + 2 new files; no new
dependencies; no schema/data migrations; one new API field (optional, defaulted).

| Area | Files | Nature |
|---|---|---|
| New prompt document | `backend/app/prompts/role_modes.py` | the four listener blocks + facilitator notes + shared invariants paragraph; authoring rules in the module docstring |
| Prompt assembly | `backend/app/graph/nodes.py` | role block resolved in `_prepare_representative_turn`; fourth segment in `_cached_system_message`; handoff note; state-copy carries role |
| Session plumbing | `backend/app/main.py`, `graph/state.py`, `transcript_logging.py` | request/response field + validation; `participant_role` on state; transcript header field |
| UI | `frontend/src/components/RoleSelector.tsx` (new), `TheTable.tsx`, `hooks/useConversation.ts`, `types/conversation.ts`, `styles/table.css` | optional pill selector; `role=` one-shot param; role passed at session start |

**Deliberately untouched:** representative permanent prompts and world capsules
(byte-identical); retrieval; the twelve-signal monitoring prompt; the frame-breaker
and relational-safety classifiers (role-blind by design — see Prompt Architecture §5);
`table_discourse.py`; the graph topology.

## Merge tiers

- **Tier A — this branch as-is (≈ one evening to merge and re-verify):** selector +
  param + injection. Prerequisite before ANY tester sees it: Validation Plan
  Battery A (content invariance) run and passed — the feature's existence test. The
  no-role default means merging the code is low-risk even with the selector left in;
  a tester who selects nothing gets today's system exactly.
- **Tier B — role-aware transparency defaults (needs the Mode One/Mode Two toggle to
  exist first):** apply governance §4's default rule mechanically. Blocked on the
  transparency-mode UI, which is its own front-end-thread feature.
- **Tier C — closing-resources coordination (blocked on closing-resources being
  built):** role shapes the default register of offered resources; design already in
  Prompt Architecture §5.
- **Tier D — role-aware relational-safety classification (deliberately NOT designed
  here):** would invalidate a live-tested classifier's record; requires its own
  adversarial re-test if ever wanted. Named so nobody drifts into it casually.

## Cautions

- **Nothing merges before or during Prototype Testing 1** (standing ops rule; never
  redeploy during a sitting window).
- The four role blocks are design-frozen drafts, internally reviewed only — the
  register they induce has NOT been observed against a live model yet (mock-LLM
  verification exercises mechanics, not conversation quality). Battery A/B/C/D of the
  validation plan is the gate, and it costs live API calls.
- The `role=` param and the map branch's `worlds=`/`mode=` parsing live on different
  branches today; whichever merges second reconciles the parse site (both parse at
  module scope, so composition is mechanical — on record in the map log,
  twenty-sixth pass).
- If the pilot merges Tier A, the onboarding screen's text does not yet mention role
  selection; a one-paragraph addition there is a content decision for Mark, not a
  code task.

## Recommendation

Hold the branch through Prototype Testing 1. If Mark wants role modes in front of
testers in a later window, run Battery A first, merge before invitations go out,
never mid-pilot — same shape as the map thread's recommendation.
