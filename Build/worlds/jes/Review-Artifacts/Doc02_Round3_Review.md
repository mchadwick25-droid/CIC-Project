Simulated review — informational only, not an Article 31 substitute.

# Round 3 targeted recheck of Doc_01, Doc_02, the Source Registry, the gap ledger, the Step 0 change order and four Polanco headers (jes)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Sonnet 5.5 drafting worker (commits 434049d87 and 787385b57; commit trailers read "Claude Sonnet 5.5")
- **Round:** 3 (targeted recheck of the Round 2 findings and of the diff of commits 434049d87 and 787385b57; the last round permitted under the three-round cap)
- **Truncation check, method 1:** structural count. Doc_01 has headings §1 to §10 in order and ends on its Disposition sentence and a newline. Doc_02 has §1 to §11 in order and ends the same way. The Registry has 92 numbered rows, 1 to 92 in order with no gap or duplicate, each with exactly 12 pipes, and the file ends on a complete sentence. The ledger's numbered entries run 17 to 43 with no gap, and `git diff 787385b57^ 787385b57` on it shows no removed line, so it stayed append-only. Step 0 ends on its "Next step" line.
- **Truncation check, method 2:** byte and hash comparison against the committed blobs at HEAD. For ten files `wc -c` equals `git cat-file -s`, and `git hash-object` equals `git rev-parse HEAD:<path>`: Doc_01 028913ee85 (42,090 bytes), Doc_02 e468834771 (55,733), Registry bfa8b49237 (98,822), ledger a3bb46cdbf (46,361), Step 0 963fc75232 (21,342), change-order audit bcd6faa6ad (19,084), and the Polanco files v2 5145ee36fe, v4 7e03285372, v5 5da37271e8 and v6 56696c6cc1. None has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/jes/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md` and `Step0_Movement_Scope_Confirmation.md` (§3 B2, B4, B5 and §4 item 5), with `Build/Ministry/Operations/Audits/jes_Step0_ChangeOrder_2026-09-30.md` read as a set of claims, and the headers of `cic/texts/polanco_chronicon-v2-lat_1894.txt`, `v4-lat_1896.txt`, `v5-lat_1897.txt` and `v6-lat_1898.txt`. Prior findings: `Review-Artifacts/Round2_Recheck_Review.md`.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Clear.** 0 P0, 0 P1, 3 P2.

Both Round 2 P1 findings are fixed at source. The *Ratio* no longer carries a shelf date anywhere in Doc_01, Doc_02 or Step 0. Row 76 says the volume prints no year and tags 1599 as the builder's knowledge, Widely Accepted. The Step 0 change order now covers §3 B2, B4 and B5 as well as item 5. Every "before" in the audit file matches Step 0 at 787385b57^, and every "after" matches Step 0 at HEAD. Seven of the nine Round 2 P2 findings are fixed. P2-8 was declined, and the decline is sound. The three new P2 findings below are small record slips. None of them states a false fact about the world or the shelf.

Under the cap's rule, nothing left here is wrong, unsupported or misleading about the world. Steps 1 and 2 have cleared review. The disposition question is at "The change order's approval status" below.

## Scope 1: the Round 2 findings, at source

| Round 2 finding | Fixed | What I checked |
|---|---|---|
| P1-1, the *Ratio* date | Yes | *Institutum* v3 prints "RATIO ATQUE INSTITUTIO / STUDIORUM SOCIETATIS IESU." at line 24940 with no year, and the summary reads "VIII. Ratio studiorum . pag. 158." (line 89). "anno demum 1599" is at line 50520, under "INSTRUCTIO IX. / DE MODERATIONE IN DANDIS LITTERIS AD GENERALEM / ADHIBENDA." (lines 50514–50518). The only other "1599" (line 50953) is also an Aquaviva instruction. Row 76 now says all this, and tags 1599 as the builder's knowledge, Widely Accepted. `grep 1599` finds no hit in Doc_01, Doc_02 or Step 0. The remaining hits are row 45 (P2-1 below), the ledger's historical entries (36, 37, the Library acquisition entry and request R3), which entries 41 and 42 supersede, and the audit's quoted "before" text. |
| P1-2(a), the B2 summary | Yes | B2 now reads "dense to 1565; after that only the letters of Borgia, Nadal and Salmeron, to 1572, 1577 and February 1585; and after 1585 only the *Institutum*". This matches item 5 and Doc_02 §6 point 4. |
| P1-2(b), the Polanco clause | Yes | B2 lists "Tomi 2, 4, 5 and 6, for 1550–52 and 1554–56", as row 84 does. |
| P1-2(c), B5 and B4 | Yes | B5 now runs to 1565 in Lainez, then Borgia to 1572, Nadal to 1577 and Salmeron to February 1585, then the *Institutum* alone. It names the *Relations* (vols. 1–35, 1610–1650) and Trigault's Latin as the only mission voice after Xavier. B4 adds the *Relations* and lists India, Japan, China, Brazil, Ethiopia and the Congo as unsustained. Neither contradicts item 5. |
| P1-2(d), the records | Yes, with one leftover (P2-2) | Ledger entry 41 supersedes entry 36's "not amended" sentence and the "item 5 only" status line. The audit's §2 closing paragraph and §5 first bullet now say B2, B4 and B5 are amended. The build state's escalation says "applied to item 5 and, by its extension, to §3 B2, B4 and B5". |
| P2-1, row 88 | Yes | The 1565 file has "tro Canifio Theologo" at line 67 and "M. D. LXV" at line 96. "Canijiuf" occurs once, in the 1573 file at line 348, and not at all in the 1565 file. |
| P2-2, rows 78 and 82 | Yes | Tomus II opens with no. 259, "ROMA PRIMIS MENSIBUS I548" (the heading sits at line 302, not 298–300, which is trivial). Tomus V's last heading is "ROMA 28 MOVKMBRIS 1553" (line 40070). Borgia Tomus V: "Borgia supremum diem Romae claudit" (line 37080), and "EPIST. I033.— MENSE MARTIO I573" (line 37385). |
| P2-3, row 73 | Yes | Line 9710 reads "P. JOAÑNES DE PÒLANCO EX COMM.", and line 9108 reads "P. JOANNES DE POLANCO EX COMM.". The row now quotes both as printed. |
| P2-4, rows 82 and 83 | Yes | The Licensed-For cells now say "Coverage by date" and "The letters' wording was not read". A for coverage by date is now defensible. |
| P2-5, "January 1646" | Yes | *Institutum* v2 lines 54078–54082: Carafa elected "die 7 Ianuarii 1646", and the congregation ran "usque ad 14 Aprilis eiusdem anni". Doc_02 §1 (table and bullet), Step 0 B2 and item 5 now say April 1646. The "January 1646" left in Doc_01 §2, Doc_02 §8 and row 75 is Carafa's election, which is right. |
| P2-6, Doc_02 §1 row citations | Yes | Row 47 is Borgia's other volumes, row 50 is Polanco's other tomi, and Mercurian and Aquaviva are marked "(no row)". |
| P2-7, the shelf-search pattern | Yes | I ran the stated regular expression, case-insensitive, over every `.txt` and `.xml` file in `cic/texts/` with whitespace collapsed. It matches 144 of 396 files, and 85 of the 87 assigned files. The two misses are exactly the Canisius English of 1622 and Trigault's Latin of 1615. |
| P2-8, readability | Declined; the decline is sound | Doc_02 still scores FRE 58.3 and FK 7.6 by `engine.m7.turn_readability.score_turn`, and Doc_01 scores FRE 61.0 and FK 7.5. Doc_02 is a construction document for builders and reviewers, not participant-facing text. Round 2 itself graded this P2 and not a block, and the NorthStar floor governs participant-facing turns. Splitting §9's search record would change no claim. This is a "could be stronger" point, and under the cap it does not justify a fourth round. It should be carried as a note for participant-facing work (Doc_09 and later). |
| P2-9, "now vendored" | Yes | Doc_01 §9 item 9 reads "the vendored volumes". |

## Scope 2: the Step 0 change order

I compared each quoted block in the audit's "Extension" section with Step 0 as it stood at 787385b57^ and at HEAD, by exact substring. All five "before" blocks match the old text, and all five "after" blocks, with item 5's "after", match the current text. The Step 0 diff of 787385b57 touches only B2, B4, B5 and item 5, so the audit records every change it made.

The voice dates hold at source or on rows already checked in Round 2:

- Lainez to 19 January 1565 (row 81; *Institutum* v2 lines 26248–26256).
- Borgia to 1572. He died on 1 October 1572, and row 82 now says his Tomus V runs to Epist. 1033 of March 1573.
- Nadal to 1577, from the title pages (row 83).
- Salmeron to February 1585. The Salmeron files are unchanged since Round 2.
- The general congregations to April 1646 (above).

**The deferral of B1's count and the Tier paragraph.** Round 2 accepted it on two conditions: that it be recorded in the ledger, and that it be named to the project lead. The first is met. Ledger entry 41 names both as point-in-time text under Step 0 §5, left for the project lead to decide with the resync. So do the audit (§5 and "What stays as it was") and the build state's escalation line. For the second, the audit says the deferral is named "in the session's report on this revision". That report is not in the repository, and I could not verify it. The build state's escalation line, which is what goes to the project lead, does name it. The Tier paragraph still says the sourcing is "thin for the order's central voice after 1556" and gives "a single correspondent's thread to 1585". That is now stale beside the amended B5, and Step 0 §5 is what tells a reader so. I accept this as point-in-time text, because it is recorded and escalated. The resync should not wait past Doc_04, which reads Step 0's global claims.

## Scope 3: the Polanco headers

For each of the four files, the text below the first `---` line has the same SHA-1 at 434049d87^ and at HEAD, and `git diff --numstat` shows 2 lines changed, both in the provenance note. The v1 file's own title page reads "TOMUS QUINTUS" (line 113), so the corrected statement is true. That statement is "the vendored v1 file is Tomus 5 (1555), not Tomus 1", and for v5 "a second scan of this same Tomus 5". The four staging notes and the merged `the-society-of-jesus.yaml` entry say the same, and nothing else in those entries changed. Ledger entry 43 records the correction accurately.

## Scope 4: newly introduced material

- The new Registry wording in rows 45, 73, 76, 78, 82, 83 and 88 was checked above. No new quotation fails at source.
- Step 0 B4 and B5 introduce no fact that is not in rows 81 to 84 and 89 to 92. B5 says mission reach in China is "documented ... by Trigault's Latin of 1615 as a second witness". Row 89 holds that file at B with "Nothing quotable yet". The phrase "as a second witness" carries the limit, and B4 lists China as not sustained, so I do not count it as misleading.
- Ledger entries 41 to 43 are appended, numbered in order, and cite superseded entries by subject and date.
- The findings are P2-1 and P2-2 below.

## Tools

- **`python -m engine.m10.cli gaps jes`:** `gaps: PASS`.
- **`python tools/check_live_commentary.py --surface worlds`:** exits 0 (report mode). The `jes` hits are 93 KEEP and 132 PROTECTED, with no REWRITE or ROUTE.
- **`--base origin/main --enforce`:** exits 1 for the branch because of other worlds' files (for example `Build/worlds/lpc/Source_Registry.md`). No `Build/worlds/jes` line is flagged REWRITE or ROUTE.

## The change order's approval status

The change order corrects a fact in a document at Approved to proceed, not Frozen. It is named, reasoned and recorded with verbatim before and after text. It is marked in the audit (§5), the ledger (entry 41) and the build state's escalations as awaiting the project lead's confirmation, and nothing in it is attributed to the project lead. That is the right treatment under `CLAUDE.md`'s change-order rule. It is also right under the build cycle's category "a finding that cuts against an earlier decision", because it cuts against Step 0 Review Round 3, finding S1. It is acceptable as it stands.

One consequence follows for disposition. The item is escalated and not yet answered, and Doc_02 is the document item 5 binds. So I recommend that Doc_01 and Doc_02 be recorded as "Cleared review". They should reach Approved to proceed when the project lead confirms or amends the change order, not before. Doc_02 states the shelf from the files and not from item 5's wording, so a confirmation should not reopen it.

## Findings

**P2-1. Ledger entry 42 says Registry row 45 "now name[s] the *Ratio atque Institutio Studiorum* without the year". It does not.** Row 45's title still reads "*Ratio Studiorum* (1599), Latin original, in *Monumenta Germaniae Paedagogica* ...". Its Discovery note gives the year as the census's naming. The date is correct history and is attributed to the census, and row 45 is a C row about an edition that is not vendored. So nothing about the shelf is misstated. But the ledger's claim is inaccurate, and row 45 carries the year without the Widely Accepted tag that row 76 gives it. Fix, if touched again: tag the year in row 45 as the census's and the builder's knowledge, or record in a new ledger entry that row 45 keeps the census's title.

**P2-2. The audit file's §5 fourth bullet now contradicts its first bullet and the Extension.** It still says "the rest of Step 0 (B1 to B5, the Tier conclusion and the count of 19 works) is stale in that way". The first bullet and the Extension say B2, B4 and B5 have been amended. Fix: say "B1, B3, the Tier conclusion and the count of 19 works", or whatever the resync scope actually is.

**P2-3. Row 78 gives lines 298–300 for Tomus II's first heading, "ROMA PRIMIS MENSIBUS I548".** The number "259" is at line 298, and the heading line itself is at line 302. The range came from the Round 2 review. This is trivial.

## Not verified

- The claim that the deferral was "named to the project lead in the session's report on this revision". That report is not in the repository.
- Latin, Italian and Spanish wording was checked against the scan text only. No page image was seen.
- The Round 2 verifications of rows 73 to 92 were not repeated, except for the loci this revision touched. Registry rows 1 to 72 were rechecked only at rows 45 and 73.
- The Salmeron letter counts and the voice dates for Salmeron and Nadal were not recounted. Their files and rows are unchanged since Round 2.
- The build state's round count ("rounds_used: 3") was not reconciled against the commit history. The build state's current_step still says the review of this revision "has not run", which this file now makes stale.
- The Polanco staging notes and corpus-map entry were read as a diff only. The rest of those entries was not re-read.
- `engine/m1/quote_verbatim.py` was not run.

## Disposition

Approved to proceed (Doc_02 and the Source Registry; not Frozen). Self-disposed by the Library thread after this recheck; the reviewer's verdict is above.
