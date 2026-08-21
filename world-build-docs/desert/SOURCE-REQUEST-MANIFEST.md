# Desert Monasticism — Source Request Manifest

**World:** `desert` / `desert-monasticism` (World #3)
**Produced at:** per-world build step 2, Source ecology (spec §4.3.2), 2026-08-21
**For:** Mark, in his operational source-acquisition role (Build-Blueprint §7)
**Status:** first version. The vendored public-domain corpus (`cic/texts/`, supplied by Mark 2026-08-15–18 for the Alexandria build, copied to this branch 2026-08-21) already covers this world's four strongest vendorable primaries; the true outstanding wantlist is §5. Rights on every SUPPLIED entry were **verified from the vendored file's own provenance header** (per spec §4.3.2 — never from this request).
**Scope basis:** the approved Doc_01 (`World-Builds/Desert-Monasticism/CiC_W3_Doc01_World_Identification.md`, Approved to proceed, reviews on file): c. 320 floor (Pachomius at Tabennesi) with Antony's 270s–305 career as the movement's own pre-floor generative reference; close c. 430 (the least-confident boundary, held as directional); Lower Egypt (Nitria, Kellia, Scetis) + the Thebaid (Pachomian houses) + Antony's two mountains; three strands (A anchoritic, B cenobitic, C semi-anchoritic); Shenoute/White Monastery excluded; Melitian relationship unresolved.
**Search basis:** every entry is grounded in a real search run 2026-08-21, recorded in `records/desert/search_record/` — including the searches that came back empty.

---

## 1. How to read this manifest

- **Vendoring rule.** Only public-domain texts are vendored (spec principle 14). SUPPLIED entries live in `cic/texts/` with rights read from each file's own header. Copyrighted works are **consultation-only**: research inputs whose text can never enter records as licensed quote material.
- **For OPEN entries**, the preferred acquisition form is the archive.org scan/text of the printed volume (carries its own title page, date, publisher — what a rights header needs). **This session's own network policy blocks archive.org downloads** (proxy CONNECT 403, verified), which is the only reason the Budge volumes are OPEN rather than SUPPLIED.
- **Priority:** P1 = the build is materially poorer without it; P2 = strongly wanted; P3 = bounded/optional.

---

## 2. Supplied and verified (no action needed)

| source record | file | what it carries for this world |
|---|---|---|
| `desert.source.athanasius-vita-antonii` | `npnf204…xml` (`DC.Rights: Public Domain`) | the founding narrative, outsider-authored; §§46–47 daily-martyrdom anchor verified verbatim |
| `desert.source.cassian-institutes` / `desert.source.cassian-conferences` | `npnf211…xml` (PD) | Egyptian teaching in codified export. Edition gaps (checked at division-body level, Review Round 1): Conf. XII and XXII and Institutes Book VI are untranslated in this edition — the sexuality material is excised entirely |
| `desert.source.palladius-lausiac-history` | `palladius_lausiac-history_clarke1918.txt` (PD) | the resident observer; Pachomius ch. XXXII; Cellia nine years |
| `desert.source.socrates-historia-ecclesiastica` | `npnf202…xml` (PD) | the only vendored English Evagrius excerpts (IV.23); the 399–400 Origenist sequence |
| `desert.source.sozomen-historia-ecclesiastica` | `npnf202…xml` (PD) | Pachomian rule content at one remove (III.14) |
| `desert.source.athanasius-festal-letters` | `npnf204…xml` (PD) | Festal Letter 39 (367) — the Nag Hammadi contested claim's anchor |
| `desert.source.jerome-de-viris` | `npnf203…xml` (PD) | Jerome's attestation of Antony's seven letters; Gennadius on Pachomius/Theodorus/Orsiesius |
| `desert.source.jerome-letter-22` | `npnf206…xml` (PD) | the 384 outside typology of Egyptian monk-kinds (§§34–36) |

Registered without files (no vendorable edition exists or acquisition is blocked): `apophthegmata-patrum`, `pachomian-corpus`, `antony-letters`, `evagrius-praktikos`, `historia-monachorum`, `kellia-excavations`, `nepheros-archive`, plus the eight consult-only scholarship records (Brakke ×2, Rubenson, Gould, Burton-Christie, Goehring, Rousseau, Veilleux — Gould and Veilleux added at Review Round 1, Finding 4, so no load-bearing name floats unregistered).

---

## 3. OPEN requests

### G1 — Budge, *The Paradise or Garden of the Holy Fathers* (1907), vols. 1–2 — **P1**
- **What:** E. A. Wallis Budge's translation of ʿEnanishoʿ's 7th-c. Syriac *Book of Paradise*: vol. 1 = Palladius + the History of the Monks (Syriac recension); **vol. 2 = the Sayings of the Fathers — the only public-domain English Apophthegmata corpus in existence.**
- **Where:** archive.org — vol. 2 identifier `ParadiseOfTheHolyFathersV2`; vol. 1 e.g. `paradiseorgarde01budggoog` / `theparadiseorgar01unkwuoft`; also `en.wikisource.org/wiki/The_Paradise/Volume_2`. Plain-text (djvu.txt) or any export carrying the title page.
- **Expected rights:** public domain in the US (1907 publication) and in life+70 jurisdictions (Budge d. 1934); a few longer-term jurisdictions differ — the file's own front matter decides at vendoring, as always.
- **Why P1:** the Apophthegmata is this world's central teaching corpus. Until this file lands, **every saying in the record set is license `paraphrase-only` and no verbatim saying can be voiced.** On arrival: verify rights from the scan's own front matter, vendor, re-verify each paraphrase-only quote against Budge's text and upgrade to `verbatim` (with the Syriac-recension caveat in each locus) where exact.
- **This session could not fetch it:** network policy blocks archive.org file downloads (verified; recorded in `desert.search.apophthegmata-pd-english`).

### G2 — consult-only acquisitions (decision, not download) — **P2**
Confirm whether these are available to the build as consult-only research inputs (never vendored, never quoted): Veilleux, *Pachomian Koinonia* vols. 1–2 (Rule + Lives); Rubenson, *The Letters of St. Antony*; Gould, *The Desert Fathers on Monastic Community*; Ward, *The Sayings of the Desert Fathers* (accuracy control for paraphrased sayings until Budge lands); Brakke ×2, Burton-Christie, Goehring, Rousseau (already carried by the prior build's registry, assumed still in hand). All except Ward now have consult-only source records.

---

## 4. Closed absences (no action possible; consequences flow forward as designed)

| search record | what's missing | consequence in the record set |
|---|---|---|
| `desert.search.pachomian-rule-english-pd` (not_found) | PD English of the Pachomian Rule | Strand B's charter is never quoted; Rule content is "as reported by" Palladius XXXII / Sozomen III.14, or consult-only paraphrase — stated in world_core cautions |
| `desert.search.pachomian-lives-english-pd` (not_found) | PD English of any Pachomian Life | founding-narrative claims held to cross-recension consistency |
| `desert.search.antony-letters-english-pd` (not_found) | PD English of Antony's Letters | the literacy contest lives at contested-claim level only; no Letters text voiced |
| `desert.search.evagrius-praktikos-english-pd` (not_found) | PD English of Evagrius's works | Evagrius quotable only via Socrates IV.23 excerpts (vendored), double-caveated |

## 5. Standing flags carried into step 3+

- **Author gravity, world-level:** the most influential witnesses are Greek-literate outsiders describing a majority-Coptic, largely non-literate movement (Doc_01 §4 — load-bearing; goes into world_core cautions).
- **Goehring verification bound** (Doc_01 §11 item 6, still open): his specific papyrological claims remain independently unverified; embeddedness claims cite Kellia + Nepheros + Goehring jointly.
- **Melitian relationship** (Doc_01 §11 item 1, still open): the Nepheros archive's representativeness rests on an unverified assumption — carried as a contested claim at step 3.
- **Nag Hammadi–Pachomian theory** (Doc_02 §5.3): genuinely unresolved in the scholarship; carried as a contested claim, neither position adopted.
- **"White martyrdom"** (Doc_01 §11 item 7): RESOLVED — in-world anchor is Vita 46–47 ("daily a martyr to his conscience"), verified verbatim; the term itself is later and external, never voiced as native (`desert.search.white-martyrdom-citation`).
- **Out-of-horizon traps in the vendored corpus:** npnf203/206 Latin Origenist polemics (Palestine/Italy quarrel, not this world's); npnf202 material past c. 430; Chalcedon-era content everywhere in series 2. The world's own late-controversy record is the Egyptian sequence of 399–400 only.

---

## 6. Search-record index

`records/desert/search_record/`: `vita-antonii-npnf204` (found) · `cassian-npnf211` (found) · `lausiac-clarke1918` (found) · `apophthegmata-pd-english` (found, acquisition OPEN → G1) · `historia-monachorum-english-pd` (found, OPEN → G1) · `pachomian-rule-english-pd` (not_found) · `pachomian-lives-english-pd` (not_found) · `antony-letters-english-pd` (not_found) · `evagrius-praktikos-english-pd` (not_found; Socrates IV.23 partial exception) · `white-martyrdom-citation` (found, resolved).
