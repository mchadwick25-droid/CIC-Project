# CiC Demo Conversation Captures V0.1

**Purpose:** Real, unedited screenshot-and-transcript material for the founder to review as raw stock for marketing preview clips. Every exchange below is genuine output from the actual deployed CiC prototype (`cic-poc/`) — real local FastAPI backend, real Claude API calls against the real per-world lexicons/permanent prompts, driven live through the real React chat UI in a headless Chromium browser (Playwright). Nothing here is invented or paraphrased Representative dialogue. Response text is verbatim, copied directly from the rendered page.

**How this was captured:** Backend (`uvicorn app.main:app --reload`) and frontend (`vite`) were started locally per the existing `.claude/launch.json` configs. A local Playwright script drove the real running app in an actual browser: it clicked through the real "Before you begin" onboarding disclosure, selected each world from the real "Choose a Tradition" screen, clicked the real "Begin Conversation with [Representative]" button, typed the exact question below into the real chat input, and waited for the real streaming response to finish before taking screenshots. No API responses were hand-edited.

**Where things live:** Screenshots are saved to `C:\Users\mchad\Documents\CiC-Project\Ministry\Communication\Demo-Captures\`. Each persona has two screenshot files — a `_question` capture (question plus the opening of the reply) and a `_full` capture (scrolled to the end of the reply, showing the closing lines and the citation-count marker `✲ N`). For the three shorter replies, the `_question` capture already contains the entire exchange top to bottom in one frame.

---

## 1. Regular visitor — The House-Churches (Chloe)

- **World / Representative:** The House-Churches, 70–200 CE — Chloe, Host of the Assembly
- **Question asked:** "What was it actually like to be part of your church, day to day?"
- **Screenshot:** `Demo-Captures\01_chloe_house_churches_question.png` (full exchange fits in one frame; `01_chloe_house_churches_full.png` is a redundant duplicate scroll position)
- **Response (verbatim):**

> Ordinary, mostly. On the day named for the sun, we gather under whatever roof will hold us — no building of our own, just a household that opens its door. Someone reads: the words of the prophets, or an account of what the apostles remembered. Whoever presides speaks a while after, urging us toward what we just heard. We stand together and pray. Then bread and wine mixed with water are brought, thanks is given over them, and we eat together — that is the center of the day, the thing everything else circles around.
>
> Before that, though, and after it, there is a great deal of ordinary care. Whoever has something to spare brings it, and it goes to whoever is caring for the widows, the orphans, the sick, the prisoner, the stranger passing through with nowhere else to eat. A catechumen might be sitting with someone that week, learning the Two Ways before coming to the water. A letter might have arrived that needs reading aloud and talking over — what another household somewhere else is facing, whether it matches what we're facing.
>
> So day to day it was not dramatic. It was a rhythm: the gathering, the meal, the care of the ones nobody else was caring for, the letters, the teaching given quietly to whoever needed it next. What is it in particular you're picturing — the gathering itself, or more what it felt like to belong to it?

- **Assessment:** Strong showcase example. Warm, concrete, sensory, exactly the "ordinary daily texture" register a visitor would want. Ends with a genuine reflective question back rather than a canned close. Three inline lexicon citations rendered as underlined terms (prophets, Two Ways, the water) plus a `✲ 5` source-count marker — good visual proof of the sourcing/citation UI for a demo. No caveats.

---

## 2. Pastor or teacher — Syriac Christianity (Mar Yausep)

- **World / Representative:** Syriac Christianity, 200–410 CE — Mar Yausep, Teacher of the Covenant Order
- **Question asked:** "How did your community handle disagreements about who should lead?"
- **Screenshots:** `Demo-Captures\02_mar_yausep_syriac_question.png` (question + first ~90% of reply) and `02_mar_yausep_syriac_full.png` (scrolled to the closing lines + `✲ 3` marker)
- **Response (verbatim):**

> We do not have one answer to that, because our own life did not give us one settled way of resolving it. Our own account of our beginning already carries the trouble inside it. Addai came to Edessa and appointed Aggai to follow him. Aggai was struck down before he could ordain anyone after himself — killed for refusing to make ceremonial hats demanded of him by a rival claimant to authority. It fell to Palut to travel to Antioch and be ordained there by Serapion, so that our own succession was secured only by reaching outward, not by anything settled at home. Even in the story we tell of our own founding, the line does not hold itself up from within.
>
> That pattern did not stay in the story. Among the Persian churches, Papa bar Aggai claimed primacy over the other bishops of his own time, and Miles of Susa and Aqib-Alaha of Karka d'Baith Slok did not accept that claim quietly. It was contested, openly, by men who held real sees of their own. And on our own side, after Barba'shmin was killed, the seat he held stood empty for twenty years. Nobody filled it. Our own community's life did not stop for that — the teaching continued, the vow was kept, the fast and the vigil went on — but the seat itself stood empty the whole time, and we do not pretend that emptiness was somehow already resolved.
>
> So when disagreement over leadership came, it was not settled by one clear channel outranking the others. A bishop's claim, a martyr's memory, a teacher's word received without ordination behind it, a vow kept among kin — none of these ever cleanly ruled the rest across the whole of our life. What holds our people together, more often than not, has been the vow kept daily and the teaching received as sound, standing in for what an office could not always secure on its own.

- **Assessment:** Strong showcase example — exactly the kind of specific, named, historically load-bearing answer a pastor/teacher persona would want, and refreshingly honest that the tradition never fully resolved the question rather than offering a tidy institutional answer. One minor, unrelated cosmetic caveat: the Facilitator's own introduction line rendered literal double-asterisks — "Please welcome **Mar Yausep**, a teacher and elder..." — instead of bold text. That's a small Markdown-rendering bug in the Facilitator's intro copy, not in Mar Yausep's actual answer, but worth a screenshot-crop decision if this exchange is used in a video (crop below the intro, or have someone check the intro-message renderer).

---

## 3. Academic or scholar — Alexandria (Theon)

- **World / Representative:** Alexandrian Christianity, c. 150–400 CE — Theon, Catechetical Teacher
- **Question asked:** "What's the actual evidence for how confident we can be about that practice? How sure are you, really?"
- **Screenshot:** `Demo-Captures\03_theon_alexandria_question.png` (full exchange fits in one frame)
- **Response (verbatim):**

> We told you the shape a formation likely took, not one seeker's counted days. That is worth holding apart plainly, because the two are not equally sure.
>
> The stages themselves — coming first as one still under instruction, the waiting before the water, the illumination baptism itself is named to be, the deepening afterward that never counts itself finished — these we hold with real confidence, because they are not inference. They are the pattern our own life set down and still keeps: the great fast, the feast that follows it, the daily return to a Scripture never read once and shelved. That rhythm is not reconstructed. It is what we do.
>
> What we cannot give you is one particular soul walking it — a name, a morning, a specific word said to a specific catechumen on a specific day. When we spoke of "a typical formation," that was offered honestly as the shape many lives probably shared, not as any single life we can point to and say: this happened, here, to this one. Where the pattern is concerned, our confidence is real. Where a particular soul's road through it is concerned, we have the outline and not the portrait — and we would rather tell you that plainly than paint a face onto it that was never there.

- **Assessment:** Strong showcase example — this is the single best of the four for demonstrating the project's anti-fabrication ethos on camera. Theon draws an explicit, unprompted line between "the pattern" (high confidence, lived/repeated practice) and "the particular soul" (no invented specifics), which is precisely the scholarly-rigor claim CiC needs to visibly earn. One framing caveat: because this was the opening question in the session (no prior turn actually described "that practice"), Theon's answer necessarily speaks to a generic/implied prior claim rather than a specific one — still coherent and in-character, but if used in a video, consider pairing it with a preceding question (e.g., "What did a typical catechetical formation look like?") so "that practice" has a visible referent on screen.

---

## 4. Reevaluation — The Desert (Papnoute)

- **World / Representative:** Desert Fathers and Mothers, c. 320–430 CE — Papnoute, Elder of the Desert
- **Question asked:** "Honestly, I'm not sure I believe any of this anymore. Why did you?"
- **Screenshot:** `Demo-Captures\04_papnoute_desert_question.png` (full exchange fits in one frame)
- **Response (verbatim):**

> We did not believe first and then act. Antony heard the Gospel read aloud in the assembly one ordinary day, and took it as spoken to him, not to whoever else happened to be sitting there. He went out on that alone, before anything was proven to him.
>
> So I would not ask you to believe the way you think belief works. I would ask: what has gone quiet in you — the word itself, or the ear that used to hear it?

- **Assessment:** Strong showcase example. No refusal, no safety-redirect, no generic "I hear you" therapy-speak — it answers from within the world's own concrete story (Antony) and turns the doubt back as a real, specific, non-preachy question. Notably restrained (short, two paragraphs) rather than padded, which reads as more genuine, not less. No caveats.

---

## Overall notes for the founder

- All four exchanges are usable as-is; none required a rephrase or fallback attempt.
- The `✲ N` citation-count marker and the underlined inline lexicon-term links (visible in captures 1 and 3) are worth keeping in frame for at least one clip — they're the most concrete on-screen proof of "this is sourced, not improvised."
- The one bug worth a ticket: the Facilitator's world-introduction message for Mar Yausep (Syriac Christianity) rendered raw Markdown bold syntax (`**Mar Yausep**`) instead of bold text — cosmetic only, does not affect the Representative's own answer, but would look sloppy if that portion of the screen is in a video crop.
- Every screenshot was produced by actually driving the real local app end to end (onboarding → world selection → live chat → real streamed Claude response); no dialogue was hand-written or adjusted after the fact.
