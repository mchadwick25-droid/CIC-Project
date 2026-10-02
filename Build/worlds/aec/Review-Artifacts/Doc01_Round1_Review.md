# Round 1 adversarial review: `aec` (Antiochene Exegetical Christianity, Chrysostom-centered), Step 0, Doc_01, Doc_02 + Source Registry

All three documents need SUBSTANTIAL REVISION. Every finding below was checked independently against the vendored files, the corpus-map (merged file and `_staging/`), the census JSON, the Step0 Conclusion docx (text pulled from `word/document.xml`), the Methodology docx, the Constitution docx, the `lpc` world files, and the holdings tool.

**What held up:**
- Both headline quotations are verbatim and in Chrysostom's own voice (Eutropius, `npnf109` line 17591; Romans 12:20, line 16323).
- The Ammianus loci and quotes are accurate.
- The census Name/Dates/Region, the Step0 Conclusion "Possible future worlds" quote, the Methodology A5 quote, and the Article 21 quotes are accurate.
- The Palladius queue entry is present, `not-yet-downloaded`.
- Registry coverage of corpus-map rows is complete (47 rows, each mapped to exactly one registry row).

---

## Step 0: SUBSTANTIAL REVISION REQUIRED

**H1 (HIGH), §3 B3, the central deliverable. The contrast with World #8 is not tested against World #8 as it actually exists, and the corpus contradicts it.** World #8 (`lpc`) is built: Doc_01–Doc_09, a Representative, and Doc_04 Approved to proceed on 2026-09-15. `lpc` Doc_04 already classifies "Preaching and Catechesis as Primary Formation Mode" (Supporting). Its Source Registry holds the *Enarrationes in Psalmos* (~695,000 words of "ordinary preached and dictated congregational exposition") and the *Tractates on John* (~412,000 words). B3's claim that serial exposition is "essentially absent" from Cyprian and present in Augustine "only as one genre among several" is false on World #8's own record. Fix: redo B3 against `lpc` Doc_04's actual classified gravities.

**H2 (HIGH), §3 B3 and §6. Escalation is required.** This document overturns a portfolio-level deferral and confirms Tier 1. CLAUDE.md lists cross-world/portfolio decisions as "Always ask." Fix: do not self-dispose.

**H3 (HIGH), A1 boundary caution. A false premise about Theodoret.** The document says the Theodoret material carried here "is not itself condemned content." But the corpus-map carries *The Anathemas of Cyril with the Counter-statements of Theodoret*; Constantinople II canon XIII (vendored, `npnf214`) anathematizes exactly this work. Fix: correct the statement.

**M1 (MEDIUM), §0.** "Retained only as a legitimate [tiebreak]" alters the docx's actual "retained only as a legitimate scheduling consideration." (Independently re-verified and already fixed by the build thread before this review completed.) The same quoted paragraph's "Standing flag" about Theodore of Mopsuestia (condemned in Byzantine tradition, venerated as "the Interpreter" in East Syriac tradition) is not carried forward anywhere.

**M2 (MEDIUM), A5. The Adversus Judaeos content is characterized in a minimizing direction.** "Harshly polemical against Christians who continued to observe Jewish festivals" takes a side on a contested question (the target of the invective) and comments on tone where §4.2 forbids exactly that. Fix: state only existence, date range, and occasion per the `npnf109` apparatus.

**M3 (MEDIUM), A5. A fabricated grounding claim.** "The corpus-map's own existing Ignatius-related note" using "Judaizing" — no corpus-map file contains "Judaiz". Fix: remove.

**M4 (MEDIUM), A1 (and Doc_01 §2).** The 430 close does not fall "before the Nestorian controversy" — it erupted 428–430 and runs through the window (Cyril's Anathemas, Nov. 430).

**M5 (MEDIUM), A1, B1, §4.3.** Theodoret's confidence is misstated as uniformly `provisional`; the corpus-map has *Eranistes* and *Letters* at `assigned`.

**L1–L6 (LOW):** window-vs-birth-year wording (§1); an altered quote inside quotation marks (A5, "Anomoean-Eunomian Christianity" for the actual slug); "third city" ranking needs qualifying for this window (B5; Constantinople outranks Antioch by 350–430); "delivered daily through Lent 387" is unsupported (B2); "no PD path" for Theodore overstates the dossier's own more precise wording (§4.4); the "first Step 0 pass to resolve a deferral" framing is unverifiable and the documentedStories finding duplicates a disclosure the census already carries.

---

## Doc_01: SUBSTANTIAL REVISION REQUIRED

**H1 (HIGH), §6.** "World #8 (… not yet built)" is false; `lpc` is built. §1's Distinctive Contribution and §6 inherit the invalid B3 contrast. Fix after Step 0 is redone.

**M1 (MEDIUM), §4.** The Theodoret material is misdescribed — the Counter-statements defend the Antiochene side against Cyril; the *Eranistes* argues against Eutychian-type Christology, not "against Nestorianism."

**M2 (MEDIUM), §4 and §7.6.** The strand decision dodges a boundary question Doc_01 itself owns: Theodoret's *HE* (323–428) is inside the window and reads like the other later-historian testimony (Socrates, Sozomen); the Counter-statements (430–431) are an edge case, condemned in 553; the *Eranistes* (c. 447) and letters fall outside the window. A strand question presupposes inclusion — sending a boundary question to Doc_04 is a category error. Fix: make the boundary finding per work, here.

**M3 (MEDIUM), §5.** "Settled post-381 consensus… not themselves party to the Trinitarian controversy" is false — Chrysostom's own vendored corpus contains an anti-Anomoean homily, and the Meletian schism divided Antioch throughout the window (Chrysostom was ordained deacon by Meletius, presbyter by Flavian, whose legitimacy Rome and Alexandria contested). No document mentions the schism; it is attested in the vendored Socrates, Sozomen, and Theodoret *HE*.

**M4 (MEDIUM), §2, §5.** Libanius and Diodore are called "not verified against a vendored primary source" — Socrates VI.3 (`npnf202`, already on this corpus-map) attests both directly. Fix: ground it there, at Confidence A.

**L1–L4 (LOW):** "3.3 million surviving words" is a raw `wc -w` of the XML including markup (about 2.74M with markup/notes stripped) — say "on disk," matching Step 0; the Statues homilies also carry `imperial-juridical-christianity` as a second id, not mentioned in §6's sharing list; "socially confident" Jewish community is an unsourced characterization; citing `rcg`'s Doc_01 as precedent when that world hasn't cleared review either.

---

## Doc_02 + Source Registry: SUBSTANTIAL REVISION REQUIRED

**H1 (HIGH), §8 and §9.6. The holdings tool is misdescribed.** `python -m engine.m9.cli holdings aec` crashes (`FileNotFoundError: records/aec`), not "no coverage row." Simulated: 74 files "in scope, unread," 6 of them tier 2 (Philostorgius, the Codex Theodosianus ×2, Boyd, npnf202, npnf214) — none disposed of.

**H2 (HIGH), §2 Representativeness. An invented family detail.** "A decurion-class family" — the vendored Schaff introduction (`npnf109` line 769) reads: "His father, Secundus, was a distinguished military officer (*magister militum*)." Fix: correct from the vendored text.

**H3 (HIGH), §3, §7, Registry row 17. The load-bearing gravity claim is licensed to Young 1997 as settled consensus, unread.** Young's actual thesis (per the reviewer's own outside knowledge, flagged as unverified/needing a second opinion) argues against the simple literal-vs-allegorical dichotomy this document relies on; O'Keefe and others contest the label too. The vendored Schaff introduction also states most of the homilies "are arranged in sermons with a moral application at the close" — relevant to Doc_01 §3's "interpretation and formation are the same activity" claim. Fix: tag the characterization Contested and flag row 17 for priority second-opinion review; ground the ancient self-description in Socrates VI.3 instead.

**M1 (MEDIUM), §1, §9.3, Registry rows 1–2.** The "representative spot-check" (the Romans 12:20 homily) is a standalone `npnf109` sermon, not part of the serial `npnf110`–`114` series B3 actually rests on. Zero loci in those 17 series rows were checked.

**M2 (MEDIUM), Registry header, rows 6, 8, 11.** Grouping hides real distinctions: row 6 merges `provisional` and `assigned` works; row 8 merges a provisional Ignatius eulogy with an assigned homily; row 11 misreports all four Theodoret works as provisional. The corpus-map now has 47 rows (Ammianus added), not 46, and Doc_02's own row-count references ("~25," "~20") don't match the actual per-file counts (18, 17).

**M3 (MEDIUM), Registry rows 13–16. Boundary Status inconsistency.** Ammianus is pagan, `role: context`, not re-verified this pass, yet marked Native/Confidence A. Socrates and Sozomen (whose subject is this world's own history) are marked Excluded, which cuts off the only independent narrative of Chrysostom's fall even though Doc_02 §8 says they're "drawn on." Row 13's "also Native to imperial-juridical-christianity" is wrong — the ijc row is a different work (Book XXVII.3), not this one (Book XXII).

**M4 (MEDIUM), Registry "Named acquisition gaps."** Refuses rows for sources it doesn't hold, contradicting the Template's own "every source currently known" instruction and this Registry's own rows 17–18 (Young, Kelly — also not held). Missing: the dossier's own §2 declined cross-links (Athanasius, Serapion, Malchion); §4's Diodore and Theodore/Mingana; Harkins 1979 (named in §9 with no row); census-named Wilken 1983, Meeks and Wilken 1978, Meyer's Palladius translation.

**M5 (MEDIUM), §9.1.** "Logged to WANTS-REGISTER.md-style tracking" — nothing was logged, and no `Build/worlds/aec/Open_Gaps_Tracking.md` exists. Reword the negative-search-result phrasing on the *Adversus Judaeos* translation to "not searched," which is accurate; a search was never actually attempted this session.

**M6 (MEDIUM), §6.** "The Anomoeans survive only through Chrysostom's framing" — but Eunomius's own *First Apology* and Philostorgius (Anomoean-sympathetic, via Photius) are vendored. Name them as own-voice candidates.

**M7 (MEDIUM), §10.** How an Article 23 "writing-from-inside" Representative handles this world's own documented anti-Jewish polemic is a governance/methodology question, not only a sourcing gap — name it as an escalation candidate.

**L1–L3 (LOW):** "September 386" for the Adversus Judaeos conflicts with Step 0/census (386-387); Olympias's letters don't survive at all, rather than merely "not currently part of holdings"; `CiC_Record_Native_World_Build_Process_V1.8.md` is cited but not present on this branch (only on `library-stage/roman-church-gregorian`); the V1.8 Step 2 outputs (quotability flags, own-voice/opponent-voice flags, a thin-evidence map, edition/language notes, `PAIRS.yaml` entries) are not produced.

**Outside these four files:** `records/worlds/aec.yaml` carries a header comment described as process narration in a canonical `records/` file.

**Answers to the brief's specific check items:** (3) the primary-gravity argument overstates what the corpus shows (Step 0 H1); (7) the holdings-tool description doesn't match reality (Doc_02 H1); (8) the strand reasoning dodges a boundary finding the evidence supports (Doc_01 M2); (9) Ammianus loci are accurate but the Registry misrepresents its Boundary Status and ijc-sharing (Doc_02 M3) — the Eutropius/Olympias/Innocent second-ids are accurate, the Statues second-id is omitted (Doc_01 L2); (10) Doc_02 mostly holds the no-characterization line on Adversus Judaeos; Step 0 A5 does not (Step 0 M2).
