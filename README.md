# Church in Conversation — the map

This repository is a modular system in three zones. **Live** is what runs and is
protected: it changes only by promotion after test and verification. **Sandbox**
is where modules are built and improved: `main`, deploying to staging. **History**
is everything superseded, kept and never deleted without instruction. The modules
are a source library shelved by tradition; worlds, each a self-contained unit that
loads only when a conversation calls it and speaks only from its own records; the
atlas; the interview engine; the table engine; the facilitator; and the build and
audit tooling around them.

Every top-level entry belongs to one of five kinds. Nothing else sits at the root.

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

## Build — the sandbox side

| entry | what it is |
|---|---|
| `worlds/` | one home per world, keyed by registry code (phase 2 of the cleanup, 2026-09-15): construction documents (Doc_01–Doc_09, reviews, lexicon and story chunks, the Representative) at `worlds/<code>/`, indexes/build log/source manifest at `worlds/<code>/build/`; `_cross-world/` holds fleet-level build documents and their generators. Six not-yet-coded worlds (Anabaptist Movements, Lollardy, Lutheran-Wittenberg, Reformed Zurich and Geneva, Society of Jesus, Tridentine Church) stay under `World-Builds/` at their long names until each gets a registry code |
| `tools/` | repo-level scripts that are not engine modules: the census validator CI runs, the lexicon compliance checker, the path check and the reorganization tooling |

## Reference — the method and spec library

| entry | what it is |
|---|---|
| `reference/L0-Reference/` … `reference/L4-Templates/` | the Level system: foundation, architecture, entry, status, operations, shared methodology, world-build methodology (including the closed Phase One World Selection), Representative methodology, encounter methodology, templates. A template exists once, here |
| `reference/Redesign-Spec/` | the record-native program spec and its artifacts (1–8), the build blueprint, the launch plan |
| `reference/method/` | the current-era build process, completion standard, register bar, naming and role discipline, voice style guide, adversarial-review practice, and the voice-rebuild decisions the readability target rests on |
| `reference/Project-Reference/` | the coach's working references: governance standing rules, review checklist, cleaning pattern log |
| `reference/fleet-voice/` | the exemplar transcript every world's voice is held to |

## Organization

| entry | what it is |
|---|---|
| `Ministry/` | decisions, features, funding, communication, organization, scholarly review, audits. `Ministry/Operations/Standing/` holds the standing tracking documents, including the fleet-wide world registry's own decision history (`WORLDS_REGISTRY_LOG.md`, moved out of `records/` 2026-09-24 — CLAUDE.md's "Keep the live/canonical surfaces clean"); `Ministry/Operations/Audits/` the dated one-off analyses and the move ledger; `Ministry/Features/<name>/` each in-development feature |

## History

| entry | what it is |
|---|---|
| `Archive/` | everything superseded, by category and date: former versions, the Ministry-Early-Days-2026-07 strategy drafts, the Syriac-Build stratum of 2026-07, the Pass2 voice-rebuild evidence of 2026-08, the Tour-Experience-Module-Phase2, superseded housekeeping. Nothing here is current; nothing here is deleted without instruction |

## How a world is named

The registry code in `records/worlds.yaml` (`alx`, `desert`, `pahc`, `hal`, `syr`,
`ijc`, `cappadocian`, `don`, …) is the key everywhere: `records/<code>/`,
`packages/<code>/`, `worlds/<code>/`. `census_id` joins a world to its
Atlas entry and to its shelf in `cic/corpus-map/`. Display names appear only as
display names.

## How things move

- A world is installed by a reviewed registry commit pointing at its package.
- Live changes by promotion from `main` to the protected `live` branch (phase 3,
  2026-09-15), after verification on `cic-engine-staging` and Mark's own review.
  Nothing merges to `live` directly — procedure and one-time setup:
  `Ministry/Operations/Standing/CiC_Promotion_Runbook.md`.
- Hot trees (`worlds/`, `records/`) move only inside a declared freeze window.
- Superseded material moves to `Archive/`; nothing is deleted without instruction.
- A working file carries no change notes. The record of a change lives in a
  supplemental file: the relevant decision log, `Open_Gaps_Tracking.md`, or
  `Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`. Every path this
  cleanup moved is in `Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md`.
- `tools/check_paths.py` runs in CI and fails on any cited path that no longer
  resolves, or any retired path that reappears (`tools/retired_paths.txt`).
