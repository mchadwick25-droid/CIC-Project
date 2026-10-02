# Texts — Acquisition Want-List

**Written:** 2026-08-18, answering Mark's question: what public-access documents on CCEL (or equivalent) could be downloaded, including things that would need translating to reach.
**Method:** derived from what the six world scrubs proved missing, checked against `cic/texts/` on disk. Nothing here is a browse result.
**Standing caveat, stated first:** this sandbox blocks patristic hosts (which is why the corpus was vendored in the first place), so **I could not verify a single one of these is actually posted on CCEL today.** Every entry names the edition, its date, and why it is public domain, so you can search for it. Where a candidate is listed without a located edition, it says so.

---

## The headline

**Thirty-seven of the thirty-eight ANF/NPNF series volumes are already vendored. One is missing: `npnf209` — Hilary of Poitiers, and John of Damascus.**

That is not a leftover. It is exactly the volume the Imperial-Juridical scrub named as its one series gap (`Texts_Scrub_imperial.md` finding 7): *"NPNF2-09 (Hilary of Poitiers) is the one series volume not vendored — it would carry Nicene-resistance documents against the Homoian establishment (Ad Constantium, Contra Auxentium) plus further Homoian creed texts."*

So the highest-confidence acquisition in the whole list is also the easiest: same series, same publisher, same source, same file format as the forty already on disk, and it fills a named hole.

---

## Tier 1 — ~~certain, one file~~ **ACQUIRED 2026-08-18**

**Done.** Mark supplied `npnf209` the same day this list was written. Vendored as
`cic/texts/npnf209_hilary-poitiers-john-damascus.xml` — CCEL ThML, `DC.Rights: Public Domain`,
print source Edinburgh: T&T Clark, 1898. It parses, it has an `ENTRIES` row, and the generated
README lists it. **The vendored corpus is now the complete ANF/NPNF set: 38 of 38 series volumes,
41 files.**

**One correction, because it matters for what gets built on it.** Both the Imperial-Juridical scrub
(finding 7) and this list, one section above, predicted the volume would carry *Ad Constantium* and
*Contra Auxentium*. **It does not.** Its own division titles give the NPNF selection as *De Synodis*,
*De Trinitate*, three Homilies on Psalms, and John of Damascus's *Exposition of the Orthodox Faith*.
Hilary's historical and polemical works are not translated in this series at all. "Auxentius" occurs
sixty-four times in the file, but in the editor's Introduction — not as *Contra Auxentium* text. If
those two works are still wanted, they need a separate acquisition and are **not** covered by NPNF.

**What arrived instead is worth more than what was asked for.** Hilary's *De Synodis* — 167,000
characters — reproduces the Eastern creeds **verbatim with their numbered anathemas** (*"If any man
says that the Father and the Son are two Gods: let him be anathema"*), plus the Homoean formula that
the Son is *"like the Father in all things, as Scripture says."*

That resolves a caveat the Imperial scrub had to leave open. Its finding 4 located those same creeds
in `npnf204` — Athanasius's *De Synodis* — and then had to flag that `srcIJC24` **excludes the
Athanasius corpus beyond the single Julius quotation**, so using them would need an owner decision.
**Hilary is an independent Latin transmitter of the same texts.** The exclusion does not reach him,
so the Homoian establishment can now be quoted in its own words with no decision required.

---

## Tier 2 — the three that change a world's shape

These are not marginal additions. Each one lifts a world out of a structural gap its scrub called load-bearing.

**1. E.A.W. Budge, *The Paradise of the Holy Fathers* (1907).**
The single most valuable acquisition on this list. Budge's translation of 'Anan-Isho's Syriac recension is public domain and carries **both** the Apophthegmata sayings **and** a Historia Monachorum text — the Desert world's two biggest absences in one file.

Today all six of Desert's sayings quotes (`desertq001`–`006`) rest on Ward 1975, which is in copyright and deliberately never vendored, and the scrub confirmed *"None of these six sayings appears anywhere in the 40 vendored volumes."* Without a PD sayings text every Desert quote stays either in-copyright-dependent or paraphrase-only — and under the Source Anchors spec (§5.2), a quote with no published wording beneath it cannot be anchored as a quotation at all. Budge is what unblocks that.

Caveat worth stating: Budge translates the **Syriac** recension, so his wording will not match Ward's Greek-based text sentence for sentence. That is a fidelity note to record on the source row, not a reason to skip it — a PD Syriac-recension wording is incomparably better than no wording.

**1a. The Pachomian corpus — the Rules and the Lives of Pachomius. ADDED 2026-08-18.**
Found by the force/story verification pass (`Finding_Force_Story_Verification_Blocked.md` §3), which
traced `srcDES002` — **13 force and story citations**, the seventh-heaviest source row in the fleet —
and found the vendored set carries only Gennadius's one-paragraph *notice* about Pachomius
(`npnf203`, div `v.iv.viii`), not his Rules or Lives. The Pachomian corpus is not in ANF/NPNF at all.

The standard English is Armand Veilleux, *Pachomian Koinonia*, 3 vols. (Cistercian Publications,
1980–82) — **in copyright**. Whether a public-domain alternative exists (an older translation of the
Bohairic or Sahidic Life, or Jerome's own Latin of the Rule, which is PD and in Migne) has **not**
been checked. Jerome's Latin Rule is the most likely PD route and would need translating, like the
*Verba Seniorum* below.

**1b. Syriac — Morris 1847 and Burgess 1853, and one entry that acquisition may not fix. ADDED 2026-08-18.**
From `Finding_Syriac_Corpus_Gap.md`. NPNF2-13 carries a *selection*: 58 of 77 Nisibene hymns, 7 of 87
Hymns on Faith, and **8 of Aphrahat's 23 Demonstrations** (I, V, VI, VIII, X, XVII, XXI, XXII, named
by the volume itself). The Syriac records cite Demonstrations 7, 11, 14 and 23, none of which is there.

*Public domain and worth searching:* **J.B. Morris, *Select Works of S. Ephrem the Syrian*** (Oxford,
Library of the Fathers, 1847); **Henry Burgess, *The Repentance of Nineveh*** (1853) and his *Select
Metrical Hymns and Homilies of Ephraem Syrus* (1853). Not checked for availability (this sandbox blocks
the patristic hosts), and **their overlap with NPNF2-13 is unmeasured** — Morris may duplicate rather
than extend it. Measure before treating either as a gain.

**The entry that acquisition may not fix.** `srcSYR009`, Ephrem's *Commentary on the Diatessaron*, is
`syrlex006`'s named primary textual base, and `syrlex006` is the harmonised-Gospel term — one of the
three features that define this world. The Syriac text was not available in the nineteenth century and
the standard English (McCarthy, 1993) is in copyright, so **a public-domain English may not exist at
all.** Same for *Contra Haereses*, the *Prose Refutations*, the *Hymns on Paradise*, and the *Commentary
on Genesis and Exodus*. This should be checked rather than assumed — but if it holds, no money closes
it, and the answer is a declared paraphrase-only scope rather than an acquisition.

**2. *Verba Seniorum*, Migne PL 73 — the Latin fallback for the same gap.**
Public domain, Latin, and the ancestor of most English sayings collections. Listed as fallback rather than first choice because it needs translating (see Tier 4) where Budge does not.

**3. Philo, trans. C.D. Yonge (1854–55), 4 vols.**
Alexandria's `srcALX008` rows Philo for licensed diagnostic use and **nothing is vendored**. Yonge is comfortably PD, was for a century the standard English Philo, and is the exact acquisition the Alexandria scrub asked for. Alexandria's account of allegorical reading has a Jewish Alexandrian antecedent it currently cannot quote.

---

## Tier 3 — located PD editions, one gap each

Each row names an edition I have reason to believe is PD by date. Ranked roughly by how much the corresponding world needs it.

| # | Want | Edition (PD by date) | World | Closes |
|---|---|---|---|---|
| 1 | **Pliny, *Letters* 10.96–97** | Melmoth, rev. Bosanquet (1878) | PAHC | The scrub's *"biggest absence in the corpus."* `srcPAHCP07` is rowed as a PRIMARY voice, `fig006` (Pliny) is undated, and three lexicon terms — *ministrae*, *hetaeria*, *pertinacia* — are declared "his vocabulary" with no text on disk. **No Pliny quote can be authored or verified today.** |
| 2 | **Ephrem, *Prose Refutations of Mani, Marcion and Bardaisan*** | Mitchell, 1912/1921 | Syriac | `srcSYR007` **already cites this edition** — it is PD and simply not vendored. The cheapest fidelity win in the Syriac world: an edition the records name, acquirable as-is. |
| 3 | **Tacitus, *Annals* 15.44** | Church & Brodribb (1876) | PAHC | `srcPAHCP08` rows Tacitus as a primary; no vendored text. |
| 4 | **Lucian, *The Passing of Peregrinus*** | Fowler & Fowler (1905) | PAHC | Primary row P10 and story 013 lean on it; not vendored. |
| 5 | **Odes of Solomon** | J. Rendel Harris, editio princeps (1909/1911) | Syriac + PAHC | Wanted independently by two scrubs (`srcSYR012`; PAHC absence 7). Earliest Christian hymnody, and PD. |
| 6 | **Acts of Thomas** | W. Wright, *Apocryphal Acts* (1871) | Syriac | Carries the Hymn of the Pearl in full — the Syriac world's signature text — in a PD English. (`npnf213` has only a subset.) |
| 7 | **Hymn of the Pearl, standalone** | A.A. Bevan (1897) | Syriac | Alternative or supplement to the above if Wright is hard to find. |
| 8 | **Chronicle of Edessa** | B.H. Cowper, *Journal of Sacred Literature* (1864) | Syriac | `srcSYR021`; not vendored. The world's own civic chronology. |
| 9 | **Origen, *Philocalia*** | G. Lewis (1911) | Alexandria | Partial mitigation for the homiletic/spiritual gap — the scrub found *"no homily exists in any vendored volume."* |
| 10 | **Eusebius, *Praeparatio Evangelica*** | E.H. Gifford (1903) | Alexandria + Imperial | Carries fragments of authors otherwise lost, several Alexandrian. |
| 11 | **Egeria, *Peregrinatio*** | McClure & Feltoe (1919) | Hieronymian | Bethlehem-era pilgrimage in a woman's voice, contemporary with Paula. |
| 12 | **Suetonius, *Claudius* 25 / *Nero* 16** | any 19th-c. PD translation (edition not yet located) | PAHC | `srcPAHCP09`; Chrestus-clause quotes unverifiable in-repo. Low priority — the clause is four words and heavily mediated. |

**Note on the Muratorian fragment:** the PAHC scrub lists it as an absence and PD translations exist, but **no source row anywhere in `cic/records/` cites it.** Acquiring it would be building new scope, not closing a declared gap. Left off the ranked list deliberately.

---

## Tier 4 — translate to reach

You asked specifically about material that would need translating. These are all PD in their original-language editions; the cost is translation work plus, under Article 31, whatever external-review burden a build-made translation carries. **That review question is not settled here** — this section says what is reachable, not that we should reach for it.

Ranked by how safe the translation is, not by how much we want the text:

| Rank | Text | PD edition | Language | Why it is ranked here |
|---|---|---|---|---|
| 1 | ***Verba Seniorum*** | Migne PL 73 | Latin | Safest. Latin, short sayings, plain syntax, and the sense is cross-checkable against Budge and against the in-copyright modern versions without copying their wording. |
| 2 | **Aphrahat, *Demonstrations* (the ones Gwynn omits)** | Parisot, *Patrologia Syriaca* I–II (1894/1907) | Syriac, **with facing Latin** | The facing Latin is what makes this feasible — a translator can work from Parisot's Latin without Syriac. **This is the only PD route to the Demonstrations `npnf213` leaves out**, which matters directly: the Syriac scrub found *"eight of the ten relevant Demonstrations are simply not in any PD English,"* and the anti-Jewish-count contradiction (see `Finding_Syriac_AntiJewish_Demonstration_Count.md`) is exactly the kind of question this would settle. |
| 3 | **Synodicon Orientale** | Chabot (1902) | Syriac, with **French** translation | The Syriac world's **closing event** — the 410 Synod of Seleucia-Ctesiphon — has no text in-corpus in any form and rests entirely on secondary rows. Chabot's French is PD and translatable by anyone with French. |
| 4 | **Liber Graduum** | Kmosko (1926) | Syriac, with Latin | `srcSYR063`. No English exists in PD at all; Kmosko's Latin is the only route. Later and harder than the above. |

---

## Not worth chasing — recorded so nobody re-derives it

- **Every modern critical edition and translation named in the records** — Ward 1975, Lehto 2010, Pharr 1952, Price–Gaddis, Russell 1980, Rubenson, Williams (Epiphanius), Kitchen/Parmentier, Kyle Smith, Amar. All in copyright, all correctly not vendored. No amount of searching changes this.
- **Didymus the Blind's Tura commentaries** — discovered 1941. There is no PD edition and there cannot be one.
- **The Bethlehem women's own words** — Paula's and Eustochium's writing does not survive independently. Everything we have of them is Jerome's, including the letter written *in their name* (Ep. 46, and the NPNF header says so). Nothing to acquire; this is an absence in the historical record, not in our library.
- **Desert's seven Apophthegmata-only figures** — Sarah, Syncletica, Theodora, Poemen, Sisoes, John brother of Pachomius, and the ammas generally. They exist nowhere outside the sayings collections. Budge (Tier 2) is the only lever; no separate acquisition reaches them.
- **Epiphanius, *Panarion* 56** (`srcSYR018`) — no PD English exists and the Greek is not a realistic translation target for us.
- **Gesta of the Carthage Conference of 411; Collectio Avellana; the Siricius/Innocent/Zosimus decretals** — no PD English, per the Imperial scrub.
- **Theodosian Code Book 16** — Pharr 1952 is the only English. Either acquire rights or quote through Sozomen VII.4 (vendored) with the mediation flagged. A policy decision, not an acquisition.

---

## What I would do with a downloading afternoon

1. `npnf209`. Certain, cheap, named by a scrub.
2. Budge 1907. It is the one file that changes a world's shape.
3. Pliny (Melmoth/Bosanquet) and Ephrem's *Prose Refutations* (Mitchell). Both close a rowed primary that has no text at all, and Mitchell is an edition the records already cite.

Everything below that is real but incremental. And the two Tier-4 translation projects — *Verba Seniorum* and Parisot — should not start until the Article 31 review question for build-made translations has an answer, which is the same open question the Source Anchors spec parks at §5.2.

---

## Addendum, 2026-09-02 — `cappadocian` and `ijc` era, cross-checked (Sonnet build pass + Opus adversarial review + Fable deep research)

Written answering the same standing question, now that `WANTS-REGISTER.md`'s "unclassified" bucket (55 rows, current as of this date) needed sorting for the two worlds that went live since this file's original pass. Method: a first Sonnet sort, an Opus adversarial review of that sort against the live register and the vendored corpus, and a Fable research pass on the primary-text leads the sort produced — each independently checking the others' work, findings kept only where corroborated or where a direct grep against the file on disk settled it. Same standing caveat as above: this session could reach WebSearch (unlike the build sandbox), but not fetch archive.org/HathiTrust pages directly, so items below are marked by how they were confirmed.

### Free — already vendored, not yet in a source record (zero download, a records task not an acquisition task)

- **Gregory of Nazianzus, Letters 48, 49 ("The Praises of Quiet"), 50, 58 — the Sasima correspondence to Basil.** Confirmed present verbatim by direct grep against `cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml` (`div3 type="Letter"`, `n="XLVIII"/"XLIX"/"L"/"LVIII"`, lines 45734–45867+). NPNF2-7 carries a Select Letters division alongside the Select Orations division already known to be in this file — the letters division had gone unchecked.
- **Amphilochius of Iconium, extracts from the *Iambics to Seleucus*.** Confirmed present verbatim by direct grep against `cic/texts/npnf214_seven-ecumenical-councils.xml` (line 1080, "Extracts from the iambics of St. Amphilochius the bishop"). This is the only PD English of anything by Amphilochius himself located anywhere in this pass — everything else attributed to him in `cappadocian`'s records turned out on check to be Basil's letters *to* him (NPNF2-8, Epp. 188/199/217), already vendored.

### Confirmed PD, not yet downloaded — real acquisitions

| Work | Edition | Rights basis | Located at |
|---|---|---|---|
| Paulinus of Milan, *Vita Ambrosii* | Kaniecka, CUA Patristic Studies 16 (Washington, 1928) — Latin text with English translation | US publication 1928, clears the date rule; independently found by both the Opus review and the Fable research pass | archive.org/details/vitasanctiambros00paul (HathiTrust record 001639802) |
| The Liturgy of St. Basil | J.M. Neale, *The Liturgies of SS. Mark, James, Clement, Chrysostom, and Basil* (London, 1859; 2nd ed. 1868/69) | pre-1929 | archive.org/details/liturgiesofssmar00neal — supersedes an initial guess at Brightman 1896, which the Opus review could not confirm actually carries an English Basil text |
| Ammianus Marcellinus, *Res Gestae* 27.3 | C.D. Yonge trans. (Bohn, 1862; also a 1902 London printing) | pre-1929 | Gutenberg #28587; archive.org/details/ammianus-marcellinus-yonge-1902. (Sat unclassified in the register through an oversight in the first sort — flagged by the Opus review.) |
| Suetonius, *Claudius* 25.4 / *Nero* 16 | J.C. Rolfe trans., Loeb (1914) | pre-1929 | archive.org/details/suetonius-loeb |
| Odes of Solomon (42 odes) | J. Rendel Harris trans. (1909; 2nd ed. 1911) | pre-1929 | archive.org/details/TheOdesAndPsalmsOfSolomon |

### No PD path exists — correctly stays consult-only, don't re-chase

- **Theodosian Code (Pharr, 1952).** Confirmed by the Opus review: no earlier complete English translation exists (the only prior English is an unpublished 1944 Vanderbilt thesis on Book IX alone). Mommsen–Meyer (1905) remains the only PD route and it is Latin-only, matching the existing note in `Build/worlds/cappadocian/cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md`.
- **Epiphanius, *Panarion* (sections on Eustathius and the Pneumatomachians).** No PD English located, full or excerpt — even Roger Pearse's own excerpt page uses Williams's in-copyright translation.
- **Council of Nicaea (325) subscription lists, as an English list.** The PD critical edition (Gelzer/Hilgenfeld/Cuntz, *Patrum Nicaenorum nomina*, 1898) is Latin/Greek/Coptic/Syriac/Arabic/Armenian only; Hefele's PD 1871 English translation discusses the signing but does not reproduce the list; the only English lists found (fourthcentury.com, Wikipedia) are modern and not PD-declared.
- **Basil's *Small Asketikon*, Rufinus's Latin recension.** No English translation of Rufinus's Latin (or of any Syriac recension) is PD — only Silvas (2005/2013, in copyright). The already-vendored Clarke 1925 translates the Greek *Great* Asketikon, a different work, not a substitute.
- **Auxentius of Durostorum's letter on Ulfila.** Likely no clean PD English exists — Scott's *Ulfilas, Apostle of the Goths* (1885, PD, archive.org/details/ulfilasapostleof00scot) discusses it at length but neither agent could confirm it reproduces a full translation rather than a paraphrase; Heather & Matthews (1991, in copyright) is described in its own front matter as bringing most of its texts into English for the first time, which weighs against an earlier full translation existing at all.

### Needs a human to open a page — the agent sandbox couldn't confirm these

- **Gregory of Nyssa, homilies on the Forty Martyrs of Sebaste, the Song of Songs, and Ecclesiastes.** McCambly's translations, hosted at lectio-divina.org, may carry a usable public-domain-equivalent declaration ("not subject to copyright" per a search-engine snippet of the site's welcome page) — worth someone actually opening the page and reading the declaration in full before relying on it. If it holds up, this closes three real gaps at once.
- **Scott's *Ulfilas* (1885)**, on the Auxentius question above — worth a direct read to settle whether it translates the letter or only summarizes it.

### One correction to how this file's own reasoning gets carried forward

The Opus review caught that two "not a real source" calls in the first sort had the right conclusion but the wrong citation trail: Julian's punitive measures against Caesarea are independently attested in Sozomen, *HE* 5.4 (already vendored, `npnf202`), not only in the Nazianzen invectives; and the Caesarea poorhouse-hospital complex is attested in Basil's own letters (`npnf208`) and Gregory's Oration 43 (`npnf207`), not merely asserted as an undocumented institutional fact. Worth remembering if either claim is ever written into an actual `cappadocian` source record — Article 28 requires the citation trail itself to be accurate, not just the conclusion it supports.
