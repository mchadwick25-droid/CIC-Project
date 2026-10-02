# Source Identification and Discovery Methodology: How Candidate Sources Get Found Before They Are Ever Catalogued — Measured Against CiC's Step 2

Every external standard, checklist, and figure below was read or verified on 2026-07-25/26. Items I fetched and read directly carry **High** confidence. Items I confirmed only through search-result summaries, library-guide restatements, or publisher/project pages carry **Medium** or **Low**, and say so. Everything I could not verify is listed at the end under "Do not cite."

This document is deliberately upstream of doc 12 and beside doc 13. Doc 12 asks how a source is described once it is in hand. Doc 13 asks whether CiC's terms mean what the field's terms mean. This one asks the question neither covers: **how does a source become a candidate in the first place, and would a second builder find the same set?**

**CiC apparatus read in full first, not assumed:** `L3B-World-Build-Methodology\Source_Registry_Template.md` (the live governing template); `Doc_02B_Approved_Source_Database_Template_V2.md` (superseded, read for its stopping rule); `CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx` Part II and Step 2, text extracted directly; `CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx`; `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`; three real built Doc_02s (`World-Builds\01-Post-Apostolic-House-Church\CiC_W1_Doc02_Source_Ecology_FINAL.md`, 242 lines including its complete 30-entry document log; `World-Builds\Desert-Monasticism\CiC_W3_Doc02_Source_Ecology.md`; `World-Builds\Syriac-Christianity-Edessa-Nisibis\Doc_02_Source_Ecology.md` header and revision log); one real markdown registry with its own limits section (`World-Builds\Imperial-Juridical-Christianity\Source_Registry.md`); and `World-Builds\Syriac-Christianity-Edessa-Nisibis\Review-Artifacts\Doc_02_Round1_Review.md`. Verdicts are against that apparatus.

---

## Summary — the five findings that matter

**1. The comparison to doc 08 §4.1 does not hold, and the truth is more uncomfortable than the one it would give.** Retrieval volume was never measured *at all* — `k=3`/`k=2` untouched since the scaffold commit, no record anywhere. Source discovery is the opposite: it is one of the most heavily reviewed things in the project. W1's Doc_02 alone carries five numbered review rounds, two cold independent reviews, and two post-finalization reopenings, all logged. But **every finding in that entire record falls into one of three classes: registry↔narrative traceability, factual accuracy of a source already found, or derived-view bookkeeping.** Across nine review passes on one document, the record contains not one finding of the class "a relevant source was never found." The apparatus is not missing. It is aimed at a different axis, and its volume produces well-earned confidence that is nonetheless silent on coverage. **Confidence: High** (read the full document log and the Syriac Round 1 review).

**2. CiC's stopping criterion for source discovery is demand-side, and a demand-side criterion structurally cannot detect the sources that matter most.** Construction Framework Step 2 states it verbatim: "The Registry's structure, and **every source currently known to the builder**, are developed in this same Step 2 pass." The superseded V2 template was sharper and worse: complete "once every gravity, force, and lexicon term needing a specific factual anchor has at least one Native or Shared Licensed-For entry." That is a test against downstream demand. **A source that would have added a gravity, added a lexicon term, or reweighted a force cannot fail it, because it would have changed the demand it is being tested against.** The Checkpoint rule ("Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row") is a third variant of the same shape — it bounds the registry below by what the narrative happened to say. **Confidence: High** (verbatim from the extracted Framework text and the live template).

**3. CiC already wrote a real saturation criterion — one step downstream — and never applied the pattern to sources.** The Interpretive Lexicon Development Framework V2.1 states: a Candidate List is "complete enough to proceed to development when the world's Historical Gravities, primary sources, and Integrated Ecology Analysis output have all been consulted, and when **continued search produces substantially diminishing returns of genuinely new candidates rather than restatements of existing ones**." That is a textbook supply-side saturation rule. It was executed once, well, in a now-archived build (`Archive\Early-Communal-Build-History\...\communal_Doc_03_Lexicon_Candidate_List.md`: "Sources consulted to saturation for this list... Continued search was producing restatements... rather than new organizing candidates"). It appears in **none** of the six current worlds' Doc_03s, and it was never written for Step 2 at all. The project has the concept, has proved it can execute it, and has it in the wrong place. **Confidence: High.**

**4. Reproducibility is the sharpest of the three gaps, and CiC's own Confidence tier B legitimizes the non-reproducible path without recording it.** Tier B is *defined* as "Specific work/locus named, not independently re-checked this session" — which permits entering a source from recall. The Imperial-Juridical registry does exactly that, openly: nine consecutive rows (27–35) plus rows 33, 37, and 38 carry Verification Notes reading "per this build's own knowledge; not independently re-checked this session." W3's Doc_02 §7 draws the line explicitly — some scholarship is "Retained per Step 0's explicit instruction," other scholarship "Not named by Step 0 but surfaced during Doc_01's drafting." So the reproducible fraction of a CiC source set is exactly the Step 0 seed list; the rest is session-contingent. And the Syriac Round 1 review documents what recall-sourced entries produce: real scholars and real theses carrying invented bibliographic specifics — "a garbled *Antichthon* 49/2015-vs-27/1993 citation," an invented "winter 344/5" date, a 2004-for-1994 translation date. The reviewer's own summary of the pattern: "None of these are wild inventions from nothing — each rides on a real scholar and a real underlying source — but that's precisely what makes them dangerous." **Confidence: High.**

**5. The single cheapest thing CiC could do is a field-bibliography sweep, and for two of its worlds the instrument is free, online, and named by the field's own society.** Patristics has a bibliography of record and CiC has never touched it: the [Bibliographic Information Base in Patristics](https://www.bibl.ulaval.ca/bd/bibp/infoeng/) (BIBP), a free Université Laval service under the auspices of the International Association of Patristic Studies, described by NAPS as "an online searchable database of articles on patristic topics with some 30,000 entries culled from 325 academic journals," covering the 1st century to the mid-9th, extended to the 14th century for Syriac, Armenian, Georgian, Coptic, Ethiopian, Persian and Arab Christian literatures. For the Syriac world specifically, Sebastian Brock's *Syriac Studies: A Classified Bibliography* and its five-yearly continuations sit on syri.ac — a site CiC's own W1 Doc_02 source list already cites for a different purpose. A sweep against one of these, producing a short list of works the sweep surfaced that the registry did not already hold, converts "we did a research pass" into an auditable artifact. **Confidence: High** for BIBP (fetched NAPS and the Laval page); **Medium** for the Brock bibliography's continuation series.

---

## 1. Systematic review and evidence-synthesis methodology

### 1a. What PRISMA 2020 requires that CiC's Step 2 does not

[PRISMA 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) (Page et al., *BMJ* 2021, doi:10.1136/bmj.n71) is a 27-item reporting checklist plus a four-phase flow diagram. Five items bear directly here, quoted verbatim from the checklist:

| Item | Checklist text |
|---|---|
| **5. Eligibility criteria** | "Specify the inclusion and exclusion criteria for the review and how studies were grouped for the syntheses." |
| **6. Information sources** | "Specify all databases, registers, websites, organisations, reference lists and other sources searched or consulted to identify studies." |
| **7. Search strategy** | "Present the full search strategies for all databases, registers and websites, including any filters and limits used." |
| **16b. Study selection** | "Cite studies that might appear to meet the inclusion criteria, but which were excluded, and explain why they were excluded." |
| **24a. Registration** | "Provide registration information for the review, including register name and registration number, or state that the review was not registered." |

Scored honestly against CiC:

**Item 5 — ALREADY DOES THIS, at a standard above most.** The Boundary Check is a stated, binary, pre-declared inclusion criterion assessed against a fixed external reference (Doc_01's boundary), with an explicit anti-drift rule ("Boundary Status is never assessed by the date a piece of scholarship happened to be written") and a two-value Exclusion Reason vocabulary distinguishing Out-of-Boundary from Named Comparandum. This is stronger than most humanities projects can show.

**Item 16b — ALREADY DOES THIS, and better than PRISMA asks.** PRISMA asks you to cite near-miss exclusions and explain them. CiC's Named Comparandum entry type not only records them but requires a Comparandum Note stating "the specific claim, image, or reading this source must not be mistaken for being this world's own." That is a stronger artifact than an exclusion list.

**Items 6 and 7 — REAL GAP, total.** There is no field, no template section, and no builder-process step anywhere in Step 2 that names where a builder looked. The entry schema's ten fields are `#`, `Source`, `Type`, `Confidence`, `Boundary Status`, `Exclusion Reason`, `Licensed For`, `Verification Note`, `Comparandum Note`, `Added`. Not one of them can hold an information source or a search strategy. Not one of the built worlds' Doc_02s or registries names a database, catalogue, bibliography, or reference work consulted as a *finding* instrument.

The distinction that makes this precise: **CiC records the verification channel and never the discovery channel.** W1's registry row 33 (quoted in doc 12) reads "Verified this session: author, exact title, journal, year, volume, and article number all confirmed directly against publisher page." That names a publisher page as the instrument that *confirmed* a source already in hand. Nothing anywhere names the instrument that *produced* it.

**Item 24a — REAL GAP, but the mildest one.** Nothing is pre-registered. CiC's compensating strength is real: the append-only protocol, the numbered review rounds, and the document logs constitute an after-the-fact audit trail of unusual density. Pre-registration's specific value — preventing criteria from drifting to fit what was found — is partly served by the Boundary Check being fixed by Doc_01 before Step 2 opens. **Confidence: High** on all four verdicts (read the checklist items directly).

### 1b. PRISMA-S — the extension that exists specifically for this problem

[PRISMA-S](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/) (Rethlefsen, Kirtley, Waffenschmidt et al., *Systematic Reviews* 10:39, 2021, doi:10.1186/s13643-020-01542-z) is a 16-item checklist developed through a three-stage Delphi survey, consensus conference, and public review, for one purpose stated in the paper: to let "interdisciplinary authors, editors, and peer reviewers... verify that each component of a search is completely reported **and therefore reproducible**."

The 16 items, verbatim: 1 Database name · 2 Multi-database searching · 3 Study registries · 4 Online resources and browsing · 5 Citation searching · 6 Contacts · 7 Other methods · 8 Full search strategies · 9 Limits and restrictions · 10 Search filters · 11 Prior work · 12 Updates · 13 Dates of searches · 14 Peer review · 15 Total records · 16 Deduplication.

**Mapped against CiC's ten registry fields, exactly one item has any home.** Item 11 (Prior work) is partly served by Step 0's named seed scholarship and by the append-only living-document discipline. Items 1–10, 13, and 14 have no counterpart of any kind. Item 15 (Total records) is partly present as the registry's own row count, which CiC tracks carefully (W1: "Registry total: 73 rows... 46 flagged for priority review") — but that is the count of records *entered*, not identified.

Note item 14 specifically: **Peer review of the search.** CiC has an unusually strong peer-review apparatus. It has never once been pointed at the search.

**Verdict: REAL GAP on 12 of 16 items, PARTIAL on 2, ALREADY DOES THIS on 1.** This is the single most directly applicable external standard in this document. **Confidence: High** (fetched and read the item list and purpose statement).

### 1c. STARLITE — the standard actually calibrated for CiC's kind of work, and the sentence to quote

The important finding of this whole section is that PRISMA is *not* the right standard to adopt wholesale, and a real information-science paper says why. Andrew Booth, ["Brimful of STARLITE": toward standards for reporting literature searches](https://pmc.ncbi.nlm.nih.gov/articles/PMC1629442/), *Journal of the Medical Library Association* 94(4), Oct 2006, 421–429, addresses qualitative systematic reviews specifically and states:

> "It is possible for a qualitative systematic review to be explicit and systematic, while not aspiring to comprehensiveness, if it employs purposive sampling of the literature from certain disciplines or even from particular years."

And on why reporting is the load-bearing part rather than exhaustiveness:

> "one cannot automatically conclude that a poorly reported review has been badly conducted, but such poor reporting does mean that many of the intrinsic virtues of a systematic review are negated."

STARLITE's eight elements: **Sa**mpling strategy · **T**ype of study · **A**pproaches · **R**ange of years · **L**imits · **I**nclusion and exclusions · **T**erms used · **E**lectronic sources.

CiC covers exactly one of the eight — Inclusion and exclusions — and covers it excellently. The other seven have no home. But the framing matters as much as the score: **STARLITE is the standard that lets CiC say, in writing and defensibly, that its source discovery is purposive rather than comprehensive, and be held to explicitness instead of exhaustiveness.** That is a far cheaper and far more honest position than pretending toward a systematic review CiC is not doing and should not do.

**Verdict: REAL GAP on seven of eight elements — and the right standard to adopt, in preference to PRISMA proper.** **Confidence: High** (fetched and read).

### 1d. The rest of the family, for completeness

[PRISMA-ScR](https://www.acpjournals.org/doi/10.7326/M18-0850) (Tricco et al., *Annals of Internal Medicine* 169(7):467–473, 2018) is the scoping-review extension — 20 essential items plus 2 optional, developed by a 24-member expert panel. Scoping reviews exist to "map evidence on a topic and identify main concepts, theories, sources, and knowledge gaps," which is a closer genre match to Doc_02 than a systematic review is. Worth naming in a conformance statement; not worth adopting as an instrument. **Confidence: Medium** (search-result summary of the publication record, not the paper).

[Cochrane Handbook chapter 4](https://training.cochrane.org/handbook/current/chapter-04) supplies two transferable practices: review authors "should work closely, from the start of the protocol, with an experienced medical/healthcare librarian or information specialist," and the search process should be documented "in an adequate amount of detail throughout the review in order to make searches of all the databases reproducible." The specialist-from-the-start recommendation has a direct CiC analogue that costs nothing: the reviewer who currently receives a finished Doc_02 could instead be given the search plan before the pass runs. **Confidence: Medium-High** (search-result summary; chapter not fetched).

---

## 2. Citation snowballing and pearl growing

### 2a. The technique, formally described

Wohlin's [*Guidelines for snowballing in systematic literature studies and a replication in software engineering*](https://dl.acm.org/doi/10.1145/2601248.2601268) (EASE '14, doi:10.1145/2601248.2601268) is the standard formal statement, widely cited well outside software engineering. Its strategy has four named components: **(1) a start set; (2) backward snowballing** — papers referenced in the start set; **(3) identification of cardinal papers; (4) forward snowballing** — papers from external sources referencing the cardinal paper. Applied iteratively until closure.

The same technique is called **pearl growing** or **citation pearl growing** in library and information science: "taking the few results that you do have and using them to identify more relevant papers," working backward through what a known-good source cites and forward through what cites it, with the additional step of harvesting the seed document's own descriptors and title/abstract vocabulary as new search terms. **Confidence: Medium-High** for Wohlin's four components (search-result summary of the paper plus its ACM record); **Medium** for the pearl-growing formulation (library guides and a Wiley *Searching Skills Toolkit* chapter).

### 2b. What CiC does, and the one honest surprise

**CiC does backward snowballing, in fact, but never labels it and cannot count it.** The evidence is in the built worlds:

- W3's §7 records Goehring as "Not named by Step 0 but surfaced during Doc_01's drafting" — a forward or lateral find, unlabelled.
- W1's document log records the *Martyrdom of Polycarp* being caught at Doc_09, and Bradshaw being caught during a fix pass rather than by the round-1 reviewer.
- W1's §10 records a whole class of finds — the Ussher–Vossius–Daillé–Pearson–Cureton–Zahn–Lightfoot sequence in Ignatius scholarship, the Simonides forgery episode, the Bryennios manuscript's discovery circumstances — that are unmistakably the product of chaining outward from a known source's own scholarly apparatus.

That work happened. Nothing in the schema records that it happened, from which parent, or how deep it went. So the project cannot answer the most basic snowballing question — *did we snowball one level or three?* — for any world.

**Verdict: PARTIAL — the technique is in use, informally and undocumented; the discipline is absent.** **Confidence: High** (all three examples read in the source documents).

### 2c. The finding that changes the shape of the recommendation

Greenhalgh & Peacock, [*Effectiveness and efficiency of search methods in systematic reviews of complex evidence: audit of primary sources*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1283190/), *BMJ* 331(7524):1064–1065, 2005, doi:10.1136/bmj.38636.593461.68, audited how all 495 primary sources in a real systematic review of complex evidence were actually found. Verbatim:

> "30% of sources were obtained from the protocol defined at the outset"
> "Fifty one per cent were identified by 'snowballing'"
> "24% by personal knowledge or personal contacts"

Conclusion, verbatim: **"Systematic reviews of complex evidence cannot rely solely on protocol-driven search strategies."**

This is the single most important external finding in this document for CiC's morale and for the correct recommendation. **CiC's heavy reliance on builder knowledge and snowballing is not a deviation from good practice in complex literatures — it is the empirical majority of how good practice actually works.** In a field-leading review, protocol-driven searching found under a third of the sources.

What follows is not "adopt a protocol instead." It is: **the informal channels are the productive ones, so they are the ones that most need labelling.** A registry that cannot distinguish a source found in a field bibliography from one recalled by the builder cannot tell a reviewer where to concentrate scrutiny — and per the Syriac Round 1 review, the recall channel is exactly where the fabricated precision lives.

Marcia Bates's [berrypicking model](https://eric.ed.gov/?id=EJ404172) (*Online Review* 13(5), 1989) supplies the theoretical backing for the same point: real academic information-seeking is an evolving, non-linear, bit-at-a-time process built from starting, chaining, browsing, differentiating, monitoring, and extracting — not a single formulated query. CiC's iterative, append-forward registry is a berrypicking apparatus, correctly. **Confidence: High** for Greenhalgh & Peacock (fetched, quoted verbatim); **Medium** for Bates's six characteristics (search-result summary).

**Verdict on this subsection: ALREADY DOES THIS on the method, REAL GAP on the labelling — and the labelling gap is what makes the method un-auditable rather than what makes it wrong.**

---

## 3. Bibliometric and citation-network methods

### 3a. What the method does

Co-citation analysis was introduced by Small in 1973 (*Journal of the American Society for Information Science* 24(4), "Co-citation in the scientific literature: a new measure of the relationship between two documents"). The core operation: two publications are co-cited if they appear together in the reference list of one or more citing publications; the more often, the more related they are assumed to be. The standard application is to reveal "the references that are repeatedly cited together and therefore function as the field's intellectual foundations." That is, precisely, a method for asking *what does this field treat as canonical for this topic* — which is the question a coverage audit needs.

Tools that operationalize it on a live citation graph: [CitNetExplorer](https://www.citnetexplorer.nl/) (van Eck & Waltman), described in its own documentation as usable "to study the development of a research field, to delineate the literature on a research topic, and to support literature reviewing"; **Connected Papers**, which builds a visual similarity graph from a seed paper using co-citation and bibliographic coupling; and [Local Citation Network](https://localcitationnetwork.github.io/), which visualizes the cited and citing neighbourhood of a set of seed articles using OpenAlex, Semantic Scholar, Crossref, or Zotero Cita as its data source. OpenAlex is the free, open citation graph underneath most of these. **Confidence: Medium-High** (project pages and the CitNetExplorer arXiv paper record; tools not run).

### 3b. Whether this could tell CiC what a world "should" have found — the honest answer is mostly no

**Verdict: REAL GAP in principle, but a low-priority one, and CiC should be told why rather than sold a tool.**

The blocking problem is coverage of the citation graph itself. The consistent finding across the bibliometric literature is that Web of Science and Scopus focus on journals, "which is problematic in Arts and Humanities where publishing books is more frequent and more important for researchers' career than publishing articles"; that Scopus has limited humanities coverage before 1996; that both carry a documented science bias; and that "English-language journals are overrepresented to the detriment of other languages." Every one of those biases lands directly on CiC's actual bibliography. Consider the real content of W1's Doc_02: Lightfoot 1885/1889, Zahn 1873, Butler 1898, Parisot's *Patrologia Syriaca* 1894/1907, Niederwimmer's Hermeneia commentary, Lampe's *From Paul to Valentinus*, the HULCE critical edition. That is monographs, critical editions, 19th-century philology, and non-English scholarship — the four categories citation graphs index worst.

**Where it is genuinely usable, narrowly:** for the live, contested, journal-shaped debates CiC's worlds actually turn on. The Hübner/Lechner Ignatian redating dispute, the Rubenson/Gould exchange on Antony's Letters, the Shaw/Jones exchange on Tacitus, the Nag Hammadi–Pachomian proximity question, the Bagnall papyrus-redating method — these are article-level debates with real forward-citation trails, and a forward-citation pass on the seed article of each would reliably surface whether a position has been answered since. That is a targeted, cheap use worth recommending. It is not a coverage audit.

**Confidence: Medium-High** on the humanities-coverage limitation as a general finding; **High** on the characterization of CiC's own bibliography (read it).

---

## 4. How historians and patristics scholars actually build a working bibliography

This is the section where CiC's gap is most concrete, because the professional practice is not a technique — it is a *named list of instruments you are expected to have consulted*, and CiC has consulted none of them.

### 4a. The instruments, by field

**Patristics and late antiquity generally — [L'Année philologique](https://about.brepolis.net/lannee-philologique-aph-2/) (APh).** The standard bibliographical tool for classical studies, published annually in print since 1928 (first volume covering 1924–1926) and now online. Its stated scope: citations to all known scholarly work on classical antiquity published in any language, anywhere in the world, with subjects that **explicitly include early Christian texts and patristics** alongside Greek and Roman literature, history, philosophy, archaeology, religion, numismatics, papyrology, and epigraphy. It indexes journals, essay collections, festschriften, dissertations, and conference papers, gathering each year's additions from roughly 1,500 periodicals plus articles from collections. **Confidence: Medium-High** on scope and periodical count (Brepolis publisher page plus three independent university library records); **Low** on the total-entry figure — see Do not cite.

**Patristics specifically — [BIBP](https://www.bibl.ulaval.ca/bd/bibp/infoeng/), the Bibliographic Information Base in Patristics.** Free, hosted by Université Laval, under the auspices of the International Association of Patristic Studies. NAPS's own description, quoted verbatim from the [NAPS resources page](https://www.patristics.org/resources/other-resources-and-guides/): "An online searchable database of articles on patristic topics with some 30,000 entries culled from 325 academic journals." Laval's own page gives "some 29,000 notices from 350 journals" — the figures differ slightly between the two pages and should be cited as approximate. Documentary field: 1st century (excluding biblical texts) to the mid-9th; for Oriental and Slavonic Christianity to 1054; **for Syriac, Armenian, Georgian, Coptic, Ethiopian, Persian and Arab Christian literatures to the 14th century.** The predecessor of record, *Bibliographia Patristica*, ran 1956–1997 in 35 volumes and ceased with the volume covering 1988–1990 — which is precisely why BIBP matters. **Confidence: High** for the NAPS description (fetched); **Medium-High** for BIBP's own scope statement; **Medium** for the *Bibliographia Patristica* publication history.

NAPS also names, on the same page: **Bibliographia Iuris Synodalis Antiqui** ("a full database of sources and literature concerning early Christian synodal law" — directly relevant to the Imperial-Juridical world's conciliar material); **Bibliographies for Theology**, covering New Testament to Reformation "with a very substantial section on the Early Church"; **Patristische Arbeitshilfen im Internet**, a maintained link list; and **Biblindex** ("index of biblical quotations and allusions in early Christian literature" — directly relevant to any world's scriptural-engagement gravity). **Confidence: High** (fetched).

**Syriac — Brock's classified bibliography.** Sebastian Brock, *Syriac Studies: A Classified Bibliography (1960–1990)* (Kaslik: Université Saint-Esprit, 1996), continued at five-year intervals in *Parole de l'Orient*: 1991–1995 in vol. 23 (1998), 1996–2000 in vol. 29 (2004), 2001–2005 in vol. 33 (2008), 2006–2010 in vol. 38 (2013). Brock's bibliographical handouts are hosted topic-by-topic at [syri.ac/brock](https://syri.ac/brock), including sections on hagiography, liturgy, and Sasanian sources; syri.ac's own [Aphrahat page](https://syri.ac/brock/aphrahat) is already cited in doc 12's source list. The Hebrew University Center for the Study of Christianity separately maintains a [Comprehensive Bibliography on Syriac Christianity](https://csc.huji.ac.il/comprehensive-bibliography-syriac-christianity). **Confidence: Medium** on the continuation series (search-result summary of Brock's CV and journal records).

**History generally — the [AHA's *Guide to Historical Literature*](https://www.historians.org/perspectives-article/guide-to-historical-literature-soon-to-be-published/), 3rd ed. (OUP, 1995).** Roughly 27,000 annotated citations across 48 sections, chiefly works published 1961–1992, each section introduced by a brief historiographical essay, each citation carrying a critical annotation averaging about 30 words written by a specialist, assembled by over 400 scholars. It is dated, and that matters — but the *genre* is the point: an annotated, expert-selected, sectioned guide to a field's literature is a real and standard instrument for checking that you have not missed something important. **Confidence: Medium** (AHA *Perspectives* announcement plus catalog records; the Guide itself not consulted).

**The current-generation equivalent — [Oxford Bibliographies](https://www.oxfordbibliographies.com/page/about).** Per its own about page, each article combines "the best features of an annotated bibliography and a high-level encyclopedia," is written and reviewed by experts "who understand the key debates and literature," runs 50 to 100 concisely annotated entries organized into topical sections, and is **"selective rather than comprehensive."** New content is added and existing articles updated. That last property is what makes it usable as a coverage instrument: an OBO article on a topic is a defensible, dated, externally-authored answer to "what would a specialist expect a bibliography of this to contain." **Confidence: Medium** (publisher pages).

### 4b. What the practice actually is, as distinct from snowballing

The [University of Illinois guide to bibliography and historical research](https://guides.library.illinois.edu/bibliography) states the concept cleanly. An **enumerative bibliography** is "a list of documents, usually published documents like books and articles" that "will attempt to be as comprehensive as possible, **within whatever parameters established by the bibliographer**." Its four types for historical research: national, personal, corporate, and subject bibliography. And a quality bibliography "will help you understand what kinds of sources are available, but also **what kinds of sources are not available** (either because they were never preserved, or because they were never created in the first place)."

Two things follow, and they cut in opposite directions.

**First, this is the discipline's own answer to the reproducibility problem, and it is different in kind from snowballing.** Snowballing propagates outward from what you already have, so it inherits your starting bias — if your start set is what you happened to know, so is everything you reach. Consulting a *field bibliography* is a check against an externally-assembled, differently-biased inventory. The two are complements, not substitutes, which is exactly why professional practice uses both. CiC uses only the first, undocumented.

**Second, that last quoted clause is a finding in CiC's favour that should be said out loud.** "Understanding what kinds of sources are not available" is, in this discipline's own idiom, one of the two things a good bibliography does. Constitution Article 20's Missing Voices / Affirmative Duty is a *requirement* to do it, and CiC executes it visibly — W3's §6 names three axes of structural suppression (literacy/language, gender, ecclesial allegiance) and connects the third to Athanasius's simultaneous role as the Melitian schism's chief adversary; the Syriac Doc_02's own reviewer singled out its enslaved-persons entry, "no dedicated scholarly treatment or surviving voice was located... named as an unfilled gap, not glossed over with inference," as "exactly the affirmative-duty behavior the Constitution's Article 20 is meant to produce." Doc 12 established that this exceeds DACS. It also satisfies half of what the historical-bibliography tradition asks of an enumerative bibliography — the half most projects skip.

**Verdict: REAL GAP on instrument consultation — total, across all six worlds, and cheap to close. ALREADY DOES THIS on the absence-naming half of bibliographic practice, at above-field standard.** **Confidence: High** (fetched the Illinois guide; read all three worlds' Missing Voices sections and the Syriac reviewer's assessment).

### 4c. One reference apparatus doc 12 already surfaced, used for a different job

Doc 12 correctly identified the *Clavis Patrum Graecorum* as the fix for CiC's missing attribution-status field. It has a second, independent function that belongs to *this* document: the CPG "lists all their works, **whether genuine or not**, extant or not," each assigned a number. That makes it a **completeness checklist for an author's corpus** — an instrument for answering "does this world's registry hold all of Ephrem that bears on this world, or the four works the builder happened to reach for?" Not duplicative of doc 12's use; the same reference work, a different question. **Confidence: Medium** (Corpus Christianorum project pages, per doc 12's own sourcing note).

---

## 5. Coverage and completeness auditing

### 5a. PRISMA's flow diagram, and the one place CiC's exclusion record is thinner than it looks

The PRISMA 2020 flow diagram tracks: records identified · records removed as duplicates · records screened · records excluded · reports sought for retrieval · reports assessed for eligibility · reports excluded with reasons · studies included. Item 16a requires describing "the results of the search and selection process, from the number of records identified in the search to the number of studies included."

CiC keeps the *bottom* of that funnel unusually well. Exclusions are entered rather than discarded, with reasons, in an append-only record — and per doc 12's framing, the retrieval `/audit` endpoint is a positive apparatus for the runtime.

**The registry, however, is a negative apparatus, and doc 12's own distinction is the cleanest way to say why this matters.** A source that a builder considered and rejected before it earned a row leaves no trace at all. The registry's floor is "sources someone decided to enter," so *records identified* is unknowable and *records screened* is unknowable. CiC's own template says the honest version of this in its own voice: a registry "only classifies sources someone has already proposed as candidates."

**Verdict: PARTIAL — the exclusion half is strong and better than the standard asks; the identification half does not exist.** **Confidence: High.**

### 5b. Relative recall — the cheapest real coverage measurement available, and the one that yields a number

Sampson et al., [*An alternative to the hand searching gold standard: validating methodological search filters using relative recall*](https://link.springer.com/article/10.1186/1471-2288-6-33), *BMC Medical Research Methodology* 6:33, 2006. The method: assemble a gold-standard set of known-relevant items from an independent source, then compute relative recall as the number of gold-standard items your search retrieved divided by the total in the gold standard. It exists precisely as a practical substitute for exhaustive hand-searching. Reported practice treats a set on the order of 100 items as an appropriate gold standard for validating a filter; a proportionally smaller seeded set is the obvious adaptation for a single world.

**This is the direct answer to doc 08 §4.1's actual complaint.** That section's charge against retrieval was not that it was wrong but that it had never been *numbered*: "output length is one of the most carefully measured things in the system. Input retrieval volume has never been looked at once." Source discovery is in the same condition on the coverage axis. Relative recall gives it a number, from a ten-item seeded set, in one pass, without new infrastructure. **Confidence: Medium** (search-result summaries of the Sampson paper and its downstream applications; the paper not fetched).

**Verdict: REAL GAP — and the highest-value, lowest-cost item in this document.**

### 5c. PRESS — peer review of the search, which CiC is one question away from having

McGowan, Sampson, Salzwedel, Cogo, Foerster & Lefebvre, [*PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement*](https://www.jclinepi.com/article/S0895-4356(16)00058-5/fulltext), *Journal of Clinical Epidemiology*, 2016. An evidence-based guideline comprising four documents — an Evidence-Based Checklist, Recommendations for Librarian Practice, Implementation Strategies, and a Guideline Assessment Form. Its central recommendation: search strategies for knowledge syntheses "should be peer reviewed using a structured tool," on evidence that doing so "can improve the quality and comprehensiveness of the search and reduce errors."

**CiC's review apparatus is already stronger than most digital-humanities projects will ever build.** W1's Doc_02 went through five numbered rounds, two cold independent reviews with zero prior context, and two post-finalization reopenings, each documented with findings, fixes, and disagreement logs. The Syriac Doc_02 got adversarial review that caught a systematic fabricated-precision pattern. Construction Framework V7.4 added a Validation Protocol Rigor clause requiring two independent trials, fresh-context generation, and blind grading.

**And in all of it, no reviewer was ever asked whether a source was missing, and none volunteered it.** That is the whole finding. The instrument exists; it needs one question added.

**Verdict: PARTIAL — outstanding review capacity, aimed exclusively at the output rather than the search.** **Confidence: High** on CiC's review record (read the full document logs); **Medium** on PRESS's four components (search-result summary).

### 5d. Saturation, and CiC's own already-written version of it

The qualitative-research literature is where an explicit *stop looking* rule is actually theorized. Hennink & Kaiser, "Sample sizes for saturation in qualitative research: a systematic review of empirical tests," [*Social Science & Medicine* 292 (2022): 114523](https://www.sciencedirect.com/science/article/pii/S0277953621008558), systematically reviewed empirical tests of saturation and reported saturation reached at roughly 9–17 interviews or 4–8 focus group discussions depending on design. More useful than the numbers is the operational finding: the most common approach is a **pre-determined stopping criterion**, and one of the most widely applied is to conduct two or three additional units after apparent sufficiency and check whether anything new appears. **Confidence: Medium** on the specific ranges (search-result summaries of the paper, not the paper itself); **Medium-High** on the pre-determined-stopping-criterion practice.

The transferable shape is exactly three parts: *declare the criterion in advance; keep going past the point of apparent sufficiency; record that you did.*

**And CiC has already written this sentence, one step downstream.** The Interpretive Lexicon Development Framework V2.1: a Candidate List is complete "when the world's Historical Gravities, primary sources, and Integrated Ecology Analysis output have all been consulted, and when continued search produces substantially diminishing returns of genuinely new candidates rather than restatements of existing ones." Note that it has all three parts — a declared instrument set, a diminishing-returns test, and an implicit requirement to have continued past sufficiency to observe the restatements.

Its one clean execution, in the archived Early-Communal build's Doc_03: "Sources consulted to saturation for this list: Doc_02's full primary corpus (community manuals, letters, Hermas, Justin, martyr-acts, apologists, outside witnesses) and the Doc_01 preliminary-forces frame. Continued search was producing restatements (e.g., further gathering-verbs, further virtue/vice lists from the Two Ways) rather than new organizing candidates. Doc_04 gravity work may still surface additions (expected per LDF workflow); any will be logged in Doc_06's version note." That paragraph names the corpus consulted, states the diminishing-returns observation with concrete examples of what the restatements *were*, and pre-commits where later additions will be logged. It is a better saturation statement than most published qualitative studies produce.

It appears in none of the six current worlds' Doc_03s, and there has never been a Step 2 equivalent.

**Verdict: REAL GAP for Step 2; PARTIAL for the project — the criterion is written, was executed once, and is currently unexecuted everywhere.** **Confidence: High** (grepped all current Doc_03s; read the archived one and the Framework text).

### 5e. The one coverage mechanism CiC actually invented, and it should be generalized rather than replaced

W1's Doc_02 §1.8, added at Step 9 after Part VI Validation & Testing surfaced an "Author Dominance" finding, is a genuine supply-side coverage check and nothing in this document's external sources is a better fit for CiC's problem:

> "of the seven candidate gravities Doc_04 tested, three depend substantially or entirely on Ignatius as their only Asia Minor evidentiary voice... Of Doc_09's thirteen catalogued stories, two rest on Ignatius alone... and a third partially."

And its stated purpose: "a downstream reader or reviewer should be able to see, in one place, how concentrated this world's own vivid and quotable material actually is, rather than discovering it only by independently summing scattered per-document disclosures."

That is a **single-source dependency audit** — a real, quantified answer to "did our search find enough, or did we build a world on one voice?" It detects exactly the failure a coverage audit is for. Its limitations are all structural rather than conceptual: it exists in one world of six, was added post-hoc at Step 9 after a testing pass forced it, is computed by hand, and has no field or template section anywhere.

Its companion, W1 §1.7, is the same story on the exclusion side: a full world-specific rationale for excluding the Pastoral Epistles, added at Step 9 because Differentiation Testing found the exclusion had been "an unargued project-level default."

**Verdict: ALREADY DOES THIS, once, better than any external instrument surveyed — and PARTIAL as a project, because it is one world's post-hoc invention rather than a mechanism.** **Confidence: High** (read both sections).

---

## Direct answers to the three comparison questions

### Q1. Is there a stated search strategy — where did the builder look, and how would someone else know if they'd covered the same ground?

**REAL GAP, with genuine partial credit that should not be dismissed.**

**What exists.** Four things, and they are more than nothing:

1. **A topical orientation that governs scope.** Construction Framework V7.4, before Step 2: "Before source ecology work is scoped, the builder conducts preliminary forces identification... This preliminary work frames how source ecology is conducted — **which sources are sought**, what silences are expected to be meaningful." The project has explicitly thought about search framing; it framed by *topic*, not by *instrument*.
2. **A six-stream coverage frame, and it is the real asset here.** Step 2's ecology activity list requires primary voices, secondary voices, institutional, liturgical, material, and ordinary-participant evidence. This is a structured completeness frame across evidence *kinds*, and it demonstrably works: W1's §5 (Material Evidence) exists, is thorough, and concludes that the category is "thin-to-absent by design of the evidence itself, not by any failure of research" — a conclusion only reachable because a required stream forced the look. Doc 12 credited CiC's answer to IDE criterion 2.1 ("Are there principles of selection (or sampling)?") as outstanding. The refinement this document adds: CiC answers the *selection* half of 2.1 outstandingly and the *sampling frame* half not at all, because you cannot state a principle of sampling without stating the population you sampled from.
3. **A partially reproducible seed set.** Step 0 hands forward named secondary works, and W3's §7 shows them being honoured as instructions ("Retained per Step 0's explicit instruction").
4. **Post-hoc, prose, non-required descriptions of the pass.** W1: "a five-angle deep-research pass covering manuscript transmission histories, primary liturgical evidence, material culture/archaeology, the secondary scholarship landscape, and source asymmetry/outside witnesses." W3: "a targeted research pass on primary transmission history, material/papyrological evidence, and the six named secondary works." Both are useful. Both are unrequired, so they vary — five angles versus three — and neither names a single instrument.

**What does not exist.** No field, no template section, no required builder step names *where* anyone looked. Zero of STARLITE's eight elements except Inclusion/exclusions; zero of PRISMA-S items 1–10, 13, and 14. **Across six built worlds, not one Doc_02 or registry names a database, catalogue, bibliography, or reference work consulted as a discovery instrument.** The Imperial-Juridical registry's own "Notes on this Registry's own limits" section is candid and careful about five distinct classes of limitation and says nothing whatsoever about where its sources came from.

The precise formulation: **CiC records the verification channel and never the discovery channel.** A second builder given the same instructions would know which six evidence streams to fill and which Step 0 works to retain, and would have no way to know whether the first builder consulted BIBP, L'Année philologique, a university library catalogue, Google Scholar, or nothing at all.

### Q2. Is there a reproducibility property — would a second builder find roughly the same set?

**REAL GAP, and the sharpest of the three. The honest answer is: partly, and the reproducible part is small and identifiable.**

**The reproducible fraction** is the Step 0 seed list plus whatever the six-stream frame forces into view. That is real. It is also, on the evidence of W3's §7, a minority of a world's secondary scholarship.

**The non-reproducible fraction is licensed by the schema itself, and openly declared in production data.** Confidence tier B is defined as "Specific work/locus named, not independently re-checked this session" — a tier that permits entering a source from recall with no discovery record. The Imperial-Juridical registry uses it exactly that way, in the clear: nine consecutive rows (27–35) plus rows 33, 37, and 38 carry Verification Notes of the form "A standard, widely-cited reference work **per this build's own knowledge**; not independently re-checked this session" and "A well-established archaeological fact per this build's own knowledge." The registry's limits section defends this correctly — "used as named, credible references at the confidence level the Template actually defines for that condition, not overstated as freshly verified" — and it is right that the *confidence labelling* is honest. What is missing is orthogonal: the schema records how well the source was checked and never records where it came from.

**Three pieces of evidence that this is a live risk, not a theoretical one:**

- **The Syriac Round 1 review's fabricated-precision pattern**, in the reviewer's own words: "a repeated, identifiable pattern of inventing false precision on top of real sources (a fabricated 'winter 344/5' date, a wrong 1994-vs-2004 translation date, a wrong Gorgias 2005-vs-2011 date, a garbled *Antichthon* 49/2015-vs-27/1993 citation, a probable ninth-vs-tenth-century error, an unsupported 'folio loss' causal claim, an ambiguous double-use of 'Taylor')... each rides on a real scholar and a real underlying source — but that's precisely what makes them dangerous." This is the recall channel's characteristic failure signature, and a `discovery_channel` field would have told the reviewer which rows to check first.
- **The builder's own risk self-assessment was not predictive.** Same review: "The Carmina Nisibena CSCO numbers, which Doc_02 itself flags as needing verification, actually check out fine — **the self-flagged item turned out correct, while unflagged items contained the real errors.**" A structural field beats a builder's intuition about where the risk sits.
- **The one artifact that might have carried the discipline forward does not exist as a file.** W1's Doc_02 names the `cic-source-registry` skill in its "Governed by" line, and §2 attributes to it a genuinely valuable discovery discipline — "each scholar's actual center of expertise verified rather than assumed from name-recognition alone, per the `cic-source-registry` skill's explicit discipline." That discipline produced W1's best work in this whole area: the flag that Timothy D. Barnes "is not primarily an Ignatius scholar" and should be cited as a supporting voice only; the G.W.H. Lampe / Peter Lampe collision; the note that Milavec's professional identity has since shifted. **A repository-wide grep for `cic-source-registry` returns exactly one file — W1's Doc_02 itself. No skill file exists anywhere in the project.** So the single best piece of discovery discipline the project has produced is preserved only as a citation to a thing that isn't there, and W3's and IJC's Doc_02s show no equivalent scholar-expertise verification pass at all.

**The essential counterweight, and it changes the recommendation rather than softening the finding.** Greenhalgh & Peacock found 24% of a real review's 495 sources came from personal knowledge or contacts and 51% from snowballing, against 30% from the protocol, and concluded that reviews of complex evidence "cannot rely solely on protocol-driven search strategies." **CiC's reliance on builder knowledge is normal and productive.** The defect is not the channel; it is that the channel is unlabelled, which makes it un-auditable, un-weightable, and — as the Syriac review shows — the exact place where fabricated specifics enter unflagged.

### Q3. Is there a stated stopping criterion — when is source-gathering for a term or topic considered complete?

**PARTIAL. Three criteria exist. All three are demand-side or possession-side. The supply-side one, which the project has already written for a different step, is absent.**

| Criterion | Where it lives, verbatim | What it actually tests |
|---|---|---|
| **Possession** | CF Step 2 / Source Registry Template step 5: "every source currently known to the builder... are developed in this same Step 2 pass" | Whether the builder wrote down what they already knew. **Satisfiable by a builder who looked nowhere.** |
| **Downstream demand** | Doc_02B V2 step 8 (superseded): complete "once every gravity, force, and lexicon term needing a specific factual anchor has at least one Native or Shared Licensed-For entry" | Whether current downstream needs are anchored. **Structurally cannot detect a source that would have changed the needs** — added a gravity, added a term, reweighted a force. |
| **Narrative coverage** | The Checkpoint rule: "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row" | Whether every claim written is traceable. Bounds the registry below by what the narrative happened to say. |

The demand-side criterion is the one to name precisely, because it is the most sophisticated of the three and its blind spot is a logical consequence of its design rather than an oversight. **A source is judged complete when it satisfies the demand; a source that would have created new demand is invisible to the test.** That is the same class of defect doc 08 identified in the Tier-1 short-circuit — a mechanism that cannot evaluate the condition it was built to evaluate — arriving from a different direction.

**And the project already owns the missing piece.** The Lexicon Development Framework's diminishing-returns sentence is a supply-side saturation criterion with all three parts the qualitative-research literature asks for. It governs Step 3, was executed once in an archived build, and appears in no current world's Doc_03. Lifting it into Step 2 requires writing one adapted sentence.

### The doc 08 §4.1 verdict, stated plainly

**Not the same pattern, and not the more comfortable alternative.** Retrieval volume had no measurement, no record, and no reviewer. Source discovery has an extraordinary review record — nine documented passes on W1's Doc_02 alone, cold and adversarial reviewers with no prior context, independent re-verification the project lead requested and got, and a document log honest enough to record that `recalc.py`'s "0 errors" is not an arithmetic check and should not be cited as one. That is a serious apparatus.

Every finding it has ever produced is about traceability, factual accuracy of a source in hand, or bookkeeping. The one finding that came closest to coverage — the *Martyrdom of Polycarp*, surfaced at Doc_09 after having been "cited substantively and load-bearingly across Doc_01, Doc_04, Doc_05, and Doc_08" — was a **missing row for an already-used source**, not a missing source. The genuinely coverage-shaped findings (W1 §1.7 and §1.8) both arrived at Step 9, from a Validation & Testing pass, in one world, and neither became a mechanism.

So the diagnosis is not "untuned like retrieval." It is: **a strong audit instrument, pointed at an adjacent axis, generating well-earned confidence that is structurally silent about coverage.** In practical terms that is harder to fix than an unmeasured parameter, because there is no obvious hole to notice.

---

## Recommendations

### Tier 1 — three fields, into the Source Registry entry schema, at the same priority doc 12 assigned `attribution_status`

Doc 12 recommends a Tier 1 schema pass and gives the reason these belong in it rather than Tier 2: a blank is itself a defect, and the information is **unrecoverable later**. Nobody will reconstruct in six months where a source came from. Add a **Discovery Provenance** block, parallel to doc 12's proposed Description Control rename:

```
discovery_channel        field-bibliography | database-search | library-catalogue |
                         backward-snowball | forward-snowball | cited-in-another-row |
                         step0-seed-list | prior-world-build | builder-prior-knowledge |
                         reviewer-supplied | participant-question
                         [PRISMA-S items 1-7; STARLITE "Approaches"]
                         — required on every row, Native and Excluded alike

discovery_instrument     free text, the named instrument and how it was used:
                         "BIBP, searched 2026-07-26, subject=Aphrahat";
                         "Brock, Classified Bibliography 1996, Hagiography section";
                         "backward from row 10's own bibliography";
                         "builder prior knowledge, no instrument"
                         [PRISMA-S 8 "Full search strategies"]

discovery_date           ISO date [PRISMA-S 13 "Dates of searches"]
```

Three notes on the design, each load-bearing:

- **`builder-prior-knowledge` must be a neutral, stateable value, not a confession.** Greenhalgh & Peacock is the citation that makes it respectable — 24% of a field-leading review's sources came from exactly there. The point of the label is not to shame the channel; it is to let a reviewer sort by it. Per the Syriac Round 1 review, that column *is* the fabricated-precision risk map.
- **It must be required on Excluded rows too.** A Named Comparandum found by a builder who already knew the trap is a different quality of evidence from one a field bibliography surfaced, and the Comparandum Note is the most safety-critical text in the registry.
- **`discovery_channel` and `evidentiary_weight` (doc 12's Tier 1 proposal) are independent axes and should not be collapsed.** How much load a source can bear is not how it was found.

One field belongs in doc 12's **Tier 2**, alongside its proposed `relations[]` array, because it is the same graph:

```
snowball_parent_row      row id — required when discovery_channel is
                         backward-snowball, forward-snowball, or cited-in-another-row
                         [Wohlin's backward/forward snowballing]
                         Makes "how many levels did we snowball" answerable for the
                         first time; currently unanswerable for every world.
```

Follow doc 12's stated sequencing rule for a living append-only document: version the schema, mark existing rows `schema_version: 1`, and **backfill `discovery_channel` only** — coarsely, at the block level (the IJC registry's own limits section already effectively tells you that rows 27–35 are `builder-prior-knowledge`). Do not attempt to backfill `discovery_instrument` or `discovery_date`; that information is gone, and inventing it would reproduce precisely the fabricated-precision failure the Syriac review caught.

### Tier 2 — one new required Doc_02 section, on the STARLITE headings

Add a numbered section to Doc_02 — **numbered, so a reviewer can find it from the table of contents, which is the specific lesson Doc_04's template preamble already learned about verification-by-index.** Structure it on STARLITE's eight elements, because STARLITE is the standard that licenses purposive rather than comprehensive literature sampling as long as it is explicit, and that is the standard CiC should actually be held to:

| STARLITE element | What CiC's section states | Status today |
|---|---|---|
| **Sampling strategy** | Purposive, comprehensive within the six evidence streams, or selective — declared, not implied | Absent |
| **Type of study** | Which of P/S/M/L was sought through which channel | Absent |
| **Approaches** | The `discovery_channel` mix actually used, **with counts** — the row-level fields above make this a derived view, not new work | Absent |
| **Range of years** | The publication window searched for secondary scholarship. **CiC needs this more than most projects**, precisely because its Boundary Check deliberately refuses to filter by publication date — so the registry must say what window was actually searched, or a reader will assume "all of it." | Absent |
| **Limits** | **Languages of scholarship searched.** Doc 12 found no language field for the source; the sharper gap here is the language of the *search*. A Syriac world searched only in English-language scholarship has a coverage limit that nothing currently records anywhere. | Absent |
| **Inclusion/exclusions** | Boundary Check + the two-value Exclusion Reason vocabulary | **Present, best-in-class** |
| **Terms used** | The actual name forms and terms tried — **including the ones that returned nothing**, which is where the Missing Voices work and the search record meet | Absent |
| **Electronic sources** | Named instruments | Absent |

### Tier 3 — four process actions, in cost-to-benefit order

**1. A field-bibliography sweep, as a required Step 2 gate, with a named instrument per world and a one-page deliverable.** This is the cheapest closure of the largest gap in this document. Name the instrument per world family:

- Patristics and late antiquity → **BIBP** (free) and **L'Année philologique** (subscription; check institutional access)
- Syriac → **Brock's *Syriac Studies: A Classified Bibliography*** and its *Parole de l'Orient* continuations, via syri.ac; plus the Hebrew University CSC Comprehensive Bibliography
- Conciliar and juridical material → **Bibliographia Iuris Synodalis Antiqui**
- Scriptural engagement in any world → **Biblindex**
- Any world, current-scholarship check → the relevant **Oxford Bibliographies** article
- An author's corpus completeness → **CPG / CPL** numbering

Deliverable: a short list of works the sweep surfaced that the registry did *not* already hold, each dispositioned — added / Out-of-Boundary / Named Comparandum / not obtainable. **That list is CiC's PRISMA flow diagram.** It converts "we did a five-angle research pass" into an artifact a reviewer can check, and it partly closes the identification-half gap in §5a by giving the top of the funnel a trace.

Attach it to the Freeze Criteria. V7.4 already added "Source Registry complete... and the deployed Permanent Prompt's grounding-anchor paragraph verified to be drawn from it"; this is the natural companion clause, and the Freeze Criteria are where V7.4 has shown it puts the rules it means.

**2. A ten-item relative-recall test, run by the reviewer rather than the builder.** Before or during review, the reviewer names ten works a competent specialist would expect any bibliography of this world to contain, drawn from an instrument independent of the build — a standard handbook's bibliography, an Oxford Bibliographies article, a field bibliography's topic section. Then check the registry. Recall = found ÷ 10, recorded in the document log.

This is the item that answers doc 08 §4.1 in its own terms. It produces a number, from an independent gold standard, at a cost of one reviewer-hour, with no new infrastructure. Run it on the six existing worlds and there is a baseline.

**3. One added review question, on the PRESS principle.** Add to the Doc_02 review prompt, verbatim:

> *Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly.*

The evidence for why this specific wording: across W1's nine documented review passes, no reviewer was ever asked this, and none volunteered an answer. The "say so explicitly" clause matters — it converts silence from ambiguous into informative, which is the same move CiC's own Affirmative Duty makes about absent voices.

**4. Generalize W1 §1.8 from one world's post-hoc insight into a template field.** The Ignatius aggregate-dependency accounting is CiC's own invention and is a better fit for its problem than anything external surveyed here. Make it a **derived registry view**: source × downstream artifact (gravity / force / lexicon term / story), with per-source concentration counts. Doc 12 already recommends `evidentiary_weight` and a machine-readable export; this view falls out of both nearly for free. Then single-source dependency is visible by construction at Step 2 instead of discovered at Step 9 in one world of six.

### One sentence to add, verbatim, to two places

Add to the Source Registry Template's builder process (step 5) and to Construction Framework Step 2, adapted directly from the project's own Lexicon Development Framework sentence so the phrasing and the standard match across steps:

> Source gathering for this world is complete enough to proceed when the named field bibliographies for this world's period and language have been swept, every one of the six evidence streams has been searched rather than merely assessed, backward snowballing has been run on the registry's highest-weight Native rows, and continued search produces substantially diminishing returns of genuinely new candidates rather than restatements of sources already held. State that finding explicitly in Doc_02's Search Strategy section, naming what the last unproductive searches actually turned up, rather than asserting completeness. This replaces "every source currently known to the builder," which is a test of what the builder possesses rather than of what the search covered.

That single paragraph closes Q3 and half of Q1, costs one sentence in each of two documents, and uses a rule CiC wrote itself, executed once, and proved it could execute well.

### One thing not to do

**Do not adopt PRISMA proper, do not pre-register a protocol, and do not aim at comprehensiveness.** CiC is not conducting a systematic review of a bounded journal literature, and the humanities-coverage limitations in §3 mean a database-protocol approach would perform worse here than the berrypicking CiC already does. Booth's sentence is the standard to claim and the one to quote in a conformance statement: a review can be "explicit and systematic, while not aspiring to comprehensiveness, if it employs purposive sampling of the literature." Explicitness is achievable this quarter. Comprehensiveness is not achievable at all, and claiming it would be the kind of overclaim the Source Registry Template already knows how to avoid — it names its own predecessor's overclaim in its own text.

---

## Do not cite — items I could not verify directly

Listed so nobody quotes them on my authority.

- **L'Année philologique's total entry count.** A figure of "1,490,000+ entries" appears in library-guide restatements. I did not confirm it against Brepols. Cite APh's scope and its ~1,500 indexed periodicals; **do not cite an entry total.**
- **BIBP's exact size.** NAPS says "some 30,000 entries culled from 325 academic journals"; Laval's own page says "some 29,000 notices from 350 journals." Both are project-authored and they disagree. Cite as approximately 29,000–30,000 notices from roughly 325–350 journals, or quote one page and attribute it.
- **Wohlin 2014's four components** — start set, backward snowballing, cardinal papers, forward snowballing — come from search-result summaries plus the ACM record, not the paper. The component names and the ACM DOI (10.1145/2601248.2601268) are not in doubt; **do not attribute any verbatim wording to Wohlin.**
- **PRESS 2015's four constituent documents and its recommendation wording** — search-result summary of the *Journal of Clinical Epidemiology* article. The guideline exists and is correctly attributed; **do not quote its checklist items.**
- **Sampson et al. 2006 on relative recall**, and the "~100 relevant studies is an appropriate gold standard" threshold — search-result summaries. The method and the citation are solid; **treat the 100-item figure as reported practice, not as a stated requirement.**
- **Hennink & Kaiser 2022's specific saturation ranges** (9–17 interviews, 4–8 focus groups) — search-result summary, paper not read. Treat the direction as solid and the ranges as approximate. **Hennink, Kaiser & Marconi 2016 on code saturation versus meaning saturation** appeared only as a downstream reference in a search summary; **do not cite it for anything.**
- **Small 1973** and the independent co-discovery by **Marshakova-Shaikevich 1973** — well-established in the secondary literature, neither paper read. Cite the concept; **do not quote either.**
- **Bates 1989's six characteristics** (starting, chaining, browsing, differentiating, monitoring, extracting) — search-result summary of *Online Review* 13(5). **Do not quote.**
- ***Bibliographia Patristica*'s publication history** (1956–1997, 35 volumes, ceasing with the 1988–1990 volume) — one library guide. Plausible and widely repeated; **verify before citing the volume count.**
- **The AHA *Guide to Historical Literature* 3rd ed. figures** (~27,000 citations, 48 sections, 400+ scholars, 30-word average annotation) — AHA *Perspectives* announcement plus catalog records, not the Guide.
- **Cochrane Handbook chapter 4** — I did not fetch the chapter. Cite the information-specialist and search-documentation recommendations as summarized; **do not quote.**
- **Capture-recapture estimation of missed studies** exists as a coverage-audit technique in the evidence-synthesis literature. **I did not research it and make no claim about it.** Named here only as a lead for anyone extending this work.

**One internal do-not-cite, which matters more than the external ones.** The **`cic-source-registry` skill** is named in W1's Doc_02 "Governed by" line and credited there with a specific, valuable discovery discipline. A repository-wide search finds it named in that one file and finds no skill file anywhere. **Do not cite it as a live governing artifact, and do not assume any world other than W1 was built under it.** If the discipline it carried is wanted, it needs to be written into the Source Registry Template as text.

---

## Sources

**Systematic review and search reporting:** [PRISMA 2020 statement (Page et al., *BMJ* 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) · [PRISMA 2020 flow diagram guidance (UNC)](https://guides.lib.unc.edu/prisma) · [PRISMA-S (Rethlefsen et al., *Systematic Reviews* 10:39, 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/) · [PRISMA-S at Springer](https://link.springer.com/article/10.1186/s13643-020-01542-z) · [PRISMA-ScR (Tricco et al., *Ann Intern Med* 169:467–473, 2018)](https://www.acpjournals.org/doi/10.7326/M18-0850) · [Booth, "Brimful of STARLITE," *JMLA* 94(4):421–429, 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC1629442/) · [PRESS 2015 Guideline Statement (McGowan et al., *J Clin Epidemiol*)](https://www.jclinepi.com/article/S0895-4356(16)00058-5/fulltext) · [PRESS checklist summary (Karolinska)](https://kib.ki.se/en/search-evaluate/systematic-reviews/press-2015-checklist-search-strategies) · [Cochrane Handbook ch. 4, Searching for and selecting studies](https://training.cochrane.org/handbook/current/chapter-04) · [Documenting and reporting the search process (SuRe Info, York)](https://sites.google.com/york.ac.uk/sureinfo/home/documenting-and-reporting-the-search-process)

**Snowballing, pearl growing, search behaviour:** [Wohlin, Guidelines for snowballing (EASE '14)](https://dl.acm.org/doi/10.1145/2601248.2601268) · [Greenhalgh & Peacock, *BMJ* 331:1064–1065, 2005](https://pmc.ncbi.nlm.nih.gov/articles/PMC1283190/) · [Citation pearl growing (Oulu University Library)](https://libguides.oulu.fi/c.php?g=110917&p=718840) · [Citation Pearl Searching, *Searching Skills Toolkit* (Wiley)](https://onlinelibrary.wiley.com/doi/10.1002/9781118463093.ch11) · [Bates, The design of browsing and berrypicking techniques (ERIC EJ404172)](https://eric.ed.gov/?id=EJ404172)

**Bibliometrics and citation networks:** [CitNetExplorer](https://www.citnetexplorer.nl/) · [CitNetExplorer paper (van Eck & Waltman, arXiv 1404.5322)](https://arxiv.org/pdf/1404.5322) · [Local Citation Network](https://localcitationnetwork.github.io/) · [Co-citation analysis overview (E-LIS)](http://eprints.rclis.org/17524/1/Co-citation.pdf) · [Networks as interpretative frameworks: co-citation analysis in early modern letters (*DSH* 39(1))](https://academic.oup.com/dsh/article/39/1/321/7512118) · [The journal coverage of Web of Science and Scopus (*Scientometrics*)](https://link.springer.com/article/10.1007/s11192-015-1765-5) · [Web of Science Core Collection's coverage expansion: the forgotten Arts & Humanities Citation Index? (arXiv 2312.05524)](https://arxiv.org/pdf/2312.05524)

**Field bibliographies and historical bibliographic practice:** [BIBP — Bibliographic Information Base in Patristics (Université Laval)](https://www.bibl.ulaval.ca/bd/bibp/infoeng/) · [NAPS, Other Resources and Guides](https://www.patristics.org/resources/other-resources-and-guides/) · [NAPS, Bibliographic Information Base in Patristics](https://www.patristics.org/resources/bibliographic-information-base-in-patristics/) · [IAPS, Bibliographical Databases](https://aiep-iaps.org/bibliographical-databases) · [L'Année philologique (Brepolis)](https://about.brepolis.net/lannee-philologique-aph-2/) · [L'Année philologique (Yale record)](https://search.library.yale.edu/databases/6074663) · [Brock, Bibliographical Handouts (syri.ac)](https://syri.ac/brock) · [Brock, *Syriac Studies: A Classified Bibliography (1960–1990)* (syri.ac record)](https://syri.ac/bibliography/333075684) · [Comprehensive Bibliography on Syriac Christianity (Hebrew University CSC)](https://csc.huji.ac.il/comprehensive-bibliography-syriac-christianity) · [Bibliography and Historical Research (Illinois)](https://guides.library.illinois.edu/bibliography) · [AHA, Guide to Historical Literature Soon to Be Published (*Perspectives*, Nov 1994)](https://www.historians.org/perspectives-article/guide-to-historical-literature-soon-to-be-published/) · [Oxford Bibliographies, About](https://www.oxfordbibliographies.com/page/about) · [Reference Tools, History (Brown)](https://libguides.brown.edu/history/reference)

**Coverage auditing and saturation:** [Sampson et al., Validating search filters using relative recall (*BMC Med Res Methodol* 6:33, 2006)](https://link.springer.com/article/10.1186/1471-2288-6-33) · [Evaluating sensitivity of literature search strings using relative recall (*Research Synthesis Methods*)](https://www.cambridge.org/core/journals/research-synthesis-methods/article/practical-guide-to-evaluating-sensitivity-of-literature-search-strings-for-systematic-reviews-using-relative-recall/BC6A8387DAB7539D7F96EBD5965ECC32) · [Hennink & Kaiser, Sample sizes for saturation (*Soc Sci Med* 292:114523, 2022)](https://www.sciencedirect.com/science/article/pii/S0277953621008558)

**CiC internal sources read:** `L3B-World-Build-Methodology/Source_Registry_Template.md` · `L3B-World-Build-Methodology/Doc_02B_Approved_Source_Database_Template_V2.md` · `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx` (Part II; Step 2; text extracted) · `L3B-World-Build-Methodology/CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx` · `L3B-World-Build-Methodology/CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx` · `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Doc02_Source_Ecology_FINAL.md` (complete, incl. document log) · `World-Builds/Desert-Monasticism/CiC_W3_Doc02_Source_Ecology.md` · `World-Builds/Syriac-Christianity-Edessa-Nisibis/Doc_02_Source_Ecology.md` · `World-Builds/Syriac-Christianity-Edessa-Nisibis/Review-Artifacts/Doc_02_Round1_Review.md` · `World-Builds/Imperial-Juridical-Christianity/Source_Registry.md` · `Archive/Early-Communal-Build-History/Early-Communal-WorldBuilds/communal_Doc_03_Lexicon_Candidate_List.md` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/04_BuildProcess_Methodology_Mapping.md` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/08_LiveConversation_DataAccess_Failures.md` (§4.1) · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/12_Academic_Source_Organization_Standards.md`
