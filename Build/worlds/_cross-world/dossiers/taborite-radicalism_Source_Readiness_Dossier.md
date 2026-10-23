# Source Readiness Dossier — Taborite Radicalism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.11
**Corpus-map slug:** `taborite-radicalism`
**Time window:** 1420–1452
**Region(s):** Bohemia (the town of Tábor in southern Bohemia and its field armies)
**Dossier author / date:** Era VI library session, latinwest batch, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. The census files this entry as "Within Another World (A5)": the other world is `the-hussite-and-bohemian-brethren-movement`, which has its own dossier and 23 vendored files. Before this pass no bucket file existed for this entry. This pass vendored three files whose Taborite content is first-hand or primary, staged them here, and proposes cross-link rows to the Hussite files. Registry entries, seed rows and cross-link rows sit in the lead's snippet files until merged.

## 1. Already assigned

Every row is a file vendored this pass. Scale is the vendored file size in characters, header included. The Hussite dossier's 23 files are cross-linked in §2.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Chronicon Taboritarum (John of Lukavec and Nicholas of Pelhřimov) and the Taborite priests' replies (Höfler II, 1865) | hofler | tradition | assigned | ~2.22M chars | `hofler_geschichtschreiber-husitischen-bewegung-v2-lat_1865.txt` |
| Tractatus de origine Hussitarum, a Catholic account that names the Adamites and Taborites (Höfler II, 1865) | hofler | context | provisional | ~2.22M chars | `hofler_geschichtschreiber-husitischen-bewegung-v2-lat_1865.txt` |
| Prameny k synodám strany pražské a táborské, 1441–1444: Taborite priests' answers, in Czech (Nejedlý, 1900) | nejedly | tradition | assigned | ~619K chars | `nejedly_prameny-k-synodam-strany-prazske-a-taborske-ces_1900.txt` |
| Articuli sacerdotum hereticorum et Pikharditarum, and the Anonymus de origine Taboritarum (Höfler I, 1856) | hofler | context | provisional | ~1.89M chars | `hofler_geschichtschreiber-husitischen-bewegung-v1-lat_1856.txt` |

**Voices.** Taborites speak in two vendored texts.

- **The Chronicon Taboritarum** (Höfler II, item XXIV) is the priests' own account, in Latin, of their case against the Prague masters, from the mountain gatherings of 1419 to the Council of Basel. It prints the five articles said to have been preached to the mountain gathering of 1419 (printed pp. 478–479): priests hold no land or rents by civil title, tithes are freely given support and not a debt, priests give up civil lordship, the Gospel law suffices for the church without the old-law ceremonies and added rites, and the faithful flee thieves and robbers who climb in another way. A footnote at the foot of p. 700 marks the end of "the confession of the Taborites" (the Chronicon's first part) and cites p. 503 of a Rotterdam printing of 1616. Part II (printed p. 701 ff.) tells the Bohemians' hearing at Basel on the four articles of Prague. The Hussite dossier listed the Taborite articles and the Four Articles as open leads; this is the nearest text to both on the shelf. Nicholas of Pelhřimov is the census's Biskupec.
- **Nejedlý, 1900** prints the Taborite priests' replies to Rokycana at the synods of 1441–1444, in Czech, among the Prague party's own articles. The Taborite writer speaks of "the Taborite priests" in the third person in some passages, so each passage needs its speaker checked.

No text of Jan Žižka or Prokop the Bald is vendored; they appear in the hostile and secondary accounts (§2).

**Hostile and outside voices.** Lawrence of Březová and Aeneas Sylvius Piccolomini are on the Hussite shelf and are cross-linked in §2. Höfler I's Picard articles and the *Tractatus de origine Hussitarum* are hostile records about radical groups near Tábor.

**Scan quality.** Höfler II and Nejedlý read with scattered letter errors; they are first witnesses once checked against the page image. Höfler I reads with scattered errors after its opening pages.

## 2. Cross-link opportunities

Checked by searching the bodies of every `cic/texts/*.txt` for Taborites, Tábor, Táborští, Thaboritae, Žižka and Prokop, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`. All files below are already assigned to the Hussite entry.

- **Lawrence of Březová, *Historia Hussitica*** (Goll, 1893; `laurentius-de-brezova_historia-hussitica-lat-ces_goll1893.txt`). The main hostile, Prague-side chronicler of Tábor (about 270 mentions). Goll's note near file lines 1669–1674 says the text carries, after the Adamites' articles of 1421, further inserted articles "de Pikardis", "hereticorum Waldensium et decardorum" and "sacerdotum hereticorum et Pikardicorum". Tier: same time-place. Proposed row: context / provisional.
- **Piccolomini, *Historia Bohemica*** (1592 and 1524 printings). A papal observer on Tábor (28 and 26 mentions). OCR poor; second witness. Tier: same time-place. Proposed rows: context / provisional.
- **Palacký, *Urkundliche Beiträge*, Bände I and II.** Documents of the wars from Hussite, Taborite, Catholic and royal hands; the Taborite documents are mostly the editor's German summaries. About 9 and 31 mentions. Tier: same time-place. Proposed rows: context / provisional.
- **Lützow, *The Hussite Wars*** (about 310 mentions) and **Gillett, *Life and Times of John Huss*, II** (about 215). Secondary English narratives. Context only. Tier: same time-place.
- **Van Braght, *Martyrs' Mirror*.** A 1660 Anabaptist reading, with a "confession of the Taborites drawn up in 1431" whose source is not vendored (file line 47614). Tier: same time-different-region.
- **Goll, *Quellen*, I and II** (vendored this pass; staged on the Hussite entry). The Brethren's early writings, which look back on the Taborite field armies and the pacifism that followed them. Tier: same time-place.
- **Chelčický, *Síť víry*.** Three mentions of Tábor in the Czech; the revulsion at armed radicalism that the census names runs through the book, but the Taborites are rarely named. No row proposed.

## 3. Verified acquisition leads

Each lead was checked on the host: item record read, title page read in the OCR, text file fetched and sampled. The first three rows are vendored. Rights basis is public domain by date unless the row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Geschichtschreiber der husitischen Bewegung in Böhmen, Theil I (FRA Scriptores II). Vendored as `hofler_geschichtschreiber-husitischen-bewegung-v1-lat_1856.txt`. | Constantin von Höfler (editor) | none (Latin) | 1856 | https://archive.org/details/bub_gb_3fyRbn_1No4C | pd-us-by-date; Public Domain Mark 1.0 on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Geschichtschreiber der husitischen Bewegung in Böhmen, Theil II (FRA Scriptores VI), with the Chronicon Taboritarum. Vendored as `hofler_geschichtschreiber-husitischen-bewegung-v2-lat_1865.txt`. | Constantin von Höfler (editor); Nicholas of Pelhřimov and John of Lukavec | none (Latin) | 1865 | https://archive.org/details/bub_gb_AnOWDr0KmJYC | pd-us-by-date; Public Domain Mark 1.0 on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Prameny k synodám strany pražské a táborské (vznik Husitské konfesse) v létech 1441-1444. Vendored as `nejedly_prameny-k-synodam-strany-prazske-a-taborske-ces_1900.txt`. | Zdeněk Nejedlý (editor) | none (Czech with Latin) | 1900 | https://archive.org/details/pramenyksynodm00nejeuoft | pd-us-by-date; NOT_IN_COPYRIGHT on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Fontes rerum Bohemicarum / Prameny dějin českých, tom. V (Pulkava, Březová and the Hussite chronicles in Czech). Not opened: Březová is already on the shelf in Goll's 1893 edition (the Hussite world's file). | Historický klub, Prague | none (Latin and Czech) | 1873 | https://archive.org/details/fontesrerumbohe00goog | pd-us-by-date; NOT_IN_COPYRIGHT on the item | October 2026: item metadata read; title page read in the OCR (tom. V, Pulkava and Laurentius of Březová); 3.4 MB file listed, not opened further. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Fudge, *The Crusade against Heretics in Bohemia, 1418–1437* (Ashgate, 2002) | The census's English route to the Taborite manifestos and chiliast articles | In copyright. The Latin underneath it is partly on the shelf (Höfler II, Palacký, Březová). |
| Kaminsky, *A History of the Hussite Revolution* (California, 1967) | The standard account | In copyright and secondary. A renewal check cannot be done from this environment, so it is a lead, not a download. |
| Příbram, *Život kněží táborských* (the Lives of the Taborite priests) | The census names it; an intra-Hussite heresiology | Not located. Höfler II's 24 items do not include it and title searches on the host found nothing. |
| *Archiv český* and *Staří letopisové čeští* | Palacký's Czech editions of Hussite documents and annals | Not on the host: title searches for both found nothing. Palacký's *Documenta* and *Urkundliche Beiträge* are on the shelf. |
| Höfler, *Geschichtschreiber der husitischen Bewegung*, vol. III (1866; `geschichtschreib03hofl`, `bub_gb_DyYEvSyun98C`) | The third volume of the set | Fetched (756 KB): Höfler's German introduction and the index to the set. No source text of its own. Its index points to the Taborite articles (II, 479) and the Four Articles (II, 701) in the vendored vol. II. |
| Höfler vol. I and II, second scans (`geschichtschreib01hofl`, `geschichtschreib02hofl`, `bub_gb_Y2kyqXPJkdUC`, `bub_gb_D8Ethg7iFAUC`) | Other copies of the vendored volumes | Duplicates. The vendored scans have the higher word-form coverage (0.74 against 0.68 for vol. II) and carry the host's Public Domain Mark. The item record of `geschichtschreib02hofl` gives 1856 for vol. II; the title page reads 1865. |
| Nejedlý, other scans (`pramenyksynodam00nejegoog`, `pramenyksyuodms00nejegoog`, `pramenyksynodmst0000neje`) | Other copies | Duplicates of the vendored scan; the last carries no rights field. |
| Toman, *Husitské válečnictví za doby Žižkovy a Prokopovy* (1898; `husitske_valecnictvi-toman`) | The wagon-fort tactics | Czech scholarship, not a source. Listed, not fetched. |
| *Fontes rerum Bohemicarum* (Czech edition, 1871 and 1873; `fontesrerumbohem04emle`, `fontesrerumbohe00goog`) | Hussite chronicles in Czech | Title page of tom. V read (Pulkava and Březová); not opened further. Březová is on the shelf in Goll's edition. |
| Four Articles of Prague as the Praguers issued them; the Taborite twelve articles | The Hussite dossier's open leads | The Four Articles are quoted in Höfler II (Part II, printed p. 701 ff., in the Basel hearing) and in the legate's reply in Palacký. No separate edition was found. The Taborite five articles are in the Chronicon (§1). |

## 5. Open cross-world questions

- **Within another world (A5).** The census files Tábor inside the Hussite world. This pass staged the Chronicon and Nejedlý twice: here as tradition (assigned) and on the Hussite entry as tradition (provisional). The Hussite dossier says the Taborite strand had no voice of its own; it now has two vendored texts. Whether Tábor is a separate Representative or a strand of the Hussite one is for Step 0 of the Hussite world.
- **Tábor and Basel.** The Chronicon's Part II is the Bohemians' hearing at the Council of Basel. It is staged on the Latin Papal Church entry (V.14) as context. Which world reads the hearing is open.
- **The Adamites and the Picards.** Höfler I prints articles of the Picards, and Březová prints articles of the Adamites; whether they are one sect is a scholarly question (Lützow argues the Adamites had nothing to do with Hussitism). It belongs to the Inquisition-Record entry (V.13), and Tábor's part in destroying the Adamites is told by hostile chroniclers.
- **Žižka and Prokop.** The census names them among the voices. They appear only in outside accounts on the shelf. A Representative for them would rest on Březová, Piccolomini and Lützow.
- **Unity of the Brethren.** Goll and Chelčický look back on Tábor. The Unity is in the Hussite world, not this one.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says no creedal question: the argument was about practice and property. The five articles in the Chronicon confirm that: property, tithes, ceremonies and the Gospel as rule. The Chronicon is not read through for the eucharistic positions, which Nejedlý's synods of 1441–1444 take up in detail.

**Sourcing (B1).** The census says "Chronicled largely by opponents and moderate Hussites", and the shelf agrees: Březová, Piccolomini and the secondary narratives are hostile or outside. The two inside texts now vendored are the strongest the project can have: a Latin chronicle by the priests and a Czech record of their replies. Neither has a public-domain English translation.

**Ecology (B2).** Two inside texts, many hostile ones. The inside texts are mostly argument with Prague. Nothing vendored shows daily life at Tábor or the field army.

**Uniqueness (B3).** The entry is a wing of the Hussite world, not a separate church; it ended at Lipany and the surrender of 1452. Its separateness is the argument: the Hussite world is the one that carried on.

**Audiences (B4).** Nothing institutional survives. The town is still there and the wagon-fort tradition is studied.

**Scale (B5).** About 4.7 million characters in three vendored files (two volumes of Höfler and Nejedlý). The first-hand material is the Chronicon (a few hundred thousand characters inside Höfler II) and Nejedlý.

**Recommendation: part of another world.** The Taborite voice exists in Latin and Czech and is vendored, which the Hussite dossier lacked. It is a strand of the Hussite world and the census files it so (A5); the Chronicon and Nejedlý are best read as that world's Taborite sources, with Tábor's own Representative an open question for the Hussite build. This is a recommendation for Mark to weigh, not a decision.
