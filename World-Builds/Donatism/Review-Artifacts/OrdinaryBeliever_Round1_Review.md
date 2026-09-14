# Adversarial Review — commit `a90b6665` (Donatism ordinary-believer pass, Round 1)

Independent Opus review of the first drafted revision addressing the 5-finding
fleet source-fidelity audit (average-believer coverage in `records/don/`).
Reviewed against `CLAUDE.md` in full. Verdict: **SUBSTANTIAL REVISION REQUIRED.**
Full findings and fixes are recorded in `don_Decision_Log.md`; this file
preserves the review's own text per this project's convention that the full
adversarial-review text lives in `Review-Artifacts/`.

## Findings, most severe first

### F-1 — BLOCKING. The Optatus addition self-disposes an escalation-category question reserved for the project lead

**File/field:** `records/don/doctrinal_witness/don.dw.what-we-did-with-the-power-we-had.md` — `text` (new circumcellion sentences), `positions[]`, `sources[]` (new Optatus III.4 entry), `confidence.divergence_note`.

The Optatus passage the diff draws on (`cic/texts/optatus_against-the-donatists.txt` ~lines 2000–2004) **is the Axido/Fasir passage**. The debt-relief and master/slave material is the immediate continuation of: *"in their insanity called Axido and Fasir 'Captains of the Saints,' no man could rest secure in his possessions."* The two quoted phrases sit two and four sentences downstream of that clause, inside one continuous narrative.

`World-Builds/Donatism/don_Decision_Log.md` line 506 records that `Doc_09_Story_Inventory.md` §6 **"declined to build this material into anything at all, calling it 'a genuinely live Article 23 question this document's own scope should not resolve casually.'"** Line 508 escalates it explicitly: *"whether the Axido/Fasir material should be removed... softened further, or left as currently hedged is named here as an open question for the project lead's own judgment, not self-disposed by this build thread."* Line 564 lists it as still open.

This diff builds that exact material into a **Tier-1, retrieval-enabled, participant-facing, emic** record with two direct quotations, and never names the reservation anywhere — not in the divergence_note, not in the body note, not in the commit message.

**Why it matters:** CLAUDE.md default actions — "Governance or methodology change → Always ask"; "Cross-world or portfolio-level decision → Always ask." And "A blocking review finding can't be dismissed by self-certification."

**Fix:** remove the two added Optatus sentences from `text`, the corresponding `positions[]` entry, and the new Optatus `sources[]` entry, pending the project lead's Article 23 disposition — or escalate the question explicitly rather than resolving it in passing.

### F-2 — BLOCKING. The new circumcellion clause merges existence-attestation with characterisation

**File/field:** same record, `text`, final clause of the circumcellion paragraph.

> "...we also will not wave it away as invention, **because the same account is the one imperial law eventually moved against, for reasons of its own.**"

Three problems:

1. **It violates `don.core.donatism` caution 4 verbatim:** *"its CHARACTERISATION is substantially shaped by that polemic, and the two must never be merged."* The clause uses the legal attestation (existence) as a reason to credit Optatus's characterisation. That is the merger, in the direction caution 4 names.
2. **It contradicts `don.contested.circumcellion-character`'s own `concedes` field:** *"No Donatist-voiced or non-mediated text in this world's own vendored corpus corroborates the group's character, scale, or typical conduct at all."*
3. **It is not accurate.** In Optatus III.4 the party that moved against them was **Taurinus**, a civil official acting on a letter from the **Donatist bishops themselves** — not imperial law. The Theodosian anti-circumcellion legislation is separate and later.

Compounding it, the record's own closing note still asserts *"The Circumcellion paragraph holds `don.core.donatism`'s caution 4 split exactly."* After this edit, it does not.

**Fix:** delete the causal clause. If any version of the paragraph survives F-1, it should end at "...in that manner or that often."

### F-3 — BLOCKING. The forced-rebaptism paragraph reverses the discipline it claims to follow, and certifies the reversal inside the record that set the rule

**Files:** `don.dw.becoming-one-of-us.md` (`text` ¶3), `don.limit.bagai-violence-no-account.md` (new body note).

`don.limit.bagai-violence-no-account`'s own `why_sources_cannot_answer` quotes Doc_09 §8 item 3 and generalizes it: *"this record follows the identical discipline: **it states the limit itself, not the allegations' own content**, and does not repeat the specific charges as though this world could confirm or dispute them."* Its body note adds: *"it names the limit, once, at the level of generality Doc_09 itself uses."*

I read Doc_09 §8 item 3 directly (line 130). The **first** of the three allegations it covers is *"the forced rebaptism of the 'Mappalians'"* — i.e. the Crispinus episode. So the new paragraph narrates the content of an allegation this world's own governing document decided not to narrate: number, location, and an embedded hostile quotation, in first-person emic voice.

That may be a defensible change. What is not defensible is the note added to `don.limit.bagai-violence-no-account`:

> "...under the **identical discipline** this record established first -- name the charge, do not confirm it, do not deny it."

The discipline this record established was *not* to name the charge's content. The diff changed the rule and wrote into the rule-setting record that it hadn't. The limit record now points at a record that breaks the limit.

**Fix:** either revert to limit-naming, or escalate the methodology change to the project lead with Doc_09 §8 item 3 in front of them — and in either case correct the bagai-violence note, which currently misdescribes what happened.

### F-4 — MAJOR (source fidelity). "in a single day" appears in no source

**Files/fields:** `don.dw.becoming-one-of-us.md` — `text` ("forcing eighty of its tenants into that water **in a single day**") and `positions[]` ("forcing eighty tenants into the water **in a day**").

Latin, `augustini_scripta-contra-donatistas..._petschenig1908-1910.txt` lines 30829–30832 (*Contra litteras Petiliani* II.83.184):

> "...non dubitauit in fundo catholicorum imperatorum... **uno terroris impetu** octoginta ferme animas miserabili gemitu mussitantes rebaptizando submergere?"

`uno ... impetu` = "by a single onset/assault of terror." NPNF (npnf104 line 17447) renders it **"under the sole influence of terror"** — the exact phrase the record quotes two clauses later. There is no day anywhere in the Latin or the English. This reads as `uno ... impetu` being rendered twice: once correctly as the quotation, once as a fabricated time detail.

**Why it matters:** "Source fidelity — never invent." **Fix:** delete from both fields.

### F-5 — MAJOR (source fidelity). "young" is an invented age

**File/field:** `don.dw.becoming-one-of-us.md`, `text`: "seized **a young Catholic** still under instruction at Constantina."

Petschenig lines 71989–71990: *"laicum nostrum catechumenum natum de parentibus catholicis Peti[li]anus tenuit"* — "a layman of ours, a catechumen, born of Catholic parents." No age term. CLAUDE.md is explicit: **"No invented family, age, personal history, or anecdote."**

**Fix:** "a Catholic layman still under instruction." "Born of Catholic parents" is available if the sentence wants a detail.

### F-6 — MAJOR. "tenants" is imported from the source the record says it deliberately did not use

**Files/fields:** `don.dw.becoming-one-of-us.md` — `text`, `positions[]`, `tensions[]`, and `sources[]` locus.

The cited locus (Answer to Petilian II.84.184) says **"eighty souls"** on *"a farm belonging to the Catholic emperors"* — never tenants. "Tenants" comes from Letter 66 / the NPNF editorial introduction (npnf104 line 10292: "had bought a state farm at Mappalia, and had rebaptized the tenants"). The record's own body note says Letter 66 was **"Left deliberately unused."**

Doc_09 §8 item 3 already did this exact analysis and warned against it: the Letter-66 tenant/landlord framing *"is not Augustine's own wording but the NPNF translator's own endnote (n. 1877)... attributed here to the editor, not silently presented as the letter's own allegation."*

Related, smaller: the `sources[]` locus reads "Book II, ch. 84, SS184 — Crispinus of Calama **and the farm near Hippo**." "Near Hippo" is attested at **ch. 100** (npnf104 line 17931: "bought a farm near our city of Hippo"), not at ch. 84.

**Fix:** "eighty souls" (Latin is *octoginta ferme*, "about eighty"; NPNF's "no less than eighty" is itself loose); drop "tenants"; re-cite or drop "near Hippo."

**Credit where due:** the pass quietly improved on Doc_09 here without noticing. The "eighty" figure **is** Augustine's own body text at II.83/84.184 (*octoginta ferme animas*), unlike the Letter-66 instance Doc_09 attributes to the editor. Doc_09 §8 item 3 is now narrowly out of date and should be updated to say so.

### F-7 — MAJOR. "the identical charge the other way" is wrong, and the review note's reasoning inherits the error

**File/field:** `don.dw.becoming-one-of-us.md`, `text` ¶3 and closing body note.

> "The same opponent brings the identical charge **the other way**: that a bishop of ours, Petilian..."

Both charges run the same direction — Augustine accusing Donatists. Crispinus and Petilian were **both Donatist bishops**. The closing note compounds it:

> "this world's own discipline does not get to believe the charge against **an opponent's bishop** more readily than the charge against its own."

Crispinus was not an opponent's bishop. Petschenig line 48818: *"Crispinus Calamensis **uester** episcopus."* npnf104 line 10355: "Crispinus, the Donatist bishop of Calama." The whole stated rationale for treating the two charges identically rests on a misreading.

Related and in the same direction: the `text` calls Crispinus **"a landholder of ours"** while calling Petilian "a bishop of ours." Crispinus was a bishop too. Demoting this world's own bishop to a landholder softens its institutional implication in the charge — the precise softening this record says it refuses.

**Fix:** "a matching charge against another of our bishops"; name Crispinus as a bishop of ours who bought a farm; rewrite the note's rationale.

### F-8 — MODERATE. Adeodatus: the underlying Latin is visibly corrupt and undisclosed; and the "boast or admission" hedge is a false binary

**File/fields:** `don.dw.becoming-one-of-us.md` — `text`, `confidence.divergence_note`, `tensions[]`, body note.

**What checks out:** act 154 ✓, first cognitio ✓, line range 121373–121387 ✓, Adeodatus is a Donatist bishop speaking in his own voice against the Catholic Severianus ✓, and the translation is fair.

**What doesn't.** `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` line 121385 literally reads:

> `mei  lcrrore  succubucrunl  omnes,  qui  in  eodcm  loco` / `COnSliluli  crant.`

The rendered English requires four silent emendations (*lcrrore→terrore*, *succubucrunl→succubuerunt*, *COnSliluli crant→constituti erant*) and drops *Etiam* and *eodem*. The vendored file's own header says quotations from it need *"careful visual cross-check... before being relied on for a verbatim claim,"* and `don.core.donatism` caution 2 calls this scan **"this corpus's worst OCR on record for a text of that significance."** The record discloses only "not visually cross-checked against a page image" — which understates it — and, unlike the Petilian Latin, never says the English is this build's own translation with no established English edition.

**On the hedge.** In context the reading is not 50/50. Severianus claims the place was always Catholic; Marcellinus asks *"utrum in ea plebe episcopus nunc sit"*; Adeodatus answers *"In plebe mea est, circum circa meum est totum. Etiam mei terrore succubuerunt omnes..."* The tone is plainly an assertion of dominance — a boast. What is **not** ambiguous is the content: *terrore* is Adeodatus's own word, and on either tone it concedes fear did the work. The record's framing lets a reader hear the coercive content itself as unsettled, which it is not. **This is over-caution running in the direction that flatters the world.**

**Fix:** say the tone reads as a boast and that the boast *is* the admission. Move the OCR condition and the own-translation disclosure into `confidence.divergence_note` — matching how the Petilian Latin and the virgins passage were handled.

### F-9 — MODERATE. "OCR clean" is claimed at the one word that isn't

**File:** `don.dw.becoming-one-of-us.md`, body note: the Sermo ad Caesarienses lines are "**OCR clean**, translated here directly."

Petschenig line 71990 reads **`Petialius tenuit`**. The corrupt word is the name of the man the entire charge is attributed to. The identification is contextually secure (Constantina was Petilian's see), but it is an emendation, not a clean reading.

**Fix:** state the emendation rather than claiming clean OCR.

### F-10 — MODERATE. A Contested, OCR-only, self-translated source now carries load-bearing content in a record whose confidence block still reads A / verified-direct / Widely Accepted

**File/field:** `don.dw.what-belonging-cost.md` — `confidence`, `tensions[]`, `text`.

`don.story.passio-donati-sermon`'s own confidence block: `formation_confidence: Contested`, and *"The text survives only in raw, uncorrected Latin OCR and no established published English translation was consulted... close literal renderings, not certified translation."*

The content itself verifies. PL8 lines 649–662, chapter **XIII**. But `what-belonging-cost` kept `citation_specificity: A` / `verified-direct` / `Widely Accepted`, and its `tensions[]` named only the author/date dispute — not the OCR condition or the fact that this English is a fresh, unpublished rendering. CLAUDE.md: "Never present a disputed claim as settled."

Smaller: **"pietas"** rendered as **"love."** In this sentence it is kin-duty / family devotion — which is the entire reason the passage was cited. "Love" loses the point.

**Fix:** carry the OCR + own-translation caveat into `confidence.divergence_note`; render *pietas* as family devotion, not love.

### F-11 — MODERATE. A superseded overclaim was left standing in the field it lives in

**File/field:** `don.limit.no-ordinary-day-survives.md`, `sources[]`:

> `locus: Optatus I.16 and Augustine Letter XLIII SS26 - **the whole of what survives on women among us**`

The same record's own new body note says this citation *"had... become narrowly overstated,"* and its `divergence_note` now names a third trace. The record contradicts itself in its own front matter. CLAUDE.md "Fix it right": *"No fix on a fix. If a previous fix was wrong or incomplete, undo it and redo it right."*

**Fix:** amend to "...the whole of what survives on women among us **in their own names**" (or equivalent).

### F-12 — MINOR. Self-contradiction inside the circumcellion paragraph

Independent of F-1/F-2: the paragraph says *"we will not repeat that portrait as though it were a police report"* and then repeats the portrait across four clauses with two direct quotations. If any version survives, the refusal sentence and the repetition cannot both stand as written.

### F-13 — MINOR. Quotation mechanics, all drifting the same way

- `"The condition of masters and slaves was completely reversed"` — Optatus has this mid-sentence after *"By the judgement and command of these outlaws,"*. Capitalized without brackets, no ellipsis.
- `"most of our laity, **in his words**, confess this one point in our system displeases them"` — De Baptismo I.5.6 (npnf104 line 12744) says **"almost all their laity."** "In his words" is attached to a quantifier he did not use.
- "**some** who wished to join us" — the source says **"many** who... wish to secede to them."

Each shift is small; all three run in the direction that makes this world look better. **Fix:** restore "almost all" and "many"; bracket or re-cut the Optatus quotation.

### F-14 — MINOR. The pass is recorded only inside the records it changed

No entry was added to `World-Builds/Donatism/don_Decision_Log.md` for the audit, the five gaps, or the three deliberately-unused leads named in the `becoming-one-of-us` body. CLAUDE.md: *"Every known gap, open question, or review outcome belongs in that world's Open_Gaps_Tracking.md — never left to live only in a conversation thread."*

## What checks out — verified independently, not taken on the diff's word

1. **The baker/boycott correction is CORRECT.** Direct re-read of npnf104 line 17440 confirms: the baker is the enforcer; the Catholic deacon-landlord is the one cut off. NPNF's own endnote 2198 settles it. The Latin (Petschenig 30821–30828) confirms. The original fleet audit had it backwards; the drafting pass's correction is right, and both quoted phrases are verbatim.
2. **Reciprocity on the two new cross-references is correct** — zero findings on either new pair.
3. **The gate-battery claim is CORRECT — verified by differential build.** 17/18 gates pass at both baseline and HEAD; reciprocity fails identically at 55 findings both times. No new reciprocity findings introduced.
4. **Schema and world_id are clean.** All 6 files parse as valid YAML; all carry `world_id: donatism`; no `canon_cells` were touched; all referenced `source_id`s resolve.
5. **No duplication** found across `records/don/`.
6. **The virgins passage is sound** — and the record under-claims it, if anything.
7. **Register and voice hold** — emic first-person throughout, no academic hedging, no AI tells.

## Overall verdict

**SUBSTANTIAL REVISION REQUIRED.** Ten items must change (F-1 through F-8, F-10, F-11); F-9, F-12, F-13, F-14 to be swept in the same pass. Full disposition recorded in `don_Decision_Log.md`.
