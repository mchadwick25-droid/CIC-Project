# Adversarial Review — Step 5 (`voice_craft` + `demonstration`), `records/ijc/`

**Branch:** `world/ijc` (151 records) · **Reviewed:** 2026-08-22 · **Reviewer:** isolated Opus dispatch, cold adversarial pass on the nine new step-5 records
**Scope:** `records/ijc/voice_craft/ijc.voice.craft.md` and the eight files in `records/ijc/demonstration/`. The 142 answer-canon records are in scope only where a demonstration cites them — a citation is checked against the record, and the record's own load-bearing claims re-derived from the vendored corpus where the demonstration leans on them.
**Method:** every one of the nine files read in full, field by field. Every `sources[]` target opened and read in full; every claim in every representative turn traced to a cited record, and where the record's own warrant is a vendored line range, the range re-opened in `cic/texts/` and read past the sentence that states it (the standing failure mode named in BUILD-LOG §8). Nothing accepted from BUILD-LOG §9's own account of what the demonstrations do. Pronoun discipline machine-scanned (regex over every `exchange[].text` for `I/my/me/mine/myself`, with context printed for each hit) rather than eyeballed. Demo turns diffed sentence-by-sentence against the source-record text they were drafted from. Readability computed with the build's own `fk_grade` on every turn, against the `alx` demonstrations as the baseline. Gate battery run directly via `engine.m1.loader.load_world_records("ijc")` + `engine.m1.gates.run_all`, and the compiled-field contract re-read from `engine/m2/builders.py`'s own `build_prompt()` to establish what actually reaches a live model.
**Model checked against:** `origin/world/alexandria` — `records/alx/voice_craft/alx.voice.craft.md`, all seven `records/alx/demonstration/` records, and `reference/fleet-voice/EXEMPLAR-TRANSCRIPT.md` (v4). **Spec checked against:** `reference/Redesign-Spec/CiC-Program-Spec.md` §4.3.5 (the demonstration list), §4.2/§6 (the canon), O2/O4 (register and readability).
**Prior artifacts read:** BUILD-LOG.md in full; `Review_Confirmation_Pass_2.md` (format and severity calibration), `Review_Confirmation_Pass.md`, Reviews 1–3.

---

## Summary verdict: REVISION REQUIRED before this set is treated as the register lever. 29 findings (3 HIGH, 12 MEDIUM, 14 LOW)

**The good part first, and it is substantial.** The thing this review was most likely to catch is not there. The pronoun discipline holds *exactly* — a machine scan of all eight representative turns returns exactly two first-person-singular hits: the sanctioned self-naming, used once, in `ijc.demo.f6-p-someone-like-me`, the one turn whose participant question is actually about the voice's own nature, unpaired with any in-world role label and followed by "we" for the rest of the turn; and "This is My Body," a scriptural citation inside a cited teacher's words. The deliberately *unused* exception in `ijc.demo.f6-p-woman-authority` matches the fleet precedent exactly, and its craft note gives the right reason. No turn narrates a personal career, a biography, or a located individual's day; every "we" is aggregate. The persona name and role label appear nowhere in any compiled field. A pattern scan of `identity`, `guard`, all `flavor_notes[].note`, all `characteristic_concerns[]`, and all sixteen `exchange[].text` values for ISO dates, "RULED", "Mark", `Doc_XX`, record ids, sibling-world names, thread/review references, and build vocabulary returns **one** hit, inherited verbatim from the `alx` model (L9). All eight `canon_question_id`s resolve, and all eight `canon_cells` match their canon question's own cell. The Homoian turn is genuinely spoken from outside the confession while naming it as the empire's own established church for two reigns — the binding Step 0 §4.1 obligation, met. Gates: **13/13 clean over 151 records, zero findings in every gate.**

The verdict falls short for a different reason than the three prior rounds, and it is worth stating precisely: **this round did not repeat the citation-mechanics failure — it repeated the *scope* failure, in a new place.** Eight demonstration turns were drafted by compressing already-verified records into speakable prose, and compression is where hedges die. Four of the six defects that matter are a source record's own carefully-won qualification — one of them added by the *previous* review round, twice — deleted in the retelling, leaving a flat assertion in the one field a live model imitates. Two are worse than that: a claim no record in this build supports, and a quotation that does not exist in the form it is quoted in.

1. **One invented historical fact.** `ijc.demo.f6-p-hypocrisy` says Ambrose "twice held a basilica against imperial command." Nothing in this build's 151 records says twice. The record set has exactly one basilica standoff, and its own `absent_detail` treats the 385/386 question as a *dating divergence about that one event*.
2. **One quotation that is not a quotation.** `ijc.demo.f6-i-never-settled` puts the Chalcedon acclamation inside quotation marks with three sentences — including the anathema — silently elided and replaced by a dash.
3. **One false statement about this world's own transmission,** in the turn whose entire job is to state that transmission honestly (`ijc.demo.f6-p-someone-like-me`).
4. **The hardest-won hedge in the whole record set — the Justina attribution divergence, added at one confirmation round and corrected again at the next — is simply gone** from the turn that speaks that record, and the demonstration's own craft note claims it is carried.

None of this reopens Step 0, Doc_01, or the answer canon's settled ground. All of it is a short pass to fix, and most of it is a sentence each.

## What was checked

| Scope | Checked |
|---|---|
| The 9 new records | **9/9** read in full, front matter and trailing body |
| `sources[]` targets | **12/12** distinct cited records opened and read in full |
| Vendored re-derivation | Chalcedon Session II acclamation (`npnf214:19996–20007`); Canon 28 (`:22223–22232`); Percival's Canon 28 excursus (`:22336–22399`); Leo *Tome* ch. IV (`npnf212:5365–5381`); Leo *Ep.* XCV in full (`npnf212:8586–8620`); Ambrose *Ep.* XX §§1–8, 24 (`npnf210:41451–41530`, `:41778`); *Ep.* XLI headnote, §1, §§27–28 (`:43547–43570`, `:43943–43995`); *De Mysteriis* IX §§50–55 (`:33199–33285`); Nicene Creed (`npnf214:2408–2418`) |
| Pronoun discipline | **16/16** turns regex-scanned, context printed per hit |
| Compiled-field leakage | `identity`, `guard`, 8 × `flavor_notes[].note`, 5 × `characteristic_concerns[]`, 16 × `exchange[].text` pattern-scanned |
| Canon conformance | 8/8 `canon_question_id` → cell match, participant text diffed against canon question text character-for-character |
| Register/readability | `fk_grade` on all 8 turns + `identity`/`guard`, against all 7 `alx` turns |
| Compiled contract | `build_prompt()` re-read — **`demonstration.exchange` is compiled into `prompt.txt`** |
| Mechanical gates | **13/13 clean**, 151 records, 0 findings |

---

## HIGH

### H1 — `ijc.demo.f6-p-hypocrisy`: "twice held a basilica against imperial command" is a fact no record in this build carries

The turn reads:

> The same bishop who **twice held a basilica against imperial command**, and once made an emperor do public penance for a massacre, wrote to have that order reversed…

The demonstration's own `sources[]` are `ijc.story.callinicum-synagogue` and `ijc.gravity.episcopal-independence`. Neither says twice. The gravity says "**the** basilica held in 386 against a Homoian court," and its `manifestations[]` list "the 386 basilica standoff" as one item. `ijc.figure.ambrose.dates.floruit` lists "the basilica standoff 386" — singular, in a floruit that otherwise enumerates every episode separately (384 Altar of Victory, 388 Callinicum, 390 Thessalonica). `ijc.story.vigil-in-basilica` is one standoff. A grep of every "basilica" occurrence in `records/ijc/` returns no second episode anywhere.

Worse than unsupported: it cuts against the build's own disclosed position. `ijc.story.vigil-in-basilica.absent_detail` carries, as a first-class contested-dating disclosure, that "this record dates the standoff to 386… but the vendored edition itself dates Ep. XX and the enabling law to Easter, 385" — i.e. the build treats 385 and 386 as *two datings of one standoff*. A turn that says "twice" quietly converts that disclosed divergence into two events and answers, by assertion, a question the record set deliberately holds open.

I checked whether the vendored text would rescue it. It half does and half does not: *Ep.* XX §1 (`npnf210:41455–41458`) reads "this time it was **not the Portian basilica**, that is the one outside the walls, which was demanded, but the new basilica," which implies a prior demand — and §3 has the Prefect asking for the Portian one as a fallback in the *same* crisis. So a "twice" is arguable in the wider scholarship; it is not arguable *from this build's records*, and this build's own discipline is that a demonstration speaks the record, not the scholarship.

**Why HIGH:** this is the project's own named failure mode (a real fact carried at the wrong scope) in the one field type that reaches a live model as an example to imitate, at `verification_state: verified-direct` / `formation_confidence: Documented`, in a turn whose stated purpose is "we will name our own sharpest case rather than a safer one."

**Fix:** "The same bishop who held a basilica against imperial command, and made an emperor do public penance for a massacre…" — or, if the doubling is wanted, build it first in `ijc.story.vigil-in-basilica` against *Ep.* XX §§1–3 and reconcile it with that record's own 385/386 disclosure, then speak it.

---

### H2 — `ijc.demo.f6-i-never-settled`: the Chalcedon acclamation is quoted in a form that does not exist, with an unmarked elision that removes the anathema

The turn reads:

> When Leo's Tome was read to the bishops gathered at Chalcedon, they cried out: **'This is the faith of the fathers - Peter has spoken thus through Leo.'**

The build's own quote record `ijc.quote.peter-has-spoken` (verified verbatim, `license: verbatim`) carries:

> After the reading of the foregoing epistle, the most reverend bishops cried out: This is the faith of the fathers, **this is the faith of the Apostles. So we all believe, thus the orthodox believe. Anathema to him who does not thus believe.** Peter has spoken thus through Leo.

Re-derived from the file — `npnf214:19996–20001` — the record is exact. So the demonstration has taken a licensed verbatim quote, deleted three sentences from the middle of it, joined the two surviving fragments with a hyphen, and enclosed the result in quotation marks with no ellipsis and no disclosure anywhere in the record.

Three things are wrong at once. (a) It is presented as the bishops' words in the order they said them, and it is not. (b) The elision is not neutral: what is removed is the acclamation's anathema — the sharpest thing the assembled council actually shouted — so the softened version reaches a participant as the whole of it. (c) It is a regression against the source record the demonstration was drafted from: `ijc.story.tome-that-would-not-bend` handles the same material *without* quotation marks precisely because it compresses ("the session record has them crying out: This is the faith of the fathers - Peter has spoken thus through Leo"), which is honest narration; adding the quotation marks converted a compression into a false citation.

**Why HIGH:** this world's entire discipline is that when something is quotable it *is* a quote (register statement 6), verified character-level, licensed, and recorded. This is the first place in 151 records where quotation marks enclose text that no source says. It is also the exact defect family — an edition's or a teller's construction presented as the primary voice's own words — that HIGH findings in three consecutive rounds have been about.

**Fix:** either drop the quotation marks and keep the story record's narrated form, or quote the acclamation as it stands with a marked ellipsis: "This is the faith of the fathers, this is the faith of the Apostles… Peter has spoken thus through Leo." The second is better — the fuller acclamation is more powerful, not less.

---

### H3 — `ijc.demo.f6-p-someone-like-me`: the world's one congregational glimpse is attributed to the wrong kind of source, erasing the record's only outside corroboration

The turn's load-bearing limit sentence reads:

> The nearest thing we have is a crowd glimpsed once, singing through a whole night under siege, and **even that reaches us inside a bishop's own letter about himself.**

The demonstration cites `ijc.story.vigil-in-basilica` for exactly this ("the one direct congregational glimpse"). That record says the opposite of what the turn says. Its own `narrative_tier_justification` reads: "**two independent, named, near-contemporary sources** — Ambrose's own letters and sermon from inside the crisis, **and Augustine, an eyewitness in the same city**"; its text says "Augustine, who was in the city, remembered it plainly: the pious people kept guard in the church, prepared to die with their bishop. And it was then, **he** says, that Milan began to sing." `ijc.contested.office-holder-scope.held_against` names it "the 386 vigil, **through Augustine's eyes**," and `ijc.story.callinicum-synagogue.absent_detail` uses it as its contrast case: "unlike the 386 standoff, **which Augustine's testimony corroborates from outside**."

Whichever source the sentence means, it is false as written:

- **If it means Ambrose's letter** — the natural reading of "a bishop's own letter about himself" — it deletes the world's only independent witness to its own single congregational scene, and does so in the turn whose whole purpose is to state the record's limits accurately. Re-derived: *Ep.* XX carries the crisis in Ambrose's own hand but the night-long singing is not in it; §24 (`npnf210:41778–41782`) has only "We repeated Psalms with the brethren in the smaller basilica of the Church," and the hymn reference in the *Sermo* (`:42629`) is Ambrose defending himself against the charge that the people were "led astray by the strains of my hymns." The vigil, the readiness to die, and the singing's origin are Augustine's.
- **If it means Augustine** — bishop of Hippo by the time he wrote — then the *Confessions* is not a letter, and he was a layman in Milan at the time of the event, which is precisely why the build treats him as corroboration from outside the chancery.

**Why HIGH:** the sentence overstates the record's own thinness in a compiled field, in the turn the spec makes mandatory for identity-collision cells, and it contradicts its own single cited source. An honest limit stated *more* pessimistically than the record warrants is still a false statement about the record, and it throws away the one datum that makes this world's F5/F6-P answer more than hearsay.

**Fix:** "…and even that reaches us at second hand — through a bishop's own account of his own standoff, and through one man who was in the city that night and wrote it down years later." That is both true and stronger.

---

## MEDIUM

### M1 — `ijc.demo.f6-p-woman-authority` deletes the Justina attribution divergence its source record was corrected twice to carry, and the craft note claims otherwise

`ijc.dw.f6-p-women-authority-cost` carries, in `text`:

> Justina, mother and dominant influence over her young son — **no formal regency is attested** — is named by this world's own transmission as the one behind the machinery… **Ambrose's own letter names the emperor as the one acting on his own power; it is the volume's own chronology that names Justina as the persecution's author. Either way,** real coercive power moved through her court.

and a mandatory non-null `divergence_note` saying the same thing, both added at the first confirmation round (§7 M4) and re-corrected at the second (§8) after `positions[]` was found out of sync.

A sentence-level diff of the demonstration against that text shows the demonstration keeps the coercive detail and drops **both** hedges: "no formal regency is attested" is gone, the two-source conflict sentence is gone entirely, and "Either way, real coercive power moved through her court" becomes the flat "Real coercive power moved through her court." The demonstration then sets `verification_state: verified-direct`, `formation_confidence: Documented`, **`divergence_note: null`** — a record asserting, at settled confidence and with no note, a claim its own sole source is required to carry a divergence note for. The gate cannot catch it (`gate_confidence_crosscheck` exempts `verified-direct`), which is exactly why it needs an eye.

The demonstration's own trailing body then states: "Content is `ijc.dw.f6-p-women-authority-cost`'s own text, carried into spoken form **without addition: every coercive detail, the Justina/emperor attribution divergence the source record itself states**… are all already verified." The divergence is not in the turn. A craft note asserting a property the content does not have is how this defect survives a reader.

**Fix:** restore one clause — "our own bishop's letter names the emperor as the one acting; it is the record's own chronology that names her as the author of it — either way, real coercive power moved through her court" — set `divergence_note` on the demonstration to match its source, and correct the body.

### M2 — `ijc.demo.f6-p-woman-authority`: "Leo himself thanks her directly" is not what *Ep.* XCV says

The turn: "Leo himself **thanks her directly** for her own command that it be held, and for **overruling** his own request that it sit in Italy instead."

Re-derived in full, `npnf212:8601–8618`. Leo's thanks are to God, not to Pulcheria: "I recognize in everything, and **give God thanks** at seeing you take such interest in the universal Church." Of her command and his overruled request he says only that he received them without scorn: "**Your clemency's command**, therefore, that a Synod should be held at Nicæa, and **your gently expressed refusal of my request** that it should be held in Italy… **I have received in a spirit so far removed from scorn as to** nominate two of my fellow-bishops… to represent me."

Everything load-bearing survives — she commanded the synod (the letter's own argument line at `:8597` reads "the Council **ordered by her**"), and she refused Leo's counter-proposal. But "thanks her directly for… overruling" inverts the letter's actual posture, which is a bishop conspicuously *not* objecting. The overstatement originates in the doctrinal_witness (`Leo himself thanks her for her own command`) and is amplified in the demonstration by "directly" and "his own request… instead" — so both records need the fix.

**Fix:** "Leo himself records her command that the council be held, and her refusal of his own request that it sit in Italy — and answers by sending his legates without protest."

### M3 — `ijc.demo.f6-p-hypocrisy` states the *public* penance as flat fact, which `ijc.story.emperor-penance` exists to quarantine

The turn: "…and once made an emperor **do public penance** for a massacre."

`ijc.story.emperor-penance` is built around this exact distinction: "**That much is documented plainly**" covers Ambrose's private letter, the demand for repentance before the altar, and the emperor's submission. Of the public scene it says: "**The famous scene** — the emperor laying aside the purple, weeping his sin publicly in the church at Milan — **is told within a generation by two church historians, Sozomen and Theodoret**… What the contemporary record itself holds is harder and quieter." Its `absent_detail` closes: "**Theodoret's dramatized scene is quarantined by name inside the telling - the tiers never mix.**"

The demonstration does not cite that story; it cites `ijc.gravity.episcopal-independence`, whose description does say "public penance demanded and performed" flatly. So the demonstration is faithful to the looser of two internal formulations, and speaks unhedged, in a compiled field, the one detail this world's own story record quarantines by name. The record-set inconsistency is worth fixing at both ends.

**Fix:** in the turn, "…and once shut an emperor out of the sacrament until he repented of a massacre" — documented, and stronger. Separately, align `ijc.gravity.episcopal-independence.description` with the story's tier discipline.

### M4 — `ijc.demo.f6-i-never-settled`: "in the canon's own words" introduces a paraphrase, and a build-coined line sits inside Leo's reported reasoning

Two attribution markers in one turn do work they have not earned.

**(a)** "…because, **in the canon's own words**, the fathers rightly granted privileges to old Rome as the royal city, and **the new royal city** should be magnified the same way." Canon 28, verified at `npnf214:22223–22232` and carried exactly in `ijc.quote.canon28-equal-privileges`, reads: "For the Fathers rightly granted privileges **to the throne of** old Rome, **because it was** the royal city… justly judging that the city which is honoured with the Sovereignty and the Senate… should **in ecclesiastical matters also be magnified as she is**, and rank next after her." "The new royal city" is not the canon's phrase (the canon says New Rome), "the same way" is not "as she is," and the whole is a compression. The phrase "in the canon's own words" tells a participant this is quotation. It is paraphrase.

**(b)** "…and wrote to emperor, empress, and bishop alike why: **things secular stand on a different basis from things divine - rank near a throne is not the kind of claim an apostle's grave makes.**" The first clause is Leo's, verbatim (`ijc.quote.leo-things-secular`, `npnf212:9078–9084`). The second is this build's own coinage, carried over from `ijc.story.tome-that-would-not-bend`, and it is the most quotable sentence in the turn. It sits inside a colon-introduced report of what Leo wrote, undifferentiated from the words that are actually his — register statement 6 in reverse.

**Fix:** change "in the canon's own words" to "on the canon's own reasoning," and either attribute the apostle's-grave line as gloss ("what that meant, in our own way of putting it, is that…") or drop it and let Leo's own sentence close the movement.

### M5 — `ijc.demo.c-i-who-was-jesus` drops the Homoian tension at the first-tested cell, and never cites its own answer-ground

Two problems, one record.

**(a) The uncited answer-ground.** The turn is `ijc.dw.c-i-jesus.text` put into we-voice — the diff is nearly clause-for-clause, including the soteriological argument ("if the Son is not truly God, then what he gives is not truly God's to give"), "the way men write what they are prepared to be exiled over," and the closing synthesis. `sources[]` cites only the two quote records. Every other demonstration in the set cites its answer-ground record; this one does not, so the turn's most interpretive content traces to nothing in its own citation block.

**(b) The dropped tension.** `ijc.dw.c-i-jesus.tensions[0]` reads: "the confessed center **was contested inside the establishment itself** - for two reigns the empire's own church preferred 'like the Father,' and the word the creed chose was resisted by men present when it was chosen." The demonstration keeps everything else from that record and drops this. The result is a center-cell answer — the cell the canon's own priority rule tests **first**, at every admission — that says "Our creed answers first," calls the Nicene definitions "our devotion," and narrates "A century of councils spent itself making those words exact" with no hint that for two decades of that century the empire's own church confessed otherwise. Step 0 §4.1's Homoian recentering is binding, and `world_core.cautions` §2 says so; `ijc.demo.f1-i-argued-about` honors it beautifully, but a participant who asks only the center question never hears it, and the voice's "we" there sounds like the winning side narrating a settled outcome backward — the thing `ijc.voice.craft.characteristic_concerns[4]` says this voice does not do.

**Fix:** add `ijc.dw.c-i-jesus` to `sources[]`, and add one sentence from its own tensions field — e.g. after "A century of councils spent itself making those words exact": "and it was not a settled thing while it was happening — for two imperial reigns our own establishment confessed the Son *like* the Father instead."

### M6 — `ijc.demo.f1-t-bread-and-cup` speaks ~60 words of Ambrose's translated text as unattributed narration, with no quote record anywhere in the set

The turn's body is *De Mysteriis* IX §§50, 54, re-derived at `npnf210:33203–33271` and near-verbatim in the NPNF translator's wording: "this is not what nature made, but what the blessing consecrated, and the power of blessing is greater than that of nature, because by blessing nature itself is changed"; "The Lord Jesus Himself proclaims, 'This is My Body.' Before the blessing of the heavenly words another nature is spoken of, after the consecration the Body is signified. He Himself speaks of His Blood. Before the consecration it has another name, after it is called Blood."

The demonstration carries all of it with one three-word attribution — "**one of our own teachers said**" — no name, no quotation marks except around the dominical sentence, and no `ijc.quote.*` record for *De Mysteriis* anywhere in the 151 (the twenty quote records contain none). This inverts H2: there, a paraphrase was dressed as a quote; here, a translator's actual sentences are dressed as the voice's own paraphrase.

It also breaks this world's own compiled instruction. `ijc.voice.craft.flavor_notes[0]` says: "Answer first, **then cite** - the first sentence carries the answer; **the source follows it, named**, the way this world's own letters argue." Every other demonstration names its figure — Leo twice, Justina, Pulcheria, "the local bishop," "the same bishop." The one place the voice quotes at length is the one place it names nobody. (Ambrose is on the record as this world's own Milan bishop; there is no privacy or contested-attribution reason for the anonymity.)

**Fix:** name Ambrose and mark the quoted sentences, or — better, and consistent with the build's own discipline — create the missing `ijc.quote.ambrose-blessing-changes-nature` record from `npnf210:33203–33205` and `:33263–33271`, license it verbatim, cite it, and let the turn quote it properly.

### M7 — Half the turns sit above the reading floor; the demonstrations are the register lever, and they teach a harder voice than the fleet's

`fk_grade` (the build's own function, ceiling 10) on every representative turn, with the `alx` model beside it:

| ijc | FK | alx | FK |
|---|---|---|---|
| `f6-p-someone-like-me` | 7.4 | `c-p-want-to-believe` | 4.9 |
| `f1-t-bread-and-cup` | 9.1 | `c-i-who-was-jesus` | 5.9 |
| `c-i-who-was-jesus` | 9.3 | `f6-p-someone-like-me` | 5.7 |
| `f5-i-ordinary-day` | 9.9 | `f5-i-women-own-words` | 6.1 |
| `f6-p-hypocrisy` | **11.9** | `f6-t-going-to-hell` | 7.1 |
| `f6-p-woman-authority` | **11.9** | `f6-t-marriage-ending` | 7.3 |
| `f6-i-never-settled` | **12.2** | `f6-p-woman-authority` | 8.0 |
| `f1-i-argued-about` | **14.0** | | |

Four of eight are above the ceiling; the whole set runs 3–6 grades above the model it was built from. `f6-i-never-settled` contains an **86-word sentence** (FK 18.1), and `f1-i-argued-about` has three sentences of 33–40 words each. `gate_readability` does not see any of this — it is scoped to `term` and `honest_limit` fields — but O4 says "readability outranks flavor everywhere," statement 3 says one idea per sentence, and §4.3.5 makes demonstrations "the register lever": these are the examples a live model imitates every turn. A world admitted on this set will speak at FK 12.

Note what this is *not*: it is not the content's fault. `f5-i-ordinary-day`, whose material is the thinnest in the set, comes in at 9.9 because its source honest_limit had to pass the gate. The four over-ceiling turns are the four drafted freely.

**Fix:** split the long sentences; the content survives it intact. The 86-word Chalcedon sentence wants to be four.

### M8 — The spec's own demonstration list is not satisfied: no lament exchange, and no F6-T identity-collision turn

Spec §4.3.5: "Demonstrations are the register lever: a modest set per world against canon questions — center cells first, the identity-collision cells with the spoken non-judgment line in the world's own idiom, honest limits in voice, **one lament exchange**."

There is no lament turn in the set. All eight open by answering; none uses the personal-wound register where, per §6's own runtime rule, "witness comes before answer and statement 1 is deliberately suspended for the turn." `f6-p-hypocrisy` sits at a personal-register cell but opens "Yes, and we will name our own sharpest case" — answer-first. The `alx` model has exactly one, labeled in its own craft note as "the one lament exchange the spec requires," and the exemplar transcript treats that turn as demonstrating a register nothing else in the set demonstrates. `ijc.limit.c-p-jesus-to-you` exists and would carry one.

Separately, §6's identity-collision block names three questions across F6-P **and F6-T** and closes "demonstrations for these cells required before any world opens." The set has two, both F6-P; there is no F6-T demonstration of any kind. (F6-T's divorce and hell material was left as a disclosed gap in BUILD-LOG §6, so this may be a deliberate deferral — but it is undisclosed in §9, which lists the eight records as if the set were complete.)

**Fix:** add a lament turn built on `ijc.limit.c-p-jesus-to-you`; either add an F6-T identity-collision turn or disclose the deferral in BUILD-LOG §9 with the reason.

### M9 — `ijc.voice.craft.guard` replaces the fleet floor line instead of carrying it

`guard` reads: "Honest office-holder scope beats invented ordinary life, absolutely."

Spec §4.3.5: "The guard is **the one fleet floor line** (honest thinness over invented depth, absolutely) **plus at most a line or two** where a world's measured failure demands it." `alx.voice.craft.guard` is the floor line verbatim.

The ijc guard is a good world-specific line — it names this world's real primary risk, exactly as the task requires — but it *substitutes* for the floor rather than adding to it, so the general prohibition is nowhere in the compiled Guard section. As written, the guard licenses nothing about inventing a quote, a Homoian self-testimony, a council's wording, or a figure's motive; it speaks only to ordinary life. Given that H1 and H2 are both inventions of the kind the floor line covers and neither is about ordinary life, the substitution is not academic.

**Fix:** "Honest thinness beats invented depth, absolutely — and here that means honest office-holder scope beats invented ordinary life."

### M10 — Across the set, the three strands are not held evenly: Constantinople never speaks its own case

The three-strand discipline is met at the level the task names — nowhere does a turn adjudicate, and `f6-i-never-settled` closes "We do not resolve that for you now; our own record never did." But look at the set as a whole:

- **Rome's claim** is voiced positively twice, in its own strongest evidence: the Tome read at Chalcedon and acclaimed (`c-i`), and the acclamation plus Leo's reasoned rejection given at length (`f6-i`).
- **Constantinople's claim** appears once, and only as reported reasoning that the same turn's next two sentences deny. Its own positive case — `ijc.contested.canon-28-meaning.claim`: "the councils **recognized, rather than invented**, the new capital's rank," with the concession that "the empire's ecclesiastical weight had really moved east" — is cited in that demonstration's `sources[]` ("the unresolved contest named") and then never spoken. The turn even frames the canon through Rome's objection to it ("not because an apostle had ever taught there").
- **Milan's claim** appears once, in `f6-p-hypocrisy` — its worst instance, chosen deliberately and rightly. Its positive form ("the emperor is within the Church, not above it," `ijc.term.imperator-intra-ecclesiam`, `ijc.quote.ambrose-emperor-in-church`) is spoken nowhere.

The set therefore *states* that the contest is unresolved while *demonstrating* only one strand in its own voice. Since demonstrations teach by example, this is the shape a live voice will reproduce.

**Fix:** one added sentence in `f6-i-never-settled` giving Constantinople's case in its own terms (the contested_claim's `claim` and `concedes` fields are already written for it), and consider whether the set wants one turn where Milan's sacramental-independence claim is voiced positively rather than only at its cost.

### M11 — `ijc.demo.f6-p-woman-authority`'s "Yes, twice" drops both of its source record's tensions

`ijc.dw.f6-p-women-authority-cost.tensions` carries two qualifications, and the demonstration carries neither in full:

- "both women reach us **exclusively through hostile or interested male authors**" — half-kept (the Justina clause survives; nothing corresponding for Pulcheria beyond "a place in the correspondence of powerful men").
- "**this is two data points, not a pattern the record lets us generalize with** - what these two women's experience does and does not say about women's authority more broadly is exactly what the sources cannot tell us" — dropped entirely.

The turn also never says what the `alx` parallel turn says first and what this record set plainly supports: no woman appears in any church office anywhere in this world's record. The participant asked "could a woman carry real authority **among you**"; the answer given is two imperial principals, one of whom exercised state power *against* the church. A flat "Yes, twice" at an identity-collision cell, with the record's own "not a pattern" caveat removed, over-answers.

**Fix:** keep the two cases, add the caveat the source record wrote for exactly this purpose, and state the office fact plainly.

### M12 — Structural: `demonstration.exchange` is compiled into `prompt.txt` and is outside every content gate's field map

`build_prompt()` emits, after the terms, witnesses, limits and stories, `f"Demonstration: {demo['id']}"` with the full exchange text. So every representative turn reaches a live model. But:

- `gate_no_build_attribution._ATTRIBUTION_FIELDS` has no `demonstration` entry — the ISO-date/`ruled by`/working-scope patterns are not applied to any turn (nor to `voice_craft.flavor_notes[].note` or `characteristic_concerns[]`, both of which `build_prompt()` also emits, though the gate does scan `characteristic_concerns` separately).
- `gate_readability` covers `term` and `honest_limit` only — hence M7 going unseen.
- Nothing checks that a demonstration's spoken content is traceable to its own `sources[]`, which is the failure mode of H1, M1, M3 and M5.

The gate battery was designed before this record type had content in it. Every finding in this review is in a field the battery does not look at, which is not a criticism of the battery — it is the reason a human pass was needed here — but it should be recorded rather than rediscovered.

**Fix (offered, not required by this pass):** add `demonstration: ["exchange"]` (flattened) to `_ATTRIBUTION_FIELDS`; extend `gate_readability` to demonstration turns at the same ceiling; and note `alx`'s own `gate_grounded_claim` (experimental, `engine/m1/gates_experimental.py`) as the natural home for a demonstration-scoped grounding check — the exemplar transcript records it catching precisely this class on `alx`'s own demonstrations.

---

## LOW

- **L1 — `ijc.demo.c-i-who-was-jesus`'s craft note misdescribes its own ellipsis.** It says the Leo quotation is "truncated with a disclosed ellipsis **at the same point that record's own body notes as its mid-sentence break**." `ijc.quote.leo-tome-each-form`'s body note is about the quote's *end* ("'carrying out what appertains to the flesh' completes the sentence past the extraction window"). The demonstration's ellipsis is in the *middle*, eliding two whole sentences ("and in this union there is no lie… so man is not swallowed up by the dignity"). The elision itself is honest and marked; the justification for it is about something else. Also undisclosed: the leading "For" is dropped from both surviving fragments.
- **L2 — the creed is rendered near-verbatim but silently altered while flagged as the creed's own answer.** "Our creed answers first: very God of very God, of one substance with the Father, who **for us** and for our salvation came down and was made man, suffered, and rose the third day." `ijc.quote.nicene-creed` (exact at `npnf214:2408–2418`) reads "…begotten, not made, **being** of one substance with the Father… Who **for us men** and for our salvation came down [from heaven] and was incarnate and was made man. He suffered and the third day he rose again." Unquoted, so not H2's defect — but "our creed answers" reads as citation, and the modernization of "for us men" is a silent doctrinal-text edit in a compiled field. Either quote it or mark it as summary.
- **L3 — "For most of a century" inflates the build's own arithmetic.** `ijc.demo.f1-i-argued-about` opens "For most of a century, whether the Son is of one substance with the Father, or only like him." `ijc.term.homoousios.senses.translational` says the word was "argued, enforced, reversed, and re-enforced across **half a century**." Same family as §7's "fifteen years, not sixteen."
- **L4 — two participant turns diverge from the canon question they cite.** `f1-t-bread-and-cup` and `f6-p-woman-authority` render the canon's em dash as a hyphen; the other six match character-for-character, and all seven `alx` turns keep the em dash. Cosmetic, but the participant line is supposed to *be* the canon question.
- **L5 — Ambrose's reverential capitals lowercased in `f1-t-bread-and-cup`.** "The Lord Jesus **himself** proclaims"; "**He himself** speaks of **his** Blood" — the file prints "Himself," "He Himself," "His Blood" (`npnf210:33263–33268`). Also "trades-people" → "tradespeople" in `f6-p-woman-authority`. The identical defect family (sentence-case drift inside quoted material) was fixed twice in §8 L10.
- **L6 — "It was withdrawn" hardens what the source says.** `ijc.demo.f6-p-hypocrisy`; `ijc.story.callinicum-synagogue` says Ambrose "refused to offer the sacrament until the emperor **promised**, there and then, to withdraw it. Theodosius yielded." Re-derived at `npnf210:43979–43994`: Theodosius "**said that he would amend the edict**," "he **promised** that it should be so," and Ambrose closes "everything was done as I wished" — his own claim, in the letter the same demonstration correctly says is the only account we have. Mild, because the turn does disclose the sourcing two sentences later.
- **L7 — the "sharpest case" is quietly softened.** `f6-p-hypocrisy` gives Ambrose's objection as "judging it intolerable that a bishop be made to fund a synagogue," dropping the second half the story record carries — "and worse for the burning of a Valentinian house, **which he called worse than heathen**, to go answered at all" (verified: *Ep.* XLI names both burnings, `npnf210:43564–43568`). A turn that announces it will not choose the safer example should not drop the harder half of the example.
- **L8 — "states both halves at once" re-drifts toward a compression this build corrected twice.** `f6-i-never-settled` opens "Our own closing scene **states both halves at once** and resolves neither." BUILD-LOG §3.1 records the legacy "the same council, in the same session" as a corrected factual error, and §6 records three further "days apart / same week" corrections; `ijc.story.tome-that-would-not-bend.absent_detail` fixes the interval at three weeks and says "the drama is real, **the compression is the teller's**." The demonstration keeps the record's safe "before it dispersed" and then adds "at once" back in the framing sentence.
- **L9 — `ijc.voice.craft.identity` carries build-architecture vocabulary in a compiled field.** "The persona's name and role label are **registry data (the two sanctioned fabrications)** and never appear in world records, this one included." This is inherited verbatim from `alx.voice.craft` and so is a fleet-level question, not an ijc defect — but it is the only phrase in any compiled ijc field that describes the build rather than the world, it sits in the Identity section a live model reads as its own self-description, and the `no-build-attribution` gate's keyword patterns cannot see it. Worth raising once at fleet level rather than silently copying forward into `syr`.
- **L10 — a small self-contradiction inside `voice_craft`.** `identity` says the role label "never appear[s] in world records, **this one included**," while the compiled `self-reference` flavor note prints the role word twice ("not an in-world role like '**deacon**' or 'judge'"; "'I am a **deacon**, not a judge' is wrong"). The prohibition needs the example, so the fix is in the identity clause, not the note.
- **L11 — "the women our record names are two empresses" undercounts by one.** Carried verbatim from `ijc.limit.f5-ordinary-day` into `f5-i-ordinary-day`. Marcellina, Ambrose's sister, is named in this build's own citation apparatus as the addressee of *Epp.* XX and XLI (`ijc.quote.ambrose-cannot-surrender.sources[].locus`) and both demonstrations refer to her ("to his sister"). Nothing of her own survives, so the point stands — but "names" is the wrong verb, and this is a compiled honest-limit statement. "The women our record lets us *see acting* are two empresses" would be exact.
- **L12 — the `term-introduction` flavor note models a gloss the term record does not give.** The compiled example is "the claim that a see's rank follows the emperor's own residence - our word for it was **presbeia**." `ijc.term.presbeia.plain_meaning` leads with "The 'prerogative of honor': Constantinople's claim to rank second among the churches… Rank follows the throne." The word names the prerogative; the flavor note's gloss names the argument for it. Since this note is the compiled template for how *every* term gets introduced, it should model the term record's own plain meaning.
- **L13 — Percival's own limiting reading of the legates' objection is carried nowhere, and the demonstration asserts the objection.** `f6-i-never-settled`: "Leo's own legates objected in the council itself." True — Lucentius, at the last session. But the vendored excursus (`npnf214:22345–22365`) argues the legates had *already conceded the rank*: at Session I, Paschasinus said "We will, please God, recognize the present bishop Anatolius of Constantinople as **the first** [i.e. after us]," and Percival treats Lucentius's later protest as made "in a moment of heat and indignation." This is the same shape as §7's Coustant finding — a limiting counter-reading sitting in the build's own apparatus, unrecorded. Its natural home is `ijc.contested.canon-28-meaning.held_against`, and it strengthens the unresolved holding rather than weakening it.
- **L14 — two coined quotable lines, against register statement 6.** `c-i`'s close ("The definitions are our devotion, in the only idiom we had") is the most memorable sentence in the turn and is the voice's own coinage; its craft note acknowledges this openly, which is the right instinct, but statement 6 is that when something deserves to be quotable it *is* a quote. Inherited from `ijc.dw.c-i-jesus`, so a record-set question, not only a demonstration one. (M4(b) is the sharper instance.)
- **L15 — "Under Constantius" needs its numeral.** `f1-i-argued-about` names "Constantius" bare where every record in the set (`ijc.term.homoios`, `world_core.cautions` §2, `ijc.figure.constantius`) says Constantius II. In a world that also contains Constantine and Constantius Chlorus in the participant's likely background knowledge, the numeral is not pedantry.

---

## Verified sound — recorded so a fix pass does not damage it

**The pronoun discipline is exact, and this is the finding I most expected to have to write up and did not.** A regex scan of all sixteen `exchange[].text` values for `I|I'm|I've|my|My|me|Me|mine|myself` returns two hits in eight representative turns:

1. `ijc.demo.f6-p-someone-like-me`: "**I am a representative of Church and Empire, not here to judge you** - only to hand on what we held." Once, turn-initial, at the one participant question in the set that is actually about the voice's nature, unpaired with any in-world role label, and followed by "we" for the remaining eleven sentences. This is the sanctioned form, in the sanctioned place, matching `alx.demo.f6-p-someone-like-me` and EXEMPLAR-TRANSCRIPT v4 exactly.
2. `ijc.demo.f1-t-bread-and-cup`: "This is **My** Body" — a dominical citation inside a cited teacher's words, which is the licensed carve-out.

`ijc.demo.f6-p-woman-authority` is tagged identity-collision and correctly *declines* the exception, with a craft note giving the fleet's own reason (the question is about the world's content, not the voice's nature) — the precedent `alx` established when it converted that same turn. No "we are not your judge" line anywhere hardens into an identity claim. **No turn narrates a personal career, an individual's day, a located "I was there," or anything an apocrisiarius-persona would say about himself.** The Marius/Deacon-of-the-Letters identity appears in no compiled field of any of the nine records.

**Compiled-field leakage: clean but for L9.** `identity`, `guard`, all eight `flavor_notes[].note`, all five `characteristic_concerns[]`, and all sixteen `exchange[].text` scanned for ISO dates, "RULED"/"ruled by", "Mark", `Doc_XX`, `ijc.`/`alx` record ids, "fleet", "registry", "schema", "gate", "build", "review", "spec", and canon-machinery vocabulary. One hit, L9's inherited `alx` sentence. Every "record" occurrence is in-world ("our record," "our own record's terms"). All the build-process disclosure in these nine files — the identity-confirmation ruling, the "corrected in that record directly ahead of this demonstration" note, the verification claims — lives in trailing bodies, which `engine/m1/loader.py` excludes from every builder. That is the build's own convention, correctly applied.

**The Homoian recentering is met, and met well.** `ijc.demo.f1-i-argued-about` is the strongest turn in the set. It refuses the slur by name ("'Arian' is not a fair word"), states the establishment fact plainly and in the right direction ("bishops who confessed the Son of one substance with the Father were the ones removed and exiled, not the reverse"), gives the formula's own content and its own reason for refusing both rival words, speaks all of it from outside ("the formula **the imperial church itself held**"), and states the evidential asymmetry without hiding behind it ("almost everything we know of it comes through the very side that eventually defeated it"). It tracks `ijc.term.homoios`'s informational, evidential and personal senses clause for clause. Nothing in it reads as spoken from inside the confession, and nothing treats it as an always-defeated fringe. (M5 is that this obligation is met *here* and nowhere else.)

**Structure and mechanics.** 13/13 gates clean over 151 records, zero findings in every gate, re-run directly. All eight `canon_question_id`s resolve to real fleet canon questions; all eight `canon_cells` match their question's own cell; six of eight participant turns are the canon question character-for-character (L4 is the other two). Confidence blocks are internally well-formed and pass the cross-check (M1 is a substantive, not mechanical, mismatch). The three-strand contest is never adjudicated in any turn (M10 is about balance, not adjudication). The honest-limit-in-voice turn (`f5-i-ordinary-day`) carries `ijc.limit.f5-ordinary-day.statement` essentially verbatim — including the "two empresses" correction §9 describes — with only "the record" → "our record," which is the right change; it is a system-apology-free limit spoken as the voice's own honesty, exactly as the spec and the `alx` pattern require.

**BUILD-LOG §9's account is accurate on the points I could check independently:** the exception is used exactly once and in the record §9 names; it is deliberately not used in the other identity-collision turn; the `ijc.limit.f5-ordinary-day` "an empress and a regent" → "two empresses" correction is real and is reflected in both records; `f6-p-hypocrisy` does use Callinicum rather than a safer instance. The one claim in §9 that does not hold is "**All content is drawn from and cites already-verified ijc records; none is fresh invention**" — H1 is fresh, and M5/M6's content is drawn from records the demonstrations do not cite.

---

## Fix ordering

1. **H1, H2, H3** — one sentence each, all three in compiled participant-facing content, all three checkable in files already in the repo. H2 in particular should be fixed before anything quotes these demonstrations onward.
2. **M1, M2, M3, M4** — the four dropped or overstated qualifications. M1 restores a hedge two prior review rounds paid for; do it with the `divergence_note` in the same pass.
3. **M5, M6** — the two citation-integrity items: the uncited answer-ground plus the missing Homoian tension at the center cell, and the unattributed *De Mysteriis* block (worth creating the missing quote record while the passage is open at `npnf210:33203`/`:33263`).
4. **M7, M9** — the two register items, both mechanical: split the long sentences, restore the fleet floor line to `guard`.
5. **M8, M10, M11** — the set-shape items: the missing lament turn, the strand balance, the woman-authority caveats. M8 may resolve as a disclosure rather than a record.
6. **M12** — the gate-coverage gap, if the project wants the mechanical guard rather than relying on this pass having found everything.
7. **L1–L15** — the rest. L9 and L13 are worth routing somewhere other than this world (fleet, and the answer canon, respectively).

No finding in this pass reopens Step 0, Doc_01, or the answer canon's settled ground, and none requires re-running the identity confirmation — the persona itself is not implicated in any finding, and §9's rationale for it holds against everything I read.

**Overall verdict: REVISION REQUIRED — the voice itself is right and the pronoun discipline that three fleet revisions were spent on holds exactly, but the eight demonstrations lose, in compression, the qualifications that make this record set trustworthy, and three of them state something no record in the build supports; fix the three HIGH findings and the four dropped-hedge MEDIUMs and this set becomes what §4.3.5 needs it to be.**
