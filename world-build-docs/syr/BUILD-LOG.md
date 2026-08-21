# syr — Record-native build log (steps 1–4)

**World:** #7, Syriac Christianity (Edessa/Nisibis), `syr` / `syriac-edessa-nisibis`
**Base:** the approved legacy build (Doc_01–Doc_09 + Decision Log, all Approved to proceed by Mark, 2026-07-07/08, with post-approval corrections through 2026-07-11) re-expressed in the Artifact-1 record schema, per the settled Step 0/Step 1 scope. Nothing in Doc_01's determinations was reopened.
**Stopping point (by instruction):** full content canon complete; **no** voice_craft, demonstration, compile, or admission work.

## Stage log

| stage | records | committed | checks at stage exit |
|---|---|---|---|
| corpus vendoring | cic/texts (47 files, from world/alexandria, unmodified) | `syr step 2 prep` | rights read from file headers |
| registry + world_core + source ecology | 1 world_core, 35 source, 16 search_record; SOURCE-REQUEST-MANIFEST | `syr steps 1-2` | full gate battery; only expected coverage blanks |
| lexicon | 9 term; LEXICON-INDEX | `syr step 3 (lexicon)` | FK ≤ 10 on all quick/plain meanings; reciprocity green |
| figures + gravities | 9 figure, 6 gravity | `syr step 3 (ecology, part 1)` | gates green; tension-coverage informational finding documented in-record |
| forces + contested claims | 13 force, 8 contested_claim; FORCES-INDEX | `syr step 3 (ecology, part 2)` | gates green; both required transmission entries present |
| answer canon | 22 doctrinal_witness, 3 honest_limit | `syr step 4 (answer canon)` | 26/28 cells closed; F5-I/F6-E deferred to stories by design |
| stories + quotes | 9 story, 18 quote, 1 source (reception dossier); STORY-INDEX | `syr step 4 (stories + quotes)` | **all 12 gates: 0 findings; 28/28 cells covered** |
| self-review + independent review | fixes | `self-review pass` + review-fix commits | see REVIEW-ROUND-1.md |

**Final census: 150 records** (36 source · 22 doctrinal_witness · 18 quote · 16 search_record · 13 force · 9 figure · 9 story · 9 term · 8 contested_claim · 6 gravity · 3 honest_limit · 1 world_core). Coverage: 27 cells substantive, 1 (F5-T) honest-limited — the deliberate honest route.

## Verification discipline applied

- Every `license: verbatim` quote mechanically verified as a normalized substring of its cited vendored file, this session; the one edition oddity ("than to that", NPNF Theodoret) kept exactly and flagged.
- Doctrinal-witness claims traced to vendored passages read this session or to approved legacy findings at their stated confidence; two claims found to outrun the vendored attestation during self-review (a trinitarian-formula phrasing; a baptismal-imagery phrasing; an unattested Simeon paraphrase) were corrected to exactly-attested content before review.
- Post-approval corrections honored throughout: School of Nisibis c. 489–496; malpana/choir-leadership excluded as in-window fact; Jacob of Nisibis death year open; Simeon dating dispute carried; Rabbula's role Contested; Ewangeliyon-da-Mhallete name-dating unresolved.
- canon_cells assigned at authoring time on every gravity/force/contested_claim; three contested claims and four late-window/reception records deliberately cell-less with in-record rationale.
- `gate_no_build_attribution`: 0 findings (no dates, rulings, or process language in compiled-facing fields).
- Experimental gates: `grounded-claim` 0 findings; `tension-coverage` 1 informational finding on `syr.gravity.authority-ambiguity` — a real asymmetry mirroring Doc_04's own Interaction Matrix (no opposing-pole record was ever mapped; the poles are internal to the ambiguity), documented in the record body. **For Mark's review, not auto-fixed.**

## Review round

An independent adversarial review (fresh-context agent, no authorship involvement) was dispatched over the full corpus against the vendored texts and the approved legacy documents; its artifact is `REVIEW-ROUND-1.md` in this directory, and its findings and dispositions are logged there and in the closing commits.

## Escalation check (CO-022 categories)

- Representative identity/name/title: **not touched.** The registry carries the prior-framework values (Yausep/Mar, ruled by Mark under the old framework) as working data, explicitly pending step-5a re-confirmation.
- Portfolio/cross-world: corpus vendoring reuses the fleet's shared cic/texts unchanged — additive, no cross-world decision made.
- Governance/methodology: none changed.
- Unresolved tensions: none created; the standing open questions (authority structure, dates) are carried as records, exactly as the approved documents instruct.
