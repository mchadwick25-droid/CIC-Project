Simulated review — informational only, not an Article 31 substitute.

Round: 1
Reviewer model: Opus
Reviewer agent: independent subagent, fresh context, read-only
Drafter model: Opus
Drafter agent: the session's own Opus thread
Truncation check, method 1: last section heading "## Changes checked and found sound"; last line begins "19. Gates."
Truncation check, method 2: 12 numbered findings + 19 sound-change bullets = 31

Verdict: FAIL

Scope: I reviewed `git diff 7061fd237..HEAD` on records/cappadocian-rulings. That covers commits 0e77a55cd and 803ddccd7. They touch 29 record files, the site JSON, the package pin, `engine/m10/reviewfile.py` with its tests, and `engine/m9/enforce.py`. I checked every changed field against Mark's 13 October rulings and against the vendored sources cited in the brief. I graded every changed spoken or evidence field with `engine.m1.gates.grade_text`. I ran the embedded-quotation survey for cappadocian and `tools/check_live_commentary.py --base 7061fd237 --enforce`. I ran `python3 -m engine.m10.tests` (22 passed) and `python3 -m engine.m9.cli check` (exit 0). Two findings block, and both are in the source records from ruling 6. One source record now says a vendored work is missing when it is present. Both source records still cite an edition that does not contain the work. Everything else is sound or non-blocking.

## Findings

1. **cappadocian.source.gregory-nyssa-on-the-holy-spirit, `edition` (and `kind`). BLOCKING.**
   Old: `edition: '... vendored as cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt'`, `kind: vendored`.
   New: "Not in the vendored npnf205: neither On the Holy Spirit against the Macedonians nor the sermon on the Deity of the Son and Spirit is in that volume, which names the Macedonians only in a footnote."
   The first half of this is false. `cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt:27918-27920` reads "On the Holy Spirit. / Against the Followers of Macedonius." The full treatise follows. The volume's chronology also lists it at :411 ("377. Against Macedonius."), and it is discussed at :2576 and :27286. The second half is true. *On the Deity of the Son and the Holy Spirit* is not in npnf205: there is no money-changer, bath or bread passage. That sermon is the only work the one citing record uses (story.money-changers-unbegotten, locus "the money-changers/bath-attendants complaint, on the deity of the Son and Spirit"). So lowering that story is correct, but the record now states something untrue about the Library.
   Fix: split the record into two. One is a vendored record for *On the Holy Spirit, against the followers of Macedonius*, at npnf205:27918. The other is an unvendored record for *On the Deity of the Son and the Holy Spirit*. Point money-changers-unbegotten at the unvendored one. If you do not split it, at least rewrite `edition` so it says the treatise is present at :27918 and only the Deity sermon is missing. The emic-vendored-only count stays at 66 either way, because money-changers still cites an unvendored work.

2. **Both source records, `citation` and `discovery_channel`. BLOCKING.**
   Unchanged text in both records: `citation: '... Nicene and Post-Nicene Fathers, 2nd series, vol. 5 (...), ed. Schaff'`. `discovery_channel` also still says "a named, vendored text already sitting in cic/texts/".
   The new `edition` and `kind: unvendored` say the opposite. For the Life of Gregory Thaumaturgus, NPNF 2.5 does not contain the work at all. It only mentions it (npnf205:1246, :21346). A citation to a volume that does not hold the work is a citation error.
   Fix: change `citation` to name the work without the NPNF 5 edition, or name a real edition marked unacquired. Rewrite `discovery_channel` so it no longer says the text is vendored.

3. **cappadocian.figure.gregory-thaumaturgus and cappadocian.force.thaumaturgan-inheritance, `confidence.verification_state`. NON-BLOCKING.**
   Both records still say `verified-via-authority`. Both cite the now-unvendored Life for "the conversion-numbers legend" and "the seventeen-to-seventeen conversion claim". The two stories were lowered to `named-not-rechecked`, but these two records were not.
   Fix: lower both records to match. Or re-cite the claim to the vendored editor's introduction at `cic/texts/anf06_gregory-thaumaturgus-...xml:839-840` ("only seventeen Christians in the whole city ... only seventeen pagans").

4. **cappadocian.dw.customs-from-the-apostles, `positions[1]`. NON-BLOCKING.**
   Old: "the argument for their authority was universality and impersonal transmission, not a documentary chain any one person could produce".
   New: "Their authority came from the apostles. It was handed down unwritten, in a mystery, with the same force as the written. No one could show a written chain back to them."
   The second and third sentences match Basil, *On the Holy Spirit* 27 ("in a mystery"; "the same force"). The first sentence states apostolic origin as settled fact. The record's own `use_note` ("held to be apostolic") and `tensions` (no chain exists) do not support that.
   Fix: "Our teachers held that their authority came from the apostles."

5. **cappadocian.force.gentry-household, `description`. NON-BLOCKING.**
   New: "The mother taught the psalms and made vows for her children."
   The psalm teaching is correct for Emmelia (`gregory-nyssa_life-of-macrina_clarke1916.txt:120`). I found no vow by Emmelia in the Life of Macrina. A grep for vow, dedicate and consecrate finds only Gregory's own pilgrimage vow at :108. The original listed "the mother's vows" loosely across two households. The rewrite gives both acts to one mother in one sentence.
   Fix: drop "and made vows for her children". Or attach the vow to Gregory of Nazianzus' household, with a source.

6. **cappadocian.gravity.martyrs-land, `description`. NON-BLOCKING.**
   Old: "the panēgyris calendar". New: "Their feasts set the calendar".
   This overstates the claim. The martyrs set the festival calendar, not the whole calendar, which also had Easter and the Lord's feasts.
   Fix: "Their feasts set the festival calendar".

7. **cappadocian.force.eunomian-movement, `description`. NON-BLOCKING.**
   (a) The rewrite drops content without saying so: "that he knew God as God knows himself" and "trembling as they did it". Only build codes and scoring notes were meant to go. Restore the claim, attributed to hostile report, or record why it was dropped.
   (b) Old: "rebaptism versus graded reception". New: "the line between rebaptism and the graded welcome of those who came back."
   Graded reception in Basil Ep. 188, canon 1, covers people coming over from heretical and schismatic groups. Many of them had never been in the catholic church, so "came back" is too narrow. Fix: "those who came over from other groups".

8. **Build vocabulary left in rewritten gravity and force descriptions. NON-BLOCKING.**
   - hesychia-summons: "The pull touches nearly every other gravity."
   - hesychia-summons: "The evidence for it in the careers is documented." This is the scoring note in plain dress.
   - renunciation-order: "It counts as a lasting tension. A side with no voice of its own cannot carry more weight than that." This is the old ranking note, "a voiceless party cannot anchor more than a finding of counter-force".
   - Five force descriptions open a sentence with "This force ...". This is the fleet norm (51 force files use it), so I do not count it against this change.
   Fix: "every other pull in this world". Cut the two scoring sentences, or turn them into world content.

9. **Honesty wording left in touched doctrinal witness records. NON-BLOCKING.**
   - dw.psalms-teach-the-singer `tensions[0]`, new text: "...that gap is named, not filled". This narrates the voice's own limit and is a not-X-but-Y closer.
   - dw.not-a-death-wish `positions[0]` (spoken, evidence-head) and `sources[0].locus`: "held together honestly". Only the quotation marks were removed.
   Fix: "we cannot give our teachers' answer on the violence in scripture". Use "held together" without "honestly".

10. **cappadocian.core.cappadocian, `living_traditions`. NON-BLOCKING.**
    New: "...without the later Western addition" and "...in its Western form", then "we do not speak to the filioque".
    The facts are right. But the field points at the filioque twice and then says it does not speak to it.
    Fix: drop one of the two references, or soften the disclaimer to "we do not judge the filioque dispute".

11. **cappadocian.voice.craft, `identity`. NON-BLOCKING.**
    New: "across its whole span, from about 325 to 394. ... This people's own witness, across its whole span."
    The phrase repeats. The old text used "window" the first time.
    Fix: drop one "across its whole span".

12. **`engine/m10/reviewfile.py` and its tests. NON-BLOCKING.**
    The logic holds:
    - A full ID must be `claude-opus-5-5`.
    - A bare tier must be "opus".
    - Partial versions such as "Opus 4" and "Opus 5" are rejected.
    - Decorated values such as "Opus 5.5 (1M)" and "Opus." are rejected, as before.
    I probed 12 spellings.
    The bare-tier path cannot check the version. That is by design, but "Opus" will pass for any Opus generation. The new tests cover a bare Opus being accepted and a bare Sonnet reviewer being rejected. No test pins a wrong-generation full ID such as `claude-opus-4-1` being rejected.
    Fix: add that test.

## Changes checked and found sound

1. living_traditions: Basil and Gregory of Nazianzus replace "the elder Gregory". "Word for word", "nearly all Protestant" and "more widely than almost anything" are gone. FK 6.6, FRE 71.0.
2. contested.eustathian-radicals: "fasted on Sundays" matches Gangra's synodical letter ("fasting on the Lord's Day", npnf214:8505) and canon XVIII (npnf214:9131). "Sabbath-fasters" is gone.
3. force.persecutions-nearness: Eupsychius is added under Julian. This is consistent with figure.eupsychius and with Sozomen in npnf202. The text does not call him a bishop, which is correct.
4. force.gentry-household: the grandmother taught "the words of the blessed Gregory" (npnf208:37061-63). "Credited the women of the house" is backed by Ep. 223 ("from my blessed mother and my grandmother Macrina", npnf208:39213).
5. gravity.hesychia-summons: "never returned" is replaced by the return to Pontus and the recall. Both match Or. 43 (npnf207:41819-21 and :41900).
6. force.generations-close: Basil's 379 death date is now given as tradition, with 377 as a contested redating. "Nine months" matches the Life of Macrina ("the ninth month or a little longer", clarke1916:184).
7. The three repeated closing lines are gone. A grep of records/cappadocian finds no "given a hearth", "had banked" or "no hand can hold". The "sabbath", "lamp-lighting", "one small word" and "courtier" wording is gone too.
8. voice_craft: guard, the honest-limits note and characteristic_concerns[5] no longer announce honesty. The build words ("registry data", "sanctioned fabrications") are gone from identity. The name, the role and the one sanctioned self-description are unchanged. The four graded fields score FK 5.2–6.1 and FRE 71.8–78.2.
9. dw.marriage-ending: the positions and use_note match canon 4 ("one year ... some say two", npnf208:35030-32), canon 77 (npnf208:38592) and Moralia LXXIII (clarke1925:10192ff and :10213).
10. dw.customs-from-the-apostles: use_note.means ("handed down in a mystery") is now in line with the record's text.
11. term.panegyris: the "market thinly sourced" exclusion is removed. Longer Rules 39–40 attest the market (clarke1925:17528-34 and :17586-606).
12. story.thaumaturgus-legend: "his city of Neocaesarea" matches anf06:839-840 ("in the whole city").
13. Stories:
    - doxology-stand ("both forms") matches *On the Holy Spirit* 1.3 (npnf208:8794).
    - valens-caesarea (the decree signed, then dropped when the emperor's son fell ill) follows Or. 43.
    - macrina-refusal's "her parents brought proposals", in both `text` and `absent_detail`, matches clarke1916:124.
    - slave-market-sermon's runaway-slave rule matches the Asketikon's "Concerning slaves" (clarke1925:14044-46).
14. Ruling 6 checks: the Life of Gregory Thaumaturgus is not in npnf205. That volume only refers to it (:1246, :21346). The Deity sermon is not in npnf205 either. Lowering both stories is correct.
15. Readability: all 22 changed graded fields pass FK ≤ 10 and FRE ≥ 60. The lowest is force.persecutions-nearness at FRE 60.3, a thin margin. Ungraded fields (story `text`, use_note, tensions) are excluded by design.
16. The embedded-quotation survey for cappadocian is still 0 records and 0 spans. `check_live_commentary --enforce` is clean on all changed files.
17. demo.was-jesus-god: the source locus and the body note now say "the doxology challenge". The quote body now says "two forms of a familiar prayer side by side". This matches dw.confession-not-a-vote:41-43.
18. Waiver counts: readability 203, shelf-row 52, emic-vendored-only 66. `engine.m9.cli check` exits 0 with "every waiver is live and current", and enforce.py:299 requires exact counts. The +4 matches the four emic records that cite the two sources.
19. Gates: `pytest engine/m10/tests/test_reviewfile.py` passed 22 tests. The package repin and site recompile are consistent with commit 0e77a55cd.