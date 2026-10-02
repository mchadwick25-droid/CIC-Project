Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry: targeted recheck of the directed corrections of 2026-09-29 (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-recheck subagent, fresh context, launched from session_01JiDJCtJ4ADkPYsNytZikCp (wrote none of the text under review)
- **Drafter agent:** lpc Library thread, commits 578aa048, 4a1d9418, 74945eba, 5b02c718, 4a445ad1 and cc8ac10c (trailers read "Claude Sonnet 5.5")
- **Round:** 32 (a targeted recheck of the Round 31 independent check's findings, P1-1 to P1-6 and P2-A to P2-F; not a full re-review)
- **Truncation check, method 1:** structural count. Registry: 229 table lines, every one with exactly 12 pipes (11 cells); 227 numbered rows forming exactly the set 1 to 227, no duplicates; the saturation statement ends on a complete sentence ("… carried at `Open_Gaps_Tracking.md` (OG-24) and `Doc_02_Source_Ecology.md` §9."). Doc_02: headings §1 to §10 all present, in order (lines 11, 31, 63, 77, 89, 103, 118, 122, 129, 148); §10 ends on a complete sentence.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD a14284de. `wc -c` equals `git cat-file -s` (Registry 236,861 bytes; Doc_02 82,609 bytes; Open_Gaps_Tracking 123,062 bytes); `git hash-object` equals `git rev-parse HEAD:<path>` for all three (Registry c414c36f, Doc_02 ecaaf674, Open_Gaps 267bc21d); both documents end with a newline.
- **Date:** 2026-09-29
- **Documents:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, `Build/worlds/lpc/Source_Registry.md` (with `Open_Gaps_Tracking.md` OG-23 and OG-24 read for routing)
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish (P0/P1/P2 correspond to HIGH/MEDIUM/LOW in Rounds 1 to 30).

## Verdict

**The twelve directed corrections hold at source. The new rows added in the same pass do not all clear.** 0 P0, 2 new P1, 8 new P2.

Every correction that changes a claim was checked against the vendored file by structure marker, not against the Registry. All twelve Round 31 findings are resolved as directed. Two of them (P1-2, P1-4) resolve by routing a Confidence letter to the project lead (OG-23), not by deciding it. That routing is correct for a sourcing conclusion.

The new material is where the defects are. Row 214 points four of its thirteen structure markers at the wrong text. Row 216 gives a publication year the file does not support. The rest are residues of the corrected claims, provenance lost in the narration cut, and a status line that pre-announced this recheck as covering the corrections.

## Per-finding table

| Finding | Status | Evidence |
|---|---|---|
| P1-1 Doc_02 CIL VIII and Codex | Resolved (residue: new P2-2) | Doc_02:93 now reads "the Numidia supplement is vendored (`cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt`; the rest of the volume is not)". File header: "Supplementum, Pars II: Inscriptionum Provinciae Numidiae Latinarum Supplementum … MDCCCXCIV (1894)". Doc_02:97 now reads "held in the shared corpus and usable directly by this document, the same position row 37 records for *CIL* VIII"; Registry row 37 (line 50) says "Vendored in the shared corpus — the Numidia supplement". Doc_02:97 parentheses balance (3 open, 3 close), as they did before. |
| P1-2 Row 44 ground | Resolved as directed; letter routed | Registry:58 now reads "The Licensed-For content has been read against the vendored file … What has not been done is a reading of the Codex beyond that provision. The Confidence letter stays at B pending a decision (`Open_Gaps_Tracking.md`, OG-23)". Source: `theodosianus-16_mommsen-meyer1905.txt`:86853 `XVI,  5,  21  (392  lun.  15).`; 86855–86857 `Id  haereticis  erroribus  quoscumque  con- / stiterit … denis  libris  auri  viritim / multandos  esse  censemua`; 87882 `circumcelliones  argenti  pondo  decem`. All three line numbers match. The false ground is gone. The row now gives no positive ground for B (see "What one round cannot close"). |
| P1-3 Act 158 | Resolved | `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`:121764 `158.  Augustinus  episcop`; 121768 `mendalum  â¢usccpi  fll  nibacripsj.`; no speaker line between. Parallel subscriptions: 121736 `Adeodetui  epi-` to 121740 `scrlpsi  Csrtliegine.`; 121772 `Vincmstius  epiecopete` to 121775 `boc  mendetum  i  uib-`; 121784 `bi;cC0M.slanliiiicii5is` to 121787 `daluin  275  MMOfi  et  subscripai.`. Fourteen act headers confirmed by grep: 50 (126796), 53 (126874), 98 (127458), 158 (121764), 160 (128393), 162 (128450), 187 (128716), 189 (128731), 201 (129009), 206 (129060), 257 (129393), 265 (130240), 267 (130313), 272 (130298). Registry:83 now gives fourteen headers, thirteen speech acts, "Still a floor". Doc_04 reliance matches Doc_04:212 ("One narrow finding survives and is relied on here: act 158 (file line 121764) is Augustine's subscription") and `Doc_04_Superseded_Claims.md`:7. |
| P1-4 Rows 14, 213; Doc_02 line 27 | Resolved; row 14 letter routed | Row 213 (Registry:278): `cic/corpus-map/donatism.yaml` holds "Letters of St. Augustin: the Donatist correspondence", `context assigned`; `_staging/npnf101_augustine-confessions-letters.yaml`:66–69 `atlas_ids: - donatism`, `role: context`; not in `latin-pastoral-congregational-christianity.yaml`. Rows 13/14 `tradition` there (checked). Overlap with row 43 now disclosed. `npnf101`:29650–29652 "To Generosus … Fortunatus, Alypius, and Augustin Send Greeting"; 29696 "2. For if the lineal succession of bishops is"; 29710 "succession no Donatist bishop is found." Row 14 (Registry:27): `npnf104`:16903 `<div4 type="Chapter" n="51"`, 16910 `118.  Augustin answered`, 16912 "the chair … of the Roman Church, in which Peter sat, and which Anastasius fills to-day"; div3 at 15751 is `n="II"`. Row 14 still carries A on one locus; the split-letter question is routed to OG-23 rather than settled. Doc_02:27 updated. |
| P1-5 Corpus count | Resolved | Recomputed from every atlas yaml in `cic/corpus-map/`: lpc 104 raw, 94 `tradition`, 10 `context`, 92 distinct `tradition` titles (duplicates: the Enchiridion, the Scillitan Martyrs). Next-largest raw: 69 (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied); next-largest `tradition`: 61 (`alexandria-catechetical.yaml`). The ten `context` entries: Delehaye 1921, Harnack 1913, Monceaux 1901/1902/1905, von Soden 1904/1909 (seven, 1901–1921), plus the Collatio, Prosper, and the Latin Library Codex. Four Petschenig entries are `tradition, assigned`. None of the 13 new files appears in any corpus-map file. Doc_02:13 matches all of this. |
| P1-6 Possidius | Resolved (residue: new P2-3) | Doc_01:94 (§5) cites "*Vita* ch. VIII, in the chapter heading and in the narrative alike", and "read in full at `Review-Artifacts/Possidius_Full_Read_2026-09-16.md`". `possidius_vita-augustini_weiskotten1919.txt`:2036 `Designatur episcopus vivo Valerio et a Megalio primate`; 2077 "dained by the primate Megalius". Read artifact line 1: "complete read, all thirty-one chapters". Doc_02:21, 59, 60 and 83 now agree with this. |
| P2-A Row 65 wording | Resolved | Registry:83 opens "**Not currently vendored (Lancel).**" |
| P2-B Line numbers | Resolved | 86853/86856/87882 (row 44) and 113068/113076 (row 65) checked: 113068 `ACTORES    VII.`, 113076 `Augustinus  Uipporegiensis.` |
| P2-C Row 29, 204 path | Resolved (copies outside scope remain) | the file tertullian-s-voice.yaml does not exist in the corpus map; `latin-apologists.yaml`:140 "tertullian-s-voice itself is merged into latin-apologists"; Perpetua at 128/144. Rows 29 (Registry:42) and 204 (Registry:269) updated. |
| P2-D Row 189 path | Resolved | Registry:246 names `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`; the file exists. |
| P2-E Joint letter; §118 | Resolved | See P1-4 evidence. |
| P2-F Doc_02 Status | Resolved (see new P2-7) | Doc_02:3 now discloses post-disposition edits. |

## New findings

**P1-A. Row 214 points four structure markers at the Retractationes excerpts, not at the works.** CSEL prints each work's *Retractationes* passage *after* the work. Four of row 214's line numbers (Registry:279) land on those passages:

- *Psalmus contra partem Donati* "2065": line 2059 `AVGVSTINI RETRICTATIONVM LIB. I CiP. XVIII (IX)`, 2065 `1. Dolens etiam causam Donatistarum`. The work's heading is at 1255 (`PSALMUS / CONTRA PARTEM DONATI`), its text from 1294.
- *Contra epistulam Parmeniani* "8441": 8436 `AVGVSTINI RETRlCTiTIONYM LIB. II CiP. XLIII (XVII)`, 8441 `1. In quibusdam libris contra epistulam Parmeniani`. The work begins at 2087 (`CONTRA EPISTULAM PARMENIANI / LIBRI III.`), Liber primus at 2124.
- *Gesta cum Emerito* "72784": 72778 `RETRiCTiTIOMYM LIB. II GiP. LXXVII`, 72784 `1. Aliquanto post conlationera`. The work begins at 72033–72035 (`XI.` / `GESTA CVM EMERITO`); 72774 carries its explicit (`Eiplicinnt gesta beati angnstini`).
- *Contra Gaudentium* "78580": 78574 `RETRICTATIONYM LIR. II CAP. LXXXY`, 78578 `CONTRA GAUDENTIUM DONATISTARUM EPISCOPUM,`. The work begins at 73260–73263 (`XII.` / `CONTRA GAVDENTIVM DONATI-`); the Appendix follows at 78734.

The other nine markers land on the works' own headings or sigla (for example 8475 `DE BAPTISMO LIBRI VII.`, 24750 `CONTRA LITTERAS PETILIANI`, 41779 `CONTRA CRESCONIVM`). A builder following 8441 to *Contra Parmenianum* reaches a thirty-line Augustine retrospect, not the three books. The same four numbers appear in the file's own new "Contents map" header (cic/texts, outside this scope).

**P1-B. Row 216 gives PL 38 a year the file does not support.** Registry:281 reads "Migne, *Patrologia Latina* 38: Augustine, *Sermones* 1–340 (Paris, 1861)". The file's title page (`PATROLOGIjE TOMUS XXXVIII. / S. AURELII AUGUSTINI / TOMUS QUINTUS (pARS PRIOR).`) is followed at line 177 by `1845`. The file header gives "1845 (archive.org catalogue date …)". `grep 1861` finds nothing in the file. The only 1861 in the Library's records is `REGISTRY.yaml`:1736, about PL 36–37. This is a bibliographic date with no source.

**P2-1. Row 225 says the imprint page was not confirmed. The file has it.** Registry:290: "the imprint page was not confirmed." `koch_cyprianische-untersuchungen-deu_1926.txt`:90–91 `BONN` / `A. MARCUS UND E. WEBER'S VERLAG`; 109 `Copyright 1926 by A. Marcus & E. Webers Verlag in Bonn.` The row's "(Bonn, 1926)" is right. Its disclaimer is wrong. The file header's "Publisher: De Gruyter" is contradicted by the title page (cic/texts, outside scope).

**P2-2. The Codex correction left two contradicting sentences.** Doc_02:97 says the Mommsen–Meyer file is "held in the shared corpus", then calls row 88 "A second copy of the same work, **this one actually vendored**". Row 88 (Registry:118) still says "row 44 remains the higher-confidence source for wording, this row the one actually committed to `cic/texts/`". Row 44 (Registry:58) now calls row 88 "a second committed copy". Both files are committed.

**P2-3. Row 45 still routes the Megalius identification through NPNF.** Registry:59 Licensed-For: "the source, **via NPNF's own editorial note**, for the Megalius/primate-of-Numidia identification Doc_01 §5 cites directly to *Vita* ch. VIII". The same row's Verification Note says Doc_01 cites the *Vita* directly. This is a residue of P1-6.

**P2-4. The narration cut removed some provenance along with the narration.** In the diff, I read each cut in rows 6, 14, 19, 37, 44, 56, 65, 70, 79, 85, 88, 102, 122, 135 and 213, and at Doc_02 lines 13, 21, 23, 25, 59, 83, 91, 95, 107 and 112. Most cuts are pure process narration. The cuts listed here carried a fact about who decided or supplied something, or when:

- Row 44: "supplied directly **by the project lead**" (twice) and "**Per the project lead's own decision** it is handled as …". Doc_02:97 still says "supplied by the project lead", so the two files now differ.
- Row 88: "**per his own description of the task**". The book-by-book download now reads as a verified fact, not as the supplier's account.
- Row 6 (Registry:19): "per the corpus map's own **2026-08-26 ruling**". The placement now reads as mere shelving, not as a ruling.
- Registry:4: Doc_01's "Approved to proceed, **2026-09-01**" lost its date.

No cut I read removed a claim about the historical world. The cuts added no new fact.

**P2-5. Row 189's "299" search is described inaccurately and does not settle absence.** Registry:246 says a search for "299" "finds only citations". Line 23084 (`MAI XV. 299`) is a running head. Morin labels sermons by the earlier collection (Mai, Denis, and so on), not by letter-suffixed Maurist numbers. A search for "299" therefore cannot show that 299/D is absent. The row does not claim absence outright, so this is polish.

**P2-6. OG-24 calls a Doc_04 item open when Doc_04 already carries it, and it misses one record.** OG-24 (Open_Gaps_Tracking:1484) says "Doc_04 Round 11 (b) is still open: add the act-158 grounds to Doc_04 Open Item 6". Doc_04:212 already reads "the act header at line 121764 runs on to the subscription formula at line 121768 with no intervening speaker". Doc_04 was last changed on 2026-09-26 (b73abfd2). OG-24 names the `records/lpc` source and honest_limit records, but not `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` (see copies below). OG entries are append-only, so this needs a new entry, not an edit.

**P2-7. Both Status lines said this recheck covered the corrections before the recheck existed.** Doc_02:3 and Registry:3 read "a targeted recheck (`Review-Artifacts/Doc02_Targeted_Recheck_2026-09-29.md`) covers them". They were written before this file. Read as "this recheck covers the corrections", the sentence is true. Read as "the corrections have been confirmed", it overstates: P1-A and P1-B are open.

**P2-8. The Petschenig header now contradicts itself** (cic/texts, outside this scope, reported because row 214 rests on it). It says the file holds "the title pages of 'Pars II' … and 'Pars III' (CSEL 53)", then "Pars III's own title page was not captured in this OCR". Lines 60475–60501 print `VOL.  LHI.` … `MDCCCCX.` The PL 38 and PL 39 headers say "the OCR title page carries no imprint year". PL 38 prints `1845` at line 177 and PL 39 prints `1863` at line 171.

## Checks run with nothing found

- Rows 215, 217–224, 226 and 227 against their file headers and title pages. Zycha CSEL 41: `VOL.  XXXXI  (SECT.  V PARS  III)` at 30, `MDCCCC.` at 56. PL 39: `SERMO CCCXCVI` at 16224, `APPENDIX.` at 17566. PL 40: `TOMUS  SEXTUS.` at 267; *De catechizandis rudibus* at 302 and *De symbolo ad catechumenos* at 326. Morin: `MDCCCCXXX` at 54, `Romae, die 28 Augusti 1930.` at 109. Krüger 1893, Christopher 1926 and Gebhardt 1902 match their headers; Gebhardt has *Acta S. Cypriani* at 459 and *Passio SS. Mariani et Iacobi* at 463. The PL 8 slice is lines 59841–66071, and von Soden's 1909 article is lines 567–2534, as their headers state. Benson: `MACMILLAN AND CO., Limited` / `NEW YORK : THE MACMILLAN COMPANY` / `1897` at 40, 42 and 43. Gsell: `CHAMPION` at 52–54, `1922` at 58, `HIPPONE.` at 822.
- Row 214's other nine markers; Pars II title page `VOL.  Lll.` … `MDCCCCIX.` from line 24180.
- Doc_02:13's figures, Doc_02:93, and the Registry's saturation statement (sweep method and limits) against OG-24: consistent.

## Copies found outside Doc_02 and the Registry (not edited)

- `Build/worlds/lpc/Doc_04_Gravity_Discovery.md`:7 still quotes row 65 as "available to Doc_04, and not yet drawn on by it". It also calls the Registry "returned to independent review 2026-09-13" with nothing after.
- `Build/worlds/lpc/Source_Acquisition_Manifest.md`:29 has Possidius as the source "via NPNF's own editorial apparatus" for an identification Doc_01 "disclose[s] as resting on an unvendored work". Line 73 has the *Gesta* "not usable directly by this document without its own vendoring step" and "he speaks in at least fourteen numbered acts".
- `Build/worlds/lpc/Representative/lpc_Rep_Phase3_Voice_Construction.md`:80 twice cites `tertullian-s-voice` as a live corpus.
- `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md`:258–260 has "He speaks in at least fourteen numbered acts … we have not yet drawn on them". Lines 325–326 have "In fourteen numbered acts, Augustine speaks … and each act has been counted and quoted". Not in OG-24.
- `records/lpc/source/lpc.source.lancel-actes-de-la-conference-de-carthage-411.md`:18 has "FOURTEEN numbered acts in which he speaks"; line 22 has "not yet drawn"; line 38 has `rights_status: public-domain`. Already in OG-24.
- `cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt` header: the same four wrong markers as P1-A, and the Pars III contradiction (P2-8).

`lpc_Decision_Log.md` and earlier review artifacts keep the old wording as history. They are not counted here.

## What one round cannot close (for Mark)

1. **Confidence letters (OG-23).** Row 44 sits at B with its false ground removed and no positive ground stated. Row 14 sits at A on one locus. Whether a row may carry a split letter is a methodology question. Both are sourcing conclusions for the project lead.
2. **Rights on publication date alone (OG-24).** Rows 219 (Morin 1930) and 225 (Koch 1926) have no rights tag on the host. Whether foreign works of 1926–1930 stand on the 95-year rule is a governance call.
3. **Copies in other documents and records.** Doc_04, the Manifest, the Phase 3 Representative file and `records/lpc` carry the old act-158, Possidius and path wording. Correcting them is outside this thread's edit scope. The records copies need a records fix cycle.
4. **The review cap.** This is round 32 on Doc_02 against a cap of 3. P1-A and P1-B are narrow, mechanical corrections to rows written in this pass. How they are governed, as a directed correction or another round, is the same governance call Round 31 routed.
