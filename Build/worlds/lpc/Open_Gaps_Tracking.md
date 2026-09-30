# Open Gaps — Latin Pastoral-Congregational Christianity ("The Ordinary Church") Formation World

Running, dated ledger for the lpc world build (world-code `lpc`, `world_id`
`latin-pastoral-congregational`, `card_name` **"The Ordinary Church"**), matching the
discipline `Build/worlds/don/Open_Gaps_Tracking.md` and `Build/worlds/cappadocian/Open_Gaps_Tracking.md`
already use: dated entries, disclosed-recovery notes, honest status, project-lead-anchored
where confirmation is a project-lead act. Per CLAUDE.md's own rule ("Every known gap, open
question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to
live only in a conversation thread"), `lpc` was, until this file, the only world in the
portfolio without one.

**A note on provenance, stated plainly.** `lpc` has never carried a standalone
`Open_Gaps_Tracking.md` before this file. Its own build has used `lpc_Decision_Log.md`
(2,157 lines, dated entries from 2026-09-01 through 2026-09-24) as that record throughout,
alongside two documents that are easy to mistake for a gap tracker but are not one:
`lpc_Gapped_Formation_Precedent.md` is a **substantive methodological ruling document** —
advisory precedent on gapped/diachronic formation-types, received from the project lead
2026-09-15 and cited as the basis for closing two of Doc_04's own open items — not a running
list of open questions; and `Doc_04_Superseded_Claims.md` is a **correction-history
companion** to Doc_04 specifically, holding claims that document has withdrawn, not a
world-wide tracker. This file is created now per CLAUDE.md's own rule and the fleet
convention every other world uses, and it works **from** the Decision Log, these two
documents, the `Review-Artifacts/` directory (its listing independently checked against
round counts the Decision Log claims), and direct, on-disk verification of registration and
compilation state — not around any of them. Every entry below traces to a specific dated
Decision Log section, a named `Review-Artifacts/` file, or a directly-verified file on disk.
Nothing here is invented to fill a gap in what the record actually shows; where the record
itself is silent, or where this review could not independently verify a claim, that is
stated rather than papered over.

---

## Thread scope and governing documents

`lpc` is built under the same `cic-build-cycle` discipline as every other CiC world: one
document at a time, review-gated, self-governing within four escalation categories
(Representative identity/title, portfolio-level/cross-world, governance/methodology, and
unresolved tensions the pipeline cannot close on its own), never self-assigning Frozen
status. World-code `lpc` was assigned at Step 0, this world's first document.

**Construction window:** *c.* 246–430 CE, Roman North Africa (Carthage, Hippo Regius).
**Strand determination:** strand-singular, but of a distinctive shape this project had not
previously built: a **gapped/diachronic** formation-type — two anchor figures, Cyprian
(*c.* 246–258) and Augustine (391–430), separated by a 133-year interval with no surviving
voice native to this world's own boundary, the interval itself richly attested but almost
entirely through sources belonging to the neighboring, already-built Donatism world
(`lpc_Gapped_Formation_Precedent.md` §1–§2; Doc_01 §5). **Representative:** Datus, **"Bishop
of the Kept Flock"** — a bishop within an urban African congregation, holding a *libellus
pacis* (a certificate of peace with names written on it) as his identity-constitutive object
(2026-09-15 entry, "M1 RESOLVED").

Governing documents used throughout, per the Decision Log's own citations: the Constitution
(Articles 3, 21, 22, 23, 24, 29, 31, 33 all invoked by name at various points);
`CiC_L3B_Formation_World_Construction_Framework_V7.4` and its companion Blueprint; the
Interpretive Lexicon Development Framework (LDF) V2.1; the Forces Framework V1.1;
`CiC_L3C_Representative_Construction_Framework_V3.2` (Parts Three through Ten, cited as
"RCF V3.2" throughout the Representative build); and
`Build/reference/method/CiC_World_Build_Completion_Standard_V1.3.md` (§A/§B, the record-native
completeness and gate requirements a real world-freeze needs — see OG-2 below). This
world's own Decision Log cites its escalation/attribution/disposition rule as "CO-022"
throughout, functionally the same discipline `don`'s and `cappadocian`'s own logs cite as
CLAUDE.md/`cic-build-cycle`'s escalation categories.

---

## Source acquisition — G1 through G9, closed except a small G4 residual

Nine acquisition requests (G1–G9) ran against this world. This build's own network access
was blocked at the infrastructure level through at least 2026-09-05 (confirmed by two
independent tools, `WebFetch` and a direct `curl`, both returning a 403 policy denial),
forcing G1, G3, and a partial G4 to route through the project lead's own manual download and
supply (`lpc_Decision_Log.md`, 2026-09-05 entries). Network access was confirmed working
2026-09-08 (the same two-tool cross-check, now returning HTTP 200), after which the
remaining acquisitions ran directly:

- **G1** (Hartel's Cyprian, CSEL 3) — Pars I–II fulfilled 2026-09-05 (project-lead-supplied
  docx, Registry row 191); Pars III fulfilled 2026-09-08 (row 194). **Closed in full.**
- **G2** (Harnack's *Vita Cypriani*) — closed 2026-09-08, a genuinely new find
  (`texteunduntersuc3839akad`) no prior search round had located.
- **G3** (Possidius, *Vita Augustini*, Weiskotten 1919) — fulfilled 2026-09-05
  (project-lead-supplied docx, Registry row 192). **Closed in full.**
- **G4** (Goldbacher's Augustine *Epistulae*, CSEL 34/1, 34/2, 44, 57, 58) — CSEL 57 Pars IV
  fulfilled 2026-09-05 (row 193); CSEL 34/1, 34/2, and 44 fulfilled 2026-09-08 (rows
  195–196). **CSEL 58 (praefatio and indices only, no letter text of its own) was
  deliberately not chased further**, named a "minor, low-value residual" at the 2026-09-08
  entry — no later Decision Log entry records it being closed. Still open on the terms the
  record itself uses.
- **G5** (Monceaux, *Histoire littéraire de l'Afrique chrétienne*) — closed 2026-09-08, after
  a citation-accuracy correction found the Manifest's own long-standing lead was actually
  Tome Cinquième (already vendored on the sibling Donatism branch), not Tome Premier; the
  actual three relevant volumes (Tomes I, II, III) independently located and vendored.
- **G6** (Augustine's *Retractationes*, CSEL 36) — closed 2026-09-08, a genuinely new find.
- **G7** (von Soden's *Briefsammlung*) — closed 2026-09-08.
- **G8** (von Soden's *Prosopographie*) — closed 2026-09-08, a genuinely new find, located by
  searching the periodical series' own title rather than the article's.
- **G9** (Delehaye's *Passions*) — closed 2026-09-08.

**A separate, ten-file batch** was independently re-vendored 2026-09-08, closing a prior,
never-merged sibling research session's own work (`session_01WLxhNbVhjkf1R2SAh8dxxT`) rather
than trusting it — independent re-verification found the underlying content sound but caught
a real extraction hazard (Hartel's Pars III bound in the same scan as an unrelated Arnobius
work) and a misleading filename on the sibling's own copy, both avoided in this thread's own
re-fetch.

**The *Codex Theodosianus*** was vendored twice, on the project lead's own direct decision
(2026-09-02): once by reference only (OTA's TEI edition, CC BY-NC-SA, cited but never
committed to `cic/texts/`, per that project's own in-copyright-material rule), and once fully
vendored (`cic/texts/codex-theodosianus_latinlibrary.txt`, The Latin Library's public-domain
text, supplied directly by the project lead, book by book) — with the edition-provenance gap
between the two disclosed rather than treated as equivalent.

`lpc`'s branch merged with the shared cross-world Library Build Engine on `main` (158
commits) 2026-09-03, per the project lead's explicit direction, closing zero conflicts inside
this world's own build folder.

---

## Build log — Doc_01 through Doc_09, and the World Profile (per-document disposition)

*(Format: document · review outcome · revision rounds · review-artifact file(s) ·
disposition. Every entry below is drawn directly from `lpc_Decision_Log.md`'s own dated
sections and the named `Review-Artifacts/` files, cross-checked against the directory
listing.)*

- **Doc_01 — World Identification, Boundaries, Orientation** (2026-09-01): **Approved to
  proceed.** **9 review rounds** (`Review-Artifacts/Doc01_Round1–9_Review.md`). Central
  finding: strand-singular per Article 21's own test, on evidence demonstrated independently
  in *both* the Cyprian and Augustine phases rather than requiring the 133-year gap to be
  bridged. A live methodology question — three competing readings of the portfolio-level
  Step 0 phrase "orthogonality to state power" — was put to the project lead 2026-09-01; his
  answer settled *method* (report what the sources document, including a figure's own change
  over time, rather than manufacture a single theory to fit a screening phrase) rather than
  selecting one of the three readings, and Doc_01 §7 was revised accordingly across two
  further rounds. **Six post-disposition edits** are disclosed in the document's own status
  line, per this world's own standing discipline against silent post-disposition drift; a
  seventh, larger correction (Possidius *Vita* ch. VIII's own account of Augustine's
  ordination) followed 2026-09-16, see below.
- **Doc_02 — Source Ecology + `Source_Registry.md` + `Source_Acquisition_Manifest.md`**
  (first self-disposed 2026-09-02): **Approved to proceed, then reopened and re-disposed
  twice more — the most contested document set in this world's build.** First
  self-disposition: **14 rounds** (`Doc02_Round1–14_Review.md`), Round 14 the first to return
  0/0/0/0. Reopened 2026-09-08 for the day's own vendoring integration: **Rounds 15–27**
  (`Doc02_Round15–27_Review.md`), a project-lead-directed banner-stripping rewrite (all three
  documents rewritten to remove inline "corrected here, independent review Round N's own X"
  correction-history apparatus from live prose, per the project lead's own 2026-09-08
  direction that this history belongs in the Decision Log, not the construction document
  itself), and **twenty-seven rounds' worth of a single recurring failure shape, tracked
  explicitly by name across the whole sequence: a fix pass, in the act of correcting one
  finding, introduces or leaves stale a further claim the review never asked it to touch.**
  Reopened a second time 2026-09-09 for two Registry sourcing-conclusion corrections (row 65,
  the 411 Conference acts; row 44, the *Codex Theodosianus*): **Rounds 28–29**
  (`Doc02_Round28–29_Review.md`), each round catching a real factual misattribution the prior
  fix pass had introduced (Letter 185 §25's fine first mis-sourced to the wrong statute, then
  mis-quoted from an entirely different work) — traced to one shared mechanism, "a search too
  strict for the text it was run against, then trusted because it returned something." A
  wrong-tree branch fork (2026-09-09/10) briefly produced a false "Round 27 unfixed" claim,
  retracted 2026-09-10 once reconciled. **Final self-disposition: a scoped Round 30**
  (`Doc02_Round30_Review.md`), 2026-09-12, **CLEARED — 0/0/0/1 COSMETIC** — the first
  disposition since Round 14 to rest on a clean review rather than a direct project-lead
  instruction to close regardless of outcome.
- **Doc_03 — Lexicon Candidate List** (2026-09-09): **Approved to proceed**, on the project
  lead's own direct instruction, **not** on a terminal clean review — this document never
  cleared an independent review at zero findings at any point in its history. 18 candidate
  terms (restructured from an original 14), five thematic clusters. **2 saved review-artifact
  rounds** (`Doc03_Round1_Review.md`: 4H/8M/8L/2C; `Doc03_Round2_Review.md`: 4H/12M/13L/2C,
  31 findings, all fixed), **plus two further independent re-reviews disclosed in the
  Decision Log but never saved as their own review-artifact files** — a gap from this
  project's own "a review exists as a file, not a claim" discipline, disclosed in the
  document's own disposition entry rather than smoothed over. Central finding-chain: Round 2
  found the Round 1 fix pass had reversed Doc_01 §6's own grace/purity finding (attributing
  Cyprian's minister-purity refusal to the wrong bishop); the first unsaved re-review found
  the Round 2 fix pass had, in the act of fixing 31 findings, broken this world's own
  banner-stripping rule at scale (31 "an earlier draft" references where 2 had stood before)
  and misattributed a new candidate term's source location; the second unsaved re-review
  found two further problems in the fix pass that closed those.
- **Doc_04 — Gravity Discovery** (drafted 2026-09-12): **Approved to proceed 2026-09-15, then
  formally CLEARED the same day** — the most contested single document in this world's
  build. Final classification (per `Doc_04_Gravity_Discovery.md` §3, as ratified): Primary
  and Supporting gravities including G1 (Pastoral Office as Territorial Flock-Keeping), G2,
  G3, G6, and **G5 (Conciliar Authority Theory), whose own classification was superseded five
  times across nine review rounds** before the project lead ruled it directly
  (2026-09-14: **Supporting**) — see `Doc_04_Superseded_Claims.md` §1 for the full withdrawal
  chain (did-not-reach-gravity-status → Tensional → Supporting-on-a-misread-third-clause →
  Supporting-with-an-invalid-inference → Supporting-under-a-misapplied-ambiguous-results
  provision). **11 review rounds** (`Doc04_Round1–11_Review.md`). The 411 Conference *Gesta*
  was read twice in an attempt to shore up G5 with Donatism's own home-territory evidence;
  **both reads were withdrawn as unsound** (Round 5: overstated; Round 6: unsound in a worse
  way — a genuine ~7,000-line band mistaken for footnote apparatus without being opened). No
  third read was commissioned, on the project lead's own gapped-formation-precedent-informed
  decision that a third attempt at the same source for the same purpose is the pattern, not
  the fix (`lpc_Gapped_Formation_Precedent.md` §4a). **The morning of 2026-09-15, Doc_04 was
  approved "with the escalation carried open" on the mistaken belief that Round 11's four
  HIGH findings were still unfixed; hours later, the same entry's own author found and
  corrected the error** — the four HIGH findings had in fact already been closed before the
  approval was given, and Doc_04 was reassessed and formally **CLEARED, "no twelfth round,"**
  the same day. This reversal is recorded in full at the Decision Log's own 2026-09-15
  entries ("Doc_04 cleared; and a correction to this morning's own approval entry"). Residual
  MEDIUM/LOW findings from Round 11 are "carried, not chased" — record-state items, none
  touching a gravity, a test, or a classification.
- **Doc_05 — Ecological Reconstruction** (drafted 2026-09-14): **Approved to proceed
  2026-09-15**, by the project lead's own direct instruction (not self-disposed — a CO-022
  escalation category was open). 2 review rounds (Round 1: 8 findings, REVISION REQUIRED, all
  applied; Round 2, "final gate," 0 High, 6 new findings applied). A live cross-world
  terminology question — "Boundary Structures" vs. "Boundary Ecology," a contradiction inside
  the Constitution and Forces-Framework governing texts themselves, not merely between them —
  was ruled *for lpc specifically*: **"Boundary Structures" is canonical for this world.**
  The governing texts' own underlying self-contradiction is unresolved and inherited by every
  future world (see OG-9).
- **Doc_06 — Full Interpretive Lexicon** (drafted 2026-09-14): **Approved to proceed
  2026-09-15**, project-lead direct instruction. 18 chunks (later 19, a term added on the
  project lead's own direction at Round 1) plus a generated index. 3 review rounds: Round 1
  (3H/3M/2L/0C, REVISION REQUIRED, all applied); Round 2 ("final gate," 4 findings applied on
  the project lead's own direction, **6 findings deliberately not applied**, on his earlier
  direction to fix four and proceed); Round 3 found the Round 2 fix pass had broken
  something, fixed, index regenerated (all 247 index cells re-derived with zero mismatches).
- **Doc_07 — Integrated Ecology Analysis** (drafted 2026-09-15): **Approved to proceed
  2026-09-15**, project-lead direct instruction. 2 review rounds: Round 1 (1H/2M/2L, all
  applied); Round 2 (1H/4M/6L/3C, confirmed all Round 1 fixes and judged the document
  adequate). **Disclosed build-cycle departure**: this document was drafted on three
  undisposed inputs (Doc_04, Doc_05, Doc_06 were all still undisposed at the time of
  drafting) — named as a real departure, not cured retroactively. **Unlike the sibling
  Donatism world's own Doc_07, which was built on the M4 Change Order's Smart
  seven-dimension lens spine after a live methodology escalation, no comparable escalation or
  rebuild is recorded for lpc's own Doc_07** — it remains blocked, alongside the World Profile
  template, on the same inherited pre-M4 lens-structure mismatch don's build resolved for
  itself (see OG-9).
- **Doc_08 — Forces Document + `lpc_Force_Index.md` + `scripts/gen_force_index.py`** (drafted
  2026-09-15): **Approved to proceed 2026-09-15**, project-lead direct instruction, **not**
  self-disposed. **8 review rounds** (`Doc08_Round1–8_Review.md`), every one SUBSTANTIAL
  REVISION REQUIRED. **Rounds 5 through 8 each explicitly record that no HIGH finding touches
  the forces analysis itself** — every finding from Round 6 onward is against the
  certification apparatus or the index generator script, a recurring, tracked failure shape
  ("a guard that shares its definition with the thing it guards is not a guard"; "a control
  stated more broadly than it is implemented is worse than no control, because the next round
  will trust it," repeated verbatim at Rounds 6, 7, and 8). **Round 8 (2026-09-15,
  `Doc08_Round8_Review.md`), the most recent review this document has received, found 2 HIGH,
  5 MEDIUM, 6 LOW, 1 COSMETIC — all against the generator — and no later Decision Log entry
  records these findings being fixed or re-reviewed.** See OG-3.
- **Doc_09 — Story Inventory + 7 `Story-Chunks/` + `lpc_Story_Index.md`** (drafted
  2026-09-15): **Approved to proceed 2026-09-15**, "with the escalation carried open,"
  project-lead direct instruction, not self-disposed. **8 review rounds**
  (`Doc09_Round1–8_Review.md`); Rounds 1–7 SUBSTANTIAL REVISION REQUIRED, Round 8 MINOR
  REVISION (0 HIGH — the first round of eight to reach it). **8 of 11 HIGH findings across
  the whole review history are one recurring defect: a silence asserted about a source, which
  the source in fact refutes** — one instance (Round 7's) survived six prior rounds
  undetected, purely because no reviewer happened to quote that specific sentence. Built as a
  structural control: `Doc09_Claims_Register.md` + `scripts/check_claims.py`, which derives
  every corpus-absence claim from the deliverables and halts on an unregistered claim or a
  stale register entry. **At disposition (2026-09-15): 142 claims derived and registered, with
  137 of the 142 remaining UNVERIFIED** (Decision Log's own disposition entry, its fourth point, 2026-09-15;
  registration is the control, verification separate work). A separate structural pass the
  same day extracted 76 correction-history notices (3,266 words) out of the deliverables and
  deleted `notice_strip.py` (387 lines) once it was no longer needed. Carried open at
  disposition: the CF V7.4 Tier 3 escalation for `lpcstory006` (governance/methodology,
  unresolved); the Round 8 fix pass itself unreviewed; Possidius *Vita* XIX–XXVII unread; 137
  of 142 claims UNVERIFIED.
- **World Profile** (`lpc_World_Profile.md`, drafted 2026-09-14, inferred as this world's
  next document by comparison with `desert`, Donatism, and `hal`'s own sibling precedent, per
  its own 2026-09-15 disclosure — **never separately confirmed by the project lead as this
  world's own Step-sequence item**, treated as confirmed by his own "start doc_09b"): **Approved
  to proceed 2026-09-19**, project-lead direct instruction. **5 review rounds**
  (`WorldProfile_Round1–5_Review.md` plus three Round 4 dimension files — Condensation,
  Consistency, SourceFidelity), cleared at Round 5 (0/0/0/2 COSMETIC). Round 1 found 5 HIGH
  including a fabricated quotation; Round 4 — the first review to see the document after a
  33% condensing pass — found 5 HIGH again, two of which had survived three prior rounds
  because no round before it swept every quotation and locus to source. **The build thread's
  own attempt to self-apply this disposition on 2026-09-16, after Round 5 came back clean,
  was explicitly refused as self-approval** — CO-022 permits self-disposition, but the
  project lead's own standing rule (a thread never scores its own work as passing) took
  precedence, and the refusal is recorded as correct rather than quietly dropped. Carried
  open: 4 MEDIUM/5 LOW/1 COSMETIC Round 4 findings, deliberately unapplied on the project
  lead's own instruction; the portfolio-level items from Doc_07 §8's fourth item, carried open at the 2026-09-15 disposition; the World Profile
  length target ("no complex world in the portfolio meets it," routed to a coach handoff); an
  exhaustive citation-locus sweep (~90 loci), never completed by any round.

**A recurring, tracked pattern, worth naming plainly in the terms the Decision Log's own
2026-09-01 entries first established for it and the 2026-09-10 entry later root-caused:**
across Doc_02's ~30 review rounds, Doc_08's 8 rounds, and Doc_09's 8 rounds, this world's own
build shows the same failure shape recurring at a new site each time — a fix pass, in the act
of correcting a named finding, introduces or leaves stale a further claim the review never
asked it to touch. The 2026-09-10 entry names a specific root cause for the largest instance
of it (Doc_02's own Status lines and §10 restating round counts and disposition history
inline, in prose, rather than pointing at a single source of truth) and fixed it at the
source rather than per topic. A narrower version of the same shape — the citation-locus
error, the failure mode `don`'s own Doc_08 is named for — recurs independently across the
Representative-construction phases; see the Representative build log below and OG-5.

---

## Representative build log — Datus, "Bishop of the Kept Flock"

**Identity and image decision** (2026-09-15, "M1 RESOLVED," decided by the project lead as
one packaged choice per `CLAUDE.md`'s own rule): **Datus** (a real African cognomen of the
period, attested zero times across the 38 vendored corpus files but grounded in *Dativus*,
one of Cyprian's own addressed Numidian confessor-bishops), **"Bishop of the Kept Flock"**
(113 combined occurrences of flock/shepherd/pastor in Cyprian's corpus alone), object **a
*libellus pacis*, a certificate of peace with names written on it** (Cyprian's own *Ep.* XV,
carrying three gravities at once — G1, G2, and the Tensional G8), image a painterly oil bust
portrait per the locked portfolio standard. **The grounding brief names six open items the
decision itself does not close** — five are administrative or template gaps (world not yet
registered; the portrait file not yet committed at decision time; the L4 Representative
Construction Notes Template's own missing image/appearance section, raised as a methodology
gap for the project lead; dress and complexion flagged INFERENCE, not DOCUMENTED). **The
sixth is substantive and, as far as this review can find, still open — see OG-1 below.**

**Representative construction resumed 2026-09-23** (Go-Live Pipeline Coordinator thread,
after branch reconciliation), running RCF V3.2 Parts Four through Nine end-to-end under
`cic-build-cycle` self-governance:

- **Phase One — Ecology Assessment** (drafted earlier, reviewed 2026-09-23): **Approved to
  proceed.** 1 round (`Phase1_EcologyAssessment_Round1_Review.md`), SUBSTANTIAL REVISION
  REQUIRED — 2 HIGH, 4 MEDIUM, 1 LOW. Both HIGH findings were fabricated- or wrong-citation
  claims about sibling canonical documents and Doc_08's own Force IDs, both independently
  re-verified and corrected. Targeted recheck cleared same day.
- **Phase Two — Formation Calibration** (2026-09-23): **Approved to proceed.**
  `Review-Artifacts/Phase2_FormationCalibration_Round1_Review.md`, 1H/3M/1L/1C. The HIGH
  finding was a citation-locus error reproducing a defect Phase One's own Round 1 review had
  already caught and fixed once (Doc_07 §2D's three dominant doctrinal bodies misdescribed as
  one) — the first of five such recurrences across the Representative phases, see OG-5.
  Merged to `main` at `708aa13` (the Phase Two pull request, 2026-09-23).
- **Phase Three — Voice Construction** (2026-09-23): **Approved to proceed.**
  `Review-Artifacts/Phase3_VoiceConstruction_Round1_Review.md`, 1H/2M/0L/2C. The HIGH finding
  misattributed the Passion of Perpetua and Felicitas's exclusion to a date-boundary reason
  when Registry row 204 in fact excludes it by prior cross-world ruling (assigned to
  `tertullian-s-voice`). Merged at `6d2379e4` (the Phase Three pull request, 2026-09-23).
- **Phase Four — Engagement Architecture** (2026-09-23): **Approved to proceed**, no HIGH
  findings. `Review-Artifacts/Phase4_EngagementArchitecture_Round1_Review.md`, 0H/2M. Built
  its own distinctive Dynamic Encounter mechanism (**Answerability → the Argued Case → the
  Road Back**), deliberately distinct from Donatism's own Threshold–Narration–Jeopardy,
  confirmed by direct comparison. One MEDIUM finding was a second citation-locus error (Doc_05
  §5.4 vs. the correct §5.1). Merged at `3f2b7454` (the Phase Four pull request, 2026-09-23).
- **Representative Artifact Construction — Permanent Prompt + World Capsule Core**
  (2026-09-23): **Approved to proceed.** `Review-Artifacts/RepresentativeArtifacts_Round1_Review.md`,
  1H/5M/2C, plus one MEDIUM completed and one small technical correction (a genuine internal
  contradiction — Hippo Regius called both "inland" and "coastal" in the same clause) found
  and disclosed at the targeted recheck. The HIGH finding was a mandatory-boilerplate edit
  (world-specific imagery substituted into the template's own fixed backstop-mechanism
  sentence), restored verbatim. Merged at `4e84d208` (the Representative Artifact Construction pull request, 2026-09-23).
- **Phase Five — Boundary Testing, Round 1** (2026-09-23): **Approved to proceed**, held as
  "the complete, honest record it is — not a false clean pass." A 14-probe **simulated**
  battery (isolated-subagent method, per the sibling `don` precedent — Constitution Article 31
  names this informational only, not a substitute for governed live-runtime validation; **no
  live AWS Bedrock generation has been run against lpc's own artifacts**, see OG-11). Result:
  10 of 14 PASS cleanly, 2 AMBIGUOUS, 1 FAIL. The FAIL (Probe 12, claim-laundering — both
  deployed artifacts stated only one of Augustine's three documented coercion-development
  stages) was fixed in both artifacts. **Probe 11 (Relational Safety) was AMBIGUOUS and was
  not force-fit into an artifact edit** — logged as an explicit Phase Six design requirement
  instead (the Facilitator layer must pre-empt Datus's own voice on genuine distress signals,
  which an isolated Datus, tested with no Facilitator layer present, was found to freely
  author redirect-shaped content around). **Explicitly not yet Freeze-eligible on Relational
  Safety grounds** at this disposition. Merged at `119e927f` (the Phase Five Round 1 pull request, 2026-09-23).
- **Phase Six — Facilitator Coordination** (2026-09-24): **Approved to proceed.**
  `Review-Artifacts/Phase6_FacilitatorCoordination_Round1_Review.md`, 0H/3M. **Central,
  independently-verified finding:** `engine/m4/turn.py`'s portfolio-level
  "Facilitator-only" routing decision (the same one `don`'s own build commissioned) is
  genuinely world-independent, unconditional code (`voice_event = None` on the
  `ACUTE_DISTRESS` branch, no per-world gate) — so the architectural fix Probe 11 called for
  is already live and automatically covers `lpc`, closing that design requirement with no
  world-specific engine change needed. Merged at `d93f2adc` (the Phase Six pull request, 2026-09-24); a small follow-up
  citation-locus fix merged at `cead10a1` (the Phase Six citation-locus fix pull request, 2026-09-24).
- **Phase Seven — Encounter Ecology Mapping** (2026-09-24, drafted as an honest
  **retrospective audit**, following the sibling `don`/Syriac precedent for a Phase Seven
  built after Representative construction rather than before it, since no such document was
  produced for `lpc` at world-build Step 9): **Approved to proceed.**
  `Review-Artifacts/Phase7_EncounterEcologyMapping_Round1_Review.md`, 4H/4M/1C. Findings
  included a G5 Formation-test-verdict inversion, a fabricated Permanent Prompt section
  citation, and — the one finding carried forward rather than resolved on the spot — **§3's
  claim that both deployed artifacts "preserve the done/said distinction" for worship and
  liturgical life was found false**: Phase One's own richer, already-Approved 2026-09-19
  liturgical finding (catechumenate stages, the renunciation formula, the imposition of the
  hand) does not in fact appear in either deployed artifact. Named **open item §6.3**, a
  genuine, disclosed integration gap between an already-Approved finding and the deployed
  artifacts. Merged at `ef3ffe09` (the Phase Seven pull request, 2026-09-24).
- **World Context Layer, chunks 001–005** (2026-09-24): **Approved to proceed.**
  `Review-Artifacts/ContextLayer_Round1_Review.md`, 2H/5M/2C, concentrated mostly in
  `lpcctx003`. Drafted specifically to route Phase Seven's own §6.3 depth into the
  token-constrained context layer rather than reopen the already-disposed Permanent Prompt
  and Capsule Core — **this closes the substance of §6.3.** Merged at `7da29b42` (the World Context Layer pull request, 2026-09-24).
- **Voice Configuration for Datus** (2026-09-24, `lpc_Voice_Configuration_Datus.md`):
  **Approved to proceed.** `Review-Artifacts/VoiceConfiguration_Round1_Review.md`, 1H/2M/1C.
  The HIGH finding presented disclaimed editorial apparatus (*plebs*, explicitly not a
  headword per `lpclex010`) as genuine runtime vocabulary; removed. **Model selection, live
  audition, and pronunciation-dictionary testing are all explicitly, honestly left
  PENDING** — no live ElevenLabs platform access exists in this build thread's own
  environment, following the same disclosure pattern the Cappadocian/Eumathios precedent
  set. Merged at `b7dc7d0c` (the Voice Configuration pull request, 2026-09-24).

**As of the most recent Decision Log entry (2026-09-24), RCF V3.2's Representative
construction sequence through Phase Seven, Representative Artifact Construction, and both
remaining deployment outputs (World Context Layer, Voice Configuration) is complete and
Approved to proceed at every step.** No Part Eight (Table Readiness) work, no live M3
sealed-probe admission battery, and no world registration have been reached — see OG-2 and
OG-11.

---

## Standing open items (project-lead-facing) — not resolved by this file

### OG-1. The certificate/portrait-object silhouette collision with Theon and Albina — explicitly "Not decided here," and no later entry resolves it.

The M1 identity decision's own grounding brief (2026-09-15, item 5) found a **binding
cross-portfolio constraint on `main`** that this branch predated: `donatism/Fidelis_Portrait_Prompt.md`
records the project lead's own direct critique rejecting a codex as Fidelis's object —
*"Silhouette recognition at icon/table-scene scale does not survive that distinction; two of
seven Representatives reading as 'a bishop holding a book' defeats the object system's own
purpose"* — and explicitly extends the ban to any collision with **Theon (an opened scroll)**
or **Albina (a wax tablet and stylus)**. Datus's certificate is a flat written-text object
that, at icon scale, reads as the same pale-rectangle-in-two-hands silhouette as both. Three
options were named — (a) keep the certificate and record the collision explicitly, since it
is DOCUMENTED and identity-constitutive where Fidelis's rejected codex was only a candidate;
(b) substitute the non-textual ransom purse of `lpcstory004`; (c) no object, as Fidelis was
resolved — and the entry closes: **"Not decided here."** This review found no later Decision
Log entry, through 2026-09-24, that revisits or resolves this question. **Genuinely open,
reserved for the project lead**, per the entry's own framing.

### OG-2. World-freeze compilation and registration have not begun — confirmed directly on disk.

`records/lpc/` does not exist. `packages/lpc/` does not exist. `records/worlds/` holds a
`.yaml` entry for twelve worlds (`alx`, `cappadocian`, `desert`, `don`, `fix`, `gallic`,
`hal`, `ijc`, `pahc`, `rzg`, `syr`, `witt`) and has **no `lpc.yaml`** (checked directly,
2026-09-24). This matches the Decision Log's own repeated, explicit disclosure: registration
requires a `state` field, and every existing registry entry's `state` values (`built`,
`admitted`, `open`) only begin at first compile, which `lpc` has not reached (2026-09-21
entry, "Branch reconciliation applied"). Per
`Build/reference/method/CiC_World_Build_Completion_Standard_V1.3.md` §A, a real world-freeze
requires a full set of record-native artifacts this world does not yet have — populated
`world_core`, `source`, `term`, `story`, `quote`, `gravity`/`force`, `figure`,
`contested_claim`, and `voice_profile`/`demonstration` records, plus every view rendering
without error — and §B requires machine gates passing with committed run output, not
self-reports. **This is precisely the shape of blocker `don`'s own Phase Eight hit**, and
that world's own precedent is exact: *"The project lead ruled: Commission full record-native
compilation of Donatism before Phase Eight"* (`don`'s own 2026-09-10 entry). No comparable
commissioning has happened for `lpc` as of the most recent Decision Log entry. This is a
portfolio-level decision reserved for the project lead, not something to self-decide, per the
2026-09-21 entry's own explicit routing ("A registry entry with no `state`, or an invented
one, would be a new registry shape with no fleet precedent — routed back to the project lead
rather than decided inside this reconciliation pass"). Separately: `cic-website/data/world-census.json`
does carry an **atlas-level** reference entry for `latin-pastoral-congregational-christianity`
(id, `atlasId: "I.8"`, era 1) — this is part of the broad historical atlas of candidate and
reference formation-types (which also lists many never-built worlds, e.g. Marcionism,
Montanism) and should not be read as a live/admitted registry entry; `cic-poc/frontend/src/data/worlds.ts`
carries no `lpc` entry at all (checked directly).

### OG-3. Doc_08's certification apparatus (`scripts/gen_force_index.py`, `lpc_Force_Index.md`) — Round 8's own HIGH findings stand unfixed, on the record's own terms.

Rounds 5 through 8 of Doc_08's own review history each confirm, explicitly, that **no HIGH
finding touches the forces analysis itself** — the analysis has been clear to proceed to
Doc_09 for four consecutive rounds. What remains open is the generator script and its
certification apparatus. **Round 8** (`Doc08_Round8_Review.md`, 2026-09-15) found **2 HIGH, 5
MEDIUM, 6 LOW, 1 COSMETIC**, all against the generator: a false force-gravity connection
reaching the emitted Index with every guard clean, exit 0 (a notice-tag detector narrowed to
the wrong scope by its own prior fix, so a live correction-notice format in this world's own
Decision Log walks straight through it); a false `CLEARED` review-status claim rendered into
the Index's own Disposition line, caused by a hard-coded character-offset read of a verdict
block; and a wrong connection count (14 reported against Doc_08 §9's own certified 15) after
one dropped table pipe silently removed a row from both the parse and the count in the same
edit. **No Decision Log entry after Round 8 records any of these three findings being fixed
or re-reviewed.** Doc_08 was nonetheless disposed Approved to proceed the same day
(2026-09-15) by direct project-lead instruction, with this precise gap disclosed plainly in
the disposition table itself: *"the Round 8 revision remains unreviewed."* Standing,
disclosed, unfixed defect in build tooling — the forces analysis and Doc_08's own prose are
not implicated.

### OG-4. The 411 Conference *Gesta* — closed as a source question, not an open item, but the reasoning is worth carrying forward explicitly.

Two independent attempts to extract Candidate 5 (G5)-supporting evidence from the *Gesta
Collationis Carthaginiensis* (Donatism's own home-territory source) were each withdrawn as
unsound (Round 5: overstated; Round 6: unsound in a worse way — see `Doc_04_Superseded_Claims.md`
§2). No third read was commissioned, on the project lead's own gapped-formation-precedent
reasoning that a third attempt at the same source for the same purpose is the pattern to
break, not the fix to chase. G5 stands **Supporting** on the project lead's own direct ruling
(2026-09-14), not on *Gesta* evidence, which is "relied on for nothing" in the current text
(`Doc_04_Superseded_Claims.md` §2). This is a closed decision, not an open question — recorded
here, per the discipline `don`'s own OG-4 and `cappadocian`'s own OG-9/OG-10 already model,
because it is exactly the kind of accepted, narrowly-scoped resolution that should be named
rather than silently dropped. **One loose end this review could not independently verify:**
`Source_Registry.md` row 65 (act 158) was, per Round 11's own recommendation (2026-09-14
entry, "Round 11's H2, H3 and H4 applied"), *flagged rather than amended*: "Row 65 is flagged,
not amended. Round 11 recommends appending the explanation to `Source_Registry.md` row 65.
That document is *returned to independent review*; the amendment belongs to that review, and
Open Item 6 says so in terms." Whether row 65 has since been annotated with that explanation (the 2026-09-14 entry quoted above)
was not checked directly in this review.

### OG-5. A recurring citation-locus error across the Representative-construction phases — the same failure class `don`'s own Doc_08 is tracked for, distributed across this world's Representative phases instead of concentrated in one document.

Independently caught once at each of five separate Round 1 reviews: Phase Two (Doc_07 §2D's
three doctrinal bodies misdescribed as one — itself a *repeat* of a defect Phase One's own
Round 1 had already caught and fixed once in a sibling document); Phase Three (Perpetua's
Passion exclusion reason misattributed); Phase Four (Doc_05 §5.4 cited for content that is
actually at §5.1); Phase Six (a follow-up citation-locus fix, the Phase Six pull request of 2026-09-24); Phase Seven (one
MEDIUM finding named explicitly as "a citation-locus error" alongside the four HIGH
findings). None of these individually rises above MEDIUM severity and every instance was
caught and fixed at its own Round 1 — this is not a live defect in any deployed artifact. It
is named here as a standing methodological pattern for whoever next reviews this world's own
documents, the same way `don`'s own Open Gaps file names its Doc_08 pattern: a world whose
Doc_05–Doc_08 span carries a genuinely dense cross-reference web is, on this world's own
evidence, at real and repeated risk of exactly this error class.

### OG-6. Doc_09's Claims Register — the great majority of registered corpus-absence claims remain UNVERIFIED.

At Doc_09's own disposition (2026-09-15): 142 claims derived and registered, with 137 of the
142 remaining UNVERIFIED (registration is the control; verification is separate work). The
most recent count this review could independently locate
(2026-09-16 controls check, part of the Possidius *Vita* ch. VIII correction pass) states 142
claims against 142 register entries, **9** carrying a recorded check — 133 UNVERIFIED, a
small improvement over the disposition-time count. Per the register's own explicit
disclosure, registration establishes that a claim is known and answerable, not that it is
true; most of the 133 are not mechanically decidable (a judgement about a corpus, not a
string search). **Not a defect — an honest, disclosed backlog**, in the same spirit as `don`'s
own OG-11 disclosure. No later Decision Log entry records a further verification pass.

### OG-7. Doc_09's own Tier-3 escalation for `lpcstory006` — a governance/methodology question, named and left open.

CF V7.4 Tier 3's own definition carries two clauses that point in opposite directions for
this specific story: the genus clause ("resting on collected tradition rather than direct
documentation," which would exclude an eyewitness account) and the hagiographic-convention
clause. Named explicitly at Doc_09's own 2026-09-15 disposition as "still a
governance/methodology question for the project lead." No later entry resolves it.

### OG-8. Possidius's *Vita* ch. XIX–XXVII — read at source, not yet built into a story.

Read in full 2026-09-15 (`Review-Artifacts/Possidius_XIX-XXVII_Read_2026-09-15.md`), closing
the reading gap Doc_09's own disposition had named as open. Per Phase Four's own 2026-09-23
entry, this material is still named as one of two open items in Doc_09's story-tier mapping —
"read at source but not yet built into a story." Narrow, disclosed, unresolved as of the most
recent record.

### OG-9. Portfolio-level template and methodology defects Doc_05–Doc_08 are each individually blocked on — inherited, not `lpc`'s own to fix.

Named explicitly at the 2026-09-15 joint disposition entry ("dispose 05 06 07 08"), each
holding a genuine CO-022 escalation category open that the project lead's own direct
instruction disposed around rather than closed:

- **Doc_05** — the *Boundary Structures*/*Boundary Ecology* terminology divergence **inside
  the Constitution and Forces-Framework governing texts themselves** (each contradicts
  itself, not only the other). Ruled `Boundary Structures` canonical *for `lpc` specifically*
  (2026-09-14); the underlying governing-text contradiction is unresolved and, per
  `cappadocian`'s own Open Gaps file, also affects `alx`, `don`, and `cappadocian`'s own
  Doc_05 files, which use the other term.
- **Doc_06** — the LDF Part III Key Texts/Key Sources template mismatch.
- **Doc_07** — the World Profile/Doc_07 template's pre-M4 lens structure. **Unlike `don`'s own
  Doc_07**, which was rebuilt live on the M4 Change Order's Smart seven-dimension spine after
  an explicit escalation, no comparable rebuild or escalation is recorded for `lpc`'s own
  Doc_07 — it was drafted and disposed on the older structure, and this gap is inherited
  rather than closed.
- **Doc_08** — a corpus-wide editorial-apparatus question, of which `lpc` holds eight local
  instances.

"Until those close, every future world jams at the same place. Nothing in `lpc` fixes them"
(2026-09-15 entry, verbatim). All four are named for a coach thread or the project lead, not
this build thread.

### OG-10. The gapped-formation-types ruling is portfolio-level guidance currently filed only inside `lpc`'s own build folder, and has an open, unmerged companion PR.

The Article 3 ruling (2026-09-16, adopted from `lpc_Gapped_Formation_Precedent.md`) *"binds
every gapped candidate"* per its own text, but sits only in `Build/worlds/lpc/`, outside this build
thread's own write scope to relocate — named twice for a coach-thread or project-lead
placement at `world-build-docs/_cross-world/` and routed to
`Review-Artifacts/L3_Methodology_Defects_Coach_Handoff_2026-09-16.md`. The portfolio Step 0
Conclusion document itself still logs the underlying question as "Constitutional ambiguity
flagged, not resolved" — now stale, and not editable by a build thread. Separately,
**`Build/Ministry/Operations/Standing/CiC_GoLive_Pipeline_Status.md`** (its fourth item, checked directly in
this review) confirms **the `lpc` gapped-formation-worlds-precedent pull request** (as of 2026-09-24) is still **open,
doc-only, mergeable clean** — "Mark's to merge or not" — and notes it may itself be
superseded once fully reconciled with the ruling's actual adoption commit (`b20688de`).

### OG-11. No live runtime (M3 sealed-probe / AWS Bedrock) validation has been run for `lpc`.

Phase Five's own 14-probe battery is explicitly disclosed as **simulated** (isolated-subagent
embodiment, scored by a second isolated subagent), the project's own established lower-cost
first pass — Constitution Article 31 names this informational only, not a substitute for
governed live-runtime validation, and the Phase Five disposition itself states plainly: "Not
yet Freeze-eligible on Relational Safety grounds." No entry through 2026-09-24 records a live
Bedrock trial, an M3 sealed-probe run, or even a scheduled next step toward one — the gate
every other live fleet world (`don`, `cappadocian`, etc.) passed at 28/28 before admission has
not yet been reached for `lpc`.

### OG-12. Datus's portrait is committed to the brand-assets source folder but wired to no live-serving location, and its filename does not match the fleet's own stated naming convention — both confirmed directly on disk, neither previously disclosed anywhere in this build's own record.

`Build/Ministry/Communication/Brand-Assets/Representative-Portraits/README.md` states the naming
convention plainly: *"files are named `Name_Portrait.png`."* The committed file, verified
directly in this review, is `Build/Ministry/Communication/Brand-Assets/Representative-Portraits/lpc/Datus_Portrait.jpg`
— `.jpg`, not `.png`. This same drift already exists, disclosed, elsewhere in the fleet — both
`rzg/Theophilus_Portrait.jpg` and `witt/Nikolaus_Portrait.jpg` are `.jpg` against the identical
stated `.png` convention, and `rzg`'s own `Open_Gaps_Tracking.md` names it directly ("kept as
`.jpg`, the actual generated format, not re-encoded"); named here as `lpc`'s own instance of
an already-accepted fleet pattern, not a novel one. More substantively: the 2026-09-15 M1
entry itself named a second serving location the finished image would need,
`cic-website/assets/portraits/`; **this review searched both `cic-website/` and `cic-poc/`
directly and found no file named for Datus anywhere in either tree** (an atlas-level
placeholder page, `cic-website/tree/latin-pastoral-congregational-christianity.html`, already
exists for this world but carries no portrait reference). This is exactly the "approved but
never placed" gap `don`'s
own Open Gaps file names as a precedent to avoid (contrasting its own portrait, which shipped
to `cic-poc/frontend/public/images/portraits/donatism.png` and was wired into
`cic-poc/frontend/src/data/worlds.ts` and `cic-website/traditions/donatism.html` in the same
pass that committed it) — `lpc`'s own portrait has reached the brand-assets source folder but
not yet either live-serving location, and (per OG-2) `lpc` has no world registration or
census entry for either site to wire it into yet regardless. This review found no Decision
Log entry, no Review-Artifact, and no README note disclosing either point. Narrow on its own,
but the kind of small drift this project's own review discipline exists to catch rather than
let compound; named here for whoever next touches the portrait pipeline or `lpc`'s own
eventual site wiring.

### OG-13. Voice Configuration's own PENDING items — disclosed prerequisites, not a gap to close from inside this build.

Model selection, live ElevenLabs audition, and pronunciation-dictionary testing all remain
explicitly PENDING in `lpc_Voice_Configuration_Datus.md` as of its own 2026-09-24 disposition,
because no live ElevenLabs platform access exists in this build thread's own working
environment. This mirrors the only project-wide precedent for the same situation
(`cappadocian_Voice_Configuration_Eumathios.md`). **Not a gap to close** — recorded here for
completeness, matching `don`'s own OG-6 discipline of naming every standing, honestly-disclosed
prerequisite rather than only the ones still in dispute.

### OG-14. The canon-closure pass of 2026-09-25 (Part 8, `wb_lpc_s2z_canon_closure.py`) — an independent Opus fidelity review found the coverage method itself was unsound, not just individual records; the PR is held unmerged pending rework.

2026-09-25: PR #557 added `canon_cells` tags across all 67 pre-existing lpc records
(`wb_lpc_s2y_canon_cells.py`) and closed the fleet's 28 canon cells with 3 new
`doctrinal_witness` and 7 new `honest_limit` records (`wb_lpc_s2z_canon_closure.py`). All
21 M1 gates, including `canon-coverage`, passed clean. An independent Opus fidelity review
(routed through the tech-readiness coordinator thread, per this project's own "a blocking
review finding can't be dismissed by self-certification" rule) found the gates cannot see
what this review did: **the root cause is methodological, not a handful of typos** — each
`honest_limit`'s claimed absence was checked only against `lpc`'s own already-built 67
records, never against Doc_02 or the vendored corpus directly. Six of the seven new
`honest_limit` records are, on independent primary-source verification, contradicted by
material already sitting in this world's own vendored sources:

- **F5-T** (`lpc.limit.wealth-and-marriage-untaught`) — *On Works and Alms* and *On the
  Dress of Virgins* are both in `lpc.source.cyprian-minor-pastoral-treatises` (Doc_02 §1
  names *On Works and Alms* directly).
- **F4-P** (`lpc.limit.the-unquiet-mind-and-the-unrepentant`) — Enchiridion ch. 73 (loving
  the enemy who "wishes you ill"), `lpc.story.the-plague-and-the-enemies`, and Confessions
  I.i.1 ("restless till it rests in Thee") all bear on this cell directly; the review also
  notes this contradicts the same PR's own C-P witness.
- **F4-E** (`lpc.limit.apostolic-origin-undefended`) — On Baptism V.23
  (`cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`, line 13141 —
  **independently re-verified in this thread**: "the custom, which is opposed to Cyprian,
  may be supposed to have had its origin in apostolic tradition") and Cyprian Ep. 73
  ("Whence is that tradition?") both speak to exactly this cell's own question.
- **F3-E** (`lpc.limit.the-outsiders-own-view`) — Cyprian's *Address to Demetrianus*
  answers the pagan charge that Christians caused "wars, famine, pestilence" — a direct
  outsider-accusation response this world's corpus does hold.
- **F2-T** (`lpc.limit.scriptures-own-place-unaddressed`) — Ep. 73 sets scripture over
  custom ("custom without truth is the antiquity of error"); the Genesis-as-science half of
  the cell remains genuinely unconfirmed.
- **F2-P** (`lpc.limit.violence-in-scripture-unaddressed`) — Augustine's *Reply to Faustus*
  XXII.74–79 (`lpc.source.augustine-anti-manichaean-corpus`) directly defends the wars of
  Moses against exactly this charge.
- **C-E** (`lpc.limit.no-chain-of-witnesses`) — only partly wrong: *City of God* XXII.5
  does argue for the resurrection's own credibility, so the record needs narrowing to the
  eyewitness-chain point specifically, not left as a blanket absence.

Separately, and independently re-verified in this thread: the C-P witness's own quotation
("Grant me chastity and continency, but not yet") is verbatim but mis-cited (line
12745–46 of `cic/texts/npnf101_augustine-confessions-letters.xml`, not 12747 as the PR's
own generator script states) and, more substantively, **misrepresents its own context** —
the source frames it as a youth's prayer recalled later ("in the very outset of my
youth"), not a present-tense prayer from someone "already persuaded the truth was true."
The review also found: the C-T and C-I witnesses each need register/accuracy fixes (an
overclaimed "we do not differ from any other church" line ignoring this world's own
Homoian-Vandal/Arian-Maximinus material already in the corpus; a dropped "ascension into
heaven" clause; several sentences over the 25-word style ceiling); a forced `F4-T` tag on
`lpc.term.catechesis` that implies adult-only baptism against the term's own cited
Enchiridion ch. 52 ("not adults only, but infants as well"); a better home for
`lpc.term.compel-them-to-come-in` and `lpc.contested.compel-coercion-development` at F3-P
rather than F6-P; disclaimer-as-crutch phrasing reading as generated; and process
narration in all 10 new record bodies, in `locus` fields, in `why_sources_cannot_answer`,
and in both generator scripts' own docstrings — a direct instance of the standing
live-surface-commentary rule now in `CLAUDE.md`, plus a swallowed-exception pattern in
`wb_lpc_s2z_canon_closure.py`'s own `--validate` mode (`except Exception: registry = {}`)
that could silently hide a real registry-load failure behind an apparently clean run.

**Standing state:** The canon-closure pull request of 2026-09-25 is open, CI green, `mergeable_state: clean`, but **held
unmerged** on the coordinator thread's own explicit instruction — Mark merges this PR
himself after the rework, and any revised quotes/absence claims get independently
re-checked again before that (self-certification does not count, per this project's own
standing rule). Not resolved by this entry — logged per CLAUDE.md's own rule that a review
outcome never lives only in a conversation thread. The rework itself (author substantive
records from the loci above where they hold, narrow claims that are only partly wrong,
fix the two mis-cited/mis-contextualized quotes, retag F4-T, strip the commentary, and fix
the swallowed exception) is a separate, not-yet-started piece of work.

### OG-15. The rework of the canon-closure pass logged 2026-09-25, applied on branch `lpc-record-compilation-part7-witness-limit-ambient` (the same pull request) — every finding checked against the vendored corpus directly, not self-certified; independent re-confirmation still required before merge.

For each of the six contradicted `honest_limit` records, the loci OG-14 named were read
and verified directly against the vendored XML, then either a new `doctrinal_witness`
record was authored from that material or the `honest_limit` was narrowed to the residual,
still-genuine absence — the same choice OG-14's own rework instruction offered:

- **F5-T** — `lpc.witness.almsgiving-quenches-sin` answers the wealth question (On Works
  and Alms); `lpc.limit.wealth-and-marriage-untaught` narrowed to marriage/weddings, where
  On the Dress of Virgins SS18 confirms weddings took place but states no teaching on
  marriage itself.
- **F4-P** — `lpc.witness.restless-heart-and-the-unrepentant-enemy` answers the restless-mind
  and forgiving-an-enemy sub-questions (Confessions I.i.1; Enchiridion 73-74);
  `lpc.limit.the-unquiet-mind-and-the-unrepentant` narrowed to prayer that goes unanswered.
- **F4-E** — `lpc.witness.tradition-tested-by-apostolic-warrant` states both anchor bishops'
  own, differing tests for apostolic origin (Cyprian Ep. 73; Augustine On Baptism V.23);
  `lpc.limit.apostolic-origin-undefended` narrowed to the absence of any named practice
  (catechesis, preaching, reconciliation) actually traced to the apostles.
- **F3-E** — `lpc.witness.blamed-for-the-worlds-troubles` answers the neighbours'-accusation
  sub-question (An Address to Demetrianus); `lpc.limit.the-outsiders-own-view` narrowed to
  catacombs, Constantine, and an outsider's own strangeness-perception.
- **F2-T** — `lpc.witness.scripture-above-councils` answers whether scripture stood above
  bishops and councils (On Baptism II.3.4; Cyprian Ep. 73);
  `lpc.limit.scriptures-own-place-unaddressed` narrowed to the Genesis-as-science question
  alone.
- **F2-P** — `lpc.witness.violence-commanded-not-cruel` answers the cell in full (Reply to
  Faustus XXII.71-79); `lpc.limit.violence-in-scripture-unaddressed` retired, the cell no
  longer needing an honest_limit at all.
- **C-E** — `lpc.limit.no-chain-of-witnesses` narrowed, not replaced, per OG-14's own
  instruction: City of God XXII.5's evidential argument is now stated in the record, while
  the absence of any personal or living chain of witness stands as the genuine, narrower
  finding.

Also from OG-14: the C-P witness's quote re-grounded to Confessions VIII.vii.17 (the youth's
prayer) and VIII.vii.18 (the separate, later persuaded-but-still-unable-to-act moment),
"one of our own founders" removed; the C-T witness's overclaimed "we do not differ from any
other church" line replaced with the Maximinus/Vandal-Arian material, and its sentences
brought under the style ceiling; the C-I witness's dropped "ascension into heaven" restored
and "not merely in a mystical sense" no longer flattened to "not a story"; `F4-T` re-grounded
on `lpc.term.catechesis` with Enchiridion ch. 52 ("not adults only, but infants as well") now
cited, so the cell answers the baptism-mode question rather than only describing adult
catechesis; `lpc.term.compel-them-to-come-in` and `lpc.contested.compel-coercion-development`
retagged from F6-P to F3-P, a direct match to `_fleet.canon.f3-p-02`
("Your church used power against Christians who disagreed. Defend that."), where the earlier
F6-P placement (a hypocrisy question) was a stretch; the swallowed `except Exception:
registry = {}` in `wb_lpc_s2z_canon_closure.py --validate` removed; both generator scripts'
docstrings corrected to the post-rework state and stripped of session-referential narration
and embedded dates (the `iso-date` pattern `tools/check_live_commentary.py` itself flags),
with a note that their own `WITNESSES`/`LIMITS`/`ASSIGN` data blocks are now stale build
history, not to be re-run without first syncing them to the hand-revised live records.

All 21 M1 gates, including `canon-coverage` and `reciprocity` (11 new relations added, both
directions, once the new records' own edges were checked), pass clean on the full lpc + fleet
corpus. `tools/check_live_commentary.py` finds no new findings on any touched file. FK grades
on every new/revised spoken field (`statement`, `text`, `positions`, `tensions`) run 5.0-10.5,
one (`lpc.witness.tradition-tested-by-apostolic-warrant`'s `tensions`) rewritten down from
10.5 to keep the whole set at or under FK 10.

**Not resolved by this entry.** Per CLAUDE.md's own rule, self-certification does not count —
an independent fidelity review of this rework is still required before Mark merges the canon-closure pull request (2026-09-25),
exactly as OG-14 already states. This entry records what changed and why, not that it has
been approved.

---

### OG-16. Round-2 rework of the 2026-09-25 canon-closure pull request, after an independent review found its own round-1 pass of that date had repeated its root cause — absences checked against lpc's own already-tagged records, not against the full set of texts `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` assigns to this world.

Every `honest_limit` and every `doctrinal_witness` sentence claiming an absence ("no
source", "nothing in our record", "neither bishop") was swept against the corpus map's own
assigned texts directly, not only against lpc's own already-built records. Five more
contradicted absences surfaced this round, beyond the four the review named — one from that
same sweep (marriage) plus a Genesis-as-science and a Constantine sub-question the review's
own four items did not individually cover in full. For each, the loci were read and verified
directly against the vendored corpus, then a new `doctrinal_witness` was authored or an
existing one corrected, and the paired `honest_limit` narrowed or, where every sub-question
of its cell is now genuinely answered, retired.

**Contradicted absences fixed:**

- **F5-T** (marriage) — `lpc.witness.marriage-a-threefold-good` (On the Good of Marriage,
  SS7 and SS32: the threefold good of marriage — offspring, faith, sacrament — and its
  indissolubility). `lpc.limit.wealth-and-marriage-untaught` retired: both halves of the
  cell (wealth via `lpc.witness.almsgiving-quenches-sin`, marriage via this record) are now
  answered.
- **F4-P** (unanswered prayer) — `lpc.witness.heard-for-salvation-not-for-wish` (Ten
  Homilies on the First Epistle of John, Homily VI SS6-7: Paul's thorn in the flesh, "heard,
  then, for salvation" though "not heard according to his wish"). `lpc.limit.the-unquiet-
  mind-and-the-unrepentant` retired: all three of the cell's sub-questions are now answered.
- **F2-T** (Genesis as science) — `lpc.witness.days-before-the-sun` (City of God XI.7, the
  first three days before the sun existed; XII.10, rejecting histories that allot many
  thousand years to the world's past). `lpc.limit.scriptures-own-place-unaddressed` retired:
  both of the cell's sub-questions are now answered.
- **F4-E** (apostolic origin) — `lpc.witness.baptism-traced-to-the-apostles` (On Baptism
  II.7.10, non-rebaptism "rightly believed to have been handed down from the apostles";
  IV.24.32, infant baptism "rightly held to have been handed down by apostolical
  authority"). `lpc.witness.tradition-tested-by-apostolic-warrant`'s own closing sentence
  overclaimed that neither bishop traces any specific practice to a named apostolic origin —
  corrected to note this dispute-specific finding is about the Stephen/rebaptism test only.
  `lpc.limit.apostolic-origin-undefended` narrowed, not retired: catechesis, the road back,
  and the teaching before the water remain genuinely untraced.
- **F3-E** (Constantine) — `lpc.witness.constantine-did-not-corrupt` (City of God V.25:
  God granted Constantine's success on purpose, so no one could claim greatness required
  worshipping demons). `lpc.limit.the-outsiders-own-view` narrowed, not retired: catacombs
  and an outsider's own strangeness-perception remain genuinely unanswered.

**Other blocking findings, fixed:**

- `lpc.witness.violence-commanded-not-cruel`'s "Did the violence... trouble our own people?
  No" was false — Confessions III.vii.12 has Augustine's own account of being "much
  disturbed" by scripture's violence, as a young Manichaean adherent before he held the
  faith. Fixed to disclose that youthful trouble alongside the mature, settled answer,
  rather than erasing it.
- `lpc.witness.restless-heart-and-the-unrepentant-enemy` claimed "full pardon... waits on
  the other person's own asking." Enchiridion 73 actually sets two standards: loving an
  unrepentant enemy as the highest calling every believer should strive for regardless of
  the other's repentance, and forgiving from the heart when asked as the ordinary standard
  the Lord's Prayer requires. Chapter 74 addresses only refusing someone who has asked, not
  a claim that pardon must wait on asking. Rewritten to the accurate two-tier structure.
- `lpc.witness.almsgiving-quenches-sin` attributed "As water extinguisheth fire, so
  almsgiving quencheth sin" to Cyprian's own composition ("he wrote"). It is Cyprian quoting
  scripture (Sirach 3:30) — the source text itself says "the Holy Spirit speaks in the
  sacred Scriptures, and says..." Fixed to attribute it as scripture, quoted.
- "Our first/second anchor bishop" (construction vocabulary, not this world's own voice) —
  swept and replaced with "Cyprian"/"Augustine" by name across 17 files (a multiline sweep
  caught several instances split across YAML line-wraps that an initial single-line search
  missed). "Held elsewhere"/"given elsewhere" (record-organisation narration referring
  readers to another file rather than answering directly) — found in one record
  (`lpc.limit.the-outsiders-own-view`) and rewritten to a self-contained answer.

**FK.** Nine round-1/round-2 spoken fields scoring under 7.5 (4.96–7.32) were revised —
combining short, choppy sentences into longer ones that still carry only the original
content — to 7.97–9.58. One new field (`lpc.witness.baptism-traced-to-the-apostles`, 11.35)
was split back down to 9.26. The don precedent's 8–10 target band is met without flattening
any of the content.

**Locus/consistency fixes.** `grant-me-chastity-but-not-yet`'s "not yet" prayer locus
corrected 12745-46 → 12746-47; its second locus (VIII.vii.18) given an exact line (12762),
previously undated. `the-only-son-and-the-trinity`'s Enchiridion 56 locus corrected 21851
(the chapter heading) → 21856 (the actual quoted sentence); its Possidius ch. 17 locus given
an exact line (2942), previously undated. The Cyprian-Epistle-73-to-Augustine-On-Baptism
interval, given inconsistently as "a century" in one record and "a century and a half" in
another for the same two dates (256 CE to ~400/401 CE, ~145 years), standardized to "a
century and a half" in both. `scripture-above-councils`'s opening "Yes" to "did we hold
scripture as our only authority" softened to "Only in a specific sense, not without real
qualification," since On Baptism V.23 elsewhere accepts unwritten universal custom as
carrying real apostolic authority too. `lpc.demo.compel-three-phase`'s `canon_question_id`
(`_fleet.canon.f6-p-05`) and `canon_cells` (`F6-P`) both corrected to `_fleet.canon.f3-p-02`
/ `F3-P`, matching the canon-closure pull request's own (2026-09-25) round-1 retagging of the term/contested_claim records this
demo illustrates — this one record was missed in that pass.

**Change-history narration removed** from record bodies I authored or touched this round —
"Narrowed from an earlier draft that claimed X — false", "corrected here", "F4-T rework
note", and a "this world's own build has been caught by it repeatedly" line in
`lpc.story.hundred-thousand-sesterces`'s `narrative_tier_justification` (which, because it
sat inside YAML frontmatter with no blank-line paragraph break, caused
`check_live_commentary.py`'s change-history-block widening to flag the file's entire
frontmatter as one block). No new commentary was added in its place — the surviving text
states scope and sourcing only. Pre-existing body commentary in files this round did not
otherwise touch (`lpc.demo.road-back-examined`, `lpc.demo.compel-three-phase`'s own
pre-existing body, and roughly 360 other hits across the world) is left for Mark's ruling on
record bodies, per OG-14's own standing note.

**Root-cause fix, `wb_lpc_s2z_canon_closure.py`.** Running the script with no arguments
still called `emit_witness`/`emit_limit` against its own `WITNESSES`/`LIMITS` lists, which
still carried the pre-review text for four `honest_limit` slugs this rework and the canon-closure pull request's (2026-09-25)
own round 1 have since narrowed or retired (including `violence-in-scripture-unaddressed`,
deleted in round 1). A re-run of the bare script would have silently overwritten every
correction. Fixed at the root by retiring the write path entirely rather than re-syncing the
embedded lists yet again: the script now refuses any invocation without `--validate`,
explaining why, and `--validate` itself now returns exit code 1 when any gate reports a
finding (it previously always returned 0, findings or not).

**Verification.** `wb_lpc_s2z_canon_closure.py --validate`: all 21 M1 gates clean (28/28
canon cells: 23 substantive, 5 honest_limit — C-E, F1-E, F2-E, F5-E, F6-P — 0 empty, 0
multiple). `tools/check_live_commentary.py --surface records`: zero hits in every file this
round touched. FK: all round-1/round-2 spoken fields land in 7.60-9.89, matching the don
precedent's 8-10 target band (the two records at 7.60/7.97 sit just under it but were not
part of the review's own "under 7.5" list). Every quote and every new locus re-verified
directly against the vendored `cic/texts/` XML. Branch merged current `main` (was 35 commits
behind at the start of this round; a clean fast-forward-then-merge, no conflicts).

**Residual, disclosed rather than fixed this round:**

1. `wb_lpc_s2y_canon_cells.py --validate` carries the same `except Exception: registry = {}`
   swallowed-exception pattern round 1 removed from `wb_lpc_s2z_canon_closure.py`, and its
   own bare-invocation `apply_assignments()` path was not audited for the same
   stale-data-regeneration risk `wb_lpc_s2z_canon_closure.py` had. Not in scope for this
   round's named findings; worth a future pass.
2. The pre-existing Registry-row-5 citation conflict OG-14 already logged (two different
   works cited under the same row number) is unaffected by this round and remains open.

Full findings, search method, and before/after are in the 2026-09-25 canon-closure pull request's own body.

### OG-17. Round-3 (final) rework of the 2026-09-25 canon-closure pull request, Mark's own personally-authorized targeted round, bar stated as "scholarly rigor that would impress a professor of church history, not perfection."

Six items named directly, plus two residual defects this round's own sweep surfaced beyond
them.

**F4-E (apostolic origin), re-narrowed rather than left overclaiming an absence.**
`lpc.limit.apostolic-origin-undefended`'s own closing line — that the one-episcopate's
undivided character is "a general conviction, not a traced lineage" — was itself
contradicted by four texts the corpus map assigns to this world: Augustine, Letter LIII SS2
(the bishops of Rome named in unbroken succession from Peter to Anastasius, against a
Donatist claim of "episcopal succession"); Answer to Petilian II.51 (the chairs of Peter and
James, and who sits in them "to-day"); Cyprian, Epistle XXVI SS1 ("through the changes of
times and successions, the ordering of bishops... flow onwards"); and Cyprian, Epistle
LXVII SS5 ("the practice delivered from divine tradition and apostolic observance"). All
four independently re-verified directly against the vendored text at the exact lines named
in this round's own brief. A traced lineage for the office of bishop itself does exist in
this world's own corpus — a new `doctrinal_witness`, `lpc.witness.apostolic-succession-of-
bishops`, was authored to carry it, and the limit was rewritten to acknowledge it while
narrowing the residual, genuine absence to catechesis, the road back, and the teaching
before the water. Letter LIII belongs to an 11-letter Donatist-correspondence cluster the
corpus map's own staging file documents but had not yet promoted into the main map or the
Source Registry — promoted this round as Registry row 213 and a new source record
(`lpc.source.augustine-donatist-correspondence`), rather than left unlicensed. Answer to
Petilian's own Registry row (14) and source record were likewise upgraded from "named for
completeness, not drawn on for a specific claim" to a directly-verified locus, since II.51
is now drawn on for exactly that. The limit's own text also said Augustine traces "baptism
itself" to the apostles; the sibling witness record already said "infant baptism" correctly
— the limit now matches it.

**F2-T (Genesis as science), a reversed claim corrected.** `lpc.witness.days-before-the-sun`
said Augustine "rejected... any history that claimed the world was many thousand years
old" — backwards. City of God XII.10 (verified directly, line 22598) rejects histories
claiming *many more* thousand years than Scripture allows, and states Augustine's own
reckoning plainly: "not 6000 years have yet passed." Both `tensions` and `text` fixed to say
this correctly — Augustine held the world was under 6,000 years old, not that he rejected
thousands-of-years claims generally. The record's own source locus, which previously named
only the chapter heading (22565-22568), now also names this specific line.

**F3-E (Constantine), an overstatement softened rather than left standing.**
`lpc.witness.constantine-did-not-corrupt` said "Augustine took up this question directly,
and did not think so." City of God V.25 (re-verified, lines 11099-11122) does not argue
"did Constantine corrupt the church" at all — its own subject is why God granted a
Christian emperor earthly prosperity, so that no one could claim greatness required
worshipping the old gods. Reframed as the nearest material this world's own corpus carries
to the question, not a direct answer to it. The matching line in
`lpc.limit.the-outsiders-own-view` corrected the same way.

**Small, required, fixed.**
- "A century and a third" vs. "a century and a half" for the same 256-to-c.401 gap: OG-16
  had claimed this was already standardized to "a century and a half" — that claim was
  itself incomplete. Nine instances across seven files (`communion-over-separation` x2,
  `answerability-as-ground`, `font-twice-answered`, `two-cities-scale`, `heresy`,
  `transmission-institutionally-dominant-side`, `illegal-to-established-shift` x2) still
  read "a century and a third" (133 years, wrong) rather than "a century and a half" (145
  years, the correct rounding); all nine corrected this round, not just the two the brief
  named directly.
- `lpc.witness.violence-commanded-not-cruel` said Augustine was troubled by "the wars and
  killings scripture reports." Confessions III.vii.12 (re-verified, line 5893-5894) records
  a different, more specific question: "Are they to be esteemed righteous who had many
  wives at once and did kill men, and sacrificed living creatures?" Both instances corrected
  to match the source.
- `lpc.limit.ordinary-interior-life` claimed a blanket absence of any believer's own
  first-person interior experience at the font. Confessions IX.vi.14 (re-verified, lines
  13731-13732) is a real exception — Augustine's own weeping at his own baptism at Milan,
  387, before he held any office, though written down years later, already a bishop.
  Acknowledged honestly rather than left as a false blanket claim; the general finding
  (episcopal mediation, no anonymous or ordinary believer's voice) stands.

**Optional, done where trivial.** The "an earlier draft... corrected here" process
narration at `lpc.demo.compel-three-phase` (line 61) removed, per Mark's own Decision 4.
"Anchor figures" (construction vocabulary) at `lpc.limit.411-gesta-unread` replaced with
"Cyprian and Augustine" by name. Sentence-length trimming not separately pursued this round
beyond what the FK fixes below required — no specific 37-48 word instance was named, and a
blind sweep risked exactly the kind of speculative, ungrounded rewrite this project's own
"no easy fixes" rule warns against.

**Residual defects this round's own verification pass surfaced, fixed rather than shipped.**
1. The new witness record's own `associated-with` edges to `lpc.witness.baptism-traced-to-
   the-apostles` and `lpc.witness.tradition-tested-by-apostolic-warrant` lacked reciprocal
   back-edges (the M1 reciprocity gate caught this). Fixed by adding the back-edges. A third
   pair of edges, to `lpc.figure.cyprian` and `lpc.figure.augustine`, was removed instead of
   reciprocated — no other `doctrinal_witness` record in this world links to either figure
   record directly, and adding the first such edge would have set a one-off precedent rather
   than followed an established one.
2. Several of this round's own edits introduced plain-scalar YAML lines ending in an
   unescaped colon followed by a folded line break, which resolves to "word: word" and
   breaks the parser the same way OG-14/15's own YAML gotchas did. Caught by test-parsing
   every touched file's own frontmatter directly rather than trusting a visual read, not by
   the gate battery (which cannot run at all against unparseable YAML). Six instances fixed
   across five files.
3. Two edits introduced canonical-surface process narration this project's own rule against
   inline review-round references forbids (as logged 2026-09-25: "corrected #557 round 3," in `lpc.source.
   augustine-answer-to-petilian`'s divergence_note/rights_status/docstring and in `lpc.
   witness.constantine-did-not-corrupt` and `lpc.witness.days-before-the-sun`'s own
   docstrings) — caught by `check_live_commentary.py`, not self-caught, and removed.
4. Two `honest_limit` statements (`apostolic-origin-undefended`, `ordinary-interior-life`)
   scored FK 10.2-10.8 against this round's own longer, more qualified sentences — above the
   readability gate's ceiling of 10. Both rewritten to shorter sentences carrying the same
   content; re-verified at 6.1 and 8.8.

**Verification.** All 21 M1 gates clean (`engine.m1.gates.run_all`, including
canon-coverage). `tools/check_live_commentary.py --surface records`: zero REWRITE hits in
every file this round touched (remaining hits in touched files are pre-existing
`doc-ref`/`section-ref` content in `force/` records belonging to the 2026-09-25 re-voicing pull request's own scope, not
introduced this round, and left untouched per this round's own "touch nothing else"
instruction). Every quote and every new locus re-verified directly against the vendored
`cic/texts/` XML, including the four apostolic-succession sources named in the brief and the
Confessions III.vii.12 and IX.vi.14 loci. Branch merged current `main`.

**Not in scope this round, disclosed rather than silently skipped.** The OG-numbering
collision this build's three parallel unmerged branches (the canon-closure, re-voicing and quote-rendering pull requests, all 2026-09-25) each carry —
this branch's own four canon-closure entries number a different entry than the re-voicing pull request's own first entry — is
unresolved here, per this thread's own standing instruction to disclose rather than guess a
resolution, reserved for a later reconciliation pass.

---

### OG-19. Re-rendered all 5 of `lpc`'s quote `modern_rendering` fields under the V1.5 rendering-fidelity standard (`engine.m1.rendering_fidelity`'s own "translation, not summation" rule).

**What was checked.** Every `quote` record in `lpc` with a non-empty `modern_rendering` (5 of
5) was checked clause-by-clause against its own `text` field for the V1.5 standard: a
rendering must carry every clause of the original into modern English, nothing left out,
nothing added, nothing compressed into a shorter paraphrase that drops real content. `text`
itself was not re-verified against the vendored corpus in this pass — all 5 records already
carry `verification_state: verified-direct`, and rendering fidelity is a distinct question
from source-verbatim fidelity (the same distinction `rendering_fidelity.py`'s own docstring
draws). The live Haiku grader that module uses could not be run in this build environment (no
`boto3`/Bedrock access here) — this check was done by direct clause-by-clause reading instead,
the same discipline the grader formalizes.

**All five `modern_rendering` fields are authored by an Opus subagent**, per CLAUDE.md's own
rule that any `modern_rendering` is Opus-authored, never Sonnet. Every clause of every
rendering was independently re-checked by this thread against its own `text` field before
applying, and FK was independently re-verified directly with `engine.m1.fk.fk_grade` rather
than trusted from the subagent's own self-estimate.

**Current state, all 5 records, clauses verified complete against `text`:**

1. **`lpc.quote.bishop-of-bishops`** — carries "according to the allowance of his liberty and
   power," "can no more be judged by another than he himself can judge another," and "of
   preferring us in the government of His Church" in full. FK 8.34.
2. **`lpc.quote.ancient-venom-against-my-episcopate`** — carries "mindful of their conspiracy"
   and "sacrilegious machinations with their accustomed craft" ("with their usual cunning,"
   matching "accustomed" without overstating it into "have always used," which implies an
   unbroken permanent habit the source does not claim). FK 8.10.
3. **`lpc.quote.longing-expectation-is-a-prayer-for-me`** — carries the source's own hedge,
   "I imagine" (not the stronger, unhedged "I know"), and adds nothing beyond the source (no
   invented clause). The long first sentence is split after "who want to hear." into its own
   sentence beginning "So I am not speaking...", matching the source's own two distinct
   thoughts rather than running them together. FK 4.42 for the split version — genuinely low
   for this short a quotation, not a defect; a single-sentence alternative was not used because
   it re-merges the two thoughts the split exists to separate.
4. **`lpc.quote.clamour-and-tears`** — stays in Possidius's own third-person narration ("The
   Catholics... laid hands on him... they demanded it"), not recast into first person. The
   clause "because all of them, with one accord, wanted this done and carried through" restores
   the source's own causal "for" and its sense of active desire ("desired"), which an earlier
   version had lost by splitting the sentence and weakening "desired" to "agreed." Restoring
   the causal link produced a 33-word sentence carrying two ideas; split into "...brought him
   to the bishop to be ordained. They did this because all of them, with one accord, wanted it
   done and carried through." — every sentence now 20 words or fewer. The record's own
   `divergence_note`, which illustrates the OCR-artifact fix, uses the same third-person
   phrasing ("they demanded it...") for internal consistency. FK 7.50.
5. **`lpc.quote.shepherd-wounded-in-the-flock`** — carries "I share in the grievous burden of
   sorrow and mourning" and keeps "my own integrity and my personal soundness" as two distinct
   qualities. Follows the source's own three sentence breaks: "I wail with those who wail, I
   weep with those who weep..." is its own sentence, not joined to the previous one with "and."
   The sentence "My own integrity... when his flock is wounded" ran 30 words and joined two
   ideas with "because"; split at the point corresponding to the source's own "since" into "My
   own integrity and my personal soundness do not lure me into soothing my griefs. That is
   because it is the shepherd who is wounded most deeply when his flock is wounded." — every
   sentence now 20 words or fewer. FK 4.74.

**A locus correction, `lpc.quote.longing-expectation-is-a-prayer-for-me`.** The record's own
`sources[].locus` field said the sermon was "delivered at the matins of the Nativity
festival." Checked directly against the source (`npnf106...xml`, line ~9398): the sermon's own
opening says the opposite — at matins, Augustine deferred the very question this sermon now
resolves ("it was in the matins of the festival of the Lord's Nativity, that I put off the
question which I had proposed for resolution"). This sermon was delivered some time after
that matins service, not at it. Fixed in both the `sources[].locus` field and the docstring.

**Protected fields.** Only `modern_rendering` was touched in all 5 records (plus the one
`divergence_note` cross-reference in `lpc.quote.clamour-and-tears`, and the one
`sources[].locus` correction in `lpc.quote.longing-expectation-is-a-prayer-for-me`, both noted
above). `text`, `speaker_or_author`, `confidence`, `retrieval`, and every other field are
byte-identical to before this pass — confirmed by diff review, not by intent alone.

**Verification.** `engine.m1.gates.run_all`: all 21 gates clean except the pre-existing,
out-of-scope `canon-coverage` gaps. `tools/check_live_commentary.py --surface records`: zero
hits in any of the 5 touched files. FK grade on all 5 final `modern_rendering` fields:
`bishop-of-bishops` 8.34, `ancient-venom-against-my-episcopate` 8.10,
`longing-expectation-is-a-prayer-for-me` 4.42, `clamour-and-tears` 7.50,
`shepherd-wounded-in-the-flock` 4.74 — all under the readability gate's ceiling of 10; the two
low scores are the honest result for genuinely short, now fully split quotations, not a
defect.

---

## Closed items — verified in this review, not merely inherited from the Decision Log

**Datus's portrait — committed, contra a still-live impression the M1 decision entry alone
would give a reader.** The 2026-09-15 identity decision named the portrait "not committed" as
an open item. The 2026-09-21 branch-reconciliation entry records it merged from a stranded
branch (`mchadwick25-droid-patch-1`) to `Build/Ministry/Communication/Brand-Assets/Representative-Portraits/lpc/`.
**Independently confirmed present on disk in this review**: both `Datus_Portrait.jpg` and
`Datus_Portrait_Prompt.md` exist at that path (see OG-12 above for the one residual naming
discrepancy this check surfaced).

**Article 29, Living Tradition Status — CONFIRMED, 2026-09-16, flag true, statement
adopted.** The project lead confirmed the mechanism (Facilitator-carried, not
Representative-carried — Datus stays temporally bounded and holds none of it, following
Alexandria's own confirmed precedent) earlier the same day, then confirmed Article 29 itself
directly: *"confirm true and adopt the draft."* `living_tradition_flag: true`; the
distinguishing statement at `Review-Artifacts/Living_Tradition_Distinguishing_Statement_DRAFT_2026-09-16.md`
is now in force, not draft. **This world's freeze-eligibility gate on this specific axis is
discharged.** Article 31 external scholarly review is a separate gate and remains untouched
by this — no entry in this build's own record claims it has occurred, matching the standing
every other live fleet world carries per `cappadocian`'s own OG-4.

**Article 3, gapped-formation-types, as applied to `lpc` specifically — CLOSED,
2026-09-16**, by the project lead's direct ruling adopting `lpc_Gapped_Formation_Precedent.md`
§3's own test. *"`lpc` is one formation world."* The identical question at the portfolio
level (whether any gapped candidate may recur across a temporal interval at all) remains open
in the sense that its portfolio-level filing is still pending — see OG-10.

**Candidate 5 / G5 classification — CLOSED (Supporting), 2026-09-14/15**, after five
supersessions across nine review rounds, by direct project-lead ruling and the gapped-formation
precedent's own "five re-classifications is the stop signal" rule — closed by ruling, not by
further evidence, and recorded as such rather than presented as an evidentiary resolution.

**Phase Seven's own §6.3 open item (the liturgical-richness/deployed-artifact integration
gap) — CLOSED, 2026-09-24**, by the World Context Layer chunks 001–005, which route the depth
to the retrievable context layer per that layer's own architectural purpose, rather than
reopening or patching the already-disposed Permanent Prompt and World Capsule Core.
Independently verified: `lpcctx001`–`lpcctx005` all exist on disk at `Build/worlds/lpc/`.

**The `rights_status` fleet-wide internal-narration defect (the 2026-09-20 library data integrity pull request, `e5a50654`) — does not
apply to `lpc`.** That fix targeted `records/<world>/source/*.md` files across `don`,
`cappadocian`, `gallic`, `rzg`, and `witt`. `lpc` has no `records/lpc/` directory at all (see
OG-2), so it carries no `rights_status` fields to have been affected — confirmed directly by
the absence of the directory, not by a clean sweep of it.

**OG-1, the Datus portrait-object silhouette collision with Theon and Albina — RESOLVED,
2026-09-24, by the project lead.** Presented directly with the three options this file's own
OG-1 entry above names — (a) keep the certificate and record the collision, (b) substitute
the ransom purse of `lpcstory004`, (c) drop the object as Fidelis resolved — **the project
lead chose (b), the ransom purse.** Reasoning given: it resolves the Theon/Albina collision
outright, and unlike (c), it preserves the held-object-vs-empty-hands lever that separates
Datus from Fidelis, the sharpest visual adjacency in the fleet, which dropping the object
would have re-opened. Applied to `Datus_Portrait_Prompt.md` the same day: the certificate
marked superseded (not rejected on source-fidelity grounds — it remains a true, attested
object; it is superseded solely by the silhouette constraint), grounded instead in Cyprian's
*Epistle* LIX (the hundred thousand sesterces sent to the Numidian bishops for captives'
ransom — G3 and G1, not G2/G8), and a correction recorded in the same edit: the prompt file's
own prior dismissal of the purse as reading "generic almsgiving" was not accurate to
`lpcstory004`'s source, which is a specific, checkable act of collegial obligation, not
generic charity. **Image regenerated and committed, 2026-09-24, closing the last open piece
of OG-1.** `Datus_Portrait.jpg` now depicts the purse, generated from the corrected prompt in
`Datus_Portrait_Prompt.md` Part Four (the prompt-update pull request, 2026-09-24) via Gemini, external to this thread's own
tooling, and reviewed and approved by the project lead directly against that prompt before
being committed. The prompt's alt text is updated to match and its provisional flag lifted.
OG-1 is now fully closed — decision, prompt text, and image all agree. OG-1's own original
entry above is left as written, per this file's
append-only discipline; this closing note is the record of its resolution.

**Article 31 (external scholarly review) — this file's own repeated framing was wrong, and
is corrected here.** OG-2 above and the Phase Five entry both describe Article 31 as a still-
live gate lpc has "not yet reached" and treat it as parallel to OG-11's genuine open item
(no live Bedrock validation run). **It is not a live gate.** Per Mark's own direct, dated
rulings — `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, 2026-07-21 ("Article
31 external scholarly review: reworded to aspirational, no longer a go-live dependency...
we will readjust or wording to be aspirational but no longer a dependency to go live. still
fully transparent") and 2026-08-02 ("we are setting this as a year 2 project... Article 31 is
reset as an aspirational goal in year two of the 5 year timeline") — **Article 31 is
provisional-by-design and non-blocking through freeze and admission, for every world in the
fleet, `lpc` included.** `cappadocian`'s own OG-4 already states this correctly ("outstanding,
and (per Mark's standing ruling) non-blocking... the same standing every other live fleet
world carries"); this file's own OG-2 and Phase Five entries did not, and neither did the
2026-09-16 M1-consequences entry or the 2026-09-23 Phase Five entry in `lpc_Decision_Log.md`
— all corrected by cross-reference here rather than by rewriting those dated entries. **What
this does not change:** the Article 35 simulated-review labeling requirement stays in force
(every AI-run review round is still marked "Simulated review — informational only, not an
Article 31 substitute") — what changed is only whether Article 31 blocks go-live, not whether
reviews must disclose that they aren't it. **What this also does not touch:** OG-11 (no live
AWS Bedrock / M3 sealed-probe validation run against lpc's own artifacts) is a genuinely
separate, still-real, still-open technical gate — internal live-model validation, not human
external scholarly review — and nothing about it is resolved by this correction.

---

## Project-lead decisions, dated (summary index)

*(Full context for each is in the build-log and Representative sections above; this is a
flat, dated index for quick reference, matching the Alexandria model's own convention.)*

- **2026-09-01** — "Orthogonality to state power": method instruction (report what the
  sources document, including change over time, rather than manufacture a single theory).
- **2026-09-02** — *Codex Theodosianus*: reference-only (OTA, CC BY-NC-SA), then a second,
  fully vendored public-domain copy supplied directly (The Latin Library).
- **2026-09-02** — Cross-world "Library Build Engine" thread commissioned (portfolio-level,
  logged in `lpc`'s own thread for provenance only).
- **2026-09-03** — Merge `lpc`'s branch with the shared cross-world library engine on `main`.
- **2026-09-08** — Banner-stripping standing rule adopted for this world's own build
  documents (Doc_02 first, then extended to `Source_Registry.md` and
  `Source_Acquisition_Manifest.md`).
- **2026-09-09** — Doc_03 self-disposed to Approved to proceed on direct instruction (no
  terminal clean review).
- **2026-09-09** — Registry Round 26/rows 65 and 44 reopened, then, via relay-channel
  triggers, disposed to Approved to proceed on the substance of Round 29's own findings
  (not a clearing review).
- **2026-09-12** — A scoped Round 30 directed (not a full round, not an unreviewed close),
  cleared, Doc_02/Registry self-disposed.
- **2026-09-14** — Candidate 5 (G5): ruled **Supporting**, ending five supersessions across
  nine rounds.
- **2026-09-15** — Doc_04 approved "with the escalation carried open," then, the same day,
  the four Round 11 HIGH findings confirmed closed and Doc_04 formally **CLEARED — "no
  twelfth round."**
- **2026-09-15** — Doc_09 approved, "with the escalation carried open," and the build moved
  to full auto.
- **2026-09-15** — "dispose 05 06 07 08" — all four approved to proceed by direct
  instruction, each still carrying an open, inherited, portfolio-level escalation category.
- **2026-09-15** — Representative identity and image (M1): **Datus, Bishop of the Kept
  Flock**, certificate of peace, painterly oil portrait — decided as one packaged choice.
- **2026-09-16** — Possidius *Vita* ch. VIII ruling: corrects Doc_01 §2's congregational-consent
  finding — six documents named at the ruling, **eight found and fixed** once a second sweep
  caught two more stating the same caution in different words (three verification passes
  before propagation was confirmed).
- **2026-09-16** — This world's three names ruled: `world_id` `latin-pastoral-congregational`,
  `display_name` "Latin Pastoral-Congregational Christianity," `card_name` **"The Ordinary
  Church."**
- **2026-09-16** — Article 3 (gapped formation-types) ruling adopted for `lpc`.
- **2026-09-16** — Living Traditions mechanism: Facilitator-carried, not Representative-carried
  (*"im ok if the facilitator handles it, it solves my tention"*).
- **2026-09-16** — Article 29 confirmed: *"confirm true and adopt the draft."*
- **2026-09-19** — World Profile approved to proceed, on direct instruction — the build
  thread's own earlier self-application of this disposition (2026-09-16) was explicitly
  refused as self-approval.
- **2026-09-21** — Branch reconciliation approved (branch `lpc-reconcile-branches`, pushed to
  `origin`; this review could not independently confirm a specific PR number for it — a particular PR number
  appears once elsewhere in the log, in an unrelated 2026-09-23 entry's parenthetical listing
  several PR numbers together, and is not itself confirmation) — portrait merged into place;
  registration explicitly **not** done, routed back to the project lead.
- **2026-09-23 to 2026-09-24** — RCF V3.2 Phases One through Seven, Representative Artifact
  Construction, World Context Layer, and Voice Configuration each drafted, independently
  reviewed, and self-disposed by the build thread per CO-022 (no escalation category
  triggered at any of these steps).

### OG-18. Re-voiced the `name`/`description`/`manifestations` fields on all 25 gravity/force records and the four `world_core` spoken fields (`horizon`, `formation_logic`, `thinness`, `cautions`) — build vocabulary stripped, every fact and disclosed uncertainty preserved; several residual items surface as a result and are logged here rather than fixed in the same pass. Renumbered from this branch's own original number to OG-18 (round 3 of the re-voicing pull request, 2026-09-25) to avoid colliding with the canon-closure pull request's own four entries of the same date, since the two branches numbered independently off the same base — per the managing thread's own instruction, using the next free number after that pull request's highest.

All 8 `records/lpc/gravity/*.md` and 17 `records/lpc/force/*.md` records carried heavy
construction-process vocabulary directly in their spoken fields: `Doc_04 §3 Candidate N`,
`Doc_08 Cell 2A Force 2A-3`-style codes, `Registry row N`, ALL-CAPS section headers ("LAYER 1
— HISTORICAL EVENT", "CONFIDENCE/GRAVITY CROSS-CHECK", "FORCES-CONNECTION"), six-test names
used as bare labels, gravity/force shorthand (`G1`–`G8`, `1A-1`, `2B-4`), and `[PRIMARY]` /
`[SUPPORTING]` / `[TENSIONAL]` tags embedded in eight gravity records' own `name` fields. The
`world_core` record's `horizon`, `formation_logic`, `thinness`, and `cautions` — compiled into
every participant turn — carried the same pattern at far greater density (up to ~970 words per
field), plus governance-article citations (`Article 21`, `Article 33`), `CONFIRMED by the
project lead`-style build-process framing, and ALL-CAPS numbered caution items.

Every field was drafted by an Opus subagent working from the exact original text, reviewed line
by line against that original, and checked directly: every substantive fact, name, date,
confidence distinction, and disclosed uncertainty was required to survive in plain language: only
the analyst scaffolding was stripped. `lpc.gravity.pastoral-office-flock-keeping`'s Letters XXXI
and CCXIII are both Augustine's own — both independently verified directly against
`cic/texts/npnf101_augustine-confessions-letters.xml` (Letter XXXI, "To Paulinus and Therasia,"
lines 25749-25988: "the greater burden of sharing the episcopate... the importunity of the
people"; Letter CCXIII, "Augustin Designates his Successor," line 55243). Cyprian's own account
of coming to office is carried separately by the 256 Council preface and Pontius's narrative,
already named in the same record. A quotation about a corrupted letter given inconsistently
between a record's own `description` and `manifestations` fields was resolved to the fuller
wording and independently verified against
`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`. Seven further leaked confidence-grade
predicates ("is/are Documented", used as project vocabulary rather than plain description) and
one `§`-symbol section reference were found and rewritten during a second `check_live_commentary.py`
pass, after the first pass and full re-voice were already applied.

**Verification:** all 21 M1 gates run directly (`engine.m1.gates.run_all`) against the real lpc +
fleet corpus, including `reciprocity`, `quote-verbatim`, and `quote-mark-fidelity` — clean, with
only the pre-existing `canon-coverage` gap (lpc's `canon_cells` tagging pass lives on the
still-unmerged canon-closure pull request branch (2026-09-25), not on `main`, so this branch does not carry it and canon-coverage
findings here are expected, not caused by this pass). `tools/check_live_commentary.py --surface
records` — zero new findings on any touched file after the second pass; remaining hits on these
25 gravity/force files and the one `world_core` file are all in fields this pass was explicitly
scoped to leave alone (`divergence_note`, `sources[].locus`, `thin_topics`, and the closing
docstring below each record's own frontmatter). FK grade on every re-voiced field: gravity/force
`description` ranges 6.6–10.5 (three fields 10.02–10.47, close to but not strictly under the
FK-10 target, matching the established precedent for this exact fix on `don`'s own equivalent
pass, where several fields landed 10.02–10.78 and were treated as acceptable rather than
blocking); `world_core`'s four fields range 7.85–8.79, closely matching `don`'s own mean of 8.81.

**Residual items, named rather than quietly left, per this fix's own instruction to move
six-test and provenance material out of the spoken field and log what it leaves behind:**

- **Dangling `sources[].locus` pointers.** Most of these 25 records' `sources[]` entries read
  `locus: see this record's own body text for the specific locus Doc_04/Doc_08 cite` — written
  when the `description` field itself still carried structured `Doc_04`/`Doc_08` citations.
  After this pass, `description` no longer carries pinpoint citations in that form, so these
  `locus` pointers now point at prose that does not resolve them. Not fixed in this pass, which
  was scoped to the three spoken fields only; a follow-up pass should either restate each
  `locus` with its own real citation or point it at the `divergence_note`, which still carries
  the structured citations this pass left untouched.
- **A pre-existing Registry-row citation conflict, found rather than caused by this pass.**
  Before this rewrite, `lpc.gravity.preaching-and-catechesis` cited "Registry row 5" for
  Cyprian's *De Dominica Oratione*, while `lpc.force.plague-of-cyprian` and this same gravity
  record's own `manifestations` cited "Registry row 5" for *De Mortalitate* — two different
  works under one row number. Direct check against `Build/worlds/lpc/Source_Registry.md` finds row 5
  is neither: it is Cyprian's *Ad Quirinum*. This pass drops the row citations from both spoken
  fields (consistent with stripping Registry references generally), which makes the conflict
  moot for participant-facing text, but the underlying registry mis-citation in these records'
  own `divergence_note`/`sources[]` fields is untouched and should be corrected in a citation
  pass.
- **`world_core`'s `thin_topics` notes still carry build vocabulary** ("this build has not
  answered", "the Affirmative Duty's own bounded-reconstruction test has not yet been run") —
  named as out of scope by the drafting agent and left untouched here, since the task this pass
  was scoped to named only `horizon`/`formation_logic`/`thinness`/`cautions`. Worth a same-pattern
  pass if `thin_topics` is itself a spoken field compiled into participant-facing prompts.
- **The eleventh `cautions` entry (the note that the record this world rests on was itself under
  independent review at the time of compilation) is restored**, as the eleventh, with the shame/
  self-forgiveness item renumbered to 12. Checked directly against `Source_Registry.md`'s own
  current header rather than assumed: that review was returned to 2026-09-13 and, as of this
  entry, **has not yet returned** — the caution's own standing content is current, not stale.

**A second independent review of this same pass found further defects, fixed in place rather
than layered as a separate entry, since they correct this entry's own earlier work rather than
add new work:**

- Two lines quoted an internal construction document as though participants were hearing the
  world's own words: `pastoral-office-flock-keeping`'s "In the words of this world's core
  identity... 'pastoral and sacramental before it is juridical'" and
  `conciliar-authority-theory`'s "'between two bishops at two moments separated by over a
  century.'" Both now state the same content directly, without quoting or naming the internal
  document.
- Six places credited this compilation's own reading or reasoning to "the world" itself, as
  though the world were the one asserting it: the 133-year-silence force's "No primary source
  this world names" and "this world's own limits forbid that"; `world_core.thinness`'s "nothing
  this world says yet draws on them"; `cautions` seventh entry's "Nothing this world says rests on
  which version came first" (literally incoherent, since De Unitate *is* something this world
  says); `cautions` ninth entry's "this world still dates the Conference"; `cautions` sixth entry's
  "this world's own premises"; and `collegial-communion-preserved`'s "The world's coherence...
  rests on this gravity." All six now read as "our own reading" / "we" / "our own account."
- "Survives only in Latin" (`transmission-institutionally-dominant-side` and
  `corpus-outliving-the-world`, in both `description` and `manifestations`) mischaracterized
  Registry row 209: the row states only that this corpus holds no English translation of the
  Retractationes, not a claim about the work's own historical survival. Both records now say
  that directly.
- The word "gravity" itself, and its own six-test vocabulary, still leaked into spoken text
  well past the `[PRIMARY]`/`[SUPPORTING]`/`[TENSIONAL]` tags the first pass already removed:
  all 8 gravity records opened with "A primary/supporting/tensional gravity," `conciliar-
  authority-theory` still narrated its own reclassification history and quoted "the forces
  framework" by name, and "gravity" recurred as a bare noun in `illegal-to-established-shift`,
  `manichaeism-and-pelagian-anthropology`, `plague-of-cyprian`, `standing-legal-condition-
  unlicensed-religion`, and `penitential-discipline`. Rewritten to describe the same
  claims — how central a concern is, how it was weighed, how confident the evidence is — in
  plain language, without naming the project's own classification method. **This claim was
  itself incomplete at the time it was first written**: a third review (see below) found
  "gravity"/"gravities" still present roughly 20 times across the 8 gravity records'
  `description` and `manifestations` fields, `penitential-discipline` alone carrying 5 of
  them. All are now removed; a direct field-by-field re-sweep after the fix confirms zero
  remaining instances anywhere in the 25 gravity/force records or the four `world_core`
  fields. "Anchor" (`anchor bishop`, `anchor voice`, `anchor controversies`) was swept from
  `world_core`'s `horizon`, `thinness`, and `cautions` the same way.
- `world_core.thinness`'s "The rites themselves have never been read as evidence in their own
  right" turned a limit of this compilation into a claim about all scholarship; restored to
  "We have not yet read the rites themselves as evidence in their own right."
- `decian-persecution-libelli-system` had flattened two sources of different citation grades
  (the Epistles, A; De Lapsis, B) into one undifferentiated "documented"; the distinction is
  restored in plain language, matching the pattern already used elsewhere in this pass.
- `confessors-claim-to-grant-peace`'s "This force is the world's defining tension" overstated
  its own finding; corrected to "the one tension of its kind in this world's record."
- Stock phrasing repeated across many records without variation — "To the world itself"/"For
  this world," (9 instances), "One caution was flagged/disclosed from the start" (4), "There is
  no confidence gap" (4) — was individually reworded so the same claim is not stated in
  identical language file after file. **This claim was also incomplete**: a third review found
  `grace-and-human-incapacity` still carried the literal sentence "There is no confidence gap
  for the gravity within Augustine's phase," unreworded. Fixed to "Within Augustine's own
  phase, that carries no confidence gap of its own" (also clearing the last "gravity" instance
  named above).
- Four fields sitting well under the FK 8–10 target (`vandal-invasion-siege-of-hippo` 6.64,
  `corpus-outliving-the-world` 6.81, `inherited-latin-theological-vocabulary` 7.08,
  `illegal-to-established-shift` 7.46) were lifted to 7.9–9.1 by combining short sentences
  that carried the same content, not by adding or cutting anything.
- The Possidius quote "under compulsion and constraint" (`congregational-acclamation-
  overriding-preference`), flagged as unverifiable, was checked directly against
  `cic/texts/possidius_vita-augustini_weiskotten1919.txt` and found verbatim at lines 2142-2143
  — hyphenated across a line wrap in the source file ("under com-/pulsion and constraint"),
  which is why an unbroken-phrase search missed it. Not a fabrication; the record's own vague
  `locus` field ("see this record's own body text") is now replaced with the exact line
  citation.

**Re-verification after these fixes:** all 21 M1 gates clean (only the pre-existing, expected
`canon-coverage` gap on this branch, same as before); `tools/check_live_commentary.py --surface
records` clean on every touched field; FK grade across all 25 gravity/force `description` fields
and the four `world_core` fields now runs 7.4–10.5, with the four previously-low fields lifted
and no field newly pushed out of range.

**A third independent review (this round, round 3 of the 2026-09-25 re-voicing pull request) found further residue from the
second pass's own fixes, corrected in place rather than layered as a new entry:**

- `conciliar-authority-theory`'s own description still narrated its reclassification history
  and the project lead's own ruling ("It was placed in different categories several times...
  rests on a direct decision by the project's own lead"), merely paraphrased rather than
  removed. Rewritten to state only the plain uncertainty about the underlying historical
  claim: that both formulas are solidly attested, but the evidence for their organizing
  breadth is thin.
- The "gravity"/"There is no confidence gap for the gravity" false-claim corrections above.
  A genuinely exhaustive re-sweep this round (parsing each record's actual YAML field values
  directly with `yaml.safe_load`, not a line-based `grep`, after two prior grep-based sweeps
  both missed real instances) found and fixed 24 total "gravit" occurrences across 6 gravity
  records' `description`/`manifestations` fields: `collegial-communion-preserved` (3),
  `grace-and-human-incapacity` (4), `pastoral-office-flock-keeping` (2),
  `penitential-discipline` (5: 4 in `description`, 1 in `manifestations` -- matching the ×5
  the review named), `preaching-and-catechesis` (6: 5 in `description`, 1 in
  `manifestations`), `sacramental-ordination-validity` (4). Zero force records were affected;
  the two prior sweeps' method (line-based `grep` with type filters) is the likely cause of
  the earlier miss, since a YAML-aware parse catches every instance directly.
- New stock sentences the second pass's own fixes had introduced, not caught by that pass's
  own review: "This is one of this world's central concerns." (the gravity-record opener,
  ×3: `collegial-communion-preserved`, `penitential-discipline`,
  `sacramental-ordination-validity`), "This is a real concern in this world, though a
  narrower one." (×2: `grace-and-human-incapacity`, `preaching-and-catechesis`), "...worth
  naming..." (×4: `conciliar-authority-theory`, `confessor-authority-vs-episcopal-peace` ×1
  each in two places, `grace-and-human-incapacity`, `penitential-discipline`), "...thinly
  sourced..." (×3: `confessor-authority-vs-episcopal-peace`, `penitential-discipline`,
  `sacramental-ordination-validity`). Each instance reworded individually rather than replaced
  with a second small set of repeated templates.
- `world_core.cautions` sixth entry's "A firm classification looks reachable from our own
  premises" — "classification" is the project's own build vocabulary (matching gravity
  records' own `classification: primary/supporting` field); reworded to "A firm answer looks
  reachable from our own premises, but it has not been settled."
- Non-blocking items also fixed: `thinness`'s "independently checked for this world" reworded
  to match main's own "verified in this build for this world" phrasing;
  `conciliar-authority-theory`'s closing "one our own picture of that world stays incomplete
  on" reworded to "leaves our own picture of that world incomplete here." `thinness`'s "any
  confirmed world so far" was first reworded to "of any world in this record," which a later
  recheck correctly flagged as no longer a real comparison (the record describes one world, so
  comparing it to "any world in this record" is circular) — fixed to "of any world we have
  built so far," restoring the comparison against the other worlds this project has built.

**Re-verification after this round's own fixes:** all 21 M1 gates clean (same pre-existing,
expected `canon-coverage` gap). A direct YAML-field parse (not `grep`) across all 25
gravity/force records and the four `world_core` fields confirms zero remaining "gravit"
instances and zero remaining instances of any of the four flagged stock phrases.
`tools/check_live_commentary.py --surface records` clean on every field this round touched.

Logged here per the standing rule that a review outcome, or a fix that surfaces further items,
never lives only in a conversation thread or a PR description.

### OG-20. `Source_Registry.md` has never run the V7.4 field-bibliography sweep proper; row 33's Confidence letter has not been decided against the same standard rows 30–32 now carry — both stated in the Registry's own saturation section, neither previously carried into this ledger.

Logged 2026-09-26, during the fleet-wide live-surface-commentary cleanup pass (`tools/check_live_commentary.py`), which found both items stated inline in `Source_Registry.md` without a corresponding entry here.

**Item one — the sweep.** `Source_Registry.md`'s own saturation section discloses plainly: the ten-item relative-recall test and PRESS question (CF V7.4's own Doc_02 review requirement) ran for the first fourteen review passes and found the same underlying gap fourteen independent ways, but this is a recall check against specialist bibliographies, not the broader field-bibliography sweep V7.4 assigns to Step 2 itself. That broader sweep has never been run, on this document's own account (`Doc_02_Source_Ecology.md` §9 carries the same disclosure). Not a defect — an honest, disclosed limit on how far this Registry's own claim to completeness reaches, in the same spirit as OG-6's Doc_09 claims backlog.

**Item two — row 33's Confidence letter.** Rows 31 and 32 (Lancel; Burns, *Cyprian the Bishop*) were independently WebSearch-re-verified and sit at Confidence B on the pattern "bibliographic details confirmed, not independently read." Row 33 (Burns & Jensen, *Christianity in Roman Africa*) received the same WebSearch verification on the same date (`lpc_Decision_Log.md`, 2026-09-02) but was left at Confidence C, because a Confidence-rating change is one of the four things CO-022 defines as a substantial revision and this document set was already disposed — the build thread did not self-apply the upgrade. Whether row 33 should rise to Confidence B on the same basis rows 31–32 already carry is a project-lead or future-review-round decision, not resolved by this entry.

---

*This file's own scope note, for the next thread that touches it: OG-1 through OG-4 are the
items that most directly bear on this world's own path to a real world-freeze and to
Representative-construction closure — the portrait-object collision (OG-1) and world-freeze
compilation/registration (OG-2) are both, on the record's own terms, reserved for the project
lead, not this build thread. OG-5 through OG-13 are disclosed, routed, or surfaced-but-undecided
items of varying weight — several are honest backlogs rather than defects (OG-6, OG-13), one
is a standing tooling gap in build apparatus rather than in any deployed artifact (OG-3), and
none is blocking in the sense CO-022 uses that word. Per CLAUDE.md's own rule, entries in this
file are append-only and numbered; a merged entry's number does not change, and any future
cross-reference should cite subject and date, not a bare OG-number alone.*

### OG-21. Present state of `lpc` at the V2.0 re-baseline, 2026-09-29: records exist, Datus's identity is decided, no registry entry, and the numbering of the canon-closure entries collides.

Logged 2026-09-29 by the V2.0 re-baseline thread, from the files on disk. This entry states the present truth; it does not edit any earlier entry.

- **Records exist.** 310 record files sit under `records/lpc/` (14 record types). Earlier entries that describe the records as not yet built are out of date.
- **Identity decided.** Datus, Bishop of the Kept Flock, is recorded as the Representative in `lpc_Decision_Log.md` and the System Hub Decision Log. No identity-options file exists; whether one is required is a question for the project lead (stop point 1 of the launch prompt).
- **No registry entry, no `build/` folder before today.** The `lpc` registry entry (the world file under `records/worlds/`) does not exist, so handoff checks 1, 2, 4, 5 and 6 fail until it does. Only the project lead creates it and sets `safety_adjacent`. The `build/` folder, state file, cost ledger and re-baseline declaration were created on 2026-09-29.
- **Numbering collisions.** The four canon-closure entries of 2026-09-25 and the re-voicing entry renumbered the same day were numbered on two branches off the same base. The re-voicing entry sits after the quote-rendering entry in file order. Noted, not renumbered; cite by subject and date.
- **OG-4** attributes "relied on for nothing" to the Doc_04 appendix, which says the opposite (Doc_04 relies on Gesta act 158). See the Doc_04 independent check of 2026-09-29.

### OG-22. Independent checks of what was left open, Phase L0, 2026-09-29: five review files, findings carried here so none lives only in a thread.

Each check is an independent Opus 5.5 re-confirmation, not a revision round. Files are in `Build/worlds/lpc/Review-Artifacts/`. Findings below are the reviewers' own; each is to be verified against source before any fix.

- **Doc_04** (`Doc04_Independent_Check_2026-09-29.md`). No open finding changes a gravity, a classification or an Interaction Matrix relation; candidate 5 is Supporting at every site. Still open: Round 11 M1, M2, M4, M6 and most LOW/COSMETIC items; Round 8 H1(d). New N1 (stale pointers to closed Open Items 6 and 8 in Doc_04, Docs 05, 07, 08 and the G5 record, needing one named change order), N2 (Lancel source record still lists act 158 as a speech), N3 (Lancel source record `rights_status: public-domain` for an in-copyright edition; the 411-Gesta limit record repeats it), N4 to N7 (LOW).
- **Doc_08** (`Doc08_Round9_Targeted_Check_2026-09-29.md`). Forces analysis and Index values correct; generator reproduces the Index byte for byte. Two HIGH: the verdict parser takes the first verdict word in a review file, and any mention of "approved to proceed" reads as approval. Doc_08's Disposition claims both fixed. Four MEDIUM, six LOW, two COSMETIC. Round 8 H2 remains open, so OG-3 is partly stale.
- **Doc_02 and `Source_Registry.md`** (`Doc02_Returned_Review_Independent_Check_2026-09-29.md`). Eight location claims from 2026-09-13 resolved. Open: 6 P1, 6 P2. Row 44's Confidence letter; act-158 fix to row 65 not applied; Doc_02 lines 93 and 97 still say CIL VIII and the Codex Theodosianus are not vendored; corpus count false (map holds 104 raw, 94 tradition, 92 titles; four CSEL 51 to 53 entries lack a row); rows 14 and 213 changed by PR #557 round 3 without review; Possidius passages out of date against Doc_01 §5.
- **Docs 03, 05, 06, 07** (`L0_Docs03-05-06-07_Carried_Open_Check_2026-09-29.md`). Correction: Doc_07 is on the seven-dimension lens spine (§2A to §2G); OG-9's Doc_07 bullet recorded a defect in the old Doc_07 template. Doc_05 is the document that does not carry the spine (Completion Standard V1.4, section F, against Construction Framework V7.4 Step 5). Other open items: Doc_07 §2F overstates an absence (Possidius Vita ch. V); Doc_07 Round 2 NEW-L2, L4, L5, C2 not applied; lexicon terms `lpclex017` and `lpclex018` and records `lpc.term.libelli` and `lpc.term.libellatici-sacrificati` deny attestation that Cyprian's Epistle LI carries; no lexicon-index generator exists though the index claims one; Doc_05 §11 items and Doc_03 tagging question undisposed; statuses out of date on the 411 Gesta.
- **Routing.** All five reach a project-lead decision on how to close (rounds against the cap, change orders, waivers). See the stop point 1 package.

### OG-23. Confidence-letter decisions the Library sweep of 2026-09-29 left to the project lead: row 44, row 33, and split letters (rows 11 and 14).

Logged 2026-09-29 by the Library thread. These are sourcing and methodology conclusions, so the sweep did not decide them.

- **Row 44 (*Codex Theodosianus*, Mommsen–Meyer).** The row sits at B. Its old stated ground, that the Licensed-For content had not been read against the vendored file, was false: *CTh* XVI.5.21 was located by structure marker (heading at line 86853, operative clause at lines 86855–86857 of `theodosianus-16_mommsen-meyer1905.txt`). Decision needed: raise the letter under the calibration rule, or state what remains unread.
- **Row 33 (Burns and Jensen).** The row sits at C on the same WebSearch verification that puts rows 31 and 32 at B. Decision needed: B, or C with a stated reason. This is the second item of OG-20.
- **Split letters (rows 11 and 14).** Row 11 carries A for four verified loci and leaves the body-level claim unverified. Row 14 (raised in PR #557 round 3, the lpc records fix of 2026-09-25) carries A for one verified locus, Book II ch. 51 (§118), and leaves its body-level claim unverified. The calibration rule gives a row one letter. Decision needed: may a row carry a split letter, and if not, which letter does each row take?

### OG-24. Open items after the Library sweep of 2026-09-29 (Doc_02 and `Source_Registry.md`).

Logged 2026-09-29 by the Library thread.

- **Sweep not complete.** The standard bibliographies (*Clavis Patrum Latinorum*, Quasten and Altaner, Frend, Merdinger, Lancel, Hoffmann–Schöne–Zeller) were not opened. Also unreached: Diehl's *ILCV*, *CIL* VIII beyond the Numidia supplement, the *Registri Ecclesiae Carthaginensis Excerpta* (searched for in Mansi 3 and 4, Turner tome 1 fasc. 1 and Lauchert and not found), Migne PL 3–4 (not found on archive.org), CSEL 60 (year unread). Schanz Teil 4, the second half of Ribbeck and the first half of the BKV *Johannes* were not located. Gsell's *Histoire ancienne de l'Afrique du Nord* was found and not opened. Gallica and HathiTrust refuse the connection and might hold the missing items. See the Registry's saturation statement. This narrows OG-20 item one; it does not close it.
- **Verified, not fetched.** CSEL 42, CSEL 25.1 and CSEL 43 have seed rows with status `not-yet-downloaded`, as do the second sweep's Raulx letters and sermons (tomes 2–3, 7–11), Poujoulat's letters, Migne PL 35, the BKV letters of Cyprian (year unread), Hefele's German and English councils, Toutain, Freppel, Monceaux's *Saint Cyprien*, Schanz Teil 3, Harnack Band 1, Mansi vol. 1 and Newman. CSEL 58 (praefatio and indices) is still unacquired.
- **Corpus map.** The 38 files at Registry rows 215–252 were staged and merged on 2026-09-30 (45 assignments; Ribbeck is double-placed to `lpc` and `donatism` on the project lead's decision). Their roles are mostly `provisional`: per-work loci are not located for Zycha CSEL 41, Migne PL 39 and 40, and Morin. In-hand files with no row in this Registry: `tyconius_liber-regularum_burkitt1894.txt` (assigned to `donatism` only), `optatus_libri-vii-critical_ziwsa1893.txt` (named only inside row 64), `monumenta-vetera-donatistarum_migne-pl8.txt`, and the Councils of Carthage I–IV, *Breviarium Hipponense* and *Teleptensis* printed in the Bruns file at row 202.
- **Rights basis by date alone.** Rows 219 (Morin, 1930) and 225 (Koch, 1926), and rows 228, 229, 234, 238, 239, 243, 245, 246, 251 and 252, have no rights tag on the host and stand on the printed year. Rows 244 (Hefele, 1921) and 250 (Bardenhewer, 1924) are foreign works cleared under the 95-year rule. Nothing later than 1930 was vendored. The project lead asked on 2026-09-30 that publicly accessible material be used; the Library thread read that as covering works public by date and did not extend it to in-copyright editions, which stay consult-only. Confirmation of that reading is still needed.
- **Translations are second witnesses.** Rows 232–234, 244–246 and 251–252 are German or French translations, so they are cross-checks against the Latin, not the originals. The Raulx French (rows 245–246) is matched to its Latin originals by title only. The Uhl, Postille and Hayd Fraktur OCR is too poor for a verbatim-quote check.
- **OCR.** The Migne volumes (rows 216–218, 223) interleave columns and apparatus. Quotations from them need a visual check.
- **Row 59.** Munier's CCSL 149 may have an earlier public-domain printing of the African conciliar corpus. None is named or ruled out.
- **`records/lpc`, not edited by this thread.** `source/lpc.source.lancel-actes-de-la-conference-de-carthage-411.md` gives `rights_status: public-domain` for Lancel's in-copyright edition (the Migne printing is the public-domain text), lists act 158 among fourteen acts in which Augustine speaks (thirteen, floor), and says the *Gesta* are "not yet drawn on" by Doc_04. `honest_limit/lpc.limit.411-gesta-unread.md` repeats `license: public-domain` for the same source. The build thread needs to correct these.
- **`build/` and Docs 03 to 09, not edited.** Anything there that cites row 65's "fourteen acts", row 44's "not read" ground, or row 213's "not yet promoted" wording needs the same correction. Doc_04 line 7 still says the *Gesta* are "not yet drawn on by it". `Source_Acquisition_Manifest.md` lines 29 and 73 still carry the NPNF-apparatus route for Possidius and "fourteen numbered acts"; `lpc_Rep_Phase3_Voice_Construction.md` line 80 still cites `tertullian-s-voice`. `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` (lines 258–260, 325–326) repeats "fourteen" acts and "not yet drawn on". Doc_04 §7 Open Item 6 (the 411 *Gesta* read and act 158, closed as a persistence question on 2026-09-15) already carries the act-158 grounds.
- **Possidius and Doc_01 §2.** `Possidius_Full_Read_2026-09-16.md` reports that Doc_01 §2's claim that popular acclamation does not recur at the same office for both figures is refuted by *Vita* ch. VIII. The read escalated it. This Doc_02 pass does not change Doc_01.

### OG-25. Independent recheck of the Library's fix pass and the lpc correction passes, 2026-09-30: closed items, and what stays open.

File: `Review-Artifacts/Doc02_Registry_FixPass_Recheck_2026-09-30.md` (Opus 5.5, targeted recheck; 0 P0, 3 P1, 7 P2). All three Round 33 P1s are closed, and every changed claim about a source's text was verified at the vendored file (act 158 a subscription; Theodosian Code XVI.5.21 and XVI.5.52; Letter LIII a joint letter; Petilian Book II chapter 51, section 118; Possidius Vita ch. VIII).

**Open P1.**
- The corrected 258 to 391 silence claim (OG-54) is still false in seven places, because it says Optatus is "the one" Registry text dated inside the gap. Row 265 holds a document dated 317 to 337; row 26 (Native) holds Carthage canons of 345 to 348 and of 387 or 390; row 202 holds Bruns's text of the Carthage council under Gratus; row 59 is Munier's *Concilia Africae a. 345*. Places: Doc_02 line 120, Doc_05 line 27, Doc_08 lines 23 and 264, the transmission force record, `lpc.limit.the-silent-century.md`, and `wb_lpc_s25.py`. Whether conciliar canons count as a surviving voice under Doc_01 section 5 is a project-lead decision.
- Row 265 is Excluded as Out-of-Boundary on grounds the Template does not allow (shelf and authorship, not date or place). Options: Native without a licence, or Named Comparandum. Project-lead decision.
- Re-running the generators would bring back corrected wording: `wb_lpc_s28.py` (line 353 hard-codes public domain for Lancel; line 883 "nothing dated in between"), `wb_lpc_s21.py` (Lancel public-domain, row 11 at A for the whole body, Burns and Jensen at C, Petilian at B), `wb_lpc_s25.py` (replaces the plain spoken text with Layer-form text).

**Open P2.** Row 227 places `CLASSIS V` at 117125; it is at 117124. Rows 267 to 272 lack the sentence giving the reason for Confidence A. Rep Phase 3 line 80 quotes row 204 as "the corpus map's ruling"; the row says "by prior ruling". World core line 436 still says "207 of the Registry's 212 rows". The succession witness text says "Counting back from" where Letter LIII counts forward from Peter. "Donatism's territory" and "hold it provisionally" are build vocabulary in a spoken field. Doc_05 and Doc_08 still carry commentary the checker flags.

**Routing.** The silence claim and row 265 wait on the project lead. The generator, row 227, rows 267 to 272, Rep Phase 3, world core and witness items are the lpc build thread's, to fix after that decision.

### OG-26. The `lpc` registry entry created with `safety_adjacent: false`, the fleet audit changed to fit a world that is not yet compiled, and the two waivers that follow, 2026-09-30.

**Decided by the project lead, 2026-09-30.** `safety_adjacent` is `false` for `lpc`, set on the new registry entry (the world file under `records/worlds/`). Evidence: a read-only keyword search of `records/lpc/`, the story and lexicon chunks and Docs 04, 08 and 09 found no suicide or self-harm material; Circumcellions appear only as background source context; the material near distress is historical persecution, grief and penance. Lean validation stays the default; thin evidence, a Contested Primary claim or a fabrication finding still trigger full validation.

**The entry** carries only what the files give: kind, world_id, census_id and the flag. It has no `state`, card fields or package, which come at admission. Its `state` is the project lead's to give.

**Audit change, approved by the project lead.** In `engine/m1/cross_world.py`: (1) a world with no `state` neither sets nor is measured against the fleet's registry key set; (2) `safety_adjacent` is not a fleet-wide key, because handoff check 1 enforces it and already exempts the grandfathered worlds; (3) the serving-layer checks (package pin, app assets, site portrait, Table seat) run only on worlds that carry a `state`. A new test covers the key-set rule, and one existing test now passes the compiled worlds. The stale `unregistered-world-dir/lpc` waiver is removed. Alternatives considered: fill the whole entry now (needs the Representative's identity, a packaged choice not yet made); register about 22 waivers (a workaround).

**Waivers registered (`ACCEPTED_OPEN`, owner: lpc build thread, Phase L2).** `figure-dates-keys/lpc` and `ui-field-leak/lpc`: the seven `lpc` figure records key `dates` as `display` and carry build references ("this session", "Doc_01 SS2") and record ids in text a participant reads. To be rewritten as born, died or floruit in plain prose, then both waivers removed.

**Also decided.** The `wb_lpc_s2x` generators: retire to `Archive/` once the records phase confirms nothing depends on them, because the records now differ from what they produce (207 records generated against 208 committed; five differ). Rows 215 to 217 of the Registry lack the Confidence A sentence the Petschenig rows now carry; to be added at the next Registry pass.

**Not `lpc`'s.** `tools/check_paths.py` reports one new unresolved citation, in `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (a citation to a staging file of the ANF volume 8 corpus-map entry, written with an ellipsis in place of the full name). Flagged for the grkap owner.

### OG-27. The 258 to 391 silence claim has now needed three substantial revisions; escalated to the project lead, 2026-09-30.

The claim has been corrected three times: the first correction (OG-54), the restatement after the Opus recheck (OG-25), and the restatement checked in `Review-Artifacts/SilenceClaim_Correction_Verification_2026-09-30.md` (0 P0 resolved: 1 P0, 5 P1, 7 P2). The verifier confirmed every source citation and found the restated list still incomplete. Under the review-cycle cap, no fourth restatement is attempted until the project lead decides.

**P0.** Registry rows 231 and 232 hold the *Passio* of Marianus and Jacobus and the *Passio* of Montanus and Lucius, written after Cyprian's death. Montanus and Lucius is a clergy letter from prison to the congregation ("Et nobis est apud uos certamen, dilectissimi fratres"), names Cyprian as the teacher of the faith ("quam Cypriano docente didicerant") and dates itself after his death ("episcopus noster solus passus fuisset"); both acts date from 259. Neither appears in any `lpc` document or record.

**The decision.** Do the acts of 259 break the silence of a congregational voice continuous with Cyprian's that Doc_01 section 5 binds the world to? Everything downstream of the answer waits on it: the wording of every copy of the claim, the Documented rating on the transmission force, the Permanent Prompt line "your own congregational voice falls silent", and the Story Index and Doc_09 "no story from inside the silence".

**Recommendation.** Treat the two acts as the tail of Cyprian's phase (259), keep 258 as the marker of Cyprian's own ministry and the gap as roughly 130 years, and say so: the silence runs from the last voice of Cyprian's community to Augustine's ordination. Add the acts as a named exception group in Doc_02 section 7. This narrows the claim by about a year and does not disturb the two-phase construction.

**Waiting on that decision (P1).** `wb_lpc_s21.py` lines 4390 to 4393 and 4489 to 4490 and world core lines 409 and 410 still carry the old "holds nothing dated inside it" and "only through Donatism's own territory" wording; the Doc_09, Claims Register and Story Index "cannot be" lines; `lpc_Gapped_Formation_Precedent.md` line 21; world core caution 2 against Doc_02 section 8 and row 22; the force record's spoken text (Theodosian Code group missing; "belongs to another community" against Native Optatus).

**Independent of the decision (P2), to fix in the same pass.** Optatus dates: only the TEI headers read "fl. 366-385"; the row 27 file and the Ziwsa scan read "c. 366-393". Doc_02's description of rows 26, 59 and 202 is narrower than their Licensed-For cells. "Richly attested through Donatism's own territory" dropped Doc_01's "overwhelmingly". The Theodosian Code locus is quoted with single spaces where the file prints double. Two library leads: Knopf nos. 19 to 22 and 29 (African acts from inside the gap) have no Registry row, and the `lpc` census entry says "the same Hippo congregation" where Cyprian's church was Carthage.

### OG-28. The silence claim closed under the project lead's ruling of 2026-09-30, with the items it leaves open, 2026-09-30.

**Closed.** Doc_02 section 7 is the canonical statement, and every copy (Docs 05, 08 and 09, the Gapped Formation Precedent, the force and limit records, the world core, the World Profile, generators `wb_lpc_s21`, `s25` and `s28`) says the same: the texts written at and just after Cyprian's martyrdom (the *Acta Cypriani*, Pontius's *Life* and the two martyr acts of rows 231 and 232) stand at the start of the interval, belong to his phase and do not fill the silence, and no source fixes their order. Verified by `SilenceClaim_Ruling_Verification_2026-09-30.md` and the fixes that followed it. Doc_05 section 7 no longer says the interval's sources are "None". The limit record's locus no longer calls 256 the last dated act. Claims register rows `ffbf9d5d` and `efb28ac4` replace `db01c6d3` and `cc0fa5c1` (UNVERIFIED, to be verified in the register conversion).

**Open.**
- The seven figure records were rewritten (OG-26 waivers removed, never valid for a new world under the records gate).
- The force record's `register` is `etic`, as are all 17 `lpc` force records; other worlds' force records are mostly emic, and emic switches on the experimental voice gates. A whole-world decision for the records phase.
- `regate lpc` reports 54 unchanged public-facing fields that already fail readability at the base, and 4 edited fields below FK 8. To be found and fixed in the records phase.
- Rep Phase 5 Round 1 line 33 says the Council of Cirta is known only through the rival communion; Optatus narrates it (row 27, dated 305). A finished test record: fix at the next Phase 5 round.
- The website's `lpc` tree page and its census entry say Augustine preached to the same congregation as Cyprian (Hippo and Carthage); outside `lpc`'s documents, for the owner of `cic-website`.
- Library leads: Knopf nos. 19 to 22 and 29 (African acts) have no Registry row.

### OG-29. Claims register verification, 2026-09-30: 111 claims checked at source; 53 marked, 58 could not be, and the false ones fall into a few repeated defects.

Four independent Opus checks (`Build/Ministry/Operations/Audits/lpc_Claims_Verification_Findings_2026-09-30.md` holds every finding with its evidence and a proposed true wording). Result in `lpc_Claims_Register.md`: 35 VERIFIED, 18 JUDGEMENT, 58 UNVERIFIED (the 58 are claims the check found false, overstated or unsupported, and stay unmarked until the wording is corrected). Nothing has been applied to an approved document.

**Repeated defects (each spans several documents and records).**
- **A. Lay awareness of the conciliar question (G5).** Doc_04 says no evidence shows ordinary believers or most clergy were even aware of it, and that neither bishop's theory is visible outside one locus. The preface of the 256 council (Registry row 4, row 261) records presbyters, deacons and most of the congregation present when the "bishop of bishops" formula was spoken. Cyprian restates the free-judgment position in Epistles LIV, LXXI and LXXV; Firmilian contests Stephen in Epistle LXXIV; Augustine appeals to plenary councils in Letters XLIII and LIV, and his *Psalmus contra partem Donati* was written for the common people. Awareness is attested; formation by the question is not. Carried by Doc_04, Doc_05, Doc_07, Doc_08, the World Profile and G5-related records.
- **B. Presbyters "almost only as faction".** Epistles IV, XXXV and XXXVIII show presbyters and deacons running the church, celebrating with confessors and acting as Cyprian's agents; Numidicus is the subject of the world's own story 3. Carried by Doc_07 and Doc_05.
- **C. "Nothing survives" claims that ignore what the corpus holds.** The 258 to 391 silence records drop Doc_02 section 7's scope; a Confessions V.8 oratory to Cyprian at Carthage around 383 lies inside the gap; a Guelferbytanus tractatus is unassessed; Possidius is also attested in the Gesta of 411; women's voice (Quartillosa, first person) is not absent; the non-episcopal record is not missing (a deacon and two lay confessors write in their own voices).
- **D. Grace in Cyprian's phase.** The record says no evidence has been found; Cyprian states the theme in *Ad Donatum* 4 and *Ad Quirinum* III.4, and Augustine cites him for it.
- **E. Doc_05 on the rites.** Doc_05 line 151 says the rites at Carthage and Hippo are attested in nothing the build has verified; Epistle LXIX and Augustine's sermons to candidates attest them, and the world's own catechesis chunks carry both.
- **F. Doc_09 sections 6 and 8 say Augustine's sermons on Perpetua are "not available to this build at all".** They are vendored in row 227 as second-witness OCR (Sermones CCLXXX to CCLXXXII).
- **G. Doc_02 line 45, 57 and section 7:** the Hartel Praefatio dates *De Pascha Computus* to 243 and reasons about *De duplici martyrio*; "several women correspondents" overstates two addressees; Possidius is not single-work visibility.
- **H. Closed items called open:** Doc_07 and Doc_09 call two questions open that Doc_04 section 7 closed on 2026-09-15.

**Single-claim findings (P1 and P2).** Force 2A-2 is not the only isolated force (1B-3 too); Doc_08 line 297 on the plague against Pontius, *Life* 9 to 11; a story chunk says the treatises never name the unwilling survivor (*On the Mortality* 17 does); Tier 3 rule stated more broadly than applied (lpcstory002); material evidence is not only rows 37 and 38; Norton (row 186) also addresses the election; the "bishop of bishops" formula is not the sole ground of G5 (and its confidence is Inferential-Thin); Prosper is cited beside Possidius; "no source fixes their order" (Life 11.1 cites the Acts of the first hearing; Harnack has the Life before the compiled Acta); a quotation of Doc_01 with "own" inserted; a Doc_03 quotation "sets" for "set"; three details in Vita IV, not two; 1110900c on candidates 5 and 7.

**Needs the project lead.** Corrections to approved Docs 02, 03, 04, 05, 07, 08 and 09 change claims, so they go as one named change order, each verified by a separate agent that sweeps every copy. Defect A reaches Doc_04's premise for G5; the classification (Supporting, on the project lead's ruling) is not proposed to change, but the six tests for G5 are to be rechecked once.

### OG-30. The claims change order and the G5 rulings of the project lead, 2026-09-30: what was decided, applied and reaffirmed.

**Change order approved (2026-09-30).** The 58 claims the four source checks found false, overstated or unsupported (OG-29) were corrected in Docs 02, 03, 04, 05, 06, 07, 08 and 09, the World Profile, the Capsule Core, the Gapped Formation Precedent, Representative Phases 1, 2, 3 and 7, the story and lexicon chunks, and 40-odd records and their generators. Each correction was verified at the vendored file by structural marker. Independent verification: `Review-Artifacts/ChangeOrder_Verification_2026-09-30.md` (51 closed, 7 leaning on an unlicensed text, then closed by the two rulings below), `Review-Artifacts/G5_SixTest_Recheck_2026-09-30.md`.

**G5 rulings.** (1) The strand-singular finding is reaffirmed, and Doc_01 is not reopened: Doc_04 section 3 surfaces evidence Doc_01 had not weighed on that axis (the 256 preface, Epistles LIV, LXXI, LXXIV, LXXV, Letter LIV), and it shows disagreement inside one communion (Candidate 3's shape), not two communities; this answers the condition in Doc_01 section 8's tenth open item (carried in the Doc_01 section 8 entry of 2026-09-30). (2) Doc_04's verdict texts follow the Framework's own tests: G5 Repetition passes; Persistence passes narrowly; Explanatory passes narrowly (Letter LIV); Formation does not clearly pass; Dependency as written. G5 stays Supporting on the project lead's ruling, and Doc_04 now records that Supporting also rests on its own six-test result. G7 (grace) fails as an organizing force, not as a theme (Cyprian states it; Augustine carries it forward). Candidate 6 Repetition names the over-century gap and the 87 bishops of the 256 council (the stated number in the ANF05 editor's note and the Latin title; a count of the speaking paragraphs gives 84). (3) Letter XLIII is struck from the wording (it sits in the Donatist cluster row 11 excludes). (4) Augustine's *Psalmus contra partem Donati* is licensed at Registry row 273, narrowly.

**Open, for the Library thread (through the project lead).** A second corpus-map assignment of the *Psalmus contra partem Donati* (Petschenig CSEL 51, the file behind rows 214 to 217 and 266 to 272) to this world's shelf: the corpus map assigns it to `donatism` only. Row 273 states the request.

**Open, for the project lead.** The Gapped Formation Precedent, section 4, still says the candidate "structurally needed the gap bridged"; with G5 now attested on both sides that clause is arguably still a premise problem, and correcting it would change the precedent's argument. Not changed.

**Not applied, by design.** Row 227's Sermones CCLXXX to CCLXXXII (Perpetua) and 309 to 313 (Cyprian) stay unread; Doc_09 records them as a Tier-question candidate, and no story is built from them.

### OG-31. Claims register complete, 2026-09-30; the readings the silence judgements rest on, for the project lead.

`lpc_Claims_Register.md`: 104 claims derived and registered, 0 UNVERIFIED. The final pass was checked by `Review-Artifacts/ClaimsChangeOrder_FinalRecheck_2026-09-30.md` (7 VERIFIED, 14 JUDGEMENT, none unmarked). Findings of all passes: `Build/Ministry/Operations/Audits/lpc_Claims_Verification_Findings_2026-09-30.md`. The old five-column `Doc09_Claims_Register.md` and `scripts/check_claims.py` stay in place as the pattern the register template cites; they are superseded by the new register.

**Open, for the project lead: three readings behind the silence judgements (Widely Accepted), beyond the ruling of 2026-09-30.**
- Does "in the Registry" mean only the Native rows? Row 265 is Excluded, but it holds the *Gesta apud Zenophilum*, in which the Cirta congregation of 305 cries against a traditor bishop ("exaudi deus, ciuem nostrum uolumus, ille traditor est", appendix file lines 484 to 493 and 568 to 570) and a deacon says "we did not communicate with him", the practice Cyprian lays down in Epistle LXVII. That is a congregation's voice dated inside the interval, in a Donatism-world document. The claims list row 265 among the texts dated inside the gap and say of it only that none "carries on Cyprian's voice", which is true because of its Excluded status, not because of what the text says.
- *Confessions* III.12: a Catholic African bishop gives Monica pastoral counsel about 373. The ruling on the oratory (seen through Augustine's eyes) covers it by the same logic but does not name it.
- Optatus names the "cathedra ... Cypriani" (row 264 file lines 561 and 988); the judgements read "voice" as the pastoral or congregational voice the record's next sentence defines.

**Outside the claims tool.** The transmission force record's line "the one thing of ours that carries it across" is contradicted by its own next sentences; the registered claim "No other force of ours does" is true.

### OG-32. The Source Readiness Dossier's open cross-world questions, carried into this ledger, 2026-09-30.

The dossier (`Build/worlds/_cross-world/dossiers/latin-pastoral-congregational-christianity_Source_Readiness_Dossier.md`, section 5) lists four open cross-world questions. This entry carries the two the handoff gate found missing, in the dossier's own words, with their present state. The Hilary-identity question and the Article 3 century-gap question were already carried.

- **Optatus's world placement** — currently `provisional` in this world's own corpus-map, self-flagged as inferred from region and date alone ("Mark may prefer another Latin home for a Numidian polemicist"). The world's own Step 0 (section 4 item 2a) names three live options: re-home to Donatism, hold here as the Catholic-side tradition, or double-place, the way the Council of Carthage under Cyprian already is. Present state: Optatus is held here as Native (Registry rows 27, 64 and 264, `role: tradition`, and `role: context` on the Donatism shelf, so in effect double-placed), drawn on for no claim, and the placement is still the project lead's question. The Petschenig and Ziwsa Latin critical editions are linked to rows 27 and 264 without settling it.
- **A resolved item, noted so nobody re-opens it:** the world's own Step 0 surfaced and, with the project lead's direct authorization, fixed a genuine boundary breach in the already-built Imperial and Juridical Christianity world's own records (two load-bearing quote records citing *Confessions* material outside IJC's own declared license). Logged in full at `Build/worlds/ijc/Open_Gaps_Tracking.md`, the boundary-breach entry on `ijc.source.augustine-confessions` (fixed 2026-09-01); mentioned here only for cross-reference, not reopened.

### OG-33. Doc_01 section 8, open items carried forward: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 171:** "**The century-gap's Source Ecology consequence (§5 above; Step 0 §4 item 1).** Doc_02 must name the documentary gap precisely — an honest silence in this world's own record between 258 and 391, not a general absence of evidence about that period — and distinguish it clearly from the rich, but Donatism-territory, evidence that does survive for those decades." **Status: Closed.** Discharged by Doc_02 section 7 and Doc_02 section 9 (its line for this item reads 'discharged'). The wording of the 258 to 391 silence was settled by the project lead's ruling, recorded in the ledger entry on the silence claim closed under the ruling of 2026-09-30. (2026-09-30)
- **Line 172:** "**The Donatism boundary's remaining open items (§7 above; Step 0 §4 item 2).** The Optatus placement question (re-home, hold, or double-place); the duplicated Council-of-Carthage-under-Cyprian corpus-map rows; the Article 23 reconstruction of Donatism as this world's own internal rival. The reading-divergence question itself is resolved by this document (§5 above); [...]" **Status: Open in part.** Doc_02 section 9 carries all three sub-parts and resolves none. (1) Optatus placement: open, the project lead's question (ledger entry on the Source Readiness Dossier's open cross-world questions, 2026-09-30). (2) Duplicated Council-of-Carthage rows: the corpus map still holds two entries for the 256 council (the npnf214 and anf05 editions) and no file records a reconciliation; open, a corpus-map edit that belongs to the Library thread. (3) Article 23 reconstruction of Donatism: routed to Representative construction; Representative Phases 3 and 4 cite Article 23, but no file says whether they discharge Doc_02's routing; status not determined from the files, and a check of those two phases against Doc_02 section 6 would settle it. The reading-divergence part is closed in Doc_01 section 5. (2026-09-30)
- **Line 173:** "**Source-skew disclosure, sharpened form (Step 0 §4 item 3).** Both anchor voices are bishops; this world's own "ordinary believer" subject matter is attested only through episcopal mediation. [...]" **Status: Closed.** Discharged in Doc_02 section 6 (Doc_02 section 9, third accounted item). (2026-09-30)
- **Line 174:** "**The corpus-map as required, not sufficient, Doc_02 input (Step 0 §4 item 4).** cic/corpus-map/latin-pastoral-congregational-christianity.yaml is a real starting inventory, to be cross-checked and extended, not duplicated wholesale. This includes the Augustine–Jerome correspondence's own deliberate double-placement with World #9 (§7 above): Doc_02 inherits it as given, not as a boundary breach to resolve, and should say so explicitly rather than let a reader re-discover the question this document has already answered." **Status: Closed.** Discharged in Doc_02 section 1 and Source_Registry row 10, which states the double placement (Doc_02 section 9, fourth accounted item). (2026-09-30)
- **Line 175:** "**The Tertullian dropped-voice disclosure (§7 above; Step 0 §4 item 6).** Doc_02's Author Gravity work for Cyprian should name Tertullian as a real, non-Native influence-source (Excluded / Named Comparandum), and log the disclosure rather than let it pass silently a second time." **Status: Closed.** Discharged in Doc_02 section 2 and Source_Registry row 5 (Doc_02 section 9, fifth accounted item). (2026-09-30)
- **Line 176:** "**The Antiochene primary-gravity contrast (§7 above; Step 0 §4 item 7).** Doc_04's gravity-orientation work should keep this world's own gravity classification framed in terms that would survive a future validated contrast against an Antiochene candidate, not merely in terms of geography or language." **Status: Closed.** Discharged by name in Doc_04 section 5, in the paragraph that opens with this item. (2026-09-30)
- **Line 177:** "**Doc_04's formal six-test assessment of the primary characterization this document establishes (§3, §4, §5 above; Step 0 §4 item 8).** This document states the primary characterization on this world's own ecological terms first, at §3, before applying it to the World #4 boundary at §5, per Step 0 §4 item 8's own primary-gravity-first discipline. Doc_04 generates its own candidate gravities independently from Doc_02's Source Ecology, per CF V7.4 Part III's own Candidate Gravity Generation discipline, and states explicitly whether this document's preliminary reading survives that independent derivation — including, with particular weight, the conciliar-authority uncertainty §4 above discloses and does not resolve (item 10 below)." **Status: Closed.** Doc_04 sections 3 to 5 carry the six-test assessment and state whether the preliminary reading survives; Doc_04 was cleared on 2026-09-15. The conciliar-authority condition is answered by the project lead's G5 rulings of 2026-09-30 (ledger entry on the claims change order and the G5 rulings). (2026-09-30)
- **Line 179:** "**A possible portfolio-wide process gap, for a coach pass rather than this document to decide:** this document's Round 1 review found that World Separation Criteria (§4 above) is absent from IJC's own Doc_01 as well, and that the Forces Framework's Layer-1 apparatus (confidence levels, named sources per force) is not run at Step 1 by either this world's or IJC's own preliminary sketch. If a coach pass agrees these are gaps in how Doc_01s are being built against CF V7.4 Part I portfolio-wide, that is a System Hub process finding, not something this document resolves for other worlds." **Status: Not determined.** Doc_01 leaves this to a coach pass. No file on disk records a coach-pass outcome (a search of Build/Ministry for 'World Separation Criteria' found nothing). A System Hub record of a coach pass on Doc_01 against Construction Framework V7.4 Part I would settle it. (2026-09-30)
- **Line 180:** "**The conciliar-authority axis within Strand Determination (§4, §5 above) — the strand-singular finding's own governing, recorded form, held subject to this document's reopening caveat, not yet closed.** Cyprian's own egalitarian, non-coercive theory of inter-episcopal authority (256 Council preface) and Augustine's own hierarchical, correctable theory of conciliar authority (*On Baptism* II.3) are real, substantial differences this document argues do not clearly touch this world's own formation-relevant ground, but does not consider fully settled. §5's own discipline governs here: the strand-singular finding stands per Article 21 and CF V7.4 until and unless Doc_04's formal six-test assessment, weighing this axis directly, surfaces evidence this document has not weighed — in which case the finding is reopened rather than defended past the evidence." **Status: Closed.** The project lead's G5 ruling of 2026-09-30 reaffirms the strand-singular finding, does not reopen Doc_01, and states that Doc_04 section 3 surfaced the evidence and answers the condition of this item (ledger entry on the claims change order and the G5 rulings). (2026-09-30)
- **Line 181:** "**Step 0's own now-inaccurate disclosures, a record-correction item rather than a live construction question (§5 above) — three now-false statements, not one.** This world's own cleared Step 0 states, as binding disclosure, that Donatism's own Step 0 reads the portfolio entry's "not the schism-crisis angle" parenthetical as qualifying both anchor figures together. On the sibling branch's current, corrected, and cleared state, none of the three statements carrying that claim is still true: (a) §3 B3 and §4 item 2(e) state the general claim; (b) §2 A5, the fullest and most specific of the three, additionally quotes Donatism's draft directly for it — "Cyprian and Augustine's ordinary pastoral office and sacramental care" — words no longer present anywhere in Donatism's own Step 0; (c) §2 A5 further states that Donatism "makes that reading binding on its own Doc_01 (its §4 item 4)" — also no longer true, since Donatism's own Step 0 §4 item 4 now binds the Coach3 axis to its own Doc_01, not the parenthetical reading. This document does not reopen its own Step 0 to fix any of the three — not because the build thread lacks the write access (Step 0 sits inside this world's own build folder, within this thread's scope), but because Step 0 is a separately cleared document with its own disposition, and amending a cleared document is a different act from discharging Doc_01's obligations; [...]" **Status: Open.** Step0_Movement_Scope_Confirmation.md still contains all three quoted statements (checked on disk, section 2 A5, including the quoted words about ordinary pastoral office and sacramental care and the words 'makes that reading binding'). Step 0 has not been amended; the correction awaits a separate act on that cleared document or the branch merge. (2026-09-30)
- **Line 182:** "**Why this document declines to gloss "orthogonality to state power," named here for whoever next relies on the World #6 boundary this document states (§7 above; §9 below).** The portfolio-level Step 0 Conclusion's "orthogonality to state power" clause is a screening-level compression written before this world's own construction began. This document does not certify what it means, per the project-lead instruction on method recorded and quoted verbatim at lpc_Decision_Log.md (2026-09-01 entry): report what the sources document rather than resolve them into a single reading for the sake of a tidy portfolio-level fit. What §7 reports instead is the actual, textured arc: on the evidence this document has examined, Cyprian never solicits state power; Augustine's own relationship to it develops across three phases, not two — an early opinion, by his own retrospective account, against any coercion; a real but narrow solicitation of legal protection, argued, but in the event not granted, early in his own episcopate, at a council NPNF's editorial note dates 401 (Letter 185 §25); and, later, a sustained defense of broader compulsion, after an argued change of position he records in his own words (Letter XCIII §17, a.d. 408). Whoever next builds on this document's World #6 boundary section should carry that three-phase sequence forward, not a single static label and not a two-phase compression. [...]" **Status: Closed.** A standing record of the considered account, with no action pending; it stays open to correction only by re-examination of the sources. The method instruction of 2026-09-01 is indexed in the ledger's dated project-lead decisions. (2026-09-30)

### OG-34. Doc_02 section 9, open items and handoffs: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_02_Source_Ecology.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 131:** "**Source Acquisition — substantially closed this revision (2026-09-08).** Source_Acquisition_Manifest.md, accompanying this document, originally set out nine real, checked acquisition candidates (G1–G9) for the project lead's decision. With this build session's own network access confirmed working for the first time (lpc_Decision_Log.md's 2026-09-08 "Network access confirmed working" entry), eight of the nine are now closed on their own public-domain footing: G1 (Hartel's CSEL 3, complete, rows 191 and 194), G2 (Harnack's *Vita Cypriani*, row 205), G3 (Possidius's *Vita Augustini*, row 192, closed 2026-09-05), G5 (Monceaux vols. I–III, rows 206–208), G6 (Knöll's *Retractationes*, row 209), G7 (von Soden's *Briefsammlung*, row 210), G8 (von Soden's *Prosopographie*, row 211), and G9 (Delehaye's genre study, row 212). **Not all eight by this build thread's own fetching:** two of the eight — G3 in full and G1's own Pars I–II — were supplied directly by Mark himself on 2026-09-05, before this session's own network access existed; only G1's own Pars III, G2, G5, G6, G7, G8, and G9 were fetched directly by this build thread once that access was confirmed, on 2026-09-08. **Only G4 remains open, and only for its own smallest remaining part:** Goldbacher's Augustine *Letters*, CSEL 34/1–2, 44, and 57 Pars IV are all now vendored (rows 195–196, 193); CSEL 58 (praefatio and indices, no letter text of its own) is not vendored, because the only public scan of CSEL 58 located on the Internet Archive is a 1961 Johnson Reprint Corporation facsimile, excluded on the same ground as row 197's CSEL 33 facsimile. [...]" **Status: Open in part.** G1 to G3 and G5 to G9 are closed (Doc_02 itself and the Manifest). The G4 residual stays: CSEL 58 is not vendored, and the file was retired to the archive on the ground row 197 already states (ledger entry on the Library pre-Step-3 readiness sweep, 2026-09-29). (2026-09-30)
- **Line 132:** "The material/epigraphic evidence named at §5 (basilica archaeology, *CIL* VIII) has not been independently verified against a specific site report, catalog, or inscription this session — flagged for priority second-opinion review before it supports any specific claim." **Status: Open.** A standing, disclosed limit. No file records a site report, catalog or inscription checked for basilica archaeology or CIL VIII; the Library sweep of 2026-09-29 lists none. (2026-09-30)
- **Line 133:** "Rows 34 and 35 of Source_Registry.md (Fahey, Rebillard) remain recalled from field knowledge rather than independently re-read as of this document's own original 2026-09-01 drafting session, nor in any later pass — flagged for priority review per the Registry's own trigger. Row 38 (basilica archaeology) is recalled from field knowledge in the same way but is not itself part of that flagged group: row 38's own Licensed-For states a negative ("Not currently licensed for a specific claim"), which the Registry's own trigger rule explicitly excludes from the flag; the underlying material is flagged for priority attention elsewhere in this document instead, at §5's closing sentence and §9 item 2. Row 37 (*CIL* VIII) is not part of this group either: row 37's own Discovery channel and Verification Note ground it in the sibling Donatism build's own already-verified Registry entry, not in field knowledge, the same footing row 36 (Shaw) already stands on outside both groups in this item. Rows 30–33 (Brown, Lancel, Burns's *Cyprian the Bishop*, Burns & Jensen) are bibliographically WebSearch-verified but not independently re-read for their own argument or content. **Rows 46–47 (Clarke, van der Meer) are not WebSearch-verified** — both are recalled from general field knowledge and each is flagged in its own row for priority second-opinion review before it supports any specific claim. **Every row added from Round 2 onward, per this world's own PRESS and recall-test dispositions, carries a further verification state: WebSearch-verified bibliographically (editor, publisher, year, series), but with no specific locus, passage, or argument independently checked against either the work itself or a primary source, unless that row's own Verification Notes state a higher check was done (e.g., row 56, Monceaux, WebSearch-verified for extent and rights position at Confidence B).** This item states that rule rather than a row range, since a row range would need updating every time the Registry grows — the Registry's own row-by-row Verification Notes column is the authoritative record of which specific check each row has actually had." **Status: Open in part.** Registry rows 34 and 35 still read 'Recalled from general field knowledge' and rows 46 and 47 still read 'not corroborated by an independent WebSearch' (checked in Source_Registry.md on 2026-09-30). Row 33 was raised to Confidence B on 2026-09-29 (Library readiness sweep entry). The rest of the item is a statement of rule. (2026-09-30)
- **Line 134:** "The Affirmative Duty's secondary (bounded-reconstruction) prong (§6 above) is not exercised in this pass — Letters CXXVI and CCXI (§6 above) are real candidates for it, identified and verified this revision, but neither has yet been tested against the Framework's three bounding conditions. [...]" **Status: Open in part.** Doc_05 section 1.4 discharges the prong (Doc_05 section 11, sixth item), but only on the extension that Doc_05 section 11 (thirteenth item) leaves to the project lead to confirm or reject; no ruling is on file. So the discharge is conditional and open. (2026-09-30)
- **Line 135:** "Whether Letters CXXVI (Albina), CCXI (the Nuns of Hippo), or Sermons 280–281 on Perpetua and Felicitas (Registry row 122, named at §6 above) meet this world's own load-bearing threshold comparable to the sibling Donatism build's own Lucilla finding (§6 above) is an open question this revision raises rather than settles — carried forward for Doc_05/Doc_07's own further work." **Status: Open in part.** Answered in Doc_05 section 1.4: the load-bearing trace is the anonymous Hippo congregation of 411, not Letter CXXVI's Albina, the nuns, or the Perpetua sermons (Decision Log, Doc_05 entry). The answer is conditional on the same unresolved Article 20 extension. (2026-09-30)
- **Line 136:** "**The ten-item relative-recall test and PRESS question were run once per review round through Round 14; no round after Round 14 has run either instrument** (stated here as a standing rule rather than a per-round enumeration, matching Source_Registry.md's own parallel practice). **Round 15 reviewed the 2026-09-08 revision itself; every round since has verified the prior round's own fix pass (Rounds 18 onward also adding a cold, whole-document read alongside that verification). None of these rounds has run either instrument.** Results are recorded in Source_Registry.md's own saturation statement, the single authoritative count, not restated here, to avoid the two documents drifting apart. [...]" **Status: Open in part.** The field-bibliography sweep ran on 2026-09-29 and is recorded in Source_Registry.md's saturation section (Library readiness sweep entry, 2026-09-29). The recall test and PRESS question have not been run since Round 14, as the item states, and the saturation statement stays open. (2026-09-30)
- **Line 137:** "Doc_03 (Lexicon) should draw its candidate terms from this document's own Native Registry entries, with particular attention to this world's own vocabulary as it actually appears in the primary corpus (e.g., the conciliar-authority language of the 256 preface, the lapsed/penitential vocabulary of *De Lapsis*) rather than generic scholarly labels." **Status: Closed.** Consumed: Doc_03 was built and Approved to proceed on 2026-09-09 (ledger's dated project-lead decisions). Whether its term choices follow this direction was not re-checked here. (2026-09-30)
- **Line 138:** "**Resolved 2026-09-08.** Registry row 41 (the *Acta Proconsularia Sancti Cypriani*, Cyprian's own trial record) was named from general field knowledge, not independently located at a specific URL — this item named that as a weaker acquisition lead than the other candidates. G1's own Pars III fulfillment (row 194) includes the Acta Proconsularia directly (pp. CX–CXIV of the printed volume, immediately following the Vita); [...]" **Status: Closed.** Marked 'Resolved 2026-09-08' in the item itself; G1 Pars III (row 194) includes the Acta Proconsularia. (2026-09-30)
- **Line 139:** "**The liturgical-evidence category, assessed at §5 above as its own category, has not been read as liturgical evidence specifically** — the works named there (*De Dominica Oratione*, the creedal and catechetical works, the baptismal-validity treatises, the *Confessions*' own catechumenate narrative) are known for their doctrinal argument, not yet reread for what they show about the rite's own form. [...]" **Status: Open in part.** The liturgical read was done on 2026-09-19 (Review-Artifacts/Liturgical_Evidence_Read_Cyprian_2026-09-19.md and Liturgical_Evidence_Read_Augustine_2026-09-19.md). Its candidate terms are not yet in the lexicon and Doc_05 section 3 was not updated (Phase L0 check, 2026-09-29). Open as to integration. (2026-09-30)
- **Line 140:** "**The Story Inventory's own provisional beginning (CF V7.4 Part II) is not yet started at §4 above** — no story is assigned a tier, though Pontius's *Life* is described there in terms matching the Framework's own Tier 3 definition without being so labeled. This may be a portfolio-wide gap in how Step 2 is currently being applied (the sibling Donatism build's own Doc_02 has the same shape) rather than a defect specific to this document; named here either way rather than left unmentioned, for a coach pass to assess across worlds if it is the former." **Status: Closed.** Closed for this world: Doc_09 Story Inventory exists (Doc_05 section 11, ninth item). The portfolio-wide question, whether the gap is a pattern for a coach pass, has no recorded outcome. (2026-09-30)
- **Line 141:** "**Doc_01 §8's binding open items directed at this document (items 1–5) are individually accounted for here:**" **Status: Closed.** A lead-in line; each of the five items is accounted for in the lines that follow, with the outcome of each given in the five lines that follow. (2026-09-30)
- **Line 142:** "Item 1 (century-gap disclosure) — discharged, §7 above." **Status: Closed.** Discharged in Doc_02 section 7; the silence claim's wording was settled by the project lead's ruling of 2026-09-30 (ledger entry on the silence claim closed under that ruling). (2026-09-30)
- **Line 143:** "Item 2 (the Donatism boundary's remaining open items) has three sub-parts, all three named here rather than only two: the Optatus placement question (re-home, hold, or double-place) — disclosed and carried forward this revision, §1 above and Registry row 27, on the corrected fact that the census has already double-placed him; the duplicated Council-of-Carthage-under-Cyprian corpus-map rows — disclosed and carried forward, §1 above and Registry row 42; and the Article 23 reconstruction of Donatism as this world's own internal rival — routed, not resolved, by §6 above's own routing note (Article 23 governs how this world's eventual Representative characterizes its opponents; that is a future document's concern, not this one's). None of the three is resolved here: [...]" **Status: Open in part.** Same three sub-parts as Doc_01 section 8 item 2: Optatus placement open (project lead); duplicated Council-of-Carthage rows still present in the corpus map; Article 23 routing not determined from the files. See the Doc_01 entry above, 2026-09-30. (2026-09-30)
- **Line 144:** "Item 3 (sharpened source-skew disclosure) — discharged substantively at §6 above, which names the episcopal-mediation skew specifically rather than only in general terms." **Status: Closed.** Discharged in Doc_02 section 6. (2026-09-30)
- **Line 145:** "Item 4 (the corpus map as required-but-not-sufficient input, including the Augustine–Jerome correspondence's own deliberate double-placement) — discharged, §1 above and Registry row 10, which states the double placement explicitly per item 4's own instruction." **Status: Closed.** Discharged in Doc_02 section 1 and Source_Registry row 10. (2026-09-30)
- **Line 146:** "Item 5 (Tertullian disclosure at Doc_02's own Author Gravity work) — discharged, §2 above and Registry row 5." **Status: Closed.** Discharged in Doc_02 section 2 and Source_Registry row 5. (2026-09-30)

### OG-35. Doc_04 section 7, open items carried forward: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_04_Gravity_Discovery.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 207:** "**Two Confidence/Gravity Cross-Check divergences are carried forward explicitly to Doc_05 and Doc_08, not resolved here, per the Cross-Check's own governing rule.** (a) **Candidate 3** — underlying facts Documented; the one-gravity synthesis itself Widely Accepted. (b) **Candidate 5** — both formulas' existence Documented; their organizing breadth not supported at the same level, flagged and not upgraded, per §3's own restored Cross-Check note. Candidate 5's is the more consequential of the two, sitting on this document's most contested candidate, and it is recorded here so it travels rather than resting only at §3." **Status: Open.** Carried by design and not closed: Doc_05 (the Confidence cross-check note at its line 135) and Doc_08 (the G5 connection, carried as Doc_04's incomplete-ecology finding) both carry it forward. No file resolves either divergence. The G5 six-test recheck of 2026-09-30 (Review-Artifacts/G5_SixTest_Recheck_2026-09-30.md) records the verdicts but does not remove the confidence divergence. (2026-09-30)
- **Line 208:** "**Candidate 5 is classified Supporting** on the project lead's ruling, which its own six-test result (§3) also fits, and not on any 411 Conference evidence. **What Doc_05, Doc_07 and Doc_08 should do with it:** treat it as a Supporting gravity; do not suppress it, since both formulas' existence is Documented and the disagreement is real; treat the Cross-Check divergence at Open Item 1 as a statement about *evidential confidence*, which CF V7.4 distinguishes from gravity strength, not as a finding that the candidate fails to organize; [...]" **Status: Open in part.** Closed as to classification: Supporting, by the project lead's ruling of 2026-09-14, with the six-test result also recorded (G5 rulings, 2026-09-30). Open as to wording: the item's last clause still says Open Items 6 and 8 'may both bear on the classification', though both were closed on 2026-09-15. This is the stale-pointer finding of the Doc_04 independent check of 2026-09-29, which asks for one named change order; it has not been applied to this line. (2026-09-30)
- **Line 209:** "**A Framework/Template mismatch, not a Framework gap.** Doc_04_Gravity_Discovery_Template_V1.0.md §4 names a fourth classification label, "did-not-reach-gravity-status," that Construction Framework V7.4 Part III does not. The mismatch is real and remains Imperial-Juridical-Christianity's own already-open System Hub item, not re-logged here. [...]" **Status: Open.** Not this world's to close. It is the Imperial and Juridical Christianity world's own open System Hub item (process findings in Build/worlds/ijc/Open_Gaps_Tracking.md), checked on 2026-09-30. (2026-09-30)
- **Line 210:** "**The Manichaean half of Doc_03's own "refusing a purity/sufficiency test" gravity candidate (Registry row 22's own Licensed-For phrase)** was not independently tested here as its own candidate, since Doc_03's own discovery pass had not yet surfaced a specific enough term to test against (Doc_03's own Notes: "Elect"/"Hearers" are located-but-not-yet-verified leads). If a future pass verifies specific anti-Manichaean vocabulary the way Doc_03 verified "grace" for the Pelagian half (Registry row 23), that material should be tested against this document's own Candidate 7 to determine whether it is the same gravity's own second front or a genuinely distinct ninth candidate." **Status: Open.** Not tested. Doc_05 section 11 (fifth item) carries it unchanged, and the Doc_03 discovery gap for Elect and Hearers is open (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 211:** "**Candidate 8's own Strand B-equivalent status is moot in a strand-singular world**, but its own *phase*-boundedness (Cyprian-only, no Augustine-phase material identified) is itself carried forward as an open item: a future ecological-reconstruction pass (Doc_05) finding Augustine-phase confessor- or ascetic-authority material this document has not located would bear directly on whether this candidate's own Tensional classification should be revisited." **Status: Closed.** Answered in the negative at Doc_05 section 2.3 (Doc_05 section 11, fourth item: Augustine-phase confessor material). Doc_04's own line still reads 'carried forward as an open item', which is out of date. (2026-09-30)
- **Line 212:** "**CLOSED AS A PERSISTENCE QUESTION, 2026-09-15, on the gapped-formation precedent** (lpc_Gapped_Formation_Precedent.md §4a). **Reading the 411 *Gesta* to shore up Candidate 5 is the precedent's named failure mode**: it is native to Donatism's own world, not this one, and two independent attempts to extract findings from it were both found unsound on review — one counting Migne's editorial apparatus as conference record, one mistaking a genuine ~7,000-line band for apparatus without opening it. The precedent's rule: such a source may be used *"for narrow, specific, independently-verifiable facts only … never asked to retroactively prove a thin candidate's persistence across a century it was never written to document."* **The *Gesta* remains available for narrow factual checks and remains listed as unread; it is no longer carried as an open question about Candidate 5's persistence.** The original item read: Candidate 5's Repetition and Persistence findings rest on a search bound, not an exhausted corpus: the Migne PL XI printing of the *Gesta Collationis Carthaginiensis* (cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, per Registry row 65's Verification Note) records the 411 Conference, the most obvious place in this world's corpus where inter-episcopal authority structure would be visible among clergy other than the two anchor figures. **Two attempts to read it were withdrawn** (Doc_04_Superseded_Claims.md §2). The question is open and unprejudiced. **The read should be commissioned from a thread that wrote neither withdrawn version, and its findings applied by a thread other than the one that reads.** One narrow finding survives and is relied on here: act 158 (file line 121764) is Augustine's subscription to the delegation's mandate, not a debate speech. **The grounds, verified at source 2026-09-14 rather than carried from either withdrawn read:** the act header at line 121764 runs on to the subscription formula at line 121768 with no intervening speaker verb and no intervening act number. **The formula is OCR-corrupt in this printing and will not be found by searching for its classical spelling**: [...]" **Status: Closed.** Closed 2026-09-15 as a persistence question, on the gapped-formation precedent (the item itself; the ledger entry on the 411 Gesta). The Gesta stays listed as unread and available for narrow checks. Source_Registry row 65 now carries the act 158 explanation the item said was flagged, not applied (checked 2026-09-30). (2026-09-30)
- **Line 213:** "**Closed 2026-09-14.** Candidate 5's classification, escalated to the project lead under CO-022 category 4 on 2026-09-13, is ruled **Supporting**. Round 2's own escalation assessment held that no category applied and the matter could close inside the pipeline; that disagreement is recorded rather than resolved in favour of the outcome." **Status: Closed.** Closed 2026-09-14: Candidate 5 ruled Supporting by the project lead. (2026-09-30)
- **Line 214:** "**CLOSED, 2026-09-15, on the gapped-formation precedent handed to this build thread by the project lead** (lpc_Gapped_Formation_Precedent.md §4b). **This item is a sixth attempt at a cleaner classification for Candidate 5**, after five supersessions across nine rounds and the project lead's ruling. The precedent names that pattern and its remedy: *"Treat five consecutive re-classifications of the same candidate as itself the signal to stop and accept the narrower finding."* **Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding.** Supporting rests on the candidate's own six-test result (Repetition passes, Persistence passes narrowly, Formation does not clearly pass, Dependency passes narrowly, Explanatory passes narrowly) as well as on the ruling. The argument below is recorded, not pursued. Originally raised by Doc04_Round9_Review.md. That review holds that a determinate Framework classification for Candidate 5 is reachable from this document's own premises, on the argument that Primary is excluded at §3, that Tensional is excluded, and that all three of the candidate's demonstrated relations in §6 being with Primary candidates is Supporting's own second clause. [...]" **Status: Closed.** Closed 2026-09-15 on the gapped-formation precedent; Candidate 5 is Supporting and thin, and the argument is recorded, not pursued. (2026-09-30)

### OG-36. Doc_05 section 11, open items and handoff: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_05_Ecological_Reconstruction.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 354:** "**Doc_04 §7 item 6 — the 411 *Gesta*, unread and closed as a persistence question.** Two attempts withdrawn; Doc04_Round11_Review.md names the absence of an owner and an acceptance criterion as the reason the item was not actionable as it stood. Doc_04 has closed it on the gapped-formation precedent, and the *Gesta* stays available for narrow factual checks. It bears on G5's Repetition and Persistence and on §6.1 above. **This document adds no third attempt and draws nothing from it.** Commissioning it requires the project lead: a thread that wrote neither withdrawn version to read it, and a different thread again to apply the findings." **Status: Closed.** Closed as a persistence question 2026-09-14 and 2026-09-15 (ledger entry on the 411 Gesta; Doc_04 section 7, sixth item). The Gesta stays unread and available for narrow checks; no third read is commissioned. (2026-09-30)
- **Line 355:** "**Doc_04 §7 item 8 — whether a determinate Framework classification for G5 is reachable from Doc_04's own premises.** Raised by Round 9; Doc_04 has closed it on the gapped-formation precedent and records the argument without pursuing it. Not touched here: [...]" **Status: Closed.** Closed 2026-09-15 on the gapped-formation precedent (Doc_04 section 7, eighth item). (2026-09-30)
- **Line 356:** "**Doc_04's own disposition.** Findings from Rounds 5–11 remain outstanding, and Doc_04's governance/methodology escalation remains open with three items on record. [...]" **Status: Open.** Per the Phase L0 independent-checks entry of 2026-09-29, Doc_04 Round 11 M1, M2, M4 and M6, most LOW and COSMETIC items, and Round 8 H1(d) are still open. No later file records them closed. (2026-09-30)
- **Line 357:** "**Doc_04 §7 item 5 — Augustine-phase confessor- or ascetic-authority material. ANSWERED HERE, in the negative** (§2.3), on a **corrected** sweep of all eight Augustine volumes: twenty occurrences, rule stated, all read, all enumerated, the enumeration reconciled to the per-volume counts. **The first version of this check was wrong** — case-sensitive, so blind to Confessor, reporting seventeen and enumerating sixteen; Round 1's H1 caught it and §2.3 records the correction in place. **The finding survives the correction and is strengthened by it:** the two occurrences the flawed sweep missed are the closest thing in the corpus to Cyprian's usage — *Felix the Confessor*, in Augustine's own words — and they are a **dead Italian saint with a basilica**, in a treatise about whether burial beside a saint profits the dead. [...]" **Status: Closed.** Answered in the negative in Doc_05 section 2.3, on a corrected sweep; the item records its own correction. (2026-09-30)
- **Line 358:** "**Doc_04 §7 item 4 — the anti-Manichaean half of Doc_01 §6's fifth-candidate material**, never independently tested as its own candidate. Unchanged here; nothing in this document assumes it either way." **Status: Open.** Still untested (Doc_04 section 7, fourth item; Phase L0 check of 2026-09-29, Doc_05 row 'anti-Manichaean candidate': open). (2026-09-30)
- **Line 362:** "**Doc_02 §9 items 4 and 5 — Article 20's secondary prong. DISCHARGED** at §1.4, with a correction: the load-bearing against-the-grain trace in this world is **corporate and anonymous** (the Hippo congregation of 411), not any of the three named individuals Doc_02 proposed as Lucilla-comparators. [...]" **Status: Open in part.** Discharged at Doc_05 section 1.4, but conditional on the Article 20 extension below, which is unresolved (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 363:** "**Doc_02 §9 item 9 — the liturgical material has still not been read *as* liturgical evidence.** §3 is written under that limit and says so. **This is the single largest recoverable gain available to this world's reconstruction**: rows 5, 9, 15 and 18 exist, are vendored, and have simply not been re-read for rite-form rather than doctrine. Recommended as the highest-value next acquisition-free task." **Status: Open in part.** The liturgical read was done on 2026-09-19 (two files in Review-Artifacts). Doc_05 section 3 has not been updated, and the lexicon candidates are not integrated. (2026-09-30)
- **Line 364:** "**Doc_02 §9 items 2 and 3 — no site report, inscription, or excavation record independently verified; rows 34, 35 flagged for priority review; rows 63 and 82 now name an excavation for each city but neither has been re-read.** §3 and §6.9 are bounded by this. [...]" **Status: Open.** A standing, disclosed limit: no site report or inscription verified (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 365:** "**Doc_02 §9 item 10 — the Story Inventory's provisional beginning (CF V7.4 Part II) is not yet started.** Named by Doc_02 as possibly a portfolio-wide gap rather than a defect specific to this world. **Not started here either**, and flagged: Pontius's *Life* and the Perpetua sermons are this world's obvious first two entries when it is." **Status: Closed.** Closed by Doc_09 Story Inventory (Phase L0 check, 2026-09-29: 'Stale. Closed by Doc_09'). (2026-09-30)
- **Line 369:** "**CLOSED, 2026-09-16 — read at source, in full.** Review-Artifacts/Possidius_Full_Read_2026-09-16.md, all thirty-one chapters. The original item read: *"Possidius's Vita Augustini (row 192) is vendored and unread beyond one identification."* It is this world's only biographical memory of its second phase (§6.3), and the read bore on §1, §4.1 and §6.3 exactly as the item predicted; [...]" **Status: Closed.** Closed 2026-09-16 by the full read of Possidius (the item itself). (2026-09-30)
- **Line 370:** "**The editorial-apparatus discipline (§0.6, §9.6) should be applied to the whole vendored corpus, not only to the passages this document quotes.** Two of the passages used here had 19th-century editorial matter inside the same paragraph as the bishop's words, and one of them carries a substantive interpretive claim about Cyprian's motive. **Other quotations elsewhere in this build may not have been checked this way.** This is a finding about the corpus, not about any one document, and is routed to review rather than acted on unilaterally." **Status: Open.** A corpus-wide, portfolio-level question routed to the project lead; the ledger entry on portfolio-level template and methodology defects (2026-09-15) carries it under Doc_08, with eight local instances. No ruling on file. (2026-09-30)
- **Line 371:** "**The rural and Punic/Berber-speaking substrate remains wholly unreconstructed** (§6.9), and this bounds what Doc_07 and any eventual Representative may say about congregational life outside Carthage and Hippo." **Status: Open.** A standing, disclosed limit on what Doc_07 and the Representative may say about rural and Punic-speaking congregations. (2026-09-30)
- **Line 372:** "**Article 20's against-the-grain condition, applied to a genre the Framework does not name.** §1.4 argues why a concession against interest in personal correspondence satisfies the condition, and states what the argument does *not* license. **It is an interpretive extension, flagged for the project lead to confirm or reject**, not a reading this document treats as settled. If rejected, §1.4's bounded reconstruction falls and Article 20's secondary prong reverts to undischarged for this world." **Status: Open.** Left to the project lead to confirm or reject. No ruling found in the Decision Log or the ledger (Phase L0 check, 2026-09-29; Decision Log searched again on 2026-09-30). If rejected, the secondary prong reverts to undischarged. (2026-09-30)
- **Line 373:** "**Doc_03_Lexicon_Candidate_List.md states corpus counts without stating a matching rule.** Its flock/shepherd/pastor figure of 113 reproduces exactly under raw substring matching and returns 109 under word-boundary matching on the nouns, the difference being *flocking*, *flocked*, *pastores* and *pastoral* (§4). **Neither count is wrong; the rule is simply unstated**, and the same will be true of Doc_03's other frequency figures. Doc_03 is Approved to proceed and belongs to another thread — **flagged, not edited from here**, per the project's own rule for doc-hygiene on content that is not one's own." **Status: Open.** Open. Doc_03 belongs to another thread and was flagged, not edited (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 374:** "**The *Boundary Structures* / *Boundary Ecology* divergence, established by sweeping each L3 file in full rather than its Step 5 entry alone.** The conflict does **not** run *between* the two documents, and *"Boundary Ecology"* is **not** absent from the Forces Framework. Each document uses both terms, and each is inconsistent with itself." **Status: Open in part.** Ruled for this world: Boundary Structures is canonical for lpc (2026-09-14). The inconsistency inside the governing texts is portfolio-level and open (ledger entry on portfolio-level template and methodology defects, 2026-09-15). (2026-09-30)
- **Line 383:** "L3B Construction Framework V7.4 | Part VII, Step 5 dimension list | **Boundary Structures**" **Status: Open in part.** A row of the Doc_05 table of term use across the governing texts; it is evidence for the preceding item, with the same status: ruled for this world on 2026-09-14, inconsistency in the governing texts open at portfolio level. (2026-09-30)
- **Line 384:** "L3B Construction Framework V7.4 | Part VII, Step 5 forces line | **Boundary Ecology**" **Status: Open in part.** A row of the Doc_05 table of term use across the governing texts; it is evidence for the preceding item, with the same status: ruled for this world on 2026-09-14, inconsistency in the governing texts open at portfolio level. (2026-09-30)
- **Line 385:** "L3B Construction Framework V7.4 | Part VII, naming CiC's own additions | **Boundary Structures**" **Status: Open in part.** A row of the Doc_05 table of term use across the governing texts; it is evidence for the preceding item, with the same status: ruled for this world on 2026-09-14, inconsistency in the governing texts open at portfolio level. (2026-09-30)

### OG-37. Doc_06 section 5, open items carried forward: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_06_Full_Lexicon_Development.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 120:** "**The lexicon is built on two upstream documents disposed only on the project lead's instruction.** Doc_04 and Doc_05 are both Approved to proceed, 2026-09-15, by the project lead, with escalation categories carried open against each. **Nothing in this lexicon depends on any finding still in dispute** — the gravity spine has been stable since Doc_04's Round 2 and the Doc_05 findings that move tiers here survived two rounds. [...]" **Status: Closed.** A statement of fact, true on disk: Doc_04 and Doc_05 were approved to proceed on 2026-09-15 by the project lead. No action pending. (2026-09-30)
- **Line 121:** "**CLOSED, 2026-09-16 — Possidius's *Vita Augustini* (Registry row 192) has been read in full** (Review-Artifacts/Possidius_Full_Read_2026-09-16.md, all thirty-one chapters). It was the natural source for the *suffrage* entry's Augustine half, and that entry no longer rests on Augustine's own letters alone: Lexicon-Chunks/lpclex011_suffrage.md now rests its account of his two offices on the *Vita*'s chapters IV and VIII, corrected accordingly. [...]" **Status: Closed.** Closed 2026-09-16 by the full read of the Vita (the item itself). (2026-09-30)
- **Line 122:** "**One term this lexicon does not contain, flagged rather than added.** Doc_05 §3 establishes that both of this world's defining crises are, at bottom, disputes about *rites*, and that the liturgical material has **never been read as liturgical evidence** (Doc_02 §9 item 9). If that reading is done, it will very likely surface at least one term — a name for the rite of reconciliation itself, or for the baptismal rite as administered — that Doc_03's candidate discovery could not have found, because it swept for doctrine rather than rite. **Adding a term on that expectation would be invention; [...]" **Status: Open in part.** The liturgical read was done on 2026-09-19; the term it may surface was not added and the candidates (public confession, the baptismal interrogation) are not integrated (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 123:** "**Source_Registry.md is returned to independent review**, and every chunk's Key Sources cites it. No row this lexicon depends on is among those corrected on 2026-09-13." **Status: Closed.** The Registry went through independent check on 2026-09-29 and a fix-pass recheck on 2026-09-30 (Review-Artifacts/Doc02_Returned_Review_Independent_Check_2026-09-29.md and Doc02_Registry_FixPass_Recheck_2026-09-30.md). Residue is carried in the ledger entries on those checks, dated 2026-09-29 and 2026-09-30. (2026-09-30)
- **Line 124:** "**Doc_03's corpus counts are reproducible but their matching rule is unstated.** Doc_05 §11 item 14 established that the flock/shepherd/pastor figure of 113 reproduces exactly under markup-stripped substring matching and returns 109 counting the pastoral nouns alone. Every frequency figure quoted in these chunks is Doc_03's, and the same caution applies to all of them. Doc_03 is Approved to proceed and another thread's — **flagged, not edited from here.**" **Status: Open.** The matching rule for Doc_03's frequency counts is still unstated (Phase L0 check, 2026-09-29). Doc_03 is another thread's. (2026-09-30)
- **Line 125:** "**The editorial-apparatus problem is corpus-wide and this lexicon is where it bites hardest.** Lexicon_Deployment_Index.md §7 registers **seven** entries that rest near 19th-century editorial matter printed inside or beside the primary text. One of those — the volume preface calling Augustine's coercion doctrine *"a false exegesis"* and *"least satisfactory to Protestant readers"* — is a **Protestant editor's theological verdict sitting in the same volume as the text it judges**, and is precisely the kind of material that could reach a participant as this world's own voice if a later pass were less careful. Doc_05 §11 item 11 routed the corpus-wide question to the project lead; this document registers **seven** local instances: five are excluded from their entries outright, the sixth is marked in place where a World Meaning turns on it, and the seventh is a misquotation this deliverable itself committed inside the entry it had just added." **Status: Open.** Portfolio-level: the corpus-wide editorial-apparatus question, carried under Doc_08 in the ledger entry on portfolio-level template and methodology defects (2026-09-15). The local instances remain as stated. (2026-09-30)
- **Line 129:** "**A discovery-method finding that outlives the term it recovered.** Doc_03 swept the Latin headword *libelli*, correctly found it absent from the vendored English corpus, and did not sweep the English word the translation uses 42 times. **A headword sweep in the original language cannot find a term the surviving corpus only ever names in translation.** This world's corpus is a 19th-century English translation throughout; every other frequency-based discovery judgement in Doc_03 rests on the same method. [...]" **Status: Open.** Left to the project lead as a method question (Phase L0 check, 2026-09-29: 'Goes to Mark'). No ruling on file. (2026-09-30)
- **Line 131:** "**A third governing-document inconsistency, of the same family as the two already open.** LDF Part III's Tier 1 section list names **Key Texts** and **Key Sources** as two distinct sections; the L4 Deployment Lexicon Chunk Template has only Key Sources, and no chunk in any world carries a Key Texts section. Round 1's M3. **Not resolved here** — the L4 template is a coach-thread file and the Framework is governing methodology; both are outside a build thread's write scope. [...]" **Status: Open.** Portfolio-level: the Key Texts and Key Sources mismatch, carried in the ledger entry on portfolio-level template and methodology defects (2026-09-15). No ruling on file. (2026-09-30)

### OG-38. Doc_07 section 8, open items and handoff: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_07_Integrated_Ecology_Analysis.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 242:** "**§4 is a synthesis, not a compilation.** Doc_08 owes the full six-cell matrix at three layers, Transmission as a named force dimension in cells 2B and 3B, and the Forces-and-Gravities Synthesis. §4's four named force-clusters — the Decian administrative demand, the Donatist appeal to Cyprian's authority, the plague, and the metabolize-crisis-into-teaching mechanism — are the threads to compile, not the compilation." **Status: Closed.** Consumed: Doc_08 Forces Document exists and had a targeted check on 2026-09-29 (Review-Artifacts/Doc08_Round9_Targeted_Check_2026-09-29.md). (2026-09-30)
- **Line 243:** "**G5's incomplete-ecology shape must be carried, not resolved.** Doc_04 records that this candidate exhibits the shape the Forces Framework names for a gravity that cannot be fully connected to the forces acting on the world. §4 confirms rather than closes it. [...]" **Status: Closed.** Carried as instructed: Doc_08 states the G5 force connection is indirect and carries Doc_04's incomplete-ecology finding forward. (2026-09-30)
- **Line 244:** "**Transmission is unusually load-bearing in this world** and §3A gives Doc_08 its starting point: continuity across the 133-year gap is textual rather than successive; a non-textual continuity, the oratory in memory of Cyprian at Carthage that *Confessions* V.8 records, is not assessed here." **Status: Not determined.** Doc_08 names the oratory in memory of Cyprian (Confessions V.8) but does not assess it. The ledger entry on the claims register (2026-09-30) mentions a ruling covering it, but the ruling's own file was not found. The project lead's 2026-09-30 ruling text on the oratory would settle it. (2026-09-30)
- **Line 248:** "**Three documents reached *Approved to proceed* only on the project lead's own instruction, never by self-disposition** — Doc_04, Doc_05, Doc_06 — carrying **three portfolio-level items** (the corpus-wide editorial-apparatus question; the *Boundary Structures* / *Boundary Ecology* inconsistency inside both L3 files; the Key Texts / Key Sources template mismatch), **four governance/methodology items** (Doc_04's three plus the translated-corpus discovery-method finding), and **no unresolved tension** (item 6 records the closed *Gesta* question)." **Status: Open in part.** The Gesta part is closed (ledger entry on the 411 Gesta). The three portfolio-level items stay open (ledger entry on portfolio-level template and methodology defects, 2026-09-15), and the item's count of open tensions rests on the stale Gesta state (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 249:** "**A fourth Framework/template divergence, added here.** The Doc_07 template documents the pre-M4 lens structure while the Framework and the Completion Standard require the M4 spine (§1). **Named for census-level correction, not corrected from here** — L4 templates are coach-thread files." **Status: Open.** The Doc_07 template predates the M4 lens structure; the template belongs to the coach thread. The Phase L0 check of 2026-09-29 corrects the record: Doc_07 itself is on the seven-dimension spine; the defect is in the template. (2026-09-30)
- **Line 250:** "**The 411 *Gesta* remains unread** but is closed as a persistence question (Doc_04 §7 item 6); and **Doc_04 §7 item 8 is closed** on the gapped-formation precedent, which records the argument without pursuing it — Round 9's finding that a determinate Framework classification for G5 is reachable from Doc_04's own premises and has not been run. **Item 2 binds every downstream document to note both; [...]" **Status: Closed.** Both closed: the Gesta on 2026-09-15 and the classification question on 2026-09-15 (Doc_04 section 7, sixth and eighth items). (2026-09-30)
- **Line 251:** "**CLOSED, 2026-09-16 — Possidius's *Vita Augustini* (row 192) has been read in full** (Review-Artifacts/Possidius_Full_Read_2026-09-16.md, all thirty-one chapters). It was the natural source for §2C's thinnest corner, and §2C and §2F both now draw on it." **Status: Closed.** Closed 2026-09-16 by the full read of the Vita (the item itself). (2026-09-30)
- **Line 252:** "**The liturgical material has never been read *as* liturgical evidence** (Doc_02 §9 item 9). Given §2A's finding that this world's crises *are* rite disputes, **this is the highest-value unblocked task in the build**, and Doc_06 §5 item 3 expects it to surface at least one further lexicon term." **Status: Open in part.** The read was done on 2026-09-19; the lexicon terms it proposes are not integrated (Phase L0 check, 2026-09-29). (2026-09-30)
- **Line 253:** "**This world still has no Open_Gaps_Tracking.md**, required of every world by CLAUDE.md and held by only three of twelve. Fleet-level." **Status: Closed.** Out of date: this ledger, Open_Gaps_Tracking.md, now exists for lpc. (2026-09-30)
- **Line 254:** "**This document runs about 12% over the template's word target** (§1), and the overage grew across two fix passes because each added content a finding required. **A condensing pass on §2 is the remedy** — the nine lenses repeat between their two halves in places — and it should be run by a thread that is not also applying findings, since every pass that has tried to trim while fixing has added more than it cut." **Status: Open.** The condensing pass has not been run (Phase L0 check, 2026-09-29). The length was not re-measured after the change order of 2026-09-30. (2026-09-30)

### OG-39. Doc_09 section 8, open items carried: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Doc_09_Story_Inventory.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 134:** "**The *Acta Proconsularia* is unread** (§6 item 2). Reading it would move lpcstory006 from Tier 3 to Tier 1. **Ranked second** among the unread sources, behind item 9." **Status: Open.** The Acta Proconsularia is still recorded as vendored in Latin only and unread (Decision Log, Doc_09 entry); no file records a read. (2026-09-30)
- **Line 135:** "*(Merged into item 5 below; the number is kept so cross-references to later items stay valid.)*" **Status: Closed.** A placeholder: the item was merged into the Perpetua sermons item and its number kept. Nothing further to carry. (2026-09-30)
- **Line 136:** "**The provisional Step-2 inventory was never made** (Doc_02 §9 item 10) — disclosed at the head of this document. Whether that is a defect in this build or a portfolio-wide pattern is Doc_02's own open question and is not resolved here." **Status: Closed.** Closed for this world by Doc_09 itself. Whether the missing Step-2 inventory is a portfolio-wide pattern has no recorded outcome. (2026-09-30)
- **Line 137:** "**The 411 *Gesta* remains unread** and no story draws on it (Doc_08 §9)." **Status: Closed.** Closed as a persistence question 2026-09-15. The Gesta remains unread and no story draws on it. (2026-09-30)
- **Line 138:** "**Augustine's sermons on Perpetua (*Sermones* CCLXXX to CCLXXXII, row 227) are vendored as second-witness OCR and unread** (§6 item 1). A reading task; sermons on the Scillitan martyrs also stand in rows 229 and 230, unread (row 230 is a finding aid only, licensed for no claim about Augustine's own preaching)." **Status: Open.** Still unread. The claims change order of 2026-09-30 left Sermones CCLXXX to CCLXXXII unread by design and records them as a Tier-question candidate (ledger entry on the claims change order, 2026-09-30). (2026-09-30)
- **Line 139:** "**lpcstory005 still paraphrases rather than quotes Lucian's grant of peace**, pending a check of the ANF parenthesis against the Latin at rows 191/194." **Status: Open.** Still open: lpcstory005 keeps its paraphrase discipline, and the check of the ANF parenthesis against the Latin at rows 191 and 194 is not recorded as done. (2026-09-30)
- **Line 140:** "**CF V7.4's Tier 3 definition points two ways at lpcstory006, and this build cannot settle which clause governs.** The tier's **genus clause** — material *"resting on collected tradition rather than direct documentation"* — **excludes an eyewitness**, and Pontius is one. The tier's **hagiographic-convention clause** describes this story exactly. Tier 3 is assigned here on the conventions and **against the genus clause**, which is disclosed in the chunk's Tier Justification. **Routed to the project lead as a governance/methodology item.** This is distinct from the *"a source is not a tier"* escalation withdrawn at Round 4: [...]" **Status: Open.** Open, for the project lead: the ledger entry on Doc_09's own Tier-3 escalation for lpcstory006 states that no later entry resolves it. (2026-09-30)
- **Line 141:** "**Augustine's *Confessions* (row 9) yields no story, and is the strongest Phase Two candidate for the next pass** (§6 item 3). Phase Two currently rests on one story from a four-chapter span of Possidius (XXVIII–XXXI, of which XXXI carries the story), while the one extended first-person text this world has goes unused. The scope reason given — that it narrates a conversion rather than a pastorate — is thin, and Book X in particular is a bishop examining his own continuing sin." **Status: Open.** Open: Confessions yields no story and is named the strongest Phase Two candidate. No file records a decision to build one. (2026-09-30)
- **Line 142:** "**CLOSED, 2026-09-15 — read at source.** Review-Artifacts/Possidius_XIX-XXVII_Read_2026-09-15.md. What remains open is building a story from it, not reading it. The original item read: Possidius, *Vita Augustini* XIX–XXVII — nine chapters of ordinary episcopal practice — is vendored, Native (row 192), and unread (§7 item 5; Doc_05 open item 10). It is the only extended account of the daily work this world makes its Primary gravity, and it sits in the file lpcstory007 already draws on. **Reading it is the largest available improvement to this document — ranked first, ahead of item 1** — because it bears on whether Doc_09 should carry a Tier 4 story at all, where item 1 changes one story's tier." **Status: Closed.** Closed 2026-09-15 by the read at source (the item itself). Building a story from it remains open (ledger entry on Possidius chapters XIX to XXVII). (2026-09-30)

### OG-40. Step 0 section 4, binding items: present status of each, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 134:** "**The Article 3 century-gap ambiguity (binding on Doc_01's Strand Determination and World Continuity & Distinction work).** Carried forward verbatim from the Step 0 Conclusion, neither created nor resolved by this confirmation (§2 above). Doc_01 must make an actual, reasoned determination — strand-plural (Cyprian-strand, Augustine-strand, explicitly reasoned per Article 21) or some other coherent framing — rather than silently assuming continuity or silently treating the gap as immaterial." **Status: Closed.** Closed for this world: Doc_01 section 5 makes the determination (re-confirmed by Doc_01 Round 9 review), and Article 3 was ruled closed for lpc on 2026-09-16 (ledger, closed items). The portfolio-level filing is tracked separately. (2026-09-30)
- **Line 135:** "**The World #4 (Donatism) boundary (binding on Doc_01/Doc_02) — now specific, not general.** This world holds Cyprian's pastoral office under persecution and Augustine's ordinary congregational life; the schism-crisis itself belongs to World #4, per the reciprocal Article 23 obligation established at §2 A5 above — this is a characterization of Cyprian's own primary gravity, not a blanket exclusion of schism-related material from this world's own sources (§3 B3). Concretely: (a) Optatus's *Against the Donatists*, currently assigned to this world in the corpus-map on a provisional, self-flagged-as-inferred basis, presents a genuine open placement question — re-home to Donatism, hold here as the Catholic-side tradition (the corpus-map's own stated reason), or double-place — that Doc_02 must actually resolve, not inherit silently and not pre-decide; (b) the Council of Carthage under Cyprian (256) is modeled **twice** in the corpus-map under different vendored editions — once with an explicit Donatism double-placement note (npnf214, author: council-of-carthage-under-cyprian) and once without one (anf05, author: cyprian, the edition this document's own B1 cites) — Doc_02 must reconcile the duplication, not carry only one row's note forward; (c) the Anonymous Treatise on Re-baptism's Donatism bearing is explicitly unassigned by the corpus-map and Doc_02 should either resolve or preserve that as a stated unresolved question, not silently claim it as exclusively Native; (d) Doc_02 must reconstruct the Donatist schism as this world's own internal rival, from this world's own perspective, per the Article 23 reciprocal obligation now on record with Donatism's own parallel build; [...]" **Status: Open in part.** (a) Optatus placement open, the project lead's question (Source Readiness Dossier entry, 2026-09-30). (b) Duplicate corpus-map rows for the 256 council still present. (c) The Donatism bearing of the Treatise on Re-baptism: Source_Registry row 8 holds it as Native at Confidence C, and whether the bearing is stated was not determined from the files. (d) Article 23 routing: not determined from the files. (e) Reading divergence: closed in Doc_01 section 5. (2026-09-30)
- **Line 136:** "**Elite/literate/male source-skew, sharpened form (binding on Doc_02).** Both anchor voices are bishops; the world's own "ordinary believer" subject matter is attested only through episcopal mediation. Doc_02 must name this specifically, not defer to the general portfolio-wide caveat alone. Article 20's affirmative duty (whose voices the source record structurally suppresses) is a Construction Framework Step 2 activity and belongs here, not at Doc_01 (correcting §2 A5's earlier misrouting)." **Status: Closed.** Discharged in Doc_02 section 6. (2026-09-30)
- **Line 137:** "**A mature but incomplete source-assignment already exists and should be used, not re-derived from zero, and not trusted uncritically (binding on Doc_02).** cic/corpus-map/latin-pastoral-congregational-christianity.yaml is a real, reasoned starting inventory and should be treated as required input to Doc_02's own Source Registry work — cross-checked and extended, with item 2's specific corrections applied, not duplicated wholesale." **Status: Closed.** Discharged: Doc_02 was built on the corpus map, with the corrections (Doc_02 section 1). (2026-09-30)
- **Line 138:** "**Reciprocal boundary obligations from two already-built worlds (binding on Doc_01).** IJC's own Step 0 §4 item 3 logged: "The authority-structure/state-power boundary... must be stated explicitly in Doc_01, since World #8 is not yet built and cannot itself hold the line from its side" — that condition has now changed, and Doc_01 must state the boundary from this world's own side. Separately, and distinctly, Hieronymian's built Doc_01 §8.1 is on record waiting for this world to "independently" supply "the comparison's other half" of its own authority-mode contrast (charismatic-scholarly vs. [...]" **Status: Closed.** Discharged in Doc_01 section 7 (World #9 'Discharged here'; the state-power boundary stated from this world's side). (2026-09-30)
- **Line 139:** "**The Tertullian dropped-voice disclosure (binding on Doc_01/Doc_02).** Per §1 above: this world's own existence, in its current Cyprian/Augustine shape, is why Tertullian — "credited with forging much of the Latin theological vocabulary the whole Western tradition depends on" — has no world of his own. Doc_02's Author Gravity work for Cyprian should name Tertullian as a real, non-Native influence-source (Excluded / Named Comparandum, not Native — Tertullian is not this world's own voice), and this disclosure itself should be logged rather than silently absorbed." **Status: Closed.** Discharged in Doc_02 section 2 and Registry row 5. (2026-09-30)
- **Line 140:** "**The Antiochene primary-gravity contrast (binding on Doc_01/Doc_04).** The Step 0 Conclusion holds this world out as the standing comparison case for Antiochene Christianity (a Possible Future World, not selected for this phase): Antiochene was held out of Phase One "pending a validated primary-gravity contrast against world #8 that doesn't rely on geography or language." This world's own Doc_01 boundary work and Doc_04 gravity-orientation work should establish Cyprian's and Augustine's primary characterization in terms that would survive that contrast if Antiochene is ever built — not merely in terms of Latin/Greek or North Africa/Antioch — per §3 B3 above." **Status: Closed.** Discharged by name in Doc_04 section 5. (2026-09-30)
- **Line 141:** "**Primary-gravity-first discipline (binding on Doc_01, general methodological note).** The Step 0 Conclusion's own Primary-gravity-first rule was adopted specifically in response to a review finding about *this world's own* history (the original World #8/#9 split had used neighbor-protection — shielding Donatism's distinctiveness — as an unstated tiebreaker rather than reasoning to Cyprian's own primary characterization first, "though partly mitigated there, since Cyprian's ecclesiology and pastoral crisis-management are historically fused rather than cleanly separable"). Doc_01's own gravity-orientation work should establish Cyprian's and Augustine's primary characterization on this world's own ecological terms first, and treat neighbor-distinctiveness (from World #4 in particular) as a tiebreak only where genuinely needed." **Status: Closed.** Discharged: Doc_01 states the primary characterization first, at section 3, before the World #4 boundary (Doc_01 section 8, seventh item). (2026-09-30)

### OG-41. Decision Log, the Representative identity and image entry (2026-09-15) and the Doc_04 closure entries: present status of each open item, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/lpc_Decision_Log.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 1534:** "**lpc is not in the worlds registry.** Nine worlds are registered and this is not one of them, so there is no world entry to carry a representative: {name, role_label} line. Adding one is world registration — it needs card_name, census_id, thinness_statement, state and a package manifest hash — and is a separate step from M1. [...]" **Status: Open in part.** A registry entry now exists at records/worlds/lpc.yaml, created 2026-09-30 with kind, world_id, time window, place, census_id and safety_adjacent only. The Representative line, card fields, thinness statement, state and package hash are not there; they come at admission and are the project lead's (ledger entry on the registry entry, 2026-09-30). (2026-09-30)
- **Line 1535:** "**The portrait file is not in the repository.** Per Representative-Portraits/README.md the convention is Name_Portrait.png; this one belongs at [the Datus portrait path, omitted], and at cic-website/assets/portraits/ for serving. The image was produced outside this session and has not been committed." **Status: Closed.** The portrait is committed at Build/Ministry/Communication/Brand-Assets/Representative-Portraits/lpc/ (branch reconciliation, 2026-09-21; both files present, checked 2026-09-30). The name-convention drift and the missing serving location stay open in the ledger entry on the Datus portrait being wired to no live location. (2026-09-30)
- **Line 1536:** "**the L4 Representative Construction Notes Template has no image or appearance section**, though CLAUDE.md cites it as governing the identity-and-image package. Every image brief in the portfolio so far has been written ad hoc into an SVG header or a build ledger, as this one is. **A real gap between CLAUDE.md and the template, raised for the project lead** — closing it is a methodology change." **Status: Open.** The template Build/reference/L4-Templates/Representative_Construction_Notes_Template.md has no image or appearance section (searched 2026-09-30). Closing it is a methodology change, so it is the project lead's. (2026-09-30)
- **Line 1537:** "**[CORRECTED, 2026-09-15 — checked against origin/main after this entry was first written.]** An earlier version of this item said Fidelis had no image documentation of any kind. **That is false.** main carries donatism/Fidelis_Portrait_Prompt.md — a full research brief and generation prompt, APPROVED 2026-09-10, with a disposition history. The stale loose file this build was reading (Fidelis_Portrait.png.jpg at the folder root) had since been reorganised into the per-world folder convention. **The error was mine: I read a branch that predates main's reorganisation and reported an absence that the live repository refutes** — this world build's own recurring defect class, committed in its own Decision Log." **Status: Closed.** A recorded self-correction (2026-09-15): main carries the Fidelis portrait brief. No action pending. (2026-09-30)
- **Line 1539:** "**Dress and complexion are INFERENCE, not DOCUMENTED.** Stated here so no downstream document treats them as established." **Status: Closed.** A standing disclosure, not a gap: Datus_Portrait_Prompt.md still flags dress and complexion as inference (checked 2026-09-30). (2026-09-30)
- **Line 1716:** "closed.** It was a **sixth** attempt at a cleaner classification for Candidate 5, after five supersessions across nine rounds and the project lead's direct ruling of 2026-09-14. The precedent: *"Treat five consecutive re-classifications of the same candidate as itself the signal to stop and accept the narrower finding."* **Candidate 5 is Supporting and honestly thin, and that is the answer.** The argument is recorded, not pursued." **Status: Closed.** Closed 2026-09-15; Candidate 5 is Supporting (Doc_04 section 7, eighth item). (2026-09-30)
- **Line 1717:** "closed as a Persistence question.** It proposed reading the 411 *Gesta* to shore up Candidate 5. The *Gesta* is **native to Donatism's world, not this one**, and the precedent records both prior extraction attempts failing review. Its rule: such a source is for *"narrow, specific, independently-verifiable facts only."* The *Gesta* stays available for narrow checks and stays listed as unread; [...]" **Status: Closed.** Closed 2026-09-15 as a persistence question (Doc_04 section 7, sixth item; ledger entry on the 411 Gesta). (2026-09-30)

### OG-42. Doc01 Round 8 review: present status of its findings, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/Doc01_Round8_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 179:** "**The provenance is never disclosed.** §5 attributes the flag only to *"the harder, adjacent question Step 0 flagged and left open,"* with no pointer, in a section whose immediately preceding sentence points to this world's own Step0_Movement_Scope_Confirmation.md. The words "portfolio," "Constitutional ambiguity," "standing interpretive question," "gapped" and "diachronic" appear nowhere in Doc_01 in this connection — I swept for all five. A reader cannot tell from Doc_01 that this is a portfolio-level logged ambiguity in which this world is the named test case, rather than a housekeeping deferral by its own Step 0. This is precisely the disclosure CO-022 category 2's second sentence asks for — *"Label it explicitly as portfolio-level in whatever document records it, distinct from an ecology-grounded finding"* — and it is the label §5 and §9 do supply, correctly, for the Coach3 axis and for the orthogonality clause." **Status: Closed.** Fixed. Doc01_Round9_Review.md re-derived the Round 8 findings and found the HIGH fixed completely. Doc_01 section 5 now names the portfolio Step 0 Conclusion's 'Constitutional ambiguity flagged, not resolved', and section 9 now counts three category 2 items (checked on disk 2026-09-30). (2026-09-30)
- **Line 180:** "**§9 assesses it under no category, while claiming completeness.** §9's category-2 paragraph says *"two items"*; its category-3 paragraph says *"Two candidates"*; its closing paragraph says *"Category 3's candidate is §5's Article 21 reading-divergence."* The Article 3 answer appears in none of the three enumerations." **Status: Closed.** Fixed. Doc01_Round9_Review.md re-derived the Round 8 findings and found the HIGH fixed completely. Doc_01 section 5 now names the portfolio Step 0 Conclusion's 'Constitutional ambiguity flagged, not resolved', and section 9 now counts three category 2 items (checked on disk 2026-09-30). (2026-09-30)
- **Line 181:** "**Worse, §9 uses it as support without having assessed it.** §9 line 267 argues that the Article 21 reading is *"the same kind of judgment this document has already made, **without escalating**, for Article 3's 'sufficient historical coherence,' Article 15's development-and-instability principle, and Article 29's confirmation gate."* It is not the same kind in the relevant respect. Articles 15 and 29 carry no portfolio-level logging as unresolved; the Article 3 question carries an express one, naming Cyprian/Augustine-with-Donatism-between as its instance. [...]" **Status: Closed.** Fixed. Doc01_Round9_Review.md re-derived the Round 8 findings and found the HIGH fixed completely. Doc_01 section 5 now names the portfolio Step 0 Conclusion's 'Constitutional ambiguity flagged, not resolved', and section 9 now counts three category 2 items (checked on disk 2026-09-30). (2026-09-30)

### OG-43. Doc02 Round 1 review: present status of the quoted corpus-map entry, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/Doc02_Round1_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 94:** "*The Acts of the Council of Carthage under Cyprian (256, on baptism)*, author: council-of-carthage-under-cyprian, source_file: npnf214_seven-ecumenical-councils.xml, **confidence: provisional**, with the note *"Donatism is included as shared ancestry rather than heresiology: the Donatists claimed this council's baptismal doctrine as their patrimony... [...]" **Status: Open.** This quotes the corpus-map entry for the 256 council, marked provisional on its double placement with Donatism. The entry is unchanged in the corpus map (checked 2026-09-30); the duplicate-row question is open (Doc_01 entry above). (2026-09-30)

### OG-44. Doc04 Round 3 review: present status of its Candidate 5 findings, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/Doc04_Round3_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 70:** "**Line 164, §4's summary row, Classification column:** *"**Tensional** — tested against Supporting and Primary and reaches neither; **reaches Tensional on the Framework's own "unresolved pressure within the ecology" definition** (see §3, §5)."* No provisional marker, no escalation, no "pending". This asserts exactly the proposition §3 says was never earned by the test." **Status: Closed.** Fixed: Doc_04 now labels only Candidate 8 Tensional, and Candidate 5 is Supporting at every site (Doc_04 independent check of 2026-09-29; Doc_04 searched for 'Tensional' on 2026-09-30). (2026-09-30)
- **Line 71:** "**Line 173, §5:** *"What it is not, on §3's own corrected classification, is **Primary or Supporting**: it is **Tensional**, an unresolved pressure within the ecology that does not organize broadly."* §5 contains no mention of the escalation at all." **Status: Closed.** Fixed: Doc_04 now labels only Candidate 8 Tensional, and Candidate 5 is Supporting at every site (Doc_04 independent check of 2026-09-29; Doc_04 searched for 'Tensional' on 2026-09-30). (2026-09-30)
- **Line 72:** "**Line 186, §5's survival bullets:** Candidate 5 *"tested here for the first time as a candidate gravity and **found Tensional**, a genuine, bounded result rather than a foregone one"*; line 188: *"one axis Doc_01 flagged for particular weight is **tested and found Tensional** without reopening the finding that flagged it."*" **Status: Closed.** Fixed: Doc_04 now labels only Candidate 8 Tensional, and Candidate 5 is Supporting at every site (Doc_04 independent check of 2026-09-29; Doc_04 searched for 'Tensional' on 2026-09-30). (2026-09-30)
- **Line 73:** "**Line 203, §6:** *"Candidate 5's own row is included on the same footing as any Tensional gravity's, since it was **fully tested**."*" **Status: Closed.** Fixed: Doc_04 now labels only Candidate 8 Tensional, and Candidate 5 is Supporting at every site (Doc_04 independent check of 2026-09-29; Doc_04 searched for 'Tensional' on 2026-09-30). (2026-09-30)
- **Line 74:** "**Line 208, §7 Open Item 2 — the item that carries the claim to Doc_05/Doc_07/Doc_08:** *"it remains real, substantial, and directly quoted evidence of a live theological difference between this world's own two anchor figures, **tested and confirmed as its own bounded, unresolved pressure within the ecology**."* Open Item 2 is the one place a downstream builder is *guaranteed* to read, and it instructs them on a classification it presents as settled, with no pointer to Open Item 7 five lines below it." **Status: Closed.** Fixed: Doc_04 now labels only Candidate 8 Tensional, and Candidate 5 is Supporting at every site (Doc_04 independent check of 2026-09-29; Doc_04 searched for 'Tensional' on 2026-09-30). (2026-09-30)

### OG-45. Doc04 Round 5 review: present status of its residue findings, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/Doc04_Round5_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 73:** "**The Decision Log**, line 652, says: *"a residue sweep confirmed the only remaining Tensional references are Candidate 8's own (genuinely Tensional, untouched) and the historical record in Open Item 6 and §8."* I enumerated all sixteen lines containing "Tensional" at HEAD and classified each. Fifteen are accounted for by that description. [...]" **Status: Closed.** Fixed: no live Tensional label remains on Candidate 5 in Doc_04 (searched 2026-09-30; Doc_04 independent check of 2026-09-29). (2026-09-30)
- **Line 74:** "**Round 4's H1 is reported resolved.** Round 4 named three sites: line 99, line 175, line 211. Lines 99 and 175 were rewritten. **Line 211 was not touched at all** — Round 4 had already flagged it as byte-identical to ccb25f37, and it is still byte-identical now, one round later." **Status: Closed.** Fixed: no live Tensional label remains on Candidate 5 in Doc_04 (searched 2026-09-30; Doc_04 independent check of 2026-09-29). (2026-09-30)

### OG-46. Doc04 Round 9 review: present status of its Doc_05 pointer finding, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/Doc04_Round9_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 303:** "*"**revisit the classification**, which the Framework directs for ambiguous candidates and which **Doc_05 is the first step positioned to do**."* Checked against CF V7.4's Step 5 entry (paragraphs 652–663): Doc_05's activities are reconstructing the ecology dimensions, integrating forces, applying Article 23, and running the Proportionality and Ecological Integration Assessments. **Gravity classification is Step 4's activity (paragraph 649) and appears nowhere in Step 5's list.** The Framework does direct revisiting *as ecological reconstruction progresses*, so the pointer is not wrong in principle — but the document asserts Doc_05 is *"positioned"* to do it without checking, and names no mechanism by which a reviewed and approved Doc_04 would be amended by a later document. [...]" **Status: Closed.** Superseded: Doc_04 no longer carries the 'positioned to do' instruction (searched 2026-09-30), and the Open Item it came from was closed 2026-09-15. (2026-09-30)

### OG-47. Phase L0 check of Docs 03, 05, 06 and 07: the items it found missing from this ledger, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/L0_Docs03-05-06-07_Carried_Open_Check_2026-09-29.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 225:** "Doc_03's governance item, its two discovery gaps, and the unswept rows." **Status: Open.** Open as of the check, and no later file records a fix: Doc_03's Part II tagging question at candidate stage and the Contest Type gap (the Contest Type half discharged in substance by Doc_06 section 3), the Manichaean Elect and Hearers discovery gap, the epidemic and mortality vocabulary absence, and the unswept rows 1, 19 and 21. (2026-09-30)
- **Line 227:** "Doc_06's carried R2 findings (M-N3, L-N2 residue, L-N3, C-N1), the *suffrage* [DR] tension, the M-R2 residue and the §5.7 discovery-method item." **Status: Open.** Open as of the check, and no later file records a fix (the claims change order of 2026-09-30 did not touch lpclex017 or lpclex018 in any file read): Doc_06 Round 2 findings M-N3, L-N2 residue, L-N3 and C-N1, the suffrage [DR] tension, the M-R2 residue, and the discovery-method item. (2026-09-30)
- **Line 229:** "The liturgical-read lexicon candidates of 2026-09-19, not yet integrated." **Status: Open.** Open: the lexicon candidates proposed by the liturgical reads of 2026-09-19 (public confession; the baptismal interrogation) are not integrated. (2026-09-30)

### OG-48. World Profile Round 1 review: present status of the Doc_04 Open Item 8 findings, checked 2026-09-30.

Each item is quoted from `Build/worlds/lpc/Review-Artifacts/WorldProfile_Round1_Review.md` and given its status from the files on disk on 2026-09-30. No item is decided here.

- **Line 188:** "Section 2, G5 *Brief description*: *"**Doc_04 §7 Open Item 8 records that Doc04_Round9_Review.md holds a determinate Framework classification is reachable from Doc_04's own premises and has not been run — the outcome that argument reaches would agree with Supporting, but the warrant is unaddressed, not settled**, and this document does not resolve it either."*" **Status: Closed.** Closed: Doc_04 Open Item 8 was closed 2026-09-15, the World Profile was approved to proceed on 2026-09-19 after later rounds, and the current profile no longer carries the quoted wording (checked lpc_World_Profile.md on 2026-09-30). (2026-09-30)
- **Line 189:** "Disposition: *"The one genuine disagreement this document carries forward … Doc_04 §7 Open Item 8 records that a later review round … holds Doc_04's own classification of G5 is reachable by an argument Doc_04 itself has not run…"*" **Status: Closed.** Closed: Doc_04 Open Item 8 was closed 2026-09-15, the World Profile was approved to proceed on 2026-09-19 after later rounds, and the current profile no longer carries the quoted wording (checked lpc_World_Profile.md on 2026-09-30). (2026-09-30)
- **Line 190:** "Disposition, *Escalation-category assessment*: *"*Unresolved tensions:* one carried forward and disclosed rather than resolved — Doc_04 §7 Open Item 8, above."*" **Status: Closed.** Closed: Doc_04 Open Item 8 was closed 2026-09-15, the World Profile was approved to proceed on 2026-09-19 after later rounds, and the current profile no longer carries the quoted wording (checked lpc_World_Profile.md on 2026-09-30). (2026-09-30)

### OG-49. The Doc_08 generator's two HIGH defects fixed, and what the fix leaves open, 2026-09-30.

Decided by the project lead on 2026-09-30 (option (b) of the Doc_08 independent check, `Review-Artifacts/Doc08_Round9_Targeted_Check_2026-09-29.md`): fix the two HIGH defects, cut the claims the code does not support, and keep the rest open.

**Fixed in `scripts/gen_force_index.py`.** The verdict parser reads only the `## VERDICT` heading lines and halts when a heading is missing, states two verdicts, or disagrees with another heading; a second method compares each Doc_08 Document Log row with the parsed verdict. Approval is read only from the leading words of Doc_08's Status line and of the Disposition section's opening paragraph; a mismatch halts. One notice pattern now serves the stripper, the detector and the no-notice rule, and the five notice shapes the check named all halt. A self-test runs before Doc_08 is read. `--help`, a missing directory, no review files and a missing heading now halt with a message. `lpc_Force_Index.md` regenerates byte-identical.

**Text cut to what the code derives.** The Index controls paragraph and Disposition, and Doc_08's controls paragraph, Status line, Disposition and section 9 closure sentence. Doc_08's section 5 third point and section 9 second point now say the 411 *Gesta* question is closed as a persistence question (Doc_04 section 7, closed 2026-09-15); section 8 no longer says `[ADDED ...]` clauses are retained deliberately.

**Still open.** A notice in a shape outside the new pattern is not detected, and a legitimate bracket of notice shape still halts (the Index "Limits" paragraph says so). Section 9's cell distribution is read by nothing beyond the count. The other forms of the review-history guard (a round run twice, deleted Round 3 and Round 4 rows) are not caught. Doc_08 lines 217 and 334 carry commentary the checker flags. Whether the Round 9 check counts as a review of the Round 8 revision is the project lead's question, the fourth decision listed in that review file (2026-09-29). Generator line count of flagged commentary: 28 (from 75).


### OG-50. The silence claims and row 194: an open exception found, 2026-09-30.

An independent check (`Review-Artifacts/ClaimsScopeRecheck_2026-09-30.md`, finding F1) found that the silence claims scoped to the Registry's Native rows overreached. Row 194 (Hartel, CSEL 3 Pars III, Opera Spuria) is Native and holds two pseudo-Cyprianic works in a bishop's pastoral voice whose date and place are not fixed. *De singularitate clericorum* is a bishop's letter to his clergy (Hartel III, lines 9562-9570); Koch (row 233, `koch_cyprianische-untersuchungen-deu_1926.txt`, line 22909) writes that it was probably composed toward the end of the third century, and reports Achelis's pre-Nicene date and the ascription to Macrobius by Morin and Harnack (lines 20766-20790). *De aleatoribus* is a bishop's homily (Hartel III, line 4982); Monceaux (row 207, tome 2, lines 6655 and 6671) gives it to an African bishop of Cyprian's school, calls it a true homily, and fixes no date. The earlier ground, "no vendored file places them inside the interval", was false for the first work and open for the second.

**Changed 2026-09-30.** Doc_02 section 7, Doc_05 section 0.3 and line 293 and its sources table, Doc_08's structural-fact paragraph and the Layer 1 paragraph of Force 3B-2, the core, force and limit records and the generators that emit them (`scripts/wb_lpc_s21.py`, `wb_lpc_s25.py`, `wb_lpc_s28.py`) now state the exception. Doc_02 section 7's set-aside sentence for rows 6 and 194 is replaced by what Hartel, Koch and Monceaux report, and it now names row 39 (the standing reference to Hartel's whole edition), the row-229 tractatus and the rowless Knopf acts nos. 19-22 and 29. Eleven claims took new ids and are registered in `lpc_Claims_Register.md`; eight are UNVERIFIED, pending re-verification by an independent reviewer.

**Open.** The boundary status of *De singularitate clericorum* and *De aleatoribus* is unassessed. Whether either falls inside the interval, and whether either belongs in or outside the Native rows, is a Registry boundary decision for the build thread and the project lead. Until it is made, neither work is assessed and neither is drawn on.

**Smaller observations, handled 2026-09-30.** (1) Doc_02 section 7 did not mention the row-229 tractatus or the rowless Knopf acts; it does now. (2) The force record's description called the Confessions V.8 oratory "not yet assessed" while Doc_02 section 7 treats the passage as seen through Augustine's eyes; the description and the core record's note now say the passage does not fill the silence and that only a link to Cyprian that does not run through texts is unassessed. (3) Doc_02 said Hartel argues that *De duplici martyrio* is later than Cyprian; Hartel notes the mentions of Diocletian and Maximin and of the Turks and says he does not know whether Gravius and others were right to suspect that Erasmus produced it (lines 39121-39125 of the row 194 file). The text now says that. (4) Row 39 also covers the spuria, through row 194; Doc_02 now says so. `lpc_World_Profile.md` line 428 and `lpc_Gapped_Formation_Precedent.md` speak of a congregation's voice or were received from the project lead, and were left as they stand.

**Not verified, left out of the text.** The date of the Cirta hearing (303 or 320) and the wording of *Confessions* III.12 could not be verified as the project lead stated them. The text keeps the dates and quotations it already carried, each with its source line, and adds nothing on either point.

**Awaiting a decision.** Thirteen REWRITE or ROUTE commentary lines in `Build/reference/text-renderings/` (the verbatim Word text of reference documents) are flagged by the commentary checker; they await a decision on whether that folder is excluded from the tool. Separately, the Step 0 passage at line 163 describes the CO-022 rule as having three limbs according to the installed skill, while the repository copy of the build-cycle skill has four; which one governs is not settled.

### OG-51. The silence claims, fourth pass: the exception is now stated as a class, 2026-09-30.

The independent check of 2026-09-30 on the row-194 exception (`Review-Artifacts/ClaimsException194_Verification_2026-09-30.md`) found two P1 defects. F1: "two short pseudo-Cyprianic works" undercounts. Row 194 and row 6 also hold *De spectaculis* and *De bono pudicitiae*, written as an absent bishop's letters to his people, which Monceaux gives to a cleric of Cyprian's school soon after 258 and the Registry's row 6 note gives, in part, to Novatian; a short letter headed to the people of Carthage (Hartel III, line 15508) is undated. F2: the date of Pontius's *Life* was stated as settled ("written at and just after" the martyrdom). Harnack (row 205) gives 259 as the prevailing view of 1913, while Koch (row 233) follows Reitzenstein and Martin and puts its author at the end of the third century at the earliest. This is the fourth pass on the silence claim (after the Optatus correction, the scope restatement and the row-194 exception of the same day), made on the project lead's instruction as a change order, not as a new review round.

**Decision.** The exception is stated as a class and not as a list, so that it cannot be undercounted a fourth time: "with open exceptions among the pseudo-Cyprianic works of rows 6 and 194, whose date and place the vendored files do not fix; none is assessed, and none is drawn on for a claim." The works are named in one place only, Doc_02 section 7's explanatory paragraph, with what Hartel, Koch, Monceaux and the row 6 note say, each re-read at its line. Enumeration ends here. A work not listed in that paragraph falls under the class if it is pseudo-Cyprianic in rows 6 or 194 and the vendored files do not fix its date and place.

**Changed 2026-09-30.** The class wording replaces the enumerated wording in Doc_02 section 7, Doc_05 section 0.3 and line 293 and its sources table, Doc_08 (the structural-fact paragraph and the Layer 1 paragraph of Force 3B-2), the core, force and limit records, and the generators `wb_lpc_s21.py`, `wb_lpc_s25.py` and `wb_lpc_s28.py`. Where a record speaks in the plain voice, it says only: "Some short works handed down under Cyprian's name may come from those years." The date of Pontius's *Life* is tagged Contested in Doc_02 section 8, and every place that called it written "at and just after" the martyrdom now says that the *Acta Cypriani* and the martyr acts of rows 231 and 232 belong to Cyprian's phase and that the *Life*, dated to 259 or much later, is a life of him and does not fill the silence (Docs 02, 05, 08 and 09, the three records, the generators). Doc_02 section 7 also carries the smaller corrections: Koch rejects the Macrobius ascription of *De singularitate clericorum* and thinks its author was not a schismatic bishop, and the Donatist-origin view is Achelis's; Monceaux sets *De aleatoribus* in third-century Africa and names no year; Hartel's "nescio annon iure" leans toward suspecting that Erasmus produced *De duplici martyrio*; it is a different manuscript, the Orléans codex, and not Morin, that gives the Holy Innocents sermon to Optatus, and Morin judges this likely. A pointer to Doc_02 section 7 was added to Doc_01's statement of what is missing, Doc_09's "what the gap lacks" sentence and the World Profile's temporal-scope paragraph. `Source_Registry.md` rows 6, 194, 205, 207 and 233 now say in their Licensed-For cells that they are cited at Doc_02 section 7 as disclosure only (row 194 and row 6 as named exceptions to the silence claim, rows 205, 207 and 233 for what they report), not drawn on; their Confidence letters are untouched. Nine claims took new ids in `lpc_Claims_Register.md` (one new sentence among them) and are UNVERIFIED, check "pending re-verification"; three Doc_09 claims took new ids in `Doc09_Claims_Register.md` (one of them was VERIFIED on 2026-09-16 before the pointer was added to its sentence, and is now UNVERIFIED).

**Open.**
- The boundary decision on the pseudo-Cyprianic works of rows 6 and 194 (whether any falls inside the interval, and whether any belongs in the Native rows) is still open, routed as in the row-194 exception entry of the same date to the build thread and the project lead. Until it is made, none is assessed and none is drawn on.
- If the decision places any such work inside the interval, the spoken copies change: `lpc_Representative_Permanent_Prompt_Datus.txt` line 21, `lpc_World_Capsule_Core.md` line 79 and the limit record's spoken statement. They were deliberately given no exception language, because it would be scholarly meta-commentary in the world's own voice.
- `lpc_Gapped_Formation_Precedent.md` line 21 ("no surviving voice in the Registry, native to this world's own boundary, that continues Cyprian's") carries an unqualified sentence. It was received from the project lead and was not edited; the project lead decides whether it is qualified.
- General silence statements outside the claim sentences are unqualified and hold on the reading "a congregation's own voice": Doc_05 line 305; Doc_07 lines 176 and 232; Doc_08 line 359; Doc_09 line 23 (first sentences) and Story Index line 93; World Profile lines 428 and 650 to 654; Capsule Core line 79; Permanent Prompt line 21; Representative Phases 1, 2, 3, 4, 6 and 7; the core record's horizon and thinness passages. They are revisited when the boundary decision is made.
- Rows 207 and 233 are cited at Doc_02 section 7 for disclosure. The Registry's priority-review rule for rows of Confidence C still applies to them, and to row 205 for the date of the *Life*.
- Whether *De spectaculis* and *De bono pudicitiae* count as a bishop's voice at all, given the Novatian ascription that row 6 records and Koch warns against treating as settled, is a reading that belongs with the boundary decision.
- `scripts/check_claims.py` (the Doc_09 register's own checker) already reported unregistered Doc_09 and story-chunk claims before this pass; this pass did not add to them. They remain for the Doc_09 register conversion.


### OG-52. The silence claims, class-level recheck: open disclosures, 2026-09-30.

The independent recheck of 2026-09-30 (`Review-Artifacts/ClaimsClassException_Recheck_2026-09-30.md`) found no false claim among the twelve it checked; ten stand as readings (JUDGEMENT, Widely Accepted) and two as verified. It found one P1 wording defect beside the claims, now fixed: the core record and the force record (and their generators `wb_lpc_s21.py`, `wb_lpc_s25.py`) stated Pontius's authorship as settled; they now read "the life that bears the name of his deacon Pontius". Three citation fixes were applied in Doc_02 section 7 (Hartel lines 702–713, Monceaux lines 5105–5112, and Koch's "novatianischen" given as his own quotation marks).

Open, not yet applied, each a disclosure and not a correction of a claim:

- Gebhardt's volume (the row 232 file) also prints the Gesta apud Zenophilum and the Acta purgationis Felicis (nos. XX–XXI), with no row. Doc_02 section 7 and row 232 do not say so, as row 231 does for its acts.
- Doc_02 section 7 could name Mensurius's letter to Secundus, known only through Augustine's Breviculus (row 268), as the nearest case under the documents of the Donatist dispute.
- `lpc_Gapped_Formation_Precedent.md` line 21 still says "written at and just after his martyrdom". It was received from the project lead; this entry routes the dating to him together with the silence sentence.
- Augustine preaches Crispina of Theveste (martyred 304) in two feast-day sermons in row 20 (the Expositions on Psalms 121 and 138). No lpc file mentions her. Doc_09's sentence that this world tells itself no stories at all is true only for stories that begin inside 258–391 and are told in our own voice; a disclosure is proposed: Augustine preaches one martyr of those years on her feast, as he preaches Perpetua (named in Doc_02 section 6, the Perpetua sermons); it is a Phase Two telling and is not built here.
- The spoken copies (Permanent Prompt, Capsule Core, the limit statement) and the plain "our own deacon Pontius" in `lpc.story.election-of-cyprian` stand in the emic voice until the boundary decision on rows 6 and 194 is made (see the entry on the fourth pass of the silence claims, 2026-09-30).

### OG-53. Library pre-Step-3 readiness sweep for `lpc`, 2026-09-29 and 2026-09-30: what it did, what the project lead decided, and what stays open in files the Library does not own.

**Done (Library thread).**
- The V7.4 field-bibliography sweep OG-20 item one asked for was run: bibliographies opened, the OpenGreekAndLatin `csel-dev` repository probed by path, works enumerated for Cyprian, Augustine's pastoral and congregational works, the Donatist sources and the other North African sources. Method, result, limits and the sandbox blocks are in `Source_Registry.md`'s saturation section. OG-20 item one is discharged, with its limits stated there.
- 42 files were vendored for `lpc` (25 from the sweep, 17 `csel-dev` TEI files: Cyprian's 15 works and Optatus), the Petschenig file's description was corrected (it holds CSEL 51, 52 and 53), and the CSEL 58 file was retired to `Archive/Retired-Library-Texts/` because the only public scan located on the Internet Archive is a 1961 Johnson Reprint facsimile, excluded on the ground row 197 already states. The Registry has 272 rows.
- The directed corrections from `Review-Artifacts/Doc02_Returned_Review_Independent_Check_2026-09-29.md` were applied and rechecked (`Doc02_Directed_Corrections_Recheck_2026-09-29.md`). The 30-round cap on Doc_02 does not apply to them, by the project lead's ruling of 2026-09-29.

**Decided by the project lead (2026-09-29), each applied in the Registry.** Row 44 at Confidence A (its Licensed-For is confined to CTh XVI.5.21). Row 33 at Confidence B, which discharges OG-20 item two. No row carries a split letter: rows 11 and 14 are narrowed to their verified loci and the whole-work claims sit in new rows 243 and 244 at B. Rows 227, 228 and 230 at B, the rule text unchanged (rows 191 and 193 keep C for OCR, which the rule text does not name). Rows 231 and 232 carry the Cyprianic acts only; the Scillitan and Perpetua acts are rows 245 to 248. Seven authentic Petschenig works are on the `lpc` and Donatism shelves. Every other letter stays.

**Open, to be confirmed.** Row 229 (Morin) holds 33 Native sermons and nine unassessed tractatus; it was narrowed to the 33 and not split, because unassessed acts get no row. The project lead has not been asked whether that reading is right.

**Open, in files the Library does not edit** (owners: the `lpc` build thread and whoever owns `records/lpc`): `Doc_02_Source_Ecology.md` line 120 says no Registry row dates from the 258 to 391 gap, which rows 27, 64 and 264 to 265 (Optatus, 366 to 384) contradict, so how Doc_01's "honest silence" binding coexists with the Optatus rows needs a decision. `Doc_04_Gravity_Discovery.md` line 7 quotes row 65's old "not yet drawn on by it". `Source_Acquisition_Manifest.md` lines 33, 35 to 37, 39, 41, 73, 75 and 81 (branch-relative wording, G4 CSEL 58 reason). `Build/worlds/lpc/scripts/wb_lpc_s21.py` lines 41, 115, 205, 669, 1568, 1669, 1684, 2108 to 2109, 2134, 4367, 4396 to 4399, 4414 to 4418 and 4526 (the generator repeats the old row wording, so regenerating brings it back). Records: `lpc.source.lancel-actes-de-la-conference-de-carthage-411.md` (act 158 counted as a speech, "not yet drawn on", `rights_status: public-domain` for an in-copyright edition), `lpc.limit.411-gesta-unread.md` (`license: public-domain`), `lpc.core.latin-pastoral-congregational-christianity.md` (fourteen acts, "silver fines", `tertullian-s-voice`), `lpc.source.codex-theodosianus-mommsen-meyer.md` (says the content is unread and calls XVI.5.52 a silver schedule; row 44 is now A), `lpc.source.augustine-correction-of-the-donatists.md` (silver wording), `lpc.source.augustine-donatist-correspondence.md` (Letter LIII as Augustine's own, "not yet promoted"), `lpc.witness.apostolic-succession-of-bishops.md` (succession list attributed to Augustine alone), `lpc.source.augustine-answer-to-petilian.md` (locus "Book II SS51"), `lpc.source.burns-jensen-christianity-in-roman-africa.md` (row 33 is now B), `lpc.source.augustine-general-correspondence.md` (row 11 narrowed), `lpc.source.possidius-vita-augustini-standing-reference.md` (says not vendored), `lpc.source.goldbacher-augustine-epistulae-standing-reference.md` (CSEL 58 statement). Also `Representative/lpc_Rep_Phase3_Voice_Construction.md` lines 80 and 92 name the removed `tertullian-s-voice`.

**Open, Library thread.** The Gesta cum Emerito locus in the Petschenig staging file and header (72784) is the text's opening; the work's own heading is at line 72037. Duchesne's scan in the download queue is a reprint whose rights are unsettled. Monceaux tomes IV to VI are vendored (Donatism shelf) and have no Registry rows.


**Closed, 2026-09-30.** Row 229 stays unsplit, ruled by the project lead (`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, 2026-09-30). Still open for the lpc thread: Doc_02 §7 line 120 (the 258–391 silence claim) against Optatus rows 27, 64 and 264.

### OG-54. Doc_02 section 7, the 258 to 391 silence claim, decided against the Optatus rows, 2026-09-30.

The claim said no Registry row dates from within the 133-year gap between Cyprian's death and Augustine's ordination. Rows 27, 64 and 264 (Optatus of Milevis, *Against the Donatists*, active 366 to 385 by the vendored file header) do, and row 27 is Native for this world. Row 265 is Excluded.

**Alternatives.** (A) Change the rows: mark Optatus out of boundary. Rejected, because the Library's rows record a real boundary decision (a provisional Latin home, double-placed on the Donatism shelf) that this thread does not own. (B) Leave the claim and add a note elsewhere. Rejected, because the claim would stay false as written. (C) Correct the claim to what the rows show. Chosen.

**Decision.** Section 7 now says no source supplies a pastoral or congregational voice from within the gap, names Optatus as the one Registry text that dates from inside it, and states that it is Donatism's territory, is held provisionally, and is drawn on for no claim. Doc_01's binding is about a surviving voice continuous with Cyprian's, so it stands. The Registry rows are unchanged.

**Check.** Included in the targeted Opus recheck of the Library's Round 33 fix pass. A separate agent sweeps every other copy of the claim (Doc_01, Doc_05, the world core record).

### OG-55. Registry rows renumbered after the merge with main, 2026-09-30.

**Decision (the project lead, 2026-09-30).** The merge of `origin/main` into this branch found both sides numbering new Registry rows from 214. Main keeps rows 214–252 as it wrote them: text, numbers, Confidence letters and statuses. This branch's rows 214–326 were reconciled to that. Where main's row already registers the same edition, this branch's row was dropped as a row, and only facts that are true, that main lacked and that matter were carried into main's row. Every other row was renumbered from 253 upward, in its original order, with every field kept. The Registry's no-renumbering rule gives way to this decision for these rows only. The Registry now has 355 rows, numbered 1–355 without gap or duplicate.

**Old number to new number.** Rows 1–213 are unchanged. Earlier entries of this ledger and the review files in `Review-Artifacts/` written before 2026-09-30 keep the old numbers and are read through this table.

| Old row (this branch) | New row |
|---|---|
| 214–224 | 253–263 |
| 225 (Zycha, CSEL 41 scan) | dropped; main's row 215 |
| 226 (Krüger, *De catechizandis rudibus*) | dropped; main's row 220 |
| 227–231 | 264–268 |
| 232 (Gebhardt, Cyprianic acts) | dropped; main's row 222 |
| 233 (Koch, *Cyprianische Untersuchungen*) | dropped; main's row 225 |
| 234–237 | 269–272 |
| 238 (Benson) | dropped; main's row 226 |
| 239 (Mesnage) | dropped; main's row 238 |
| 240 | 273 |
| 241 (Audollent) | dropped; main's row 239 |
| 242 (von Soden, the rebaptism article) | dropped; main's row 224 |
| 243–246 | 274–277 |
| 247, 248 (Gebhardt, Scillitan and Perpetua acts) | dropped; main's row 222 |
| 249–326 | 278–355 |

**What was carried into main's rows.** Row 215: the print-check licence for the Leipzig TEI texts of rows 257–263, and the second CSEL 41 scan (`augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41.txt`). Row 220: the licence wording (the German matter not licensed) and the title-page and opening lines, which are the same file. Row 222: the Scillitan act as a Named Comparandum on the ground of row 28 and the Perpetua act as Out-of-Boundary on the ground of row 204, with the Comparandum Note; the second-printing licence beside row 268; the act headings and openings re-located in main's scan; the second scan (`gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt`). Row 224: the consultation scope, the link to row 211 and the second copy of the slice. Row 225: the consultation scope, the Doc_02 §7 citation and the contents lines, which are the same file. Row 226: the consultation scope and checks re-located in main's scan. Row 238: the consultation scope, the Toulotte link (row 273), checks re-located in main's scan and the second scan. Row 239: the consultation scope, the bibliography line in main's scan and the second copy. Morin 1917 (old row 229, now row 266) is a different edition from main's Morin 1930 (row 219), so it stays. The Petschenig work rows (253–256, 295–302), the Knopf acts (276–277) and the PL 8 excerpt of 340–348 (old row 298, now row 327) register works or files that main's rows do not, so they stay.

**The Benson correction.** Old row 238 described the Toronto scan (`cyprianhislifehi00bensuoft`). The file in the Library is main's University of California scan (`hislifehicyprian00bensrich`), so main's row 226 stands. Only what is true of that scan was carried, and its lines were checked in the file: the title page at line 25, the author at line 34, the imprint at lines 40–43, and contents chapter X at line 416.

**The corpus-map correction.** Old rows 266–272 (now 295–301) said the corpus map places those works in `lpc` and `donatism`. Main's Petschenig staging file places four works of the file in `lpc` (rows 253–256) and says the file's other works have no assignment. The rows now say so. Row 300 now gives the file's contents-map line for the *Gesta cum Emerito* as 72034, and row 253 says the file header gives the Pars III title page only.

**Conflicts left to the project lead, not decided here.**
- Confidence. This branch had C where main has B for Koch's *Cyprianische Untersuchungen* (row 225), Benson (row 226), Mesnage (row 238), Audollent (row 239) and von Soden's rebaptism article (row 224). Main's B stands. `Doc_02_Source_Ecology.md` §3 now states both letters for its fifteen secondary works.
- Corpus map against main's rows. Rows 215, 219, 220 and 222 say "Not assigned to this world in the corpus map". The corpus map assigns their files to `lpc` (row 222's three acts `provisional`, with a note citing row 222). Main's text was kept.
- A stale corpus-map bucket. The merged tree holds main's generated `latin-pastoral-congregational-christianity.yaml` (147 entries) beside this branch's staging files. The staging files hold 59 `lpc` assignments that the bucket lacks. A re-merge by `cic/engine/corpus_map_merge.py` would give 206 raw entries, 161 `tradition` and 159 distinct titles. Many kept rows (among them 257–273, 276 and 278–292) cite bucket entries that now exist only in staging. They were left as written, pending a Library re-merge. The census at Doc_02 §1 gives the merged tree's present figures.
- Morin. Row 266 says Morin's 1917 edition is the only Latin witness of its sermons in the corpus. Main's Morin 1930 (row 219) cites the Guelferbytan collection throughout. Whether it also prints those sermons was not checked.
- Claim `004afcf9`. Its check searched the 326 rows this branch held, not main's rows 214–252. The register's source cell now says so.

**Claims re-registered.** In `lpc_Claims_Register.md`, seven claims changed only in their row numbers, and their old checks still hold, so each keeps its status with a note in its check cell: `07009ff9` (was `e4f0349e`), `cb404015` (was `6e285cef`), `98da5674` (was `065954da`), `416e1e7e` (was `3669587c`), `80391933` (was `361181c3`), `39404aae` (was `fea87e6e`) and `1652508f` (was `fb07c9ad`). One claim was restated and is UNVERIFIED, pending re-verification: `47bbbca6` (was `3969e707`), the world core's count of uncompiled rows. In `Doc09_Claims_Register.md`, `f739b561` (was `2572f600`) and `69e69995` (was `a3aeea2f`) changed only in their row numbers and keep their status.

**Not edited.** `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (Library-owned) cites old rows 225, 227–232 and 245–248; read it through the table above.


### OG-56. Handoff gate after the merge with main, 2026-09-30: eleven checks pass; the corpus-map file is the Library's to fix.

After the merge with main and the renumbering in the entry on the Registry rows renumbered after the merge with main (2026-09-30), `handoff lpc` passes eleven of twelve checks. Check 6 fails: the generated `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` on main carries no `row_id` on any of its 147 rows, and the Library issues every `row_id`. The staging files hold 59 lpc assignments the generated file lacks, so a Library re-merge would also change the atlas counts that Doc_02 section 1 states (it uses the merged tree's current figures). Main's Registry rows 215, 219, 220 and 222 say "Not assigned to this world in the corpus map", which the corpus map contradicts; the Library owns those rows. The recorded review-file counts in the re-baseline declaration were brought to the disk (Doc_01 12, Doc_02 35, Doc_04 12, Doc_08 9) after the gate began counting every review file; the added files are the independent checks the declaration names and the Library's rechecks, and the project lead is asked to confirm that reading.

### OG-57. B-1b relative recall and PRESS run for `lpc`, 2026-09-30: recall 10/10, four items routed to the pre-freeze re-sweep.

Build Process V2.0 step B-1b, run once against the Registry at rows 1–355. The record is `records/lpc/search_record/lpc.search.relative-recall-and-press.md`.

**Method.** Ten works were listed from field knowledge before the Registry, Doc_02, the corpus map or `cic/texts` were opened. Only `records/worlds/lpc.yaml` and Doc_01 sections 1 and 2 were read first. Each work was then checked against its Registry row and vendored file. The PRESS question was asked verbatim as CF V7.4 words it: "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly." It was answered from field knowledge first, then checked the same way.

**Recall: 10/10, no misses.** Cyprian's Epistulae, De lapsis, De unitate and the Sententiae of 256; Pontius's Vita Cypriani; Augustine's Confessiones, De catechizandis rudibus, Sermones ad populum and Epistulae; Possidius's Vita Augustini. Each is held with a vendored text; the rows and files are in the record. The ten are the core of the field, so the score shows the core is held and says little about the margin. Two hits named modern finds: the Divjak letters are row 49 and the Mainz sermons row 50, both in copyright and consultation-only.

**PRESS, first answer (before the check).** The African conciliar canons of 393–419 with the Registri ecclesiae Carthaginensis excerpta; the Gesta collationis Carthaginiensis of 411; the Acta Proconsularia Cypriani. All three are held (rows 26, 202 and 228; rows 65, 229 and 297; rows 41, 194, 222 and 268). The Registri excerpta as a separate collection stay open in `lpc.search.registri-ecclesiae-carthaginensis-excerpta` (title sweep, second pass, 2026-09-30).

**PRESS, answer after the check: three sources the Registry does not hold.**
- De miraculis sancti Stephani protomartyris, the miracle book written at Uzalis for its bishop Evodius, c. 420–425; public domain in Migne PL 41. `lpc.search.de-miraculis-sancti-stephani-uzalis`.
- The Acts of Maximilian (Theveste, 295), Felix of Thibiuca (303) and Crispina (Theveste, 304), vendored in Knopf–Krüger 1929 (`cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt`, lines 6454, 6753 and 7928). Row 268 leaves them unassessed. This touches the Crispina disclosure proposed in the silence-claims recheck (2026-09-30). `lpc.search.knopf-african-acts-maximilian-felix-crispina`.
- Diehl, Inscriptiones Latinae Christianae Veteres (1925–1931), already listed as not reached in the saturation record. `lpc.search.diehl-ilcv`.

**Routed to the pre-freeze re-sweep (Open).** The three PRESS namings above, and one part of a recall hit: the Erfurt sermons of Augustine, in copyright, to be rowed as consultation-only beside row 50 (`lpc.search.augustine-erfurt-sermons`). For each, the re-sweep rows the work or declares a non-row with a reason. No Registry row was added in this run.

**Open, for the owners of those files.** `Source_Registry.md`'s saturation section, `Doc_02_Source_Ecology.md` §9 and `lpc.search.latin-pastoral-source-discovery-saturation` still say the recall test and PRESS question have not run since the fourteenth review pass. This run makes that out of date. They were not edited here.
