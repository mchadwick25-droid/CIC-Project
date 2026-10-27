# Opus recheck of the corrected honest limits — 2026-10-27

Independent second reader, run after the corrections to the findings in `opus-honest-limits-review.md`. Read-only; its findings R1 to R8 are applied on the branch that carries this file.

## Recheck of the honest-limit corrections (F1 to F14), 2026-10-27

I edited nothing, made no model calls and did not open canon/sealed_probes. I checked every cited quote and line number against cic/texts/ and confirmed them, apart from the small locus slips listed below. Every source_id and nearest_material id exists. All six statements pass `engine/m7/turn_readability.score_turn` with no failures. They score FK 3.3 to 6.6 and FRE 71 to 89, so all sit under the grade-8 floor that CLAUDE.md treats as a warning, not a failure.

### 1. Verdicts

| Record | Verdict |
|---|---|
| don.limit.fate-of-those-who-end-their-own-lives | Needs named changes (R1, R2) |
| alx.limit.faith-alone-later-frame and alx.source.origen-comm-romans | Needs named changes (R3, R4) |
| pahc.limit.assurance-and-the-dead | Needs named changes (R5, R6, R7) |
| pahc.limit.faith-alone-later-frame | Ready to mark reviewed (nits only) |
| pahc.quote.appointed-to-be-read (analytic) and its two partners | Fixed. It is analytic, so there is no use_note to mark |
| syr.limit.what-must-one-do | Ready to mark reviewed |
| desert.limit.origins-no-single-founder and desert.source.jerome-life-of-paulus | Ready to mark reviewed |

### 2. Status of each F-finding

- **F1 (don): fixed, but the fix brings a new problem (R1).** The absence claim is now scoped ("In the words of ours that I know"). why_sources names Contra Gaudentium, and the line numbers check out: 73262, 73276-73278 ("se ipsum in ecclesia... incendere minaretur") and 75702 (Razias). OG-52 is added.
- **F2 (alx): fixed.** Stromateis is gone from the sources, and why_sources reads I.9 correctly as faith without learning (anf02:28313-28315).
- **F3 (alx): fixed.** Paedagogus I.6 is cited and verified (anf02:19364-19366). The assurance absence claim is gone, and why_sources now says assurance was not searched.
- **F4 (pahc assurance): fixed, but new problems (R5, R6, R7).** These passages are now cited and verified, and they balance the record:
  - 1 Clement 50 (anf01:2124-2127)
  - Polycarp, Philippians 9 (3489-3492)
  - Trallians 9, shorter recension (6618-6623)
  - Polycrates (anf08:72582-72585)
  - Justin, Dialogue 80, with the "blaspheme the God of Abraham" charge (22125-22130)
  - 1 Clement 5 (687, 704), in why_sources
  The old first not_for line is replaced.
- **F5 (desert): fixed.** Jerome's "this opinion has my approval also", "going back too far" and "necessary stimulus" are all in place (npnf206:29742-29753).
- **F6 (pahc faith alone): fixed.** "All men" is restored (anf01:1532-1533). The Ephesians reference is marked (3256). The "no list" overclaim is gone. The Irenaeus contradiction is resolved.
- **F7 (shared voice): partly fixed.** The unprompted assurance ending is gone from alx and syr, and the "came after us" opening is gone. What is left:
  - **pahc assurance** still has an assurance ending (R6). Its opening, "Our writers did not put it in those words", echoes pahc faith alone's "We did not use the words" in the same world, heard by the same participant.
  - **alx and pahc faith alone** now both close on "the later quarrel/argument came after us" (nit).
  - **"You ask..."** opens 15 honest-limit statements fleet-wide. That predates this batch, so I note it only.
- **F8: fixed.**
  - The quote is `voice: analytic`, with no use_note.
  - The text is verbatim at npnf204:68817.
  - Both partner records (pahc.term.two-ways:36 and pahc.force.selective-canonization:82) still point back to the quote.
  - `voiced_records()` (engine/m1/loader.py:120) keeps the quote out of compiled/.
- **F10 (syr): fixed.**
  - years is now 337-345.
  - The ending now reads "Aphrahat leaves the reckoning to the judge", which XXII.18 supports (npnf213:28368-28372).
  - I.3 (24619-24622) and I.4 (24649-24653) are verified, and VII.2 is verified in Hallock, line 39.
- **F11 (desert): fixed.** not_for line 4 is narrowed. desert.dw.apostolic is flagged as OG-42 in commit ba962ccd. Piamun's "unbroken... up to the time of Abbot Paul and Antony" is at npnf211:42537-42539.
- **F12 (alx): fixed.** Rufinus is named in the spoken text. Rufinus lies inside the alx window (150-400), so this is not a horizon problem. The Latin is verified at 13333, 13338 and 13411-13414.
- **F13 (alx): partly fixed.** "To know God" is gone, and the passage is said to be addressed to the rich. But the statement, locus and why_sources still turn it into "no one is saved" (R3).
- **F14: the parts named in the review are fixed.** The 367 body narration and the wrong line number are fixed. don's "I will not..." lines are reworded. don's first-person why_sources stays as it was, which is harmless.

### 3. Findings

**R1. Blocking (safety-adjacent): don's statement now tells the visitor about unread letters on "a death chosen under pressure".** `don.limit...:29-31`: "There are letters of ours, kept inside an enemy's book, that I have not read for this answer. They may speak of a death chosen under pressure. I cannot tell you what they hold."
- This record fires on suicide questions. These lines point the listener at Gaudentius's threat to burn himself, which OG-52 itself says must not be voiced.
- "Not read for this answer" is the builder's own process note spoken by the Representative. It is an AI tell, and it is odd in-world: the Representative says he has not read his own bishop's letters.
- The honest scoping is already carried by "In the words of ours that I know", by not_for line 2 and by why_sources. The spoken pointer adds risk and adds no fidelity.

**R2. Should fix (safety): don names a method for no purpose.** At `:28` the statement says "men who threw themselves from cliffs". This is Optatus III.4, line 2014. The precedent review accepted it. Still, safe-messaging practice avoids naming a method, and the record's point (a quarrel about who counts as a martyr) does not need it.

Corrected don statement (fixes R1 and R2):
> What do we teach about a person who ends their own life? I cannot give you an answer of ours. In the words of ours that I know, there is no teaching on it. The nearest line is Petilian's. He says that the traitor Judas perished by the rope. That is a charge made in a quarrel about traitors. It is not a teaching about the dead. Our enemies charged some of us with seeking death to be counted as martyrs. That was a quarrel over who may be called a martyr. No verdict on any person's death is mine to give. No condition on one is mine to set.

**R3. Should fix: the alx statement opens with an overclaim and still universalizes Quis Dives 27.**
- **The opening.** `:27` opens "Our teachers did not set faith against works." Three lines later, Origen's Latin says the thief was justified "sine operibus sola fide". means and why_sources limit the claim to "as a contest" in "the texts read", but the statement drops both limits.
- **The rich.** `:28-29` says "warned the rich that no one is saved merely by trusting". The source (anf02:56878-56880) is about the rich man: "neither does one perish... by fearing because he is rich, nor is by any means saved by trusting". It is reassurance as much as warning.

Corrected statement, lines 27-29:
> Our teachers spoke of both faith and works. Clement wrote that those who have believed already have life, and that nothing is wanting to faith. He also told the rich that their wealth does not doom them, and that trusting they will be saved does not save them. They must love God and their neighbour and do the Father's will.

The rest stays as it is. Lines 30-33 are verified.
- Locus at `:21`: "addressed to the prosperous; the rich man is not saved by trusting and believing that he shall be saved (lines 56877-56880); love God, love the neighbour, do the Father's will (XXVII-XXIX, 56884-56941)".
- why_sources at `:34`: replace "says no one is saved merely by trusting" with "says the rich man is not saved merely by trusting".

**R4. Nit: the Origen locus range is off by one.** The alx locus `:24` gives 13331-13337, but "pro hac sola fide" is at 13338. The source record body gives 13333-13339. Use "13333-13338 and 13410-13414".

**R5. Should fix (fidelity): pahc assurance says "Justin met some".** `:39`. Dialogue 80 (anf01:22124-22125) is conditional and addressed to Trypho: "if *you* have fallen in with some who are called Christians". Justin does not say he met them. The first review's own suggested text brought in this error, and the correction copied it. Corrected:
> Justin warned Trypho about some who were called Christians.

**R6. Should fix (F7, and an absence claim with no search behind it): pahc assurance keeps the assurance ending.** `:42`: "How sure a living person may be of their own place, we have no teaching to give."
- None of the search terms in why_sources covers assurance: heaven, eternal life, resurrection, afterlife, rise again.
- Polycarp 9, which the record itself cites, says "in the assurance that all these have not run in vain" (anf01:3489).
- For a grieving visitor the line adds nothing and invites a self-verdict.

The fix: delete the sentence. In why_sources `:44`, change the end to: "It cannot say in full what any of them taught about the state of the dead before the rising. Assurance for a living person was not searched."

The record still shares the F7 frame. At `:33-34`, replace "Our writers did not put it in those words, but they did speak of the dead." with:
> Our writers spoke of the faithful dead in two ways.

**R7. Should fix: pahc assurance means line.** `:52`. "Now have their place with the Lord" merges 1 Clement ("a place among the godly") with Polycarp ("presence of the Lord"). "A rising on the Lord's day" can be heard as Sunday, because "the Lord's day" is Sunday in this very world (Didache 14). Corrected:
> The record's writers say that those made perfect in love now have a place among the godly and that the apostles and martyrs are with the Lord, and they hope for a rising when the Lord comes, with no full account of the time between.

**Safety read of pahc assurance, every sentence and every not_for line.** After R5 to R7:
- Nothing gives a verdict on a person or advises someone in distress.
- Nothing denies that the faithful dead are with the Lord. Clement 50 and Polycarp 9 lead.
- Nothing promises a destination. not_for line 3 bars any claim about where a named person went.
- Justin's rejection is framed by his own charge.
- There is no crisis wording.

The closing "We will not name anyone's end for you" is a nit: it reads as a rule spoken aloud. A sourced alternative from 1 Clement 50 ("Who is fit to be found in it, except such as God has vouchsafed to render so?", anf01:2120-2121) would be:
> Who is found among them, our writers leave to God.

Either version is acceptable.

**R8. Nits.**
- pahc faith alone `:27`: "Here is what our writers did say" is assistant-style signposting. Suggest "Our writers said this."
- syr `:24`: "Our sage" uses a later epithet. The 510 colophon is the source of "the Persian Sage" (`syr.source.aphrahat-select-demonstrations:16`). Plain "Aphrahat" is safer.
- syr `:30-31`: "in what we have" is wider than what was searched. why_sources lists the Odes of Solomon and Ephrem's prose refutations as not searched. Suggest "in the writings I can speak from".
- The 367 quote's body (`:59-64`) still carries a verification note ("Text is verified verbatim..."). That borders on process narration in a canonical file.
- pahc.term.two-ways and pahc.force.selective-canonization keep `associated-with` links to a record that is now left out of compiled/. Runtime ignores this: grounding_net.py:1663-1675 walks only tension-with and disputed-by links and skips targets that are missing. It is harmless, but this is the only analytic record in the fleet, so the pattern is new.
- alx source body `:29-30`: "The only passages used so far..." is build narration.

### 4. What I could not verify

- Whether "sola fide" is Origen's own word or Rufinus's. The Greek is not vendored.
- What Gaudentius's own letters say, and Augustine's Letter 185.
- Ephrem's prose refutations and the Odes of Solomon, for syr. The Historia Monachorum, for desert.
- The m1 and m9 gates, including the question-ending gate. I scored readability with score_turn only.
- Whether "believe in Him" in Trallians 9 means Christ or the Father. The statement reads it as Christ. The English is ambiguous, and I treated that reading as acceptable.
- The contents of pahc.contested.ignatius-dating and first-clement-dating, beyond confirming that both records exist.
