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
  137 of the 142 remaining UNVERIFIED** (Decision Log's own disposition entry, item 4;
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
  lead's own instruction; the portfolio-level items from Doc_07 §8 item 4; the World Profile
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
  Merged to `main` at `708aa13` (PR #447).
- **Phase Three — Voice Construction** (2026-09-23): **Approved to proceed.**
  `Review-Artifacts/Phase3_VoiceConstruction_Round1_Review.md`, 1H/2M/0L/2C. The HIGH finding
  misattributed the Passion of Perpetua and Felicitas's exclusion to a date-boundary reason
  when Registry row 204 in fact excludes it by prior cross-world ruling (assigned to
  `tertullian-s-voice`). Merged at `6d2379e4` (PR #451).
- **Phase Four — Engagement Architecture** (2026-09-23): **Approved to proceed**, no HIGH
  findings. `Review-Artifacts/Phase4_EngagementArchitecture_Round1_Review.md`, 0H/2M. Built
  its own distinctive Dynamic Encounter mechanism (**Answerability → the Argued Case → the
  Road Back**), deliberately distinct from Donatism's own Threshold–Narration–Jeopardy,
  confirmed by direct comparison. One MEDIUM finding was a second citation-locus error (Doc_05
  §5.4 vs. the correct §5.1). Merged at `3f2b7454` (PR #454).
- **Representative Artifact Construction — Permanent Prompt + World Capsule Core**
  (2026-09-23): **Approved to proceed.** `Review-Artifacts/RepresentativeArtifacts_Round1_Review.md`,
  1H/5M/2C, plus one MEDIUM completed and one small technical correction (a genuine internal
  contradiction — Hippo Regius called both "inland" and "coastal" in the same clause) found
  and disclosed at the targeted recheck. The HIGH finding was a mandatory-boilerplate edit
  (world-specific imagery substituted into the template's own fixed backstop-mechanism
  sentence), restored verbatim. Merged at `4e84d208` (PR #456).
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
  Safety grounds** at this disposition. Merged at `119e927f` (PR #460).
- **Phase Six — Facilitator Coordination** (2026-09-24): **Approved to proceed.**
  `Review-Artifacts/Phase6_FacilitatorCoordination_Round1_Review.md`, 0H/3M. **Central,
  independently-verified finding:** `engine/m4/turn.py`'s portfolio-level
  "Facilitator-only" routing decision (the same one `don`'s own build commissioned) is
  genuinely world-independent, unconditional code (`voice_event = None` on the
  `ACUTE_DISTRESS` branch, no per-world gate) — so the architectural fix Probe 11 called for
  is already live and automatically covers `lpc`, closing that design requirement with no
  world-specific engine change needed. Merged at `d93f2adc` (PR #485); a small follow-up
  citation-locus fix merged at `cead10a1` (PR #486).
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
  artifacts. Merged at `ef3ffe09` (PR #488).
- **World Context Layer, chunks 001–005** (2026-09-24): **Approved to proceed.**
  `Review-Artifacts/ContextLayer_Round1_Review.md`, 2H/5M/2C, concentrated mostly in
  `lpcctx003`. Drafted specifically to route Phase Seven's own §6.3 depth into the
  token-constrained context layer rather than reopen the already-disposed Permanent Prompt
  and Capsule Core — **this closes the substance of §6.3.** Merged at `7da29b42` (PR #491).
- **Voice Configuration for Datus** (2026-09-24, `lpc_Voice_Configuration_Datus.md`):
  **Approved to proceed.** `Review-Artifacts/VoiceConfiguration_Round1_Review.md`, 1H/2M/1C.
  The HIGH finding presented disclaimed editorial apparatus (*plebs*, explicitly not a
  headword per `lpclex010`) as genuine runtime vocabulary; removed. **Model selection, live
  audition, and pronunciation-dictionary testing are all explicitly, honestly left
  PENDING** — no live ElevenLabs platform access exists in this build thread's own
  environment, following the same disclosure pattern the Cappadocian/Eumathios precedent
  set. Merged at `b7dc7d0c` (PR #492).

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
Open Item 6 says so in terms." Whether row 65 has since been annotated with that explanation
was not checked directly in this review.

### OG-5. A recurring citation-locus error across the Representative-construction phases — the same failure class `don`'s own Doc_08 is tracked for, distributed across this world's Representative phases instead of concentrated in one document.

Independently caught once at each of five separate Round 1 reviews: Phase Two (Doc_07 §2D's
three doctrinal bodies misdescribed as one — itself a *repeat* of a defect Phase One's own
Round 1 had already caught and fixed once in a sibling document); Phase Three (Perpetua's
Passion exclusion reason misattributed); Phase Four (Doc_05 §5.4 cited for content that is
actually at §5.1); Phase Six (a follow-up citation-locus fix, PR #486); Phase Seven (one
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
**`Build/Ministry/Operations/Standing/CiC_GoLive_Pipeline_Status.md`** (item 4, checked directly in
this review) confirms **lpc PR #230** ("gapped-formation-worlds-precedent") is still **open,
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

### OG-14. PR #557's canon-closure pass (Part 8, `wb_lpc_s2z_canon_closure.py`) — an independent Opus fidelity review found the coverage method itself was unsound, not just individual records; the PR is held unmerged pending rework.

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

**Standing state:** PR #557 is open, CI green, `mergeable_state: clean`, but **held
unmerged** on the coordinator thread's own explicit instruction — Mark merges this PR
himself after the rework, and any revised quotes/absence claims get independently
re-checked again before that (self-certification does not count, per this project's own
standing rule). Not resolved by this entry — logged per CLAUDE.md's own rule that a review
outcome never lives only in a conversation thread. The rework itself (author substantive
records from the loci above where they hold, narrow claims that are only partly wrong,
fix the two mis-cited/mis-contextualized quotes, retag F4-T, strip the commentary, and fix
the swallowed exception) is a separate, not-yet-started piece of work.

### OG-15. OG-14's rework applied on branch `lpc-record-compilation-part7-witness-limit-ambient` (PR #557) — every finding checked against the vendored corpus directly, not self-certified; independent re-confirmation still required before merge.

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
an independent fidelity review of this rework is still required before Mark merges PR #557,
exactly as OG-14 already states. This entry records what changed and why, not that it has
been approved.

---

### OG-16. Round-2 rework of PR #557, after an independent review found OG-15's own round-1 pass had repeated its root cause — absences checked against lpc's own already-tagged records, not against the full set of texts `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` assigns to this world.

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
/ `F3-P`, matching PR #557's own round-1 retagging of the term/contested_claim records this
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
still carried the pre-review text for four `honest_limit` slugs this rework and PR #557's
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

Full findings, search method, and before/after are in PR #557's own body.

### OG-17. Round-3 (final) rework of PR #557, Mark's own personally-authorized targeted round, bar stated as "scholarly rigor that would impress a professor of church history, not perfection."

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
   inline review-round references forbids ("corrected #557 round 3," in `lpc.source.
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
`doc-ref`/`section-ref` content in `force/` records belonging to PR #562's own scope, not
introduced this round, and left untouched per this round's own "touch nothing else"
instruction). Every quote and every new locus re-verified directly against the vendored
`cic/texts/` XML, including the four apostolic-succession sources named in the brief and the
Confessions III.vii.12 and IX.vi.14 loci. Branch merged current `main`.

**Not in scope this round, disclosed rather than silently skipped.** The OG-numbering
collision this build's three parallel unmerged branches (PR #557, #562, #563) each carry —
this branch's own OG-14/15/16/17 numbers a different entry than PR #562's own OG-14 — is
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

**The `rights_status` fleet-wide internal-narration defect (PR #321, `e5a50654`) — does not
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
`Datus_Portrait_Prompt.md` Part Four (PR #514) via Gemini, external to this thread's own
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
  `origin`; this review could not independently confirm a specific PR number for it — "PR #353"
  appears once elsewhere in the log, in an unrelated 2026-09-23 entry's parenthetical listing
  several PR numbers together, and is not itself confirmation) — portrait merged into place;
  registration explicitly **not** done, routed back to the project lead.
- **2026-09-23 to 2026-09-24** — RCF V3.2 Phases One through Seven, Representative Artifact
  Construction, World Context Layer, and Voice Configuration each drafted, independently
  reviewed, and self-disposed by the build thread per CO-022 (no escalation category
  triggered at any of these steps).

### OG-18. Re-voiced the `name`/`description`/`manifestations` fields on all 25 gravity/force records and the four `world_core` spoken fields (`horizon`, `formation_logic`, `thinness`, `cautions`) — build vocabulary stripped, every fact and disclosed uncertainty preserved; several residual items surface as a result and are logged here rather than fixed in the same pass. Renumbered from this branch's own original OG-14 to OG-18 (PR #562 round 3) to avoid colliding with PR #557's own OG-14/15/16/17, since the two branches numbered independently off the same base — per the managing thread's own instruction, using the next free number after #557's highest.

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
still-unmerged PR #557 branch, not on `main`, so this branch does not carry it and canon-coverage
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
- **`cautions` item 11 (the note that the record this world rests on was itself under
  independent review at the time of compilation) is restored**, as item 11, with the shame/
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
  this world says yet draws on them"; `cautions` item 7's "Nothing this world says rests on
  which version came first" (literally incoherent, since De Unitate *is* something this world
  says); `cautions` item 9's "this world still dates the Conference"; `cautions` item 6's
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

**A third independent review (this round, PR #562 round 3) found further residue from the
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
- `world_core.cautions` item 6's "A firm classification looks reachable from our own
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
- **Numbering collisions.** OG-14 to OG-17 (PR #557) and the entry renumbered to OG-18 (PR #562) were numbered on two branches off the same base. OG-18 sits after OG-19 in file order. Noted, not renumbered; cite by subject and date.
- **OG-4** attributes "relied on for nothing" to the Doc_04 appendix, which says the opposite (Doc_04 relies on Gesta act 158). See the Doc_04 independent check of 2026-09-29.

### OG-22. Independent checks of what was left open, Phase L0, 2026-09-29: five review files, findings carried here so none lives only in a thread.

Each check is an independent Opus 5.5 re-confirmation, not a revision round. Files are in `Build/worlds/lpc/Review-Artifacts/`. Findings below are the reviewers' own; each is to be verified against source before any fix.

- **Doc_04** (`Doc04_Independent_Check_2026-09-29.md`). No open finding changes a gravity, a classification or an Interaction Matrix relation; candidate 5 is Supporting at every site. Still open: Round 11 M1, M2, M4, M6 and most LOW/COSMETIC items; Round 8 H1(d). New N1 (stale pointers to closed Open Items 6 and 8 in Doc_04, Docs 05, 07, 08 and the G5 record, needing one named change order), N2 (Lancel source record still lists act 158 as a speech), N3 (Lancel source record `rights_status: public-domain` for an in-copyright edition; the 411-Gesta limit record repeats it), N4 to N7 (LOW).
- **Doc_08** (`Doc08_Round9_Targeted_Check_2026-09-29.md`). Forces analysis and Index values correct; generator reproduces the Index byte for byte. Two HIGH: the verdict parser takes the first verdict word in a review file, and any mention of "approved to proceed" reads as approval. Doc_08's Disposition claims both fixed. Four MEDIUM, six LOW, two COSMETIC. Round 8 H2 remains open, so OG-3 is partly stale.
- **Doc_02 and `Source_Registry.md`** (`Doc02_Returned_Review_Independent_Check_2026-09-29.md`). Eight location claims from 2026-09-13 resolved. Open: 6 P1, 6 P2. Row 44's Confidence letter; act-158 fix to row 65 not applied; Doc_02 lines 93 and 97 still say CIL VIII and the Codex Theodosianus are not vendored; corpus count false (map holds 104 raw, 94 tradition, 92 titles; four CSEL 51 to 53 entries lack a row); rows 14 and 213 changed by PR #557 round 3 without review; Possidius passages out of date against Doc_01 §5.
- **Docs 03, 05, 06, 07** (`L0_Docs03-05-06-07_Carried_Open_Check_2026-09-29.md`). Correction: Doc_07 is on the seven-dimension lens spine (§2A to §2G); OG-9's Doc_07 bullet recorded a defect in the old Doc_07 template. Doc_05 is the document that does not carry the spine (Completion Standard V1.4, section F, against Construction Framework V7.4 Step 5). Other open items: Doc_07 §2F overstates an absence (Possidius Vita ch. V); Doc_07 Round 2 NEW-L2, L4, L5, C2 not applied; lexicon terms `lpclex017` and `lpclex018` and records `lpc.term.libelli` and `lpc.term.libellatici-sacrificati` deny attestation that Cyprian's Epistle LI carries; no lexicon-index generator exists though the index claims one; Doc_05 §11 items and Doc_03 tagging question undisposed; statuses out of date on the 411 Gesta.
- **Routing.** All five reach a project-lead decision on how to close (rounds against the cap, change orders, waivers). See the stop point 1 package.

### OG-23. Library pre-Step-3 readiness sweep for `lpc`, 2026-09-29 and 2026-09-30: what it did, what the project lead decided, and what stays open in files the Library does not own.

**Done (Library thread).**
- The V7.4 field-bibliography sweep OG-20 item one asked for was run: bibliographies opened, the OpenGreekAndLatin `csel-dev` repository probed by path, works enumerated for Cyprian, Augustine's pastoral and congregational works, the Donatist sources and the other North African sources. Method, result, limits and the sandbox blocks are in `Source_Registry.md`'s saturation section. OG-20 item one is discharged, with its limits stated there.
- 42 files were vendored for `lpc` (25 from the sweep, 17 `csel-dev` TEI files: Cyprian's 15 works and Optatus), the Petschenig file's description was corrected (it holds CSEL 51, 52 and 53), and the CSEL 58 file was retired to `Archive/Retired-Library-Texts/` because the only public scan located on the Internet Archive is a 1961 Johnson Reprint facsimile, excluded on the ground row 197 already states. The Registry has 272 rows.
- The directed corrections from `Review-Artifacts/Doc02_Returned_Review_Independent_Check_2026-09-29.md` were applied and rechecked (`Doc02_Directed_Corrections_Recheck_2026-09-29.md`). The 30-round cap on Doc_02 does not apply to them, by the project lead's ruling of 2026-09-29.

**Decided by the project lead (2026-09-29), each applied in the Registry.** Row 44 at Confidence A (its Licensed-For is confined to CTh XVI.5.21). Row 33 at Confidence B, which discharges OG-20 item two. No row carries a split letter: rows 11 and 14 are narrowed to their verified loci and the whole-work claims sit in new rows 243 and 244 at B. Rows 227, 228 and 230 at B, the rule text unchanged (rows 191 and 193 keep C for OCR, which the rule text does not name). Rows 231 and 232 carry the Cyprianic acts only; the Scillitan and Perpetua acts are rows 245 to 248. Seven authentic Petschenig works are on the `lpc` and Donatism shelves. Every other letter stays.

**Open, to be confirmed.** Row 229 (Morin) holds 33 Native sermons and nine unassessed tractatus; it was narrowed to the 33 and not split, because unassessed acts get no row. The project lead has not been asked whether that reading is right.

**Open, in files the Library does not edit** (owners: the `lpc` build thread and whoever owns `records/lpc`): `Doc_02_Source_Ecology.md` line 120 says no Registry row dates from the 258 to 391 gap, which rows 27, 64 and 264 to 265 (Optatus, 366 to 384) contradict, so how Doc_01's "honest silence" binding coexists with the Optatus rows needs a decision. `Doc_04_Gravity_Discovery.md` line 7 quotes row 65's old "not yet drawn on by it". `Source_Acquisition_Manifest.md` lines 33, 35 to 37, 39, 41, 73, 75 and 81 (branch-relative wording, G4 CSEL 58 reason). `Build/worlds/lpc/scripts/wb_lpc_s21.py` lines 41, 115, 205, 669, 1568, 1669, 1684, 2108 to 2109, 2134, 4367, 4396 to 4399, 4414 to 4418 and 4526 (the generator repeats the old row wording, so regenerating brings it back). Records: `lpc.source.lancel-actes-de-la-conference-de-carthage-411.md` (act 158 counted as a speech, "not yet drawn on", `rights_status: public-domain` for an in-copyright edition), `lpc.limit.411-gesta-unread.md` (`license: public-domain`), `lpc.core.latin-pastoral-congregational-christianity.md` (fourteen acts, "silver fines", `tertullian-s-voice`), `lpc.source.codex-theodosianus-mommsen-meyer.md` (says the content is unread and calls XVI.5.52 a silver schedule; row 44 is now A), `lpc.source.augustine-correction-of-the-donatists.md` (silver wording), `lpc.source.augustine-donatist-correspondence.md` (Letter LIII as Augustine's own, "not yet promoted"), `lpc.witness.apostolic-succession-of-bishops.md` (succession list attributed to Augustine alone), `lpc.source.augustine-answer-to-petilian.md` (locus "Book II SS51"), `lpc.source.burns-jensen-christianity-in-roman-africa.md` (row 33 is now B), `lpc.source.augustine-general-correspondence.md` (row 11 narrowed), `lpc.source.possidius-vita-augustini-standing-reference.md` (says not vendored), `lpc.source.goldbacher-augustine-epistulae-standing-reference.md` (CSEL 58 statement). Also `Representative/lpc_Rep_Phase3_Voice_Construction.md` lines 80 and 92 name the removed `tertullian-s-voice`.

**Open, Library thread.** The Gesta cum Emerito locus in the Petschenig staging file and header (72784) is the text's opening; the work's own heading is at line 72037. Duchesne's scan in the download queue is a reprint whose rights are unsettled. Monceaux tomes IV to VI are vendored (Donatism shelf) and have no Registry rows.


**Closed, 2026-09-30.** Row 229 stays unsplit, ruled by the project lead (`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, 2026-09-30). Still open for the lpc thread: Doc_02 §7 line 120 (the 258–391 silence claim) against Optatus rows 27, 64 and 264.

### OG-24. Doc_02 section 7, the 258 to 391 silence claim, decided against the Optatus rows, 2026-09-30.

The claim said no Registry row dates from within the 133-year gap between Cyprian's death and Augustine's ordination. Rows 27, 64 and 264 (Optatus of Milevis, *Against the Donatists*, active 366 to 385 by the vendored file header) do, and row 27 is Native for this world. Row 265 is Excluded.

**Alternatives.** (A) Change the rows: mark Optatus out of boundary. Rejected, because the Library's rows record a real boundary decision (a provisional Latin home, double-placed on the Donatism shelf) that this thread does not own. (B) Leave the claim and add a note elsewhere. Rejected, because the claim would stay false as written. (C) Correct the claim to what the rows show. Chosen.

**Decision.** Section 7 now says no source supplies a pastoral or congregational voice from within the gap, names Optatus as the one Registry text that dates from inside it, and states that it is Donatism's territory, is held provisionally, and is drawn on for no claim. Doc_01's binding is about a surviving voice continuous with Cyprian's, so it stands. The Registry rows are unchanged.

**Check.** Included in the targeted Opus recheck of the Library's Round 33 fix pass. A separate agent sweeps every other copy of the claim (Doc_01, Doc_05, the world core record).

### OG-25. Independent recheck of the Library's fix pass and the lpc correction passes, 2026-09-30: closed items, and what stays open.

File: `Review-Artifacts/Doc02_Registry_FixPass_Recheck_2026-09-30.md` (Opus 5.5, targeted recheck; 0 P0, 3 P1, 7 P2). All three Round 33 P1s are closed, and every changed claim about a source's text was verified at the vendored file (act 158 a subscription; Theodosian Code XVI.5.21 and XVI.5.52; Letter LIII a joint letter; Petilian Book II chapter 51, section 118; Possidius Vita ch. VIII).

**Open P1.**
- The corrected 258 to 391 silence claim (OG-24) is still false in seven places, because it says Optatus is "the one" Registry text dated inside the gap. Row 265 holds a document dated 317 to 337; row 26 (Native) holds Carthage canons of 345 to 348 and of 387 or 390; row 202 holds Bruns's text of the Carthage council under Gratus; row 59 is Munier's *Concilia Africae a. 345*. Places: Doc_02 line 120, Doc_05 line 27, Doc_08 lines 23 and 264, the transmission force record, `lpc.limit.the-silent-century.md`, and `wb_lpc_s25.py`. Whether conciliar canons count as a surviving voice under Doc_01 section 5 is a project-lead decision.
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

The claim has been corrected three times: the first correction (OG-24), the restatement after the Opus recheck (OG-25), and the restatement checked in `Review-Artifacts/SilenceClaim_Correction_Verification_2026-09-30.md` (0 P0 resolved: 1 P0, 5 P1, 7 P2). The verifier confirmed every source citation and found the restated list still incomplete. Under the review-cycle cap, no fourth restatement is attempted until the project lead decides.

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

**G5 rulings.** (1) The strand-singular finding is reaffirmed, and Doc_01 is not reopened: Doc_04 section 3 surfaces evidence Doc_01 had not weighed on that axis (the 256 preface, Epistles LIV, LXXI, LXXIV, LXXV, Letter LIV), and it shows disagreement inside one communion (Candidate 3's shape), not two communities; this answers Doc_01 section 8 item 10's condition. (2) Doc_04's verdict texts follow the Framework's own tests: G5 Repetition passes; Persistence passes narrowly; Explanatory passes narrowly (Letter LIV); Formation does not clearly pass; Dependency as written. G5 stays Supporting on the project lead's ruling, and Doc_04 now records that Supporting also rests on its own six-test result. G7 (grace) fails as an organizing force, not as a theme (Cyprian states it; Augustine carries it forward). Candidate 6 Repetition names the over-century gap and the 87 bishops of the 256 council (the stated number in the ANF05 editor's note and the Latin title; a count of the speaking paragraphs gives 84). (3) Letter XLIII is struck from the wording (it sits in the Donatist cluster row 11 excludes). (4) Augustine's *Psalmus contra partem Donati* is licensed at Registry row 273, narrowly.

**Open, for the Library thread (through the project lead).** A second corpus-map assignment of the *Psalmus contra partem Donati* (Petschenig CSEL 51, the file behind rows 214 to 217 and 266 to 272) to this world's shelf: the corpus map assigns it to `donatism` only. Row 273 states the request.

**Open, for the project lead.** The Gapped Formation Precedent, section 4, still says the candidate "structurally needed the gap bridged"; with G5 now attested on both sides that clause is arguably still a premise problem, and correcting it would change the precedent's argument. Not changed.

**Not applied, by design.** Row 227's Sermones CCLXXX to CCLXXXII (Perpetua) and 309 to 313 (Cyprian) stay unread; Doc_09 records them as a Tier-question candidate, and no story is built from them.
