# Step 2 Source Ecology - Review Round 2

**World #3: Desert Monasticism** — branch `world/desert`, commit 84a9a288 ("desert step 2, review round 1: apply 5 substantial + 10 cosmetic findings")

**Reviewed:** the 24 source records in `records/desert/source/`, 10 search records in `records/desert/search_record/`, and `world-build-docs/desert/SOURCE-REQUEST-MANIFEST.md`, after the Round 1 revision.

**Reviewer stance:** independent, adversarial, no drafting or Round 1 context. Per this project's discipline, no fix was accepted on the revision's say-so: every one of the fifteen findings was re-verified against primary ground truth — direct grep/read of the vendored files in `cic/texts/`, the cleared Doc_02 and approved Doc_01, the prior build's record store (`cic-poc/backend/wrs/records/desert_world/source/`), and a fresh run of the full M1 gate battery. All 34 records were read in full; the entire revision diff was walked to check for newly introduced errors.

---

## A. Per-finding verification

### Substantial findings

**Finding 1 (Cassian edition gaps) — GENUINELY FIXED.** Ground truth re-established by direct read of `npnf211_sulpitius-severus-vincent-lerins-cassian.xml`: Institutes Book VI div3 at exactly line 21559 with "We have thought best to omit altogether the translation of this book." (stub body at 21565–66); Conference XII div3 at exactly 37466 with "Not translated." (37474); Conference XXII div3 at exactly 46037 with "This Conference is omitted." (46045). All four offending locations now state the omissions as edition facts:
- `desert.source.cassian-conferences.md` edition field carries an EDITION GAP clause with both Conference stubs at the correct line ranges, "twenty-two of twenty-four Conferences carry text," plus a CORRECTION HISTORY block that retracts the false division-count "check" and records the standing rule ("a division existing is not the text existing").
- `desert.source.cassian-institutes.md` edition field states the Book VI gap at 21559–21568, "eleven of the twelve books carry text," and correctly notes the omitted book sits inside the eight-faults psychology the source is registered for.
- `desert.search.cassian-npnf211.md` note now lists all three gaps with correct loci; the false "(it is not)" is gone, replaced by an accurate correction history.
- Manifest §2 row now reads "Edition gaps (checked at division-body level, Review Round 1): Conf. XII and XXII and Institutes Book VI are untranslated."

I additionally scanned the entire Cassian span (lines 14912–52260) for any further omission stubs the fix might have missed while claiming "only these three": the only "omit/not translated" hits are the three known stubs (plus an unrelated footnote). The new completeness claim ("twenty-two carry text / eleven carry text") is itself verified, not just asserted.

**Finding 2 (Palladius confidence upgrade) — GENUINELY FIXED.** `desert.source.palladius-lausiac-history.md` now carries `formation_confidence: Widely Accepted`, matching the cleared Doc_02 §2.1 ("Widely Accepted as to authorship, approximate date, and general content" — confirmed at Doc_02 line 86) and §9 (line 180). The record adds an explicit confidence-correction note naming the Round 1 finding and the principle (holding the Clarke file documents the edition, not the fourth-century facts). Its loci re-verified against the vendored txt: prologue at 185, Arsisius at 227, "I sojourned in this Cellia nine years" at 295 (confirmed as Palladius's own first-person statement, ch. XVIII), Pachomius ch. XXXII at 397ff.

**Finding 3 (Socrates anthropomorphite misfiling) — GENUINELY FIXED.** Independently re-grepped `npnf202`: the IV.23 division ("The Deeds of Some Holy Persons who devoted themselves to a Solitary Life") is at exactly line 13377, IV.24 ("Assault upon the Monks…") at 13720, "These are his words:" at exactly 13550, and there are **zero** "anthropomorph" hits between 13377 and 13719; the first hit is at 17687, in the Book VI Theophilus sequence (footnotes there cross-reference "chap. 7"). The record's work field now places the anthropomorphite affair in Book VI with an explicit "NOT in the IV.23–24 digression" clause, and the edition field carries the corrected division-boundary loci (13377; 13550–~13719; ~17687). Finding 9's loci corrections ride in the same field and are exact.

**Finding 4 (Gould/Veilleux unregistered) — GENUINELY FIXED.** Both records exist and are accurate:
- `desert.source.gould-desert-fathers.md`: *The Desert Fathers on Monastic Community* (Oxford Early Christian Studies, OUP, 1993) — matches srcDES017's own row verbatim (including the quoted "load-bearing in Doc_02's own SS1.3 argument yet had no registry row" and the academic.oup.com verification claim, both confirmed by direct read of srcDES017). Consult-only rights, weight `contested` with the rationale stated, and an honest fence that the specific venue of Gould's Rubenson critique is not pinned by this corpus.
- `desert.source.veilleux-koinonia.md`: *Pachomian Koinonia*, 3 vols. (Cistercian, 1980–1982) — matches srcDES018's row (confirmed by direct read).
- **Reciprocity verified:** gould ↔ rubenson-letters, gould ↔ antony-letters, veilleux ↔ pachomian-corpus all reciprocate (and the reciprocity gate passes). Gould's counter-position framing matches Doc_02 §1.3 (line 42) and Doc_01 §10 (line 145). Manifest G2 and the §2 registered-without-files note both now list Gould and Veilleux ("no load-bearing name floats unregistered"), and the "eight consult-only scholarship records" count is arithmetically right (Brakke ×2, Rubenson, Gould, Burton-Christie, Goehring, Rousseau, Veilleux).

**Finding 5 (Paieous / Kramer-Shelton conflation) — GENUINELY FIXED, in the correct form for an unconsultable edition.** `desert.source.nepheros-archive.md` now separates the two dossiers: Nepheros (mid-4th c., Kramer-Shelton 1987) vs. the "related but DISTINCT" Paieous correspondence (monastery of Hathor, 330s–340s, P.Lond. VI, ed. H. I. Bell, 1924). That split matches my own knowledge of the editions (P.Lond. VI 1913–1922 is the Bell 1924 Melitian archive of Apa Paieous; *Das Archiv des Nepheros* 1987 is the later dossier). Critically, the record does not overclaim the check: the archive-to-edition mapping is explicitly held at verified-via-authority with a stated instruction to re-check against the editions themselves before any figure or quote record leans on either monk by name — exactly what the finding demanded, since the editions remain unconsultable from this session. The characterization stays inside the cleared Doc_02 §5.2 (re-read: Hipponon/Heracleopolite, Melitian, "intermediary" organization, unverified-representativeness assumption all match), and the refinement of Doc_02's single-archive phrasing is explicit and attributed, not silent.

### Cosmetic findings

**Finding 6 (Festal Letters locus) — GENUINELY FIXED.** Direct read of npnf204: the Letters div1 is at exactly line 60975 and Letter 39's own div4 ("(For 367.) Of the particular books and their number, which are accepted by the Church…") begins at exactly line 68714. The record carries both, retires line 7291 with an explanation, and keeps an appropriate fragment-transmission caveat.

**Finding 7 ('Remoboth') — GENUINELY FIXED.** Grep confirms zero "remnuoth" hits in npnf206 and "Remoboth" at exactly line 6634. The record gives the edition's form as governing for locus matches, with the scholarly "remnuoth" marked as such.

**Finding 8 (npnf206 range start) — GENUINELY FIXED.** "There are in Egypt three classes of monks" confirmed at exactly line 6623; the record's range now opens there, and the two anchor loci (6630, 6724) still stand.

**Finding 9 (npnf202 loci) — GENUINELY FIXED.** Verified with Finding 3 above: 13377 division, 13550 "These are his words:", ~13719 end.

**Finding 10 (Bamberger) — GENUINELY FIXED.** Both the source and search records now cite "Cistercian Studies 4, 1970" (correct per my knowledge of Bamberger's *The Praktikos; Chapters on Prayer*), with the ACW misattribution recorded as corrected.

**Finding 11 (Cassian provenance) — GENUINELY FIXED.** Both Cassian records' discovery_channel now cites "srcDES026, added 2026-07-27 by change order CO-P2-10(c) - the cleared Doc_02 itself never rowed Cassian." Verified against srcDES026's own body by direct read: "Added per CO-P2-10(c)… Doc_02's ecology never rowed it," `added: 2026-07-27 (CO-P2-10c)`. Exact match.

**Finding 12 (manifest rights overstatement) — GENUINELY FIXED.** Manifest G1 now reads "public domain in the US (1907 publication) and in life+70 jurisdictions (Budge d. 1934); a few longer-term jurisdictions differ — the file's own front matter decides at vendoring." The false "everywhere since 2005" is gone; the replacement is accurate.

**Finding 13 (Rule-witness count) — GENUINELY FIXED in all three locations.** `pachomian-corpus` (three witnesses: Palladius XXXII, Sozomen III.14, Gennadius), `sozomen-historia-ecclesiastica` ("two content-bearing vendored witnesses… Gennadius's notice… is a third, thinner vendored witness — existence and the angelic-dictation frame only"), and `desert.search.pachomian-rule-english-pd` (same three, with the same thinness qualifier). The Gennadius locus (npnf203 line 42250, "Pachomius the presbyter-monk") re-verified directly.

**Finding 14 (not_found phrasing) — GENUINELY FIXED.** All four not_found records (pachomian-rule, pachomian-lives, antony-letters, evagrius) now phrase within the channel: "No public-domain English translation … was located, and this search knows of none."

**Finding 15 (commit-title count) — FIXED in the only available form.** The original commit title cannot be rewritten; the revision commit's message records the correction explicitly ("Prior commit title miscounted 16 source records; 22 shipped, 24 now").

## B. New-error check on the revision itself

The full diff of 84a9a288 (23 files) was walked. Every changed factual claim was re-verified above; the added prose (Vita emic-register rationale; the ammas-fold RECORDED DECISION carrying Doc_02 §1.6's exact bounds — Widely Accepted presence for Syncletica/Theodora/Sarah, Inferential-Thin beyond the sayings, confirmed against Doc_02 lines 64/71; the Cassian correction histories) introduces no new factual claims that fail verification. **No fix introduced a new error.**

## C. Fresh adversarial pass

Independently checked beyond the Round 1 surface: Cassian division loci 14912/16537/25863/36699/42272 (all exact); Vita divisions 30411/30986 and §§46–47 quotes at 32364/32399–32400 (verbatim); De viris "Antonius the monk" at 41173; Sozomen I.12–14 (confirmed as the monastic chapters: div3 ids iii.vi.xii–xiv, "On the Organization of the Monks," "About Antony the Great," "Account of St. Ammon," lines 27196/27307/27423) and VI.29–31 monastic census chapters; the Payne Smith revision note at npnf204 line 62177; Jerome Letter 22's internal "third class" usage (see observation 2); Doc_02 §§1.3, 1.6, 5.2, 9 consistency; srcDES017/018/026 ground truth; the confidence rule (the only Documented records without verified-direct are Kellia and Nepheros, both carrying non-null divergence_notes); manifest arithmetic (9 supplied + 7 unvendorable + 8 consult-only = 24; 6 found + 4 not_found = 10 search records).

**M1 gate battery executed** (engine.m1.loader → 34 records; run_all with fleet + registry): schema-validation, referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, no-build-attribution all PASS; canon-coverage FAIL on blank cells only — correct and expected at step 2.

**New findings:** no substantial findings. Two cosmetic-grade observations, neither blocking:

1. **COSMETIC — Festal Letters reviser uncredited.** `desert.source.athanasius-festal-letters.md` says "the 1854 Oxford rendering as revised in Robertson's NPNF" — accurate, but the volume's own note (npnf204 line 62177) credits the revision to Miss Payne Smith, and this record set otherwise follows a per-work translator-credit discipline (Ellershaw, Gibson, Zenos, Hartranft, Fremantle, Richardson, Clarke are all named). Pre-existing wording, untouched by the revision except for the locus; add the name whenever the record is next edited.
2. **Observation (no action) — the double "third class" in Jerome Letter 22.** The vendored edition itself calls Remoboth "the class called Remoboth… Thirdly" in the §34 enumeration (line 6634) and then calls anchorites "the third class" in §36's discussion order (line 6724). Both of the record's statements are verbatim-accurate to the file; a one-line note would spare a step-4 builder momentary whiplash, but nothing in the record is wrong.
3. **Observation (carried from Round 1, unchanged by design)** — `records/worlds.yaml` still has no desert entry; no gate requires it at step 2, and registration remains a compile-time concern for the build thread to confirm.

---

## VERDICT: CLEARED - no substantial revision required

All five substantial and all ten cosmetic Round 1 findings are genuinely fixed, verified against the vendored files, the cleared Doc_02, and the prior build's record rows — not against the revision's own claims. The fixes' new assertions (the "only these three gaps" completeness claim, the Gould/Veilleux registration details, the two-archive Nepheros split) were themselves re-verified and hold. No fix introduced a new error; the fresh pass surfaced nothing above cosmetic grade. Gates are green except expected canon-coverage. The two cosmetic observations above can ride along with the next routine edit; neither warrants a revision cycle.
