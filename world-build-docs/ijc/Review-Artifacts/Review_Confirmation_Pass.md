# Adversarial Confirmation Pass — `records/ijc/` after the 2026-08-21/22 fix round

**Branch:** `world/ijc` (137 records) · **Reviewed:** 2026-08-22 · **Reviewer:** isolated Opus dispatch, follow-up verification
**Method:** every fix re-derived from the vendored files in `/home/user/CIC-Project/cic/texts/` with `<note>`/`<scripRef>` elements stripped before comparison (regex note-stripper, entities unescaped, whitespace normalized); nothing accepted from the BUILD-LOG's own account, nothing accepted from memory. Gate battery run directly against `engine.m1.gates.run_all` with `loader.load_world_records("ijc")`; every record's front matter additionally `yaml.safe_load`-ed file-by-file.
**Prior artifacts checked against:** Review1_Quote-Source-Fidelity_Round1.md, Review2_Historical-Accuracy_Round1.md, Review3_Canon-Structure-Discipline_Round1.md, BUILD-LOG.md §6, and the full fix diff `3397335e..HEAD -- records/ijc/`.

---

## Summary verdict: MOSTLY CONFIRMED — 22 residual/new findings (1 HIGH, 8 MEDIUM, 13 LOW)

**The headline is good and should be stated plainly: all 12 HIGH findings from the three original reviews are genuinely fixed.** Not merely changed — changed to something I could verify true against the vendored file, at the right scope, with the right citation. The Milan-agreement quote conflation, the Auxentius over-split, Callinicum's actual content, the hymn-singing rescope, the Chalcedon three-week interval, the inverted Julius/Alexandria clause, the three false honest_limit negatives, the F6-P stretched tag, and the missing cell-scoped negative searches were each re-derived from source and each check out. Twenty-two of the twenty-four MEDIUM findings are fixed or defensibly dispositioned. The new material is, on the whole, better-sourced than the material it replaced: the Ambrose *De Mysteriis*, Leo *Ep.* LIX, Ambrose *Concerning Widows*, Ambrose *Ep.* XX.6–7, Ambrose *Epp.* XL–XLI, and Chalcedon Session IV passages are all exact.

The verdict falls short of clean for three reasons, in descending weight:

1. **One new factual error was introduced** by the fix pass and propagated into four places, including two compiled participant-facing fields, at `verified-direct`/`load-bearing`: Leo's "Collections" sermons are tied to an "autumn fast" that does not exist. The vendored file's own explanatory note, three paragraphs from the passage cited, identifies the occasion as the octave of SS. Peter and Paul (early July) — a collection day, not a fast.
2. **Five more fixes each landed a smaller new error or a misattribution** of the same family the reviews were built to catch — a chapter title quoted as an author's sentence, a document misidentified, claims attributed to an edition's introduction that it does not make.
3. **R1's LOW block was almost entirely not worked.** Not one quote `locus` line-range was edited in the whole fix diff, so all seven of R1-L7's too-narrow loci stand exactly as they were.

None of this reopens Step 0 or Doc_01 settled ground, and none of it is unfixable in a short pass.

## What was checked

| Scope | Checked |
|---|---|
| Original HIGH findings | **12/12** re-derived from source against current record state |
| Original MEDIUM findings | **24/24** re-checked at record + citation level |
| Original LOW findings | **18/~22** spot-checked (task asked for ≥10) |
| New records (12) | **12/12** read in full; every source locus and quoted span re-verified against the vendored file |
| Quote records | **20/20** texts re-diffed against their editions; **20/20** loci machine-checked for containment |
| Compiled-field leakage | Every `doctrinal_witness.text`, `honest_limit.statement`, `story.text`/`tellable_as`, `term.plain_meaning`/`quick_meaning`/`world_word`, `world_core.horizon`/`formation_logic`/`thinness`/`cautions` scanned against the `build_prompt()`/`build_chunks()` field contract in `engine/m2/builders.py` |
| Mechanical gates | **13/13 clean**, 137 records, 0 findings across all gates |
| YAML front matter | **137/137** parse individually under `yaml.safe_load`; 0 failures |

---

## HIGH

### H1 — `ijc.dw.f4-t-collections-discipline`: Leo's Collections sermons tied to an "autumn fast" that does not exist; propagated to 3 further records

The record (new, added by the fix pass to correct R3-H2) states in `text`:

> This world had a real giving discipline, preached at least twice in the sermons that survive, **tied to an autumn fast kept for exactly this purpose**

and again in `positions`:

> this discipline was **tied to a specific liturgical occasion (an autumn collection-fast)**, giving it institutional shape rather than leaving it as private virtue alone

and again in `tensions` ("proportional almsgiving preached at a particular fast"). It propagates verbatim into `ijc.search.f5-t-negative-sweep.note` ("preach proportional almsgiving as a binding duty tied to an autumn fast") and into `ijc.source.leo-sermons.work` and its trailing body ("on almsgiving discipline tied to the autumn collection-fast").

**Both halves are wrong, and the vendored file says so in the very passage cited.** Sermon IX is at `npnf212_leo-great-gregory-great.xml:13503`, Sermon X at `:13707` — both correctly located by the record. But at `:13612–13617`, inside Sermon IX §III, the edition's own note on *dies apostolicæ institutionis* reads:

> "Dies apostolicæ institutionis: this was, as note 6 explains, **the octave of SS. Peter and Paul**, but how far Leo actually attributes its institution to the Apostles themselves, is a little doubtful."

and note 6 itself (`:~13400`) glosses it "octave of SS. Peter and Paul), the day on which in pagan times the…". The occasion is therefore **early July, not autumn**, and it is a **collection day, not a fast**. Sermon X's own opening confirms the character — "celebrate with the devotion of religious practice that day which they purged from wicked superstitions and consecrated to deeds of mercy" (`:13716`) — a day of almsgiving replacing a pagan festival.

Leo's autumn fast is a separate and separately-preached thing: "we keep the spring fast in Lent, the summer fast at Whitsuntide, **the autumn fast in the seventh month**, and the winter fast in this which is the tenth month" (`:14420`), preached in Sermons LXXXVIII–XC "On the Fast of the Seventh Month" (`:21349`ff). Those sermons contain no reference to the Collections at all (checked: zero hits for "collection" in `:21349–21560`). The build appears to have conflated two distinct Leonine occasions.

**Why HIGH:** this is the project's own named failure mode — a real, sourced fact carried at the wrong scope — newly introduced *by* the round that existed to eliminate it, in `doctrinal_witness.text` and `positions` (both compiled into `prompt.txt` and the `doctrinal_witness` chunk), at `citation_specificity: A` / `verification_state: verified-direct` / `evidentiary_weight: load-bearing`. The remainder of the record is sound and well-sourced — I verified "He only who knows what He has given to each, discerns aright how much a man can and how much he cannot do" (`:13733`), "committed to our stewardship" (`:13738`), and the ransom/stranger/exile triad ("if out of the abundance of their great possessions the captive gets not ransom, nor the stranger comfort, nor the exile relief. Rich men of this kind are needier than all the needy… outwardly splendid, they have no light within", `:13757`ff) — so the fix is one clause away from correct.

**Fix:** in all four records, replace "an autumn fast"/"the autumn collection-fast" with the day the file names — the annual collection on the octave of SS. Peter and Paul, a day of almsgiving that displaced a pagan festival (Serm. IX §III, X §I; the edition's note at `npnf212:13612`). Drop the word "fast" from the giving-discipline claim entirely, or state separately that Leo *also* preached seasonal fasts, which is true but is a different set of sermons and is not what these two license.

---

## MEDIUM

### M1 — `ijc.figure.theodosius`: R1-M2's fourth occurrence of the wrong Theodoret chapter was missed

R1-M2 named three records citing the penance scene as **V.18**; all three (`theodoret-he`, `ambrose-epistles`, `npnf210-ambrose`) now correctly read V.17. But `ijc.figure.theodosius`'s body still reads:

> Ambrose's own contemporary letter (Ep. 51 …) versus **Theodoret V.18** (the famous dramatic scene, a generation later, told to edify)

Verified: `npnf203_theodoret-jerome-gennadius-rufinus.xml:16499` is "Chapter XVII.—Of the massacre of Thessalonica; the boldness of Bishop Ambrosius, and the piety of the Emperor"; `:16714` is "Chapter XVIII.—**Of the Empress Placilla**", which has nothing to do with the penance. **Fix:** V.18 → V.17 in the body; and since the whole scene sits inside V.17, the `sources[].locus` "V.17-18" can drop the range too.

### M2 — `ijc.figure.pulcheria`: the new bridge_line sourcing misidentifies the document

The fix for R2-M5 replaced the unsourced "hailed as its guardian" with:

> `bridge_line:` the empress **the council's own synodal letter** names alongside Marcian as "most pious and in all respects faithful"…
> `sources:` — `ijc.source.chalcedon-acts`, locus: **the council's own synodal letter to Leo** (npnf214 from line 20330)

The phrase is real and verbatim — "at the prayer of our most pious and beloved of Christ Emperor Marcian, and of our most pious and in all respects faithful Empress, our daughter and Augusta Pulcheria" (`npnf214:20344`ff). But it is **not from the council's synodal letter.** The passage is headed, at `npnf214:20328`:

> "Notes. **Anatolius of Constantinople.** (Ep. to St. Leo. Migne, Pat. Lat., Tom. LIV. … col. 978.)"

and Percival's own sentence closing the extract explicitly distinguishes the two documents: "From this passage can easily be understood the very obscure passage **in the letter of the Council to Leo**…" It is Anatolius of Constantinople's own letter, printed in Percival's editorial Notes.

**Why MEDIUM:** the fix cured an unsourced bridge_line by creating a misattributed one, in a field the record set treats as participant-facing. **Fix:** "the letter Anatolius of Constantinople sent to Leo, which names her…", and correct the `sources[].locus` accordingly.

### M3 — `ijc.source.ambrose-de-mysteriis`: three claims attributed to "this edition's own introduction" that the introduction does not make

The `author` field reads:

> Ambrose of Milan (attributed; authenticity questioned by some **16th-century** and later writers, but **accepted by the Benedictine editors** and, **per this edition's own introduction, now universally admitted**)

The edition's introduction (`npnf210_ambrose-select-works-letters.xml:1172–1181`) says, in full, on this point:

> "On doctrinal grounds the authenticity of the work has been impugned **by some modern writers**, but there is **no sufficient foundation for their arguments**, as the teaching may be paralleled in many other passages of St. Ambrose."

No century is named; the Benedictine editors are nowhere associated with *De Mysteriis* (the introduction associates them with *De Sacramentis*, a different and doubtful work, at `:1673`); and "universally admitted" appears nowhere in the file (greps for `universally admitted`, `sixteenth century`, `16th` return nothing relevant). The derived `tensions` line in `ijc.dw.f1-t-bread-made-body` carries the same unsupported "**from the sixteenth century onward**" into a compiled `doctrinal_witness` field.

**Fix:** rewrite to what the introduction actually says, or drop the "per this edition's own introduction" warrant. The record's substantive content is otherwise exact — I verified *De Myst.* IX §50 and §54 word-for-word at `npnf210:33204`ff and `:33263`ff, and the c. 387 dating at `:1181`.

### M4 — `ijc.dw.f6-p-women-authority-cost`: Ep. XX.6–7 is cited at `verified-direct` for a claim its own text does not make

The record's `text` states Justina "commanded the machinery of the state directly… That was real power, **exercised in her own name**", sourced to `Ep. XX.6-7 (npnf210 from line 41434)` at `citation_specificity: A` / `verification_state: verified-direct`.

The coercive detail is exact — I verified every element at `npnf210:41493–41512`: "the heaviest sentences were decreed, first upon the whole body of merchants", "two hundred pounds' weight of gold was required within three days' time", chains "placed on the necks of innocent persons" in "the last week of Lent", "The prisons were full of trades-people", "All the officials of the palace… were commanded to keep away". **But Ambrose never names Justina in Epistle XX.** The decrees are given in the passive, and where an actor is named it is the emperor: "the Emperor was exercising his rights since everything was under his power" (§8). A grep of the whole volume puts "Justina" at `:514, 692, 704, 727, 993, 998, 1093, 1618, 8154` (all front matter, chronology, or editorial introduction) and at `:41944` — a note inside *Letter XXI*, not XX. The attribution to Justina is real history but comes from the edition's editorial framing and from Sozomen, not from the cited locus.

Compounding it, the record contradicts itself internally: `text` says "**no formal regency is attested**" (correctly, fixing R2-L3), while `positions` still reads "**Justina's regency** commanded fines, imprisonment, and the machinery of the palace".

**Fix:** either drop the confidence to match the actual chain (Ambrose documents the coercion; the attribution to Justina is the edition's and Sozomen's), or add the volume's own chronology (`npnf210:704`, "The persecution at Milan of Catholics by Justina in Holy Week") as the warrant for the attribution and cite it. And strike "regency" from `positions` to match the record's own correction.

### M5 — `ijc.story.vigil-in-basilica`: an NPNF editorial summary quoted as Ambrose's own sermon wording

`absent_detail` now reads:

> a real imperial law (January 386, granting Homoian worship assembly) that **Ambrose's own sermon on the crisis names and censures as "Auxentius' cruel law"**

That phrase is the NPNF editor's *argument* prefixed to the sermon, at `npnf210:42083`: "…he **censures Auxentius' cruel law**, answers the Arians' objections, and states that he will gladly discuss the matter in the presence of the people." Ambrose's own body text uses different words — "Let him take away his laws with him" (§23, `:42432`), "giving bloody laws with his mouth, writing them with his hand" and "this law, which sanctions such perfidious decrees" (§24, `:42443`ff).

This is the identical defect R2-L9 caught in `ijc.figure.damasus` (a chapter title quoted as Socrates's sentence) — fixed there, reintroduced here. The substance survives intact: Ambrose does name and censure the law as Auxentius's own. **Fix:** quote Ambrose's own words ("his laws", "bloody laws", "perfidious decrees") or drop the quotation marks.

### M6 — Undisclosed record-vs-edition dating divergence on the Milan basilica crisis (R2-M2's residual)

Every ijc record dates the great basilica standoff to **386** and the enabling law to **January 386** (`ijc.story.vigil-in-basilica`, `ijc.figure.ambrose.floruit`, `ijc.figure.justina.floruit`, `ijc.dw.f6-p-women-authority-cost`, `ijc.core.imperial-juridical`). This follows mainstream scholarship and I have no quarrel with the history. But the vendored edition these records cite as their direct warrant dates it differently and says so twice:

- `npnf210:41438` (Ep. XX's own headnote): "**The date of the letter is Easter, a.d. 385.**"
- `npnf210:704–710` (the volume's chronology): under **385** — "The persecution at Milan of Catholics by Justina in Holy Week. **The law of Valentinian II., granting Arians equal rights with Catholics. Auxentius claims the see of Milan.** [Sermon against Auxentius…]"

`grep -rn "385" records/ijc/` returns **zero hits**: the divergence is nowhere carried. This is exactly the class the record set's own `world_core` caution 5 makes binding ("CONTESTED DATING AND ATTRIBUTION carried as first-class content, never silently resolved"), and it is the un-worked half of R2-M2 (whose "385 precursor" was never added).

**Fix:** one clause in `ijc.source.ambrose-epistles` or `ijc.story.vigil-in-basilica.absent_detail` noting that de Romestin's edition dates Ep. XX and the law to Easter/385, and that this build follows the now-dominant 386 chronology — the same treatment the build already gives the two conversion accounts.

### M7 — R3-H5's structural fix covers 2 of the 7 honest-limited cells

R3-H5 ("no search_record anywhere documents a negative search for ANY honest-limited cell's subject matter") was called the single most consequential fix in that review. Two cell-scoped sweeps were added — `ijc.search.f1-t-negative-sweep` and `ijc.search.f5-t-negative-sweep` — and both are good records: I verified every positive find they claim (Leo *Ep.* LIX.4 at `npnf212:7398`; Ambrose *De Myst.* IX at `npnf210:33189`; *Concerning Widows* I.1–2 at `npnf210:38813`; Leo Serm. IX–X at `npnf212:13503/13707`).

But the remaining five honest-limited cells — **C-P, F2-P, F4-P, F5-I, F6-E** — still carry negative claims with no documented negative search behind them. All 16 pre-existing search_records remain work/volume-scoped (only 2 of 18 carry a `canon_cells` value). The root cause the review diagnosed is corrected only where it had already produced a caught error; the same exposure remains on five cells nobody has swept. Given that two of the three false negatives were found in already-vendored, already-licensed volumes, that is a live risk, not a theoretical one.

**Fix:** run the five remaining cell-scoped sweeps and record them, or state explicitly in the BUILD-LOG that the structural fix was scoped to the two cells with known errors and that the other five remain un-swept.

### M8 — R2-M9's second half was not worked: the vendored counter-reading of Julius's "custom" is still carried nowhere

The primary half is fixed well — `ijc.quote.julius-custom` and `ijc.figure.julius` now scope "earliest surviving voice" to this world's own window and name Victor c.190 and Stephen 256 as outside it.

The second half is untouched. Three lines below the quoted sentence, the vendored NPNF204 apparatus reads (`npnf204_athanasius-select-works-letters.xml:~23552`):

> "**In the passage in the text the prerogative of the Roman see is limited, as Coustant observes, to the instance of Alexandria**; and we actually find in the third century a complaint lodged against its Bishop Dionysius with the Pope."

`grep -rn "Coustant" records/ijc/` returns nothing. This is a limiting reading of the build's single most load-bearing primacy quote, sitting inside the build's own vendored file, and neither the quote record, `ijc.gravity.primacy-claiming`, nor `ijc.contested.primacy-reception` (which is otherwise the strongest record in the set) records it.

**Fix:** one sentence in `ijc.contested.primacy-reception.held_against` or the quote record's body carrying Coustant's limitation as a registered counter-reading.

---

## LOW

- **L1 — R1-L7 entirely unfixed.** `git diff 3397335e..HEAD -- records/ijc/quote/ | grep locus` returns **nothing**: not one quote locus was edited. Machine-verified misses: `nicene-creed` cited 2404–2416 (quote runs past 2416 to "…in the Holy Ghost"); `canon28-equal-privileges` 22218–22231 (runs past 22231); `constantine-bishop-outside` cited at the single line 66733 (actual span 66693–66733); `julius-custom` 23550–23552 (actual 23510–23551 — the cited start is *after* the quote begins); `leo-tome-each-form` 5366–5372 (actual 5326–5380); `lactantius-dream` cited at the single line 10612, the chapter-division line (the quote runs to 10620); `vc-conquer-by-this` 61196–61207 off by one (needs 61208). All quote **texts** remain exact; only the loci are wrong.
- **L2 — R1-L8 unfixed.** `ijc.quote.milan-edict` still ends "…appeared best." where `anf07:10684` reads "…appeared best**;** so that that God…"; `ijc.quote.chalcedon-definition` ends "…our Lord Jesus Christ." where `npnf214:20296` reads "…our Lord Jesus Christ**,** as the Prophets of old time have spoken…". Neither substitution is disclosed, while `julius-custom` discloses its own.
- **L3 — R1-L9 unfixed.** `ijc.quote.canon28-equal-privileges`'s note still puts the edition's inline gloss in Latin letters — 'the edition's inline Greek gloss **"(isa presbeia)"**'. The file prints "(ἴσα πρεσβεῖα)" (`npnf214:22226`).
- **L4 — R3-L8 unfixed.** `ijc.dw.f4-t-baptism-threshold.text` still addresses "**a modern asker**" in the third person inside compiled answer-ground.
- **L5 — R3-L5 unfixed.** `records/worlds.yaml` `role_label` still reads "Deacon of the Letters", dropping "Apocrisiarius" from Mark's own recorded 2026-07-22 decision, which survives only in the adjacent comment. (Defensible as deferred to the step-5a touchpoint, but it is unfixed.)
- **L6 — R2-L8 unfixed.** `ijc.term.homoios`'s personal sense still asserts a formal requirement — "his own ordination **required** it".
- **L7 — `ijc.figure.ambrose`, inside the H-1 fix's own warrant quotation.** Two small defects in the *Sermo c. Aux.* 22 citation, which is the whole evidentiary basis for the two-Auxentii identification. (a) The quotation silently drops words: the record has "called by one name in the parts of Scythia […], called by another here"; `npnf210:42422` reads "**He is** called by one name in the parts of Scythia, **he is** called by another here." (b) The inserted gloss "**[Durostorum's own province]**" is wrong — Durostorum was the seat of Moesia Secunda, not Scythia Minor; Ambrose's "the parts of Scythia" is a loose lower-Danube reference. An inaccurate editorial bracket placed inside the quotation that carries the identification is worth correcting even though the identification itself is right. Same gloss propagates as "Scythian origin" (correct, as written) into `ijc.source.auxentius-letter-ulfila`.
- **L8 — `ijc.dw.f4-t-baptism-threshold`, arithmetic in the R2-M8 fix.** "Theodosius was baptized early in his reign (380, within two years of taking power, **sixteen years before his death**)". Baptized 380, died 395 — **fifteen** years. (R2-M8 said "year 2 of 16", meaning the reign's length; the fix converted that into a wrong interval.)
- **L9 — `ijc.dw.f4-e-ancient-custom`, three residuals in the R2-H3 fix.** (a) The record renders Augustine's scope as "imitated… by many, almost all, of **the West's** congregations"; `npnf101:13774` reads "by almost all of Thy congregations **throughout the rest of the world**" — a narrowing, so safer than the original error, but still not what Augustine wrote, and the same phrasing is carried into `ijc.story.vigil-in-basilica.text`. (b) The Hilary counter-datum H-3 asked for is asserted anonymously ("a Latin hymn tradition already existed before 386 in the West's own record") and left **unsourced**, though it is in this build's own registered `npnf209` at `:3709–3731` ("He has always had the fame of being the earliest Latin hymn writer"; "in its 13th canon couples Hilary with Ambrose as the writer of hymns"). (c) The `tensions` line is self-contradictory: "**the eyewitness's own word** 'antiphonal' is not in this record's evidence" — it is not the eyewitness's word, which is the point.
- **L10 — `ijc.source.symmachus-memorial` / `ijc.story.altar-of-victory`.** Both put in quotation marks "so great a **mystery** could not be reached by one road **only**". `npnf210:40794` reads: "We cannot attain to so great a **secret** by one road." The story's `text` presents it as unquoted paraphrase (acceptable); the source record's body and the story's trailing body both quote the drifted wording.
- **L11 — `ijc.dw.f6-p-women-authority-cost`, locus annotation.** Leo's Ep. CV is described as "addressed as the convening power for **a new council**". `npnf212:9162`ff shows Ep. CV congratulating Pulcheria on a synod **already held** ("through your Grace's zeal") and protesting Anatolius's Canon 28. Her standing as a real addressee — the record's actual point — is fully borne out; the "new council" framing is not.
- **L12 — R2-M7 residual.** The anachronism was fixed where it was sharpest (`ijc.figure.constantius`'s locus now distinguishes the 340s–350s "Eusebian" depositions from the Homoian settlement of 357 onward), but `ijc.term.homoousios`'s personal sense still lumps all exiles under "bishops exiled under **Homoian emperors**".
- **L13 — `ijc.limit.c-p-jesus-to-you`, in the R3-M3 fix.** The quoted Leo passage lowercases and re-punctuates inside the quotation marks: the record has "let the sinner be glad in that he is invited to pardon**;** let the gentile take courage…"; `npnf212:14509` reads "**L**et the sinner be glad in that he is invited to pardon**.**  **L**et the gentile take courage…". Trivial, and the substance and the Sermon XXI.I citation are both exact.

---

## Verified fixed — recorded so a clearing pass does not damage it

**All 12 HIGH findings, each re-derived from source:**

- **R1-H1** `ijc.source.lactantius-de-mortibus` — now carries the ANF7 wording ("When we, Constantine and Licinius, emperors, had an interview at Milan…", `anf07:10684`) and explicitly names the Eusebius/McGiffert wording as the *other* transmission, correctly located at `npnf201:50280`. All four file-line claims (414, 9967, 10612, 10676) verified exact.
- **R2-H1** `ijc.figure.ambrose` — two Auxentii, not three, warranted from *Sermo c. Aux.* 22 (`npnf210:42414`ff: "The portent is one, the names are two! … he changed his name so as to call himself Auxentius, because there had been here an Arian bishop, named Auxentius"), at disclosed dominant-not-unanimous confidence, propagated correctly to `ijc.source.auxentius-letter-ulfila`, `ijc.contested.homoian-content`, and `ijc.core.imperial-juridical`'s Absent Stories item (2).
- **R2-H2** Callinicum — new `ijc.story.callinicum-synagogue` is excellent and fully sourced: "burnt by Christians **at the instigation of the bishop**" and "the synagogue **be rebuilt by the Bishop himself**" both verified (`npnf210:43565` and `:43166`); the Valentinian meeting-house, the monks' punishment, the sermon before Theodosius and the withheld sacrifice all confirmed against Epp. XL–XLI. Propagated into `ijc.gravity.episcopal-independence`'s description and manifestations and into `ijc.limit.f6-e-earlier-windows.statement`.
- **R2-H3** Hymn-singing — rescoped to Augustine's own hedge and "antiphonal" struck from the claim (see L9 for what remains).
- **R2-H4** Chalcedon interval — "three weeks" and 10 Oct/31 Oct 451 now stated identically in `ijc.story.tome-that-would-not-bend`, `ijc.force.authority-contest`, and `ijc.quote.peter-has-spoken`. (Note: Percival's extracts do not themselves date Session II; the dates rest on mainstream chronology, with `npnf214:20517` independently attesting an Oct. 31 session.)
- **R2-H5** `ijc.gravity.primacy-claiming` — the inverted clause is corrected exactly as prescribed, with the Eusebian gloss folded in.
- **R3-H1/H2/H3** — the three false honest_limit negatives are corrected and the replacements verified word-for-word: Leo *Ep.* LIX.4 "after the transmission of original sin to their descendants" (`npnf212:7398`, letter confirmed at `:7250` as "To the Clergy and People of the City of Constantinople"); Ambrose *De Myst.* IX §§50/54 (`npnf210:33204`, `:33263`); Ambrose *Concerning Widows* I.2 quoting 1 Cor. 7 (`npnf210:38845`, treatise at `:38813`, division at `:38761`).
- **R3-H4** F6-P — the stretched tag is removed from `ijc.story.emperor-penance` and the cell is now answered by two records that genuinely address its questions (f6-p-05 by Callinicum, f6-p-06 by the new women's-authority witness).
- **R3-H5** — two cell-scoped negative sweeps added (see M7 for the residual).

**MEDIUM findings verified fixed:** R1-M3 (nicene-creed brackets — the two square-bracket insertions are now kept as printed and the Greek/Latin glosses correctly named as the single omission convention, all verified at `npnf214:2404`ff); R1-M4 (chalcedon-definition — "[of God]"/"[united]" kept, "[Person]" correctly identified as falling outside the span at `:20279`); R1-M5 (`ijc.search.ammianus-english` now backed by a real fails-closed source record); R1-M6 (the file does print Greek Χ U+03A7 at `anf07:10620` — verified); R2-M1, M3, M4 (Sozomen VII.25 confirmed at `npnf202:42146` as an independent corroborating chapter), M6, M8, M10 (Session IV verified precisely: Paschasinus speaks first and recites Nicaea → Constantinople → Ephesus/Cyril → Leo's writings, and the bishops then cry out "So we all believe, so we were baptized, so we baptize" — `npnf214:20105`ff); R3-M1, M2, M3 (Leo Serm. XXI.I verified at `npnf212:14509`), M4, M5 (all 12 doctrinal_witness records now tier 1), M6 (both reshaping edges now `tension-with`, reciprocity gate clean), M7.

**LOW findings verified fixed:** R1-L10; R2-L1 (dangling ref), L2, L4, L5, L6, L7 (the Ammianus casualty note is exact — `npnf202:14189`: "one hundred and thirty-seven citizens were killed in the course of a single day"), L9 (Socrates's own sentence "many lives were sacrificed in this contention" verified at `npnf202:14209`, correctly distinguished from the chapter heading at `:14175`), L10 (Canon 3's "because Constantinople is New Rome" at `npnf214:14400` and Canon 28's "because it was the royal city" at `:22225` now correctly separated in `world_core.formation_logic` and `ijc.term.nea-rhome`); R3-L2, L3, L6.

**Compiled-field leakage:** clean. A field-by-field scan against `engine/m2/builders.py`'s actual contract found no "other worlds"/"worlds that kept them"/sibling-world names/review-process language in any of `doctrinal_witness.text`, `honest_limit.statement`, `story.text`, `story.tellable_as`, `term.plain_meaning`/`quick_meaning`/`world_word`, or `world_core.horizon`/`formation_logic`/`thinness`. `world_core.cautions` §6 no longer names sibling worlds; the two internal record-id references remaining there ("see ijc.contested.office-holder-scope", "see ijc.contested.homoian-content") sit in the one location the `alx` exemplar precedents. "Corrected at review" language survives in `gravity.description`, `story.absent_detail`, and trailing bodies — all of which are outside the compiled contract, so this is consistent, not leakage.

**Mechanical gates:** 13/13 clean over 137 records (schema, referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution), zero findings. Independently, all 137 front matters `yaml.safe_load` individually with no parse failures — no unquoted colons, no unescaped apostrophes inside single-quoted scalars. All 20 quote texts remain exact against their editions; note-stripping still holds in every interleaved case.

---

## Fix ordering

1. **H1** — the autumn-fast error, in all four records. It is in compiled participant-facing content and is the only finding here that would put a false statement in a Representative's mouth.
2. **M2, M3, M5** — the three misattributions (Anatolius's letter, the *De Mysteriis* introduction, the NPNF argument-summary). Each is a one- or two-sentence rewrite and each is the exact defect class this review series exists to catch.
3. **M1, M4** — the wrong Theodoret chapter and the Justina attribution/confidence mismatch.
4. **M6, M8** — two disclosure gaps: the 385/386 edition divergence, and Coustant's limiting reading of Julius.
5. **M7** — decide and record: run the five remaining cell-scoped sweeps, or state the scope limit honestly in the BUILD-LOG.
6. **L1–L3** — R1's unworked LOW block; L1 in particular is mechanical and can be regenerated from a script rather than by hand.
7. **L4–L13** — the rest.

No finding in this pass contradicts Doc_01 or Step 0 settled ground, and none requires reopening any finding the three original reviews cleared.
