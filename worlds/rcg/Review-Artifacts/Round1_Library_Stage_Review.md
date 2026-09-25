# Adversarial Review, Round 1: `rcg` library stage (Step 0, Doc_01, Doc_02 + Source_Registry)

**Reviewer:** independent Opus review agent, dispatched 2026-09-25, per `anthropic-skills:cic-build-cycle`.
**Scope:** `worlds/rcg/Step0_Movement_Scope_Confirmation.md`, `worlds/rcg/Doc_01_World_Identification_Boundaries_Orientation.md`, `worlds/rcg/Doc_02_Source_Ecology.md`, `worlds/rcg/Source_Registry.md`, as drafted 2026-09-25, before this round's revisions.

Reviewed against the cic-build-cycle skill, which the reviewer found at `/root/.claude/skills/synced/*/cic-build-cycle/SKILL.md`. The reviewer re-checked every direct quotation against the vendored files and re-ran or simulated the tools the documents rely on.

**Verdicts:**
- **Step 0:** SUBSTANTIAL REVISION REQUIRED
- **Doc_01:** SUBSTANTIAL REVISION REQUIRED
- **Doc_02 + Source_Registry:** SUBSTANTIAL REVISION REQUIRED

**The good news first:**
- None of the Gregory quotations is fabricated. The Universal Bishop passages (`iii.v.v.x-p7`/`p8`), the Leander letter wording (`iii.v.i.xxx-p5`/`p6`), the three *servus servorum Dei* headings, and the Pastoral Rule opening (`iii.iv.ii.ii-p3`) all match the files word for word, and the speaker is correct.
- The Straw (UC Press 1988) and Markus (CUP 1997) citations are real books.

The failures are misattributed project-data quotes, wrong loci and verification claims, one inflated confidence tag, a methodology misreading, and gaps in the disposition coverage V1.8 requires.

---

## Step 0 (`worlds/rcg/Step0_Movement_Scope_Confirmation.md`)

**S0-1 HIGH: census "why" quote is misattributed (§0, repeated in §3 B2 and §5.1).**
The document "quotes" `world-census.json` II.18 `why` as posing an eligibility question ("whether these decades are a world or the opening of the medieval papacy..."); the live census `why` field says nothing like this — it is a narrative note about Gregory's 590 election, the Sicilian estates, the Lombard dukes and the 596 mission. The wording traces to the Source Readiness Dossier, itself sourcing an older prototype file. Fix: attribute the question to where it actually lives; quote the live census exactly.

**S0-2 HIGH: Section B is misapplied, and an escalation was missed (§0, §3 conclusion, §5.1, §6).**
The Methodology's own Section B text says it is "a phase-level process... never a per-world process." Self-assigning "Tier 1 — Strong seed" to a census "Possible Future World" without a portfolio-level survey is a cross-world/portfolio-level decision — one of the four `cic-build-cycle` escalation categories — yet the document's own escalation self-assessment claimed otherwise. Fix: keep the Section A/B analysis as a recommendation; label the tiering as a portfolio-level question and escalate it rather than self-dispose.

**S0-3 MEDIUM: census "Sourcing" field misquoted while presented as "quoted verbatim" (§1).** Fix: quote exactly or mark as paraphrase.

**S0-4 MEDIUM: "Gregory's four surviving works" is false (§3 B1, B2).** The 40 *Homilies on the Gospels*, the 22 *Homilies on Ezekiel*, and a Song of Songs exposition also survive, unvendored. Fix: say "four vendored works"; name the rest as acquisition leads.

**S0-5 MEDIUM: word-count contradiction (§3 B1).** "Roughly a quarter of a million words" undercounts once the four Moralia volumes (~1.02M words by direct count) are included.

**S0-6 MEDIUM: the World #6 distinction ("imperial absence" versus "imperial partnership") is overstated (§3 B3; §4.2).** Gregory's election awaited imperial confirmation; he spent ~6 years as apocrisiarius at Maurice's court; the Universal Bishop letter is itself addressed to Maurice, asking him to act. Fix: restate as imperial weakness/incapacity in Italy specifically, alongside continued imperial-church partnership.

**S0-7 MEDIUM: wrong cross-world list (§3 B3, third bullet).** The dossier's four Register `context` holders are anglo-saxon, merovingian, byzantine, and early-benedictine-italian-monasticism — not donatism (whose link is the separate Turchi edition). Fix the list.

**S0-8 LOW: arithmetic.** "179 years after Nicaea" should be 235 (560 − 325).

**S0-9 LOW: unsourced claim.** "Still assigned in seminary formation today" needs a source or should be softened.

**S0-10 LOW:** confirm the Methodology document cited as governing is current, not superseded.

---

## Doc_01 (`worlds/rcg/Doc_01_World_Identification_Boundaries_Orientation.md`)

**D1-1 HIGH: the *servus servorum Dei* reading is tagged "Dominant Modern Reconstruction" against the verified evidence (§5; also Doc_02 §1, §3, §7).** The formula heads Ep. I.1 (September 590); the Universal Bishop protest is 595 (Book V). The NPNF endnote at `iii.v.i.i-p8` says the title predates Gregory (Damasus, Augustine) and occurs "four times only" in the Register. A 590 usage cannot be explained as a rebuke of a 595 dispute. Fix: downgrade to Contested, disclose the chronology and predecessors, remove the unverified reading.

**D1-2 MEDIUM: the single-strand argument conflates authorship with world plurality (§4).** The Moralia was largely written before the pontificate; the Dialogues' Equitius episode (Book I, preaching "not having received holy orders, nor yet licence of the Bishop of Rome," authorized instead by vision) evidences a genuinely different authority ground within this world's own Native corpus. Fix: engage this directly rather than assume it away.

**D1-3 MEDIUM: Constantinople is missing from the boundary (§2).** Gregory's diaconate/apocrisiarius years (c. 579–586) belong in the boundary; the Moralia was begun there.

**D1-4 MEDIUM: wrong cross-world list repeated (§6, third bullet).** Same error as S0-7.

**D1-5 LOW: Orthodox "Doctor of the Church" (§1).** Eastern Orthodoxy has no formal "Doctor of the Church" title; say Catholic Doctor of the Church, venerated as a saint (Gregory the Dialogist) in Orthodoxy.

**D1-6 LOW: Istrian schism date (§2).** "Dating from 553" is imprecise; the break followed Vigilius's/Pelagius I's later assent (c. 554–557), and involved Liguria/Milan too.

**D1-7 LOW: Reccared's conversion date (§2).** Should read "587 (personal); 589 (III Toledo)."

**D1-8 LOW: cross-reference errors** (§6 "§3 B3" doesn't exist in Doc_01; §7 item 7 cites "§4/§5" for a claim only in §4; §7 item 2 sends a Doc_01-bound obligation to Doc_02; §1 cites `syr` Open_Gaps by bare number).

---

## Doc_02 + Source_Registry (`worlds/rcg/Doc_02_Source_Ecology.md`, `worlds/rcg/Source_Registry.md`)

**D2-1 HIGH: the Dialogues "verification" is really the vendoring header, so Confidence A is inflated (§1; Registry row 8).** Lines 15–20 are the vendoring header's own Content note, not the body text. Fix: re-verify against the body text directly (~line 3395–3408) and cite that.

**D2-2 HIGH: *servus servorum* reading tagged DMR and pinned on Markus (§1, §3, §7).** Same problem as D1-1, plus an untraced attribution to Markus specifically (§9.3 admits this). Fix: remove the Markus attribution unless traceable.

**D2-3 MEDIUM: the Istrian quote is at the wrong locus and is one-sided (§1 bullet 4).** "apparently supported by the Emperor... bring the Istrian" occurs at ~line 23070, not 22434–22466; the cited range instead says the effort was "in vain." Maurice in fact ordered Gregory to stop pressing the Istrians (591). Fix: correct the locus and disclose both framings.

**D2-4 MEDIUM: the Leander letter is misplaced in the Register (§1 bullet 2).** Locus `iii.v.i.xxx` is Book I, Ep. 43 (591), not Book IX — contradicts the Registry's own row 1 (Books I–VIII). Also, the Reccared passage opens the next paragraph, not "the very next sentence."

**D2-5 MEDIUM: the holdings step is misreported and incomplete (§8, §9.7).** `python -m engine.m9.cli holdings rcg` actually crashes (`FileNotFoundError: records/rcg`), not "no coverage row." Several in-scope files (e.g. `npnf214_seven-ecumenical-councils.xml`, which holds the Second Council of Constantinople, i.e. the Three Chapters council itself) get no disposition line.

**D2-6 MEDIUM: false "no within-window narrative" claim (§4; also Step 0 B1).** Gregory of Tours, *History of the Franks* X.1 (c. 591–594), independently narrates the 590 plague/election from an eyewitness deacon's report, within the window, and is one of the census's own cited `documentedStories` sources. Not vendored — needs naming as an independent within-window witness and acquisition lead. Same for the *Liber Pontificalis* and John the Deacon's *Vita* (out of window).

**D2-7 MEDIUM: the Open_Gaps_Tracking claim is false, and handoff items 9–10 are not met (§8).** §8 claims the Moralia gap is "the leading item" in `Open_Gaps_Tracking.md`; that file has zero entries. The dossier's cross-world questions are not logged in Open_Gaps or `NEEDS-RULING.md`.

**D2-8 MEDIUM: Registry checkpoint violations.** Several specific claims (Istria, Lombards, Bertha, transmission history) rest on the NPNF editorial apparatus, which has no row of its own. The Whitby Life, Paul the Deacon, and John the Deacon have no Excluded/Out-of-Boundary rows.

**D2-9 MEDIUM: the stated reason for the Moralia gap is inaccurate (§1, §9.1).** Doc_02 says OCR irregularity prevented locating the dedicatory epistle to Leander; it is in fact easily locatable (line ~387), with a directly relevant, quotable passage at lines ~545–560 on the contemplative/active tension. Fix: close the gap properly rather than leave an untrue reason on record.

**D2-10 MEDIUM: incomplete Article 23 rival routing (§6).** Surviving Donatism gets no treatment beyond the Turchi row; the Register itself contains at least one Donatist letter (Ep. I.74, per the apparatus), which also partly answers the Turchi duplication question.

**D2-11 MEDIUM: transmission claim misattributed (§2).** Line 22132 is a Prefatory Note on how the selection was made, not a statement about sixth-century archival practice; the actual archive statement (mentioning John the Deacon) sits further on (~line 22971). The NPNF follows the Benedictine arrangement, not MGH/Norberg — relevant to the Turchi cross-check and undisclosed.

**D2-12 LOW: Registry row 9 contradicts §8** (Native with a Licensed-For target, vs. "out of scope for this pass").

**D2-13 LOW: gender section wording (§6).** "Lombard and Visigothic royal women" is imprecise; name Theodelinda (a Catholic Lombard queen, complicating the "Arian Lombards" framing) and Brunhild specifically.

**D2-14 LOW: overstated Lombard evidence (§1 bullet 1).** The "barbarians... in Europe" passage is general rhetoric, not Lombard-specific, and shouldn't be cited as primary Lombard evidence without qualification.

**D2-15 LOW: cross-reference and Step 2 output gaps.** "Doc_01 §4.1" should be "Step 0 §4.1"; V1.8's own Step 2 outputs (a per-file quotability flag; edition/original-language/primary-vs-cross-check pairing) are largely absent.

---

## Cross-cutting finding (all three documents)

**X-1 MEDIUM: process narration in canonical files.** Heavy "this session"/"this build thread" language and embedded Status/Disposition revision-history narration. Flagged against V1.8 handoff item 11 and CLAUDE.md's live/canonical-surface rule.

**Disposition of X-1, decided by the build thread rather than accepted wholesale:** independently checked against `worlds/ijc/Doc_02_Source_Ecology.md` and its own Disposition section (an already-cleared, comparable library-stage document), which carries exactly this kind of inline revision-history narration ("Round 1 independent adversarial review (2026-07-20) returned SUBSTANTIAL REVISION REQUIRED...") as part of its own required Disposition section, per the `cic-build-cycle` skill's own instruction to "log it: document name, review outcome, how many revision rounds it took... which disposition it received." This is the skill's own required audit trail, not the "notes, commentary, change history, review discussion" CLAUDE.md's live-surface rule names as prohibited — that rule is aimed at process narration with no structural home, not at a Disposition section the build-cycle discipline itself requires every document to carry. Not applied as a blanket rewrite; retained per established, already-cleared project precedent. If a future full-system review reaches a different reading of CLAUDE.md's rule against ijc's own precedent too, that is a portfolio-level/methodology question for the project lead, not something this world's own build resolves unilaterally by rewriting only its own documents.

---

**Root cause, worth naming:** several findings share one root cause — facts carried over from the Source Readiness Dossier or from this build thread's own prior general knowledge without direct re-verification against the live census, the corpus-map, or the vendored files themselves (S0-1, S0-7, D1-4, D2-9). The fixes applied in this round re-verify each such claim against its actual primary source rather than the secondary account it was carried from.
