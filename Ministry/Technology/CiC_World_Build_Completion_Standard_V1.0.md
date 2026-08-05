# CiC World-Build Completion Standard V1.0

**Status: GOVERNING — adopted by Mark, 2026-07-27 (S6.1, per-document
M; drafted same day, adopted as drafted).** Source: Pass 1 §11
(Deliverable 10), carried into this standalone governing document per
the Pass 2 blueprint, with only what Pass 2 actually established folded
in — each fold-in is marked `[Pass 2:]` so its provenance stays
visible. Per §E below: changes to this standard are Change Orders,
never silent edits; a world freezes against the version in force when
its build began. The machine gates (`cic-poc/backend/wrs/gates/`) cite
this document as the requirements source.

One document, existing before a world is built, checked at freeze,
every check producing a saved artifact. It resolves the circular freeze
gate by splitting **world-freeze** from **representative-freeze**, and
it is the single reference the gates, the assembly, and the metrics
point at rather than restating requirements in their own words.

## A. World-freeze — required record completeness

| Record type | Required at freeze | Notes |
|---|---|---|
| `world_core` | `time_window`, `horizon`, `formation_logic` populated; `gravities[]` resolves to real gravity records | The always-present world's-own-ground segment and the per-seated-world anachronism check read this record — an unpopulated core is freeze-blocking, not a silent gap. [Pass 2: `pairing_guidance` and `cautions` populated — the Facilitation Brief and the runtime cautions render from them (S2.7a/S5.5)] |
| `source` | Envelope + Tier-1 fields populated; `attribution_status` on every P-row; `discovery_channel` on every row; the world's `search_record` complete on the STARLITE headings; field-bibliography sweep run and dispositioned; saturation statement present with the last unproductive searches named | Tier-2 fields (external ids, transmission path, rights) populate forward; **rights become blocking at public-repository ship** [Pass 2: the repository ships fail-closed meanwhile — unset rights render as metadata + attribution only, never text (FLAG-013 discipline)]. [Pass 2, F2 reading, Mark's OK standing: for already-built worlds the sweep runs at migration time, the `search_record` documents that migration-time sweep explicitly scoped as such; prospective §11 applies in full to the next new world] |
| `term` | Tier 1/2: all four sense fields, `quick_meaning`, `voice_surface`, `semantic_domain`, at least one directional `field_relation`, typed retrieval block, licensed sources. Tier 3: `quick_meaning` + sources minimum | `prior_sense: none-attested` is an answer, not a blank. [Pass 2: `plain_explanation` authored to the reading floor per CO-P2-12 — Level 2's content source, machine-checked at the gate; `contested_claim_ids` populated where a claim rides the term (FLAG-014's close)] |
| `story` | Tier with justification; `owner_figure_id` (composite-owner convention per CO-P2-06: a Tier-4 composite is owned by the community figure, never the persona); `attested_occasion`; `tellable_as`; every element sourced; `gravity_links[]` typed (CO-P2-04) | |
| `quote` | Locus, translation-used, license | |
| `gravity` / `force` | Six tests recorded per candidate including not-advanced (named keys per CO-P2-02); `interaction[]` and `connections[]` typed and reciprocity-checked; every force carries Layer 4 — `elaboration` or explicit `stasis`; every force carries `sources[]` | [CO 2026-08-05, full-system review Rigor P0-3: `sources[]` added — the one world that omitted it on every force record (Imperial-Juridical, 0/10) passed this row anyway, since nothing here required it. A force whose evidence genuinely lives in a different world's own registry (a pre-window inheritance force, for example) still needs `sources[]` populated or left honestly empty with the reason stated in the record's own body — an undocumented empty is what this CO closes, not the possibility of a real empty] |
| `figure` | Every figure named in any voice-bearing record exists, with `narratable` set | [Pass 2: including figures the lexicon leans on — the missing-Evagrius class (FLAG-015)] |
| `contested_claim` | At minimum, the world's Primary-gravity claims: held / conceded / pressure response / divergence partners mapped against live worlds | Feeds the Table Readiness question bank and the held-position metrics |
| `voice_profile` + `demonstration` | Profile complete with register evidence and trait rubric; demonstrations diversity-reviewed against the parroting warning | [Pass 2: norms checked against every probe category — the FLAG-005 lesson, standing practice per CO-P2-11c] |
| Views | All views render without error; the Facilitation Brief renders complete (its human-judgment records authored during the build, not at the end); repository view renders with rights resolved or fail-closed | A world that cannot render cannot freeze |

## B. World-freeze — gates that must show a real pass, as saved artifacts, never self-reports

All machine gates green with committed run output; content review
rounds saved per CO-020/CO-022 discipline (no self-certified
dismissals); the reviewer's relative-recall run recorded; the PRESS
question answered explicitly; the retrieval golden set authored (12–20
cases) and its baseline committed.

## C. Representative-freeze — after world-freeze

The assembly renders within budget; RCF Part Eight's probe categories
**plus the parroting and pushback categories** [Pass 2: eight Part
Eight categories in V3.2 — Register-Fidelity is a Part Five
construction check, not a probe category (FLAG-017); the Self-
Referential pass criterion is the validated standard: in-voice
acknowledgment of speaking from a formed tradition, never a
persona-claim, never AI/project awareness], run under the Construction
Framework V7.4 Validation Protocol Rigor discipline (two independent
generation trials — one resampled from development probes, one
held-out novel; fresh-context generation; blind grading); continuity
regression against the prior version where one exists; and the **Table
Readiness Round passed** — seated with one live world on a
`divergence_partners` question, graded on vocabulary borrowing,
anachronistic reach, and held-position vs. convergence, with findings
routed **(a) runtime, (b) records — fix, regenerate, rerun, or (c)
framework change**, and (b)/(c) closed or explicitly accepted by Mark
before freeze. The loop back is part of the standard, not an exception
to it. [Pass 2: run for the first time at S5.6 — the loop back fired
(FLAG-018), was fixed and re-proven, and the freeze followed; the
gate report + Ecology Assessment + Validation Matrix are the artifact
shape.]

## D. Metrics that gate a freeze

Named now, thresholds set only once real baselines exist:
field-completion = 100% on required fields; referential-integrity and
reciprocity violations = 0; `do_not_retrieve_when` violations = 0 on
the golden set; Pass@k floor, held-position/concession bands, and the
parroting ceiling recorded as `TBD-pending-baseline` in
`cic-poc/backend/wrs/parameters.yaml`'s metric records and set in one
decision when six-world baselines exist (S6.6). [Pass 2: the
operational numbers live in the parameters file, which the governing
documents now point at — the S5.5 pointer series.]

## E. Standing rules

The standard is versioned; a world freezes against the version in
force when its build began; changes to this standard are Change
Orders, never silent edits. Its own health check is the machine-gate-
failure count — a standard nothing ever fails is not a standard.

## F. The lens spine (M4, adopted 2026-07-27) — [new in V1.0, not in Pass 1 §11's own text]

World-builds ask all of Smart's seven dimensions as the fixed spine,
per-world yield stated as a finding (a thin dimension is a result, not
a coverage failure); Material Culture is required; an ethical/legal
lens is required; Boundary Structures and Formation Logic remain CiC's
own additions, named as additions. Dimension naming (Smart's names vs
CiC's own) is settled per document in the S6.1 wording sessions.
