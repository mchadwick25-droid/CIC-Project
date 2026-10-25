# Decision 8B Quotes Review: lpc, 2026-10-25

**Scope.** Commits `04dc52f0` and `10a9b220` on `claude/lpc-next-2026-10-25` (`git diff 6dbd7b7c HEAD -- records/lpc Build/worlds/lpc/scripts`):
- the 29 new quote records in `records/lpc/quote/`;
- the host edits in 7 stories, 3 gravities, 5 forces and 1 term, plus the three relation-only edits on existing quote records;
- the rewrite of the description of `lpc.force.congregational-acclamation-overriding-preference`.

**Reviewer.** Opus 5.5. This is the separate Opus check on modern renderings that Decision 8B requires.

**Method.**
- Each `text` was compared word for word with the vendored file at the cited lines. Editor's notes, scripture-reference notes and page-break tags were stripped first.
- Each cited range was checked at both ends. The check asked whether the first and last words of the passage fall on the first and last cited lines.
- Each `modern_rendering` was read clause by clause against its text field. Where a `divergence_note` names Latin, the rendering was also read against Hartel, Petschenig or Weiskotten. The four Acta renderings were read against Knopf/Krueger and Gebhardt.
- Each host edit was read against its source and against the quote record it now points to.
- No model API was called. Readability was scored locally with `engine.m1.gates.grade_text`.

## Per-record table

"Text verified" means the wording is word for word. Locus problems are noted separately and appear as findings F1 and F6.

| Record | Text verified | Rendering verdict | Notes |
|---|---|---|---|
| a-dreadful-plague-broke-out | Y | Pass | suos/exponere choice confirmed in Hartel 40787. Latin range starts one line late: "erupit postmodum" is on 40782 (F1). |
| a-hundred-thousand-sesterces | Y | Pass | Hartel 10888-10896 confirmed. Two editor's notes stripped. |
| a-standard-bearer-of-the-sect | Y | Pass | Hartel 41312-41317 confirmed. The lens note's three "turned charges" match Pontius 41320-41323. |
| because-i-am-already-weary | Y | Pass | Follows the ANF "already weary". Hartel reads *tam lassus*, "so tired"; not misleading. |
| boast-in-nothing-since-nothing-is-our-own | Y | Pass | The added "says" is disclosed. Augustine's citations confirmed at npnf105 18089, 20912 and elsewhere. English range ends on 53433, not 53432 (F1). |
| chosen-while-still-a-neophyte | Y | Pass | sacerdotium, nouellus and generosa indoles confirmed in Hartel 40550-40562. |
| christ-redeemed-in-our-captive-brethren | Y | Pass | Hartel 10842-10851 confirmed. Every clause is kept. |
| earlier-councils-corrected-by-later | Y | Pass | Petschenig 10209-10247 confirmed: *per concilia*, *experimento rerum*, *reprehendi*, *caritate*. NPNF locus "line 11303" is wrong: the passage runs 11301-11304 (F1). |
| good-done-to-all-not-only-the-household | Y | Pass | Hartel confirmed. Latin starts on 40854, not 40855 (F1). |
| grief-and-not-without-tears | Y | Pass | *cum maximo gemitu* rendered "great grief"; acceptable. English range ends on 36012, not 36011 (F1). |
| grieve-with-me-for-my-sister | Y | Pass | *in morte sororis meae* and *exacerbauit* confirmed (Hartel 3119-3124). The translator's sense is kept and disclosed. |
| he-covered-his-eyes-with-his-own-hand | Y (Knopf 4923-4927) | Pass | Close to the Latin. *cum ... non potuisset* split into two sentences; *lacinias manuales* rendered "strips of cloth". |
| he-slept-with-his-fathers | **N** | Pass | The text field inserts "..." where the source has none (F2). Latin range 4940-4942 leaves out "Membris omnibus sui corporis" on 4899 (F1). |
| it-becomes-us-to-answer-to-our-birth | Y | Pass | Hartel *non suis tantum* and the apparatus *sed etiam alienis add. v* confirmed, so the note is correct. Latin starts on 40837 (F1). |
| let-us-too-be-beheaded-with-him | Y (Gebhardt 6628-6631) | Pass | *dicebat* rendered "kept saying"; *tumultus fratrum exortus est* and *prosecuta est* exact. |
| numidicus-remained-unwillingly | Y | Pass | *remansit inuitus* in Hartel, with *inuictus Bv* in the apparatus, confirmed. *dignatione diuina* confirmed. Every clause is kept. |
| o-blessed-people-of-the-church | Y | Pass | *sacerdotis*, *tractante* and *legationis litteras* confirmed (Hartel 41359-41367). *quicumque* rendered "some ... each of them"; acceptable. |
| shut-up-in-two-cells | Y | Pass | *partim ... quam uniuersis quod censuimus* supports "partly ... partly". English starts at "You" on 30702, not 30703 (F1). |
| such-a-one-with-his-friends | Y | Pass | *cum suis*, *propinqui et adfines et liberti ac domestici* and *paenitentiam* confirmed. English range ends on 29949, not 29948 (F1). |
| thanks-be-to-god | Y (Knopf 4910-4911) | Pass | *placet* rendered "it is decided"; exact. The spelling note on *animadverti* is correct. |
| the-case-set-before-the-bishop | Y | Pass, with P2 | *cum Dominus coeperit*, *exomologesi*, *tractatum*, *hae* and *quas* confirmed. "As is done here" is attached to the request, not to the procedure (F12). |
| the-paper-itself | Y | Pass | *scriptura*, *sensus* and *clericae* confirmed (Hartel 1229-1236). |
| the-people-kept-watch-at-the-door | Y | Pass | Latin range is shifted by one line: *receptum* is on 41246 and the passage ends on 41250 (F1, F6). |
| the-psalms-hung-upon-the-wall | Y | Pass, with P2 | "Shortest" follows Weiskotten, but *paucissimi* means "very few" (F7). Latin range 4887-4911 runs past the Latin into apparatus and English. The Latin ends on 4899 (F6). |
| the-trees-and-the-trembling-executioner | Y | Pass | Hartel's *conuallis scripsi ... aequalis v* is confirmed, and the note is correct. Latin range ends on 41359, not 41360; 41360 is the next passage (F6). |
| the-whole-people-of-the-brethren-came | Y (Knopf 4877-4881) | Pass | Exact to the Latin. *omnes* is correctly "all of them". |
| thirteen-letters-sent-to-rome | Y | **Revise** | The rendering adds a clause (F3). |
| thousands-of-certificates-daily | Y | Pass | *nefandis libellis* and *libellorum milia* confirmed, so the lens note is right. Latin range 2992-2998 ends in the apparatus. The passage runs 2992-3012 (F1). |
| walled-in-by-a-mingled-multitude | Y | Pass | *princeps* wordplay confirmed (Hartel 41268). The lens note's "Christians and pagans" rests on Pontius 15, *gentilibus et dolendum*. |

**Attribution.** All 29 are correct:
- Pontius and Possidius are never credited with Cyprian's or Augustine's words.
- Lucian and Celerinus are credited with their own letters.
- The Acta string matches the fleet's convention for works with no named author.
- Scripture inside a quotation is guarded in every case where it occurs.

**Relations.** Every host edit carries a relation to its quote record. Three host sentences were turned from quotation into paraphrase with no quote record behind them (F11).

## Findings

| # | Grade | Record(s) | Finding | Fix |
|---|---|---|---|---|
| F1 | P1 | 12 records | **Some cited line ranges leave out part of the quoted passage**, although each record claims verified-direct. **English:** boast 53424-53433; grief 36009-36012; shut-up 30702-30711; such-a-one 29936-29949; earlier-councils 11301-11304 (also align the body note). **Latin:** thousands 2992-3012; he-slept 4899 and 4940-4942; plague 40782-40791; good-done 40854-40895; it-becomes-us 40837-40843; people-kept-watch 41246-41250. | Correct the loci in the records and in `wb_lpc_s24.py`. |
| F2 | P1 | he-slept-with-his-fathers | The `text` field is not word for word. It inserts "..." where the source has no gap, only a facing Latin page. An ellipsis tells the reader something was left out, and here nothing was. | Remove the ellipsis. Keep the page-break explanation in the body and locus only. |
| F3 | P1 | thirteen-letters-sent-to-rome | The rendering adds meaning. "They did what they could with the Lord's help..." makes the letters the ones doing the striving and repeats the measure. In the source, the measure is Cyprian's own abilities, *Domino suggerente*. | For example: "Nothing was lacking in them, as far as my poor abilities could strive, with the Lord's help, under the law of faith and the fear of God." Then list the four items. |
| F4 | P1 | lpc.story.the-plague-and-the-enemies | The host paraphrase adds a cause. "So many that they were no longer bodies but corpses" is not in Pontius. His contrast is that the dead lay unburied as carcasses, not that there were many of them. | For example: "bodies left where they fell, no longer bodies but the corpses of many." |
| F5 | P1 | lpc.story.the-death-of-cyprian | The host paraphrase misattaches the blood. "An example to his own people, whose blood would begin to make discipline firm" reads as the people's blood. The source says Cyprian's: "with his blood discipline would begin to be established". | For example: "...an example to his own people, and said that with his blood discipline would begin to be made firm." |
| F6 | P2 | trees, psalms, people-kept-watch | Some Latin ranges run past the passage. The trees range should end on 41359. The psalms range should be 4887-4899. The people-kept-watch end is covered in F1. | Correct the loci. |
| F7 | P2 | the-psalms-hung-upon-the-wall | "The shortest penitential Psalms" follows Weiskotten. But *qui sunt paucissimi de poenitentia* means "the very few psalms of penitence", and there is no `divergence_note`. | Follow the Latin ("the few penitential psalms") with a divergence note, or keep "shortest" and add the note. |
| F8 | P2 | lpc.story.the-death-of-cyprian | "Cyprian had the young women guarded, since they had all stayed in the street" now reads as if the women were the ones who stayed. In the Latin, *omnes* means the whole people. | "...since the whole people had stayed in the street..." |
| F9 | P2 | acclamation force (rewrite) | "He gave way under pressure" understates Possidius's "under compulsion and constraint" (*compulsus atque coactus*). This is the force's own key evidence. | "...he was compelled and gave way." |
| F10 | P2 | acclamation force (rewrite) | Two small changes from the source. "Two or three years later" drops the earlier "roughly". "A rival group held an old hatred against him" loses "against my episcopate, that is, against your suffrage and God's judgment", the link the force rests on. **Checked and correct:** "Valerius, the bishop of Hippo" (Possidius IV, "the holy Valerius was bishop in the Catholic church at Hippo"; VIII, *Valerio antistite*); the audience; the gladness and clamour; the refusal while his bishop lived; the examples from overseas and Africa; Pontius's neophyte; "your suffrage and God's judgment" (Ep. XXXIX). Scored with `grade_text`: FK 7.2, FRE 66. | Restore "about two or three years". Say the old hatred was aimed at his election, which was the people's choice and God's judgment. |
| F11 | P2 | death story; transmission force; conciliar gravity; Celerinus story; acclamation and transmission manifestations | **Leftover or record-less quotations.** The conciliar gravity still quotes "a bishop of bishops." with no relation to `lpc.quote.bishop-of-bishops`. The Celerinus `absent_detail` still quotes "that she might not sacrifice". The `manifestations` of the acclamation and transmission forces still carry quotations. Three sentences became paraphrase with no quote record behind them: Acta 2.1 ("a large crowd gathered at Sextus's place") and the two Retractationes phrases. The Retractationes phrases have no vendored English, so a paraphrase is right there. | Decide the manifestations and `absent_detail` scope. Add the conciliar relation. Extract the Celerinus quotation, or log it in Open_Gaps_Tracking. |
| F12 | P2 | the-case-set-before-the-bishop | "I make this request, as is done here" attaches *sicut hic* to the request. It belongs to the procedure and the grant of peace. | For example: "I ask, brother, that as is done here, when the Lord has begun..." |
| F13 | P2 | acclamation force | **Governance.** The Decision 8B ruling of 2026-09-25 (System Hub Decision Log) says a readability rewrite "is a separate task with its own review and never part of the same PR". The rewrite is a separate commit on the same branch. This review covers its facts. | Open it as its own PR, unless Mark has ruled the exception. |

**Checked and found correct (host edits).**
- Collegial and conciliar gravities.
- Grace gravity.
- Celerinus story: grief, prison and grant sentences.
- Election story.
- Sesterces story.
- Numidicus story.
- Psalms story.
- The certificates term.
- Augustine-engagement, confessors, Decian and transmission forces (Cyprian sentences).

Each edit stays inside its quote's own sentence, says no more and no less than the source, and carries its relation. The acclamation description is the stated exception.

## Verdict

**Revise.**

Five P1 findings (F1-F5). Each is a narrow fix:
- correct the loci;
- remove the ellipsis;
- re-render one clause of one rendering;
- re-word two host sentences.

The 28 other renderings meet the rendering bar. No rendering exceeds about 25 words in a sentence. A targeted recheck of F1-F5, plus whichever P2s are taken up, is enough. A full re-review is not needed.
