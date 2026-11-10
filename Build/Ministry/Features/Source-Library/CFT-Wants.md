# Church Family Tree wants — the Library's list

**Charter (Mark, 2026-11-10):** "launch a library thread that is patterned after previous threads with
full research, organization and render abilities to find the sources you need, public domain in any
language we can find it."

One list of texts the tree's workers need, each tied to the entry or gap it serves. A want is filled
only when the text is vendored in `cic/texts/` with rights read from the host and the title page, and
shelved in `cic/corpus-map/`. Rights rows live in `Build/worlds/_cross-world/download-queue-seed.yaml`.
The page for Mark renders this list (https://claude.ai/artifact/RTJ2uXC4rjqKEguvt4UiDP); this file is the record.

States: **filled** (vendored and shelved) · **held already** (in the Library unused; now shelved) ·
**located** (found and rights clear, not vendored) · **none survives** (no own text exists, so no
search can fill it) · **not found** (searched; where is said) · **queued** (a later batch).

## Batch 1 — the later-worlds people gate (Open-Gaps 164, 2026-11-10)

Source: `Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/final_rows.json`. Each held
person failed "own words held" (answer C). The want is a text written by them or issued in their name.

| person | want | state | file(s) | unblocks |
|---|---|---|---|---|
| Pamphilus of Caesarea | Apology for Origen, Book I (Rufinus's Latin) | filled | `pamphilus_apologia-pro-origene-rufinus-lat_lommatzsch1846.txt`; second witness `origen_opera-omnia-t7-pamphilus-apologia-pg17-grc-lat_migne1857.txt` | The Apology itself is now held. Mark's question B (a book written jointly with Eusebius) still decides whether it counts. |
| Heraclius | The Ecthesis (638) | held already | `mansi_sacrorum-conciliorum-collectio-tomus-10-lat_welter-facsimile1901.txt`, lines about 100110-100680 (Lateran 649, Secretarius III) | A document issued in his name is now on his home shelf, so the own-words test is met. The count passed already. He can be built. |
| Francis of Assisi | Rule, Testament, letters, Canticle | filled | `francis-assisi_writings-of-saint-francis_robinson1906.txt`; `francis-assisi_opuscula-lat_quaracchi1904.txt` | Own words are held. He is still a founder, so Mark's question A decides. |
| Bonaventure | writings of his own | filled | `bonaventure_life-of-saint-francis-legenda-maior_salter1904.txt`; `bonaventure_tria-opuscula-breviloquium-itinerarium-de-reductione-lat_quaracchi1911.txt` | Own words are held, he founded nothing, and the count passed. He can be built. |
| Priscillian | the Wurzburg tractates | filled | `priscillian_quae-supersunt-lat_schepss1889-csel18.txt` | Own words are held. He is still a founder, so question A decides. |
| Mani | text of his own in Manichaean transmission | not found | Searched archive.org for Müller 1904, the Turfan Estrangelo fragments: not there (HathiTrust is behind a browser check). The Kephalaia (1935-1940) and the Psalm-book (1938) are too late. Augustine's quotations of the Fundamental Epistle (CSEL 25, 1891) are an opponent's quotations. | Nothing. He is a founder anyway. |
| Kaleb | an inscription in his name | not found | Littmann, Deutsche Aksum-Expedition IV (1913), read: it has no Kaleb inscription. Nothing else before 1931 was found. | Nothing. |
| Valdes of Lyon | his profession of faith (c. 1180) | not found | No printing before Dondaine (1946, not public domain) was found on archive.org; Müller 1886 read. | Nothing. |
| Mesrop Mashtots | a work of his own | none survives | No extant work of his own is known; Koriun's Life is about him. | Nothing. |
| Paul of Samosata, Basilides, Valentinus, Maximilla | words of their own | none survives in their own transmission | Only opponents' quotations survive. Valentinus's Gospel of Truth is a 1950s find of disputed authorship. | Nothing. |
| Hilarion of Gaza | words of his own | none survives | Jerome's Life is about him. | Nothing. |
| Johannes Tauler | writing of his own | none survives | His sermons survive as his hearers' notes. Vetter (1910) prints the same notes. | Nothing. |

Located, not vendored: Bonaventure, Opera omnia VIII (Quaracchi 1898), the Latin Legenda maior
(seed row, `not-yet-downloaded`).

## Batch 1 — Library defects (Open-Gaps 165 and 152)

| defect | fix |
|---|---|
| Hippolytus's Refutation shelved as Montanism's own voice | Role set to `context` on `montanism-the-new-prophecy` and on `ebionite-nazoraean-current`, which had the same fault. It stays `tradition` on `roman-church-third-century`, Hippolytus's own church. |
| Nikodemos's Synaxaristes on the 1453-1650 shelf | Removed from `orthodoxy-under-the-ottomans-parish-millet-and-n`; it stays on the 1650-1821 and Kollyvades shelves. The Pedalion (1800) sits on the same shelf for the same reason. It is not moved yet: see the open questions. |
| PO17 described as Petit's Florence documents | The row was right but named the whole volume. Loci now give line ranges: the Lives at 156-17448, Petit's Mark of Ephesus at 17449-49934, the Arabic Synaxary from 49935. |
| The Brosset file is the Introduction volume | The file header now says so. The two chronicle-voice rows are replaced by one `context` row for Brosset's study. The chronicle text itself is a new want (batch 2). |
| "Whole file" loci on multi-work volumes | Fixed for PO17. The general pass (707 staging files say "whole") is batch 2: Langlois's sections, the anf volumes, the PO fascicules. |
| People rows' `year`; the Ephrem alias | The census owner's, not the Library's. Passed on. |
| Busch's Chronicon Windeshemense (ruling 6) | `tradition` on the Devotio Moderna shelf. |
| Love's Mirror | Added as `tradition` on `carthusians-later-middle-ages` (a new shelf). The earlier rows stay as they were. |
| Bell, Part II (the Melitian papyri) | Added as `tradition` on `melitian-schism` (a new shelf). The `desert` row stays: see the open questions. |
| Simeon of Beth Arsham (ruling 5) | Already on the Syriac Orthodox shelf, inside the John of Ephesus and Zachariah rows. No move was needed. |
| Theophilus row to II.1 | Not done: "may move" is a census question, not a Library one. |

### Open questions (cross-world; for the coordinator)

1. Bell 1924, Part II, is `tradition` on the built `desert` world's shelf. It is the Melitian
   community's own voice, not desert monasticism's. Removing it changes what desert reads.
2. The Pedalion (1800) is on the 1453-1650 shelf, the same out-of-window fault as the Synaxaristes.
   It is a canon collection whose canons are older, so a builder might keep it as law in force.

## Batch 2 and later — queued

- **Eras 8-9 holds** (`CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`): Haiti, Cuba and Puerto Rico, the
  Bethlemites, Cancuc and the Talking Cross, the Thrissur Chaldeans, Hermano Pule, the Peking
  mission, Australia and New Zealand, Pai Mārire and Ringatū, Korea, the Antiochene Orthodox after
  1815, the Syriac Orthodox and Syriac Catholics, the Tolstoyans, Rabinowitz, the Transylvanian
  Unitarians, the Dukhobors and Molokans.
- **Living traditions with no entry after a date** (Open-Gaps 158): 79 gaps, worked by era.
- **Families the tree doesn't reach** (Open-Gaps 159): the Patriarchate of Alexandria, Cyprus, the
  Polish, Czech-Slovak and Macedonian churches, and the Eastern Catholic churches never named.
- **Living marks graded none** (Open-Gaps 162): Kongo, Transylvania, the Schwenkfelders, New France.
  These want dated own-voice items after 2010. That is mostly the web, not public-domain print.
- **The Georgian chronicle** in Brosset's translation (the text volumes of 1849-1857).
- **The loci pass** for multi-work volumes.
