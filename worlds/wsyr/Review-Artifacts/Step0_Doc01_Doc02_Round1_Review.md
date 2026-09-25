# Adversarial Review, Round 1: wsyr library stage (Step 0, Doc_01, Doc_02, Dossier, Open Gaps, registry)

**Reviewer:** Opus, isolated adversarial review pass, 2026-09-25. Independent
of the drafting thread; instructed to read every primary source directly
rather than trust the drafts' own summaries, per `cic-build-cycle`'s review
requirements.

**Verdict: SUBSTANTIAL REVISION REQUIRED.**

I opened every primary file myself rather than relying on the drafts'
summaries. Most of the spot-checks the drafts ran hold up. But the drafts
misstate what several of their own vendored files contain. Three of the
central conclusions also fail against the sources: the eligibility-floor
argument's confidence claim, the strand determination, and the
scope/continuity claims.

Note: the work was committed as b95dc401 while I was reviewing. That commit
message repeats the "Chalcedon's own 451 bifurcation" error (see D1-2).

## Spot-checks the task asked me to rerun

| Claim | Result |
|---|---|
| Brooks renders him "James" | **Confirmed.** Lives line 26185, "The Forty-Ninth History, of the Blessed James the Bishop". |
| "Burd'ana" means patchwork garment, from a cloak he cut in two | **Confirmed, but the locus is wrong.** The footnote is at lines 26244-26246, not 26301 (26301 is a running header). The word "felt" does not appear. Brooks himself glosses the cloak "of withes (?)". The drafts should not present this as refuting the horse-cloth gloss, which rests on the Syriac word's usual meaning (a coarse saddle-cloth). Non-blocking. |
| About 15 years in Constantinople under Theodora; joint consecration with Theodore for "Hirtha of the Saracens" | **Confirmed.** Lines 26222-26282; ch. 50 (line 26688ff) repeats it. Calling Hirtha "the Ghassanid capital" is a gloss. Brooks's ch. 50 note calls it "the seat of the Roman Saracens", while his ch. 49 note says "also called Hirtha d-Nu'man". Non-blocking. |
| Tralles mission in Payne Smith III.36-38; "seventy thousand" only in the Preface | **Narrative confirmed. The locus is III.36-37**; III.38 begins "Eutychius enjoyed the patriarchate". "Seventy thousand" is indeed absent from the III.36-37 narrative. But the provenance conclusion drawn from this is wrong (Doc_02 finding 5). |

## Step 0

**S0-1 (REAL). The floor argument's "Widely Accepted" tag is overstated and partly contradicted by a vendored source.**
- The claim: the dispute was over "whether 'two natures' or 'one united nature' was the correct formula for saying the same substantive thing", tagged Widely Accepted (§1). A3 adds "a claim both sides read in the same realist, ontological sense."
- Severus, in the vendored Select Letters I.1 (part1 lines 687-731), calls Chalcedon's doctrine and Leo's Tome "the life blood of the abomination of Nestorius". He also explicitly rejects accepting Chalcedon as merely a rejection of Nestorius and Eutyches.
- The substantive issues were real. Severus treated nature and hypostasis as concrete near-equivalents, so "two natures after the union" meant Nestorianism to him. He also rejected the Tome's "each form acts" (the operations question that later drove monoenergism).
- "Merely verbal" is a modern ecumenical and theological judgment: Lebon's "verbal monophysitism" thesis and the agreed statements of 1989/1990, not "1990s-2000s". The more directly relevant text is the 1984 Syriac Orthodox-Catholic common declaration. Historians still contest it.
- Step 0 cites Frend 1972 as its authority, but Doc_02 §4 and Open Gaps #8 say Frend was never consulted and would not be relied on alone. That is an internal contradiction.
- **Fix:** separate the two claims — (a) Documented: Severus and the movement affirmed each of the five Article 4 commitments and condemned Eutyches by name; (b) Contested/modern-ecumenical-judgment: that the schism was substantially formulaic. The floor still clears; only the confidence claim needs to change.

**S0-2 (REAL). "Full Trinitarian faith (miaphysite theology is not itself in dispute on this point)" leaves out the Tritheist schism inside the movement, within this window.**
- The vendored EH Part III covers it at length: Book I, lines ~4475-4860, on Conon, the Condobaudites, John Philoponus and a rival Tritheist episcopate. John himself calls them heretics.
- Julianism (Christ's body incorruptible from the union, bearing on commitment iii, "truly human") was also a live anti-Chalcedonian faction; the vendored Lives footnote at line 26095 has the Julianists expelling Theodosius in 535.
- The movement-level floor still clears, but these factions need to be named as boundary cases, the way `syr` handled Bardaisan.

**S0-3 (REAL). B3: Egypt had "a largely self-governing territorial base" it "did not need" Theodora for, while Syria had "no patriarchal seat".**
- Theodosius of Alexandria was himself exiled and kept at Constantinople under Theodora from 536/7 for about 30 years (Lives, lines 26069-26082).
- Alexandria had imposed Chalcedonian patriarchs (Proterius; Paul of Tabennesi, 537).
- The Syrian miaphysites did keep a patriarchal succession of Antioch: Sergius of Tella, then Paul (Lives lines 26121-26140, Brooks's own note: "in the Monophysite succession, as opposed to the Chalcedonian patriarchs"). Later Peter of Callinicum and Athanasius Gamolo held the see to 631.
- **Fix:** restate the contrast as "no possession of the see" rather than "no seat", and soften the Egypt comparison.

## Doc_01

**D1-1 (REAL). §3 and §9.3 say the core geography "sits entirely inside the Eastern Roman/Byzantine Empire throughout its own window" and "does not span two states". False.**
- The Sasanians occupied Syria and Mesopotamia c. 610-628. Khosrow II's court favoured the miaphysites.
- The miaphysite church was organised on the Persian side too: Ahudemmeh consecrated by Jacob c. 559, Tagrit and Mar Mattai, the Maphrianate of Tagrit (629).
- The 7th century (the Antioch-Alexandria schism 586-616; Heraclius's union efforts) is missing from the internal-hinges section entirely.
- Weakens the Yarmouk rationale, which should account for the 610-628 interruption.
- The `place` field in `records/worlds/wsyr.yaml` repeats the error.

**D1-2 (REAL). §8 and §9.6 say `syr` "bifurcates" at Chalcedon into sibling East and West branches. Not in `syr`, and historically wrong.**
- `syr` Doc_01 §8 never mentions Chalcedon. It names the "institutionally organized Church of the East" (410) as its successor and assigns *Ephrem's hymnic corpus* to that East Syriac line.
- So "this world inherits Ephrem's Edessene legacy specifically" contradicts `syr`'s own text.
- The East/West separation was not a Chalcedon event — institutionally 410/424, theologically/administratively c. 431-489 (Beth Lapat 484, Seleucia 486, School of Edessa closed 489).
- Roman-side Edessa itself fed the East Syriac line too (Ibas, "School of the Persians").
- "Sibling branches of `syr`" is defensible (census `syr` relationsSummary: "Parent of the Church of the East and the Syriac Orthodox Church"). "Bifurcation at 451" and the Roman-half/Persian-half split are not.
- **Fix:** keep "sibling descendants". Drop the Chalcedon-bifurcation claim. State both churches claim Ephrem.

**D1-3 (REAL). §5 says Philoxenus's vendored Discourses are not Christological and his doctrinal corpus "not vendored this session". Wrong about the file.**
- The vendored Budge Vol. II contents (philoxenus file lines 325-348) list "The Creed of Philoxenus", "A Confession of Faith", "Against those who maintain two natures", "Against every Nestorian", "Against Nestorius" — Philoxenus's own Christological texts, in translation, inside the vendored file.
- Same error in the staging YAML, Doc_02 §3, Open Gaps #6.

**D1-4 (REAL). §6's strand determination uses the wrong test and misses the evidence.**
- Argues strand-singular because Severus and Jacob are "temporally sequential phases", citing the `ijc` merge as analogy. `ijc`'s own Doc_01 (line 57) says sequential phases are a world-merge finding (Article 15), explicitly "not a strand finding". The real strand question is simultaneous divergence.
- A simultaneous divergence does exist in this window, per the vendored EH Part III: a rival Tritheist episcopate (Book I); the Paulite/Jacobite schism (Book IV) — monasteries splitting, abbots appealing to Jacob, Jacob dying en route to Alexandria to help settle it, al-Mundhir's intervention.
- "Jacob inherits an already-doctrinally-settled movement" is false. John of Tella's mass ordinations (before 538) mean clandestine ordination did not begin with Jacob in 542 either.
- **Fix:** redo §6 against the simultaneous-divergence test, using EH III Books I and IV.

**D1-5 (REAL). Theodora's 548 death is cited "per the vendored Lives, ch. 47/49".**
- The footnote (line 26025) is in ch. 48 and concerns Anthimus's deprivation in 536 (+12 = 548). Nothing to do with Jacob.

**D1-6 (REAL). Contradicted by the vendored text:**
- "Edessa (where Jacob Baradaeus was consecrated bishop)" (§3) — he was consecrated *for* Edessa while resident in Constantinople.
- "consecrated in secret by a fugitive" (§8) — the census names the exiled, court-held patriarch Theodosius as the consecrator.
- Severus as "the last legitimately appointed Chalcedon-era patriarch of Antioch" (§1) — wrong on the succession (see S0-3).
- "Books III-VI derive from a Chalcedonian author" (§5, §9.7) — see D2-1.

## Doc_02

**D2-1 (REAL, blocking). The Zachariah compilation's voice is inverted.**
- Table A, the staging YAML, Open Gaps #4 and Doc_01 all call Zacharias Scholasticus "(Chalcedonian)" and say his Books III-VI "are closer to context/opponent-voice".
- The vendored 1899 introduction (lines 255-370) says Evagrius cites him as "a Monophysite writer"; he wrote the History (450-491) between 491 and 518, and a Life of Severus defending Severus; only "at a later time, conforming perhaps to the Chalcedonian faith", did he become bishop of Mitylene.
- Books III-VI are anti-Chalcedonian material written before his conversion, if any. The tagging runs backwards.
- The staging claim that the 1899 edition "predates that authorship analysis" is also false — the same introduction already separates the compiler from Zachariah ("to whom the name of Zachariah was wrongly attached").

**D2-2 (REAL, blocking: misquote). Doc_02 §11 item 6 quotes line 26025 as "Theodora lived 12 years after [Jacob's consecration]", "consistent with her 548 death".**
- The bracketed words are not in the text and name the wrong referent (Anthimus's deprivation, 536). 542+12=554 would not even work for Jacob. This is the recurring defect type: a misattributed quote presented as verified.

**D2-3 (REAL). EH Part III's holdings are misdescribed.**
- Table A says "Book III (and index fragments of IV-VI)"; the file contains Books I-VI in translation (body headings at lines 5883, 9233, 12719, 16886, 17506).
- The staging note says II.44 "does not survive in this volume" — it does (~line 9000, "ninety-nine new churches and twelve monasteries").
- This error is what hid the Tritheist and Paulite material from D1-4.

**D2-4 (REAL). "Jacob Baradaeus left no surviving writing of his own" (§3; Open Gaps #5).**
- Letters attributed to Jacob may survive in Syriac (Chabot's CSCO *Documenta ad origines monophysitarum illustrandas*); an anaphora is ascribed to him. Not independently confirmed this pass — reclassify as an acquisition gap, not an absence of evidence.

**D2-5 (REAL). The "seventy thousand" figure is traced to the wrong source.**
- Called "the 1860 editor's own summary" — the Preface (lines 208-224) attributes it to Part II extracts preserved in the Chronicle of Dionysius (Assemani, Bibliotheca Orientalis ii) — i.e. John's own Part II material, not an editorial invention. The correct next step is those Part II fragments (Chronicle of Zuqnin/Pseudo-Dionysius), not further searching in Part III.

**D2-6 (REAL). The self-designation is rated "not located" / Inferential-Thin. The already-checked text shows it.**
- Ch. 49-50 (already verified for other claims) say "the party of the believers", "the orthodox believers", "the opponents of the synod of Chalcedon". EH III uses "the orthodox party"/"bishop of the orthodox" (e.g. ~line 9000).

**D2-7 (REAL). Severus's letters dismissed as "administrative correspondence"; his own doctrinal argument called unvendored, "most consequential gap".**
- Ep. I.1 and others contain substantial doctrinal argument against Chalcedon, the Tome, and Eutyches (see S0-1). The gap is narrower: his separate treatises and homilies.

**D2-8 (REAL, moderate). "Women appear only as reported patrons" (Theodora, the Ghassanid court), repeated in the registry `thinness_statement`.**
- The Lives gives whole chapters to women ascetics (e.g. ch. 12, two sisters; ch. 27, Susan; ch. 28, Mary the anchorite; ch. 54, Caesaria the patrician). The "no first-person female voice" point stands, but "only as patrons" is not accurate.

**Minor, non-blocking:** Joshua the Stylite praises Flavian II of Antioch (line 3895, the patriarch Severus replaced in 512) — a relevant lead for the chronicler's-allegiance open question. The political-patronage evidence is ch. 50, not ch. 49.

## Dossier / Open Gaps / registry

- **(REAL, hygiene rule)** `records/worlds/wsyr.yaml` carries a 16-line process-narration comment header; no other `records/worlds/*.yaml` has any comments.
- **Open Gaps #12** lists "missing card_name" among waived defects, but card_name is set and the waiver text already says so — minor inconsistency.
- **Dossier §3:** the Brooks quote used to support Kugener's PO 2 edition actually names **Nau's** French translation — two different editions, minor.
- **Correct as represented:** the Chronicle of Edessa placement matches `NEEDS-RULING.md`; "Chalcedonian per its own introduction" is supported (Cowper line 32); the Phase One Step 0 Conclusion does name the Cyrilline/miaphysite Egyptian tradition as deferred; the census quotes are accurate.

## Mechanical checks

- `python3 -m engine.m1.cross_world`: exit 0, six `wsyr` waivers in `ACCEPTED_OPEN`, each dated and reasoned.
- `corpus_map_merge.py --check`: exit 0, `wsyr` bucket has 11 work rows.
- `texts_registry.py`: **exit 1**, 2 problems (`fixture-synthetic_later-summary.txt`, `fixture-synthetic_witness-scroll.txt`, "undeclared vendoring") — pre-existing, unrelated to this build, dated from an earlier merge. The seven new files raise no problems. But Doc_02 §2 claims the tool reports clean, and Open Gaps #13 attributes this finding to `corpus_map_merge` instead of `texts_registry.py` — both need correcting.

## What a revision must change (substance)

1. S0-1: re-tag the "formulaic" claim as Contested/modern-ecumenical-judgment; rest the floor on primary texts.
2. S0-2 and D1-4: name the Tritheist, Julianist and Paulite factions; redo the strand test for simultaneous divergence.
3. D1-1: correct the geography and political status (Persian occupation, Persian-side church, 7th century).
4. D1-2: remove "bifurcation at Chalcedon"; make consistent with `syr` §8.
5. D2-1: reverse the Zachariah voice tagging in all four places.
6. D2-2 and D1-5: remove the fabricated bracket.
7. D2-3: correct the EH Part III holdings.
8. D1-3, D2-4, D2-6, D2-7: correct the "not vendored / doesn't exist" conclusions about Philoxenus's Christology, Jacob's writings, the self-designation, Severus's doctrine.
9. D2-5: correct the provenance of the 70,000 figure.
10. D2-8: correct the women and thinness statement.
11. D1-6: fix the Edessa consecration, the "fugitive", and the "last legitimate patriarch".

Wording-level items (loci, "felt", the Hirtha gloss, III.38, the registry comment header) are non-substantial but should be fixed in the same pass.

---

## Round 2 targeted recheck (against the Round 1 fixes, commit e8d2c80a)

**Verdict: SUBSTANTIAL REVISION REQUIRED.** Most Round 1 findings were fixed
correctly. The fix pass itself introduced new errors while adding the
Tritheist material: it used the 1860 translator's own editorial excursus
(drawing explicitly on the 13th-century chronicler Bar-Hebraeus) as if it
were John of Ephesus's own contemporary narrative, in five places, and it
mischaracterized the Tritheist dispute as a rival reading of the
Christological "one nature" formula when it is actually a Trinitarian
dispute (Ascunages's own quoted creed affirms "one nature of Christ" and
diverges only on how many "Godheads" the Trinity contains). It also left
stale "formulaic" wording in Step 0 immediately next to the paragraph that
re-tags that same claim as Contested, added an unsupported specific
consecration date for Sergius of Tella (544/546), and a minor overreach
("Jacobite... was never its own chosen name"). The 586-616 Antioch-
Alexandria schism and Heraclius's reunion efforts, flagged as missing from
Doc_01's own internal-hinges list, were still missing.

Independently verified before fixing: the Payne Smith/Bar-Hebraeus
attribution directly, at `cic/texts/john-of-ephesus_ecclesiastical-
history-part3_paynesmith1860.txt` around line 4568 ("We may now, however,
return to our author, whose narrative will be found to confirm the above
statements of Bar-Hebraeus").

All findings fixed in a further revision (commit — see git log): the
misattribution corrected across the EH3 staging file, Doc_01 §1/§2/§6,
Doc_02 (Table A, author-gravity section, §8, verification loci), Step 0
§1, and Open_Gaps item 5; the Tritheist dispute recharacterized as
Trinitarian throughout; the "formulaic" wording in Step 0 rewritten to
match the claim-one/claim-two structure; the Sergius date replaced with
the vendored text's own vaguer "some years after" and flagged as
unconfirmed; the Jacobite overreach narrowed; the 586-616 schism/Heraclius
material added as a named (not yet researched) internal hinge in Doc_01 §2
and a new Open_Gaps item.

**This is the third round of substantial revision.** Per `cic-build-cycle`'s
own review-cycle rule, three rounds is the cap — if a further review still
finds substantial issues, this document must stop and escalate as an
unresolved tension rather than attempt a fourth round.

---

## Round 3 targeted recheck (against the Round 2 fixes, commit 6a822f4c) — CAP REACHED, ESCALATING

**Verdict: SUBSTANTIAL REVISION REQUIRED.**

The Round 2 fix corrected the original misattribution (crediting the
translator's own excursus to John of Ephesus) but overcorrected: several
passages now state John of Ephesus is *not* a source for the Tritheist
controversy at all, which is also false. Checked directly against
`cic/texts/john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`:
the translator's excursus runs c. lines 4471-4575 (the Ascunages creed, the
Condobaudite background, and the reported four-day disputation all sit
inside it — a translator's footnote around lines 4714-4726 even flags that
Bar-Hebraeus "substitutes the name of John of Asia for Stephan" in one
detail, casting further doubt on any claim that John himself took part).
But John's own narrative resumes at line 4580 (Conon's arrest) and covers
the Tritheite controversy at real length afterward — c. 300 lines,
including John of Ephesus himself refusing the Tritheites' bribes and
calling them heretics (~4625-4640), a debate ordered before the patriarch
and synod (~4700), John naming John Philoponus by name as the one who
"first led them into error" (~4777-4790), and the resulting Cononite/
Athanasian split (~4808-4880). The corpus-map staging file
(`cic/corpus-map/_staging/john-of-ephesus_ecclesiastical-history-part3_
paynesmith1860.yaml`) and Doc_02 §2's own verification-loci bullet already
state this correctly (excursus vs. John's own narrative, split at line
~4579). Five other passages do not:

- Doc_02 lines 25-27 ("is not John's own reporting")
- Doc_02 lines 158-160 ("**Not** the source for the Tritheist/Trinitarian
  controversy in Book I")
- Doc_02 lines 238-240 (the faction "known to this build via... translator's
  excursus, not John of Ephesus's own reporting" — false for Philoponus,
  whom John names himself)
- Doc_01 §6 (this build's "own knowledge of it comes from the... excursus...
  not from John of Ephesus's own contemporary narrative" — misleading; John's
  own narrative runs on for c. 300 lines)
- Open_Gaps item 5 ("the Book I controversy material... is the translator's
  excursus... corrected throughout" — too broad)

All other Round 2 findings (Trinitarian-not-Christological framing, the
Step 0 "formulaic" claim/A3 consistency, the Sergius of Tella date, the
Jacobite self-designation overreach, the 586-616 schism/Heraclius gap) are
confirmed FIXED, independently re-verified against the primary sources.
Mechanical checks all pass (`engine.m1.cross_world` exit 0,
`corpus_map_merge.py --check` exit 0, `texts_registry.py` only the two
pre-existing, unrelated fixture-synthetic problems).

**This is the third round of substantial revision. Per `cic-build-cycle`'s
own cap, this document set now stops and escalates as an unresolved
tension rather than attempting a fourth round.** The remaining fix itself
is narrow and precisely specified (reword the five passages above so they
match what the staging file and Doc_02 §2 already correctly state: the
Ascunages creed / Condobaudite background / four-day disputation are the
translator's own excursus via Bar-Hebraeus; the Tritheite schism narrative
from line 4580 onward, including John's own participation and his naming
of Philoponus, is John of Ephesus's own reporting) — but per this
project's own review-cycle discipline, applying it is not this build
thread's call to make unilaterally at this point. See
`Open_Gaps_Tracking.md`'s own final entry and this world's handoff report
to the project lead.
