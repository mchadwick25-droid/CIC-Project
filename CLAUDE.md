# CIC-Project — Working Rules

These rules apply to every session in this repo. Read them before doing anything else.

## Fix it right

- No easy fixes. No band-aids, no workarounds, no "good enough for now."
- No fix on a fix. If a previous fix was wrong or incomplete, undo it and redo it right — don't stack a second patch on top of it.
- Find and fix the root cause, not the symptom. If the root cause isn't clear yet, say so and investigate before touching code.
- No shortcuts that trade correctness or completeness for speed.

## Keep the live/canonical surfaces clean

The following are **live and used by the program, or are canonical build output**. They contain only what runs the program or constitutes the finished record — no notes, commentary, change history, review discussion, or process narration embedded in them:

- `engine/`, `cic/engine/` — the core engine
- `records/`, `packages/`, `canon/`, `cic/corpus-map/`, `cic/texts/` — structured world data and compiled build output
- `world-build-docs/` — the canonical construction documents (Doc_01–Doc_09 per world) once finalized

Notes, decision logs, audit trails, adversarial-review rounds, status reports, and strategy discussion belong in `Ministry/` (e.g. `Ministry/Operations/Audits/`, the various `*_Decision_Log.md` files) — never inline in the files listed above. If you find commentary, changelog cruft, or leftover process notes in a live/canonical file, treat that as corruption: remove it, don't add to it.

(This categorization is inferred from the repo layout — correct it if something's miscategorized.)

## Usage/credit discipline

Weekly usage credits keep running out. To fix that without losing quality:

- Opus is for the final adversarial-review gate only. Draft and do intermediate revision rounds with Sonnet.
- From round 2 onward, do a targeted recheck (only what changed, against prior findings) instead of a full re-review from scratch.
- Push mechanical work — package rebuilds, citation/log fixes, formatting, indexing — to Haiku.
- Batch related work into one longer session instead of many short restarted ones; short sessions lose the prompt cache and re-pay for context every time.
- Spread heavy build/review days across the week instead of bursting most of a week's work into 1–2 days.
- Use event-driven waits (PR/CI subscriptions) instead of manual polling loops.
- Check `/usage` periodically to catch a runaway pattern before it costs the rest of the week.
