# Doc_06 — Full Interpretive Lexicon Development: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-15.

**Documents reviewed as one co-produced Step 6 deliverable, per their own stated Disposition:**
- `Doc_06_Full_Lexicon_Development.md` (136 lines), DRAFT, no prior review round.
- `Lexicon-Chunks/lpclex001_the-flock.md` through `lpclex018_libellatici-sacrificati.md` — all eighteen chunks read in full.
- `Lexicon_Deployment_Index.md` (all eight sections).

**Read as governing standard, not reviewed:** `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0; `CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx` (full text extracted from `word/document.xml` and stripped of markup); `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part III and Part VII (cited by Doc_06; not separately extracted this round beyond confirming the Step 6 activity-list language Doc_06 quotes); `CiC_L1_Constitution_V2_2.docx` (full text extracted; Articles 17, 19, 26, 30 located by heading); `Doc_01_World_Identification_Boundaries_Orientation.md` (companion citations only), `Doc_02_Source_Ecology.md` (companion citations only), `Doc_03_Lexicon_Candidate_List.md` (full), `Doc_04_Gravity_Discovery.md` (full) and `Doc_04_Superseded_Claims.md` (referenced, not opened — nothing this round rests on it), `Doc_05_Ecological_Reconstruction.md` (full), `Source_Registry.md` (row lookups only, not read cover to cover), `/home/user/cic-project/CLAUDE.md`. `World-Builds/Imperial-Juridical-Christianity/Lexicon_Deployment_Index.md` and its `Doc_06` read for house form only, per the assignment's own instruction.

**Read at source and independently re-run:**
- Every Master Table cell in `Lexicon_Deployment_Index.md` §1 was **re-derived programmatically from the eighteen chunk files** (a Python script parsing each chunk's front-matter block: Term, Tier, Tags, Aliases, Related-Terms, plus a regex sweep of each chunk's own body for `Registry row(s) N` citations and for the literal string "Author Gravity note") and diffed cell-by-cell against the index's printed table. This is the direct test the assignment and the index's own header both invite ("re-deriving it is the check: regenerate and diff").
- Every Related-Terms edge across all eighteen chunks was parsed independently (not read off the index) and checked for reciprocity by building the directed-edge set and testing `(a,b) ∈ edges ⇒ (b,a) ∈ edges` in both directions.
- Every quotation checked below was located and character-compared against the vendored source: `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (Cyprian) and `cic/texts/npnf101_augustine-confessions-letters.xml`, `npnf104_augustine-anti-manichaean-anti-donatist.xml` (Cyprian's own quotes are all in `anf05`; the Augustine quotes checked span `npnf101` and `npnf104`).
- The *libelli*/`libell-` headword-absence claim and the *plebs*-occurrence claim were each independently re-run against the raw XML, scoped to Cyprian's own `div1` section specifically (`id="iv"`, `title="Cyprian."`), not the whole `anf05` volume (which also contains Hippolytus, Caius and Novatian).
- Doc_03's Tier 1 flag column was independently tallied (12 Yes / 6 No), and each of the four terms Doc_06 §2.2 reports as down-tiered, plus the one held at Tier 2 (§2.3) and the two moved to Tier 3, were traced back to their specific Doc_03 row and forward to their specific Doc_04/Doc_05 citation.

### A check that failed and was confirmed before being trusted (per the assignment's own instruction)

My first pass on the *plebs* claim (chunk `lpclex010`: *"a sweep of the vendored Cyprian corpus returns exactly three occurrences, all three inside the 19th-century American editor's introductory and elucidatory prose, none inside Cyprian's letters"*) ran an unscoped, whole-file, case-insensitive regex against `anf05` and returned **seven** occurrences, not three — an apparent contradiction. Before reporting that as a finding, I mapped each hit to its enclosing `<div1>` and found four of the seven sit in `div1 id="iii"` (Hippolytus's material, which precedes Cyprian's own `div1 id="iv"` in the same bound volume and is not part of "the vendored Cyprian corpus" the claim is about) and the remaining three sit inside `<note>` elements within Cyprian's own `div1 iv` — i.e., editorial endnotes, not Cyprian's letters. Rescoped correctly, the claim is **exactly right**: three occurrences, all editorial, none in Cyprian's own words. My own first check was the one measuring something adjacent to the claim (whole-volume vs. Cyprian's-own-corpus); the document under review was not. This is recorded per the assignment's instruction rather than silently discarded.

### Method

I drafted nothing under review and hold no prior position on any tier, tag, or classification here. I treated every quoted string as a claim to re-check regardless of a "re-verified at source" note attached to it, and every characterization of Doc_03/Doc_04/Doc_05 as a claim to verify against those documents directly rather than against Doc_06's gloss of them. Where the index claimed to be script-generated and diffable against the chunks, I generated the diff myself rather than accepting the claim because the mechanism sounds sound.

---

## VERDICT: REVISION REQUIRED

**Findings: 3 HIGH · 3 MEDIUM · 2 LOW · 0 COSMETIC — 8 in total.**

**What holds up.** This is a carefully built deliverable and the five house review-questions mostly clear it. Every direct quotation checked against the vendored XML — the *De Lapsis* grief and watch-keeping passages, the 256 preface's egalitarian formula (including its exact, unbracketed-then-bracketed editorial interjection), the *De Unitate* "God for his Father" line, Epistle XXXIX's "suffrage"/"ancient venom" language, *On Baptism* II.3's plenary-councils passage and its "neither sacrament may be wronged" passage, and both halves of the "compel them to come in" parable exegesis — reproduces exactly. Reciprocity is genuinely perfect: an independent parse of all eighteen chunks' Related-Terms fields returns 110 directed edges forming 55 reciprocal pairs with zero one-directional links, matching the index's own claim precisely. The By-Tag counts in `Lexicon_Deployment_Index.md` §3 (AS 6, SC 12, DR 8, TC 10, RT 8, PV 11, CT 3) all independently reproduce from the chunks. The CT Contest Type check (§4) is accurate: exactly three CT-tagged terms, all three with a substantive, specific, non-templated Contest Type section. The Author-Gravity-Risk column (§6) matches the presence/absence of an "Author Gravity note" in each chunk exactly, all seven Yes cells verified. No analytical-distance marker ("scholars believe," "this reflects," "the sources indicate," "evidence suggests," "historically," "reconstruction," and near-variants) survives anywhere in any World Meaning section across all eighteen chunks — a full, clean pass. Doc_06's tier-reasoning is traceable rather than asserted: the "twelve of eighteen" Doc_03 Tier-1-flag count, the four down-tiered terms' grounding in Doc_04 Candidate 4's classification and Doc_05 §5.2's restatement of it, the *libelli*/*libellatici* headword-absence and editorial-endnote claims, and the "compel them to come in" Tier 2 argument against Doc_04 §2's declined-candidate finding all check out against the cited documents directly, not against Doc_06's paraphrase of them. The escalation-category assessment is complete and accurate against Doc_04's and Doc_05's own disposition records.

**What does not.** The index's own central boast — that it is script-generated and safe to re-derive and diff — fails on direct re-derivation for one cell. One tag contradicts an explicit, on-the-record instruction from the very document it is supposedly carried forward from, with the contradiction visible against the deliverable's own Cross-Build Sheet. And the editorial-apparatus register, built specifically to keep 19th-century editorial matter out of this world's own voice, missed one live instance of exactly that failure mode inside a Tier 1 entry — one document after the same material had been caught and correctly disclosed. None of these touch the tier spine, the CT tagging, the quote fidelity, or the great majority of the deliverable's claims, which is why this is REVISION REQUIRED and not SUBSTANTIAL REVISION REQUIRED.

---

## The five lexicon-index review questions, answered directly

**1. Is the master index actually derived from the same chunk files, or has it already drifted?** **Mostly yes, with one confirmed drift.** Re-deriving the full Master Table programmatically from the eighteen chunks and diffing it against `Lexicon_Deployment_Index.md` §1 cell-by-cell (Tier, all seven tag columns, Aliases, Related-Terms, and the Registry-row citations parsed out of each chunk's own Key Sources prose) turns up exactly one mismatch, at row 01: see **H1** below. Every other one of the 18×13 cells I checked matches exactly. The index's claim to be diffable is itself true and is what let this defect surface in the first place — the drift is real but narrow.

**2. Does every CT-tagged term have its Contest Type section actually completed?** **Yes, all three, no exceptions.** *grace*, *schism*, and *"compel them to come in"* each carry a `## CT Contest Type` section naming a primary and secondary contest type and stating, in a dedicated closing sentence, what the entry therefore does not do. None is templated or vague. This is the one check this skill's own guidance names as the most common lexicon gap, and it is not a gap here.

**3. Does every World Meaning read from inside the world's own ecology, with no analytical-distance markers surviving?** **Yes, cleanly, across all eighteen entries.** I extracted every World Meaning section (and the two Tier 3 entries' Quick Meaning, which stands in for it per template) and swept for "scholars believe," "this reflects," "the sources indicate," "evidence suggests," "historically," "reconstruction," and a wider net of softer equivalents ("seems to," "appears to," "we know," "the record shows," "modern historians/scholars," "later readers"). Zero hits. Grace's chunk correctly carries the Reported-Experience Status marker verbatim rather than hedging around it. This is a genuinely clean result and I report it as such rather than manufacturing a finding to fill the section.

**4. Are Related-Terms links reciprocal, verified by parsing rather than by trusting the index's claim?** **Yes, fully — 110 directed edges, 55 reciprocal pairs, zero one-way links**, independently confirmed by parsing all eighteen Related-Terms fields myself and building the edge set from scratch rather than reading §5's prose. This matches the index's own claim exactly. The historical claim that a first pass produced "27 one-way or broken links" that were then fixed is not independently checkable (no artifact preserves the pre-fix chunk state), so it is reported as unverified rather than confirmed — but the only thing that matters for a reviewer today, the current reciprocity, is independently true.

**5. Does the Author-Gravity-Risk column match what each chunk's Key Sources section actually says?** **Yes, exactly.** All seven "Yes" cells (the flock, the lapsed, reconciliation/penitential discipline, confessor, grace, plenary Council, compel them to come in) correspond to a chunk that actually carries an "Author Gravity note" naming a single-source or single-voice dominance; all eleven "No" cells correspond to chunks with no such note (including *communion* and *heresy*, which instead carry a *Confidence* note about their own synthesis-versus-fact distinction — correctly not conflated with Author Gravity). This is not asserted by default anywhere; it is derived, and it derives correctly.

---

## HIGH

### H1 — The index's own Source Registry Cross-Reference for term 01 ("the flock") omits three of the five rows its own Key Sources section cites

**Site:** `Lexicon_Deployment_Index.md` §1, row 01, "Source Registry Cross-Reference" cell: `Rows 1, 19`. Compare `Lexicon-Chunks/lpclex001_the-flock.md`, Key Sources: *"Cyprian's own words carry the image throughout: De Lapsis 4 (…); the watch-keeping passage (…); and the relief provision for '…' Registry rows 1, 2, 3, 5. Augustine's Sermons carry the cognate fold image (row 19)."*

**What I found.** The chunk itself explicitly cites Registry rows **1, 2, 3, 5, and 19** — the phrase "Registry rows 1, 2, 3, 5" appears verbatim in the chunk's own Key Sources paragraph. The index's cross-reference cell for this same term lists only **1, 19**, silently dropping rows 2, 3, and 5. Every other one of the eighteen rows' cross-reference cells I independently re-derived (all eighteen were checked, not just this one) matches its chunk exactly — this is the sole mismatch found in the entire table, which is exactly the shape of defect the assignment asked this review to hunt for: a single mismatched cell in an index that claims perfect derivation.

**Why this matters.** The index's own header states, as its central claim to trust: *"Every row below is parsed directly out of Lexicon-Chunks/lpclex*.md by script… this index cannot silently drift from the chunks it indexes. Re-deriving it is the check: regenerate and diff, and any difference is a real divergence rather than a stale copy."* That claim is falsified for this one row. A reviewer or a builder consulting the index alone to check provenance for "the flock" would believe its evidentiary base is two Registry rows when it is actually five, missing three-fifths of the citation.

**Fix.** Correct the cell to `Rows 1, 2, 3, 5, 19`. Given that the header's whole justification for the index is script generation, the more important fix is finding and correcting whatever caused the extraction script to under-parse this one Key Sources paragraph (most plausibly: a regex anchored on "Registry row(s)" that stopped at the first sentence-ending clause and missed the trailing "Augustine's Sermons carry… (row 19)" being folded back in without the earlier "rows 1, 2, 3, 5" list), and re-running the full extraction rather than hand-patching the one visible cell.

---

### H2 — "suffrage" carries a [PV] tag that Doc_03 explicitly says should not apply to it, and that contradicts the index's own Cross-Build Sheet

**Site:** `Lexicon-Chunks/lpclex011_suffrage.md` front-matter, `Tags: AS, PV`; `Lexicon_Deployment_Index.md` §1 row 11 and §3 ("[PV] Plural Voices" list, which includes *"suffrage"*); compare `Lexicon_Deployment_Index.md` §8 Cross-Build Sheet, which lists *"suffrage"* under **"Cross-phase."**

**What I found.** `Doc_03_Lexicon_Candidate_List.md`'s own Notes section states the operating rule for this exact tag as it applies to this exact term, by name: *"[PV] marks a term whose evidence sits within one of this world's own two phases specifically, not across the whole reconstructed ecology — Part II's own definition, applied below to every single-phase term; **it does not sit on 'suffrage,' which is a cross-phase pattern rather than a single-phase term.**"* Doc_03's own table entry for "suffrage" carries the single tag `[AS]` — no `[PV]`. Every other cross-phase term in this lexicon (the flock, preaching, catechesis, "the people," communion, heresy, schism — all eight terms the index's own §8 Cross-Build Sheet lists as "Cross-phase") correctly carries no [PV] tag; every single-phase term (the lapsed, reconciliation, confessor, libelli, libellatici/sacrificati, bishop of bishops, the one episcopate on the Cyprian side; grace, plenary Council, compel them to come in on the Augustine side) correctly does. "Suffrage" is the one exception in the entire eighteen-term set, and it is the one term Doc_03 named specifically to warn against.

**Why this matters.** This is not a cosmetic mislabel: [PV] is defined by LDF Part II as a tag that *"should trigger explicit attention during Internal Plurality review… rather than silent flattening into one position,"* and this skill's own design brief exists specifically so a builder can filter "show me every PV term" and trust the list. A reviewer or Representative-training pass filtering the By-Tag sheet for single-phase-only vocabulary would incorrectly pull "suffrage" into that set, and the deliverable's own §8 Cross-Build Sheet — which correctly classifies suffrage as cross-phase — sits three sections away from a tag that says the opposite, inside the same file, with nothing in Doc_06 acknowledging or arguing for the departure from Doc_03's explicit instruction.

**Fix.** Remove [PV] from `lpclex011_suffrage.md`'s Tags field and from the two index tag lists (§1 row 11, §3), unless a builder can articulate why LDF Part II's broader "not universally representative" language (rather than Doc_03's own narrower phase-based operationalization of it) justifies keeping it — in which case that reasoning belongs in Doc_06 §2 or §3 as a stated departure from Doc_03, not silently carried through the chunk build.

---

### H3 — "the lapsed" absorbs the *libellatici*/*sacrificati* editorial classification into its own World Meaning without disclosure — a sixth editorial-apparatus instance the register missed

**Site:** `Lexicon-Chunks/lpclex002_the-lapsed.md`, World Meaning: *"Some of them went up and burned the incense; some never went near the altar but bought a paper saying they had, and thought the difference would hold."* Compare `Lexicon_Deployment_Index.md` §7, Editorial-Apparatus Register (five entries, none naming "the lapsed"), and `Lexicon-Chunks/lpclex018_libellatici-sacrificati.md`, Key Sources: *"This classification reaches this record as the vendored English edition's own 19th-century editorial endnote, attached to the anonymous treatise against Novatian (Registry row 8, Native, Confidence C) — not to an independently re-verified passage of De Lapsis."*

**What I found.** The distinction narrated in `lpclex002`'s World Meaning — some lapsed by actually sacrificing, others by obtaining a certificate without sacrificing — is precisely the *libellatici*/*sacrificati* two-way classification. `lpclex018` and `Doc_03` both disclose, correctly, that this classification is not Cyprian's own words: it is the vendored volume's own 19th-century American editorial endnote, attached to a different, Confidence-C text (the Anonymous Treatise Against the Heretic Novatian, Registry row 8), not to *De Lapsis*. `Doc_05_Ecological_Reconstruction.md` §1.1 uses the same content in an inhabited passage and **discloses it in the very next line**: *"The libellatici/sacrificati distinction rendered here as 'some went up… some never went up but paid' is the vendored edition's own 19th-century editorial note… and marked here as editorial, not as Cyprian's own two-way classification."* `lpclex002`'s own Key Sources and Author Gravity note say nothing of this — the chunk simply states the distinction as fact, with no caveat, no cross-reference to `lpclex018`'s disclosure, and no entry in the Editorial-Apparatus Register at `Lexicon_Deployment_Index.md` §7.

**Why this matters.** This is exactly the failure mode Doc_06 §5 item 6 names as the reason the register exists: material that *"could reach a participant as this world's own voice if a later pass were less careful."* It happened here, inside a Tier 1 entry, one document after the same content was correctly caught and disclosed in Doc_05. A Representative drawing on `lpclex002` alone (the intended runtime unit — chunks are meant to be self-contained per LDF Part VI) would present the editor's classification as Cyprian's own without ever surfacing the caveat that lives only in a different, Tier 3 chunk a participant is unlikely to have triggered.

**Fix.** Add the same disclosure Doc_05 §1.1 and `lpclex018` already carry — one sentence in `lpclex002`'s Key Sources or Author Gravity note, naming the *libellatici*/*sacrificati* framing as editorial rather than Cyprian's own — and add `lpclex002` as a sixth row to `Lexicon_Deployment_Index.md` §7's Editorial-Apparatus Register.

---

## MEDIUM

### M1 — Both Tier 3 entries carry a Key Sources section, which the L4 template and LDF Part III both explicitly exclude from Tier 3 — and the excluded content is exactly what justifies their tier

**Site:** `Lexicon-Chunks/lpclex017_libelli.md` and `lpclex018_libellatici-sacrificati.md`, both carrying a `## Key Sources` section.

**What I found.** `L4-Templates/Deployment_Lexicon_Chunk_Template.md` states, for Key Sources: *"{Include for Tier 1 and Tier 2. Omit for Tier 3.}"* `Interpretive Lexicon Development Framework V2.1` Part III is more specific still: *"A Tier 3 entry should contain only: Quick Meaning, and, where applicable, a single-line Distortion Risk note. Full World Meaning, Ecological Function, and source citation are not required at this tier. A Tier 3 entry that begins to require these should be reclassified to Tier 2 rather than expanded in place."* Both governing texts agree, in near-identical language, that a Tier 3 chunk should not carry Key Sources. Both `lpclex017` and `lpclex018` do — and the content inside those sections is not incidental: it is the evidentiary disclosure (the Latin headword's total absence from the corpus; the classification's editorial, not-Cyprian's-own provenance) that is the *entire stated reason* these two entries sit at Tier 3 rather than Tier 1 or 2. Nothing in Doc_06 acknowledges this as a template departure.

**Why this matters.** LDF Part III's own instruction for exactly this situation — a term whose Tier 3 status depends on content that Tier 3 structure does not carry — is not "keep the section anyway": it is *"should be reclassified to Tier 2 rather than expanded in place."* The two entries currently do the opposite: they keep Tier 3 status and expand the structure to carry the disclosure that earns it, which is the one combination the Framework names as wrong. This is a genuine, if narrow, structural non-compliance — not a factual error, and not one that misleads a reader (the disclosure is honest and necessary), but an unacknowledged departure from an explicit rule in both governing documents.

**Fix.** Either (a) reclassify `lpclex017` and `lpclex018` to Tier 2, which the Framework's own escape hatch invites and which would let them retain Key Sources legitimately (their Distortion Risk and Ecological Function sections would then need the standard Tier 2 treatment too), or (b) keep Tier 3 and move the evidentiary disclosure into the Distortion Risk section's World Hearing line or a short unlabeled provenance sentence rather than a formally named Key Sources heading, and state the departure explicitly in Doc_06 §2.3 rather than leaving it silent.

---

### M2 — The confessors' own attested "certificate" (*libellus pacis*) practice, directly on-topic for the G8 confessor-authority tension, was never tested as lexicon vocabulary

**Site:** `Doc_03_Lexicon_Candidate_List.md`, Notes on scope and process (the "*libelli*" and "confessor" entries); `Lexicon-Chunks/lpclex004_confessor.md` and `lpclex017_libelli.md`.

**What I found.** Doc_03's own Notes acknowledge, by name, that *"a scholarly name for the confessors' own written instrument, libellus pacis, is well attested in modern Cyprian scholarship; it is not proposed as a candidate headword here, since the headword itself — libellus/libelli — does not occur anywhere in Cyprian's own vendored English corpus."* That specific claim — about the **Latin** headword — is independently verified true (the sole `libell-` occurrence in the whole volume sits in a different text's editorial endnote, not in Cyprian's own words; confirmed by direct search above). But a full-text search of Cyprian's own `div1` section for the **English** word actually used by this translation for exactly this practice — "certificate" — returns **38 occurrences**, concentrated in Epistles discussing confessors and martyrs issuing "certificates" of reconciliation to the lapsed on their own authority without episcopal control (e.g., *"thousands of certificates were given, against the Gospel law"*; *"I beg you that you will designate by name in the certificate those whom you yourselves see, whom you have known, whose penitence you see to be very near to full satisfaction"*). This is the informal confessor-issued peace-certificate practice that is the direct textual engine of G8 (the confessor-authority Tensional gravity) and of the reconciliation/penitential-discipline gravity — not the Decian sacrifice-certificate the *libelli* entry is actually about, but a closely related, separately well-attested practice using the corpus's own English word for it. No chunk names it; no Doc_03 row proposes it; Doc_06 §5's list of carried-forward gaps does not mention it.

**Why this matters.** This is a genuine Three Sources Principle candidate (a Representative discussing how confessors granted peace informally would very plausibly need this vocabulary) that fell through a gap in Doc_03's own dismissal reasoning: checking only whether the Latin headword occurs, not whether the corpus's own English translation term for a closely adjacent practice does. It is not an invented claim and nothing currently in the lexicon is wrong because of it — it is a completeness gap of the kind LDF Part I's "diminishing returns" test exists to catch, and this pass has not reached it.

**Fix.** Not a defect requiring rework of what exists; flag as a candidate-discovery gap for a future Doc_03/Doc_06 pass, alongside the already-disclosed rite-of-reconciliation gap at Doc_06 §5 item 3, rather than silently absorbing it into the existing confessor/reconciliation entries without a headword.

---

### M3 — LDF Part III names "Key Texts" as a required Tier 1 section distinct from "Key Sources," but the L4 template and every chunk have no such section

**Site:** `Interpretive Lexicon Development Framework V2.1` Part III, Tier 1 requirements list (*"Key Texts — primary textual evidence, where applicable / Key Sources — primary historical voices or texts substantively informing this entry's reconstruction"*), versus `L4-Templates/Deployment_Lexicon_Chunk_Template.md` and all eighteen chunks, which carry only "Key Sources."

**What I found.** LDF Part III lists Key Texts and Key Sources as two separate, named Tier 1 sections. The L4 template itself — the document every chunk cites as its own completion standard — has no "Key Texts" heading at all, and neither does any of the eighteen chunks. This is not a defect in Doc_06's own work: every chunk faithfully follows the template it is governed by, and the template is what actually ships. But it means LDF Part III's own text and its own downstream template disagree about what a Tier 1 entry requires, and nothing in this build's construction record (Doc_06, the index, or the Decision Log) names the discrepancy.

**Why this matters.** This is the same species of defect as the already-logged *Boundary Structures* / *Boundary Ecology* inconsistency Doc_05 §11 item 15 found between the Forces Framework and the Construction Framework — a governing-document internal mismatch that will keep silently under- or over-specifying every future world's lexicon build until it is reconciled at the L3B level, not something a single world's build thread can fix from inside.

**Fix.** Route to the project lead alongside the already-open Boundary Structures/Ecology item, as a second instance of the same category of governing-document drift; no action required inside this world's build.

---

## LOW

### L1 — Doc_06 §2.3 characterizes *libelli*/*libellatici* as "already Tier 2 candidates in Doc_03," which overstates what Doc_03 actually assigned

**Site:** `Doc_06_Full_Lexicon_Development.md` §2.3: *"libelli and libellatici/sacrificati were already Tier 2 candidates in Doc_03 and are Tier 3 here."*

**What I found.** Doc_03's own Disposition states plainly: *"this document assigns no final tier classification of its own, since tiering depends on Doc_04's gravity findings and Doc_05's ecological reconstruction."* Doc_03's table carries only a binary "Tier 1 Flag: Yes/No" column; a "No" (which both *libelli* and *libellatici*/*sacrificati* received, alongside "the people," "suffrage," "the one episcopate," and "schism") is not itself an assignment to Tier 2. Doc_06's phrasing retrospectively upgrades a "not flagged Tier 1" into "a Tier 2 candidate," which is a looser characterization of Doc_03's own explicit self-description than the rest of Doc_06's otherwise careful sourcing discipline uses elsewhere.

**Why this matters.** Not substantively misleading — the four other "No"-flagged terms did land at Tier 2 here, and only these two moved further to Tier 3 — but it is an imprecise gloss on a document (Doc_03) that took unusual care to state exactly what it was and was not deciding.

**Fix.** Rephrase to something like "were not flagged for Tier 1 consideration in Doc_03 (the same status four other terms that remain at Tier 2 here received) and are Tier 3 here."

### L2 — Doc_06 §1's "one disclosed exception" framing is confusing: no term was actually added

**Site:** `Doc_06_Full_Lexicon_Development.md` §1: *"It does not add terms Doc_03 did not surface — with one disclosed exception at §5 item 3, which is flagged rather than added."*

**What I found.** §5 item 3 is a **gap flagged and explicitly not filled** ("Adding a term on that expectation would be invention; naming the gap is not"). Calling this an "exception" to the no-new-terms rule, only to immediately clarify that nothing was in fact added, states the sentence backwards from how it reads on first pass.

**Fix.** Reword to something like: "It does not add terms Doc_03 did not surface, and names one place where a future reading may surface one, at §5 item 3, without adding it here."

---

## Article 19 / invention check

Every quoted primary-source passage across all eighteen chunks that I traced to source (a substantial majority, spot-checked across all seven Tier 1 entries and four of nine Tier 2 entries, targeting the highest-stakes and CT-tagged terms specifically) reproduces the vendored text exactly, including the two chunks carrying a live editorial-apparatus warning (`lpclex001`, `lpclex012`), where the precise, unusual bracket placement in the source (an editorial note that opens *unbracketed* and is only partially bracketed) is reproduced correctly rather than smoothed into a conventional bracket. I found no sentence in any chunk asserting a specific historical fact with no traceable source behind it — every substantive claim I checked traces to a Registry row, a Doc_03/Doc_04/Doc_05 finding, or a directly-quoted primary text. The one real gap found (M2, the *libellus pacis*/"certificate" vocabulary) is an omission, not an invention: nothing false is asserted, a genuine candidate was simply never tested. H3 is the one place fabrication-adjacent risk actually materialized — not invented content, but uncaptioned editorial content presented as the world's own voice, which is the specific harm the project's editorial-apparatus discipline exists to prevent.

---

## Is the deliverable adequate to proceed to Doc_07?

**Yes, after one narrow fix pass — not as drafted.** The three HIGH findings are each small, mechanical, and independently verifiable as fixed once corrected: one index cell, one erroneous tag on one chunk, one missing disclosure sentence plus one register row. None of them touch the gravity spine, the tier classifications as a whole, the CT tagging, or the quote fidelity, all of which independently verify as sound. Doc_06 §6's specific handoff to Doc_07 — that the affective lens draw on *confessor*, *the lapsed*, and *reconciliation*, and the conceptual lens treat *communion*/*heresy* as this world's organizing pairing — rests on Tier 1 entries that are, on this review's own checking, accurately sourced and well-argued; that handoff does not need to wait on H1–H3's fixes to be sound advice for Doc_07, since none of the three HIGH findings falls inside those specific entries' World Meaning or Ecological Function content (H3 touches `the lapsed`'s World Meaning specifically, so that one entry's fix should land before Doc_07 draws on it for the affective lens). The departure from the build cycle recorded in Doc_06's own Disposition (drafted on both Doc_04 and Doc_05 while both remain undisposed, on the project lead's direct instruction) is recorded plainly, names the two specific open items it depends on being small and non-load-bearing, and I found nothing in this lexicon's own content that actually depends on anything currently in dispute at Doc_04 or Doc_05 — that self-assessment holds up.

---

## Escalation assessment (CO-022)

**1. Representative identity, title, or voice — does not apply.** Confirmed independently: nothing in Doc_06, the chunks, or the index makes or implies an identity, title, or voice decision for this world's Representative. §6's handoff to Doc_07 names lenses and entries, not a Representative decision.

**2. Portfolio-level or cross-world — two items, both correctly inherited and neither decided here, plus one this review adds.** Doc_06 §5 item 6 (the corpus-wide editorial-apparatus question, routed by Doc_05 §11 item 11) and the Disposition's citation of the *Boundary Structures*/*Boundary Ecology* inconsistency (Doc_05 §11 item 15) are both correctly carried as open rather than resolved here — verified against Doc_05's own escalation record. **This review adds a third, of the same kind**: M3 above, the LDF Part III / L4 template "Key Texts" vs. "Key Sources" mismatch, which is a governing-document-level inconsistency in the same family as the Boundary Structures item and should reach the project lead alongside it rather than be treated as specific to this world.

**3. Governance or methodology — open, unchanged.** Doc_04's three-item governance/methodology escalation remains open (confirmed against Doc_04's own Disposition) and Doc_06 correctly adds none of its own to that category. H1–H3 and M1–M2 above are ordinary, correctable review findings specific to this world's own build, not governance-or-methodology-category items.

**4. Unresolved tensions — one open, correctly carried.** The evidentiary question at Doc_04 §7 Open Item 6 (the 411 *Gesta*, unread, no owner, no acceptance criterion) is the one item Doc_06 names, and this review confirms nothing in the lexicon's own content relies on it. No further unresolved tension found: every finding in this review has a clear, narrow fix rather than being a standoff between two positions that cannot be settled from inside the lexicon.

---

*End of Round 1 review. Simulated review — informational only, not an Article 31 substitute.*
