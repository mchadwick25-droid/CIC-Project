# 03 — Trust and honest-sourcing presentation

**How credible sites and products make sourcing, provenance, and admitted limits a reason to trust them — and what CiC can adapt.**

| | |
|---|---|
| Workstream | Website V2 (`Build/Ministry/Features/Website-V2/`) |
| Type | Research brief — input to D2/D3. Records findings and recommendations; **decides nothing.** |
| Date | 2026-09-08 |
| Prepared by | Fable (deep research, per the model-routing ruling of 2026-09-01) |
| Method | Live web research (search + page reads), September 2026. See §8 for limits: many primary sites were unreachable through the session's egress proxy, so a number of quotations below are carried through search-index excerpts or secondary coverage and are flagged as such. |

---

## 0. The question, and what the record already settles

**The question.** CiC's deepest design commitment — a Representative voice that never invents a source, quote, or detail, says plainly what it does not know, and traces every claim to a real named source — currently reaches the visitor as one line of disclosure: *"You will be in conversation with a representative voice, not a person who lived — built from one tradition's own letters and records, and honest about where they run out"* (storyboard 1.3d′; the same sentence heads every tradition page). Mark wants that honesty to become a **draw** — the reason a skeptical visitor, whose first reaction to any AI voice is reasonably *"is this just another slop generator?"*, decides to trust this one.

**What is already ruled, and binds this brief.** The Decision-Log and storyboard settle four things this research must respect rather than reopen:

1. **The door comes before the mechanism.** Direction 03 ("Institutional" — method, confidence scale, sourcing shown *before* anyone is invited to begin) was named by its own author as the most attackable direction, and the constitution's S0 puts the door first (Decision-Log, Directions list).
2. **Tradition pages stay short.** The "record behind the voice" finding aid — sources table, gravities, confidence legend, contested list, review status — was cut from both shipped tradition pages ("cutting everything past what interests, orients, and engages"; Chloe's page 628 → 272 lines). That depth "lives in the record store and, if ever wanted, in About's 'how it works,' not repeated on every tradition page" (storyboard, tradition-page order).
3. **The disclosure line keeps its position** — ahead of any conversation link, on every surface — but its wording moved from mechanism ("an AI system," "shows its sources as it speaks") to the world being represented ("a representative voice, not a person who lived"), because the earlier wording "led every page with the mechanism instead of the world" (Design V2 §3.7 item 8, change order 2026-09-03).
4. **The homepage sample exchange and disclosure grid were cut** as "explanation about the experience, not the experience" (storyboard §1.4/1.5 removal note).

So the brief's real question is narrower and harder than "how do you present sourcing": **how does honesty become visible and persuasive *inside* a short, warm, story-led page — without a record section, without leading with the mechanism, and without a caveat?** The research below turns out to answer exactly that, and to support those four rulings rather than strain against them.

---

## 1. The cross-cutting findings (read this section if nothing else)

Five things held across every category.

**F1. Transparency that lives in a box is not seen.** The most sobering finding in the whole pass: when three McClatchy newspapers added a *"Why did we report this story?"* box to stories, a Center for Media Engagement survey of 321 readers found most did not notice it at all, and it did not significantly change trust in the story. Only **33.7%** remembered the box when it was embedded in the story text, and **21.2%** when it sat at the bottom of the page (Nieman Lab, 2020, reporting the CME study). Nieman's headline said it plainly: *"readers have to find your transparency first."* Transparency has to be **placed where the eye already is**, in the flow, or it might as well not exist. This is direct evidence for ruling 2 above — and a warning that a disclosure line at the foot of a section is functionally invisible.

**F2. The strongest trust-builders show the evidence, not a statement about the evidence.** The New York Times Visual Investigations team's own description of its method is that *"the audience is seeing the evidence for themselves"*; its co-founder Malachy Browne: *"There is an incredible amount of documentary evidence hiding in plain sight … When you gather and analyze it, you can answer key journalistic questions like when and where did an event happen, who was involved, what happened and how."* Bellingcat used pictures or video to support its analysis in **97.9%** of its content, "to walk the reader slowly through the logic." BBC Verify's launch rationale from BBC News CEO Deborah Turness: audiences want *"not just what the BBC knows, but how it knows it"* — delivered as a *"how we verified this"* button under images that expands into the steps taken. Google's NotebookLM: click any citation and *"the exact passage where that information came from is highlighted."* In every case the credibility comes from **the source being one gesture away**, not from a sentence asserting that sources exist.

**F3. The most convincing honesty is spoken *in the voice*, not in the chrome.** The Holocaust-survivor installations (USC Shoah Foundation's *Dimensions in Testimony*) answer an unmatched question with the survivor's own recorded line, *"I'm afraid I cannot answer that question."* The Dalí Museum's *Ask Dalí* has the AI Dalí explain himself in character: *"they used something called a large language model in a recreation of my voice, and here I am."* The NET Bible sells its 60,000 notes as letting you *"look over the translators' shoulders."* A limit stated by the speaker, in the speaker's own register, reads as **integrity**; the same limit in a footer reads as **liability**.

**F4. Constraint-as-promise beats capability-as-promise.** The products and exhibits that are actually praised for honesty all lead with what they *only* do: NotebookLM is *"grounded in your documents, not the whole internet"* — *"if information isn't in your uploaded sources, it won't claim it."* Magisterium AI *"learns exclusively from a meticulously curated database"* of 23,000 Church documents. The National WWII Museum's *Voices from the Front* promises *"authentic and unaltered answers in each interviewee's own words and voice."* Dimensions in Testimony: *"The answers are not artificially generated … They do not alter, edit or manipulate answers."* The constraint **is** the pitch. And the cautionary tail is just as consistent: the promise must be true, or it curdles. Columbia Journalism Review's 2025 audit found Perplexity wrong on 37% of a citation task despite its source-first interface; critics of Magisterium AI note its "accurate answers" claim *"is only valid with considerable qualification"* because hallucination is intrinsic to the underlying model; Google's AI Overviews (glue on pizza) showed how fast confident wrongness destroys a trust asset.

**F5. Confidence language works as a small, fixed, explained vocabulary — and fails as a bare number.** Sherman Kent's CIA study found the same phrase ("serious possibility") read as 20% by some policymakers and 80% by others; a 2015 Reddit recreation found perceptions have barely moved. The systems that work — IPCC's calibrated terms (*very likely* = 90–100%), GRADE's four-circle certainty symbols (⊕⊕⊕⊕ / ⊕⊕⊕○ / ⊕⊕○○ / ⊕○○○), Gwern's eight Kesselman words (*certain · highly likely · likely · possible · unlikely · highly unlikely · remote · impossible*) — share three properties: **few terms, defined once, used identically everywhere.** The systems that mislead — the Consensus Meter's "41% yes" that hid the fact that every tier-one study was negative; the hurricane cone's "containment effect" (people outside the cone assume they are safe) — present a number or a shape that *looks* precise while dropping the quality of the evidence behind it.

---

## 2. Category 1 — Historical archives and museum digital exhibits

### 2.1 Museum provenance narratives: a grammar in which gaps are data

Major art museums (the Met, Philadelphia, Oberlin, NCMA, the Art Institute of Chicago and others) publish object provenance in a shared convention, codified by the American Alliance of Museums. It is worth quoting the rules because the *format itself* is the honesty:

- Provenance is listed chronologically from the earliest known owner; owners' life dates sit in **brackets**; dealers and auction houses sit in **parentheses**.
- A **semicolon** means the work passed directly between two owners; a **period** means a direct transfer did not occur, or *is not known to have occurred*.
- Uncertain information is flagged with **"possibly"** or **"probably"** and explained in a footnote.
- The museum documents the source for each owner or transaction, and *"in publishing provenance information, the museum should include an explanation of its format."*

**Pattern:** a tiny, consistent typographic grammar in which *a gap is a visible mark* (the period, the "probably"), plus a one-time explanation of the grammar. **Why it builds trust:** the reader is never asked to take the museum's word that the record is complete; the punctuation shows exactly where it isn't. It is also quiet — no warning boxes, no red text — and reads as scholarly care rather than defensiveness. (Note: the Met's and British Museum's own object pages were unreachable in this pass; the conventions are quoted from the AAM guide as republished by Krannert Art Museum and the Met's provenance-research resources page.)

### 2.2 Cooper Hewitt's collection notice: plain admission plus an open door

The landing page of the Smithsonian's Cooper Hewitt collection site tells the visitor that cataloguing 215,000+ objects *"is a work in progress, and users may encounter records with very little information, factual errors, or harmful language,"* and invites feedback. **Pattern:** a plain-language admission in the institution's own voice, at the front door, paired with a way to respond. **Why it builds trust:** it says the quiet part before the visitor finds it, in ordinary words, and it frames the visitor as a collaborator rather than a consumer. The tone is a person talking, not a policy.

### 2.3 Papyri.info and the Leiden conventions: the gap is typeset

Papyrologists have a century-old convention for showing what they cannot read, and papyri.info renders it on screen: square brackets `[ ]` for text lost to damage, with dots inside equal to the estimated number of missing letters; letters inside brackets for a scholar's *restoration* (i.e., an educated guess, visibly marked as one); a **dot under a letter** for an uncertain reading. In the digital edition each mark is real data (`<gap reason="lost" quantity="5" unit="character"/>`, `<unclear>`), and each edition carries its editorial history. **Pattern:** uncertainty and absence are *first-class typographic objects*, not prose apologies. **Why it builds trust:** a fragment full of brackets is, paradoxically, more convincing than a clean text — the reader can see the scholar refused to paper over the hole. This is the closest analogue anywhere to CiC's "where the record is quiet."

### 2.4 Sefaria: click any line, see everything that touches it

Sefaria's reading interface makes sourcing a gesture: click any passage and a side panel (the "Resource Panel") opens with **Related Texts** grouped by category — Commentary, Talmud, Midrash and so on — because *"all texts are linked to each other."* Every text sits beside its original language. Reviewers note the effect: it *"allows users to verify citations and read surrounding context themselves instead of trusting secondary sources."* **Pattern:** in-place, categorized, click-to-reveal connections, with the primary text always one step away. **Why it builds trust:** the site never asks to be believed; it keeps handing you the original.

### 2.5 The NET Bible: transparency as the entire product

The New English Translation's identity *is* its 60,000 translator and text-critical notes, which *"bring complete transparency to every major translation decision and invite you to look over the translators' shoulders."* The stated motive was accountability: every working draft was published online and *"Bible scholars, ministers, and laypersons from around the world logged millions of review sessions"* — *"not to achieve a consensus translation, but to be accountable, to be transparent."* Text-critical notes flag where manuscripts disagree. **Pattern:** the apparatus is not hidden behind the text; it is the reason to choose this text. **Why it builds trust:** for a religious audience specifically — CiC's audience — visible textual honesty is already a recognized virtue, not a strange scholarly habit. The NET Bible proves the market exists.

---

## 3. Category 2 — Investigative journalism: sourcing as part of the reading experience

### 3.1 ProPublica: the methodology note, the editor's note, and the invitation to criticize

ProPublica routinely publishes a separate *"How We Reported This Story"* piece alongside major investigations, and — more unusually — explains its reasoning in editor's notes. Nieman Reports describes the 2015 Surgeon Scorecard: a searchable database, *"a detailed discussion of its methodology,"* an editor's note from Stephen Engelberg on the reasoning, and at the end *"Engelberg invited criticism from readers with a dedicated email address,"* with ProPublica making a habit of responding publicly to critics. It has also published *"reporting recipes"* so others can replicate stories. **Pattern:** method + reasoning + a named door for disagreement. **Why it builds trust:** inviting criticism signals the work can withstand it. **Caveat (F1):** as a separate page it is read by the committed, not the passing visitor — which is why the best ProPublica pieces also weave sourcing into the article body.

### 3.2 The Trust Project: eight disclosures, like a nutrition label

Adopted by 120+ news sites (after a design sprint hosted by The Washington Post and a Design Day with the Society for News Design), the Trust Indicators are eight standardized disclosures: **Best Practices** (mission, ethics), **Author Expertise**, **Type of Work** (news / opinion / analysis labels), **Citations and References**, **Methods** ("a behind-the-scenes look at the why and how"), **Locally Sourced**, **Diverse Voices**, **Actionable Feedback**. They are explicitly described as *"like nutritional labels."* Measured effects: trust in *The Mirror* rose 8% after adding them; UT-Austin's Center for Media Engagement found higher reputation evaluations when the indicators were present; 59% of participants said a "Behind the Story" section would increase trust. **Pattern:** a small fixed set of labels, always in the same place, so a reader learns them once. **Why it builds trust:** consistency — the reader stops evaluating each article from scratch.

### 3.3 The box nobody saw (the caution that governs everything above)

Covered in F1; repeated here because it sits squarely in this category. Three newspapers, 321 readers, a "Why did we report this story?" box: 33.7% noticed it in-text, 21.2% at page bottom, no significant trust effect. The lesson is not "don't explain"; it is **"explanation only works where attention already is."**

### 3.4 NYT Visual Investigations: annotated evidence in the body

Rather than a reporter asserting a conclusion, the Times's visual investigations present *"small clips with annotations on them"* — timestamps, circled objects, geolocation overlays — so that *"the audience is seeing the evidence for themselves."* The work is *"very evidentiary in nature."* **Pattern:** the source *is* the content; annotation replaces assertion. **Why it builds trust:** the reader performs the verification, and a performed verification is remembered where a promised one is not.

### 3.5 Bellingcat: show every step, archive every link

A study of Bellingcat's 2014–2020 output found pictures or video supporting the analysis in 97.9% of pieces; researchers archive source pages (archive.org, archive.today) so evidence remains checkable years later — which is how its open-source evidence was upheld in the European Court of Human Rights. **Pattern:** evidence inline, links preserved, chain of custody visible. **Why it builds trust:** nothing depends on the reader's faith in the author.

### 3.6 BBC Verify: the "how we verified this" button

Launched 2023 after audience research that *"amid disinformation and sensationalism, they need to see the BBC's workings to maintain trust."* Turness: *"At BBC News we know that trust is earned."* The on-page expression is a single affordance — a *"how we verified this"* button beneath an image or video that reveals the verification steps. **Pattern:** one small, consistently placed control that opens the method on demand. **Why it builds trust:** it costs the uninterested reader nothing and gives the skeptic exactly what they came for. This is the cleanest model for CiC's "one link to the record" compromise.

### 3.7 Sidenotes: citations in the margin, not the basement

Tufte's argument, implemented in Tufte CSS and on Gwern.net: footnotes force the reader to *"jump to the bottom of the page, lose context, and find the way back,"* whereas sidenotes *"let the reader instantly read them without needing to refer back and forth,"* providing *"citation metadata for the reader in context."* On narrow viewports the notes collapse until toggled. **Pattern:** the citation sits beside the sentence it supports. **Why it builds trust:** the source is *present* rather than *referenced*.

### 3.8 Fact-checker scales: a vocabulary that includes "we couldn't tell"

The Washington Post's Fact Checker uses one to four Pinocchios, a **Geppetto Checkmark** for the fully true, an upside-down Pinocchio for flip-flops, and — the detail that matters here — a **scales-of-justice symbol** *"for claims that are too difficult to verify or require more time and/or data."* PolitiFact's Truth-O-Meter works the same way. **Pattern:** a small pictorial scale that has an honest symbol for *unverifiable*. **Why it builds trust:** admitting "we don't know" is a rating, not a failure.

### 3.9 The Conversation: one uniform disclosure line, every article

Every article on The Conversation carries a **Disclosure statement** naming the academic author's funding and affiliations, *"consistent with standards in academic publishing,"* and the site states this is *"designed to protect and foster the bond of trust between The Conversation and readers."* **Pattern:** short, identical in form, always in the same place, never skipped. **Why it builds trust:** a disclosure that appears every time reads as a habit of the house; one that appears only sometimes reads as damage control.

---

## 4. Category 3 — AI products honest about their limits

**The honest headline first.** Genuine examples of an AI product's *interface or marketing* turning "here's what this can't do" into a trust feature are **rare**. The overwhelming industry pattern is the footer disclaimer — *"ChatGPT can make mistakes. Check important info."* — which a CHI 2026 workshop paper (*"Can Make Mistakes": AI Chatbot Disclaimers as Failed Explainability Surfaces*) characterizes as *"vague, unactionable, and inconsistent with actual system behavior"*: a neglected surface that nonetheless shapes users' mental model of what kind of epistemic agent the system is. That footer is, structurally, exactly what CiC's current one-liner is at risk of becoming. The exceptions below are real, and they share one move: **the limitation is the product's identity, not its caveat.** Notably, the two strongest examples are museum projects about *real recorded humans*, where "nothing is generated" is literally true — which is both the model to learn from and the bar CiC cannot fully meet (see §4.11).

### 4.1 Dimensions in Testimony (USC Shoah Foundation) — the constraint *is* the promise

Visitors ask a Holocaust survivor questions aloud and receive real-time video replies. Every partner museum's description leads with the constraint: *"The answers are not artificially generated — all their actions, such as answers and movements, are pre-recorded"*; *"They do not alter, edit or manipulate answers"*; survivors *"in their own words."* Each survivor recorded answers to roughly 1,500 questions (Pinchas Gutter's figure). When no recorded answer matches, the survivor's own recorded line plays: *"I'm afraid I cannot answer that question."* **Pattern:** (1) the "can't" stated up front as the source of authenticity; (2) the refusal delivered *in the person's own voice*, as part of the experience; (3) a concrete number (1,500 questions) standing in for an abstract claim of thoroughness. **Why it builds trust:** the visitor learns that a refusal is proof the system is doing what it promised, and comes to *want* the refusal. No AI-generated voice can claim "not generated," but the three-part pattern transfers wholesale.

### 4.2 Voices from the Front (National WWII Museum / StoryFile) — "authentic and unaltered"

Same architecture, framed the same way: *"authentic and unaltered answers in each interviewee's own words and voice"*; each participant answered up to 1,000 questions; AI is named only as the matching layer (*"voice recognition to match visitor inquiries with the most relevant video responses"*). **Pattern:** AI's role is named precisely and narrowly. **Why it builds trust:** saying exactly what the AI does is more credible than saying it is "safe."

### 4.3 Ask Dalí (Salvador Dalí Museum, 2024) — in-character disclosure, and its critics

A generative voice (GPT-4 plus ElevenLabs, trained on Dalí's writings — *Diary of a Genius*, *The Secret Life* — and archival interviews) answers questions through a lobster telephone. Two design choices matter. First, the disclosure happens **in character**: the AI Dalí tells visitors *"they used something called a large language model in a recreation of my voice, and here I am."* Second, the museum's framing is *entry*, not oracle — director Hank Hine: *"we have a commitment to find ways for our visitors to find delight and special kind of entry into Dalí's spirit"* — and coverage notes *"just about all of the AI artist's 'words' were at some point spoken by Dalí himself."* The critical response is instructive: ARTnews framed both Ask Dalí and the Musée d'Orsay's *Hello Vincent* as *"ventriloquizing the dead"* and asked whether *"being the custodian of a collection permit[s] stewardship of a soul."* Hello Vincent (trained on ~900 letters) was reportedly re-tuned after so many visitors asked Van Gogh why he killed himself that the program now *"steers the conversation in life-affirming directions."* **Pattern:** the voice names its own nature, warmly, once. **Why it builds trust, and where it fails:** in-character honesty is disarming; but because the voice is *generatively free*, critics reasonably worry it will say things the person never said — and the Van Gogh retuning proves it. CiC's source-tracing discipline is precisely the answer to that objection, which is why it deserves to be foregrounded.

### 4.4 Google NotebookLM — "grounded in your sources," click-to-passage

The product's identity is its restriction: *"grounded in your documents, not the whole internet."* Every answer carries inline numbered citations; clicking one opens the source panel with *"the exact passage where that information came from … highlighted."* Coverage stresses the honesty behaviour: *"if information isn't in your uploaded sources, it won't claim it."* (One secondary source reports ~13% response-level hallucination in journalistic tests versus ~40% for ungrounded LLMs; unverified in this pass and cited only as reported.) **Pattern:** sources strip + numbered inline cites + click-to-highlighted-passage. **Why it builds trust:** verification is one click and lands on the *actual words*, not a title.

### 4.5 Magisterium AI — "learns exclusively from," with the qualification critics demand

Catholic answer engine: *"learns exclusively from a meticulously curated database of authoritative Catholic sources — over 23,000 official Magisterial documents,"* with *"verifiable citations linking to source documents."* Its own FAQ (via Hallow) concedes that *"any generative AI system can 'hallucinate' … users should always consult the original documents."* Critics (Public Discourse, *"Beware of Catholic AI"*) argue the "accurate answers" claim *"is only valid with considerable qualification"* and raise deeper concerns about outsourcing faith to a chatbot. **Pattern:** closed corpus + document-linked citations. **Why it builds trust — and the lesson:** the closed corpus is a genuine differentiator, but the honest version of the promise must say what remains possible (misreading a real source), not only what is excluded (inventing one). CiC's stronger position is that its voice is built to *say* when it doesn't know; that behaviour, shown, is worth more than any corpus claim.

### 4.6 Elicit — a "supporting quote" behind every cell, and "not mentioned" as an honest value

Elicit's extraction tables back *"all information … with supporting quotes from the underlying papers,"* expose a *"Reasoning for …"* field, and return *"not reported / not explicitly mentioned"* when a paper is silent. Independent evaluations still caught occasional hallucinations (e.g., detecting a conflict-of-interest statement that was absent). **Pattern:** every claim has its quote attached; silence is a legitimate answer. **Why it builds trust:** "not mentioned" as a first-class output teaches users that the tool would rather say nothing than guess.

### 4.7 iA Writer 7 — AI text visibly marked

The Authorship feature lets a writer mark passages as AI-written; they render dimmed/greyed (or with a gradient) until edited, entirely locally. iA's stated principle: *"the less we can trust what we read, the more we need to know who wrote it."* **Pattern:** provenance carried by the typography of the text itself. **Why it builds trust:** the reader can see, not be told, what is whose.

### 4.8 Anthropic publishing Claude's system prompts

Since August 2024 Anthropic has published and logged changes to the system prompts that govern Claude.ai, a move VentureBeat reported as *"winning praise for transparency"* and that developers noted *"stands out among other AI companies."* **Pattern:** the operating instructions are public and versioned. **Why it builds trust:** mechanism disclosed voluntarily, before anyone demanded it. (Relevant to CiC's About page, not its tradition pages, per ruling 3.)

### 4.9 Content Credentials (C2PA) — provenance as a small pin

The cross-industry standard backed by Adobe, Microsoft, Google, the BBC, AP, Leica and Nikon marks media with a minimalist **"CR" pin icon** whose design brief required that it *"conveyed trust, indicated the presence of more information, [and] could be immediately and universally understood."* Clicking reveals a tamper-evident history of how the image was made. **Pattern:** a tiny, consistent glyph that expands into the full provenance. **Why it builds trust:** it makes provenance *ambient* — present on everything, demanding nothing.

### 4.10 Contrast cases — what buried or false honesty looks like

- **"Can make mistakes" footers** (ChatGPT, Claude, Gemini): ubiquitous, unread, and *"inconsistent with actual system behavior"* (CHI 2026 workshop paper). The pattern CiC's single line must not resemble.
- **Character.AI**: added *"the AI is not a real person"* to every chat only in October 2024, after a teenager's death — honesty arriving as remediation, which reads as such.
- **Historical Figures app (2023)**: let users chat with Hitler and Goebbels; NBC found *"contradictory responses invented by the software, which doesn't profess to use real quotations or citations"* — including a Hitler bot calling the Holocaust *"a terrible mistake."* The exact failure CiC is built to prevent, and the exact thing a skeptical visitor fears.
- **Google AI Overviews (May 2024)**: *"add about 1/8 cup of non-toxic glue to the sauce"* — an 11-year-old Reddit joke delivered with full confidence; MIT Technology Review's diagnosis was that the system *"can't tell jokes from facts — and can invent confident-sounding answers."*
- **Perplexity**: a source-first interface that CJR's 2025 audit still found wrong on 37% of a citation task, with failure modes of *misattribution* (right fact, wrong source) and *fabrication*. A citations UI is not the same as honesty; the discipline behind it is.

### 4.11 The gap CiC has to be honest about

Every fully convincing example above is either (a) a real recorded person (Dimensions in Testimony, Voices from the Front), where "not generated" is literally true, or (b) a document-retrieval tool (NotebookLM, Elicit), where "grounded" is mechanically enforced. CiC is a third thing: a *generated* voice that is *disciplined* to source. The honesty framing therefore has to do two jobs at once — say what the voice is built from (like NotebookLM) **and** say what it does when the sources run out (like the survivor's *"I cannot answer that"*). The current line already gestures at both ("built from … letters and records, and honest about where they run out"); the recommendations in §6 are about making both *visible*.

---

## 5. Category 4 — Visual and verbal language for confidence

### 5.1 Sherman Kent's words of estimative probability — and why words alone drift

Kent (CIA, 1964) found that *"serious possibility"* in a 1951 estimate of a Soviet attack was read as a 20% chance by some policymakers and 80% by others, and that *"probable"* ranged from 30% to 75% between readers. His fix was a fixed table — *certain* 100%, *almost certain* 93% (±6), *probable* 75% (±12), *chances about even* 50% (±10), *probably not* 30%, *almost certainly not* 7%, *impossible* 0%. A 2015 Reddit recreation by zonination (an Information is Beautiful award winner) found *"perceptions … have changed very little since the studies in the 1950s"* — the spread is still wide. **Lesson:** a confidence word only communicates if it is defined once and used consistently; ad-hoc hedging ("fairly likely," "some suggest") communicates almost nothing.

### 5.2 IPCC calibrated language

*Virtually certain* (99–100%), *very likely* (90–100%), *likely* (66–100%), *about as likely as not* (33–66%), *unlikely* (0–33%), *very unlikely* (0–10%), *exceptionally unlikely* (0–1%), with confidence expressed separately (low/medium/high/very high) and italicized in the text. Used across the IPCC, USGCRP and NRC for thirty years. **Pattern:** the confidence word is *typographically marked* (italic) inside ordinary prose, so the reader sees it is a term of art. **Why it works:** it lives in the sentence, not in a sidebar.

### 5.3 GRADE certainty of evidence

Cochrane and clinical guidelines rate evidence *high / moderate / low / very low* and print it as four circles: ⊕⊕⊕⊕, ⊕⊕⊕○, ⊕⊕○○, ⊕○○○. **Pattern:** a four-step glyph readable in a glance, no number. **Why it works:** it communicates *ordinal* strength honestly without implying false precision — the opposite of a percentage.

### 5.4 Gwern's confidence and importance tags; Maggie Appleton's growth stages

Every Gwern.net essay opens with metadata: a **confidence** tag drawn from the Kesselman list — *certain · highly likely · likely · possible · unlikely · highly unlikely · remote · impossible* — an **importance** rating, and a **status** (notes / draft / in progress / finished). Readers on Hacker News called the belief tags something they *"absolutely love."* Maggie Appleton's digital garden marks every note *seedling / budding / evergreen* and argues for **"epistemic disclosure"**: telling readers *"how seriously to take content"* is *"what makes it safe to publish something imperfect."* **Pattern:** a one-line epistemic header, fixed vocabulary, on every piece. **Why it builds trust:** it signals the author has *thought about* how sure they are, which is more reassuring than certainty.

### 5.5 scite Smart Citations — supporting / mentioning / contrasting

scite classifies each citing sentence and shows a badge: a checkmark-in-circle for **supporting**, a dash-in-circle for **mentioning**, a question-mark-in-circle for **contrasting**, with counts, and the citing sentence shown in context. **Pattern:** three glyphs plus the quoted context. **Why it builds trust:** it shows *disagreement* as information rather than hiding it — a claim with visible contrasting citations feels more honestly presented than one with none.

### 5.6 The Consensus Meter — and the critique that defines the failure mode

Consensus.app answers yes/no questions with a meter: share of the top 20 papers saying *yes / no / possibly / mixed*, plus quality badges (recency, methods, journal rank, citations) and a "Study Snapshot." Librarian Aaron Tay's 2025 deep dive gives the cautionary case: for "Does chess training causally improve academic performance?" the meter read 41% yes / 12% possibly / 24% mixed / 24% no — but *"none of the seven 'yes' studies are tier-one … while the tier-one studies are among the more negative results."* His verdict: the meter *"embodies a problematic approach to evidence synthesis that the systematic review community largely abandoned decades ago."* **Lesson:** a headline percentage that ignores source *quality* misleads precisely the readers it is meant to help.

### 5.7 The Scientific Evidence Indicator (Danish science-journalism study)

A small graphic placed at the top of health-science news stories, scoring the underlying study on publication channel (peer-reviewed or not), method (a 7-point evidence hierarchy) and researcher experience. Evaluation: it *"demonstrate[d] some success in helping readers recognize whether studies have undergone scientific peer review,"* but showed *"challenges in facilitating a more in-depth understanding."* **Lesson:** one binary the lay reader already understands ("was this checked by someone else?") lands; multi-dimensional scoring does not.

### 5.8 The hurricane "cone of uncertainty" — the containment effect

Twenty years of misreading: people assume everything outside the cone is safe (the *"containment effect"*). The NHC's 2024 redesign did not add more statistics; it added inland watches and warnings *on the same map*, because *"the absence of displaying those warnings inadvertently gives the impression that it's all clear."* **Lesson:** a shape that visually bounds uncertainty invites the reader to treat the boundary as a wall; showing *what lies outside* the confident region is the fix.

### 5.9 WikiTree — certain / uncertain, never without a source

A genealogy wiki lets each fact be flagged *certain* ("confirmed with reliable sources") or *uncertain* ("suspect it's correct but lack solid evidence"), with the house rule *"never enter information … even uncertain information, without including your source."* **Pattern:** a two-state flag bound to a mandatory citation. **Why it works:** the flag never floats free of the evidence.

### 5.10 Cross-references

The Leiden brackets (§2.3), the Washington Post's scales-of-justice for "unverifiable" (§3.8), and the museum provenance period-vs-semicolon (§2.1) are all confidence languages too — each with an explicit mark for *we do not know*, which is the mark most systems forget.

---

## 6. Synthesis — seven patterns CiC could adapt

Opinionated, and constrained by the four rulings in §0. Each recommendation names the surface it belongs on, the real example it borrows from, and the trap it avoids.

### (a) Showing a Representative's sourcing in and around the site's preview material

**R1. Set the silence in type: a Leiden-style mark for "where the record is quiet."**
The tradition page already carries one "honest-limit statement, quoted, in the tradition's own words." Give that quotation — and any future preview excerpt — a visible, consistent typographic device for the gap itself (an em-rule, a bracketed ellipsis `[ … ]`, or a hairline break), used identically across all seven traditions and explained once in About. The gap becomes a visible object the visitor learns to recognize, not a sentence apologizing for it.
*Borrowed from:* papyri.info / Leiden conventions (§2.3); museum provenance periods (§2.1). *Avoids:* prose hedging that Kent's data shows readers ignore (§5.1).

**R2. One "from" device, everywhere, that opens to the actual words.**
The storyboard already gives each "question people bring" a one-line source note and quotes the quiet statement from a real record id. Make that attribution a *signature*: the same small glyph and position beneath every quoted line on the site (the questions, the quiet statement, the "who is speaking" names, any preview exchange), and on tap/hover or click it reveals the underlying passage — the source's words, not just its title. This is the C2PA pin and the Sefaria panel at CiC scale: ambient, uniform, one gesture from the original.
*Borrowed from:* NotebookLM click-to-highlighted-passage (§4.4); Sefaria Resource Panel (§2.4); Content Credentials pin (§4.9); The Conversation's uniform disclosure line (§3.9). *Avoids:* a sources table — the finding aid Mark cut (§0, ruling 2).

**R3. Show one real refusal, in the flow, before the seat.**
The homepage sample exchange was rightly cut as "explanation about the experience." This is different: a single short excerpt — two lines at most — of the Representative *declining* a question ("The letters we have don't say. I won't guess for them.") with its R2 attribution beneath, placed in the reading flow where the eye already is (on the tradition page, the "where we are quiet" slot; on the homepage, the sentence after 1.3d′), never in a box, never at the foot. The CME data says a box is seen by a third of readers; a line in the flow is seen by all of them. Dimensions in Testimony proves a refusal *in the voice* is the single most persuasive honesty moment an interactive exhibit has.
*Borrowed from:* *"I'm afraid I cannot answer that question"* (§4.1); the CME placement finding (§3.3). *Avoids:* re-creating the cut §1.4 sample exchange — this is one refusal, not a demonstration of the experience.

**R4. A three-word source-strength vocabulary, carried in the attribution line, never as a legend.**
The record store already tags witness texts *Widely Accepted*. Adopt a fixed, tiny vocabulary — on the order of *widely accepted · contested · quiet* — defined once in About's "how it works," and let it appear only as a single italic word inside the R2 attribution (IPCC-style: a term of art marked in the sentence). No numbers, no meter, no badges, no legend section on tradition pages (already cut and rightly). Three words is the GRADE lesson; the italic-in-prose is the IPCC lesson; "contested" as a positive value is the scite lesson.
*Borrowed from:* IPCC (§5.2), GRADE (§5.3), Gwern's fixed list (§5.4), scite's *contrasting* (§5.5). *Avoids:* the Consensus Meter's percentage trap (§5.6), the cone's containment effect (§5.8), and the multi-dimensional score the SEI study showed lay readers cannot use (§5.7).

### (b) Reframing "not a real person, here's how it's built" as a promise

**R5. Rewrite the disclosure line as a constraint-promise, in the same position.**
The 1.3d′ line already carries the substance. Its *grammar* is still a caveat ("not a person who lived"). The examples that work invert the grammar: they lead with what the thing *only* does. A candidate, offered for Mark's ear rather than as copy: *"Every word Chloe says traces to something her people actually wrote. Where their letters run out, she says so."* Then, quietly, the fact: *"She is a representative voice, not a person who lived."* Same position (before any conversation link, per ruling 3), same brevity, the world before the mechanism — but the honesty is now the first clause, not the concession.
*Borrowed from:* *"not artificially generated … in their own words"* (§4.1); *"authentic and unaltered"* (§4.2); *"grounded in your documents, not the whole internet"* (§4.4). *Avoids:* the "can make mistakes" footer grammar (§4.10) and the Magisterium over-claim — the second sentence keeps it true (§4.5, §4.11).

**R6. Let the voice say what it is — once, in character, naming its sources not its model.**
Ask Dalí's most disarming moment is Dalí explaining himself. CiC's equivalent is not "I am an AI" (mechanism — ruled off tradition pages) but the Representative naming *whose* letters she is built from, in her own register: "I speak from what Ignatius wrote on the road, what the Didache taught, what Pliny reported of us. Nothing else." That sentence can be the "who is speaking" paragraph's first line. It answers the skeptic's "is this slop?" with a bibliography delivered as testimony.
*Borrowed from:* Ask Dalí's in-character disclosure (§4.3); NET Bible's "look over the translators' shoulders" (§2.5). *Avoids:* the ventriloquism objection (§4.3) — the voice claims only its sources, never the person.

**R7. One "how we know what she says →" link near the seat, opening to the record and to a door for correction.**
Not a section, not a finding aid: a single BBC-Verify-style affordance beside the seat line that opens the record store view for that tradition (sources, the confidence vocabulary defined, review status) — the depth the storyboard already assigns to About's "how it works." Inside it, borrow Cooper Hewitt's plain admission and ProPublica's invitation: *this record is a work in progress; it will contain errors; here is where to tell us.* The link costs the seeker nothing and gives the pastor, the scholar, and the skeptic exactly the thing they came to check. The Trust Project's *Methods*, *Citations* and *Actionable Feedback* indicators, collapsed to one control.
*Borrowed from:* BBC Verify's "how we verified this" button (§3.6); Cooper Hewitt's notice (§2.2); ProPublica's criticism email (§3.1); Trust Project indicators (§3.2). *Avoids:* Direction 03's "record before the door" (§0, ruling 1) — this sits *beside* the door, one click deep.

### What not to do (each backed by a failure above)

- No percentage, meter, or score of confidence (Consensus Meter, §5.6).
- No bounded "confidence shape" that implies safety outside it (hurricane cone, §5.8).
- No multi-dimensional evidence scorecard on any visitor page (SEI study, §5.7).
- No transparency *box* or footer; if it is worth saying, it goes in the flow (CME, §3.3; disclaimer paper, §4.10).
- No "AI" badge on every message or an "AI system" lead — the mechanism stays in About (ruling 3; Ask Dalí's critics, §4.3).
- No promise stronger than the build can keep: "traces to a source" is defensible; "cannot be wrong" is not (Magisterium critics, §4.5; Perplexity, §4.10).

---

## 7. Where this leaves the four rulings

The research **strengthens** all four. Ruling 1 (door first) is what BBC Verify's button and NotebookLM's citation do — method one gesture away, never in front. Ruling 2 (no finding aid on tradition pages) is the CME finding restated: a record section would not be read. Ruling 3 (world before mechanism) is Ask Dalí's lesson: the voice names its sources, and the LLM is named elsewhere. Ruling 4 (no sample exchange) stands; R3 proposes a single refusal line, not an exchange, and should be read against that ruling by Mark rather than assumed compatible.

---

## 8. Limits of this pass

- **Reachability.** The session's egress proxy blocked direct reads of nearly every primary page (metmuseum.org, britishmuseum.org, gwern.net, sfi.usc.edu, propublica.org, thetrustproject.org, magisterium.com, ia.net, npr.org, artnews.com, niemanlab.org, the museum partner pages, and others). Quotations were therefore carried through search-index excerpts and reputable secondary coverage (Nieman Lab, GIJN, VentureBeat, CJR, MIT Technology Review, UNSW, Yahoo Finance's carriage of the WWII Museum press release, library guides). Where a figure rests on a single secondary claim it is flagged in the text (the NotebookLM 13%/40% figure especially). A follow-up pass with unrestricted fetch should verify verbatim wording before any of it is quoted on the site.
- **Search budget.** The session's web-search allowance was exhausted at 200 queries; a final sweep for (i) any AI product that *markets* "it will say I don't know," and (ii) a canonical museum "harmful language / incomplete records" statement beyond Cooper Hewitt's, was not completed. The §4 headline — that such marketing is rare — is a confident reading of ~40 queries across the space, not a proof.
- **Transfer risk.** The most persuasive honesty examples (§4.1–4.2) concern recorded humans; CiC's voice is generated. §4.11 states the gap; R5's two-sentence structure is the proposed way to be honest about it.

---

## Sources

**Museums and archives**
- AAM provenance conventions as republished by Krannert Art Museum — https://kam.illinois.edu/resource/aam-resource-how-read-provenance-narrative
- The Met, Provenance Research Resources — https://www.metmuseum.org/es/about-the-met/provenance-research-resources
- Philadelphia Museum of Art, Provenance — https://www.philamuseum.org/provenance
- Cooper Hewitt collection site notice — https://collection.cooperhewitt.org/
- Cooper Hewitt, The Interactive Digital Visitor Experience — https://www.cooperhewitt.org/new-experience/
- Papyri.info review, RIDE — https://ride.i-d-e.de/issues/issue-9/papyri-info/
- Leiden+ (Digital Classicist wiki) — https://wiki.digitalclassicist.org/Leiden-plus
- ENCODE Leiden+ guidelines — https://encode-guidelines.github.io/guidelines/leiden+/
- Sefaria Resource Panel guide — https://help.sefaria.org/hc/en-us/articles/18472472138652-Quick-Guide-Meet-the-Sefaria-Library-Resource-Panel
- Sefaria, interconnected texts — https://help.sefaria.org/hc/en-us/articles/18613227644316-How-to-Find-Interconnected-Texts
- NET Bible Full Notes Edition (Thomas Nelson) — https://www.thomasnelsonbibles.com/product/net-bible-full-notes-edition/
- NET Bible 2019 preface — https://bibleversion.org/bible/versions/modern-english/net-bible-new-english-translation-net/net-bible-new-english-translation-2019-full-notes-edition-preface/
- British Museum Collection Online (CIDOC paper) — https://cidoc.mini.icom.museum/wp-content/uploads/sites/6/2018/12/82_papers.pdf

**Journalism**
- Nieman Lab, "Maybe greater transparency can increase trust in news — but readers have to find your transparency first" (2020) — https://www.niemanlab.org/2020/01/maybe-greater-transparency-can-increase-trust-in-news-but-readers-have-to-find-your-transparency-first/
- Center for Media Engagement, Testing Behind the Story Cards — https://mediaengagement.org/research/behind-the-story-cards/
- Trusting News on the CME "explain your process" study — https://trustingnews.org/research-explain-process-boxes-build-trust-center-media-engagement/
- Nieman Reports, "Can 'Extreme Transparency' Fight Fake News…" — https://niemanreports.org/can-extreme-transparency-fight-fake-news-and-create-more-trust-with-readers/
- ProPublica, "How We Reported This Story" (example) — https://www.propublica.org/article/illinois-school-students-seclusion-rooms-methodology
- ProPublica, "Why We're Giving Away Our Reporting Recipe" — https://www.propublica.org/article/why-were-giving-away-our-reporting-recipe-304
- The Trust Project, About — https://thetrustproject.org/about/
- The Trust Project, adoption and Mirror result — https://thetrustproject.org/2018/10/news18/
- Android Community, the 8 indicators — https://androidcommunity.com/trust-projects-8-indicators-to-help-news-organizations-build-credibility-20171117/
- Story Jungle interview, NYT Visual Investigations — https://en.storyjungle.io/interviews/-the-audience-is-seeing-the-evidence-for-themselves-_a-231-6366.html
- GIJN, Malachy Browne on visual investigations — https://gijn.org/stories/malachy-browne-future-visual-invsetigation-ai/
- Bellingcat, open-source evidence upheld in the ECHR — https://www.bellingcat.com/resources/2023/03/28/how-open-source-evidence-was-upheld-in-a-human-rights-court/
- Study of Bellingcat's investigation patterns 2014–2020 — https://vc.bridgew.edu/cgi/viewcontent.cgi?article=1202&context=ijcic
- BBC Verify (Wikipedia) — https://en.wikipedia.org/wiki/BBC_Verify
- "Explaining the 'how' — the launch of BBC Verify" — https://stephenheins.substack.com/p/explaining-the-how-the-launch-of
- Gwern, Sidenotes in Web Design — https://gwern.net/sidenote
- Tufte CSS — https://edwardtufte.github.io/tufte-css/
- Washington Post Fact Checker (Ballotpedia) — https://ballotpedia.org/The_Washington_Post_Fact_Checker
- The Conversation, editorial guidelines 2021 — https://cdn.theconversation.com/static_files/files/1797/The_Conversation_Global_Editorial_Guidelines_2021.pdf

**AI products and installations**
- "Can Make Mistakes": AI Chatbot Disclaimers as Failed Explainability Surfaces (CHI 2026 workshop, Zenodo) — https://zenodo.org/records/20387079
- USC Shoah Foundation, Dimensions in Testimony — https://sfi.usc.edu/dit ; FAQ — https://sfi.usc.edu/dit/faq
- Museum of Jewish Heritage, Dimensions in Testimony — https://mjhnyc.org/exhibitions/new-dimensions-in-testimony/
- Virginia Holocaust Museum, Dimensions in Testimony — https://www.vaholocaust.org/dimensions-in-testimony/
- Dimensions in Testimony (Wikipedia) — https://en.wikipedia.org/wiki/Dimensions_in_Testimony
- National WWII Museum, Voices from the Front — https://www.nationalww2museum.org/visit/museum-campus-guide/louisiana-memorial-pavilion/voices-from-the-front
- StoryFile / WWII Museum press release (Yahoo Finance) — https://finance.yahoo.com/news/storyfile-debuts-innovative-ai-video-200800249.html
- Dalí Museum, Ask Dalí — https://thedali.org/exhibit/ask-dali/
- NPR on Ask Dalí — https://www.npr.org/2024/07/18/nx-s1-5043649/you-can-now-ask-salvador-dali-questions-sort-of-as-part-of-an-ai-installation
- blooloop on Ask Dalí (Hine quotes) — https://blooloop.com/technology/news/dali-museum-artificial-intelligence-ask-dali/
- ARTnews, "…Uncomfortable Questions about Ventriloquizing the Dead" — https://www.artnews.com/art-news/issue/salvador-dali-vincent-van-gogh-ai-installations-ethics-1234714954/
- Open Culture on Hello Vincent — https://www.openculture.com/2024/02/hello-vincent.html
- NotebookLM, document-grounded AI (Emergent Mind) — https://www.emergentmind.com/topics/notebooklm
- NotebookLM grounded-in-your-documents overview — https://www.kzsoftworks.com/blog/notebooklm-this-ai-is-grounded-in-your-documents-not-the-whole-internet
- Magisterium AI, Why Magisterium AI — https://www.magisterium.com/about/why-magisterium-ai
- Magisterium AI FAQ (Hallow) — https://help.hallow.com/en/articles/10601094-magisterium-ai-faq
- Public Discourse, "Beware of Catholic AI" — https://www.thepublicdiscourse.com/2025/11/99435/
- Elicit feasibility study (Research Synthesis Methods) — https://www.cambridge.org/core/journals/research-synthesis-methods/article/using-elicit-ai-research-assistant-for-data-extraction-in-systematic-reviews-a-feasibility-study-across-environmental-and-life-sciences/C97DAEC70C3173A260F0B12E729E7250
- iA Writer, Authorship — https://ia.net/writer/support/editor/authorship ; "See What AI Wrote" — https://ia.net/topics/see-what-ai-wrote
- VentureBeat, Anthropic releases system prompts — https://venturebeat.com/ai/anthropic-releases-ai-model-system-prompts-winning-praise-for-transparency
- C2PA, official Content Credentials icon — https://c2pa.org/introducing-official-content-credentials-icon/
- C2PA UX guidance — https://spec.c2pa.org/specifications/specifications/2.0/ux/UX_Recommendations.html
- VentureBeat on Character.AI's October 2024 changes — https://venturebeat.com/ai/character-ai-clamps-down-following-teen-user-suicide-but-users-are-revolting
- NBC News on the Historical Figures app — https://www.nbcnews.com/tech/tech-news/chatgpt-gpt-chat-bot-ai-hitler-historical-figures-open-rcna66531
- MIT Technology Review on AI Overviews — https://www.technologyreview.com/2024/05/31/1093019/why-are-googles-ai-overviews-results-so-bad/
- UNSW on AI Overviews — https://www.unsw.edu.au/newsroom/news/2024/05/eat-a-rock-a-day-put-glue-on-your-pizza-how-googles-ai-is-losing-touch-with-reality
- CJR, "AI Search Has a Citation Problem" — https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php

**Confidence language**
- Sherman Kent, Words of Estimative Probability — https://philarchive.org/rec/KENWOE ; overview — https://en.wikipedia.org/wiki/Words_of_estimative_probability
- zonination, Perceptions of Probability — https://github.com/zonination/perceptions
- IPCC AR6 WGI Summary for Policymakers (calibrated language box) — https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf
- Crimmins et al., calibrated language in U.S. climate assessments — https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001817
- GRADE symbols (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5502230/ ; Cochrane Handbook ch. 14 — https://training.cochrane.org/handbook/current/chapter-14
- Gwern, About (confidence tags) — https://gwern.net/about ; HN discussion — https://news.ycombinator.com/item?id=10862311
- Maggie Appleton, Epistemic Disclosure — https://maggieappleton.com/epistemic-disclosure ; Garden — https://maggieappleton.com/garden/
- scite badge documentation — https://scite.ai/badge ; scite in QSS — https://direct.mit.edu/qss/article/2/3/882/102990/
- Consensus Meter help article — https://help.consensus.app/en/articles/10069920-the-consensus-meter
- Aaron Tay, "A 2025 Deep Dive of Consensus" — https://aarontay.substack.com/p/a-2025-deep-dive-of-consensus-promises
- "How trustworthy is this research?" Scientific Evidence Indicator (Digital Journalism 2023 / arXiv) — https://arxiv.org/pdf/2202.00069
- University of Miami on the cone redesign — https://news.miami.edu/stories/2024/02/cone-of-uncertainty-graphic-to-feature-more-information.html
- WikiTree Help: Uncertain — https://www.wikitree.com/wiki/Help:Uncertain
