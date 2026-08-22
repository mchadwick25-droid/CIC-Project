# syr — Lexicon master index (step 3, record-native)

Derived from the nine `records/syr/term/` records, which re-express the approved legacy Deployment Lexicon (Doc_03/Doc_06, chunks `syrlex001–009`, approved 2026-07-08) in the Artifact-1 term schema. One row per term; this index is regenerable by reading the records — the records are the source of truth.

| term record | legacy chunk | tier | canon cells | CT (contest stated?) | high-distortion-risk | single-source risk | relations (reciprocal) |
|---|---|---|---|---|---|---|---|
| `syr.term.raza-shrara` | syrlex001 | 1 | F2-I, F2-P | — | yes ("just a metaphor") | Brock-synthesis flag carried in evidential sense | madrasha · ewangeliyon-da-mhallete |
| `syr.term.qyama` | syrlex002 | 1 | F4-I, F3-I | yes — internal structure thin/contested (→ `syr.contested.qyama-structure`) | yes (monk/nun import) | low for Dem 6 core; choir-leadership claim excluded | ihidaya · tahwyata |
| `syr.term.tahwyata` | syrlex003 | 2 | — | — | mild | — | qyama · ihidaya |
| `syr.term.madrasha` | syrlex004 | 1 | F3-I | — | yes (hymn-as-decoration) | genre-priority claim bounded to genre level | raza-shrara · memra |
| `syr.term.memra` | syrlex005 | 3 | — | — | yes (later-genre readback) | Brock authenticity assessments | madrasha |
| `syr.term.ewangeliyon-da-mhallete` | syrlex006 | 2 | F2-I | yes — name's earliest attestation unresolved (→ `syr.contested.diatessaron-name`) | yes (four-Gospel assumption) | — | raza-shrara |
| `syr.term.ihidaya` | syrlex007 | 1 | F4-I | — | yes (solitary/hermit) | dual-attested, low | qyama · tahwyata |
| `syr.term.mar` | syrlex008 | 3 | — | — | mild (contemporary-usage assumption) | — | none (by design) |
| `syr.term.catholicos` | syrlex009 | 2 | F3-I | yes — application-to-this-world contest (→ `syr.contested.papa-primacy`) | yes (retrojected office) | — | none (by design, flag-only) |

**Checks discharged (cic-lexicon-index bar):**
- Every CT-tagged legacy term carries its contest into a record: qyama and Catholicos state it in the evidential sense and link to a dedicated `contested_claim` record (built at the ecology step); Ewangeliyon da-Mhallete likewise (`syr.contested.diatessaron-name`).
- Reciprocity: every `associated-with` relation above is declared on both ends (gate `reciprocity` enforces this mechanically on every run — the index cannot drift from the records).
- No analytical-distance markers in compiled meaning fields (the Doc_06 Round 1 named-scholar fix carried forward; scholarly attribution lives in `sources` and the evidential sense).
- Excluded terms remain excluded, not silently dropped: **malpana** and **Peshitta** (attestation post-dates 410 — Doc_03 §3, Doc_06 §3), **kasyutha/hayla kasya** (folded into raza-shrara), **qaddishutha**, **dukrana** (await primary-text verification).
- Readability: `quick_meaning` and `plain_meaning` pass the FK ≤ 10 gate on every term.
