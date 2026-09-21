# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 7 Independent Adversarial Review

**Documents reviewed:**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_02_Source_Ecology.md` (current revision, commit `dfe085b6`)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Registry.md` (same revision — 98 rows)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Acquisition_Manifest.md` (same revision — G1–G8)
- and, for the post-disposition edits it has now received and the disclosure record attached to them, `Doc_01_World_Identification_Boundaries_Orientation.md` lines 3 and 186, together with `lpc_Decision_Log.md` (all nine entries)

**Review date:** 2026-09-02
**Reviewer:** independent adversarial review thread. Did not draft any of the three documents, did not draft this world's Step 0, Doc_01, or any prior revision, and did not write Rounds 1–6 of this document set. **Rounds 1 through 6 were read in full and treated as claims to be re-derived, not as authority** — including Round 6's own "What was checked and found clean" section, which is re-checked here rather than carried forward. Every commit touching `Doc_01_World_Identification_Boundaries_Orientation.md` since its self-disposition was enumerated directly with `git log --follow`, not read off the document's own count. The Registry's 98 rows were extracted programmatically (row numbers, pipe-count-per-row, physical order). The vendored `codex-theodosianus_latinlibrary.txt` file was checked directly against `cic/texts/README.md`, `cic/engine/texts_registry.py`, and its own header. The sibling Donatism build's branch was re-fetched this session and found to have moved twice past Round 6's own snapshot.

**Governed by:** `cic-build-cycle` (CO-022), read in full at the live skill this session; Construction Framework V7.4's Doc_02 review requirement (the ten-item relative-recall test and the PRESS question, quoted verbatim in the recall-test section below); `Source_Registry_Template.md` V1.0, read directly at `L3B-World-Build-Methodology/Source_Registry_Template.md` rather than assumed; `cic/texts/README.md` and `cic/engine/texts_registry.py`, both read and the latter run directly this session; `Doc_01_World_Identification_Boundaries_Orientation.md`; `lpc_Decision_Log.md` (all nine entries, read in full); `Review-Artifacts/Doc02_Round1_Review.md` through `Doc02_Round6_Review.md`, all six read in full.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 2 MEDIUM · 3 LOW · 1 COSMETIC.**

**Four things should be said before the findings.**

**First: no historical, bibliographic, or primary-source claim was falsified this round.** Every load-bearing quotation I re-checked at source still holds — Epistle XXXIX (not Epistle XL) carries "your suffrage and God's judgment" and "ancient venom," confirmed directly against `anf05_hippolytus-cyprian-caius-novatian.xml`; the patrimony sentence at `npnf104`'s Book III ch. 2 §2 (`div4 id="v.iv.v.ii"`) is present and reads as claimed. The Registry's structure is clean: 98 rows, 1–98, no duplicate, no gap, every row a consistent 11-column table row, verified programmatically rather than read by eye. The vendored `codex-theodosianus_latinlibrary.txt` file (Registry row 88) contains all 16 `LIBER` headings in order, exactly as `cic/texts/README.md`'s own entry claims, and its rights basis and edition-provenance gap are disclosed accurately in both the file's own header and the Registry row. Running `cic/engine/texts_registry.py` directly, the seven "problem" entries it reports (undeclared-vendoring files, zero-citation files) all belong to other world-builds' vendored texts, not this one's — this world's own entry is clean. **This is the third consecutive round with no falsified substantive claim.**

**Second: the structural remedy Round 6 diagnosed and applied — replacing a maintained enumeration with a stated rule pointing at the table — is holding up cleanly everywhere it was actually applied.** The priority-flag section (Registry §"Priority second-opinion review flags"), the Manifest's §3 never-vendored list, and Doc_02 §9 item 3's verification-status index were all converted from row-range lists into rules last round. I checked each rule against the current 98-row table, including the ten rows added since (89–98): all three rules resolve correctly against every row they reach, with no mislabelled row and no stale range. **Where Round 6's own diagnosis was applied, it worked, for a second round running.**

**Third: the same diagnosis was not applied everywhere the same fragility exists, and two of those un-remediated spots produced this round's own findings — one of them the fourth occurrence of a defect three prior rounds already thought they had fixed.** Doc_01's post-disposition edit count is wrong again: it says four, `git log --follow` shows five, and the fifth is the very commit that wrote "four" — the count did not account for its own act of being written. This is the same miscount Round 4's L3, Round 5's M8, and Round 6's M2 each already found and corrected once; each fix held for exactly one round before the next post-disposition edit reintroduced it. Separately, `lpc_Decision_Log.md`'s own entry declaring that its directional pointers ("above," "below," "the next entry") "are being retired in favor of dating and content description" is false in the same sentence that makes the claim — it uses "above" twice — and false again in the two entries appended immediately after it, which use "the entry above" three more times without qualification.

**Fourth: two placement notes that were never converted to the structural remedy went stale a further time, in the same commit that added the ten rows that made them stale.** Row 60's own placement note at line 71 still reads "sits after row 70 below" — the exact sentence Round 6's own L7 quoted and asked to be corrected — while a second, separately-worded note about the same row, added to answer L7, itself now understates the row's position by seventeen further rows, since rows 89–98 were inserted below it in the same commit that touched neither note to account for them.

---

## Method — what was actually checked

- **`git log --follow` run directly on `Doc_01_World_Identification_Boundaries_Orientation.md`**, not read off its own status line's count. Five commits found after its self-disposition (`ef3e255a`): `4796ee34`, `252a0dd7`, `ce8246f2`, `8360e103`, `10ce5efc`. `git show --stat` run on the two most recent repository commits (`10ce5efc`, `dfe085b6`) to confirm which files each actually touches; `dfe085b6` does not touch Doc_01. `git show` diffs read hunk-by-hunk for `10ce5efc`'s and `8360e103`'s changes to Doc_01's status line and §9 note, to establish what each commit actually changed rather than trusting either commit's own description of itself.
- **`Source_Registry.md`'s 98 rows extracted programmatically**: row numbers 1–98 complete, no duplicate, no gap; every row's pipe count checked against the 11-column header (12 pipes expected; none deviated).
- **`Source_Registry_Template.md` V1.0 read directly** at `L3B-World-Build-Methodology/Source_Registry_Template.md` (not assumed from memory or from what the Registry itself claims the Template says): the Type/Confidence axes, the binary Boundary Check, the Exclusion Reason table, the Licensed-For requirement, the append-only living-document protocol, and the re-keyed priority-review trigger were all checked against the Registry's actual practice. No violation found (Confidence E does not appear anywhere in the table; every Excluded row carries Out-of-Boundary or Named Comparandum; every Native row states something in Licensed-For, even where that something is a disclosed absence of one).
- **`cic/texts/README.md` and `cic/engine/texts_registry.py` read, and the latter run directly this session** (`python3 cic/engine/texts_registry.py`). Row 88's vendored file confirmed present on disk (1,782,548 bytes, 7,500 lines), its 16 `LIBER` headings located and confirmed in order by direct grep, and its header text read in full against the Registry row's and Decision Log's own description of it.
- **The Decision Log read in full, all nine entries, checked for internal chronological order and for whether its own stated editorial practice (retiring directional pointers) is actually followed in the entries that come after the sentence stating it.** Grepped for "above," "below," "next entry," "entry above," "most recent entry" across the whole file.
- **`Source_Acquisition_Manifest.md` read in full**, its G1–G8 entries cross-checked against the Registry rows each claims to correspond to, and its own summary sentence (line 15) checked against each individual G-entry's own stated origin.
- **The sibling Donatism build's branch re-fetched this session** (`origin/claude/record-native-world-build-v2-e2s0dt`), found at `7a675068`, two commits past Round 6's own snapshot (`8a2f4ae6`). The new commits checked directly: one is a Doc_03 draft (does not touch the Registry rows this world cites), the other corrects the sibling's own row 37 (an unrelated numbering namespace — this world cites the sibling's rows 1, 4, 16, 24, and 48, none of which the new commit touches). The sibling's own G3 (*Codex Theodosianus*) status re-read at the new head and found unchanged from Round 6's account.
- **Ten fresh recall-test items and the PRESS question**, composed from six instruments none of Rounds 1–6 used, verified against live web search this session (publisher, series, year, and — where relevant — public-domain status and hosting), and checked by grep against all three documents plus the full 98-row Registry to confirm none is already named.

---

## HIGH

**None.** Third consecutive round with no falsified historical or bibliographic claim. Every claim the prior rounds' findings turned on was spot-checked at source this round (Epistle XXXIX/XL, the Book III ch. 2 §2 patrimony sentence, the vendored *Codex Theodosianus* file's structural integrity) and each holds.

---

## MEDIUM

### M1. Doc_01's post-disposition edit count is wrong again — it says four, `git log --follow` shows five, and the fifth is the commit that wrote "four"
`Doc_01_World_Identification_Boundaries_Orientation.md` line 3 (status line) and line 186 (§9's post-disposition note).

The current status line reads: *"Post-disposition corrections, recorded here per CO-022's own disclosure requirement — **four** of them (count corrected here, Round 6's own M2, from an earlier draft that named three; identified below by what each one changed rather than by a Decision Log entry number...)"* and lists four items: (1) the Ep. XL→Epistle XXXIX citation fix, (2) the stale round-count fix, (3) *"this status line and §9's own post-disposition note (below) were corrected once, describing edits (1) and (2)"*, (4) *"this status line and §9's own post-disposition note were corrected **a second time**, to state this current count of four and drop the numbered Decision Log pointers that kept going stale."*

`git log --follow` on this file, run this session, returns **five** commits after the 2026-09-01 self-disposition (`ef3e255a`): `4796ee34`, `252a0dd7`, `ce8246f2`, `8360e103`, `10ce5efc`. Comparing each commit's actual diff to Doc_01:

| # | Commit | What it changed in the status line / §9 note |
|---|---|---|
| 1 | `4796ee34` | Ep. XL → Epistle XXXIX (item 1) |
| 2 | `252a0dd7` | "all eight rounds" → "all nine" (item 2) |
| 3 | `ce8246f2` | First introduced the "post-disposition corrections" framing, describing two edits (matches item 3's "corrected once, describing edits (1) and (2)") |
| 4 | `8360e103` | Rewrote the note from "two" to "**three**," adding a new self-referential item 3 and renumbered Decision Log pointers ("second," "fourth," "sixth" entry) |
| 5 | `10ce5efc` | Rewrote the note from "three" to "**four**," replaced the item-3 wording again (now describing `ce8246f2` instead of itself), added item 4, and dropped the numbered pointers |

Item (4)'s text — *"corrected a second time"* — describes only one correction between item (3) and the current state. In fact there were **two**: `8360e103` (two→three) and `10ce5efc` (three→four), each a distinct commit with its own diff to this exact paragraph. `10ce5efc`'s own edit silently absorbed `8360e103`'s edit into itself, so the enumeration describes five real commits with only four items, one of which stands in for two.

This is the same defect Round 4's L3 (one→two), Round 5's M8 (two→three), and Round 6's M2 (three→four) each already found and corrected once. Each correction held for exactly one further commit before the next post-disposition edit went uncounted — and this time, the miscount is built into the very commit that was written to fix the prior round's miscount, because writing "the count is now N" is itself the (N+1)th edit and nothing in three successive fixes has accounted for that self-reference. §9's post-disposition note (line 186) carries the identical bug in parallel wording: *"the status line and this note were then corrected **twice more**, first to describe those two edits and then to state the current count of four"* — again collapsing `8360e103` and `10ce5efc` into one step ("then to state...four") when they are two distinct commits.

**Required:** state five, enumerate the fifth (`10ce5efc`, the commit making this very correction — an inherently self-referential item, since the correction is itself the edit being counted), or adopt a form immune to this self-reference (e.g., "N edits before this one; this correction is not counted as a further edit since it corrects the count rather than the document's substance" — a distinction CO-022's own *Coach verification* exception already draws for non-substantive corrections, and one this note has never yet invoked for itself).

### M2. The Decision Log's own claim that it has retired directional pointers is false in the sentence that makes it, and in the two entries added after it
`lpc_Decision_Log.md` line 89 (the claim); lines 77, 103, 105, 111 (the violations).

Line 89, closing the entry titled *"Two more Decision Log pointer/count defects found by Round 6"*: *"**The two entries above** are now in chronological order... This log's own directional language ('above,' 'below,' 'the next entry,' 'the most recent entry,' 'the entry after this one') **is being retired** in favor of dating and content description, for the same reason."*

The sentence declaring retirement uses "above" itself, to refer to the two entries it has just reordered. That is arguably transitional wording inside the entry making the change. What is not transitional: the entry immediately preceding it, corrected **by** this same commit (per its own heading note), still reads at line 77: *"an earlier version of this heading called this Doc_01 edit 'the third post-disposition' one, which **the very next entry below** found was, in the same commit, also said of a different edit."* And the two entries appended **after** line 89's retirement claim — both dated the same day, both part of recording the *Codex Theodosianus* vendoring — use the identical pattern three more times:

- Line 103 (heading): *"...closing the gap **the entry above** left open."*
- Line 105 (Context): *"Discussing **the entry above's** own OTA/CC-BY-NC-SA gap..."*
- Line 111 (Escalation check): *"...the same project-lead resource decision **the entry above** records..."*

None of these three is flagged as a deliberate exception; each reads as ordinary, unselfconscious use of the exact pointer form the log had just, two entries earlier, declared itself to be retiring "for the same reason" the reordering was needed. If the log is ever reordered or another entry inserted between these — which is exactly the failure mode that has already happened twice (Round 5's insertion, Round 6's correction of it) — "the entry above" in three separate places will silently point at the wrong entry again, which is precisely the staleness this log's own retirement clause exists to prevent.

This is not a factual error about the world's history or sources — it is the Decision Log's account of its own current editorial state being wrong, the same class of self-referential defect Round 6's M3 and M4 addressed for this same file. It recurs here for a further, seventh consecutive round in which some part of this log's own account of itself needed correction, this time inside the entries added to correct the sixth occurrence.

**Required:** replace "the entry above" (lines 103, 105, 111) and "the very next entry below" (line 77) with named-heading or dated pointers, consistent with what line 89 already claims has been done; or narrow line 89's own claim to describe only the two specific entries it actually applied to, rather than stating a general retirement that the file's own next two entries contradict.

---

## LOW

**L1.** `Source_Registry.md` line 71 — **Round 6's own L7 remains unfixed at its original site.** The note reads: *"row 60, added in the same pass, **sits after row 70 below** (rows 61–87 were inserted between 59 and 60)."* Row 60's actual table row is at line 133 — physically after all of rows 61–98, not merely row 70. This is the exact sentence Round 6's L7 quoted as wrong and asked to be corrected; it is byte-identical to how Round 6 found it. A second, separately-worded note about the same row's placement (line 131: *"physically after rows 61–87"*) was added at Round 6 and is more accurate, but it does not replace or correct line 71 — the file now carries two different claims about where row 60 sits, one of them still the one Round 6 flagged as wrong.

**L2.** `Source_Registry.md` lines 131 and 135 — **the two placement notes added or touched at Round 6 were not extended to the ten rows (89–98) added in the same commit.** Line 131: *"Row 60, created at Round 3, sits here — physically after rows 61–87..."* Line 135: *"Row 52 continues to sit here, physically after rows 53–87 and after row 60 above..."* Both rows (60 at line 133, 52 at line 137) physically sit after rows 89–98 (lines 118–129) as well, since those ten rows were inserted between rows 87/88 and row 60 in the very commit that produced or last touched both notes. Neither note is false about the ordering it does state (60 and 52 are indeed both after 61–87), but both now understate the gap by ten further rows, in the same commit that created the gap — the same un-extended-enumeration pattern Round 6 diagnosed and fixed for the priority-flag section, the Manifest's §3 list, and Doc_02 §9 item 3, but never applied to these two placement notes, which remain hard-coded row-range prose rather than a rule.

**L3.** `Source_Acquisition_Manifest.md` — Round 6's M8 suggested, in its own words, *"consider carrying [the sibling build's] source-integrity warning into this world's Manifest"* — the sibling's own on-record warning that a site calling itself "sourcelibrary.org" delivered a file carrying "a systematic invisible Unicode payload" and "should not be used for any future acquisition." That suggestion was not taken up: this world's Manifest still routes the project lead to open-web searches for G6's and G8's own missing Internet Archive identifiers (§1's network-access-limitation paragraph) with no comparable warning anywhere in the document. Round 6 phrased this as a suggestion ("consider"), not a required fix, so this is not counted as an unaddressed MEDIUM finding — but the operational risk it names is real, on this document set's own record (via the sibling branch), and remains unpropagated into the document that actually sends the project lead onto the open web.

---

## COSMETIC

**C1.** `Source_Acquisition_Manifest.md` line 15 — **the summary sentence misattributes G8's own origin.** It reads: *"G7 and G8 added this revision, per Round 6's own PRESS answer 1 disposition instruction."* G8's own entry, two paragraphs below (line 31), correctly states: *"**Added this revision (Round 6's own recall-test item 2).**"* G7 (row 89) is indeed PRESS answer 1; G8 (row 90) is recall-test item 2, a different disposition from a different part of Round 6's own review. The summary sentence conflates the two origins for both candidates it introduces.

---

## Ten-item relative-recall test

Composed fresh this round from six instruments none of Rounds 1–6 used: **Subsidia Hagiographica / the Bollandist Society's own reference publications**, **Studia Patristica Supplements** (Peeters), **Oxford Studies in Historical Theology** (Oxford University Press), **Women in Antiquity** (Oxford University Press), **The Fathers of the Church: A New Translation** (Catholic University of America Press), and the **Journal of Roman Archaeology Supplementary Series**. All 43 works Rounds 1–5 named and the further 10 works Round 6 named (53 total, all now rowed or excluded at rows 30–98) were excluded from consideration before this list was built, and the ten below were separately grepped against the current text of all three documents and the full 98-row Registry table before being counted as new. Every item was verified this session by live web search against publisher, series, and catalogue records.

| # | Work | In Registry? |
|---|---|---|
| 1 | Hippolyte Delehaye, *Les Passions des martyrs et les genres littéraires*, Subsidia Hagiographica 13b (Brussels: Société des Bollandistes, 1921; 2nd ed. 1966) | **No** |
| 2 | *Bibliotheca Hagiographica Latina antiquae et mediae aetatis*, ed. Socii Bollandiani (Brussels: Société des Bollandistes, 1898–1901; *Supplementum*, 1911; *Novum Supplementum*, ed. H. Fros, Subsidia Hagiographica 70, 1986) | **No** |
| 3 | Charles A. Bobertz, *Cyprian of Carthage: Priest and Patron*, Studia Patristica Supplements 12 (Leuven: Peeters, 2023) | **No** |
| 4 | Michael Cameron, *Christ Meets Me Everywhere: Augustine's Early Figurative Exegesis*, Oxford Studies in Historical Theology (Oxford: Oxford University Press, 2012) | **No** |
| 5 | Gillian Clark, *Monica: An Ordinary Saint*, Women in Antiquity (Oxford: Oxford University Press, 2015) | **No** |
| 6 | Sister Rose Bernard Donna (trans.), *St. Cyprian: Letters (1–81)*, The Fathers of the Church 51 (Washington: Catholic University of America Press, 1964) | **No** |
| 7 | Roy J. Deferrari et al. (trans.), *Saint Cyprian: Treatises*, The Fathers of the Church 36 (Washington: Catholic University of America Press, 1958) | **No** |
| 8 | Sister Wilfrid Parsons (trans.), *Saint Augustine: Letters*, The Fathers of the Church 12, 18, 20, 30, 32, 5 vols. (Washington: Catholic University of America Press, 1951–1956) | **No** |
| 9 | Susan T. Stevens, Angela V. Kalinowski, and Hans Vanderleest, *Bir Ftouha: A Pilgrimage Church Complex at Carthage*, Journal of Roman Archaeology Supplementary Series 59 (Portsmouth, RI: JRA, 2005) | **No** |
| 10 | Susan T. Stevens, *Bir el Knissia at Carthage: A Rediscovered Cemetery Church*, Report No. 1, Journal of Roman Archaeology Supplementary Series 7 (Ann Arbor: JRA, 1993) | **No** |

**Recall = 0/10.** Checked by case-insensitive grep across all three documents and the full Registry table on author, title, and series forms ("Delehaye," "Bollandist," "Bobertz," "Cameron," "Monica: An Ordinary," "Fathers of the Church," "Bir Ftouha," "Bir el Knissia," "Bibliotheca Hagiographica") — zero hits on every term.

**Reading the number.** Seven rounds, seven independent instrument sets: 0/10, 3/10 (Round 1's own PRESS dispositions found again), 0/10, 0/10, 0/10, 0/10, 0/10. This round's own gap has a shape worth naming rather than only a size: **items 1–2 and 6–8 point at a category this Registry has never held any instrument for at all — hagiographic-genre theory and the standard mid-20th-century English translation series (Fathers of the Church) that sits alongside, and in the letters case fills a real hole beside, the 19th-century ANF/NPNF translations already vendored.** No modern English translation of Augustine's own general correspondence is named anywhere in this 98-row Registry; only the 19th-century NPNF (vendored) and Goldbacher's unread Latin critical edition (row 61) exist. Items 9–10 point at a narrower, specific gap: row 38's own Confidence-D "only the category, no specific site report" admission for Carthage specifically (row 82, Ennabli, is a citywide overview; neither Stevens excavation report is currently named).

**Dispositions.** Per CF V7.4's rule, each of the ten is dispositioned here so the build thread can row it or exclude it with a reason; none is excluded on my own authority.

**Row it:** item 1 (Type S, Native, C — **public domain (1921)**, hosted at `archive.org/details/lespassionsdesm00dele` — a real G-request, not merely consultation-only; licensed for the Author Gravity risk analysis of Pontius's *Life*, Doc_02 §2 and §4, which currently has no theoretical instrument behind it — see PRESS 2); item 2 (Type L, Native, C — base volumes public domain (1898–1911), the 1986 *Novum Supplementum* in copyright; licensed for dating and identifying Pontius's *Life* (BHL 2041) and the *Acta Proconsularia*, row 41 — this Registry's first hagiography-specific reference instrument of any kind, alongside Dekkers's CPL, row 57, for the wider patristic corpus); item 3 (Type S, Native, C, consultation-only — licensed for row 1's own election claim and Doc_02 §2's Representativeness discussion; see PRESS 3); item 4 (Type S, Native, C, consultation-only — licensed for rows 19–21, Augustine's own preaching/exegesis, one of this world's largest primary bodies with no secondary instrument on its own method); item 6 (Type P/S, Native, C, consultation-only — a second, independent modern English translation of Cyprian's letters, from a different tradition than Clarke's ACW, row 46); item 7 (Type P/S, Native, C, consultation-only — the modern parallel translation to ANF05's own rendering of row 5's minor treatises); item 8 (Type P/S, Native, C, consultation-only — the sharpest gap of the ten; see PRESS 1); item 9 (Type M, Native, C, consultation-only — licensed for row 38/82, a full excavation monograph closing exactly the Confidence-D gap row 38 discloses); item 10 (Type M, Native, C, consultation-only — the same licensing, a second and earlier Carthage excavation report by the same excavator).

**Row or exclude, builder's call:** item 5 (Clark, *Monica*) — Monica's own formation predates this world's c. 246–430 boundary (Doc_02 §6 already excludes her presence from the Article 20 discharge on exactly this ground, since she dies at Ostia in 387 before Augustine's own presbyterate); a monograph specifically about her could be rowed Native-but-flagged on the same "held for want of a better connection" basis row 25 (*Soliloquies*) already uses for a comparable boundary tension, or excluded as Out-of-Boundary in the manner of rows 70, 86, and 98. Either is defensible; this document does not decide it.

---

## PRESS question

Asked verbatim: **"Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."**

I can name three. All are different from the 53 works Rounds 1–6 named, each of which is now rowed or excluded.

**1. Sister Wilfrid Parsons (trans.), *Saint Augustine: Letters*, The Fathers of the Church 12, 18, 20, 30, 32, 5 vols. (Washington: Catholic University of America Press, 1951–1956).** *Disposition: row it — Type P/S, Native, Confidence C, consultation-only (in copyright), Licensed For rows 10, 11, and 43.* This is the sharpest gap this round found, and it is a plain one: this Registry currently names exactly one English rendering of Augustine's general correspondence — the 19th-century NPNF translation already vendored — and one unread Latin critical edition (Goldbacher, row 61, Manifest G4). It names no modern English translation at all, though a direct, well-known, complete one has existed since the 1950s and is the version most American seminary and university libraries actually hold. Rows 10, 11, and 43 rest at Confidence A on the NPNF rendering specifically; a specialist bibliography of this world would be expected to at least name the standard mid-20th-century alternative, the same way this Registry already names Clarke's ACW translation (row 46) alongside ANF05 for Cyprian's own letters.

**2. Hippolyte Delehaye, *Les Passions des martyrs et les genres littéraires*, Subsidia Hagiographica 13b (Brussels: Société des Bollandistes, 1921; 2nd ed. 1966).** *Disposition: row it — Type S, Native, Confidence C, **public domain**, Licensed For Doc_02 §2's and §4's Author Gravity assessment of Pontius's own *Life*.* Doc_02 §4 states the Author Gravity risk directly and well — *"written by a deacon with every personal and institutional reason to idealize his own bishop"* — but names no scholarly instrument for what a *passio*/formation-biography genre reliably preserves and where it reliably shapes. Delehaye's is the foundational modern study of exactly that distinction, for the same corpus of early Christian biographical writing Pontius's *Life* belongs to, and it is public domain on its 1921 imprint, freely hosted at the Internet Archive — an acquisition candidate, not merely a consultation, on the same footing von Soden's two 1904/1909 monographs reached at Round 6.

**3. Charles A. Bobertz, *Cyprian of Carthage: Priest and Patron*, Studia Patristica Supplements 12 (Leuven: Peeters, 2023).** *Disposition: row it — Type S, Native, Confidence C, consultation-only (in copyright), Licensed For row 1 and Doc_02 §2's Representativeness discussion of Cyprian.* Row 1 licenses Cyprian's own election language — *"your suffrage and God's judgment"* — as this world's own central documentary anchor for how episcopal legitimacy was understood in this world's Cyprian phase, and Doc_02 §2 builds a Representativeness assessment directly on the patron-bishop dynamic that language implies. This Registry currently holds no monograph on that dynamic specifically — Burns's *Cyprian the Bishop* (row 32) covers his social governance during and after the Decian persecution, a related but distinct question from the mechanics of patronage his own election drew on. Bobertz's is the standard modern account of exactly that mechanism, working from the same corpus this Registry already holds at Confidence A.

---

## Assessment: is the structural remedy holding?

**Yes, where it was actually applied — and this is now confirmed across two consecutive rounds rather than one.** The three enumerations Round 6 converted from maintained lists into stated rules — the priority-flag section, the Manifest's §3 never-vendored list, and Doc_02 §9 item 3's verification-status index — were checked again this round against all ten rows added since (89–98), and every one resolves correctly. No row is mislabelled by any of the three rules; nothing needed correcting in any of them this round. That is real evidence the remedy generalizes: a rule stated once and checked against the table, rather than restated and extended by hand each time a row is added, does not go stale merely because the table grows.

**No, where the same fragility exists in a form the remedy never reached.** Three separate instances this round show the same underlying disease recurring in places the cure was never applied, or applied only halfway:

1. **The row 60 and row 52 placement notes (L1, L2) remain hard-coded row-range prose, not rules.** They are structurally identical to the enumerations that were fixed — a claim of the form "this row sits physically after rows X–Y" that must be updated by hand every time a row is inserted between them — and, predictably, they went stale again in the very commit that added ten more rows below them. Converting these two notes to a rule ("this row's own physical position is disclosed rather than corrected to numeric order; see the table for its current neighbors") would close this permanently, the same way the three other conversions did.

2. **The Decision Log's own directional-pointer retirement (M2) is a case of the remedy being *declared* rather than *applied*.** Line 89 states the fix in the abstract ("is being retired") without auditing the file's own existing text for violations, and the two entries appended in the same pass as the declaration were not checked against it either. This is not a new kind of failure — it is the oldest one in this document set's history (an unre-derived claim reaching a live document, first logged in this same file's own second entry, 2026-09-01) recurring inside the file that exists specifically to track that pattern.

3. **Doc_01's post-disposition edit count (M1) shows the remedy's actual limit.** Dropping the numbered Decision Log pointers — Round 6's own fix — correctly removed one source of staleness (a pointer that goes wrong when the log is reordered). It did not address the more basic problem, which is arithmetic self-reference: a sentence that states "N edits have been made to this document" is falsified the moment it is written, because writing it is itself an edit. No version of this count across four rounds of fixes has accounted for that, and a rule pointing at `git log` would not either, unless the rule is phrased to exclude the correcting edit itself from the count it states — a distinction available in CO-022's own *Coach verification* exception (a correction that changes no substantive claim is disclosed, not necessarily tallied as a further "edit" in the sense this note is trying to count) but never yet invoked here.

**The general reading, extending Round 6's own conclusion rather than restating it.** Round 6 found that deleting an enumeration in favor of a single authoritative pointer works, and that compressing an enumeration into a shorter summary claim does not. This round adds a third case: converting an enumeration into a *rule* also works, cleanly, for two consecutive rounds — but only where the conversion actually happens. Two placement notes and one Decision Log paragraph still carry the old, hand-maintained form, and all three produced findings this round. The remedy is sound; its application has not yet reached every instance of the problem it was built to solve.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Not touched anywhere in the three documents or this round's findings. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** Neither M1 nor M2 decides anything for a reason external to this world's own ecology; both are internal record-keeping defects inside this world's own build. The sibling Donatism build's own state was re-checked at a fresh fetch (`7a675068`) rather than from Round 6's snapshot, and nothing this world cites from it (rows 1, 4, 16, 24, 48, and the G3 *Codex Theodosianus* discharge state) has changed. **Not an escalation.**

**3. Governance or methodology decisions.** None of this round's findings changes how the build process itself works; M1 and M2 are both corrections to this specific world's own disclosure record. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close on its own.** No two reviews disagree here — this round's findings are new instances of a previously-diagnosed pattern (Round 6's own account of the pattern, and Rounds 4/5's own findings on the same Doc_01 count), not a disagreement between reviews about what the record says. Both M1 and M2 are closed at the artifact (`git log --follow`, and a direct grep of the Decision Log's own text), the same way every prior round's instance of this pattern was closed. **Not an escalation.**

**No escalation category applies.**

---

## Eligibility for disposition

CO-022's *Disposition* rule requires **both** that the document has cleared an independent review without that review calling for substantial revision, **and** that none of the four escalation categories applies.

**The second condition is met.** No escalation category applies, checked independently this round rather than accepted from Doc_02 §10's own account of itself.

**The first condition is not met.** M1 changes a disclosure count in an Approved-to-proceed document that this document set's own status lines and §9 both point to as evidence of a working correction record. M2 changes what the Decision Log — the artifact CO-022's own *Revision decision* rule requires review disagreements to be logged in, and the artifact Doc_02 §10 explicitly delegates that logging duty to — actually says about its own current state. Both are "substantial" on CO-022's own test in the same sense Round 6's M2, M3, and M4 were: a claim about what the record shows, checked against the file, and found not to match it.

**None of the two MEDIUM findings is a factual error about this world's history, its sources, or its ecology.** For the third consecutive round, no substantive claim was falsified, and the structural remedy applied since Round 5 continues to hold everywhere it was actually used. What remains unconverged is the same self-referential bookkeeping this document set has had at every round since Round 3: a claim about how many times something has been corrected, or about what a governing document's own current practice is, written in a form that the next edit — sometimes the very edit making the claim — falsifies.

**These three documents are not yet eligible for disposition.** A revised `Doc_02_Source_Ecology.md` / `Source_Registry.md` / `Source_Acquisition_Manifest.md` (and, for M1, `Doc_01_World_Identification_Boundaries_Orientation.md`) goes through independent review again.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED.**
