# Church in Conversation — the map

This repository is a modular system in four zones. **Live** is what runs and is
protected: it changes only by promotion after test and verification. **Build**
is everything that builds or governs the system without being part of what runs
it — method, records-in-progress, decisions, tooling — kept in one place so the
root shows only the running program by default. **Sandbox** is active
next-version work: experimental changes and in-progress redesigns not yet part
of Live and not settled enough to be Build. **History** is everything
superseded, kept and never deleted without instruction. The modules are a source
library shelved by tradition; worlds, each a self-contained unit that loads only
when a conversation calls it and speaks only from its own records; the atlas;
the interview engine; the table engine; the facilitator; and the build and audit
tooling around them.

Every top-level entry belongs to one of four kinds. Nothing else sits at the root.

## Live — what deploys, and what reads it

"Render" below means the `cic-engine` production service, deploying from the protected
`live` branch — `cic-engine-staging` (deploying `main`) reads the identical set, ahead
of promotion. See "How things move" for the promotion path.

| entry | module | read by |
|---|---|---|
| `engine/` | interview engine, table engine, facilitator (m5), build engine (m1–m3), audit and cost (m7, m8), API | Render (Docker COPY), CI, engine |
| `records/` | world truth — one directory per world by registry code; `_fleet/` is fleet-shared; `worlds/<code>.yaml` is the registry, one file per world | Render, CI, engine |
| `packages/` | compiled world packages, derived from `records/`; only pinned manifests are tracked | Render, CI, engine |
| `canon/` | sealed admission probes (fleet-shared) | CI, engine |
| `fixtures/` | the synthetic fixture world and seeded defects | CI, engine |
| `cic/` | **the Library**: `texts/` (vendored public-domain editions, flat, one copy of each), `corpus-map/` (which works belong to which tradition, at which locus, in what role), `engine/` (corpus tools) | Render (`cic/texts/` only, for the in-image compile), engine gates at build time; never at runtime |
| `cic-poc/` | the participant-facing frontend (interview and table); the proof-of-concept backend it was named for is retired | Render (Docker COPY `frontend/`), CI |
| `cic-website/` | the public site and the Atlas; `data/world-census.json` is the census | Cloudflare (assets directory), CI |
| `cic-worker/` | the Cloudflare Worker in front of the site's assets: answers byte-range requests under `/audio/` (iPhone Safari needs them to play and seek narration); everything else is served unchanged | Cloudflare (`wrangler.jsonc`) |

## Build — everything that builds or governs the system, not itself part of what runs it

Moved under one top-level `Build/` (2026-09-26, Live/Build split) so the root shows only
the Live zone plus `Archive/` by default. `tools/` splits across this line: the 5 scripts
CI actually runs (`check_paths.py`, `check_live_commentary.py`,
`check_no_embedded_world_data.py`, `repin_stale_worlds.py`, `validate-census.mjs`) stay at
root `tools/`; everything else in `tools/` — scripts nothing in CI invokes — moved to
`Build/tools/` with the rest below.

| entry | what it is |
|---|---|
| `Build/worlds/` | one home per world, keyed by registry code (phase 2 of the cleanup, 2026-09-15): construction documents (Doc_01–Doc_09, reviews, lexicon and story chunks, the Representative) at `Build/worlds/<code>/`, indexes/build log/source manifest at `Build/worlds/<code>/build/`; `_cross-world/` holds fleet-level build documents and their generators. Four not-yet-coded worlds (Anabaptist Movements, Devotio Moderna and the Brethren of the Common Life, Lollardy, Tridentine Church) stay under `Build/World-Builds/` at their long names until each gets a registry code |
| `Build/reference/L0-Reference/` … `Build/reference/L4-Templates/` | the Level system: foundation, architecture, entry, status, operations, shared methodology, world-build methodology (including the closed Phase One World Selection), Representative methodology, encounter methodology, templates. A template exists once, here |
| `Build/reference/Redesign-Spec/` | the record-native program spec and its artifacts (1–8), the build blueprint, the launch plan |
| `Build/reference/method/` | the current-era build process, completion standard, register bar, naming and role discipline, voice style guide, adversarial-review practice, and the voice-rebuild decisions the readability target rests on |
| `Build/reference/Project-Reference/` | the coach's working references: governance standing rules, review checklist, cleaning pattern log |
| `Build/reference/fleet-voice/` | the exemplar transcript every world's voice is held to |
| `Build/Ministry/` | decisions, features, funding, communication, organization, scholarly review, audits. `Build/Ministry/Operations/Standing/` holds the standing tracking documents, including the fleet-wide world registry's own decision history (`WORLDS_REGISTRY_LOG.md`, moved out of `records/` 2026-09-24 — CLAUDE.md's "Keep the live/canonical surfaces clean"); `Build/Ministry/Operations/Audits/` the dated one-off analyses and the move ledger; `Build/Ministry/Features/<name>/` each in-development feature |
| `Build/tools/` | the building-tools subset of `tools/`: the reorganization/citation-rewrite tooling, the lexicon compliance checker, and the Church Family Tree (Atlas) page generators |

## Sandbox — active next-version work

| entry | what it is |
|---|---|
| `Sandbox/` | experimental engine changes, in-progress redesigns, and next-version drafts of any kind — not yet part of Live, not settled enough to be Build. Pure code only, clean like Live — no design notes, decision logs, or process narrative (decided 2026-09-26). Support material for `Sandbox/<project>/` lives in `Build/Ministry/Features/<project>/` instead, the same place every other feature workstream keeps its own design notes and decision log — so promoting out of Sandbox is just moving clean code, never a "strip commentary first" step. Distinct from the existing per-feature design-exploration folders under `Build/Ministry/Features/<name>/Sandbox/`, which stay tied to their own feature's decision log |

## History

| entry | what it is |
|---|---|
| `Archive/` | everything superseded, by category and date: former versions, the Ministry-Early-Days-2026-07 strategy drafts, the Syriac-Build stratum of 2026-07, the Pass2 voice-rebuild evidence of 2026-08, the Tour-Experience-Module-Phase2, superseded housekeeping, superseded method documents, superseded engine code. Nothing here is current; nothing here is deleted without instruction |

## How a world is named

The registry code in `records/worlds/<code>.yaml` (`alx`, `desert`, `pahc`, `hal`, `syr`,
`ijc`, `cappadocian`, `don`, …) is the key everywhere: `records/<code>/`,
`packages/<code>/`, `worlds/<code>/`. `census_id` joins a world to its
Atlas entry and to its shelf in `cic/corpus-map/`. Display names appear only as
display names.

## How things move

- A world is installed by a reviewed registry commit pointing at its package.
- Live changes by promotion from `main` to the protected `live` branch (phase 3,
  2026-09-15), after verification on `cic-engine-staging` and Mark's own review.
  Nothing merges to `live` directly — procedure and one-time setup:
  `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`.
- Hot trees (`Build/worlds/`, `records/`) move only inside a declared freeze window.
- Superseded material moves to `Archive/`; nothing is deleted without instruction.
- A working file carries no change notes. The record of a change lives in a
  supplemental file: the relevant decision log, `Open_Gaps_Tracking.md`, or
  `Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`. Every path this
  cleanup moved is in `Build/Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md`.
- `tools/check_paths.py` runs in CI and fails on any cited path that no longer
  resolves, or any retired path that reappears (`tools/retired_paths.txt`).
