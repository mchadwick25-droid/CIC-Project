# Independent Review — Round 3 (Opus, targeted recheck)
## Target document: `witt_Phase7_Encounter_Ecology_Mapping_DRAFT.md`

**Date:** 2026-09-28
**Reviewer:** Claude Opus 5.5, a separate review agent with fresh context. It did not draft or revise this document. It is the same model that wrote Round 2.

**What this review is.** A targeted recheck of the revision (commit `ade63af88`) against the four Round 2 findings P7-S1 to P7-S4 in `witt_Phase7_Review_Round2_Opus_Independent.md`. It also checks the revision thread's account in `Open_Gaps_Tracking.md` OG-44, and whether this document is consistent with Phase Five and Phase Six as they now stand. It is not a fresh review.

**Verdict: SUBSTANTIAL. Not cleared.** P7-S1, the headline overturn, is fully resolved and verified. P7-S3 is resolved once the propagation fixes below are applied. The underlying conclusion was verified against the deployed prompt. P7-S2 and P7-S4 are only partly resolved. Round 2 asked for specific re-derivations that were not done, and one per-domain statement now contradicts Phase Five's revised scoring.

---

## Section 1 — What was checked

- The diff `7b37c68b6..c5685e29d` for this file, and the current file in full.
- `witt_GoLive_Adversarial_Review_Round1.md` N-1 (lines 548, 550, 673) and `witt_World_Profile.md` line 795 (the 2026-09-19 change order), for P7-S1.
- `witt_Doc_09_Story_Inventory.md` §5. Each of the eight strings Phase Seven now quotes was checked by exact-match search: all present.
- The deployed `packages/witt/2026-09-26T20-13-54Z/compiled/prompt.txt`: the [honest-limits] rule (line 53) and "What we keep returning to" (lines 31–37), for P7-S3.
- `witt_Representative_Permanent_Prompt_Nikolaus.txt` line 19 (the `.txt` synthesis paragraph).
- Cross-document: Phase Five's current Summary Table, Section 3.2 (AN-3), Section 8 (Open Item 6), and Phase Six's current B3 and B7.

---

## Section 2 — Round 2 findings, one by one

| Finding | Status | Basis |
|---|---|---|
| **P7-S1** "favorable at Step 8" | **Resolved; verified** | §8 and §11 now quote N-1's Step-8 text exactly ("and, for the 1543 treatise, its documented seven-point programme"; "whose actual recommendations we can state…"). They name it as the root cause of B-1 and cite the 2026-09-19 change order, which is confirmed at World Profile line 795. The syr comparison is withdrawn. OG-44 records the withdrawal of OG-42's sentence, as Round 2 asked. |
| **P7-S2** "no evidence-absent domain" | **Partly resolved (R3-P7-1)** | The false claim is withdrawn and Doc_09 §5 is quoted accurately. But Round 2's required separation of absent from thin was not made, and the paragraph now contradicts itself. |
| **P7-S3** ¶31 miscount / `.txt` as deployed | **Resolved, after propagation fixes (Section 4)** | The ¶31 correction is accurate (ten sentences, seven limits, no material culture) and cites the deployed [honest-limits] rule, quoted exactly from line 53. But §1, the §2 G4 bullet, §6.1 and the §9 last row still treated the `.txt` as deployed, and §6.1 described the deployed prompt as surfacing the synthesis "in second-person address, as Nikolaus's own opening statement." That was false of the deployed artifact. This reviewer checked the conclusion against the compiled prompt. It holds: "What we keep returning to" carries "a promise carried to the ears, never a heart shaped like clay - the one settled belief our world turns on", in we-voice. So the fixes are propagation only. |
| **P7-S4** Phase Five as "actual Representative output" | **Partly resolved (R3-P7-2)** | §2's closing paragraph and §11 are corrected. §3's opening, §3's per-domain "held" bullets, the §2 G8 bullet and §6's opening still present Phase Five's authored text as confirmation. One bullet (AN-3) now contradicts Phase Five outright. |

---

## Section 3 — Substantial residual findings

### R3-P7-1 (P7-S2 residual). §3 now calls all six World Profile §8 domains "thin-but-real" in the same paragraph that quotes Doc_09 naming two of them as absent. The §9 table was not separated.

**Found.** The revised §3 opens: "World Profile §8's own six Honest Limits domains are all *thin-but-real*." It then quotes Doc_09 §5: "**No woman's own story** — 'There is no version of any story in this inventory that can be retold from a woman's own perspective without crossing into invention.'" That is World Profile §8 domain 2 (Phase Six B3: "no text written by a woman survives in this world's library at all"). Domain 6, material culture, is "no material-culture source is vendored in this library at all" (World Profile §8, quoted at Phase Five CT-2). By Doc_09's own category, both are evidence-absent, not thin-but-real. Round 2 said explicitly: "The §9 table's Q2 column, and the §3 'distinct category' paragraph, need revising to separate the evidence-absent domains (a woman's own account; the peasants' side of 1525; an ordinary pastor's or parish's own voice; material culture …) from the thin-but-real ones." The §9 table is unchanged. "Women's own voice" and "Material culture" sit in the same Q2 category as household reception.

**Required.** Correct the "all thin-but-real" sentence. Separate the evidence-absent domains from the thin-but-real ones in §3 and in §9. This changes a stated classification, so it is substantial, though the edit is small.

### R3-P7-2 (P7-S4 residual). Several passages still treat Phase Five's authored probes as confirmation, and the AN-3 bullet now contradicts Phase Five.

**Found.** Round 2 said: "§3's per-domain 'held' statements and §11's verdict need re-deriving once Phase Five is re-settled." §11 was re-derived. §3 was not.
- **§3 opening** still reads "confirmed here directly against **actual Phase Five probe output** rather than assumed." Round 2 quoted this exact sentence as an instance of the finding.
- **§3, domain 3** still reads "tested in Phase Five (AN-3, the Tetrapolitan Confession probe), **held at SECOND LOOK**." Phase Five's revision scores AN-3 **FAIL** (feigned ignorance with a knowledge leak; S-6). That is a direct cross-document contradiction.
- **§3, domain 5** says CL-1 was "tested at the highest caution level" and gives no result. §8 and §9 correctly say the live system does not hold cleanly.
- **§2, G8 bullet:** "Phase Five … **directly confirmed** this domain sustains five- and six-turn deepening exchanges." **§6 opening:** "**confirmed directly** by Phase Five's probe battery and DEV Battery." Both are authored-text claims.
- **§2's closing paragraph** says "Phase Five's own revision states this plainly (its Open Item 6)." Phase Five's revised Open Item 6 no longer contains that statement. The revision deleted it (Phase Five Round 3, R3-2). The citation now points at nothing.

**Required.** Re-derive §3's per-domain statements from Phase Five's current scores. AN-3 is FAIL: it is a feigned-ignorance defect, and whether that bears on the information-versus-encounter question should be stated, not assumed. CL-1 follows whatever score Phase Five settles (Phase Five Round 3, R3-4 recommends FAIL). Replace "actual … output" and "confirmed directly" with language matching Phase Five's evidentiary status once Phase Five restores it. Point the Open Item 6 citation at wherever Phase Five puts that disclosure.

---

## Section 4 — Cosmetic and propagation fixes applied directly (2026-09-28)

None changes a finding, a verdict, or a per-domain result. Recorded here, not inline.

- **C-1.** Status paragraph: "(Phase Five, then Phase Six, now both settled, then this document)" → both "themselves revised and awaiting Round 3 independent review". Neither is settled.
- **C-2.** Four stale "Approved to proceed" claims about Phase Five and Phase Six are corrected: the "What kind of document" paragraph, the "Governed by" parenthetical ("(all Approved to proceed)"), §0.3, and §11's "every answer traces to a specific, already-Approved-to-proceed prior document". Doc_01–Doc_10 and World Profile remain correctly described as Approved to proceed.
- **C-3.** P7-S3 propagation, conclusions verified unchanged:
  - §1 now names the `.txt` as the design artifact and adds the compiled prompt, at the points actually cited.
  - The §2 G4 bullet now cites the deployed "What we keep returning to" line ("the household examined and fed. Three parts said morning, table, and night"; verified present) alongside `.txt` ¶19/21.
  - §6.1 now says the deployed prompt surfaces the synthesis in its own "we" in "What we keep returning to", quoted exactly, and that the second-person opening statement is the `.txt`'s.
  - The §9 last row now cites the compiled prompt, with `.txt` ¶19.
  - §6.1's own assessment ("defensible … surfacing … directly") holds on the deployed text, so it was not touched.

---

## Section 5 — Boundaries, other notes

- **No new live probes; no Facilitator turn type designed or implied. Confirmed.** §9's 1543 row names the missing turn type (OG-24) and does not sketch one.
- **Not findings, for the next revising thread:**
  - §8's heading still says "with one real exception." After P7-S1 there are two: the G13 register, and the 1543 boundary that a prospective Phase Seven "might genuinely have caught."
  - §8's "Why not much" paragraph calls World Profile §8 "a document produced independently of, and prior to, any Representative-construction decision." Its current 1525/1543 text is the post-construction 2026-09-19 change order, which §8 itself now says.
  - Round 2 asked that Open Item 3 (read Doc_04 and Doc_07 directly) be completed in this revision. It was not. The limitation is still honestly disclosed, so this is not a finding, but the request stands.

---

## Section 6 — Verdict and disposition

**Verdict: SUBSTANTIAL. Not cleared; not eligible for "Approved to proceed."**

- Resolved: P7-S1; P7-S3 (with C-3).
- Open: **R3-P7-1** (P7-S2), **R3-P7-2** (P7-S4).

Both residuals are small edits, but they are substantive under the skill's definition: a classification, and per-domain results that contradict Phase Five. R3-P7-2 depends on Phase Five settling first, both on CL-1's score and on its evidentiary-status wording. The directed order (Five, then Six, then Seven) should hold. A next revision would be **round 2 of the three-round cap**. No escalation category is triggered by this document's own residuals. This review does not change the document's status line.
