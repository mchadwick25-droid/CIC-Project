# Pass 2 FLAGS

Defects found in the Pass 1 design, the Pass 2 blueprint, or a previous step's output are appended here with evidence (Session Contract rule 6). Never silently patched. Whether to change course is Mark's call or a review-round call.

Format per entry: `## FLAG-NNN — <title>` / found-during step / evidence / status (`open` / `resolved-by-Mark` / `withdrawn`).

## FLAG-001 — S1.1's R-lite "token counts match exactly" is unsatisfiable as written

- **Found during:** S1.1 (implementing the B-COST checkpoint).
- **Evidence:** The blueprint's S1.1 checkpoint reads: *"an independent session re-runs 5 of the turns and confirms token counts (input/output/cache-read/cache-creation) match **exactly** — these are deterministic given identical inputs, not subject to 'noise'."* Three of the four counts cannot match exactly on any real re-run: (1) a re-run turn's **input** is never identical, because every turn's prompt embeds previously *generated* text (the facilitator's reception/handoff and all prior responses vary per generation); (2) **output** tokens are sampled, not deterministic; (3) **cache-read/creation** depend on the API cache's state at call time. The premise "deterministic given identical inputs" is true only of a hypothetical byte-identical API replay, which the raw log does not (and reasonably could not) capture.
- **Reading applied pending Mark's call** (stricter-than-possible replaced by strongest-available, same intent — a fabricated or mis-aggregated baseline must not survive): the R-lite artifact instead verifies (a) **exact recomputation** — every number in the committed baseline report re-derived from the committed raw log by an independent recomputation, exact match required; and (b) **live shape re-verification** — fresh re-runs of sample turns confirming the same call-site composition (labels × models per turn) and same order-of-magnitude token counts, with the variance sources named.
- **Status:** open (S1.1 completed under the reading above; revisit if Mark wants a different instrument).

