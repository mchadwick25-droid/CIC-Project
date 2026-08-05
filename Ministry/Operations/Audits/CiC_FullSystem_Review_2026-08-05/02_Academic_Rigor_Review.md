# Academic Rigor Review — Would a Seminary Church-History Professor Trust This?

Run 2026-08-05 under `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`:
source-level verification (every claim checked against the actual file or the actual
primary/secondary source, not against a summary — including not against docs 12–14's own
summaries), the fixed P0/P1/P2 vocabulary, structural checks counted rather than eyeballed,
and a plain verdict at the end. All reading done directly in this pass; no sub-agents, per
the note at the bottom of `CiC_Redesign_Research_2026-07-25/00_INDEX.md`.

---

## 1. What I read, what's new here, what I deliberately left alone

### 1a. Prior work read in full first

`12_Academic_Source_Organization_Standards.md`, `13_Terminology_Alignment_Audit.md`,
`14_Source_Identification_Discovery_Methodology.md`, `06_SixWorld_Defect_Quantification.md`,
and both index files. I took their external-standard citations as given — I did not
re-derive DACS 4.5, TEI `@locus`, CPG *dubia/spuria*, STARLITE, PRISMA-S, or Greenhalgh &
Peacock. What I checked is whether **their findings still describe the system as it stands
on 2026-08-05**, which turns out to be a much larger question than it was on 2026-07-26,
because most of them have been acted on.

### 1b. The single most important fact about the current state

**Docs 12, 13 and 14 are no longer a list of open gaps. They were built.** Between
2026-07-26 and 2026-08-01 the project (a) folded doc 14's recommendations into the governing
methodology nearly verbatim, (b) adopted a standalone governing Completion Standard, and
(c) migrated all six worlds into a new record store whose schema implements most of doc 12's
Tier 1/Tier 2 field list and doc 13's `register` field.

Verified directly:

- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`,
  Step 2, now requires a `search_record` kept as discovery proceeds; per-row
  `discovery_channel` / `discovery_instrument` / `discovery_date`; a field-bibliography
  sweep before the Registry closes; a **saturation statement naming the last unproductive
  searches**; and, in the Doc_02 review requirement, the ten-item relative-recall test and
  the PRESS question **asked verbatim in doc 14's own wording**.
- `Ministry/Technology/CiC_World_Build_Completion_Standard_V1.0.md` (GOVERNING, adopted by
  Mark 2026-07-27) makes those requirements freeze conditions with machine gates in
  `cic-poc/backend/wrs/gates/`.
- `cic-poc/backend/wrs/schema/records.schema.json` carries `attribution_status`,
  `attribution_note`, `level_of_description`, `language`, `script`, `genre_form`,
  `edition`, `edition_status`, `consulted_as`, `external_ids`, `field_state`,
  `transmission_path`, `license`, `display_permitted`, `citation_specificity`,
  `verification_state`, `evidentiary_weight`, `grade_criteria_version`,
  `discovery_channel/instrument/date`, `snowball_parent_row`, plus doc 13's
  `register: emic | etic | emic-unavailable`, `semantic_domain`, `field_relations`,
  `divergence_partners`, and the split `eviction_priority` / `cache_stability`.
- All six worlds now have freeze declarations
  (`Ministry/Technology/Pass2/gates/S6.2_*_FREEZE_DECLARATION.md`, the last dated
  2026-08-01) and `Ministry/Technology/Pass2/drafts/CiC_FAIR_Conformance_and_Deviation_Statement_DRAFT_2026-07-27.md`
  is doc 12's Tier-3 item 1, drafted.

So the useful question is no longer "what's missing" but **"is the built thing real, and is
it real to the same depth everywhere?"** That is what this document measures.

### 1c. Two worlds read deep, and why those two

- **Syriac Christianity (Edessa/Nisibis)** — built first (2026-07-07/08), carries the
  largest review corpus in the project (50 files in `Review-Artifacts/`; doc 06 counted 49
  review files across the world),
  and is the world whose own Doc_02 Round 1 review diagnosed the project's signature failure
  mode: "a repeated, identifiable pattern of inventing false precision on top of real
  sources." If the review apparatus works anywhere, it works here. It is also the world
  whose material (Syriac, non-Greek, non-Latin) is hardest for a generalist to check —
  which makes it the best test of whether the sourcing is real or plausible-sounding.
- **Imperial and Juridical Christianity** — built last (2026-07-19/22), with the most
  process scaffolding, and per doc 06 the **worst round record in the portfolio** (zero of
  ten documents cleared in a single round; 40% needing three rounds). It is also the world
  most exposed to the angle I was asked to hunt: modern political and confessional framing
  (Constantine, church-and-state, papal primacy, "Arianism") retrojected into a pre-modern
  voice.

Read in full for both: `Doc_02_Source_Ecology.md`, `Doc_04_Gravity_Discovery.md`, the
Registry (`Source_Registry.md` for IJC; `data/syriac_world/source_registry.json` for Syriac —
Syriac's `.xlsx` is not in the repo, PAHC's is and I opened it, see P1-3), the deployed
Permanent Prompts, and the freeze declarations. Spot-checked more lightly: all four other
worlds' Doc_02s, HAL's in near-full because it turned out to be the fleet's best.

### 1d. Structural checks I ran myself rather than trusting

All numbers below are from scripts run against `cic-poc/backend/wrs/records/` on 2026-08-05,
not from any project artifact:

| Check | Result |
|---|---|
| Source-link referential integrity (every `sources[].source_id` on every claim-bearing record resolves to a real source row in the same world) | **897 links, 6 worlds, 0 unresolved** |
| Source rows fleet-wide | 270 (PAHC 76, SYR 64, IJC 41, ALX 37, DES 26, HAL 26) |
| Rows carrying `discovery_channel` | 270 / 270 |
| Rows carrying `discovery_instrument` | **40 / 270 (15%)** |
| `discovery_channel` distribution | builder-prior-knowledge 169, field-bibliography 55, backward-snowball 19, reviewer-supplied 16, step0-seed-list 6, database-search 4, cited-in-another-row 1 |
| Term records with all four diachronic sense fields | 116 / 118 |
| Term records with the three-axis confidence block | **118 / 118** |
| `verification_state` distinct values fleet-wide | **1** (`verified-via-authority`, 118/118) |
| `edition` / `translation` / `consulted_as` populated | **0 / 270 each** |
| `external_ids` populated | **0 / 270** |
| `register: emic-unavailable` used | **0 records fleet-wide** |
| Force records carrying `sources[]` | ALX 18/18, DES 12/12, HAL 12/12, PAHC 14/14, SYR 13/13, **IJC 0/10** |
| `language`/`script` disagreement | PAHC: 16 rows `grc` + `Latn` |
| Language-code standard | ALX/DES/SYR use ISO 639-3 (`eng`,`lat`); PAHC/IJC use ISO 639-1 (`en`,`la`); HAL mixes both |

### 1e. What I deliberately did not cover

Retrieval architecture and runtime engineering (doc 03's angle); participant-facing
accessibility and reading level (docs 01 and 04); the Facilitator's live conversational
behavior and the safety layer; the Atlas; the `.docx` build-methodology documents other than
Construction Framework V7.4; and the four non-source `.xlsx` index workbooks. I also did not
attempt a coverage audit of my own — I did not try to name what each world's bibliography is
missing, because the project now runs that test itself (see §2.6) and running it worse would
add nothing.

---

## 2. What a real scholar would recognize as genuinely good

These are not throat-clearing. Each is something I checked and could defend to a
dissertation committee.

### 2.1 The bibliographic apparatus in Syriac Doc_02 §2 is accurate to a level that recall does not produce

I checked every row of the Ephrem edition table in
`World-Builds/Syriac-Christianity-Edessa-Nisibis/Doc_02_Source_Ecology.md` §2 against my own
knowledge of the CSCO series:

- *Hymns on Faith*, 87 hymns, Beck CSCO 154–155 (1955); Wickes, CUA Press 2015 as the first
  complete English — **correct on all four points**, including the "first complete" claim.
- *Contra Haereses*, Beck CSCO 169–170 (1957) — correct, and "no complete modern English
  translation exists" is correct.
- *Hymns on Paradise*, 15 hymns, Beck CSCO 174–175 (1957), Brock SVS 1990 — correct.
- *Carmina Nisibena*, Beck CSCO 218–219 and 240–241 (1961/1963) — **correct**, and this is
  the row Doc_02 itself flags as needing checking. Doc 14 noticed the same irony from the
  other side ("the self-flagged item turned out correct, while unflagged items contained
  the real errors").
- *Nativity* CSCO 186–187 (1959); *Virginity* CSCO 223–224 (1962), McVey Paulist 1989;
  Tonneau CSCO 152–153 (1955); Mitchell 1912 & 1921; Leloir (Armenian 1953, Syriac 1963 +
  1990); McCarthy Oxford 1993 — all correct.

On Aphrahat: Parisot, *Patrologia Syriaca* I/1–2 (1894, 1907) as the critical edition;
Lehto (Gorgias 2010) as the standard complete English; **Gwynn's NPNF 2nd ser. vol. 13
covering only eight of the twenty-three** — correct and unusually precise; the 336/7 +
344 + August 345 composition scheme and the 22-letter alphabetic acrostic — correct; the
Georgian version of Demonstration 6 derived from an Armenian intermediary and transmitted
under a misattribution to Hippolytus, held distinct from the separate Armenian version
misattributed to Jacob of Nisibis, ed. Antonelli 1756, 19 homilies — **correct, and this is
exactly the kind of detail that is very hard to get right from memory and very easy to
garble.** Whatever produced it was in contact with real bibliography.

On the Diatessaron: the Dura-fragment dispute is stated with the correct sides (Joosten
defending; Parker, D. G. K. Taylor and Goodacre against — that is a real 1999 joint paper),
and Petersen 1994, Crawford & Zola 2019, Barker 2022 are all real and correctly dated.

### 2.2 The Imperial-Juridical world's Homoian disclosure is the most professionally
courageous thing in the corpus

`World-Builds/Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` §7 is a *required*
methodological obligation, not an optional courtesy, and it says the thing most seminary
surveys will not say: "For a combined span of roughly two decades within this world's own
312–451 window, 'the Roman imperial church' and 'Homoian Christianity' were, at the level of
state-recognized establishment, the same thing." It gets the supporting detail right — the
"Dated Creed" correctly identified as the Fourth Sirmian formula dated 22 May 359, Rimini
and Seleucia the same year, the Homoian creed subscribed at Constantinople in 360, Valens
364–378 — and it names the transmission asymmetry precisely, including the correction its
own Round 1 review forced: that the Auxentius letter on Ulfila survives inside the
*Dissertatio Maximini contra Ambrosium*, a **Homoian** work, in Paris lat. 8907, as an
erased layer. Round 1 caught the first draft asserting the exact inverse (that the
containing work was hostile-Nicene) — an inverted-source error of precisely the class the
Standard Practice document exists to catch, caught by the project's own review.

Other IJC specifics I checked and found correct: Julius I's 341 letter preserved in
Athanasius, *Apologia contra Arianos* 21–35; Leo's Tome = Epistula 28; CTh 16.1.2
("Cunctos populos," 380); CTh Title 16.8's actual rubric; Eusebius's hedged letter to his
own congregation about *homoousios*; Eusebius's silence on Crispus and Fausta; Augustine
*Confessions* 9.7 on the antiphonal singing during the 386 standoff; Theodoret rehabilitated
at Chalcedon and condemned only at 553; *episkopos tōn ektos* correctly parked at Contested.

### 2.3 Hieronymian is the fleet's best document on confidence discipline

`World-Builds/Hieronymian-Ascetic-Literary/hal_Doc_02_Source_Ecology.md` gets Jerome's birth
date right *as a dispute* (Kelly c. 331 vs. Rebenich c. 347, with the age-at-death argument
named), gets every letter number, date and addressee right (Epp. 22, 46, 77, 107, 108, 127),
gets the Vulgate's two phases right (Gospels against the Greek c. 382–384 at Rome; OT from
the Hebrew c. 390–405 at Bethlehem, under *Hebraica veritas*), and gets Fabiola's 395
Bethlehem visit cut short by the Hun invasion right. More importantly it does two things
almost no undergraduate-facing project does:

- It **downgrades itself**: "an earlier draft rated this range as 'Documented-to-Widely-
  Accepted,' which overclaimed the top of the range against the document's own vocabulary."
- It **catches its own self-contradiction**: an earlier draft claimed independent,
  non-Jerome evidence for Fabiola's hospital "while in the same breath admitting no
  epigraphic or administrative trace had been found."

And on Palladius it simply refuses to cite: "the specific passage and its precise wording
could not be pinned to an exact chapter/section reference in this document's research pass
and should be independently verified... **do not cite a specific claim from Palladius until
the passage is located and confirmed.**" That is the correct professional move.

### 2.4 Syriac Doc_04 contains the single most convincing artifact in the corpus

Two things in `Doc_04_Gravity_Discovery.md`:

- **C4's Formation test is recorded as a Fail and carried forward.** "The evidence base
  speaks to modern reconstruction difficulty... rather than to how the ambiguity was
  actively lived and experienced by participants at the time. **Fail, carried forward as an
  open item rather than smoothed into a nominal pass (Round 2 correction).**" A build
  process that lets a candidate keep a failing test on the record, because the honest answer
  is a fail, is doing something most published work does not.
- **C2 had a sub-claim surgically removed rather than re-flagged.** The claim that Ephrem
  personally organized the *bnat qyama* choirs was excluded from a Primary gravity's
  evidentiary basis because its attestation (Jacob of Serugh's panegyric; the Syriac *Vita
  Ephraemi*) is sixth-century, outside the world's own 200–410 boundary — and the exclusion
  was then written forward as a standing instruction to Doc_09 so it "cannot be quietly
  reintroduced as in-window fact." That is temporal-boundary hygiene applied against the
  project's own interest in a vivid claim.

### 2.5 Per-claim traceability is not a slogan; it holds mechanically

I resolved every source pointer myself: **897 links across six worlds, zero unresolved.**
Doc 12 credited CiC with requiring source declaration per *claim* where TEI requires it per
*document*; that is now machine-true, not aspirational, and I confirmed it independently
rather than trusting the gate reports.

### 2.6 Doc 14's cheapest recommendation was executed fleet-wide, with real numbers and real misses

`Ministry/Technology/Pass2/reviews/` carries a ten-item relative-recall run and the verbatim
PRESS question for every world: **Desert 9/10, PAHC 9/10, HAL 9/10, Syriac 8/10, IJC 7/10,
Alexandria 6/10.** The misses are named, not softened. Desert's missing item is John
Cassian — correctly identified as "the largest genuine gap... an in-window (c. 420s)
participant-witness of Scetis practice and the principal transmission channel of this
world's formation logic to the Latin West," with the boundary problem (written in Gaul,
about Egypt) named as the reason it deserves a dispositioned row rather than silence. IJC's
PRESS answer identifies Dagron's *Naissance d'une capitale* and observes, unprompted, that
"**Strand B... currently has NO dedicated secondary row** — its scholarship rides the
conciliar primary rows plus generalist coverage, while Strands A and C each carry two or
more dedicated studies." That is a self-diagnosed structural imbalance in its own
bibliography. Doc 14 asked for a baseline; there is one.

### 2.7 The Constitution's confidence vocabulary has teeth

Construction Framework V7.4 Part II fixes five levels *and prohibits language*: "'settled,'
'proves,' 'consensus,' 'certainly'" unless Documented is genuinely met. And there is **no
Tier 5** — generated illustrative narrative is prohibited outright: "If the evidence does not
support a story, the story does not exist for this world. Silence in thin areas is the right
response." A rule that forecloses the most tempting shortcut in the whole enterprise, stated
in the governing document rather than in a footnote.

### 2.8 Doc 12's highest-value structural fix landed completely

Doc 12's finding #3 — "Confidence conflates pointer specificity, verification recency, and
evidentiary weight" — is now implemented on **118 of 118 term records in all six worlds**:
`citation_specificity`, `verification_state`, `verification_date`, `evidentiary_weight`,
`formation_confidence`, as five separate fields. And the Level 3 participant view renders
them in plain English (`wrs/views/plain_explanation.py`, `CONFIDENCE_PLAIN`), stating the
constitutional level verbatim and then explaining it, rather than replacing the vocabulary.
See P1-1 for what still defeats it in practice — but the structure is genuinely there.

---

## 3. Findings

Severity per the Standard Practice: **P0** = blocks / must fix. **P1** = materially improves.
**P2** = polish.

---

### P0-1 — 50 source rows assert a discovery channel their own world's search record denies

**Where.** `cic-poc/backend/wrs/migrate/s62_syr_source_rows.py` lines 203–206 assign
`discovery_channel` by a **type rule, not by evidence**:

```python
"discovery_channel": ("builder-prior-knowledge"
                      if stype in ("P", "M")
                      else "field-bibliography"),
```

with the comment "scholarship rows arrived via the field bibliography." The same convention
runs through `s62_alx_source_rows.py` (every S row hard-coded `discovery_channel="field-bibliography"`)
and `s62_hal_s21.py`.

**Why it's a P0.** The same world's own search record says the opposite. `wrs/records/syriac_world/search_record/srcSYRsearch001.md`:

> "NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L'Année
> philologique; Oxford Bibliographies; the Hugoye cumulative index; a systematic GEDSH
> pass."

Identical declarations appear in `srcPAHCsearch001/002`, `srcIJCsearch001/002`, and the
HAL and ALX equivalents. **No field bibliography has been consulted anywhere in the fleet.**
Yet 55 rows carry `discovery_channel: field-bibliography`, of which **50 (27 Syriac, 12
Alexandria, 11 Hieronymian) carry no `discovery_instrument` at all**. Only the five Desert
rows so labelled name an actual instrument, and even those name publisher pages and a Coptic
Congress preliminary bibliography rather than a field bibliography proper.

Doc 14 anticipated this exactly: "Do not attempt to backfill `discovery_instrument` or
`discovery_date`; that information is gone, and inventing it would reproduce precisely the
fabricated-precision failure the Syriac review caught." It sanctioned backfilling
`discovery_channel` only "coarsely, at the block level" — meaning **from evidence** (its
worked example is IJC's own limits section stating that rows 27–35 are builder-prior-
knowledge). Here the backfill is from a heuristic, and it lands on the value that most
flatters coverage.

The consequence is not cosmetic. `discovery_channel` is the one field in the entire
apparatus whose purpose is to tell a reviewer *where to concentrate scrutiny* — doc 14's own
words: "that column *is* the fabricated-precision risk map." As populated, it points a
reviewer away from 50 rows that are in fact recall-sourced, and it will be read by any
outside reader as a coverage claim.

**Fix.** Re-stamp the 50 rows either `builder-prior-knowledge` or a new
`unrecorded-legacy` enum value, and add a gate: `discovery_channel` in
{`field-bibliography`, `database-search`, `library-catalogue`} requires a non-null
`discovery_instrument`. One migration script edit and one gate function. Then re-run the
freeze gate reports so the declarations reflect the corrected data.

---

### P0-2 — Six worlds froze against a Freeze Criterion the governing document still asserts is a gate

**Where.** `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`, Freeze Criteria,
lists among world-freeze conditions:

> "External Scholarly Review complete (Article 31 — freeze-eligibility gate)"

Against that: `Ministry/Technology/Pass2/gates/S6.2_IJC_FREEZE_DECLARATION.md` (2026-08-01,
world 6 of 6) — "**Article 31 (telos): provisional BY DESIGN** — your year-two ruling
governs; not an open item." The Syriac declaration: "**Article 31 (external scholarly
review)** — the project-lead gate; the telos rides provisional on it." ALX, HAL and PAHC
carry the same. `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md` records the
reviewer search as **open since 2026-07-08**, with two candidates explicitly ruled out.

**No scholar outside this project has read any world.** All six are frozen.

**Why it's a P0.** Not because deferring is wrong — Mark made an explicit, recorded,
defensible decision, and the freeze declarations disclose it every time. It is a P0 because
V7.4's own **Record Integrity Principle**, added in this same version, says: "When a later
document... resolves a finding recorded in an earlier document, the earlier document must be
updated with a closing cross-reference — not left to silently contradict the newer record."
The Framework is currently the earlier document contradicting the newer record, about its own
freeze criteria, and it is the document an outside reviewer would read first to find out what
"frozen" means here. A reader who reads the Freeze Criteria and then reads a freeze
declaration will conclude the project froze against its own rule. It did not; it changed the
rule and never wrote that down.

Second, on substance: doc 12 named a concrete, free, mid-development route to real outside
review — *Reviews in Digital Humanities*, which "explicitly allow[s] project directors to
seek review at any point in a project's development." Two weeks on it appears in exactly two
places in the repo: one line of `CiC_System_Redesign_Pass1_Design_2026-07-26.md` and one
line of the FAIR statement draft. `Ministry/Scholarly-Review/` holds a reviewer brief at
V0.2 DRAFT and world briefs for four of six worlds (none for Alexandria or IJC), all draft.

Compounding it: the Freeze Criteria in question sit in a document still marked "not yet
ratified" (see P1-9), while the standard that operationalizes them was adopted as governing.

**Fix.** Two moves, both cheap. (1) Amend the Freeze Criteria text to state the actual rule
in force: Article 31 review is a *post-freeze* obligation on a stated timeline, not a
freeze-eligibility gate, with the ruling cited — and ratify the document while doing it.
(2) Send one world to RDH. Desert is the right one — it is the only world with a complete rendered repository and a FAIR export, and
its relative recall is 9/10.

---

### P0-3 — In the fleet's least-verified world, ten force records carry no sources at all

**Where.** `cic-poc/backend/wrs/records/imperial_juridical_world/force/*.md` — all ten
records end `sources: []`. Every other world: ALX 18/18, DES 12/12, HAL 12/12, PAHC 14/14,
SYR 13/13 carry source links. IJC is 0/10, alone.

These are not stub records. `ijcforce1A1.md` states "Constantine's victory at the Milvian
Bridge (312) and the subsequent legal toleration of Christianity (Edict of Milan, 313)...
**Confidence: Documented**" and carries three narrative layers plus a Layer-4 elaboration.
A Documented-confidence historical claim with an empty source array is a claim the
Checkpoint rule was written to make impossible.

**Why this is worse in IJC specifically.** IJC is the world where, after an honest Round 1
recalibration, **zero of 38 registry rows carry Confidence A**; 31 carry B, defined in the
registry's own disclosed note as "checked against this build's own historical knowledge, not
independently re-verified against an accessible source this session." `discovery_channel` for
IJC is `builder-prior-knowledge` on 35 of 41 rows (85%). So the world with the thinnest
verified evidentiary base is also the only one whose forces are untraceable to it.

**Why the gate can't see it.** `CiC_World_Build_Completion_Standard_V1.0.md` §A's
`gravity`/`force` row requires "six tests recorded per candidate... `interaction[]` and
`connections[]` typed and reciprocity-checked; every force carries Layer 4." It does not
require `sources[]`. The one world that omitted them passes.

**Fix.** Add `sources[]` to the Completion Standard's force row and to the field-completion
gate; then populate IJC's ten. The registry rows exist (rows 1–3, 16, 5–7, 9–11) — this is
linking, not research.

---

### P1-1 — `verification_state` is a four-value axis with one value, fleet-wide

118 of 118 term records read `verification_state: verified-via-authority`. Not one reads
`verified-direct`, `named-not-rechecked`, or `unverified`. A field whose distribution is a
constant carries zero information, and this is the specific axis doc 12 introduced to stop
"verification recency" from hiding inside a compound grade.

The cost is concrete. IJC's registry says in prose, honestly, that nothing was re-verified
this session. PAHC's registry contains rows independently checked against publisher pages.
Both render `verified-via-authority`. The honest distinction the build actually made in
free text is erased by the structured field built to hold it — which is doc 12's own
complaint, running backwards.

**Fix.** Re-grade the 118 records against the four real values; it is a mechanical pass
because the source rows' verification notes already say which is which. Add a gate that
fails a fleet-wide single-value distribution on any enum field — that check would have
caught this in one run.

---

### P1-2 — The priority-review trigger now sits below the actual risk boundary

The Source Registry rule flags "entries resting at Confidence C or below that are intended to
support a vivid, specific claim." That threshold was set when B meant "specific work/locus
named." After IJC's Round-1 recalibration, **B means recall**: "drawn from this build's own
historical knowledge; not independently re-collated this session." IJC has 31 rows at B and
3 at C-or-below. The rule that exists to catch the fabricated-precision failure mode flags
three rows and misses the thirty-one where doc 14's own evidence says the risk actually
lives.

**Fix.** Re-key the trigger off the axes that now exist rather than off the legacy letter:
flag any row where `discovery_channel == builder-prior-knowledge` **and**
`verification_state != verified-direct` **and** it licenses a claim whose
`evidentiary_weight == load-bearing`. That is computable today from committed data.

---

### P1-3 — The record-native migration lost queryable fields the original builds had

`World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Source_Registry_FINAL_v2.xlsx` (opened
directly) has 73 rows and twelve columns including **Citation Reliability** (A 9 / B 50 /
C 12 / D 2), **Confidence Level** in the constitutional vocabulary (Documented 7 / Widely
Accepted 33 / Contested 28 / N/A 5), and **Priority Review Flag** (Yes **46** / No 27), plus
four derived sheets: By Confidence Level, By Boundary Status, By Author, and a Priority
Review Queue.

In the migrated record — `wrs/records/pahc_world/source/srcPAHCP01.md` — all three are
collapsed into a prose string:

> `verification_note: 'Registry-carried assessment fields, verbatim: confidence_level=Contested; citation_reliability=C; priority_review_flag=Yes. Notes: ...'`

Nothing is lost as *information*, and the migration is transparent about what it did. But
the record store is now the system of record ("the record store drives every world in the
fleet" — IJC freeze declaration), and three fields that were sortable, filterable, and
generating a live review queue are now a substring. Doc 12's central diagnosis was judgments
"stored in free text where the next builder has to rediscover it by reading." The fix
reproduced it. ALX, DES, HAL and PAHC carry no recoverable letter grade at all in the record
store; only SYR (in the body, `Registry confidence grade: A/B/C/D` — 28/19/5/1) and IJC
(inside the note string) do.

**Fix.** Promote `citation_reliability` (or map it onto the existing `citation_specificity`),
`formation_confidence`, and `priority_review_flag` to first-class source-row fields, parsed
back out of the notes where the migration put them. PAHC's 46 flagged rows are a real
standing review queue that currently cannot be listed.

---

### P1-4 — Doc 12's #2-rated gap (work / edition / translation) is still fully open in data

`edition`, `translation`, `consulted_as`, `edition_status` exist in the schema and are
populated **0, 0, 0 and 1 times across 270 rows**. `external_ids` is 0/270. Syriac's
`work_title` still holds the whole composite string doc 12 quoted as its exemplar problem —
e.g. `srcSYR001`: "Ephrem the Syrian, Hymns on Faith (87 hymns). Ed. Beck, CSCO 154-155
(1955). Trans. Jeffrey Wickes, CUA Press, 2015." One work, one critical edition, one
translation, one string, no field saying which was read. Syriac also carries `work_author` on
only 7 of 64 rows and `work_locus` on 11 — the fleet's largest registry is its least
structured, while ALX/DES/HAL/PAHC are at or near 100% on both.

I would not fix this on all 270 rows. Roughly 40 rows are primary texts doing real work; the
rest are modern monographs where the composite string is fine and Chicago 14.142–14.152 does
not bite. **Fix:** populate `edition`, `translation`, `consulted_as`, `edition_status` on
P-type rows only, and add Syriaca.org URIs to the Syriac P-rows — Aphrahat, Ephrem, and the
Doctrina Addai all have them, they are free, and doc 12 called this "the best
effort-to-legitimacy ratio in this document." It is still unclaimed.

---

### P1-5 — Etic categories carried in the emic register, including in a deployed prompt

Doc 13's finding was that CiC keeps making the emic/etic distinction under five improvised
names. The `register` field now exists (`records.schema.json:55`) and is applied uniformly —
terms and stories `emic`, everything else `etic`. But **`emic-unavailable` is used zero
times fleet-wide**, and the case doc 13 named as its motivating example is still mis-registered:

- `wrs/records/desert_world/term/desertlex008.md` — `term: Apophthegma (Saying)`,
  `register: emic`. Its own `plain_explanation` says: "The famous collections came later,
  made by editors after this world's own time." *Apophthegma* is the editors' Greek
  rhetorical label; the desert's own idiom for the thing is a *word* asked of an elder
  (*eipe moi rhēma*), and the Desert lexicon has no entry for it. This is the exact defect
  doc 07 traced to a voice failure and doc 13 proposed `emic-unavailable` to prevent.
- `data/imperial_juridical_world/ijc_Representative_Permanent_Prompt_Marius.txt`: "**We
  speak of ourselves as the Church of the Empire**." No fourth- or fifth-century Christian
  used that as a self-designation; it is the modern historiographical *Reichskirche*
  category, placed in the first-person plural in the deployed prompt of the last-built
  world. Same class, one level further downstream, where a participant meets it.

To be fair to the build: the IJC prompt is otherwise unusually disciplined about this — it
uses *primatus*, *communio*, *concilium*, *homoios* in-register, and it hedges the Ambrose
quotation correctly ("the words he is remembered to have spoken"). The Syriac prompt renders
the C4 gravity — "Authority-Structure Ambiguity," an unambiguously analytical construct —
into properly emic material ("You have watched a see stand empty twenty years, your teaching
received all the same"), which is exactly right. The failure is narrow and fixable, not
pervasive.

**Fix.** (a) Re-register `desertlex008` as `emic-unavailable` with the etic label named as
such, and add the attested emic term. (b) One pass over all six deployed prompts checking
every first-person self-designation against the world's own term records; anything with no
`emic` term behind it gets rewritten or dropped. (c) Add `emic-unavailable` to the Completion
Standard's term row as an expected — not exceptional — value, the way
`prior_sense: none-attested` already is.

---

### P1-6 — A manuscript-content error in a twice-reviewed FINAL document

`Doc_02_Source_Ecology.md` §2, Odes of Solomon: "British Library Add. 14538, 'Codex
Nitriensis' (Syriac, **36 of 42 odes**, c. 10th c.)."

Standard descriptions of Codex N give its contents as Odes 17:7–42:20 — that is
approximately **26** odes, not 36. (The 40-ode figure belongs to the Harris manuscript,
which Doc_02 correctly identifies as the most complete.) The tenth-century date and the
Bodmer XI / *Pistis Sophia* details around it are correct.

I flag this at Medium confidence in my own check — I have this from standard manuscript
descriptions, not from Lattke's or Charlesworth's apparatus in hand, and I would want it
verified against one of those before it is corrected. But it is exactly the profile the
Syriac Round 1 review named: "each rides on a real scholar and a real underlying source —
but that's precisely what makes them dangerous." It survived two review rounds and a
second-pass verification whose own summary said "a broader independent skim of the rest of
the document found no further instances of the earlier error pattern."

**Fix.** Verify against Lattke's Hermeneia apparatus; correct or confirm; and note in the
Doc_02 revision log that the Round-2 "no further instances" sweep was a skim, not a
re-derivation — which is the honest label for what it was.

---

### P1-7 — A contested identification stated flatly inside the section built for confidence discipline

IJC Doc_02 §7 describes Maximinus as "the same Maximinus who later debated Augustine, c.
427–428." The *Collatio cum Maximino* date is right, and the identification is the majority
scholarly position (Gryson), but it is not uncontested, and it is asserted with no
confidence marker in the one section of the document whose entire purpose is confidence
discipline about Homoian material. Nothing downstream leans on it, which is why this is P1
and not P0.

**Fix.** One clause: "identified by most scholarship, though not universally, with the
Maximinus who debated Augustine." That is the five-level vocabulary doing its job.

---

### P1-8 — No cross-check between a claim's confidence and its sources' verification state

Syriac Doc_04's Confidence/Gravity Cross-Check is a genuine strength (§2.4 above). There is
no analogue one level down. IJC has `formation_confidence: Documented` on **8 of 12** term
records while **0 of 41** IJC source rows were verified against an accessible source. Under
the Constitution's own definition ("multiple independent sources with no serious scholarly
dispute") that is defensible — Documented describes the state of the evidence, not the
builder's diligence. But the divergence is exactly what the Doc_04 cross-check exists to
make visible, and at the record level it is invisible and ungated.

**Fix.** A gate: a term at `formation_confidence: Documented` whose every licensed source
carries `verification_state != verified-direct` must carry an explicit divergence note, on
the Doc_04 cross-check's own pattern. This is a dozen lines of gate code and it would surface
the IJC pattern immediately.

---

### P1-9 — The governing method is split across two versions, and the one carrying all the fixes has never been ratified

`CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` opens with:

> "**Status: DRAFT** — pending Opus deep review and project-lead review; **not yet
> ratified.**"

V7.4 is the version that carries doc 14's entire recommendation set (the `search_record`,
the per-row discovery fields, the field-bibliography sweep, the saturation statement, the
relative-recall test, the PRESS question), the new Record Integrity Principle, the new
Fix-the-Mechanism principle, and the Freeze Criteria that P0-2 turns on. It is cited as
governing by three worlds' Doc_02s (PAHC, Syriac, IJC) while three others (Alexandria,
Desert, Hieronymian) cite **V7.3**. Meanwhile `CiC_World_Build_Completion_Standard_V1.0.md`
was adopted as **GOVERNING** on 2026-07-27 and states that "the machine gates
(`cic-poc/backend/wrs/gates/`) cite this document as the requirements source" — i.e. a
ratified standard now depends on an unratified framework.

This is the mechanical explanation for a good deal of the cross-world unevenness catalogued
in P2-7 and P2-8: three worlds were built to a method that did not yet require the fields
the other three carry. It is not a rigor failure so much as an unfinished bookkeeping state
— but it means that "governed by the Construction Framework" currently names two different
documents depending on which world you open, and neither is unambiguously in force.

**Fix.** Ratify V7.4 (folding in P0-2's Freeze Criteria correction in the same pass), and
add one line to each V7.3-built world's Doc_02 header stating which V7.4 requirements it
predates and where they were retro-satisfied — which for the source rows is already true
(the migration-time sweeps and search records), just not stated in the world's own document.

---

### P2 items

- **P2-1.** Keser-Kayaalp, "The Cathedral Complex at Nisibis," *Anatolian Studies* 63 (2013)
  is co-authored with Nihat Erdoğan. Syriac Doc_02 §6 and the registry row cite Kayaalp
  alone. Minor, but this project checks author identity carefully elsewhere.
- **P2-2.** Syriac Doc_02 §2: "the name 'Aphrahat' appears only from the tenth century
  onward (Bar Bahlul, Elias of Nisibis)." Bar Bahlul is tenth-century; Elias of Nisibis
  (975–1046) is an eleventh-century witness. "Onward" technically covers it; the pairing
  reads as though both are tenth-century.
- **P2-3.** HAL Doc_02 §2.2's honest open flag on Palladius can be closed: the passage on
  Paula being hindered by Jerome is *Historia Lausiaca* 41. One lookup closes a flag the
  document correctly refused to write around.
- **P2-4.** IJC Doc_02 §9 open item 1 (Susan Wessel's monograph title, Confidence C, flagged
  2026-07-20) rode through freeze on 2026-08-01 as a standing limit. The title in the
  registry's own "working recollection" is correct: *Leo the Great and the Spiritual
  Rebuilding of a Universal Rome* (Brill, Supplements to VC 93, 2008). A single lookup has
  been outstanding for twelve days across a freeze. The flag system works; the closing loop
  is slow on the cheapest items.
- **P2-5.** The disclaimer "Simulated review — informational only, not an Article 31
  substitute" appears in ALX, IJC, SYR and PAHC review artifacts and **not** in
  Desert-Monasticism's or Hieronymian's. Since freeze declarations rest on those reviews,
  the disclaimer should be uniform.
- **P2-6.** Confidence-vocabulary density across the six Doc_02s varies about fivefold:
  PAHC 69 uses in 241 lines, ALX 54/258, DES 46/214, HAL 44/176, SYR 16/199, IJC 12/139.
  SYR and IJC concentrate the vocabulary into a single Confidence Map section and hedge in
  ordinary prose elsewhere — good writing, but it means most individual claims in those two
  documents carry no machine-readable or reader-visible level.
- **P2-7.** `genre_form` (doc 12 gap #7, rated High) is populated in ALX 26/37, SYR 33/64,
  DES 17/26, HAL 14/26, and **0/76 in PAHC and 0/41 in IJC**. `transmission_path` is
  populated in ALX (14) and DES (8) and **zero times in the other four**, though doc 12
  rated it Medium and V7.4 makes Transmission History a required fifth Author-Gravity
  dimension. `script` is populated everywhere except IJC (0/41).
- **P2-8.** Language codes are not standardized: ALX/DES/SYR use ISO 639-3 (`eng`, `lat`,
  `fra`), PAHC/IJC use ISO 639-1 (`en`, `la`, `fr`), HAL mixes both. A `language=eng` filter
  over the FAIR export misses 60 rows. And **PAHC carries `script: Latn` on all 16 of its
  `grc` rows** — the Didache, 1 Clement, Polycarp, the Abercius inscription and the
  Alexamenos graffito are all recorded as written in Latin script. This is P2 today and
  becomes P0 the day `sources.json` ships publicly, because it is the first thing a
  cataloguer notices and it is free to fix.

---

## 4. Now vs. over time

### This week (all mechanical, none requiring research)

1. **Re-stamp the 50 mis-labelled `discovery_channel` rows** and add the
   instrument-required gate (P0-1). This one is genuinely urgent because it is actively
   misleading.
2. **Reconcile the Freeze Criteria text with the Article-31 ruling, and ratify V7.4 in the
   same pass** (P0-2 half 1, P1-9) — one paragraph plus a status-line change, under V7.4's
   own Record Integrity Principle. Six frozen worlds are currently governed by an unratified
   draft.
3. **Link IJC's ten force records to their registry rows; add `sources[]` to the Completion
   Standard's force row and to the gate** (P0-3).
4. **Normalize language codes to ISO 639-3 and fix the 16 `grc`/`Latn` rows** (P2-8), with
   a gate for language/script agreement.
5. **Close the four one-lookup items:** Wessel's title, Palladius *HL* 41, Keser-Kayaalp's
   co-author, the Codex N ode count (P1-6, P2-1, P2-3, P2-4).

### This month

6. **Make `verification_state` real** — re-grade 118 term records against the four values,
   and add a single-value-distribution gate that would have caught it (P1-1).
7. **Re-key the priority-review trigger** off `discovery_channel` + `verification_state` +
   `evidentiary_weight` instead of the legacy letter grade (P1-2).
8. **Restore Citation Reliability / Confidence Level / Priority Review Flag as fields**,
   parsed back out of the migration's own note strings; PAHC's 46-row review queue is
   currently unlistable (P1-3).
9. **Add the Documented-vs-unverified-sources gate** (P1-8).
10. **Run one real field-bibliography sweep, on two worlds only.** Syriac against Brock's
    *Syriac Studies: A Classified Bibliography* and its *Parole de l'Orient* continuations
    via syri.ac (free), Desert against BIBP (free). Not the whole fleet — two worlds, then
    look at what turns up and decide whether it was worth it. Every world's saturation
    statement currently declares these unaccessed; two sweeps convert a standing limit into
    evidence either way.
11. **Emic audit of the six deployed prompts** and first use of `emic-unavailable` (P1-5).

### Over time

12. `edition` / `translation` / `consulted_as` / `edition_status` on the ~40 P-type rows that
    actually bear weight — not all 270 (P1-4).
13. Syriaca.org `external_ids` on the Syriac P-rows; free, and it puts CiC into the same
    identifier graph as the field's own reference works (P1-4).
14. Publish the Conformance and Deviation Statement, currently DRAFT since 2026-07-27. It is
    the cheapest legitimacy item in doc 12 and it is written.
15. **Get one outside reader.** See below.

---

## 5. Bottom line, in the professor's own voice

**"I like it, with two specific caveats — and I'd want one thing before I put my own name
near it."**

I have read a fair number of digital-humanities projects that describe themselves as
rigorous. Most of them mean that the people who built them were careful. This one means
something harder: that the carefulness is written down as rules, checked by other passes,
and recorded when it fails. I checked roughly sixty specific bibliographic and historical
claims across four worlds — CSCO volume numbers, letter numbers, conciliar canons, edition
dates, manuscript sigla, the Fourth Sirmian formula's exact date, a Georgian translation
transmitted under Hippolytus's name — and found **one likely error** (the Odes of Solomon
manuscript count) and two things I'd want stated more carefully. That is a better hit rate
than I get from a well-supervised dissertation chapter. Whatever process produced the Ephrem
edition table and the Aphrahat transmission history was in contact with real bibliography,
not paraphrasing an encyclopedia.

More impressive than the accuracy is the failure record. A build that lets a gravity keep a
**failing** Formation test on the page because the honest answer is a fail; that removes a
vivid claim from a Primary gravity's evidence base because its attestation is a century and a
half too late; that refuses to cite Palladius until someone finds the chapter; that catches
its own draft claiming independent evidence and admitting in the same breath that none was
found; that recentres Homoian Christianity as *the imperial church for two decades* rather
than a defeated heresy — that is a project doing the thing history departments say they
teach. The five-level confidence vocabulary with prohibited words, the affirmative duty to
name whose voice is missing, and the flat prohibition on invented illustrative narrative are
better commitments than most published popular history operates under.

**Caveat one is the honest one, and it is about provenance, not accuracy.** Fifty source rows
currently tell a reader they were found in a field bibliography when the same world's own
search record says no field bibliography was ever opened. Nobody lied; a migration script
guessed, on a type rule, and guessed generously. But provenance is the one field where a
guess is worse than a blank, because the whole point of it is to tell me where to look
harder. Fix that before anyone outside sees it.

**Caveat two is about consistency, and it is the answer to the question I was actually
asked.** The same standard is *specified* everywhere and *applied* at visibly different
depths. Hieronymian and Post-Apostolic will take a hard look. Imperial-Juridical will not:
zero of thirty-eight rows verified against an accessible source, eighty-five percent of them
from the builder's own recall, ten force records with no sources at all — and it is the world
whose subject matter (Constantine, primacy, church and empire) is the most freighted and the
most likely to be pressed by a real participant. The build knows this and says so in plain
language in its own registry notes, which is why I call it a caveat and not a disqualification.
But if I were assigning worlds to students, I would send them to Bethlehem and Rome-the-
house-churches and tell them to treat the imperial world as a first draft.

**And the thing I'd want before I put my own name near it: one real outside reader.** Not
another internal pass. The internal passes are already good — nine rounds on one Doc_02,
adversarial reviewers with no drafting context, a standing rule against self-certified
dismissals, a relative-recall score computed for every world with the misses named. What
they cannot do is the one thing they have never done: put a specialist in front of a world.
Every finding in this document, including mine, was findable from inside the project. The
class of error that survives an apparatus like this is precisely the class only a person who
has spent twenty years in the Syriac or Late Antique field notices in the first ten minutes —
a framing that quietly assumes a settled position, a scholar cited for something adjacent to
what they actually argued, a strand that is a modern construct wearing a fourth-century
name. The Framework already calls external scholarly review a freeze-eligibility gate. Six
worlds are frozen and the reviewer search has been open since 8 July.

**The single biggest lever is closing that gate — and the cheapest version costs a week.**
Doc 12 already found the door: *Reviews in Digital Humanities* takes projects mid-development,
publishes signed reviews, and evaluates against the AHA and MLA guidelines. Send Desert. It
is the only world with a complete rendered repository, a FAIR export, and a 9/10 relative
recall, and its one named coverage gap (Cassian) is a gap a reviewer would respect for having
been named. One outside reader would do more for this project's trustworthiness than the next
five internal rounds combined — and, on this evidence, the project would survive it in good
shape.

---

## 6. Confidence on my own checks — read before quoting me

Same discipline docs 12–14 apply to themselves.

**High confidence** (I know this material directly and would defend the check): all CSCO
volume/year pairings for Beck, Tonneau and Leloir; Parisot *PS* I/1–2; Gwynn's eight
Demonstrations in NPNF2.13; Aphrahat's 336/7 – 344 – Aug 345 composition scheme and the
alphabetic acrostic; the Georgian-from-Armenian Demonstration 6 under Hippolytus's name and
the separate Antonelli 1756 Armenian version; Jerome's Epp. 22/46/77/107/108/127 with dates
and addressees; the Vulgate's two phases; Kelly vs. Rebenich on Jerome's birth; Julius I in
*Apol. c. Ar.* 21–35; Leo Ep. 28; CTh 16.1.2 and Title 16.8's rubric; the Dated Creed of
22 May 359 with Rimini/Seleucia and Constantinople 360; Constantius II 353–361 and Valens
364–378; Eusebius's letter to Caesarea; Theodoret 451/553; Jerome *DVI* 115 on Ephrem the
deacon; Jacob of Serugh c. 451/2–521; the Chronicle of Edessa in Vat. sir. 163 on the 201
flood; the School of Nisibis at c. 489–496; Gushtazad and Simeon bar Sabba'e's refusal of
the double tax.

**Medium confidence — verify before acting:** the Odes of Solomon Codex N ode count (P1-6);
the Keser-Kayaalp co-authorship (P2-1); the Maximinus identification's contested status
(P1-7); BL Add. 17182's second part as 510 vs. 511 (Syriac Doc_02 §3 says 510; I have seen
511 in Wright's catalogue tradition and did not resolve it, so I have **not** raised it as a
finding).

**Do not cite me for:** any claim about the `.xlsx` registries other than PAHC's — I opened
only that one and the other 22 workbooks are unexamined; any claim about the Alexandria or
Desert Doc_04s, which I read only in summary; any claim about retrieval, runtime, safety, or
participant experience, which are other reviewers' angles and which I did not touch.

**Internal do-not-cite, and it matters:** the five Desert rows labelled
`discovery_channel: field-bibliography` **do** name real instruments and are not part of
P0-1. Only the 50 instrument-less rows in Syriac, Alexandria and Hieronymian are.

---

## 7. Sources read

**Prior audits (in full):** `CiC_Redesign_Research_2026-07-25/` docs 00, 06, 12, 13, 14.
**Standing:** `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`;
`CiC_System_Hub_Decision_Log.md` (2026-07-26/27 entries);
`Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md` (Article 31 entries).
**Governing method:** `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`
(full text extracted and read); `L3B-World-Build-Methodology/Source_Registry_Template.md`;
`Ministry/Technology/CiC_World_Build_Completion_Standard_V1.0.md`;
`Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_0.md`.
**Syriac:** `Doc_02_Source_Ecology.md`, `Doc_04_Gravity_Discovery.md`,
`syr_Representative_Permanent_Prompt_Yausep.txt`, `syr_World_Capsule_Core.md`,
`Review-Artifacts/` (index + selected rounds), `data/syriac_world/source_registry.json`.
**Imperial-Juridical:** `Doc_02_Source_Ecology.md`, `Doc_04_Gravity_Discovery.md`,
`Source_Registry.md`, `ijc_Representative_Permanent_Prompt_Marius.txt`.
**Spot-checked:** PAHC `CiC_W1_Doc02_Source_Ecology_FINAL.md` and
`CiC_W1_Source_Registry_FINAL_v2.xlsx` (opened); Alexandria `Doc_02_Source_Ecology.md`;
Desert `CiC_W3_Doc02_Source_Ecology.md` and `Doc_02_Review_Round1.md`; Hieronymian
`hal_Doc_02_Source_Ecology.md`.
**Record store:** `cic-poc/backend/wrs/` — `schema/records.schema.json`, all 739 records
across seven record sets, `migrate/s62_{syr,alx,hal,pahc,ijc}_*.py`, `views/level3.py`,
`views/plain_explanation.py`, `gates/core.py`, `data/desert_world/{sources,repository}.json`.
**Build record:** `Ministry/Technology/Pass2/` — `BUILD_STATE.md`, `reviews/S2.1b_coverage_check.md`,
`reviews/S6.2_{ALX,SYR,HAL,PAHC,IJC}_s21b_coverage.md`, `gates/S6.2_*_FREEZE_DECLARATION.md`,
`drafts/CiC_FAIR_Conformance_and_Deviation_Statement_DRAFT_2026-07-27.md`.
