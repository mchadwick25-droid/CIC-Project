# M1 — Record-store physical form (Pass 1 §12.2) — DECIDED

**Date:** 2026-07-26. **Decided by:** Mark, in the Pass 3 build thread
("follow your recommendation" to the singly-presented proposal).

**Decision:** the blueprint §2.1 proposal, adopted as proposed —
**files-in-git**: one file per record, one directory per world under
`cic-poc/backend/wrs/records/<world_dir>/<record_type>/`, structured front
matter validated by a committed JSON Schema (S1.5). Git supplies the
append-only discipline; the validator supplies database-grade checking; a
database remains a later optimization behind the same schema.

**Presented with alternatives:** (1) SQLite (stronger day-one query power,
loses diffable records); (2) one YAML per record type per world (fewer
files, worse merges, no per-record history). Both declined in favor of the
recommendation.

**Unblocks:** S1.5 (schema implementation + traceability matrix), S1.3
(gate runner — one unit with S1.5, schema first), and the S1.4 parameters
file's form question (a standalone YAML file, consistent with files-in-git).

**Also recorded in:** `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
(2026-07-26 entry; that file carries other uncommitted work of Mark's, so the
entry rides in the working tree until his own Decision Log commit — this
file is the committed record).
