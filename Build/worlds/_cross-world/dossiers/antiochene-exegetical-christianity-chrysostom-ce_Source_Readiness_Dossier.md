# Source Readiness Dossier — Antiochene Exegetical Christianity (Chrysostom-centered)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** I.13
**Corpus-map slug:** `antiochene-exegetical-christianity-chrysostom-ce`
**Time window:** c. 350–430
**Region(s):** Antioch
**Dossier author / date:** source-research thread, 2026-09-15
**Corpus-map / `cic/texts/` state as of:** PR #179 (merged 2026-09-13)

## 1. Already assigned

46 work-rows, ~3.34 million words on disk (`wc -w` across all six `npnf109`–`npnf114` files). ~34 rows are Chrysostom's own voice (role `tradition`, confidence overwhelmingly `assigned`) — essentially the complete NPNF1 Chrysostom set: priesthood/ascetic/exile homilies, Matthew, Acts+Romans, Corinthians, Galatians–Philemon and the other epistles, John+Hebrews. Secondary voices: Theodoret of Cyrrhus (4 works — full *Ecclesiastical History*, *Eranistes*, the Anathemas counter-statements, 181 Letters; `provisional`, since he sits at the window's edge, d. c.457), the *Apostolic Constitutions* (`tradition`, `provisional` — same city and generation, though a church-order/liturgical compilation rather than exegetical), and the two Letters of Innocent of Rome concerning Chrysostom (`tradition`, `provisional` — his correspondence with Rome over the deposition, kept here as part of the Chrysostom dossier even though it is imperial-juridical material first). Context/hostile-witness: Socrates, Sozomen, Cyril of Alexandria, Cassian's *On the Incarnation, Against Nestorius* (opponent's testimony to Antiochene Christology, one generation on), the Council of Ephesus (431) and Second Council of Constantinople (553) acts.

Census's "rich ordinary-lay ethical-formation material" undersells the scale — this is one of the largest single-figure holdings in the whole corpus-map. It is not, however, the whole of Chrysostom's authentic output (missing: the 67 Homilies on Genesis, the Psalms/Isaiah commentaries, scattered freestanding moral homilies in PG 47–64 never translated in NPNF) — roughly 60–70% of his translatable corpus.

## 2. Cross-link opportunities

Checked exhaustively (every corpus-map staging file mentioning "Chrysostom" or "Antioch," 20 files) — already fully mined, nothing new found this pass:

- Socrates *Eccl. Hist.* Book VI and Sozomen Book VIII (Chrysostom's episcopate and fall) — already linked, `context`.
- Theodoret — already linked, `provisional`.
- Ephesus 431 acts — already linked, `context`.
- Athanasius's *Tomus ad Antiochenos* — explicitly considered and correctly declined (different schism, different century).
- Serapion of Antioch fragments (anf08) — wrong era (190–203), correctly held elsewhere.
- Malchion's synodal letter against Paul of Samosata (anf06) — correctly assigned to the separate `antiochene-church-third-century` (I.42) bucket instead.

**Closed, 2026-09-25:** Ammianus Marcellinus's *Res Gestae* (`ammianus-marcellinus_roman-history_yonge1862`, vendored 2026-09-13, previously cross-linked only to `imperial-juridical-christianity` for the unrelated 366 Rome basilica riot) — Book XXII's own account of Julian wintering at Antioch in 362–363: the Temple of Apollo fire at Daphne, Julian's shutting of the city's chief church on suspicion of Christian arson, and the resulting Antiochene quarrel that produced the *Misopogon*. Added as `context`: a pagan eyewitness's account of church-state hostility in this world's own city, a generation before Chrysostom's ministry there but squarely inside the c. 350–430 window — the same register already given to Socrates, Sozomen and Cyril on this bucket.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Dialogue of Palladius Concerning the Life of Chrysostom | Palladius, Bishop of Aspuna | Herbert Moore | 1921 | https://archive.org/details/thedialogueofpal00mooruoft | pd-us-by-date | direct WebFetch verification, 2026-09-13 (publisher, date, translator, `NOT_IN_COPYRIGHT` tag, full-text downloadability all confirmed against the host directly). Queued, status `not-yet-downloaded`. |

A contemporary, sympathetic eyewitness account of Chrysostom's fall and exile — the same shape of gap Possidius' *Life of Augustine* closes for `lpc`. Not currently vendored; only Palladius's separate *Lausiac History* is.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Diodore of Tarsus | Founding figure of the Antiochene exegetical school | No PD English translation exists at all — the only substantial rendering (Hill, SBL 2005) is copyrighted; surviving fragments are untranslated Greek in Migne PG 33 |
| Theodore of Mopsuestia — *Commentary on the Nicene Creed* (Mingana, Woodbrooke Studies 5, 1932) | Tagged "Public Domain" on archive.org, confirmed real and substantial (74,684-word OCR) | Two-part closure: (a) 1932 publication isn't due to enter US public domain until 2028, so the site's own tag needs independent rights verification, not blind trust; (b) even if cleared, this is his episcopal-Mopsuestia work, not the earlier Antiochene-presbyterate material (Commentary on the Twelve Prophets) that would actually anchor this world — that survives in Greek but its only translation (Hill, 2004) is copyrighted |

## 5. Open cross-world questions

- Theodoret's fit remains genuinely provisional — he sits at the window's edge (d. c.457, writing c.447–449), a coda rather than a co-equal second voice. Not a sourcing gap to close, a characterization question for Step 0/Doc_02 to weigh.
- Honest framing for whoever drafts Doc_01/Doc_02: this is "Chrysostom-centered," not a full "Antiochene school" — the school's other two pillars (Diodore, Theodore) have no clean PD path in.
