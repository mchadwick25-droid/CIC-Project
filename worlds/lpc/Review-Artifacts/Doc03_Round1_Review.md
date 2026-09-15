# Doc_03 — Lexicon Candidate List: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review — first review of a freshly-drafted, never-reviewed Step 3 deliverable

**Documents reviewed (working tree, branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_03_Lexicon_Candidate_List.md` (42 lines) — read in full, every table cell parsed programmatically and read individually
- `Doc_01_World_Identification_Boundaries_Orientation.md` — §2 (historical boundaries, the Cyprian/Augustine ordination pathways), §3 (the four named candidate gravities), §4 (the three authority axes), §5 (strand determination in full), §6 (preliminary forces, the six-cell sketch), §7 (World #6 boundary, the withdrawn *episcopatus unus est* citation, the three-phase coercion arc), §8 (all twelve open items)
- `Doc_02_Source_Ecology.md` — §5 (liturgical evidence, line 91), §6 (Article 20 disclosure line 107; Article 23 routing note line 114), §9 item 7 (line 137), section boundaries enumerated
- `Source_Registry.md` (212 rows) — rows 1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 15, 18, 22, 23, 28, 29, 42, 43, 62 parsed cell-by-cell from the raw table, Licensed-For and verification columns read in full
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Step 3 extracted verbatim (zipfile + regex on `word/document.xml`), all five Activities read
- `reference/L3B-World-Build-Methodology/CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx` — Foundational Principles and Parts I–IV extracted verbatim and read in full
- `worlds/ijc/Doc_03_Lexicon_Candidate_List.md` — read in full as peer precedent, and all three of Doc_03's cross-references to it checked at source
- `Review-Artifacts/Doc02_Round1_Review.md`, `Doc02_Round2_Review.md`, `Doc02_Round26_Review.md` — read for the Article 20 / lay-voice defect history and for this folder's review-artifact format
- `lpc_Decision_Log.md` — escalation-check entries; `worlds/desert/CiC_W3_Doc01_World_Identification.md` §escalation for the standing four-category wording

**Review date:** 2026-09-09
**Reviewer:** independent adversarial review thread. Did not draft Doc_03, did not draft Doc_01, Doc_02, or the Registry.

**Method note.** Every quoted phrase in Doc_03 was located in Doc_01/Doc_02/Source_Registry by literal string search and compared word-for-word; where a phrase did not resolve, the whole repository was searched before the phrase was called unattested. Every Registry row Doc_03 cites was parsed from the raw table and its Licensed-For and verification columns read, not summarised from Doc_02's account of them. All counts in the "Notes on scope and process" section were recomputed from the table by script rather than read from the prose.

Marking per Constitution Article 31: **Simulated review — informational only, not an Article 31 substitute.**

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 4 HIGH · 8 MEDIUM · 8 LOW · 2 COSMETIC.**

**This is a serious, well-disciplined first draft, and a large part of it holds under direct check.** The 256 preface fragments ("judging no man, nor rejecting any one from the right of communion, if he should think differently from us"; "by tyrannical terror"; "proper right of judgment") are verbatim against Doc_01 §4. Both *On Baptism* II.3 fragments are verbatim. The I.1.2 quotation ("he who is ordained, if he depart from the unity of the Church, does not lose the sacrament of conferring baptism") is verbatim, and "valid but unfruitful" is Doc_01's own gloss. "your suffrage and God's judgment," "ancient venom," "through the love of Valerius and the importunity of the people," "structurally the same," "catechetical exposition of the church's own set prayer," and the Doc_02 §9 item 7 quotation with its ellipsis are all exact. The withdrawn-citation account at the "one episcopate" entry is an accurate and genuinely valuable restatement of Doc_01 §7. The ordinal claims about Doc_01 §3's candidate gravities (second-named = penitential discipline; fourth-named = collegial communion) and Doc_01 §4's second named axis (rival-consecration-validity) are all correct. All three cross-references to Imperial-Juridical's Doc_03 — the *Caesaropapism* exclusion, the interested-advocate pattern for primacy vocabulary, and the mixed-picture-as-candidate-observation framing — were checked at source and are accurate. **Table integrity is clean**: 14 table rows, uniform 7 pipes / 6 cells each; 54 `**` markers, even total, zero odd-count lines.

**The strand/phase framing is faithful and does not need reopening.** Doc_03 correctly reports Doc_01 §5's strand-singular finding as governing, correctly carries the conciliar-authority axis's disclosed non-closure forward from §8 item 10, correctly declines to treat the two conciliar formulas as a strand-plural finding, and explicitly states that the Phase column "does not revisit" the determination. It neither overstates nor understates the uncertainty. Two blemishes attach to it (L2, and one leg of M2), but the framing itself is sound and is the draft's best structural decision.

**Where the findings are.** Four places where the draft reaches past what Doc_01/Doc_02/the Registry actually establish — one quotation attached to the wrong ordination (H1), two Latin forms that exist nowhere in the governing set (H4), a corpus-wide negative that the draft's own table and Doc_02 §6 both contradict (H3) — and one structural gap: the candidate list covers two of Doc_01's four named candidate gravities and none of Doc_01 §6's named cross-phase candidate, which defeats Step 3's own stated purpose for the gravities it leaves without vocabulary (H2). The MEDIUMs are three arithmetic/accounting errors in the Notes, two exclusion-reasoning defects, a Registry-row mischaracterisation, a risk-classification category error, and the absent Part II tagging.

---

## HIGH findings

### H1 — The "suffrage" entry attaches Letter XXXI §4 to Augustine's ordination to the **presbyterate**; Doc_01 §5 and Registry row 11 both attach it to his acceptance of the **episcopate**, and Doc_01 §2 explicitly holds that his episcopate was *not* a popular acclamation

**Location:** line 25, the "suffrage" entry, Preliminary Definition column.

Doc_03 writes:

> paired with, but not verbally identical to, Augustine's own account of his own **ordination to the presbyterate** "through the love of Valerius and the importunity of the people" (Letter XXXI §4)

Doc_01 §5 (line 92) reads:

> Augustine, of his own ordination, writes that "the blessed father Valerius… **insisted upon adding the greater burden of sharing the episcopate with him**," a burden he accepted "through the love of Valerius and the importunity of the people" (Letter XXXI §4)

Registry row 11's verification column carries the same quotation in the same frame: *"Letter XXXI §4 ('the blessed father Valerius… insisted upon adding the greater burden of sharing the episcopate with him… through the love of Valerius and the importunity of the people')… directly located and quoted in Doc_01's own Round 9 revision."*

The quoted words describe the **episcopate**, not the presbyterate. Worse, the substitution runs directly against the distinction Doc_01 §2 spends a paragraph establishing and refuses to let collapse:

> baptized in 387, seized by the Hippo congregation and ordained *presbyter*, against his own wishes, in 391…; his own later rise to the *episcopate*, in 395/396, came by a different mechanism entirely — Valerius's own designation as coadjutor and consecration by Megalius… — **not a second popular acclamation**. The recurring element is congregational demand overriding an initially reluctant convert's own preference at the point of entry into clerical office; **it recurs at the presbyterate for Augustine and the episcopate for Cyprian, not at the same office**.

Doc_03's entry then builds its whole cross-phase pattern claim on the merged version — "an adult convert compelled into clerical office by congregational demand, against his own preference," cited to Doc_01 §2 — while dropping §2's "not at the same office" qualifier entirely. This is exactly the smoothing the entry's own Author Gravity note claims to be guarding against.

**Fix:** In the Preliminary Definition, change "ordination to the presbyterate" to Augustine's acceptance of *sharing the episcopate* with Valerius, matching Doc_01 §5's own frame. In the Author Gravity cell, restore Doc_01 §2's office qualifier: the congregational-demand pattern recurs at the presbyterate for Augustine (391, Hippo's seizure) and at the episcopate for Cyprian, **not at the same office** — which strengthens, rather than weakens, the entry's own "not one settled term" caution.

---

### H2 — Candidate discovery is materially incomplete against Doc_01's own named candidate gravities and the Registry's own licensed Native rows, defeating Step 3's stated purpose for the gravities left without vocabulary

**Location:** the table as a whole; line 31 (exclusions); line 33 (Tier 1 note).

CF V7.4 Step 3's Purpose is stated in one sentence: *"Identify candidate vocabulary before gravity discovery so gravities can be tested in the world's own language."* Measured against that, the coverage is:

| Doc_01's own named candidate gravity | Source | Doc_03 vocabulary |
|---|---|---|
| 1. Pastoral office as flock-keeping (a bishop's authority as care for a bounded local community, not jurisdiction over other sees) | §3, first-named | **None.** "The one episcopate" is defined as *De Unitate*'s ecclesiology and the ground of the egalitarian conciliar formula — the jurisdictional side §3 explicitly distinguishes flock-keeping *from* |
| 2. Penitential discipline and reintegration of the failed | §3, second-named | *lapsi*, *libelli*, reconciliation — Tier 1 Yes ×2. Covered |
| 3. Preaching and catechesis as the primary mode of ordinary formation | §3, third-named | catechumen/catechesis — Tier 1 **No**; **preaching**: no term at all |
| 4. Collegial communion maintained despite disagreement | §3, fourth-named | communion — Tier 1 Yes. Covered |
| "Refusing a purity/sufficiency test" (both anchor figures resist a purity-test that would exclude the compromised) | §6, "What was it refusing," expressly named "a preliminary observation worth Doc_04's own testing" | **None** |

Registry rows 22 and 23 (Augustine's anti-Manichaean and anti-Pelagian corpora) are **Native, Confidence B**, and are licensed in terms that name that fifth candidate directly — row 22: *"the 'refusing a purity/sufficiency test' gravity candidate (Doc_01 §6)"*; row 23: *"grace/sufficiency-test gravity candidate."* Doc_03 does not draw a single term from either row and, at line 31, describes their position as one where "Doc_02 names these corpora's own existence (§1) but does not evidence any specific recurring term" — which is not what the Registry says about them (see M3).

Further Native rows carrying licensed subject matter with no candidate term: **row 5**, licensed *"De Mortalitate specifically for the epidemic gravity"* — Doc_01 §6 places epidemic disease (the Carthage plague, c. 249–262) in the Ongoing/External cell, and no mortality/plague/consolation vocabulary appears; **rows 1 and 7**, carrying the confessor and martyr material (row 7 is Pontius, Confidence A, on Cyprian's election and exile) — no confessor, martyr, or *plebs*/people term appears, though the "suffrage" entry is entirely about the congregational voice; and Doc_02 §9 item 7's own named example, *"the lapsed/**penitential** vocabulary of De Lapsis"* — the lapsed half is covered, the penitential half is represented only by "reconciliation," with no term for penance/penitential process itself.

Compounding this: catechesis (§3's third-named candidate gravity) is flagged Tier 1 **No** on the ground that it is "not itself organizing a Primary or Supporting gravity the way the terms flagged Yes above do." That ground pre-judges Doc_04, which the same document elsewhere insists is Doc_04's own work; and it is applied inconsistently, since the three other §3 candidate gravities with vocabulary are all flagged Yes on the very ground catechesis is denied. The cell also calls catechesis "Doc_01 §3's own primary formation-ecology finding" in the same breath — §3's third bullet names preaching and catechesis "the primary mode of ordinary formation."

**Fix:** Add candidate terms for §3's first candidate gravity (a flock-keeping/pastoral-charge term drawn from Cyprian's and Augustine's own words, and a congregation/*plebs* term), for preaching, for penance/penitential process as distinct from reconciliation, and for at least one term reaching Doc_01 §6's purity/sufficiency-test candidate from rows 22/23. Add a mortality/consolation term from row 5 or state on the record why the epidemic force yields no vocabulary. Either flag catechesis Tier 1 Yes on parity with the other §3 candidate gravities, or restate its "No" on a ground that does not pre-empt Doc_04 — and correct "primary formation-ecology finding" to §3's actual "third-named candidate gravity."

---

### H3 — The Author Gravity synthesis asserts a corpus-wide negative that Doc_03's own table contradicts, cites Doc_02 §6 for it when §6 says the converse, and reinstates a defect Doc_02 Round 1 already caught and Doc_02 §6 was rewritten to discharge

**Location:** line 32 (synthesis bullet) and line 16 (*lapsi* Author Gravity cell).

Line 32 states:

> nearly every term above is known *only* through one or the other bishop's own regulating, disciplining, or arguing voice — never through the lapsed believer's own account of what *lapsi* meant to live through, **never through a lay believer's own account of communion or reconciliation**, never through a rival's own first-person defense of a position Cyprian or Augustine argues against.

Doc_03's own reconciliation entry (line 18) says the opposite two rows above the synthesis: Epistles XX–XXI are *"two confessors, not bishops, writing to each other in their own first-person voice about a specific reconciliation."* Doc_02 §6 (line 107) is more emphatic still: *"Two lay believers' own letters survive in their own words: Epistles XX and XXI… two confessors, writing to each other in the first person about the reconciliation of Celerinus's lapsed sisters at Rome, neither yet ordained at the time of writing."* Registry row 1 licenses them as *"this world's own lay-confessor first-person voice."* And Registry row 7 is Pontius the Deacon — a Confidence A, non-episcopal, extended first-person Native voice — which Doc_03 does not cite anywhere.

Line 16 compounds this by attributing a corpus-wide negative to Doc_02 §6 as if §6 asserted it:

> No lapsed believer's own first-person account of the experience survives anywhere in this world's own corpus (**Doc_02 §6's own Article 20 disclosure**)

Doc_02 §6 contains no such statement. §6's Article 20 work is the *discharge* — an enumeration of the non-episcopal voices that **do** survive. The negative Doc_03 attributes to it is Doc_03's own, unverified, and asserted without any corpus check of its own.

This is the precise defect `Doc02_Round1_Review.md` recorded as H6 against Doc_02's own earlier §6 — an unverified corpus-wide negative about lay voices, of which that review wrote: *"These were one grep away."* Reinstating it at the vocabulary level after Doc_02 fixed it at the narrative level is the shape this build's history warns about most.

**Fix:** In line 32, replace "never through a lay believer's own account of communion or reconciliation" with the accurate form — the lay-confessor exception (Epistles XX–XXI, row 1) and Pontius (row 7) exist and are named, and the pattern is that they are few, occasional, and clerically framed, not that they are absent. In line 16, either drop the parenthetical citation to Doc_02 §6 and mark the "no lapsed believer's own account" claim as this document's own unverified negative pending a corpus check, or run that check and cite it. Add row 7 to the "suffrage" entry's Registry Source(s) as the third, non-episcopal witness to Cyprian's election.

---

### H4 — Two Latin headwords are presented as this world's own vocabulary but appear nowhere in Doc_01, Doc_02, or the 212-row Registry; one is a reordering of the single Latin phrase Doc_01 §7 withdrew, inside the very entry that says it does not repeat that use

**Location:** line 20 (*concilium plenarium*), line 26 (*unus episcopatus*).

Literal string search across `Doc_01`, `Doc_02` and `Source_Registry.md`, then across the whole repository:

| Form as printed in Doc_03 | Occurrences in Doc_01 | Doc_02 | Registry | Repo |
|---|---|---|---|---|
| *concilium plenarium* | 0 | 0 | 0 | 0 |
| *unus episcopatus* | 0 | 0 | 0 | 0 |
| *episcopatus unus est* (the form Doc_01 actually carries) | 1 (§7, as a **withdrawn** citation) | 0 | 0 | — |

*concilium plenarium* is a Latin form supplied for an English-translation phrase ("plenary Councils") that this world's vendored corpus carries only in NPNF's English. Doc_02 §9 item 7's instruction — the one Doc_03's own header quotes as governing — asks for "this world's own vocabulary **as it actually appears in the primary corpus**… rather than generic scholarly labels." A Latin form supplied by the drafter to dress an English phrase is the failure mode that instruction names.

*unus episcopatus* is worse-placed. Doc_01 §7 reads: *"An earlier draft of this document cited* episcopatus unus est *(De Unitate 5…) as Cyprian's own answer to Stephen; it is not… "* — a withdrawn citation. Doc_03's entry correctly narrates that withdrawal and states "This document does not repeat that withdrawn use" — while printing, as the term's own headword, a reordered form of the withdrawn phrase, unattested in that form anywhere. Whatever the intention, the effect is to reintroduce the withdrawn Latin into the lexicon's own headword line.

**Fix:** Drop *concilium plenarium* entirely; the term is `"plenary Council"` as this corpus carries it, and the entry loses nothing. For the one-episcopate entry, either drop the Latin gloss and head the term `"the one episcopate"`, or — if a Latin form is wanted — print *episcopatus unus est* with an explicit note that Doc_01 §7 withdrew it as a proof-text for the anti-Stephen argument and that it is used here only as *De Unitate*'s general ecclesiological formula. The second option is defensible; the current form is not.

---

## MEDIUM findings

### M1 — Three further Latin forms are unattested in the governing set, and the *lapsi* definition imports an outside taxonomy and contradicts itself

**Location:** lines 16, 24, 27.

*lapsi*: 0 occurrences in Doc_01, Doc_02 or the Registry (which use "the lapsed" throughout). *schisma*: 0 in Doc_01/Doc_02; the one Registry hit is inside the word "schismatic" in row 13. *haeresis*: 0 in this world's entire document set (the repo hits are Imperial-Juridical's own `records/ijc/term/` files, a different world's Registry-grounded vocabulary). Unlike H4's two, these are standard Latin forms of terms this world's corpus genuinely uses in translation, so the defect is lighter — but the draft prints them italicised and unmarked, as though attested.

Separately, the *lapsi* definition (line 16) reads: *"Carthaginian Christians who sacrificed, offered incense, or obtained a certificate of compliance during the Decian persecution (250) **without actually sacrificing**."* Two problems. The trailing modifier attaches to the whole list, so as written it says people "sacrificed… without actually sacrificing." And the tripartite taxonomy is imported: "incense" occurs **zero** times in Doc_01, Doc_02 or the Registry. Doc_01 §2 evidences only *"the* libelli *(sacrifice-certificate) system"* — the certificate mechanism, not a three-way division of the lapsed.

**Fix:** Either mark the Latin forms as the drafter's supplied standard forms not attested in this world's vendored corpus (a one-clause note, or a small attestation column), or head each term with the English the corpus actually carries and put the Latin in a note. Rewrite the *lapsi* definition to what Doc_01 §2 evidences — Christians who complied with the Decian edict's sacrifice requirement, including those who obtained a *libellus* without sacrificing — and drop the incense category unless it can be sourced.

### M2 — Three of the Notes section's own counts are wrong, recomputed from the table

**Location:** lines 33 and 34.

Recomputed by script from the twelve term rows:

| Claim | Recomputed | Result |
|---|---|---|
| "**Six** of twelve candidate terms are flagged Yes for Tier 1" (line 33) | *lapsi*, reconciliation, "bishop of bishops", "plenary Council", communion, "compel them to come in", heresy = **7** | **Wrong — seven of twelve** |
| "**Four** terms sit cleanly in one phase (*lapsi*, *libelli*, reconciliation, and 'the one episcopate' in Cyprian's; 'plenary Council' and 'compel them to come in' in Augustine's)" (line 34) | The parenthesis itself lists **six**; the table's actual single-phase count is **7** (5 Cyprian + 2 Augustine, "bishop of bishops" being the fifth Cyprian-phase term the list omits) | **Wrong twice — the number contradicts its own list, and both contradict the table** |
| The phase accounting as a whole (line 34) | "four" clean + a pair of 2 + "four" cross-phase + suffrage = 11 or 13 depending on how "plenary Council" is counted; the table is 7 single-phase + 5 cross-phase = 12 | **Does not sum to 12** |

The third leg has a substantive cause, not just an arithmetic one: line 34 counts "plenary Council" **both** as a term sitting cleanly in Augustine's phase **and** as half of a pair "deliberately paired across the phases… rather than placed in either phase alone" — while the table does assign each of the pair a single phase (Cyprian-phase / Augustine-phase). "Bishop of bishops" is then silently dropped from the clean-phase list although the table gives it Cyprian-phase.

The "slight majority" characterisation at line 33 survives the correction (7/12 is still a slight majority), so this is a count and accounting error, not a collapse of the argument — but it is the kind this build's own review history treats as a real finding, and it touches a Tier classification claim.

**Fix:** "Seven of twelve." Rewrite line 34's accounting to the table: seven terms sit in a single phase (*lapsi*, *libelli*, reconciliation, "bishop of bishops", "the one episcopate" in Cyprian's; "plenary Council" and "compel them to come in" in Augustine's), five are cross-phase (communion, catechumen/catechesis, schism, "suffrage", heresy), 7 + 5 = 12. Then state the conciliar pair's cross-phase pairing as a relationship *between* two single-phase terms, which is what the table actually encodes, rather than as an alternative to phase placement.

### M3 — The Manichaean/Pelagian exclusion contradicts Doc_02 §6's own routing note and understates what the Registry says about rows 22 and 23

**Location:** line 31.

Doc_03 excludes Donatist vocabulary on Article 23 scope grounds, then excludes Manichaean and Pelagian vocabulary "for a different reason than the Donatist exclusion," calling it "an evidentiary gap in this document's own work so far, **not a scope exclusion on Article 23 grounds**."

Doc_02 §6's routing note (line 114) treats all three identically and by name:

> How this world's eventual Representative characterizes this world's own opponents — **the Donatists, the Manichaeans, the Pelagians**, each already engaged as a live controversy in the primary sources at §1 above — is Article 23's future concern, not this section's.

So the asymmetry Doc_03 draws is not one Doc_02 §6 supports. Separately, the evidentiary characterisation is wrong on the record: Doc_03 says Doc_02 merely "names these corpora's own existence (§1)," but Registry rows 22 and 23 are **Native, Confidence B**, with Licensed-For fields that tie them to a specific named gravity candidate (row 22: *"the 'refusing a purity/sufficiency test' gravity candidate (Doc_01 §6)"*; row 23: *"grace/sufficiency-test gravity candidate"*). These are Augustine's **own** works — this world's own voice, not the opponents' vocabulary — which is precisely why an Article 23 opponent-characterisation exclusion does not reach them, and why H2's gap over them is a real omission rather than a defensible boundary.

**Fix:** Restate the exclusion so it tracks Doc_02 §6: opponent-*characterising* vocabulary (Donatist, Manichaean, Pelagian alike) is Article 23's concern; **Augustine's own** anti-Manichaean and anti-Pelagian vocabulary in rows 22 and 23 is Native and in scope, is licensed for a named Doc_01 §6 gravity candidate, and its absence here is a discovery gap this pass should close (see H2), not a boundary.

### M4 — The Tertullian exclusion is reasoned on origin rather than usage, and as written would suppress the Lexicon Framework's own second Three-Sources category

**Location:** line 31.

Doc_03 excludes "*Tertullian's own coined vocabulary*" because Tertullian "is credited with forging the Latin theological vocabulary this world inherits, but is not himself this world's own voice (Doc_01 §7); drawing his own terms into this list would blur exactly the boundary Doc_01 and Doc_02 §1 both take care to hold."

The row-29 exclusion is real and correctly cited — Tertullian is Excluded / Named Comparandum. But the exclusion Registry row 29 makes is of **Tertullian as a source**, not of any word he coined. As Doc_03 states it, a term would be excluded because of who first coined it, even where Cyprian's or Augustine's own corpus uses it — which is a different rule, and one that runs against Interpretive Lexicon Development Framework V2.1's Three Sources Principle, whose second category is exactly *"shared vocabulary common across Christian tradition broadly, which this world uses with its own distinctive assumptions"* ([SC]), and whose accompanying warning is that *"a lexicon restricted only to exotic or untranslatable terms will miss the second and third categories, which are often where the most significant distortion risk for modern readers actually lives."* Doc_01 §6's own framing supports usage, not origin, as the test: Tertullian gave North African Christianity "the Latin theological vocabulary **this world inherits**."

**Fix:** Restate: Tertullian is excluded as a *source* (row 29, Named Comparandum) and no claim in this list rests on his text; but a term is a candidate on the strength of its use in **this world's own Native corpus**, whatever its coinage history — so Tertullianic-origin vocabulary that Cyprian or Augustine actually uses is in scope, and its absence here is a discovery matter, not a boundary.

### M5 — The Letter 185 §§25–26 solicitation is attributed to Augustine personally and its two registers are collapsed, dropping two qualifications Doc_01 and the Registry both hold deliberately

**Location:** line 22, the "compel them to come in" entry.

Doc_03: *"a real but narrow, and in the event unsuccessful, solicitation of legal protection early in his own episcopate (Letter 185 §§25–26)"* — inside a sentence whose subject throughout is Augustine's own three-phase development.

Doc_01 §7 (line 160) and §8 item 12 both place the solicitation at **a council**: *"at a council of African [bishops] — dated 401 by NPNF's own editorial footnote at Letter 185 §25, **not by Augustine's own text, which does not date it**… the party Augustine belonged to 'carried our point'."* Registry row 12 carries the same care: *"a council NPNF's own editorial footnote dates 401's own narrower solicitation of state power (Letter 185 §§25–26; the 401 date is the footnote's own, not Augustine's own text's, per Doc_01's own established distinction, **carried here rather than dropped**)."* Doc_03 drops "at a council" and, with it, the collective-action fact the two upstream documents both hold on the record.

Second, the entry's definition states the doctrine as *"the Christian ruler may and should use civil compulsion to bring a separated party back into the one communion."* That is Letter 185's **pastoral-corrective register alone**. Doc_01 §5 names that register as the easy answer and expressly refuses to rest on it: the letter *"also runs a second, non-pastoral register — the Christian ruler's own general duty to legislate against error — which is not, on its own terms, a claim about restoring a specific separated party to communion at all, and is the register §4 finds genuinely harder to reconcile."* The entry's phase cell does say "two-register defense," so the draft knows this; the definition itself nonetheless performs exactly the flattening the Author Gravity cell claims to prevent.

**Fix:** Restore "at a council of African bishops," and note that the 401 date is NPNF's editorial footnote's, not Augustine's text's. Rewrite the definition to hold both registers — a separated party's recovery **and** the Christian ruler's general duty to legislate against error — per Doc_01 §4/§5.

### M6 — Registry row 3's Confidence B is attributed to the two-recension question; row 3 attributes it to something else and names the recension fact as an addition

**Location:** line 24, the "schism" entry.

Doc_03: *"a live textual question Doc_01 §7 names and does not resolve (**Registry row 3's own Confidence B, downgraded from A on exactly this ground**)."*

Row 3's verification column reads:

> **Confidence B rather than A:** what Doc_01's own Round 2 review established was that *De Unitate* 5 does not carry Cyprian's anti-Stephen position… — a finding about what this row is *not* licensed for, **not an independent verification of any specific locus within the treatise itself, and none is named here**. *De Unitate* 4–5 **also** survives in two recensions… — a transmission fact Doc_01 §7 names and does not resolve, carried here rather than dropped

The stated ground for B is the absence of any independent locus verification, arrived at through the anti-Stephen finding. The recension fact is introduced with "also" as a further transmission fact carried forward, explicitly not as the ground. Row 3 also says "Confidence B rather than A," a first assignment, not a downgrade from a prior A.

**Fix:** *"(Registry row 3 stands at Confidence B — on the absence of any independent locus verification within the treatise, per its own note; the two-recension fact is carried there as an additional, unresolved transmission question rather than as the ground of that rating.)"*

### M7 — The list's highest Author Gravity rating is justified entirely on Distortion Risk grounds, and imports an unsourced scriptural citation

**Location:** line 22, the "compel them to come in" entry.

The Author Gravity Risk cell reads *"**Very high — the single highest distortion-risk term on this list.**"* CF V7.4 Step 3's activity is *"Flag Author Gravity risks (terms that appear to carry unusual weight from specific voices)."* Distortion Risk is a separate, independently-tagged dimension in Interpretive Lexicon Development Framework V2.1 Part II ([DR], "the gap between likely modern hearing and this world's actual understanding"), and the cell's whole justification is [DR] reasoning — later reception history, the gap between modern hearing and the world's own development. The result is that the top Author Gravity rating on the list is not an Author Gravity finding at all, while the term's actual author-gravity position (this doctrine is known only through Augustine's own advocacy for it, in his own defence, with no Donatist first-person answer in this world's Native corpus) goes unstated.

Separately, the definition adds *"(echoing Luke 14:23)"*. "Luke 14" occurs **zero** times in Doc_01, Doc_02 and the Registry. The scriptural attribution is true history but is imported knowledge, unsourced within the governing set, and not covered by rows 12 or 43's Licensed-For.

**Fix:** Rate the cell on author gravity (Augustine as sole surviving advocate, no rival first-person answer in this world's corpus) and move the reception-history/modern-hearing material into an explicitly labelled distortion-risk note flagged for Doc_06's [DR] treatment. Drop "(echoing Luke 14:23)" or source it to a Registry row that licenses it.

### M8 — No Part II classification tags, and no thematic organisation, with the omission undeclared

**Location:** the table as a whole; header line 6.

Interpretive Lexicon Development Framework V2.1, Part IV, step 1: *"Candidate Discovery (Part I) produces a **tagged**, organized Candidate List."* Part I: *"Candidate discovery should produce a Candidate List, **organized into thematic sections reflecting the ecology's own conceptual clusters** rather than alphabetical convenience, since alphabetical ordering obscures the conceptual relationships the lexicon exists to reveal."* Part II supplies the tag set ([AS]/[SC] origin; [DR]/[TC]/[RT]/[PV]/[CT] risk-and-function) and instructs that *"tags should be assigned based on the term's actual demonstrated function during candidate discovery."*

Doc_03 carries no tags and no thematic sections — one flat, unsectioned table. The peer precedent does the same, but declares it: Imperial-Juridical's Doc_03 header states *"No per-term chunk files, **tags**, or CT Contest Type sections are built here."* Doc_03's header (line 6) lists "no per-term chunk files, [CT] contest-type sections, or final tier assignment" — **tags** is absent from that list, so the omission is not disclosed here at all, and only [CT] is deferred.

Two of the tags would do real work in this draft immediately: [PV] ("important within some streams, voices, or periods… but not universally representative") is exactly the phase-attribution distinction the draft is reaching for by hand, and [SC] is the category M4's Tertullian exclusion would otherwise suppress.

**Fix (document-level):** At minimum, add "tags" to the header's own list of deferred items so the omission is declared, as IJC's does. Better: apply Part II's Origin tags ([AS]/[SC]) and [PV] to the twelve terms now — they are cheap at this stage and directly support Doc_04 — and group the table into the conceptual clusters it already implies (penitential/lapsed; conciliar authority; communion and boundary; formation and catechesis; office and calling). Whether Doc_03s across the portfolio should be built with Part II tags is a methodology question, not this document's to settle alone — routed in the escalation section below.

---

## LOW findings

### L1 — "sets himself up as a bishop of bishops": a word substitution inside quotation marks
**Line 19.** Doc_03: *no bishop **"sets** himself up as a bishop of bishops."* Doc_01 §4 and Registry row 4 both read *"neither does any of us **set** himself up as a bishop of bishops."* The inflection was changed to fit the surrounding sentence. **Fix:** recast outside the quotation — *that no one of them may "set himself up as a bishop of bishops."*

### L2 — "closest call" is quoted to Doc_01 §8 item 10; it occurs only at Doc_01 §5
**Lines 8 and 19.** The phrase occurs exactly once in Doc_01, at §5 (*"It is weakest on the conciliar-authority axis, which §4 flags as the closest call and does not consider fully closed"*). §8 item 10 carries the substance ("not yet closed," the reopening caveat) but not those words. The substance of both Doc_03 sentences is correct; only the quotation's address is wrong. **Fix:** cite the phrase to Doc_01 §5 and the non-closure/reopening caveat to §8 item 10.

### L3 — "the reconciliation of Celerinus's lapsed sisters at Rome" is attributed to Row 1; the phrase is Doc_02 §6's
**Line 18.** The phrase is verbatim from Doc_02 §6 (line 107). Registry row 1 names Epistles XX–XXI as *"Celerinus to Lucian" / "Lucian Replies to Celerinus"… "this world's own lay-confessor first-person voice"* and does not contain the quoted words. **Fix:** attribute the quotation to Doc_02 §6 and cite row 1 for the letters themselves.

### L4 — The two phases are defined by episcopal date-ranges that do not cover the world's own declared span, leaving cited material in neither phase
**Line 8.** The Phase column is defined as "Cyprian's episcopate, 248/249–258; Augustine's episcopate, 395/396–430." Doc_01 §2's declared horizon is **c. 246–430**, opening at Cyprian's conversion. Material Doc_03 itself cites falls outside both phases: row 9's *Confessions* conversion narrative (386–387, licensed for exactly that), and Augustine's 391 presbyterate ordination, which is the event the "suffrage" entry's cross-phase pattern actually turns on (see H1). **Fix:** define the phases as *Cyprian's phase (c. 246–258)* and *Augustine's phase (386–430)*, or state explicitly that the labels name the two episcopates and that pre-episcopal material is attributed to the adjacent phase.

### L5 — Registry row 7 (Pontius) is cited nowhere, though it bears directly on the "suffrage" entry and on the Author Gravity synthesis
**Lines 25, 32.** Row 7 is *Pontius the Deacon, The Life and Passion of Cyprian* — Native, **Confidence A** — licensed for *"Cyprian's own election specifically (Doc_01 §2, 'by the judgment of God and the favour of the people, he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte')."* It is a third, non-episcopal witness to the same election the "suffrage" entry is built on, with its own distinct vocabulary. **Fix:** add row 7 to the "suffrage" entry's sources; it also directly qualifies H3's synthesis.

### L6 — The Author Gravity Risk column carries non-author-gravity content in four entries without saying so
**Lines 17, 22, 24, 26.** *libelli*: evidentiary thinness (not re-verified at source). "compel them to come in": distortion risk (M7). schism: textual transmission / two recensions. "the one episcopate": a withdrawn-citation caution. Only the "suffrage" entry names what it is doing (*"the caution is evidentiary rather than interest-based"*). The content is valuable in every case; the column heading no longer describes it. **Fix:** either rename the column (e.g. "Author Gravity & Evidentiary Risk") or label each cell's risk type as the "suffrage" entry already does.

### L7 — Doc_01 §5's own stated reading on the lapsed-concern question is dropped
**Line 16.** Doc_03: Doc_01 "raises, without resolving," whether the underlying concern persists into Augustine's phase. Doc_01 §5 goes one step further: *"This document's own reading, consistent with §4's, favors the former; that reading is Doc_04's own to confirm, not asserted as settled here."* Doc_03's "does not decide" is correct as to settlement but omits the recorded lean. **Fix:** add that Doc_01 §5's own reading favours persistence, while leaving confirmation to Doc_04.

### L8 — No discovery-saturation statement
**Line 33 and the Notes generally.** Interpretive Lexicon Development Framework V2.1, Part I: *"A Candidate List should be considered complete enough to proceed to development when the world's Historical Gravities, primary sources, and Integrated Ecology Analysis output have all been consulted, and when continued search produces substantially diminishing returns of genuinely new candidates."* Two of those three inputs do not exist at Step 3, which the draft could say; what it does not say anywhere is how discovery was run against the inputs that do exist, or whether it reached diminishing returns. Given H2, it plainly did not. **Fix:** add a short discovery-coverage note — which Registry Native rows were swept for vocabulary, which were not, and on what basis the sweep stopped — in the same spirit as the Registry's own saturation statement.

---

## COSMETIC findings

### C1 — Row 5 is cited under a Latin title the Registry row does not use
**Line 23.** Doc_03 cites *"Row 5 (*De Dominica Oratione*…)."* Registry row 5's own title for that work is *On the Lord's Prayer*; the Latin form comes from Doc_02 §5, which is quoted correctly in the same cell. Harmless, but a reader checking row 5 by title will not find it. **Fix:** *"Row 5 (*On the Lord's Prayer* / *De Dominica Oratione*)."*

### C2 — "two confessors, not bishops" understates what the record establishes
**Line 18.** Doc_02 §6 and Registry row 1 both establish the stronger fact: neither Celerinus nor Lucian was **ordained at all** at the time of writing. "Not bishops" leaves room for a clerical status the sources exclude. **Fix:** "two lay confessors, neither yet ordained."

---

## Mechanical checks — all pass

- **Pipe count:** 14 table rows (header, separator, 12 terms). Every row: 7 `|`, 6 cells. Uniform.
- **Bold markers:** 54 `**` across the file, even total; zero lines with an odd count; no unclosed or nested-broken pair found.
- **Table parse:** the table parses cleanly to 12 term rows with 6 columns each under a naive `split('|')`; no cell contains an unescaped pipe.
- **Registry rows cited:** 1, 2, 3, 4, 5, 9, 11, 12, 13, 15, 18, 43. All twelve exist in `Source_Registry.md`, all are classified **Native**, none is Excluded, and each carries subject matter consistent with the entry citing it — with the four qualifications recorded at H3 (row 1's lay-confessor licence contradicting the synthesis), M3 (rows 22/23 uncited), M5 (row 12's council/date qualifications dropped), and M6 (row 3's Confidence B ground mischaracterised). Row 9's use for the *Confessions*' catechumenate narrative is not named in row 9's own Licensed-For, but Doc_02 §5 cites row 9 for exactly that in cleared text, so it holds.

---

## CO-022 escalation-category assessment

Run against the four standing categories.

**1. Representative-identity decisions — does not apply.** Nothing in Doc_03 names, titles, characterises, or constrains this world's Representative. The draft's own self-assessment at line 41 is correct on this point.

**2. Portfolio-level / cross-world decisions — does not apply, checked rather than assumed.** Doc_03 makes three cross-world references, all to Imperial-Juridical's Doc_03; all three were checked at source and all three *apply* IJC's precedent rather than making a new determination. The Donatist-vocabulary exclusion applies two determinations already made and already labelled upstream — Doc_01 §5's World #4/#8 boundary (itself labelled CO-022 category 2 there, adopted from `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`) and Doc_02 §6's Article 23 routing note. M3's defect in that exclusion's *reasoning* is an internal inconsistency with Doc_02 §6, fixable from documents in hand; it does not create or reopen a portfolio question. No candidate term claims vocabulary another world holds as native.

**3. Governance / methodology decisions — TRIPPED, at low intensity, and recommended for routing rather than for blocking this document.** M8 is not only a defect in this draft. Interpretive Lexicon Development Framework V2.1 Part IV requires candidate discovery to produce a *"tagged, organized Candidate List,"* and Part I requires thematic sectioning. Two worlds have now produced a Doc_03 without either: Imperial-Juridical's (cleared, Round 2 COSMETIC ONLY, which declares the tag omission on its face) and this one (which does not declare it). Whether Step 3 across the portfolio should be run with Part II tags and thematic clusters, or whether the Framework's Part I/II requirements are properly read as Step 6 obligations, is a question about how Doc_03s are built portfolio-wide, not a question this world's build thread should settle by itself in either direction. This is the same shape as **Doc_01 §8 item 9**, which this world already routed to a coach pass as a System Hub process finding rather than resolving locally, and the same routing is recommended here.

Recommended handling: this document should (a) declare the tag omission in its own header as IJC's does, which is entirely within its own competence, and (b) log the portfolio question as an open item for a coach/System-Hub pass. Neither step requires waiting on that pass, and none of the other twenty-one findings in this review depend on how it comes out.

**4. Unresolved tensions the pipeline can't close — does not apply.** Every finding here is closable from documents already in this world's build folder; none requires a decision the pipeline cannot make. Two near-misses, both checked and neither tripping: the conciliar-authority axis's non-closure is a *routed* open item (Doc_01 §8 item 10, explicitly assigned to Doc_04's six-test assessment), not a new tension — and Doc_03's handling of it is faithful, so it neither reopens nor prematurely closes anything; and H2's gap over Doc_01 §6's purity/sufficiency-test candidate is a discovery omission this document can fix from rows 22 and 23, not a question about whether that candidate exists.

**Result: one category tripped (category 3, methodology), at a level warranting routing to a coach pass and a header disclosure, not project-lead escalation ahead of this document's own revision cycle. Categories 1, 2 and 4 do not apply.**

---

## Note on disposition — deliberately not assessed

Consistent with this folder's practice, this review does not recommend a disposition. The draft's Status line commissions one independent round before any self-disposition and states that findings are to be shown to the project lead before any fix is applied; that sequencing is the build thread's and the project lead's to run, not this review's to pre-empt.

---

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 4 HIGH · 8 MEDIUM · 8 LOW · 2 COSMETIC.**

**Simulated review — informational only, not an Article 31 substitute.**
