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

**Source:** `cic/texts/perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` (header content note); `cic/corpus-map/_staging/anf03_tertullian.yaml` and `perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml` (notes); Step 0 §2 A5 and §4 item 7 (LPC's `world_core` record).
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

The re-run found the LPC use in OG-11 and one further PAHC use (`pahc.source.lucian-peregrinus` triangulates with Tertullian's *Apology* 39). It also found one PAHC wording item: `pahc.force.systematic-theological-mode-elsewhere` says the *Apology* opens a body of confident Latin defense, which Step 0 §4 item 1, rule (a), does not adopt. The item is carried to PAHC (OG-44 there) and is not edited. Matches in other worlds that were inspected are volume-title strings and the word "perpetual"; they were not each opened.
