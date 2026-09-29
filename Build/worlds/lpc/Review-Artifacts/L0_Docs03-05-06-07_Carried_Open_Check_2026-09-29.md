Simulated review — informational only, not an Article 31 substitute.

# `lpc` Phase L0 — independent check of Docs 03, 05, 06 and 07: carried-open findings, the lens spine, and source fidelity

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Drafter model note:** the pre-V2.0 Decision Log does not record a drafter model per document; the value above is the routing the project rules gave these four steps. It is stated, not verified.
- **Reviewer agent:** independent Phase L0 reviewer subagent, fresh context, session_01EgyL7xtErqj72CaFiEUx4q
- **Drafter agent:** pre-V2.0 `lpc` build thread (drafting and fix passes of 2026-09-09 to 2026-09-16)
- **Round:** 1
- **Truncation check, method 1:** end-of-file inspection. `tail -c 120` on Doc_03, Doc_05, Doc_06, Doc_07 and `Open_Gaps_Tracking.md`; each ends on a complete sentence and a newline, inside its own last section.
- **Truncation check, method 2:** byte and structure comparison. `wc -c` on disk equals `git cat-file -s HEAD:<path>` for all five (64109, 101813, 32535, 46192, 114540), and each Doc's last H2 is its `## Disposition` section (lines 90, 405, 160, 270).
- **Date:** 2026-09-29
- **Scope:** Doc_03, Doc_05, Doc_06, Doc_07 (with the 19 `Lexicon-Chunks/` and `Lexicon_Deployment_Index.md` as Doc_06 co-outputs); `Doc03_Round1–2`, `Doc05_Round1–2`, `Doc06_Round1–3`, `Doc07_Round1–2`; `Open_Gaps_Tracking.md`; `lpc_Decision_Log.md` (grepped); `build/lpc_Rebaseline_Declaration.md`.
- **Severity vocabulary:** P0 blocks; P1 materially wrong or misleading, fix before freeze; P2 polish or record hygiene.
- **This is not a revision cycle.** Nothing was edited except this file. No round counter is consumed: the file name matches no `Doc_0N_…Round_N` pattern in `engine/m10/rounds.py`.

---

## Verdict

**0 P0 · 8 P1 · 6 P2.** Proceed with Phase L0. Nothing here blocks the next step. Two P1s touch deployable records (`lpc.term.libelli`, `lpc.term.libellatici-sacrificati`) and must be fixed before freeze.

**The brief's premise did not survive checking.** The brief, and `build/lpc_Rebaseline_Declaration.md`, say Doc_07 "was never built on the seven-dimension lens spine." It was. Doc_07 §2A–§2G are Smart's seven, in Smart's order, and §2H–§2I are the two CiC additions, named as additions. `Doc07_Round1_Review.md` confirmed this at the time. **The document that is not on the spine is Doc_05.** The error is traced to its root in P1-1.

---

## Method

- Read in full: `CLAUDE.md`, the Adversarial Review Standard Practice, Completion Standard V1.4 (and §F of the archived V1.3), `engine/m10/reviewfile.py`, `engine/m10/rounds.py`, `Pass2-decisions/M4_lens_spine.md`, Build Process V2.0's Step 3–10 table, and CF V7.4 Part VII Steps 5–7 (extracted from the docx, lines 655–690).
- Read in full: Doc_06, Doc_07, `lpclex017`, `lpclex019`. Read by section: Doc_03 (header, Notes, Disposition), Doc_05 (§0, §3, §6.5, §11, Log, Disposition).
- Each prior round's findings were listed from its headings. Each one's state was then checked in the current file, not taken from the fix pass's own account.
- Source checks ran against `cic/texts/` by structural marker, never by line position. `div1`/`div2`/`div3` `title=` spans were used for anf05, npnf101, npnf104 and npnf105; `<note>` spans were removed before tag-stripping. Hartel CSEL 3 was checked by its `Epistulae` page headers, and Possidius by chapter heading.
- `tools/check_live_commentary.py --surface worlds` was run for the commentary counts.

**Quotations re-verified verbatim (all IN-TEXT, outside `<note>`):**
- Doc_07: *"it is the shepherd that is chiefly wounded in the wound of his flock"*; *"I wail with the wailing, I weep with the weeping"*; *"ancient venom"*; *"your suffrage and God's judgment"*; *"concerning five schismatic presbyters"*; *"judging no man, nor rejecting any one from the right of communion…"* (div2 *The Seventh Council of Carthage*); Letter CXXVI's *"the more venerable and aged men who had come up to me in the apse"*, *"gathered in front of the steps"* and *"returned to my own seat"*; *On Baptism*'s *"are often corrected by those which follow them…"*; Possidius ch. VIII *"under compulsion and constraint"* (hyphenated across a line in the vendored text).
- `lpclex019`: all eight Cyprian quotations. *"thousands of certificates were daily given, contrary to the law of the Gospel"* sits in div3 *Epistle XIV*. The withdrawn variant *"…were given, against the Gospel law"* is NOTE-ONLY, which confirms the chunk's own correction.
- Counts reproduced: *certificate(s)* 42 in the Cyprian `div1`, 38 outside `<note>`, as stated.

---

## (1) Carried-open findings, per document, as the files on disk stand

"Ledger" means Open_Gaps_Tracking (OGT) plus the Decision Log (DL). Where disk and ledger disagree, disk governs, and the disagreement is noted.

### Doc_03 — Lexicon Candidate List (2 saved rounds)

| Carried item | State on disk | Ledger |
|---|---|---|
| Round 1 (22) and Round 2 (31) findings | Disposition says all fixed. No later review contradicts it. | Consistent |
| Revision 3 and 4 re-reviews never saved as files | **Open, and it cannot be cured afterwards.** Disclosed in the Disposition. | OGT build log discloses it |
| Governance: Part II tags at candidate stage; [CT] without a Contest Type | Portfolio question **open**. The CT half is discharged in substance by Doc_06 §3. | **Not in OGT** |
| Manichaean *Elect*/*Hearers* discovery gap | **Open** | **Not in OGT** |
| Epidemic/mortality vocabulary (absence finding) | **Open**, stated as a finding | **Not in OGT** |
| Rows 1, 19, 21 unswept; the diminishing-returns point not reached | **Open.** Since overtaken: Doc_06 §2.4 added *certificates*, and the 2026-09-19 liturgical reads propose further candidates (*exomologesis*/public confession; the baptismal interrogation). None has entered the lexicon. | **Not in OGT** |
| Matching rule unstated (Doc_05 §11.14; Doc_06 §5.5) | **Open.** Flagged, not edited. See P2-3. | Not in OGT |
| Discovery-method finding (Doc_06 §5.7) | **Open.** Goes to Mark. | Not in OGT |
| *libellatici*/*sacrificati* "correct source (row 8, not row 2)" | **Wrong.** See P1-5. | — |

### Doc_05 — Ecological Reconstruction (2 rounds; one left under the cap)

| Carried item | State on disk | Ledger |
|---|---|---|
| Round 1 (8 findings) | **Fixed.** Round 2 confirmed all eight. | Consistent |
| Round 2 N1–N6 | **All fixed on disk**, checked one by one. N1: the six-site table at §11.15. N2: the §0.7 forces row now names §6.3/§6.5/§6.8. N3: the "markup-stripped" rule and the 114 figure are at §4. N4: "four specific ways". N5: "Preface", with c. 580–662 and no century claim. N6: the attribution has its own subject, and the list numbering is intact. | **Document Log omits Round 2 and its fix pass. The Disposition says only "Round 2 run", with no verdict.** See P2-1. |
| §11.1 the 411 *Gesta* "no owner, no criterion" | Text is stale | **OGT OG-4: closed** by project-lead decision (no third read) |
| §11.2 Doc_04 Open Item 8 | **Open** | Doc_04's own L0 check |
| §11.3 Doc_04 Rounds 5–11 | **Open** | Doc_04's own L0 check |
| §11.4 Augustine-phase confessors | Closed (answered in the negative) | Consistent |
| §11.5 anti-Manichaean candidate | **Open** | Not in OGT |
| §11.6 Article 20 secondary prong | Discharged, **conditional on §11.13** | — |
| §11.7 liturgical material never read as liturgical evidence | **Done 2026-09-19** (`Liturgical_Evidence_Read_Cyprian/Augustine_2026-09-19.md`). Doc_05 §3 was written under the old limit and has not been updated. | OGT mentions the reads only under Phase Seven |
| §11.8 no site report or inscription verified | **Open** (honest limit) | — |
| §11.9 Story Inventory not started | Stale. **Closed by Doc_09.** | — |
| §11.10 Possidius | Closed | Consistent |
| §11.11 corpus-wide editorial apparatus | **Open.** Portfolio item. | DL; OG-9 lists it under Doc_08 |
| §11.12 rural and Punic/Berber substrate | **Open** (honest limit) | — |
| §11.13 Article 20 applied to personal correspondence, "for the project lead to confirm or reject" | **Open. No ruling found in the DL.** | **Not in OGT** |
| §11.14 Doc_03 matching rule | **Open** | Not in OGT |
| §11.15 Boundary Structures | Ruled for `lpc`. The inconsistency inside the L3 files is **open** (portfolio). | OG-9 |

### Doc_06 — Full Lexicon, 19 chunks and index (3 rounds: **at the cap**)

| Carried item | State on disk | Ledger |
|---|---|---|
| Round 1 (8) | Fixed, except H3, which was fixed wrongly. That became R2 H-N1, which R3 then found partly fixed. | — |
| R2 **M-N3**: `lpclex017`/`018` cite nothing for their new sections; `lpclex017` denies an attestation the deliverable itself proves | **Open, and worse than R2 knew.** See P1-5. The claim has propagated into two term records. | Doc_06 Disposition; **not in OGT** |
| R2 **L-N2**: review-round narration in chunks and the index | **Partial.** The 2026-09-26 commentary pass cleaned most of the chunks. Residue remains: `lpclex012` ("across all nine of Doc_01's review rounds"), `lpclex016`, and `lpclex019`'s correction paragraph. The index header and §2–§7 still narrate Rounds 1–3. | Not in OGT |
| R2 **L-N3**: zero-Tier-3 premise | **Open.** The conclusion survives. | Index §2 records it |
| R2 **L-N4**: discovery-method item filed nowhere | **Fixed.** The escalation assessment now files it. | — |
| R2 **C-N1**: two recapitalised quotations in `lpclex019` | **Open.** `lpclex019`'s World Meaning still begins *"Designate by name…"*; the source reads "designate". | Not in OGT |
| R2 "noted": *suffrage* carries no [DR] | **Open.** Recorded in index §3 prose. | Not in OGT |
| R3 (12 findings; the log says "all applied") | H-R1 **fixed**: the ambiguous-alias cell is present. M-R2 **partial**: §5 item 7 still gives the bare "42 times". L-R2 **kept "deliberately"**: the correction notice sits in `lpclex019` Key Sources, and its Final Assembly line calls it a "bracketed block" though no brackets remain. The rest were not re-derived here. **The claim that the index was regenerated by script cannot be re-run.** See P1-6. | DL says all applied |
| §5.3 liturgical term | The read is done and has proposed candidates. **Not integrated.** | Not in OGT |
| §5.4 Registry returned to review | **Open** (the Registry's own L0 check) | Rebaseline Declaration |
| §5.5, §5.7 | **Open.** Go to Mark. | Not in OGT |
| §5.6 editorial apparatus (7 local instances) | **Open.** Portfolio item. | OG-9 |
| §5.8 Key Texts / Key Sources | **Open.** Portfolio item. | OG-9 |

### Doc_07 — Integrated Ecology Analysis (2 rounds; one left under the cap)

| Carried item | State on disk | Ledger |
|---|---|---|
| Round 1 (5) | **Fixed** (R2 confirmed all five) | Consistent |
| R2 NEW-H1, M1, M2, M3, M4, L1, L3, L6, C1, C3 | **Fixed** | — |
| R2 **NEW-L2** (§2E "the wider one holds even where the primacy question is not live…") | **Not fixed.** The clause is verbatim at §2E. | **Doc_07 log: "All applied"; DL: "fourteen new findings applied"** (stale) |
| R2 **NEW-L4** (*ad nostra subsellia* printed from an NPNF `<note>`) | **Not fixed.** Confirmed NOTE-ONLY in npnf101. | The DL itself calls it "carried", which contradicts its own "fourteen applied" |
| R2 **NEW-L5** (§7 lacks "What external scholarly review should focus on") | **Not fixed.** The phrase is absent. | Stale |
| R2 **NEW-C2** ("two recalled-from-field-knowledge rows"; item 3 flags four) | **Not fixed** | Stale |
| §8.1–3 handoffs to Doc_08 | Consumed (Doc_08 exists) | — |
| §8.4 upstream portfolio items | **Open** | OG-9 |
| §8.5 **the L4 template's** pre-M4 structure | **Open**, against the *template*, not against Doc_07 | **OG-9 and the Rebaseline Declaration misstate it.** See P1-1. |
| §8.6 *Gesta* / Open Item 8 | *Gesta*: stale (**OG-4 closed**). OI 8: **open** | — |
| §8.8 liturgical read | Stale. **Done 2026-09-19.** | — |
| §8.9 "no Open_Gaps_Tracking.md" | Stale. **The file exists.** | — |
| §8.10 condensing pass on §2 | **Open** | Not in OGT |

---

## (2) The lens spine against Completion Standard V1.4 §F

**What §F requires.** All seven of Smart's dimensions are asked, and each one's yield is stated as a finding. Material Culture is required. An ethical/legal lens is required. Boundary Structures and Formation Logic are named as CiC additions. Dimension naming is settled per document. **"Doc_05 and Doc_07 carry this spine."** That last sentence is new in V1.4: V1.3 §F named no documents. Build Process V2.0's Step 5 and Step 7 rows say the same.

### Doc_07: on the spine. What is missing is small.

| §F element | Doc_07 |
|---|---|
| Ritual/practical | §2A ✓ |
| Experiential/emotional | §2B ✓ |
| Narrative/mythic | §2C ✓. Yield "very little", stated as a finding. |
| Doctrinal/philosophical | §2D ✓ |
| Ethical/legal (required) | §2E ✓ |
| Social/institutional | §2F ✓. Contains an error: see P1-3. |
| Material (required) | §2G ✓. Thin on archaeology and document-borne, stated as a finding. |
| Additions named as additions | §2H, §2I ✓ |
| Per-dimension yield | Each lens opens "What this lens reveals…". Thin yields are restated at §7 ✓ |
| Dimension naming settled | **Implicit only.** Smart's names are used without a stated choice. (P2) |
| Governing citation | Cites **V1.3** §F, which is archived. The world now builds to V1.4. (P2) |

**What closing Doc_07 needs.** No rebuild. One targeted Sonnet fix pass, well under two hours of editing:
- P1-3 (§2F).
- The four R2 residuals (NEW-L2, L4, L5, C2).
- The stale §7/§8 items: *Gesta*, liturgical read, OGT.
- The V1.4 citation, plus one sentence settling dimension naming.
- The §1/§8.10 length figures.
- Clearing its 4 REWRITE/ROUTE commentary lines, as `CLAUDE.md` requires of any PR that edits a live file.

Then one targeted Opus recheck. That is round 3, the last under the cap. The optional `world_core.integrative_observation` field is not populated in `records/lpc/world_core/`. Carrying §6 there is a cheap V2.0 step, but not a freeze requirement.

### Doc_05: not on the spine. This is the real gap.

Doc_05's coverage map (§0.7) follows **CF V7.4 Part VII's Step 5 activity list**: Human, Community, Worship, Organizational and Ministry ecologies, plus eleven named dimensions. It does not follow Smart's seven.

| Smart dimension | Doc_05 |
|---|---|
| Ritual/practical | ≈ §3 Worship Ecology (not named as the Smart dimension) |
| Experiential/emotional | ≈ §6.5 |
| Social/institutional | ≈ §2 and §4 |
| Doctrinal/philosophical | partly in §6.7 and §6.1. **Not asked as a dimension.** |
| Narrative/mythic | **Not asked** |
| Ethical/legal (required) | **Not asked.** Penitential discipline is treated as practice, and coercion under §6.8 as power. |
| Material (required) | **Not asked as a dimension.** The site-report limit appears only as a limit on §3 and §6.9. |
| Per-dimension yield | Absent for the four not asked |

**Why this happened, and why it goes to Mark.** CF V7.4 places the spine at **Step 7 only** (docx text, Step 7 Activities). Its Step 5 text lists the older dimensions, and Doc_05 followed that faithfully. Completion Standard V1.4 §F then extends the spine to Doc_05. The Standard's precedence clause governs how a freeze is *tested*. It does not say whether a build-step document drafted to CF V7.4 must be rebuilt. **The governing texts diverge, and that is a methodology question.** `rounds.py` also leaves Doc_05 exactly one review round.

**Options for closing it (for Mark):**
- **(A) Ruling or waiver.** Doc_07's spine serves both documents for `lpc`. Zero drafting. §A requires an owning finding (this one) and Mark's approval.
- **(B) Spine pass on Doc_05.** Add three short sections (Narrative/mythic, Ethical/legal, Material, about 300–500 words each, with yield as a finding) and map Doctrinal. Reuse Doc_07 §2C/§2E/§2G evidence and the 2026-09-19 liturgical reads. About 1,500–2,000 words of Sonnet drafting and one Opus round, the last one available.
- **(C) Crosswalk only (recommended).** Add a Smart-seven table beside Doc_05 §0.7. It maps each dimension to the Doc_05 section that answers it, or to the Doc_07 §2x that carries it, with the yield in one line. About 300 words and a targeted recheck. The spine is then genuinely *asked* in Doc_05 at a cost proportionate to a document already Approved to proceed.

Separately, CF V7.4 Step 5 against Completion Standard §F is a Change Order candidate at portfolio level. It will recur in every world.

---

## (3) Findings

### P1-1 — The ledger says Doc_07 is off the spine. It is not, and the error has spread into the L0 plan.

- **Sites:** `Open_Gaps_Tracking.md` Doc_07 build-log bullet ("no comparable escalation or rebuild is recorded for lpc's own Doc_07 — it remains blocked…"); OG-9 ("it was drafted and disposed on the older structure"); `build/lpc_Rebaseline_Declaration.md` ("Doc_07 was never built on the seven-dimension lens spine").
- **Evidence:** Doc_07 §1 (its lens-structure note) and §2A–§2I. `Doc07_Round1_Review.md`: "all seven Smart dimensions are present and substantively treated".
- **Root cause:** the DL's 2026-09-15 joint-disposition entry lists "the World Profile / Doc_07 **template's** pre-M4 lens structure (Doc_07)". That is Doc_07 §8 item 5, a defect in the L4 template. OGT read it as a defect in Doc_07 itself.
- **Fix:** append a correcting OGT entry (entries are append-only) and correct the Declaration's L0 line. Record the real gap as Doc_05's (P1-2). Do not rebuild Doc_07.

### P1-2 — Doc_05 does not carry the M4 lens spine that V1.4 §F requires of it.

As set out in (2). The Ethical/legal and Material lenses are required, and neither is asked. This goes to Mark as a methodology question, with options A, B and C above.

### P1-3 — Doc_07 §2F calls ordinary presbyteral work "essentially unattested". A source Doc_07 says it read in full contradicts that.

- **Site:** §2F: "the ordinary, non-factional work of a presbyter in this world is essentially unattested".
- **Source:** Possidius, *Vita* ch. V (`possidius_vita-augustini_weiskotten1919.txt`, the English immediately before the "CHAPTER VI" heading): Valerius gave his presbyter the right to preach in his presence, and "some other presbyters by permission of their bishops began to preach to the people in their presence." The Latin is at *Caput V*'s close: *"accepta ab episcopis potestate, presbyteri nonnulli coram episcopis populis tractare coeperunt."* Augustine's own presbyterate (391–395/396) is the same kind of evidence.
- **Context:** Doc_07 §2C states the *Vita* "has been read in full". `lpc_World_Profile.md` already carries the correction ("Possidius chapter V is the counter-instance… The distortion is real for Cyprian's phase; it is not a blanket silence"). Doc_07 is now stale against a later, approved document.
- **Fix:** restrict the claim to Cyprian's phase and cite *Vita* ch. V for Augustine's.

### P1-4 — Doc_07's own record, and the DL, say every Round 2 finding was applied. Four were not.

NEW-L2, NEW-L4, NEW-L5 and NEW-C2 are unchanged on disk (see the Doc_07 table in (1)). The Document Log says "All applied" and the DL says "fourteen new findings applied". The DL entry also calls NEW-L4 "carried", which contradicts its own count. A record that overstates what was fixed is exactly the kind of claim the next round trusts.

### P1-5 — Two lexicon entries, Doc_06 §2.3 and two term records deny attestation that the vendored Native primary text carries.

- **Sites:**
  - Doc_06 §2.3: *libellatici/sacrificati* "reaches this record as the vendored edition's own 19th-century editorial endnote on a different, Confidence-C text".
  - `lpclex017` Key Sources: "on Doc_01's gloss rather than on attestation in this world's own primary text".
  - `lpclex018`, same framing.
  - `records/lpc/term/lpc.term.libelli.md` and `lpc.term.libellatici-sacrificati.md`: `formation_confidence: Inferential-Thin`, a `divergence_note`, and the spoken `senses.evidential` field, which repeats the claim.
  - Doc_03's "correct source (row 8, not row 2)".
- **Source, English:** ANF Epistle LI (div3 `title="To Antonianus About Cornelius and Novatian."`) carries both classes in Cyprian's own words: *"those who receive certificates are to be put on a par with those who have sacrificed"*, *"the receivers of certificates should in the meantime be admitted, that those who had sacrificed should be assisted at death"*, and the certificate-buyer's *"I pay a price for this purpose…"*.
- **Source, Latin:** Hartel CSEL 3 (Registry row 39, Native, vendored 2026-09-05/08, before Doc_03 and Doc_06 were drafted), at the *Epistulae LV. 11–14* page header: *"libellaticos cum sacrificatis aequari"*, and *"examinatis causis singulorum libellaticos interim admitti, sacrificatis in exitu subueniri"*. *"libello a martyribus accepto"* occurs four times elsewhere in the letters. The `libell-` family occurs about 50 times in the file, and some of those mean "little book".
- **What holds:** the narrow claim that the *Latin headword* is absent from the vendored *English* corpus. What does not hold is every wider sentence built on it.
- **Why P1:** this under-claims rather than fabricates. But it sets a Documented mechanism to Inferential-Thin in two deployable records. It also puts build vocabulary ("Doc_01's own gloss", "our vendored English corpus") into a spoken field, which the file-discipline read at freeze will catch.
- **Fix:** do it at the record layer and then in the chunks. Cite row 1 (Ep. LI) and row 39 (Ep. 55), re-set `formation_confidence`, and strip the build vocabulary from `senses.evidential`. This is R2's M-N3, carried open, with new evidence.

### P1-6 — The claim that the index is regenerated, never hand-edited, cannot be re-run.

- **Sites:** `Lexicon_Deployment_Index.md` lines 6–7 ("Generated from the chunk files…", "regenerated, never hand-edited"); Doc_06 log ("index regenerated by script"); DL 2026-09-15 (third) ("regenerated by script end to end").
- **Check:** no `lpc` lexicon-index generator exists anywhere in the repository. `Build/worlds/lpc/scripts/` holds the force and story index generators, not a lexicon one; the only lexicon-index generator is `Build/worlds/pahc/build/generate_lexicon_index.py`. No script name appears in the DL or OGT.
- **Why it matters:** the control that R3's H-R1 turned on is unverifiable. A future chunk edit has no generator to rerun.
- **Fix:** commit the generator, or restate the index as hand-maintained with the date of its last full re-derivation.

### P1-7 — Open_Gaps_Tracking omits most of the carried-open items for Docs 03, 05, 06 and 07.

`CLAUDE.md` requires every known gap in OGT. Missing:
- Doc_03's governance item, its two discovery gaps, and the unswept rows.
- Doc_05 §11.13, the Article 20 extension awaiting Mark, with no ruling in the DL.
- Doc_06's carried R2 findings (M-N3, L-N2 residue, L-N3, C-N1), the *suffrage* [DR] tension, the M-R2 residue and the §5.7 discovery-method item.
- Doc_07's four unapplied R2 findings and its §8.10 condensing pass.
- The liturgical-read lexicon candidates of 2026-09-19, not yet integrated.

This review adds none of them to OGT (brief: edit nothing else). They should be appended, numbered, citing subject and date.

### P1-8 — Carried statuses in the four documents contradict later decisions, and one of them feeds the escalation counts.

- **The 411 *Gesta*.** Doc_05 §11.1, the Doc_06 Disposition, and Doc_07 §7, §8.6 and its Disposition carry it as an open "unresolved tension", with no owner. OGT OG-4 records it as **closed** by project-lead decision. Every CO-022 "unresolved tensions: one open" count in these documents rests on the stale state.
- **Also stale:** the liturgical read (done 2026-09-19); Doc_07 §8.9 (OGT exists); Doc_05 §11.9 (Doc_09 exists).
- **Graded P1, not P2,** because a reader re-deriving the escalation state from these documents gets the wrong answer.

### P2-1 — Doc_05's self-record omits Round 2.

The Document Log stops at the Round 1 fix pass. The Disposition says "Round 2 run" with no verdict (0H 1M 3L 2C, "adequate to proceed with N1 and N3 corrected"). All six Round 2 findings are in fact fixed.

### P2-2 — Doc_06 residue.

- §5 item 7 gives "42 times" without the 38 (M-R2 residue).
- `lpclex019`'s correction paragraph in Key Sources is process narration in a deployment chunk. Its Final Assembly line describes a "bracketed block" that no longer carries brackets.
- `lpclex012` and `lpclex016` cite "Doc_01's review rounds" as provenance.
- C-N1 is open.

### P2-3 — Doc_03's frequency figures count the NPNF/ANF apparatus.

Doc_06 applied the `<note>` exclusion only to *certificate*. Recounted in the Cyprian `div1`, tag-stripped:

| Term | With notes | Notes removed |
|---|---|---|
| *confessor(s)* | 150 | 139 |
| *the lapsed* | 96 | 91 |
| *flock/shepherd/pastor* | 113 | 106 |

The span also includes the editor's Introductory Notice, Pontius and the *Treatises Attributed to Cyprian on Questionable Authority*. No tier changes. But "in Cyprian's corpus alone" overstates what was counted.

### P2-4 — Doc_07 housekeeping.

- It cites Completion Standard V1.3.
- It never states its dimension-naming choice.
- §1's "about 6,650 prose words" and §8.10's "about 12% over" do not agree with each other. The regex `[A-Za-z'’]+` gives 6,452 before the Document Log, and 6,961 for the whole file.
- §1's status table still gives the Registry as "returned to independent review". That is still true, but it now belongs to the separate L0 check.

### P2-5 — Two Round 1 reviews in scope ran on Sonnet.

DL line 994 (Doc_06 Round 1) and line 1106 (Doc_07 Round 1) both say "Sonnet per CLAUDE.md's cost rule". Current rules put every review round on Opus. The Rebaseline Declaration's accepted-history table does not list Doc_06 or Doc_07, so this is recorded for Mark rather than assumed accepted.

### P2-6 — Live-surface commentary.

`check_live_commentary.py` counts REWRITE/ROUTE lines of Doc_03 4, Doc_05 15, Doc_06 3, Doc_07 4. Any fix PR on these files must clear its own file's lines.

---

## What one round cannot close (goes to Mark)

1. **The Doc_05 lens spine.** Options A/B/C in (2). The recommendation is C.
2. **CF V7.4 Step 5 against Completion Standard V1.4 §F.** A portfolio Change Order candidate.
3. **Doc_05 §11.13.** Confirm or reject Article 20's against-the-grain condition as applied to personal correspondence. §1.4's bounded reconstruction depends on it.
4. **Doc_06 is at the three-round cap.** Any re-review after fixing P1-5 or P1-6 is a round 4 and routes to the project lead. Alternatively, the fix lands at the record layer and is checked under the record review, not as a Doc_06 round.
5. **The standing portfolio items** (OG-9): the L3 Boundary inconsistency, the Key Texts/Key Sources mismatch, corpus-wide editorial apparatus, and the L4 Doc_07 template (the correct reading of what was previously mislabelled "Doc_07 pre-M4").
6. **Doc_06 §5.7 and the Doc_03 tagging question.** Both are methodology questions.
7. **Whether the 2026-09-19 liturgical-read candidates enter the lexicon**, as new terms or by amending Doc_06. This is a scope decision, since Doc_03 and Doc_06 are Approved to proceed.
8. **The two Sonnet-reviewed Round 1s** (P2-5): accept them as history, or not.

Everything else (P1-1, P1-3 to P1-8, P2-1 to P2-4, P2-6) is mechanical or correctable in place. It fits within one targeted fix pass per document and the remaining round budget.
