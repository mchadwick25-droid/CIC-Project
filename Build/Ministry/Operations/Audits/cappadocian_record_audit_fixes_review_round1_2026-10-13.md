Simulated review — informational only, not an Article 31 substitute.
Review round 1, cappadocian record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Round: 1
Reviewer model: Opus
Reviewer agent: independent subagent, fresh context, read-only
Drafter model: Opus
Drafter agent: the session's own Opus thread made the record edits; this reviewer did not draft them
Truncation check, method 1: the file ends on the last bullet of 'Changes checked and found sound' (the Iconium / Doc_01 line), a complete sentence with its closing citation
Truncation check, method 2: the saved file is 14,652 characters, the same length as the reviewer's returned message, counted separately before saving

Verdict: FAIL

Scope: Commit 42ef9c4 changes 77 record files under `records/cappadocian/` and two waiver counts in `engine/m9/enforce.py`. I compared each record against `origin/main` field by field. The working-tree records are byte-identical to 42ef9c4. No uncommitted record edits exist. The brief expected readability rewrites to 12 fields still sitting in the working tree, but none are there. Those rewrites are either already in the commit or were never made. The only uncommitted changes are the package pointer in `records/worlds/cappadocian.yaml`, the site JSON, and an untracked `packages/cappadocian/2026-10-13T04-36-23Z/`. For each changed spoken field I checked four things. Are its claims supported? Is each quote rendering faithful to the record's `text`? Do Mark's rulings hold? Does it pass readability? I also checked the vendored sources named in the brief and ran `gate_horizon` and `gate_readability` on old and new records. Read-only. No model calls.

Mechanical results:
- All 77 frontmatters parse.
- No body (below-frontmatter) text changed.
- No field outside the spoken fields changed.
- All 84 changed fields pass readability, from FK 3.3 to 9.7 and FRE 60.1 to 89.5.
- The readability findings fall from 274 to 228, which matches the new waiver.
- The horizon findings fall from 5 to 4. The finding removed is the one for `dw.catholic-and-its-rivals.text` (see Finding 4).

## Findings

1. **dw.not-a-death-wish / text**, BLOCKING.
   Old: "one of our own bishops was executed under the last persecuting emperor - not because he sought death, but because he would not deny the faith when denial was the one way out offered."
   New: "Decades later, under the last persecuting emperor, one of our own, Eupsychius of Caesarea, was put to death. We kept his feast every year. We have no word from our own side of what he said at the end. Wanting to die was never the virtue we named. The virtue we named was refusing to deny the faith when denial was the one way out."
   Source: Sozomen V.11 (`cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml:36048-56`): "I believe that Eupsychius was condemned in consequence of the demolition of the temple of Fortune." The NPNF note on Basil Ep. 100 (`npnf208_basil-letters-select-works.xml:30451-53`) says the same.
   The fix corrects "bishop" and drops the explicit motive. But the paragraph still places him as its example of refusing to deny under threat. The only surviving account gives a different cause, and that cause bears directly on the death-wish question. The record's `sources[2].locus` still reads "executed under Julian for refusing to deny the faith." Its `use_note.means` still cites Eupsychius as an instance of refusal. The drift has moved into the record's metadata and implication rather than being removed.
   Fix: either say what the later historian reports, in the world's voice (for example, "A later historian says he was condemned for his part in pulling down the temple of Fortune in our city"), or take Eupsychius out of this field. Then correct the locus and `use_note.means` to match.

2. **term.panegyris / plain_meaning and quick_meaning**, BLOCKING.
   Old: "merchants set up stalls -- worship and social life together in one event" / "vigil, preaching, and a market".
   New: "Traders may have come too, but our word of that is thin." / "vigil and preaching on one holy day."
   Source: Basil, Longer Rules 39-40 (`cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt:17532` and `:17586-17606`). Rule 39 sends brothers to "the functions designated fairs" (Clarke's note: πανηγύρεις) to sell their work. Rule 40 says "buying and selling conducted at martyrs' tombs is not fitting for us," and that others "may have used the time and place as a market and fair."
   The evidence is not thin. It is direct, and it comes from the world's own rule. The fix introduced an under-claim and a new hedge. `use_note.means` still says "vigil, preaching and market," so the record now disagrees with itself.
   Fix: "Buying and selling went on there too. Basil's rule told the brothers not to trade at the martyrs' tombs." Put the market back into `quick_meaning`.

3. **dw.psalms-teach-the-singer / text**, BLOCKING.
   Old: "That question, honestly, is one our own surviving voices do not address directly, at least not in anything we can point you to".
   New: "We have no word from our own teachers about the violence in our scriptures."
   Source: Gregory of Nyssa, Life of Moses II.91-92. It asks how the death of the Egyptian firstborn fits God's goodness, and reads the passage spiritually. This text is not vendored. The new sentence is a flat claim that nothing exists, and it is false. The old wording was badly phrased, with an assistant-style "honestly," but it limited the claim to what could be shown. The fix removed that limit along with the tell.
   Fix: keep the absence limited, in the world's voice. For example: "On the violence in our scriptures, we can give you nothing from our teachers here." Or, once Life of Moses is vendored, name Gregory's spiritual reading.

4. **dw.catholic-and-its-rivals / text and the m1:horizon/cappadocian waiver (5 to 4)**, BLOCKING.
   Old: "Orthodox and Catholic dogmatics still argue in vocabulary this circle fought to place. So, more distantly, does Protestant dogmatics."
   New: "The teachers who formed us became curriculum, liturgy, and law for the traditions that trace themselves back through the councils. ... Churches today still argue in the words we fought for."
   Source: `engine/m1/gates.py:1571` (`gate_horizon`) only matches dated terms. On `origin/main` it flags this field for "the protest at Speyer (1529)." On HEAD it does not. Removing the word "Protestant" cleared the gate. But the voice still speaks from after the window closes in 394: "Churches today" and the later traditions. The waiver was lowered because of this edit. The defect is now invisible to the gate and missing from the register.
   Fix: rewrite from inside the window, ending at "We lived through one of those councils, at Constantinople." Leave the modern bridge to the Facilitator. If Mark rules that this cell may look forward, mark it that way and put the waiver back to 5.

5. **story.doxology-stand / text, story.macrina-refusal / text, demo.was-jesus-god / sources[].locus**, NON-BLOCKING.
   The commit fixed the doxology account in seven spoken fields. The account now reads "praying with the people," with both forms used (DSS 1.3, `npnf208:8793-98`). But the story's own `text` still says Basil "stood at the evening lamp-lighting" and treats the incident as one changed preposition. It now contradicts its own new `tellable_as`. `demo.was-jesus-god`'s source locus still says "the lamp-lighting challenge." `story.macrina-refusal.text` (:45) and its `absent_detail` still say "her mother tried to arrange." The source says "her parents brought proposals" (`gregory-nyssa_life-of-macrina_clarke1916.txt:128`). `quote.basil-on-the-doxology-challenge`'s body (:121) quotes the retired dw wording, which is commentary in a canonical file.
   Fix: log these in `Open_Gaps_Tracking.md` and fix them in a follow-up slice. `story.text` was outside the audited field list.

6. **term.doxologia / plain_meaning**, NON-BLOCKING.
   New: "Our fight over the Holy Spirit broke out over one line of prayer."
   Source: DSS 1.3 (`npnf208:8793-98`). The doxology incident was the occasion of the treatise, not the start of the dispute. Basil's dispute over the Spirit was already live before it, for example his break with Eustathius.
   Fix: "One flashpoint in our fight over the Holy Spirit was a single line of prayer."

7. **term.mysterion / plain_meaning and quick_meaning**, NON-BLOCKING.
   New: "We used it of the sacred rites above all" / "above all in the holy rites of the church."
   The ranking "above all" is new. Nothing in the record's `senses` or `use_note` supports it. `use_note.means` lists rite, Scripture and God on an equal footing.
   Fix: drop "above all," or source it.

8. **Repetition closers in four fields**, NON-BLOCKING.
   - **demo.woman-authority**: "Her own voice was not written down. ... It was real, and it carried a teacher's title. Her own voice was not kept." The echo is a rhythmic closer. Drop the last sentence.
   - **term.akatalepsia**: "We held that together with a second truth ... We held both truths together." Drop the last sentence.
   - **dw.not-later-formulas**: "in those terms" appears twice in three sentences. Drop "We did not argue it in those terms."
   - **demo.was-jesus-god**: "gave glory in two forms. One was to the Father with the Son, together with the Holy Spirit." The second form is never named. Add "the other, through the Son in the Spirit," as `dw.holy-spirit-honored` does. "everyone knew they were not small" is kept from the old text. It is a flourish with no source and could go.

9. **dw.marriage-ending / text**, NON-BLOCKING.
   New: "A husband whose wife left him could be pardoned." and "A year of penance came first, sometimes two".
   Source: canon 9 (`npnf208:35217-22`): "the man who has been abandoned is pardonable, and the woman who lives with such a man is not condemned". This means pardoned for taking another woman. Canon 4 (`:35030`): "some authorities say two years".
   As written, the reader cannot see what is pardoned. That hides the custom's unequal treatment, which the next sentences rely on.
   Fix: "could take another wife and be pardoned." Change "sometimes two" to "some said two." Everything else in this rewrite checks out: canon 77 (`:38592-96`), canon 9 and Moralia LXXIII (`clarke1925:10194-10209`, plus the Benedictine note at `npnf208:35190-95`). It is a real correction of the old text, which ran divorce and widowhood together.

10. **dw.doubt-and-unfinished-growth / text**, NON-BLOCKING.
    New: "That was the struggle of faith." Moralia VIII.1 (`clarke1925:8218`) only says one should not waver. This gloss has no source. The kept sentence "built an entire account of the Christian life on that feeling never fully going away" misstates Nyssa. His endless growth rests on God having no limit, not on a felt sameness.
    Fix: "One of our teachers, Gregory of Nyssa, taught that growth toward God is never finished."

11. **limit.no-stones-to-show / statement**, NON-BLOCKING.
    Kept: "Our own mother is said to have gathered the bones there".
    In the we-voice this gives the Representative a mother (Emmelia), which brushes against the no-invented-family rule.
    Fix: "Basil's mother, Emmelia, is said to have gathered the bones there".

12. **demo.never-settled / exchange[1].text**, NON-BLOCKING.
    New: "our letters give all three reasons".
    The caution-under-the-court reason comes from Gregory's Oration 43.68-69 (`npnf207:~42948-76`), which is an oration, not a letter. The "real reserve" reading is the critics' charge as Gregory reports it in his Ep. 58.
    Fix: "our own writings give all three reasons".

## Changes checked and found sound

- **All six quote renderings are faithful clause by clause** to their `text`. I also checked each `text` against its vendored source: Ep. 16 (`npnf208:24124-45`), canon 4 (`:35030-35`), Longer Rule 7 (`clarke1925:13200-08`), Ep. 226 (`npnf208:39742-52`) and Life of Macrina (`:128`). The "parents"/"bridegroom who was away" wording and the closing "since God the Creator ordained" are now carried in full.
- **Eupsychius as a layman of Caesarea**, not a bishop, is correct in `dw.a-stranger-weather`, `term.martys-martyrion` and `figure.eupsychius`. "Basil's letters invite bishops to his feast" matches Ep. 100 (`npnf208:30450`).
- **The doxology fixes are correct** in the dw, demo and term fields: two forms, "praying with the people," and the charge of "novel and ... mutually contradictory terms" (DSS 1.3).
- **customs-from-the-apostles and unwritten-carries-too** now rest on DSS 27.66: "in a mystery," "the same force," facing east, and the words "in preface and conclusion" (`npnf208:13918-14019`). The old claim that the customs counted as apostolic because they were everywhere is gone.
- **The deathbed in where-was-god and stillness** now matches On the Soul and Resurrection (`npnf205:38089-100`): she let him grieve, then checked him with 1 Thessalonians. The old "no one rebuked him" contradicted that source and is removed.
- **how-it-reached-us**: "lists still differed over a few books at the edge" is supported by Gregory's list and Amphilochius on Revelation (`npnf214:44066-92`).
- **stillness**: Basil's Pontus retreat and Gregory's flight there after a forced ordination match the Oration 2 title and introduction (`npnf207:23578-98`).
- **basileias** "the new city" matches Oration 43.63 (`npnf207:42735`). **valens** tellable_as and bridge_line match 43.52-54 (`:42433`).
- **someone-like-me**: "The rule forbade cooking richer food for a guest" matches Longer Rule 20 (`clarke1925:15104-74`). **hardest-true-thing**: the runaway sentence matches Longer Rule 11 (`:14044`), and the unsupported "Our brotherhoods kept them" is gone.
- **eikon**, **pleonexia**, **psalmodia**, **philanthropia**, **eusebeia** and **agennetos** each drop an overclaim. **askesis** now matches the Gangra canons the record cites (`npnf214:9136`).
- **Honesty preambles are removed**: "So here is what we can show you honestly," "the honest answer is this," "We are not saying sorry," "we say so honestly." So are the coined closers: "the reserve's vindication or its monument," "Last, and first," "kept company," "two things we never settled." So are build or modern-reader words: "A rule we hold ourselves to," "university library," "Historians know us."
- **Tense ruling holds**: "Jesus is God," "Jesus is the Son ... he was the ground," "The Spirit is no lesser presence." The community's past stays in the past tense.
- **"we said he claimed"** now marks Eunomius's knowledge claim as his opponents' report.
- **whose-voice-we-lack and where-record-thinnest**: "Only a few left words of their own" and the Basil-or-Gregory authorship of the letter on the words for God are stated plainly, with no hedging filler.
- **Story tellable_as and figure bridge_line rewrites** are plain, sourced and free of tells. The famine story drops "young." Forty of Sebaste is now "the eastern provinces," not "empire-wide." The Julian story drops its coined closer. Iconium as "within this world's region" matches Doc_01's geographic scope (`Build/worlds/cappadocian/cappadocian_Doc_01_World_Identification.md:34`).