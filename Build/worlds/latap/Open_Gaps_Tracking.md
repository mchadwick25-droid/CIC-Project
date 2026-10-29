# Open Gaps — The Latin Apologists

Append-only ledger for this world's build. Entries are numbered and dated; a merged entry's number never changes. Cross-references cite subject and date, not a bare number. The world's file-code is `latap`.

---

## OG-1 — `safety_adjacent` is not set on the `latap` registry entry (2026-10-29)

**Source:** `records/worlds/latap.yaml`; `Build/Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md` (entry `latap`).
**Status:** Open. Owner: the project lead.

The file-code `latap` is registered as a candidate world, census id `latin-apologists`. The registry log records that the code was ratified on 2026-10-29. Step 0's header still reads "none assigned" and is not edited. No `safety_adjacent` value is set. Handoff check 1 (identity) fails until the project lead sets it.

## OG-2 — Step 0 and the dossier count the shelf at one moment; the shelf has grown (2026-10-29)

**Source:** `Step0_Movement_Scope_Confirmation.md` §3 B1 ("43 works on 96 rows"); the Source Readiness Dossier §1; `cic/corpus-map/latin-apologists.yaml` on `main` at the start of this build (100 rows).
**Status:** Open. Owner: Library thread.

Step 0 and the dossier are point-in-time under their own wording and are not edited. The bucket stood at 100 rows when the library stage began; the four-row difference from 96 is not itemised here. The library stage added 17 rows: 8 context rows for ancient testimony (Jerome's *De viris illustribus* chapters 18, 53, 58, 79 and 80, Gennadius's chapter 15, and Jerome's Letters 70 and 84); 8 rows for modern scholarship (Harnack, Schanz-Hosius-Krueger, Brewer, Monceaux I to III, and Audollent's two scans); and one Latin-only row for Lactantius's lost-works fragments. Doc_02 states the current counts.

## OG-3 — The ANF07 "Fragments of Lactantius" are two poems of uncertain authorship, not fragments of lost works (2026-10-29)

**Source:** `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` div2 `iii.vi` (the heading is "Fragments of Lactantius"; its three divisions are The Phoenix, A Poem on the Passion of the Lord, and a General Note whose text says there is no manuscript authority for ascribing the poems to Lactantius); `lactantius_de-opificio-de-ira-carmina-lat_brandt-csel27-1.txt` lines 10119 (CARMINA), 10126 (DE AVE PHOENICE), 10806 (DE PASSIONE DOMINI) and 11021 (LIBRORVM PERDITORVM FRAGMENTA).
**Status:** Open. Binding on Doc_02. The finding cuts against Step 0 §3 B1 and the dossier §1, so it goes to the project lead as an unresolved tension the pipeline cannot close on its own.

The corpus-map pairing was wrong in both directions. The English "Fragments of Lactantius" is the Latin *Carmina*, not the lost-works fragments, and the Latin *Carmina* have an English twin, contrary to the map's earlier note. Step 0 §3 B1 counts the ANF div2 `iii.vi` at 3,932 words as Lactantius's fragments; a recount by the same method reproduces 3,932 for the whole division, which is the two poems and the General Note. Step 0's roster claim "Lactantius 4 works" and the original-seven total of 464,840 words rest on that count. The staging rows are corrected (the English row is retitled, set to `provisional`, and paired with the Latin *Carmina*; the Latin lost-works fragments are a separate Latin-only row). Step 0 is not edited. Whether Step 0 is reopened to restate its counts is the project lead's decision.

## OG-4 — The Library notes say the patristic text hosts are blocked; archive.org and the others answered on 2026-10-29 (2026-10-29)

**Source:** `Build/Ministry/Operations/Standing/CiC_Source_Research_Practice.md` ("Known blocker"); `Build/worlds/_cross-world/CORPUS-USE.md` (header).
**Status:** Open. Owner: the source-research thread.

From this build session an HTTPS request returned HTTP 200 for archive.org, ccel.org, newadvent.org, tertullian.org, en.wikisource.org, la.wikisource.org, gutenberg.org and raw.githubusercontent.com. archive.org item metadata and full-text files were downloaded. No host was denied, so no workaround was needed and `read_documentation` was not consulted. The standing note may be out of date for some sessions. This changes which leads in OG-7 are acquirable now.

## OG-5 — The new staging keys wait in staging; the merge keeps eight fields (2026-10-29)

**Source:** `cic/engine/corpus_map_merge.py` (`_KEEP`); the library-stage ruling that rows are born complete.
**Status:** Open. Owner: the tooling change order, not yet landed.

Each corpus-map row for this world now carries, in its `_staging/` file, the additive keys `locus_ids`, `language`, `date` (a window, its source and a `formation_confidence` tag, or "unknown" with what was checked), and `voice_of` where the role is not `tradition`. The merge writes only `row_id`, `work`, `author`, `source_file`, `locus`, `role`, `confidence` and `note`, so the bucket `cic/corpus-map/latin-apologists.yaml` does not show them. That is expected. `corpus_map_merge.py --check` accepts the extra keys. A staging row's `voice_of` is a list of `{author, loci}` entries. `language` is an ISO 639-3 code, or a list of two when one row spans two languages (the Robinson Passion).

## OG-6 — Stale references to the retired slug `tertullian-s-voice` (2026-10-29)

**Source:** `cic/texts/perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` (header content note); `cic/corpus-map/_staging/anf03_tertullian.yaml` and `perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml` (notes); Step 0 §2 A5 and the §4 obligation on the Tertullian and Article 21 boundary (LPC's `world_core` record).
**Status:** Open. Owner: Library thread for the file header and the staging notes; LPC's owner for its record.

The slug names the census entry that merged into this one. The Robinson file header still says the Passion is assigned to it, and calls the file a second witness to an excluded comparandum of another world. The Robinson staging note and two Passion and Apology notes in `anf03_tertullian.yaml` named it and are now rewritten without the slug. One note remains, on the Post-Apostolic House-Church row of the Apology, which is another world's row. The file header is the Library's record and is not edited here.

## OG-7 — Leads not vendored, now reachable (2026-10-29)

**Source:** `Source_Registry.md` rows 68 to 73; the Source Readiness Dossier §4.
**Status:** Open. Owner: the source-research thread.

Not vendored: Jerome's *Chronicle* in a critical edition (the dossier records two disagreeing statements about Helm 1913); Augustine's *De haeresibus* (an 1721 edition seen); Lactantius's *De mortibus persecutorum* in Latin (CSEL 27 part 2 fascicle 2; IJC's side of the split); Ebert (1868/70) and Norden (1897) on Minucius Felix; Bardenhewer, Teuffel-Schwabe, Massebieau and the other dating scholars reported at second hand; Tertullian's CSEL 69 and 70 (in copyright; not acquirable). Vendored in this stage because they were located and verified: Harnack's *Chronologie* Band 2 (1904), Schanz-Hosius-Krueger Teil 3 (1922) and Brewer's *Kommodian von Gaza* (1906).

## OG-8 — The CIL VIII Numidia cross-link is named, not verified (2026-10-29)

**Source:** the Source Readiness Dossier §2 (CIL VIII Supplementum, Numidia, Cagnat-Schmidt 1894, assigned to `donatism` only).
**Status:** Open. Owner: whichever Doc_02 reaches it first.

Arnobius's Sicca is in Numidia and Step 0 B5 names Numidia as one of the world's regions. No inscription was located or read against any claim this world makes. The file is not assigned here, and no Registry row is entered for it.

## OG-9 — Vendored files that mention these authors and are assigned only to other worlds (2026-10-29)

**Source:** a shelf search recorded in `Source_Registry.md` (saturation statement).
**Status:** Open. Placing any of them here needs the project lead or the Library thread's ruling.

Ranked by mentions of Tertullian, Minucius Felix, Arnobius, Lactantius or Commodian, the unassigned files with the most are: `npnf201_eusebius-church-history-life-of-constantine.xml` (280), `koch_cyprianische-untersuchungen-deu_1926.txt` (224), `audollent_carthage-romaine-fra_1901.txt` (206, now assigned here), `koch_cathedra-petri-deu_1930.txt` (197), `mansi_sacrorum-conciliorum-collectio-tomus-2-305-346-lat_welter-facsimile1901.txt` (169), `lucifer-cagliari_opuscula-lat_hartel1886-csel14.txt` (163), `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` (155), `benson_cyprian-his-life-his-times-his-work_1897.txt` (141) and `apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt` (132). None was read for a claim in this build. The Eusebius and Epiphanius volumes could bear on Tertullian and the New Prophecy.

## OG-10 — Neighbour re-confirmation of shared boundaries (2026-10-29)

**Source:** `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md` ("Neighbour re-confirmation"); Doc_01 §7.
**Status:** Open. Owner: the three neighbour worlds' own threads.

Doc_01 names three built neighbours: Post-Apostolic House-Church Christianity (`pahc`), Latin Pastoral-Congregational Christianity (`lpc`) and Imperial-Juridical Christianity (`ijc`). Each is asked to re-confirm its shared boundary from its own side. The request is logged in each neighbour's `Open_Gaps_Tracking.md`: `pahc` OG-44, `lpc` OG-114 and `ijc` entry 48, all dated 2026-10-29.

## OG-11 — Tertullian's *On Modesty* chapter XXII is cited by LPC as comparandum evidence (2026-10-29)

**Source:** `records/lpc/source/lpc.source.tertullian-de-pudicitia.md`; `records/lpc/force/lpc.force.decian-persecution-libelli-system.md`; `records/lpc/gravity/lpc.gravity.confessor-authority-vs-episcopal-peace.md`; Doc_01 §7.
**Status:** Open. Cross-world question. Owner: the project lead or the two worlds' threads.

LPC's Registry excludes Tertullian's corpus as a Named Comparandum, yet LPC's source record cites chapter XXII of *On Modesty* (`anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, lines 9554–9566, by LPC's own reading) as comparandum evidence, and two LPC records rest a sentence on it. *On Modesty* is on this shelf, co-assigned to Montanism, and the bishop it attacks is Contested. Nothing here is decided and no LPC record is edited. The weight the two worlds give the same chapter is not settled.

## OG-12 — Step 0 §4 item 7's overlap sweep is dated; the sweep was re-run for Doc_01 and the new LPC and PAHC uses are recorded (2026-10-29)

**Source:** Doc_01 §7; a case-insensitive search of `records/` for the five authors' names and titles.
**Status:** Open. Owner: the neighbour worlds' threads.

The re-run found the LPC use in OG-11 and one further PAHC use (`pahc.source.lucian-peregrinus` triangulates with Tertullian's *Apology* 39). It also found one PAHC wording item: `pahc.force.systematic-theological-mode-elsewhere` says the *Apology* opens a body of confident Latin defense, which Step 0 §4 rule (a) on the census phrases does not adopt. The wording item is carried to PAHC (OG-44 there) and is not edited. Matches in other worlds that were inspected are volume-title strings and the word "perpetual"; they were not each opened.

## OG-13 — Doc_01 open items carried forward (2026-10-29)

**Source:** Doc_01 §9.
**Status:** Open. Owner: the project lead for the questions; Doc_02 and later steps for the disclosures.

- *The strand finding* (§5): confirm strand-singular, or order two strands (outward and inward).
- *Representative.* Decided later in the build, at Doc_10, as a packaged choice among two to four candidates.
- The *Octavius* date, as two Contested ranges, with a `contested_claim` record.
- Commodian's date, Contested, with the fifth-century view disclosed wherever his date is used.
- Minucius Felix's Christological silence, disclosed at the count in §8.
- Lactantius's pneumatology, chiliasm, the Book II passage on a second being, and the manuscript-only dualist passages (Step 0 §4 obligation 5).
- Arnobius's anthropology and the correct attribution of the dream-and-bishop story to Jerome's *Chronicle* (Step 0 §4 obligation 2).
- The seven New Prophecy works as a disclosed later-career complication, two of them pre-break (Step 0 §4 obligation 8). The Passion's date and compiler (Step 0 §4 obligation 9).
- *Cross-world items.* LPC's records cite Tertullian's *On Modesty* chapter XXII as comparandum evidence (§7), and whether the two worlds hold it at the same weight is a cross-world question. A PAHC force record says the *Apology* "opens" a body of Latin defense, which Step 0 §4 obligation 1, rule (a), does not adopt (§7).

## OG-14 — Step 0 §4 obligations: dating poles and the Commodian ranges (2026-10-29)

**Source:** Step 0 §4 dating tables.
**Status:** Open. Owner: Doc_01 wording (met) and Doc_02 disclosures.

- **Minucius Felix and Commodian's dating — cited judgments supplied here; the roster question settled by the approved slate; awaiting independent review (binding on Doc_01's wording).** The census flags both as barely datable in one sentence: "Three of the five are barely datable: Minucius Felix within a century, Commodian within three centuries; ..." (the census sentence goes on to Tertullian's dates and names only two of its "three"). This item's rule was that an author judged more likely to fall outside the 197–320 window is reassigned, not retained by default. The Library decision log entry "Window slate for the Greek and Latin Apologists approved," quotes the project lead's words on the slate shown to him as "yes, approve the slate and proceed." For this world the slate reads: "Minucius Felix (Contested, 160-192 or 200-250; the Roman church entry I.33 makes no claim on him, so nothing moves), Commodian (Contested, with the minority 5th-century thesis disclosed), Arnobius, Lactantius, Tertullian's Montanist-era works, Perpetua." The rule that entry states is that a work whose plausible date range overlaps its world's window "stays, tagged Contested, with the dispute stated where the work is used." Both authors therefore stay. What follows is the evidence behind the two `Contested` tags.
- Pole | Range | Proposals, with the source that reports them
- A. Before Tertullian's *Apology* (late 197) | c. 160–192 | Ebert 1868/70 (180–190), Keim (180), Aubé (c. 177), Krüger (under Marcus Aurelius), Schanz's earlier view (before 161), Schwenke, Reck and Reinach (before Tertullian) — all in Monceaux I, lines 32371–32395, note 10. Norden 1897, Waltzing, Baehrens (before 163), Boenig and Dombart, as listed in Schanz–Hosius–Krüger III (1922), pp. 267–269. Bardenhewer 1901, on Ebert's view, the start of Commodus's reign (180–192).
- B. After the *Apology* | c. 200/213–250 | Coxe in ANF04, "[a.d. 210.]" and "Possibly as late as a.d. 230" (lines 17040–17062). Boissier, c. 215. Monceaux 1901: "entre 213 et 250" (I, lines 33092–33095). Massebieau 1887, 238–246. Neumann, c. 248. Harnack 1904: not written in the second century, and more probably between Maximinus Thrax and Decius (c. 235–249), inside an overall range of 160 to 250 (II.2, pp. 324–330).
- Source | Range proposed | Inside c. 197–320?
- Dombart, CSEL 15 (1887), preface, lines 149–151: "media fere parte tertii post Christum saeculi"; his note at lines 11904–11908 reads the "seventh persecution" as Decius's (249–251) | mid-third century | Inside
- Ebert 1868/70: *Carmen apologeticum* 249, *Instructiones* a few years earlier (Monceaux III, lines 37333–37337); Teuffel–Schwabe 1891 has *Instructiones* c. 238. Harnack calls Ebert's Goths-under-Philip peg "unhaltbar" | c. 238–249 | Inside
- Aubé 260; Kraus, *Carmen* not before the early fourth century; Jülicher, the century 250–350 left open (all as listed by Harnack II.2, pp. 433–442) | 250–350 | Inside, except any part after 320
- Bardenhewer 1901 (OCR of a Fraktur scan; paraphrased only): about the middle of the third century, usually just after the Decian persecution, with no sure anchors | c. 250 | Inside
- Harnack 1904, II.2, pp. 433–443: not before c. 260, probably soon after Diocletian's persecution (*Carm.* 871 "duo Caesares," 911 "tres Caesares"; probable use of Lactantius); window 260 to c. 350. In 1893 he had left it open "bis 311" | 260–c. 350; preferred c. 305–320 | Straddles 320
- Monceaux III (1905), lines 37704–37716 and 37384–37390: "C'est donc entre 260 et 313"; "très vraisemblable" 305–313; not later than 313 | 260–313 | Inside
- Brewer: c. 458–466 (Harnack's figure; the earlier article Harnack quotes says "um 458–460 in Südgallien"). The fuller argument is in *Kommodian von Gaza* (1906), whose table of contents has chapters on Commodian's stay at Arles and his origin at Gaza in Syria. Harnack (1904) calls the date "paradox" and says Brewer's promised argument had not yet appeared. Brewer's argument is UNVERIFIED beyond his table of contents and Harnack's report | fifth century | Wholly outside, and outside Era 1
- Gennadius, *De viris illustribus* 15 (`npnf203_…xml`, lines 42419–42432); the NPNF gloss reads "Flourished about 270. There is wide variety of opinion ... some placing as early as 250 and some nearly one hundred years later." Gennadius wrote c. 477–494 (Harnack) and gave no date | — | —

## OG-15 — Step 0 §4 obligations: binding disclosures and the Lactantius and Tertullian dating tables (2026-10-29)

**Source:** Step 0 §4 binding obligations.
**Status:** Open. Owner: Doc_02, and the sweep owner for the overlap sweep.

- **Arnobius' anthropology, its provenance, and his date (binding on Doc_02).** Name the soul's-non-natural-immortality argument (Book II) as a real, idiosyncratic position, correctly attributed to Jerome's report — "if Jerome is to be believed" — not to Arnobius' own admission. *De viris illustribus* 79 says only that Arnobius "was a most successful teacher of rhetoric at Sicca in Africa during the reign of Diocletian, and wrote volumes Against the nations which may be found everywhere" (`npnf203_…xml`, lines 41017–41022). *Ep.* 70.5 (`npnf206_jerome-principal-works.xml`, line 16716) says he "has published seven books against the Gentiles, and his pupil Lactantius as many." The dream and the bishop are the *Chronicle*'s alone (§2 A2). **Dating: composition c. 296–310, begun c. 296–297 and finished after the edicts of 303. Tag `Widely Accepted` for the span c. 295–310; `Dominant Modern Reconstruction` for the finer order (Books I–II first, later books after 303). Jerome's 326/327 is `Documented` as a statement and is rejected as a date of composition; Harnack notes it merely opens Jerome's continuation.** Internal evidence, in the vendored Latin: "trecenti sunt anni ferme minus uel plus aliquid, ex quo coepimus esse Christiani" (I.13, TEI lines 469–471); Rome's age given as about a thousand and fifty years (II.71, lines 4586–4588), which gives c. 297 on Varro's reckoning, the one the ANF06 editor prefers (Fabian reckoning: 303); and IV.36, "nam nostra quidem scripta cur ignibus meruerunt dari? cur immaniter conuenticula dirui" (lines 7434–7437), which Harnack and Monceaux read as the edicts of 303 already issued. Proposals in the public-domain sources: ANF06 "[a.d. 297-303.]"; Teuffel–Schwabe c. 295; Ebert and Schanz 303–310; Allard 303; Harnack 304–310 (II.2, pp. 414–415); Monceaux III (lines 21741–21860), composition between 284 and 311, Book I c. 296, Book II 296 or 297, Book IV after mid-303. The whole span lies inside the window.
- **Minucius Felix's Christological absence (binding on Doc_02).** Doc_02 must disclose the absence honestly and present the live scholarly question as open, not pre-decide it — and state the count accurately rather than as a single hard figure: zero occurrences of "Jesus," "Son of God," or incarnation language in Minucius' own prose, and "Christ"/"crucifi-" together occurring four times total, all in ANF editorial apparatus (two chapter headings, one footnote, and one bracketed in-text gloss), none in Minucius' own text. Doc_02 must present this as a disclosed textual fact bounded to what was actually counted, not as an unqualified single-occurrence measurement. The dating question at obligation 1 does not change this duty.
- **The Tertullian/Article 21 boundary — RESOLVED (see §2 A5 above).** Tertullian is included: the formerly separate census entry I.17 merges into this candidate. **No further Doc_01 work is required on the boundary question itself.** What remains for Doc_01 is the constructive task the ruling opens rather than closes: building this candidate's own roster, developmental-sequence argument, and worship-practice ecology (§3 B2 above) around the shelf as it now stands (§3 B1), with Tertullian's *Apology* as the roster's best-anchored first date and not as the opening of the Latin case (obligation 1, rule (a)).
- **Lactantius' pneumatological and eschatological complications (binding on Doc_02).** Jerome's charge (*Ep.* 84.7, to Pammachius and Oceanus; `npnf206_…xml`, lines 19196–19212) reads: "Lactantius in his books and particularly in his letters to Demetrian altogether denies the subsistence of the Holy Spirit, and following the error of the Jews says that the passages in which he is spoken of refer to the Father or to the Son and that the words 'holy spirit' merely prove the holiness of these two persons in the Godhead. But who can forbid me to read his *Institutes* ... simply because this opinion of his is to be abhorred?" It is leveled at Lactantius' books generally, "particularly" his letters to Demetrianus — not at the letters alone. The letters are lost and not among the vendored texts; the charge is not confined to them and reaches the vendored *Divine Institutes*. Doc_02 must state plainly that no primary text of the charge's sharpest instance (the lost letters) survives, while the charge itself is leveled at the corpus this candidate does hold. Harnack cites the same passage for why the letters were lost. **Chiliasm.** *De viris illustribus* 18 (on Papias) says: "Irenaeus and Apollinaris and others who say that after the resurrection the Lord will reign in the flesh with the saints, follow him. Tertullian also in his work *On the hope of the faithful*, Victorinus of Petau and Lactantius follow this view" (`npnf203_…xml`, lines 39880–39885). *De viris illustribus* 80, on Lactantius, says nothing about chiliasm or the Spirit. It lists works and says "In his extreme old age he was tutor to Crispus Caesar a son of Constantine in Gaul" (lines 41028–41056). The Latin of Book VII carries the view: "regnet per annos mille iustitia" and "per annos mille dominetur" (Brandt's TEI, lines 35342 and 35379–35382). **Two spirits, and a caution.** The passage quoted at §2 A2 stands in Brandt's constituted text (II.8.4, TEI lines 7395–7396: "deinde fecit alterom [sic; the apparatus at line 7423 reads *alterum*], in quo indoles diuinae stirpis non permansit"). Brandt's prolegomena (`lactantius_divinae-institutiones-epitome-lat_brandt-csel19.txt`, lines 591–600) say that some manuscripts carry bold interpolations of two kinds: long addresses to Constantine (his notes to pp. 4, 10 and 668, 5) and a fuller dualist doctrine (his notes to pp. 130, 5 and 602, 2, and to *De opificio* 19, 8). One such dualist passage, on two spirits "rectum atque prauum," stands in his apparatus at p. 130, 5. Harnack reports that Brandt gives these additions to an interpolator writing very soon after Lactantius, perhaps at Trier, and holds that Lactantius himself cannot be ruled out, since the pieces show his style and he could have added them later (II.2, pp. 415–426). Doc_02 must not quote the manuscript-only dualist or Constantine passages as Lactantius' voice without stating this dispute. **Dating** (Harnack II.2, pp. 415–426; Monceaux III):
- Life | born not after c. 250; at Nicomedia by 303/305; tutor to Crispus in Gaul c. 317 (Jerome, *Chronicle*; *De viris illustribus* 80); death date unknown (NPNF's "Died 325" is an editor's gloss) | The tutorship is `Documented` as Jerome's statement and `Dominant Modern Reconstruction` as Harnack's arithmetic for c. 317
- *On the Workmanship of God* | 303/304 (Harnack) | not separately tagged
- *Divine Institutes* | written from 304, before April 311, finished nearer 305/306 than 311 (Harnack); 307–311 (Monceaux) | `Widely Accepted` for 304–311
- *On the Anger of God* | soon after the *Institutes* (Harnack) | not separately tagged
- *Epitome* | after 313 (Harnack) | not separately tagged
- *De mortibus persecutorum* | autumn 313 to autumn 314; latest possible 321 (Harnack); Seeck 317–321 and Brandt April 315 dissent | `Contested`: Harnack 313–314, Brandt April 315, Seeck 317–321. One source gives 313–314 against two dissenting dates, so the tag is not Widely Accepted
- **The Lactantius/IJC boundary.** This is not open Doc_01 work; it is already resolved in `cic/corpus-map/latin-apologists.yaml`, splitting Lactantius' apologetic corpus (this candidate's) from *De Mortibus Persecutorum* (IJC's). Doc_01 should cite and respect this ruling, not re-derive it. One disputed matter bears on wording. Harnack holds that *De mortibus* is Lactantius's (the *De persecutione* of Jerome's *De viris illustribus* 80) and Brandt denied it (II.2, pp. 415–426, as reported by Harnack). The map's ruling and IJC's source record both attribute the work to Lactantius, and IJC's record does not name the dispute (its `author` field reads "Lactantius (c. 250-325 CE)"; the 325 is the NPNF editor's gloss at *De viris illustribus* 80). Doc_01 should name the authorship dispute wherever it mentions the work. Whether the split's wording changes is a decision for the project lead; nothing in IJC's records is edited here. Post-1930 work on the authorship and date exists; that is UNVERIFIED, from memory, and not cited.
- **Full built-world overlap sweep — run read-only.** Method: a case-insensitive search of `records/` for Tertullian, Minucius, Arnobius, Lactantius, Commodian, Perpetua, Demetrian, "Vanity of Idols," "Octavius," "Divine Institutes" and "Ad Nationes," with the source-volume filename strings and `tertullian.org` URLs excluded, and each hit read in context ("Perpetua" also matches "perpetual"). Results, world by world. **PAHC:** Tertullian's *Apology* and *Against Marcion*, `register: etic` and `corroborating`, clean and needing no ruling (§3 B3). **LPC:** now has compiled records; it shares Cyprian's *Address to Demetrianus* and *On the Vanity of Idols*, uses both, and excludes Tertullian and the *Passion of Perpetua* (§3 B3). LPC's `world_core` record still says the Passion's Perpetua portion is assigned to `tertullian-s-voice`, a slug that no longer exists. That is LPC's own record, not edited here. LPC also has Augustine's Sermons 280–281 on Perpetua and Felicitas, which are a different work. **IJC:** Lactantius' *De mortibus* only (§3 B3); no IJC record cites Tertullian or the *Divine Institutes*. **Fleet-level records (`_fleet`):** `_fleet.source.tertullian-against-praxeas` (`register: etic`, `evidentiary_weight: load-bearing`, `formation_confidence: Documented`, ANF03 English) is cited by `_fleet.modern.trinity` and `_fleet.contested.theophilus-triad-referent`. The record notes that the ANF03 edition "does not carry the Latin text"; the Latin of *Against Praxeas* is now vendored (Kroymann, CSEL 47, and Oehler). No ruling is proposed; it is noted for System Hub. **Desert:** one quote record cites an ANF editorial footnote that names Tertullian's *De Corona*; it is not a use of Tertullian's text. **Gallic:** `gallic.term.trial` reports what Vincent of Lérins says about Origen and Tertullian; it is not a use of Tertullian's text. **Alexandria, Cappadocian, Hieronymian, Syriac, `don`, `rzg`, `witt`, `fix`:** no hit for any of the six authors other than volume-title strings (the Cappadocian source records name Arnobius only in the ANF06 volume title). **Minucius Felix, Commodian, Arnobius and Lactantius' apologetic works:** no built-world record cites them, apart from the LPC note that *On the Vanity of Idols* compiles Tertullian and Minucius. **Perpetua:** LPC only. I.33 and the remaining Era 1 entries: the earlier full Era 1 sweep, whose own stated scope was "the nineteen Era 1 entries not already checked by the drafts," excluded this candidate and I.35; the I.35 comparison is this document's own direct check (§3 B3). The new I.33 finding is at §3 B3. Doc_01 should re-confirm rather than re-run from zero. No built world's records are edited by this sweep.
- **Tertullian's own later New Prophecy (Montanist) alignment (binding on Doc_02), per §2 A2 above.** Name the seven works the map co-assigns to `montanism-the-new-prophecy` (*On Monogamy*, *On Modesty*, *On Fasting*, *On the Veiling of Virgins*, *On Exhortation to Chastity*, *De Fuga in Persecutione*, *Against Praxeas*) as a real, disclosed idiosyncrasy, on the same standard already applied to Minucius Felix's Christological silence, Lactantius' pneumatology, and Arnobius' anthropology — not a floor-level divergence (the census's own Montanism entry states the New Prophecy shared the condemning churches' own doctrine) but a genuine later-career shift in authority and discipline that Doc_02 must not smooth into an undifferentiated single "Tertullian" voice across his whole corpus. **Jerome's report** (*De viris illustribus* 53, `npnf203_…xml`, lines 40489–40519): "He was presbyter of the church until middle life, afterwards driven by the envy and abuse of the clergy of the Roman church, he lapsed to the doctrine of Montanus, and mentions the new prophecy in many of his books. He composed, moreover, directly against the church, volumes: *On modesty, On persecution, On fasts, On monogamy,* six books *On ecstasy,* and a seventh which he wrote *Against Apollonius.*" Jerome's list names four of the seven (*On Modesty*, *De Fuga*, *On Fasting*, *On Monogamy*). The NPNF gloss "Born about 160, christian 195, apology 198, died about 245" is editorial. **Dating**, from three public-domain authors (Harnack 1904, II.2, table pp. 295–296; Schanz–Hosius–Krüger III 1922; Monceaux I, table pp. 208–209, lines 17640–17720):
- *On Exhortation to Chastity* | 204–206/7, before the break | probably before 207 | between 208 and 211, before the schism
- *On the Veiling of Virgins* | 204–206/7, before the break | 207 at the latest; not yet excluded from the church | between 208 and 211
- *De Fuga in Persecutione* | 211 or 212 | close to *The Chaplet* (211) | 213, after the break
- *Against Praxeas* | c. 213–218 | not tabulated | after 213
- *On Monogamy* | soon after 217/8 | c. 217–220 | after 213
- *On Fasting* | soon after 217/8 | after *On Monogamy* | after 213
- *On Modesty* | not long before 222/3 | the last work; Callistus (217–222) the "überwiegend Wahrscheinliche"; Esser proposed Zephyrinus (198–217) | 217–222, probably the last surviving work
- The break with the church | 207/8 | not fixed | 213
- **The *Passion of Perpetua and Felicitas* — date and attribution disclosure (binding on Doc_02).** The approved slate keeps Perpetua on this shelf. The date: Robinson's introduction fixes no year and notes only the incidental "natale tunc Getae Caesaris" (`perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, lines 1734–1737); Wallis in ANF03 gives about 202 (`anf03_tertullian.xml`, line 59461); Monceaux gives 7 March 203 (I, line 5625); Harnack prefers 203 (II.2, pp. 321–324). Tag: 7 March 202 or 203, under Severus, `Widely Accepted`; both years are inside the window. The visions of Perpetua and Saturus are their own writing: `Widely Accepted`. Who compiled the rest is `Contested`: Robinson finds it "in the highest degree probable" that the Passion is "a genuine addition to the hitherto recognised works of the great master" (lines 3356–3364); Coxe in ANF03 thinks Tertullian was "the *editor* of the story, not its author" (line 59449); Harnack, Neumann and Monceaux doubt it, and Harnack says certainty cannot be reached. That the compiler's own colouring is Montanist is `Dominant Modern Reconstruction` (Harnack: "Der Montanismus des Redaktors ist m. E. unverkennbar"). Doc_02 must not present the Passion to a Representative as Tertullian's own work.

## OG-16 — The saturation statement is not closed (2026-10-29)

**Source:** Doc_02 §9; `Source_Registry.md`, the saturation statement.
**Status:** Open. Owner: the Library thread, or the source-research thread.

The Registry and Doc_02 do not close the saturation statement. The field-bibliography sweep has not been run against any external instrument. The instruments not reached are the post-1930 scholarship on Tertullian and the Latin apologists, later handbooks, the *Cambridge History of Early Christian Literature* and the *Dictionary of Christian Biography*.

## OG-17 — Commodian's Carmen apologeticum has no English text (2026-10-29)

**Source:** Doc_02 §1; Step 0 §3 B1.
**Status:** Open. Owner: the source-research thread.

No English translation of the *Carmen apologeticum* was located. A Representative's English for it would be rendered from the Latin, and Doc_10 must say so wherever the poem is used.

## OG-18 — Robinson's conclusion on the original of the Passion was not read (2026-10-29)

**Source:** Doc_02 §2, the Passion of Perpetua and Felicitas.
**Status:** Open. Owner: the Library thread.

Robinson's later chapters compare the Greek and the Latin witnesses. This build read his description of the manuscripts and did not read to his conclusion on which is the original. A Representative must not assert which is the original until that is read.

## OG-19 — Doc_01 repeats the Lactantius count that includes the poems (2026-10-29)

**Source:** Doc_01 §3, the Heresy bullet; Doc_02 §1; the Lactantius "Fragments" finding.
**Status:** Open. Owner: the Library thread, with the project lead's decision on a change order.

Step 0 and Doc_01 §3 give 285,187 words for Lactantius's four works. Doc_02 §1 shows that 3,932 of those words are the two poems the ANF07 file prints as "Fragments of Lactantius", so the three genuine works are 281,255. No comparison in Doc_01 changes. Doc_01 is approved to proceed and not frozen; a correction to its sentence is a change order, named and reasoned, and it is not made as a quiet edit.

## OG-20 — Stale references elsewhere that the dossier lists and this world does not edit (2026-10-29)

**Source:** Source Readiness Dossier section 5, "Stale references elsewhere"; Step 0 §4 items 1, 6 and 7.
**Status:** Open. Owner: each record's own owner.

LPC's `world_core` record still names `tertullian-s-voice` as the home of the Passion's Perpetua portion (see also the stale-slug entry of 2026-10-29). The census wording that Tertullian "opened" the Latin case appears in six places listed in Step 0 §4 item 1, rule (a): I.43 `voices`, `why`, `relationsSummary` and `longDescription`, I.17 `relationsSummary`, and the edge from I.17 to I.43. The I.43 `sourcing` field attaches "just under half a million words" to Lactantius alone, and Doc_02 §1 shows that the figure 285,187 behind it counts two poems that are not shown to be his (the Lactantius count entry of 2026-10-29). IJC's source record for *De mortibus* gives the author's dates as c. 250–325 without naming the authorship dispute. None is edited by this world.

## OG-21 — Correction to the findings on the ANF07 "Fragments of Lactantius" and on the Doc_01 count (2026-10-29)

**Source:** Round 1 review of Doc_02 and the Registry (`Review-Artifacts/Doc02_Round1_Review.md`, the P0 finding); `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` div2 `iii.vi`.
**Status:** Open. Corrects the entries titled "The ANF07 'Fragments of Lactantius' are two poems of uncertain authorship, not fragments of lost works" and "Doc_01 repeats the Lactantius count that includes the poems". Those entries stay as written, and this entry supersedes their claims.

The division holds three parts: four prose fragments of Lactantius's lost works quoted through later authors (509 words), two poems of uncertain authorship (2,285 and 961 words), and the editor's General Note (177 words), 3,932 words in all. The earlier finding was wrong to say that the division holds no fragments of lost works, and wrong to pair the English poems with the Latin *Carmina* and the Latin fragments with no English. The corrected pairing is as the corpus map had it before: the English division pairs with the Latin of CSEL 27 part 2 fascicle 1, which prints the poems and the lost-works fragments. The staging rows are restored to their earlier title, role and confidence, with locus and date keys added. The three genuine works are 281,255 words, and 281,764 with the fragments. Step 0's 285,187 and Doc_01 §3 still include the two poems and the editor's note. Both documents are approved to proceed and are not edited. A correction to them is a change order for the project lead.

## OG-22 — Dossier items and one Step 0 wording that this world cannot close (2026-10-29)

**Source:** Source Readiness Dossier section 5; Step 0 §4, the Arnobius obligation; Round 1 review, findings on the dossier questions and on the soul.
**Status:** Open. Owner: each item's own owner; the project lead for the Step 0 wording.

Four dossier questions travel with this world and are decided elsewhere. First, the I.33 touchpoint: I.33's census story for Callistus lists Tertullian's *On Modesty* as a source. Second, the fleet-level record `_fleet.source.tertullian-against-praxeas` says the ANF03 edition "does not carry the Latin text", while the Latin is now vendored here. Third, IJC's source record for *De mortibus* gives the author's dates as c. 250–325 without naming the authorship dispute. Fourth, the stale references listed in the entry on stale references elsewhere. None is edited here.

Separately, the Arnobius obligation in Step 0 §4 asks that Arnobius's teaching on the soul be attributed on Jerome's report. The vendored Jerome notices (*De viris illustribus* 79 and *Letter* LXX) say nothing about the soul. Doc_02 §7, on Arnobius, therefore reads the doctrine in Arnobius's own Book II (chapters XXXI, XXXV and LXII) and keeps Jerome to the dream and the bishop. Whether Step 0's wording should change is the project lead's decision.

## OG-23 — Library-stage status when work paused: Doc_02 Round 2 Clear with open P2s (2026-10-29)

**Source:** `Review-Artifacts/Doc02_Round2_Review.md`; draft pull request #1293.
**Status:** Open. Owner: the build thread on resume.

Round 2 of Doc_02 and the Registry returned Clear (P0 none; two new P1, both fixed since: the corpus-map counts and the Files-table rows for the Passion). Doc_02 still reads Draft and has not been self-disposed as approved to proceed. Six new P2 and four partly fixed Round 1 P2 remain open and are listed in the review: the Appendix poems stated flatly as not Tertullian's, the date of the break stated twice, the Registry row 33 and row 38 readings, the "adds no corpus count" sentence, Gennadius with one paragraph, the manifest's blank check table and its Step 2 date, and two loose sentences (row 44 on fragment sources, the ledger entry on stale references). Handoff checks still failing are not this branch's to close: the unset `safety_adjacent`, Step 0 at seven review files with its latest review lacking the approval phrase, and 24 quotation findings that sit in Step 0. The Registry generator scripts were lost with the session scratchpad, so later Registry edits are made in the file directly. No Round 3 has been started.
