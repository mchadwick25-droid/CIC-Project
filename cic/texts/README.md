# Vendored public-domain source texts

Full text of editions this build's quote records cite, committed so that
wording can be verified *reproducibly* — by any session, at any time,
without network access. That matters here for a specific reason: the
sandbox this project's agents run in blocks every patristic text host
(ccel.org, newadvent.org, wikisource, archive.org, gutenberg, tertullian.org),
so before these files existed a quote record could not be verified at all
and `gate_quote_fidelity_recording` had nothing honest to record.

PUBLIC DOMAIN ONLY. Every file here must be out of copyright, and its own
provenance header must say so. In-copyright editions (Holmes 2007, Ward
1975) are referenced by `source` record and never vendored — committing
them would be redistribution.

| file | edition | source record | covers |
|---|---|---|---|
| `anf01_apostolic-fathers-justin-irenaeus.txt` | Ante-Nicene Fathers vol. 1 (Roberts & Donaldson eds.; Coxe, American ed.; Buffalo, 1885). CCEL proofed transcription; header states `Rights: Public Domain`. Supplied by Mark 2026-08-15. | `srcPAHCS62` | Ignatius, Polycarp (letter + Martyrdom), 1 Clement, Justin Martyr |
| `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.txt` | Ante-Nicene Fathers vol. 2: Fathers of the Second Century (same eds./publisher, 1885). CCEL proofed transcription; header states `Rights: Public Domain`. Supplied by Mark 2026-08-15. | none yet | Shepherd of Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria |

| `anf03_tertullian.txt` | Ante-Nicene Fathers vol. 3: Latin Christianity: Its Founder, Tertullian (Roberts, Donaldson, Menzies eds.; 1885/1896). CCEL proofed transcription; header states `Rights: Public Domain`. Supplied by Mark 2026-08-15. | none yet, but see note | Tertullian: Apologetic, Anti-Marcion, Ethical works |

NOTE ON anf03: carries Tertullian's Apologeticus (the Apology) - the
PRIMARY TEXT srcPAHCP15 already cites in pahc ("Tertullian, Apology 39",
language corrected grc->lat earlier this session). No quote record for
Tertullian was in this session's worklist, but the translation edition is
now sitting here if one is ever wanted.

NOT IN THIS SERIES: anything post-Nicaea (325 CE) by definition — Athanasius,
Julius I of Rome, Ambrose, Leo I, etc. belong to the companion Nicene and
Post-Nicene Fathers series instead. Checked directly in anf02: every
"Julius" occurrence in the file is Julius Africanus (the chronographer) or
Julius Caesar, not Julius I of Rome — confirming the volume cannot carry
his 341 letter to the Eusebians (needed for `srcIJC04`/`srcIJC42`), which
is why a separate NPNF vol. 4 supply is still needed.

Not records: nothing here is schema-validated or read by the runtime. These
are reference copies for verification, cited by the `source` records that
carry the bibliographic data.
