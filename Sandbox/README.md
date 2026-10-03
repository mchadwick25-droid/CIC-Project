# Sandbox

Active next-version work: experimental engine changes, in-progress redesigns, and
anything else being built toward a future version of the system that isn't yet
part of what's live and isn't settled method or history either.

Distinct from:
- **Live** (repo root) — what's actually deployed today.
- **`Build/`** — the settled method, records-in-progress, decisions, and tooling
  that produced the current live system.
- **`Archive/`** — superseded material, kept for the record.

Existing per-feature design-exploration folders under
`Build/Ministry/Features/<name>/Sandbox/` stay where they are — those are tied to
a specific feature's own decision log, not this top-level Sandbox.

## Discipline: pure code, same as Live

`Sandbox/` holds only the actual system pieces being built toward a next
version — code, configs, assets — clean, exactly like the Live zone. No
design notes, decision logs, or process narrative live in here (decided
2026-09-26).

All support material for what's being built in `Sandbox/<project>/` lives in
`Build/Ministry/Features/<project>/` instead — the same place Website-V2,
Library-Access-Gate, and every other feature workstream already keeps its
own design notes and decision log. This means promoting a project from
`Sandbox/` into Live is just moving clean code to its new home — there is
never a "strip the commentary out before this counts as clean" step,
because commentary was never allowed in here to begin with.
