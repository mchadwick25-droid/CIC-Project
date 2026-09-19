# Doc_01 Review, Round 1 — Lutheran Wittenberg & Its Congregations (Atlas VI.1)

**Document under review:** `World-Builds/Lutheran-Wittenberg/witt_Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, 187 lines)
**Reviewer:** independent adversarial reviewer, cold — no drafting context. Every quotation and every claim of presence/absence below was re-checked directly against the named file, not against the document's own citation of it.
**Date:** 2026-09-15

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

17 substantial findings, 15 cosmetic. The document is honest in temperament — it discloses gaps energetically and it does not invent history. But its verification claims outrun what it actually checked in several places; it quotes a methodology document it did not quote; it attributes a Latin phrase to a vendored treatise that does not contain it; it invents a cross-reference to a sibling world's Doc_01 that says the opposite of what is attributed to it; it asserts two absences that its own vendored library contradicts; and it does not actually answer Part I's World Continuity & Distinction subsection. The pattern is not carelessness about history — it is a document that trusts the corpus-map and the sibling Step 0 documents where it claims to have trusted the primary files.

---

## SUBSTANTIAL FINDINGS

### S1 — §7 and the header: a methodology quotation attributed to a document that does not word it that way

**Where:** header line 7 ("Forces Framework V1.1 §4 (Step 1 integration point, **quoted directly** in §7 below)") and §7 line 105.

**What the document says:** *"Quoting the Forces Framework directly (V1.1 §4, Step 1): \"What generated this world? What larger world was it embedded in? What was it responding to? What was it refusing?\""*

**What I found when I opened the Forces Framework.** `CiC_L3A_Forces_Framework_V1.1.docx`, §4, Step 1 (paragraph 163) reads, in full:

> "Forces analysis begins here. Before source ecology work is scoped, the builder conducts preliminary forces identification: what generated this world, what larger world was it embedded in, what was it responding to, what was it refusing? This preliminary work is not the complete forces analysis — it is the frame that governs how source ecology work is conducted. Without preliminary forces identification, source ecology work lacks the orientation it needs to recognize which sources speak to forces and which are silent about them."

Four lowercase clauses inside one question, separated by commas. The four-separate-capitalised-questions form the document prints verbatim is the **Construction Framework V7.4 Part I**, paragraph 124:

> "Before source ecology work is scoped, the builder conducts preliminary forces identification. What generated this world? What larger world was it embedded in? What was it responding to? What was it refusing? This preliminary work frames how source ecology is conducted — which sources are sought, what silences are expected to be meaningful."

The content is equivalent; the attribution is not. The document claims twice to be quoting the Forces Framework "directly" and prints the Construction Framework's wording instead. Under this project's own rule that every quotation is re-verified verbatim against the cited source — and given its documented history of a fabricated, inverted methodology quotation — this is not a citation-tidiness matter. Fix by either quoting FF V1.1 §4 accurately or citing the Construction Framework Part I as the source of the four-question form.

### S2 — §4: the document contradicts itself about whether the catechisms are vendored

**Where:** §4, "Linguistic" paragraph, line 63.

**What the document says:** "Luther's own catechisms and hymns **(not yet vendored, see §10)** were written in German specifically so that lay households, not only clergy, could use them."

Both catechisms **are** vendored. The document's own header (line 11) lists `luther_large-catechism_bente-dau1921.txt` and `luther_small-catechism_smith1994.txt` among the six files it read directly. §2.2 says "the Small and Large Catechisms, **both vendored here**." §10 gives word counts for both (48,425 and 4,360). §1 cites "the Small Catechism's own household framing." And §10 does not say the catechisms are unvendored — it names "catechism companions, hymns, *Table Talk*, and *Bondage of the Will*" as still-unvendored, so the "see §10" pointer does not support the parenthetical either. The parenthetical presumably meant "hymns" alone; as written it is a flat self-contradiction in the section where the document makes its strongest linguistic claim.

### S3 — §3: a [Documented] tag resting on a verification claim that four of the six files refute

**Where:** §3, line 53.

**What the document says:** "**Core:** Wittenberg, in Electoral Saxony... **[Documented]**, confirmed directly by **every vendored file's own place of composition or address**."

**What I found.** Case-insensitive counts of "Wittenberg" across the six files:

| file | hits | what they are |
|---|---|---|
| `luther_works-v1-selected_jacobs-spaeth1915.txt` | 34 | genuine — e.g. "From Wittenberg on the Vigil of All Saints, MDXVII" |
| `luther_works-v2-selected_jacobs-spaeth1916.txt` | 35 | genuine |
| `luther_large-catechism_bente-dau1921.txt` | 1 | "This text was converted to ASCII format for **Project Wittenberg** by..." |
| `melanchthon_apology-augsburg-confession_bente-dau1921.txt` | 1 | "This text was converted to ASCII format for **Project Wittenberg** by..." |
| `luther_small-catechism_smith1994.txt` | 5 | all "Project Wittenberg" — the modern digitiser, "Fort Wayne, Indiana: Project Wittenberg, 2004" |
| `melanchthon_augsburg-confession_anon-pg275.txt` | **0** | none |

Three of the six files mention Wittenberg only as a 20th/21st-century digitisation project in Indiana. The sixth does not mention it at all — its own title page reads "Which Was Submitted to His Imperial Majesty Charles V **At the Diet of Augsburg** in the Year 1530." The claim as written is false, and it is contradicted two paragraphs later by §3's own note that the Diet of Augsburg "took place in Augsburg, not Wittenberg." The underlying historical claim (Wittenberg is the core) is fine and is genuinely Documented; the sentence asserting how it was verified is not. Rewrite it to say the two Holman volumes confirm it directly and the confessional files do not bear on it.

### S4 — §1: a Latin phrase in quotation marks attributed to a vendored treatise that does not contain it

**Where:** §1, second bullet, line 20.

**What the document says:** "justification by faith apart from meritorious works... (*A Treatise on Christian Liberty*'s \"simul justus et peccator\" paradox; Augsburg Confession Article IV)".

**What I found.** `grep -in "simul just\|simul iustus\|peccator"` across all six vendored files returns exactly two hits, both in Latin footnote apparatus in Volume I and neither related: line 886 ("*suorum concedemus et concedimus veniam peccatorum*") and line 3106 ("*Instructio pro confessione peccatorum abbrevianda...*"). The phrase "simul justus et peccator" occurs **nowhere** in this world's vendored library, and it certainly does not occur in *A Treatise on Christian Liberty*.

Where it actually comes from: the corpus-map's own editorial note for that work — "the 'simul justus et peccator' freedom/bondage paradox stated in Luther's own words." That is a modern cataloguer's label, not a quotation from the 1520 treatise. The document has taken a phrase in quotation marks from a generated index file and presented it as the treatise's own. (Historically the formula belongs to Luther's Romans lectures and *Against Latomus*, not the *Freedom of a Christian*.) Either drop the quotation marks and the attribution, or replace it with something the treatise actually says.

### S5 — §6: a cross-reference to a sibling Doc_01 that says the opposite of what is attributed to it

**Where:** §6, line 97.

**What the document says:** "A second candidate this document also considered and rejects as a strand, **for the same reason as Gallic Monastic-Ascetic Christianity's own Doc_01 rejected a comparable temptation**: the 1522 Wittenberg unrest..."

**What I found in `World-Builds/Gallic-Monastic-Ascetic-Christianity/gallic_Doc01_World_Identification.md` §6.** It rejects nothing. It records:

> "**Finding, corrected from the first draft (Round 1 finding S14): provisionally strand-singular, per the Framework's own stated default, pending Doc_04.**"

and then explicitly holds its candidate division (the Loire node vs. the Lérins–Marseilles southern pair) **open**, laying out evidence in two labelled directions — "**For treating this as one world (or one world with two strands)**" and "**For treating this as a lineage of two**" — and closing:

> "If Doc_04 finds these do not hold across both nodes, or finds the absence of a documented Tours-to-south link decisive, this section's framing should be read as the record of what was tested and why it remained open at Doc_01 — not an argument this document is trying to win in advance."

There is no "comparable temptation" rejected there, and certainly not on the ground Wittenberg's document claims (an internal disagreement that "resolves within the window... a transition event, not a strand"). This is an invented precedent, dressed as a methodological alignment. Remove it or replace it with the precedent that actually exists.

### S6 — §6: the strand finding's hedge contradicts the Framework it invokes, and drops the correction its own model precedent carries

**Where:** §6, lines 93 and 99.

The document records "provisionally strand-singular, per the Framework's own stated default... **pending whatever Doc_04's cross-strand gravity testing may find**."

Construction Framework Part I, paragraph 116: "**This determination is made at Step 1 and governs all subsequent work.** Strand attribution applies only where Step 1 established strands." Paragraph 122 gives Step 4 *cross-strand gravity testing* across already-confirmed strands — not authority to reopen whether strands exist.

The Gallic Doc_01 the document points to at S5 makes exactly this correction on its own record, as a Round 2 finding:

> "**Methodological note (Round 2 finding N11):** the Framework gives Step 4 cross-strand *gravity testing*, not explicit authority to revise a Step 1 strand finding — so this status is delivered as this document's own finding under the Framework's own default rule, not withheld as 'not actually made'..."

Wittenberg's Doc_01 reproduces the precedent's hedge and omits the correction that review forced onto it. There is also an internal tension: §6 rejects both candidate strands flatly ("**This is not a strand** in Article 21's own sense"; "a transition event, not a strand") while labelling the overall finding "provisional." Either the evidence settles it or it doesn't.

### S7 — §8: Part I's World Continuity & Distinction subsection is not actually answered

**Where:** §8 as a whole, lines 119–143.

Construction Framework Part I (paragraphs 128–140) defines this subsection around five questions:

- What does this world inherit from prior worlds?
- What does it transmit to subsequent worlds?
- What shared material functions differently within this ecology than in adjacent ecologies?
- Where does continuity mask genuine ecological change?
- Where does apparent discontinuity mask deeper structural continuity?

— with the instruction "The goal is neither artificial disconnection nor differentiation collapse. Shared inheritance should be acknowledged. Distinctive ecological function should be demonstrated."

§8 is six neighbour-comparison subsections (VI.2, VI.3, VI.22, VI.11, V.5, the Augustinian Hermits). Inheritance is touched once, at §8.6. **Transmission to subsequent worlds is absent entirely** — and the census supplies material for it in a field the document otherwise mines heavily (`legacy`: "an ongoing communion of tens of millions... congregational hymn-singing in the local language, the small catechism learned by heart at home, and a tradition of church music that runs from Luther's own tunes through to Bach"). **Shared-material-functioning-differently, continuity-masking-change, and discontinuity-masking-continuity are all absent.** §8.1 comes closest ("share the same generating refusal of papal authority and much of the same early theological vocabulary") but does not develop it.

This is the one required Part I subsection where the document substitutes a different structure for the one the Framework specifies, and loses four of five questions doing it.

### S8 — §2.2: a truncated Step 0 quotation that manufactures the tension the section then resolves

**Where:** §2.2, line 36.

**What the document says:** "Step 0's own §1 candidate-identification line describes the window as running through \"the consolidation of the Lutheran territorial churches after the **Peace of Augsburg (1555)**.\"" — introduced under the heading "**The real alternative, named rather than smoothed over.**"

**What Step 0 §1 actually says** (`Step0_Movement_Scope_Confirmation.md` line 15):

> "Atlas VI.1, 'Lutheran Wittenberg & Its Congregations,' **1517–1580**, Saxony then Northern Europe. Martin Luther and Philip Melanchthon, and the first generation of the Wittenberg reform: the 95 Theses (1517) through the consolidation of the Lutheran territorial churches after the Peace of Augsburg (1555) **and into the next generation**."

Two things are cut. The clause "and into the next generation," which is precisely what carries Step 0 past 1555; and the fact that the same sentence opens by stating the window as **1517–1580**. Step 0 does not offer 1555 as a closing candidate at all — it gives 1580 and passes through 1555 on the way. The document's "real alternative, named rather than smoothed over" framing is generated by the truncation, then half-defused three lines later ("the census's own 1580 figure is not in tension with either"). The substantive point — that 1555 is a real internal-transition marker Doc_02/Doc_04 should carry — is worth keeping; the claim that Step 0 pointed at 1555 as an ending is not.

### S9 — §8.3: a binding obligation attributed to both worlds that the cited document binds on one

**Where:** §8.3, line 131.

**What the document says:** "...and (§4 item 5) names this relationship **binding on both worlds' Doc_01s** as \"primary structural material, not incidental.\" ... Doc_02 for both worlds should expect to cite each other as primary named rivals, **per both Step 0 documents' own instruction**."

**What the Tridentine Step 0 §4 item 5 actually says:**

> "**Direct doctrinal engagement with Lutheran Wittenberg and the Reformed cities (binding on Doc_01, cross-referenced with VI.1's and VI.2's own Step 0 documents).** **This candidate's own Doc_01** should treat those two relationships as primary structural material, **not incidental cross-references**."

It binds *its own* Doc_01, cross-referencing VI.1's and VI.2's Step 0 documents. It does not place an obligation on Wittenberg's Doc_01. Two further slips in one sentence: the quotation is truncated ("not incidental." for "not incidental cross-references"), and the Doc_02 instruction is **only** in VI.1's own Step 0 (§2 A3: "Doc_02 for both worlds should expect to cite each other as the primary named rival") — the Tridentine Step 0 says nothing about Doc_02 here, so "per both Step 0 documents' own instruction" is wrong.

### S10 — §5 and §11.3: an asserted absence that a vendored file directly fills

**Where:** §5, "Has worship changed substantially?", line 83; repeated at §11 item 3, line 172.

**What the document says:** "...the actual reformed liturgical practice as lived (German-language services, congregational hymn-singing) **rests on texts — hymns, service orders — not yet vendored (§10)**. Doc_05 should treat this as argued-for-in-doctrine but **not yet demonstrated-in-lived-practice from this world's own current library**."

**What I found in `melanchthon_augsburg-confession_anon-pg275.txt`, Article XXIV (line 785 ff.)** — a vendored file, and a first-person description of practice as actually conducted in 1530:

> "Falsely are our churches accused of abolishing the Mass; for the Mass is retained among us, and celebrated with the highest reverence. Nearly all the usual ceremonies are also preserved, save that the parts sung in Latin are **interspersed here and there with German hymns, which have been added to teach the people**... **The people are accustomed to partake of the Sacrament together**, if any be fit for it, and this also increases the reverence and devotion of public worship. For **none are admitted except they be first examined**. The people are also advised concerning the dignity and use of the Sacrament..."

This is congregational German hymn-singing, communion practice, and pre-communion examination, described by the movement about itself, in a file the document counted the words of. The claim of absence is wrong as stated. It can be narrowed honestly — no service order or hymn text is vendored, and Article XXIV is an apologetic self-description addressed to an emperor, not a neutral record — but it cannot stand as "not yet demonstrated-in-lived-practice from this world's own current library."

### S11 — §4: a second asserted absence overstated against the vendored Large Catechism

**Where:** §4, "Social" paragraph, line 65.

**What the document says:** "This document does not know, from what it has actually read, how well Wittenberg's doctrine reached an ordinary Saxon villager by, say, 1550 — **only that** the project's own census entry states this is a live, documented, and disillusioning question..."

**What I found in `luther_large-catechism_bente-dau1921.txt`, Luther's own preface (lines 42–110)** — 1529, Saxony, the founder's own first-hand assessment of reception:

> "...we see to our sorrow that many pastors and preachers are very negligent in this, and slight both their office and this teaching... For, alas! as it is, **the common people regard the Gospel altogether too lightly, and we accomplish nothing extraordinary even though we use all diligence**... Yea, even among the nobility there may be found some louts and scrimps, who declare that there is no longer any need either of pastors or preachers..."

The narrower claims in the same paragraph **do** hold — see WHAT HELD UP below — but "only that the census states" is false: the document holds primary testimony on the reception question from the founder's own side and did not use it. This matters beyond tidiness, because reception-versus-ideal is the census's stated reason this world is interesting, and §10 calls it "the single most consequential open sourcing question this world's Doc_02 faces."

### S12 — Confidence vocabulary is applied to five claims out of dozens, and never at the level the evidence calls for

**Where:** whole document.

Construction Framework paragraph 192: "Evidence should be evaluated using the fixed five-level confidence vocabulary from Constitution Article 17. **All reconstruction uses this vocabulary consistently.**"

Tag counts:

| document | Documented | Widely Accepted | Dominant Modern Recon. | Contested | Inferential |
|---|---|---|---|---|---|
| `gallic_Doc01_World_Identification.md` | 4 | 7 | 0 | 5 | 3 |
| `hal_Doc_01_World_Identification...md` | 3 | 7 | 4 | 4 | 2 |
| **this document** | **3** | **2** | **0** | **0** | **0** |

Two of five levels, five tags total. The gap is not cosmetic, because the document contains a textbook **Contested** claim and leaves it untagged: §4's "live scholarly debate (Strauss's 'failure' reading versus Scribner's and Kittelson's critiques)" is exactly what the Framework defines as Contested — "Live scholarly disagreement; no dominant position... Carry the tension; do not resolve it." Also untagged: all six World Separation Criteria answers (§5), all four candidate gravities (§1), the whole of §7, and every historical assertion in §2.3 (the Wartburg/Karlstadt sequence, the post-1525 settlement with princes).

### S13 — §8.4: a sibling Step 0 states the opposite relationship and is not engaged

**Where:** §8.4, line 135.

**What the document says:** "Unlike this world's relationship to the three movements above, **this is not a rival-by-direct-argument relationship**... This document finds no documented direct link and does not manufacture one."

**What `World-Builds/Society-of-Jesus/Step0_Movement_Scope_Confirmation.md` §2 A3 says:**

> "**The direct, real rival relationship in this batch is Lutheran Wittenberg and the Reformed cities** — the Jesuits were founded explicitly within, and as a response to, the same crisis those two candidates answer from the opposite direction."

That document exists in the repository, was drafted the same day as the three the document did read, and states the relationship from the other side in terms flatly contrary to §8.4's. The document's own posture elsewhere (§8.2: "Doc_02 should not let this world's own account of its formation stand in for the Anabaptists' own account") is the right one and is not applied here. Either consult VI.11's Step 0 and engage it, or say plainly that §8.4 rests on this world's own Step 0 B3 and the census alone and that VI.11's own document has not been read.

### S14 — §1: an addressee in the evidenced list that no vendored work has

**Where:** §1, third bullet, line 21.

**What the document says:** "addressed to specific named readers (the Archbishop of Mainz in 1517, the German nobility in 1520, Pope Leo X, **brother-monks** and princes)".

**What I found.** The addressees actually present in the two Holman volumes: Albrecht of Magdeburg and Mainz (the 1517 letter); Pope Leo X (with *Christian Liberty*); "Martin Luther, Augustinian, **to his friend, Herman Tulich**" (*Babylonian Captivity*, line 6477); Nicholas von Amsdorf (*Open Letter to the Christian Nobility*, per the volume's own introduction and the corpus-map); "To the Most Illustrious Prince and Lord, **Frederick**, Duke of..." (*Fourteen of Consolation*, line 4244); "To the Illustrious, High-born Prince and Lord, **John**, Duke of..." (*Treatise on Good Works*, line 6722). Princes, yes. No vendored work is addressed to monks. Drop "brother-monks" or replace it with a real addressee.

### S15 — §10: an unrecorded acquisition narrative that conflicts with the dossier it cites

**Where:** §10, line 163.

**What the document says:** "**The Bondage of the Will (Luther, trans. Cole, 1823)** — named by Step 0's own dossier as a strong lead, not vendored this pass. **Two archive.org identifiers were tried and both were unsatisfactory (one lending-restricted, one an unverified, messy OCR scan); a third candidate (`martinlutheronb00colegoog`) was named but not tried.**"

**What the dossier says** (`world-build-docs/_cross-world/dossiers/lutheran-wittenberg-and-its-congregations_Source_Readiness_Dossier.md`, line 28):

> "| The Bondage of the Will | Luther | Henry Cole | 1823 | archive.org `bondagewill00colegoog`, `martinlutheronb00colegoog`, `bondageofwill00mart` (three separate scans) | pd-us-by-date | **direct fetch, 2026-09-15** |"

All three identifiers are recorded as host-verified by direct fetch. The document asserts a contrary finding about two of them, that finding exists nowhere on the record, and it does not disclose that it is in tension with the dossier's own verification status. Either record the attempts properly (with which identifiers, and what was actually seen) and flag the dossier row as needing correction, or state the gap without the unverifiable narrative. Same bullet, separate gap: §10's still-unvendored list ("catechism companions, hymns, *Table Talk*, and *Bondage of the Will*") omits the **four remaining PD Philadelphia Edition volumes** Step 0 B1 names as host-verified — a larger sourcing gap than any item actually listed.

### S16 — §10/§12: "confirms Step 0's floor-clearance claim in full" is more than Article III says

**Where:** §10, line 164; repeated in §12's verification list, line 184.

**What the document says:** "Article III's Christology was likewise read directly and **confirms Step 0's floor-clearance claim in full**."

**Step 0's Article III claim** (§2 A1): "Article III affirms Christ's full deity and full humanity, virgin birth, true death and burial, descent, bodily resurrection, ascension, session at the Father's right hand, and return to judge — **matching all five of Article 4's commitments above, point for point**."

**What Article III actually contains** (`melanchthon_augsburg-confession_anon-pg275.txt`, line 208 ff.): the Christological list is all there and accurate. But commitment (1) — "One God, the Father, the Almighty, maker of heaven and earth" — is not in Article III; it is in Article I ("the Maker and Preserver of all things, visible and invisible"). Commitment (5) — "The Holy Spirit as Lord and giver of life, **worshiped and glorified together with the Father and the Son**" — is not in Article III either; Article III mentions the Spirit only as sent into believers' hearts, and the co-equality claim sits in Article I's three-coeternal-persons language. The floor clears comfortably on Articles I **and** III together. Step 0's "point for point" on Article III alone is an overstatement, and the document's "in full" endorses it as independently verified. Say I+III together, and note that Step 0's Article III claim was slightly too broad — that is a genuine, reportable verification result rather than a rubber stamp.

### S17 — §7 does not do the job the Forces Framework's Step 1 integration point exists to do

**Where:** §7, closing line 115.

Both governing documents define this section's **output** as an orientation for Step 2. Forces Framework §4, Step 1: "it is the frame that governs how source ecology work is conducted. **Without preliminary forces identification, source ecology work lacks the orientation it needs to recognize which sources speak to forces and which are silent about them.** Output: Preliminary forces identification (governs Step 2 scope)." Construction Framework para 124: "This preliminary work frames how source ecology is conducted — **which sources are sought, what silences are expected to be meaningful**."

The four forces themselves are substantive and well argued — this is not a perfunctory section. But §7 closes with "This preliminary work frames, but does not substitute for, the complete forces analysis at Doc_08" and stops. It never states which sources Doc_02 should therefore seek, or which silences should be read as meaningful. §10 and §11 carry sourcing gaps forward, but as an inventory of what is missing, not as forces-derived expectations. One paragraph connecting §7's four findings to Doc_02's search would close this.

---

## COSMETIC FINDINGS

**C1 — §2.1, off-by-one line citation.** "dated in the file itself \"OCTOBER 31, 1517\" (line 993)". It is at **line 992** of `luther_works-v1-selected_jacobs-spaeth1915.txt`.

**C2 — §2.1, the line-436 parenthetical is garbled.** "(marked in the file at line 436 as a heading reached earlier in a different arrangement of the same volume's front matter)". Line 436 is not front matter in a different arrangement; it is the unit's own section title page — "THE DISPUTATION OF DOCTOR MARTIN LUTHER / ON THE POWER AND EFFICACY OF INDULGENCES / (THE NINETY-FIVE THESES) / 1517 / TOGETHER WITH THREE LETTERS EXPLANATORY OF THE THESES" — followed immediately by the editors' INTRODUCTION, then the letter (I, line 990 ff.) and the Theses (II, line 1138 ff.). Describe it as the section title; the sentence currently confuses a reader who goes to check it.

**C3 — work title follows the corpus-map rather than the file.** The document cites "*To the Papacy at Rome*" four times (§1, §5, §7). Volume I's own contents page and section heading read "**THE PAPACY AT ROME** / AN ANSWER TO THE CELEBRATED ROMANIST AT LEIPZIG" (line 12211). Minor, but it is a tell that the citation came from the index rather than the text.

**C4 — §8.1, wrong census id.** The document writes `the-reformed-cities`. The census id is `the-reformed-cities-zurich-and-geneva`. Ids are the join key for corpus-map filenames; get it right.

**C5 — §7, quotation placed in the wrong section of the Reformed Step 0.** "the Reformed cities' own sibling Step 0 (§2 A3, \"the Marburg break with Luther\")". That exact string is §4 **item 5**'s heading. §2 A3 reads "the Marburg Colloquy (1529) Eucharistic break with Luther, from this movement's own side."

**C6 — §8.2, ellipsis hides a qualifier.** The Anabaptist Step 0 §2 A3 reads "...both Lutheran Wittenberg and the Reformed cities **(both in this batch,** from the establishment side**)** and, more distantly, the Tridentine Church." The document's ellipsis removes the opening parenthesis and drops the closing one, leaving unbalanced punctuation in the quotation.

**C7 — §6, strand definition quoted under the wrong authority and altered.** Attributed to "Article 21's own sense." Constitution V2.2 Article 21 reads "Strand is defined as **a meaningfully distinct pattern** of formation emphasis, practice, authority structure, or ecological orientation within a single world, **not merely a variation in detail**." The plural "patterns" form the document prints is the Construction Framework's (para 115). The dropped clause is the one that best supports the document's own argument.

**C8 — §10, "correcting Step 0 §3 B1's own disclosed rough estimate."** B1 gives no numeric estimate to correct — only a qualitative comparison ("on the order of the merged Latin Apologists' 1.19M words once fully vendored, though that comparison is qualitative, not measured"). Also worth noting: 488,093 raw words is under half that figure, for a much smaller slice of the corpus, so "confirms Step 0's own qualitative read" needs the scope difference stated.

**C9 — §4, the Augsburg Confession called a "confessional Latin document."** The vendored file's own preface (lines 76 and 88) says the estates were to "set forth and submit their opinions and judgments in **the German and the Latin language**" and "to wit, **in Latin and German**." It was submitted in both. The document asserts this in the same breath as "the vendored corpus itself shows this directly."

**C10 — §8.5, dropped "c."** Lollardy's window is "**c.** 1380-1520" in both the census and that world's own Step 0. The document prints "1380–1520."

**C11 — header, file-code asserted without a record.** The document opens with "file-code `witt`." Step 0 records "**World file-code: none assigned — not yet selected**," and the G0 note does not assign one. I found no registry entry assigning it. Small, but a build-wide identifier should be recorded somewhere before a document treats it as settled.

**C12 — §1's third bullet answers part of Framework para 92.** The Framework asks for "recurring patterns of **worship**, formation, interpretation, **belonging**, and authority." §1 covers doctrine-in-writing, confessional self-definition, and reception-checking; worship and belonging are not addressed there. (Worship gets a partial answer at §5; belonging does not appear.)

**C13 — §8.4, unsourced additions, and a silent Step 0 correction.** "founded in 1540... but in **Rome and Paris**" and "**Peter Canisius's later mission**" carry no source and no confidence tag. Separately, the document is **right** and Step 0 is **wrong** on a point it passes over silently: Step 0 B3 says the Society was "founded 1540, **a full generation after Luther's own death in 1546**" — 1540 precedes 1546. The document quietly states the correct relation ("during Luther's own lifetime") without flagging that it is correcting Step 0. The G0 note (line 15) asks for exactly this kind of finding to be reported plainly, and §12's list of what was verified against Step 0 does not include it.

**C14 — §10, wrong obstacle named for the women's voices.** The document flags the access problem only for Sehling ("mostly untranslated German/archival"). The actual barrier for Grumbach (Matheson, T&T Clark, **1995**) and Zell (McKee, Chicago, **2006**) is that both are in-copyright modern editions — which is the thing Doc_02 will have to solve. The census also records "Both verified this session," which the document does not carry forward.

**C15 — §4 census quotation attributed to the wrong field.** "the census's own `why` field names this directly (\"put the Bible, a catechism and a hymnbook into ordinary German households\")". The phrase is real but sits in `longDescription`, not `why`. The `why` field contains no such wording.

---

## WHAT HELD UP

These I checked myself, directly, and found accurate. Do not re-litigate them in the revision round.

**Word counts (§10) — exact.** `wc -w` on all six files returns 141,744 / 167,827 / 48,425 / 4,360 / 111,117 / 14,620, total **488,093**. Every figure matches, and the disclosure that this is a raw whole-file count including editorial apparatus, not a div2-boundary extraction, is correct and appropriately hedged.

**The 1517 letter (§2.1, §7) — accurate in substance.** The salutation reads "To the Most Reverend Father in Christ and Most Illustrious Lord, **Albrecht of Magdeburg and Mainz**, Archbishop and Primate of the Church, Margrave of Brandenburg" (line 995); the editorial dateline is "OCTOBER 31, 1517" and Luther's own subscription is "From Wittenberg on the Vigil of All Saints, MDXVII" (line 1091), which agree. The Theses do follow immediately, as section II beginning line 1138. The characterisation as "a bounded, respectful protest to a specific archbishop about a specific abuse" is right, and the enclosure reading is supported by the letter's own closing: "**If it please the Most Reverend Father he may see these my Disputations**, and learn how doubtful a thing is the opinion of indulgences."

**Augsburg Confession Article I (§10) — correct, and the correction of Step 0 is real.** The article names "the Manichaeans... also the Valentinians, Arians, Eunomians, Mohammedans, and all such. They condemn also the Samosatenes, old and new." Step 0's "the Arians, Manichaeans, and other ancient deniers" does compress it. Article IV likewise checks out as the justification article ("men cannot be justified before God by their own strength, merits, or works, but are freely justified for Christ's sake, through faith").

**Sacraments reduced from seven to two or three (§1, §5) — verified in the text, both halves.** *Babylonian Captivity*: "At the outset I must deny that there are seven sacraments, and hold for the present to but three--baptism, penance and the bread" (line 6695), and later "strictly speaking, but two sacraments in the Church of God--baptism and bread" (line 10362). The "two or three" formulation is exactly right.

**Marburg is genuinely unsourceable from this library (§7, §11.1).** "Marburg" and "Zwingli" each return **zero** hits across all six vendored files. The document's refusal to overstate here is correct. (Constructive note, not a finding: Augsburg Confession Article X *is* vendored and states the Lutheran position that broke the fellowship — "the Body and Blood of Christ are truly present, and are distributed to those who eat the Supper of the Lord; and they reject those that teach otherwise." §7 and §11.1 could cite it without overclaiming anything about the Colloquy itself.)

**The visitation records are genuinely absent (§4, §10).** "visitor" and "visitation" return zero hits in both catechisms and in the Apology — Luther's Small Catechism preface, with its famous "when I, too, was a visitor" line, is **not** in the Smith translation as vendored. The document's claim that it has nothing in the visitation record's own words, and nothing in an ordinary believer's own voice, holds. (S11 concerns only the broader "does not know... only that the census states" formulation.)

**The Eight Wittenberg Sermons (§2.3) — quotation and framing both verified.** The corpus-map note is transcribed verbatim, and the file's own editorial introduction corroborates it independently: Wartburg from 4 May 1521; return to Wittenberg 6 March 1522; sermons from Sunday 9 March "and the seven days following"; "Melanchthon, ardent in the beginning, could not hold back the radical procedure of **Carlstadt** and Zwilling"; "**Carlstadt was silenced**, the city council made acknowledgment to Luther... and Wittenberg bowed to law and order."

**Both rights flags (§10) — exactly as carried.** `REGISTRY.yaml` and the corpus-map both record the Small Catechism as a 1994/2002/2004 Robert E. Smith translation whose PD basis "rests on the translator's own release for free distribution via Project Wittenberg," not the by-date rule; and the Augsburg Confession as "TRANSLATOR FLAGGED, not closed... NOT confirmed to be the same Bente/Dau Concordia Triglotta translation as the companion Apology... despite a stylistic resemblance." The document restates both accurately and for the right reason.

**Census quotations (§1, §4, §5, §8) — verbatim.** "Founder corpus kept distinct from the congregations' record so founder-gravity discipline can run"; the full Augustinian Hermits sentence in `relationsSummary`; "sibling-rival of the Reformed" and "rival of Rome"; "Child of late-medieval piety and its protest"; "wider evangelical orbit"; "the movement's most-watched model of a pastor's family"; the Strauss/Scribner/Kittelson interpretation-care note; "Saxony, then N. Europe" and "North Europe"; the Matheson 1995 and McKee 2006 editions. All check out. (C15 concerns only which field one of them sits in.)

**Sibling Step 0 quotations (§8.2, §8.3) — verbatim.** The Anabaptist Step 0's "persecuted by, and in real tension with, both Lutheran Wittenberg and the Reformed cities... from the establishment side" and the Tridentine Step 0's "Lutheran Wittenberg and the Reformed cities are this candidate's own named, direct doctrinal targets — Trent's own canons anathematize positions each of those two candidates' own confessional documents affirm" are both accurately transcribed. The Reformed Step 0's §4 item 5 does exist and does bind VI.2's own Doc_01 on Marburg with a cross-reference to VI.1 — so §9 item 3's cross-reference is correct as written.

**Structural completeness, apart from S7.** Distinct World Criteria (§1), Temporal Scope with all four questions (§2), Geographic Scope (§3), Cultural Scope covering all four of linguistic/social/political/institutional (§4), **all six** World Separation Criteria questions asked and answered in the Framework's own order (§5), Strand Determination with an explicit recorded finding (§6), and Preliminary Forces Identification with four substantive, non-perfunctory answers (§7) are all present. The Step 0 disclosure routing is also correct: items 1 and 2 are binding on Doc_02 in Step 0's own words and are correctly deferred, item 3 is binding on Doc_01 and is genuinely addressed at §7 and §8.1, item 4 is done in §10.

**Dates and placements checked against the census.** Lollardy = Atlas V.5, era 6, England — the "Era VI world despite the batch's own Era VII framing" note is right. Society of Jesus = VI.11, 1540. Tridentine = VI.22. Anabaptists = VI.3. Luther's death in 1546 is correct (and Step 0's is the error; see C13). Peace of Augsburg 1555 and *cuius regio, eius religio* are correctly characterised. The Book of Concord contents named as vendored/unvendored are right.

---

## RECOMMENDATION

One full revision round, not a spot-check. S1, S4, and S5 belong to the same family — three claims sourced from an index or a sibling document while presented as sourced from the primary text or the cited framework — and the reviser should go back to the underlying files for each rather than rewording in place. S3, S10 and S11 are all "I checked and there is nothing there" claims that a check refutes; the reviser should re-read what the six files actually contain on worship, on reception, and on place, since in each case the library is richer than the document credits it with being. S7 needs new material, not an edit. Everything else is correctable in place.
