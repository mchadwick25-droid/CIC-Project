# Gallic identity-and-scaffolding pass: adversarial review, round 1 (2026-10-07)

Scope: branch `records/identity-scaffolding-gallic`, commit 72b3eeae, diffed with `git diff origin/main...HEAD`. Five records were compared old against new, sentence by sentence: the four witnesses' `text`, the term's `plain_meaning` and `quick_meaning`, and every edited markdown body. The OG-26 entry and the pin were also checked. No model or API call was made, and no record was edited.

Mechanical checks, all run on the branch:
- `engine.m10.cli records gallic`: PASS.
- `engine.m10.cli regate gallic --base origin/main`: PASS. The only notes are base failures, unchanged.
- `tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- `engine.m2.site_cli staleness-check`: gallic `stale: false`, and no world in the fleet is stale.
- Embedded-quotation baseline test: passes.
- `engine.m9.cli check`: exit 0. The m9 gate reports "every finding is waived, every waiver is live and current", so the `m1:readability/gallic` waiver (count 101) is not stale.
- Pin: `records/worlds/gallic.yaml` names `packages/gallic/2026-10-07T00-25-25Z`. The `manifest_hash` `sha256:98f0c1e9...6dbb08` matches the sha256 of that package's `manifest.json`.
- Own sweep of every in-scope spoken field in `records/gallic/` for `?`, second person and stage-direction phrases. Results are under item (b).

## Verdict: REVISE

Oblique disagreement: no. The author judged gallic not oblique, and I agree. The world's sources do tell who Christ was through a story: Martin refuses the purple Christ (Vita XXIV). But that story gives a plain who-statement that the record's own `positions[0]` already states ("the Christ we confessed is the crucified one"). Inst. III.3 also says "our Lord and Saviour" outright. That is not desert's case, where the single command is itself the answer. Leading with who keeps the sources' shape.

## Findings

### 1. SUBSTANTIAL: orphaned "it" changes what the Trinity sentence says (`gallic.dw.one-person-two-substances`)
Old: "... refused it - and innovated nothing. So, did we believe in the Trinity? We held there was no other way to say it."
New: "... refused it - and innovated nothing. We held there was no other way to say it."
The removed question carried the antecedent, the Trinity. Now "it" reads back to the Ephesus sentence, so the line claims there was no other way to say *mother of God*. That is a different claim. It also leaves the retrieve_when question ("believed in the Trinity") with no sentence that names it.
Fix: "We held there was no other way to speak of the Trinity." This adds nothing; the subject comes from the removed question.

### 2. SUBSTANTIAL: answer dropped for the "strangest" question (`gallic.dw.laughed-at-and-reported`)
Old: "What would an outsider have found strangest? We can only tell you what they laughed at."
New: "We can only tell what was laughed at."
The old answer was an honest limit: we cannot say what an outsider found strangest, only what was laughed at. The new sentence drops what the limit is about. "Only" now has nothing to contrast with. The third retrieve_when line ("what an outsider would have found strangest") gets no answer in its own terms. Changing "they" to the passive is fine, because some of the laughers named next (bishops, our own presbyter) were not outsiders.
Fix: "What an outsider found strangest, we can only tell from what was laughed at."

### 3. SUBSTANTIAL: genuine contested-claim notes deleted from bodies, and the deletions are not logged
- `gallic.dw.one-person-two-substances` body, removed: "Not resolved here: whether Vincent held the brethren's position on grace (gallic.contested.massilian-label; gallic.contested.who-holds-antiquity)". The kept sentence ("Vincent is used only for the confession ... never for the grace question") keeps the usage rule. It loses the statement that a contested question is left unresolved, and the only pointers to the two contested records: neither id appears anywhere else in the file. This is source apparatus for a contested claim (CLAUDE.md, Trust and source fidelity), not process narration.
  Fix: restore it as "Not resolved here: whether Vincent held the brethren's position on grace (gallic.contested.massilian-label; gallic.contested.who-holds-antiquity)."
- `gallic.dw.laughed-at-and-reported` body, removed: "Nothing in gallic.contested.election-as-capture is resolved: the bishops' objection is given as Sulpitius reports it, and tensions[0] says whose report it is." The frontmatter `divergence_note` and `use_note` still name the contested record, so less is lost here. It is still a genuine source note and not process commentary.
  Fix: restore "Nothing in gallic.contested.election-as-capture is resolved: the bishops' objection is given as Sulpitius reports it."
OG-26's "Commentary removed" list names neither deletion. It describes the "Judgment calls" paragraph as kept apart from its label, yet this sentence went with it.

### 4. SUBSTANTIAL: OG-26 is inaccurate (`Build/worlds/gallic/Open_Gaps_Tracking.md`)
- "the four witnesses' frontmatter still names "Doc_01", "Doc_06", "Tier 3" in `divergence_note` and loci". This is false. None of the four files contains "Doc_01" or "Doc_06" (checked by grep). What the frontmatter actually holds:
  - "Tier 3 for the cloak vision" (`christ-in-the-beggar-and-the-guest`)
  - "Tier-3-shaped wonders" (`the-christ-who-bears-the-wounds`)
  - "the approved prompt's own thin-domains paragraph says" (`one-person-two-substances`)
  - "read at its own line(s) ... for this record" (`laughed-at-and-reported`, `one-person-two-substances`, `the-christ-who-bears-the-wounds`)
  Restate it with these strings.
- "Commentary removed" leaves out the two contested-note deletions (finding 3). It also leaves out the softened verification disclosures (finding 6).
- "all nine `gallic.demo.*` records carry one or two question-form lines". Inaccurate: `gallic.demo.power-against-dissent`'s participant turn is a statement ("Your church used power against Christians who disagreed."). The entry also misses that some demo *replies* carry second-person directions, which are scaffolding of the kind this pass removes:
  - `gallic.demo.record-thinnest`: "One more thing belongs with all of this, and you should weigh it."
  - `gallic.demo.never-settled`: "We do not settle it for you."
  Name them as out-of-scope carry-overs for the build thread.
- After fixes 1-3 (and 5 if taken), restate "What moved" to match. The one-person line should say that the Trinity subject was kept. The laughed-at line should give the new strangest sentence.
- Accurate parts:
  - The five-record list matches the diff.
  - The pin and package id are correct.
  - "No story record needed a change" holds: there are 15 stories. The only question in `germanus-scruple-at-morning-service` is Germanus's own reported argument ("why should chastity be any different?"), which is not scaffolding.
  - The `progress-vs-alteration` misquote is real: the source at line 13802 has "Shall there, then, be no progress in Christ's Church?". Registering it unfixed is correct, because it is quoted source speech, untouched, and outside this pass.
  - "No known-wrong claims in these five records against OG-24/OG-25" holds. OG-24 lists no defect in any of these records, and OG-25's errors are in replies. The witnesses keep the right facts: the cell for the purple Christ, and the cloak vision at night while still a catechumen.

### 5. NOT SUBSTANTIAL, should fix: the term rewrite was not warranted and left a fragment (`gallic.term.beginning-of-a-good-will`)
New `plain_meaning`: "It asks whether God has mercy on us because we first showed a good will. Or whether our good will begins because God first had mercy."
The second sentence is a fragment. More to the point, the two questions were never scaffolding. They are the world's own question, the one the term names. Its locus calls Conf. XIII.11 "the question, verbatim", and `gallic.demo.never-settled` speaks it as a question. The brief allows questions that are the world's own argument to stay. Turning them into indirect speech flattens the world's voice and changes no claim. The new `quick_meaning` ("...: whether our good will begins with us or with God's mercy.") is grammatical and acceptable.
Fix: restore the origin/main `plain_meaning` ("The one question our whole argument about grace turns on. Does God have mercy on us because we first showed a good will? Or does our good will begin because God first had mercy?"). It is identical to the base, so the regate cannot regress.

### 6. NOT SUBSTANTIAL: verification-status disclosures softened in bodies
- `the-christ-who-bears-the-wounds`: "cited through their term records, verified at Doc_06, not re-read here" became "cited through their term records."
- `laughed-at-and-reported`: "did not hit a single-line grep at this step" became "both phrases wrap across lines in the flattened file."
- All four heading lines lost "for this record".
Dropping the Doc_ references is right. But "not re-read for this record" is a fidelity disclosure, and it should stay. Fix: "...cited through their term records and were not re-read for this record." Do the same for the two wrapped phrases in `laughed-at`: "...and were not confirmed at a single line for this record."

### 7. NOT SUBSTANTIAL: wording in `gallic.dw.one-person-two-substances`
"We did not put his death as taking our punishment in our place." The claim is the same as the old "Not in those words", but "put ... as" is awkward. It can read as "regard" rather than "phrase". Suggested: "We never said that he died to take our punishment in our place." The added "Personal Lord and Saviour was not our phrase." is sourced from the record's own `tensions[3]` ("personal Lord and Saviour is not our phrase"), and OG-26 says so. Acceptable.

### 8. NOT SUBSTANTIAL: openers (item a)
- `the-christ-who-bears-the-wounds`: "Jesus was our Lord, the crucified one." This leads with who, in the world's words.
  - "The crucified one" was already in the text ("The Lord we knew was the crucified one"), from Vita XXIV via `gallic.quote.martin-on-the-christ-with-wounds`, and is the record's own `positions[0]`.
  - "Our Lord" is Inst. III.3's "our Lord and Saviour", already in the text.
  - Nothing new is added, and there is no modifier such as "truly".
  - The next sentence, "At Tours it comes as a story.", has a weak "it" (the statement just made). Optional: "At Tours this comes to us as a story."
- `christ-in-the-beggar-and-the-guest`: a bare "Yes." is acceptable. The question is a would-he question, so "Yes." answers it in its kind without restating it. The old text already gave "So, yes." as the answer, and moving it first adds nothing. Optional, so it reads well when retrieved for the other two questions: "Yes, he would have."
  - "Only one man's private word about Christ survives" replaces "One man's own word survives". "Private" and "only" come from the record's own `positions[3]` ("the private answer survives once") and `tensions[1]`. Acceptable.
- `laughed-at-and-reported`: "No, we did not hide in the catacombs." answers the did-X question. Good.
- `one-person-two-substances`: "Yes, Jesus was God." answers the did-X question. Good.
- `laughed-at-and-reported`: removing "Did it change what we were?" leaves the empire question answered only through the Martin, Hilary and Treves sentences, as before. No antecedent breaks, because "Martin's road..." stands alone. Acceptable.

### 9. NOT SUBSTANTIAL: leftover scaffolding and scope (item b)
In witness, term and story spoken fields, nothing remains apart from quoted or reported source speech:
- quote-record `text`/`modern_rendering` questions and second person
- `receiving Christ in you` inside the witnesses
- Germanus's farmer question
- Vincent's quoted question in `progress-vs-alteration`
- "the Lord your God trieth you" in `trial`
- "within you" in `kingdom-within`
`gallic.term.penance-satisfaction` `quick_meaning` "until the Abbot bids you rise" is the rule's generic "you", not a stage direction. Keep it.
The nine demo records are out of scope. See finding 4 for the gap entry.
The `progress-vs-alteration` misquote is out of scope for this pass (an untouched quote stays untouched). It belongs to the build thread as a defect, like OG-24 items 10-13.

### 10. NOT SUBSTANTIAL: doubtful lines kept in bodies, and frontmatter apparatus (item d)
- Keep the `laughed-at` catacombs-dating note ("answered 'no' on this world's own dating (its span opens c. 360) and on Sulpitius's own 'without shedding his blood'"). It states the source basis of an answer.
- Keep the term's relation-typing note. It explains a typed relation, which is genuine apparatus.
- Keep the Marseilles-location note.
- No remaining process narration was found in any of the five bodies. "Closes ...", the B-7 history, "discipline held", "Reciprocal associated-with declared" and "Built from Doc_06" are all gone.
- Frontmatter: "Tier 3" / "Tier-3-shaped" is the project's narrative-tier reliability vocabulary, not commentary. Keep it. "the approved prompt's own thin-domains paragraph says" (`one-person-two-substances` `divergence_note`) cites a build artefact as authority, not a source. It is not change history, and it sits outside this pass's spoken-field scope. Do not edit it here. Register it accurately in OG-26 (finding 4) for the build thread. The removal of "CT tag (Meaning) carried from Doc_06 section 3." from the term's `divergence_note` was provenance only, and was a sound removal.

### 11. Quotes (item g)
No quoted source wording was changed or reordered. The quoted spans are byte-identical, only rewrapped:
- "I am the soldier of Christ, it is not lawful for me to fight"
- "receiving Christ in you/them I ought to refresh him"
- "the least of these"
- Vincent's formula
- Inst. III.3
So OG-26's "none needed re-verification" holds.

## For round 2
Recheck findings 1-4 (required) and 5-6 (recommended) only. Rerun regate, the records gate and the commentary check after the edits. Rebuild and repin if records change.
