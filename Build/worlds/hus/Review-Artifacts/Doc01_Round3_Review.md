Simulated review — informational only, not an Article 31 substitute.

# Doc_01, Doc_02, Source Registry and gap ledger: Round 3 targeted recheck (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (revision commit 605c7c2f1; commit trailer reads "Claude Sonnet 5.5")
- **Round:** 3
- **Truncation check, method 1:** structural count. Doc_01: headings §1 to §10 present and in order (lines 13 to 214), 216 lines, ends on the §10 disposition sentence and a newline. Doc_02: headings §1 to §11 present and in order (lines 11 to 180), 182 lines, ends on the §11 disposition sentence and a newline. Registry: 54 numbered rows, every one with exactly 12 pipes (the header row also has 12); the numbers form exactly the set 1 to 54, with rows 25 to 28 as tombstones; letters A 18, B 8, C 23, D 1, and 4 tombstones marked "—". Open_Gaps: entries 1 to 25, R1 to R9 and E1 to E5 all present; the file ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 605c7c2f1. For all four files `wc -c` equals `git cat-file -s` (Doc_01 47,040 bytes; Doc_02 33,968; Registry 41,788; Open_Gaps 21,672), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_01 22e35159cb…, Doc_02 263e163316…, Registry 3e7e0f3d26…, Open_Gaps 15b3c52364…). None of the four has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md`, as committed at HEAD 605c7c2f1
- **Prior findings rechecked:** `Review-Artifacts/Round2_Recheck_Review.md` (0 P0, 3 P1, 7 P2). The drafter's table in `Build/Ministry/Operations/Audits/hus_Round2_Revision_2026-09-30.md` was treated as claims and checked at source.
- **Scope:** the diff of 605c7c2f1 only, plus the P1-1 record in `Build/Ministry/Operations/Audits/hus_Round1_Revision_2026-09-30.md` (added in c1bacd3bd).
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Clear.** 0 P0, 0 P1, 3 P2.

All three Round 2 P1 findings and all seven P2 findings are fixed. Every touched locus and quotation was read in the vendored file. The project lead's ruling now rests on his own recorded answer, and that answer was confirmed against the session's own record. The revision introduces nothing wrong, unsupported or misleading. The three P2 findings below are wording and provenance polish. None of them changes a claim, a tag, a sourcing conclusion or a boundary, so none of them starts a new round.

This was the third and last revision round allowed under the cap. Step 1 (Doc_01) and Step 2 (Doc_02, Registry, gap ledger) have cleared review. The strand ruling is already the project lead's own decision. The remaining questions for him (Article 29, the Representative, registration of `hus`) are carried as open and are not decided in these documents.

## Scope 1: the ten prior findings, checked at source

| Finding | Status | Checked at source |
|---|---|---|
| P1-1 ruling record | Fixed | See Scope 3. Doc_01 §5 "Ruling", Open_Gaps 5(a) and 13 now cite his answer, "One world, three strands (Recommended)", and the audit file. Doc_01 §9 item 1 and the header refer to the §5 ruling, which carries the citation. |
| P1-2 Rome in the Forces lens | Fixed | Doc_02 §6 last survivorship bullet now says Rome's opposition is attested "mostly through its targets (Hus's replies) and through later historians", and that Piccolomini is "the only Roman-side witness on the shelf". This agrees with the paragraph above it ("its own voice is absent") and with Doc_02 §2 ("The only contemporary hostile voice on the shelf"). |
| P1-3 Nuremberg from a Lollardy file | Fixed | A search of Doc_01, Doc_02, the Registry and Open_Gaps for "Norimberg", "Nuremberg" and "not settled" finds the reading only in Open_Gaps E3. Doc_02 §2 and row 48 now keep only Schaff's Frankfurt. R2 no longer states the reading. Open_Gaps section E's "Doc_02 does not rely on any of them" is now true. Doc_01 §7 still names the Loserth file by path as the place where Wyclif's own text is vendored; that is unchanged, and it is a pointer, not evidence for a claim. |
| P2-1 "Martyrum honores" | Fixed | Doc_01 §5 now paraphrases: the Bohemians "honoured the burned men as martyrs". Piccolomini line 4086 reads "Bohemis Martyrum honores meruere: nec minores quam Petrus & Paulus apud Romanos habiti" (scan: "Bohemss … minoret … cr"). The paraphrase is faithful. The cited line 4087 is one line off (P2-3). |
| P2-2 creed tag | Fixed | Doc_02 §8 now carries the Nicene wording, "incarnate of the Holy Spirit", "bodily" and "Lord and giver of life" as an untagged absence, "silent, not denied". This matches Doc_01 §8 and Open_Gaps 4. No sixth level is used. |
| P2-3 Doc_01 §6 readability | Fixed | Rescored with `engine.m7.turn_readability.score_turn`, markdown stripped, quotations left in: §6 FK 7.1, FRE 59.3, as the drafter says. The Round 2 judgment stands: a construction document with verbatim quotations, acceptable. |
| P2-4 tombstones | Fixed | Rows 25 to 28 each read "Vacated; number not reused." with 12 pipes. The header's "Numbers 25 to 28 are not used, and they are not reused" agrees. |
| P2-5 rights wording | Fixed, with a small new inaccuracy (P2-1 below) | Rows 44 to 51 now share one formula. Row 50's variant ("19th-century") is justified: the vendored passage gives no date for Erben's editions. |
| P2-6 loci | Fixed | Seifferth line 8214 reads "Note [15] to pap^e 121" (the next note, [16], is at 8270, so the 1508 passage at 8262–8264 is inside Note [15]). "the Minutes of an old Synod" runs over lines 8216–8217. *De Ecclesia* p. 70 now 5429–5434, and "in judgment" is at 5434. |
| P2-7 ascension and Timothy parity | Fixed | *De Ecclesia* lines 3715–3721: "who ascended again into heaven, as is said in John 3 : 13 … And the as-cent was a local movement by which he took with himself the other parts of the body." Both quotations in Doc_01 §8 match after line-break-hyphen normalisation. §8 now counts the ascension for Hus's own gloss and discounts the Timothy passage for its lack of one, so the two cases are visibly treated alike. |

## Scope 2: what the revision newly introduced

Every changed line of 605c7c2f1 was read.

- **Doc_01 §6.** The Layer 1 sketch and the six-cell table were split into shorter sentences. Apart from the splits and short lead-ins ("four settings", "three things"), the content is unchanged: the same events, dates, cells and groups. Nothing of substance was added.
- **Doc_01 §5 and §8.** Covered in Scope 1. No new claim beyond the verified quotations.
- **Doc_02 §2, §6, §8.** Covered in Scope 1. No new citation, and no new use of a file assigned to another world.
- **Registry rows 7, 43 to 51.** Loci verified as above. No row's letter changed. No new row. The added Open_Gaps E3 sentence places the Loserth reading where the Registry header says such material belongs.
- **Tags.** No confidence tag was raised. One was removed (Doc_02 §8, now an absence), which is the correct direction.
- **Invention.** None found. The rights formula marks every date it does not take from a vendored file as builder knowledge, with one inaccuracy in the other direction (P2-1).
- **Narration in live files.** None found by reading. See Scope 4 for the checker.

## Scope 3: the P1-1 ruling record

- `Build/Ministry/Operations/Audits/hus_Round1_Revision_2026-09-30.md`, section "The project lead's ruling, in his own answer (2026-09-30)" (added in c1bacd3bd), gives the question, the three options and "His answer, verbatim: "One world, three strands (Recommended)"", with the session `session_019FXuEebrCDmzYe987sNAxL` and the date.
- I checked this against the session's own transcript on disk (`/root/.claude/projects/-home-user-CIC-Project/dc4537a0-d0c6-598f-ba9d-8cae1a07bfe2.jsonl`). An `AskUserQuestion` call with header "Hussite scope" put the same question with the same three options. The user's tool result, timestamped 2026-09-30T02:03:36Z, reads: "…two worlds?"="One world, three strands (Recommended)". The question text, the option labels and the answer all match the audit file word for word.
- This is a choice-box selection from the recommended option, and the record says so plainly. That meets the build cycle's bar of a verifiable record that the project lead said it.
- Doc_01 §5 says the answer "is recorded verbatim, with the session and date" in that file. Open_Gaps 5(a) and 13 say the same. All three citations are accurate. The ruling date, 30 September 2026, matches.
- The census grouping is still labelled a portfolio-level reason in Doc_01 §4 and §5 (checked in Round 2, unchanged).

## Scope 4: tool runs

- `python -m engine.m10.cli gaps hus`: `gaps: PASS`, exit 0.
- `python tools/check_live_commentary.py --surface worlds`: exit 0. For the four files:
  - Doc_01: 1 hit, PROTECTED (the §9 route-cue heading).
  - Doc_02: 1 hit, PROTECTED (the §10 route-cue heading).
  - Open_Gaps: 30 hits, all PROTECTED.
  - Registry: 50 hits (21 KEEP, 29 REWRITE), all iso-date, one per real row, in the Added and Discovery cells that Framework V7.4 Step 2 requires. The four tombstones add none. This is the same schema data cleared in Rounds 1 and 2.

## Findings

**P2-1. Row 48 calls its dates builder knowledge when they come from Schaff.**
- Where: Registry row 48, Verification Note: "The work is dated before 1930 (from the builder's knowledge)".
- The 1558 and 1715 printings are dated in the vendored file, Schaff lines 2225–2229, which the same cell cites. The formula understates the evidence; it does not overstate it. Row 46 also says "from the builder's knowledge" twice in one cell.
- Fix, when next touched: for row 48, say the dates are Schaff's; drop the repeat in row 46.

**P2-2. Row 7's parity parenthesis reads as a contradiction.**
- Where: Registry row 7: "(the same treatment as the Timothy passage, which counts only as a scripture quotation and is not counted)".
- It says "the same treatment" and then describes a different outcome. The meaning is "the same test". Doc_01 §8 states it clearly ("so unlike the ascension it is not counted").
- Fix, when next touched: "the same test as the Timothy passage, which has no gloss of Hus's own and is not counted".

**P2-3. Two small locus and transcription points.**
- Doc_01 §5 cites Piccolomini "line 4087" for the martyrs passage. "Martyrum honores meruere" is at line 4086; 4087 continues the sentence ("quam Petrus … Romanos habiti"). Cite 4086–4087.
- Registry row 43 puts "to page 121" in quotation marks as the text of line 8214. The scan reads "to pap^e 121". The Registry header says no OCR correction was applied to any quoted word. Drop the quotation marks or quote the scan.

## Not re-verified

- Any material outside the diff of 605c7c2f1, except the P1-1 record. Rounds 1 and 2 cover the rest.
- The claim that no hus-assigned file gives "Norimbergae" (the drafter's reason for dropping the reading). Only the four documents under review were searched.
- The whole-document readability figure the drafter gives (own prose, quotations removed, FRE 61.0). Only §6 was rescored.
- Publication years and rights of rows 44 to 51. No external instrument was used.
- The meaning of the paraphrase beyond the sentence at lines 4086–4087, and whether line 4086 falls inside the sect chapter (Round 2 accepted the chapter placement).

Disposition: Approved to proceed (self-disposed by the Library thread after the Round 3 clearance; recorded at the time in the document status lines).
