# Open Gaps — The Society of Jesus

Append-only ledger for this world's build. Entries are numbered and dated; a merged entry's number never changes. Cross-references cite subject and date, not a bare number. The world's file-code is `jes`.

---

## OG-1 — Institutional voice after 1556 is thinner than a first reading of the corpus suggests (2026-09-30)

**Source:** `Step0_Review_Round3.md`, finding S1.
**Status:** Open. Binding on Doc_02.

The vendored volumes cover the order's institutional voice as follows, checked against their own title pages:

| Vendored file | Title page reads | Covers |
|---|---|---|
| `lainez_epistolae-et-acta-v1-lat_1912.txt` | TOMUS PRIMUS 1536-1556 | Ends before Lainez's generalate (1558–65) |
| `polanco_chronicon-v1-lat_1894.txt` | TOMUS QUINTUS (1555); body opens ANNUS 1555 | The single year 1555 |
| `nadal_epistolae-v1-lat_1898.txt` | TOMUS PRIMUS (1546-1562) | Nadal's letters to 1562 |
| `salmeron_epistolae-v2-lat_1906.txt` | TOMUS PRIMUS 1536-1565 | Salmeron's letters to 1565 |
| `salmeron_epistolae-v3-lat_1906.txt` | TOMUS SECUNDUS 1565-1585 | Salmeron's letters to 1585 |

Institutional voice is dense to 1556, partial to 1562, and after that rests on one correspondent (Salmeron) to 1585. Nothing vendored gives the voice of Lainez as General, of Borgia (1565–72), or of Mercurian (1573–80). Doc_02 must not look for Lainez's generalate or Polanco's earlier years in these files. Doc_02 either narrows its institutional claims after 1556 to what is held, or acquires later volumes first.

**Disagreement between review rounds.** Round 2 of the Step 0 review supplied a re-dating of "Lainez (General 1558–65) ... c. 1580" without checking the volumes' title pages. Round 3 found it wrong. The title pages above support Round 3. The Round 2 wording is not carried into any document.

## OG-2 — Vendored file headers contradict the corpus-map on second-witness status (2026-09-30)

**Source:** `Step0_Review_Round3.md`, finding L3 (carried from Round 2, finding m4).
**Status:** Open. Owner: Library thread.

The provenance headers of the files vendored on 2026-09-25 say the text is "a second witness, never primary evidence". That contradicts the corpus-map and `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` point 5 for the clean-scan files. Under that ruling only the 1606 Constitutions, Nadal's *Adnotationes* and Ribadeneira's 1572 life are held at second-witness status for scan quality. Files affected among this world's works: `lainez_epistolae-et-acta-v1-lat_1912.txt`, `nadal_epistolae-v1-lat_1898.txt`, `nadal_scholia-in-constitutiones-lat_1883.txt`, `polanco_chronicon-v1-lat_1894.txt`, `salmeron_epistolae-v2-lat_1906.txt`, `salmeron_epistolae-v3-lat_1906.txt`, `ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt`. The corpus-map notes are the authority. The headers are to be corrected at source by the Library thread.

The second half of L3, the "Correction (2026-09-25)" narration in the Constitutions and *Adnotationes* corpus-map notes, is no longer present in `cic/corpus-map/`.

**Resolution, 2026-09-30:** see the entry "OG-2 resolved: the seven Latin file headers now state primary evidence" below.

---

## OG-3 — OG-2 resolved: the seven Latin file headers now state primary evidence (2026-09-30)

**Source:** commit c11c0801b; the headers of the seven files named in OG-2.
**Status:** Resolved. Owner was the Library thread.

Each of the seven headers now says that, under the intake rule (scan quality decides quotability, not language), the Latin text is primary evidence for the movement, and that wording is to be checked against the page image before it is quoted. None of the seven headers still says "second witness". The corpus-map notes for the clean-scan files are consistent with the headers. The second half of OG-2, the narration in the corpus-map notes for the Constitutions and the *Adnotationes*, is no longer present in `cic/corpus-map/`. The header rule asks for a check against the page image. No page image was available to Doc_02, so its Latin quotations are checked against the scan text only.

## OG-4 — Ignatius's own vendored letters run to March 1548, not to 1547 (2026-09-30)

**Source:** `Doc_02_Source_Ecology.md` §1 and §6; Registry rows 9 and 16.
**Status:** Open. Owner: project lead (change order to Step 0 wording).

Step 0 §4 (the global and missionary sourcing gap) and the source dossier say that Ignatius's own vendored letters end in 1547. That is right for the O'Leary/Goodier English selection. The Latin *Monumenta Ignatiana* volume (Tomus Primus, 1903) runs further. Its last dated letter heading in the body reads "ROMA 28 FEBRUARII 1548" (line 38789), with one more undated heading for "exeunte Februario aut ineunte Martio 1548" (line 38859). Ignatius's own letters after March 1548 are not vendored. The years 1548–56 are the gap (Registry row 49). Doc_02 states the later date.

## OG-5 — The Generals speak on the shelf as senders of register copies to Salmeron (2026-09-30)

**Source:** Registry rows 26, 67 and 69; `Doc_02_Source_Ecology.md` §6.
**Status:** Open. Binding on Doc_02. The wording of Step 0 §4 (the global and missionary sourcing gap) and of the first entry above (institutional voice after 1556) needs a decision from the project lead.

Step 0 §4 (the global and missionary sourcing gap) and the first entry above (institutional voice after 1556) say that nothing vendored gives the voice of Lainez as General, of Borgia or of Mercurian. That is true of any volume by them. It is not true of every page. Salmeron's two volumes print letters under their names to Salmeron, drawn from the Generals' registers. Counted from the scan's headings, there are about twenty headed Lainez in Tomus Primus (some before his generalate), about 45 headed Borgia, about 76 headed Mercurian and about 17 headed Aquaviva in Tomus Secundus. Three samples were read: Lainez to Salmeron, Rome, 23 June 1560 (Spanish); Mercurian to Salmeron, Rome, 9 October 1573 (Italian); and Borgia's of 4 March 1565 (Italian), which speaks of the vicar in the third person. The Lainez Praefatio says that most letters of his generalate were written in his name by secretaries. So the voice is the office's, in one man's correspondence, and mostly in Italian and Spanish. The gap after 1562 and 1585 stands. Doc_02 §6 states the fuller fact. Whether Step 0 §4 and the first entry above are to be amended by change order is a decision for the project lead. Nothing in Step 0 or the first entry has been edited.

## OG-6 — The Article 4 floor, clause by clause, and what it cannot reach (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §8.
**Status:** Open.

Doc_01 §8 quotes the five commitments verbatim from Constitution V2.3 and sets out what the founders' generation shows. Commitment 4 is largely shown, in Ignatius's compilation of the Gospel scenes, in Faber, and in a catechetical text attributed to Xavier. Commitments 1, 2, 3 and 5 are shown in substance. Some clauses are shown only in Coleridge's English rendering of material attributed to Xavier, and its attribution to Xavier is Inferential/Thin. These clauses are not found in the Society's own words: "of all that is, seen and unseen", "Light from Light", "true God from true God", "eternally", "Lord and giver of life". They are silent, not denied. Nothing on the shelf contradicts a commitment. The check cannot reach two things. One is the later mission voice, including the Chinese and Malabar Rites. The other is the order from 1585 to 1650. Both need sources from section B.

## OG-7 — The strand finding is a recommendation, and awaits the project lead (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §5 and §9 (the strand finding).
**Status:** Open. Decision for the project lead.

Doc_01 §5 records strand-singular as the builder's finding and as a recommendation. It gives the case for two strands, a European one and a mission one, at full strength. No later document should treat the finding as settled until the project lead confirms it or orders two strands. Doc_04 tests whichever is chosen. The finding rests on the absence of a mission voice after Xavier's death, and it is Inferential/Thin.

## OG-8 — Living Tradition Status (Article 29) is triggered and not confirmed (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §1 and §9 (Living Tradition Status).
**Status:** Open. Decision for the project lead.

Triggered by the census's `living: true` and by the fact that every vendored edition of the Society's own texts is by a member of the Society. Not confirmed. A world touching a living tradition is not freeze-eligible until Article 29 confirmation is done. The tradition or traditions to name are not decided here.

## OG-9 — The Representative is not decided (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §9 (the Representative).
**Status:** Open. Escalation category: Representative identity.

No decision is made or implied. The shelf's voice is fullest for 1540–1562 and thinnest after 1585 (Doc_02 §6). The choice goes to the project lead as a packaged choice among two to four candidates with trade-offs, at the proper step.

## OG-10 — `jes` is not registered in `records/worlds/`, and the cost ledger is not opened (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §9 (registration of `jes`); `build/jes_Build_State.yaml`.
**Status:** Open. Owner: project lead.

The file-code `jes` was assigned by the project lead. `records/worlds/jes.yaml` does not exist, and nothing was added to `records/`, `packages/`, `cic/texts/` or `cic/corpus-map/`. `build/jes_Build_State.yaml` exists with Steps 0 to 2 recorded. No cost ledger was opened, and the session's token spend was not measured.

## OG-11 — The Canisius scan and its file header (2026-09-30)

**Source:** Registry row 34; `Doc_02_Source_Ecology.md` §7 (the Canisius scan).
**Status:** Open. Owner: Library thread.

The corpus-map note holds *A Summe of Christian Doctrine* (1622) as `tradition`, `assigned`, with no scan-quality flag. Reading it shows long s printed as f, marginal Scripture references interleaved with the text, and letters misread (Registry row 34). The quote gate reads ſ as s, but the scan prints f for ſ in many places, and the marginal noise breaks continuous passages. The file header says the scan was not checked beyond the opening pages. Doc_02 uses it only by paraphrase and does not decide whether it is garbled under the Library's rule of 2026-09-25. The Library should rule. A clean witness of the same work is a request (R8).

## OG-12 — Boero's Part the Second is Faber's diary in English (2026-09-30)

**Source:** Registry rows 19 and 20; `cic/corpus-map/the-society-of-jesus.yaml`, the Boero entry.
**Status:** Open. Owner: Library thread.

The corpus-map note says it is not established how much of the *Memoriale*'s own text the Boero volume quotes. Part the Second (from line 9212 of the file) is an English rendering of the whole diary, from a Latin lithograph, condensed in places to match Boero's Italian. The map holds the whole volume as `context`, `provisional`. The Library may want a work-level entry for Part II as a translation of Faber's own text. Doc_02 treats it as an English witness of row 18 and does not quote it as Faber's words.

## OG-13 — File-level points for the Library (2026-09-30)

**Source:** the vendored files named below; Doc_02 §1 and the Registry.
**Status:** Open. Owner: Library thread.

- `faber_memoriale-lat_1873.txt`: the title page prints the year 1872 (line 178). The editor's Preface is dated 8 December 1873 (lines 413–414). The header says 1873. The scan also prints the diary's opening year as "1842" (line 283), where the sense requires 1542.
- `polanco_chronicon-v1-lat_1894.txt`: the filename says 1894 and "v1". The header and title page say Tomus Quintus, printed 1897.
- `salmeron_epistolae-v3-lat_1906.txt`: the filename says 1906, and the title page says 1907.
- `francis-xavier_life-and-letters-v1_coleridge1872.txt`: the text gives the bull as "Sept. 17, 1540", and the contents page gives "Sept 27, 1540" (row 21). The Lainez editors give 27 September.
- The census's `dates` field for VI.11 reads "1540-1650". No change is proposed.

## OG-14 — The census's Xavier story and the shelf (2026-09-30)

**Source:** `cic-website/data/world-census.json`, VI.11, `documentedStories`; Registry rows 23 and 43.
**Status:** Open. Owner: project lead (census); Doc_09.

The census's story "Xavier Writes from Kagoshima" is rated Tier 1 and marked "from reference summaries; primary text not yet read". It cites the Costelloe translation (letter 90). The shelf holds the same letter in Coleridge's translation (Letter LXXIX, "To the Society at Goa", Cagoxima, 5 November 1549; Registry row 23). The census's quoted wording ("the best who have as yet been discovered") is not in Coleridge's translation, and Coleridge's own wording is different. When Doc_09 uses this story, it must quote one translation and name it. The census's "three hundred thousand" for the Japanese church and "some two hundred and fifty" colleges by 1600 have no support on the shelf and were not tested.

## OG-15 — The Chinese and Malabar Rites controversy has no source on the shelf (2026-09-30)

**Source:** Step 0 §4 (the rites controversy); Registry rows 51 to 53.
**Status:** Open. Binding on Doc_01 and Doc_02.

Doc_01 treats the controversy as an in-window scope boundary and carries its dates from Step 0 §2 A3 unverified. No vendored source confirms them. No confidence tag is assigned to them. Requests R3 and R4 in section B would supply sources.

## OG-16 — Author Gravity risks for Doc_04 (2026-09-30)

**Source:** `Doc_01_World_Identification_Boundaries_Orientation.md` §3.
**Status:** Open. Binding on Doc_04.

Doc_01 §3 lists seven candidate gravities, each with a named Author Gravity risk: the Principle and Foundation rests on Ignatius alone; the discernment rules are a manual and not a record of use; obedience to the hierarchical Church is Ignatius's rule for the exercitant; help to souls rests on one instruction; being sent rests on Xavier through Coleridge; education rests on no vendored college rule; and adaptation to other cultures has no vendored source. Doc_04 must test them against the Registry's Native rows only.

## Section B — Source requests to the Library thread (no source has been fetched)

A garbled scan stays a second witness. A clean public-domain original in Latin, Spanish, Italian or Portuguese counts as primary evidence under the 2026-09-25 intake ruling. The items below are leads from the builder's knowledge and from the bibliographic footnotes and prefaces in the vendored apparatus. **None has been rights-checked or verified to exist as a public-domain scan. The Library thread should verify each.** Priority order.

- **R1. The *Jesuit Relations*** (Thwaites, 1896–1901, 73 volumes). The largest missing body of the Society's own missionary voice inside the window. Named in the census (Registry row 42).
- **R2. The Formula of the Institute, the bulls and the decrees of the general congregations.** Lead: *Institutum Societatis Iesu* (Florence, 1892–93). Named by the vendored MHSI preface (rows 14, 38). It would also give the Society's own text of the 1540 and 1550 charters, and the decrees from 1558 on.
- **R3. The *Ratio Studiorum* of 1599, in Latin.** Lead: the *Monumenta Germaniae Paedagogica* edition (Berlin, 1887–94), and the MHSI *Monumenta Paedagogica* named in the Lainez preface (rows 45, 46).
- **R4. China and India.** Ricci's own writings and Trigault's *De Christiana expeditione apud Sinas* (1615); de Nobili's writings; and the documents of the rites controversy of 1623, 1627–28 and 1645 (rows 51–53).
- **R5. The Generals' own volumes.** *Lainii Monumenta*, later volumes (row 48); the MHSI *Sanctus Franciscus Borgia* volumes (row 47). They would let the Generals speak for themselves after 1558, and not only through register copies to Salmeron.
- **R6. Ignatius's letters after March 1548.** The other volumes of *Monumenta Ignatiana*, Series I (row 49). The Spanish autograph of the *Exercises* and the Latin versions of 1548 (row 72).
- **R7. Xavier in the original languages.** *Monumenta Xaveriana* (row 41). Also the source of Coleridge's "Explanation of the Creed", for which he names none (rows 22, 62).
- **R8. A clean witness of Canisius, of the Constitutions and of the *Adnotationes*.** For the Constitutions: the critical edition (row 40). For Canisius: a legible edition of the Latin catechism or a cleaner scan of the English (row 34). For Nadal's *Adnotationes*: a cleaner edition of the Latin (row 29).
- **R9. The letters of Ignatius's first companions.** The MHSI volumes for Broët, Le Jay, Codure and Rodrigues (row 64), and the *Epistolae Mixtae* and *Litterae Quadrimestres* (row 46).
- **R10. Polanco's other tomi and Nadal's own *Opuscula* and *Chronicon* (rows 50, 66).** They fill 1540–1554 and 1556–76, and Nadal's own diary.
- **R11. Salmeron's own commentaries** (Madrid, 1597–1602; row 63). A large body of Jesuit exegesis from inside the window.
- **R12. A Latin witness of the *Autobiography*.** The Codretto translation (row 71).
- **R13. The litterae annuae** (row 44). A genre lead only.
- **R14. Bibliographic instruments for the field-bibliography sweep.** Sommervogel, Alegambe and Southwell, the *Archivum Historicum Societatis Iesu* bibliographies (rows 57, 58). These are instruments, not sources.

## Section C — Process record

17. **Drafting status, 2026-09-30.** Doc_01, Doc_02 and the Registry are drafts. No independent review has run. No document has been approved to proceed, and none is frozen.

## Section D — Open items carried from the phase documents

18. **Doc_01 §9 and Doc_02 §7** carry the six binding points of Step 0 §4 forward. Four are handled in Doc_02 §7. The sourcing gap is handled in Doc_02 §6 and in the entries on Ignatius's letters to March 1548 and on the Generals' register copies. The selection rationale is disclosure only.
19. **The Trent split** is settled at the corpus-map level and is not reopened.
20. **The census `dates` field and propagation.** The census entry needs no date change. The census's story notes are in OG-14. Nothing in `cic/corpus-map/`, `records/` or `packages/` was edited.

## Section E — Candidates on other worlds' shelves (no Registry row; the project lead's authorisation is needed before any is placed in this world)

Placing a work on this world's shelf is a cross-world decision. It is not made here. The files below are assigned to other worlds by the corpus map. Counts are of matches for the Jesuit words, and none of these files was read beyond a first look at the matches.

- **E1. Bellarmine's devotional works** (`bellarmine_eternal-happiness-of-the-saints_dalton.txt`, `bellarmine_joys-of-the-blessed_foxton1722.txt`, `bellarmine_minds-ascent-to-god_1925.txt`, `bellarmine_souls-ascension-to-god_hall1703.txt`). Assigned to the Tridentine Church as `tradition`. The file matches the Jesuit words six times, and the matches were not read. A Jesuit voice that this world's shelf does not hold, if the author is confirmed as a member of the Society. Cross-world placement needs the project lead.
- **E2. Sarpi, *History of the Council of Trent*** (`sarpi_history-of-the-council-of-trent_brent1676.txt`), assigned to the Tridentine Church. It names Lainez 14 times and Salmeron 6 times, and mentions the Jesuits 8 times. A Venetian outsider's account of the Jesuit theologians at Trent.
- **E3. *The Roman Breviary*** (`roman-breviary_bute1908.txt`), assigned to the Tridentine Church. It mentions the Society 8 times, Xavier 4 times and Borgia 5 times. Possible liturgical evidence for the Jesuit saints.
- **E4. Barlow, *Brutum Fulmen*** (`barlow_brutum-fulmen_1681.txt`), assigned to the Tridentine Church. It names Loyola, Bellarmine and Suárez. An English Protestant work. Hostile witness.
- **E5. The Roman Catechism** (`council-of-trent_roman-catechism_mchugh-callan1923.txt`), assigned to the Tridentine Church, one match. The Church's own catechism beside Canisius.
- **E6. Smith, *Account of the Greek Church*** (`smith-thomas_account-of-the-greek-church_1680.txt`), assigned to Orthodoxy under the Ottomans. It mentions the Jesuits 16 times. An Anglican account of Jesuits in the Levant.
- **E7. Calvin, *Letters*, vols. 1, 2 and 4, and the *Institutes*, vols. 2 and 3**, assigned to the Reformed cities. Seven matches in vol. 4, and a few elsewhere.
- **E8. Van Braght, *Martyrs Mirror*** (`van-braght_martyrs-mirror_sohm1886.txt`), assigned to the Anabaptist and Hussite worlds. It mentions the Jesuits 38 times, mostly as persecutors of the Anabaptists.
- **E9. A bound-in study of Japan inside the Boyd volume** (`boyd_ecclesiastical-edicts-theodosian-code_1905.txt`, assigned to Donatism). The file's header says the volume binds three separately authored studies. The third is "The International Position of Japan as a Great Power" (Hishida, 1905). It mentions the Jesuits 10 times, for example Xavier's arrival in 1549 (the scan prints "Koyoshima") and an estimate of native Christians in 1581. A secondary study of 1905. The Library may want to say whether it should be split from the Boyd file.
- **E10. Lützow, *Bohemia*, and Gillett, *Life and Times of Huss*, vol. 2**, assigned to the Hussite world. They mention the Jesuits 48 and 53 times, in Bohemia after the Society reached Prague in 1556. Most matches are probably after the window.

## Section F — The binding points of Step 0 and the questions of Doc_01, restated for the ledger

21. **The Constitutions and Nadal's *Adnotationes* are vendored but not primary-quotable, and are binding on Doc_02 (2026-09-30).** Both the 1606 Latin Constitutions and Nadal's 1595 Latin *Adnotationes* are vendored and close a real sourcing gap. Both are flagged as garbled scans under the scan-quality ruling of 2026-09-25 and held at second-witness status until a cleaner edition is vendored. Doc_02 does not quote either verbatim as primary text. It cites them as second-witness institutional material (Registry rows 29 and 36). The Constitutions still lack any public-domain English translation, since the Ganss translation of 1970 and 1996 is in copyright (row 39). Requests R8 and R2 in section B.
22. **Faber's own *Memoriale* is vendored directly, and is binding on Doc_02 (2026-09-30).** Faber's own spiritual diary is vendored in Latin as a genuine primary Faber voice, not only Boero's biography of him. Doc_02 cites the *Memoriale* itself as Faber's primary voice. Boero's volume remains available as context and biography alongside it, and its Part the Second gives the diary in English, in a condensed form (Registry rows 17 to 20; the Boero entry above).
23. **The Trent split is settled and needs no action (2026-09-30).** The corpus-map assigns the shared Waterworth Trent Canons and Decrees `tradition`, `assigned` for the Tridentine Church and `context`, `assigned` for this world. It is settled at the corpus-map level. Doc_02 uses the text only for the Article 4 context (Registry row 35).
24. **The Chinese and Malabar Rites controversy is in-window, not excluded, and is binding on Doc_01 (2026-09-30).** Ricci, de Nobili and the events of 1623, 1627–28 and 1645 fall inside 1540–1650. Doc_01 treats the controversy as a real scope boundary to engage, not an exclusion to disclose. No source for it is on the shelf (the rites entry above).
25. **The global and missionary sourcing gap after Xavier's death is binding on Doc_02 (2026-09-30).** The vendored corpus's own missionary voice is concentrated in the founding generation, to Xavier's death in 1552. Institutional material is dense to 1556, runs to 1562 through Nadal's letters, and after that rests on Salmeron's letters alone, to 1585. The *Jesuit Relations* should be assessed before any claim of sustained global reach across the full window. Doc_02 §6 states the gap. The corrections to the wording of this point are in the entries on Ignatius's letters to March 1548 and on the Generals' register copies.
26. **The unattributed selection rationale is disclosure only (2026-09-30).** Neither the desert-monastic echo nor the Catholic-renewal framing has a findable record of the project lead's own reasoning. Both are presented as the builder's own reading, not the project lead's verified words. Doc_02 does not use either as an argument.
27. **Living Tradition Status (Article 29): which present-day tradition or traditions the confirmation names, and by what criteria (2026-09-30).** Open, for the project lead. See the entry above on Living Tradition Status.
28. **Vendored works assigned only to other worlds that mention the Jesuits, and the census notes on the shelf, are recorded in this ledger (2026-09-30).** They are in section E, and the census notes are in the entry on the census's Xavier story. Placing any of them here needs the project lead.
