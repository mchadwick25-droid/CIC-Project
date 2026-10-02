Simulated review — informational only, not an Article 31 substitute.

# Doc_04 — Gravity Discovery (lpc): independent targeted check of the findings carried open from Rounds 5–11

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** independent reviewer subagent, fresh context, session_01EgyL7xtErqj72CaFiEUx4q
- **Drafter agent:** lpc build thread
- **Round:** 12 — an independent targeted check after Round 11. It is not a revision round, and it does not reopen Doc_04.
- **Truncation check, method 1:** content hash and byte size of Doc_04 (74954 B, 266 lines), the appendix (8339 B, 61 lines) and Round 11 (59192 B, 428 lines) compared to the HEAD blobs at 0769ae705 with git hash-object and git cat-file -s; all three identical.
- **Truncation check, method 2:** structural completeness of Doc_04 and the appendix. The full heading sequence runs §1–§8 plus Disposition. Every table row has the same pipe count (§4 10×6, §6 10×10, §8 28×5). No line has an odd count of bold markers. The last line of each file ends a complete sentence.
- **Review date:** 2026-09-29
- **Drafter provenance note:** Doc_04 and its reviews do not record which model drafted them. CLAUDE.md routes Doc_04 drafting to Fable and revision to Sonnet. The text on disk is the product of the revision passes, so the drafter field gives the revision model. That is the routing default, not verified provenance.

**Scope.** Doc_04, the appendix `Doc_04_Superseded_Claims.md`, Rounds 5–11, `Open_Gaps_Tracking.md`, and targeted greps of `lpc_Decision_Log.md`, Docs 05–09, `lpc_World_Profile.md`, `Representative/` and `records/lpc/`. Where the files and the ledger disagreed, the files on disk were trusted. Candidate 5's classification is the project lead's ruling and is not revisited here.

---

## 1. Verdict

**No open finding changes a gravity, a classification, a six-test verdict or a matrix relation, in Doc_04 or downstream.** Candidate 5 is Supporting everywhere it is stated. Open findings do reach downstream *record text* in three places (N1–N3 below). None of the three moves a gravity.

## 2. High finding re-verified at source

**Act 158: Doc_04's one relied-on source fact holds.** I opened `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` and checked it by structural marker:

- line 121756 is the preceding act header, `l.")7. PtUUamt tpiucpit dixii` (act 157, Petilianus, with a speech verb);
- line 121764 is the act header, `158. Augustinus episcop`;
- lines 121765–67 run through `...tribuno el nourio Marcdliuo` with no speech verb (*dixit*);
- line 121768 is the subscription formula, `mendalum ·usccpi fll nibacripsj` (*mandatum suscepi et subscripsi*);
- the neighbouring subscriptions in the giving voice (`...mandavi et subscripsi`, 121736–46) and Vincentius's `hoc mendetum` (121775) match.

This confirms Round 11's H3 adjudication. For contrast, the strict scan for Augustine act headers that do carry *dixit* finds 50 (126796), 53 (126874), 160 (128393), 187 (128716), 201 (129009) and 272 (130298). Act 14 at 125505 (`Angustinus episcopus ... dixit`) is a genuine fifteenth instance, missing from row 65's list, as the Decision Log records.

The CF V7.4 text was also checked, using `word/document.xml` paragraphs 305, 306, 310, 311 and 312. It confirms Round 11's L2 and Round 8's H1(d) below.

## 3. Carried-open findings, and what the files on disk show now

| Finding | Present disposition on disk |
|---|---|
| R11 H1 (Status/Disposition round range) | **CLOSED.** Line 3 reads "1–11" and "5–11", and §8 lists 11 rounds. |
| R11 H2 (completeness claim) | **CLOSED.** Appendix l.3 is softened, l.7 is consistent with it, and Doc_04's closing paragraph after §8 is softened. |
| R11 H3 (act-158 adjudication propagated unverified) | **CLOSED** at Decision Log ll.831, 859, 871. Re-verified at source in §2 above. |
| R11 H4 (unmarked withdrawn basis) | **CLOSED.** The Decision Log l.793 marker is present. |
| R11 M1 (Tensional exclusion exists only as withdrawn material; appendix §1.2 "nothing depends on it" vs Doc_04 l.91) | **LIVE.** |
| R11 M2 (escalation positions diverge) | **LIVE, and wider.** Disposition l.266 still gives "two items" for governance (the Decision Log gives three, and Round 11 added a fourth, (d)). It also counts §7 Open Item 6 as an open tension, but Open Item 6 has been **CLOSED** since 2026-09-15 (l.212). |
| R11 M3 (inline correction narration) | **PARTLY CLOSED.** The l.175 sentence is gone. l.34 ("citation correction, not a classification change") and l.207 ("restored") are live. |
| R11 M4 (appendix l.5 vs the §4 preamble) | **LIVE.** |
| R11 M5 (the pass's self-report) | Record-only. It concerns a past Decision Log entry, so no fix on disk applies. |
| R11 M6 (§5 l.188 drops the search-bound qualifier) | **LIVE.** §3 l.90/94 and §4 still state the bound, so the verdict is unaffected. |
| R11 M7 (Open Item 6 has no owner or criterion; blind read unrouted) | **MOOTED.** Open Item 6 was closed on the precedent, and the blind read is logged in §8. |
| R11 L1, L4, L5, L6, L8, L10; C1, C2, C3 | **LIVE** (appendix l.35, l.61, l.31, the §1 heading, the §4 cell, l.33, the §4 third entry, and the §8 "Mechanical pass" row). |
| R11 L2 / R9 L1 (Primary definition quoted as 3 of 4 sentences, no ellipsis) | **LIVE** at l.99. Verified against CF ¶305. |
| R11 L3 / R9 C2 (altered verbs in the Doc_01 quote) | **LIVE** at l.7. Verified against Doc_01 l.177, which has "generates … states". |
| R11 L7 / R9 L3–L5 (*Gesta* artifact) | **PARTLY CLOSED.** "immutable history" remains at artifact l.10. The other two phrases are absent. |
| R11 L9 ("See the seventh entry") | **LIVE** at Decision Log l.777. |
| R8 H1(d) (the Cross-Check rule generalised) | **LIVE** at l.96. CF ¶310 is a bar on *upgrading* a candidate with strong tests but thin evidence, and l.96 paraphrases it as applying to any divergence. |
| R9 H4 / Open Item 8 (determinate classification reachable) | **DISPOSED.** Declined on the ruling and precedent §4b, and recorded at l.214. |
| R6 M9 / R9 M11 / R10 M11 (row 65 vs act 158) | **Doc_04 side CLOSED. Registry side NOT AMENDED.** Row 65 still reads "a genuine act in which Augustine speaks". See N2. |
| R9 M8, M12; R10 L10–L12 | Decision-Log-only record items. Not re-checked line by line. M12 is subsumed in R11 M2. |

## 4. New findings from this check

**N1 — MEDIUM (P1).** Doc_04 left stale status pointers behind when it closed Open Items 6 and 8, and they have spread downstream.

- Inside Doc_04:
  - l.97 routes the forces residue to Open Item 6;
  - l.105 says Round 9's finding "is unaddressed and is carried at §7 Open Item 8";
  - l.208 says "Open Items 6 and 8 may both bear on the classification";
  - l.266 counts Open Item 6 as an open tension.
- Doc_04's list of Round 11 MEDIUMs at l.259 names M1–M4 and omits M5–M7. Open_Gaps_Tracking and the Decision Log l.1748 repeat "four MEDIUMs".
- The stale pointers are inherited by:
  - Doc_05 l.173, 215, 317 and 354. Line 317 says the *Gesta* "is the one place that could change" G5, which contradicts precedent §4a;
  - Doc_07 l.94 and 250 ("Open Item 8 remains unaddressed");
  - Doc_08 l.358;
  - `records/lpc/gravity/lpc.gravity.conciliar-authority-theory.md`, whose description says "It remains open".

All of this is record-state text. None of it changes a gravity.

**N2 — MEDIUM (P1).** The row 65 explanation is still unapplied, and its effect reaches `records/`. `lpc.source.lancel-actes-de-la-conference-de-carthage-411` lists act 158 among the "FOURTEEN numbered acts in which he speaks", which contradicts the fact verified in §2. The number in `world_core` ("at least fourteen") stays true only because act 14 at 125505 replaces act 158. This answers OG-4's open loose end: row 65 has not been annotated.

**N3 — MEDIUM (P1).** A rights status is misstated in `records/`. The same Lancel source record gives `rights_status: public-domain; vendored in cic/texts/`. Its own `edition` field, Registry row 65 and Doc_04 l.90 all say that Lancel's Sources Chrétiennes edition is in copyright and consultation-only. Only the Migne PL XI printing is public domain. `lpc.limit.411-gesta-unread` repeats the error, citing the Lancel source with `license: public-domain`. This is the conflation row 65 itself warns against.

**N4 — LOW (P2).** In `world_core`, cautions item 9 says "In fourteen numbered acts" with no floor, and "each act has been counted and quoted". Row 65 asks that any restatement carry the floor, and it gives only a scan count. This record is participant-compiled.

**N5 — LOW (P2).** Open_Gaps_Tracking does not list the carried Round 5–11 findings, only "carried, not chased". Its OG-4 attributes "relied on for nothing" to appendix §2. That phrase does not occur in the appendix, whose line 7 says one narrow finding *is* relied on.

**N6 — LOW (P2).** Process narration sits in canonical records: the body of the gravity record ("See this script's own docstring…") and the body of the limit record. Under the rule for live and canonical surfaces, these are flagged here and not touched, because they belong to another thread's scope.

**N7 — LOW (P2).** The G5 gravity record assigns `formation_confidence: Inferential-Thin`, a tier Doc_04 never names. Doc_04 says only that existence is Documented and that breadth is "not comparably supported". The record discloses this as its own conservative choice, and the choice runs in the direction CF ¶310 points. It is noted, not faulted.

## 5. Is the Supporting ruling applied consistently?

**Yes, with no exceptions found.** The ruling appears as Supporting in each of these places:

- Doc_04 l.3, l.84, l.101, §4 l.162, §5 l.186 and 188, and Open Item 2;
- Doc_05 l.23 and 173;
- Doc_07 l.40;
- Doc_08 l.27;
- Doc_09 l.25;
- World Profile l.124–128;
- Representative Phase 1 l.96 and Phase 2 l.64;
- `records/lpc/gravity/*`: all eight classifications match §4 (P: 1, 2, 3, 6; S: 4, 5, 7; T: 8), and G5's record states the ruling as its provenance.

## 6. Items for the project lead (this check cannot close them)

1. **Round cap.** `roundcount lpc 4` fails with 11 rounds against a cap of 3. `--check-new --round 12` also reports it (informational here, and this file deliberately does not match the round-file pattern). Either the "no twelfth round" ruling gets an `ACCEPTED_OPEN` waiver, or this failure will recur on every run.
2. **Governance/methodology escalation.** It has been open since 2026-09-14 and now carries items (a)–(d). Only the project lead can close it.
3. **One change order to propagate the Open Item 6/8 closures (N1)** into Doc_04's own pointers, the approved Docs 05, 07 and 08, and the G5 record. The work is mechanical, but it edits four approved documents, so it should go through as a named change order rather than quiet edits.
