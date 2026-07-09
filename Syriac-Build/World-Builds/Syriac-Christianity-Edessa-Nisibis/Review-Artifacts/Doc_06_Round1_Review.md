**Simulated review — informational only, not an Article 31 substitute** (Constitution Article 35, Section B)

**Document reviewed:** Doc_06_Full_Lexicon_Development.md, Lexicon-Chunks/*, and Lexicon_Deployment_Index.xlsx, World #7: Syriac Christianity (Edessa/Nisibis)
**Review round:** 1
**Recovery note:** Verbatim original review-agent output, retrieved directly from the session transcript (`47f6719b-134c-455f-b73b-9be8fc43fd3e.jsonl`, tool_use_id `toolu_01CBDCfbMFgFZ1o9k5bHCzX4`), not a reconstruction or summary.

---

# Adversarial Review — Doc_06 Full Lexicon Development, Round 1
World #7: Syriac Christianity (Edessa/Nisibis), c. 200–410 CE

## Environment note (read this before the findings)

While reading the four "ground truth" prior documents, I hit the exact stale-file symptom the task brief warned about, twice, with two different outcomes:

- **Doc_05_Ecological_Reconstruction.md**: the bash-mounted filesystem consistently returned a 29,115-byte file ending mid-sentence at "Authority Structures (4.1) remain." A second, independent access path (native Windows `Read` tool at `C:\Users\mchad\Documents\CiC-Project\...`) showed the complete, correct 157-line file with a proper closing Open-Items list. **This confirms the known bash-mount caching artifact is real and currently active in this session** — I used the Read-tool version for all Doc_05 analysis below.
- **Doc_03_Lexicon_Candidate_List.md**: both the bash mount and the native Read tool agree — independently — that the file is only 107 lines / 22,660 bytes, ending mid-sentence in the middle of the Mar entry ("Sources: Sebastian Brock,"). Section 2 (Catholicos), Section 3 (malpana/Peshitta exclusions), Section 3.3, and Section 4 are **absent from the file as it currently exists**, on both access paths. Since the two independent tools agree (unlike the Doc_05 case), this looks like a genuine, current data-loss/save problem with Doc_03 itself, not a read-side artifact — worth flagging to the maintainers directly. I reconstructed most of the missing content via the unaffected companion `Lexicon_Candidate_Index.xlsx` (all 5 sheets read cleanly) to cross-check Doc_06's Section 2/3 claims, but **could not verify** Doc_06's specific claim that "Doc_03 Section 3.3" names exactly "kasyutha/hayla kasya, qaddishutha, dukrana" — that content is in neither the truncated Doc_03 nor its index.

## (a)/(b) Issues found

1. **[Environment/process, not a Doc_06 authorship defect]** Doc_03 truncation described above. Blocks full independent verification of Doc_06 §3's "Section 3.3" citation until Doc_03 is confirmed restored.

2. **[Substantial]** Doc_06 §3: *"malpana: the earliest attested titles at the School of Nisibis, founded c. 489–496, are mhaggyana, mpashshqana, and mqarrena, not malpana in that institutional sense."* I grepped every document and workbook in the folder — these three title-names appear **nowhere** except in this one sentence of Doc_06. Doc_03/its index only established that malpana's attestation for Ephrem specifically "could not be verified" and that the School of Nisibis postdates him by a century; they never named replacement titles. This is new, specific, unverified detail introduced at Step 6, at exactly the level of specificity (named technical terms) this project's own revision logs (Doc_01–Doc_04) repeatedly caught as invented precision. It doesn't appear in a chunk file (malpana isn't built), but it's a live claim in Doc_06's own narrative and should be sourced or removed.

3. **[Substantial, narrow scope]** `Lexicon_Deployment_Index.xlsx`, **Terms** sheet: rows 6 (Ewangeliyon da-Mhallete) and 7 (Iḥidaya) both show **RT = "N"**, but both chunk files' own front-matter carry the RT tag ("Yes"), and the same workbook's own **By Tag** sheet correctly lists both terms under RT. The Terms sheet contradicts both the source chunk files and its own sibling sheet — exactly the "independently drifted data" failure mode the review brief asked me to check for. A retrieval system filtering on the Terms sheet's RT column would silently exclude two runtime-relevant terms.

4. **[Cosmetic-to-substantial, template compliance]** Doc_06 §1 explicitly asserts: *"Tier 3 entries carry Quick Meaning and a single-line Distortion Risk pairing only... no Tier 3 entry here was expanded with sections the LDF reserves for Tier 1/2."* This is inaccurate for 2 of the 3 Tier 3 entries:
   - `syrlex008_mar.md` includes a full "## Key Sources" section — a Tier 1/2-only section per the tier spec.
   - `syrlex009_catholicos.md` includes a full paired "Modern Hearing:"/"World Hearing:" Distortion Risk (not single-line) plus an entirely extra "## Standing Distortion-Risk Note" section not in the template at all.
   Only `syrlex005_memra.md` actually matches the stated Tier 3 discipline. Doc_06's own self-description of structural compliance is wrong for the majority of its Tier 3 entries.

5. **[Cosmetic]** `syrlex001_raza-shrara.md`, World Meaning: *"...a phrase Sebastian Brock's scholarship on Ephrem develops as hayla kasya, 'hidden power.'"* This names a modern scholar and "scholarship" inside inhabited World Meaning prose, violating the LDF's no-analytical-distance-marker rule for that section — the same pattern Doc_05's own Round 1→2 revision explicitly caught and fixed elsewhere (Harvey/Beck/Koltun-Fromm moved into bracket tags). The underlying claim is fine and already correctly hedged in the Key Sources note; this is a placement fix, not a substance fix.

6. **[Cosmetic, process-transparency]** Doc_06 §0's "all eight tier estimates held" is demonstrated with real Doc_04 engagement only for the four Tier 1 terms; Tier 2/3 assignments (taḥwyāṯā, Ewangeliyon, memra, Mar) are asserted as "remain" with no term-specific engagement with Doc_04/05's actual findings (e.g., Doc_05 §4.1's direct discussion of "Mar Jacob" vis-à-vis C4 is a natural hook for Mar that goes unused). I independently re-checked all four and they hold up — so the conclusions are right, but the documented "recheck" leans toward assertion for more than half the terms.

7. **[Minor, worth a maintainer note only]** Catholicos is given a literal "Tier: 3" in both its chunk front-matter and the new index, rather than preserving the distinct "Flag-only" bucket Doc_03's own companion index took a Round-2 fix to establish. Doc_06 §2 transparently explains this choice in prose, so it isn't a silent drift — just a loss of a distinction the predecessor document worked to keep visible.

## (c) Checked out fine — should NOT be changed

- **World-code claim (§0):** independently verified against Doc_01's full text (confirmed complete via two access paths) — no world-code of any kind exists in Doc_01. Doc_06's gap-naming-and-assigning approach is accurate and exactly the transparent behavior this project's discipline calls for.
- **qyama (syrlex002) and Ewangeliyon da-Mhallete (syrlex006) hedges:** both precisely carry forward their required exclusions — the Ephrem-choir claim is correctly excluded from qyama's evidentiary basis (matches Doc_03 1.2 and Doc_04's Round 2 narrowing exactly); Ewangeliyon's name-dating is correctly stated as unresolved, not settled either direction (matches Doc_03 1.6/1.6a and Doc_04 C5 exactly, including the Theodoret/Crawford detail).
- **Catholicos entry and §2's reasoning:** consistent with, not contradictory to, Doc_03's "not a normal vocabulary candidate" disposition; built narrowly as claimed, Related-Terms intentionally empty and justified.
- **Related-Terms reciprocity:** fully verified across all four layers (each chunk's front-matter, each chunk's own Reciprocity Note, Doc_06 §4's summary table, and the index's Related-Terms Reciprocity sheet) — complete agreement everywhere, all links reciprocal, both non-reciprocal cases (Mar, Catholicos) stated by design in every layer. This is the most cleanly executed part of the document.
- **Ecological Function / gravity claims:** every chunk's claim checked against Doc_04's actual C1–C6 classifications and Interaction Matrix — no overclaiming found anywhere (e.g., Ewangeliyon correctly says C5 "Supporting," not Primary; qyama's C2×C4 "Reshaping" claim matches Doc_04's matrix cell verbatim).
- **Sourced citations:** Brock, Murray, Harvey, Malki Malki, Griffith, Petersen, Wickes, Parisot, Lehto, Kitchen/GEDSH all trace cleanly to Doc_02's Source Registry with matching author/title/year/journal/volume — no fabricated or misattributed citation found (item 2 above is unsourced narrative detail, not a miscite).
- **CT Contest Type sections:** all three CT-tagged entries have genuine, specific, filled-in contests matching the index's own CT Contest Type Check sheet.
- **Confidence calibration:** no entry claims stronger confidence than Doc_02–05 already established for the same facts.

## (d) Overall verdict: **Needs substantial revision**

Specific items requiring fixes before finalization: **item 2** (unsourced malpana title-names — remove or source), **item 3** (index RT-column drift on 2 rows), and **item 4** (Tier 3 template overbuild on Mar and Catholicos, plus correcting Doc_06 §1's inaccurate compliance claim). Items 5–7 are cosmetic/minor and can be bundled with the substantial fixes rather than triggering a separate round. Item 1 (Doc_03's apparent truncation) should be resolved by the maintainers independently of Doc_06, but blocks full sign-off on Doc_06 §3's Section 3.3 citation until confirmed.

---

*(Agent metadata from original transcript: agentId a9c4fe7c0ed2cbd1f; subagent_tokens 172971; tool_uses 38; duration_ms 570831.)*
