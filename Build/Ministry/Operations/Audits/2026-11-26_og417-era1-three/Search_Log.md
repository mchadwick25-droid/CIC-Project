# Library search log: three thin era 1 traditions, 2026-11-26

The search record for Open-Gaps 417: `bardaisanite-current`, `modalist-monarchianism` and
`danubian-latin-christianity`. Mark lifted the source-research hold for these three only (2026-11-26, "a",
then "yes" to the order of work). The other held items stay held: Open-Gaps 419, 415 and the Pilgrims in 385.
No model spend; no brief was rebuilt.

The vendored files and their rights are recorded in `cic/texts/REGISTRY.yaml` and in each file's header. The
queue rows are in `Build/worlds/_cross-world/download-queue-seed.yaml`. The shelf rows are in
`cic/corpus-map/_staging/` and the three merged buckets.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | every file came from here |
| HathiTrust | not needed: every item wanted was found on archive.org | no |

No item had to be left for a person to fetch in a browser.

## Holdings check, before any search

Before the session the three buckets held 3, 3 and 2 rows. A grep of all `cic/texts/` files for the names
(Bardesanes/Bardaisan/Βαρδησ-, Noetus/Νοητ-, Praxeas, Sabellius/Σαβελλ-, Patripassian, Sirmium, Pettau/Poetovio,
Remesiana, Siscia, Quirinus, Pannonia, Mursa, Singidunum, Ratiaria, Germinius, Ursacius) found much already held
and unread for these entries. Those files were given shelf rows, with no new download:

- **Bardaisan:** Eusebius, Church History IV.30 (npnf201); Epiphanius, Panarion 56 (Holl 1922); Hippolytus,
  Refutation VI and VII (anf05); Sozomen III.16 and Theodoret, Church History IV.26 in NPNF numbering, on
  Harmonius (npnf202, npnf203); Jerome, Lives of Illustrious Men 33 (npnf203); the Chronicle of Edessa (Bardaisan's
  birth, year 465 of the Greeks); Michael the Syrian, Book VI chapter 6 (Chabot); the npnf213 dissertation's
  quotation of Ephrem's verses on a book of Bardaisan.
- **Modalists:** Hippolytus, Against Noetus and Refutation IX (anf05, as `context`); Novatian, On the Trinity
  (anf05); Eusebius, Church History VII.6 (npnf201); Athanasius, Defence of Dionysius and De Decretis 25-27
  (npnf204); Basil's letters (npnf208); Epiphanius, Panarion 57 and 62 (Holl 1922); Augustine, De haeresibus 36
  and 41 (the PL 42 file).
- **Danubian:** the Passio of Irenaeus of Sirmium (both Gebhardt 1902 files); Acta Sanctorum March III (Irenaeus;
  Montanus and Maxima at Sirmium) and April III (Pollio of Cibalae); Hilary's Collectanea (Feder 1916: Germinius,
  Valens and Ursacius) and De Synodis (PL 10); Athanasius, De Synodis (npnf204); Socrates II.29-30 on Photinus of
  Sirmium (npnf202); the Scolia Arriana with Palladius of Ratiaria and Secundianus (Kauffmann 1899); Jerome, Lives
  of Illustrious Men 74 on Victorinus (npnf203).

## Searches and what was taken

All on archive.org, by title and editor, in Latin, Greek, Syriac, English and German. Each pick: metadata read,
title page read in the OCR, the wanted passage found, djvu.txt fetched, byte count matched to the listed size.

| tradition | file | what it adds | quotable? |
|---|---|---|---|
| Bardaisan | `patrologia-syriaca_pars1-t2-...-syr-lat_parisot-nau-kmosko1907.txt` | the Book of the Laws of Countries in Syriac with Nau's Latin; Nau's chapter of ancient witnesses | Nau's Latin, as a translation; Syriac OCR unusable |
| Bardaisan | `eusebius_praeparatio-evangelica-t1-libri-1-9-grc_gifford1903.txt` | Praeparatio VI.10, the Greek extract from the dialogue on fate | yes, Greek fair: check against the page image |
| Bardaisan | `eusebius_preparation-for-the-gospel-t3-pt1-books-1-9_gifford1903.txt` | Gifford's English of the same | yes |
| Bardaisan | `ephraim_opera-syriace-latine-t2-sermones-adversus-haereses-syr-lat_benedictus1740.txt` | Ephrem's 56 hymns against heresies | second witness only (long s read as f; Syriac unusable) |
| Bardaisan, Modalists | `theodoret_opera-omnia-t4-haereticarum-fabularum-compendium-pg83-grc-lat_migne1864.txt` | Compendium I.22 (Bardesanes, Harmonius), II.9 (Sabellius), III.3 (Noetus) | yes, Latin fair, Greek fair |
| Modalists, Bardaisan | `hippolytus_refutatio-omnium-haeresium-grc_wendland-gcs26-1916.txt` | the Greek of the Refutation, Book IX on Noetus, Zephyrinus and Callistus | yes, Greek fair: check against the page image |
| Modalists | `hippolytus_quae-feruntur-omnia-contra-noetum-grc_lagarde1858.txt` | the Greek of Against Noetus | second witness (Greek OCR poor to fair) |
| Modalists | `novatian_de-trinitate-lat_fausset1909.txt` | Novatian's Latin | yes |
| Modalists | `novatian_treatise-on-the-trinity_moore1919.txt` | Moore's English | yes |
| Modalists | `dionysius-alexandria_letters-and-other-remains-grc_feltoe1904.txt` | Dionysius of Alexandria on the Sabellians of the Pentapolis; the Refutation and Defence | yes, Greek fair |
| Modalists | `dionysius-alexandria_letters-and-treatises_feltoe1918.txt` | Feltoe's English | yes |
| Modalists | `filastrius_diversarum-hereseon-liber-lat_marx-csel38-1898.txt` | the Noetiani and Sabelliani (53-54) | yes |
| Danubian | `victorinus_opera-lat_haussleiter-csel49-1916.txt` | the Latin of both Victorinus works; Jerome's revision on facing pages | yes |
| Danubian | `niceta-remesiana_life-and-works-lat_burn1905.txt` | Niceta of Remesiana's Latin works | yes |
| Danubian | `ruinart_acta-martyrum-sincera-lat-grc_ratisbon1859.txt` | the acts of Irenaeus of Sirmium, Pollio of Cibalae, Serenus of Sirmium, Quirinus of Siscia | yes, Latin good to fair |

Two Google scans (Lagarde, Burn) had Google's preamble removed as a host addition, recorded in each header.
The Victorinus scan is a Johnson Reprint facsimile of the 1916 print, the only scan found; the Library has taken
such facsimiles before (Cyprian CSEL 3, Wyclif De ecclesia). Feltoe 1918's title page prints no year; the
preface is signed March 1918 and the catalogue agrees, which INTAKE §2 accepts.

## Found and not taken, or not had

- **Cureton, Spicilegium Syriacum (1855).** Located and rights-clear (archive item spicilegiumsyria00cureuoft),
  queued as not-yet-downloaded. Not needed now: its English is held in anf08 and Nau gives the Syriac with Latin.
- **A clean text of Ephrem's Hymns against Heresies.** Beck's edition and German (CSCO, 1957) is in copyright.
  The only old print (Rome 1740) is held as second witness. Quotes from Ephrem against Bardaisan come through
  Mitchell's Prose Refutations (held) or the npnf213 dissertation.
- **Niceta in English.** Walsh's translation (Fathers of the Church 7, 1949) would need a renewal search; not
  needed, since Burn's Latin is held.
- **The Passio of the Four Crowned Martyrs** (the Pannonian quarries near Sirmium). A title search for the Acta
  Sanctorum November volumes found nothing; not searched further. A later candidate.
- **Councils of Sirmium.** No acts survive apart from what Hilary, Athanasius and the historians keep; those are
  held and shelved.
- **Julius Africanus and Porphyry on Bardaisan.** Not searched; Nau's testimonia chapter quotes both, as a
  finding aid.

## Can each tradition now carry a brief at C or better?

Under `Brief-Kit/Kit.md` (Rigor): every claim on a line from an old source, no modern opinion. This judges
the Library's holdings, not a brief; the briefs are rebuilt by the tradition line.

- **Bardaisan: yes.** His own words survive in the dialogue, now held in English, Greek (Eusebius) and Latin
  (Nau). Hostile and later witnesses are shelved (Eusebius, Epiphanius, Hippolytus, Theodoret twice,
  Sozomen, Jerome, Ephrem through Mitchell), with the Chronicle of Edessa's dated birth. Limits: the hymns of
  Ephrem are second witness only, and the two portraits (the dialogue against fate, Ephrem's cosmology)
  disagree. The brief must tell that disagreement rather than settle it.
- **Modalists: yes, comfortably.** Opponents only, as the census says, but many and early: Tertullian,
  Hippolytus (English and Greek), Novatian, Dionysius of Alexandria and Dionysius of Rome, then Epiphanius,
  Filastrius, Augustine, Basil and Theodoret. Limit: no word of Noetus, Praxeas or Sabellius survives except as
  their opponents quote it.
- **Danubian: yes, for a C, with two questions for the rebuild.** Held now: Victorinus in Latin and English,
  Jerome on him, five martyr acts of Sirmium, Cibalae and Siscia, and the Homoian paperwork of Sirmium. Two
  questions the tradition line must settle before writing, not ruled here: whether the Homoian bishops of the
  Danube (Valens, Ursacius, Germinius, Palladius) are this entry's own voice or belong to
  `homoian-arian-christianity` (shelved here as context only); and whether Niceta of Remesiana, whose works
  fall at and after the window's end (c. 250-400), enters the story.

## The Danubian questions, settled by the sources (2026-11-26)

Mark asked that the two Danubian questions follow the sources (Decision-Log, same date).

- **The Homoian bishops.** Their letters and notes are by Latin bishops of the region's own sees, inside its years. The Hilary Collectanea and Scolia Arriana rows are now `tradition` for this entry, as well as for `homoian-arian-christianity`.
- **Niceta.** Checked in the held files: Gennadius, Lives 22 (npnf203) names him bishop of Romatia and lists his six books; the Acta Sanctorum June V dossier tells his two visits to Nola from the Dacians. The primary witness, Paulinus of Nola's poems, was not held, so it was found and vendored: Hartel, CSEL 30 (Vienna, 1894), archive item sanctipontiimer00paulgoog, Google's preamble of 46 lines removed and recorded. Carmen 17 sends Niceta home "usque Dacos"; Carmen 27 welcomes him back. The poems place him after the entry's map years, so he is told as what came of the tradition. Both held files and the poems are now shelved to the entry, which has 19 rows (16 before this step).
- Paulinus's Carmina may also serve other entries (Italian and Gallic ascetic currents); they are shelved here only for Niceta, and are open to the next session that checks those entries.
