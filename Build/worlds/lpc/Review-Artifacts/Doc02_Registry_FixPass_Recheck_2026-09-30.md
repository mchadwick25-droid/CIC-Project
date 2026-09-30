Simulated review — informational only, not an Article 31 substitute.

# Doc_02, Source Registry and downstream copies: targeted recheck of the Library's Round 33 fix pass and the lpc do-first corrections (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** Library-thread drafting worker (commits f4f200cce and e2ce41327, session_019FXuEebrCDmzYe987sNAxL) and the lpc build-thread worker (do-first commits 83d21c56c, fafd9b68f and 061e90648); all trailers read "Claude Sonnet 5.5"
- **Round:** 34 (a targeted recheck of what changed since Round 33, against Round 33's findings; not a new revision round)
- **Truncation check, method 1:** structural count. Registry: 274 table lines (header, separator, 272 rows), every row with exactly 12 pipes; the numbered rows are exactly 1 to 272, no gap and no duplicate; the file ends on a complete sentence and a newline. Doc_02: ten `## ` headings, §1 to §10 in order; §10 ends on a complete sentence and a newline. All 14 changed `records/lpc` files parse as YAML front matter and end on a complete sentence.
- **Truncation check, method 2:** byte and hash comparison against the committed blobs at HEAD 061e90648. `wc -c` equals `git cat-file -s` and `git hash-object` equals `git rev-parse HEAD:<path>` for the Registry (418,692 bytes, 8e2fc8cef4), Doc_02 (89,943 bytes, 9f46efe4eb), the force record (4,721 bytes, fc21fff103) and the succession witness (6,348 bytes, ebe8aa28e9). No uncommitted changes under `Build/worlds/lpc` or `records/lpc`.
- **Date:** 2026-09-30
- **Scope:** `git diff 75c29ccb0 HEAD` for the Library fix pass; `git diff 0780fd2a8 HEAD` for do-first 1, 2 and 2b.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** 0 P0, 3 P1, 7 P2.

Round 33's three P1 findings are closed on disk as written. Four of its six P2 findings are closed; one is moved rather than fixed and one is still open. Every do-first correction about a source's text checks out at source: act 158, act 14, the two Theodosian statutes, Letter LIII, Petilian chapter 51 section 118, Possidius chapter VIII, and the Cyprian wording.

The main problem is the corrected silence claim. It now says Optatus is "the one Registry text" dated inside 258–391. That is false: the Registry holds other texts from inside the interval, among them African conciliar canons of 345–348 and 387/390 in rows that are Native. The claim has been copied into seven places. The other two P1 findings are a boundary status that does not meet the Template's definition (row 265), and generators that would restore corrected wording if re-run.

## Round 33 findings: status on disk

| Round 33 finding | Status | Checked |
|---|---|---|
| P1-1 row 265 value outside the Template | Closed as a value. The new value raises P1-2 below | Row 265 (line 330) now reads **Excluded**, Out-of-Boundary |
| P1-2 Doc_02 line 47, row 229's reason | Closed | Line 47 now gives two reasons. Row 228's header states misreads about one word in ten; row 229's own note gives the first-edition, only-witness reason |
| P1-3 change history in rows 243–248 Discovery | Closed | Each Discovery cell is now channel / instrument / date only. Registry REWRITE lines fell from 73 to 69; ROUTE stays 7 |
| P2-1 rows 267–272 at A with no Confidence sentence | **Open** | None of rows 267–272 carries a `**Confidence A**` sentence; row 266 does (P2-2 below) |
| P2-2 the Caesarea sermon exception | Closed | Line 47 ends "apart from the Caesarea sermon (row 270)" |
| P2-3 row 14 marker | Closed | The paragraph `v.v.iv.li-p3` is at npnf104 line 16910 |
| P2-4 row 268 `PAO.` | Closed | Row 268 quotes `PAO. 177, 12 ED. KNOELL`, as line 66062 prints |
| P2-5 row 264 Boundary cell | Closed | The cell reads `Native`; the reasoning moved to Licensed For |
| P2-6 row 227 markers | **Moved, not fixed** | P2-1 below |

## What was verified at source

- **Act 158 is a subscription.** `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` line 121764 prints `158.  Augustinus  episcop`, and the lines that follow carry `Marcdliuo` and `mendalum ·usccpi fll nibacripsj` (*mandatum suscepi et subscripsi*). The other thirteen listed acts (126796, 126874, 127458, 128393, 128450, 128716, 128731, 129009, 129060, 129393, 130240, 130298, 130313) each carry the *dixit* formula. Act 14 at line 125505 reads `Angustinus episcopus ... dixit. Nos in hoc consensisse litteris nostris expressimus. Et alia manu. Recognovi.` That is a short statement followed by a signature, so "a further speech" holds. Thirteen as a floor, plus act 14, is right.
- **Theodosian Code, `theodosianus-16_mommsen-meyer1905.txt`.** At XVI.5.21 (line 86853) the fines are `denis libris auri` (86856, 86863). At XVI.5.52 (line 87872) the scale runs `auri pondo quinquaginta` down to `plebei auri pondo quinque`, then `circumcelliones argenti pondo decem` (87876–87882). The corrected wording "mostly in pounds of gold, with ten pounds of silver for the Circumcellions" is exact.
- **Letter LIII is a joint letter.** In npnf101, line 29644 opens `vii.1.LIII`, and the salutation reads "To Generosus … Fortunatus, Alypius, and Augustin Send Greeting". §2 reads "The successor of Peter was Linus … whose successor is the present Bishop Anastasius. In this order of succession no Donatist bishop is found." The witness record's "the successor of Peter" is verbatim.
- **Petilian, Book II chapter 51, section 118.** npnf104 has `div4 n="51"` at 16903 and §117 at 16905. §118 (`v.v.iv.li-p3`) opens at 16910, and the chair sentence ("in which Peter sat, and which Anastasius fills to-day … in which John sits today") is at 16912.
- **Possidius, *Vita* ch. VIII.** `possidius_vita-augustini_weiskotten1919.txt` line 2075 `CHAPTER VIII`; line 2077 `dained by the primate Megalius`; line 2131 `Megalius, Bishop of Calama, and at that time primate of`.
- **Cyprian.** In anf05, line 31259 (Epistle XXVI §1) reads "through the changes of times and successions, the ordering of bishops and the plan of the Church flow onwards". Line 37558 (Epistle LXVII §5) reads "the practice delivered from divine tradition and apostolic observance". Both are quoted verbatim.
- **CSEL 58.** `Archive/Retired-Library-Texts/augustine_epistulae-praefatio-indices-lat_goldbacher-csel58.txt` line 98 reads `First reprinting, 1961, Johnson Reprint Corporation`. Row 197 records the 1962 Johnson facsimile of CSEL 33 as excluded. The Manifest and Goldbacher-record wording holds.
- **Lancel rights.** Row 65 says the count was read in the Migne PL XI file, and the new Lancel `rights_status` says the same. `lpc.limit.411-gesta-unread` now reads `in-copyright-consultation`. No other `records/lpc` source entry cites Lancel as public domain.
- **Row status letters in the records.** Row 33 is B, and so is the Burns–Jensen record. Row 44 is A, and so is the Codex record. Row 10 is B and row 43 is A, as the Goldbacher record says. Row 204 names `latin-apologists`, as the Manifest, Rep Phase 3 and world core now do. The Donatist-cluster staging entry has `atlas_ids: donatism` only, and it entered `donatism.yaml` in commit 8c5eb2c46 (2026-08-27).
- **Optatus's dates.** Both Optatus TEI headers read `Optatus of Milevis (fl. 366-385)`.

## Findings

**P1-1. The corrected silence claim is false as written, and it has been copied into seven places.**

The places are:

- Doc_02 §7 (line 120): "The one Registry text that dates from inside it is Optatus of Milevis."
- The same "one Registry text" wording at Doc_05 line 27, Doc_08 lines 23 and 264, and the force record (lines 17, 32 and 68).
- `wb_lpc_s25.py` lines 1543 and 1576.
- The silent-century limit record (line 32), which says "the one Native text".

The Registry holds other texts from inside 258–391:

- **Row 265 (Registry, Excluded).** The appendix file's first document, `I. Gesta apud Zenophilum` (TEI line 124), is dated by `Constantino Maximo Augusto et Constantino iuniore nobilissimo caesare consulibus` (line 129) at Thamugadi. Constantine the younger was Caesar from 317 to 337, so the document falls inside the interval on any reading. The appendix also holds the *Acta purgationis Felicis* (line 711) and Constantine's letters (lines 1054–1531).
- **Row 26 (Native, named at Doc_02 §1, line 19).** The vendored NPNF Code of Canons lists its source councils as "Carthage (under Gratus)—345–348" and "(under Genethlius)—387 or 390" (npnf214 lines 32278–32279). It gives canon II as "taken from Canon j., of the Council of Carthage held under Genethlius, a.d. 387 or 390" (line 32592).
- **Row 202 (Native, A).** Its vendored Bruns file prints `CONCILIUM CARTHAGINENSE PRIMUM TEMPORE JULII I PAPAE`, with Gratus of Carthage presiding (`codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt` lines 7852–7858). Julius I was bishop of Rome from 337 to 352.
- **Row 59 (Native, not vendored).** Munier, *Concilia Africae a. 345 – a. 525*.
- **Row 229 (Native).** Its nine unassessed tractatus are ascribed on the title page in part to Optatus of Milevis.

So "the one Registry text" is false because of row 265. "The one Native text" is false because of rows 26, 202 and 59. There is a wider problem too. The councils of Gratus and Genethlius are Catholic African bishops making pastoral discipline at Carthage. They bear on the first clause, "no source … supplies a pastoral or congregational voice from within" the gap. Doc_05 and Doc_08 now make that clause about the whole Registry, not only Doc_02 §1's sources.

There is also an internal conflict. The new sentences call Optatus "Donatism's territory". Row 27 records him as Native, `role: tradition` on this shelf. Doc_02 §1 (line 23) calls him "`tradition` here and `context` on the Donatism side", and Doc_09 line 120 calls him "Native to *this* world".

Does the claim still discharge Doc_01 §5? Doc_01 line 110 asks Doc_02 to name what is missing: "a surviving voice, continuous with Cyprian's own ordinary-pastoral mode, from within this world's own boundary". The corrected §7 discharges that only if conciliar canons are not such a voice. That is a judgment, not a count. It goes to Mark (see the last section).

Is Documented still the right level for the force record? The level fits a checkable fact about the record, and the sentence as written is not true. It stays right once the sentence states only what the Registry shows: which rows date from inside the interval, and which of them this world draws on. As it stands, "anyone can check it against the catalogue" invites a check that the sentence fails.

**P1-2. Row 265 (line 330): Excluded, "Out-of-Boundary for this world", on grounds the Template's definition does not cover.**

`Source_Registry_Template.md` line 58 defines Out-of-Boundary as "a straightforward temporal or geographic mismatch against Doc_01" (c. 246–430, Latin North Africa). The row's stated ground is different: the file is on the `donatism` shelf, and it is not Optatus's own composition. Neither is a temporal or geographic mismatch. The documents are Latin, African (Thamugadi, Carthage) and dated inside the boundary (P1-1).

Round 33 said that if the status was not known, "the choice goes to the project lead". The Library chose it itself. The only reason it recorded is that the Template allows two values (`Build/Ministry/Operations/Audits/lpc_Doc02_Registry_Narration_Moved_2026-09-29.md`, Part E). No ruling in `LIBRARY-DECISION-LOG.md` covers row 265. A boundary status on a shared source is a cross-world decision. It goes to Mark with options:

- Native with no licence, the footing of rows 70, 86, 87 and 127, which the Manifest §3 describes.
- Excluded as a Named Comparandum, with a Comparandum Note.

**P1-3. The generators would bring corrected wording back.** I ran copies of `wb_lpc_s21.py`, `wb_lpc_s25.py` and `wb_lpc_s28.py` in a scratch tree, not in the repo. I then compared their output with the committed records.

- `wb_lpc_s28.py` was not touched by do-first 2 or 2b:
  - its `src()` hard-codes `"license": "public-domain"` (line 353), so `lpc.limit.411-gesta-unread` goes back to public domain for Lancel;
  - line 883 still says "with nothing dated in between" for `lpc.limit.the-silent-century`.
- `wb_lpc_s21.py` restores four old versions:
  - Lancel's `rights_status` becomes "public-domain; vendored in cic/texts/" (`RIGHTS_VENDORED_VERIFIED`, lines 352–356), the claim do-first 2 corrected;
  - row 11 gets back its "Confidence A covers two things: a body-level characterization" (line 638), against the ruling that narrowed row 11;
  - Burns–Jensen goes back to C, "left at C pending" (line 1857);
  - the Petilian record goes back to B, `named-not-rechecked` (lines 708–716).
- `wb_lpc_s25.py` would replace the force record's plain spoken description with its "LAYER 1 -- HISTORICAL EVENT …" build-vocabulary text (lines 1538–1545).

The Codex, Goldbacher, Possidius and Correction records come out the same apart from wrapping and quoting. The world-core output differs throughout. The succession witness and the Donatist-correspondence record have no generator.

Either bring the generators into line with the records, or mark them retired so no one re-runs them. Which one is a process decision (see the last section).

**P2-1. Row 227 (line 292).** It now puts `CLASSIS V` and `SERMONES DUBII` both at line 117125. In `augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt`, line 117124 is `CLASSIS  V.` and line 117125 is `SERXffONES  DUBII.` Give each heading its own line.

**P2-2. Rows 267–272.** The Confidence A reason that Round 33 asked for (its P2-1) is still missing.

**P2-3. `Representative/lpc_Rep_Phase3_Voice_Construction.md` line 80.** It quotes row 204 as "the corpus map's ruling". Row 204 contains no such phrase: it reads "Out-of-Boundary for this world by prior ruling". `git log -S` finds the phrase in no version of the Registry. Do-first 2 edited this sentence and left the misquotation.

**P2-4. `lpc.core.latin-pastoral-congregational-christianity.md` line 436.** It says "207 of the Registry's 212 rows are compiled; these five are not". The Registry now has 272 rows. Rows 245–248 and 265 are also Excluded and are not compiled. Do-first 2 edited this paragraph (the bucket name) and left the count.

**P2-5. `lpc.witness.apostolic-succession-of-bishops.md`, the `text` field.** It says the bishops were "Counting back from the present bishop of Rome, Anastasius … they reached Linus". Letter LIII §2 runs the other way, forward from Peter: "The successor of Peter was Linus, and his successors … whose successor is the present Bishop Anastasius". The `positions` field has it right ("Reckoning from Peter"). This wording predates the corrections.

**P2-6. The force record's spoken description (lines 30–35).** It is plain: short sentences, a we/our voice, and no row numbers. Two phrases are build vocabulary, though: "It belongs to Donatism's territory" names another world in the portfolio, and "We hold it provisionally" is a corpus-map confidence term. Rewrite these once P1-1 is settled.

**P2-7. Commentary left in edited live files.** Do-first 2b edited Doc_05 and Doc_08. The checker still flags Doc_05 at 3 REWRITE and 12 ROUTE lines, and Doc_08 at 3 REWRITE and 2 ROUTE. `CLAUDE.md` says an edit to a live file also removes the commentary already in it.

## Other copies of the old wording

I searched `Build/worlds/lpc` (outside Review-Artifacts), `records/lpc`, `packages`, `canon`, `engine`, `Build/worlds/_cross-world` and `cic/corpus-map`.

- None of these remain in any live file: "not yet drawn on" (for the *Gesta*), "fourteen acts", "silver fines", "Book II §51" or "Book II SS51", "named by Peter himself", "no row in `Source_Registry.md` dates".
- `tertullian-s-voice` survives only as history: in row 29's note that the entry was merged, and in corpus-map notes.
- The one surviving copy of the old silence wording is `wb_lpc_s28.py` line 883 (P1-3).
- `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` line 1483 and `donatism.yaml` line 423 say "at least fourteen numbered acts". Thirteen plus act 14 makes that true, so it is not a defect.
- The hits in `lpc_Decision_Log.md` and `Open_Gaps_Tracking.md` are audit trail and are left as they are.

## Not verified

- Doc_02 sections other than §2 (line 47) and §7, and Doc_05 and Doc_08 beyond the edited lines.
- The Codex of 419's own text, for which canons come from which council. I relied on the NPNF editor's list, at the lines cited.
- The world-core record beyond the edited paragraphs.

## For Mark (a single recheck cannot close these)

1. **The 258–391 silence.** Do the Carthage councils under Gratus (345–348) and Genethlius (387/390), held inside rows 26 and 202, count as "a surviving voice … from within this world's own boundary" under Doc_01 §5? If they do not, the claim can be restated as a true fact about the record. If they do, the gap is narrower than Doc_01 states, and that is a Doc_01 question.
2. **Row 265's boundary status** (P1-2).
3. **Optatus as "Donatism's territory" against row 27's Native, `tradition` placement.** This is the double-placement wording that OG-24 declined to change.
4. **The `wb_lpc_s2x` generators.** Are they kept in step with the records, or retired as provenance? A process decision (P1-3).

## Reviewfile result

`python -m engine.m10.cli reviewfile Build/worlds/lpc/Review-Artifacts/Doc02_Registry_FixPass_Recheck_2026-09-30.md` exits 0 (PASS). The file name carries no "Round", so `roundcount` does not count it.
