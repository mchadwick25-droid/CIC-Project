# Contextual indexing: cost estimate

Status: pending option, not authorized, to be put to Mark later only if retrieval on lpc proves weak.

Prices: Haiku 4.5 from engine/m8/price_tables.py. Batch discount: the vendor's published batch rate is assumed to be half the standard rate (the repo carries no batch price), and the live-test guard does not expose the batch endpoint.

Assumptions behind every modeled row (replaced by the segmenter's real passages file by file as they exist): about 275 words a passage; characters per token Latin script 4.0 (low band) to 3.2 (high band), Greek and other scripts 2.4 to 1.5; output 55 (low) to 100 (high) tokens per context line; cache prefix 4300 (low band) to 9000 (high band) tokens per window, 4300 being the assumed Haiku cache minimum of 4,096 plus margin; 2% of high-band calls re-write the cache instead of reading it; 45 fresh tokens a call plus 220 per window for the edge neighbours. Shared files count once in the union and once in each world that holds them, so the world rows add up to more than the union.

| Scope | Files | Passages | Text tokens (low-high) | Standard path | Batch path (assumed) | One call per window, standard |
|---|---:|---:|---|---|---|---|
| union | 338 | 305,265 | 154.3M to 198.2M | $438.12 to $745.54 | $219.06 to $372.77 | $279.78 to $388.32 |
| world alx | 36 | 51,692 | 27.3M to 35.2M | $76.18 to $128.67 | $38.09 to $64.33 | $49.01 to $67.70 |
| world cappadocian | 37 | 47,441 | 27.7M to 38.8M | $73.23 to $125.95 | $36.61 to $62.98 | $47.64 to $68.84 |
| world desert | 17 | 19,514 | 10.5M to 13.3M | $29.02 to $48.57 | $14.51 to $24.29 | $18.71 to $25.59 |
| world don | 34 | 35,817 | 18.1M to 22.4M | $51.53 to $86.57 | $25.76 to $43.28 | $32.93 to $44.77 |
| world gallic | 8 | 7,610 | 3.9M to 4.8M | $11.13 to $18.55 | $5.57 to $9.28 | $7.14 to $9.64 |
| world hal | 11 | 17,331 | 9.1M to 11.3M | $25.48 to $42.51 | $12.74 to $21.25 | $16.38 to $22.16 |
| world ijc | 58 | 73,905 | 38.2M to 49.0M | $107.27 to $182.08 | $53.63 to $91.04 | $68.74 to $95.20 |
| world lpc | 112 | 100,107 | 49.4M to 61.2M | $142.13 to $239.87 | $71.07 to $119.93 | $90.51 to $123.40 |
| world pahc | 35 | 40,889 | 21.4M to 26.7M | $59.98 to $100.36 | $29.99 to $50.18 | $38.54 to $52.34 |
| world rzg | 42 | 34,625 | 15.8M to 19.6M | $47.26 to $80.96 | $23.63 to $40.48 | $29.76 to $40.98 |
| world syr | 27 | 29,330 | 15.0M to 18.6M | $42.54 to $71.30 | $21.27 to $35.65 | $27.25 to $36.99 |
| world witt | 28 | 15,381 | 6.7M to 8.3M | $20.67 to $35.40 | $10.33 to $17.70 | $12.95 to $17.81 |
| sample (lpc, modeled from the file list) | 3 | 242 | 0.1M to 0.2M | $0.36 to $0.57 | $0.18 to $0.28 | $0.23 to $0.31 |

## What drives the union cost

| Component | Low | High |
|---|---:|---:|
| cache_write | $208.28 | $321.97 |
| cache_read | $115.16 | $246.99 |
| fresh_input | $30.72 | $23.94 |
| uncached_small_windows | $0.01 | $0.01 |
| output | $83.95 | $152.63 |

## Largest files in the union (by high estimate, top 40)

| File | Worlds | Source | Passages | Windows | Low | High |
|---|---|---|---:|---:|---:|---:|
| augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt | lpc | modeled | 4,657 | 354 | $6.81 | $11.42 |
| amphilochius-iconium_opera-pg39-grc-lat_migne1858.txt | cappadocian | modeled | 3,345 | 363 | $5.30 | $9.35 |
| basil_opera-omnia-pg31-grc-lat_migne1857.txt | cappadocian | modeled | 3,074 | 347 | $4.97 | $8.73 |
| augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt | lpc | modeled | 3,674 | 229 | $4.91 | $8.48 |
| basil_opera-omnia-pg29-grc-lat_migne1857.txt | cappadocian | modeled | 2,849 | 312 | $4.55 | $8.01 |
| athanasius_opera-omnia-pg26-grc-lat_migne1857.txt | alx,ijc | modeled | 2,818 | 307 | $4.49 | $7.89 |
| npnf108_augustine-exposition-psalms.xml | lpc | modeled | 2,958 | 230 | $4.37 | $7.30 |
| gregory-nazianzen_orationes-27-45-pg36-grc-lat_migne1858.txt | cappadocian | modeled | 2,518 | 279 | $4.03 | $7.10 |
| gregory-nyssa_opera-omnia-pg44-grc-lat_migne1858.txt | cappadocian | modeled | 2,483 | 284 | $4.04 | $7.09 |
| anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml | alx,pahc,syr | modeled | 2,838 | 220 | $4.26 | $7.02 |
| anf03_tertullian.xml | pahc | modeled | 2,758 | 231 | $4.22 | $6.99 |
| athanasius_opera-omnia-pg25-grc-lat_migne1857.txt | alx,ijc | modeled | 2,466 | 276 | $3.98 | $6.99 |
| josephus_works-antiquities-wars-life_whiston1859.txt | alx,pahc,syr | modeled | 3,048 | 178 | $3.96 | $6.92 |
| npnf204_athanasius-select-works-letters.xml | alx,desert,ijc,pahc | modeled | 2,779 | 220 | $4.17 | $6.91 |
| crespin_histoire-des-martyrs-t3-fra_benoit-lelievre1889.txt | rzg | modeled | 2,869 | 198 | $4.01 | $6.83 |
| augustine_opera-minora-catechetica-lat_migne-pl40.txt | lpc | modeled | 2,789 | 205 | $4.01 | $6.77 |
| mansi_sacrorum-conciliorum-collectio-tomus-2-305-346-lat_welter-facsimile1901.txt | alx,don,ijc,lpc | modeled | 2,860 | 192 | $3.95 | $6.73 |
| gregory-nazianzen_epistulae-carmina-pg37-grc-lat_migne1857.txt | cappadocian | modeled | 2,377 | 266 | $3.83 | $6.72 |
| anf05_hippolytus-cyprian-caius-novatian.xml | cappadocian,don,lpc | modeled | 2,652 | 220 | $4.08 | $6.71 |
| npnf201_eusebius-church-history-life-of-constantine.xml | alx,ijc,pahc,syr | modeled | 2,704 | 210 | $3.99 | $6.68 |
| gregory-nyssa_opera-omnia-pg45-grc-lat_migne1858.txt | cappadocian | modeled | 2,331 | 267 | $3.79 | $6.66 |
| augustine_sermones-1-340-lat_migne-pl38.txt | lpc | modeled | 2,717 | 197 | $3.88 | $6.57 |
| anf04_tertullian4-minucius-felix-commodian-origen1-2.xml | alx,desert,hal | modeled | 2,586 | 215 | $3.95 | $6.53 |
| gregory-nyssa_opera-omnia-pg46-grc-lat_migne1863.txt | cappadocian | modeled | 2,204 | 247 | $3.55 | $6.24 |
| npnf111_chrysostom-homilies-acts-romans.xml | ijc | modeled | 2,505 | 198 | $3.71 | $6.22 |
| pl11-zeno-optatus-collatio-carthaginiensis_migne.txt | don,lpc | modeled | 2,557 | 190 | $3.69 | $6.21 |
| anf07_lactantius-apostolic-constitutions-didache-liturgies.xml | alx,hal,ijc,pahc,syr | modeled | 2,351 | 205 | $3.69 | $6.04 |
| gregory-nazianzen_orationes-pg35-grc-lat_migne1857.txt | cappadocian | modeled | 2,187 | 229 | $3.42 | $6.03 |
| quick_synodicon-in-gallia-reformata_1692.txt | rzg | modeled | 2,595 | 156 | $3.41 | $5.92 |
| mansi_sacrorum-conciliorum-collectio-tomus-5-431-441-lat_welter-facsimile1901.txt | ijc | modeled | 2,531 | 160 | $3.40 | $5.86 |
| npnf101_augustine-confessions-letters.xml | don,hal,ijc,lpc | modeled | 2,398 | 181 | $3.49 | $5.86 |
| marius-mercator_opera-omnia-lat_migne-pl48.txt | ijc | modeled | 2,324 | 181 | $3.43 | $5.75 |
| anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml | alx,pahc,syr | modeled | 2,274 | 187 | $3.46 | $5.72 |
| npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml | lpc | modeled | 2,331 | 175 | $3.39 | $5.68 |
| epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt | cappadocian | modeled | 1,972 | 222 | $3.19 | $5.60 |
| mansi_sacrorum-conciliorum-collectio-tomus-4-410-431-lat_welter-facsimile1901.txt | lpc | modeled | 2,388 | 155 | $3.25 | $5.57 |
| anf01_apostolic-fathers-justin-irenaeus.xml | pahc | modeled | 2,232 | 172 | $3.30 | $5.49 |
| npnf105_augustine-anti-pelagian-writings.xml | gallic,lpc | modeled | 2,225 | 171 | $3.30 | $5.48 |
| npnf113_chrysostom-homilies-galatians-philemon.xml | ijc | modeled | 2,233 | 165 | $3.22 | $5.43 |
| npnf104_augustine-anti-manichaean-anti-donatist.xml | don,ijc,lpc | modeled | 2,229 | 165 | $3.23 | $5.42 |
