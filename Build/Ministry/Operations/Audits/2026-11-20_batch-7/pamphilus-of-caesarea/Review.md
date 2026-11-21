# Review: Pamphilus of Caesarea

Story: `pamphilus-of-caesarea.brief.txt` (21 lines, 11 paragraphs). Judged against `Brief-Kit/Kit.md`, `Outline.md` (after `Fixes.md` and `Recheck.md`), the approved heart in `../Hearts.md`, and the Decision-Log entries "Batch 6: where sources disagree" and "Change order: the stories approved before the kit…" (2026-11-19) and the four "Batch 7: …" entries of 2026-11-20. Line numbers below are the brief's.

## 1. The test, from one hearing

- **Who:** Pamphilus, a presbyter (one of the elders) of the church at Caesarea in Roman Palestine, who gathered a church library, copied most of Origen's books by hand, and was put to death for his faith about 310.
- **What happened:** he gave his wealth to the poor and his books to readers. He was arrested and tortured in the Great Persecution, worked with Eusebius from prison on a Defense of Origen, and was put to death by the sword with other prisoners. After his death Jerome and Rufinus fought over whether he wrote the Defense.
- **Why the connection matters:** his copies kept Origen's work for later scholars like Jerome, and his name as a martyr gave the Defense its weight in the quarrel over Origen.

None of the three is blank or wrong. Where I got lost: at line 13, "Twelve died, and Pamphilus…" I first heard thirteen deaths. At line 1, "He seems to me…" comes straight after the Croesus gloss, and for a moment "he" could be Croesus. Line 15 carries five moves in 82 words, and Rufinus arrives with no hint of who he is, but it can be followed. Nothing reads as a children's book or talks down.

**My heart, written before reading `Hearts.md`.** Pamphilus, a presbyter of Caesarea, built the church's library around Origen's books, copied most of them himself, and gave Scripture freely to readers. Jailed and tortured in the Great Persecution, he worked with Eusebius on a Defense of Origen and died a martyr about 310. His copies carried Origen's work to Eusebius and Jerome, and his martyr's name made the Defense a weapon, and its authorship a fight, in the quarrel over Origen.

**The approved heart** (Hearts.md; Outline lines 5–11) matches this. Its "Also told" adds the four-voice authorship scene: Eusebius "jointly"; Jerome first for Pamphilus, later for Eusebius; Rufinus "is said"; Photius five books and one.

**Essence timing.** The essence is complete at "He was put to death for his faith about 310." (line 3). That is **word 183** by plain count, about 1:13. The core claim, the Defense from prison with Eusebius, ends at word 174. Both are past about 150. **BLOCKING (B1, below).**

**Also told, present with weight:**
- Inheritance and giving books: present (lines 5, 7).
- The Defense's argument (searched, not decreed): present (line 11), with "only its first book survives, in Rufinus's Latin" (line 15).
- Torture, two years, death with eleven others: present (lines 9, 13). The count is ambiguous (M1).
- Authorship scene: Eusebius, Jerome first and later, Rufinus's answer and the editors are present. **Rufinus's "is said" and Photius's five-and-one are missing (B3).**
- What came of him: the Defense as a weapon is present (line 19). **The library feeding Eusebius's history is missing (B4).** Jerome's use of the library is carried by the opening.

**Order.** After the essence the life runs once, in order: inheritance and books → gift of books → arrest late 307 → the Defense → death 309/310 → the dispute, 392 to about 402 → the weapon → the ending. The essence reaching ahead is allowed. Line 17's back-reference to "jointly" is the one clause the outline asks for. Nothing is told twice and nothing jumps back.

**Ending.** It ends on the person, with the opening's image seen again (outline ending (a)). One phrase in it needs a fix (M3).

**Names.** Pamphilus, Origen, Jerome, Eusebius and Rufinus each act or link. Croesus occurs only inside the quote, with its gloss. No name is heard once without acting or linking.

**Opening.** The name comes in the first sentence. There is no held-back reveal. The opening runs four sentences against the kit's "about three"; B1's fix brings it to three.

## 2. Scores

- **Voice: 4.** A documentary narrator's register. The quotes do work the narrator can't. Lines 5 and 17 read a little like a report on the record, but within bounds.
- **Craft: 3.** Strong frame: the copies "marked with his blood" open and close it. The dispute is told as a scene in time order. But the essence lands late, and the heaviest item in "what came of him" is missing.
- **Rigor: 3.** Most sentences trace cleanly and all three quotes check verbatim. However, two credited voices from the approved heart are missing, one quoted span hides a cut, and "a century dead" is wrong.
- **Accessibility: 4.** Grade 9.0 (7.4 with names out), reading ease 74.2 with names out, 17.9 words a sentence, longest 29. Glosses are worked into the sentence. Origen's full plain sense comes one paragraph late (M2).

**Score run:** `python -m engine.m1.profile_readability …/pamphilus-of-caesarea.brief.txt` gives 592 words, grade 9.0 (names out 7.4), reading ease names out 74.2, 17.9 words a sentence, longest sentence 29 words: pass.

## 3. Verdict: REVISE

Five BLOCKING findings, each with a small fix. With every fix below applied, the story runs about 645–650 words (about 4:20). That stays under the 4:30 ceiling (about 675 words; Mark, 2026-11-20).

## 4. Findings

### BLOCKING

**B1. The essence is complete at word 183, past about 150.** The opening holds all of Quote 1 from "I embrace". That leaves no room for the essence inside the first minute. The outline left room for this: its Openings line allows "from 'I embrace' (or the whole)" while its beat plan puts the opening, the essence and beat 1 at about 150 words.
- Fix (line 1). Delete the whole sentence: `"I embrace and guard them with such joy that I think I own the wealth of Croesus," he wrote, naming a king of old famous for his riches.`
- Then replace `"If it is a joy to have one letter of a martyr, how much more to have so many thousand lines!` with `"If it is a joy to have one letter of a martyr," he wrote, "how much more to have so many thousand lines!`
- Net: −26 words. The essence then ends at about word 157, about 1:03. The quote now starts at a sentence boundary, so no cut is hidden. Croesus drops out, and so does its gloss. The joy and the "many thousand lines" that the ending echoes both stay.
- **Do not say (add to Outline):** Not Quote 1 from "I embrace" in the opening. Begin it at "If it is a joy", so that the essence is complete by about 150 words.

**B2. A quoted span hides a cut (line 7).** Quote 2 runs as one span from "Who among those eager to learn…" to "…whenever need arose." Inside it, the source's second sentence is silently dropped ("If he saw any of them lacking what they needed to live, he gave freely what he could."; JER-L 31257–31258, Outline line 70). The cut also strands the "too" in "He gave the holy Scriptures too". The outline left room for this: line 70 says "The writer may drop the second sentence".
- Fix: after `Who among those eager to learn was not a friend of Pamphilus?` insert ` If he saw any of them lacking what they needed to live, he gave freely what he could.` (+18 words). This is the outline's rendering, word for word.
- **Do not say (add to Outline, replacing line 70's "The writer may drop the second sentence (need of food) but keeps the rest whole"):** Not Quote 2 with its second sentence dropped inside one quoted span. Quote it whole.

**B3. Two voices of the approved authorship scene are missing (lines 15, 17).** The approved heart names Rufinus's "is said" and Photius's "five books and one". The outline still holds both, at beat 6 (lines 54 and 58) and, for Photius, at "Also told" (line 10). Each is a held source that says something different, so each is credited (Mark, 2026-11-19). The story is 83 words under the ceiling, so neither needed to go. Line 15 also runs "About 392" straight into Rufinus's Latin, which came in 397.
- Fix 1 (line 15). Replace `About 392, Jerome listed the Defense under Pamphilus's name, and Rufinus put its first book, all that survives, into Latin.` with `About 392, Jerome listed the Defense under Pamphilus's name. In 397 Rufinus of Aquileia put its first book, all that survives, into Latin as Pamphilus's, though he called it the book Pamphilus "is said to have written".` (+14 words; the quoted words stand at Outline line 54; source JER 45146–45147, "the book which he is said to have written in his defence in Greek", checked).
- Fix 2 (line 17). Replace `Modern editors read it the same way.` with `Five centuries later, a scholar in Constantinople who read all six books said Pamphilus wrote five in prison, working with Eusebius, and Eusebius the sixth alone. Modern editors read it as joint work.` (+26 words; PHOT 11437–11442; "working with Eusebius" keeps the Do not say on Eusebius in prison).
- **Do not say (add to Outline):** Not the authorship scene without Rufinus's "is said to have written" and Photius's five books and one. Both are in the approved heart. Remove "Optional" from beat 6's Photius line, and remove "the Photius clause (beat 6)" from the Length line's cut-first list.

**B4. The heaviest item in "what came of him" is missing.** Outline line 63 ranks it first: the library outlived him, and Eusebius drew on it for his history. The Connection (line 87) says the listener "must be told" how the books passed to "Eusebius and then Jerome". The story gives Jerome's use (line 1) but never says Eusebius worked from the library.
- Fix (line 19). Before `The Defense became a weapon in the quarrel over Origen.` insert `The library outlived him. Eusebius drew much of his history from it, his English editor judged, and Jerome worked from it.` (+21 words; EUS-McG 43017–43020: "to which Eusebius owes a large part of the materials of his history. Jerome also made extensive use of it").
- **Do not say (add to Outline):** Not "what came of him" without its first item. Say that Eusebius drew much of his history from the library, crediting his editor once.

**B5. "A teacher a century dead" is wrong (line 19).** Origen died about 253 (CEN `origen`, "c. 203-253"; Outline line 22). The Defense was written in 307–310, about half a century later. In the quarrel about 400 he was about a century and a half dead. Either way it is not "a century". The outline left room for this at line 64.
- Fix: replace `a teacher a century dead` with `a teacher half a century dead` (+1 word).
- **Do not say (add to Outline, and correct line 64):** Not "a teacher a century dead". Origen died about 253 and the Defense was written about 307–310: "half a century dead".

### MINOR

**M1. The death count can be heard as thirteen (line 13).** Replace `Twelve died, and Pamphilus, their only presbyter, was put to death by the sword.` with `Twelve died in all. Pamphilus, the only presbyter among them, was put to death by the sword.` (+2 words; EUS 47068–47074, "They were twelve in all … Of these the leader and the only one honored with the position of presbyter … was Pamphilus").

**M2. Origen is first heard without his plain sense (line 1).** The gloss arrives in line 3. "His books explaining Scripture" gives a first sense, so this is not blocking. If the reviser wants it at first hearing without lengthening line 1, do both of these:
- At line 1, replace `twenty-five volumes of Origen's commentaries, his books explaining Scripture,` with `twenty-five volumes of commentaries by Origen, the great Bible scholar, his books explaining Scripture,`.
- At line 3, replace `Origen, the great Bible scholar of the century before, had taught there.` with `Origen had taught there in the century before.`

Net about −1 word. Line 1 then runs about 31 words, so this one is optional. If it is not taken, the current text stands.

**M3. The ending adds a cause the outline doesn't hold (line 21).** "Behind the whole quarrel lay the books themselves" tells the listener that the copies underlay the quarrel. The outline's ending (a) asks only for the opening image seen again. Replace `Behind the whole quarrel lay the books themselves,` with `And at Caesarea lay the books themselves,` (−3 words; DVI 75, "quae usque hodie in Caesariensi bibliotheca habentur", JER-L 58489–58490).

**M4. Rufinus's first mention.** The census and the outline's Names list use "Rufinus of Aquileia" at first mention. This is covered if B3 Fix 1 is applied as worded.

**M5. The Defense's addressees are missing (line 11; Outline line 8).** The outline's "Also told" says the Defense was written to Christians condemned to the mines of Palestine. Its weight, the argument, is present, so this is optional. Add it only if the count stays under about 660 after the BLOCKING fixes. After `The Defense speaks of the ideas` the reviser could write: `It was written to Christians sent to forced labor in the mines of Palestine, and it speaks of the ideas` (with the gloss from Outline line 24).

### Length

592 words by the scorer, about 3:57. That is under the 4:00 aim and the 4:30 ceiling, so no cut is needed for length. I asked of each part whether the story needs it. Every paragraph carries the heart, an "also told" part, the record's force (the torture, the death), a credited view, a plain sense or the connection. I list no cuts. B1's trim of Quote 1 is a fix for the essence's timing, not a length cut. With B1–B5 and M1, M3 and M4 applied, the story is about 646 words, about 4:18.

### Sentences

The longest is 29 words (scorer). None runs past 30. B3 Fix 2's Photius sentence is 26 words.

### Words to explain

- presbyter (line 3): given. Matches the outline.
- Origen: given at line 3, one paragraph after first hearing (M2).
- the Great Persecution (line 3): given, without "which began in 303". It says less than the outline's gloss, not more.
- a book defending Origen (line 3): given.
- sacrifice (line 9): given.
- Croesus (line 1): given in the same breath. It drops out under B1.
- commentaries (line 1): given.
- Not used: confessors/mines, the twelve prophets, Arian, heretic. None of the outline's barred words appear.
- No gloss is given on a word a grown listener knows.
- No plain sense says more than the outline's gloss.

### Where held sources differ

- Eusebius and Jerome are each credited on the inheritance and the buying (line 5).
- Jerome is credited on "most of" the copying (line 3).
- 309 or 310 is given as both (line 13).
- "By the sword" follows the outline's permitted wording.
- Eusebius's two statements are set side by side (lines 15, 17). The editors are credited.
- Missing: Rufinus's "is said" and Photius's view (B3).
- One quoted span hides a cut (B2).

## 5. Source check

Every sentence traced to the outline and the source sheet. Quotes were re-checked in `cic/texts/`:

- **Quote 1** (line 1) against the Latin, JER-L 58490–58496 (`jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`): "manu ejus exarata reperi, quae tanto amplector et servo gaudio, ut Croesi opes habere me credam. Si enim laetitia est, unam epistolam habere martyris, quanto magis tot millia versuum, quae mihi videtur sui sanguinis signasse vestigiis". The story's words match the outline's rendering (line 69) word for word, from "I embrace" to the end.
- **Quote 2** (line 7) against JER-L 31256–31264 (same file). Sentences 1, 3, 4 and 5 match the outline's rendering (line 70) word for word. Sentence 2 is dropped inside the span (B2).
- **Quote 3** (line 11) against APOL-L 14211–14215 (`pamphilus_apologia-pro-origene-rufinus-lat_lommatzsch1846.txt`) and APOL-M 42051–42056 (`origen_opera-omnia-t7-pamphilus-apologia-pg17-grc-lat_migne1857.txt`). Both prints agree. The story matches the outline's rendering (line 71) word for word. The lead-in, "the ideas that came to Origen from the Scriptures", is the plain sense of "quae per nimiam discussionem et per multam scrutationem Scripturarum animo disputantis occurrunt" (APOL-L 14208–14210) and is what the outline asks for.
- **"jointly"** (line 11): EUS 36975–36976 (`npnf201_eusebius-church-history-life-of-constantine.xml`), "did the work jointly". Outline line 73.
- **"since they think a martyr praised him"** (line 19): JER-L 31320–31321, "quem putant a martyre praedicatum". Outline line 73.
- No other quoted words appear in the story.

Other claims:
- "About eighty years" is DVI 392/3 against death about 310.
- "Late in 307", the sides scraped, two years: E7, E11.
- The new governor, the refusal, twelve in all, the only presbyter: E11, EUS 47068–47074. See M1 on the count.
- The authorship sequence 392 → about 400 (letter) → Rufinus's answer → Jerome's books against Rufinus: D1, in the outline's corrected order.
- The Life's "nothing but letters to friends": JER-L 31264–31265. It is credited to the Life, not said in the narrator's voice.
- "A teacher a century dead": wrong (B5).
- Do not say list: honored throughout. Eusebius is not put in prison; neither authorship is told as fact; there is no motive for Jerome; "most", not "all"; "about 310" / "309 or 310"; no "burned".
