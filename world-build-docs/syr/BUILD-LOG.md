# syr — Record-native build log (steps 1–5b/d)

**World:** #7, Syriac Christianity (Edessa/Nisibis), `syr` / `syriac-edessa-nisibis`
**Base:** the approved legacy build (Doc_01–Doc_09 + Decision Log, all Approved to proceed by Mark, 2026-07-07/08, with post-approval corrections through 2026-07-11) re-expressed in the Artifact-1 record schema, per the settled Step 0/Step 1 scope. Nothing in Doc_01's determinations was reopened.
**Stopping point (by instruction):** full content canon complete (steps 1–4); step 5's voice_craft record (sub-steps b/d) drafted and independently reviewed to a clean disposition. **No** demonstration (5c), voice validation (5e), compile, or admission work — those still wait on the M4 live-generation design.

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

An independent adversarial review (fresh-context agent, no authorship involvement) was dispatched over the full corpus against the vendored texts and the approved legacy documents. **Verdict: COSMETIC ONLY** — zero substantial findings across all 150 records; every verbatim quote independently re-verified exact; every settled legacy correction confirmed faithfully carried corpus-wide. Eight cosmetic findings (a garbled clause, an overstated search note, a sourcing-completeness gap in one contested claim, a mis-quoted paraphrase, an inherited arithmetic error, process-language residue in six non-compiled-but-adjacent fields, two trailing-body id typos, one mid-clause quote truncation) were applied directly per the build-cycle discipline for cosmetic fixes — no fresh review round required. Full detail and per-finding disposition in `REVIEW-ROUND-1.md`. Post-fix: full gate battery re-run, 0 findings; strictly-compiled fields re-scanned for build-attribution language, 0 violations.

## Step 5 (voice build) — sub-steps b/d only

Representative identity (name Yausep, role Mar) confirmed by Mark as
carrying forward from the prior framework; registry updated. `syr.voice.craft`
(the capped per-world voice layer: identity, flavor_notes, characteristic_concerns,
guard) drafted against the completed record corpus, then run through two
rounds of independent adversarial review (fresh-context agent, no
authorship involvement), following the same process the PAHC precedent
build used for its own voice_craft record.

- **Round 1** (`VOICE-CRAFT-REVIEW-ROUND-1.md`): verdict SUBSTANTIAL REVISION
  REQUIRED — 16 substantive findings (two fabricated source bodies in
  `identity`; an unattested martyr-quote category; a misstated contested_claim
  finding; a caution-4/caution-8/caution-5 violation apiece; a FORMATION
  TEST FAIL misread as lived experience; a living-tradition conflation in
  the sanctioned self-naming line; both LEGACY-PARTICIPANT-CARD-REFERENCE.md
  safety items omitted; a guard length/scope overrun; a structural gap
  with zero flavor-tagged notes) plus cosmetic findings. All fixed in a
  full revision; fixes independently re-verified in round 2.
- **Round 2** (`VOICE-CRAFT-REVIEW-ROUND-2.md`): verdict MINOR FIXES NEEDED
  — confirmed all 16 round-1 findings correctly fixed, then found one
  round-1 finding (the pastoral-warmth/dependency-amplifier safety item)
  still half-fixed, four new problems introduced by the fix pass itself,
  and six cosmetic items. Disposition of each is logged in `syr.voice.craft.md`'s
  own trailing body (round-3 revision note) rather than restated here;
  fixed directly (self-performed verification, not a third independent
  dispatch, matching the PAHC precedent's own practice for a comparably
  small, fully-enumerated residual) and re-checked against the gate
  battery.

Full gate battery (schema, completion, `gate_no_build_attribution`) and
an independent pronoun/fabrication scan re-run clean after each round's
fixes.

## Escalation check (CO-022 categories)

- Representative identity/name/title: **confirmed by Mark, in chat, 2026-08-22** — Yausep/Mar carries forward from the prior framework as the settled name and role. The registry entry is updated accordingly. Step 5a's full identity-emergence write-up (the rationale derived from this build's own completed records) is still owed when the voice build begins; that is drafting work, not an open decision.
- Portfolio/cross-world: corpus vendoring reuses the fleet's shared cic/texts unchanged — additive, no cross-world decision made.
- Governance/methodology: none changed.
- Unresolved tensions: none created; the standing open questions (authority structure, dates) are carried as records, exactly as the approved documents instruct.
