# Artifact 1 — Normative Record Schema & World Registry

Companion to `CiC-Program-Spec.md` (Stage 0.5.1). Status: NORMATIVE DRAFT — defaults are decided; anything marked `DECIDABLE` may be overturned with a recorded reason. Everything here serves rulings already made (records as sole source of truth; canon coverage through record types; three-axis confidence; honest limits as data; rights fail-closed).

## 1. Physical form

- One record = one file: YAML front matter between `---` fences (all structured data) + a free markdown body (provenance and build notes — never read by any builder). Proven form; carried forward.
- Store layout: `records/<world_key>/<record_type>/<id>.md`. Fleet-level records: `records/_fleet/<record_type>/…` (canon questions, modern terms).
- Storage engine: **files in git** (the store IS a git repository; history is the audit trail). `DECIDABLE` only if scale breaks it (unlikely below ~200 worlds).
- ID scheme: `<world_key>.<type>.<slug>` (e.g. `alx.term.logos`, `_fleet.canon.c-i-01`). IDs are permanent; slugs never recycled.

## 2. The world registry — the ONE registry

`records/worlds.yaml`. Everything about a world derives from here; **no world identifier may appear anywhere else in code or config** (spec principle 4).

```yaml
worlds:
  alx:
    world_id: alexandria-catechetical
    display_name: Alexandrian Christianity
    time_window: {start: 150, end: 400}
    place: "Alexandria and Egypt"
    representative: {name: Theon, role_label: Catechist}   # the two sanctioned fabrications (spec principle 14)
    state: building        # building | built | admitted | open | withdrawn
    census_id: "IX.12"     # this world's entry in the Atlas census (world-census.json) — the Atlas↔interview mapping is data, never a hand-synced list
    package: {manifest_hash: "sha256:…", location: "s3://…/alx/2026-09-01T…/"}
    thinness_statement: "Richest in teaching and argument; thinner on…"
    living_tradition_flag: false   # true => doorway carries the living-tradition distinction (spec §6)
```

State transitions are registry commits only: `building→built` (gates green), `built→admitted` (admission passed + Mark's sign-offs), `admitted→open` (registry flip = the door opens), any→`withdrawn`. A test asserts the runtime reads world facts from the registry alone.

## 3. The envelope (every record)

Required floor: `id`, `world_id`, `record_type`, `schema_version`. All else per-type; requiredness beyond the floor is the field-completion gate's job, not the schema's (proven split).

```yaml
id: alx.term.logos
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: draft            # draft | ready | frozen  (advances via build-step exit checks; frozen at Mark's checkpoint)
register: emic           # emic | etic | emic-unavailable — the record's STANCE; distinct from the voice register (spec O2) and the question register (I/E/P/T)
canon_cells: [F1-I, C-T] # NEW — the coverage map lives ON records: which canon cells this record serves
confidence:
  citation_specificity: B          # A..E
  verification_state: verified-direct   # verified-direct | verified-via-authority | named-not-rechecked | unverified
  evidentiary_weight: load-bearing      # load-bearing | corroborating | illustrative | contested
  formation_confidence: Documented      # Documented | Widely Accepted | Dominant Modern Reconstruction | Contested | Inferential-Thin
  divergence_note: null    # REQUIRED (non-null) when formation_confidence=Documented and no source is verified-direct
sources:
  - {source_id: alx.source.clement-paidagogos, locus: "1.6", license: public-domain}
retrieval:               # only on chunk-feeding types (term/story/ambient/doctrinal_witness)
  tier: 1                # 1 core / 2 supporting / 3 ambient
  retrieve_when: []      # empty array is the typed null — NEVER an em-dash or "n/a" (sentinel rule)
  do_not_retrieve_when: []
relations:               # typed, reciprocity-gated
  - {type: presupposes, target: alx.term.gnosis}
```

Relation types (closed vocabulary, inverses declared): `presupposes/presupposed-by`, `precondition-for/enabled-by`, `tension-with` (symmetric), `illustrated-by/illustrates`, `associated-with` (symmetric). Extending the vocabulary is a gate-integrity change (own reviewed step).

## 4. Record types (15 per-world + 2 fleet)

Per-world: **world_core** (time window, horizon, formation logic, thinness, cautions) · **source** (the registry of what survives: author, work, edition, rights_status, attribution_status, discovery channel, external ids) · **term** (plain_meaning FIRST, world_word, false_friend[], four-register senses, quick_meaning ≤ FK 10) · **story** (narrative_tier 1–4 with required justification, tellable_as, text, absent-detail note) · **quote** (text, speaker figure-id, source+locus, license: verbatim | paraphrase-only | do-not-voice) · **figure** (names[] tagged in-world/scholarly, dates, narratable, bridge_line) · **gravity**, **force**, **contested_claim** (claim, held_against[], concedes, divergence_partners[]) · **doctrinal_witness** (NEW: the world's own answer-ground for a foundations/center cell — the witness text, its positions, its tensions, sources; one per cell where substantive) · **honest_limit** (NEW: `{statement (in-voice, plain), why_sources_cannot_answer, nearest_material[]}` — the cell it answers is the envelope's `canon_cells` — "our record does not answer this" as data) · **ambient** (daily-life records; structurally barred from formation claims) · **demonstration** (worked exchanges incl. foundational and identity-collision cells with the spoken non-judgment line) · **voice_craft** (the per-world half of the prompt as data: tagged paragraphs per assembly segment; native measure as observation, never enforcement) · **search_record** (what was searched, including searches that returned nothing).

Fleet: **canon_question** (`{cell, text, source: array of corpus|ext|new (mixed provenance allowed), canon_status: seed|vetted|retired, tags: e.g. [identity-collision], phrasing_rules_checked: true}` — `canon_status` is deliberately not the envelope's `status`; a canon question's lifecycle is its own) · **modern_term** (display_terms, origin_year, modern_sense, underlying_subject, distinguishing_claim, native_subject_map).

## 5. Worked examples (compact but complete)

```yaml
# records/alx/honest_limit/alx.limit.f5-women-own-words.md
id: alx.limit.f5-women-own-words
world_id: alexandria-catechetical
record_type: honest_limit
schema_version: 2
status: draft
register: emic
canon_cells: [F5-I]
statement: >
  You ask what the women among us said of their own lives. I must be honest:
  the writings we have are men's. The women are present in them — taught,
  baptized, remembered — but their own words were not kept.
why_sources_cannot_answer: "No female-authored Alexandrian Christian text survives from the window."
nearest_material: [alx.figure.demetria, alx.story.catechumen-household]
confidence: {citation_specificity: A, verification_state: verified-direct,
             evidentiary_weight: load-bearing, formation_confidence: Documented, divergence_note: null}
sources: [{source_id: alx.source.survey-corpus, locus: "registry-wide", license: public-domain}]
```

```yaml
# records/_fleet/canon_question/_fleet.canon.c-i-01.md
id: _fleet.canon.c-i-01
world_id: _fleet
record_type: canon_question
schema_version: 2
cell: C-I            # families: C(center), F1..F6 × registers I|E|P|T
text: "Who was Jesus, to you and your people?"
source: [corpus]
canon_status: seed
phrasing_rules_checked: true
```

```yaml
# records/alx/quote/alx.quote.clement-new-song.md  (type example)
id: alx.quote.clement-new-song
world_id: alexandria-catechetical
record_type: quote
schema_version: 2
canon_cells: [C-I]
text: "…"                     # exact translated text from the cited edition
speaker_or_author: alx.figure.clement
license: verbatim             # do-not-voice quotes SHIP in the index so a violation is recognizable
sources: [{source_id: alx.source.clement-protrepticus, locus: "1.1", license: public-domain}]
confidence: {citation_specificity: A, verification_state: verified-direct,
             evidentiary_weight: illustrative, formation_confidence: Documented, divergence_note: null}
```

## 6. Validation

Per-type JSON-Schema, `unevaluatedProperties: false` (unknown field = hard error). Plus hand rules: sentinel strings rejected in retrieval blocks; `divergence_note` conditional requirement; `canon_cells` must exist in the canon; every relation's target must resolve and reciprocate. The gate battery (referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, **readability** (quick_meaning and plain fields ≤ FK 10), **canon-coverage**, **inertness**) runs per package build; gate changes are their own reviewed steps (gate-integrity rule). Coverage rule: for every canon cell, every open world has ≥1 `doctrinal_witness`/`term`/`story`/`quote` serving it OR exactly one `honest_limit` — never neither, never blank.
