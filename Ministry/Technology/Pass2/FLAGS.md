# Pass 2 FLAGS

Defects found in the Pass 1 design, the Pass 2 blueprint, or a previous step's output are appended here with evidence (Session Contract rule 6). Never silently patched. Whether to change course is Mark's call or a review-round call.

Format per entry: `## FLAG-NNN — <title>` / found-during step / evidence / status (`open` / `resolved-by-Mark` / `withdrawn`).

## FLAG-001 — S1.1's R-lite "token counts match exactly" is unsatisfiable as written

- **Found during:** S1.1 (implementing the B-COST checkpoint).
- **Evidence:** The blueprint's S1.1 checkpoint reads: *"an independent session re-runs 5 of the turns and confirms token counts (input/output/cache-read/cache-creation) match **exactly** — these are deterministic given identical inputs, not subject to 'noise'."* Three of the four counts cannot match exactly on any real re-run: (1) a re-run turn's **input** is never identical, because every turn's prompt embeds previously *generated* text (the facilitator's reception/handoff and all prior responses vary per generation); (2) **output** tokens are sampled, not deterministic; (3) **cache-read/creation** depend on the API cache's state at call time. The premise "deterministic given identical inputs" is true only of a hypothetical byte-identical API replay, which the raw log does not (and reasonably could not) capture.
- **Reading applied pending Mark's call** (stricter-than-possible replaced by strongest-available, same intent — a fabricated or mis-aggregated baseline must not survive): the R-lite artifact instead verifies (a) **exact recomputation** — every number in the committed baseline report re-derived from the committed raw log by an independent recomputation, exact match required; and (b) **live shape re-verification** — fresh re-runs of sample turns confirming the same call-site composition (labels × models per turn) and same order-of-magnitude token counts, with the variance sources named.
- **Status:** open (S1.1 completed under the reading above; revisit if Mark wants a different instrument).

## FLAG-002 — S2.2's coverage parity vs. Ecological Function's schema home (sequencing wrinkle)

- **Found during:** S2.2 (term records, mechanical half).
- **Evidence:** S2.2's P checkpoint requires every sentence of the chunk's five body sections (including **Ecological Function**) to land in exactly one record field, with the retired retrieval-condition classes as the only legal drops. But Pass 1 §3.2 gives Ecological Function prose no mechanical-half home: it is *absorbed into typed `field_relations[]`* — which is S2.3's new-authoring scholarship, not S2.2's mechanical split. Landing it nowhere fails parity; typing it at S2.2 would smuggle S2.3's judgment into the mechanical step.
- **Reading applied pending Mark's call:** at S2.2 the Ecological Function text is parked verbatim inside `world_meaning` under an explicit marked delimiter ("`[Ecological Function — parked at S2.2; restructured into typed field_relations at S2.3 per §3.2]`"), so parity holds with zero illegal drops and the parking is visible to the batch reviewer rather than silent. S2.3's declared move is then to convert that parked prose into typed edges (+ notes) and remove the parking block, with parity re-run at S2.3 counting the EF sentences as landed in `field_relations[].note`.
- **Status:** open (S2.2 executed under this reading; revisit at S2.9 if Mark prefers a dedicated interim field or another shape).

## FLAG-003 — §11-A's story requiredness (`owner_figure_id`) does not fit Tier-4 composites

- **Found during:** S2.4 (Desert story records).
- **Evidence:** Pass 1 §11-A requires `owner_figure_id` on story records at freeze, and the S1.3 completion gate encodes that. `desertstory008` (A Day in a Kellia Cell) is an explicitly-marked Tier-4 composite reconstruction — per its own template rule it follows no one person's day, so it has no owner figure, and `owner_figure_id` must reference a resolving `figure` record (prose like "none — composite" cannot go in an id field). The story record is honest; the requiredness rule is one tier too broad.
- **Reading applied pending Mark's call:** the field stays honestly unset; the completion gate's violation on `desertstory008` **stands documented** in every gate run rather than being suppressed — the gate-integrity rule (§0 rule 4) forbids editing the completion profile in the session that must pass it, and that is exactly right here. S2.9 Change-Order candidate: exempt Tier-4 composites from `owner_figure_id` (or define a composite-owner convention), as Mark decides.
- **Status:** open.

## FLAG-004 — S2.4 silently dropped the story chunks' "Formation Ecology Connection" section

- **Found during:** S2.8 (building the story-chunk view; the render's completeness check is exactly what surfaced it).
- **Evidence:** every deployed story chunk carries a `## Formation Ecology Connection` section (hand-authored prose linking the story to specific gravities — e.g. desertstory004's linkage of the leaking-jug story to gravity 5's self-directed register and to the live-test guard). `wrs/migrate/s24_stories_quotes_figures.py`'s `parse_story()` extracts only Story Text / Tier Justification / Usage Guidance; no story-record field carries the Formation Ecology Connection text, and S2.4's own G/R artifacts do not declare the drop. Pass 1 §3.4's story record has no named home for it either (closest candidates: a typed story→gravity link, or an `ecology_connection` prose field — neither exists). This is the same shape as FLAG-002 (content with no mechanical-half home), but unlike FLAG-002 it was dropped silently instead of parked visibly — a genuine S2.4 process miss, caught by S2.8's completeness check doing its job. **Same class, second instance:** desertstory008's Tier-4 `## Source Identification` section (the composite template's required per-element source table — 9 element/source pairs) was also silently dropped at S2.4; no record field carries it.
- **Reading applied pending Mark's call:** the story-chunk view renders without the section; the render-parity classified diff tags every Formation Ecology Connection line as `defect — FLAG-004`, so the gap stays visible in the parity artifact rather than being smoothed. S2.9 Change-Order candidate: add a home (typed story→gravity links with a note field, or an `ecology_connection` field) and backfill the eight sections verbatim.
- **Status:** open.

