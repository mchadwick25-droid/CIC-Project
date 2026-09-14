# WITHDRAWN — both versions of this source read are withdrawn in full

**Withdrawn 2026-09-14, on the project lead's direction.** Neither version of this read may be cited, and nothing in `Doc_04_Gravity_Discovery.md` relies on either.

- **Version 1** was audited by `Doc04_Round5_Review.md` and found **OVERSTATED**: it never searched `concili-` in a read testing a candidate named *Conciliar Authority Theory*; it reversed the polarity of Emeritus's speech at line 117505; it counted Migne's editorial apparatus as conference record, including a bishop who subscribes at the Lateran Council of **649**; its `mandat` count was ~45% low; and it missed two of Augustine's acts.
- **Version 2** — the rewrite below, which corrected several of those — was audited by `Doc04_Round6_Review.md` and found **UNSOUND**, which is worse. It asserted that lines 118500–125499 are Migne's footnote apparatus, having measured footnote-marker density **without opening the band**; the band in fact holds 40 numbered act headers, 138 `mandav*` subscription formulae and 401 `episcop-` tokens, and is the mandate-subscription roll-call. It attributed *illum tranquillissimum concilii locum* to Petilianus's act 9, when that phrase sits in the **right-hand column** of a two-column line and belongs to an edict about who may enter the venue — the same speaker-misassignment class version 1 committed, in the artifact written to correct version 1, with version 1's own two-column-bleed disclosure deleted.

**Two findings survive the withdrawal**, both independently confirmed at Round 6 and kept because they are checkable and narrow: Augustine subscribes the delegation's mandate in his own name at file line 121764 (normalized *mandatum suscepi et subscripsi*), which diagnoses the act-158 anomaly Registry row 65 records without explaining; and the Aurelius sentence at line 117492 exists, with the right speaker, on-axis. **Neither is relied on by Doc_04**, which now carries the whole question open at §7 Open Item 6.

**Why this file is kept rather than deleted.** Review artifacts in this world are immutable history. The two failures share one mechanism — *a check that proves something adjacent to the claim, then trusted because it returned something* — and version 2 demonstrates that the mechanism survives being named, documented, and deliberately guarded against by its own author. That is the most useful thing in this folder, and deleting it would destroy it.

**Recommended:** any future read of this source should be commissioned from a thread that wrote neither version, with its findings applied by a thread other than the one that reads.

---

# Targeted source read — the *Gesta Collationis Carthaginiensis* against Candidate 5's Persistence test

**Date:** 2026-09-14. **Superseded and rewritten the same day**, on the project lead's direction, after `Doc04_Round5_Review.md` audited the first version and found it **overstated**. This file replaces that version entirely. What the first version got wrong is recorded in full at the end, because three of its errors were the build's own documented failure mode and the record is worth more than the tidiness.

**Source:** `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (144,733 lines), the Migne *PL* XI printing recorded at `Source_Registry.md` row 65's Verification Note.
**Not a review round.** A source read, supplying evidence to a decision the build thread does not make. It reaches no classification.

## Quotation discipline

The scan's OCR is poor and its own provenance header warns against verbatim reliance. **Every reading below is a normalization, not a quotation.** Every claim is cited **by file line**, because act numbering is not unique across this volume.

## Structural finding, and the reason the first read went wrong

**The acts proper occupy lines 116000–118499 and 125500–130999. The band between them, 118500–125499, is Migne's own prosopographical footnote apparatus** — the editor's notes identifying bishops by the councils they attended. Measured by footnote-marker density per 500 lines, the apparatus band runs 9–27 markers with almost no numbered speeches, while the acts bands run 5–35 numbered speeches with almost none. **The first version of this read took its episcopal census from 118400–123000, which is substantially apparatus, not conference record.**

## Finding 1 — conciliar authority is invoked on the record, by bishops other than Augustine

An OCR-tolerant `concili-` sweep restricted to the acts proper returns a small, clean set. These are the on-axis passages:

- **Aurelius of Carthage, act 40, line 117492** — normalized: *Nec enim egredi possumus limitem istius mandati, quod nobis patres vel fratres nostri universalis concilii Ecclesiae catholicae, hic apud Carthaginem constituti, mandarunt.* He cannot go beyond the limit of the mandate which the fathers and brothers of the **universal council of the catholic Church**, constituted at Carthage, gave.
- **Line 118113** — the delegates describe themselves as *certi numero adsumus electi ab universali catholico concilio*: a fixed number, **elected by the universal catholic council**.
- **Line 127075** — *nostri, quibus universale concilium mandavit* — those to whom the **universal council** gave mandate. Possidius speaks immediately after.
- **Petilianus, act 9, line 116941** — on who may approach *illum tranquillissimum concilii locum* beyond the prescribed number: the council's own constitution as a procedural question, argued by the Donatist side.
- **Augustine, act 158, line 121764** — not a debate speech but **his own subscription to the mandate**: *mandatum suscepi et subscripsi*, at Carthage, before Marcellinus. This is why act 158 carries none of the speech formula the other acts share, which Registry row 65 had already flagged as anomalous without identifying the cause.

**So the delegation is not self-authorizing.** It is elected by, mandated by, and bound to the limit of a *universale concilium* — stated by Aurelius in his own voice, restated collectively twice, and subscribed by Augustine personally.

## Finding 2 — and it is genuinely contested, on the axis, between the two sides

**Emeritus of Caesarea, line 117497** — normalized: *Fidei causa est, quae et sine mandato ipso iure agi potest... Quid est quod de mandato, vel de obligatione mandati, de subscriptione, de modo, de formulis, quaeritur?* — it is a cause of faith, which can be pursued by right **even without a mandate**; why is there all this questioning about the mandate, its obligation, subscription, manner and formulae? He continues (117505): *superfluumque sit ceterorum mandatum, cum in uno consistat Ecclesiae tota persona* — the mandate of the rest is superfluous, since the whole person of the Church subsists in one.

**That is the disagreement, and it is precisely Candidate 5's axis.** The Catholic side grounds its standing in a universal council's mandate; the Donatist side answers that conciliar mandate is a formality irrelevant to the cause, since the Church's whole person subsists in one. Two rival theories of where authority above the individual bishop resides, argued on the record, by bishops who are neither Cyprian nor Augustine.

**The first version of this read cited line 117505 neutrally, as "a legal argument about whether the mandate of the remainder is superfluous," losing both the speaker and the polarity** — and so missed that the strongest evidence for the axis being *contested* was sitting in the sentence it had already found.

## Finding 3 — the scale, stated honestly

Within the acts proper there are **180 numbered speeches** across **93 raw speaker-tokens**, which collapse under OCR variation to roughly a dozen real persons: Marcellinus the *cognitor* (32 speeches), Petilianus (~20), Emeritus (9), Augustine (17, see below), Alypius (4), Aurelius (3), Fortunatianus (3), with Adeodatus and Possidius also speaking. **This is a small cast, not dozens of disputants** — the first version's "250 `episcop-` tokens across dozens of named bishops" counted Migne's footnotes and is withdrawn.

**Augustine speaks in 17 numbered acts, not fourteen.** Registry row 65 lists 50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, 267, 272; to these add **14** (line 125505, `Angustinus`), **230** (129294, `Autjuslinus`) and **252** (129318, `AM(jus!i?iMS`). All seventeen confirmed at their own lines. Row 65's instruction that any restatement carry the floor rather than assert fourteen flat is vindicated twice over.

**`mandat-` in the acts proper: 35 strict, 64 OCR-tolerant** (`mandalo`, `mandalum`, `mandali`, `mandaium`). The first version reported 58 across a span mixing acts and apparatus, using the strict pattern only.

## What this supports, and what it does not

**Supports:** the axis is attested in a second, independent, non-treatise setting; it is invoked by named bishops other than the two anchor figures (Aurelius, Petilianus); and it is genuinely *contested* between the two sides as a question about where authority above the individual bishop lies.

**Does not support:** a claim that conciliar authority theory was operative among *ordinary clergy* or shaped ordinary formation. The cast is a dozen delegates and a judge. Candidate 5's Formation test is untouched by this evidence and still does not pass.

**Does not support either:** the first version's framing of the *mandatum* as in itself an inter-episcopal authority instrument. In Roman procedure a *mandatum* is a procuratorial instrument — a power to act for a party — and much of the litigation about it at 411 is exactly that. **What is on-axis is not the mandate as such but its stated source: a universal council, which elects the delegates and binds their limit, and whose standing the other side denies.**

## What the first version of this read got wrong

Recorded rather than quietly replaced, because the pattern matters more than the corrections.

1. **It never searched `concili-`** — roughly 100 hits in its own declared span — in a read commissioned to test a candidate named *Conciliar Authority Theory*. It searched `mandat`, `plenari`, `auctoritat` and `primat`. The single most obvious term went unrun, and with it the Aurelius sentence that is the best evidence in the file.
2. **It reversed a passage's polarity.** Line 117505 is Emeritus arguing the mandate is beside the point; the read paraphrased it as neutral legal argument and used it to support the opposite conclusion.
3. **It counted editorial apparatus as conference record.** "Constantinus, line 119042" is a bishop subscribing at the **Lateran Council of 649** under Pope Martin, named in Migne's footnote (72) to gloss a place-name. He was cited as a 411 subscriber.
4. **Its `mandat` count was ~45% low**, excluding OCR variants — in the artifact that names too-strict searching as this build's documented failure mode.
5. **It missed two of Augustine's acts** (230, 252) and misdescribed a third (158 is a subscription, not a speech).

All five are the same mechanism in different clothes: **a check that proves something adjacent to the claim, then trusted because it returned something.** The correction that mattered was not a better pattern but a different move — enumerate the population and look at it, rather than pattern-match against it.
