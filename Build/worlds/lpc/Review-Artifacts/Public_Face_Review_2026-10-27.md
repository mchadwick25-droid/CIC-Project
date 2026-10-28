# lpc public face (registry card, living_traditions, portraits, accent colour): independent review

**Verdict: Revise.** Three P1 findings and nine P2 findings. Most of the card holds to its records; the blocking items are a deleted safety flag, an unlogged methodology call on `living_traditions`, and the `Catholics` alias note.

- Change set: `git diff --cached` (7 files): `records/worlds/lpc.yaml`; `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` and its generator `Build/worlds/lpc/scripts/wb_lpc_s21.py`; `cic-website/assets/portraits/datus.jpg`, `cic-website/assets/portraits/thumb/datus.webp`, `cic-poc/frontend/public/images/portraits/thumb/datus.webp`; `Build/Ministry/Features/Conversation-Transparency-Engine/World-Accent-Colours.md`.
- Grounding read: the approved world front `Build/worlds/lpc/surface/world_front/lpc.front.latin-pastoral-congregational-christianity.md`; the lpc records named below; Doc_01 §1; `lpc_Decision_Log.md` entries "2026-09-16 — Project lead's Article 29 confirmation" and "2026-10-23 — `safety_adjacent` set to true"; `Review-Artifacts/Living_Tradition_Distinguishing_Statement_DRAFT_2026-09-16.md` (adopted); `Representative/lpc_Representative_Permanent_Prompt_Datus.txt`; `Open_Gaps_Tracking.md` OG-92; the witt, cappadocian and don models.
- Reviewer model: Opus 5.5 (`claude-opus-5-5`). Round 1.
- No repo file was modified other than this one. No model call, no metered spend. `canon/sealed_probes/plaintext/` was not read.

## Checks

1. **Mechanical.**
   - `records/worlds/lpc.yaml` parses (`yaml.safe_load`). `app.order` 12 is used by no other world (1 to 11 are taken). PASS.
   - `python -m engine.m1.cross_world`: 0 new defects, 6 accepted-open, 223 observations; nothing for lpc. PASS.
   - `python -m engine.m6.cli check`: `"pass": true`, no changes. PASS.
   - `python -m engine.m10.cli deployed lpc`: PASS (prompt recompiled from the pin; staleness not checked because `state` is `building`).
   - `engine.m10.common.safety_adjacent_status('lpc', <staged entry>)` returns `(None, "records/worlds/lpc.yaml has no safety_adjacent field ...")`. Handoff check 1 now fails (P1-1). The full `engine.m10.cli handoff lpc` run did not finish inside the tool limit, so the check was run directly.
   - All 15 topic words are on the shared list of 35. Every note is 14 words or fewer. PASS.
2. **Portraits.** `datus.jpg` is 1024×572 and matches the approved `Build/Ministry/Communication/Brand-Assets/Representative-Portraits/lpc/Datus_Portrait.jpg` pixel for pixel (mean difference 0). Its aspect ratio (1.790) matches nikolaus and theophilus (1344×750, 1.792). The source is only 1024 wide, so this is native size, not a downscale. Both thumbs are 344×192 like nikolaus and theophilus, and the two copies are byte-identical. PASS.
3. **Accent colour.** `#85914E` computes to 5.42:1 against `#17130F` and 5.12:1 against `#1E1913`. It is HSL 70.7°, 30.0%, 43.7%. Desert (`#9D893B`) is 47.8°, 45.4%, which is 22.9° away, and witt (`#579C40`) is 105.0°, 34.3° away. Tyrian `#6B3FA0` and lapis `#1E40AF` are more than 150° away. The entry's figures are right to rounding. The described cloak and tunic colours match the image. PASS.
4. **Readability (`engine.m1.gates.grade_text`).**
   - doorway_description: FK 8.3 / FRE 63.0. No sentence over 22 words. PASS.
   - intro: FK 6.1 / FRE 66.4. record_holds: FK 6.5 / FRE 63.8. aliases: FK 7.2 / FRE 65.6. PASS.
   - summary: FK 7.0 / FRE 66.0. One sentence of 23 words ("A century and a half later ... called him an outsider"). PASS.
   - living_traditions: FK 4.1 / FRE 87.9. PASS.
   - Topic notes, all 15 together: FK 8.2 / **FRE 57.4**, under the 60 floor (P2-8). For comparison, don scores 60.2 and witt 70.2.
   - thinness_statement: FK 51.8. It is one semicolon list, the same shape as don (FK 30.4) and witt (FK 50.5). That is a fleet format question and is not graded here.
5. **Topics: does the record base hold a view of its own?**

| Word | Strength | Supporting record | Call |
|---|---|---|---|
| Baptism | strong | `lpc.gravity.sacramental-ordination-validity`, `lpc.demo.font-twice-answered` | keep |
| Sin and forgiveness | strong | `lpc.gravity.penitential-discipline`, `lpc.term.reconciliation-penitential-discipline` | fix wording (P2-8) |
| Persecution | strong | `lpc.force.decian-persecution-libelli-system` (Documented) | keep |
| Martyrs | some | `lpc.gravity.confessor-authority-vs-episcopal-peace`, `lpc.quote.thousands-of-certificates-daily`, `lpc.story.the-death-of-cyprian` | fix (P2-5) |
| Church leaders | strong | `lpc.gravity.pastoral-office-flock-keeping`, `lpc.term.the-people` | keep |
| Church councils | some | `lpc.gravity.conciliar-authority-theory` (Inferential-Thin as an organising concern, but each bishop's theory is Documented in his own words), `lpc.quote.bishop-of-bishops`, `lpc.quote.earlier-councils-corrected-by-later` | keep |
| Church splits | strong | `lpc.gravity.collegial-communion-preserved` (Widely Accepted), `lpc.force.donatist-schism` | fix (P2-1) |
| The emperor and the state | strong | `lpc.contested.compel-coercion-development`, `lpc.demo.compel-three-phase`, `lpc.force.illegal-to-established-shift` | keep (P2-8 wording) |
| Salvation and grace | strong | `lpc.gravity.grace-and-human-incapacity` | keep |
| Heaven, hell and judgment | strong | `lpc.witness.punishment-without-end` | keep |
| Feast days and remembering the dead | some | `lpc.witness.remembered-at-the-altar` | keep |
| Caring for the sick | some | `lpc.story.the-plague-and-the-enemies` (Widely Accepted, Pontius only) | fix (P2-4) |
| Money and the poor | strong | `lpc.witness.almsgiving-quenches-sin` | fix (P2-3) |
| The Bible and how to read it | some | `lpc.witness.scripture-above-councils` | keep (P2-8 wording) |
| Marriage and family | some | `lpc.witness.marriage-a-threefold-good` | keep (P2-8 wording) |

6. **Claim tracing (fields not listed under Findings trace cleanly).**
   - doorway_description: the persecution of 250 (`lpc.force.decian-persecution-libelli-system`); the road back (front `orientation.story` 5); 246 to 430 and the two cities (front story 1); one bishop per people (front story 2); Augustine on Cyprian (front story 11, `lpc.gravity.collegial-communion-preserved`); the 430 close (front story 14). One sentence fails (P2-2).
   - intro and summary: front `skim.tile`, nearly word for word. record_holds: tile and `lpc.limit.the-lapsed-own-account`, and it follows the 2026-10-19 rule. `shaped`: `lpc.figure.cyprian`, `lpc.figure.augustine`, `lpc.figure.possidius`.
   - thinness_statement: world_core `thinness` and the honest_limit records. The 133-year silence is rightly tagged Contested (`lpc.limit.the-silent-century`). One parenthesis fails (P2-7).
   - Notes not fixed below: Baptism (front story 7 and 11); Persecution (front story 4); Church leaders (front story 2 and 3); Church councils (`lpc.quote.bishop-of-bishops`, `lpc.gravity.conciliar-authority-theory`: "a council of one province must yield to a plenary council"); Salvation and grace (front story 13); Heaven, hell and judgment ("some, indeed very many, make moan", `lpc.witness.punishment-without-end`); Feast days (`lpc.witness.remembered-at-the-altar`: "these gifts help only those who earned that help in life").
   - living_traditions: "no one church is our single heir", "before the Western church divided" and "none holds the whole of it" match the adopted statement §2 ("No single tradition is this world's heir"; "ancestral to the Western church *before its divisions*"; "Every Western communion has a claim ... none has an exclusive one"). They also match the Permanent Prompt's closing paragraph, which Doc_10 §6 says carries this in the voice's own terms. The text names no heir, states none of the four divergences, does not judge later disputes, and does not speak *for* any church, so it holds to caution 16. It is framed as the project lead's confirmed finding, not as a settled historical claim. Two problems remain: P1-2 (placement) and P2-9 (one sentence).

## Findings

### P1 (blocking)

- **P1-1 (`records/worlds/lpc.yaml`): `safety_adjacent: true` has been deleted.** The staged diff removes the line `safety_adjacent: true`; it is gone from the working tree too. Set by: `lpc_Decision_Log.md`, "2026-10-23 — `safety_adjacent` set to true (project lead's ruling, stop point 1 item 1)"; `build/lpc_Handoff_Manifest.md` row 1. Effect: handoff check 1 now fails ("has no safety_adjacent field; the project lead sets it"), and `safety_adjacent_status` returns `None`. That would take lpc off the full validation route that `lpc_Doc_10_Representative_Construction.md` §7 depends on. A build thread may not remove a field that only the project lead sets. **Fix:** restore `safety_adjacent: true` (for example after `census_id`, where it was). Keep the move of `state:` only if it is meant.

- **P1-2 (world_core `living_traditions`, and `horizon`): this settles a question logged as the project lead's, and leaves the old text beside it.** `Open_Gaps_Tracking.md` OG-92, "Open, for the project lead": whether the confirmed Living Tradition Status "moves into `world_core.living_traditions`. That is a methodology decision." No Decision Log entry or OG update records a ruling. CLAUDE.md, default actions: "Governance or methodology change: Always ask". Second problem: `horizon` still carries "This tradition is still living, but it has no single named heir ... close to how most historic Christian churches understand the work of a parish or a diocese". So the voice now gets two living-tradition statements. The horizon one makes the post-430 survey that `P2_Record_Fixes_Review_2026-10-27.md` P2-3 flagged against caution 16. The s21 note now says "`horizon` and `living_traditions` state the confirmed finding", which records the duplication rather than resolving it. **Fix:** if the project lead has ruled in conversation, log that ruling (Decision Log and OG-92) with this change. In the same change, replace the `horizon` paragraph with the earlier review's wording: `Its core is an ordinary bishop's care of a local flock, in one place, through the sacraments and the gathered congregation. It is not a claim that belongs to one see's own line of succession.` Then mirror the change in s21 `HORIZON` and the s21 note. If he has not ruled, put it to him before merging.

- **P1-3 (`card.aliases`, `Catholics`): the note takes one side of a dispute and leaves out the gloss the records require.** Current: "Possidius's word for Augustine's own congregation; it means the whole church of his day." The alias itself is well supported, more widely than the brief says. Support: `lpc.quote.clamour-and-tears` ("The Catholics"), `lpc.quote.pardon-through-a-wicked-clergyman` ("a Catholic minister"), `lpc.quote.ye-belong-to-my-care` ("a Catholic people"), and world_core `horizon` ("the same catholic communion that Cyprian had led"). The note has two faults.
  1. "the whole church of his day" adopts the Catholic party's claim against the Donatists, who claimed the same thing in the same towns. Doc_01 §5 says the build "does not adjudicate which communion was legitimately the church". This is a contested claim presented as settled.
  2. The records require a gloss against the modern reading. `lpc.quote.pardon-through-a-wicked-clergyman` claim_guard: "'Catholic' in this passage must not be read as 'Roman Catholic'; it means the Church in communion across the world, and a gloss is needed if the term is shown to a participant." `lpc.quote.earlier-councils-corrected-by-later` not_for: "a claim that 'Catholic' here means a modern denomination". This is a living-tradition world, and the adopted statement says "No present-day body may be presented as *the* continuation of it". A searchable alias "Catholics" with no gloss invites exactly that reading.

  **Replacement (14 words):** `Their own word: the church in communion across the world, not today's Roman Catholic Church.` Keep `kind: own`.

### P2

- **P2-1 (topic `Church splits`): the note states as a rule what the record says is a tendency.** Current: "Bishops who disagreed sharply stayed in communion. The Donatists set up a rival church." `lpc.gravity.collegial-communion-preserved` says bishops "work to keep communion rather than break it". It rates the cross-phase pattern Widely Accepted, and its not_for lists "a claim that bishops never broke communion". **Replacement (14):** `Bishops tried to hold together through disagreement. The Donatists set up a rival church.`

- **P2-2 (`doorway_description`): "This church argued hard about the font, about councils and about grace, but always inside a bond it would not break."** The grace argument did not stay inside the bond. `lpc.gravity.collegial-communion-preserved`: "The fight over grace went another way. African councils condemned what the Pelagians taught. ... It does not reach teaching a council judged heresy." The Permanent Prompt says the same. The sentence comes from the approved front's `skim.tile`, which has the same defect. That is outside this change set and should be logged in `Open_Gaps_Tracking.md` for the front. **Replacement (21 words, FK 8.3 / FRE 72.7):** `This church argued hard about the font and about councils, but kept its bond even with a bishop it judged wrong.` (The front's `relations_summary` says "This church kept its bond, even with the bishop it judged wrong.")

- **P2-3 (topic `Money and the poor`): the note credits Cyprian with a Scripture quotation and ends in a fragment.** Current: "Cyprian wrote that almsgiving quenches sin as water quenches fire, and told the rich." `lpc.witness.almsgiving-quenches-sin`: "Scripture itself says what almsgiving does, and he quoted the words directly". "and told the rich" leaves out what he told them ("share your gains with Christ"). **Replacement (14):** `Cyprian taught, quoting Scripture, that almsgiving quenches sin; he told the rich to share.`

- **P2-4 (topic `Caring for the sick`): the note gives a one-witness story as plain fact.** Current: "In the plague Cyprian told his people to help everyone, enemies included." `lpc.story.the-plague-and-the-enemies` is Widely Accepted. Its `means` says "Pontius says that in the plague Cyprian preached love of enemies". Its not_for includes "a claim that any source outside Pontius describes the relief". The front teaser says "Only his deacon's account keeps the sermon." **Replacement (14):** `Cyprian's deacon says that in the plague, Cyprian urged help for everyone, even enemies.`

- **P2-5 (topic `Martyrs`): the note never mentions martyrs.** Current: "Confessors claimed to grant peace to the lapsed; Cyprian said it was not theirs." Someone who searched "Martyrs" gets a note about confessors, who by the records' own definition survived (`lpc.term.confessor` retrieval: "a martyr, who died, rather than a confessor, who survived"). Cyprian's own words name both groups: the lapsed "were everywhere soliciting the martyrs" and he wrote "to call the martyrs and confessors back" (`lpc.quote.thousands-of-certificates-daily`). The tag passes the test: the confessor-and-martyr claim to grant peace is a Documented tension (`lpc.gravity.confessor-authority-vs-episcopal-peace`), and `lpc.story.the-death-of-cyprian` adds Cyprian's own death. The replacement keeps the gravity's guard against "resolved" and against "usurpers or heroes". **Replacement (14):** `The lapsed begged martyrs and confessors for peace; Cyprian held it was not theirs.`

- **P2-6 (`card.aliases`, `Latin Pastoral Congregations`, `kind: scholarly`): no record or scholar uses this name.** The string appears in no lpc record. It is a shortened form of this project's own world name, and `scholarly` claims that scholars use it. The rule is that aliases come only from the world's own records (`Topic-Tags-Trace.md`, "Alternate names"). Its note ("this church had no special name for itself") also sits awkwardly beside the `Catholics` alias, which is labelled `own`. **Fix:** drop this alias. The front already explains that the world name is a modern label.

- **P2-7 (`thinness_statement`): "women's own words (named women appear only in letters addressed to them or sermons about them)".** `lpc.limit.womens-own-voice` names more than that: Numeria and Candida "discussed, weighed, and sent to their peace by two men writing to each other about them"; Numidicus's wife and daughter in a letter about him; and Quartillosia, whose vision a martyr account gives "in her own first person". "Only ... addressed to them or sermons about them" is wrong. **Replacement parenthesis:** `(no text a woman wrote survives; women appear in men's letters, sermons and one martyr account)`.

- **P2-8 (topic notes, readability and one broken sentence): the notes together score FRE 57.4, under the floor of 60.** Worst: Sin and forgiveness (FRE 41.6), The Bible (44.0), Marriage (44.0), The emperor (47.6). In "Those who failed under persecution walked a road back, weighed, then received home openly", "weighed" and "received" have no subject, so the sentence does not parse. With P2-1, P2-3, P2-4, P2-5 and the four replacements below, the notes together score FK 7.5 / FRE 61.2. Each stays within 14 words and within its record:
  - Sin and forgiveness: `Those who gave way could come back, by a road examined and walked openly.` (front story 5)
  - The Bible and how to read it: `Scripture stood above any bishop's letter, but bishops and councils held real authority too.` (`lpc.witness.scripture-above-councils`: "Our bishops and councils held real authority of their own")
  - Marriage and family: `Augustine said marriage is good in three ways: children, faithfulness, and its sacrament.` (`lpc.witness.marriage-a-threefold-good`)
  - The emperor and the state: `Cyprian asked the state for nothing. Augustine later backed force against the rival church.`

- **P2-9 (`living_traditions`, sentence 8): "If you hear your own church in us, take it as a likeness across a long distance, not as a warrant."** This is the move the adopted statement gives to the Facilitator: "Where a participant hears their own tradition in him, the Facilitator names the distance rather than letting the resemblance stand as endorsement." The Decision Log adds: "Datus holds none of it." The rest of the text limits what Datus himself claims. This sentence addresses the participant's own church and passes judgment on it. **Fix:** delete it. The next two sentences ("Those churches have their own voice ... We leave that to them.") already close the field, as witt's and the Permanent Prompt's do.

## Notes (not findings)

- The pinned package (`2026-10-27T14-24-15Z`) predates the world_core edit. Rebuild and re-pin after the fixes, under the default action for a `records/` edit.
- The Church councils note ("a wider council can correct a narrower one") is softer than On Baptism II.3.4 ("must yield"), but it matches the gravity's own wording and is not wrong.
- Calling the Donatists "the rival church" in two notes follows the front and the records' own usage; this world speaks from the Catholic side by design.

## Verdict

**Revise.** Restore `safety_adjacent: true` (P1-1). Log the project lead's ruling on `living_traditions` and resolve the duplicate `horizon` paragraph in the same change (P1-2). Rewrite the `Catholics` alias note with the gloss its records require (P1-3). Apply P2-1 to P2-9. A round-2 targeted recheck should cover only those items, plus `cross_world`, `m6 check` and the handoff identity check.
