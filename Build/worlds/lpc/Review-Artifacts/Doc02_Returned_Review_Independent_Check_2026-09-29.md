Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry: independent check of the review returned 2026-09-13 (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.0
- **Reviewer agent:** independent-review subagent, fresh context, session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** lpc build thread and the 2026-09-26 live-surface clean-up pass (commit trailers read "Claude Sonnet 5"; the 2026-09-13 correction, 7f71981fd, reads "Claude Opus 5"; the restore, 45aa2333, reads "Claude Opus 5.5")
- **Round:** 31 (a targeted check of the review returned on 2026-09-13; not a new revision cycle)
- **Truncation check, method 1:** structural count. Registry: 215 table lines, every one with exactly 12 pipes; 213 numbered rows forming exactly the set 1 to 213; the saturation statement ends on a complete sentence. Doc_02: headings §1 to §10 all present, in order; §10 ends on a complete sentence.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 6053424ff. `wc -c` equals `git cat-file -s` (Registry 220,657 bytes; Doc_02 81,540 bytes), `git hash-object` equals `git rev-parse HEAD:<path>` for both files, and both files end with a newline.
- **Date:** 2026-09-29
- **Documents:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, `Build/worlds/lpc/Source_Registry.md`
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish (P0/P1/P2 correspond to HIGH/MEDIUM/LOW in Rounds 1 to 30).

## Verdict

**The 2026-09-13 corrections hold. The files as they now read do not clear.** 0 P0, 6 P1, 6 P2.

All eight text-location corrections are true on disk. The row 44 narrowing does not hold as written. The companion Doc_02 was never brought into line. Edits made after the disposition added new errors, and none of them was reviewed: the PR #197 line, #557 round 3, and the 2026-09-26 clean-up. Nothing found misstates the historical world or invents a source. Every error concerns the build's own record of what it holds and how it knows it.

## What the 2026-09-13 return asked

From `lpc_Decision_Log.md`, entry "2026-09-13 — `Source_Registry.md`: eight stale text-location claims corrected", and commit 7f71981fd:

1. Rows 37, 44, 56, 64, 65, 206 and 208 had said their texts were "on the sibling Donatism build's own branch" and "not usable directly by this document without its own vendoring step". These were rewritten to say the texts are held in the shared corpus. Row 65 was also rewritten to say the *Gesta* is "available to Doc_04, and not yet drawn on by it".
2. Row 44's Confidence B had rested on two legs. It was narrowed to the one leg said to still hold: "the vendored file has not been read against this row's Licensed-For content".

One more item was routed to this review later. Doc_04 Round 11 (2026-09-14) adjudicated act 158 against the source file. It recommended an amendment to row 65 and said the amendment "belongs to that review" (`Doc04_Round11_Review.md`, "Adjudication at source").

## Item 1: the eight location corrections (resolved, one residue)

Checked at HEAD. Every file named is present and tracked:

- `cil8-supplementum-numidiae_cagnat-schmidt1894.txt`
- `theodosianus-16_mommsen-meyer1905.txt`
- `optatus_libri-vii-critical_ziwsa1893.txt`
- `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`
- `monceaux_histoire-litteraire-afrique-chretienne-tome4_1912.txt`, `tome5_1920.txt`, `tome6_1922.txt`

None of the five stale phrases, or the three looser variants the Decision Log names, survives anywhere in the Registry.

The PR #197 reconcile (e4fcf352c) replaced the whole Registry with that line's copy. I checked that the correction survived it: it did.

**P2-A. Row 65 still opens "Not currently vendored on this world's own branch."** The sentence means Lancel's edition, which is true. But it is the branch-relative wording the 2026-09-13 entry said it would stop using, and it sits directly before the cell's account of the *Gesta* printing that *is* vendored. Compare row 64, which avoids the problem with "Not currently vendored (Labrousse)."

## Item 2: the row 44 narrowing (not resolved) — P1-2

The one remaining leg is contradicted by the same cell. Row 44's Licensed-For is "the underlying imperial statute behind the Theodosian-law fine Augustine's own Letter 185 §25 cites". The Verification Note then does exactly that work. It names the provision as *CTh* XVI.5.21, cites its heading and the operative phrase by file line, maps §25's wording onto it "clause for clause", and ends "Identified against both files directly."

I re-read the provision at source (`theodosianus-16_mommsen-meyer1905.txt`, heading `XVI, 5, 21 (392 lun. 15).` at line 86853). It reads *"Id haereticis erroribus quoscumque constiterit vel ordinasse clericos vel suscepisse officium clericorum, denis libris auri viritim multandos esse censemus"* (lines 86855–86857; the scan prints *censemua*, normalized here). So the Licensed-For content has been read against the vendored file. Two statements in the cell say it has not: "Not independently checked against a specific locus" and "Confidence deliberately left at B, not raised: this row's Licensed-For content has not been read against the vendored file".

The error runs in the cautious direction, but the stated ground for the letter is false. The build thread must either raise the letter under the calibration rule, or state precisely what remains unread. Either choice is a change to a sourcing conclusion.

## Item 3: the act-158 amendment routed here (not applied) — P1-3

Row 65 still calls act 158 "a genuine act in which Augustine speaks". It still counts it among "**fourteen** numbered acts in which Augustine speaks".

I checked the source file. At line 121764 (`158.  Augustinus  episcop`), the act runs straight on to the garbled subscription formula at 121768 (`mendalum ·usccpi fll nibacripsj`, i.e. *mandatum suscepi et subscripsi*). No other speaker comes in between. This confirms Round 11's reading: act 158 is a subscription to the mandate, not a speech. The floor for speech-form acts is thirteen.

Row 65 also says the *Gesta* is "not yet drawn on" by Doc_04. Doc_04's own line 7 says it "relies on one narrow fact from a withdrawn read", and that fact is this act. Row 65 should carry Round 11's amendment and state accurately what Doc_04 relies on.

## Changes since 2026-09-13

Commits that touch the two files since the disposition:

- 7f71981fd: the correction itself
- The PR #197 line, brought in by e4fcf352c: Doc_02 edits, unreviewed
- 978d26c35: #557 round 3, Registry rows 14 and 213, unreviewed
- 28e35b19e, 87cea0c09, b2a5ab01, 7aabc5d8 and 45aa2333: the live-surface clean-up and its repairs

**P1-1. The corrections were never carried into Doc_02, which now contradicts its companion.**

- Doc_02 line 93 says *CIL* VIII (row 37) is "not currently vendored".
- Doc_02 line 97, on the *Codex Theodosianus*, says: "The vendored file is not present on this world's own branch, so it is not usable directly by this document without its own vendoring step, the same position row 37 records for *CIL* VIII". The same sentence had just named the file `cic/texts/theodosianus-16_mommsen-meyer1905.txt` as vendored. Row 37 no longer records that position.

These are the exact phrases the Registry corrected on 2026-09-13. The same parenthesis in line 97 also has a closing bracket with no opening one.

**P1-4. #557 round 3 changed two Registry rows after the disposition, and nobody reviewed it.**

*What holds.* Both new quotations are verbatim at source:

- *Answer to Petilian* II, ch. 51 (§118), line 16912: "the chair of the Roman Church, in which Peter sat, and which Anastasius fills to-day…"
- Letter LIII §2 (a.d. 400), lines 29696–29710: "For if the lineal succession of bishops is to be taken into account… In this order of succession no Donatist bishop is found."

*Row 14.* The row was raised from B to A, "A for that one locus and B for the rest". The calibration rule gives a row one letter, earned on its Licensed-For. Row 14's Licensed-For still includes a body-level claim this build has not verified: "the most extensive surviving Donatist voice… in Augustine's own refutation". Row 11 carries exactly this split and names it "a question… not decided in this pass". Row 14 settles on its own authority a question row 11 leaves open.

*Row 213.* Three statements are wrong:

- "Not yet promoted into the main corpus map" is false. The cluster has been in `cic/corpus-map/donatism.yaml` since 8c5eb2c46 (2026-08-27). It is in neither this world's map nor its staging assignment, whose `atlas_ids` is `donatism`.
- "The same normalization row 13 and row 14 carry" is false for this world's map. Both works are `role: tradition` in `latin-pastoral-congregational-christianity.yaml`, and row 14 says so itself.
- The row claims no overlap with rows 10 and 11. It does overlap row 43 (Letter XCIII), which it does not disclose.

*Doc_02.* Line 27 still says row 14 is "not independently drawn on for a specific claim in this world's own construction". That is no longer true.

**P1-5. The corpus count at the head of Doc_02 is now false, and the clean-up is what made it false.**

Doc_02 line 13 reads "90 `tradition`-role census entries, 88 distinct titles… 99 raw entries against the next-largest's 68, 90 `tradition`-role entries against 59". Before b2a5ab01 this read "90 `tradition`-role census entries **as of 2026-09-08**". Removing the date turned a true dated figure into a false present one.

The corpus map now holds 104 raw entries, 94 `tradition`, 92 distinct titles. The next-largest file holds 69 raw entries (`alexandria-catechetical.yaml`, 61 `tradition`). The claim that this is the largest file still holds.

The growth is four `tradition` entries added by d4512b644 (2026-09-24): Petschenig's CSEL 51–53, *De Baptismo*, *Contra Epistulam Parmeniani*, *Contra Cresconium* and *De Unico Baptismo*. They are vendored at `cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`. **None has a Registry row, and Doc_02 does not mention them.**

The Registry's saturation statement now points to Doc_02 §1 as "the single current source" for the count, so the stale figure is the only one either document gives.

**P1-6. Doc_02's Possidius passages are out of date and contradict themselves.**

Line 21 says Doc_01 "discloses [the Megalius identification] as carried in this world's vendored corpus 'only as NPNF's own editorial note'". It then says "corrected at Doc_01 §5, this flag discharged", followed by "not corrected here, since Doc_01 is… outside scope". This sentence came in on the PR #197 line after the disposition.

Doc_01 §5 now cites Possidius, *Vita* ch. VIII, directly and points to a full read (`Review-Artifacts/Possidius_Full_Read_2026-09-16.md`). Doc_02 still says otherwise in two places:

- §2 *Limitations*: "not yet independently read beyond the specific passages the vendoring pass sampled"
- §4, line 83: drawn on "only indirectly, via NPNF's own editorial apparatus… has not yet been read"

Both have been false since 2026-09-16.

**P2-B. The line numbers in rows 44 and 65 are off by one.** Every cited line is one lower than its place in the file today: 86852→86853, 86855→86856, 87881→87882, 113067→113068, 113075→113076. Round 30 disclosed this as COSMETIC and held it "pending the… language-header fix". That fix is 7fc7832d5 (2026-09-09) and has already landed, so nothing blocks the correction. The world folder now cites the same file on two numbering bases: row 65 on the old one, Doc_04 and its Round 11 on the new.

**P2-C. Row 29 cites `cic/corpus-map/tertullian-s-voice.yaml`, which no longer exists.** It was merged into `latin-apologists.yaml` by a5a7e312c (2026-09-10). Row 204's "assigned to `tertullian-s-voice`" is stale for the same reason.

**P2-D. Row 189 cites the path `cic/texts/npnf106_...xml` with an ellipsis.** The file is `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`.

**P2-E. Two small gaps in #557's own wording.** Letter LIII is headed as a joint letter from "Fortunatus, Alypius, and Augustin" (line 29650). Row 213 calls it "Augustine's own named succession" without saying so. Row 14's "Book II §51" is NPNF's chapter 51; the section is 118.

**P2-F. Doc_02's Status line does not disclose post-disposition edits.** The Registry's Status line says it "has been edited after its disposition". Doc_02 has been edited too, by the PR #197 line and the clean-up, and says nothing.

## What the clean-up cut (noted, not edited)

Real content removed:

- **The census date and baseline in Doc_02 §1** (b2a5ab01). This removed "as of 2026-09-08", the "up from 73" baseline, and the list naming the eleven second-witness entries. The first two cuts cause P1-5. Without the third, Doc_02's "eleven" can no longer be checked from the document.
- **Divjak's 1975 and Dolbeau's 1990 and 1996 dates** (b2a5ab01). Restored by 45aa2333, so resolved.
- **Row 56** (87cea0c09). Removing "this revision" left "independently checked **" before the cell break, a bold marker that no longer closes. Cosmetic.
- **The Registry saturation statement** (87cea0c09). This removed the original saturation basis (73 works; 65 `assigned`, 8 `provisional`) and the round-by-round list of recall-test instruments. Both survive in `lpc_Decision_Log.md` (lines 160, 198, 204) and in `Doc02_Round1–14_Review.md`, so they were moved, not lost. But the saturation statement the template requires now gives no figure of its own, and its pointer leads to the stale one (P1-5).

Moved correctly: row 33's Confidence question now points to `Open_Gaps_Tracking.md` OG-20, which exists.

Process narration only: the row 44 history, the round tags on row ranges, and the "this session" wording. Nothing of substance was lost.

§9 is protected. b2a5ab01 touched it and 7aabc5d8 restored it. Its only remaining difference from the approved text is two process clauses removed by 28e35b19e, which carry no substance.

## Checks run with nothing found

- Every `cic/texts/` and `cic/corpus-map/` path in both files resolves, apart from P2-C and P2-D.
- Every vendored row's file header matches the row's title, editor and date. Checked for rows 37, 44, 64, 65, 88, 191–213. Among them: Hartel 1868/1871; Goldbacher CSEL 57, 1911; Weiskotten 1919; Harnack TU 1913; Bruder 1838; Monceaux 1901/1902/1905.
- No invented source was found.
- Epistle XXXIX against XL (a clause added to Doc_02 after the disposition): "your suffrage and God's judgment" and "ancient venom" sit at `anf05` lines 32372–32373, inside Epistle XXXIX (div3 from 32346). Epistle XL begins at 32578 and carries neither phrase. The clause is correct.

## What one round cannot close (for Mark)

1. **The review cap.** Doc_02 now has 30 round files against a cap of 3, and this check makes a 31st. P1-1 to P1-6 need a fix pass, and CO-022 treats P1-2, P1-4 and P1-5 as substantial. How that pass is governed is a governance call: a further round, or a directed correction with a targeted recheck. CLAUDE.md's cap rule sends it to Mark.
2. **Row 44's letter (P1-2) and row 14's split letter (P1-4).** Both are sourcing conclusions. Row 14 also settles the calibration question row 11 leaves open: can a row carry a split letter? That is a methodology question.
3. **Changes made by other workstreams.** #557 (a records fix cycle) and d4512b644 (a vendoring pass) changed this world's evidentiary base after its disposition, and neither routed the change through this review. Whether such passes must reopen Doc_02 and the Registry is a process decision.

## Outside this scope, noted only

- `records/lpc/honest_limit/lpc.limit.411-gesta-unread.md` gives `license: public-domain` for Lancel's Sources Chrétiennes edition, which is in copyright.
- Provenance headers in several vendored `cic/texts/` files still carry lines like "corrected here, independent review Round 23's own M1": commentary on a live surface.
- None of `Doc02_Round1–30_Review.md` carries the V2.0 header, so all 30 would fail `reviewfile`.
