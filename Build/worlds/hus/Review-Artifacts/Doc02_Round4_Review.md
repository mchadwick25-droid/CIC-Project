Simulated review — informational only, not an Article 31 substitute.

# Doc_01, Doc_02, Source Registry and gap ledger: targeted recheck after the new sources (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (revision commit cdfa28dad and audit-file commit 447caa85d; commit trailer reads "Claude Sonnet 5.5")
- **Round:** 4 (round 1 of the new-material cycle that the Library's acquisition of 2026-09-30 opened; the prior cycle closed at Round 3)
- **Cycle reset:** the Library's acquisition of significant new material (Foxe vol. III and Van Braght placements, Palacký, Novotný, Erben, Chelčický and other vendored works); the three-round cap counts from significant new material (`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, entry "The three-round cap counts from significant new material").
- **Truncation check, method 1:** structural count. Doc_01: headings §1 to §10 present and in order (lines 13 to 217), 219 lines, ends on the §10 disposition sentence and a newline. Doc_02: headings §1 to §11 present and in order (lines 11 to 222), 224 lines, ends on the §11 disposition sentence and a newline. Registry: 79 numbered rows, every one with exactly 12 pipes; the numbers form exactly the set 1 to 79, with rows 25 to 28 as tombstones; letters A 32, B 19, C 18, D 1, and 9 rows marked "—" (4 tombstones, 5 superseded). Rows 55 to 79: A 14, B 11. Open_Gaps: entries 1 to 35 with no gap and no renumbering of entries 1 to 26 (diffed against cdfa28dad~1), R1 to R9 and E1 to E5 present; the file ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD cccf44f33 (no `hus` file changed after cdfa28dad). For all four files `wc -c` equals `git cat-file -s` (Doc_01 53,684 bytes; Doc_02 53,335; Registry 86,546; Open_Gaps 33,897), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_01 4a20748da1…, Doc_02 d22338e5c7…, Registry dfa46fb024…, Open_Gaps 08f3383dc3…). None of the four has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md`, as committed at cdfa28dad
- **Prior clearance:** `Review-Artifacts/Round3_Recheck_Review.md` (Clear, 0 P0, 0 P1, 3 P2). The drafter's account in `Build/Ministry/Operations/Audits/hus_NewSources_2026-09-30.md` was treated as claims and checked at source.
- **Scope:** the diff of cdfa28dad, limited to the five scope items set by the launching instruction.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** 0 P0, 1 P1, 7 P2.

The new rows are sound work. About 95 quoted strings and structure markers in rows 55 to 79 were re-matched by script in the vendored files, and every one is there, as the scan prints it. The corpus recount is exact by two methods. The cup letters, the *natus*/"conceived" correction, the Four Articles in two Latin orders, Comenius's twelve slips and the Compactata date all hold at source. The confidence tags are conservative on the five-level vocabulary.

The one P1 is a misdescription of the source at the centre of the new Article 4 check. Three live files say Hus's Czech Nicene exposition glosses each clause. In fact, it passes over the clauses from the crucifixion to the return in one phrase. The floor's result still holds, because the short exposition in chapter XXVI covers those clauses. But the statement as written is not what the text does.

Nothing found invents a source, a person or a detail. The one-world, three-strand ruling is untouched. Article 29, the Representative and the registration of `hus` are left open.

## Scope 1: the new Registry rows

Every locus below was matched in `cic/texts/` after whitespace and line-break-hyphen normalisation only, within three lines of the cited line.

| Row | Quote / marker at source | Confidence earned | Witness | Note |
|---|---|---|---|---|
| 55 | Heading "Gallo (Havlikoni) praedicatori in Bethlehem." 7456, number "80." at 7455, running head p. 128; "Noli resistere …", "quia nulla scriptura …", "praepara te …", "Motiva pro communione calicis …", "Scriptum in vinculis …" 7470–7485; "quod laicis fidelibus bibere licet de calice domini" 7365–7366, in a passage that calls this "errorem" | A: each licensed statement read | First, fair | Part I heading is at 817/820, not 815; "Amicis suis Constantiae" at 5439, not 5437 (P2-4) |
| 56 | "Relationis M. Petri de Mladenowic" 13041; Part V heading 17032; "auferimus a te calicem hunc redemtionis" 17267; "Deus mihi, inquit, testis est" 17380–17381; "Christe fili dei vivi miserere mei" 17393; "Qui natus es ex Maria virgine" 17394. Workman's "Who was conceived of the Virgin Mary" at Letters 13349–13350 | A | First | The *natus*/"conceived" correction is right |
| 57, 59, 61, 62, 64, 66, 69, 75, 77 | Remainders; the sizes (1.82M, 1.48M, 1.24M, 1.15M, 818K, 1.00M, 3.28M, 1.53M, 1.22M) match `len()` | B, licensed for nothing specific | As stated | Clean |
| 58 | No. 141 heading 19197; six manuscripts listed at 19204–19207 (M, Cpi, Vdn, Vidb, Vdb, Gr), with Palacký's no. 80 cross-cited; "Motiva pro comunione calicis" 19246; note naming *De sanguine Christi sub specie vini a laicis sumendo*, "Op I 42—44", 19285–19286; no. 140 at 19081/19083; no. 95 at 14647/14649, "označil list jakožto nejistý" 14671–14672, "Hortare ad confessionem fidei et communionem utriusque speciei" 14701–14702 | A | First | See P2-6 on what the row leaves out about no. 95 |
| 60 | All fourteen Czech strings match, lines 2163–2415 | A for the lines read | First | See P1-1 on "his gloss on each" |
| 63 | "Slyš, dcerko! …" 4802; "s chotěm svým Ježíšem, pravým bohem a pravým člověkem, přebývala" 4805–4806; Erben's item 6 at 14655, "toho času byl Hus ještě v Čechách" 14663–14664, "a v žádném jich ani slovíčkem …" 14674–14675, "Petr z Mladěnovic, neopominul …" 14678–14679. Erben's two letters are the Hawlik letter and the one to Wenceslas of Dubá and John of Chlum, as Open_Gaps entry 30 says | A | First | Clean |
| 65 | "Kapitola čtrnáctá." 2869; the two-whales sentence 2951–2953; "Protož kterakť nebezpečné …" 4489–4490. Chapter LXVIII starts at 9643; the "judge does not kill, the law does" argument is there (lines 9666 and 9711) | A | First | Clean |
| 67 | "Authorship and Date." 587; "Thus we have no direct Ms. evidence for assigning the tract to Hus." 590–592; Flajšhans at 353–356 | B | First (Latin) | See P2-3 |
| 68 | "Nos inagistpr civiími" 41973; Article 2 Latin 41996–41997, Czech 42043; "Třetí:" 42234; "Quarto" 42302; the Taborite twelve 42673–42674; the priests' articles 44388–44389 and 44396–44397; the Latin Picards passage, "fratrum cohabitacione [de] Thabor repulsi … per quendam rusticum, qui se Moysen nominabat" 54878–54888; "svlekúce sé nazí okolo ohne tancovali" 54999–55000; "po sv. LukáSi … MCCCCXXI" 55118–55119; Goll's note on the Breslau manuscript and Peter of Dresden 1612–1625 | A as a second witness: outline only, nothing quoted | Second, correctly | Clean |
| 70 | "Satisfaftiva Fratrum Waldenfium" 17311; running head 17358; "Omnem vidclicet fidei veritatem" 17361; the Apostles' Creed, Nicaea and Athanasius 17361–17366; "PROFESSIO FIDEI TRINITATIS BENEDICTiE" 17371; the Christ section 17388–17410 (Pilate misread "Piiato", tomb, third day, fortieth day, right hand); "D E SPIRITU SANCTO VERA EIDES" 17415; the Eucharist "sub panis vinique speciebus utrisque" 17549–17550; "EXCUSATIO FRATRUM WALDENSIUM" 18148; "fumimus & comedimus fub utraque fpecie" 18976–18977; "hoc,quod hi laborent manibus fuis" 18455 | A as a second witness | Second, correctly | Doc_01 §8's outline of the Unity's confession is supported |
| 71 | Excluded, Out-of-Boundary, B | Fits | — | Clean |
| 72 | "De Adamitis hereticis. CAP. XLI." 4521; "Poggus florentinus" in 4075–4083 | A as a second witness | Second, correctly | Clean |
| 73 | Section 60 at 2517–2530: nine men by vote ("per suffragia, viros nouem"), twelve sealed slips ("schedulis occlusis duodecim"), nine blank, three inscribed ("Est"); section 61 at 2532–2543, Michael of Žamberk and two others, Bishop Stephen, bishops created by laying on of hands; the section misnumbered "65" at 2567–2577; running head 2562 | A as a second witness | Second, correctly | The lot statement is exact |
| 74 | "1420, m. Jul. (bei Prag)" 1994; "Antwort auf die vier Prager Artikel" 1996–1997; "Responsio domini Fernandi …" 2001; "de verbo ad verbum" 2057–2058; the four points at 2060–2081 in the order cup, preaching, clergy, sins; "die vier Prager Artikel und alle heilsamen Lehren des Evangeliums zu schützen" 20170–20171 | A | First | Clean |
| 76 | "Endlicher Abschluss der Compactaten …" 21226–21227; "1436, Jul. 5 (Iglau)" at 21224 and 21244; "Summa actorum inter legatos concilii Basiliensis" 21250; "ipso die post festum sancti Procopii" 21251–21252; no. 912 heading 19197 | A | First | The feast-day arithmetic is disclosed as the builder's knowledge |
| 78 | "We, Nicholas, by the grace of God bishop of Nazareth, and inquisitor" at 34376; "a faithful and a catholic man" 34383 | A for the one licensed fact | See P2-5 | Clean |
| 79 | "retained and accepted therefrom, among other articles, that it does not become a Christian to swear" 47374–47376; the Taborites as Waldenses from 47499 | See P2-2 | See P2-5 | See P2-2 |

**Rights.** Every new row states "public domain by date" and the file header for each of the 13 new files reads "Rights: Public Domain" with the publication date the row gives (1524, 1690, 1702, 1837, 1865, 1866, 1868, 1869, 1873, 1886, 1893, 1912, 1920, 1927).

**Superseded rows.** Rows 34, 35, 49, 50 and 51 carry "—" for Confidence, "Superseded: the work is on the shelf; see rows …" in Licensed For, and point to the right replacement rows. The header states the rule. This is clean.

## Scope 2: claims the new material changed

- **Article 4 on Hus's Czech creed.** Chapter XXVII (2248–2266) sets out the whole Nicene Creed in Czech, and the quoted clauses are exact. Chapter XXVIII glosses the Father, "things seen and unseen", only-begotten, begotten before all ages, God from God, Light from Light, true God, begotten not made, one substance, "through whom all things were made", "came down from heaven" and the incarnation. It then writes "a tak jsa člověkem, ukřižován jest; a tak dále až do onoho slova: přijde s oslavností" (lines 2362–2363): "and so on up to the words 'will come with glory'". The Spirit is glossed from 2369 (Lord, giver of life, *filioque*, worshipped and glorified). So the Nicene gloss skips the passion, burial, rising, ascension and session. Chapter XXVI glosses those clauses on the Apostles' Creed (2170–2205), and there much is legible: "neb jest pravý buoh a pravý člověk", "Narodil sě z Marie panny", "Trpěl pod Pontským Pilátem" (misread "I*ontským", 2180), "pohřeben" (2185), "tíétí deň z mrtvých vstal" (2190). The floor holds. The description is P1-1.
- **The Unity's Latin confession.** Supported as described in Doc_01 §8 and Doc_02 §8, at second-witness level (row 70 above). Tagged Inferential/Thin in the Confidence Map. That is conservative.
- **The lot.** Comenius has twelve sealed slips, nine blank and three inscribed, among nine men chosen by vote (2517–2527). Doc_02 §3 item 2, §4 and Open_Gaps entry 32 state it correctly. They also say it is not shown to be the census's Lhotka story.
- **The Four Articles.** The legate's order (cup, preaching, clergy, sins) and Březová's order (preaching, cup, clergy, sins) are both right at source. "Four points: Documented" and "The order: Contested" are defensible.
- **Confidence Map splits.** "Hus defended the cup from prison: Documented" rests on the Latin in six manuscripts and in Palacký. Erben's dissent is disclosed in the same row, and it answers a Czech translation of 1563/64 dated 1414. "Came to it late: Contested" is well founded. Workman's "Hitherto" refers to the time when Chlum invoked Hus's authority, and his cross-references are to prison letters. Novotný's no. 95 is before Hus's imprisonment. "Compactata 5 July 1436: Documented" rests on Palacký's dated heading, the Latin "ipso die post festum sancti Procopii" and Lützow. Every changed tag uses the five-level vocabulary, and none is set above its evidence.

## Scope 3: "not vendored" and "absent" statements

Every "not vendored" statement in Doc_01, Doc_02 and the Registry was checked against the filenames in `cic/texts/` and against full-text search, and every one is true. The statements cover Goll, Gillett vol. I, Loserth's *Hus und Wiclif*, Nedoma, Kybal, Flajšhans, the *Historia et Monumenta* of 1558/1715, Spinka, Kaminsky, Fudge, Šmahel, Brock, Richental, the *Acta*, the 1501 hymnbook, Gregory's letters, the 1535 Cologne *Fasciculus*, the *De sanguine Christi* tract and the *Archiv český*. Doc_02 §1's "What the shelf still lacks" holds. Stale current-tense statements remain in Open_Gaps (P2-1).

## Scope 4: the corpus recount (`LC_ALL=C.UTF-8`)

| Figure | Method 1 (Python `len()`) | Method 2 (`wc -m`; `sed -n` for line ranges) | Claimed |
|---|---|---|---|
| 23 assigned files (24 corpus-map entries) | 35,341,097 | 35,341,097 | 35,341,097 |
| Bytes | — | 36,047,134 (`wc -c`) | 36,047,134 |
| Foxe 30742–46807 / Van Braght 47370–47660 / Brown 17311–19520 | 1,018,510 / 10,416 / 162,022 | same | same |
| Working corpus | 22,880,482 | same | 22,880,482 |
| Tradition role (11 files, Brown at its section) | 12,852,753 (56.2%) | — | 12,852,753 (56%) |
| Eight quotable-after-page-check files / the rest | 8,919,310 (39.0%) / 3,933,443 | — | same |
| Hus's two English works | 1,408,217 | — | same |
| Shelf | 396 `.txt`+`.xml` (358 + 38) of 403 entries; `REGISTRY.yaml` is a list of 396 | — | same |

The shelf search counts were also rerun with `grep -l`: 73 files for whole-word "Hus|Huss", and 25 for Hussite, Utraquist, Calixtine or Taborite. Both match.

## Scope 5: placement, invention, rulings, hygiene, tools

- `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml` assigns Foxe vol. III (role context, locus 30742–46807) and Van Braght (role context, locus 47370–47660, the Taborite sections 47499–47566) to this world. Rows 78 and 79 are in order. No row draws on a work assigned only to another world. Section E and entry 27 record the other-world candidates, and none has a row.
- Nothing is invented. No detail, date or person appears that the files do not carry, except the Procopius arithmetic and the "August 1420" year, and both are disclosed.
- The one-world, three-strand ruling is unchanged in substance. Only its evidence lines were updated. Article 29, the Representative and registration stay open (Open_Gaps entry 35, Doc_01 §9).
- `python -m engine.m10.cli gaps hus`: PASS.
- `python tools/check_live_commentary.py --surface worlds`: for the `hus` files, Doc_01 and Doc_02 show only PROTECTED lines. The Registry shows 54 REWRITE (iso-date) lines, all in the Added and Discovery cells that Framework V7.4 Step 2 requires. That is the same schema data cleared in Rounds 1 to 3, now one per real row. Open_Gaps shows only PROTECTED.
- `--base origin/main --enforce`: exit 1 across the branch (412 REWRITE/ROUTE lines, most in `_cross-world` and other worlds). Restricted to `Build/worlds/hus/`, the only hits are those 54 Registry schema cells.
- **Readability of the changed prose.** Doc_01 and Doc_02 mostly keep short declarative sentences, one point to a sentence. The Article 4 bullets and Doc_02 §3 items 2 and 6 are dense with quoted Czech and Latin, which is what a builder-facing check needs. Registry cells are long by design. No AI-voice filler was found.

## Findings

**P1-1. The Nicene gloss is described as covering every clause, and it does not.** Registry row 60's Licensed For says "the clauses of the Nicene Creed and his gloss on each". The Doc_02 §8 row "Hus affirms the creed's substance" says the exposition "sets out and glosses each clause of the Nicene Creed". Open_Gaps entry 28 says the same ("glosses each clause"). Hus's chapter XXVIII passes from the incarnation to the return with "a tak dále až do onoho slova: přijde s oslavností" (Erben vol. 1, lines 2362–2363). Those clauses are glossed in chapter XXVI, on the Apostles' Creed (2170–2205). Doc_01's §8 Result ("every clause of the five is set out and glossed") is true only when XXVI is counted, and its commitment-4 bullet does draw on XXVI. Required fix: state that XXVII sets out the Nicene Creed; that XXVIII glosses it clause by clause except the crucifixion through the session, which it passes over; and that XXVI glosses those clauses on the Apostles' Creed. Optional: Doc_01's commitment-3 note ("too garbled to quote") overlooks XXVI's legible "Narodil sě z Marie panny" (about 2176) and "neb jest pravý buoh a pravý člověk" (2171). The conclusion of the floor check does not change.

**P2-1. Stale current-tense statements in Open_Gaps.** The Section B heading still reads "(no source has been fetched)". The Section E heading says its works have "no Registry row", while E1 and E2 are now rows 78 and 79. R1 still says Foxe "is vendored and assigned to another world". Entry 26's R6 line says "The Taborite articles are not located in any vendored file", and its R7 line says the letters to Dr. Augustine "were not located". Entries 27, 31 and 32 carry the new facts, but they do not name the older sentences they overtake. The numbered entries are append-only, so the remedy is for entries 27, 31 and 32 (or a new entry) to name each overtaken sentence. Correcting the two section-heading parentheticals is the project's hygiene call.

**P2-2. Row 79 reaches outside the mapped locus, and its A exceeds what was read.** The Verification Note cites a note at lines 47774–47777. The corpus map's locus, and the Registry's own count, stop at 47660. Licensed For is "how a 1660 Anabaptist martyrologist read Hus and the Taborites", but only the Hus entry and the start of the Taborite notice were read. The "Taborite confession of 1431" was "not read closely". The fix is to drop the out-of-locus note or say it lies outside the mapped section, and to narrow Licensed For to the two passages read (or grade B).

**P2-3. Row 67 licenses nothing, yet two claims draw on it.** Doc_01 §7 and Doc_02 §3 item 1 say the *Tractatus responsivus* "draws long passages from Wyclif's *De potestate pape*". The claim is true at source (Thomson's introduction, line 742, and the apparatus at 2039 and 11307). But row 67's Licensed For reads "Nothing yet", and its note does not cite those lines. The fix is to license the row for the editor's statements on authorship and on the Wyclif borrowing, with the line numbers.

**P2-4. Line-number slips of one to five lines.** Row 55 gives Part I at 815, where "PARS PRIMA." is at 817 and "EPISTOLAE M JOANNIS HUS," at 820; it gives "Amicis suis Constantiae" at 5437, where it is at 5439. Row 76 gives no. 964 at 21246, where the dated heading is at 21244 and "Summa actorum" at 21250. Row 78 gives the testimonial at 34375, where it is at 34376. Every marker is present and unambiguous.

**P2-5. Rows 78 and 79 do not use the Witness vocabulary.** The header requires each Verification Note to open with a Witness of *first* or *second*. These two rows open "Witness: English …, legible", which is not bolded and uses neither term. The fix is to name them as first-witness English of a secondary compilation, or to state that the first/second distinction applies to original-language rows only.

**P2-6. Row 58 leaves out two facts about no. 95 that bear on the Contested tag.** Novotný says no manuscript survives: "Rukopis nezachován, zastupují ho Opera" (14654). The text rests on the printed *Opera*. He also argues that the letter was written at Constance "když Hus přijímání pod obojí byl již schválil" (14676), and that in prison Hus spoke of the cup "zdrželivě" (with reserve) where he had earlier been more decided (14683–14685). Both facts strengthen the case that the claim is disputed, and neither is in the row or in Doc_02 §3 item 6.

**P2-7. Change-relative wording in live files.** Several phrases measure the text against an earlier state of the shelf, not the shelf as it is: "are now on the shelf" (Doc_01 lines 65 and 103; Doc_02 lines 137 and 168), "it is no longer total" (Doc_02 §6), "is now checkable" (Registry row 68) and "now speaks in its own words in part" (Doc_02 §6). The classifier does not flag them. They are mild change history in canonical text, and the fix is to state the present fact ("is on the shelf").

## Not re-verified

- Every quotation in rows 1 to 54 and every corrected older row (5, 11, 13, 16, 22, 29 to 33, 39, 43, 48) beyond the "not vendored" statements. Round 3 cleared the former, and the corrections were not diffed line by line.
- Czech and Latin wording against page images. None was available, and every match here is to the OCR text.
- The Mehrning/Lydius attribution in row 79, and Calvin's *Letters* vol. 4 as "a letter to Calvin from the Bohemian Brethren" (Open_Gaps entry 27).
- Rights beyond the file headers (for example, the status of Thomson's 1927 English introduction outside the United States).
- The Build State YAML and the audit file's account beyond the claims listed in scope.
- Doc_01 and Doc_02 text outside the changed lines.

## Outside this scope, noted only

- Chelčický's chapter LXVIII opens with the Basel dispute between Master Giles and "kněz Mikuláš, biskup piesecký", the Taborite bishop Nicholas of Pelhřimov. That is a Taborite figure inside a first-witness Czech text, and a lead for the Taborite-voice gap at a later reading.
- Hus's gloss on the *filioque* (XXVIII, lines 2381–2393) reports his own conversation with Greeks. It bears on nothing in Article 4, but it is a vivid first-person passage for later documents.
