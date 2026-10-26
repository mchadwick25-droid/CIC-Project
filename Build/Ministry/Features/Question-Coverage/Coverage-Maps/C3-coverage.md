# C3 coverage map: hell, heaven, judgment, and after death

Read-only pass, 25 October 2026; nothing in the repo was edited. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; file paths, line numbers and verification results are in `search/C3/C3-coverage.json`.

## The sub-questions

The 30 C3 questions plus R-09, R-20 and R-22 group into eight:

| id | sub-question | canon / question ids |
|---|---|---|
| S1 | Was hell and a last judgment real to you? How did you picture, preach and use it? | C3-05, 21, 25, 29, 30; R-09 |
| S2 | Was hell forever, or did it end? | C3-02, 03, 06, 17 |
| S3 | Did everyone get restored in the end, even the devil? (Origen, Nyssa) | C3-07, 22, 23 |
| S4 | Were the wicked destroyed rather than tormented? | C3-08 |
| S5 | What happens right after death: waiting place, Sheol/Hades, purgatory, prayer for the dead; ghosts; reincarnation | C3-04, 09, 10, 11, 24, 27; R-22 |
| S6 | What is heaven like; resurrection of the body; seeing loved ones again; losing it after baptism | C3-12, 19, 28 |
| S7 | Who is lost: outsiders, Jews and pagans, a loved one who did not believe, unbaptised infants, suicide | C3-01, 13, 14, 15, 16, 26; R-20 |
| S8 | The end of the world: rapture, Antichrist, millennium, "in your lifetime?" | C3-18, 20 |

Only S7's first question (F6-T) has a canon cell. S7's infant and suicide questions and S5 are Facilitator-adjacent: the redirect is template-anchored, but the Representative still needs honest ground for the in-character part.

## Layer table

R = RENDERED (a record speaks to it), L = LOADED (vendored and mapped, read in context, no record), I = IDENTIFIED (registered, unvendored), O = OTHER, "-" = nothing found.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R | R* | R | L | L | R | R* | R |
| cappadocian | L | L | L | L | L | R | L | L |
| desert | R | L | - | - | L | R | R | R |
| don | R | L | - | - | - | L | R* | R |
| gallic | R | L | - | - | R | R | R* | R |
| hal | R | L | R | - | L | R* | R | R |
| ijc | R* | L | - | - | L | L | R* | L |
| lpc | L | L | L | L | L | L | L | L |
| pahc | R* | L | - | L | L | R | R | R* |
| rzg | R* | L | L | L | L | L | L | L |
| syr | R | L | - | - | R | R | R | R |
| witt | R | R | R | R* | R | R | R | R |

`*` = partial: a record exists but answers only part of the sub-question or only as a guard (details per world). Worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) have LOADED/OTHER rows in the JSON only.

Verification: 25 quote records are cited as RENDERED above; all 25 MATCH their vendored file verbatim (file and line in the JSON). Four matched only after an editorial artifact was allowed for: a section number inside the text (Athanasius, Didache), a line-end hyphen (Salvian), an italic-tag boundary (Aphrahat), and soft hyphens in the ANF transcription (Origen, De Principiis IV.1.16, anf04 line 33725). None is a wording change.

## World by world

**Alexandria (alx).** Can say today, with verified words: punishment is a physician's fire (Origen, Philocalia XXVII, line 436); the restoration of all is Origen's open question, not settled doctrine (`alx.term.apokatastasis`, `alx.contested.origen-positions`); the body rises transformed (`alx.term.anastasis`, Athanasius quote); the millennium was argued out at Arsinoe. Would go thin or wrong: whether hell *ends* (the voice can only defer; Origen's De Principiis II.10-11 is vendored in anf04 and unquoted); what happens right after death (nothing; Origen's "school of souls", De Princ. II.11.6, and Clement's descent-preaching, Strom. VI.6, are vendored); the dead baby and suicide (nothing in records or texts for this world). Must add: a second quote so the voice is not Origen-only (Clement, Strom. VII on corrective punishment, anf02); an honest_limit on annihilation (the vendored hits are Arnobius and Methodius, not Alexandrians); a quote or honest_limit on the interim state. Files: `records/alx/quote/`, `records/alx/honest_limit/`.

**Cappadocians (cappadocian).** The clearest live defect in the cluster, and the prior map was right about it. No record mentions hell or judgment at all; `Build/worlds/cappadocian/Open_Gaps_Tracking.md` line 667 already says the witnesses cannot answer "hell for outsiders", and item 3 (line 787) logs the probe that said Nyssa "never made the claim plain". Meanwhile the library holds, confirmed in context: Catechetical Oration 26 on the restoration of all (`npnf205_gregory-nyssa-dogmatic-treatises.txt` 44408-44422); the purgatorial-fire image in On the Soul and Resurrection (39606-39618); On Infants' Early Deaths (32849); Nazianzen's Oration 40.23 on infants who die unbaptised, "neither glorified nor punished" (`npnf207` 38478-38496); and Basil's Rules on eternal punishment (`basil_ascetic-works-longer-shorter-rules_clarke1925.txt` 7722, 11714), which turn out to be vendored and mapped. The world argued with itself (Basil forever, Nyssa purgation ends), so the right build is a contested_claim, not one quote. Must add: quote records for Cat. Or. 26 and Or. 40.23 (Documented, renderings on Opus), a contested_claim on how far Basil and Nazianzen shared Nyssa's hope, an honest_limit on annihilation and on end-times, and a lexicon term for purgation (*katharsis*). Caution for the thread: npnf207 also holds Cyril of Jerusalem; the prayers-for-the-dead and Antichrist hits there (lines 2866, 1208) are his, not Cappadocian.

**Desert (desert).** Honest and already well guarded: judgment certain and no system (`desert.dw.judgment-and-resurrection`), "hell" absent from the Vita (`desert.limit.outsiders-condemned`), the body back whole (Antony's deathbed). Would go thin: forever/ends, restoration, annihilation (nothing, honestly); the moment of death (the Vita's vision of souls rising past the accuser, 65-66, and the Sayings' Sheol lines in `anan-isho_paradise-v2-sayings_budge1907.txt` 1144 are vendored and unquoted). Must add: absence records for S2-S4 in the shape of the existing limit, after reading the Sayings and not only the Vita; a quote or story for Vita 65-66. The Macarius-and-the-skull saying was not found in Budge vol. 2 by the terms used; check before citing it.

**Donatists (don).** `don.dw.the-line-we-actually-drew` is a model of discipline: it refuses to turn sacramental nullity into damnation. "The end of the world we cannot speak to at all" and "whether babies were washed we cannot tell" are honest limits already inside witnesses. The hazard is R-20: Augustine's charge that Circumcellions threw themselves over precipices is vendored (`npnf104` 16889) and unframed; a participant asking about suicide could pull it unguarded. Everything vendored on Donatist hell-talk is the other side (Optatus, now confirmed vendored; Augustine). Must add: a contested_claim on voluntary death among the Circumcellions; an honest_limit that the movement's own afterlife voice (the martyr acts, `don.source.tilley-donatist-martyr-stories`, unvendored) is not in the library.

**Gallic monastics (gallic).** Strong on judgment and the end (three Salvian/Vincent quotes and two Antichrist quotes, all verified); weak on hell itself, which sits only in `gallic.gravity.judgment-imminent-present` and two terms, while Cassian's "fear of hell" (`npnf211` 35548) and Salvian's "Gehenna will be in flames" (`salvian_...sanford1930.txt` 2677) are unquoted. The best unrendered story in the cluster is Vita Martini 7 (`npnf211` 1014-1016): the dead catechumen brought "before the tribunal of the Judge, and being assigned to gloomy regions and vulgar crowds", then sent back. Correction to the prior map: `npnf211` line 5547 is Sulpitius's letter, not Cassian, and "fire of purgatory" there is the editor Clericus's footnote. Risk: `gallic.term.predestination` ("God wills all to be saved; to think otherwise is blasphemy") can be misread as universalism and its not_for does not guard that. Must add: quote records for Cassian XI.6, Salvian 2677 and Vita Martini 7; a not_for on the predestination term; infants belong to Prosper (registered unvendored; De vocatione omnium gentium is OTHER).

**Jerome's circle (hal).** Good witness (`hal.dw.hell`: real punishment, restoration renounced, "no census of the lost"), thin on verbatim: the only verified quote is the Ciceronian dream. The Apology against Rufinus renunciation ("the devil will be saved; a thing which no man ... could say", `npnf203` 53776), Letter 124's list of Origen's errors (`npnf206` 40528) and Letter 39's "mourn only for him whom Gehenna receives" (`npnf206` 7903) are all confirmed and unquoted. Must add those three as quote records; an honest_limit on duration, which the witness never states.

**Imperial-juridical (ijc).** Only the creed's "judge both the quick and the dead" (verified) and the Altar of Victory story, which is about toleration, not fate. Leo's Sermon IX (`npnf212` 13585-13587) states endless punishment and turns it at once to mercy; Ambrose on his dead brother (`npnf210`) is unquoted. Must add: a Leo quote, and a decision whether this world answers afterlife questions at all.

**Latin pastoral (lpc, building).** 330 records and not one on hell, judgment, purgatory or the dead (direct grep: zero). The library under it is the richest in the fleet, all confirmed in context: Cyprian's reunion passage, "a great number of our dear ones is awaiting us, and a dense crowd of parents, brothers, children" (`anf05` 47279-47280); Cyprian to Fidus on baptising infants before the eighth day (`anf05` 35892); Augustine's "tender-hearted Christians" who deny eternal punishment (`npnf102` 43953); the purgatorial fire as an open question (Enchiridion 69, `npnf103` 22300-22312); offerings "propitiatory for the not very bad" (Enchiridion 110, 23570-23582); Monica's "remember me at the Lord's altar" (`npnf101` 14194); City of God I.17 on suicide (`npnf102` 2426). This is the world most likely to be asked C3-13, C3-15 and R-20, and today it has nothing. Belongs to the LPC thread; the build needs quote records for each of the above plus a contested_claim on infants (Cyprian's practice against Augustine's "mildest condemnation", `npnf105` 2558).

**Post-apostolic house church (pahc).** Not checked by the prior map; it holds surprises. Rendered: the Two Ways (verified, but its not_for forbids using it as an afterlife threat), Polycrates' "great luminaries ... shall rise again" (verified, filed under F3-I so retrieval on an afterlife question is not guaranteed), Justin's reasonable livers (verified) against the Two Ways. Unrendered and confirmed: Justin, Dialogue 5, "the soul is not in its own nature immortal" (`anf01` 17704), the fleet's only real ground for C3-08; Hermas, Sim. 9.16, the apostles preaching and baptising the dead (`anf02` 4660-4672); Justin Dial. 130's "unquenchable fire, remaining immortal" (`anf01` 24766); the Apocalypse of Peter's lake of fire (`anf09` 12618). Must add: quote records for Justin Dial. 5 and Hermas Sim. 9.16; a story from Didache 16 or Justin Dial. 80 for the millennium.

**Zurich and Geneva (rzg).** Thin for a world that will be asked this constantly. The one F6-T record is a guard (`rzg.witness.a-narrow-true-church`, not_for: no claim on damnation). The prior map's "term predestination" was not found among the records. Vendored and unquoted: Institutes III.5 on purgatory and prayer for the dead (vol. 2 from 11000); Zwingli's "Of Purgatory" (vol. 3, 40 hits) and the Sixty-Seven Articles' "purgatory ... man's invention" (`zwingli_selected-works_jackson1901.txt` 2530); and, for the dead baby, Calvin's own heading "Error of those who adjudge all who die unbaptized to eternal destruction" (vol. 3, 15757). The Zwingli "unbaptized infants are not under condemnation" hit (vol. 3, 1523) is the editor's paraphrase, not Zwingli. Must add: quote records for Institutes III.5 and IV.16, Zwingli on purgatory, Geneva Catechism on the descent; the Exposition of the Faith (Hercules and Socrates in heaven) is in the unvendored Latin Works vol. 2.

**Syriac (syr).** Can quote: Death trembling (Nisibene XXXV, verified), Sheol "receives the departed without distinction" (verified), the poison-in-the-food image (verified), with the emic hedge "we drew far less of the modern map of who exactly burns". Ephrem's Testament curses ("may he be cast into Gehenna of fire", `npnf213` 11642-11644) are a will's curse on a rich burial, not doctrine; they would change tone, not teaching, and need a careful not_for if quoted. Aphrahat's Demonstration VIII on the sleep of the soul (`npnf213` 26376 ff) is the distinctive Syriac interim-state teaching and is unrendered. C3-26 ("all Jews damned?") lands on the anti-Jewish polemic records, which hold the polemic without a verdict; check their not_for. Must add: Dem. VIII quote; honest_limit for restoration and annihilation (nothing in Ephrem or Aphrahat as vendored).

**Wittenberg (witt).** Fullest in the fleet; the only world with every cell rendered. AC XVII ("tormented without end"; the Anabaptists' end-of-punishments condemned) and the Small Catechism verified. Two gaps: the Apology's "the ancients speak of prayer for the dead, which we do not prohibit" (`melanchthon_apology-augsburg-confession_bente-dau1921.txt` 9481) is the nuance C3-10 needs and is unquoted; and the confession's hard words on the unbaptised ("eternal death upon those not born again through Baptism") are rendered without Luther's pastoral softening (the 1542 miscarriage consolation and the 1522 Rechenberg letter are OTHER; the 1519 Sermon on Preparing to Die is not in the vendored Holman vol. 1). Table Talk is vendored and unread for Luther on suicides. Must add: an Apology XXIV quote; a decision on the Rechenberg letter.

## Other sources (outside the repo; from working knowledge, not fetched)

The ones that would change an answer: Zwingli, *Exposition of the Faith* (Latin Works vol. 2, Hinke 1922, PD-US; vol. 2 is the one volume not vendored); Calvin, *Psychopannychia* (Tracts vol. 3, Beveridge 1851); Luther's 1522 letter to Hans von Rechenberg (Smith and Jacobs 1918) and the 1542 *Trost den Weibern* (WA 53, German); Prosper, *De vocatione omnium gentium* (PL 51); Tyconius, *Liber Regularum* (Burkitt 1894); M.R. James, *Apocryphal New Testament* (1924) for the full Apocalypse of Peter; Terry's *Sibylline Oracles* (1899) II.330-338; Nyssa, *De mortuis* (PG 46, Greek); Jerome on Jonah and Ephesians (PL 25-26, Latin); Severus of Antioch's hymns on the departed (Brooks, PO 6-7). Editions, hosts and licences for all of these, per world, are in `search/C3/other.json`.

## Not checked

- The first tool run (`search/C3/bad-run1/`) is invalid: its alternation groups were split on commas. Only the second run is used.
- `canon/sealed_probes/` was not read; the Cappadocian probe finding is cited from `Open_Gaps_Tracking.md`.
- The tool scans whole mapped files, so shared volumes yield hits for the wrong author (Cyril in npnf207, Gregory the Great in npnf212, Arnobius in anf06); flagged per cell, but not every LOADED line was traced to its work.
- Non-English vendored texts were counted, not read. Vita Antonii 65-66, Tertullian De anima 55-58, Tatian Or. 13, Augustine Sermons 172-173 and Table Talk on suicides are cited by section, not line.
- The seven record-less worlds were grepped, not read; `fix` was excluded. Readability of spoken fields was not graded. Which `lpc` draft records are in the compiled package was not checked.
