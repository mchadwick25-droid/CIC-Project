# Doc_02 Source Ecology (Donatism) — Revision Round 1: Independent Adversarial Review

**File under review:** `Build/worlds/don/Doc_02_Source_Ecology.md` (revision of 2026-09-02, commit `a1f84b56`, "Revise Doc_02 to integrate the completed G1–G7 acquisition round")
**Baseline compared against:** `bd838c40` (the "Approved to proceed" state after five review rounds)
**Reviewer stance:** cold, adversarial, no access to the drafting conversation. Every claim treated as unverified until opened against the vendored file itself.
**Date:** 2026-09-02

---

## OVERALL VERDICT: **SUBSTANTIAL REVISION REQUIRED**

This is not a cosmetic-fix verdict and it is not close to one. The revision is well-shaped — the sermon integration has the right *form* (a full five-item Formation Narrative evaluation in §4, a matching §6 Source Asymmetries bullet, a Confidence Map entry, an Open Item), which is what Mark asked for. But its *content* fails independent verification at the level of the central new claim, and the failure has a single dominant cause:

> **The revision analysed the newly-vendored anonymous sermon almost entirely through Jean Mabillon's 17th-century apparatus, while holding — vendored in the same acquisition round, cited four separate times in the same revision, and named in §3 as Confidence A — a 1920 scholarly monograph that devotes a chapter section to that exact text, calls it by its standard scholarly name, dates it twenty-three years earlier, identifies its probable author, and resolves the title problem the document says it "reports rather than resolves."**

Monceaux, Tome V, treats this sermon at length as the ***Passio Donati*** — one of the three principal Donatist martyr-texts, alongside the *Passio Marculi* and the *Passio Maximiani et Isaac*, which he groups as a deliberate trio. The document presents it instead as an obscure incidental find whose only witnesses are the Migne file and Mabillon. Nearly every High-severity finding below descends from that one un-run check.

A second, independent cluster of failures sits in §5's CIL work, where the inscription actually adduced is misprovenanced, the better inscription is declared absent from a volume that contains it, and a phrase is presented in quotation marks that appears in neither editorial note.

The `don_Decision_Log.md` (line 154) tracks a **recurring failure mode across nine prior review rounds**: "a fabricated or misattributed citation, an uncredited reuse of a neighboring document's language, or a reviewer-supplied citation or fix wording adopted into the document's own voice without independent verification," with the note that Rounds 4–5 ran clean on it. **It has recurred in this revision, in at least four distinct instances** (H7, H8, M3, and the fabricated "as distinct from" quotation). That pattern-level finding should be recorded in the Decision Log regardless of what happens to the individual items.

Findings that were checked and **held** are listed at the end (§"What Verified Clean"), which is substantial — the Monceaux/Tyconius material in §1–§3 is, with two small exceptions, accurately reported.

---

# HIGH SEVERITY

## H1. §4 and §6 — The "newly-discovered" sermon is the well-known *Passio Donati*, and §6's claim that nothing about it is checkable outside the Migne file is false

**Location:** §4, sermon bullet, opening and *Author Gravity risk* clause; §6, first bullet, final sentence.

**Claim made:** §4 introduces the text as "An anonymous Donatist-authored sermon on an earlier, less-attested persecution (found incidentally while acquiring the Passiones above, not itself requested…)". §6 states: "nothing about this sermon's author, precise date, or full content is checkable against any source outside the vendored text and Mabillon's own apparatus."

**What I found on checking:** `/home/user/CIC-Project/cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt` — vendored 2026-09-01 as Manifest G6, Registry row 40, cited by this same revision in §1, §2, §3, and §4 — contains a dedicated treatment of this text under the standard scholarly title ***Passio Donati*** / *Sermo de Passione Donati*. It appears in the chapter argument-summary at line 3018–3032 and is analysed continuously at lines 3038–3266. Monceaux groups it explicitly with the two Passiones the document *did* request:

> "Cette littérature est représentée encore par trois opuscules très curieux, conservés entièrement, animés d'un même esprit, étroitement apparentés, et, tous les trois, de destination liturgique… Un sermon : la *Passio Donati*. Un récit : la *Passio Marculi*. Une lettre : la *Passio Maximiani et Isaac*." (lines 3044–3049)

He further calls it the source of "les seuls renseignements un peu précis que nous possédions sur la persécution de 317, sur les premiers martyrs donatistes" (lines 3262–3265). The text is cited by name at least fifteen further times across the volume (lines 817, 1634, 2289, 3086, 4956, 4988, 5801, 7014, 7070, 7273, 7318 …).

**Why it matters:** Three distinct problems. (1) §6's "nothing… is checkable against any source outside the vendored text and Mabillon's own apparatus" is simply false, and it is false about a file this document itself vendored, cites, and rates Confidence A. (2) The framing of the text as an incidental, uncorroborated curiosity systematically understates it — this is a named, standard, much-discussed Donatist document, not an orphan. (3) The document's own §3 licenses Monceaux "as a second, independent route to the Macarian-repression Passiones" — the obvious next step (does Monceaux also treat the third text in the same file?) was never taken. The whole of H2, H3, H4 and M3 below follow from that single omission.

---

## H2. §4, §6, §8 — The dating adopted (Mabillon, *c.* 340) is superseded by a vendored source that dates the events to 12 March 317 and the sermon to *c.* 320; the document flags the dating "Contested" without naming the competing authority it holds

**Location:** §4, sermon bullet, *Authorship and date* and *Proximity*; §6 first bullet; §8 "Contested" band; §9 item 12.

**Claim made:** "his own reasoned dating, cross-referencing the imperial agents named in the text (Leontius and Ursacius) against Optatus's own chronology, places the events described at *circa* 340, 'certainly before Macarius was sent to Africa around 348' — several years earlier than the Macarian-repression Passiones above." §8 lists this as Contested: "a reasoned inference from internal evidence, not a date stated in the text itself, and not independently checked against his own cited cross-references this session."

**What I found on checking:**

Mabillon's Latin is quoted accurately as far as it goes (Migne file lines 183–186: "Videntur itaque, quæ hic referuntur contigisse circa annum [3]40, aut paulo post, certe antequam Macarius mitteretur in Africam circa annum 348"). The document silently drops Mabillon's own hedge "*aut paulo post*."

But Monceaux, lines 3072–3086, rejects that dating on argued grounds:

> "D'après le texte de la *Passio*, la persécution fut déchaînée par un édit d'union. Il y a eu, dans l'histoire du Donatisme, quatre édits de ce genre : ceux de 316, de 347, de 405, et de 412… L'orateur dit que les tombeaux et les épitaphes de ses martyrs conserveront à jamais le souvenir de la « persécution de Cæcilianus ». Comme Cæcilianus de Carthage est mort peu après 325, il s'agit de la persécution qui sévit de 317 à 321… **C'est donc le 12 mars 317 qu'ont succombé les héros de la *Passio Donati*.**"

And on the sermon's own composition date (lines 3133–3137):

> "De tout cela il résulte que le sermon *De Passione Donati* est presque contemporain des martyrs du 12 mars 317. Il doit être antérieur à l'édit de tolérance de 321. **On ne se trompera guère en le plaçant vers 320**, à l'anniversaire du 12 mars."

Monceaux's dating rests on the same "persecutio Cæcilianensis" datum Mabillon used — but Mabillon reasoned that Caecilian died by the Council of Sardica (347) so the events must precede *that*, whereas Monceaux uses the tighter fact that Caecilian died shortly after 325 and pins the persecution to the 316 edict of union.

**Why it matters — three consequences, all material:**

1. **§8's "Contested" entry is honest in form but empty in substance.** It says the dating was "not independently checked against his own cited cross-references this session." The actual problem is not that Mabillon's cross-references were unchecked; it is that a directly competing, later, argued dating sits in a vendored file the document cites four times. A Confidence Map that names a claim "Contested" without naming the source of the contest it already holds is not doing the work.

2. **The ecology changes completely on Monceaux's date.** A Donatist sermon of *c.* 320 would be the **earliest Donatist-authored text in this world's entire vendored corpus** — roughly contemporary with the *Gesta apud Zenophilum* (320) that §1 lists in Optatus's appendix, and forty-five years earlier than Optatus himself. That is a first-order source-ecology fact for a document whose §1 opening paragraph is about the shape of the surviving record. It is not mentioned.

3. **§4's "Formation ecology revealed" conclusion is built on the weaker of the two datings and is arguably inverted by the stronger one.** The document concludes that the annual-commemoration practice "predates the Macarian repression itself, resting the 'Church of the Martyrs' self-understanding on a deeper root than the 347–348 material alone would suggest." Monceaux says the opposite about the *direction* of the evidence (lines 3097–3099, 3131–3133): "Notons aussi que **c'était alors une nouveauté**, de fêter l'anniversaire des martyrs de la secte et de leur consacrer un sermon… Cet exorde ne se comprend que dans les premières années du schisme, **en un temps où l'hagiographie donatiste en était encore à ses débuts**." On Monceaux's reading the sermon documents the *invention* of the practice, not a deeper root beneath it. That is a better and more interesting formation finding than the one the document states — and it is the opposite of it.

---

## H3. §4 — "*Authorship and date:* anonymous" suppresses the single most consequential thing a vendored source says about this text: that its author was probably Donatus the Great

**Location:** §4, sermon bullet, *Authorship and date*.

**Claim made:** "*Authorship and date:* anonymous."

**What I found on checking:** Monceaux, lines 3139–3164, argues from the Donatist rule that only a bishop preached, and only in his own diocese, that the sermon must be by the Donatist bishop of Carthage *c.* 320:

> "l'orateur est sûrement un évêque, parlant à ses fidèles. Seul, en ces temps-là, l'évêque prêchait devant le peuple… Par conséquent, le sermon *De Passione Donati* doit avoir pour auteur l'évêque donatiste qui dirigeait vers 320 la communauté dissidente de Carthage. **C'est Donat le Grand, le primat du parti, qui remplit ces fonctions de 313 à 347. C'est donc à lui qu'il faudrait attribuer notre sermon.**"

Monceaux then hesitates on literary grounds ("nous n'y reconnaissons ni le ton, ni la manière, ni l'éloquence hautaine de Donat le Grand"), noting the Donatus of 313 differed from the later "despot" Optatus paints — so he does not settle it. His chapter argument-summary carries the point as a standing heading: "**Il est peut-être de Donat le Grand**" (line 3019).

He also finds the preacher an **eyewitness**: "la vivacité des impressions de l'orateur, **témoin oculaire**, et la violence de ses attaques contre Cæcilianus, encore vivant" (lines 3094–3096).

**Why it matters:** This is the highest-value single datum available anywhere in this revision. A sermon *possibly by the movement's eponymous founder*, certainly by a Carthage bishop, certainly by an eyewitness, is a wholly different evidentiary object from "an anonymous sermon." It bears directly on §2 (Author Gravity — a Donatist-side entry with a named candidate author would be the first), on §6 (Missing Voices — the strongest possible correction to the concentration), and on Doc_09. Reporting "anonymous" with no qualification, when a vendored authority argues a specific attribution and the document is *citing that authority elsewhere in the same paragraph cluster*, is an understatement severe enough to mislead every downstream document.

To be clear about the correct treatment: the document should **not** assert Donatus's authorship. It should report that Monceaux argues for it on institutional grounds and hesitates on literary ones, and mark it Contested. Silence is the one option that is not defensible.

---

## H4. §4 — "a death within that basilica" materially understates a massacre attested in three independent places in the vendored material

**Location:** §4, sermon bullet, *Genre conventions*.

**Claim made:** "its content describes a 'military action' against Donatists at Carthage in which a church building ('*basilica*') was seized, and **a death within that basilica**, rather than a single confessor's interrogation and execution."

**What I found on checking — three sources, all in files this revision cites:**

1. **Mabillon's own apparatus** (Migne file, lines 214–216), in the very argument the document paraphrases elsewhere: the title cannot refer to Donatus of Bagai, who Augustine says was thrown into a well, "quod nulli e martyribus cujus fit hic mentio, convenire potest: **cum omnes in basilica a militibus cæsi fuerint**" — "since **all** were slain in the basilica by the soldiers." Plural, and it is the load-bearing premise of the very argument the document reports.

2. **The sermon's own §VIII** (Migne file, lines 531–534): "cum **omnis ætas et sexus** clausis admodum oculis cæsa in media basilica necaretur. Basilica, inquam, intra cujus parietes et occisa et sepulta sunt **corpora numerosa**" — every age and sex slain in the middle of the basilica; numerous bodies both killed and buried within its walls.

3. **Monceaux**, lines 3179–3200: "Batailles dans des basiliques. — **Nombreuses victimes donatistes**"; "Un évêque du parti, qui se trouvait là, l'évêque de Sicilibba, fut grièvement blessé. **Beaucoup de Donatistes furent assommés à coups de bâtons**; les victimes furent ensevelies dans le sanctuaire. Dans la même basilique, ou dans une troisième, **l'évêque d'Advocata fut tué avec de nombreux fidèles**… La relation paraît donc mentionner **deux ou trois groupes distincts de martyrs**."

**Why it matters:** The document is a *source-ecology* document; its job is to characterise what a source contains. It characterises a multi-basilica massacre of men, women and children, in which one bishop was killed and another gravely wounded, as "a death within that basilica." The understatement is not conservative caution — it is inaccurate, in a section whose stated purpose is to assess "Formation ecology revealed," and it drains the text of exactly the martyr-cult content §4's opening paragraph says is this world's distinctive strength.

---

## H5. §4 — The *Passio Isaac et Maximiani* is called "anonymous" with "an appended epistle of the martyr Macrobius." The vendored file's own heading names Macrobius as its author, and the work *is* the epistle

**Location:** §4, *Passio Isaac et Maximiani* bullet.

**Claim made:** "**Now vendored** (same file as the *Passio Marculi* above, Registry row 20; Manifest G4), with its own opening 'Incipit Passio SS. Martyrum Isaac et Maximiani' and **an appended epistle of the martyr Macrobius** to the church at Carthage. *Authorship and date:* **anonymous**, from the same Macarian-repression context (347–348)."

**What I found on checking** (`monumenta-vetera-donatistarum_migne-pl8.txt`):

- Line 1367–1370, the work's own printed rubric: "**PASSIO MAXIMIANI ET ISAAC DONATISTARUM AUCTORE MACROBIO**."
- Line 1495–1496, Mabillon's note: "Incipit passio. **Hujus auctor Macrobius Donatista et suorum in urbe Roma occultus Episcopus**, de quo Gennadius in lib. de Scriptoribus Eccl. c. 5." — "the author of this is Macrobius the Donatist, and the **hidden bishop of his own people in the city of Rome**."
- Line 1508–1510: "Scripserat autem Macrobius hanc epistolam ad plebem Carthaginis, ut ex fine hujus instrumenti constat."
- Line 1929–1930, the work's explicit: "**Explicit epistola beatissimi martyris Macrobi ad plebem Karthaginis de passione martyrum Isaac et Maximiani.**"
- Monceaux, line 3048–3049 and 3028: "Une lettre : la *Passio Maximiani et Isaac*"; "Lettre de l'évêque Macrobius à la communauté donatiste de Carthage."

**Why it matters:** Three separate failures in one bullet. (1) The text is not anonymous; it has a named Donatist author. (2) The epistle is not "appended" to the Passio — per the file's own explicit and per Monceaux, the Passio *is* the epistle. (Mabillon separately prints a *Fragmentum epistolæ Macrobii* at line 2196, a second recension; conflating the two would explain but not excuse the error.) (3) The detail that Macrobius was the Donatists' clandestine bishop **in Rome** is a significant, checkable geographic fact about the movement's reach that this world's build does not have anywhere else, and it sits three lines from material the document did quote.

This bullet was rewritten in this revision (the pre-revision version read "not yet independently vendored or verified this session"), so the error was introduced when the file was actually opened — which is worse than inheriting it.

---

## H6. §6 — "the first vendored text in this world's corpus… that speaks as a Donatist" is contradicted by §4 of the same document

**Location:** §6, first bullet, second sentence.

**Claim made:** "This sermon is the **first vendored text in this world's corpus**, alongside Tyconius's own *Liber Regularum* (§1, §2 above), that **speaks as a Donatist rather than being spoken about or through by one** — a distinction this document has drawn sharply throughout."

**What I found on checking:** §4 of this same revision reports as newly vendored, in the same file:
- the *Passio Marculi*, whose rubric the document itself quotes as "PASSIO MARCULI **SACERDOTIS DONATISTAE**";
- the *Passio Isaac et Maximiani*, authored by **Macrobius**, a named Donatist bishop (H5 above), writing in the first person to the Donatist congregation at Carthage ("Opportunus me, fratres, et lætus scribendi ad vos… ardor accendit", line 1383);
- and the separate *Fragmentum epistolæ Macrobii Donatistæ* at line 2196.

The vendored file's own header states this outright: "Creator(s): Anonymous Donatist author (item 1); **anonymous Donatist hagiographer(s) (items 2–3)**."

**Why it matters:** This is a straight internal contradiction between §4 and §6 of a single document, introduced in a single revision, on the point the document names as its central evidentiary problem. It also inflates the novelty of the sermon at the direct expense of the two acquisitions that were actually requested (G4). The correct statement is that the G4 acquisition delivered **four** non-hostile-mediated Donatist voices at once (sermon, *Passio Marculi*, Macrobius's letter, Macrobius fragment) alongside G1's Tyconius — which is a much stronger finding than the one the document makes, and would have justified a genuinely upgraded §6 assessment of the Author Gravity concentration.

---

## H7. §4 and Registry row 19 — The *Passio Marculi* heading is quoted with a truncation that inverts its sense, and Migne's hostile editorial rubric is presented as "the text itself"

**Location:** §4, *Passio Marculi* bullet, first sentence (identical wording is carried in `Source_Registry.md` row 19).

**Claim made:** "**Now vendored** … **headed in the text itself** 'PASSIO MARCULI SACERDOTIS DONATISTAE… QUI SUB MACARIO INTERFECTUS A DONATISTIS,' **dated by its own heading** to 'ANNO DOMINI 348.'" And later: "on the dating given both in the standard field literature (Frend, row 23) and **confirmed directly by the text's own heading**."

**What I found on checking** (`monumenta-vetera-donatistarum_migne-pl8.txt`, lines 664–673):

```
ANNO DOMINI 348.
PASSIO MARCULI SACERDOTIS DONATISTAE,
QUI SUB MACARIO INTERFECTUS A DONATISTIS PRO MARTYRE HABEBATUR.
(Ex Analectorum Mabillonii tom. IV, p. 105, Collata ad codicem ms. Corbeiensem…)
```

Three distinct problems:

1. **The truncation inverts the grammar.** As the document quotes it — "QUI SUB MACARIO INTERFECTUS A DONATISTIS" — the fragment reads "who, under Macarius, was killed **by the Donatists**," which is nonsense and the reverse of the actual sense. The words cut by the ellipsis-free truncation, "PRO MARTYRE HABEBATUR," are precisely what "A DONATISTIS" governs: "who, killed under Macarius, **was held to be a martyr by the Donatists**." A quotation that cannot be parsed as quoted is a quotation-integrity failure regardless of intent.

2. **It is not "the text itself."** This is Migne's/Mabillon's descriptive catalogue rubric, and it is written from the *Catholic* side — "was *held* to be a martyr by the Donatists" is a distancing formula. The Passio's own heading, sixty lines further down at line 873, is "**INCIPIT PASSIO BENEDICTI MARTYRIS MARCULI. 8 (al. die 5) kal. decembris.**" The vendored file's own header (line 13) likewise calls it "Passio Benedicti Martyris Marculi." In a document whose central discipline is separating a source's self-description from hostile mediation, quoting an editor's hostile rubric as the text's self-description is a category error, not a slip.

3. **"ANNO DOMINI 348" is Migne's dated section marker, not the text's own date.** The vendored file's own EXCERPT NOTE (lines 52–59) states this explicitly: the excerpt boundaries were drawn at "the volume's own dated section markers" — "ANNO DOMINI 340" for the sermon and the equivalent for what follows. The document *itself* applies the correct discipline to the sermon ("This dating is Mabillon's own inference from internal evidence, **not a stated date in the text itself**") and then abandons it one bullet earlier for the Passio Marculi ("dated by its own heading," "confirmed directly by the text's own heading"). The Passio's own dateline gives only a day — "8 (al. die 5) kal. decembris" — with no year. Registry row 19 is at Confidence A partly on the strength of this.

Monceaux devotes a section to "La *Passio Marculi*. — **Date de l'ouvrage**" (line 3024) which was not consulted.

---

## H8. §5 — The CIL work contains a provenance error, a self-contradiction, a phrase in quotation marks that appears in neither note, and three missed inscriptions

**Location:** §5, first bullet (Epigraphic evidence). Identical errors are carried in `Source_Registry.md` row 27, which is at Confidence A.

**Claim made:** "**Resolved to a specific catalogued inscription** (Confidence A, Registry row 27; the *Corpus Inscriptionum Latinarum* VIII **Numidia supplement**, Registry row 48, Manifest G7): inscription *CIL* VIII 20482 ('DEO LAVDES SVPER AQVAS…', **a fragment found near Constantine**) carries the editors' own note identifying 'Deo laudes' as the Donatists' own sign, '**as distinct from**' the Catholic 'Deo gratias'; **a second passage in the same volume, independent of the first**, makes the identification in fuller form, naming Bagai and Thamugadi as the Donatists' primary seats… though the specific inscription's own archaeological context (find-site, date, **physical description beyond 'a fragment'**) has not been further researched this session, and **a cross-referenced second inscription (no. 17732) that the editors cite for fuller discussion was not found in this particular volume**."

**What I found on checking** (`cil8-supplementum-numidiae_cagnat-schmidt1894.txt`):

**(a) The find-spot is wrong, and the province is wrong.** Line 56818 carries the section heading "**MAVRETANIA SITIFENSIS SVPPL.**" Inscriptions 20480, 20481 and 20482 all fall under it. 20482's own entry (lines 56868–56870) reads: "fragmentum epistylii ut videtur (longum m. 1,80, altum 0,20, litt. [alt.] 7 Poulle). **[Beni] Fuda ad portam domus Farges**." Beni Fouda is in the Sétif region — the volume prints it in the *Mauretania Sitifensis* supplement, not among the Numidian material. The document's "found near Constantine" appears to be a misreading of the bibliographic citation immediately below ("Poulle **rec. de Const.** XXVI p. 388 n. 77") — the *Recueil de la Société archéologique de Constantine*, a **journal**, not a find-spot. This is a textbook instance of the "misattributed citation" failure mode the Decision Log tracks.

  This is not pedantry: Registry row 48's own warrant stresses "This is the **Numidia supplement fascicle specifically**… **Numidia is this world's own Donatist heartland province**," and §5 is built around Numidian material. The one inscription actually adduced is not Numidian.

**(b) The document contradicts itself two clauses apart, and the "missing" inscription is the better one.** The document says the second, fuller passage is "in the same volume, independent of the first," and then says n. 17732 "was not found in this particular volume." **The fuller passage IS n. 17732.** It sits at lines 3850–3859, in the section headed "**V (VII). BAGAI (Ksar Baghaï)**," immediately after that section's own cross-reference "v. infra n. 17731." Its text and note read (OCR-normalised):

  > `[DE]O LAVDES` **(bis)** … "Uti [Deo] gratias (cf. n. 2292) catholicorum, ita [Deo] laudes signum ac tessera fuit Donatistarum, quorum sedes primariae erant **Bagai et Thamugadi**." — found "in pilis duabus… prope Bagai. Nunc asservantur Khenchela."

  So: it is present; it is a real catalogued inscription, not merely an editorial "passage"; it carries "DEO LAVDES" twice on two pillars; and it is **from Bagai itself** — one of the two Donatist primary seats its own note names, and a site of first-rank importance to this world (the 394 Bagai council, §1). The document declared absent the single best piece of epigraphic evidence in the volume for its own claim, and used a fragmentary architrave from another province instead.

  It also follows that the two attestations are **not** "independent of the first": the first note's entire content is a cross-reference *to* the second. There is one editorial identification, not two. That inflates the evidentiary weight behind a Confidence A rating.

**(c) The phrase "as distinct from" is in quotation marks but appears nowhere.** 20482's note reads, in full: "Deo laudes (de hoc signo Donatistarum cf. supra ad n. 17732)." It contains no comparison with *Deo gratias* at all — that comparison belongs to 17732's note, and its Latin is "Uti… ita…" ("just as… so…"). Presenting an English phrase in quotation marks that appears in neither note, attached to the wrong note, is a fabricated quotation.

**(d) At least two further *Deo laudes* inscriptions in the same file were missed.** Line 4550: n. **17368** (Ain Mtirschi), "DEO LAVDES." Line 24461: n. **18669** (Duar Medfun, "in lapide magno"), "**DEO LAVDES DICAMVS**." With 17732 and 20482 that is four attestations in one volume — a materially stronger epigraphic base than the document claims, found by a single grep.

**(e) The disclaimer is false in its own terms.** The document says the "physical description beyond 'a fragment'" was not researched. The entry it cites gives the description in full: an architrave fragment, 1.80 m long, 0.20 m high, letters 7 cm. Simultaneously asserting an unsupported find-site and disclaiming a description the cited entry supplies is a discipline failure in both directions at once.

---

# MEDIUM SEVERITY

## M1. §4 and §6 use Registry row 50 well beyond the licence row 50 grants, and leave row 50 stale

**Claim made:** §4 runs the full five-item Formation Narrative evaluation on the sermon, and §6 adds a Source Asymmetries bullet, both citing "Registry row 50."

**What I found:** `Source_Registry.md` row 50 states its own licence: "**Licensed only for its own existence, genre, and Mabillon's own dating analysis at this pass; its theological or rhetorical content has not itself been analyzed**," and closes: "**Not yet evaluated** against Doc_02 §4's five-item formation-narrative framework or §6's Source Asymmetries discussion — flagged here as a new find requiring that evaluation in a future pass, **not a completed one**."

Doc_02 §4 now makes content claims (the "military action," the seized basilica, "a death within" it, the liturgical-practice inference, the Author Gravity assessment) that row 50 explicitly does not license, and §6 runs the Source Asymmetries discussion row 50 says has not been run. Meanwhile row 50 was not updated in this revision.

**Why it matters:** The masthead states that Doc_02 and the Registry are "co-equal outputs, not sequential ones," and that "Every specific claim below is traceable to a Source Registry row." A claim traceable to a row that disclaims it is not traceable. Either the row's licence must be widened (with its Verification Note rewritten to say what was actually read) or the §4/§6 content claims must be pulled back. Right now the pair is internally inconsistent, and the inconsistency runs in the direction of overclaiming.

## M2. §3's Confidence-A licensing of Monceaux exceeds what Registry row 40's own Verification Note records

**Claim made:** §3: "Confidence A on identity and general coverage (directly verified this session against the vendored text), Registry row 40… **Licensed for: Tyconius's biography and reception (§1, §2 above)**."

**What I found:** Registry row 40's Licensed-For field names only "A second, independent public-domain route to the Macarian-repression Passiones (rows 19, 20); corroborating literary-historical treatment of Optatus, Tyconius, and the earliest Donatist writings generally." Its Verification Note ends: "**Specific content (e.g. the Tyconius chapter's own analysis) not yet read in depth for a substantive claim** beyond confirming its existence and general coverage."

The Registry's own calibration rule (line 8) is explicit: "Confidence **A** is used where **every specific thing a row's Licensed-For field names** was itself directly read and verified against the vendored text this session."

**Why it matters:** §1, §2 and §4 now draw eight or more substantive characterisations from the Tyconius chapter's analysis. Those readings appear (I verified them — see "What Verified Clean") to have actually been done and done accurately. The problem is purely that the Registry row was not updated to say so, so §3's licensing statement is unsupported by the row it cites, and row 40 still carries a disclaimer that the document has silently overrun. This is the mirror image of M1 and should be fixed in the same pass.

## M3. §4 — "Honoratus of Sicilibis (**Scillium**)" is an invented identification, contradicted by the vendored file's own note and by Monceaux; and the other half of Mabillon's argument is dropped

**Claim made:** "Mabillon argues from internal evidence that neither name is actually spoken in the sermon itself, and that the events instead concern a bishop he identifies as **Honoratus of Sicilibis (Scillium)**."

**What I found:** Mabillon writes (Migne file, lines 128–131): "fit tantum ibi mentio Honorati episcopi **Scilibensis aut potius Sicilibensis** in provincia proconsulari." He gives two spellings of one name and prefers the second. He never mentions Scillium. The file's own Variorum note (lines 577–588) fixes the place beyond argument:

> "Scilibensis. **Legendum Sicilibensis.** In concilio Carthaginensi sub S. Cypriano sententiam dixit Satius a **Siciliba**… Nota urbs ex **Itinerario Antonini**, ubi dicitur **Sicilibra**: apud Anonymum Ravennatem **Siciliba**. Hæc sita erat in provincia proconsulari et utrumque Tuburbum oblique respiciebat, **a majori M. passuum 18 distans**."

Sicilibba is a town 18 Roman miles from Tuburbo Maius. Scillium/Scili — home of the Scillitan martyrs — is a different place. Monceaux independently uses "Sicilibba" throughout (lines 3022, 3192, 3314). The parenthetical gloss "(Scillium)" is the document's own addition, is unsupported, and is contradicted by the file it cites.

**Also dropped:** Mabillon's argument has two halves, and the document reports only one. The other (Migne lines 186–216) is that the "Donatus" of the title might be Donatus of Bagai (Optatus III.4; Usuard's martyrology at 4 March, "passus sub Ursatio duce et Marcellino tribuno, quod cum actis nostris concinit") — which Mabillon then **refutes**, because Augustine (Hom. XI in Ioannem) says that Donatus was thrown into a well, whereas all the martyrs here were killed in the basilica. Registry row 50 records this half ("speculates a possible identity between the 'Donatus' named in the title and Donatus of Bagai"); Doc_02 does not. Losing it loses the reasoning that produces the conclusion the document does report.

**And it is superseded anyway.** Monceaux (lines 3243–3259) resolves the title problem differently and better:

> "Nulle part, dans la relation, ne figure un martyr Donatus ni un martyr Advocatus. En revanche, le récit mentionne le meurtre d'un **évêque d'Advocata ou Abvocata**… L'opuscule aurait été intitulé : *Sermo de Passione Donati ep(iscopi) Advocat(ensis)* ou *Avioccal(ensis)*… cet évêque d'Advocata ou Avioccala, dont on nous conte la mort, et qui se serait appelé **Donatus**."

That is: "Advocatus" is a place (Avioccala), and "Donatus" is the name of its bishop, who *is* killed in the narrative — so the title is largely right, merely corrupted. The document says it "reports rather than resolves" this question while holding a vendored resolution of it.

## M4. §4 — Mabillon's dating is described twice as "internal evidence"; it is overwhelmingly external

**Claim made:** §4: "This dating is Mabillon's own inference from **internal evidence**, not a stated date in the text itself." §8 repeats: "a reasoned inference from **internal evidence**."

**What I found:** Mabillon's chain (Migne lines 140–216) runs on external witnesses almost throughout — Optatus lib. III §4 and §5 and lib. II (quoted verbatim), the Zenophilus proceedings of 320, the *Acta Collationis Carthaginiensis* diei III cap. 258 (the letter of Januarianus, quoted verbatim), Usuard's martyrology at 4 March, Augustine *Hom. XI in Ioannem*, Cresconius and Petilian as reported by Augustine, and the death of Caecilian before the Council of Sardica (347). The only genuinely internal datum is that the present instrument shows Leontius as *comes* and Ursatius as *dux* at the same time.

**Why it matters:** Not a large error on its own, but it misdescribes the *kind* of argument being relied on, and it does so in the sentence that sets the confidence level. An external-cross-reference argument is checkable against vendored texts (Optatus and the relevant Augustine are both vendored); an "internal evidence" argument is not. Calling it internal is what makes §9 item 12's "flagged for a future pass" look adequate when it isn't — see L9.

## M5. §4 — The ellipsis in Mabillon's judgment of the author removes the concessive that frames it

**Claim made:** Mabillon "judges the author 'a certain African writer, not unskilled… versed not slightly in the sacred letters and in the precepts of Christian doctrine.'"

**What I found** (Migne lines 217–222), in full:

> "Ceterum opus istud est **Afri cujusdam scriptoris non infantis**, et **licet in Ecclesiam catholicam egregie maledici**, attamen **haud indocti et imperiti**: imo hominis est in sacris litteris et in christianæ doctrinæ præceptis **non mediocriter versati**, qui multa præclara profert, **utinam in meliori causa**."

The document's ellipsis silently removes "**although he reviles the Catholic Church remarkably**," and its quotation stops before "**would that it were in a better cause**." What remains reads as a scholarly compliment; what Mabillon actually wrote is a backhanded concession by a hostile Catholic editor about a competent heretic.

**Why it matters:** The document uses this judgment to establish the sermon's standing as a serious Donatist voice. The removed material does not undercut *that* — it arguably strengthens it — but removing it without ellipsis-marking the concessive is exactly the "elided quotation trusted rather than the source re-opened" variant the Decision Log records Round 5 catching and fixing. It should not recur. (Also minor: "sermonem habitum" is "the sermon was *delivered*," not "writing.")

## M6. §4 — The "annual liturgical commemoration" claim is attributed to the heading and to a phrase that does not mean what the sentence needs

**Claim made:** "its own text carries the heading '4. Idus Martii Sermo de Passione SS. Donati et Advocati,' **identifying it as read aloud at an annual liturgical commemoration** ('*anniversaria solemnitate*')."

**What I found:** The heading contains a date and a title; it identifies nothing about liturgical use. The phrase "anniversaria solemnitate" is from the sermon's §I (line 247) and there refers to the reading of *persecution-gesta generally* — "nec inconsulte in honorem martyrum et ædificationem credentium **anniversaria solemnitate leguntur**" — not to this sermon. The claim is nonetheless **true**, and better evidence for it sits unused in the same file: Mabillon's admonitio, "Sermo est habitus 4 Idus Martii **in solemni et anniversaria commemoratione** quorumdam Donatistarum qui apud suos pro martyribus habebantur" (lines 123–125), and the sermon's own §IX, "**Nam et anniversalis dies religiosa devotione non immerito celebratur**" (line 540). Monceaux cites exactly these two loci in his footnote 6 (line 3110–3113) and builds his whole "panégyrique prononcé dans une église pour un anniversaire de martyrs" reading on them.

**Why it matters:** A correct conclusion supported by the wrong citation is still a citation failure, and here the correct citations were three lines away in the same file. Fix the attribution rather than the conclusion.

**Related, and substantive:** the *manuscript title* and the *heading* the document treats as two separate witnesses are the same title with a liturgical date prefixed — and Mabillon's own conclusion is that the title is **alien to the sermon** ("Ergo alienus est titulus ab ipso sermone," line 216). Calling it "its own text['s]" heading concedes nothing Mabillon grants.

## M7. §1, §3, §6 — Boyd is used as a corroborating authority on the Circumcellions, where his single sentence about them is precisely the hostile characterisation the document says must be marked

**Claim made:** §6: "Boyd's now-vendored corroborating history (§1, §3 above) discusses the surrounding legislative sequence (C. Th. xvi.5.3–58) extensively but does not itself quote 16.5.52, and never uses the term *agonistici* — Boyd, writing in 1905, uses only 'Circumcellions' throughout, itself a small data point on how the field's own terminology has shifted since."

**What I found:** Boyd's only sentence on the group (line 6748) reads:

> "The Circumcellions, a mendicant, socialist sect, were appealed to for aid by the Donatists at the time of the persecution of Constans. Northern Africa was soon infested with a body of religious fanatics, escaped slaves, erring priests and nuns who tortured the Catholics, defiled churches and forced the laity to accept Donatist baptism."

That is Augustine's and Optatus's framing restated uncritically in 1905 — the exact construction §6 says Shaw's *Sacred Violence* is the standard treatment of. Boyd also writes, a paragraph earlier: "The emperors from Constantine to Honorius, **with the exception of Constans, permitted the Donatists to remain unmolested**" — which is flatly contradicted by the 317–321 Caecilianist persecution that this same revision's newly-vendored sermon documents (H2), and by Optatus.

**Why it matters:** §3 does not have a Boyd entry at all (it is cited only through §1's Registry row 49), so no confidence rating or licensing statement governs its use — yet §6 leans on it in the Circumcellion bullet, which is the bullet most exposed to exactly this bias. Boyd should be given a §3 entry with an explicit note that his own Donatist/Circumcellion narrative is uncritical of the hostile sources and is licensed for the **legislative sequence only**, not for characterisation. The document's use of him for the terminological observation is fine; its silence about his framing is not.

## M8. §2 names an open question that §9 does not carry forward

**Claim made:** §2, Optatus/*Limitations*: Ziwsa's CSEL 26 is now vendored, "but its own apparatus has not yet been read for that purpose this session; **this limitation is named as open, not resolved**."

**What I found:** §9 "Open items carried forward" has twelve numbered items. None of them is the Optatus second-edition question. Item 1 mentions G2 only as discharged. So a limitation the document explicitly declares "open" in §2 is not on the open-items list — a thread that the "now vendored" update created and then dropped.

**Why it matters:** §9 is the mechanism by which this document's unfinished business survives into Doc_04/Doc_08. An item declared open in the body and absent from §9 will not survive. Add it as item 13.

## M9. Monceaux says something directly bearing on Doc_01 §4's cleared strand finding, and the revision does not surface it

**Claim made:** §1: "Doc_01 §4 found that Tyconius's own dissent does not rise to strand status (**no attested following, parallel authority structure, or distinct communal practice**); that finding does not depend on this acquisition and is not reopened here." §2, *Limitations*, restates it.

**What I found:** Monceaux, lines 3529–3536:

> "Repoussé par les Donatistes, et ne pouvant se décider à se rallier aux Catholiques, Tyconius, à son corps défendant, **devint le chef d'une petite Église schismatique, où peut-être il était le seul fidèle**."

On its face, "became the head of a small schismatic church" is an attested (if nominal) parallel authority structure — and Monceaux's own qualifier, "where perhaps he was the only member," is what defeats it. That qualifier *corroborates* Doc_01 §4's finding, and rather elegantly.

**Why it matters:** The document repeatedly says the Tyconius finding "is not reopened here" — which is correct procedure. But when a revision vendors a new source that speaks directly to a cleared finding, the honest move is to report that the new source was checked against it and what the check showed. Here the check would have *strengthened* the cleared finding at no cost. Leaving it out means a future reader who opens Monceaux will find a sentence that looks like counter-evidence to a cleared finding, with no record that the build ever saw it. This is close to, but in my judgment does not reach, the "unresolved tension between cleared documents" escalation category — see M10.

## M10. §10's escalation re-assessment is stated as run, but its premises do not survive verification

**Claim made:** §10: "**Escalation-category assessment… re-run for this revision's own new content**… none of the four categories is triggered by this revision either. The new material is ecology-grounded (a newly-vendored primary text, a newly-vendored secondary chapter, a newly-resolved inscription attribution), decided for no reason external to this world's own evidentiary situation."

**Assessment:** On the corrected facts, I believe the **conclusion still holds** — I did not find anything in this revision that triggers Representative-identity, portfolio-level/cross-world, or governance/methodology escalation, and the Article 20/23 routing (unchanged from the cleared version) is applied correctly. The Monceaux/Doc_01 §4 point (M9) is the only near-miss, and it resolves in favour of the cleared finding rather than against it.

But the re-assessment as written was run against the document's own summary of the new material, not against the sources. Two of its three named grounds are wrong as stated: the "newly-resolved inscription attribution" is misprovenanced and self-contradictory (H8), and the "newly-vendored primary text" is misdated, misattributed and mischaracterised (H1–H4). An escalation check whose factual premises fail is not a check that has been run.

**Required:** re-run §10's assessment after the H- and M-level corrections, and state in the Decision Log that it was re-run on corrected facts. Do not carry the current §10 paragraph forward unchanged.

---

# LOW SEVERITY

**L1. §1 — Monceaux's six manuscript spellings of Tyconius reduced to four, presented as a complete list.** The document gives "(Thiconius, Tychonius, Ticonius, and Tyconius all attested)". Monceaux (lines 8463–8467) gives six: "*Thiconius* ou *Thyconius* ou *Tichonius* ou *Ticonius* ou *Tychonius* ou *Tyconius*." The two dropped forms include *Tichonius*, which Monceaux says was formerly the near-consensus spelling ("Jadis… l'on s'accordait à peu près pour écrire Tichonius") — the one variant with a history worth reporting. Either mark the list as partial or complete it.

**L2. §1 — "rather than Numidia" is the document's gloss, not Monceaux's.** Monceaux writes only "Il était Africain (*Afer*), de l'Afrique propre, c'est-à-dire de Proconsulaire" (line 8487). The Numidia contrast is a reasonable inference in this document's context (§5 turns on the Numidia/Proconsularis distribution) but should be marked as the document's own, not attributed to Monceaux. Relatedly, "certainly raised in the Donatist faith" is presented as something Monceaux "records"; his basis (line 8488–8490) is an argument from silence — "autrement, ses adversaires n'auraient pas manqué de lui rappeler qu'il avait changé de camp" — which is worth a half-clause.

**L3. §6 — "Boyd… uses only 'Circumcellions' throughout" overstates a single occurrence.** "Circumcellions" appears exactly once in Boyd's essay (line 6748). "Throughout" implies a settled usage across a body of discussion; the accurate statement is that Boyd uses the term once, in his only sentence on the group. (The *agonistici* half of the claim is correct — I confirmed the word appears nowhere in the file; the only near-hits are "antagonistic," lines 8671 and 18254.)

**L4. Registry-row citation inconsistency across §1, §9 and §10.** §1 cites "Registry rows 17 and 39" for *Contra Cresconium* and *Contra epistulam Parmeniani*; §9 item 10 and §10 both cite "rows 17, 18, 39." Row 18 is *Contra epistulam Parmeniani*, so §1 is the one that is wrong.

**L5. §3 — dangling cross-reference.** Monceaux's entry closes: "a distinction from **the Confidence-A rows above** that rest on direct primary-text reading." There are no other Confidence-A entries in §3 (Frend B, Shaw B, Tilley C, Brown B). If Registry rows are meant, say so.

**L6. §4 — *Proximity* slides from dating events to dating composition.** "*Proximity:* **on Mabillon's own dating**, a near-contemporary composition." Mabillon dates the *events* ("quæ hic referuntur contigisse circa annum 340"); on the sermon's composition he says only that its style proves the author ancient and that it was delivered while the Donatist sect flourished. Monceaux is the one who dates the composition (*c.* 320) and who establishes the far stronger proximity claim — that the preacher was an eyewitness (H3).

**L7. §4 — "the 'deceitful frauds and snares of gentle deception' **of persecutors**" flattens the sermon's own distinction.** The sermon's whole rhetorical premise is the *contrast* between open persecution and deceptive friendly seduction under the pretext of unity — "Magis enim necessaria instructio illic est, ubi **professa hostilitas non est**" (lines 251–253), and Valesius's note on the passage makes it explicit: "Fatetur ergo hic [auctor] rem ad persecutionem in Donatistas non fuisse similem persecutioni ethnicorum in Christianos" (lines 261–263). The Latin attributes the frauds to those "quæ sub obtentu religionis animas fraudulenta circumventione subvertunt" — deceivers, precisely *as opposed to* open persecutors. Small, but it inverts the point of the passage quoted.

**L8. §9 item 12 misses the checks that are available now.** Item 12 flags the sermon's "fuller narrative content" for Doc_09. It does not flag that Mabillon's own apparatus cross-references **Optatus III.4 and III.5** and **Augustine** on the Leontius/Ursatius persecution — both vendored, in `optatus_against-the-donatists.txt`, `optatus_libri-vii-critical_ziwsa1893.txt` and the NPNF Augustine volumes — and are therefore checkable *this pass*, not a future one. Combined with M4's mischaracterisation of the dating argument as "internal," this makes the open item look adequate when a cheap, immediately available verification was left on the table.

**L9. §4 — "his own chapter outline names… as distinct sections."** "Condamnation de Tyconius par un concile. — Ses dernières années" (Monceaux line 8420–8421) are topics listed in the argument-summary line of chapter V section I, not distinct sections of the chapter. Trivial, but the document is elsewhere careful about this kind of distinction.

**L10. §5 — Monceaux's own treatment of the *Passio Marculi*'s date was not consulted** ("La *Passio Marculi*. — **Date de l'ouvrage**," line 3024), even though §3 licenses Monceaux as "a second, independent route to the Macarian-repression Passiones alongside the vendored Migne text" and §4's Passio Marculi dating rests on Frend plus a misread editorial heading (H7).

---

# What Verified Clean

I want to be explicit about what held up, because it is a lot, and because the Monceaux/Tyconius work — which the review brief flagged as a target — is largely accurate.

**Monceaux on Tyconius (§1, §2) — every substantive characterisation checked against the French text and confirmed:**

| Document's claim | Monceaux, verbatim | Verdict |
|---|---|---|
| a layman in a movement where "only the primate spoke in the party's name," laity having little standing but to obey | "c'était un écrivain laïque… dans ce monde si discipliné des schismatiques, **où le primat seul parlait au nom du parti**, et où l'on ne reconnaissait guère aux laïques qu'un droit, **le droit d'obéir**" (8426–8429) | Accurate |
| a polemicist "like every Donatist" who pursued truth even against his own side, provoking "scandal and irritation" | "Polémiste, Tyconius l'était sans doute, **comme tout Donatiste**… mais il l'était à sa manière, **qui scandalisait et irritait les siens**, ne cherchant dans la polémique que la vérité… sans crainte de déplaire à ses amis ou de travailler pour ses adversaires" (8434–8440) | Accurate |
| an exegetical system original enough to "impose itself on both rival Churches" and inspire Augustine | "il réussit à fonder un système original d'exégèse, qui mérita ce privilège unique, **de s'imposer également aux deux Églises rivales, et d'inspirer Augustin lui-même**" (8443–8445) | Accurate |
| African by birth, of Proconsular Africa | "Il était Africain (*Afer*), de l'Afrique propre, c'est-à-dire **de Proconsulaire**" (8487) | Accurate (see L2 on "rather than Numidia") |
| certainly raised in the Donatist faith | "Il avait été **sûrement élevé dans la foi donatiste**" (8488) | Accurate (see L2 on the basis) |
| Monceaux follows the oldest *Regulae* MS's "Tyconius" | "le plus ancien manuscrit des *Regulæ* donne **Tyconius**. Par suite, c'est la leçon la plus autorisée : nous nous y tiendrons" (8475–8477) | Accurate (Cod. Remensis 364) |
| §2: what survives is "only in part," *Liber Regularum* substantially complete, rest via fragments and via Parmenian/Augustine/Gennadius | "cette œuvre **ne nous est connue qu'en partie**. Si nous possédons le Livre des *Regulæ*, nous n'avons sur le reste que des données incomplètes : fragments de plusieurs ouvrages, analyses ou réfutations **de Parmenianus, d'Augustin, de Gennadius**, ou autres" (8448–8456) | Accurate |
| Monceaux cites Burkitt 1894 as his own edition of the text | "Nous citerons l'ouvrage d'après l'édition critique de Burkitt, *The Book of Rules of Tyconius* (Cambridge, 1894…)" (8497–8503) | Accurate — genuine cross-validation |
| §9 item 11: Monceaux's biographical footnotes are Aug. *Ep.* 93.10.43–45 and *C. ep. Parm.* I.1 | "Cf. Augustin, *Epist.* 93, 10, 43-45 (éd. Goldbacher, 1898); *Contra Epistulam Parmeniani*, I, 1 (éd. Petschenig, 1908)" (8497–8503) | Accurate |
| §3: Monceaux corroborates the Registry's Migne column citations for both Passiones | "*Passio Marculi*, p. 760 / 761 / 762 / 766 Migne"; "*Passio Maximiani et Isaac*, p. 768 / 770–773 / 772 Migne" (1860, 1965, 1971, 2186, 3547) | Accurate. Minor: the Isaac/Maximianus citations (768–773) run *past* the Manifest's 760–766 range, so they extend rather than corroborate it |

**Other checks that held:**

- **Burkitt file identity** — genuine 1894 *The Book of Rules of Tyconius*, Texts and Studies III/1, Burkitt named as editor. Correct edition. ✔
- **Petschenig file** — both *Contra Cresconium* (four books, with internal "Explicit liber quartus… contra Cresconium") and *Contra epistulam Parmeniani* (three books, "Explicit liber tertius… contra parmeniani epistolam") confirmed present in the single vendored file, as §1 claims. ✔
- **Boyd, *agonistici*** — the term appears nowhere in the file. ✔
- **Boyd, C. Th. xvi.5.52** — not quoted; Boyd's citation chain runs …47, 51, 55 (of 412), 54 (of 414), 56–58. ✔
- **Boyd, 405 legislation at xvi.5.38–39** — confirmed: footnote 2 to p. 56, "C. Th., xvi, 5, 38, 39. It is interesting to note that this was the first state legislation on heresy approved by Augustine," attached to the 405 Honorius law declaring the Donatists heretics, confiscating their assembly places, excluding testamentary rights and imposing fines. ✔ (Boyd does not use the phrase "Edict of Unity"; that is the document's label, which is fine.)
- **Boyd, sequence xvi.5.3–58 and laws quoted verbatim in Latin** — xvi.5.3 at the head of the chain; xvi.5.28 and xvi.5.41 both quoted in full Latin, xvi.5.41 naming the Donatists directly. ✔
- **CIL 20482's editorial note, verbatim** — "Deo laudes (de hoc signo Donatistarum cf. supra ad n. 17732)." ✔ (Everything the document builds around it is wrong; the quotation itself is right.)
- **The Bagai/Thamugadi content** — "Uti [Deo] gratias… catholicorum, ita [Deo] laudes signum ac tessera fuit Donatistarum, quorum sedes primariae erant **Bagai et Thamugadi**." ✔ substantively, though see H8(b) on where it is and what it is.
- **The sermon's manuscript title and heading** — "De passione sanctorum Donati et Advocati" (line 126–127) and "4. Idus Martii Serm[o] de Passione SS. Donati et Advocat[i]" (line 228–229). ✔ (OCR-normalised; noted, not faulted.) Monceaux quotes the identical heading at line 3110.
- **The sermon's exordium, in substance** — the document's rendering of §I is a fair paraphrase of "Si manifesta persecutionum gesta non otiose conscripta sint, nec inconsulte in honorem martyrum et ædificationem credentium anniversaria solemnitate leguntur: cur non magis subdolæ fraudes et blandæ deceptionis insidiæ conscribantur pariter et legantur…" (lines 232–251), with the caveat at L7. ✔
- **Mabillon's "militaris executio"** — "Describitur autem illic militaris executio adversus aliquot Donatistas Carthagini gesta: in qua erepta est eis basilica" (lines 132–134). The document's "military action… in which a church building was seized" is accurate. ✔ (The clause that follows it is not — H4.)
- **Mabillon's date words** — "circa annum [3]40… certe antequam Macarius mitteretur in Africam circa annum 348" (lines 183–186). ✔ verbatim, modulo the dropped "aut paulo post."
- **Mabillon on the manuscript title** — "Inscribitur in manuscripto: *De passione sanctorum Donati et Advocati*. At in ipso sermone **neutrius nomen habetur**… Unde non Donati, neque Advocati, sed **Honorati potius Passio dici deberet**" (lines 126–132). ✔ as far as the document goes (see M3 for what it omits and mis-glosses).
- **Mabillon on the author's competence** — the words quoted are present (lines 217–222). ✔ (See M5 on the ellipsis.)
- **The *Passio Isaac et Maximiani* incipit** — "Incipit Passio SS. Martyrum Isaac et Maximiani, quæ est 7 kal. septembris" (lines 1379–1380). ✔ (The authorship claim in the same sentence is not — H5.)
- **Remaining "not vendored" statements, checked one by one:** the *Gesta Collationis Carthaginiensis* ("confirmed unavailable in the public domain and not requested"), the Mommsen–Meyer *Codex Theodosianus* critical edition ("remains unvendored after five separate acquisition attempts"), and Gregory the Great's Register (§7, "not yet vendored") are each still accurate against `Source_Acquisition_Manifest.md`, `Source_Registry.md` and `cic/texts/`. No stale "not currently vendored" statement survives anywhere in the document. ✔
- **Escalation categories** — no category is triggered on the corrected facts (see M10 for why the check nonetheless has to be re-run).

---

# Did the revision do the job Mark asked for?

Mark's instruction (`don_Decision_Log.md`, 2026-09-01): row 50 "is a genuine primary source and **should be integrated into Doc_02 at a base level**, not left as a flagged Registry row alone."

**On form: yes.** The sermon gets a full five-item Formation Narrative evaluation in §4, a substantive Source Asymmetries bullet in §6, a Confidence Map entry in §8, and an Open Item in §9. That is integration, not a mention. The §6 bullet in particular does the right conceptual work: it identifies the sermon as a correction to the Author Gravity concentration and immediately bounds the correction. The instinct is sound and the structure is right.

**On substance: not yet, and in one specific way it fails in both directions at once.** It *overclaims* where the evidence does not reach — "the first vendored text… that speaks as a Donatist" (H6), "the most direct correction available to this world's central evidentiary problem," "nothing… is checkable against any source outside the vendored text and Mabillon's own apparatus" (H1). And it *underclaims* exactly where the evidence is strongest — "anonymous" for a text a vendored authority attributes to Donatus the Great (H3), "a death" for a multi-basilica massacre (H4), *c.* 340 for a text dated 317/*c.* 320 by the same authority (H2), an incidental curiosity for one of the three canonical Donatist martyr-texts (H1).

The overclaiming and the underclaiming have the same root: the sermon was assessed against one 17th-century apparatus rather than against the modern scholarship the same acquisition round put on disk. Fixing that one thing — reading Monceaux, lines 3018–3266 — resolves H1 through H4 and M3 together, and produces a *stronger and more defensible* §4/§6 than the document currently has.

---

# Recommended disposition

**Do not self-dispose.** Revise and re-review. Specifically, in priority order:

1. **Read Monceaux, `monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt` lines 3018–3266**, and rewrite §4's sermon bullet and §6's first bullet against it. Name the text as the *Passio Donati*. Report the 317 / *c.* 320 dating as the modern reading against Mabillon's *c.* 340, and mark the dating Contested in §8 with both authorities named. Report Monceaux's Donatus-the-Great hypothesis *and* his hesitation. Report the eyewitness finding. Correct "a death" to what the sources say. Correct the title question to Monceaux's *Donati ep. Avioccalensis* resolution, marked as the modern proposal against Mabillon's Honoratus one.
2. **Fix H5, H6 and H7** — Macrobius's authorship, the §4/§6 contradiction, and the *Passio Marculi* heading quotation and dating.
3. **Rebuild §5's epigraphic bullet from the file** — inscription 17732 (Bagai) as the primary witness, 20482 correctly provenanced to Beni Fuda in the volume's Mauretania Sitifensis supplement, 17368 and 18669 noted, and the fabricated "as distinct from" quotation removed.
4. **Reconcile the Registry** — update rows 19, 20, 27, 40 and 50 in the same pass, since M1 and M2 are Doc_02/Registry mismatches in opposite directions and cannot be fixed on one side alone.
5. **Add the Ziwsa second-edition question to §9** (M8), and add a §3 entry for Boyd with an explicit anti-bias caveat (M7).
6. **Re-run §10's escalation assessment on corrected facts**, and record in `don_Decision_Log.md` that the tracked recurring failure mode (fabricated/misattributed citation adopted without independent verification) **recurred in this revision** after two clean rounds, with the four instances named (H7, H8, M3, and the "as distinct from" quotation).
