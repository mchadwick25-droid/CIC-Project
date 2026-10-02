# Adversarial Confirmation Pass 2 — `records/ijc/` after the second (2026-08-22) fix round

**Branch:** `world/ijc` (142 records) · **Reviewed:** 2026-08-22 · **Reviewer:** isolated Opus dispatch, second follow-up verification
**Method:** every second-round fix re-derived from the vendored files in `/home/user/CIC-Project/cic/texts/` with ThML `<note>`/`<scripRef>` elements stripped before verbatim comparison (iterative note-stripper, tags removed, entities unescaped, smart quotes and dashes folded, whitespace normalized); quote loci machine-tested for containment by minimal-range search rather than eyeballed. Nothing accepted from BUILD-LOG §6/§7's own account, nothing accepted from `Review_Confirmation_Pass.md`'s own line numbers — where that review asserted a line range, I re-derived it independently, and in three cases it was wrong. Gate battery run directly via `engine.m1.loader.load_world_records("ijc")` + `engine.m1.gates.run_all`; every record's front matter additionally `yaml.safe_load`-ed file-by-file; compiled-field contract re-read from `engine/m2/builders.py` (`build_prompt`, `_chunk_text`, `build_figures_json`) and the record body's exclusion confirmed from `engine/m1/loader.py`'s own docstring.
**Prior artifacts checked against:** `Review_Confirmation_Pass.md` (all 1 HIGH / 8 MEDIUM / 13 LOW), BUILD-LOG.md §7, the second-round diff `c0863a86..HEAD -- records/ijc/`, and the full diff `3397335e..HEAD -- records/ijc/`.

---

## Summary verdict: MOSTLY CONFIRMED — the pattern repeated a third time. 23 residual/new findings (1 HIGH, 8 MEDIUM, 14 LOW)

**State the good part plainly first.** The second fix round genuinely landed its hardest and most consequential work. The fabricated "autumn fast" is gone from all four records and replaced with something the file actually supports. The Anatolius/synodal-letter misidentification, the *De Mysteriis* authorship note, the "Auxentius' cruel law" misquotation, the Justina `verified-direct` overreach with its internal contradiction, the Ep. CV "new council" framing, the 385/386 dating divergence, and Coustant's limiting reading of Julius were each re-derived from source by me and each check out — several of them word-for-word. All twenty quote texts remain exact against their editions under the build's own disclosed omission conventions. The gate battery is 13/13 clean over 142 records with zero findings, all 142 front matters parse individually, relation reciprocity is exact, no dangling ids, all 28 canon cells covered, and a fresh field-by-field scan of the actual `build_prompt()`/`_chunk_text()` contract found **no** fleet-architecture or build-process leakage in any compiled field.

The verdict falls short of clean for the reason the task anticipated: **this round, like the two before it, introduced a small number of new errors of exactly the kind it was fixing** — and this time with a specific new mechanism.

1. **One new HIGH.** The counter-datum added to close the last round's L9(b) — Hilary of Poitiers as evidence that Latin hymnody predates Milan 386 — is wrong about the vendored volume in a compiled `doctrinal_witness.text` at `A`/`verified-direct`/`load-bearing`, and is contradicted by the next four sentences of the very passage it cites.
2. **The fix round trusted the prior review's line numbers instead of re-deriving them.** Of the seven quote loci "fixed," one is now exactly right, two are improved-but-loose, one is cosmetic, and **three now point at ranges that do not contain the quote they cite** — a regression on the pre-fix state, because the prior review's own asserted ranges (`66693–66733`, `23510–23551`, `5326–5380`) were themselves wrong and were adopted verbatim.
3. **The five new cell-scoped negative sweeps close M7 structurally but not evidentially.** Two of them assert checkable corpus facts that are false, one misdescribes its single recorded finding and walks past the licensed primary text sitting directly above it, and none of the five records the actual search strings — unlike the two sweeps they were modeled on.
4. **One item the BUILD-LOG claims fixed was fixed in only one of its two places**, and the place left unfixed is a compiled `story.text` field that now contradicts this build's own quote record of the same sentence.

None of this reopens Step 0 or Doc_01 settled ground. All of it is a short pass to fix.

## What was checked

| Scope | Checked |
|---|---|
| Prior HIGH (1) | re-derived from source against current record state — **fixed**, with one new scope defect at the same spot (M3) |
| Prior MEDIUM (8) | **8/8** re-derived at record + vendored-line level |
| Prior LOW (13) | **13/13** re-derived; the 7-item locus block machine-tested for containment |
| 5 new search_records | **5/5** read in full; every corpus claim independently grepped against `cic/texts` and against this build's own `source` records' licensing scope |
| Quote texts | **20/20** machine-diffed against their editions (whole-file containment, note-stripped) — all exact |
| Quote loci | **7/7** minimal-containing-range computed from the file, not read off the record |
| Round-1 spot checks | Callinicum (`npnf210:43565`, `:43166`), Leo *Ep.* LIX.4 (`npnf212:7398`), Chalcedon Session IV (`npnf214:20105`ff), Ambrose *Concerning Widows* I.2 (`npnf210:38845`) — all confirm the prior review's account |
| Compiled-field leakage | Every `doctrinal_witness.text`, `honest_limit.statement`, `story.text`/`tellable_as`, `term.plain_meaning`/`quick_meaning`/`world_word`, `world_core.horizon`/`formation_logic`/`thinness`/`cautions`, `figure.bridge_line`, `quote.text` regex-scanned for build-process, file-path, record-id, date, and sibling-world language — **clean** |
| Mechanical gates | **13/13 clean**, 142 records, 0 findings |
| YAML front matter | **142/142** parse individually under `yaml.safe_load`; 0 failures |
| Structure | reciprocity 0 non-reciprocal edges; 0 dangling relation targets; 0 dangling `source_id`s; 28/28 canon cells carry a record |

---

## HIGH

### H1 — `ijc.dw.f4-e-ancient-custom`: the Hilary counter-datum added by this round is wrong about the vendored volume, and the passage it cites says the opposite of what it is used for

Closing the prior review's L9(b) ("the Hilary counter-datum is asserted anonymously and left unsourced"), this round added a fourth source and rewrote the compiled `text` to read:

> not, on his own words, that this was the first hymn-singing anywhere in the West; Hilary of Poitiers, a generation earlier, already has the fame of being the earliest Latin hymn writer, **and the same volume that carries his theology preserves fragments of his own hymn collection** - a counter-datum our sources do not let us collapse into this one night.

with `sources[]`:

> `ijc.source.hilary-de-synodis`, locus: the volume's own introduction to Hilary (npnf209:3709-3731), on his fame as the earliest Latin hymn writer **and the surviving hymn fragments in the same manuscript as De Synodis**

Three separate problems, all checkable in the cited file.

**(a) The volume does not preserve any hymn fragments.** `npnf209`'s Hilary contents are exactly four `div2`s: Introduction (line 496), *De Synodis* (7536), *De Trinitate* (9913), and Homilies on Psalms I, LIII, CXXX (26324). No hymns are printed anywhere. What the introduction reports, at `npnf209:3707–3710`, is that a *manuscript* holds them: "**In this same manuscript, discovered by Gamurrini at Arezzo,** are the remains of what professes to be Hilary's collection of hymns. He has always had the fame of being the earliest Latin hymn writer." The record has converted "manuscript" into "volume."

**(b) "the same manuscript as De Synodis" is the wrong manuscript.** "This same manuscript" refers back to the Arezzo codex the introduction has just been discussing — the one containing Hilary's *De Mysteriis*, named at `npnf209:3653` as "*S. Hilarii Tractatus de Mysteriis et Hymni*". *De Synodis* is not in it. The locus names the wrong work.

**(c) The cited passage refutes the use the record puts it to.** The record deploys Hilary against Augustine's claim that hymn-singing began at Milan in 386. Within the same paragraph the record cites, the introduction says:

> "and there is **no reason to suppose that he had any wide or permanent success in introducing hymns into public worship**… If Hilary must have the credit of originality in this respect, **the honour of turning his suggestion to account belongs to Ambrose**, whose fame in more respects than one is built upon foundations laid by the other. And… **not a line remains which can safely be attributed to Hilary**" (`npnf209:3728–3741`)

and, of the fragments the record calls a counter-datum:

> "But, when we come to the examination of these hymns in detail, **the gravest doubts arise**… beyond this, and the fact that the manuscript ascribes it to Hilary, **there is nothing to suggest his authorship**" (`npnf209:3774–3786`)

The edition even pre-empts the Toledo-canon evidence the prior review pointed at, calling it possibly "a mere literary flourish" (`:3731–3736`, inside a note). Hilary is credited with *writing* Latin hymns and explicitly *not* with introducing them into worship — which is precisely and only what Augustine claims for Milan.

**Why HIGH:** this is the project's own named failure mode — a real, sourced fact carried at the wrong scope — newly introduced *by* the round that existed to eliminate it, in `doctrinal_witness.text` (compiled into `prompt.txt` and the `doctrinal_witness` chunk, verified against `engine/m2/builders.py`), at `citation_specificity: A` / `verification_state: verified-direct` / `evidentiary_weight: load-bearing`. It is the third consecutive round in which the fix to a scope error at this exact record produced a new one.

**Fix:** rewrite the counter-datum to what the introduction actually supports — Hilary is credited as the earliest Latin *hymn writer* (Jerome's *Viri Illustres* is the edition's own authority for that), a manuscript at Arezzo preserved a small collection later ascribed to him, and the same introduction doubts the ascription and credits Ambrose with turning hymnody into public practice. Correct the `sources[].locus` to name the Arezzo manuscript and *De Mysteriis*, not *De Synodis*. Either way, the Hilary datum no longer counters Augustine on the point the record uses it for, so the surrounding sentence needs to change with it.

---

## MEDIUM

### M1 — Three of the seven quote-locus "fixes" now point at ranges that do not contain their quote

Not one of these was re-derived; all three took the prior review's asserted range verbatim, and the prior review was wrong. Machine-computed minimal containing ranges:

| Record | Old locus | New locus | Quote actually spans | Status |
|---|---|---|---|---|
| `ijc.quote.nicene-creed` | 2404–2416 | **2408–2418** | 2408–2418 | ✅ exact and tight |
| `ijc.quote.canon28-equal-privileges` | 22218–22231 | 22224–22232 | 22223–22232 | end fixed, start 1 line late (see L1) |
| `ijc.quote.constantine-bishop-outside` | 66733 | **66693–66733** | **66732–66734** | ❌ worse |
| `ijc.quote.julius-custom` | 23550–23552 | **23510–23551** | **23549–23552** | ❌ worse |
| `ijc.quote.leo-tome-each-form` | 5366–5372 | **5326–5380** | **5365–5381** | ❌ worse |
| `ijc.quote.lactantius-dream` | line 10612 | 10612 + "through 10620" | entirely on 10620 | cosmetic (see L3) |
| `ijc.quote.vc-conquer-by-this` | 61196–61207 | 61196–61208 | 61203–61208 | end fixed, start 7 lines early (see L2) |

The three regressions, with the vendored evidence:

- **`constantine-bishop-outside`.** `npnf201:66732–66734` reads: "…in my / hearing in the following words: **"You are bishops whose** / **jurisdiction is within the Church: I also am a bishop, ordained by God** / **to overlook whatever is external to the Church."**" The new range ends at 66733, cutting off the clause "to overlook whatever is external to the Church" — the half of the quote the record exists for — and its new start, 66693, is "which, torches everywhere diffused their light, so as to impart to this / mystic vigil a brilliant splendor beyond that of day", i.e. 39 lines of Easter-vigil narrative that is not the quote.
- **`julius-custom`.** `npnf204:23549–23552`: "**And why was nothing said to us concerning the** / **Church of the Alexandrians in particular? Are you ignorant that the** / **custom has been for word to be written first to us, and then for a just** / **decision to be passed from this place**". The new range ends at 23551, dropping the final clause; its start, 23510, is 39 lines earlier, inside an unrelated stretch of Julius's letter and its apparatus.
- **`leo-tome-each-form`.** The quote runs from "For He who is true God is also true man" at the end of `npnf212:5365` to "out what appertains to the flesh." on `:5381`. The new range ends at 5380 ("…and the flesh carrying"), truncating mid-sentence. Worse, the locus reads "**ch. IV** (npnf212 lines 5326-5380)" while chapter IV's own heading is at `:5331` — the cited start sits inside chapter III.

**Why MEDIUM, not LOW:** the prior review scored these LOW because too-narrow loci still sat inside the quote. Three now sit *outside* it, in a build whose entire discipline is precise citation, and the mechanism — adopting a reviewer's asserted line numbers without opening the file — is more concerning than the numbers.

**Fix:** set them to the computed spans: `66732-66734`, `23549-23552`, `5365-5381`. Regenerate the whole block from a script rather than by hand; the containment test is three lines of code.

### M2 — `ijc.story.vigil-in-basilica.text` still carries "the West's congregations"; only one of the two places was fixed

BUILD-LOG §7 states the fix as "Augustine's own 'throughout the rest of the world' restored in place of a narrower 'the West's'." It was restored in `ijc.dw.f4-e-ancient-custom.text`. It was **not** restored in `ijc.story.vigil-in-basilica.text`, which the prior review named explicitly ("the same phrasing is carried into `ijc.story.vigil-in-basilica.text`"):

> a custom, he wrote, kept from then till now, imitated, he says, by many, almost all, of **the West's congregations** afterward.

`npnf101:13774` reads: "which custom, retained from then till now, is imitated by many, yea, by almost all of Thy congregations **throughout the rest of the world**." The build's own quote record `ijc.quote.augustine-vigil-hymns` carries the sentence correctly — so the record set now contradicts itself about what Augustine said, with the wrong version in `story.text` (compiled into both `prompt.txt` and the story chunk) and the right one in `quotes.json`.

**Fix:** one clause in `ijc.story.vigil-in-basilica.text`, matched to the quote record.

### M3 — `ijc.dw.f4-t-collections-discipline`: the H1 fix replaced a fabricated fact with the edition's own hedged editorial reconstruction, stated as flat fact in compiled emic text

The correction itself is right and I verified its warrant: `npnf212:13612–13615`, "Dies apostolicæ institutionis: this was, as note 6 explains, **the octave of SS. Peter and Paul**"; and note 6 at `:13508–13515`, "These collections… **probably began on the 6th of July** (the octave of SS. Peter and Paul), the day on which in pagan times the *Ludi Apollinares* had also begun." Sermon X's opening at `:13716` confirms the character: "celebrate with the devotion of religious practice that day which they purged from wicked superstitions and consecrated to deeds of mercy."

But the compiled `text` now reads:

> tied to an annual collection day - **the octave of SS. Peter and Paul, in early July, a day the record says was purged from a pagan festival** and consecrated instead to deeds of mercy

I read Sermons IX and X in full with notes stripped — Leo's own words only. **Leo never names the day and never dates it.** He calls it "the day of Apostolic institution", "this Apostolic institution", and "that day which they purged from wicked superstitions"; the word "July," the octave of Peter and Paul, and the *Ludi Apollinares* all come from Feltoe's report of the Ballerini, who hedge it ("probably began"). The record drops the hedge, drops the attribution, and puts the editors' 18th-century reconstruction into an emic compiled field at `A`/`verified-direct`/`load-bearing`. The record's *body* does disclose that this comes from "the file's own note" — but the body is provenance only and is read by no builder (`engine/m1/loader.py` docstring), so the disclosure sits outside the field that carries the claim.

This is the same defect family as the prior round's M2/M3/M5 (an edition's editorial apparatus presented as the primary record's own content), reintroduced in the fix for its own HIGH.

**Fix:** in `text` and `positions`, attribute and hedge — "a day this edition's editors identify as the octave of SS. Peter and Paul in early July; Leo himself calls it only 'the day of Apostolic institution'" — or drop the date and name and keep what Leo does say, which is enough for the cell. Everything else in the record I re-verified exact (`:13733` "He only who knows what He has given to each…", `:13738` "committed to our stewardship", the ransom/stranger/exile triad at `:13757`ff).

### M4 — `ijc.search.f6-e-negative-sweep` asserts a corpus fact that this build's own source records contradict

The new sweep's `note` concludes:

> "Eusebius's own Historia Ecclesiastica is licensed here only for Books VIII-X… **and no other licensed source reaches back before 312.**"

This is false, and it is the load-bearing sentence — it is what converts F6-E's honest limit from "unsearched gap" into "genuine structural fact."

- `ijc.source.lactantius-de-mortibus.work` reads "De Mortibus Persecutorum… - **esp.** ch. 44… and ch. 48". "esp." is not a narrowing license; contrast the build's own `ijc.source.augustine-confessions`, which says "Book 9 ch. 7 **ONLY** … **NARROWLY LICENSED**". *De Mortibus* is licensed whole, and it is a continuous narrative of the Great Persecution from 303.
- `ijc.source.eusebius-vita-constantini.work` carries the *Vita* whole, with no book restriction; Book I covers the pre-312 years.

And *De Mortibus* carries the cell's **first seed question in so many words**. `anf07`, ch. XXIII:

> "the market-places filled with crowds of families, all attended with their children and slaves, the noise of torture and scourges resounded, sons were hung on the rack to force discovery of the effects of their fathers, **the most trusty slaves compelled by pain to bear witness against their masters**, and wives to bear witness against their husbands. In default of all other evidence, men were tortured to speak against themselves"

with a second instance later ("The Jew was ordered to the torture till he should speak as he had been instructed"), and martyrdom material at ch. XVI ("Having been nine times exposed to racks and diversified torments, nine times by a glorious profession of your faith you foiled the adversary").

The honest_limit `ijc.limit.f6-e-earlier-windows` is itself defensible — it is a *window* judgment ("those questions belong to the age of persecution, and our world begins where that age ends"), which is a real and honest position. What is not defensible is the sweep's added claim that the material is unreachable in the licensed corpus. It is reachable; the build has chosen not to reach for it, which is a different and more honest thing to say.

**Fix:** rewrite the sweep's `note` to state the window judgment as a window judgment and record that *De Mortibus Persecutorum* — licensed here whole — does carry torture-extracted testimony from enslaved persons at ch. XXIII, before the window opens, and is deliberately not drawn on for this cell. That is a stronger record than the current one, not a weaker one.

### M5 — `ijc.search.f5-i-negative-sweep`: its one recorded finding is misdescribed, and the licensed primary text it was annotating went unrecorded

The sweep's `note` reads:

> "One real institutional detail surfaced and was NOT previously recorded: **the 73rd Apostolic Canon forbidding any slave to be ordained**, discussed in the Leo volume's own editorial apparatus (npnf212, near line 1467)"

The apparatus at `npnf212:1467–1469` actually reads:

> "The 73rd Apost. Canon forbids any slave to be ordained **without his master's consent, and without previously obtaining his freedom**. However, in the times of S. Jerome, S. Basil and S. Greg. Nazianzen, we find cases of slaves being ordained."

Dropping both conditions turns a conditional eligibility rule into a categorical bar — a materially different canon. The sweep also drops the immediately following counter-datum (cases of slaves in fact being ordained).

More significantly, the note is that editor's footnote to **Leo's own Letter IV, ch. II, "Slaves and serfs (coloni) are not to be ordained"** (`npnf212:1449–1462`), in the build's already-licensed `ijc.source.leo-letters` — Leo's own words about actual enslaved persons, inside the window:

> "even some who have failed to obtain their liberty from their masters are raised to the rank of the priesthood, as if sorry slaves were fit for that honour… the rights of masters are infringed so far as unlawful possession is rashly taken of them."

The sweep recorded the footnote and not the letter. It also missed **Leo, Sermon XLII (On Lent, IV) §VI** at `npnf212:17413`: "**Rule your slaves and those who are put under you with fairness, let none of them be tortured by imprisonment or chains**" — licensed, primary, on point for F5-I and germane to F6-E.

Finally, the sweep's framing claim — "The great majority of 'slave' hits across the licensed corpus… are Christological ('the form of a slave', Philippians 2 language)" — does not survive counting: of 72 note-stripped hits in the Leo material, 29 are literally "form of a slave," and a substantial remainder (Ep. IV.II; Serm. XLII.VI; "if this is duly observed in the case of slaves or of lands", `:12021`; "the conduct of master and of slaves") are about actual enslaved persons.

I agree with the sweep's *conclusion* — none of this is an enslaved person's own account, so `ijc.limit.f5-ordinary-day`, which is scoped to testimony and daily-life texture, stands. The problem is that a search_record whose function is an accurate statement of what the corpus holds gets the corpus wrong, at `verified-direct`.

**Fix:** restore the canon's two conditions; record Leo *Ep.* IV.II and *Serm.* XLII.VI as the primary passages found; soften "the great majority" to what the count supports; and keep the conclusion, which is sound.

### M6 — None of the five new sweeps records the searches it ran

`ijc.search.f1-t-negative-sweep`, the record these five were built to imitate, states its actual greps: "grep against cic/texts for 'Adam', 'original sin', 'tithe'…, 'This is My Body', 'Mysteries', 'faith alone', 'sola fide' - followed by direct reading of every hit inside the already-licensed Ambrose and Leo volumes." All five new sweeps state theirs only in prose — "for first-person devotional and doubt-testimony phrasing", "for reader-experience phrasing (confusion, fright, boredom, difficulty)", "for private-prayer and personal-forgiveness phrasing", "for 'slave', 'child', household, and daily-life vocabulary". Only the F5-I one names a literal string at all.

A negative search_record's whole evidentiary value is that someone else can re-run it and get the same nothing. As written, none of the five can be re-run. Compounding it, `ijc.search.c-p-negative-sweep`'s `query` names the searched corpus as "(Eusebius, Ambrose, Leo, the conciliar acts, the church historians)" while its `note` draws a conclusion about "anywhere in this world's own licensed base" — a base that also includes Lactantius, Symmachus, Athanasius, Hilary, Jerome, Ammianus, Paulinus, and Augustine IX.7. The conclusion is broader than the stated search.

Given that M7 in the prior review was raised precisely because negative claims had been drafted without documented searches, closing it with five non-reproducible searches closes the form and not the substance.

**Fix:** add the literal search strings and the file set to each `channel`, and reconcile `c-p`'s `query` scope with its `note`'s scope.

### M7 — `ijc.dw.f6-p-women-authority-cost`: `positions` was not brought down with `text`, and now contradicts itself; the body claims a source the record does not carry

The `text` fix is good and I verified it fully — every coercive detail is exact at `npnf210:41493–41512` ("the heaviest sentences were decreed, first upon the whole body of merchants"; "two hundred pounds' weight of gold was required within three days' time"; chains "placed on the necks of innocent persons" in "the last week of Lent"; "The prisons were full of trades-people"; "All the officials of the palace… were commanded to keep away") — and the new hedge is honest: "Ambrose's own letter names the emperor as the one acting on his own power; it is the volume's own chronology that names Justina as the persecution's author." The chronology citation is exact: `npnf210:703–704`, "The persecution at Milan of Catholics by Justina in Holy Week. [Ep. 20.]".

Two things did not come with it.

**(a) `positions[0]` still carries the pre-fix confidence, and is now internally contradictory:**

> women did exercise **directly coercive state authority** in this world's own record - Justina's **dominant influence over her young son** (no formal regency is attested) commanded fines, imprisonment, and the machinery of the palace, **not merely influence behind a throne**

The bullet asserts the mode ("dominant influence over her young son") and then denies that mode in the same sentence ("not merely influence behind a throne"), and it restores flatly the "directly… commanded" claim the `text` was just corrected to hedge. This is the same shape of internal contradiction the round was fixing here.

**(b) The record's body states:** "the attribution to Justina rests on the volume's own chronology (line 704) **and Sozomen, now cited as the actual warrant**." Sozomen is not cited: the record's `sources[]` are `ijc.source.ambrose-epistles` and `ijc.source.leo-letters` only. `ijc.source.sozomen-he` exists in the set and is not referenced here.

**Fix:** rewrite `positions[0]` to match `text` ("coercive state power moved through her court; Ambrose's letter names the emperor, the edition's chronology names her"); either add the Sozomen source or strike the claim that it is cited. While there: `divergence_note` is still `null` on a record whose own text now states a divergence between two sources' identification of the actor — that is what the field is for.

### M8 — R1-M2's Theodoret chapter error survives in two more records, including the story that actually carries the scene

The prior round fixed `theodoret-he`'s body, `ambrose-epistles`, and `npnf210-ambrose`; this round fixed `ijc.figure.theodosius` (both its locus and its body — verified). Still wrong:

- `ijc.story.emperor-penance.md:22` — `locus: V.17-18 (npnf203 from line 16499 …)`
- `ijc.story.emperor-penance.md:42` — "Sozomen (VII.25) and Theodoret (**V.17-18**)"
- `ijc.source.theodoret-he.md:17` — `work: "… the fullest narrative of Ambrose's exclusion and Theodosius's penance (**V.17-18**)"`

`npnf203:16499` is "Chapter XVII.—Of the massacre of Thessalonica; the boldness of Bishop Ambrosius, and the piety of the Emperor." `npnf203:16714` is "Chapter XVIII.—**Of the Empress Placilla**", on which Valesius's own printed note observes that Flacilla's material has nothing to do with this place ("nihil pertinent ad hunc locum"). The whole penance narrative is inside V.17. The story record is the one place in the set that actually tells the scene, and its locus points partly at a chapter about a different empress who died before the massacre.

**Fix:** V.17-18 → V.17 in all three.

---

## LOW

- **L1 — `ijc.quote.canon28-equal-privileges` locus start is one line late.** Cited 22224–22232; the quote opens "**For the** Fathers rightly granted privileges…" and "For the" sits at the end of `npnf214:22223`. Should be 22223–22232. (The end fix to 22232 is correct.)
- **L2 — `ijc.quote.vc-conquer-by-this` locus start is seven lines early.** Cited 61196–61208; the quote begins "He said that about noon" at `npnf201:61203`. Lines 61196–61202 are Eusebius's own preface about the emperor's oath, not quoted. (The end fix to 61208 is correct.)
- **L3 — `ijc.quote.lactantius-dream` locus implies a span it does not have.** "ch. XLIV division at line 10612, **quote through line 10620**" — the entire quote sits on line 10620 alone (the paragraph is one long line). "quote at line 10620" is what the file supports.
- **L4 — `ijc.story.vigil-in-basilica.absent_detail`: one of the three restored Ambrose phrases is Ambrose quoting his congregation, not his own censure.** The record now attributes to "Ambrose's own sermon… names and censures directly" the phrase "let him take away his laws with him." `npnf210:42440–42441` reads: "**Of him you have well said to-day:** Let him take away his laws with him." Ambrose is repeating and endorsing what the people said. The other two phrases ("giving bloody laws with his mouth", "this law, which sanctions such perfidious decrees", §24 at `:42453` and `:42459`) are unambiguously his own and are exact. Milder than the defect it replaced, but the same family.
- **L5 — `ijc.dw.f4-e-ancient-custom.text`: Augustine's "Thy" restored without its vocative.** The L9(a) fix restored the exact wording "by many, almost all, of **Thy** congregations throughout the rest of the world" into third-person narration that is not addressed to God, leaving "Thy" with no antecedent in a compiled field. Either keep the second person by attributing it ("as he says to God, 'almost all of Thy congregations…'") or paraphrase.
- **L6 — `ijc.dw.f4-e-ancient-custom` body is now stale.** It closes "All **three** instances verified in the vendored corpus (Canon 6 wording checked at the source record; Julius and Augustine at their quote records)" — a fourth source (`ijc.source.hilary-de-synodis`) was added in this round and is unaccounted for.
- **L7 — `ijc.story.altar-of-victory.text` still adds an intensifier Symmachus does not have.** Corrected from "so great a mystery… by one road only" to "so great a **secret** could not be attained by one road **alone**". `npnf210:40793–40794` reads "We cannot attain to so great a secret **by one road**." "mystery" is fixed; "alone" is the same drift as "only." It is unquoted paraphrase, so mild — and the record's trailing body and `ijc.source.symmachus-memorial` both now quote the sentence exactly, which is the fix that mattered.
- **L8 — `ijc.term.homoios.senses.personal` swapped an unsupported positive for an unsupported negative.** Was "his own ordination **required** it"; now "**not a formal subscription his ordination required**". Neither claim is sourced in the record, and the negative is arguably the harder one to defend given the subscription demanded of bishops after Constantinople 360. Safer: say what the record does show — that the confession was the imperial church's establishment in those decades — and stop there, without a claim about ordination formalities either way.
- **L9 — `ijc.search.c-p-negative-sweep` overstates the corpus's uniformity.** "every licensed author writes as a bishop, emperor, or court historian, in doctrinal, juridical, or panegyric registers." Symmachus (pagan urban prefect, whose own source record insists he is carried as "a non-Christian voice… not a Christian source"), Lactantius (rhetorician), Jerome (*De Viris*), and Ammianus are none of the three. The point survives — no first-person devotional testimony — but the reason given is false.
- **L10 — sentence-initial capitals lowercased inside quotation marks, twice.** `ijc.story.vigil-in-basilica`: "let him take away his laws with him" (file: "**L**et him"); `ijc.figure.ambrose`: "he is called by one name in the parts of Scythia" (file: "**H**e is called"). This is the identical defect the round correctly fixed in `ijc.limit.c-p-jesus-to-you` (now exact against `npnf212:14507–14509`: "Let the sinner be glad in that he is invited to pardon.  Let the gentile take courage…").
- **L11 — `ijc.dw.f6-p-women-authority-cost` cites no source for its "help convene the council" claim.** The record's only Pulcheria source is now *Ep.* CV, correctly redescribed as retrospective. The convening claim's actual warrant is **Leo *Ep.* XCV** (`npnf212:8586`ff): "**Your clemency's command, therefore, that a Synod should be held at Nicæa, and your gently expressed refusal of my request that it should be held in Italy**…" — which is excellent evidence and is cited nowhere in the record set. (`grep -rn "XCV" records/ijc/` returns nothing.) Adding it would make the record's strongest claim its best-sourced one.
- **L12 — `ijc.figure.ambrose`'s editorial bracket is now correct but oversized.** The Durostorum/Moesia Secunda correction is right (Durostorum was the seat of Moesia Secunda, not Scythia Minor), and the dropped words are restored. But the gloss is now a 22-word argument sitting *inside* the quotation marks of the sentence that carries the whole two-Auxentii identification. Move it after the closing quotation mark.
- **L13 — `ijc.figure.pulcheria` locus points seven lines past its own document's heading.** "npnf214 **from line 20330**"; the "Notes. / Anatolius of Constantinople. / (*Ep.* to St. Leo…)" heading is at `npnf214:20321`. The quoted phrase is at `:20344`ff, so the locus is inside the letter — but 20321 is the document's actual start. Trivial; the substantive fix (naming Anatolius rather than "the council's own synodal letter") is verified exact, including the quoted "most pious and in all respects faithful" and the Euphemia altar detail, and Percival's own closing sentence distinguishing this letter from "the letter of the Council to Leo" is right where the prior review said.
- **L14 — `ijc.search.f4-p-negative-sweep` overstates a count.** "the record's one documented forgiveness case (Ambrose withholding communion from Theodosius…)" — Callinicum (`ijc.story.callinicum-synagogue`, Epp. XL–XLI) is a second documented case of remission secured from the same emperor by the same bishop, and is in the set.
- **L15 — R3-L5 remains open by design.** `records/worlds.yaml` `role_label` still reads "Deacon of the Letters" without "Apocrisiarius." The prior review called this a defensible deferral to Mark's step-5a touchpoint and the BUILD-LOG records it as deliberately left; I agree and note it only so it is not lost.

---

## Verified fixed — recorded so a clearing pass does not damage it

**The prior HIGH.** The "autumn fast" is gone from all four records (`ijc.dw.f4-t-collections-discipline` text/positions/tensions, `ijc.search.f5-t-negative-sweep.note`, `ijc.source.leo-sermons.work` and body). Sermons IX and X are correctly located at `npnf212:13503` and `:13707`; the note at `:13612` and note 6 at `:13508` both check out; Sermon X §I's "purged from wicked superstitions and consecrated to deeds of mercy" is exact at `:13716`; the sermons' substantive content ("He only who knows what He has given to each…", "committed to our stewardship", the ransom/stranger/exile triad) is exact. See M3 for the one clause still over-claimed.

**All 8 prior MEDIUMs re-derived:**

- **M1 (Theodoret V.18→V.17)** — fixed in `ijc.figure.theodosius`, locus and body; `npnf203:16499` = Chapter XVII (Thessalonica), `:16714` = Chapter XVIII (Placilla). See M8 for three records still carrying the range.
- **M2 (Pulcheria bridge_line)** — fixed exactly as prescribed. "at the prayer of our most pious and beloved of Christ Emperor Marcian, and of our most pious and in all respects faithful Empress, our daughter and Augusta Pulcheria… we placed upon the holy altar the decision" verified verbatim at `npnf214:20344`ff, under the heading "Notes. / **Anatolius of Constantinople.** (*Ep.* to St. Leo. Migne, *Pat. Lat.*, Tom. LIV… col. 978.)" at `:20321`. `bridge_line` (a compiled field via `build_figures_json`) and `sources[].locus` both corrected.
- **M3 (*De Mysteriis* authorship)** — fixed exactly. `npnf210:1178–1181`: "On doctrinal grounds the authenticity of the work has been impugned by some modern writers, but there is no sufficient foundation for their arguments, as the teaching may be paralleled in many other passages of St. Ambrose. The date is not certain, but may be about a.d. 387." No century, no Benedictine editors, no "universally admitted" — all three inventions removed from `ijc.source.ambrose-de-mysteriis.author`, and the derived tensions line in `ijc.dw.f1-t-bread-made-body` corrected to match.
- **M4 (Justina attribution + internal contradiction)** — the `text` hedge and the chronology citation are correct and verified; "Justina's regency" struck. See M7 for what did not come with it.
- **M5 ("Auxentius' cruel law")** — fixed with Ambrose's actual sentences, all verified: "Let him take away his laws with him" (`npnf210:42440`, §23), "giving bloody laws with his mouth, writing them with his hand" (`:42453`, §24), "this law, which sanctions such perfidious decrees" (`:42459`, §24). Section numbering "23-24" correct. See L4 for the one attribution nuance.
- **M6 (385/386 divergence)** — disclosed in `ijc.story.vigil-in-basilica.absent_detail`, per the prior review's own prescribed location. Both warrants verified: Ep. XX's headnote, "**The date of the letter is Easter, a.d. 385**" (`npnf210:41449`), and the volume's chronology under 385 (`:700–710`), which puts the persecution, the law of Valentinian II granting Arians equal rights, and Auxentius's claim on the see all in that year.
- **M7 (five remaining cell-scoped sweeps)** — structurally closed: `ijc.search.{c-p,f2-p,f4-p,f5-i,f6-e}-negative-sweep` added, each `canon_cells`-scoped, bringing cell-scoped coverage to all 7 honest-limited cells. See M4/M5/M6 for their evidentiary quality. Worth recording in their favour: the narrow-licensing discipline they rest on is real and correctly applied — `ijc.source.augustine-confessions` is genuinely restricted to Book 9 ch. 7 ("NARROWLY LICENSED… do not extend this license"), which is what makes the C-P/F2-P/F4-P negatives honest rather than absurd.
- **M8 (Coustant)** — fixed, verbatim. `npnf204:23560–23562`: "In the passage in the text the prerogative of the Roman see is limited, as Coustant observes, to the instance of Alexandria; and we actually find in the third century a complaint lodged against its Bishop Dionysius with the Pope." Carried in `ijc.contested.primacy-reception.held_against` as a registered counter-reading, correctly framed as the edition's apparatus rather than Julius's own text.

**Prior LOWs verified fixed:** L2 (both punctuation substitutions now disclosed — `anf07`'s "appeared best**;** so that that God, who is seated in heaven, might be benign and propitious to us" and `npnf214:20296`'s "our Lord Jesus Christ**,** as the Prophets of old time have spoken concerning him…" both confirmed); L3 (the Greek gloss restored — the file prints "(ἴσα πρεσβεῖα)" at `npnf214:22227–22228`); L4 ("a modern asker" → second person, in compiled `doctrinal_witness.text`); L8 (baptism arithmetic: 380 to 395 is now correctly "fifteen years"); L9(b) partially (Hilary now sourced rather than anonymous — but see H1) and L9(c) (the self-contradictory tensions line untangled to '"antiphonal" is not the eyewitness's own word'); L10 (`ijc.source.symmachus-memorial` now quotes "we cannot attain to so great a secret by one road", exact against `npnf210:40793`); L11 (Ep. CV redescribed — verified at `npnf212:9162`ff: "He congratulates the Empress on the triumph of the Faith, but regrets the introduction of a new controversy", "brought to a satisfactory agreement through your Grace's zeal", and the Anatolius protest); L12 (`ijc.term.homoousios` narrowed to "once the Homoian settlement became imperial policy (357 onward)", with Athanasius's earlier exiles correctly distinguished); L13 (Leo Sermon XXI.I now exact: "Let the sinner be glad in that he is invited to pardon.  Let the gentile take courage in that he is called to life.", `npnf212:14507–14509`).

**Quote texts:** all 20 machine-diffed against their editions, whole-file, note-stripped — **all exact**. The four apparent mismatches are the build's own disclosed conventions and check out: `nicene-creed` (the two Greek glosses "(γεννηθέντα)" and "(ὁμοούσιον, consubstantialem)" omitted per the stated convention, the two square-bracket insertions kept as printed), `canon28-equal-privileges` (the "(ἴσα πρεσβεῖα)" gloss omitted, now correctly named), `chalcedon-definition` and `milan-edict` (truncations, now disclosed), `augustine-vigil-hymns` (one sentence elided, with the ellipsis and the elided sentence both stated in the body). `jerome-damasus-verses` verified word-for-word at `npnf203:41380–41384`.

**Round-1 spot checks, independently re-derived:** Callinicum's "burnt by Christians **at the instigation of the bishop**" (`npnf210:43564`) and "the synagogue **be rebuilt by the Bishop himself**" (`:43165`); Leo *Ep.* LIX.4's "after the transmission of original sin to their descendants" (`npnf212:7397`); Chalcedon Session IV with Paschasinus speaking first and reciting Nicaea → Constantinople → Ephesus/Cyril → Leo (`npnf214:20103`ff); Ambrose *Concerning Widows* I.2 quoting 1 Cor. 7 (`npnf210:38845`). The prior confirmation review's account of these is accurate.

**Compiled-field leakage:** clean. A regex scan of every field `build_prompt()`, `_chunk_text()`, and `build_figures_json()` actually read — `doctrinal_witness.text`, `honest_limit.statement`, `story.text`/`tellable_as`, `term.plain_meaning`/`quick_meaning`/`world_word`, `world_core.horizon`/`formation_logic`/`thinness`/`cautions`, `figure.bridge_line`, `quote.text` — for build-process language, ISO dates, vendored-file names, `Doc_XX` references, record ids, sibling-world names, and "at review"/"corrected" phrasing returned **no** true hits. Every match on "record" is in-world usage ("our record", "this world's record"). The two internal record-id references in `world_core.cautions` are the one precedented location. This round's new build-process disclosures all landed in non-compiled fields (`story.absent_detail`, `source.work`/body, `search_record` bodies, trailing bodies), consistent with the build's own convention and with the `no-build-attribution` gate's deliberately narrow scope.

**Mechanical gates:** 13/13 clean over 142 records — schema-validation, referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution — **zero findings in every gate**. Independently: 142/142 front matters `yaml.safe_load` individually with no parse failures; 0 non-reciprocal relation edges; 0 dangling relation targets; 0 dangling `source_id`s; all 28 canon cells carry at least one record. Record-type distribution: 23 search_record · 23 source · 20 quote · 12 doctrinal_witness · 12 figure · 12 term · 10 force · 9 story · 7 contested_claim · 7 honest_limit · 6 gravity · 1 world_core.

---

## Fix ordering

1. **H1** — the Hilary counter-datum, in `ijc.dw.f4-e-ancient-custom.text` and its `sources[].locus`. It is the only finding here that puts a false statement about the vendored corpus into compiled participant-facing content.
2. **M2** — the "West's congregations" residual in `ijc.story.vigil-in-basilica.text`. One clause, compiled field, and the set currently contradicts itself.
3. **M1, M8** — the three broken quote loci and the three surviving V.17-18 references. Both mechanical; the loci should be regenerated by script with a containment assertion so this class cannot recur.
4. **M3, M7** — the two scope/confidence mismatches: the octave attribution in the collections witness, and `positions[0]` plus the phantom Sozomen citation in the women's-authority witness.
5. **M4, M5, M6** — the three sweep-quality findings. These are the substance of the M7 closure and are worth doing properly; M4 in particular replaces a false claim with a stronger true one.
6. **L1–L15** — the rest.

No finding in this pass contradicts Doc_01 or Step 0 settled ground, and none requires reopening anything the three original reviews or the first confirmation pass cleared.

**A standing recommendation, offered because the pattern is now three-for-three:** every round has fixed its findings and introduced a smaller set of the same kind, and this round's largest single cause was adopting a reviewer's asserted line numbers without opening the file. Two cheap mechanical guards would have caught most of what is above: a containment assertion for every `quote.locus` (the minimal-range computation is a few lines), and a rule that a claim in a compiled field must be traceable to a primary passage rather than to an edition's apparatus, with apparatus-sourced claims flagged in the field that carries them rather than only in the record body.
