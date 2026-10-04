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

## 2026-09-09 — Genuine acquisition pass: Bar Hebraeus's Chronicon Ecclesiasticum, Odes of Solomon closed

**Deliverable.** Two long-open acquisition questions closed by direct research, not left as open questions with no record. This build session had unusual live WebSearch/WebFetch access, atypical for a build thread (normal intake is Mark supplying files, per `cic/texts/INTAKE.md`'s own "Trigger" section) - used here specifically to answer two genuine open questions this world already carried, not to originate content.

1. **Bar Hebraeus's Chronicon Ecclesiasticum.** Doc_02 SS11's Persian episcopal-succession content (Papa bar Aggai, Simeon bar Sabbae, and successors) rested only on Fiey's modern secondary reconstruction of the Chronicle of Seert/Bar Hebraeus tradition - no primary chronicle had ever been vendored. Verified findable and public domain: the Abbeloos-Lamy critical edition (Louvain: Peeters, 1872-1877), Latin translation of the Syriac, all three volumes on archive.org, uploaded by Roger Pearse - Vol. 2 and Vol. 3 each marked "Public Domain Mark 1.0," Vol. 1 marked with the older "creativecommons.org/licenses/publicdomain/" declaration (still public domain, a different specific license marker). Vendored Volume III (the Eastern Church/Nestorian Catholicoi section - the only volume this world's own citations need) as `cic/texts/barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt`. Verified directly against the Latin text that entry 11 names Simeon bar Sabbae as Papa's own disciple and immediate successor, credits him with instituting antiphonal (two-choir) prayer modeled on a Western practice the chronicle attributes to "the fiery Ignatius," decreeing psalms recited from memory rather than from a book, thirteen years in office, and martyrdom under Shapur II alongside four bishops and ninety-nine priests, deacons, and laity. Added `records/syr/source/syr.source.bar-hebraeus-chronicon-ecclesiasticum.md`, `Build/worlds/syr/build/records/search_record/syr.search.bar-hebraeus-chronicon-pd.md`, a `cic/corpus-map/_staging/barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.yaml` staging file (`confidence: assigned`, with an `authors_ruled` entry for `bar-hebraeus`, kind `metadata-omission` - the author slug isn't yet in the auto-generated `cic/texts/AUTHORS.md`, a mechanical index-coverage gap for this corpus's first plain-text-vendored named author, not an attribution dispute) merged into `cic/corpus-map/syriac-edessa-nisibis.yaml` and `cic/corpus-map/UNATTRIBUTED.yaml` via `corpus_map_merge.py`, a `cic/texts/REGISTRY.yaml` entry disclosing the unusual `supplied_by`, and a new `sources[]` entry on `records/syr/contested_claim/syr.contested.papa-primacy.md` (now citing the primary chronicle directly, alongside its existing in-copyright-consultation-only GEDSH source). Does NOT resolve the Simeon bar Sabbae redating dispute (341 vs. the Kosinski/Burgess c. 344 argument) - that rests on modern external regnal-year/astronomical reasoning a 13th-century chronicle cannot itself adjudicate.
2. **Odes of Solomon.** `syr.source.odes-of-solomon` had stood at `rights_status: pending-verification` with an OPEN acquisition request (`syr.search.odes-of-solomon-pd`) since the legacy Doc_02 - J. Rendel Harris's 1909/1911 translation was named as the expected public-domain edition but never vendored, so "the rights gate fails closed." Verified and vendored the exact named edition: Harris's 2nd ed. (Cambridge University Press, 1911), Cornell University Library scan via archive.org, whose own front matter states "There are no known copyright restrictions in the United States on the use of the text." Saved as `cic/texts/harris_odes-and-psalms-of-solomon_harris1911.txt`. Updated `syr.source.odes-of-solomon.md` (rights_status to `public-domain`, verification_state to `verified-direct` for the source's own bibliographic facts) and closed `syr.search.odes-of-solomon-pd.md`. Added a corpus-map staging file (`confidence: assigned`, with an `authors_ruled` entry for `odes-of-solomon`, kind `anonymous` - same mechanical index-coverage reason as the Bar Hebraeus ruling above), merged into the generated corpus map via `corpus_map_merge.py`. Deliberately did NOT write a quote record: the volume's English translation-with-commentary section (distinct from its unreadable-OCR Syriac text and its Latin-retroversion Pistis Sophia appendix) has real OCR noise (a spot-checked example: a superscript verse "4" rendering as a stray "*", "grudging" rendering as "g^idging") that needs verse-by-verse reconstruction before any specific wording could be certified `verified-direct` at the quote level - named as real follow-up work in the source record's own trailing note, not rushed to produce a quote this pass.

**Review outcome.** One round, independent, cold, adversarial, checking the Latin factual claims directly against the vendored text, the Odes file's own front matter and OCR quality, the rights/acquisition reasoning against `cic/texts/INTAKE.md`'s own rules, and schema/gate/corpus-map-tool correctness. [Verdict and findings recorded once the round lands - see below / this entry's own trailing update.]

**Escalation check.** Performed; no standing category applies. Not a Representative identity decision. Not portfolio/cross-world (world-specific acquisition, not a cross-world policy change). Not governance/methodology (uses this project's own existing INTAKE.md rules, doesn't change them). No unresolved tension between review rounds. The disclosed procedural deviation (this session, not Mark, supplied both files) is a transparency item, not an escalation trigger on its own - flagged plainly in every touched record rather than smoothed over, per this project's own standing discipline against silent process deviation.

---

## Source-form fragment re-author — 2026-09-25

`syr.quote.aphrahat-anti-jewish-frame`: the larger sentence-completeness
parser (P3 Decision-Log Entry 29) flagged the rendering "A reply to the
Jews, who blaspheme ..." as verbless. Under Mark's R44 ruling of
2026-09-24 ("true ellipses get finished"), the heading is finished with
the subject and verb its structure implies: "This is a reply against the
Jews, who blaspheme the people gathered from among the Gentiles." This
also restores the source's own "against"; the prior rendering had "to",
which softened the source's polemic. Only `modern_rendering` changed;
every other field is byte-identical. Authored by Opus. Sonnet 4.6 reads
translation twice; Haiku 4.5 reads expansion, recorded as a standing
disagreement in `Open_Gaps_Tracking.md` item 14. P3 Decision-Log Entry 37
carries the fleet-wide record of this pass.

Record-note history moved here from the record body under the standing
rule that a PR editing a live file also removes its commentary: the
record's F6-T cell was assigned 2026-08-27, when it had none and sat
outside coverage.
