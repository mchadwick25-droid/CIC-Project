# G05 Supplemental Source Review — Cold Review, Round 1

**Reviewer stance:** independent, no part in drafting. Every claim below was checked against the actual vendored XML, the actual repo git history, a live re-run of the actual gate battery, and the actual corpus-map files — not against the drafting session's own description of itself.

**Under review:** `records/pahc/gravity/pahc.gravity.boundary-drawing.md` (commit `70a3366`), `records/pahc/quote/pahc.quote.melito-no-phantom.md`, `records/pahc/quote/pahc.quote.asia-rejected-new-prophecy.md`, and the regenerated `worlds/pahc/build/GRAVITY-INDEX.md`.

**Checked against:** `cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` and `cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` directly (character-by-character); `CiC_W1_Doc04_Gravity_Discovery_FINAL.md`; `CiC_W1_Doc01_World_Identification_FINAL.md` §8.3; `cic/corpus-map/post-apostolic-house-church.yaml` and `montanism-the-new-prophecy.yaml`; `engine/m1/schemas.py` and `gates.py`; a live re-run of `gates.run_all`; `worlds/cappadocian/CAPPADOCIAN_BUILD_LEDGER.md`; `git show 70a3366`.

**VERDICT: SUBSTANTIAL REVISION REQUIRED — narrow, entirely confined to the citation-precision layer (two locus/line-number errors and one silently altered punctuation mark inside a quote flagged `verification_state: verified-direct`). The historical reasoning, the schema/engine mechanics, and the internal-consistency discipline are all sound and should NOT be reworked.**

---

## SUBSTANTIAL findings

### S1. The Melito quote's cited locus range silently covers only about half the actual quotation.

`pahc.quote.melito-no-phantom.md`, `sources[0].locus`: *"anf08 line 71176-71195"*. Its own trailing note: *"Text verified directly against ... at line 71176, no elisions."*

The fragment (`cic/texts/anf08...xml`) actually runs from line 71180 (the prose begins after the title/endnote at 71176–71179) through **line 71206** (`"...true God existing before all ages."`). Line 71195 — the record's own claimed end point — falls mid-sentence. Everything from *"For, being at once both God and perfect man likewise..."* through the end sits **outside** the cited range. The quotation itself is accurate; the locus that is supposed to let a reader find it is not.

### S2. A silent punctuation substitution inside a quote marked `verification_state: verified-direct`, `citation_specificity: A`.

The vendored text (`anf08...xml` line 71198) reads *"...He gave us sure indications of His two natures**:**"* — a colon. The record had typed a dash. Small, but exactly the defect class this project's own Step 5 gravity-records review (S3, the harp-image mis-quote) treats as substantial, because these records assert character-level fidelity.

### S3. The anti-Montanist quote's cited line number is off by three lines, and repeated identically across three records.

The actual sentence ("For when the faithful throughout Asia...") is at line **11308**; the quote's own `sources[0].locus`, its own trailing note, and the gravity record's `sources[]` entry all cited **11305** — a line inside an unrelated footnote. The quoted `text` field itself was independently re-extracted and diffed: byte-for-byte accurate throughout. Pointer error only, not a misquotation.

### S4. A second, already-vendored, independent primary-voice anti-Montanist witness sits unused inside the very source record this session reopened.

`pahc.source.second-third-century-remains` lists Apollonius among its ten authors. The vendored text (`anf08...xml` lines 72746–72790) preserves genuine fragments of his own c. 211 CE tract against Montanism — independent of the Anonymous/"Asterius Urbanus" fragment actually drawn on. Not previously disclosed in that source record's own "NOT DRAWN ON" list. Does not change any claim already made; flagged as available corroboration left on the table, not required to unblock this change.

---

## COSMETIC findings

**C1.** "a full four centuries" (Anastasius c. 686–689 vs. Eusebius c. 324) rounds up from ~366 years; "nearly four centuries" is accurate.

**C2.** "about two generations after Ignatius" understates the ~80–85 year gap to the anti-Montanist fragment (c. 192–193); "roughly three generations" is closer at a conventional ~30-year reckoning.

**C3.** `cic/corpus-map/post-apostolic-house-church.yaml` has no row for the anti-Montanist fragments (anf07 div1 v) — their only corpus-map presence is in `montanism-the-new-prophecy.yaml`. Confirmed real, but per the corpus-map's own README (outside the compile path; an `observe_corpus_map` cross-world observation, not a `gates.run_all` gate) this is bookkeeping, not a blocker.

**C4.** "primary-voice" for the doubly-mediated anti-Montanist testimony is defensible standard historiographical usage (primary in content, not direct in transmission) but could use a one-clause gloss for a reader unfamiliar with the convention.

---

## Verified clean (with method)

1. Both quote texts re-extracted programmatically and diffed against the vendored files: byte-for-byte identical (Melito, after the S2 fix; anti-Montanist, throughout).
2. Transmission-chain claim (Anastasius vs. Eusebius) confirmed true from the vendored file's own endnotes, not asserted.
3. Anti-docetic content parallel (Melito's "no phantom of the imagination" vs. Ignatius's Trallians 9–10 / Smyrnaeans 2) is a fair characterization, not a stretch.
4. Anti-Montanist content correctly characterized as off-topic for docetism — read the full surrounding passage (lines 11296–11319): no christological content whatsoever.
5. Doc_01 §8.3's Montanism paragraph confirmed to cite only secondary scholarship, no primary quotation — the new quote genuinely upgrades that specific disclosure obligation, scoped correctly to Montanism only.
6. Third-Asia-Minor-profile framing is quoted from Doc_04 (lines 218, 280), not invented.
7. Classification and six-test findings untouched — `git show 70a3366` confirms the diff touches only `sources[]`, `relations[]`, and two new disclosed paragraphs; `classification: tensional` and the confidence block are unchanged.
8. No fabricated attribution anywhere in the new material.
9. Schema conformance: both quote records satisfy `COMPLETION_REQUIRED["quote"]`; valid enums; reciprocal `illustrates`/`illustrated-by` relations in the correct direction.
10. Gate battery independently re-run: zero findings except the two pre-existing `reciprocity` findings (`enslaved-voices`/`womens-own-words`), matching `CAPPADOCIAN_BUILD_LEDGER.md` line 605 and confirmed as deliberately not fixed on Mark's own prior instruction.
11. `GRAVITY-INDEX.md` regeneration confirmed genuinely generated (byte-identical re-run), diff limited to boundary-drawing's source count (1→3).
12. Melito is properly covered by the corpus-map's existing whole-author row for "Fragments of Melito of Sardis" — Fragment VII is inside that already-assigned work, not a gap.
13. Both underlying source records (`second-third-century-remains`, `anti-montanist-fragments`) predate this session, per `git log --follow`.

## Round-2 verification

Performed directly against the current files (self-verified by the build thread, per this project's own established Step 5 precedent for narrow, mechanical fixes: check the actual current file state against each finding, not the fix's own description of itself).

- **S1 (locus undercount):** LANDED. `pahc.quote.melito-no-phantom.md` and `pahc.gravity.boundary-drawing.md` both now cite "anf08 lines 71176-71206." Re-extracted the full range from the vendored file and re-diffed against the record's `text` field: identical, start to finish.
- **S2 (colon silently changed to a dash):** LANDED. Restored the colon. This required converting the `text:` field from a bare/plain YAML scalar to a double-quoted scalar, because a bare colon-plus-space breaks plain-scalar parsing (`mapping values are not allowed here`) — confirmed by running the fix through `yaml.safe_load` and `engine.m1.loader.load_world_records('pahc')` directly; both now parse clean. This is very likely *why* the dash was there in the first place (a plain-scalar workaround rather than a deliberate transcription choice) — noted for the record, not asserted as certain.
- **S3 (anti-Montanist line number off by three):** LANDED. Corrected to line 11308 in the quote's own `sources[]` and trailing note, and in the gravity record's `sources[]`. Re-verified with `grep -n` against the live vendored file.
- **S4 (Apollonius left undisclosed):** LANDED, minimally. Added a dated disclosure to `pahc.source.second-third-century-remains.md`'s own "NOT DRAWN ON" list naming Apollonius's anti-Montanist fragments as available-but-unused corroboration, and separately dismissing Claudius Apollinaris as a false lead (his preserved fragments concern the Thundering Legion / Quartodeciman dispute, not Montanism). Deliberately did NOT build a new quote/source claim for Apollonius — the reviewer marked this optional and not required to unblock, and building it out would itself require a fresh review round; kept this integration pass narrow per the reviewer's own recommendation.
- **C1 (four centuries → nearly four centuries):** LANDED.
- **C2 (two generations → roughly three generations):** LANDED.
- **C3 (corpus-map gap):** Not acted on in this pass — confirmed non-blocking by the review itself; logged in this world's Decision Log as a follow-up item, not silently dropped.
- **C4 (primary-voice gloss):** Not acted on — cosmetic, at the drafter's discretion per this project's own Revision Decision rule for cosmetic-only findings.

Re-ran the full `engine.m1.gates.run_all` battery and the `generate_gravity_index.py` regeneration after all fixes: clean except the same two pre-existing, deliberately-untouched reciprocity findings; index byte-identical to its pre-fix state (only the two source loci's text changed, not any count or structure the index reads).

**VERDICT: All 4 substantial + 2 of 4 cosmetic findings LANDED; 2 cosmetic findings (C3, C4) logged and deliberately deferred, not silently dropped. Ready for disposition.**
