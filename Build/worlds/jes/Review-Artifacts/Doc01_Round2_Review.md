Simulated review — informational only, not an Article 31 substitute.

# Round 2 targeted recheck of Doc_01, Doc_02, the Source Registry, the gap ledger and the Step 0 change order (jes)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Sonnet 5.5 drafting worker (commits 8f55a2285, 82b155536 and 1680579f9; commit trailers read "Claude Sonnet 5.5")
- **Round:** 2 (targeted recheck of the Round 1 P1 findings and of the new material; the first round of a new-material cycle under the project lead's ruling)
- **Truncation check, method 1:** structural count. Doc_01 has headings §1 to §10 in order and ends on its Disposition sentence and a newline. Doc_02 has §1 to §11 in order and ends the same way. The Registry has 92 numbered rows, 1 to 92 with no gap or duplicate, each with exactly 12 pipes; the file table and the saturation statement follow, and the file ends on a complete sentence and a newline. The ledger's numbered entries run 17 to 40 with no gap, after OG-1 to OG-16, and end on a complete sentence. `git diff d040f3c77 HEAD` on the ledger shows no removed line, so it stayed append-only. Step 0 ends on its "Next step" line.
- **Truncation check, method 2:** byte and hash comparison against the committed blobs at HEAD 1680579f9. For all six files `wc -c` equals `git cat-file -s`, and `git hash-object` equals `git rev-parse HEAD:<path>`: Doc_01 7e3c07327e (42,102 bytes), Doc_02 04d88da612 (55,650), Registry a7a77cb5d1 (97,455), ledger 3fd2966309 (41,818), Step 0 776fee7953 (20,891), change-order audit 8d3139bf32 (14,388). None has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/jes/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md` and `Step0_Movement_Scope_Confirmation.md` (§3 B2, §4 item 5), with `Build/Ministry/Operations/Audits/jes_Step0_ChangeOrder_2026-09-30.md` read as a set of claims. Prior findings: `Review-Artifacts/Round1_Review.md`.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** 0 P0, 2 P1, 9 P2.

All four Round 1 P1 findings are fixed at source. The Roman letter counts reproduce by my own two methods. The rites dates carry Inferential/Thin. The Portuguese claim now says only what rows 24 and 30 show. The Ireland report is dated "after 34 days inside Ireland". No `Build/worlds/jes` line fails the enforce gate.

The new material is careful. About 110 quotations and structure markers in rows 73 to 92 were checked against the files, and all but three match. The corpus figures reproduce exactly by two methods. Every new file's printed date is 1930 or earlier. The 1919 *Exercitia* file is the 1919 Madrid volume, not the 1955 Rome volume. The voice-coverage dates hold, with small corrections at the edges. Nothing invented was found, no row rests on a work assigned only to another world, and Article 29, the Representative and the registration of `jes` are still left open.

The two P1 findings are:

- Row 76 dates the *Ratio Studiorum* to 1599 from a note that belongs to a different text. Four other files repeat the date.
- The Step 0 change order is not yet true and complete. Its new B2 summary is wrong about the years after 1585. §3 B5, which item 5 cites, still says the Relations, Ricci and the later Lainez and Polanco volumes are not vendored. And three records still say B2 was not amended.

## Scope 1: the Round 1 P1 findings, at source

| Round 1 finding | Fixed | What I checked in `cic/texts/` |
|---|---|---|
| P1-1, the Roman letters in Salmeron's volumes | Yes | My two methods. Method 1 starts from a capitalised sender heading and requires the next non-blank line to name Salmeron. Method 2 starts from the addressee line and reads the sender line above it. Tomus Secundus: Borgia 49 / 49, Mercurian 86 / 86, Aquaviva 19 / 19, Polanco "ex comm." 12 / 12, Polanco alone 2 / 2. Tomus Primus: Lainez 17 by method 1. Polanco "ex comm." 141 / 144, plus three headings my pattern missed because the scan prints "PÒLANCO", "PÓLANCO" and "POLANGO", so about 144 to 147. The Registry's 17, 49, "about 88 (86 to 89)", "18 to 19" and "146 read in full, 156 with the damaged ones" (about 150) fit these within OCR error. Row 69's samples are right: the 4 March 1565 letter says "et il Padre vicario rimette a V. R. il tutto" (Tomus II line 2422), and the 18 November 1565 heading is "P. FRANCISCUS BORGIA" (line 4697). Doc_02 §1, §2 and §6, rows 67, 69 and 73 and ledger entry 31 carry the corrected counts. |
| P1-2, the rites dates | Yes, by Round 1 option (b) | Doc_01 §2 and §6 and Doc_02 §3, §7 and §8 tag each date Inferential/Thin and name Step 0 §2 A3 as the only basis. Ledger entry 34 supersedes the "no tag" sentence. |
| P1-3a, the Portuguese "royal right" | Yes | No "royal right", "patronage" or "padroado" is left in Doc_01 or Doc_02. Doc_01 §2, §5 and §6 now say that the King asked for men (row 15), that the brief was granted at the King's request (row 24), and that the King was to decide on the Ethiopian party (row 30). |
| P1-3b, the report "from Ireland" | Yes | Row 68 reads the heading "ALATIS CASTRIS 9 APBILIS I542" (Salmeron Tomus I line 2627), and the letter says "estuuimos 34 días dentro della" (line 2644). Doc_01 §2 says "after 34 days inside Ireland". |
| P1-4, the live-commentary gate | Yes for `jes` | `python tools/check_live_commentary.py --surface worlds --base origin/main --enforce` still exits 1, with 412 REWRITE or ROUTE lines on the branch. None of them is in `Build/worlds/jes`. The `jes` files show only KEEP and PROTECTED hits. |

## Scope 2: the new material

### Quotations and loci, rows 73 to 92

A script normalised whitespace, joined line-break hyphens (both "-" and the scan's "¬"), read ſ as s, and looked for each quotation within two lines of the cited range. I read every miss and every short range by eye. These rows match:

- Row 73: the heading, the plural "Rieri riceuemmo", the editors' "ex commissione generalium praepositorum scriptae" and the omitted passages at lines 1033–1035. The exception is at P2-3.
- Row 74: all five quotations, and the dating clause "Datum Romae, apud S. Marcum", "anno Incarnationis Dominicae mdxl", "quinto kal. Octobris" (lines 2177–2179). The Formula's introduction sits at 1789–1790, not 1788–1789, which is harmless. The bull's day of 27 September is rightly settled as Documented.
- Row 75: every congregation date, including "Is 12 Aprilis 1573 … dixit 23 Aprilis" (31422–31425), Aquaviva's election on 19 February 1581 (35924–35926), Vitelleschi's on 15 November 1615 (48587–48589), Carafa's on 7 January 1646 (54078–54079), and decree 42's "pro directione tantum et sine ulla obligatione".
- Row 76: the Ratio heading (24940), the Provincial's first rule (24963–24968) and the index entry for Aquaviva's instruction (497). The instruction's text heading at 46511 reads "INSTRUCTIO DE SPIRITU AD SUPERIORES", without Aquaviva's name. The 1599 note is P1-1.
- Row 77: the title and "Messanensi opera et studio Hieronymi Natalis, rectoris".
- Row 78: the preface's "summariis sive compendiis", and the end-points 29 March 1550, 29 November 1551, 12 April 1553 and 15 May 1554. The exceptions are at P2-2.
- Row 79: the Spanish and Latin Principle and Foundation.
- Row 80: the Acta heading, the Pamplona sentence, and the Portuguese prologue at 7171.
- Row 81: the first letters of Tomi 2 and 3, Epist. 2059 of 25 April 1564, Epist. 2230 of 19 January 1565, "diem obiit supremum" and "postridie mortis Lainii".
- Row 82: every heading named. The exception is at P2-2.
- Row 83: every title page.
- Row 84: every marker, and "Initio hujus anni octo Provincias distinctas habebat" at line 144 of the v1 file and line 94 of the v5 file (ledger entry 38).
- Rows 85 and 87: every quotation.
- Row 89: "Liber primus" and "Capvt Primvm".
- Rows 90 to 92: all 27 volume markers I tested, and the three English quotations in Vols. 5, 12 and 34. The Vol. 30 marker's scan reads "HuRONS", not "Hurons", which is trivial. The Huron instruction is printed in Le Jeune's Relation of 1637 (Vol. 12, running head at line 4530), so "the instruction of 1637" in Doc_01 §5 holds.

The misses are at P1-1 (row 76), P2-1 (row 88) and P2-3 (row 73).

### Rights

Every one of the 87 assigned files carries "Rights: Public Domain" in its header, and every printed date is 1930 or earlier. The latest are the *Exercitia* of 1919 and Lainez Tomus 8 of 1917. Three details:

- The Lainez Tomus 3 header takes 1912 from the archive record, because its title-page year is not legible.
- Three Relations headers give the series range 1896–1901, because the volume's own year is not legible.
- The drafter's flag is right. The *Exercitia* header says the item `monumentaignatia02igna` carries an archive date of 1919 but a title page of Rome, 1955, and that it is not vendored. The vendored file's title page reads "MATRITI … 1919", with a library stamp of July 1921. The only later four-digit numbers in its body are column references (for example "t. VII 1963" in a Sommervogel citation). No text of the 1955 edition is on the shelf.

### Witness status of garbled scans

The corpus map and Doc_02 §1 agree on six second witnesses: the 1606 Constitutions, the 1595 *Adnotationes*, Ribadeneira's 1572 life, Trigault's 1615 Latin and Canisius's Latin of 1565 and 1573. Rows 88 and 89 hold the last three at B, with "Nothing quotable yet". No Latin quotation in rows 73 to 92 comes from a second witness. The Relations' English quotations are Thwaites's translation, and rows 90 to 92 say so. The corpus map says to quote the French only after a check against the page image, and no French is quoted.

### Vendored and not-vendored statements

Every file named in the Registry's file table exists and is in `the-society-of-jesus.yaml`. Every C row that says "Not vendored" (rows 39, 40, 43, 46, 52 to 63, 65, 66 and 71) has no matching file. The rows now vendored (41, 47 to 51, 64 and 72) name the row that holds the file. Tomus IV and Tomi VII to XII of the Ignatius letters, Borgia Tomi I and II, Polanco Tomi 1 and 3, and Relations volumes 36 and later have no file. Doc_01 and Doc_02 are right on every point. Step 0 is not (P1-2). One citation slip in Doc_02 §1 is at P2-6.

### Letter counts

See Scope 1 for both methods. Every count stated in the files falls within my range. The one exception is "154" for Polanco by the drafter's method B (audit, fact 3), which appears nowhere in the live files and which I did not try to reproduce.

### Voice-coverage dates

| Claim | Finding at source |
|---|---|
| Ignatius to 15 May 1554, gap December 1551 to March 1553 | Holds. Tomus III ends 29 November 1551 (line 25692). Tomus V's first dated heading is no. 3315, of 12 April 1553 (line 352). Tomus VI's last heading is "ROMA 15 MAJI 1554" (38194). No Tomus IV file exists. |
| Lainez to 19 January 1565 | Holds (Tomus 8, line 18239). |
| Borgia to 1572 | Holds for his life. He died on 1 October 1572 (*Institutum* II, 31417–31419). His Tomus V runs past his death (P2-2). |
| Nadal to 1577 | Holds by the title pages. The Tomus III preface says the letters run to December 1577 (line 115). |
| Salmeron to February 1585 | Unchanged since Round 1, and the Salmeron files are unchanged. |
| General congregations to January 1646 | Carafa's election is 7 January 1646, but the eighth congregation's decrees run to 14 April 1646 (P2-5). |
| Relations 1610–1650 | Holds, from Vol. 1 "ACADIA: 1610- 1613" (197) to Vol. 35 "… 1650" (162). |

### Corpus figures

In `LC_ALL=C.UTF-8`, the sum of Python `len()` over the 87 decoded files is 106,104,896, and `cat | wc -m` gives the same. Python `split()` gives 15,791,624 words, and `wc -w` gives the same. The C-locale figures of 106,884,350 bytes and 15,674,468 words reproduce too.

I also recomputed each breakdown from the file list, and every one reproduces:

- Latin: 44 works, 82,704,760 characters (77.9 per cent).
- Relations: 35 works, 17,167,309 (16.2 per cent).
- English: 8 works, 6,232,827 (5.9 per cent).
- Context role: 5 works, 7,349,462.
- Second witnesses: 6 works, 6,000,525 (5.7 per cent).
- MHSI and Bouix: 34 files, 67,925,291 (64.0 per cent).

The shelf has 396 text files (358 `.txt`, 38 `.xml`) and 403 entries, as stated.

## Scope 3: the Step 0 change order

Item 5, as re-derived, is true against the files on every point I tested except "to January 1646" (P2-5) and "the *Ratio Studiorum* of 1599" (P1-1). The audit file's facts 1 to 5 agree with the files, and its section 6 now records the choice-box answer for `jes`, which answers Round 1's "Not verified" point. The extension to §3 B2 is not yet right (P1-2).

**Whether leaving B1's count and the Tier paragraph as point-in-time text is acceptable.** For B1's count of nineteen works and the Tier paragraph, yes, on one condition. Step 0 §5 already says that a vendoring pass leaves the document stale until it is resynced, so older figures there do not mislead a reader who reads §5. The condition is that the deferral is recorded in the ledger and named to the project lead. At present it is recorded only in the audit file's closing paragraph. For B5 and B4, no. Item 5 is binding, and it opens "Per §3 B2/B5". B5 still says "nothing is vendored on Ricci, de Nobili, or the Jesuit Relations" and "Lainez's volume ends in 1556 and Polanco's covers only 1555". Those are statements about the shelf, and they are now false. A binding item cannot rest on a section that contradicts it.

## Scope 4: conduct, tags and tools

- **Nothing invented.** No new claim was found without a row or a stated basis. Two dates on the shelf disagree, 23 and 29 April 1573 for Mercurian's election (*Institutum* II 31425; Salmeron Tomus II line 543, "Die 29 Aprilis 1573"). Both are read correctly, and the day is tagged Contested. That is conservative and right.
- **Tags.** The bull's day is Documented from the dating clause. The strand finding stays Inferential/Thin. The confidence letters of rows 82 and 83 are a little generous (P2-4).
- **Cross-world rows.** None. Every Registry file is assigned to `jes`.
- **Left open.** Article 29, the Representative and the registration of `jes` are open in Doc_01 §9. The change order is still recorded as awaiting the project lead's confirmation (audit §5; the build state's escalations).
- **The strand finding.** It is still honest. Doc_01 §5 now adds the Huron instruction to the case for two strands, and it says the Relations "have not been read for it". Doc_04 is told to test them first.
- **Process narration.** None found, except "the volumes now vendored" in Doc_01 §9 item 9 (P2-9).
- **`python -m engine.m10.cli gaps jes`:** `gaps: PASS`.
- **`python tools/check_live_commentary.py --surface worlds`:** exits 0 (report mode). The `jes` hits are KEEP (the Registry's Added and Discovery cells, and Doc_02 line 300) and PROTECTED.
- **`--base origin/main --enforce`:** exits 1 for the branch. No `Build/worlds/jes` line is flagged.
- **Readability** (`engine.m7.turn_readability.score_turn`, markdown and code spans stripped):
  - Doc_01 scores FRE 61.1 and FK 7.5.
  - Doc_02 scores FRE 58.4 and FK 7.6. The drafter's method gives 58.9. The engine reports "FRE 58.4, below the floor of 60".
  - Doc_02's lowest sections are §9 (50.3), §2 (55.8) and §8 (55.7). See P2-8.

## Findings

**P1-1. Row 76 takes the 1599 date of the *Ratio Studiorum* from a note that belongs to another text.** The row says: "A note says the rules were sent to the provinces by Aquaviva, 'anno demum 1599' (line 50520)."

Line 50520 belongs to Instruction IX, "DE MODERATIONE IN DANDIS LITTERIS AD GENERALEM ADHIBENDA" (lines 50516–50518). That is Aquaviva's instruction on restraint in writing letters to the General, and it is "anno demum 1599 aucta copiosius, ad Provincias missa" (50520–50522). The only other "1599" in the volume (50953) is also an Aquaviva instruction. The Ratio begins at 24940 with no printed date, and the volume's summary lists it as "Ratio studiorum . pag. 158" without a year (line 89).

The date of 1599 is right as history, but the shelf locus given for it does not support it. On an A row that is a sourcing error. The date is carried as a shelf fact in:

- Doc_01 §3, candidate 6 ("the shelf holds the *Ratio Studiorum* of 1599");
- Doc_02 §6, point 4;
- Step 0 §3 B2 and §4 item 5;
- ledger entry 37 ("the text of 1599 is in the *Institutum*").

Fix: correct row 76's note. Then either find a locus on the shelf that dates the text, or state the year as the builder's knowledge with a tag, as Round 1 P2-13 asked for the beatification year. Carry the result to the four places above. The ledger fix is a new entry.

**P1-2. The Step 0 change order is not yet true and complete.**

- **(a) The new B2 summary is wrong.** It reads: "A fair summary: dense to 1565, partial to 1585, and a single correspondent's thread after that." After February 1585 there is no correspondent's thread at all. B2's own previous sentence ends Salmeron's letters in February 1585, and item 5 says the same. A true summary would say something like: dense to 1565; the letters of Borgia, Nadal and Salmeron to 1572, 1577 and 1585; and after 1585 only the congregations' decrees and the *Institutum*.
- **(b) B2's first sentence is stale.** It still lists "Polanco's *Chronicon* (Tomus V, 1555 only)" among the vendored works. Tomi 2, 4 and 6 are now vendored too (row 84).
- **(c) B5 is false, and item 5 cites it.** B5 says "Lainez's volume ends in 1556 and Polanco's covers only 1555" and "nothing is vendored on Ricci, de Nobili, or the Jesuit Relations". Rows 81, 84, 89 and 90 to 92 show otherwise. B4's "not its missionary/global reach" is stale in the same way, because the Relations are the order's own mission reports.
- **(d) The records disagree with the file.** Ledger entry 36 still says "Step 0 §3 B2 and B5 and the Tier conclusion are not amended". The audit's §5 still says "It does not amend Step 0 §3 B2". The build state's escalation still says "applied to item 5 only". All three predate commit 1680579f9, and no ledger entry records the B2 extension. The audit's appended "Extension" paragraph contradicts its own §5.

Fix, as a named extension of the same change order, still for the project lead's confirmation:

- correct the B2 summary and its Polanco clause;
- bring B5, and B4's mission clause, into line with item 5;
- add a ledger entry that records the extension, supersedes entry 36's sentence, and names the B1 count and the Tier paragraph as point-in-time under §5 (Scope 3);
- bring the audit's §5 and the build state into line.

**P2-1. Row 88 gives a locus that is not in the 1565 file.** The row says: "The 1565 scan has the dedication signed 'Petrus Canijiuf' at lines 50–58." Those lines are title-page debris, and "Canijiuf" does not occur in the file. The 1565 scan names "tro Canifio Theologo" at line 67 and prints "M. D. LXV" at line 96. The 1573 signature at line 348 is right.

**P2-2. Three end-points in rows 78 and 82 are off.**

- Tomus II of the Ignatius letters begins with no. 259, "ROMA PRIMIS MENSIBUS I548" (lines 298–300), not with nos. 264 and 265.
- Tomus V's last heading is "ROMA 28 MOVKMBRIS 1553" (line 40070), not 23 November.
- Borgia Tomus V runs past Epist. 1028 of 18 October 1572 to Epist. 1033, "MENSE MARTIO I573" (line 37385). Epist. 1028 reports his death ("rese 1' anima al suo creatore" in the scan, lines 37105–37106), so the row should say that the volume ends with letters about his death.

**P2-3. Row 73 silently corrects a heading.** It quotes "P. JOANNES DE POLANCO EX COMM." at line 9710. The scan reads "P. JOAÑNES DE PÒLANCO EX COMM." The Registry's own rule is that no letter of a quotation is corrected. Either quote the scan's reading or cite line 9108, which reads exactly as quoted.

**P2-4. The confidence letters are calibrated unevenly.** Rows 82 and 83 carry A although "Only headings were read" and "Only the title pages and headers were read". Rows 86, 88 and 89, on the same kind of reading, carry B. The Registry defines A as reading the Licensed-For passages. Either narrow the Licensed-For of rows 82 and 83 to coverage by date, which the headings do show, or grade them B.

**P2-5. "To January 1646".** Step 0 §3 B2 and item 5, ledger entry 36, and Doc_02 §1 (the table and the bullet on the *Institutum*) end the decrees in January 1646. The eighth congregation elected Carafa on 7 January 1646 and ran to 14 April 1646 (*Institutum* II 54078–54082). Doc_02 §6 point 4 already says "1645–46". Say "to April 1646", or "to 1646".

**P2-6. Doc_02 §1, "What is not on the shelf", cites row 48 for missing volumes.** Row 48 is the later Lainez volumes, which are all vendored. The missing Borgia and Polanco volumes are rows 47 and 50. Mercurian and Aquaviva have no row, so say that plainly.

**P2-7. The Registry's shelf-search count of 144 cannot be reproduced from the pattern as written.** The pattern is given as "`Societatis Iesu` or `Jesu`". Read as `Societatis [IJ]esu`, the search gives 135 files and misses four assigned files. Read as the whole word `Jesu`, it gives 204 files and misses exactly the two assigned files named (Canisius 1622 and Trigault 1615). Read as the substring `jesu`, it gives 291. The "85 of 87" reproduces only with the whole word. Give the exact pattern, or the command.

**P2-8. Readability.** Doc_02 improved from 56.4 to about 58.5, but it is still under 60. Doc_02 is a construction document for builders and reviewers, not participant-facing prose, so under the `hus` precedent and Round 1 P2-14 this is a P2 and not a block. The search record (§9) and the Transmission History entries in §2 are still the place to split sentences. Both documents also score FK 7.5, and the engine marks that below its grade-8 floor. The rule in `CLAUDE.md` treats grade 8 as a floor for participant-facing text, so this is noted for Doc_09 and later, not for these documents.

**P2-9. Doc_01 §9 item 9 says "the volumes now vendored".** "Now" narrates a change inside a live file. Say "the vendored volumes".

## Not verified

- Latin, Spanish, Italian and French wording was checked against the scan text only. No page image was seen.
- Row 81's volume ranges for Tomi 4 to 7 were not checked, beyond the fact that the files exist. Nor were the Nadal volumes' letters themselves, or the dates of the Generals' ordinances in *Institutum* III.
- My own letter counts come from OCR headings, and my patterns miss some accented or damaged headings. They support the stated figures only within a few letters. I did not reproduce the drafter's method-B figure of 154 for Polanco.
- Registry rows 1 to 72 were rechecked only where the revision touched them (rows 16, 45, 63, 67, 68, 69 and the not-vendored notes). The Round 1 P2 findings were not rechecked one by one, except where they touch the new material.
- The rites dates (1623, 1627–28, 1645) and Relations volumes 36 to 73 were not tested against any source. None is on the shelf.
- I did not run `engine/m1/quote_verbatim.py`. The quotations were checked by my own normalising script and by eye.

## Outside this scope, noted only

- The enforce gate's flagged lines include six REWRITE lines in `Build/worlds/_cross-world/dossiers/the-society-of-jesus_Source_Readiness_Dossier.md` (lines 10 and 50–54). That file was last edited on this branch by the Library commit c11c0801b, not by this revision.
- The working tree has an uncommitted change to `Build/worlds/hus/Source_Registry.md`. It is not part of this review.
