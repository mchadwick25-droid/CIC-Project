Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-fable-5-1
Reviewer agent: independent Doc_10 round 1 reviewer, fresh context, high effort; read nothing of the drafting session
Drafter agent: Doc_10 drafting session, commit 8538d2a84 (its message names Fable as sole drafter; its trailer names Sonnet 5.5, the orchestrating session)
Round: 1 of 3 for Doc_10 (`roundcount lpc 10 --check-new` passed before this file was written; 0 earlier review files on record)
Truncation check, method 1: heading count and closing line. `grep -cE '^### (B|S|O)[0-9]+ '` on this file returns 21 finding headings, and `tail -n 1` returns "End of review.", both run after the last edit.
Truncation check, method 2: set comparison in Python. The finding ids in the summary table (21) equal, as a set, the ids of the `###` finding sections (21). The seven reviewed files were checked the same two ways: each file's byte count on disk equals `git cat-file -s HEAD:<path>` (Doc_10 73,529; Permanent Prompt 22,437; the four demonstrations 4,411, 4,134, 4,971 and 4,253; world_core 31,518), and each ends on a complete sentence.

# Review of Doc_10, Representative Construction Notes: Datus (`lpc`)

**Scope.** `Build/worlds/lpc/Doc_10_Representative_Construction_Notes_Datus.md`; `Build/worlds/lpc/Representative/lpc_Representative_Permanent_Prompt_Datus.txt`; `records/lpc/demonstration/` (`compel-three-phase`, `font-twice-answered`, `one-of-us-came-to-believe`, `road-back-examined`); `world_core.living_traditions` in `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md`; the compiled prompt at the package pinned at the time (its compiled prompt) where Doc_10 relies on it; the four UNVERIFIED rows Doc_10 added to `lpc_Claims_Register.md`.

**Standards read.** Build Process V2.0: the Doc_10 row, the Craft/Focus bar (a)–(e) and the surrounding rules (identity, Facilitator-only redirect, claim register, cross-document consistency), the result-label check, the voice-perspective principle. RCF V3.2 Parts Three and Eight (L3C .docx, `word/document.xml`): the four sufficiency domains, Thinness Mapping, the eight test categories, the violation indicators, Dynamic Encounter Validation. `Representative_Construction_Notes_Template.md`; `Voice_Configuration_Template.md` (dropped from the build path; read for the self-naming and register items only); the Permanent Prompt Template V2.4, Section 8 and Final Assembly 5c–5d; Naming and Role Discipline; Completion Standard V1.4; CLAUDE.md. Exemplars: `records/syr/demonstration/syr.demo.room-for-doubt.md`; the syr voice record; the previous lpc review, `Voice_Demonstrations_Review_2026-09-30.md`. Doc_01 §8; Doc_02 §6–§7; Doc_04 line 92; Doc_07 §6; the identity-options file; the Living Tradition distinguishing statement as adopted.

## Verdict

**Not approved to proceed this round.** The draft is strong. It contains no fabrication about Datus, and every quote checked against the vendored texts is faithful (table below). Both blocking findings and all eleven substantial findings of the 2026-09-30 review are closed for real, not only in words. Safety handling is correct. But eight substantial findings need wording fixes before Doc_10 clears: two misstatements in the deployed demonstrations, one closing line that models meta-commentary, a Contested date stated as settled, one absence claim that overstates its source, an overclaim and a present-day judgement in the new `living_traditions` field, an open item the document promises to carry and does not, and pass/fail language attached to authored results. None is blocking. All are wording-level, so round 2 should be a targeted recheck of these findings only.

A ninth substantial finding (S9, the two self-naming lines) is a real defect in the deployed prompt. Doc_10 handled it correctly by routing it to the project lead. It does not count against Doc_10's own revision, but it must be decided before the Self-Referential probe in Phase D.

## Gates run directly

| Check | Result |
|---|---|
| `roundcount lpc 10 --check-new` | PASS (0 review files on record before this one) |
| `prereview lpc --doc 10` | PASS on all five checks (document, m2 build 22 gates 0 failing, bar screen 13 fields 0 over FK 10, cross-world 0 new, holdings) |
| `records lpc` | PASS |
| `regate lpc` | PASS. 274 public fields, 190 new or edited; 150 below FK 8, reported and not failed |
| `gaps lpc` | PASS |
| `claims lpc` | PASS before and after this review's register edits. 114 derived, 114 registered. After this review: 1 UNVERIFIED (`e7517592`, left so on purpose, see S5) |
| `deployed lpc` | PASS at pin 2026-10-01T03-48-25Z. `living_traditions` verbatim in the prompt; no telos field to check |
| `gate_readability`, `gate_voice_perspective`, `gate_quote_verbatim`, `gate_no_build_attribution`, `gate_voice_craft_prompt_budget` (demonstration, world_core, voice_craft) | 0 findings each |
| `gate_readability_floor` (report-only) | 27 fields below FK 8, every demonstration turn among them (representative turns FK 3.6–6.2). The approved syr sample scores FK 4.3–5.5 on the same counter, so this is in line with the bar exemplar (see O2) |
| `wiring lpc` | Did not run: `ModuleNotFoundError: No module named 'anthropic'` in this container. Doc_10 records the wiring check as OUTSTANDING, which is accurate |
| `citations lpc` on the seven reviewed files | Doc_10 and the Prompt PASS. The demonstrations raise `d:wrong-type` (term, quote, gravity and story records cited in `sources[]`). The syr exemplar raises the same 28 times, so this is fleet practice, not an lpc defect (O7) |
| Seven-word overlap, demonstrations against every other record in `records/` (all worlds), the phase documents, Doc_01–Doc_09 and the Prompt | No overlap with any other world or with the Phase Five transcript. Inside lpc only named, sourced quotations (the 256 preface, Confessions I.1, VIII.7) and the Prompt's own coercion and telos sentences (O7). Six-word overlap between any two demonstrations: none |

## Quotes re-verified at source by structure marker

Every quoted or closely paraphrased line in the four demonstrations and in the Section 2 anchor table was re-read in the vendored file under its `div` or chapter heading. The drafter's claim of a script check was not relied on.

| Line as used | Vendored location and marker | Result |
|---|---|---|
| shepherd chiefly wounded in the wound of his flock; I wail with the wailing (De Lapsis §4) | ANF05 l. 43727–43729 | verbatim |
| "Such a one with his friends"; twenty or thirty; designate by name those whom you yourselves see | ANF05 `div3 id="iv.iv.x"` (Epistle X, l. 29836), l. 29940–29948 | faithful; "twenty or thirty or more" |
| your suffrage and God's judgment | ANF05 l. 32372–32373, Epistle XXXIX | verbatim |
| by the judgment of God and the favour of the people | ANF05 l. 27818, Pontius, Life 5 | verbatim |
| judging no man ... neither does any of us set himself up as a bishop of bishops | ANF05 l. 56868–56872, Seventh Council preface | verbatim; eighty-seven bishops per `lpc.ambient.council-assembly-scale` |
| sacrament of conferring baptism kept outside unity; given to no profit; returning clergy not ordained again | NPNF104 `div v.iv.iii.i`, l. 10826–10842 (On Baptism I.1.2) | faithful |
| Augustine quoting the preface as leave to differ | NPNF104 l. 11289–11295, 11623–11629, 12204–12210 | faithful ("He allows me ... to hold opinions differing from his own") |
| certain of the brethren, of whom I was one; council of 401; envoys; a law already published; fine and exile; a kind of medicinal inconvenience for hearts that cannot be softened by words | NPNF104 `div3 id="v.vi.ix"` (l. 19622), Letter 185 §§25–26 | faithful. "came back with nothing" is a little loose (O11) |
| originally my opinion was, that no one should be coerced; my own town ... fear of the imperial edicts ... would scarcely be believed; so many others mentioned to me by name | NPNF101 `div3 id="vii.1.XCIII"` (l. 37689), §17, l. 38244–38259 | faithful. "nobody would believe" sharpens "would scarcely be believed" (O11) |
| this your longing expectation is a prayer for me; the day of the public shows | NPNF106 l. 9396–9400, Sermon I | verbatim |
| all who heard rejoiced and clamored; the presbyter refused; under compulsion and constraint he yielded | Possidius (Weiskotten) l. 2133–2144, ch. VIII | verbatim |
| Give me chastity and continency, but not yet; afraid lest Thou shouldest hear me soon | NPNF101 `div3 id="vi.VIII.VII"`, quote record l. 12744–12750 | faithful to the quote record's rendering |
| left Alypius; fig-tree; How long? Why not now?; voice from a neighbouring house, "Take up and read"; returned to where Alypius sat, the volume of the apostle; as the sentence ended ... gloom of doubt vanished | NPNF101 `div3 id="vi.VIII.XII"` (l. 13075), §§28–29 | faithful |
| gave in his name; baptized with Alypius and Adeodatus | NPNF101 `div3 id="vi.IX.VI"` (l. 13672), §14 | faithful. "That spring" (O3) |
| baptized into Christ have put on Christ; Christ to be contemplated in our captive brethren; redeemed from captivity who redeemed us from death; a hundred thousand sesterces | ANF05 Epistle LIX ("To the Numidian Bishops, on the Redemption of Their Brethren from Captivity Among the Barbarians"), l. 36034–36039, 36082 | faithful |
| crucifixion, burial, resurrection ... modelled upon them, not merely in a mystical sense, but in reality; buried with Him by baptism | NPNF103 l. 21770–21800, Enchiridion ch. 53 | faithful. "not only as a figure" renders "mystical sense" acceptably |
| You have made us for yourself, and our hearts are restless until they find rest in you | NPNF101 l. 3887–3890 via the quote record's `modern_rendering` | verbatim to the rendering |

**Fabrication.** Nothing is invented about Datus: no family, age, personal history or anecdote. The role label carries the breadth, as Doc_10 §1 says. No demonstration gives a voice to 258–391, and none draws on the Donatist record.

## Summary of findings

| id | severity | where | subject |
|---|---|---|---|
| S1 | substantial | font-twice-answered | "So we stopped baptizing" makes Augustine the cause of a change that came before him |
| S2 | substantial | compel-three-phase | "Cyprian never asked the state for anything": an unsupported absence claim in the voice |
| S3 | substantial | compel-three-phase; Doc_10 §2 table | Turn 2 closes on meta-commentary, not on the source as Doc_10 says |
| S4 | substantial | Prompt l. 21; Doc_10 §3, §8 item 2 | The date and authorship of Pontius's *Life* stated as settled |
| S5 | substantial | Doc_10 §1; claim `e7517592` | "the only voice this world attests at any depth" overstates Doc_01 and contradicts Doc_02 §6 |
| S6 | substantial | `world_core.living_traditions`; Prompt l. 67; Doc_10 §6, §10 | An overclaim ("its office of bishop") and a present-day judgement ("can rightly claim") in the voice |
| S7 | substantial | Doc_10 §1, §8 | The *Dativus* conflict is said to be "carried in Section 8" and is carried nowhere |
| S8 | substantial | Doc_10 §7 | Pass/fail language attached to authored results; the rule cited from the wrong document |
| S9 | substantial, escalated | compiled prompt; voice record; Prompt l. 1, 17 | Two different sanctioned self-naming lines. The project lead decides |
| O1 | optional | Doc_10 §8 item 4; OG-65 | Ruling on the template's two "this world" instances: 5d is mis-cited |
| O2 | optional | Doc_10 §2, §7 | "inside the readability band" is not accurate for FK |
| O3 | optional | one-of-us-came-to-believe | "That spring" and the scope note's "names no feast day" |
| O4 | optional | road-back-examined | Two true details with no locus in `sources[]` |
| O5 | optional | Doc_10 §8 item 2 | Where the "about 130" figure comes from |
| O6 | optional | Doc_10 §1A | Thinness Mapping has no row for daily domestic life |
| O7 | optional | demonstrations; Doc_10 §2 | Grep-clean claim needs one qualifier; `sources[]` type practice |
| O8 | optional | all four demonstrations; Doc_10 §2 | Every first turn closes on an offer-menu question |
| O9 | optional | Prompt l. 19 | "anything before the day our own life as this office began" |
| O10 | optional | compel; font | Two meta-phrases inside turns |
| O11 | optional | compel-three-phase | Two small sharpenings of Augustine's wording |
| O12 | optional | Doc_10 §1 | The name recheck on the current corpus |

## Blocking

None.

## Substantial

### S1 font-twice-answered: "So we stopped baptizing" makes Augustine the cause

Turn 1: "Augustine, about a century and a half after that day, wrote seven books against the ruling. ... So we stopped baptizing such people again." Turn 2: "Augustine's answer became our practice." The "So" makes his book the reason the practice changed. The world's own record says otherwise. Doc_02 §7 reads the council under Gratus (c. 345–348, row 202, l. 7927–7929): asked whether one may be dipped again, all the bishops answer *Absit, absit*, "the opposite of Cyprian's own ruling". On Baptism I.1.2 describes a practice already in force ("those who return to the Church ... are not rebaptized"). Both demonstrations are compiled into the deployed prompt as exemplars, so the voice learns a false causal step. Turn 2's own sentence ("By Augustine's years we did not") is accurate and shows the fix.

**Proposed wording.** Turn 1: replace "So we stopped baptizing such people again." with "By his years we no longer baptized such people again." Turn 2: replace "Augustine's answer became our practice." with "Augustine's answer was our practice." The record body's Scope note needs no change.

### S2 compel-three-phase: "Cyprian never asked the state for anything"

This is an absolute absence claim in the voice. No cited source carries it, the claims patterns do not catch it, and it is not registered. It is also broader than the point needs. The point is that nothing in Cyprian's years corresponds to any stage of this development (the record's own Scope note). The world's records ground a narrower and stronger fact: in Cyprian's years the emperors were the persecutors (`lpc.force.decian-persecution-libelli-system`; the Valerianic persecution that ended in his death).

**Proposed wording**, turn 1, third sentence: "In Cyprian's years the emperors were the ones persecuting us."

### S3 compel-three-phase: turn 2 closes on meta-commentary

Turn 2 closes: "We hand you that in his order and in his words, and no more than that." This sentence is about the voice's own act of speaking. The Permanent Prompt's own operational test names exactly this: "a description of how you are choosing to speak with them right now ... cut it before you say it". A demonstration models that closing move for every later answer. Doc_10 §2's table also says the turn "(b) closes on the source's own reason, not a line of its own". It does not; it closes after the source. The sentence before it ("we give it to you as his reason, not as ours") already does the witness-not-recruitment work.

**Proposed wording:** delete the final sentence, so turn 2 closes on "He called the laws a kind of medicine for hearts that words could not soften." That line paraphrases Letter 185 §26 and is named in the record body. Doc_10's table claim then becomes true as written.

### S4 Pontius's *Life*: a Contested date and authorship stated as settled

Doc_02 §7 holds the *Life*'s date as Contested: 259 on Harnack's report of the prevailing view, and "the end of the third century at the earliest" on Koch, Reitzenstein and Martin, whose author "plays the eyewitness" (`den Augen- und Ohrenzeugen spielt`). It says "on either date it is a life of Cyprian ... and it does not fill the silence". It keeps the *Life* apart from the trial record and the martyr acts. `world_core` caution 2 carries the hedge correctly ("The life that bears the name of his deacon Pontius is dated to 259 or much later."). Three places flatten it:

- Prompt l. 21: "The texts written at his death stand at the start of it: the record of his trial, two martyr acts, and the life his deacon wrote of him." This states the early date and the deacon's authorship as fact.
- Doc_10 §3: "The texts written at Cyprian's death (the *Acta Cypriani*, Pontius's *Life*, the two martyr acts) stand at the start of the interval".
- Doc_10 §8 item 2: "the *Life* is held as a life of Cyprian that stands at the start of the interval on either date". On the later date it does not stand at the start. Doc_02's claim is that it does not fill the silence on either date.

**Proposed wording.** Prompt l. 21, replacing the sentence quoted: "The texts written around his death stand at the start of it: the record of his trial and two martyr acts. A life of him that bears his deacon's name stands with them. We cannot fix its year: the year after his death, or much later. On either date it tells his life, and none of these texts fills the silence." (FK 4.1, FRE 92.9.) Then delete the next sentence ("They belong to his years, and they do not fill the silence."), which this wording replaces.

Doc_10 §3: "The texts written at Cyprian's death (the *Acta Cypriani* and the two martyr acts) stand at the start of the interval and belong to his phase. Pontius's *Life* is dated 259 on the older view and to the end of the third century at the earliest on the later one (Contested; Doc_02 §7). On either date it is a life of Cyprian and does not fill the silence."

Doc_10 §8 item 2, Decision: "the *Life* is held as a life of Cyprian, which on either date does not fill the silence (Doc_02 §7)."

### S5 "the only voice this world attests at any depth" overstates its source

Doc_10 §1, *Why This Identity Was Chosen*: "a bishop is also the only voice this world attests at any depth ... (Doc_01 §8 item 3)". Doc_01 §8 item 3 says something narrower: "Both anchor voices are bishops; this world's own 'ordinary believer' subject matter is attested only through episcopal mediation." Doc_02 §6 names a deacon, Pontius, with "an extended first-person account" (row 7). It also names two lay confessors' letters in their own words (Epistles XX and XXI, row 1), and calls the skew "narrower than a blanket negative would suggest". Doc_10's own §1A table and the `world_core` thinness say the same. The sentence's real point stands: Datus can speak about the flock, not as it. This review left claim `e7517592` UNVERIFIED in the register with the check recorded. A reworded claim takes a new id.

**Proposed wording:** "The honest counterweight is recorded rather than smoothed: both anchor voices are bishops, and the ordinary believer is heard only through them (Doc_01 §8 item 3; Doc_02 §6). That makes Datus well placed to speak about the flock and structurally unable to speak as it."

### S6 `world_core.living_traditions`: an overclaim and a present-day judgement

Two sentences in the new field (compiled into the deployed prompt; the same text closes the Prompt file and is quoted in Doc_10 §10):

1. "Our churches gave rise to much of the Western church: its office of bishop, its examined road of penance, its argument over what a sacrament truly needs." The template's Version A does open "Your world gave rise to". But the appositive says the Western church got *its office of bishop* from Carthage and Hippo. A church historian would not accept that. Rome, Italy and Gaul had bishops of their own. The adopted statement says only that the Western traditions "descend in part from this material".
2. "No single church living today can rightly claim to be our one heir." "Rightly claim" judges living churches' claims, in the Representative's voice. The adopted statement's "No present-day body may be presented as the continuation" is a rule for the system, and the project lead decided the distinction is Facilitator-carried, not Representative-carried. The template asks that a participant from such a tradition "can receive [it] without feeling corrected". A Roman Catholic or Orthodox participant may well feel corrected by "rightly". The witt precedent says nothing of this kind.

Doc_10 §6 says the field "carries no divergence and no present-day judgement". Sentence 2 is a present-day judgement. The field is already provisional for the project lead's word at M2, so this proposal goes to him with it.

**Proposed wording** for the whole field (101 words, FK 7.7, FRE 69.6; the last four sentences are kept as drafted):

> Many churches living today grew in part from ours, and none from ours alone. They carried forward, in different measures, how we thought of a bishop's care for his own people, our examined road back for the fallen, and our argument over what a sacrament truly needs. What we speak from is our own life as we lived it, in Carthage and Hippo, between about 246 and 430. Our words are our own formation speaking. They are not a claim about what any living church believes or practises now. Those churches have their own voice and their own account of themselves.

Apply the same text to Prompt l. 67 in the template's address, and to Doc_10 §10's quotation. Then repin.

### S7 The *Dativus* conflict is promised to Section 8 and carried nowhere

Doc_10 §1: "One conflict stands in the record and is carried in Section 8: *Dativus* appears both as the ground for *Datus* and in the list of encumbered sententiae names." Section 8 does not carry it. Neither does `Open_Gaps_Tracking.md`: its only *Dativus* line is the M1 entry. The identity-options file §9, conflict A, says "Needs a ruling". CLAUDE.md requires every open question to be in the tracking file, never left to one document. It is an identity matter, so it belongs to the project lead.

**Proposed wording**, a new item 8 under *Calibration Judgments Made Under Uncertainty*:

> 8. **The *Dativus* conflict.** The M1 Decision Log entry grounds *Datus* on *Dativus*, and also lists *Dativus* among the names ruled out as encumbered by the 256 sententiae (identity-options file §9, conflict A). Not decided here: an identity question is the project lead's. The name stands unchanged until he rules. Evidence that would settle it: his ruling on whether *Datus* carries the encumbrance.

Add a matching numbered entry to `Open_Gaps_Tracking.md`. O12 belongs with the same entry.

### S8 Pass/fail language on authored results

Doc_10 §7 says correctly that the earlier battery's results are authored. It then reports them with pass/fail verbs: probe 4 "passed only on a retest"; probe 12 "failed on the first run ... and passed on a retest"; "probe 13 passed"; probe 14 "was scored four of four". The result-label rule is Build Process V2.0 Section 3, in the gate table, row "Result-label check": "An authored result cannot score PASS or FAIL." Doc_10 §4 attributes it to "the Completion Standard's result-label rule". The Completion Standard requires only that every result is "labeled observed or authored". (§7 cites the Build Process correctly.)

**Proposed wording.** §4, first paragraph: "Under the result-label rule (Build Process V2.0, the Result-label check) they are **authored** ...". §7 Anachronism: "probe 4's first simulated answer narrated the silence; a later simulated answer did not." §7 Claim-Laundering: "probe 12's first simulated answer left out two of the three stages; a later one, after the artifacts were fixed, carried all three; probe 13's simulated answer declined the equivalence." §7 Sustained Engagement: "deepened through G1, G2 and G3; that battery's own scorer rated it against the Article 6 conditions, a rating this process cannot count".

### S9 Two sanctioned self-naming lines in one deployed prompt (escalated)

The compiled prompt now holds two different sanctioned lines:

- the fleet pronoun rule (prompt l. 13): "One sanctioned exception, fleet-wide: 'I am a representative of Latin Pastoral-Congregational Christianity' ... Used at most once per turn";
- this world's self-reference note (prompt l. 45; voice record `flavor_notes[self-reference]`): "'I am the voice of the ordinary churches of Latin Africa - the flock kept, and the flock that keeps its own.'", once only in a conversation (the Prompt file, l. 17).

**Ruling: this is a defect, not a harmless variant.** The two instructions disagree on the words, on the form ("a representative of" against "the voice of"), and on how often (once a turn against once a conversation). The model will pick one unpredictably or say both, and the Self-Referential probe cannot be graded against a fixed pass. The world's line also breaks the register it is written for. "The flock kept, and the flock that keeps its own" is a balanced, self-composed and quotable line, the shape register statement 6 and Craft bar (b) exclude everywhere else. Doc_10 removes the same shape elsewhere in this very draft ("no door / no Master"; "Nobody's is the emptiest thing"). And "the flock that keeps its own" has no plain meaning a participant can recover. The fleet precedent is consistent: don, pahc, rzg, witt, desert and syr each carry the fleet frame with the world's own name ("I am a representative of the Church of the Martyrs."; "... of the Scattered Households."). lpc is the only world with a second form.

**What to do.** The project lead decides, because the line is part of the Representative's identity (an escalation category), and because the voice record's own review (O3) left the line to him. Recommended option, in the fleet frame, plain, with no tail. Voice record self-reference note, last sentence: "'I am a representative of the ordinary churches of Latin Africa.'" Prompt l. 17: "When someone asks you plainly what you are, you give this answer once, in these words: 'I am a representative of the ordinary churches of Latin Africa.' Then you return to speaking as 'we.' ..." (rest unchanged). Prompt l. 1, last sentence: delete "That is the flock kept by a named man who is answerable for it, and the flock that keeps its own." Then rebuild and repin. Alternatives: no world line at all, so the fleet rule governs alone; or keep the current line, accepting the conflict and the register breach. Doc_10's own handling (retain, record the alternatives, route to the project lead in §7 and §8 item 1, OG-65) is correct and needs no change. It is not counted against Doc_10's revision. It must be decided before the Phase D Self-Referential probe and Section 1A probe 4 are run, because both grade against the line.

## Optional

### O1 Ruling on the template's two "this world" instances

**Ruling: not a defect of this prompt, but Doc_10 gives the wrong reason.** Both instances ("this world's whole documented life", l. 3; "Wherever and whenever this world lived its life", l. 5) are template text with no placeholder, from the Permanent Prompt Template V2.4 l. 75–85. They are not the museum-guide backstop that check 5d protects. 5d names "Section 1's backstop paragraphs (the museum-guide worked example covering invented personal memory, self-narrated nature, narrated refusal, pronoun-defense ... and person-indexed lists)", which begin at the next paragraph. Keeping them is still right. They are instruction to the model ("You carry ..."), not words the Representative speaks, and the voice-perspective rule governs what the voice says. The Prompt file is neither deployed nor tested, and the compiled pronoun rule ("We do not call our world 'this world'") governs the deployed voice. Five other worlds' Prompt files carry the same two sentences unedited. Whether the template should say "this world" is a methodology change and the project lead's, as OG-65 already logs.

**Proposed wording**, Doc_10 §8 item 4, last sentence: "The two instances of 'this world' in the template's opening paragraphs (template l. 75–85) are kept as template text, as every other world's Prompt keeps them. They instruct the model and are not spoken. Check 5d itself protects the museum-guide paragraphs that follow. Whether the template should change is a methodology question, logged, and not a defect of this prompt." Make the same correction in OG-65.

### O2 "inside the readability band" is not accurate for FK

Doc_10 §2: "Each representative turn scores inside the readability band (FK 3.5–6.2; FRE 71–94)". §7: "the authored prose sits inside the band throughout". The band is FK 8–10 with FRE 60 or above. The turns are below the FK floor (measured FK 3.6–6.2), which the gate reports and does not fail, and which matches the approved syr sample (FK 4.3–5.5). **Proposed wording:** "Each representative turn clears the FRE floor (FRE 71–94) and sits below the FK 8 floor (FK 3.6–6.2), as the approved sample does (FK 4.3–5.5); the gate reports the floor and does not fail it."

### O3 one-of-us-came-to-believe: "That spring"

Coming straight after the garden, "That spring" reads as the same year. The garden came first and the baptism the following Easter. The Scope note says "the text names no feast day". The vendored file's editorial note to IX.6.14 does say "They were baptized at Easter", though that is the editor's, not Augustine's. **Proposed wording**, turn 1: "In time he gave in his name and was baptized, with his friend and his son beside him." Scope note: "Book IX, chapter VI ... the turn names no season, since only the editor's note gives one."

### O4 road-back-examined: two true details with no locus

"Two easier roads were on offer in Carthage itself": the records place the Novatianist consecration at Rome (`lpc.source.cyprian-epistles`). The vendored ANF05 does say Novatian's party made Maximus "their false bishop in that place" (l. 34778–34780), so the sentence is true but has no locus in `sources[]`. "they stood at the church door" is Cyprian's own image ("present themselves at the threshold of the church", ANF05 l. 31759–31760). **Proposed action:** add both loci to the Epistles entry in `sources[]`.

### O5 Where the "about 130" figure comes from

Doc_10 §8 item 2 says both figures are Doc_02 §7's own. That is true. But Doc_02's "roughly 130" belongs to the strict reading, from the end of Cyprian's phase. The voice record attaches it to "Between Cyprian's death and Augustine's ordination", which counts 133. "About 130" is a fair rounding of 133, so the voice record need not change. **Proposed wording**, item 2: "The voice record's identity field says 'about 130 years' for 258 to 391. That rounds 133; Doc_02 §7's own 'roughly 130' is its strict reading from the end of Cyprian's phase. Either way the figure is consistent, and the voice record was not reopened."

### O6 Thinness Mapping has no row for daily domestic life

RCF Part Three lists "daily domestic practices" among typical thin domains. Doc_10 §7 uses "an ordinary household's week" as a fabrication press, but §1A has no row for it. **Proposed row:** "Daily and household life | Thin | Doc_02 §6: no lay source on ordinary congregational life as such | `lpc.limit.ordinary-interior-life`; `lpc.core...` thinness".

### O7 Grep-clean claim and `sources[]` practice

Doc_10 §2 says no seven-word run is shared with another record "except a named, sourced quotation". That holds against the record store. The C-P demonstration's second turn also shares 17 seven-word runs with the Prompt's telos paragraph, and the compel demonstration 9 with the Prompt's coercion paragraph. Both were authored together under this document, and the Prompt file is not compiled, so nothing is doubled in the deployed prompt. **Proposed wording:** add "The C-P and compel demonstrations share wording with the Prompt file's telos and coercion paragraphs, written together; the Prompt file is not compiled." Separately, `citations` flags term, quote and story records in demonstration `sources[]`. The syr exemplar does the same, so this is a fleet question, not one for this world.

### O8 Every first turn closes on an offer-menu question

"Which of the three steps do you want to press on?"; "Would you like the first answer argued, or the second?"; "Which part of that do you want to stay with?"; "Is it the waiting you are asking about, or the door?" The syr sample also hands the turn back, so a question is sanctioned. But three of the four are menus, and "Would you like ...?" is service-desk cadence, an AI tell under CLAUDE.md. Doc_10's "no shared closing move" is accurate for the second turns only. **Proposed wording**, font turn 1: "Which of the two answers would you argue for?" Doc_10 §2: "no shared closing move among the second turns; each first turn hands the question back, as the approved sample does."

### O9 Prompt l. 19: "anything before the day our own life as this office began"

As written, this puts Scripture, the apostles and the martyrs before 246 outside what the voice may speak of. But Augustine preached on Perpetua and Felicitas (Sermons 280–281, row 122, Native). The template says only "anything after this world's own documented close". **Proposed wording:** "What is not yours is anything after 430."

### O10 Two meta-phrases inside turns

Compel turn 1: "We can tell you how it came about, in order." Font turn 2: "Our practice changed, and we say so plainly." Each speaks about the voice's own telling. **Proposed wording:** compel, delete the sentence (the next sentence already puts it in order). Font, "Our practice changed."

### O11 compel-three-phase: two small sharpenings

"The envoys came back with nothing" suggests a refusal. Letter 185 says the law already published "left our deputation nothing to do". "nobody would believe it had once shared it" sharpens "would scarcely be believed". **Proposed wording:** "The envoys came back without it." and "that you would hardly believe it had once shared it."

### O12 The name recheck on the current corpus

The decision record's "zero times across the 38 vendored corpus files" was true of the files then checked. Across today's `cic/texts`, *Datus* occurs as a name twice over. (1) It is a cognomen in Gsell's inscriptions of Proconsular Africa (l. 110230 ff., index l. 116492), which strengthens the attestation. (2) It is Baronius's variant reading for "Dantus", one of the Abitinian martyrs of 304, in the apparatus of the Donatist *monumenta* (`monumenta-vetera-donatistarum-303-340_migne-pl8.txt` l. 2506, 2622). The second is a minor figure in a variant reading. It does not fail Naming Discipline test 1 (a major figure), but Doc_10 §1's "collides with no figure ... of the neighbouring Donatist world" is too strong today. **Proposed wording:** "The decision record states that *Datus* occurs zero times across the 38 vendored files then checked. A recheck on 2026-10-01 finds it as an African cognomen in Gsell's inscriptions, and once as a variant reading for one of the Abitinian martyrs in the Donatist *monumenta*; neither is a major figure." Carry it with S7's entry for the project lead.

## Closure of the 2026-09-30 review's findings

| id | Closed? | Evidence in the current files |
|---|---|---|
| B1 | Yes | Participant turn 1 is `_fleet.canon.f3-p-02` verbatim; turn 1 answers it in its first sentence ("We did, in our later years") |
| B2 | Yes | The settling sentence is gone. The hedge is audible in the contested record's own two alternatives ("a real change of mind, or the way he told his own story afterwards") and in "by his own later account" |
| S1 | Yes | Council of 401, the emperors, envoys, a law already published with fines and exile (Letter 185 §§25–26). Nit at O11 |
| S2 | Yes | "We hold both" is gone; the practice change and the clergy not ordained again are stated. S1 of this review is a new, different defect |
| S3 | Yes | No cryptic font metaphor, no fleet-stock phrasing (no cross-world overlap), no builder closing line |
| S4 | Yes | Epistle X read as Cyprian's plea to the confessors to name each person; past tense; Cyprian's years |
| S5 | Yes | Coined lines and the capital-M "Master" gone; no seven-word run shared with the Phase Five transcript |
| S6 | Yes for the second turns (O8 for the first) | Second turns close on the practice, a source paraphrase (after S3's deletion), Cyprian's words, and Augustine's words |
| S7 | Yes | `lpc.demo.one-of-us-came-to-believe` answers c-p-01 and then c-p-02 in their first sentences, and tells Confessions VIII as a scene |
| S8 | Yes | "one of our bishops first held ... his colleagues laid before him" |
| S9 | Yes | "that we can date and place" in the guard and identity; the pseudo-Cyprianic class named |
| S10 | Yes | One figure per fact across the voice record, the Prompt and the demonstrations |
| S11 | Yes | Locus "Epistle X in the vendored ANF numbering (div iv.iv.x)"; "begs the martyrs to name" |

## Questions the caller asked, answered

1. **Fabrication and quotes.** No invention about Datus. Every quote re-verified at its structure marker (table above). Defects are wording-level (S1, S2, O3, O11).
2. **Silence scope and interval figures.** The scope matches Doc_02 §7 word for word. "About a century and a half" for 256 to c. 400, "about 133 years" for 258 to 391, and "about 130" in the voice record are consistent with Doc_02 §7 and the records (O5 on the rationale). The one defect is the Pontius date (S4).
3. **Demonstrations against the bar.** (a) passes: the Center-Personal answer comes in the first sentence, with no composite-voice framing. (b) passes after S3. (c) passes: no six-word run repeats across demonstrations. (d) passes: the coercion hedge is audible in the record's own terms. (e) passes: Confessions VIII, Epistle X, the 256 council and Letter XCIII's town are told as scenes. B1, B2 and S1–S11 are closed for real (table above).
4. **Permanent Prompt.** World-specific prose is in "we/our" throughout. The two template "this world" instances are acceptable but mis-justified (O1). The self-naming lines are a defect for the project lead (S9). Safety: the Representative never handles distress; the guard is in Datus's idiom ("is somebody's ... as we would hear one at our door") and points nowhere outside; no redirect is conditional on the participant saying they are fine; Doc_10 §7 assigns the redirect to the Facilitator and gives the world-specific caution against a "prove yourself first" redirect. Nothing to fix.
5. **Ecology Assessment and Encounter Ecology.** Honest and calibrated. All four domains are assessed, thinness is mapped in both directions, and the probes are named for Phase D (O6 adds one row). Section 9 is short and faithful to Phase Seven. The authored test exchanges are labelled authored and carry no PASS or FAIL; S8 corrects §7's language around the earlier battery.
6. **`living_traditions`.** In-voice, first person plural, and on the witt pattern. It carries no divergence and nothing of coercion, in line with the Article 28/29 handling. But one sentence makes a present-day judgement and one appositive overclaims (S6).
7. **The four UNVERIFIED rows.** `a609c538` set to JUDGEMENT, Inferential-Thin (accurately reports Doc_04 line 92). `f2a0dc4c` set to JUDGEMENT, Widely Accepted (Doc_02 §7's own sentence). `016b10a0` set to VERIFIED, Documented (identity-options file l. 52 and 57). `e7517592` checked and does not hold as worded; left UNVERIFIED with the check recorded (S5). `claims lpc` passes after the edits.

## Round record

This is round 1 of 3 for Doc_10. Round 2, if needed, should be a targeted recheck of S1–S8 and of any optional findings the drafter applies, against this file, at lower effort. S9 waits on the project lead's decision and is not a round-2 condition for Doc_10. The verdict above is not "no substantial finding"; Doc_10 is not approved to proceed on this round.

End of review.
