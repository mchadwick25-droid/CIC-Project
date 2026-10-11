# hal identity-and-scaffolding pass: adversarial review, round 1

Reviewer: Opus 5.5. Date: 2026-10-07. Scope: branch `records/identity-scaffolding-hal`, two commits ahead of origin/main (`fb205902` records, `8be8262a` site JSON). Diff checked: `git diff origin/main...HEAD`. No model or API call was made, and no record was edited.

What I did:
- Compared the old and new `text`, sentence by sentence, for all 14 changed records (13 witnesses, story `attack-416`). Read each record's `positions`, `use_note` and `retrieve_when` to check what the opener must answer and what the record may claim.
- Read the body of every edited file on HEAD, and the removed body lines in the diff.
- Swept every in-scope spoken field in `records/hal/` (witness, term, story, plus quote `modern_rendering`) for `?`, second person and stage-direction phrases, including untouched files. Read all nine `hal.demo.*` records for the gap entry's claims.
- Checked OG-14 sentence by sentence against the diff, OG-8, OG-12 and OG-13.
- Ran the gates (results at the end).

## Verdict: REVISE

Oblique disagreement: no. hal's sources are Jerome's letters, prefaces and the Dialogue against the Pelagians. They state who Christ is to this world outright (Ep. 108 sec. 10, Ep. 22 secs. 1 and 25). The author judged hal not oblique, and I agree. `hal.dw.jesus` already led with who, and that is right.

## Findings

### 1. SUBSTANTIAL: `hal.dw.apostolic`, opener has no verb object

New: "Some of our practices did, and some were new."

"Did" stands for "go back to the apostles", and that phrase was in the removed question. Read alone, as a retrieved chunk is, the sentence does not say what the practices did. This is an orphan of the kind the ruling forbids.

Fix: "Some of our practices went back to the apostles, and some were new." Nothing else changes.

### 2. SUBSTANTIAL: `hal.dw.marriage-ending`, first sentence does not answer the question

New: "We did not answer with a ruling. Our answer was Fabiola: divorced, she belonged here."

The question is "Could someone divorced belong here? Could they marry again?" The first sentence says how the world did not answer. The answer arrives in sentence two. The ruling says the first sentence answers, in the kind asked. alx round 1 sent back the same shape (the answer in a later sentence). This is not obliqueness in the sources. Ep. 77 sec. 3 argues the law directly, and the record keeps that argument.

Fix (one sentence, nothing added, the record's `not_for` "a general canon or ruling rather than one remembered case" still held): "Our answer was not a ruling but Fabiola: divorced, she belonged here. We kept her story where everyone could see it."

Also log in OG-14 that "here" was added to "she belonged" (from the removed question's "belong here"). The entry does not mention it now.

### 3. SUBSTANTIAL: `hal.dw.hell`, "without softening" moved from the telling onto the belief

Old: "Here is what we actually held, without softening. We believed in real judgment and real punishment."
New: "We believed in real judgment and real punishment, without softening."

In the old text, "without softening" described how the world was telling it. Now it describes the doctrine: punishment held without softening. The same paragraph then says "our writings are not consistent executors of their own severity" and that the same pen "hoped much from penance". The record's positions say "severity in principle, hope in every particular case". So the moved phrase now makes a claim the record itself qualifies. The world's own demonstration (`hal.demo.hell`) uses it as the old text did, as a frame for the telling: "Here is what we held, without softening. We believed in real judgment and real punishment."

Fix: "We believed in real judgment and real punishment. We say so without softening." alx used the same form ("We say it plainly and do not smooth it over"), and round 1 there accepted it. Update OG-14's `hell` bullet.

### 4. SUBSTANTIAL: `hal.dw.practices`, the end-times negative is widened

Old: "What about the end of the world - anything like the rapture? No such scheme is in our pages."
New: "No scheme of the end of the world, nothing like the rapture, is in our pages."

The old "such scheme" meant a rapture-like scheme. The new sentence denies any scheme of the end of the world, with the rapture only as an example. That is a wider claim. The record's positions say "no rapture scheme", and its `not_for` says "a rapture or calculated end-times scheme". Jerome's own later work on Daniel does read the end through the prophets, so the wider denial is a risk as well as a change. This is the quantifier class the brief warns about.

Fix: "No end-of-the-world scheme like the rapture is in our pages." Update OG-14's `practices` bullet.

### 5. SUBSTANTIAL: `hal.dw.one-church` body, a genuine scope disclosure was deleted

Removed: "- the living-tradition determination and its doorway chrome are Mark's touchpoint, outside this record."

"Mark's touchpoint" and "doorway chrome" are process words, and they should go. But the sentence also said one true thing about the record: it does not decide whether this world is a living tradition. That question is still open. OG-8 holds it open, and its argument rests on this note: the record "does not resolve it either way and says so in its own trailing note". The registry now carries `living_tradition_flag: false`, while OG-8 says `true`. After the deletion, OG-8's statement about the record is no longer true. OG-8 is append-only, so the record must keep the disclosure.

Fix, record body: "...without naming or ranking present-day claimants. Whether this world is a living tradition is not decided in this record." Fix, OG-14: say the attribution was cut and the scope clause kept. Also say that OG-8 quotes the old `text` ("Is there a church today you could visit that is ours? No..."), and that this now reads "No church you could visit today is ours. No single door today opens onto us." The entry's cross-reference covers only the body sentence. With these changes, OG-14 is the cross-reference OG-8 needs, and OG-8 itself stays untouched.

### 6. SUBSTANTIAL: `hal.dw.hell` body, stale build narration kept

Kept: "...is a demonstration-stage requirement in the world's own idiom, noted here for the later voice build; this witness supplies the doctrinal substance under it."

Most of this note is a fair record description. It says where the non-judgment line lives and what this witness supplies. alx round 2 kept a note of the same kind. But "noted here for the later voice build" narrates a build step, and hal's voice is already built and admitted. Under the live-surface rule it has to go.

Fix: "The non-judgment discipline for the asker ('It is not ours to judge you...') is a demonstration-stage requirement in the world's own idiom; this witness supplies the doctrinal substance under it." List the removal in OG-14.

The `marriage-ending` note ("The non-judgment line in the world's idiom is a demonstration-stage deliverable; this witness is its substance.") does not narrate a build. It describes the record. Keep it, and move it from OG-14's doubtful list to the kept list.

### 7. SUBSTANTIAL: OG-14's demonstration paragraph is inaccurate

The entry says all nine `hal.demo.*` records carry "one to three question-form lines (the participant question each answers; `born-again` three, `hell` and `suffering` two, the rest one)". It also says they carry "no second-person directions of the kind removed from witnesses".

The counts are right, but the description is not:
- `hal.demo.born-again`: the third question line is the Representative's own, "Would you like the honest version too - what happened after the turning?". It is not a participant question.
- `hal.demo.hell`: the second question is in the Representative's reply, "Is one way too narrow?". The same reply opens "Here is what we held, without softening." Those are the same scaffolding this pass removed from `hal.dw.hell`.

Fix: "Every demonstration carries the participant question or questions it answers (`suffering` has two in one turn; `born-again` has two participant turns, the second with two questions). Two Representative replies also carry scaffolding of the kind removed from witnesses: `born-again` ('Would you like the honest version too - what happened after the turning?') and `hell` ('Here is what we held, without softening.' and 'Is one way too narrow?'). Out of scope; not edited." Check the counts against the files when you rewrite this.

### 8. Not substantial: `hal.dw.was-jesus-god`, the addition recovers content; "the answer" is weak

"That is near to the later language of punishment in our place without being identical to it." The phrase "of punishment in our place" comes from the removed question ("Did he die to take our punishment, in our place?"). Without it, "the later language" points at nothing. It matches the record's positions ("not yet in later penal formulas") and its `not_for` (penal substitution). It recovers content and adds nothing new, and OG-14 logs it honestly.

The opener "Jesus is God the Son, of one being with the Father" answers the did-question in its kind. One weak spot: "we never treated the answer as negotiable" now has no question for "the answer" to answer. Optional: "...had settled that, and we never treated it as negotiable."

### 9. Not substantial: `hal.dw.sin-grace`, "that ground" now points elsewhere

"Our last great argument came close to that ground" used to point at the born-guilty question. Now it points at "everyone inherits Adam's fall, and everyone needs the washing of baptism." That is still true of the Pelagian fight. "The exact machinery of inherited guilt was still being worked out" keeps the hedge, as `not_for` requires. No fix needed. Optional: "Our last great argument came close to the question of inherited guilt."

### 10. Not substantial: `hal.dw.marriage-ending`, "Remarried, it was named a fault"

Moving "divorced, she belonged" up broke the old pair ("So: divorced, she belonged. Remarried, it was named a fault"). The second half now stands alone. It still reads correctly after "She then married again while he lived" earlier in the paragraph. No fix needed.

### 11. Not substantial: `hal.dw.authority`, untouched retrieval mismatch not logged

Its `retrieve_when` is "participant asks who appointed or ordained the bishops", and the text does not answer that. The opener was not edited, so this is not a defect of the pass. OG-14 logs the matching `sin-grace` mismatch. For consistency, add a sentence for `authority` too.

### 12. Not substantial: second-person frames in untouched witnesses

`believe` ("To someone who wants to believe and cannot, we offer...", "What we would say to you is not an argument."), `inner-life` ("To someone who cannot quiet their own head...") and `church-failure` ("If you want a church that never failed...") are offers and arguments made in the world's own voice. They do not restate a participant question. cappadocian round 1 proposed the same "For someone who wants to believe and cannot" form as its fix. No terms or stories carry scaffolding. The `?` and second-person hits in stories and quotes are quoted source speech (the crowd in `rome-crisis`, the Cicero dream, the Bridegroom letter, Rufinus to Anastasius) or the disclosure in `day-at-monastery`. Leave all of these.

### 13. Not substantial: body rewrap

Removing the cell headers left short first lines in several bodies (for example "The novelty admission is Ep. 127 sec. 5's own"). This is cosmetic only. Markdown renders it the same.

## Checks with no finding

- `hal.dw.jesus`: "To us Jesus is the Word of God made flesh. He was made flesh in the very place where we chose to live and die." It says who first, in the world's own words. "He was" is the only addition, and OG-14 says so. The sources are unchanged (Ep. 108 sec. 10; Ep. 22 secs. 1, 25). The rest of the text is identical.
- These openers answer in kind and keep every claim: `doubt` ("There was room for questions"), `empire` (catacombs; "We said the empire's embrace had corrupted the church. We said it loudly - about everyone but ourselves", with the qualifier kept), `one-church` ("Our church was Catholic"; "No church you could visit today is ours"), `record` ("we had the writings about Jesus"; "We knew the resurrection really happened from...", which is the old answer stated as the world's own), `suffering` (the old answers moved first; "Those are the answers we give, and our sobs come with them"), `authority` (Nicaea sentence, wrong-witness limit kept), `practices` (born again and tithe), `attack-416` (the restraint sentence keeps all three unknowns).
- Removed body commentary: every removed line is process (cell headers, "register bar" lines, "spoken field is written in plain modern English" lines, label-pass notes, "Re-derived from cleared Doc_09a S4...", "Serves F6-P"). The one exception is finding 5. Source notes, verification disclosures ("verified verbatim"), the uncited-Ezekiel-commentary disclosure in `empire` and the Dialogue chapter note in `one-church` were all kept.
- Quotes: no quotation in an edited spoken field was touched, so no re-verification was needed. OG-14 is accurate on this.
- Known-wrong claims: OG-12 item 2 (`was-jesus-god`, "a dying woman greeted his birthplace by name") and item 5 (`empire`, inheritances and "before dawn") are carried unchanged, and OG-14 cites both. No other OG item names an edited record's text. OG-8 concerns the registry flag, not a wrong claim, and finding 5 covers it. OG-13 is about voice replies. OG-14's note that `hal.yaml` carries `false` while OG-8 says `true` is accurate. The flag is unchanged on this branch.
- OG-14 otherwise: the record list is complete (14 records plus the pin). The 23 terms and 11 other stories are counted correctly. The list of removed notes matches the diff for every file. The oblique note, package id and gate lines are accurate.
- Pin: `records/worlds/hal.yaml` pins `packages/hal/2026-10-07T01-08-48Z`, `sha256:d7667553...69437`. This equals the SHA-256 of the committed `manifest.json`.

## Gates (run on HEAD `8be8262a`)

- `engine.m10.cli records hal`: PASS.
- `engine.m10.cli regate hal --base origin/main`: PASS. Only notes on pre-existing base failures in terms and voice_craft.
- `engine.m2.cli determinism-check hal`: PASS.
- `engine.m10.cli deployed hal`: PASS. Pre-existing notes on telos and source_anchor.
- `engine.m2.site_cli staleness-check`: hal `stale: false`; no world stale.
- `tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- Embedded-quotation baseline test: passes.
- `engine.m9.cli check`: clean, every waiver live and current.

## For the revision

Make the record fixes in findings 1-6 and correct OG-14 for findings 2, 3, 4, 5, 6 and 7. Then rebuild the package, repin, and recompile the site JSON if staleness-check marks hal stale. Rerun regate, because the hell and marriage-ending fixes change sentence counts. Findings 8-13 are optional.
