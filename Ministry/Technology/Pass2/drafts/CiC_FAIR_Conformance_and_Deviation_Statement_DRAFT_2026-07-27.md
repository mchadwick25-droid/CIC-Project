# Conformance and Deviation Statement — the CiC record repository

**DRAFT for Mark's review — S5.4, 2026-07-27.** Nothing here is adopted
until you say so; this is the one-page statement Pass 1 §5.6 calls for
(doc 12 Tier 3), written from what is actually true of the system today,
deviations first-class rather than footnoted. Scope: the Desert world's
record repository (the one migrated world); the statement extends world
by world as S6.2 migrates the fleet.

## What the repository is

Every record the Desert Representative speaks from — 99 records across
nine types (terms, stories, sayings, figures, gravities, forces,
contested claims, sources, the world core) — browsable and searchable
with no conversation running, by domain, by source, by figure, and by
contested claim. Every record renders a Level 3 face (the full scholarly
apparatus under an Observe → Reflect → Question scaffold), and every
term additionally renders a Level 2 face (the plain explanation). The
same records, not a copy: the browsable views are regenerated from the
record set and byte-checked against it.

## Conformance, stated plainly

- **Findable.** Every record has a stable id (`desertlex001`,
  `srcDES021`, …) used consistently across the repository, the
  conversation citations, and the machine export. Search is public and
  covers every record's displayable text.
- **Accessible.** The repository and per-record faces are served over
  plain HTTP endpoints with no account required; what is withheld is
  withheld by stated rights rule, never by participant type
  (Article 30 — the levels are never gated by who is asking).
- **Interoperable.** `sources.json` is a machine-readable export of the
  full source registry — ids, bibliographic identity, discovery data,
  and a rights block per row.
- **Reusable.** Rights are *stated* on every exported row — including
  the honest statement that they are not yet established (see deviation
  1), which is itself machine-readable rather than silent.

## Deviations, named

1. **Rights metadata is unpopulated.** No source row yet states
   `rights_status`, `license`, or `display_permitted` (FLAG-013). The
   system fails closed: no third-party-derived text renders publicly —
   today that means zero verbatim quote text displays, including
   wording embedded inside retellings, which the views detect and
   redact mechanically. Metadata and attribution always display. A
   per-row rights-authoring pass is the open decision; when a row gains
   permission, its text renders with no code change.
2. **External identifiers are absent.** The `external_ids` field exists
   on every source row and is populated on none — the export carries
   the field honestly empty. Linking rows to external identifiers
   (DOI, VIAF, WorldCat, editions' own identifiers) is authoring work
   not yet scheduled.
3. **Level 2 renders measure above the reading floor.** 14 of 18 term
   renders fail the constitutional floor (FK 8–10 / FRE ≥ 60) because
   the floor is unreachable by sentence-structure work alone on the
   fields as authored, and the constitutional line forbids vocabulary
   substitution (FLAG-011). Every render computes and carries its own
   measurement; nothing is presented as plainer than it measured.
4. **One world.** The repository covers the migrated world only. The
   other five worlds' material remains in its pre-migration formats
   until each migrates (S6.2).
5. **Mechanical rights detection covers exact embeddings only.**
   Paraphrase-level reuse of in-copyright translation wording is a
   human review question, part of the rights-authoring pass in
   deviation 1.

## External review

*Reviews in Digital Humanities* accepts projects mid-development
(Pass 1 §5.6 notes this); whether and when to seek outside eyes is
yours to decide — this statement is written to be handed over as-is.
