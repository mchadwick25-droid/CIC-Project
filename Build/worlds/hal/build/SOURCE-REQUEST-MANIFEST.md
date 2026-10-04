# Hieronymian Ascetic-Literary — Source Request Manifest

**World:** `hal` / `hieronymian-ascetic-literary`
**Produced at:** per-world build step 2, Source ecology (spec §4.3.2), 2026-08-21
**For:** Mark, in his operational source-acquisition role (Build-Blueprint §7)
**Status:** unlike Alexandria's first pass, this manifest starts from a corpus that is already almost entirely SUPPLIED — the vendored CCEL corpus (`cic/texts/`, supplied by Mark 2026-08-15–21, mirrored onto this branch from `world/alexandria`) covers every load-bearing primary source this world's cleared prior-build documents (Doc_01–Doc_09a, all Approved to proceed) actually cite. Rights for every SUPPLIED entry are **verified from the vendored file's own provenance header** (per spec §4.3.2 — never from this request). What remains OPEN below is contextual or apparatus-level, none of it blocking.
**Search basis:** every entry is grounded in a real check run 2026-08-21, recorded in `Build/worlds/hal/build/records/search_record/` — including the searches that came back empty (`womens-own-texts`, `latin-critical-texts`, `egeria-pilgrimage`, `prosper-chronicle`, `bethlehem-archaeology`).

---

## 0. Scope (settled — not revisited here)

Step 0 and Doc_01 are approved and binding: 382–420 CE, Bethlehem AND Rome (bipolar), the full ecology of Jerome's scholarly-ascetic project *and* the aristocratic Roman women's network (Marcella, Paula, Eustochium, Fabiola) — never Jerome as a single scholarly figure. Strand-singular. This manifest only implements that scope.

**Boundary exclusions (source-selection consequences):**
- **Pre-horizon Jerome** (Epp. 1–21, the Vita Pauli, the Chalcis desert years) — background only; flagged in `hal.core.hieronymian` cautions and the npnf206 search record.
- **Not World #8** (Latin Pastoral-Congregational): Augustine's corpus is drawn on ONLY as the other side of the Jerome correspondence (npnf101 letters), never as evidence about Augustine's own world.
- **Not Desert Monasticism**: the Lausiac History is used for its two Jerome/Paula notices (chs. 36, 41) and general monastic-template context, never as constitutive evidence — the same cross-build discipline Alexandria applies to it.

## 1. Supplied and verified (all P1/P2 needs closed)

| # | Source | Vendored file | Records |
|---|---|---|---|
| 1 | Jerome, Letters (150, incl. Epp. 22, 39, 45, 46, 57, 77, 107, 108, 127; the Marcella series; the Augustine correspondence; the 416-attack cluster 135–139) | `npnf206_jerome-principal-works.xml` (DC.Rights: Public Domain) | `hal.source.jerome-ep*`, `-marcella-letters`, `-augustine-letters`, `attack-letters-416` |
| 2 | Vulgate OT prefaces (incl. the Helmeted Preface), Gospels-revision preface, commentary prefaces | same volume, div vii.ii–vii.iv | `hal.source.vulgate-prefaces` |
| 3 | Vita Hilarionis, Vita Malchi, Against Jovinianus | same volume, div vi | `hal.source.jerome-vita-*`, `-against-jovinianus` |
| 4 | Rufinus, Apologia contra Hieronymum; Jerome, Apologia adversus Rufinum; De Viris Illustribus | `npnf203_theodoret-jerome-gennadius-rufinus.xml` | `hal.source.rufinus-apology`, `-jerome-apology-rufinus`, `-jerome-de-viris` |
| 5 | Augustine's side of the correspondence (Epp. 28, 40, 71, 75, 82 etc.) | `npnf101_augustine-confessions-letters.xml` | `hal.source.augustine-letters` |
| 6 | Palladius, Lausiac History chs. 36 + 41 (hostile independent witness; wording now collated, closing Doc_02's open flag) | `palladius_lausiac-history_clarke1918.txt` | `hal.source.palladius-lausiac` |
| 7 | Sulpitius Severus, Dialogi I.8–9 (admiring independent witness — new to this build) | `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` | `hal.source.sulpitius-dialogues` |

## 2. Open requests (none blocking)

- **P3 — Egeria, Itinerarium** (McClure & Feltoe, *The Pilgrimage of Etheria*, SPCK 1919; public domain). Context for pilgrimage infrastructure; never evidence about this community specifically. `hal.search.egeria-pilgrimage`.
- **P3 — Hilberg's CSEL Latin text of the letters** (1910–1918; PD by date, no transcription found). Would let Latin-wording claims be re-verified offline; the English corpus carries everything currently load-bearing. `hal.search.latin-critical-texts`.
- **P3 — Prosper of Aquitaine, chronicle** (no standard PD English known). Only bears on the day-level precision of Jerome's death date, which no record asserts as fact. `hal.search.prosper-chronicle`.

## 3. Consultation-only (in-copyright — never vendorable; named per Doc_02 §4)

Cain (*The Letters of Jerome*, OUP 2009; *Jerome's Epitaph on Paula*, OUP 2013), Williams (*The Monk and the Book*, 2006), Kelly (*Jerome*, 1975), Rebenich (*Jerome*, 2002), Clark (*The Origenist Controversy*, 1992; "The Lady Vanishes", 1998), Cooper (*The Virgin and the Bride*, 1996). These calibrate confidence levels throughout the record set (cited by name in record bodies); none is quoted, vendored, or treated as a licensed text. **Decision for Mark, if ever:** acquiring any of these for consultation would sharpen the Marcella-correspondence dating and the Ep. 127 analysis; nothing currently rests on unverified claims from them beyond what the prior build's reviewed documents already established.

## 4. The constitutive absence

No text composed by Paula, Eustochium, Marcella, or Fabiola survives, anywhere — not a rights problem, a survival problem; no acquisition can close it (`hal.search.womens-own-texts`, including the newly-sharpened finding that Eustochium and the younger Paula's 416 letter to Innocent is *attested but lost* via Ep. 137). Recorded as data, honored in every downstream record.

---

*Review note: this manifest documents step-2 work re-derived from the prior build's cleared Doc_02 (Approved to proceed, Rounds 1–2) with all presence/rights claims re-verified directly against the vendored files on this branch, 2026-08-21. See git history of `world/hal` for the verification commits.*
