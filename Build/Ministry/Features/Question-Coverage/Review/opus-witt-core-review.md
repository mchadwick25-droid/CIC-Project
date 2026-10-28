# Opus review: witt.core.witt witness wording (branch claude/witt-witness-wording)

Read-only. File under review: records/witt/world_core/witt.core.witt.md (diff vs origin/main).
Severity: H = blocking (misleads or contradicts at runtime), M = should fix before merge, L = polish.

## 1. Are the claims supported?

### 1525

**What holds.** cic/texts/luther_works-v4-selected_various1931.txt is on this branch (21,818 lines). It holds all three 1525 works in full in the Jacobs translation: the Admonition to Peace (heading at 9566, with the Twelve Articles), Against the Robbing and Murdering Hordes of Peasants (11802; for example "smite, slay, and stab" at 11959), and the Open Letter Concerning the Hard Book (12267). "We hold that writing" is true of the library. "He wrote against the peasants' rising" is true of the Hordes tract.

**F1 (H): "we can tell you what it said and quote it" over-promises at turn time.** thinness, lines 95-96; thin_topics note, lines 149-150 ("quote it from our own volume"); cautions, line 104.
- Retrieval at turn time runs only over the world's compiled records. engine/m1/cross_world.py:979-983 says so: "engine/m4 never opens a file under cic/texts/".
- No quote record cites the 1525 works. records/witt/quote holds seven records, and none cites witt.source.luther-admonition-to-peace or vol. IV. Open_Gaps_Tracking.md, entry "Read-only check of Luther, Philadelphia Edition vols. IV and VI" (2026-10-27), and the change order of the same date both list these quote records as "Not started".
- So the voice is told it can quote a text it has no verified line of. Any "quote" it gives would come from model memory, most likely the Fortress LW 46 wording ("Murderous, Thieving Hordes"), not the Jacobs text. That is the fabricated or unverified quotation CLAUDE.md treats as the gravest failure, and the cautions field itself bars memory-supplied corpus.
- Fix, option (a), recommended: hold the "quote it" clause until Opus-authored quote records for the three works exist and pass the verbatim check. Until then, use: "We hold that writing. We can tell you what it argued. We quote it only where our record gives its own words."
- Fix, option (b): keep the wording, but land the quote records in the same pull request.
- Either way, update the source record (see F11).

**F2 (M): "that writing" is singular, but 1525 was three writings.** thinness, line 95.
- The Admonition to Peace also rebukes the lords, and the Open Letter defends the hard book.
- "We report both as they are" means nothing if only the hard tract is told.
- Fix: "In 1525 he wrote against the peasants' rising, in three writings. We hold all three."

**F3 (M): "volume IV" and "our own volume" in the emic voice.** cautions, line 104; 1525 note, line 150.
- The volume is a 1931 American English translation (Philadelphia Edition, Jacobs). In a 16th-century "we" voice, "volume IV" is apparatus.
- "Our own volume" misstates provenance: it suggests the world's own book.
- cautions and the notes compile into the system prompt, so the Representative can repeat either phrase. engine/prose.py _LOCUS_APPARATUS does not catch "volume IV".
- Fix for cautions: "Where we must speak of 1525, we speak only from the lines of those writings our record holds, and quote only those."
- Fix for the note: "...and quote only the lines our record holds."

### 1543

**F4 (H): "only what our record says of it" sends the voice to a tertiary characterization and labels it "our record".** thinness, lines 96-97; cautions, line 105 ("we say what our record holds"); 1543 note, line 159.
- The only content the records hold for 1543 is the "seven recommended measures". It comes from a Wikipedia article: witt.source.luther-von-den-juden-und-ihren-l (B, named-not-rechecked) and witt.source.wikipedia-on-the-jews-and-their-lies, both "Widely Accepted, not Documented".
- To that, add the later-effect contest (witt.contested.1543-treatise-later-effect, Contested, two-hop).
- In the emic voice, "our record says" will be heard as the world's own 16th-century witness. It is in fact a modern tertiary summary, so the participant is misled about where the claim comes from.
- The text says nothing false, but it hides the remove.
- Fix, recommended: "In 1543 he wrote a treatise against the Jews. We do not hold that treatise. What we know of it comes from later accounts, not its own pages, so we cannot quote it."
- Whether a witness voice may name "later accounts" is a design call for Mark. It ties to the open question in the change order: whether the witness says if the writings were wrong.

**F5 (M): "part of the record we bear witness to" is wrong for 1543.** thinness, lines 94-95.
- The next sentences say the record does not hold the treatise.
- Fix: "Two writings of our founder's are part of the history we bear witness to." The old field said "history", which was correct.

**F6 (M): "We say plainly that the gap is ours."** 1543 note, line 159.
- A non-native reader may take "is ours" as "the fault or blame is ours". That is the owning stance Mark's ruling removed.
- Fix: "We say plainly that we do not have it."

**F7 (L): "We report both as they are" over-reaches for 1543.** thinness, line 97. We cannot report a text we do not hold "as it is".
- Fix: "We report what we can of both. We hide neither and soften neither."
- The two-part "hide neither / soften neither" closer is also slightly slogan-like (mild AI cadence). Acceptable if kept once.

## 2. Did the readability splits keep the meaning?

Compared clause by clause against origin/main. Every claim is kept. Two places lose a connective:

**F8 (L): the contrast is lost in thinness, lines 84-85.** "The Saxon visitation itself was made and exists. It reached us only by reference, not in hand."
- The original was "...exists, but it reached us only by reference".
- Fix: "It reached us, though, only by reference, not in hand."
- "dedicated to them by name. Not one of them speaks" (line 88) also drops "but", but it still reads as a contrast. OK.

**F9 (M): the concessive meaning shifts in cautions, line 107.**
- Original: "...not for us, however tempting it is to borrow her because we have no woman's word of our own."
- New: "It is tempting to borrow her because we have no woman's word of our own." As a free-standing sentence, it now asserts the temptation and loses the "even so, we must not" link. It can also be misparsed as giving a reason to borrow her.
- Fix: "We have no woman's word of our own, and that makes it tempting to borrow hers. We do not."

**Other splits in cautions:** the opening ("The rest of ... corpus" changed to "Our founder's corpus beyond what we actually hold"), the Worms, 'sin boldly' and Genesis items, and the Marburg/Tetrapolitan split ("It is a different, easily confused '1530 confession'") all keep their meaning. No issue.

The other thinness splits (Marburg, the 1580 book, "what we can tell you. We hold no object") keep their meaning. No issue.

## 3. Misleading, softening, defending, inventing; AI tells; non-native misreads

- Misleading: F1, F3, F4, F5.
- Softening or defending: none found. "We do not soften it" and "hide neither" are present.
- Inventing: none in the text itself. F1 creates an invention risk at runtime.
- AI tells: F7, mild.
- Non-native misreads: F6 ("the gap is ours"), F3 ("volume IV").
- "corpus" in cautions (line 99) is Latinate. It is unchanged from main and is not participant-spoken. Leave it.

## 4. Body text in the same file that still states the old rule

**F10a (H): divergence_note, lines 23-31, is now false.** The lines read: ".thinness, .cautions, and .thin_topics below state only that the treatise is real and that its argument is not the Representative's to voice, neither of which depends on or restates the tertiary characterization".
- After this change, the fields point the voice to "what our record holds" of 1543, which is that tertiary characterization.
- Fix: ".thinness, .cautions and .thin_topics below let the Representative say only what the records hold of the treatise. They say it does not hold the text and cannot quote it. Any content it gives rests on that tertiary basis and is not Documented."
- Also add that this record's A / verified-direct rating does not cover the 1525 content either, until quote records exist.

**F10b (H): the LIVING_TRADITIONS body line, line 204, is now false.** It reads: "and the 1543 treatise's existence is disclosed as existence-only in .thinness, .cautions and .thin_topics".
- Fix: "and the 1543 treatise is disclosed in .thinness, .cautions and .thin_topics as what the records hold of it, with the treatise itself not held and never quoted".
- The change order (Open_Gaps_Tracking.md, 2026-10-27) already lists F10a and F10b as left for Mark.

**The living_traditions field (lines 111-119) is consistent.** No change is needed.

## 5. Other files that still state the old rule (file:line)

### Runtime records (compile into the prompt, so they contradict the new core at turn time)

The latest package, the compiled prompt of the witt package pinned at the time, already carries the new core (lines 62 and 66) together with the old guard (line 13) and the old doctrinal witness (lines 755 and 757). That is a live contradiction.

- records/witt/voice_craft/witt.voice.craft.md:37 (guard: "not ours to lay out" for both 1525 and 1543); also 107, 118 and 144-146 (rationale: "existence-only, Facilitator-carried")
- records/witt/doctrinal_witness/witt.dw.what-we-have-never-settled.md:34, 43, 67-70 ("We do not have either text to quote from"), 75, 78, 85, 92
- records/witt/demonstration/witt.demo.record-thinnest.md:61-62, 78
- records/witt/demonstration/witt.demo.who-held-authority.md:53-55 ("structural refusal to voice 1525 content directly")
- records/witt/term/witt.term.insurrection.md:17-19, 36, 69, 76 ("not in our library", "nothing beyond its documented existence"; now factually wrong for 1525)
- records/witt/force/witt.force.popular-insurrectionary-force.md:16, 23-25, 45-60, 69 ("not independently vendored anywhere in this library")
- records/witt/force/witt.force.absent-inputs-1525-and-1555.md:22-25, 42-46, the description's last sentence ("the Representative never speaks it as its own content"), and 58
- records/witt/gravity/witt.gravity.two-governments.md:100, 130, 153 ("outside every text in this library")
- records/witt/contested_claim/witt.contested.1543-treatise-later-effect.md, the concedes field ("content and downstream effect alike are Facilitator-carried disclosure, never Representative-voiced argument")
- records/witt/story/witt.story.return-and-the-eight-sermons.md:34 ("untellable episode"; borderline)
- records/witt/story/witt.story.brussels-martyrs.md:37 (scope only; probably fine)

**F11 (H): the source record contradicts the new core.**
- records/witt/source/witt.source.luther-admonition-to-peace.md, body: "Disclosure only... never quoted as if in hand".
- It now conflicts with the core, and with its own kind: vendored line.
- records/witt/source/witt.source.luther-von-den-juden-und-ihren-l.md (body "Disclosure only... never quoted") is still consistent for "never quoted".

### Canonical build documents (Build/worlds/witt)

- Build/worlds/witt/witt_Representative_Permanent_Prompt_Nikolaus.txt:31 ("not ours to lay out", both)
- Build/worlds/witt/witt_Doc_08_Forces_Document.md:748 (§11 item 7, "Facilitator-carried disclosures")
- Build/worlds/witt/witt_Doc_10_Representative_Construction_Notes_Nikolaus.md:139-141 (State 3, existence only)
- Build/worlds/witt/witt_Doc_02_Source_Ecology.md:269 and §12.3-12.4 (1525 tracts unvendored)
- Build/worlds/witt/witt_Phase7_Encounter_Ecology_Mapping_DRAFT.md:58, 132
- Build/worlds/witt/witt_World_Profile.md §8 (Honest Limits, domain 5; change order at 795)
- Archive/Superseded-Engine-Code/Build/worlds/witt/scripts/wb_witt_s21.py:648, 685, 723, 732; Archive/Superseded-Engine-Code/Build/worlds/witt/scripts/wb_witt_s22_s23.py:2949. These are generator scripts. If they are re-run, they would restore the old wording.

Review rounds and audit files (GoLive, Phase5, Phase7, WorldFront reviews, Doc10_Review_Round1, the Open_Gaps history, BUILD-LOG:26) are a lasting audit trail. Leave them as they are.

### Change order needed
Per CLAUDE.md, the Permanent Prompt, Doc_08 §11 item 7 and Doc_10 State 3 record standing determinations ("content is Facilitator-carried"). Changing them is a governance/methodology change order. It is not a wording edit, so it goes to Mark.
