# REVIEW-ROUND-1 — Adversarial Review of the syr Record Corpus (World #7, Syriac Christianity)

Reviewer: independent adversarial review thread (no part in authoring). Date: 2026-08-21.
Scope: all 150 records under `records/syr/`, checked against the vendored primary texts in `cic/texts/`, the approved legacy build documents in `Build/worlds/syr/`, and the fleet canon questions in `engine/canon/records/canon_question/`.

## Verdict

**COSMETIC ONLY.** All eight findings below were applied directly, without a fresh review round, per the build-cycle discipline for cosmetic fixes. See the "Disposition" line added to each finding.

No finding changes any claim's substance, confidence rating, sourcing conclusion, or scope boundary. Every verbatim quote was independently re-verified against the vendored files and found exact, with correct loci. Every settled legacy correction named in the review brief (window 200–410; School of Nisibis c. 489–496, never 350; Jacob of Nisibis death year held open 338 vs 350; malpana/choir-leadership excluded as in-window fact; Bardaisan Named Comparandum, not founding voice; Aphrahat's episcopal status open; Papa bar Aggai's primacy contested; strand-singular; persecution asymmetry as a Forces matter; anti-Jewish material stated as entirely one-sided with no invented balance) is faithfully carried, in most cases enforced redundantly across multiple record types. The findings below are precision and hygiene defects that should be fixed but do not require re-derivation of anything.

## Numbered Findings

### 1. `syr.force.raza-inheritance` — garbled manifestation text (cosmetic)

Problematic text (manifestations field):

> "creation's own furniture - light, water, oil, the vine - read as razaputting truth within reach of the unlettered"

"razaputting" is a run-together of "raza" and a following clause (missing punctuation/space, and possibly a dropped word such as "—" or ", putting"). File: `records/syr/force/syr.force.raza-inheritance.md`. Severity: **cosmetic** (text corruption in a compiled-adjacent field; no factual content affected).

**Disposition: FIXED.** "razaputting" corrected to "raza, putting".

### 2. `syr.search.aphrahat-complete-english-pd` — overstated note about the anti-Jewish Demonstrations (cosmetic)

Problematic text (note field):

> "The anti-Jewish Demonstrations are among those NOT in PD English"

Stated flatly, this is in tension with the record set's own evidence: Demonstration XVII — whose own opening, "a reply against the Jews, who blaspheme the people gathered from among the Gentiles," is quoted verbatim from the vendored PD NPNF text in `syr.quote.aphrahat-anti-jewish-frame` (verified at `npnf213…xml` line 27100) — and Demonstration XXI (which stages the Jewish debater's taunt, XXI.1, verified at line 27416) ARE in PD English and are vendored. The record's own trailing body hedges correctly ("including most of the anti-Jewish set"); the note field does not. The core adversus-Judaeos set ("roughly four Demonstrations" per Doc_02 §2, none of them 17 or 21 necessarily) is indeed outside PD English, so the substantive coverage conclusion stands; only the flat phrasing is wrong. Severity: **cosmetic** — fix the note to match the trailing body's hedge.

**Disposition: FIXED.** Note reworded to state that Dem XVII/XXI (in PD English) carry anti-Jewish material of their own, while the fuller anti-Jewish set is mostly outside PD English — matching the trailing body's hedge.

### 3. `syr.contested.jacob-death-year` — the most direct vendored 338 witness is not cited (cosmetic)

The record grounds the 338 pole only in the (unvendored) Martyrologium Hieronymianum, and its sole `sources` entry is Theodoret II.26 (the 350-side tradition). But the vendored Chronicle of Edessa itself carries the 338 pole directly: entry 17, "In the year 649 [Seleucid = 337/338 CE], died Mar Jacob, bishop of Nisibis" (`cic/texts/chronicle-of-edessa_cowper.txt` line 77). The record set registers and quotes this chronicle elsewhere, so the omission is a sourcing-completeness gap, not an error of fact; adding it would not resolve the open question (the Chronicon Paschale conflict stands), so the held-open determination is unchanged. Note also the structural oddity that the `held_against` list contains a bullet supporting the claim ("the Martyrologium Hieronymianum implies 338") — it reads as "held against settling," which should be made explicit. Severity: **cosmetic**.

**Disposition: FIXED.** Added the vendored Chronicle of Edessa entry 17 ("died Mar Jacob, bishop of Nisibis," year 649 of the Greeks) as a direct 338-pole source; reworded the claim and held_against list so both poles' evidence is clearly labeled as bearing on the dispute rather than one bullet silently supporting the claim it's nominally held against.

### 4. `syr.source.jerome-de-viris` — non-verbatim wording inside quotation marks (cosmetic)

Trailing body:

> "…his writings are publicly read in some churches after the Scriptures"

presented inside quotation marks as Jerome's wording. The vendored text (`npnf203…xml` lines 41536–41545) reads: "became so distinguished that his writings are repeated publicly in some churches, after the reading of the Scriptures." The paraphrase is accurate in substance but should not wear quotation marks in a corpus whose whole discipline is verbatim-vs-paraphrase hygiene. (This is in a trailing note, not a compiled field, and it is not a quote record.) Severity: **cosmetic**.

**Disposition: FIXED.** Quotation marks removed; wording now paraphrased in the trailing body, with the exact vendored phrasing ("repeated publicly in some churches, after the reading of the Scriptures") given as the true quotation.

### 5. `syr.story.jacob-deliverance` — inherited arithmetic imprecision, "~130-160 years" (cosmetic, legacy-inherited)

`narrative_tier_justification`: "Theodoret, writing ~130-160 years after the sieges (338, 346, or 350…)". Theodoret's Historia Ecclesiastica was composed c. 444–450 and he died c. 460; the distance from the sieges is roughly 95–120 years, not 130–160. The figure is carried verbatim from the approved legacy chunk `Story-Chunks/syrstory006_jacob-nisibis-deliverance.md` (line 29), so the record faithfully re-derives an approved finding — but the approved figure itself is off, and the same "130–160" recurs in `syrstory001`'s comparative tiering argument. Nothing depends on it (the Tier 3 classification rests on genre and earliest-attestation grounds, which hold at either figure). Severity: **cosmetic**; recommend correcting the number in the record and flagging the legacy figure rather than propagating it further.

**Disposition: FIXED.** Corrected to "roughly 95-120 years" (Theodoret's Historia Ecclesiastica, c. 444-450, minus the siege years 338-350), with a note that this corrects rather than propagates the approved legacy chunk's own figure.

### 6. Process language in compiled-adjacent (not compiled-spoken) fields (cosmetic)

The strictly spoken fields named for this review — world_core horizon/formation_logic/thinness/cautions, term plain_meaning/quick_meaning, doctrinal_witness text, honest_limit statement, story tellable_as/text, quote text — were scanned and are **clean**: no "Doc_", no ISO dates, no reviewer names, no build-process vocabulary. However, adjacent structured fields carry process references that would need scrubbing if those fields are ever surfaced:

- `syr.figure.jacob-of-nisibis` and `syr.figure.simeon-bar-sabbae` `dates` fields: "held OPEN, never resolved in this record set (world_core caution 10)".
- `syr.story.abgar-addai-legend`, `syr.story.edessa-flood-201`, `syr.story.ephrem-famine-death` `narrative_tier_justification` fields: "the settled Doc_01 determination", "per the legacy repository", "The legacy repository's Round 1 review".
- `syr.dw.f4-p-penitence-prayer` `tensions`: "not this record's idiom".
- `syr.contested.qyama-structure` `held_against`: "(Doc_01 SS4's explicit flag)"; `syr.contested.jacob-death-year` `concedes`: "the legacy build's standing instruction".
- `syr.limit.f5-enslaved` `why_sources_cannot_answer`: "(the legacy source ecology's own finding)".

Whether these fields are compiled-facing is a schema question this review does not decide; flagged so the decision is deliberate. Severity: **cosmetic**.

**Disposition: FIXED.** All five instances scrubbed (figure.dates x2, story.narrative_tier_justification x3, doctrinal_witness.tensions x1 reworded for clarity, contested_claim.held_against x1, honest_limit.why_sources_cannot_answer x1) — Doc_XX/legacy-repository/world_core-caution cross-references removed from YAML fields; the underlying facts stated plainly instead. Provenance remains available in trailing markdown bodies, which are never compiled.

### 7. Trailing-body companion-quote id drift (cosmetic)

- `syr.dw.f4-p-penitence-prayer` trailing body names "aphrahat-medicine-of-penitence"; the actual record is `syr.quote.aphrahat-medicine-penitence`.
- `syr.dw.c-i-jesus` trailing body names "ephrem-only-begotten"; the actual record is `syr.quote.ephrem-only-begotten-dwelling`.

Both are non-binding notes (relations/machine fields are correct — verified by script: all relation targets and source_ids across all 150 records resolve). Severity: **cosmetic**.

**Disposition: FIXED.** Both trailing-body notes corrected to the actual record ids (syr.quote.aphrahat-medicine-penitence; syr.quote.ephrem-only-begotten-dwelling, plus the other two companion ids in that same note given their full syr.quote. prefix).

### 8. `syr.quote.pearl-mysteries` — mid-clause truncation without ellipsis (cosmetic)

Quote text ends "…pertaining to the Kingdom; semblances" — a verbatim substring (verified, `npnf213…xml` line 21794: "…mysteries pertaining to the Kingdom; semblances and types of the Majesty…"), but the cut lands mid-clause with no ellipsis marker, so a reader cannot tell the sentence continues. Severity: **cosmetic**.

**Disposition: FIXED.** Quote extended to the sentence's natural end ("...mysteries of the Son.") rather than left mid-clause; re-verified verbatim against the vendored file.

## What Was Checked and Found Clean

**All 18 quote records — every verbatim text found exactly in the cited vendored file, loci verified:**

- `abgar-letter` — `addai_doctrine-of-addai.txt`, contiguous match confirmed, legend-license framing correct.
- `aphrahat-anti-jewish-frame` (do-not-voice) — npnf213 line 27100 = Dem XVII.1 (div iii.ix.viii). Correctly held as do-not-voice with the violation-detection rationale.
- `aphrahat-medicine-penitence` — Hallock file line 29 = Dem VII.2. `aphrahat-one-innocent` — line 28 = VII.1. (File confirmed to contain Dem VII and II; VII.1/VII.2 numbering verified in the file's own section numbers.)
- `aphrahat-persecuted-litany` — npnf213 line 27954 = Dem XXI.22 (div iii.ix.ix, "Of Persecution"); litany's continuation through David (Heb. xi apparatus) to Jesus (§23) confirmed.
- `aphrahat-stone-foundation` — line 24606ff = Dem I.2. `aphrahat-sure-thing` — lines 27110–27121 = Dem XVII.2, exact through "…the Door, and the Pearl, and the Lamp". `dem6-visit-the-sick` — line 25658, div iii.ix.v = Dem VI.
- `blc-one-name` — anf08 line 68966ff (div ix.xvi), exact including "Christ—Christians" and "the days of the readings"; comparandum framing (Philip's dialogue) correct.
- `chronicle-flood-line` — Cowper line 53, exact; the 201-vs-202 era-convention discrepancy with the edition's own footnote is disclosed, not hidden.
- `ephrem-only-begotten-dwelling` and `ephrem-resurrection-pledge` — npnf213 lines 22305–22316, Homily on Our Lord opening, both exact.
- `nativity-this-is-the-day` — line 17530, div iii.v.ii = Nativity Hymn I (Morris/Gwynn, as the record states).
- `nisibene-death-trembled` — line 15643 inside div iii.iv.xxiv, whose own header reads "Hymn XXXV. Concerning Our Lord, and Concerning Death and Satan" — locus exact.
- `palladius-hospitaller` — Clarke file line 471, exact including punctuation; attribution correctly to the account's rendering.
- `pearl-mysteries` — line 21794, The Pearl I.1 (see finding 8). `sozomen-melodies` — npnf202 line 32089, inside Book III chapter 16 ("Concerning St. Ephraim") — III.16 confirmed by div structure. `theodoret-gnats` — npnf203 line 11175, inside Book II chapter "Of the siege of the city of Nisibis…" = II.26 confirmed; the edition's own "than to that" oddity kept as printed, as the record says.

**All 22 doctrinal_witness records read in full; spot-verified textual claims all held:** the seed argument (Dem VIII, npnf213 line 26401, div confirmed "Of the Resurrection of the Dead"); the XXI.1 taunt; the house-built-on-the-Stone/works-for-the-King teaching (Dem I, lines 24660ff); Dem XXII's title "Of Death and the Latter Times"; "the Kingdom which requites all" (On Our Lord); baptismal womb/white-robe imagery present in the Epiphany division (with the Beck authenticity discipline correctly enforced — voiced as "the churches' own singing"); "Three spiritual Names" baptismal language (line 20574); Sozomen III.16 containing both the famine account and Basil's admiration; Sozomen II.9's "excessive taxes" and Roman-sympathy accusation against Symeon; Socrates VII.8's Maruthas narrative with headache/fraud miracle elements correctly framed as church memory; Theodoret IV.26 on Ephraim; Jerome "Ephrem the deacon" chapter (div v.iii.cxvii) and "died in the reign of Valens". No fabricated claim was found in any doctrinal_witness text; the anti-Jewish one-sidedness is stated in C-T, F3-P, F6-I with the no-invented-balance rule carried in the tensions fields each time.

**All 6 gravity records vs Doc_04:** classifications match exactly (C1/C2 Primary, C3/C5/C6 Supporting, C4 Tensional); the C4 Formation-test FAIL is carried un-softened; C2's narrowed evidentiary basis (Dem 6 + dual-attested ihidaya, Ephrem-choir claim excluded) matches the Round 2 fix; ihidaya's VI.8 / VII.20 loci match Doc_06 §84, and Dem VI.8's English ("solitaries") confirms the attestation; the C2×C6 "no demonstrated relationship" cell and C4's no-tension-with shape match Doc_04's Interaction Matrix.

**All 13 force records vs Doc_08:** the six-cell coverage is complete (1A-1, 1A-2, 1B-1, 1B-2, 1B-3, 2A-1, 2A-2, 2B-1, 2B-2, 3A-1, 3A-2, 3B-1, 3B-2 — including both required transmission entries); the twenty-year vacancy, the Simeon redating dispute (341 vs c. 344, Kosiński/Burgess), the Reported-Experience/stated-absence discipline for the vacancy's interior and the 410 reception, and the persecution-asymmetry-as-Forces ruling are all carried faithfully. Abgar IX's execution (not imprisonment) matches Doc_01's Round 3 cosmetic fix.

**All 9 figure records:** Bardaisan narratable-false with full mediation caveats; Aphrahat narratable-false with the Wright-argument and no-live-current-debate caution from Doc_02 §11; Ephrem's narratable set correctly bounded (deaconate, 363 relocation, famine relief; malpana/choir-leadership/Vita excluded); Rabbula correctly out-of-window with the Vööbus contest; Tatian and Papa correctly non-narratable; Simeon's date dispute in the dates field itself. Doc_02's corrected tenth-century "Aphrahat" name attestation (Bar Bahlul, Elias of Nisibis) and the 510 colophon are carried exactly.

**All 9 term records vs Doc_03/Doc_06 and the Lexicon chunks:** Catholicos as flag-only anachronism guard; Peshitta correctly excluded as in-window vocabulary; the da-Mhallete name-dating contest quarantined; memra as anachronism guard; Mar at Tier 3; the qyama do_not_retrieve_when rule mechanically enforcing the choir-leadership exclusion; tahwyata's "ten of twenty-three in PD English" arithmetic checks (NPNF 8 + Hallock 2).

**All 8 contested_claim records:** each matches the legacy determination it re-derives, including the Bardaisan Nicene-floor A2 determination in full (Possekel's resurrection reconstruction, the docetism charge not sticking personally, the Ramelli calibration, Skjaervø as named minority), edessa-origins, papa-primacy (with the "settled parallel hierarchy" overstatement corrected as in Doc_01 Round 3), and qyama-structure.

**All 3 honest_limit records:** match Doc_02 §7's Harvey findings; statements are in-voice and clean; the enslaved-persons limit is absolute with no borrowed inference.

**All 9 story records vs Doc_09 and the Story-Chunks:** tier assignments match (no Tier 1 anywhere — the syrstory001 reclassification carried; single Tier 4 composite with every element separately attested and Inferential-Thin confidence; no Tier 5 anywhere); the Jacob-deliverance roles (Jacob prays, Ephrem urges — never reversed) match Theodoret's vendored text; the Basil legend carries the mistaken-identity (Eusebius of Emesa) correction; the choirs-tradition story keeps the two evidentiary layers explicitly unblended; the Simeon double-tax/collector detail matches syrstory005; the Absent Stories question is answered specifically in the world_core body.

**Sources (all 36 inventoried; ~28 read closely):** edition/translator credits for npnf213 (Stopford/Bickell, Morris, Johnston/Lamy, Johnston/Parisot, ed. Gwynn) verified against the volume's own preface (lines 10455–10510); the Hallock rights exception documented with the project-lead acceptance; the Odes of Solomon correctly fail-closed pending vendoring (and no record quotes them); GEDSH carries the 489–496 School correction; Kayaalp's baptistery-secure/cathedral-hypothetical split matches Doc_02 §6 and its Round 2 walk-back; the corrected Malki Malki 2024 citation (Religions 15(6):686) appears — the fabricated "Seppälä" citation does not appear anywhere; consultation-only sources are uniformly never quoted verbatim.

**Search records (13 of 16 read):** not_found results (complete Aphrahat PD, Persian martyr acts, Synodicon Orientale, Liber Graduum, complete Ephrem cycles) all consistent with the vendored corpus's actual contents; the Acts-of-Thomas exclusion decision is auditable.

**Mechanical checks (scripted, all 150 records):** every `relations[].target` and every `sources[].source_id` resolves to an existing record id; all `canon_cells` values are valid cells; all 28 canon cells are covered by at least one record; cell assignments spot-checked against the fleet canon_question texts (C-P physician answers the "want to believe but can't" question; F5-I limits answer the enslaved/women questions; F6-E simeon-martyrdom explicitly serves the martyrdom-death-wish question; F5-T marriage limit matches the marriage question; F2-E record-honesty matches the library question) — no mismatched cell found. Compiled-spoken fields scanned corpus-wide for "Doc_", ISO dates, reviewer names, and build vocabulary: clean (see finding 6 for adjacent fields). `records/worlds.yaml` syr entry consistent with the record set (window 200–410, Mar role, living_tradition_flag with pending re-confirmation noted).

**Fabrication watch:** no factual claim in any doctrinal_witness or story text was found unsupported by the cited vendored sources or the legacy documents; no Persian-side fact generalized to the whole world or vice versa (the frontier inversion, the tax, the vacancy, and the sieges are all correctly scoped; Roman-side Edessa is consistently described as without sustained state persecution in-window); no balancing voice, internal dissent, or Jewish counter-testimony was invented anywhere for the anti-Jewish material — its one-sidedness is stated as such in every record that touches it.
