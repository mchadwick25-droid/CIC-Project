# Open Gaps — Cappadocian Christianity (world code: cappadocian)

Running, dated ledger for the Cappadocian world build, matching the discipline of
`worlds/alx/Open_Gaps_Tracking.md`: dated entries, honest status, project-lead-anchored
where confirmation is a project-lead act. This file is new (written 2026-09-20); it does
not replace `worlds/cappadocian/CAPPADOCIAN_BUILD_LEDGER.md`, which remains the primary,
far more granular record (52 dated sections as of 2026-09-09) — this file distills that
ledger, the world's own decision artifacts, and fleet-level records that name Cappadocian
specifically, into the numbered-gap format the rest of the portfolio uses. Where a claim
below is not traceable to a specific file this session actually read, it says so rather
than asserting a round-outcome that was never found.

**One structural fact worth stating up front, because it changes what "open gaps" means
here relative to a sibling like Alexandria: Cappadocian is a live, admitted, merged-to-
`main` formation world**, not a Phase-A-only build awaiting a Representative decision.
It was built under a different, later governance track than Alexandria's — the
**Record-Native World Build Process** (V1.2/V1.3), not the Construction Framework's
self-governing Phase A/B split — whose own states run `built → admitted → open`, not
`Approved to proceed → Frozen`. As of the fleet's own 2026-09-16 status sweep
(`Ministry/Operations/Standing/CiC_GoLive_Pipeline_Status.md`), Cappadocian's row reads:
**"admitted | Live, package current | none pending | —."** Nothing below should be read
as blocking that status; these are the gaps a careful reader should still know about a
world that is, mechanically, live.

---

## Thread scope and how this world came to exist (recovery, not a fresh build)

Per `CAPPADOCIAN_BUILD_LEDGER.md` §1–§2: the world was **recovered**, not built from
scratch in this line of work. `origin/CiC-Fable-Cappadocian` — a single unattended Fable
run, forked from `CiC-Fable-Experiment`, under Construction Framework V7.3/RCF V3.1 (one
governing revision behind current at the time) — shared no git history with `main`. Its
self-contained world folder (~41 files: Doc_01–Doc_09, World Profile, Doc_10 Construction
Notes + Permanent Prompt, two Critic checkpoints, Build Record, Final Report) was
recovered by a targeted checkout, then **audited, re-reviewed, and substantially reworked**
against `main`'s current governance rather than adopted as pre-cleared. The original
build's own standing caveat, repeated in every one of its documents: *"genuine and
identifiable... none is checked"* — zero citations verified, zero live testing, built
entirely from the model's internal knowledge (`Cappadocian_Final_Report.md`, Critic
Checkpoint 1 Finding 1/19).

---

## Standing open items (numbered; carried, not resolved by this file)

### OG-1. Doc_04 Open Item 1 — Gravity 3's Primary-vs-Supporting classification. Still open; flagged for Article 31 external review.

`cappadocian_Doc_04_Gravity_Discovery.md` classifies Gravity 3 ("the contested church
under the contested empire") as **Primary with a situational annotation**, carrying as
its own standing alternative that it should be **Supporting**. An independent verification
pass (`cappadocian_Unused_Source_Verification_2026-09-09.md` §1.3, checked against the
imperial communion law CTh 16.1.3 in two Latin editions and an English discussion) found
the elevation case fails and the downgrade case is real but not decisive — the law
reassigns personnel and premises for two of the six formation instruments (baptism,
festival) without touching the instruments themselves. **Ruling, Mark, 2026-09-09**
(`CAPPADOCIAN_BUILD_LEDGER.md` §52, Ruling 4): the item **stays open**, now recorded in
Doc_04 itself as marginally re-weighted toward Supporting, not resolved — Doc_04's own
text already flags it for external (Article 31) review, and this is not a build thread's
question to close either way.

### OG-2. Doc_04 Open Item 9 — the "nothing verified" caveat was stale; narrowed, not closed.

Doc_04 §9's blanket caveat ("nothing in this build has been verified against editions or
external scholarship") had gone stale — by 2026-09-09, 62 records under
`records/cappadocian/` already carried `verification_state: verified-direct`. **Ruling,
Mark, 2026-09-09** (ledger §52, Ruling 4): narrowed in Doc_04 itself to state that most,
not none, of the build is now verified. This does not substitute for Article 31 external
scholarly review, which remains outstanding (see OG-4).

### OG-3. The circle-vs-world exposure (Critic Finding 2) — the build's own deepest named exposure, unresolved.

`Cappadocian_Final_Report.md` Part II/V: the evidence base is unusually concentrated —
three authors (Basil, Gregory of Nazianzus, Gregory of Nyssa), one family, one friendship
network, dominate nearly everything that survives. Whether "Nicene-Cappadocian/Cappadocian
Christianity formation world" overreaches an evidence base that is substantially one
household's library is named by the build's own Critic checkpoint as the sharpest open
question, explicitly routed to a Cappadocia specialist's external review, not resolvable
from inside the build. Mitigations exist (Firmilian's letter, Gangra's against-the-grain
canons, Eunomius' own surviving Apology as a fairness control, embedded Rule-questions)
but the question itself is carried open, unchanged, through every later pass.

### OG-4. Article 31 — external scholarly review. Outstanding, and (per Mark's standing ruling) non-blocking.

Article 29 (Living Tradition Status) is **CONFIRMED** for this world (G4, below). Article
31 external scholarly review has **not occurred** and is carried, per Mark's own standing
2026-07-31 ruling (cited at ledger §23), as **provisional-by-design and non-blocking
through freeze/admission** — the same standing every other live fleet world carries. It
is the accountable test for OG-1 and OG-3 above, and for the female-voice question (OG-5).

### OG-5. The female-voice question (Representative Identity Option 2) — live, not foreclosed, not built.

`cappadocian_Representative_Identity_Options.md`: a sister of the Annisa sisterhood (in
Macrina's own community) was presented as Option 2 — "the strongest evidentiary case for a
female voice anywhere in the project's current world-set," explicitly *stronger* ground
than the case already declined once for Early Latin, but resting entirely on one brother's
literary construction of that community's interior life. Mark's 2026-08-30 decision named
Option 1 (Eumathios/Chilo) without separately addressing Option 2; recorded there as "a
live, named, not-foreclosed question for a possible future separate build," not decided
and not built. Still open as of everything this session read.

### OG-6. `cappadocian.dw.reading-scripture` — a pre-existing `voice-perspective` gate false positive, disclosed, not fixed.

First measured 2026-09-04 (before any edit) and reconfirmed at every subsequent gate run
through the 2026-09-09 recompile (`CAPPADOCIAN_BUILD_LEDGER.md` §52): the one persistently
failing gate (17 of 18) is `voice-perspective` flagging the string "the world's first
days" (the created cosmos in the Hexaemeron, not the formation-world) — the gate's own
heuristic runs "~70% precision, not exact." Deliberately left unfixed by every pass that
found it, on the stated discipline that quietly editing an unrelated record to make a
report look clean is the move this project's own review discipline exists to prevent.
Owner: whoever next owns `cappadocian.dw.reading-scripture`.

### OG-7. `worlds/cappadocian/scripts/wb_cappadocian_s21.py` — a superseded generator and a disclosed live foot-hazard; ~110 of its ~116 rows never re-audited.

The B-1 record generator (`CAPPADOCIAN_BUILD_LEDGER.md` §15) is a 1,595-line script that,
if re-run, would silently regenerate several already-corrected errors it still carries in
its own source (confirmed and partially fixed for rows 31/32/39/40 at ledger §50, and for
the eleven-bishop CTh 16.1.3 string at §51/Round 3). `cappadocian_Unused_Source_Verification_2026-09-09.md`
§8 states plainly: only 5 of the Source Registry's 116 rows (31, 32, 36, 39, 40, plus 16/20
and 65 from earlier passes) have been checked against the script's own hard-coded content
across four review rounds; **the other ~110 rows have not been independently re-verified
this session and may carry their own stale claims of the same kind.** The script should be
retired or reconciled, not re-run as-is.

### OG-8. The "Basileias" naming anachronism — last known status: fixed everywhere it was checked, Doc_06 §23 itself left untouched.

Doc_02 §2's correction (the "Basileias" name is a later, post-period usage; "the new city"
is period-correct) was propagated through Doc_05, Doc_07 §2I, Doc_08, Doc_09, the
Permanent Prompt, and the `cappadocian.term.basileias` WRS record (whose `world_word` and
`false_friend` fields carry it — load-bearing, since this field feeds the live
participant-facing hover-glossary). `CAPPADOCIAN_BUILD_LEDGER.md` §11 and §17 both
explicitly name **Doc_06 §23 itself** as still carrying the uncorrected "named admiringly
after its founder" framing, flagged each time as "a future pass should close it." No later
ledger entry (through §52, 2026-09-09) records that fix being made. Status here is
therefore: **last confirmed open, 2026-08-31; not verified closed by this session.**

### OG-9. Live qualitative validation (adversarial trials, a clinician read) — not scheduled, same as the rest of the fleet.

`CAPPADOCIAN_BUILD_LEDGER.md` §32/§37: PR #73's own body named two further safety gates a
2026-08-26 fleet decision-log entry flagged as "not yet scheduled" — live adversarial
trials and a clinician read — beyond the clean M3 sealed-probe battery. Not Cappadocian-
specific; carried as the same standing every other live world holds. One live, threaded
(non-sealed-probe) conversation was read directly by Mark on 2026-09-01 (§38) and held its
disciplines throughout, but that is one session, not the structured battery OG-9 names.

### OG-10. The strict "we"-voice register question — raised by Mark, investigated, explicitly deferred.

`CAPPADOCIAN_BUILD_LEDGER.md` §39: after reading the SS38 live transcript, Mark questioned
why Chilo speaks in a strict communal "we" rather than "I am the voice of..." with history
in the third person. Checked directly against `records/alx/voice_craft/alx.voice.craft.md`:
this is a **fleet-wide rule** (Mark's own 2026-08-21 ruling, arrived at after trying an
"I"-carve-out and finding in practice it "still read as an individual... explaining
themselves, not a world speaking"), not a Cappadocian-specific choice. Three paths were
presented (an "I"-register comparison sample; reverse the ruling fleet-wide; try
Cappadocian alone as an experiment). **Mark's decision, 2026-09-01: "if it is the same
let's leave it for now and look deeper after the pilot."** Nothing changed; flagged in
`alx.voice.craft.md`'s own ruling record for a future revisit, not only here.

### OG-11. The rights_status internal-narration defect — fleet-wide, worst rate in Cappadocian (65 of 111 records), fixed 2026-09-20; not disclosed in this world's own build history before now.

**This item was not found anywhere in `worlds/cappadocian/`'s own files** — not in
`CAPPADOCIAN_BUILD_LEDGER.md` (52 sections, through 2026-09-09), not in the Source
Registry or its three review rounds, not in the Unused-Source Verification document. It
surfaced from a separate engineering thread and is recorded here so it has a home in this
world's own gap-tracking, per this project's standing rule against letting a known,
already-fixed defect go undisclosed in the world it touched.

**What happened, verified directly against the actual commit** (`e5a50654`, "Library
data integrity: strip internal build-artifact narration from rights_status," merged via
PR #321, `22f710a7`, 2026-09-20): a live conversation transcript surfaced internal
build-process notes — vendored file paths, a script name
(`cic/engine/texts_registry.py`), a build-ledger filename/section reference
(`CAPPADOCIAN_BUILD_LEDGER.md §9`) — leaking verbatim into a source record's
participant-facing `rights_status` field via `engine.m4.citation_cards`, which resolves
that field straight through into the SourceCard shown to participants. Root cause: not a
rendering bug — the field itself is legitimately participant-facing (compare alx's own
clean values, "public-domain" / "public-domain; 1907, long out of US copyright"); the
defect was in the **data** — five worlds' own source records had written this field as a
full build-narrative sentence instead of a short status.

**Cappadocian carried this defect at the worst rate of any world checked: 65 of 111
source records, 59%** (alongside don 74/76 = 97%, gallic 31/36 = 86%, rzg 15/17 = 88%,
witt 53/89 = 60%; alx/desert/hal/ijc/pahc/syr confirmed clean, 0–1 incidental match each).
Fixed by hand-mapping Cappadocian's own small set of repeated templates (shared with
don/gallic/rzg — 26 unique values across 240 records combined), stripping the ledger
reference, file path, and session-provenance narration while preserving every real
substantive rights distinction (public-domain/vendored/verified vs. not-vendored vs.
in-copyright-excluded vs. no-position-stated). Verified directly against the current repo
state: `records/cappadocian/source/*.md`'s `rights_status` fields now read as short,
clean status strings (e.g. `"public-domain; vendored, present in the shared library since
2026-08-15"`), not build narrative. Cappadocian was recompiled and re-pinned as part of
this fix (`rights_status` is part of the compiled `repository.json`, so the manifest hash
changed); `records/worlds/cappadocian.yaml`'s current pin (`packages/cappadocian/2026-09-20T03-21-39Z`)
postdates the fix.

**Disposition: CLOSED, 2026-09-20**, fleet-wide, by commit `e5a50654`. Recorded here as a
closed item precisely because it was real, it was the worst instance in the fleet, and it
had gone undisclosed in this world's own record until now — the gap being closed does not
make its prior absence from this world's own tracking acceptable to leave silent.

---

## Gate log (G1–G5) — the Record-Native process's own human-checkpoint sequence

| Gate | Status | Date | Artifact |
|---|---|---|---|
| G1 — Scope & Sources | **RE-CONFIRMED by Mark** — corrected Part A scope argument + Part B manifest, after the 2026-08-30 reopening found and fixed real errors in the first pass | 2026-08-31 | `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` |
| G2 — Representative identity | **DECIDED by Mark** — Option 1 (guest-door elder), name later changed Eumathios→Chilo (2026-09-01); Option 2 (a sister of Annisa) left open, not foreclosed (OG-5) | 2026-08-30 | `cappadocian_Representative_Identity_Options.md` |
| G3 — Register-bar read (Permanent Prompt rebuilt to `CiC_Register_Bar_2026-08-29.md` + Template V2.4) | **DONE** — two independent adversarial review rounds converged clean | 2026-08-31 | `cappadocian_Representative_Permanent_Prompt_Eumathios.txt`; `cappadocian_Doc_10_PermanentPrompt_Review_Round1.md`, `_Round2.md` |
| G4 — Article 29 (Living Tradition Status) | **CONFIRMED by Mark** — "Confirm as drafted," on the widest living-tradition correspondence in the fleet (Eastern Orthodoxy, Oriental Orthodoxy, Roman Catholicism, and nearly all Protestant/global Christianity via the shared Nicene-Constantinopolitan creed) | 2026-08-31 | `cappadocian_Representative_Construction_Notes_Eumathios.md` §6; `cappadocian_World_Profile.md` §9 |
| G5 — Freeze/admission (this track's real equivalent: Phase B record-native build → M3 sealed-probe admission) | **REACHED — ADMITTED**, then re-admitted twice more after a rename and after a Representative rename | 2026-08-31 (first admission); re-admitted 2026-09-01 (post-rename) and 2026-09-01 (post-Chilo-rename) | `records/worlds/cappadocian.yaml`; `engine/m3/reports/live-admission-report-cappadocian-*.json` |

### Review-round detail for the four documents Mark specifically asked fixed (Doc_01, Doc_02, Doc_04, Doc_06)

Three fresh-context Opus review agents ran on the recovered build (2026-08-30): one on
Doc_01, one on Doc_02 (cross-checked against the approved manifest), one auditing
Doc_03/04/06/08/09. **Headline finding** (`CAPPADOCIAN_BUILD_LEDGER.md` §5): the recovered
build's *reasoning* was consistently better than its *bookkeeping and memory* — no
fabricated source or wrong classification found, but real, recurring misremembered facts
(Basil's death year given as 378 by both Doc_01 and Doc_02 independently, corrected to
377), misattributed scholarly positions (McGuckin assigned the opposite of his actual
view), an overclaimed manifest row (NPNF2 vol. 7 falsely said to contain Gregory
Nazianzen's Invectives against Julian — caught before any file was downloaded), and the
world's most consequential single correction: **the "last martyrs" self-description was
wrong** — Eupsychius of Caesarea was martyred under Julian in 362, inside this world's own
span, feast attested in Basil's own letters — and this line sat in the opening of the
deployed-style Permanent Prompt.

**Doc_01/Doc_02 — three rounds** (`§7`): a direct rewrite addressing the first review's 15
findings each; an independent follow-up review that found most fixes held but the rewrite
had introduced new errors, including the closest thing to a fabricated source this build
produced (a claimed homily on Eupsychius that isn't actually attested — only his feast
is); a second surgical fix round; a final bounded spot-check finding one remaining
contradiction and a mislabeled confidence level, both fixed. Round counts: ~30 blocking
errors → ~14 new/smaller → 2 narrow errors — a converging, not flat or worsening, pattern.
**Doc_04/Doc_06 — one rework round each**, independently verified against their own
self-reports; one real defect found and fixed (a backwards claim in Doc_04 about its own
interaction matrix).

**Residual, disclosed and not fixed at the time** (§7): the `.docx` mirrors of Doc_01/02
were two revision rounds stale (the `.md` files are canonical, per the Build Record); a
minor imprecision on Hilary of Poitiers' exile timing; Doc_03's pruning note not yet
updated for four Tier-2→Tier-3 placements Doc_06's rework surfaced.

### Source Registry (CF V7.4 Step 2 companion to Doc_02) — three review rounds, converged

`cappadocian_Source_Registry.md`, 116 rows. **Round 1** (`cappadocian_Source_Registry_Review_Round1.md`):
completeness gaps (nine sources with no row), six broken cross-references, one
reintroduced fabrication-adjacent claim (the same Eupsychius-homily defect, caught a
second time), two Boundary/Exclusion-Reason errors, four schema violations, systematic
confidence-tier drift. **Round 2** (`_Round2.md`, against the 112-row revision): eight
further wrong cross-reference targets the revision's own audit had missed, three wrong
section pointers, a residual tier miscalibration, three more missing sources, and — most
consequential — the revision's own claim to have checked every cross-reference was itself
false. **Round 3** (`_Round3.md`, against the 116-row revision): two precisely-located
remaining errors plus three cosmetic pointer inaccuracies, recommended as narrow fixes
rather than a fourth full round. **Disposition: Approved to proceed** (self-dispositioned,
2026-08-31) — none of the four standing escalation categories applied.

### Sibling research session's Source Registry fix (rows 31, 32, 36, 39, 40) — four review rounds, 2026-09-08

A separate research session found rows 39–40 wrongly marked "not within the vendored
edition" (all five letters actually present with body text) and rows 32/36 wrongly marked
"within" the edition when only Prolegomena catalogue mentions exist, not the works' own
text. **Four Opus adversarial review rounds** each found the previous round's own fix had
introduced a new error of the identical class while correcting something else — a
self-contradiction, an overstated grounding claim, a wrong letter count corrected
incorrectly twice, a misattributed round citation. `CAPPADOCIAN_BUILD_LEDGER.md` §50
names this pattern explicitly: "every one of the three review rounds found at least one
new, real error the previous round's own fix had introduced." A Round 5 confirming review
was named as the next step and a full re-audit of the generator script's remaining ~110
rows as a disclosed, still-open gap (folded into OG-7 above).

### G3's Permanent Prompt rebuild — two review rounds

**Round 1** (`cappadocian_Doc_10_PermanentPrompt_Review_Round1.md`): register work strong,
but Tensional Gravity 9 (the reserve argument over naming the Spirit God outright) was
entirely absent from the doxology paragraph — a false-unanimity failure — and two
Template V2.4-mandatory sections (the subject-of-utterance backstop; Section 2A Approved
Source Anchoring) were missing entirely, inherited from the orphan build's older template.
Six further MEDIUM findings, ten LOW. **Round 2** (`_Round2.md`): both HIGH findings fixed
and verified; five of six MEDIUM fixed; the sixth (a Living Traditions closing) only
partly fixed, introducing two new problems — a fidelity verdict about one living
communion's faithfulness spoken from a voice that cannot know it, and a reserve-holder's
motive stated as the "we"'s own settled judgment rather than his friend's claim. Both
fixed directly; no third round commissioned (findings were narrow, low-risk, precisely
located). **Disposition: Approved to proceed**, self-dispositioned, 2026-08-31.

---

## Phase B — record-native conversion log (condensed; full detail is `CAPPADOCIAN_BUILD_LEDGER.md` §14–§27)

Mark authorized Phase B ("start Phase B now") on 2026-08-31 once G1–G4 cleared and the gap
between "Phase A complete" and "freeze/admission-ready" was named plainly. Built B-1
through B-9 (plus an inserted quote/doctrinal_witness step the governing process document
had no row for, approved separately) in sequence, each step independently re-verified
against the full gate battery before the next:

- **B-1** (world_core + 110 source records) — one real judgment-call set, self-corrected
  mid-build (the `verification_state` mapping rule caught and fixed 8 of its own
  rule-violating rows).
- **B-1a/B-1b** (discovery sweep + independent recall/PRESS test) — **caught a real
  error**: two Source Registry rows falsely claimed specific homilies were present in a
  vendored volume when only a scholarly description of them was; fixed immediately.
- **B-2/B-3** (39 term records) — **a third instance of the same "falsely verified"
  defect class** caught mid-authoring (Basil's *Against Eunomius* treatise wrongly marked
  verified); plus a duplicate-YAML-key defect across 10 of 11 gravity records, and the
  Basileias anachronism reaching a live-facing field (OG-8's origin).
- **B-4** (19 story + 15 figure records) — two more content-accuracy errors caught in
  Doc_09 itself (Basil's death date; a McGuckin/McLynn misattribution) and named as owed
  fixes to Doc_09's own prose, not just the record layer.
- **B-5** (11 gravity + 17 force records) — a YAML parsing defect and a structural
  precondition-direction error caught and fixed across 8 records before the final gate run.
- **B-6** (4 contested_claim records) — Primary-gravity minimum satisfied; Tensional-
  gravity candidates explicitly deferred, not silently dropped.
- **B-7** (voice_craft + 9 demonstrations, authored on Fable per the pinned
  voice-construction routing) — **surfaced a real process-document gap**: the governing
  process document had no step producing `quote`/`doctrinal_witness` records at all,
  despite every other admitted world holding 12–56 of each. Put to Mark; approved as a new
  inserted step.
- **Quote/doctrinal_witness step** (26 dw, 4 quote, 2 honest_limit records) — a cold
  adversarial review (blind to the drafting) found 3 real defects (a ~200-year date error,
  an uncited claim compounded by a real misattribution, a citation-range looseness), all
  fixed and independently re-verified. Also surfaced and fixed a **fleet-wide schema gap**
  (a `modern_rendering` field every world's `quote` records needed but the schema never
  declared — silently failing `gate_schema_validation` across six worlds; fixed as
  infrastructure, not content).
- **B-7a** (Facilitation Brief refresh) — corrected two stale status claims and added
  Desert as a named pairing candidate.
- **B-8** (first-ever compile) — the literal governing-document row was confirmed
  non-executable (points at infrastructure retired 2026-08-28) and structurally
  inapplicable (presupposes a migration from an existing hand-deployed corpus this
  never-deployed world doesn't have). Put to Mark; **decision: register and compile now.**
  `state: built`.
- **B-9** — confirmed to contribute nothing further beyond B-8 for a first-ever build; no
  forced task invented.
- **M3 admission** (2026-08-31, Mark: "Authorize M3 admission now.") — 28/28 sealed
  probes, real live Bedrock generation, zero failures. **ADMITTED, 2026-08-31, Mark: "yes,
  admit it."**

---

## Post-admission events (renames, portrait, doors-open, live read)

- **Full-alignment rename, 2026-08-31** (`world_id: nicene-cappadocian` → `cappadocian-trinitarian`;
  `display_name: "Nicene-Cappadocian Christianity"` → `"Cappadocian Christianity"`). Raised
  by Mark ("i was concerned that it would corrupt the world build... fix it right").
  Executed across all 259 record files, `records/worlds.yaml`, the directory itself
  (`worlds/Nicene-Cappadocian/` → `worlds/cappadocian/`, tracked git renames), and 17
  document mastheads — with historical entries and Doc_01's own original Label Test
  reasoning deliberately preserved, dated-correction-noted rather than rewritten. Required
  a recompile + fresh, second live M3 admission run (2026-09-01) to re-certify under the
  new identity — done, 28/28 again.
- **Representative rename, 2026-09-01** (Eumathios → **Chilo**). Raised by Mark ("I was
  not part of the original memorability/accessibility weighing... concerned it would be
  hard to remember"). Real candidates researched from Basil's own vendored correspondence
  (two: Urbicius and Chilo); **Mark: "go with Chilo."** Required its own recompile + third
  live M3 admission run — 28/28.
- **Icon object decided, 2026-09-01** — the loaf, grounded in three of this world's own
  sources (the brotherhood-day hospitality provision, the famine-preaching line, the
  voice_craft record's own opener imagery). **Mark: "go with the loaf."** Portrait
  artwork produced, iterated through five rounds against a full documented/inference
  grounding brief, **locked by Mark 2026-09-01** ("yes, lock it in"), wired into every
  live-facing location (Atlas census, marketing site, participant Table app).
- **PR #73 opened 2026-09-01, merged 2026-09-01** (`e948cb02`) after CI was found broken
  (7 of 16 checks red) and fixed at the design level per Mark's explicit instruction
  ("fix the fixture count test with the principle of fixing design not just adding patch
  on patch") rather than patched. `CIC_ENFORCE_ADMISSION` had been globally "1" since
  2026-08-28 (a fact this session's own earlier ledger entries had gotten wrong and
  corrected in place); the real remaining "doors open" act was the merge itself. Cappadocian
  Christianity has been a live, seventh formation world since 2026-09-01.
- **First live conversation, read by Mark, 2026-09-01** (§38) — four threaded, natural
  questions, not sealed probes; held its disciplines (we-voice, honest limits, real
  citations) throughout, unprompted.

---

## Cross-world / fleet-level findings naming Cappadocian specifically

- **OG-11 above** — the rights_status internal-narration defect (65/111 records, 59%, the
  worst rate of any world checked; fixed fleet-wide 2026-09-20, PR #321).
- **The "Boundary Structures" vs. "Boundary Ecology" terminology inconsistency**
  (`Ministry/Operations/Standing/CiC_GoLive_Pipeline_Status.md`, item 6, 2026-09-16): the
  Constitution and Forces-Framework governing documents contradict each other on the
  canonical term; ruled `Boundary Structures` for the `lpc` world specifically, but three
  sibling worlds' Doc_05 files — **alx, don, and cappadocian** — use the other term.
  **Flagged, not fixed** — doc-hygiene on content outside that thread's own scope, per
  this project's own default ("flag it, don't touch it").
- **`figure-dates-keys/cappadocian`** — an `ACCEPTED_OPEN` waiver
  (`CAPPADOCIAN_BUILD_LEDGER.md` §36): Cappadocian's figure records key contested dates as
  `display` prose (e.g. Basil's death, "traditionally placed at January 379 or September
  378, though the modern redating literature argues for 377 instead") rather than
  born/died/floruit fields, a second independently-justified minority convention alongside
  `pahc`'s own prior outlier. The fleet's own cross-world check threshold was fixed at the
  design level (a strict-majority rule instead of a "one known outlier" special case) so
  it stops mis-flagging every other world when a second real outlier exists.
- **Narrative/process-note stripping from canonical build documents** (SS41–44 of the
  ledger, and `Ministry/Operations/Standing/CiC_System_Health_Tracking.md` lines ~460–535,
  PRs #205/#206): a separate fleet-wide pass removed injected `[CORRECTED per Round N]` /
  revision-announcement narration from Alexandria, Syriac, Donatism, and Cappadocian's
  Doc_01–09 and related documents, keeping every fact and citation while dropping the
  comparison framing — the same class of "keep live/canonical surfaces clean" discipline
  this project's own CLAUDE.md states directly. Cappadocian's own generator script
  (`wb_cappadocian_s21.py`) was named as still carrying the same narrative pattern inline
  and handled as part of that pass.

---

## What this file does not claim

This file was assembled from `CAPPADOCIAN_BUILD_LEDGER.md` (52 sections), the Source
Registry and its four review-round sets, `cappadocian_Unused_Source_Verification_2026-09-09.md`,
`cappadocian_Representative_Identity_Options.md`, the two G3 Permanent Prompt review
rounds, `records/worlds/cappadocian.yaml`, `records/WORLDS_REGISTRY_LOG.md`'s own
Cappadocian section, and the fleet-level `CiC_GoLive_Pipeline_Status.md` and
`CiC_System_Health_Tracking.md`. It does not re-verify every review round's own findings
against the underlying primary sources a second time — where the ledger itself already
records that discipline (and it does so unusually often, and unusually self-critically,
for this world), this file trusts that record rather than re-deriving it. Two items are
carried here with an explicit "last known status, not reverified now" caveat rather than
a flat claim: OG-8 (Doc_06 §23's Basileias naming) and OG-7 (the ~110 unaudited Source
Registry rows) — both are honestly still open by the ledger's own most recent word on
them, not resolved by anything found while writing this file.

### OG-12. **Two fragment/verbless `modern_rendering` sentences, found by `engine/m1/sentence_completeness.py`'s report-only sweep — current as of `engine/m1/reports/sentence-completeness-report-2026-09-24.json`, not yet human-reviewed.** `cappadocian.quote.basil-on-the-doxology-challenge` ("At another, 'through the Son, in the Holy Spirit.'", `no_finite_verb`); `cappadocian.quote.macrina-refuses-remarriage` ("Her resolve held firmer than anyone would have expected from someone her age.", `no_finite_verb`). Report-only check (not in `gates.GATES`); its own docstring requires a human read against the actual fragment rule before treating either as a real defect. Logged as found and current, not adjudicated. See `worlds/pahc/Open_Gaps_Tracking.md` OG-12 for this same report-run's full fleet-wide context.
