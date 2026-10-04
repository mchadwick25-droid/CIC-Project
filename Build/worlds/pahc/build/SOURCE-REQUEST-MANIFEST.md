# Post-Apostolic House-Church — Source Request Manifest

**World:** `pahc` / `post-apostolic-house-church`
**Produced at:** per-world build step 2, Source ecology (spec §4.3.2), 2026-08-21
**For:** Mark, in his operational source-acquisition role (Build-Blueprint §7)
**Scope authority:** Step 0 and Doc_01 (approved 2026-07-07) — settled, not restated here. Six primary voices (Didache, 1 Clement, Ignatius middle recension, Polycarp's Philippians, Hermas, Justin), plus the Martyrdom of Polycarp (P16) and four outside witnesses (Pliny, Tacitus, Suetonius, Lucian). The Pastorals are excluded from the Native base per Doc_02 §1.7; Egypt is excluded per Doc_01 §3 (the Bagnall dependency, carried at full flag strength).
**Search basis:** every entry grounded in a search recorded in `Build/worlds/pahc/build/records/search_record/` — including the two searches that came back empty, which shape the quote set more than any found-search does.

---

## 1. SUPPLIED — vendored, rights verified from each file's own header

The shared corpus (`cic/texts/`, supplied by Mark 2026-08-15–18 on the alexandria/table-voice branches, carried onto this branch at setup) already covers every vendorable need:

| need | vendored file | source record(s) |
|---|---|---|
| 1 Clement (Roberts-Donaldson) | `anf01_...xml` div ii | `pahc.source.first-clement` |
| 1 Clement complete ending (Keith, from Hierosolymitanus) | `anf09_...xml` div xii | same row, completion edition |
| Ignatius, 7 letters, SHORTER/middle recension | `anf01` div v | `pahc.source.ignatius-letters` |
| Polycarp, Philippians (all 14 chs) | `anf01` div iv.ii | `pahc.source.polycarp-philippians` |
| Martyrdom of Polycarp (all 22 chs) | `anf01` div iv.iv | `pahc.source.martyrdom-polycarp` |
| Shepherd of Hermas (Crombie) | `anf02` div ii | `pahc.source.shepherd-hermas` |
| Justin, First Apology + Dialogue | `anf01` div viii | `pahc.source.justin-first-apology`, `pahc.source.justin-dialogue` |
| Didache (Riddle ed.) | `anf07` div viii | `pahc.source.didache` |
| Anti-Montanist fragments ("Asterius Urbanus") | `anf07` div v + `npnf201` (HE V.16–17) | `pahc.source.anti-montanist-fragments` |
| Eusebius, HE (McGiffert) — witness, screened | `npnf201` | `pahc.source.eusebius-historia-ecclesiastica` |
| Irenaeus, Adversus Haereses — boundary witness | `anf01` div ix | `pahc.source.irenaeus-adversus-haereses` |
| Tertullian, Apology + Adv. Marcionem — boundary/rival witness | `anf03` | `pahc.source.tertullian-apologeticus`, `pahc.source.tertullian-adversus-marcionem` |
| Barnabas 18–20 (Two Ways parallel ONLY) | `anf01` div vi | `pahc.source.barnabas` |
| Pliny, Letters 10.96–97 + Trajan's rescript, complete English | `npnf201`, McGiffert's note to HE III.33 | `pahc.source.pliny-letters` — **corrected**: first listed OPEN; the complete text was embedded in the vendored Eusebius volume's editorial note all along (see the search record's correction note). A standalone Melmoth/Bosanquet edition is now optional (P3), for second-translation cross-checking only |
| Suetonius, Claudius 25.4 + Nero 16.2 (Thomson/Forester, Bohn, 1909) | `suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt` | `pahc.source.suetonius-lives` — **acquired 2026-09-13**: moved here from Section 2's P2 list. Surfaced by a fleet cross-world research thread's resource handoff, independently re-verified against two separate public-domain digitizations of the same 1909 printing before vendoring (see `pahc.search.suetonius-english-pd`) |

## 2. OPEN — wanted, public-domain candidates named, not fetchable from this sandbox

Priority P2 (strongly wanted — each unlocks verbatim quoting for material currently paraphrase-only):

1. **Tacitus, Annals 15.44** — Church & Brodribb (1876). PD by date.
2. **Lucian, The Passing of Peregrinus** — H.W. & F.G. Fowler (Oxford, 1905). PD by date. (Harmon's Loeb v.5, 1936, would need a renewal check — the Fowler is the safe candidate.)

~~Suetonius, Claudius 25.4 + Nero 16.2 (Thomson/Forester, Bohn)~~ — **ACQUIRED 2026-09-13**, moved to Section 1.

Preferred form, per the standing rule: archive.org scan or CCEL-format export carrying its own title page/rights header — rights are verified from the supplied file's own provenance header, never from this request.

## 3. Consult-only (never vendor — in copyright)

Holmes (2007), Ehrman's Loeb (2003), Niederwimmer (1998), Osiek (1999), and the scholarship named across the approved documents — Doc_02 §2 (Lampe, Brown, Brent, Trevett, Bradshaw), Doc_02 §4 (McGowan), Doc_01 §3 / Doc_02 §10 (Bagnall), Doc_01 §8.3 (Moll, Lieu, Thomassen, Tabbernee). Cited inline in record bodies for dating/text-critical judgments; never quote-licensed. Search: `pahc.search.modern-editions-consult-only`.

## 4. Considered and not registered (decisions, not oversights)

- **2 Clement** (present in anf09) — not among the six primary voices; contested provenance; no record needs it. Noted in `pahc.search.clement-complete-anf09`.
- **The Pastoral Epistles** — excluded from the Native base by Doc_02 §1.7's two independent grounds (settled, reviewed, Mark-signed).
- **Doctrina Apostolorum** — no vendored English; the Barnabas 18–20 parallel carries the Two-Ways-circulated claim instead.
- **Revelation / seven-churches material** — the possible "third Asia Minor profile" remains the open item Doc_01 §11 and Doc_04 §3 carry; no primary registration without a decision to widen the voice set, which is not this build's to make.
