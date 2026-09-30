Simulated review — informational only, not an Article 31 substitute.

# Doc_02, Source Registry and gap ledger: Round 1 full review (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (commit 06551b798; its trailer reads "Claude Sonnet 5.5")
- **Round:** 1
- **Truncation check, method 1:** structural count. Registry: every table line has exactly 12 pipes; the 41 numbered rows form exactly the set 1 to 41, with no gap and no duplicate; the saturation statement ends on a complete sentence and a newline. Doc_02: headings §1 to §11 are all present and in order; §11 ends on a complete sentence and a newline. Open_Gaps: entries 1 to 21 and R1 to R9 are all present; the file ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 06551b798. For all three files, `wc -c` equals `git cat-file -s` (Doc_02 26,977 bytes; Registry 28,099; Open_Gaps 13,881), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_02 1c16cdef…, Registry 4b394a61…, Open_Gaps 0e4b6a3d…). None of the three files has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/hus/Doc_02_Source_Ecology.md`, `Build/worlds/hus/Source_Registry.md`, `Build/worlds/hus/Open_Gaps_Tracking.md`, as committed at HEAD 06551b798
- **Compared with:** `Build/worlds/lpc/` and `Build/worlds/rzg/` (Doc_02, Source_Registry, Review-Artifacts); Construction Framework V7.4 Part II and Step 2; `Source_Registry_Template.md` V1.0; `LIBRARY-DECISION-LOG.md`, entry of 2026-09-25
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

Verdict: Not approved to proceed. Not cleared. 0 P0, 9 P1, 12 P2.

This is a careful, honest draft. Its gaps are named, and the requests are marked as leads. Most quotations are verbatim. No source is invented, and no claim is made up to fill a gap.

The P1 findings are substantial under the build cycle's rule, because they change a sourcing conclusion, a confidence rating, or a stated fact about the shelf:

- the Forces lens is missing;
- one corpus figure is wrong;
- three A-row loci are wrong;
- in-window Unity text that is on the shelf is said to be absent;
- the Adamite rating is too strong;
- the draft gives itself a partial licence to quote the Piccolomini scan;
- sources named in support of claims have no rows;
- a vendored Hus section is missing;
- one request misreads Schaff.

## Tool runs

- `python -m engine.m10.cli gaps hus`: `gaps: PASS`, exit 0.
- `python tools/check_live_commentary.py --surface worlds`: exit 0, 21,176 hits fleet-wide. For the three files under review:
  - Doc_02: 2 hits (line 152 REWRITE, iso-date; line 156 PROTECTED, route-cue).
  - Open_Gaps: 26 hits, all PROTECTED.
  - Registry: 41 hits (20 KEEP, 21 REWRITE), one per table row, all of class iso-date.

  I checked the Registry hits by reading them. Each one is a row's Added and Discovery cells. Construction Framework V7.4 Step 2 requires both ("Every source row carries its own discovery_channel, discovery_instrument, and discovery_date"). These are schema data, not commentary. Doc_02 line 152 is the STARLITE search record, which the same Step requires. The process narration I did find is at P2-11.

## Calibration rule applied

The rule is the Registry's own, and it matches the lpc Registry. "A = the Licensed-For passages were read and matched in the vendored file by a structure marker … B = a specific work or locus is named and exists in the vendored file, but the Licensed-For content was not itself re-read. C = a real author and work, no locus checked, not vendored. D = a body or genre of material, no single text named."

Every one of the 41 rows carries exactly one letter: A 19, B 9, C 12, D 1. Every Excluded row has an Exclusion Reason and no Licensed-For. Every Native row has a Licensed-For and no Exclusion Reason.

## Spot-check at source (21 rows)

Every quotation below was matched after whitespace and line-break-hyphen normalisation only, which is the Registry's own stated method.

| Row | Letter | Result |
|---|---|---|
| 1 | A | All five quotations are at the lines given (5309, 5660, 5848, 7591, 8332). The heading markers are one or two lines early (P2-1). |
| 2 | A | 1440, "erected and endowed" at 1453 and "usually accepted …" at 1388 are exact. The 1401 note is in Letter XVIII, not Letter XVII (P1-3). |
| 3 | A | 8815 is exact. "Two Waldensians from Dresden, Peter and Nicholas" begins at 8804, and 8807 holds "in the summer of 1414" (P2-1). "decisively" at 8819 and "priest Hawlik" at 8812 support Doc_02 §3 item 6. |
| 4 | A | "I have appealed to Christ" at 11619, under LXVI (heading at 11401). |
| 5 | B | XI is marked as Czech at 3687. B is earned. |
| 6 | B | The introduction's footnote (1372–1375) gives sixty-six in the *Monumenta*, one spurious, nine first printed by Höfler, the rest by Pez, Erben and Palacký. The 82 headings run to LXXXII at 13051. |
| 7 | A | The four phrases are at 3332, 3973–3974, 5429–5433 and 6000. p. 70 is in ch. VIII (heading "CHAPTER Vm" at 5274), not ch. VII (P1-3). The ch. III heading is "CHAPTER m" at 3216. |
| 9 | A | 1514, 1516 and 2225–2229 are exact. The Calvin and Bullinger passage is at 1484–1489. The Loserth revision after Flajšhans is at 1676–1679. |
| 10 | A | "the works of Hus, as Loserth has shown, are for the most part mere copies of" at 1321. "hopelessly doctored" is at 5650, under Letter XX (P1-3). |
| 11 | A | The sect-chapter heading is at 3619 and "DE ADAMITIS" at 5132. "Martyrum honores meruere" at 4087; the Poggio passage at 4063; Dionysius and Cyprian at 3889; "Bechingne … Thabor … triginta circiter millia" at 4138–4140. The scan note is incomplete (P1-6, P2-8). |
| 13 | A | 17350, 17477, 17526 and 17710 are exact. The running head "ARTICLES OF THE CALIXTINES. 441" is present. "brother and sister" is at 17711. |
| 14 | A | 2696 is on p. 53. "They went to their punishment as to a feast" is at 3479, under the p. 73 and p. 74 heads, and "knew all the circumstances" is at 3478. |
| 16 | A | 312–313, 2774 (p. 56), 3574–3575, 5321 and 5336 are exact. "almost our sole authority" is at 5382 and "containing further statements …" at 2806. |
| 18 | A | 10012, 10068–10069, 10100, 9416–9419, 9520, 10760–10761, 10767 and 10773 are all exact. |
| 20 | A | The Kybal sentence is at 195–196, and "depended by no means entirely on foreign influences" at 192. |
| 22 | A | 198 is exact. Note [2] at 7749 reads "No indiyidnal", and it is signed "Comenius" (7767, "Oomeniiui"). The 1504 and 1508 documents are named at 288–292. |
| 23 | A | 4134 and 4162 are exact. "genuine offspring of the holy martyr Huss" is at 4151, and "Stephen burnt alive at Vienna" at 4129–4130. |
| 24 | A | "the Apostles' creed" is at 6275. |
| 25 | A | "a faithful and a catholic man" is at 34383. "THE BISHOP OF NAZARETH IN FAVOUR OF JOHN HUSS" is a running head at 34360; line 34374 reads "The Testimonial of the good Bishop of Nazareth." (P2-1). The letter does not fit the rule (P2-2). |
| 26 | A | The quoted wording matches `luther_first-principles-reformation_wace-buchheim1885.txt` at 6959–6963. `luther_works-v2…` at 4306–4308 has different wording ("John Hus … were burned … imperial safe-conduct and oath") (P2-1). |
| 27 | A | Lines 248–254 and 2771 are exact. |

## Corpus figures, by two methods

The eight assigned files were counted two ways:

1. Decoded UTF-8 character length, per file, in Python: 6,654,664 characters in all.
2. `cat` of the eight files piped to `wc -m` under `LC_ALL=C.UTF-8`: 6,654,664.

The two Hus files are 735,667 and 672,550 characters: 1,408,217 together, or 21.2 per cent. Doc_02 §1's "about 1.4 million" is right. Its "About 6.1 million characters in all" and "roughly a quarter of the shelf" are not (P1-2). The per-file sizes in rows 12, 15, 17, 19 and 21 are right.

## Findings

### P1

**P1-1. The Forces lens is missing.** Doc_02 is a Forces Framework integration point (Step 2). Framework V7.4 Step 2 requires: "Apply forces lens: which sources speak to external forces? What do silences reveal? What survivorship patterns indicate which forces were most threatening?"

Doc_02 names the Forces Framework in its header and nowhere else. lpc Doc_02 carries this as a named paragraph in §6. The hus shelf has obvious material for it:

- crusade and conciliar pressure in Lützow and Piccolomini;
- the survival of the Unity's record only through its later exile church;
- the loss of the Taborite record after 1452.

Add a Forces-lens paragraph that names the sources and the silences.

**P1-2. The corpus total is wrong.** "About 6.1 million characters in all" should be about 6.65 million. "Roughly a quarter" should be about a fifth (21 per cent). Both methods above agree.

**P1-3. Three A-row loci are wrong.**

- Workman's note that "the first year of his preaching was 1401" (line 5440) sits under Letter XVIII (heading "XVHI." at 5392), not Letter XVII. Affected: Registry row 2, Doc_02 §8 ("Letter XVII note"), and, by propagation, Doc_01 §2 (flagged for the Doc_01 round).
- "The text in the Monumenta has been hopelessly doctored" (5650) is the note to Letter XX (heading at 5617), not Letter XVII. Affected: Doc_02 §2, Transmission History.
- *De Ecclesia* p. 70 (5429–5433) is in ch. VIII, not ch. VII. Affected: Registry row 7.

The quotations are exact. The locus labels are wrong on rows whose letter claims a match by structure marker.

**P1-4. In-window Unity text is on the shelf, and the documents say it is not.** The Seifferth volume quotes the Brethren's 1508 letters to Dr. Augustine, in English, twice:

- the footnote at 548–555: "When we find them useful, or not hurtful, and not contrary to the word of God, we willingly conform to them … Ad Doctorem Augustinum, a.d. 1508";
- the Notes at 8242–8268: "We are not ashamed of our priests because they labour … with their own hands," cited to the *Fasciculus*, fol. 88.

These are short fragments of a 1457–1517 Unity document, at two removes (the 1535 printing, then the 1866 translation). The following statements are therefore false as written:

- Doc_02 §1: "No Unity text from 1457 to 1517";
- Doc_02 §6: "No Unity text from 1457 to 1517 is vendored";
- Doc_02 §7 item 1: "No … letter … by the Unity from 1457 to 1517 is on the shelf";
- Registry row 32: "No copy of any is on the shelf";
- Open_Gaps entry 1.

Give the fragments their own row, with their transmission stated. Then restate the gap as "fragments only".

The binding Step 0 finding still stands in substance. No confession, catechism or hymnbook is on the shelf.

**P1-5. The Adamite rating is too strong.** Doc_02 §3 item 4 and §8 rate "The Adamites were not Hussites" as Dominant Modern Reconstruction. The same paragraph says the claim "rests on Nedoma's article of 1891 and is unchecked against later work". A claim checked against no modern work cannot be called the leading modern reconstruction.

The vendored Lützow also undercuts it. On Březová's account, the Adamites were a party expelled from Tábor itself (Hussite Wars 5382–5392), and Piccolomini and Březová both tie them to Tábor. From my own knowledge (not an instrument read in this round), Kaminsky (1967) treats the Pikarts and Adamites as a radical offshoot of Taborite chiliasm, which is the opposite view.

Rate the claim Contested, carry both sides, and make Doc_01 §8 match.

**P1-6. The draft gives itself a partial licence to quote the Piccolomini scan, on a false premise.** Doc_02 §7 item 3 says the scan's long-s errors are ones "which the quote gate can normalise", and that "Short clean phrases can be quoted."

The quote gate's `normalize_archaic_letterforms` (`engine/m1/quote_verbatim.py`, `_LONG_S_RE = re.compile("ſ")`) replaces only the character ſ. This file contains no ſ; it prints long s as f ("Hufit", "fua", "Thaborite"). `cic/texts/REGISTRY.yaml` gives this file no letterform apparatus.

The 2026-09-25 ruling, point 5, is binary: "A garbled OCR scan stays second witness until a clean witness of the same work is vendored." Whether this scan is garbled is the Library's call. Doc_02 rightly raises that question at Open_Gaps entry 3, and should not pre-empt it with a "partly usable" status of its own. Registry row 11 (Type P, A) should say that quotability waits on that ruling.

**P1-7. Sources named in support of claims have no rows.** The Framework's checkpoint rule is binding: "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row." These sources are named in support of claims and have no row:

- Loserth, *Hus und Wiclif* (1884), cited in §3 item 1 and §8 for the Wyclif dependence;
- Nedoma's 1891 article, the stated basis of the Adamite claim;
- Kybal's work on Matthew of Janov (1905), quoted in §2 and §3;
- Flajšhans's *Super IV. Sententiarum* (1905), for Loserth's revision.

These are finds of the apparatus snowball, which the Framework requires to be dispositioned, and they have no row either:

- the *Historia et Monumenta J. Hus* (1558 and 1715), the Latin base text of *De Ecclesia* (request R2);
- Palacký's *Documenta* (1869), cited by Lützow at Hussite Wars 4121 and Life & Times 2487 and 3074 (R4);
- Erben's and Novotný's editions (R3).

Several of these are the public-domain originals the PD-original ruling treats as primary. Row each at C, with its rights basis.

**P1-8. A vendored Hus section is missing, and the saturation statement overclaims.** The saturation statement says the Registry holds "every other file that mentions Hus, the Bohemian Brethren or the Unity, by full-text search". `van-braght_martyrs-mirror_sohm1886.txt` has a Hus and Hussite section at 47370–47625. It includes:

- "A.D. 1415. At this time John Huss lived, who … accepted therefrom … that it does not become a Christian to swear";
- a notice on Hus's followers taken from Jacob Mehrning;
- the split into "Praguers" and "Taborites" (from Lydius);
- a note on the name "Bohemian brethren" (47774–47777).

This is a 1660 Anabaptist appropriation of Hus into a Waldensian and non-swearing lineage. It is exactly the kind of Named Comparandum the Template exists to catch.

Row it as Excluded, Named Comparandum. Then correct the saturation statement's "only the Seifferth volume and, in passing, a few other files". Full-text search finds 106 files with the word "Hus" or "Huss", and 8 with the Brethren and Unity terms.

**P1-9. Request R2 misreads Schaff.** R2 says: "A scholarly edition by Flajšhans is also named in Schaff's apparatus." Schaff says the opposite: "It is to be hoped that Dr. Flajshans will add to his other editions of Huss's writings a new edition of this, Huss's most important treatise" (lines 2265–2267). As of 1915 there was no Flajšhans edition of *De Ecclesia*.

R2 is a lead, but this sentence reports a vendored text wrongly. Correct it. The Latin lead should rest on the *Historia et Monumenta* (the 1558 and 1715 printings Schaff used).

### P2

**P2-1. Line markers.** These are off by one or two lines:

- the Letter headings in row 1: XVII is at 5069 (not 5067); XX at 5617; XXI at 5727; XXXIV at 7474; XXXIX at 8252;
- Letter I at 1683; XLI at 8653; LXVI at 11401;
- row 3: the quotation starts at 8804;
- row 7: "very God and very man" is at 6000;
- row 25: the running head at 34360 is not a body heading at 34374;
- row 26: the quoted wording belongs to Wace–Buchheim, not to Jacobs–Spaeth line 4306.

**P2-2. A letters for rows that license nothing.** Row 25 is at A, but its Licensed-For reads "Nothing yet". Under the Registry's own rule, A is defined by Licensed-For content. Existence and structure checks are the B case. Put row 25 at B. For the Excluded A rows (24, 26, 27), say once in the header what an A attests where no Licensed-For exists.

**P2-3. No rights basis per row.** The lpc and rzg Registries state each row's rights basis; this one states none. I checked every vendored file's header: all eleven are public domain by printed date, 1930 or earlier (1592, 1837, 1866, 1871, 1885, 1886, 1904, 1909, 1914, 1915, 1916, 1920, and the Bacon–Allen hymnal). Add the basis to each row. Also mark rows 30 (Spinka, 1965) and 40 (Loomis, 1961) as in copyright, as rows 29, 31, 36, 37 and 41 already are.

**P2-4. Confidence vocabulary drift.**

- "Documented (in the vendored edition)" with the basis "a single edition" does not fit Article 17's "multiple independent sources". Lützow 1909 (line 3429) gives the 1402 appointment independently; cite it.
- §3 item 6 has no vocabulary label.
- "its meaning Contested" for the 1401 statement names no disagreement. Workman explains it (he says Hus reckons from his 1400 ordination).

**P2-5. Jews in the vendored evidence.** §6 dates the anti-Jewish violence "(1419; …)". The vendored passages are 1422 (Hussite Wars 5810, after the execution of the priest John) and 1483 (Bohemia 10760). §5's "only as victims" is too broad as a statement about the vendored evidence. Life & Times 1294 reads "Many Jews flocked to Conrad's sermons" (Waldhauser, before the window). Limit the claim to the window.

**P2-6. Women.** §6 says: "Where a woman is addressed by Hus, it is as an object of caution (Letter XXXV)." Letter XXXV is addressed to Martin. Letter II is addressed to nuns, on virginity, with a song. Restate the sentence.

**P2-7. A dropped hedge.** §7 item 1 says Seifferth "says they were first printed" in the 1535 folio. Seifferth hedges: the footnote at line 306 reads, in the scan, "These doenments leem to have been fint printed" ("seem"). Also, lines 8267–8268 read "Fasciculus Berum Expetendarum et Fugiendarum", so the title is legible only with one misread letter.

**P2-8. Piccolomini duplicated pages.** The scan repeats page runs: 3889/4513, 4056/4664 and 4138/4742 carry the same text. The sect chapter is interleaved with the Žižka chapter (4300–4345). Add this to the scan-quality note in row 11 and §7 item 3.

**P2-9. "every file in cic/texts/ (322)".** The 322 counts directory entries. It includes five metadata files, `INDEX.sqlite` and `_intake/`. The shelf holds 315 text files (277 `.txt` and 38 `.xml`).

**P2-10. Open_Gaps.**

- Entry 8(d) cites `records/worlds.yaml`, which does not exist. The registry is `records/worlds/<code>.yaml` (root README).
- Entries 5 and 13–14 duplicate each other; so do 15 and 20, and 16 and R1.
- Entry 16 says a request "is in `Open_Gaps_Tracking.md`" from inside that file.

These are append-only, so resolve them by cross-reference, not by deletion.

**P2-11. Narration and attribution in Doc_02.**

- §1: "Its Hus section has now been checked for existence and structure" is process narration. State the finding instead.
- §2: "Workman writes that 'Everything Hus writes …' in quoting Bishop Creighton" should credit Creighton, as quoted by Workman (1361–1362).
- The "Slav and Teuton" quotation (Hussite Wars 2036) comes from row 17, which is at B.

**P2-12. Row 14's Comparandum Note.** The note says the Latin "does not support" Gillett's claim that Piccolomini "knew all the circumstances". What the Latin shows is that Piccolomini names Poggio as his source (4063). "Not supported" is a stronger claim than the text shows. Write "rests on Poggio's letter, not on presence".

## Coverage checks (Framework V7.4, Doc_02 review requirement)

**Ten-item relative-recall test.**

*Instrument:* the reviewer's own knowledge of the standard Hussite bibliographies (Kaminsky 1967; Šmahel, *Die Hussitische Revolution*, 2002; Fudge 2010). This is independent of the build, but it is not a document read this round. The network was not used.

| # | Work | In Registry? |
|---|---|---|
| 1 | Palacký, *Documenta Mag. Joannis Hus* (1869) | No (only request R4) |
| 2 | Peter of Mladoňovice, *Relatio* | Yes, row 30 |
| 3 | Lawrence of Březová, Hussite chronicle (Goll, *Fontes rerum Bohemicarum* V, 1893) | Yes, row 34 |
| 4 | Chelčický, *Síť víry* | Yes, row 35 |
| 5 | Goll, *Quellen und Untersuchungen* (1878–82) | Yes, row 33 |
| 6 | Kaminsky, *A History of the Hussite Revolution* (1967) | Yes, row 36 |
| 7 | Šmahel, *Die Hussitische Revolution* (2002) | No |
| 8 | Loserth, *Hus und Wiclif* (1884; English 1884) | No |
| 9 | Brock, *The Political and Social Doctrines of the Unity of Czech Brethren* (1957) | No |
| 10 | Fudge, *The Magnificent Ride* (1998) | No |

Recall = 5/10.

**PRESS question**, asked verbatim: "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."

Answer, with the recommended disposition for the build thread:

1. Palacký, *Documenta Mag. Joannis Hus* (Prague, 1869). A Latin and Czech original, public domain by date. Row it, C, Native.
2. Loserth, *Hus und Wiclif* (1884; English trans. M. J. Evans, *Wiclif and Hus*, 1884). Public domain by date. Doc_02 already relies on it. Row it, C, Native.
3. Brock (1957). In copyright. Row it, C, Native, consultation only.

## What I could not verify

- The Piccolomini preface sentence (that he partly saw and partly heard), and the dedicatee. The scan is too garbled to locate them with confidence.
- The Latin of the *Ratio*'s Preface at 1156–1192, beyond the 1433 and 1457 passage at 1140–1145 and 4086–4096.
- Gillett's footnote naming the "chancellor of New Prague" (17684, columns interleaved; he cites a "Diarium"). The identification with Lawrence of Březová is plausible, and Doc_02 rightly does not claim it is proved.
- B rows 5, 6, 8, 12, 15, 17, 19 and 21: only the structure claims were checked, not their full contents.
- The existence and public-domain status of the R1–R9 items outside the vendored texts. These were not checked externally in this round, which is consistent with their being marked as leads.
- The Adamite point in P1-5 rests partly on reviewer knowledge of Kaminsky. It is not a text read here, and the build thread should check it against a modern instrument.
