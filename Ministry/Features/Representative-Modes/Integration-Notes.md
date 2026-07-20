# Integration Notes — Representative Modes

## Live today

Nothing. `main`'s `cic-poc/frontend/src/components/` has no `RoleSelector.tsx`;
`cic-poc/backend/app/prompts/` has no `role_modes.py`. Confirmed by direct search.

## The code

Exists only on a local, **unpushed** branch: `claude/representative-modes-exploration`
(tip `9774447`, "Rename deconstructing role id to reevaluation") — one commit ahead of
what the Dashboard/Task Board actually cite (`1127c09`). Reachable from no other
branch; not merged into `main`.

Files touched, all inside `cic-poc/`: `backend/app/graph/nodes.py`, `backend/app/
graph/state.py`, `backend/app/main.py`, `backend/app/prompts/role_modes.py` (new),
`backend/app/transcript_logging.py`, `frontend/src/components/RoleSelector.tsx`
(new), `frontend/src/components/TheTable.tsx`, `frontend/src/hooks/useConversation.ts`,
`frontend/src/styles/table.css`, `frontend/src/types/conversation.ts`.

**A referenced parent branch, `claude/cic-poc-backend-facilitator-upgrade`, does not
exist in this local repo** — noted in case it matters for a future rebase.

**Partial adjacent piece already live:** the World Map's `/?worlds=&mode=` URL
handoff (see Atlas-World-Map's Integration-Notes.md) does NOT include `role=` yet —
confirming the map half of the URL contract shipped without the role half.

## What's blocking the merge

"Battery A" — live-model validation. Design/prompt architecture is done; nothing
merges before this runs, per the standing "nothing merges before/during a pilot"
rule, and this feature additionally has never been tested against a real model at
all (only mock-LLM mode).

## What to do once Battery A passes

Push the branch, rebase against current `main` (it will be several commits behind by
then), merge, then update this file and delete the stale commit reference in the
Dashboard/Task Board.
