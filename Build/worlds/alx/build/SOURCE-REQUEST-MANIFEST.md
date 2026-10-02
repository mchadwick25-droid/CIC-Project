# Alexandria — Source Request Manifest

**World:** `alx` / `alexandria-catechetical` (working identity — see §0)
**Produced at:** per-world build step 2, Source ecology (spec §4.3.2), 2026-08-20
**For:** Mark, in his operational source-acquisition role (Build-Blueprint §7)
**Status v2 (2026-08-20, same day):** the first version of this manifest went out as a pure REQUEST. The vendored public-domain corpus (`cic/texts/`, 38/38 ANF/NPNF volumes plus extras, supplied by Mark 2026-08-15–18) arrived on this branch hours later and **already covers seven of the eleven requests**. Those seven are now marked SUPPLIED, each with rights **verified from the vendored file's own provenance header** (per spec §4.3.2 — never from this request) and a created `alx.source.*` record. What remains below as OPEN is the true outstanding wantlist. The five decisions in §5 are still Mark's.
**Search basis:** every entry is grounded in a real search run 2026-08-20, recorded in `records/alx/search_record/` (index at §9) — including the searches that came back empty. One first-pass error was found and corrected on arrival of the real files: *Quis dives salvetur* is in ANF 2 after all (the Loeb was never the only PD English; see `alx.search.clement-loeb-butterworth`'s correction note).

---

## 0. Working scope (step 1, light — NOT a ruling)

World/Representative identity is one of Mark's four per-world touchpoints (Build-Blueprint §4). This section exists only so source selection has a boundary; it takes the Artifact-1 worked example as its working scope and changes nothing:

- **Time window:** c. 150–400 CE (per the registry example in Artifact-1 §2).
- **Place:** Alexandria and Egypt.
- **What it is:** the Alexandrian Christian formation ecology anchored on its catechetical-formation tradition — learned teaching, allegorical-spiritual reading of Scripture, staged catechumenate, confident engagement with Greek thought (Clement, Origen, the teaching tradition through Didymus, the episcopal line through Athanasius).
- **What it is *not*** (source-selection boundary only):
  - **Not the desert.** Desert monasticism is the planned second world (spec §9 stage 7). Desert-formation texts (*Apophthegmata*, Pachomian material, Evagrius) are **excluded**; the two boundary texts touching both (Life of Antony, Lausiac History) carry an explicit cross-build flag in their source records. The prior build record held the attribution question open; nothing here closes it.
  - **Not Philo / not Judaism.** Philo is pre-horizon and Jewish; listed only as a *diagnostic* acquisition (§6), never evidence of Christian practice.
  - **Not the Gnostic schools as insiders.** Nag Hammadi material would be context for what this world defined itself against; not requested at this step (§8).
  - **Not post-Chalcedon** — and specifically **not the Origenist controversy of c. 399–553**: the vendored corpus contains extensive material from that later controversy (npnf202/203/206/211/214), which is out-of-horizon for this world's voice. The corpus scrub's "Out-of-horizon traps found" section (`Build/Ministry/Technology/table_phase0/Texts_Scrub_alexandria.md`) is the standing map of what not to cite; every later build step should read it before touching anything Origen-related in those volumes.
- **Open scope question for Mark (flag, not a guess):** whether the window's *practical* center of gravity should be stated as 150–400 evenly or as "richest 180–260, thinner late" — the vendored evidence is heavily early-to-mid horizon (see G3). Affects emphasis, not the boundary.

---

## 1. How to read this manifest

- **Vendoring rule.** Only public-domain texts are vendored (spec principle 14). SUPPLIED entries live in `cic/texts/` with rights read from each file's own header (the generated `cic/texts/README.md` re-reads them on every run). §5–§6 name copyrighted works that would be **consultation-only** if acquired — research inputs whose text can never enter records as licensed quote material.
- **For OPEN entries**, the preferred acquisition form remains the archive.org scan of the printed volume (a scan carries its own title page, date, and publisher — exactly what a rights header needs), or a CCEL export matching the vendored corpus's format. New Advent e-texts are not preferred (site claims a compilation copyright on its edits).
- **Why 19th/early-20th-century translations?** The only complete public-domain corpus; serviceable for these authors; the register bar is met by the voice build, not the source translation. Where a modern edition is *materially* better, it is named in the entry and weighed in §5.
- **Priority:** P1 = build cannot proceed sensibly without it; P2 = strongly wanted; P3 = bounded/optional.

---

## 2. Primary sources

### 2.1 Clement of Alexandria — ANF vol. 2 — **P1 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20.
- **Source records:** `alx.source.clement-protrepticus` · `alx.source.clement-paidagogos` · `alx.source.clement-stromateis` · `alx.source.clement-quis-dives` (the last a first-pass correction: Wilson's *Quis dives* is in this volume).
- **Book III of the Stromateis is Latin-only in this edition** — stated by the file's own header ("Extended Latin sections") and in the source record. See G1.
- **Canon families:** C, F1, F2, F4, **F5 richly** (Paedagogus II–III; Quis dives for F5-T money), F6.

### 2.2 Clement — Loeb LCL 92 (Butterworth, 1919) — **P3 · OPEN (downgraded from P2)**
- **Why downgraded:** its unique-content claim was my error — *Quis dives* is in ANF 2. Remaining value: Butterworth's markedly more readable Protrepticus, and the *To the Newly Baptized* fragment.
- **Edition/location:** *The Exhortation to the Greeks; The Rich Man's Salvation; To the Newly Baptized* (Loeb 92, Harvard UP, 1919) — https://archive.org/details/exhortationtogre0000clem
- **Expected rights:** US public domain (1919, pre-1930). Non-US status less certain — flagged, not resolved.

### 2.3 Origen — ANF vol. 4 — **P1 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20.
- **Source records:** `alx.source.origen-de-principiis` (Rufinus-softening caveat in its work field) · `alx.source.origen-contra-celsum`.
- **Canon families:** C-E and F2-E above all (Contra Celsum, the evidential engine); F1; F2 (De Principiis IV). Modern-better: Chadwick's *Contra Celsum* (CUP 1953) — §5.
- Also in this volume for later steps: the Origen–Africanus letters (the Susanna exchange — text-critical practice material).

### 2.4 Origen — ANF vol. 9 (the surviving commentaries) — **P2 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20.
- **Source records:** `alx.source.origen-comm-john` (books I–X) · `alx.source.origen-comm-matthew` (books I–II, X–XIV). Partiality stated in the work fields.

### 2.5 Origen — *Philocalia* (Lewis, 1911) — **P2 · SUPPLIED 2026-08-21, verified**
- **Vendored file:** `cic/texts/origen_philocalia_lewis1911.txt` (commit 311b132) — "Rights: Public Domain" in the file's own header plus the transcriber's footer declaration ("transcribed by Roger Pearse, 2003... public domain - copy freely"), both read directly 2026-08-21. Translator identification (Lewis, T&T Clark 1911) is external-only — not inline in the transcription — flagged in the file's header and the source record's edition field.
- **Source record:** `alx.source.origen-philocalia`, with the reciprocal `associated-with` relation to `alx.source.origen-de-principiis` that the search record required: records citing De Principiis IV prefer or cross-check the Philocalia's Greek-derived text against Crombie-of-Rufinus.
- Content spot-verified: the senses-of-Scripture material (the Literal/Moral/Mystical table; "As man consists of body, soul, and spirit, so too does Scripture") present at file lines 51 and 76.

### 2.6 Athanasius — NPNF2-04 — **P1 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/npnf204_athanasius-select-works-letters.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20.
- **Source records:** `alx.source.athanasius-de-incarnatione` (the De inc. 54 line verified verbatim at file line 18744) · `alx.source.athanasius-vita-antonii` (cross-build flag) · `alx.source.athanasius-festal-letters` (incl. Letter 39's canon list) · `alx.source.athanasius-contra-arianos` · `alx.source.athanasius-de-decretis` (the F1-E council cell).
- Volume has documented per-work translator splits (Newman/Robertson, Ellershaw, the 1854 Festal rendering) — each source record carries a re-check-at-first-quote instruction.

### 2.7 Gregory Thaumaturgus — *Address of Thanksgiving to Origen* — **P1 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20; the Address's division at file line 2288.
- **Source record:** `alx.source.gregory-address-to-origen` (Nautin dating caveat in its work field).
- Also in this volume for later steps: Gregory's *Declaration of Faith* and Canonical Epistle.

### 2.8 Dionysius of Alexandria — **P2 · SUPPLIED via ANF 6, verified; Feltoe stays OPEN at P3**
- **Vendored:** the "Extant Fragments of Dionysius" in the same anf06 file (title at line 7864) → `alx.source.dionysius-extant-fragments`. A correction to this manifest's own framing: the fragments are directly present as collected English — "survives via Eusebius" is the *ancient* transmission story (the caveat stands in the record), not a modern-access problem.
- **Still OPEN (P3):** Feltoe, *St. Dionysius of Alexandria: Letters and Treatises* (SPCK 1918) — https://archive.org/details/stdionysiusofale00dion · Gutenberg #36539 — fuller and better organized; wanted, not blocking.

---

## 3. Secondary narrative sources (accounts *of* the world, not voices within it)

### 3.1 Eusebius — *Ecclesiastical History* (McGiffert, NPNF2-01) — **P1 · SUPPLIED, verified**
- **Vendored file:** `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` — `DC.Rights: Public Domain`, read from the file 2026-08-20.
- **Source record:** `alx.source.eusebius-historia-ecclesiastica` — the HIGH institutional-claims risk split is in its work field; only the Church History (McGiffert's translation) is the record's work, not the volume's Life of Constantine.
- Carries primary date attestations for Origen, Pantaenus, Demetrius, and others — figure-record material for step 3, with the risk screen active.

### 3.2 Palladius — *Lausiac History* (Lowther Clarke, 1918) — **P3 · SUPPLIED, verified; cross-build flag**
- **Vendored file:** `cic/texts/palladius_lausiac-history_clarke1918.txt` — "Rights: Public Domain" in the file's own prepended header, read 2026-08-20; the Didymus eyewitness passage at line 211.
- **Source record:** `alx.source.palladius-lausiac-history` — bounded to personally-witnessed Alexandria-adjacent material; received desert accounts belong to the Desert world's question.

---

## 4. Documentary channel

### 4.1 Oxyrhynchus Papyri — Grenfell & Hunt early volumes — **P3 · OPEN, bounded**
- **Edition:** *The Oxyrhynchus Papyri* vols. I–IV (Egypt Exploration Fund, 1898–1904) — archive.org scans, e.g. https://archive.org/details/oxyrhynchuspapyr01grenuoft
- **Expected rights:** public domain (1898–1904). Not in the vendored corpus.
- **Why:** the only channel where non-elite Egyptian Christians appear unmediated by a literary author (F5; the F5-E "how do historians even know" cell). **Honest bound unchanged:** huge scholarly volumes, not a curated corpus — identifying usable Christian pieces is step 3/4 editorial work, named as such, and no claim is made now about how much our window will yield.

---

## 5. Gaps — CLOSED by Mark's ruling, 2026-08-21

**RULING (Mark, 2026-08-21, relayed via the build-thread check-in):** *"the rest is not retreavable at this point (maybe later we can translate the greek text for some of these), but for now we need to move on."* All five gaps below are **closed as accepted honest absences** — recorded on each search record with the ruling and date. The translate-from-Greek possibility is real for G1 (Clement's Greek survives) and G3 (the Tura originals are Greek) but is future work carrying the unresolved build-made-translation review question. Consequences flow forward as designed: the skews go into world_core cautions at step 3, and canon cells these gaps leave unservable end in honest_limit records at step 4 — never papered over.

All four textual gaps were **independently confirmed by the corpus scrub** (`Texts_Scrub_alexandria.md`, "Absences"): the complete vendored 38-volume set lacks them too. Copyrighted works can be **consulted** during the build (informing sourced paraphrase at honest confidence) but **cannot be vendored** or quoted as licensed text (spec principle 14). The options columns below are retained as the decision record; the (a)/(b) choices are now moot except where Mark later reopens one.

| # | Gap (search record) | What's missing | Options |
|---|---|---|---|
| **G1** | `alx.search.stromateis-iii-english` (not_found; confirmed by the anf02 file's own Latin-sections header) | *Stromateis* III — marriage, sexuality, the body; feeds F5-T marriage and F6 identity-collision (divorce/remarriage) cells | (a) acquire Ferguson (FOTC 85, 1991) or Oulton/Chadwick (LCC II, 1954) consult-only; (b) accept thinness → honest_limit records. Recommend (a): those cells are canon-required and demonstration-required. *Status note (relayed 2026-08-21, not verified on this branch): Mark located an Oulton/Chadwick 1954 text and it was correctly NOT vendored (in-copyright) — option (a) may already be in hand as consult-only; the decision is still his.* |
| **G2** | `alx.search.origen-homilies-pd` (not_found; scrub concurs: "no homily exists in any vendored volume") | Origen's homiletic corpus — his *congregational* voice; without it the vendorable Origen skews elite/systematic | (a) Heine FOTC 71 (Gen/Ex), Lienhard FOTC 94 (Luke), Lawson ACW 26 (Song) consult-only; (b) accept skew → state in world_core cautions. Recommend (a) for at least one homily volume. |
| **G3** | `alx.search.didymus-tura-english` (not_found; the fleet wantlist independently rules it: "discovered 1941... there cannot be" a PD edition) | Didymus — the late-horizon teaching tradition in its own words | (a) Hill FOTC 111 consult-only; (b) accept: the late horizon speaks through Athanasius plus vendored testimonia (Palladius line 211; Jerome De viris 109 in npnf203; Socrates IV.25 in npnf202) → honest_limit where cells depend on it. Either defensible; the skew must be stated regardless. |
| **G4** | `alx.search.athanasius-marcellinus-pd` (not_found) | *Letter to Marcellinus* (praying the Psalms) | Low severity — F4 prayer served elsewhere. (a) Gregg (CWS 1980) consult-only; (b) drop. Recommend (b). |
| **G5** | `alx.search.origen-on-prayer-curtis` (found, rights caution; not vendored) | *On Prayer* — CCEL hosts Curtis's translation as PD, but it reached CCEL undated via private papers | (a) accept CCEL's PD assertion and vendor with the caution in the provenance header; (b) treat as consult-only. Mark's call — the file's own header decides at record admission either way. *Status note (relayed 2026-08-21): a CCEL ThML export of the same page was supplied but adds no provenance clarity on the chain-of-custody question; not vendored, still open.* |

**Standing recommendation on consult-only acquisitions:** research inputs for steps 3–5, never archive texts; contributions enter records as sourced paraphrase at honest confidence, never as licensed quotes.

---

## 6. Diagnostic and background sources (not world evidence)

- **Philo of Alexandria — P3 · OPEN, diagnostic only.** Yonge's translation (1854–55, 4 vols., archive.org) is comfortably PD. The fleet wantlist (Tier 2 #3) independently requests exactly this. Never evidence of Christian practice; the inheritance-vs-transformation diagnostic.
- **Secondary scholarship** (all copyrighted, consult-only; the prior build's independently-verified list, reusable as a shopping list): Young (1997); van den Hoek (1988); Chadwick (1966; 1953); Louth (1981/2007); Williams, *Arius* (1987/2001); Rubenson (1990/95); Brakke (1995, 2006); Pearson (2004); **Wipszycka (2009, 2015)** and **Bagnall (1993)** — the two most important correctives to the corpus's elite bias; Brown (1971, 1988); Runia (1993).

---

## 7. Canon coverage sketch (expectation, not verification — coverage is proven at steps 4/6)

- **C (Center):** strong. De Incarnatione, Contra Celsum (evidential), Protrepticus, John commentary.
- **F1 (God & doctrine):** strong. De Principiis, anti-Arian corpus, De Decretis (council cells), Logos material throughout.
- **F2 (Scripture & sources):** strong. Stromateis, De Principiis IV (Philocalia control pending, §2.5), commentaries, Festal Letter 39 (the canon list); Eusebius (etic) for how-we-know questions.
- **F3 (Church & world):** good. Eusebius (risk screen active), Dionysius (persecution lived), Festal Letters, Contra Celsum (outsider view).
- **F4 (Living the faith):** good. Paedagogus, Gregory's Address, Festal Letters, Dionysius on restoration of the lapsed. Prayer cells thinner while G5 is open.
- **F5 (Daily life):** **the honest-thinness family.** Paedagogus II–III and Quis dives are real strengths; Dionysius's plague letters (sickness/death); papyri pending (§4.1). But **women in their own words — no female-authored Alexandrian Christian text survives in the window** (the Artifact-1 worked example `alx.limit.f5-women-own-words` will be borne out); enslaved persons, children, rural/Coptic-speaking believers — expect honest_limit records in several F5 cells. The world's structural evidence problem, carried openly.
- **F6 (Hard places):** adequate-to-good, unevenly. Persecution/suffering strong; church-failure cells servable (the lapsed); identity-collision cells depend partly on G1. The in-horizon "Origen problem" (the tradition's ambivalence about its greatest teacher, through the c. 399–400 eruption) is strong F6 material — with the out-of-horizon trap map (§0) governing what may not be cited.
- **Register note:** personal-register (P) cells are served by the same sources; what makes them answerable is the voice build (step 5). No source is requested "for the P register" — a category error worth naming.

## 8. Not yet searched (honest bounds of this pass)

- **Coptic material in translation** (martyr acts, early Coptic scripture witness): not searched; expected mostly modern-copyrighted, unverified. Worth one pass at step 3 given the Greek/Coptic asymmetry.
- **Origen, *Exhortation to Martyrdom* / *Dialogue with Heraclides*** (the latter a 1941 Tura find — almost certainly no PD English; unverified).
- **Eusebius, *Praeparatio Evangelica*** (Gifford 1903, PD — fleet wantlist Tier 3 #10 names it for Alexandria; carries fragments of lost Alexandrian authors): flagged, not yet assessed for this world's needs.
- **Nag Hammadi in English** (context-only if ever requested): not searched.
- **Archaeology/epigraphy beyond Oxyrhynchus**: likely secondary-literature territory (Wipszycka, Bagnall) rather than vendorable texts.

## 9. Search record index (`records/alx/search_record/`)

Found, now SUPPLIED with source records: `clement-anf2` · `origen-anf` · `origen-philocalia-lewis` (supplied 2026-08-21) · `athanasius-npnf2-04` · `gregory-address-anf6` · `eusebius-npnf2-01` · `dionysius-feltoe` (via the ANF 6 fallback) · `palladius-lausiac-clarke`
Found, still OPEN: `clement-loeb-butterworth` (P3, corrected) · `origen-on-prayer-curtis` (G5 decision) · `oxyrhynchus-grenfell-hunt` (P3, bounded)
Not found (all four independently confirmed against the vendored corpus): `stromateis-iii-english` · `origen-homilies-pd` · `didymus-tura-english` · `athanasius-marcellinus-pd`

## 10. The source base as it stands (`records/alx/source/`, 18 records, all rights verified from file headers)

Clement: `clement-protrepticus` · `clement-paidagogos` · `clement-stromateis` · `clement-quis-dives`
Origen: `origen-de-principiis` · `origen-contra-celsum` · `origen-comm-john` · `origen-comm-matthew` · `origen-philocalia` (⇄ de-principiis, associated-with)
Gregory: `gregory-address-to-origen` · Dionysius: `dionysius-extant-fragments`
Athanasius: `athanasius-de-incarnatione` · `athanasius-vita-antonii` · `athanasius-festal-letters` · `athanasius-contra-arianos` · `athanasius-de-decretis`
Narrative (etic): `eusebius-historia-ecclesiastica` · `palladius-lausiac-history`

---

*Step-2 state: **CLOSED 2026-08-21.** The P1 core and the Philocalia are supplied and verified (18 source records); the five gaps are closed by Mark's ruling as accepted honest absences; only the P3 tail (Loeb, Feltoe, Oxyrhynchus, Philo/Yonge) remains as optional future acquisitions, none blocking. Step 3 (ecology reconstruction) proceeds on this base. The prior build's scrub (`Texts_Scrub_alexandria.md`) is lead material for steps 3–4 — verify every lead against the vendored text itself, never trust its paraphrase, and honor its out-of-horizon trap map. Registry entry for `alx` in `records/worlds.yaml` is deliberately not added — identity is Mark's touchpoint and the registry is the build thread's file.*
