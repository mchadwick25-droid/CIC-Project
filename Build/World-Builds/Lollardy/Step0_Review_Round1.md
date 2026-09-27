# Step 0 Review, Round 1 — Lollardy

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` (Revision 1, drafted 2026-09-15).

## Verdict

**Substantial revision needed.** The broad historical picture holds (no creedal dispute, the movement outgrew Wycliffe, the English-Reformation line is genuinely contested) and the carry-forward-not-re-derivation framing is grounded. The problems are concentrated in the sourcing section (B1/B2) and in claims about what was actually checked (A1/A3) — several claims about the census are false, some contradict the document's own dossier, and the document claims checks were performed that it elsewhere admits were not done.

## Findings

### Substantial

**S1. §3 B1 and §4.1: "Four sources the census marked 'Verified'" is false.** Checked against the census as it stood at drafting (`git show 8673befa`). Only two Lollardy sources actually carried "Verified.": Hudson's *Selections* and Tanner's *Norwich Heresy Trials*. *English Wycliffite Sermons* was tagged "[S] edition details from knowledge" — not verified even for content. Hudson's *Two Wycliffite Texts* (1993) was never a census source at all — it appears only in a story note in `river-prototype.html`. The dossier's own §4 table says exactly this; its own lead sentence and this document both contradict that table. The document also omits the one source the census did call verified (the Cambridge History of Christianity chapter) and never assesses Lahey's in-copyright *Trialogus* (2013).

**S2. §3 B1: "five genuinely PD… leads the census never named at all" is false, contradicting the dossier.** The census named "the Latin works in the Wyclif Society editions"; the dossier's own §3 says Buddensieg "Confirms the census's 'Wyclif Society editions' lead" and Forshall & Madden "Confirms the census's own lead." Dossier §6 itself says only Arnold and Vaughan were "not named in the census at all" — two, not five. B1 contradicts itself in the same paragraph by calling Vaughan a correction to "the Wyclif Society the census names."

**S3. A1 and A3 claim checks the document elsewhere admits were not done.** A1 says Article 4's commitments are "not disputed by the surviving Lollard record checked this pass"; A3 says the dossier "verified" the Twelve Conclusions and Bible tracts. But B2 and §4.3 say these "were not independently re-confirmed this pass," and §4.2 says Arnold/Matthew were "not yet vendored or content-assessed." Nothing was vendored on 2026-09-15 (drafting date) — everything was vendored 2026-09-25 per REGISTRY.yaml; the 09-15 dossier checks were rights/host checks, not content reads. A1's own text contains a leftover mid-sentence correction ("McGlothlin's Schleitheim — no, …") copied verbatim from the Anabaptist sibling document — direct evidence the "checked" list was not built from an actual check of this candidate's own sources. The floor section as written tests none of Article 4's five commitments against any text; it restates the census's own floorNote. The conclusion is historically sound and the now-vendored corpus could ground it (e.g. explicit Trinitarian lines in Arnold Vol. III, `wyclif_select-english-works-v3_arnold1871.txt` around lines 6397 and 21103) — the revision must either ground the floor in text or plainly label it carried-forward-without-a-text-check, not claim a check that didn't happen.

**S4. §3 Section B conclusion: "lateral correction… does not change that tier" is unsupported.** The census's own Tier 2 rests on "hostile trial records… alongside real internal texts"; A3's clearance rests on "what the trial records preserve"; B4's audience appeal rests on the trial-record "double witness." But the dossier found none of the trial-record witnesses accessible (Tanner and the Thorpe *Two Wycliffite Texts* are both borrow-only). Everything actually vendored is Wyclif-attributed writing plus the Bible — the dossier itself calls the corpus "a movement built around one prolific author's writings." The leg that the person-defined clearance cites currently has no accessible source, and the document never names this tension. Untested PD leads worth checking: Foxe's *Acts and Monuments* (19th-c. editions), the Rolls Series *Fasciculi Zizaniorum* (1858). Calling the sourcing change "lateral" is an unsupported sourcing conclusion.

**S5. B2/B1: "Wyclif's own academic corpus (Arnold, Matthew)" is historically inaccurate and misses that the sermon cycle is already available.** Arnold Vols. I–II contain the Sunday Gospels/Proprium/Commune Sanctorum/Ferial Gospels/Sunday Epistles cycle — the same cycle Hudson & Gradon later edited as *English Wycliffite Sermons*. Modern scholarship generally treats this cycle, and much of Matthew's collection, as Wycliffite (collective) rather than Wyclif's own personal writing — Arnold's own preface has a "Spurious and doubtful writings" section. The "complete vernacular preaching corpus" B1/§4.1 treats as closed is in fact vendored, in an older PD edition; B2's "genuinely uncertain… collective voice" framing is partly wrong; labeling these texts as Wyclif's own personal writing feeds directly into the A3 person-defined question and should be revisited.

**S6. §0, A5, B4 quote census text no longer live.** Verified with `git log -S`: the `why` wording ("carries the contest rather than the conclusion," "worth an entry on its own") was removed 2026-09-20; the statusWord's "(Era 6 Step 0)" tag was dropped by Decision 7; the statusDescription wording about the Era 6 Step 0 gate was rewritten 2026-09-25 (live text now reads "Checked here, they clear it"). These quotes were verbatim when drafted — not fabricated — but the document presents them as the census's current record when they're superseded. The carry-forward itself is grounded elsewhere: `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`, 2026-08-02 (Pass 3), "Q4 — Lollardy person-defined check CLEARED," Mark-gated, within the Era 6 Freeze — §0 should cite this instead. Note the Decision Log records only the person-defined check at that gate; "no creedal question" traces to the separate Pre-Step0 Survey floor note — A1's claim that the floor was "already established at the Era 6 Step 0 gate" overstates the record.

**S7. §0/A4: Mark's stated selection rationale has no supporting record.** The document attributes to Mark a choice made "specifically for its direct Wycliffe-Bible-translation lineage" and a "namesake theme already live in this build run." No record of either rationale was found anywhere in the repo (grepped `Build/worlds/_cross-world/README.md`, the RZG launch prompt, `Ministry/`). Attributing unrecorded motives to the project lead conflicts with this project's own source-fidelity discipline and the build-cycle skill's explicit rule that nothing is attributed to the project lead without a verifiable record. Remove or cite a record.

### Minor, but actually wrong

- §0's claim that the Wycliffite Bible "gives the movement its name" is false — "Lollard" derives from Middle Dutch *lollaert*, a term of abuse, unrelated to the translation.
- B3's "over a millennium's separation" from patristic worlds is wrong — 451 to 1380 is ~930 years.
- §4.2 is stale: says "not yet vendored," but all seven works were vendored 2026-09-25.
- B1's "no figure here is word-extracted from vendored XML" boilerplate is inapplicable (no XML here).
- B1's HathiTrust-check claim is only actually recorded for Hudson's *Selections* in the dossier.
- B5's "narrowest single-region claim in this batch" is arguable given Wittenberg's own "Saxony, then N. Europe" listing — "the only candidate confined to one region throughout" is fairer.
- The "content accuracy only, not accessibility" framing overstates the issue as a "conflation" — the census never claimed accessibility in the first place; "the census never assessed accessibility" is the more accurate framing.

### Confirmed accurate

Article 4's five commitments quoted verbatim, matching `Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` (title page reads "Version 2.3"). Dates (1401 burning statute, 1409 Arundel constitutions, 1414 Oldcastle rising, survival into the 1520s) all correct. `relationsSummary` quoted correctly. The Vaughan/Wyclif-Society naming distinction is itself handled correctly and honestly in this document (see below for a related but separate defect). Rights bases match file headers. The contested English-Reformation line is handled honestly.

## Related defects found outside this document (flagged, not fixed by this review — belongs to the thread that touched these files)

- **Duplicate registry entries:** `cic/texts/REGISTRY.yaml` has all seven Lollardy files registered twice (approx. lines 2721–2783 and 2857–2919).
- **False Wyclif Society attribution:** the vendored Vaughan file's own header, its REGISTRY.yaml note, and the corpus-map note in `cic/corpus-map/lollardy.yaml` all describe Arnold's and Matthew's editions as belonging to "the later Wyclif Society" — false. Arnold is Clarendon Press 1869–71 and Matthew is EETS 1880, both years before the Wyclif Society was founded (1882). Only Buddensieg is an actual Wyclif Society edition.
- The dossier's own §4 lead sentence ("All four… marked Verified") contradicts its own table.

## Disposition

Per `cic-build-cycle`: S1–S7 each state something false, contradicted by the record, or unsupported — this meets the project's own bar for substantial revision. The revision should correct the "Verified"/"never named" claims, either ground A1 in vendored text or label it plainly as carried-forward, re-anchor §0 to the 2026-08-02 Decision Log, reassess B1/B2/B4/Section B against what's actually vendored (including the Arnold sermon-cycle finding and the missing trial-record leg), and remove the unsupported selection rationale. This is Round 1 of the project's own three-round cap.
