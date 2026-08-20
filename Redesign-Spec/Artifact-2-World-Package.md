# Artifact 2 — World Package Layout, Manifest & Hash Protocol

Companion to `CiC-Program-Spec.md` (Stage 0.5.2). The World Package is the unit of delivery (§5A.1): the conversation system needs nothing about a world beyond its package.

## 1. Layout

```
<world_key>/<package_id>/            # package_id = UTC timestamp of the build, e.g. 2026-09-01T14-30-00Z
  manifest.json                      # the contract (below)
  records/                           # the exact record files this package was compiled from (frozen copy)
  compiled/
    prompt.txt                       # permanent prompt (assembled by segment order; cache-stable)
    capsule.md                       # world capsule
    chunks/{lexicon,story,ambient}/  # retrieval chunks (one file per record served)
    indexes/{lexicon.faiss,story.faiss}
    quotes.json                      # ALL quotes incl. do-not-voice (violation-recognizable)
    figures.json                     # name-bridge registry (post-generation decoration only)
    repository.json                  # tier-3 browsable records + sources
    coverage.json                    # canon cell -> {terms[], stories[], quotes[], figures[], status}
    frame.json                       # facilitator doorway data: thinness statement, cautions, starters per frame
  validation/
    gates-report.json                # every gate, result, and inertness report
    admission/results.json           # battery results (blind protocol, sealed-key refs)
    admission/transcripts/           # the graded transcripts
    signoffs.json                    # Mark's four touchpoints, dated; Article-31 status (aspirational note)
```

## 2. manifest.json

```json
{
  "package_schema": 1,
  "package_id": "2026-09-01T14-30-00Z",
  "world_key": "alx",
  "record_schema_version": 2,
  "built_by": "cic-compiler <git sha>",
  "records_commit": "<git sha of the records repo at build>",
  "files": { "compiled/prompt.txt": "sha256:…", "...": "every file in the package, no exceptions" },
  "coverage_summary": { "cells_substantive": 24, "cells_honest_limit": 4, "cells_empty": 0 },
  "floors": { "term": 10, "story": 6, "quote": 3, "demonstration_cells_required": ["C-*", "identity-collision"] },
  "compat": { "min_runtime": "1.0", "max_runtime": null }
}
```

- `manifest_hash` = sha256 over the canonical-JSON manifest. The **registry** (Artifact 1 §2) stores the expected `manifest_hash` per world. Chain of trust: registry (git, reviewed) → manifest (hash pinned) → files (hashes listed).
- **Load-time verification (closes the 70-file-drift class):** the runtime, when (lazily) loading a world, recomputes the manifest hash and spot-verifies every file hash it reads. **Mismatch ⇒ refuse to serve that world** (the world shows "temporarily unavailable"; other worlds unaffected). This is the named availability decision: a wrong world is worse than an absent one.

## 3. Determinism & staleness

- Same `records_commit` ⇒ byte-identical package (compiler runs twice in CI; diff must be empty).
- CI staleness job: recompile every `built|admitted|open` world from its `records_commit`; `git diff`-style comparison against the stored package; any drift is a failure. The compiler list is explicit, never a glob.
- No hand edits, ever: every compiled file carries a `generated-by` header; the gate rejects packages whose compiled files differ from a fresh compile.

## 4. Versioning & migration

- `record_schema_version` bumps require a migration note in the schema's own changelog and a recompile of affected worlds; packages are immutable — a change means a NEW package_id, re-gated; `open` worlds swap by registry pointer (atomic), old package retained for rollback.
- Runtime compatibility is declared in `compat`; a runtime refuses packages outside its declared range (loud, at load, never silent).
- Admission re-entry: a records change to an `open` world produces a new package that re-runs gates always and re-runs admission when the change touches voice_craft, demonstrations, doctrinal_witness, or any center cell (`DECIDABLE`: the exact re-admission trigger list).

## 5. Install & storage

Packages are built by CI, uploaded to object storage (S3, versioned bucket, private), and referenced by the registry. "Installing a world" = a reviewed registry commit pointing at the package. No runtime admin API exists for installation (see Artifact 6 threat model — the admin plane is git + CI, nothing else).
