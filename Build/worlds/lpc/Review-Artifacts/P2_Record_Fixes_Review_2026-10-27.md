# lpc record fixes for live findings F14 and F22 (Candida, etic and build wording): independent review

- Branch: current working branch, change set `git diff origin/main -- records/lpc Build/worlds/lpc/scripts` (10 files: 5 records, 5 generators).
- Findings answered: F14 and F22 of `Live_Validation_Review_2026-10-27.md` (lines 43 and 54).
- Scope: `lpc.story.celerinus-writes-to-lucian` (`use_note.means`, `tellable_as`, `text`); `lpc.quote.the-case-set-before-the-bishop` (`use_note.means`); world_core `horizon`, `thinness`, `cautions` item 6, `thin_topics` note; `lpc.gravity.conciliar-authority-theory` (`description`, `manifestations`); `lpc.term.the-one-episcopate` (`senses.informational`); mirrors in `wb_lpc_s21.py`, `wb_lpc_s22.py`, `wb_lpc_s24.py`, `wb_lpc_s25.py`, `wb_lpc_s2u_use_notes.py`.
- Reviewer model: Opus 5.5 (`claude-opus-5-5`). Round 1.
- No repo file was modified other than this one. No command that calls a model was run. No engine build was run.

## Which fields the voice reads

This decides where each fix has to land, so it was checked in the engine first.

- Story: the voice reads `tellable_as` (`engine/m2/builders.py` "Story" section; `engine/m4/evidence.py` `_head_text`), plus `use_note.means`, `claim_guards` and `not_for` (evidence entry). Story `text` is **never voiced**: both functions raise rather than fall back to it. `absent_detail` is not voiced either.
- Quote: `modern_rendering`, `means`, guards. Gravity: `name` (the "Gravities" list in the compiled prompt, and the participant-facing citation card via `strip_name_taxonomy_tag`) and `description`. Term: `plain_meaning` and `quick_meaning`; `senses` is not voiced.
- World_core: `horizon`, `formation_logic`, `thinness`, `cautions`, `living_traditions` are voiced. `thin_topics` goes to the grounding net, not the prompt.

Consequence for F14: the live finding said "add it to `text`". `text` is the record of what the source says, so a faithful Candida sentence there is right, but it cannot change what the voice says. The voiced fix is in `means`, `tellable_as` and the guards. For F22: the gravity `name` "Conciliar Authority Theory: Egalitarian vs. Hierarchical" is voiced, unchanged, and is the most likely source of Deep Interview turns 8 and 10.

## Checks

1. **New factual claims against the source.**
   - **Candida sentence (story `text`): CONCERN.** ANF Ep. XX §3 (`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`, 30616-30628): "because she gave gifts for herself that she might not sacrifice; but she appears only to have ascended to the Tria Fata, and thence to have descended. I know, therefore, that she has not sacrificed." Hartel (`cyprian_epistulae-lat_hartel1871-csel3-tei.txt` 3168-3170): *pro se dona numerauit ne sacrificaret: sed tantum ascendisse uidetur usque ad Tria fata et inde descendisse. hanc ergo non sacrificasse ego scio.* "Given gifts so as not to sacrifice" is faithful. "So he was sure" is close to *ego scio* ("I know"). But "she seems to have turned back on the way to the sacrifice" is the ANF endnote ("It would appear that Candida therefore repented of her purpose of sacrificing, when she was actually on her way"), not the letter. It adds a purpose and a change of mind that Celerinus does not state. The sentence is also 35 words (P2-1).
   - **"Two women, Numeria and Candida"**: matches Ep. XXI §2 ("greet Numeria and Candida") and the petition of Ep. XX §3 (*Numeriae et Candidae*). PASS for the names.
   - **Story `means` "seek peace for two women ... Lucian gave it on condition that the bishop heard each case": CONCERN.** The condition matches Ep. XXI §2 ("the case being set forth before the bishop, and confession being made"), though it drops the confession. But "two women" contradicts the record's own `text` ("for her and for two other women") and Ep. XX §2, where Celerinus asks help for his sister's "so terrible a shipwreck" from the martyrs Lucian will ask. The old `means` miscounted nothing; it miscalled. The new one removes the sister, who did sacrifice. `tellable_as` has the same undercount (P1-1).
   - **Nothing voiced now tells the voice Candida did not sacrifice: CONCERN.** The caveat still lives only in `absent_detail` (unvoiced) and now `text` (unvoiced). The voice could still call her fallen from general knowledge of the lapsed. A claim guard closes F14 at its root (P1-1).
   - **Quote `means` "Lucian grants peace to Numeria and Candida ... if each case goes to the bishop and the sin is confessed openly": PASS.** The record body already says "these" are Numeria and Candida, and the Latin *hae* is feminine.
2. **Cyprian and Augustine wording.**
   - **Cyprian, "no bishop sets himself over other bishops, and each answers to God": CONCERN (softened).** The preface to the Council of 256 (ANF 56869-56882; also in Augustine, `npnf104` 13405): no one "set[s] himself up as a bishop of bishops, nor by tyrannical terror does any compel his colleague to the necessity of obedience; since every bishop ... has his own proper right of judgment, and can no more be judged by another than he himself can judge another ... let us all wait for the judgment of our Lord Jesus Christ". The new wording drops the no-compulsion clause, which the old "non-coercive" carried and which is half the formula. It also moves the judge from Christ to "God" (P1-2).
   - **Augustine, "a wider council can correct a narrower one": CONCERN (softened and cut).** On Baptism II.3.4 (`npnf104` 11300-11304): councils "held in the several districts and provinces, must yield, beyond all possibility of doubt, to the authority of plenary Councils", and "even of the plenary Councils, the earlier are often corrected by those which follow them". "Can correct" weakens "must yield, beyond all possibility of doubt". The later-corrects-earlier half, which the old "a council's judgment can be corrected" carried and which the linked `lpc.quote.earlier-councils-corrected-by-later` exists for, is gone (P1-2).
3. **Post-430 and build wording in voiced text.**
   - Removed correctly: "ancestral to the Western church before that church divided"; "egalitarian"/"hierarchical" in `cautions`, `description`, `manifestations`, the term sense and `thin_topics`. PASS for those.
   - **Gravity `name` still reads "Conciliar Authority Theory: Egalitarian vs. Hierarchical": FAIL.** Voiced in every prompt and on the citation card (P1-3).
   - **Thinness, new sentence "No site report, inscription catalogue, or excavation record appears in the sources for this world": FAIL (false).** The world holds source records for exactly these: `lpc.source.laporte-hippone-la-vraie-basilique`, `lpc.source.marec-monuments-chretiens-dhippone`, `lpc.source.stevens-kalinowski-vanderleest-bir-ftouha`, `lpc.source.ennabli-carthage-une-metropole-chretienne`, `lpc.source.cil-viii-inscriptiones-africae-latinae`, `lpc.source.lannee-epigraphique`, `lpc.source.noel-duval-notes-depigraphie-chretienne-africaine`. All are `named-not-rechecked`. The old wording ("has been verified in this build") was true; the new one states an absence that is not so. This is the fabrication the fix had to avoid (P1-4).
   - **"This build" remains in voiced fields: CONCERN.** `horizon` ("That holds for what this build has read so far"; "sources this build places in the Donatist world"), `thinness` ("so far as this build has assessed it"), `cautions` item 2 ("that this build has assessed"). F22 named "in building this account" as a live leak of exactly this (P2-2).
   - **Horizon, "This tradition is still living, but it has no single named heir ... close to how most historic Christian churches understand the work of a parish or a diocese": CONCERN.** This is the same post-430 survey as the removed sentence, and it sits beside caution 16 ("It never speaks for any church after 430"). The record body says the world's Living Tradition Status is CONFIRMED (Doc_01 SS1) and that `horizon` carries it on purpose. The schema now has `living_traditions` for exactly that. Where the confirmed status belongs is a structural call, not a wording fix (P2-3).
   - Not voiced, noted only: `thin_topics` note "Doc_01 ... Doc_04 classifies it Supporting by a decision made outside its six tests"; `thin_topics` "independently verified in this build"; record `confidence` notes and trailing bodies.
4. **Reading level and register (`engine.m1.gates.grade_text`).**
   - Story Candida sentence: 35 words, FK 13.6 / FRE 60.1. Over 25 words (P2-1).
   - Story `means`: 26 words, FK 12.7 / FRE 50.3. `tellable_as`: FK 8.5 / FRE 66.4, plain.
   - Term sense sentence: 44 words, FK 19.6 / FRE 31.4, with two nested appositives. Worse than the base (P1-2 rewrites it).
   - Caution 6: FK 7.8 / FRE 60.7, sentences 16 and 11 words. Register matches the neighbouring cautions.
   - Gravity `manifestations`: grammatical but stacked ("Cyprian's formula, that ..., in the preface ...: ..."); acceptable for a list field.
5. **YAML and mirrors.** All five records parse (`yaml.safe_load` on the front matter). `python -m engine.m10.cli records lpc`: PASS. `claims lpc`: PASS, 107 derived, 107 registered, none unverified. Every record edit has its generator mirror: s24 (story `tellable_as` and `text`), s2u (both `means`), s21 (`horizon`, `thinness`, caution 6, `thin_topics`), s22 (term sense), s25 (gravity `description`, `manifestations`). PASS.
6. **Other changes.** None outside the stated fields. The s21 HORIZON join ("It is " + "not a claim ...") reads correctly. PASS.

## Findings

P1 means wrong, unsupported, misleading, softened or hardened, or a safety gap. P2 means a plainly correct small fix.

- **P1-1 (story `use_note.means`, `tellable_as`, `claim_guards`; generators `wb_lpc_s2u_use_notes.py` STORIES and `wb_lpc_s24.py`; record `records/lpc/story/lpc.story.celerinus-writes-to-lucian.md`).** "Two women" drops the sister, contradicting the record's `text` and Ep. XX §2. Nothing voiced says Candida did not sacrifice.
  - `means`: `Celerinus asked Lucian to win peace for his sister, Numeria and Candida, and Lucian gave it if each case went to the bishop.` (23 words, FK 11.3 / FRE 54.8; the three names lift the score.)
  - `tellable_as`: `How one confessor asked another, not a bishop, to seek peace for his sister and two other women` (FK 9.1 / FRE 61.7.)
  - Add to `claim_guards`: `Celerinus says Candida did not sacrifice; the speaker must not call her fallen or say she sacrificed.`
- **P1-2 (Cyprian and Augustine wording, all locations).** The Cyprian wording drops the no-compulsion clause and moves the judge from Christ to God. The Augustine wording weakens "must yield" to "can correct" and drops "the earlier are often corrected by those which follow". Use one form throughout:
  - World_core caution 6 (record and s21 CAUTIONS): replace `Cyprian held that no bishop sets himself over other bishops, and that each answers to God. Augustine held that a wider council can correct a narrower one.` with `Cyprian held that no bishop makes himself a bishop of bishops or forces his colleagues to obey. Each bishop judges for himself, and only Christ judges him. Augustine held that a council of one province must yield to a plenary council of the whole Christian world. Even an earlier plenary council can be corrected by a later one.` (Sentences 17, 10, 19, 12 words.)
  - Gravity `description` (record and s25): replace `Cyprian held that each bishop answers to God and none sets himself over the rest.` with `Cyprian held that no bishop forces his colleagues to obey, and that only Christ judges a bishop.` Replace `Augustine held that a wider council can correct a narrower one.` with `Augustine held that a council of one province must yield to a plenary council, and that a later plenary council can correct an earlier one.`
  - Gravity `manifestations[1]` (record and s25): replace `Augustine's formula, that a wider council can correct a narrower one,` with `Augustine's formula, that lesser councils yield to plenary ones and later councils correct earlier ones,`.
  - Term `senses.informational` (record and s22): replace the sentence beginning `This is the doctrinal ground beneath both conciliar formulas` and ending `has to work within.` with `This is the doctrinal ground beneath both views of councils. It is why Cyprian can say that no bishop sets himself over the rest. It is also what Augustine's view, that lesser and earlier councils yield to plenary and later ones, has to work within.`
  - World_core `thin_topics` note (record and s21 THIN_TOPICS): replace `Cyprian's own view, that no bishop sets himself over other bishops and each answers to God, against Augustine's own view, that a wider council can correct a narrower one.` with `Cyprian's own view, that no bishop makes himself a bishop of bishops or forces his colleagues to obey, against Augustine's own view, that lesser councils yield to plenary ones and a later plenary council can correct an earlier one.`
- **P1-3 (gravity `name`; record and `wb_lpc_s25.py` line 743).** "Egalitarian vs. Hierarchical" is voiced and on the participant card. Replace `Conciliar Authority Theory: Egalitarian vs. Hierarchical` with `What Councils Can Decide: Cyprian and Augustine` (the phrase caution 6 already uses). The id stays. Doc_04 and Doc_05 keep their own heading; they are not voiced.
- **P1-4 (world_core `thinness`; record and s21 THINNESS).** The new sentence states an absence that the world's own source records contradict. Replace `No site report, inscription catalogue, or excavation record appears in the sources for this world.` with `Site reports and inscription collections for this region exist, but none has yet been read for what it shows of this world's worship.` (23 words, FK 9.3 / FRE 69.5.)
- **P2-1 (story `text`; record and s24).** The "turned back" gloss is the translator's note, and the sentence runs 35 words. Replace `Of Candida he said more: she had given gifts so as not to sacrifice, and she seems to have turned back on the way to the sacrifice, so he was sure she had not sacrificed.` with `Of Candida he said more. She had given gifts so that she would not have to sacrifice. She seems only to have gone up as far as the Tria Fata, and then come back down. So he knew she had not sacrificed.` (FK 3.1 / FRE 91.4, longest sentence 17 words.)
- **P2-2 ("this build" in voiced world_core fields; record and s21 HORIZON, THINNESS, CAUTIONS).**
  - `horizon`: `That holds for what this build has read so far, and the claim is held as Contested.` becomes `That holds for the writings read so far, and the claim is held as Contested.` Then `mostly through sources this build places in the Donatist world, not in this world's own surviving voice.` becomes `mostly through sources that belong to the Donatist world, not to this world's own surviving voice.`
  - `thinness`: `so far as this build has assessed it (Contested; nine tractatus in Morin 1917 are not yet assessed)` becomes `so far as its writings have been read (Contested; nine tractatus in Morin 1917 are not yet read)`.
  - `cautions` item 2: `this world has no surviving pastoral voice that this build has assessed.` becomes `no pastoral voice of this world survives among the writings read so far.`
- **P2-3 (world_core `horizon`, last paragraph; record and s21 HORIZON).** "Still living ... most historic Christian churches" is post-430, beside caution 16. Replace the paragraph with `Its core is an ordinary bishop's care of a local flock, in one place, through the sacraments and the gathered congregation. It is not a claim that belongs to one see's own line of succession.` Then register in `Build/worlds/lpc/Open_Gaps_Tracking.md` whether the CONFIRMED Living Tradition Status (Doc_01 SS1) moves into `world_core.living_traditions`. That placement is a methodology call for the project lead, not part of this fix.

## How the fixes answer their findings

| Finding | Closes it on the record side? | Note |
|---|---|---|
| F14 | After P1-1 | The fix landed in `text`, which is never voiced. The new `means` stops saying "fallen" but drops the sister. Only a claim guard tells the voice Candida did not sacrifice. |
| F22, "egalitarian ... hierarchical" | After P1-3 | Every body field is clean; the voiced gravity `name` is not. P1-2 restores what the replacement wording cut. |
| F22, "verified in this build" | After P1-4 and P2-2 | The rewording made the sentence false. Three other "this build" phrases stay in voiced fields. |
| F22, post-430 | After P2-3 | One sentence removed; the paragraph around it makes the same kind of claim. |

## Verdict

**Revise.** The F14 names and condition are right, the quote `means` is right, every edit is mirrored, the records parse, and `records` and `claims` pass. Four P1s remain. The story's voiced fields drop Celerinus's sister and still carry no guard on Candida (P1-1). The Cyprian and Augustine replacements cut half of each formula (P1-2). The voiced gravity `name` keeps "Egalitarian vs. Hierarchical" (P1-3). The new thinness sentence denies sources the world holds (P1-4). Apply P1-1 to P1-4 and P2-1 to P2-3 with the text above. Regenerate through s21, s22, s24, s25 and s2u, then re-run `records`, `regate` and `claims`. Round 2 should be a targeted recheck of these seven items only.

## Round 2

- Targeted recheck of the round-1 items only, against `git diff origin/main -- records/lpc Build/worlds/lpc/scripts` (commits b828d821a, 0c0e444ee). Reviewer model: Opus 5.5 (`claude-opus-5-5`), lower effort.
- No repo file was modified other than this one. No model call, engine build, branch switch, commit or push.
- P2-3 was held for the project lead as a methodology question and is not counted here.

### Per item

- **P1-1: PASS for `means` and `tellable_as`; CONCERN for the new guard.** `means` and `tellable_as` match the round-1 text in the record and in s2u / s24. The guard was applied exactly as round 1 wrote it, in the record and in s24. But its second half, "must not call her fallen", goes further than the letters. Ep. XX §3 asks that the martyrs remit *tale peccatum* ("such a great sin") to Numeria and Candida both (Hartel 3166-3167; ANF 30616-30618), and §2 speaks of "their sin" (ANF 30590). Ep. XXI §1 calls it "so great a crime committed" (ANF 30693-30694). Giving gifts so as not to sacrifice is still a fault in both letters. The guard as written could lead the voice to say Candida did nothing wrong, which neither letter says. The round-1 text was too strong; this is a correction of the reviewer's own wording, not of the build thread's application. Fix below.
- **P1-2: PASS.** Caution 6, gravity `description`, gravity `manifestations[1]`, term `senses.informational` and the `thin_topics` note match the round-1 text, each with its generator mirror (s21, s25, s22, s21). `manifestations[0]` keeps "no bishop sets himself over the rest", which round 1 did not ask to change and which is faithful to the quoted words beside it.
- **P1-3: PASS.** The record and s25 carry `What Councils Can Decide: Cyprian and Augustine`. The old name is gone from `records/`. It survives only in the dated build output `the lpc package 2026-10-27T04-46-29Z/` (`compiled/prompt.txt`, `compiled/repository.json`, the copied gravity record), which is the earlier build and changes only on rebuild. The rebuild is still required before the fix reaches the voice. The construction documents' old title is accepted, to be logged.
- **P1-4: PASS.** The `thinness` sentence matches round 1 in the record and s21. It is true: the region's site and inscription sources are named in the world's records (Laporte, Marec, Stevens et al., Ennabli, CIL VIII, L'Année épigraphique, Duval), each `named-not-rechecked`, and the basilica-archaeology row is `unverified`. None is recorded as read. So "exist, but none has yet been read" is accurate.
- **P2-1: PASS.** Story `text` matches round 1 in the record and s24, and agrees with Ep. XX §3 (*pro se dona numerauit ne sacrificaret ... usque ad Tria fata et inde descendisse ... non sacrificasse ego scio*).
- **P2-2: PASS.** The three `horizon` / `thinness` / caution 2 phrases match round 1 in the record and s21. No "this build" remains in those voiced sentences. Caution 2 keeps "are not yet assessed" for the Morin sermons; that is not build wording.

### Nothing new broken

- All five records' front matter parses (`yaml.safe_load`). The five generators compile.
- `lpc.quote.the-case-set-before-the-bishop` agrees with the story. Its `means` names Numeria and Candida and keeps the condition and the confession; its `text` and `modern_rendering` are unchanged; the story `means` and the condition guard say the same.
- The story `means` "Lucian gave it" holds: Ep. XXI §2 says the martyrs "have given peace to all", and the quote's "not only these" extends it beyond the two women.
- The trailer note now says "Two of the claim_guards entries", which matches the four guards.
- The new guard sits beside the "do not invent words" and "condition" guards with no conflict, apart from the point under P1-1.

### Fix

In `records/lpc/story/lpc.story.celerinus-writes-to-lucian.md` `claim_guards`, and its mirror in `Build/worlds/lpc/scripts/wb_lpc_s24.py`, replace

`Celerinus says Candida did not sacrifice; the speaker must not call her fallen or say she sacrificed.`

with

`Celerinus says Candida gave gifts so that she would not sacrifice, and that she did not sacrifice; the speaker must not say she sacrificed. Both letters still call the women's act a great sin, so the speaker must not say she did nothing wrong.`

### Verdict

**Revise (one item).** P1-2, P1-3, P1-4, P2-1 and P2-2 pass, and nothing else broke. P1-1 needs the one guard fix above, which corrects round 1's own over-strong wording. Round 3, if it is needed, checks only that line and its s24 mirror. After that, rebuild so the dated package stops carrying the old gravity name.

## Round 3

- Targeted recheck of the one round-2 fix only: the last `claim_guards` entry of `records/lpc/story/lpc.story.celerinus-writes-to-lucian.md` and its mirror in `Build/worlds/lpc/scripts/wb_lpc_s24.py`. Reviewer model: Opus 5.5 (`claude-opus-5-5`), lower effort. This is round 3 of 3.
- No repo file was modified other than this one. No model call, engine build, branch switch, commit or push.

### Check

- **Wording: PASS.** The record entry and the s24 string (joined) are both, character for character, the round-2 text: "Celerinus says Candida gave gifts so that she would not sacrifice, and that she did not sacrifice; the speaker must not say she sacrificed. Both letters still call the women's act a great sin, so the speaker must not say she did nothing wrong."
- **Fidelity: PASS.** Ep. XX §3 says Candida "gave gifts for herself that she might not sacrifice", went up only to the Tria Fata and came down, and "I know, therefore, that she has not sacrificed" (ANF 30622-30630). The same letter asks the martyrs to remit "such a great sin" to Numeria and Candida (ANF 30617-30618). Ep. XXI §1 speaks of "our sisters" and "so great a crime committed" (ANF 30693-30694). Both halves of the guard hold to the letters.
- **Parse and compile: PASS.** The record's front matter loads with `yaml.safe_load`, and the last guard reads back as the text above. `wb_lpc_s24.py` compiles with `py_compile`.

### Verdict

**Approved to proceed.** The round-2 fix is in place, word for word, in the record and in s24. It is faithful to Ep. XX and XXI. As round 2 noted, the dated package still needs a rebuild before these fixes reach the voice.
