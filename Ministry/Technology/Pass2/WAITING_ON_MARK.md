# Waiting on Mark

## 2026-07-30 — VG-1a done: the alias wrong-linkage parser fix (Step 1a of the Voice-Governance Addendum)

**What changed:** one function, one file — `parse_aliases()` in `cic-poc/backend/app/rag/indexer.py`. A parenthetically-qualified alias segment (`illumination (baptismal)`) is now dropped whole instead of being stripped to its bare head. The bare-head behavior was the reproduced production bug: "illumination" silently became one of Baptism's aliases and stole Illumination's own key in the frontend map.

**Before/after, measured over all six worlds with the live code:**
- Before: 9 colliding keys, all Alexandria (Desert/Hieronymian/IJ/PAHC/Syriac all 0) — matches the plan doc §5.1's table exactly, key for key.
- After: 7 — the two parenthetical-caused collisions (`illumination`, `apokatastasis`) resolved; the 7 genuine alias-set overlaps (`photismos`, `catechist`, `communion`, `divine likeness`, `the eternal word`, `the son`, `the word`) unchanged, as expected — they're VG-1b's gate's job.
- Baptism still reachable through `photismos`, `initiation`, `the washing`, `new birth`, `the bath`, `crossing the threshold`.
- Retrieval regression (rule 2): full eval re-run vs `B-RETR-POST-P3.json` — **0 regressions; every metric identical**.

**What surprised me (filed as FLAG-028, per this step's own step-4 rule, routed to VG-1b):** the fix's drop-the-qualified-segment rule also removes 9 corpus-wide aliases whose qualifiers are benign descriptors, not collision guards — e.g. `bat qyama (singular forms)` in Syriac, `monogenes (Greek parallel)`, `communion (as juridical status)` in Imperial-Juridical, and `The Vulgate (anachronistic... label)` in Hieronymian (whose alias set is now empty). None of these were colliding; they simply stop highlighting in their own worlds. That's a bounded reachability cost the plan's rationale doesn't cover for this class — VG-1b's authoring/gate pass should decide per case (re-author unqualified where safe, or route through confirmed-gloss). One incidental win: the old parser was emitting a garbage mid-phrase fragment for ijclex003 (`the Dated Creed formula — not`); that's gone.

**Base-state note:** local main fast-forwarded cleanly onto the rolled-back `e92cf85` (pure history move, tree-identical, zero file changes). The full Syriac-freeze session survives on `origin/claude/rollback-to-fable-base` and a local safety branch `backup/syriac-freeze-16cab54`; its working-tree leftovers (untracked `wrs/records/syriac_world/`, `scripts/s62_syr_*`, staging files) are still on disk, untracked, untouched by this step.

**Not started, deliberately:** VG-1b (alias-safety gate — its fixtures must be built against this fix's corrected output, in a separate session per rule 4) and VG-1c (confirmed-gloss schema).

## 2026-07-30 — VG-1b done: the alias-safety gate (Rules A + B; Rule C deferred to VG-1c)

**What was built:** `gate_alias_safety` in the gates package, wired into the runner and selftest, with five seeded fixture sets and an override fixture. Rule A flags a generic alias (determiner-stripped single token on a 46-word curated blocklist or in a bundled offline top-5000 English frequency table — new flat file in the repo, no network). Rule B flags per-world key collisions over the post-parse space — term name ∪ parsed aliases, the same map the frontend actually renders from. The override is the term-level `alias_generic_override_note` you approve per record (schema field + traceability row added); the gate prints it as a note, never counts it, and flags a stale note.

**Verification, all green:**
- Selftest: clean set passes all seven gates; all five seeded alias defects caught; the override fixture reports-without-failing.
- Alexandria: **Rule B flags exactly the 7 documented remaining collisions** from VG-1a, key for key. Plus 29 Rule-A generic-alias findings (`the word`, `the soul`, `communion`, `the christ`…).
- Desert: 5 Rule-A (`the cell`, `elder` — the exact word useLexicon.ts's comment names as the known cross-world hazard — `saying`, `the thoughts`, `the federation`). Syriac: 4 Rule-A.
- FLAG-028's 9 dropped benign-descriptor aliases: contribute no keys, correctly not flagged anywhere.
- The six existing gates produce identical results (all zero) on both frozen worlds — adding, not touching.

**The catch worth knowing about (fixed in-step):** my first record-side key-space reproduction missed that a record alias item can bundle several quoted glosses (`'"mystery," "symbol" (gloss)'`) that the runtime parser splits into separate keys. Corrected to the full per-item parse semantics — and that correction surfaced a real finding: **Syriac's live term map contains bare English generics as keys — `truth`, `mystery`, `symbol`, `reality`, `covenant`, `saint`** — which is your original "highlighting fires too broadly" report, now machine-caught by the gate. All of it is Step-2 retrofit material (authoring decisions per case: drop, keep-with-override, or route to confirmed-gloss).

**Standing note until Step 2:** `alias_safety` is deliberately RED on the three built worlds (Desert 5 / Alexandria 36 / Syriac 4). The six original gates remain the frozen-world regression floor; the new gate's count is the retrofit worklist, not a regression.

**Next:** VG-1c (confirmed-gloss schema), then Rule C as a small follow-up, then Step 2 (retrofit) and Step 3 (clean builds for the next three worlds).

## 2026-07-30 — VG-1c done: the confirmed-gloss schema fix — Step 1 of the Voice-Governance Addendum is COMPLETE

**What changed:** `confirmed_gloss.schema.json` now describes the data the gloss mechanism actually uses. The old shape (`world_term`/`approved_gloss`) could not validate a single one of the 87 live entries — the runtime has always used `{category, original, gloss}`, with `category` deciding which way the bracket-gloss renders. The corrected entry shape is the plan's Option A: `world_id`, optional `term_id` (the future Rule-C hook; 39 of 87 entries belong to worlds with no term records yet, so requiring it now would be dishonest), `category` A/B, `original`, `gloss`, `exact_wording_required`, and optional `sources[]`/`reviewer_confirmed_date`/`review_note` (optional because your 2026-07-25 review happened but wasn't captured as structured evidence — the honest-backfill rule, not an oversight).

**Traceability:** 9 rows replacing the 3 stale ones — the corrected-shape fields carry the original Pass-1 §3.11 warrant; the four genuinely new fields carry a Pass-2-CO warrant (the same pattern CO-P2-04 used for gravity_links). Matrix clean both directions.

**Enforcement made real:** the schema was loaded but never enforced anywhere — that's now closed. `validate.py --glosses` runs actual JSON-Schema validation over the live gloss data: **87/87 valid**, per-world counts matching the plan's own §4.4 table exactly. The schema now provably governs the data it claims to govern.

**Deliberately not done (Step 2/3 territory per the plan's own sequencing):** moving the data out of the Python module into a validated YAML, the gloss referential-integrity gate, the generated-JSON view and consumer refactor, and all `term_id` backfill.

**Where this leaves the addendum:** Step 1 (1a parser fix + 1b alias-safety gate + 1c schema fix) is complete, committed, and green. Rule C wires in as a small follow-up now that `term_id` exists in the shape. Hieronymian's S2.2 can open with the fixed parser, the live gate, and the corrected schema all watching from the first record — which was the whole point of doing Step 1 first.
