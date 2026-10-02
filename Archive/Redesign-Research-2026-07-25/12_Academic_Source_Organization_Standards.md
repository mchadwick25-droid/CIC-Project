# Academic Source-Organization Standards: What Research Libraries, Digital-Humanities Projects, and Historical Method Actually Require — Measured Against CiC's Source Registry

Every standard, element list, and criterion below was read on 2026-07-25/26 from the published standard, guidelines page, or journal of record. Where I could only reach a secondary summary rather than the primary document, the finding carries a **Medium** or **Low** confidence rating and says so. Four items I could not verify at all are listed at the end under "Do not cite" so nobody quotes them later on my authority.

CiC's apparatus was read first, in full: `L3B-World-Build-Methodology\Source_Registry_Template.md` (the governing 10-field entry schema), the Doc_02 findings in `04_BuildProcess_Methodology_Mapping.md`, and 5 real populated rows from `cic-poc\backend\transcripts\d1ec86a7-dcf4-4c06-869a-f6fba1ba12cb.json`. Verdicts below are against that actual apparatus.

---

## Summary — the five findings that matter

**1. CiC's biggest real gap is an attribution-status field, and it is a patristics-specific gap that will be the first thing a patristics reviewer looks for.** The *Clavis Patrum Graecorum* — the reference apparatus of the field — assigns every work a number and lists all of an author's works "whether genuine or not," marking doubtful attributions explicitly as **dubia** (uncertain authorship) or **spuria** (false attribution). CiC's registry has no field for this. It handled the problem correctly in prose once already (row 33's note that the Ephrem/bnat-qyama-choir claim "rests on later hagiographic attribution (Jacob of Serugh, sixth-century *Vita Ephraemi*), not Ephrem's own contemporary self-testimony") but there is no column that makes the judgment queryable or forces the question on the next source. For any world touching the *Apophthegmata Patrum* or Ephraem Graecus, this is live risk. **Confidence: Medium** (Brepols/CCC pages, not the printed Clavis).

**2. CiC's single `Source` free-text field collapses a distinction that two independent standards families exist specifically to enforce.** Registry row 10 reads: "Aphrahat, *Demonstrations* 1–23. Ed. Jean Parisot, *Patrologia Syriaca* I/1-2 (1894, 1907). Trans. Adam Lehto, Gorgias Press, 2010 (complete); also Valavanolickal, Gorgias, 2005." That is one work, one critical edition, and two English translations in a single string — with no field saying which was actually read for the material licensed from it. IFLA LRM's Work→Expression→Manifestation→Item model and the Canonical Text Services URN scheme both exist to hold exactly this apart: `urn:cts:greekLit:tlg0012.tlg001:1.1` identifies the notional work, `urn:cts:greekLit:tlg0012.tlg001.perseus-grc1:1.1` identifies the specific edition. Chicago 18th ed. (14.142–14.152) makes it a citation-completeness requirement: bibliography entries for classical texts must include "the full details of the modern edition used, including the name of the editor and/or translator." **Confidence: High** for the CTS example and Chicago rule, Medium for LRM details.

**3. CiC's Missing Voices / Affirmative Duty requirement exceeds what the field's own dominant content standard requires, and CiC is currently underclaiming it.** The A4BLiP *Anti-Racist Description Resources* team states plainly that "professional standards such as Describing Archives: A Content Standard (DACS) are largely silent on how racial bias appears in finding aids, and this silence and the apparent neutrality it creates can hide racial biases." The archival-silences literature that makes CiC's requirement legible to scholars is real and citable (Carter, *Archivaria* 61 [2006]: 215–233). Constitution Article 20's affirmative duty to name whose voice is absent is a codified obligation that DACS does not impose. It should be led with in any reviewer-facing document, not hedged. **Confidence: High** for the A4BLiP characterization of DACS, Medium for the Carter pagination (search result, not the article itself).

**4. CiC's A–E "Citation Reliability" grade is doing three jobs at once, and the field's own most famous letter-grade apparatus has a documented failure mode CiC has no defense against.** The UBS Greek New Testament committee's A/B/C/D letters are the direct academic precedent for a letter-graded source apparatus, and they drifted badly: UBS3 carried 126 A-ratings and 144 D-ratings; UBS4 carried 514 A-ratings and 9 D-ratings, across editions of the same apparatus. CiC's A–E tiers as written mix pointer-specificity ("Specific work/locus named") with verification recency ("Verified this session") and say nothing about how much weight a source can bear for the claim it is licensed for. TEI's certainty module solves precisely this by requiring a `@locus` attribute that "indicates more exactly the aspect concerning which certainty is being expressed," separate from `@degree`. **Confidence: High** for TEI (read the module), Medium for the UBS counts.

**5. The cheapest available legitimacy win is a one-page conformance statement, and it answers a review criterion by name.** The IDE's *Criteria for Reviewing Scholarly Digital Editions* v1.1 — the 39-criterion catalogue used by RIDE, the review journal of record for digital editions — asks under 3.7 Data modelling: "Does the SDE follow common standards (e.g. TEI guidelines)? **If not, is the deviation from existing standards sufficiently justified?**" CiC follows no external standard and has published no justification for deviating. A short document mapping registry fields to DACS/ISAD(G)/TEI/Dublin Core and stating where CiC differs on purpose converts a silent liability into a visible methodological choice. **Confidence: High** (read the criteria page).

---

## 1. How research libraries and archives catalog primary sources

### 1a. DACS — the American content standard, and its required minimum

[DACS Chapter 1](https://saa-ts-dacs.github.io/dacs/06_part_I/02_chapter_01.html) defines 25 elements and stratifies them into Single-Level Required / Optimum / Added Value and the three Multilevel equivalents. The **Single-Level Required** set, verbatim:

Reference Code (2.1) · Name and Location of Repository (2.2) · Title (2.3) · Date (2.4) · Extent (2.5) · Name of Creator(s) (2.6) (if known) · Scope and Content (3.1) · Conditions Governing Access (4.1) · **Languages and Scripts of the Material (4.5)** · **Rights Statements for Archival Description (8.2)**

Mapping against CiC's ten registry fields: `#` covers Reference Code. Title, creator, and date are all present but bundled inside the `Source` string. `Licensed For` is adjacent to Scope and Content without being it (it records permitted downstream use rather than what the source contains). **Languages and Scripts has no CiC counterpart. Rights has no CiC counterpart.** Two of the ten elements a content standard treats as the floor for a *single* description are entirely absent.

**Verdict: NEEDS ADAPTATION on the bundling, REAL GAP on language/script and rights.** The language gap is not cosmetic for CiC — a registry that includes both `Patrologia Syriaca` (Syriac with facing Latin) and two English translations, and whose worlds span Syriac, Greek, and Latin, cannot currently answer "which of our sources did we read in the original language" from structured data. Rights becomes blocking rather than cosmetic the moment a browsable public repository ships. **Confidence: High.**

### 1b. ISAD(G) — the international standard, and the element CiC most needs

ISAD(G) 2nd ed. (2000) defines 26 elements in seven areas; six are essential for international exchange, and one of the six is **3.1.4 Level of description**. The full first-edition element list I read directly runs Reference code / Title / Dates / **Level of description** / Extent (3.1); Name of creator / Administrative-Biographical history / Dates of accumulation / **Custodial history** / Immediate source of acquisition (3.2); Scope and content / Appraisal / Accruals / System of arrangement (3.3); Legal status / Access conditions / Copyright / Language of material / Physical characteristics / Finding aids (3.4); Location of originals / Existence of copies / **Related units of description** / Associated material / Publication note (3.5); Note (3.6).

Level of description is the sharpest finding in this section, because CiC's registry violates it visibly in production data. Row 10 is an item-level description of a specific work in a specific edition. Row 13 is something categorically different: "Bnay qyama / bnat qyama institutional attestation within this world's own window: Aphrahat, Demonstration 6 (337 CE, earliest named source) and Ephrem's hymn corpus." That is an **aggregate attestation claim** assembled from two sources, one of which (row 10) already has its own row. Both sit in the same table at the same apparent level, with sequential IDs implying peer status. A reviewer trained on multilevel description will read that as an unmarked level confusion, and ISAD(G) makes marking it mandatory.

**Verdict: REAL GAP.** A single controlled field fixes it. **Confidence: High** for the element list and its mandatory status; the 3.7 Description Control area numbering I could not confirm to the sub-element (see Do-not-cite).

### 1c. Provenance and custodial history as separate, first-class information

Three converging sources:

[DCRMR](https://bsc.rbms.info/DCRMR/introduction/), the RDA-edition rare-materials standard, expanded copy-specific notes beyond DCRM(B)'s general/provenance/binding set to include **[9.42 Custodial history of item](https://bsc.rbms.info/DCRMR/additional-notes/Custodial-history-of-item/)** and immediate source of acquisition, on the principle that rare-materials cataloging "puts greater emphasis on materials as artifacts than is usual in general cataloging."

[DCMI Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) defines `provenance` verbatim as "A statement of any changes in ownership and custody of the resource since its creation that are significant for its **authenticity, integrity, and interpretation**."

[TEI's manuscript-description module](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html) gives `<history>` its own top-level slot inside `<msDesc>`, covering origin, provenance, and acquisition as structured children.

CiC has the underlying judgment — transmission history was added as a fifth Author Gravity dimension in Doc_02 "v1.6," and the Boundary Check section explicitly says the Forces Framework's transmission-history mandate "is asking the same provenance question this Boundary Check answers." The gap is location: the assessment lives in Doc_02's narrative and in per-author judgment, not as a field on the source row. A browsable repository cannot surface what is only in prose.

**Verdict: ALREADY DOES THIS as analysis, REAL GAP as structured data.** **Confidence: High** for DCMI (read the terms page) and TEI structure; Medium for DCRMR specifics.

### 1d. Description control — CiC is ahead here

ISAD(G)'s Description Control Area exists to convey "information ... about how, when and by whom the archival description was prepared." CiC's `Added` field (date plus who/what) and `Verification Note` (what was checked, when, against what) already carry this, and the real populated rows carry it at a level of specificity most finding aids do not reach. Row 33's note: "Verified this session: author, exact title, journal, year, volume, and article number all confirmed directly against publisher page. Author also holds Syriac Orthodox ecclesiastical office (Archbishop/Patriarchal Vicar, Australia/NZ) alongside academic affiliation (Australian Catholic University) — noted, not disqualifying."

That single note does description control, author-authority assessment, and disclosed-perspective work in three clauses, and the "noted, not disqualifying" formulation is exactly the disciplined move a historiography seminar teaches.

The append-only protocol — never renumber, never delete, a discredited source moves to Confidence E and disposition removed-from-use but stays as a record of what was tried — is the same principle PREMIS encodes for digital objects, where "documentation of actions that modify a digital object is critical to maintaining digital provenance, a key element of authenticity," and where even actions that alter nothing get logged as events.

**Verdict: ALREADY DOES THIS at CiC-comparable-or-better rigor.** The only recommendation is nominal: call the block "Description Control" and cite ISAD(G) 3.7. Free recognition for a rename. **Confidence: High** for the area's purpose; Medium for PREMIS specifics.

### 1e. Where CiC is *not* behind, and shouldn't be told it is

The Library of Congress was still circulating a discussion paper in 2022 on **defining** a standardized provenance field for MARC 21 bibliographic, holdings, and authority formats. Free-text provenance notes remain normal practice at the largest research library in the world. CiC's free-text `Verification Note` is not a deviation from professional practice; it is professional practice. Do not let a reviewer-anxiety pass convert this into a defect.

**Verdict: ALREADY DOES THIS.** **Confidence: Low on the paper's contents** — I could not fetch it (403). Cite it only as "a 2022 MARC Advisory Committee discussion paper on standardizing provenance," which the search result title supports, and nothing more.

---

## 2. Digital-humanities encoding and organization standards

### 2a. TEI — the mandatory `sourceDesc`, and why it corroborates CiC's strongest existing rule

[TEI P5's header chapter](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html) requires exactly one element in every TEI document, `fileDesc`, and within it exactly three: `titleStmt`, `publicationStmt`, and **`sourceDesc`** — "Of these elements, only the titleStmt, publicationStmt, and sourceDesc are required." `sourceDesc` "describes the source(s) from which an electronic text was derived or generated ... or a phrase such as 'born digital' for a text which has no previous existence."

The largest text-encoding standard in the humanities makes it structurally impossible to publish a document without stating where its text came from — including a required affirmative statement when the answer is "nowhere."

CiC's Checkpoint rule is the same instinct applied at finer grain: "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row. If a claim in Doc_02 cannot be traced to a Registry entry, this section is not finished, regardless of how complete the narrative reads." TEI requires source declaration per *document*. CiC requires it per *claim*.

**Verdict: ALREADY DOES THIS, at finer grain than TEI requires.** This is a bankable confidence statement, and it is the kind of thing to say early in any reviewer-facing document because it is checkable. **Confidence: High.**

### 2b. TEI's certainty module — the standard that diagnoses CiC's confidence grade

[TEI chapter 21/22](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html) provides `<certainty>`, `<precision>`, and `<respons>`, all members of the `att.scoping` class so a statement of confidence can attach to a whole document or any identifiable part. The load-bearing attributes:

- `@locus` — "indicates more exactly the aspect concerning which certainty is being expressed"
- `@degree` — numeric 0 to 1. The Guidelines' own example: `<certainty target="#CE-pl1" locus="name" degree="0.6"><desc>probably a placename, but possibly not</desc></certainty>`, which "expresses the point of view that there is a 60 percent chance of 'Essex' being a place name."
- `@assertedValue` — the alternative reading if the encoded one is wrong
- `<respons>` with its own `@locus` — who is responsible for *which aspect* of the markup

The diagnostic point is `@locus`. TEI's designers concluded that a confidence value is meaningless without saying what it is confidence *about*. CiC's A–E scale, read against its own definitions, is confident about at least three different things simultaneously:

| CiC tier as written | What it actually asserts |
|---|---|
| A — "Verified this session against an accessible primary source, translation, or authoritative reference" | verification recency + verification directness |
| B — "Specific work/locus named, not independently re-checked this session" | pointer specificity, verification absent |
| C — "Tied to a real author/work, no specific locus pinpointed" | pointer specificity |
| D — "Tradition/genre-level attribution, no specific text/author named" | pointer specificity |
| E — "No traceable source" | traceability |

Nothing on the scale says how much weight the source can carry for the claim it is licensed for. A source can be Confidence A (checked this session, edition confirmed) and still be a thin basis for a vivid claim — which CiC knows, because its own builder process step 4 says to "flag anything at Confidence C or below supporting a vivid, specific claim for independent second-opinion review." That rule is reaching for an evidentiary-weight axis the schema does not have, and so it can only proxy it through the specificity axis.

**Verdict: REAL GAP, and the highest-value structural fix in this document.** **Confidence: High** (read the module and its examples).

### 2c. The critical-apparatus tradition, and something CiC already has

The apparatus criticus condenses the evidentiary discussion into sigla and lemma-keyed variant lists so a reader "can see not only the text itself but also the sources, decisions, and debates on which that text is based." The positive/negative apparatus distinction matters: a **positive apparatus** lists every witness's reading; a **negative apparatus** records only divergences from the printed text, and is, in the standard criticism, "less usable than knowing what every manuscript said."

The [LDLT Guidelines](https://digitallatin.github.io/guidelines/LDLT-Guidelines.html) state the requirement flatly: "every witness or source in an LDLT edition must have both a machine-readable ID (using `xml:id`) and a human-readable siglum or abbreviation (using `<abbr>` with `type="siglum"`)." Witnesses are declared in `<listWit>` in the front matter; apparatus entries reference them via `@wit`.

Two things follow.

First, **CiC already has the sigla apparatus.** Registry IDs are machine-readable and never reused; the inline convention "(Source Registry #26, cross-checked)" is functionally a siglum resolved at runtime by `rag/source_registry.py`'s `resolve_references`. The declaration-plus-reference architecture LDLT mandates is already what CiC does.

Second, **CiC's retrieval audit is a positive apparatus and should be described that way.** `GET /api/session/{id}/audit` preserves every candidate the retriever considered, retrieved or skipped, and why. A scholar reading "we log what we didn't use, and why, not only what we used" recognizes that immediately as the positive-apparatus choice, and it is the more expensive and more trusted of the two options. Nothing needs building; the framing needs writing down.

**Verdict: ALREADY DOES THIS on both counts.** **Confidence: High** for LDLT (fetched); Medium for the general apparatus conventions.

### 2d. Persistent identifiers, and the one external hook CiC should grab

[CTS URNs](https://sites.tufts.edu/perseusupdates/2021/01/05/what-is-a-cts-urn/) in the CITE architecture produce "a semantically meaningful identifier which represents the position of a text in the hierarchy in which it is traditionally cited," resolvable at the passage level within a *specific version* or within the *notional work*. FAIR's first principle (Wilkinson et al., *Scientific Data*, 2016) is globally unique and persistent identifiers plus rich machine-actionable metadata.

For CiC's Syriac world specifically, the infrastructure already exists and is free:

- [Syriaca.org](https://syriaca.org/documentation/uris.html) mints stable URIs of the form `http://syriaca.org/person/\d+` for persons relevant to Syriac studies, with a TEI-XML record at the URI plus `/tei`, explicitly "for authority control (such as in library catalogues) and as identifiers."
- The [Bibliotheca Hagiographica Syriaca Electronica](https://syriaca.org/bhse), volume 1 of [A New Handbook of Syriac Literature](https://syriaca.org/nhsl), catalogues over 1,800 Syriac stories, hymns, and homilies on saints, organized by work, with hagiographers' names, incipit and desinit, bibliographic information, and the manuscripts containing them — downloadable in full as TEI XML, with permanent links and a channel for submitting editorial revisions.

CiC's Syriac registry names Aphrahat, Ephrem, Griffith, Brock, Harvey, and Malki. Every one of those has or could have a Syriaca.org URI. Adding an `external_ids` array costs a lookup pass and converts CiC's registry from a private list into a resource that participates in the same identifier graph as the field's own reference works.

**Verdict: REAL GAP, and the best effort-to-legitimacy ratio in this document.** **Confidence: High** for the CTS URN example and FAIR; Medium-High for Syriaca/BHSE (project documentation pages, not the TEI corpus itself).

### 2e. Relations between records

ISAD(G) 3.5.3 Related units of description; DCMI's relation vocabulary (`source`, `isVersionOf`, `hasVersion`, `references`, `isReferencedBy`, `conformsTo`); and RiC-CM 1.0 (ICA/EGAD, November 2023), which "reconciles, integrates, builds on, and replaces" ISAD(G), ISAAR(CPF), ISDF, and ISDIAH by rebuilding archival description as an entity-and-relation model rather than a flat multilevel record.

CiC's registry rows are flat and unlinked, and the cost shows in production data. Row 33 (Malki 2024) carries the warning "USE CAUTIOUSLY, does not stratify pre-/post-410 evidence." Rows 13 and 32 are the entries that *do* stratify it. The relationship among the three exists only as prose inside one row's free text, so it cannot be traversed, displayed in a browsable view, or checked for completeness.

**Verdict: REAL GAP.** **Confidence: High** for ISAD(G) and DCMI; Medium for RiC-CM.

### 2f. Attribution status — the patristics gap

The [*Clavis Patrum Graecorum*](https://www.corpuschristianorum.org/cpg) "aims to inform the user on the whole range of Greek patristic texts, their editions, **and their authenticity**. For each author it lists all their works, **whether genuine or not**, extant or not, and each work is assigned a number." Doubtful attributions are marked with **dubia** (uncertain authenticity) or **spuria** (spurious/false attribution); the CPG number is the standard scholarly reference. [*Clavis Patrum Latinorum*](https://www.corpuschristianorum.org/cpl) does the same for Latin.

CiC's registry has `Type` (P/S/M/L), which answers *what kind of source*, and `Boundary Status`, which answers *does it belong to this world*. Neither answers *is the named author actually the author*. These are independent axes: a text can be Primary, Native, and pseudonymous all at once — which is precisely the *Apophthegmata Patrum* situation, and precisely the Ephraem Graecus situation.

CiC's own data proves it needs the field. Row 33's registry note and the lexicon key-sources note both correctly identify that the Ephrem/bnat-qyama-choir linkage "rests on later hagiographic attribution (Jacob of Serugh, sixth-century *Vita Ephraemi*), not Ephrem's own contemporary self-testimony." That judgment was made, correctly, and then stored in free text where the next builder has to rediscover it by reading.

**Verdict: REAL GAP, and the one most likely to be noticed first by a patristics reader.** **Confidence: Medium** (Brepols and Corpus Christianorum project pages; I did not consult the printed Clavis).

---

## 3. Source criticism as taught and practiced

### 3a. The external/internal division

Howell and Prevenier, *From Reliable Sources: An Introduction to Historical Methods* (Cornell UP) — the standard graduate methods text — organizes source evaluation into external criticism (questions of "where, when, and by whom") and internal criticism (seven criteria, including "the genealogy of the document," meaning the document's own developmental history).

CiC's two axes map onto this cleanly and independently. The Boundary Check is external criticism: "assessed by what the source speaks *for* — its own subject, tradition, or evidentiary target — checked against Doc_01's stated boundary," with the explicit rule that "Boundary Status is never assessed by the date a piece of scholarship happened to be written." Author Gravity Assessment (visibility, representativeness, influence, limitations, transmission history) is internal criticism.

Worth naming: CiC's Boundary Check is the archival principle of *respect des fonds* applied to evidence rather than to physical arrangement — the source is classified by what it belongs to, not by where it was found or when it was made. And the accompanying rule that "Native does not mean exclusive to this world, and it was never supposed to ... Real historical traditions inherit from and cite one another constantly" forecloses the failure mode a reviewer would probe for first, which is manufactured differentiation between worlds. That paragraph is a defense already written.

**Verdict: ALREADY DOES THIS at CiC-comparable rigor.** **Confidence: Medium** for the Howell/Prevenier structure (reviews and summaries, not the book).

### 3b. The five-criterion checklist, and the one criterion CiC lacks

Presnell, *The Information-Literate Historian* (OUP, current ed. 2024) gives the criteria in the form students are actually taught them:

| Presnell criterion | CiC coverage |
|---|---|
| **Author Authority** — "Who created the item? What is his or her affiliation? What is his or her relationship to the information contained in the source?" | Covered, well. Author Gravity's visibility/influence dimensions; and row 33's note on Malki's simultaneous ecclesiastical office and academic affiliation is this criterion executed properly. |
| **Perspective and Bias** — "How do the author's bias and perspective inform the arguments and evidence presented?" | Covered. Author Gravity's limitations dimension is defined as exactly this. |
| **Accuracy and Completeness** — "How does the source compare to other similar sources? **What may have been left out?**" | Covered and exceeded. Source Asymmetry plus Missing Voices / Affirmative Duty go past what Presnell asks. |
| **Footnotes and Documentation** — "Are the author's sources ... clearly identified with complete citations to allow you to find the original source yourself?" | Partial. CiC verifies that *CiC* documented the source. Nothing records whether the *secondary source* documents its own evidence adequately. |
| **Audience and Purpose** — "Who is the intended audience? Why was the item created?" | **Not covered.** No field for genre, occasion, or intended audience. |

Audience-and-purpose is the classic category CiC has no home for, and it does real work in this material. Aphrahat's *Demonstration* 6 is a paraenetic address to a specific ascetic constituency; a conciliar act, a private letter, a polemical treatise, and an apophthegm collection each license different inferences from identical content. CiC's Doc_09 has narrative tiers for hagiographic material, so genre-awareness exists in the pipeline — but it is not on the source row, so the world's Doc_04 gravities and Doc_06 lexicon terms are licensed from sources whose genre the registry never recorded.

**Verdict: REAL GAP on Audience/Purpose (and genre/form). ALREADY DOES THIS on the other four, exceeding on Completeness.** **Confidence: Medium** (library-guide restatements of Presnell, not the book).

### 3c. Silence in the record as a scholarly category

Rodney G. S. Carter, "Of Things Said and Unsaid: Power, Archival Silences, and Power in Silence," *[Archivaria](https://archivaria.ca/index.php/archivaria/article/view/12541)* 61 (2006): 215–233, argues that archival silences are "in part, the manifestation of the actions of the powerful in denying the marginal access to archives," with direct consequences for the ability of marginalized groups "to form social memory and history," and that archivists and researchers can read "against the grain" to highlight silences.

The [A4BLiP *Anti-Racist Description Resources*](https://www2.archivists.org/standards/archives-for-black-lives-in-philadelphia-a4blip-anti-racist-description-resources) (2019, rev. Oct 2020; Antracoli, Berdini, Bolding, Charlton, Ferrara, Johnson, Rawdon) organizes its recommendations into seven categories, including **Transparency** and **Auditing Legacy Description and Reparative Processing**, on the stated premise that DACS is "largely silent on how racial bias appears in finding aids."

CiC's Missing Voices / Affirmative Duty (Constitution Article 20) is a *requirement* to name whose voice is not in the record, and the Syriac data shows it operating: row 32's verification note reads "Direct quotation confirmed: no text composed by a bnat qyama woman survives from this period," and the row's `Licensed For` is "Missing-voices assessment — bnat qyama women, structural clericalism of the source base." A source row whose licensed purpose is to document an absence is a genuinely sophisticated move.

**Verdict: ALREADY DOES THIS, above the standard the field's own dominant content standard sets.** Two honest notes. First, CiC should cite the archival-silences literature when describing this, because the requirement reads as idiosyncratic without it and as disciplinarily grounded with it. Second, A4BLiP's Transparency category includes practices CiC has not adopted — a public statement of who wrote a description and an invitation to submit corrections. Syriaca.org's BHSE has exactly that channel. **Confidence: High** for the A4BLiP structure and its DACS claim; Medium for Carter's pagination.

### 3d. The secondhand-citation rule

Chicago and Turabian discourage citing a source you have not examined; where the original is genuinely unavailable, the citation must disclose it with "quoted in" and list both the original and the consulted work in the bibliography. The principle is that "authors are expected to have examined the works they cite."

CiC's Confidence A ("Verified this session against an accessible primary source, translation, or authoritative reference") and its `Verification Note` between them mostly encode this, and the notes are specific enough to reconstruct what was and wasn't seen directly — row 29's note even distinguishes two located quotations from an "unattributed 'poetic vs. philosophical-categorical' paraphrase" and instructs using the former. That is the Chicago discipline, applied.

**Verdict: ALREADY DOES THIS, informally.** The only improvement is making `consulted_as` a controlled value rather than something a reader infers from prose. **Confidence: Medium.**

---

## 4. Citation conventions and edition status

### 4a. Which edition — the fast tell in patristics

The relevant norm is stated bluntly in the field's own guides: Migne's *Patrologia Graeca* texts "are not critical editions" and the PG "no longer fulfils the requirements of modern scholarship." Corpus Christianorum Series Graeca "replaces Jacques-Paul Migne's Patrologia Graeca and fills gaps ... while redoing deficient editions"; CSEL texts "are edited on the basis of all extant manuscripts according to the principles of modern textual criticism and thus aim to provide a critical replacement for the corresponding volumes of the Patrologia Latina"; CCSL and Sources Chrétiennes serve the same function. Chicago 18th ed. 14.142–14.152 makes naming the edition and translator a completeness requirement rather than a courtesy.

CiC passes this on substance and fails it on legibility. Row 10 names Parisot's *Patrologia Syriaca* I/1–2 (1894, 1907) — which is in fact a Syriac-Latin critical edition and remains the standard edition of Aphrahat, still cited as such in recent scholarship. But nothing in the schema distinguishes "1894 edition that is still the critical standard" from "1894 edition that CCSL replaced in 1962." A reviewer scanning dates for pre-critical editions has no field to check and must know the Syriac bibliography to acquit the row.

**Verdict: REAL GAP on edition status as a field; ALREADY DOES THIS on the underlying citation practice.** **Confidence: High** for the PG/CCSL norm; Medium for Parisot's continuing standard status.

### 4b. Graded confidence in a real apparatus, and its documented failure mode

The UBS *Greek New Testament* committee's letter grades are the closest academic precedent for what CiC's Confidence column does: A = the reading is "virtually certain"; B = "some degree of doubt"; C = "considerable degree of doubt"; D = "very high degree of doubt," the committee having "great difficulty arriving at a decision." Metzger's *Textual Commentary* documents the reasoning behind the grades.

The precedent also carries a warning worth taking seriously, described in the literature as "textual optimism": across editions of the same apparatus, UBS3 carried 126 A-ratings and 144 D-ratings while UBS4 carried 514 A-ratings and 9 D-ratings. The grades drifted upward by roughly an order of magnitude without the manuscripts changing.

CiC's registry is append-only and grades are assigned per-session at the moment of entry, by whoever is building. There is nothing in the current protocol that pins the grading criteria to a version, samples old grades for consistency against new ones, or would surface an upward drift if it happened. The failure would be invisible and would look exactly like improving rigor.

**Verdict: ALREADY DOES THIS (a graded confidence apparatus is legitimate and precedented), with a REAL GAP in drift control.** Two cheap fixes: version the grading criteria on each row, and run a periodic re-grade audit on a random sample of old rows. **Confidence: Medium** (secondary sources on the UBS grades and counts).

---

## 5. What signals academic legitimacy to a reviewer, fast

### 5a. The IDE criteria — the closest thing to a published checklist a reviewer would use

[*Criteria for Reviewing Scholarly Digital Editions*, v1.1](https://www.i-d-e.de/publikationen/weitereschriften/criteria-version-1-1/) (Patrick Sahle with Georg Vogeler and the IDE, June 2014): 39 criteria in five categories — Preliminaries of the Review, Subject and Contents of the Edition, Aims and Methods, Implementation and Presentation, Conclusion. It is the instrument [RIDE](https://ride.i-d-e.de/) applies. Verbatim, the criteria that bear on CiC:

- **2.1 Selection**: "What sources and documents have been selected and why? Are there principles of selection (or sampling)?"
- **2.3 Content**: "Is relevant content missing? **Is any omission explained and/or justified?**"
- **3.1 Documentation**: "Is there a description of the aims and methods of the SDE? If not, is this self-evident from the content and its presentation?"
- **3.4 Method**: "Which editorial school does the SDE follow? Which methodological approach does it take?"
- **3.7 Data modelling**: "Is the documentation of the data model sufficient? Does the SDE follow common standards (e.g. TEI guidelines)? **If not, is the deviation from existing standards sufficiently justified?**"

The catalogue also sets three conditions for scholarly status: editorial justification with clear rules, compliance with scholarly content standards, and realization of the digital paradigm rather than reproduction of print constraints. And it asks reviewers to disclose "their academic background, institutional connections, prior experience, and research interests."

Scored honestly against this: CiC answers **2.1 outstandingly** (stated principles of selection, plus a two-value Exclusion Reason vocabulary that distinguishes a source that was never a candidate from one deliberately recorded as a trap). CiC answers **2.3 outstandingly** (Missing Voices / Affirmative Duty *is* explained omission, as a requirement). CiC answers **3.1 and 3.4** through the L3B methodology corpus. CiC currently fails **3.7** — not because the data model is poor, but because it is undocumented in relation to any external standard and the deviation is unjustified in writing.

**Verdict: STRONG on 2.1/2.3/3.1/3.4, REAL GAP on 3.7 — and the 3.7 gap is fixable with a document rather than a build.** **Confidence: High** (read the criteria page).

### 5b. Disciplinary evaluation guidelines

The AHA's [*Guidelines for the Professional Evaluation of Digital Scholarship by Historians*](https://www.historians.org/resource/guidelines-on-the-professional-evaluation-of-digital-scholarship-by-historians/) (approved June 2015) holds that digital work should be evaluated "on its scholarly merit and the contribution that work makes to the discipline," stresses evaluating projects in their native medium, recognizing collaborative labor, and considering sustainability and revision, and puts a burden on the scholar: historians experimenting with new forms "need to be especially clear about what they are doing, what opportunities it offers, what challenges their work presents to their colleagues, and the impact of their work on the intended audiences."

That last clause is a direct instruction about CiC's own reviewer-facing writing, and it argues against understating the novelty. The MLA's companion guidelines exist and are the other instrument reviewers are pointed to (see Do-not-cite regarding their contents).

[Reviews in Digital Humanities](https://reviewsindh.pubpub.org/about) (founded 2019, launched January 2020) is the operational venue: monthly issues pairing 500-word project overviews with 500-word signed reviews, single-blind with reviewer names published, evaluated against the MLA and AHA guidelines, and explicitly allowing "project directors to seek review at any point in a project's development that they deem appropriate, recognizing that projects are developed in phases and that 'finished' is a moving target."

**This is the concrete, low-cost path to outside academic review that the brief's second goal is asking for.** It does not require CiC to be finished. **Confidence: High** for RDH's process; Medium for the AHA summary.

### 5c. FAIR

Wilkinson et al., ["The FAIR Guiding Principles for scientific data management and stewardship," *Scientific Data* 3 (2016)](https://www.nature.com/articles/sdata201618) — the most-cited data-organization standard across all of research. Findable requires globally unique persistent identifiers and rich machine-actionable metadata; Accessible requires that identifiers resolve to landing pages describing access conditions even for restricted resources; Interoperable requires formally defined formats; Reusable requires a domain-relevant standard, clear usage conditions, and enough metadata attributes for meaningful reuse.

CiC's registry today: internal sequential IDs (not globally unique), markdown plus embedded JSON (not a formally defined standard), no license or usage conditions anywhere, no export. Every one of the four principles is partially unmet, and the four fixes are the same four fixes recommended elsewhere in this document (persistent identifiers, external IDs, a rights field, a machine-readable export).

**Verdict: REAL GAP across all four principles.** **Confidence: High.**

### 5d. The participant-facing half of "browsable"

The Library of Congress's [Primary Source Analysis Tool](https://www.loc.gov/static/programs/teachers/getting-started-with-primary-sources/documents/Primary_Source_Analysis_Tool_LOC.pdf) structures non-specialist engagement as **Observe → Reflect → Question**, with a fourth "Further Investigation" section, format-specific prompt sets (manuscripts, maps, oral histories, printed texts), and a stated design intent to "scaffold inquiry rather than rush to conclusions."

This matters for the redesign's "browsable source repository" objective, because it is the answer to a question the metadata standards do not address: what a general reader should see. The metadata standards above govern what must be *recorded*. LC's tool governs what should be *shown first*. A participant-facing source view built as a field dump satisfies neither a scholar (too shallow) nor a general reader (too dense). Constitution Article 30's Level 3 disclosure — "sources with specificity, confidence, and the complete construction record, reachable on request and never gated" — is the right commitment; LC's scaffold is a tested shape for the layer above it.

**Verdict: NEEDS ADAPTATION — CiC has the disclosure commitment and lacks a presentation model.** **Confidence: Medium.**

---

## What CiC already does at real academic standard

Stated plainly, with the standard each claim can be defended against. None of these are gaps and none should be rebuilt.

1. **Per-claim source traceability, enforced by a gate.** The Checkpoint rule requires a registry row for any source named in support of a claim. TEI requires `sourceDesc` per document; CiC requires it per claim. *(TEI P5 ch. 2.)*

2. **Explicit primary/secondary/material/lexicon typology.** Four values, defined, with a stated allowance for combination. This is the first thing a historian checks and it is present, controlled, and populated. *(Standard external/internal source criticism; Howell & Prevenier.)*

3. **A graded confidence apparatus with published tier definitions.** Precedented directly by the UBS committee's A–D letter grades, and CiC's tier definitions are more operational than UBS's ("verified this session against an accessible primary source" is checkable in a way "virtually certain" is not).

4. **A declared-and-referenced sigla system.** Registry IDs are stable, never reused, and resolved at runtime from inline references. This is the architecture LDLT mandates for witnesses. *(LDLT Guidelines.)*

5. **Exclusion recorded rather than discarded, with a reasoned two-value vocabulary.** Out-of-Boundary versus Named Comparandum, with the Comparandum Note requirement to state the specific image or reading the source must not be mistaken for. IDE criterion 2.3 asks whether omission is "explained and/or justified"; this is a stronger answer than most digital editions can give. *(IDE 2.1, 2.3.)*

6. **Affirmative naming of absences.** Constitution Article 20's Missing Voices duty exceeds DACS, which A4BLiP characterizes as "largely silent" on exactly this. Row 32's licensed purpose — documenting that no bnat qyama woman's own text survives — is the requirement working. *(A4BLiP; Carter, Archivaria 61.)*

7. **Author bias and position recorded without being used to disqualify.** Author Gravity's five dimensions cover Presnell's Author Authority and Perspective-and-Bias criteria, and "noted, not disqualifying" is the correct scholarly posture rather than the safe one.

8. **Description control at above-average specificity.** `Added` plus `Verification Note` record how, when, and by whom — ISAD(G)'s Description Control Area, executed at a level of detail most finding aids do not reach.

9. **Append-only record integrity.** Never renumber, never delete; a discredited source moves to Confidence E and disposition removed-from-use and stays as a record of what was tried. This is PREMIS's event-logging principle and the archival principle that description is itself a record.

10. **A positive rather than negative apparatus for retrieval.** The `/audit` endpoint preserves every candidate considered and why it was skipped. In apparatus-criticus terms this is the positive apparatus — the more expensive and more trusted choice.

11. **Boundary status assessed by what a source speaks for rather than when it was written**, with an explicit foreclosure of manufactured differentiation between worlds. This is *respect des fonds* applied to evidence, and the anticipatory defense is already written into the template.

12. **Honest self-limitation in the template itself.** The Source Registry Template states that a registry "only classifies sources someone has already proposed as candidates. It cannot, by itself, stop a model from reaching for something nobody proposed," and names the downstream grounding-anchor paragraph as the actual fix — including the admission that "an earlier draft of this mechanism overclaimed this exact point." Reviewers weight disclosed limitations heavily, and a document that names its own prior overclaim is unusually credible.

---

## Real gaps — what a top academic reviewer would expect that CiC doesn't yet have

Each gap names the standard it is drawn from.

| # | Gap | Standard it comes from | Severity |
|---|---|---|---|
| 1 | **No attribution/authenticity status.** No way to mark a work as genuine, dubium, spurium, anonymous, or later-attributed. Independent of Type and of Boundary Status. | *Clavis Patrum Graecorum* / *Latinorum* — every work numbered, "whether genuine or not," with dubia/spuria marked | **Highest.** First thing a patristics reader checks; live risk for *Apophthegmata* and Ephrem material |
| 2 | **Work, edition, and translation collapsed into one free-text string.** Row 10 holds one work, one critical edition, and two translations with no field for which was read. | IFLA LRM WEMI; CTS URN work-vs-version; Chicago 18th ed. 14.142–14.152 ("full details of the modern edition used, including the name of the editor and/or translator") | **Highest** |
| 3 | **Confidence conflates pointer specificity, verification recency, and evidentiary weight.** No axis for how much load a source can bear, so the "flag C-or-below supporting a vivid claim" rule has to proxy it. | TEI `<certainty>` `@locus` and `@degree` | **High** |
| 4 | **No grade-drift control.** Grades assigned per session, criteria unversioned, no re-audit. | UBS3→UBS4 documented inflation (126→514 A-ratings; 144→9 D-ratings) | **High** — invisible failure mode |
| 5 | **No level of description.** Item-level rows and aggregate-attestation rows (row 10 vs. row 13) sit at the same apparent level. | ISAD(G) 3.1.4 Level of description — one of six mandatory elements | **High** |
| 6 | **No language or script field.** | DACS 4.5, a Single-Level *Required* element | **High** |
| 7 | **No genre/form or purpose/audience field.** The one classic source-criticism category with no home. Doc_09 has narrative tiers; the source row does not. | Presnell, *The Information-Literate Historian*: "Who is the intended audience? Why was the item created?" | **High** |
| 8 | **No edition-status field.** Nothing distinguishes a still-standard 1894 critical edition from a superseded pre-critical one. | The PG/PL-versus-CCSG/CCSL/CSEL norm | **Medium-High** |
| 9 | **No typed relations between rows.** Row 33's "USE CAUTIOUSLY, does not stratify pre-/post-410 evidence" cannot link to rows 13/32 that do. | ISAD(G) 3.5.3; DCMI relation terms; RiC-CM 1.0 (2023) | **Medium-High** |
| 10 | **No persistent external identifiers.** Internal sequential IDs only. Syriaca.org URIs, BHSE numbers, CPG/BHG/BHL numbers, VIAF, DOIs all unused, though the Syriac infrastructure already exists and is free. | FAIR F1 (Wilkinson et al. 2016); Syriaca.org URI policy | **Medium-High** — best effort-to-legitimacy ratio available |
| 11 | **No rights, license, or access field.** Blocking for a public browsable repository showing translated text. | DACS 8.2, a Single-Level *Required* element; DCMI `accessRights` / `license` / `rightsHolder` | **Medium**, becomes blocking at ship |
| 12 | **Transmission history is per-author prose, not a per-row field.** So it cannot be surfaced in a browsable view. | DCMI `provenance`; TEI `msDesc/history`; DCRMR 9.42 custodial history | **Medium** |
| 13 | **No state-of-the-question field.** Author Gravity covers the author's bias; nothing records whether a secondary source's reading is majority, minority, contested, or superseded in current scholarship. | Presnell (Accuracy: "How does the source compare to other similar sources?"); IDE 2.2 "What has been taken from earlier works, what is new?" | **Medium** |
| 14 | **No machine-readable export and no conformance statement.** No mapping to any external standard, and no published justification for deviating from one. | IDE 3.7: "If not, is the deviation from existing standards sufficiently justified?"; FAIR I/R | **Medium** — cheapest to close |
| 15 | **No public correction channel or description attribution.** | A4BLiP Transparency category; Syriaca.org/BHSE editorial-revision submission | **Low-Medium** |

One thing that is not a gap but needs a sentence of explanation in reviewer-facing copy: **`Licensed For` has no counterpart in any standard surveyed.** It records permission rather than description — the specific gravity, force, lexicon term, or trait a source justifies, with the rule that a Native source with nothing named there is unusable downstream. That inversion is what makes the registry a control rather than a bibliography, and it is genuinely CiC's own contribution. A reviewer will not recognize it, so it needs one explanatory line rather than being left to be inferred.

---

## Recommendations — field-level

### Tier 1: adopt now, in the schema redesign (small, high-signal)

Add these fields to the Source Registry entry schema. Controlled vocabularies given; the standard each answers to is named so the conformance statement writes itself.

```
attribution_status        genuine | dubium | spurium | anonymous |
                          pseudonymous | attributed-later
                          [CPG/CPL practice] — required on every P-type row
attribution_note          free text: whose attribution, in what source, how late
                          (e.g. "Jacob of Serugh, 6th-c. Vita Ephraemi")

level_of_description      item | work | corpus | aggregate-attestation
                          [ISAD(G) 3.1.4, mandatory] — fixes rows like #13

language                  ISO 639-3 code(s) of the source as consulted
script                    ISO 15924 code (Syrc, Grek, Latn, ...)
                          [DACS 4.5, Single-Level Required]

genre_form                letter | homily | conciliar-act | liturgical-text |
                          hagiography | chronicle | legal-rescript | polemic |
                          monastic-rule | apophthegm-collection | commentary |
                          monograph | journal-article | reference-work
                          [Presnell; ties to Doc_09's existing narrative tiers]
purpose_audience          free text, one sentence: why made, for whom
                          [Presnell: "Who is the intended audience?"]
```

Split the `Source` string into structured subfields, keeping a rendered display citation for human reading:

```
work_author               as attributed (pair with attribution_status)
work_title
work_locus                book/chapter/letter/line — the citable pointer
edition                   editor, series, year of the edition consulted
translation               translator, series, year — or null if read in original
edition_status            critical | standard-pre-critical | uncritical-reprint |
                          superseded | none-consulted
consulted_as              original-critical | original-uncritical |
                          translation | secondary-report-only
                          [IFLA LRM WEMI; CTS URN; Chicago 14.142–14.152;
                           Chicago/Turabian "quoted in" rule]
```

Split `Confidence` into three named axes, and derive the outward-facing A–E letter from them so nothing downstream breaks:

```
citation_specificity      A–E, exactly the current definitions, narrowed to
                          pointer precision only
verification_state        verified-direct | verified-via-authority |
                          named-not-rechecked | unverified
verification_date         ISO date
evidentiary_weight        load-bearing | corroborating | illustrative | contested
                          [TEI <certainty> @locus + @degree]
grade_criteria_version    version string of the grading rubric in force
                          [UBS3→UBS4 drift]
```

`evidentiary_weight` also gives the "flag C-or-below supporting a vivid claim" rule a real field to key on instead of a proxy.

### Tier 2: adopt with the browsable repository build

```
external_ids[]            {scheme, value, uri}
                          schemes: syriaca | cpg | cpl | bhg | bhl | bhse |
                          cts-urn | viaf | doi | isbn | pinakes
                          [FAIR F1; Syriaca.org URI policy]

relations[]               {type, target_row_id, note}
                          types: qualifies | is-qualified-by | corroborates |
                          contradicts | is-edition-of | is-translation-of |
                          supersedes | same-work-as
                          [ISAD(G) 3.5.3; DCMI relations; RiC-CM 1.0]

transmission_path         earliest surviving witness (date, form), transmitting
                          community, whether the surviving form is the composed
                          form
                          [DCMI provenance; TEI msDesc/history; DCRMR 9.42]

field_state                majority | minority | contested | superseded | n/a
                          — the state of the question, distinct from author bias
                          [Presnell; IDE 2.2]

rights_status              public-domain | in-copyright | licensed | unknown
license                    SPDX id or free text
display_permitted          boolean — may the repository show the text itself
                          [DACS 8.2; DCMI accessRights/license/rightsHolder]
```

Rename the existing `Added` + `Verification Note` pair as a **Description Control** block and cite ISAD(G) 3.7 in the template. Content unchanged; recognition gained for free.

### Tier 3: three non-schema actions, in order of cost-to-benefit

1. **Write a one-page Conformance and Deviation Statement.** Map every registry field to its DACS / ISAD(G) / TEI / Dublin Core counterpart, list the four fields with no counterpart (`Boundary Status`, `Exclusion Reason`, `Licensed For`, `Comparandum Note`), and say in two sentences each why CiC needs them. This answers IDE criterion 3.7 by name and converts the largest silent liability in the apparatus into a stated methodological position. Cheapest item on this list.

2. **Publish a machine-readable export** — `sources.json` per world, or a TEI `<listBibl>` — with a stable resolvable URI per row. Closes three of the four FAIR principles at once.

3. **Submit to *Reviews in Digital Humanities*.** Signed single-blind review against the MLA and AHA guidelines, with an explicit policy of accepting projects "at any point in a project's development." This is the actual mechanism for the brief's second goal, and CiC does not need to be finished to use it.

For the participant-facing repository view, structure the top layer as LC's **Observe → Reflect → Question** scaffold with the full registry row reachable beneath it, rather than presenting the row as the primary interface. Constitution Article 30's Level 3 commitment is already the right guarantee; this is only the shape of the layer above it.

### Sequencing note

Tier 1 is a schema change to a living, append-only document. Existing rows will not have the new fields, and the append-only protocol forbids rewriting them. Recommend: version the schema, mark pre-existing rows with `schema_version: 1`, and backfill only `attribution_status`, `level_of_description`, and `language`/`script` — the three fields where a blank is itself a defect. The rest can populate forward.

---

## Do not cite — items I could not verify

Four things I went after and could not confirm. Listed so nobody quotes them on my authority later.

- **MLA *Guidelines for Evaluating Work in Digital Humanities and Digital Media*** — the page returned no retrievable body text. The document exists and RDH names it as an evaluation instrument; **do not attribute any specific wording or criterion to it** without reading it directly.
- **A4BLiP *Anti-Racist Description Resources* verbatim text** — the PDF would not parse. The seven category names and the DACS-silence characterization are confirmed via the SAA standards portal and the annotated bibliography; **the recommendations under Transparency are not quoted here and should not be paraphrased as quotations.**
- **ISAD(G) 2nd ed. sub-element numbering in area 3.7** — only the area's purpose is confirmed ("information ... about how, when and by whom the archival description was prepared"). The commonly cited 3.7.1 Archivist's Note / 3.7.2 Rules or Conventions / 3.7.3 Date(s) of Descriptions numbering is plausible and widely repeated but I read it in no primary source; verify against [the ICA PDF](https://www.ica.org/app/uploads/2024/01/CBPS_2000_Guidelines_ISADG_Second-edition_EN.pdf) before citing the numbers.
- **LC MARC discussion paper 2022-DP09** — returned 403. Cite only as "a 2022 MARC Advisory Committee discussion paper on defining a standardized provenance field," which the result title supports. No claims about its contents.

Two further honest limits. The *Clavis Patrum Graecorum*'s dubia/spuria convention I have from Brepols and Corpus Christianorum project pages rather than the printed Clavis; the convention is not in doubt but the exact editorial language is not verified. And the UBS A-rating counts (126→514, 144→9) come from a secondary discussion, not from counting the editions; treat the direction as solid and the exact figures as approximate.

---

## Sources

**Archives and libraries:** [DACS Chapter 1, levels of description](https://saa-ts-dacs.github.io/dacs/06_part_I/02_chapter_01.html) · [DACS 8.2 Rights Statements](https://saa-ts-dacs.github.io/dacs/06_part_I/09_chapter_08/02_rights_statements_archival_description.html) · [DACS 2019.0.3 full text](https://files.archivists.org/pubs/DACS_2019.0.3_Version.pdf) · [ISAD(G) 2nd ed. (ICA PDF)](https://www.ica.org/app/uploads/2024/01/CBPS_2000_Guidelines_ISADG_Second-edition_EN.pdf) · [ISAD(G) element list](https://www.hi.u-tokyo.ac.jp/personal/yokoyama/jugyo99/isad\(g\)e.html) · [ISAD(G) via Archives Hub](https://archiveshub.jisc.ac.uk/isadg/) · [SAA on ISAD(G)](https://www2.archivists.org/groups/standards-committee/international-standard-archival-description-general-isadg) · [Records in Contexts (ICA/EGAD)](https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-ric/) · [RiC-CM 1.0 PDF](https://www.ica.org/app/uploads/2023/12/RiC-CM-1.0.pdf) · [DCRMR](https://rbms.info/dcrm/dcrmr/) · [DCRMR 9.42 Custodial history of item](https://bsc.rbms.info/DCRMR/additional-notes/Custodial-history-of-item/) · [PREMIS Data Dictionary v3.0](https://www.loc.gov/standards/premis/v3/premis-3-0-datadictionary-only.pdf) · [TNA digital cataloguing practices](https://cdn.nationalarchives.gov.uk/documents/digital-cataloguing-practices-march-2017.pdf) · [LC Primary Source Analysis Tool](https://www.loc.gov/static/programs/teachers/getting-started-with-primary-sources/documents/Primary_Source_Analysis_Tool_LOC.pdf)

**Digital humanities standards:** [TEI P5 ch. 2, The TEI Header](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html) · [TEI P5, Certainty, Precision, and Responsibility](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html) · [TEI P5, Critical Apparatus](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html) · [TEI P5, Manuscript Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html) · [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) · [OpenWEMI announcement (DCMI, 2024)](https://www.dublincore.org/blog/2024/announcing-openwemi/) · [IFLA resource and WEMI](https://www.ifla.org/files/assets/cataloguing/isbd/OtherDocumentation/resource-wemi.pdf) · [LDLT Encoding Guidelines](https://digitallatin.github.io/guidelines/LDLT-Guidelines.html) · [Library of Digital Latin Texts](https://ldlt.digitallatin.org/) · [What Is a CTS URN? (Perseus)](https://sites.tufts.edu/perseusupdates/2021/01/05/what-is-a-cts-urn/) · [The CITE Architecture](https://dlib.nyu.edu/awdl/isaw/isaw-papers/20-8/) · [Canonical Text Services (Digital Classicist)](https://wiki.digitalclassicist.org/Canonical_Text_Services) · [Syriaca.org URI policy](https://syriaca.org/documentation/uris.html) · [Bibliotheca Hagiographica Syriaca Electronica](https://syriaca.org/bhse) · [A New Handbook of Syriac Literature](https://syriaca.org/nhsl) · [Gateway to the Syriac Saints](https://syriaca.org/saints/index.html)

**Patristics and textual criticism:** [Clavis Patrum Graecorum (Corpus Christianorum)](https://www.corpuschristianorum.org/cpg) · [Clavis Patrum Latinorum](https://www.corpuschristianorum.org/cpl) · [CPG series (Brepols)](https://www.brepols.net/series/CCCPG) · [Yale Library, Early Christianity and Patristics: Editions & Translations](https://guides.library.yale.edu/ancientchristianity/editions) · [NAPS on Patrologia Graeca](https://www.patristics.org/resources/patrologia-graeca-ed-migne/) · [CUA guide, Critical and Standard editions](https://guides.lib.cua.edu/c.php?g=590072&p=4080616) · [EpiDoc, Apparatus criticus](https://epidoc.stoa.org/gl/latest/supp-apparatus.html) · [Burghart, "Textual Variants" (QMUL)](https://projects.history.qmul.ac.uk/wp-content/uploads/sites/6/2017/09/04-Textual-variants-MB.pdf) · [Elliott, "A Second Look at the UBS GNT"](https://translation.bible/wp-content/uploads/2024/06/elliott-1975-a-second-look-at-the-united-bible-societies-greek-new-testament.pdf) · [Edwards, "On Using the Textual Apparatus of the UBS GNT"](https://translation.bible/wp-content/uploads/2024/06/edwards-1977-on-using-the-textual-apparatus-of-the-ubs-greek-new-testament.pdf) · [syri.ac, Aphrahat](https://syri.ac/brock/aphrahat)

**Historical method:** Howell & Prevenier, *From Reliable Sources: An Introduction to Historical Methods* (Cornell UP) — [review, The Medieval Review](https://scholarworks.iu.edu/journals/index.php/tmr/article/view/15260) · Presnell, *The Information-Literate Historian* (OUP) — [publisher page](https://global.oup.com/academic/product/the-information-literate-historian-9780197749869), [criteria as taught](https://resources.library.lemoyne.edu/guides/history/primary-sources/evaluating) · [Carter, "Of Things Said and Unsaid," *Archivaria* 61 (2006)](https://archivaria.ca/index.php/archivaria/article/view/12541) · [A4BLiP Anti-Racist Description Resources (SAA)](https://www2.archivists.org/standards/archives-for-black-lives-in-philadelphia-a4blip-anti-racist-description-resources) · [Cal Poly, Gaps and Silences in the Archives](https://guides.lib.calpoly.edu/archives/critical) · [Turabian citation quick guide](https://www.chicagomanualofstyle.org/turabian/citation-guide.html) · [Chicago on classical references](https://www.chicagomanualofstyle.org/search.html?clause=classical) · [Dickinson, Citing Ancient Sources](https://libguides.dickinson.edu/classicalstudies/citing) · [SFU, Chicago secondary sources](https://www.lib.sfu.ca/help/cite-write/citation-style-guides/chicago/secondary-sources)

**Evaluation and legitimacy:** [IDE, Criteria for Reviewing Scholarly Digital Editions v1.1](https://www.i-d-e.de/publikationen/weitereschriften/criteria-version-1-1/) · [IDE, Criteria for Reviewing Tools and Environments v1.0](https://www.i-d-e.de/publikationen/weitereschriften/criteria-tools-version-1/) · [RIDE](https://ride.i-d-e.de/) · [RIDE editorial](https://ride.i-d-e.de/about/editorial/) · [Reviews in Digital Humanities — About](https://reviewsindh.pubpub.org/about) · [RDH editorial process](https://reviewsindh.pubpub.org/review-process) · [AHA, Guidelines on the Professional Evaluation of Digital Scholarship by Historians](https://www.historians.org/resource/guidelines-on-the-professional-evaluation-of-digital-scholarship-by-historians/) · [MLA, Guidelines for Evaluating Work in DH and Digital Media](https://www.mla.org/About-Us/Governance/Committees/Committee-Listings/Professional-Issues/Committee-on-Information-Technology/Guidelines-for-Evaluating-Work-in-Digital-Humanities-and-Digital-Media) *(named only — contents unverified)* · [Wilkinson et al., "The FAIR Guiding Principles," *Scientific Data* 3 (2016)](https://www.nature.com/articles/sdata201618) · [GO FAIR principles](https://www.go-fair.org/fair-principles/)

**CiC internal sources read:** `L3B-World-Build-Methodology/Source_Registry_Template.md` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/02_Codebase_Mining.md` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/04_BuildProcess_Methodology_Mapping.md` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/09_External_AIPersona_Framework_Survey.md` · `cic-poc/backend/transcripts/d1ec86a7-dcf4-4c06-869a-f6fba1ba12cb.json`
