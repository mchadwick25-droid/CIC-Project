# CiC Tour / Hosted Experience Module
## Strategy, Per-World Evidentiary Analysis, and Architecture Design — V0.3 DRAFT

**Date:** 2026-07-16 (V0.1 through V0.3 same day — see Document Log)
**Status:** Planning artifact only. Phase Two product concept. Nothing here touches `cic-poc` code, the current prototype, or Phase One testing. Every build item this document implies is named in §6 (Future Handoffs) rather than started.
**Governed by:** Vision/Mission/Convictions V1.1 (Conviction 4, Conviction 5, Historical Responsibility, Participant Agency); Constitution V2.2 (Articles 6, 17, 19, 28, 30); Construction Framework V7.3 Part II (four-tier story classification, No Tier 5) and Step 9 (Story Inventory / Doc_09); each live world's own approved Doc_09 and deployment chunks.
**Grounded in direct reading of:** all four live worlds' Doc_09 Story Inventories, the deployed World Capsule Cores and story chunks under `cic-poc/backend/data/`, `world_manifest.py`, the PAHC Permanent Prompt, and the L3D one-Representative Table Process.

---

## 1. The Concept, and the Discipline That Already Governs It

A **hosted experience ("tour")** is a mode in which the Representative does not only answer questions but invites the participant into a reconstructed moment of its world — a worship gathering, a shared meal, a daily rhythm — and walks them through it, present throughout to explain, translate, and answer questions. The tour covers **only what the sources actually support**. Where a world has no real sourced example of a communal experience, no tour is offered for that world, and that absence is an honest finding, not a gap to fill.

### 1.1 Why a tour is a higher-stakes claim

A conversational answer says *"here is what I can tell you about our gathering."* A tour says *"come — this is what a morning gathering looked like."* Structurally, that is a stronger historical claim, and under the Foundational Value of Historical Responsibility ("acknowledging where evidence is thin, where reconstruction is inferential, and where honest uncertainty is the most responsible position") it therefore requires **more** evidentiary weight, not less. Article 6's testable conditions — did the encounter "present the world honestly with its tensions held as the world held them" — apply with extra force: a beautifully staged tour of a fabricated scene would keep the Representative's voice intact while violating exactly the honesty the Standard protects.

### 1.2 The central finding of this analysis: the evidentiary bar already exists

This module does not need a new evidentiary discipline invented for it. The Construction Framework's four-tier story classification, the No Tier 5 rule, and each world's approved Doc_09 Story Inventory **already are** the tour's licensing system:

> "Generated or illustrative narrative — stories invented to illuminate formation truths but not traceable to the world's own evidence — is not permitted within this framework. If the evidence does not support a story, the story does not exist for this world. Silence in thin areas is the right response. … A generated story, however well-intentioned, is not witness." — Construction Framework V7.3, Part II (No Tier 5)

**Design consequence (the single most load-bearing decision this document proposes):** a tour is a *presentation mode over already-approved Doc_09 story chunks* — never a new content class. If a scene is not already licensed as a story chunk in a world's approved Story Inventory, it cannot be toured. The pipeline that decides whether a tour exists for a world is the pipeline that already exists; this module adds a presentation layer and its guardrails, nothing upstream.

This also means the tour inherits, for free, the discipline already operating in the deployed chunks: tier-appropriate register, Retrieve-When / Do-Not-Retrieve-When conditions, per-element Source Identification for Tier 4 material, and precedents like the Desert world's removed diet element (an unsourced Tier 4 element "must be removed from the Story Text," not kept with a caveat).

---

## 2. Product Strategy

### 2.1 What "hosted through an experience" means as a participant-facing flow

The tour differs from the existing conversational encounter in *who is structuring the next few minutes*, not in who is in control. Proposed flow:

1. **Invitation.** The Representative offers — never imposes — the tour, in its own voice, at a natural moment ("Would you like me to walk you through such a morning as Justin describes it?"). The invitation appears when conversation enters the anchor scene's own territory — in practice, when the anchor chunk's existing **Retrieve-When** conditions are met. The retrieval front-matter each chunk already carries is, unmodified, the tour's invitation heuristic.
2. **Threshold.** A visible framing moment before the scene begins: what this tour is (a witness's own account, or an explicitly marked reconstruction — see §2.2), what it is built from, and what it will not claim. The participant explicitly accepts. Declining costs nothing and changes nothing about the ordinary encounter — per Participant Agency ("the system creates conditions for discovery, not pressure toward predetermined outcomes"), the invitation is an open door, and the Representative does not re-press a declined invitation.
3. **The hosted scene, in beats.** The Representative narrates the scene as host — a small ordered sequence of moments (arrival, the reading, the prayers, the bread and cup, the collection, the dismissal — whatever the source itself gives). At every beat the participant can interrupt, ask anything, linger, or leave. Questions are answered in ordinary conversational mode (full RAG retrieval, all standing guardrails) and the tour resumes only if the participant wants it to.
4. **Return.** The tour ends by handing the participant back to open conversation, with the Representative available to reflect on what was seen. No summary is imposed, no interpretation offered unasked — "the encounter opens something — what the participant does with that opening belongs entirely to them."

The whole thing lives *inside* an existing encounter. It is not a separate app surface, not a video, not a self-running slideshow — the Representative's presence throughout is the product.

### 2.2 Two classes of tour claim — the load-bearing product distinction

The per-world analysis (§3) shows the live worlds' tourable scenes fall into exactly two evidentiary shapes, and the difference between them is a difference in *what the tour is allowed to say it is*:

**Class A — Attested-Scene Tour (Tier 1 anchor).** The scene rests on a source's own narrated description of the event, in the author's own voice. The tour's claim: *"here is what one witness tells us, in his own words."* The Representative hosts as a relayer of a named witness — "Justin tells the emperor that on the day of the sun, we gather…" — and the witness's own perspective, audience, and limits are part of the tour, not a footnote. Only one scene in the entire current portfolio qualifies (PAHC's Justin gathering).

**Class B — Reconstruction Tour (Tier 4 anchor).** The scene is a composite reconstruction of typical practice, every element separately sourced, no named individual, no specific occasion. The tour's claim: *"a morning such as ours might keep"* — and per Article 17's bar on "invisible movement from attested evidence into speculation," the reconstruction character must be **persistently visible for the tour's entire duration**, not disclosed once at the threshold and allowed to fade. Confidence is Inferential/Thin for the whole scene regardless of element quality, exactly as the Framework already rules.

**There is no Class C.** A world with neither kind of licensed scene gets no tour, and the honest product answer to "why can't I tour this world?" is itself shown: *this world's own surviving record does not preserve such a scene, and this project does not invent one.* Done right, that refusal screen is one of the most mission-expressive surfaces the product will ever have — it is Conviction 4 made visible at the exact point where every competitor product would fabricate.

### 2.3 Voice discipline in scene-narration mode

The Representative's standing discipline — never modernizing, never inventing, honest silence held rather than filled — carries into hosting unchanged, with three additions specific to narration:

- **Tier-register lock.** A Class A tour narrates in relayed-witness register with the author named throughout; a Class B tour narrates in explicit-reconstruction register throughout ("In a gathering such as ours might keep any morning…" — syrstory009's own approved opening). The registers never blend, and two differently-sourced scenes are never merged into one composite (the PAHC chunks' own diversity-first rule: Justin's gathering, the Didache's meal, and Ignatius's one-eucharist program are three practices, not one "early church service").
- **Honest-silence beats are part of the tour.** Where the source goes quiet, the tour says so *in the Representative's own voice, inside the scene*: what the hymns' words were, no one wrote down; what the room smelled like, no source says. The deployed capsules already model this register (Desert: "You can speak to its shape and its hour, not to its every phrase"). A tour that narrates smoothly past its source's silences has failed even if every stated detail is sourced.
- **No new texture, ever.** The Desert world's removed-diet-element precedent, generalized into the tour's cardinal rule: an unsourced element does not appear hedged, caveated, or "atmospherically" — it is absent. Filling a visual or narrative gap with plausible period texture is precisely the Generating drift signal the Facilitator apparatus already monitors (L3D drift signals), and tour mode is that signal's highest-stress surface.

One real, unresolved tension to flag rather than smooth: some Representatives carry deliberate *speech-economy* constraints (Chloe's permanent prompt caps even her fullest answer at two short paragraphs, "a household's measure"). Scene narration wants more continuous speech than that. Whether tour beats get a licensed, bounded exception to a Representative's own length discipline — or whether the beats must simply be built short enough to fit it (my leaning: the latter; a host who speaks in a household's measure *is* the world's own texture) — is a per-world Representative-integrity question, flagged for construction-side judgment when a Tour Manifest is built (§4.1).

### 2.4 Illustrated/visual content: a real, separate production question — named, not assumed

**The project currently has no visual-asset pipeline of any kind.** No sourcing process, no licensing process, no review discipline for images, no L4 template governing them. This module cannot casually assume "period art" exists to be dropped in, and the per-world evidence makes the problem sharper than it first appears:

- **The most textually tourable world is the least illustrable.** PAHC's own Doc_02 finding is that its window is "essentially archaeologically invisible" across all three regions — and Dura-Europos and the Abercius inscription are **Excluded** Source Registry rows that "must not be used as evidence for this world's own period, however tempting for a vivid Tier 4 setting" (PAHC Doc_09 §4, Item 10, verbatim). Illustrating Justin's gathering with the Dura-Europos house-church would violate that world's own already-signed exclusion rule. This is not an edge case; it is the flagship tour.
- **The one world with licensed archaeology is the Desert.** Kellia excavation findings (multi-room hermitages with attached oratories) are Native, registered sources in that world's own record (Doc_02 §5.1, cited in desertstory008's Source Identification). Site photography or measured reconstruction drawings of Kellia are the one place a visual layer already has an evidentiary license.
- **An image is a claim.** An illustration implying a detail the sources don't support — furnishings, dress, room size, the look of a face — is the same violation as an invented sentence, but harder to police, because images cannot hedge. A picture has no register for "Inferential/Thin."

Three honest strategic options, in ascending cost and risk:

1. **Description-first (recommended default).** The Representative's own narration is the scene-setting medium; the visual layer is typography, pacing, and restraint. Zero new pipeline; zero new violation surface; and arguably the most mission-true — the encounter stays with the witness, not the picture (Conviction 5: technology "is never the point").
2. **Registry-licensed artifacts only.** Photographs of objects/sites that are already Native rows in the world's own Source Registry (Kellia for the Desert; manuscript pages where licensed), each captioned with what it is and what it does not show. Small pipeline: rights clearance + a caption-review discipline.
3. **Commissioned illustration as "visual Tier 4."** Possible in principle only if every depicted element carries its own Source Identification and the image passes the same independent review cycle a story chunk does — i.e., a new L4 template ("Tour Visual Chunk"?) and a real production budget. This is a genuine, separately-resourced program, not a feature flag. **Generative-AI imagery is the highest-risk form of this option and should be treated as presumptively prohibited**: it manufactures unsourced detail by construction — pictorial Tier 5 — and auditing every generated pixel against a Source Identification list is harder than simply commissioning a disciplined illustrator.

The recommendation this document carries: **launch-shape the module on option 1, permit option 2 where a world's own registry licenses it, and treat option 3 as a separate future decision with its own funding-workstream implications.** A tour whose only "asset" is a disciplined voice is already the product; images are an enhancement question, not a viability question.

### 2.5 Product framing and access (revised at V0.3, per project-lead ruling)

**Decided (2026-07-16): no paywall system is planned. Everything is accessible to every participant.** The earlier "Level 2 add-on" framing is retired as a planning assumption; tiering can be revisited later if the project ever goes that way, and if it is, one commitment already binds that future conversation: *evidentiary absence is never presented as a locked feature* — a "no tour exists for this world" screen stays identical and free everywhere, because conflating a paywall with an evidentiary absence would spend the project's honesty capital on a pricing widget.

Cost note, unchanged: the tour's marginal cost is content production (Tour Manifests + review cycles + any produced audio), not runtime — which is why the standing production principle is now **whatever meets the need and is cheapest** (see §2.7).

### 2.6 The experiential palette: "let the sources perform themselves" (added at V0.2)

Worked out with the project lead on 2026-07-16, prompted by his own question — what is a creative way to stay inside the commitments and still let people *experience* each world? The answer that emerged: the module's creative space is **modal, not inventive**. An experience is built only from presentation modes whose every claim-bearing feature is attested, and the absences are themselves part of the experience. Four modes, and nothing else is in the palette:

1. **Attested text as experience.** The sources speak in their own words: Justin's order of service walked in his own sequence; a letter of Ignatius or 1 Clement *read aloud to the gathering* — which is itself PAHC's own attested network practice, and Chloe's own permanent-prompt role; the Two Ways taught to the participant-as-catechumen from the Didache's actual text; an Ephrem stanza with its refrain; the Psalter itself as the desert day's attested substrate; Jerome's own prefaces defending a translation choice.
2. **Attested form as experience.** Meter and refrain structure (in the texts themselves, even where melody is lost); the sequence of a gathering; the shape of a week (six days in the cell, the sixth-day walk); the pre-dawn hour of the qyama vigil.
3. **Attested roles and voices.** The participant handed the refrain; the participant taught as a catechumen was taught; and voices cast to match attested performers — see the women's-voices decision in §3.2. A voice that misrepresents the attested performer (a lone male narrator for a women's choir's material) is a fidelity error even when the words are sourced.
4. **Honest-silence beats.** The synaxis threshold; the lost tune; the unwritten woman's word — spoken by the Representative inside the scene, as the world telling the truth about itself.

**The refused move, restated for this palette:** compositing from adjacent cultures or eras "as long as we say it may have sounded like…" fails the Tier 4 test element-by-element (for a melody, the elements — scale, tune, vocal style — are precisely what is unattested, so nothing attested is being assembled), and a disclaimer cannot restrain a sensory claim: text can hedge mid-sentence, sound and image cannot. The project's own precedent (the Desert diet element) is removal, not caveat; the bar is constitutional (Article 19: "free invention is prohibited at every stage"), not thread-level.

**Project-lead ruling appended (2026-07-16): "let the source make the call" — and the richer the better, within it.** Where a world's approved source material supports a scene, the tour exists; more choice and more different experiences per world are good, *but only when supported by the source material*. Tour families (PAHC's gathering / path-to-the-water / day-in-the-assembly) are encouraged wherever the sources license them. This is now the general rule for boundary tensions of the §3.2 shape as well: the reviewed, licensed chunk governs; a capsule's self-limit governs unscripted expansion, not the world's own approved material.

### 2.7 Audio policy (decided at V0.3, per project-lead ruling)

- **Default is text — whatever meets the need and is cheapest.** No audio layers by default, no ambient sound design, no narration voiceover.
- **Audio only where the tour has a source-grounded performative reason** — a teaching being given, singing/recitation — i.e., moments where the *source itself* was an oral performance. The women's-voices spoken madrashe (§3.2) is the type case.
- **Decided: the Syriac audio is in Syriac, with English subtext/captions; other languages eventually.** The participant hears the attested language and reads the meaning — the same two-layer honesty as naming a translation a translation. Captions also serve accessibility, consistent with the everything-accessible ruling in §2.5.
- **The Representative itself is not audio-voiced or visually depicted; its presence remains its written voice**, with produced audio reserved for the performative moments above. *(Recorded as this document's interpretation of the project lead's "the representative is voice only" — flagged in §7 for his confirmation, since the phrase could be read more than one way.)*

---

## 3. Per-World Evidentiary Analysis

Grounded in each world's own approved Doc_09 Story Inventory, the deployed story chunks and World Capsule Cores under `cic-poc/backend/data/`, and (for world 5) the state of the build folder as of 2026-07-16. A future builder should be able to answer "is a tour possible for World X, and on what basis" from this section alone.

### 3.0 Lookup table

| World | Tour verdict | Anchor scene (ID, tier) | Tour class | Hardest constraint |
|---|---|---|---|---|
| The House-Churches (pahc) | **YES — strongest case in the portfolio** | A Sunday Gathering in Rome, As Justin Describes It (`pahcstory006`, **Tier 1**) | Class A (+ optional Class B satellites: 009, 010, 011, 012) | Rome-only; never generalized network-wide; never blended with the Didache or Ignatian practices; no visual record exists (Dura-Europos is Excluded) |
| Syriac Christianity (syr) | **QUALIFIED YES — Class B only** | A Morning Gathering of the Qyama at Nisibis (`syrstory009`, **Tier 4**) | Class B | Scene is bound to pre-363 Nisibis; Representative (Mar Yausep) is Persian-anchored; deployed capsule itself says the Representative speaks "only briefly of the gathering itself" — boundary call flagged for the project lead (§3.2) |
| Desert Fathers and Mothers (desert) | **PARTIAL — daily-rhythm tour yes; worship-service tour NO** | A Day in a Kellia Cell (`desertstory008`, **Tier 4**) | Class B | The weekly synaxis is attested in one sentence (shape and hour only) — its interior is not narratable; diet, exact hours, personal routine explicitly barred by the chunk's own front-matter |
| The Bethlehem Circle (hal) | **PARTIAL/THIN — shared-life tour possible; no congregational/liturgical tour** | A day at the double monastery (`hal_story10`, **Tier 4**); optionally the translation process (`hal_story11`, Tier 4 boundary case) | Class B | No liturgical horarium attested ("which hours, which psalms" explicitly not manufactured); S11 must never be narrated as a specific episode; newest, least live-tested world |
| Nicene-Cappadocian | **NOT ASSESSABLE — no tour** | — | — | Construction has not begun (build folder empty as of 2026-07-16); no Doc_09 exists; re-run this analysis when its Story Inventory is approved |

### 3.1 The House-Churches (Post-Apostolic House-Church, `pahc`) — YES

**The sourced communal scene exists, and it is the strongest in the portfolio — the only Tier 1 narrated liturgical description any live world has.** `pahcstory006` carries Justin Martyr's own first-person account (*First Apology* 65–67, c. 153–157 CE, Registry P06) of what "we" do on the day named for the sun: gathering, reading "as long as time allows," the presider's exhortation, standing corporate prayer, bread and wine mixed with water, thanksgiving "according to his ability," the people's Amen, and a collection for orphans, widows, the sick, prisoners, and strangers. Confidence: Widely Accepted as a description of Roman practice; Contested as a network-wide template (Bradshaw's caution, already in the chunk). This is precisely "a sourced example of a PAHC worship service."

**Satellite scenes (all Tier 4, all already licensed as chunks):** the catechumen's path to the water (`pahcstory009` — with its two-level claim discipline: the Didache-specific sequence vs. the now cross-strand-corroborated general practice), the Didache's distinct cup-first eucharist (`pahcstory010`), Ignatius's one-eucharist-under-the-bishop (`pahcstory011`), and the deliberately cross-strand "day under the bishop / day under the presbyters" (`pahcstory012`). A PAHC tour program could eventually be a small family: *the Sunday gathering* (Class A flagship), *the path to the water* (Class B), *a day in the assembly's life* (Class B, both strands held in parallel).

**Binding constraints, from the world's own record:** the Justin scene is one Roman writer's account addressed to a hostile imperial audience for a persuasive purpose — the tour must carry that vantage as part of the scene, not smooth it into neutral omniscience. It must not be generalized to Antioch or Asia Minor. The three eucharistic practices are never merged (diversity-first rule, stated in the chunks themselves). And **no visual record is available to this world at all** — its window is archaeologically invisible and its two famous "early church" visuals (Dura-Europos, Abercius) are Excluded registry rows. A PAHC tour is a description-first tour by evidentiary necessity, not by budget choice.

### 3.2 Syriac Christianity (Edessa/Nisibis, `syr`) — QUALIFIED YES, Class B only

**The sourced communal scene exists as an approved Tier 4 composite:** `syrstory009`, "A Morning Gathering of the Qyama at Nisibis" — the pre-dawn vigil of the vowed qyama, the bnat qyama choir singing Ephrem's madrashe as teaching rather than ornament, the Diatessaron read as one continuous Gospel, the combined Nativity-Epiphany feast — every element separately sourced (Aphrahat Dem. 6; Harvey on the choirs; Brock on raza/shrara; Beck on the calendar), no named individual, no specific occasion. Its Retrieve-When is already, verbatim, a tour trigger: "participant asks what an ordinary act of worship in this world actually looked or felt like."

**This world has no Class A possibility anywhere:** its Doc_09's own honest finding is **zero Tier 1 entries** — the source ecology is "structurally literary and theological rather than narrative-historical." A Syriac tour is a reconstruction tour or nothing, and its persistent Inferential/Thin marking is not negotiable.

**Three constraints from the world's own record, one of which is a genuine boundary call for the project lead:**
1. The scene's calendar detail binds it to **pre-363 Nisibis**; the chunk's own guidance bars offering it as-is for post-363 Edessa or for Aphrahat's Persian-side community specifically (the qyama/choir/hymn/Diatessaron elements generalize; the calendar detail does not).
2. **Mar Yausep is Persian-anchored** (Aphrahat's side, per the manifest's own facilitator cautions) — so the world's one tourable scene sits on the *other* side of his own anchoring. Manageable (the chunk licenses the generalizable elements; a Yausep-hosted tour would host the generalizable core and name the Nisibene calendar detail as specifically Nisibene), but it must be handled in the Tour Manifest, not improvised.
3. The deployed World Capsule Core itself tells the Representative: "You can speak richly of the vow and the endurance your own life actually holds, but only briefly of the gathering itself. Your own record kept almost nothing about it in concrete detail." **An extended hosted gathering-scene sits in visible tension with that line.** The defensible reading is that the capsule's limit governs *unscripted expansion*, while syrstory009 is exactly the licensed, reviewed, element-sourced exception the world approved for this territory — but this is a real judgment call about a live world's own self-limitation, and it belongs to the project lead, not to this document. **Flagged as the one open per-world boundary question (§7, Q1).**

**Sound findings (added at V0.2, from the project lead's own exploration).** The choir question splits three ways, and the record answers each differently:

- **The words — yes, at full strength.** Ephrem's madrashe survive as texts and are this world's own registered primary material (Source Registry #1 *Hymns on Faith*, #2 *Contra Haereses*, per `syrlex004_madrasha.md`, itself a Tier 1 lexicon entry). A tour beat can give an actual stanza and refrain, relayed and attributed ("words Ephrem set for the choirs" — which also respects Yausep's Persian anchoring), with translation named as translation and the honest note that the meter and acrostic — which the world's own lexicon entry identifies as the formation technology itself — are largely lost in English.
- **The form — yes.** The stanzaic structure with refrains (ʿonyata) and the syllabic meter are attested in the texts themselves: the *rhythm* of a madrasha survives even though the tune does not. The participant can be handed the refrain. Who sang refrain versus stanzas needs a construction-side verification pass before a Tour Manifest states it.
- **The sound — no, and it cannot be composited around.** No musical notation survives from this world's window; later manuscript rubrics preserve melody *titles*, not melodies. Nothing period-adjacent is usable either: Bardaisan's hymn texts survive mainly as fragments Ephrem quoted to refute them (no music), and the nearest notated Christian music anywhere — the Oxyrhynchus hymn (P.Oxy. 1786, Egypt, late 3rd c.) — is Greek, Egyptian, another tradition and genre, and barred by the project's own cross-contamination discipline from standing in for this world's silence. A "may have sounded like" composite is refused on the grounds stated in §2.6.
- **Decided: if the Syriac words are voiced aloud, they are voiced by multiple women.** Element-by-element: women — attested (the bnat qyama choir); multiple — attested (a choir is plural); the words — attested (Registry #1–2); spoken rather than sung — deliberately withholding the one unattested element rather than inventing it. Once voiced at all, women's voices are arguably *required* for fidelity: a lone male narrator would misrepresent the attested performance context more than a women's ensemble does. Guardrails: framed as text-in-the-attested-voices, never as performance reconstruction (no unison/style/pacing claims); the contested-pronunciation research pass is a prerequisite (§6, item 7); and the tour carries the world's own Absent Stories truth aloud — no bnat qyama woman's own composed word survives, so women's voices carrying a man's words is the record's own shape, named rather than smoothed.

### 3.3 Desert Fathers and Mothers (Desert Monasticism, `desert`) — PARTIAL

**A daily-rhythm tour is possible; a worship-service tour is not, and the distinction is exactly the thin-mention case this analysis was asked to name.**

The licensed scene is `desertstory008`, "A Day in a Kellia Cell" (Tier 4): Psalter recitation opening and closing the day, rope- and basket-weaving through the daylight hours, and on the sixth day the walk to the settlement's gathering point for the synaxis — vigil, shared liturgy, communal meal — then back to the cell for the coming week. Strand C (semi-anchoritic) only, per its own front-matter.

**The synaxis itself is a thin mention, not a narrated description.** The entire communal-worship content of this world's record is that one sentence — shape and hour, sourced (Doc_03 §1.13; Doc_06 §2.6) — and the deployed capsule says so in the world's own voice: "What your own worship actually sounded like, word for word, is not something you can give in full. You can speak to its shape and its hour, not to its every phrase." A tour may *walk to* the synaxis and say honestly what is and is not known of it; it may not *enter and narrate* it. The chunk's own Do-Not-Retrieve-When already bars specifics beyond what is sourced (diet, exact hours, personal routine — the removed diet element must not be reintroduced).

**What about the Tier 1 material?** This world's three Tier 1 scenes (Antony's call, the staged withdrawal, Pachomius's founding of the koinōnia) — the "three Tier-1 founding scenes told in full" — are *stories to be told*, and they are individual, specific-event narratives, not communal experiences a participant can be hosted through. Narrating Antony's call is already licensed conversational material; it is not a tour in this module's sense, and stretching "tour" to cover story-telling would blur the module's own definition. The honest verdict: **one Class B tour (the day's rhythm, cell to synaxis-threshold and back), no worship-service tour, and the absence of the synaxis's interior is itself a beat in the tour.** Done well, Papnoute standing at the door of the gathering saying *what happened inside, word for word, no one wrote down* may be the single most formation-true moment this module could produce anywhere in the portfolio.

### 3.4 The Bethlehem Circle (Hieronymian Ascetic-Literary, `hal`) — PARTIAL/THIN

**A shared-life tour is possible at Tier 4; no congregational or liturgical tour is possible at all.**

Licensed scenes: `hal_story10`, "A day of study, prayer, and manual labor at the Bethlehem double monastery" (Tier 4 composite: the structured common life from Ep. 108, Hebrew study under named teachers from Jerome's own prefaces, the praefatio/epistula correspondence practice) — **with the explicit, signed constraint that no liturgical horarium is attested: "which hours, which psalms" is not manufactured**, so the day can be toured in its shape but not clock-and-psalm scheduled. And `hal_story11`, the translation of a biblical book from Hebrew consultation to finished preface (Tier 4, a disclosed boundary case: composite in method but single-person in subject — it must never be narrated as a specific, individually attested episode, and never used to overstate Jerome's contested Hebrew fluency).

**The world's own Absent Stories list closes the liturgical door plainly** (Doc_09a §4, item 6): no story of catechesis, initiation, or ordinary congregational life exists — this world's formation medium was elite-textual, not mass-catechetical, and that is "a structural feature of the world, not an oversight." There is no worship service to tour, and none should be sought.

**Additional caution:** this is the newest and least live-tested world (per its own facilitator cautions in the manifest). If tours roll out world-by-world, this world goes last on live-testing grounds alone, independent of its evidence.

A distinctive opportunity worth naming: `hal_story11` could ground the portfolio's only *scholarly-practice* tour — being walked through how a biblical book became Latin, by the household that paid for that conviction. It is not a communal rite, but it is this world's own communal life at its most attested, and it may be the more honest "experience" of this world than any liturgical scene could be.

### 3.5 Nicene-Cappadocian — NOT ASSESSABLE; NO TOUR

The world's build folder (`worlds/Nicene-Cappadocian/`) is **empty as of 2026-07-16**. Construction has not begun: no Doc_09, no Story Inventory, no capsule, no Representative. Per this module's own rule that a tour can only be licensed by an approved Story Inventory, the verdict is automatic: **no tour, and nothing to analyze yet.** This is not a finding about the eventual world's evidence (the Cappadocian record may in time support strong scenes — that judgment belongs to its future Doc_02/Doc_09, not to this document). Action carried: re-run this section for World 5 when its Doc_09 is approved.

---

## 4. Architecture

Designed only now that §3 is done, because the scope follows from it: the module must serve **one Class A tour and three-to-four Class B tours across four worlds, with per-scene constraint lists that differ sharply** — so the architecture's core object is a per-scene manifest that carries those constraints, not a generic "tour engine" that assumes scenes are interchangeable.

### 4.1 The Tour Manifest — the module's core artifact

One manifest per tourable scene, authored on the construction side (not at runtime), derived **only** from an approved Doc_09 chunk, and subject to the same independent review cycle every construction document gets. Contents:

- **Anchor:** the story chunk ID (e.g. `pahcstory006`), its tier, and its class (A or B). The manifest may not cite material outside the anchor chunk (plus explicitly named satellite chunks) — the manifest is a *projection* of the chunk, never an extension of it.
- **Beats:** a small ordered sequence of scene moments, each carrying (a) narration text or narration bounds *in the Representative's own voice and register*, (b) the specific sourced elements it may draw on (for Class B, mapped one-to-one against the chunk's own Source Identification), and (c) any **honest-silence beat** the sources require (the Desert synaxis threshold; the unrecorded hymn texts).
- **Register banner text:** the persistent participant-facing marking — Class A: *"A witness's own account — Justin Martyr, writing c. 155"*; Class B: *"A reconstruction of typical practice — no single recorded event; every element sourced"* — displayed for the tour's whole duration (Article 17's visible-confidence rule, applied to a mode instead of a sentence).
- **Refusal list:** the scene's own Do-Not conditions, inherited from the chunk's Do-Not-Retrieve-When plus tour-specific additions (PAHC: no generalization beyond Rome, no blending the three eucharists; Syriac: calendar detail named as Nisibene, not offered for the Persian side as-is; Desert: no synaxis interior, no diet/hours; HAL: no horarium, S11 never a specific episode).
- **Entry/exit:** the invitation line (in-voice), the threshold framing, and the return-to-conversation handoff.
- **Visual assets, if any:** each image bound to a beat and to a Native registry row, with its caption and its own "what this does not show" line (§2.4, option 2 only, until a visual pipeline exists).

**Future handoff named plainly:** a new L4 template — *Tour Manifest Template* — with the same review-gated build cycle as every other construction document, plus a validation-suite extension (the current probe battery has no scene-narration/Generating-under-narration probe category; tour mode must not ship on conversational validation alone).

### 4.2 Invitation, acceptance, and exit — Participant Agency in the mechanics

- The invitation is **surfaced by the Representative in-voice** when the anchor chunk's Retrieve-When conditions fire, rendered in the UI as a visibly distinct, optional card (so the participant sees it as a door, not as the conversation's mandatory next step). It can also be participant-initiated from the world's info surface ("what can this Representative walk me through?" — including, for non-tourable worlds, the honest refusal text).
- **Explicit acceptance is required** before any mode shift; declining leaves the conversation exactly as it was, and the Representative does not re-offer unprompted within the session.
- **Exit is one action, available at every beat**, and exiting is never framed as abandonment. Interrupting with a question is not exiting — Q&A inside a tour is the point of hosting.
- The Facilitator's threshold role (welcome/introduction/close, per the L3D Table Process) extends naturally: the Facilitator frames what a tour is at the threshold, in its own already-established voice, and the tour runs inside the ordinary two-party table without new turn-management machinery.

### 4.3 The Representative's role shift, and the guardrails that hold it

In ordinary conversation the Representative is a *witness answering*; in a tour it is a *host narrating* — same person, same formation, same honesty, different rhetorical stance. The shift is implemented as a **mode overlay on top of the unchanged Permanent Prompt** (never a replacement prompt): the overlay grants narration stance, binds it to the manifest's beats and register, and restates the no-new-texture rule. Guardrails, in order of importance:

1. **Tier-register lock** (§2.3) — enforced by the manifest's per-beat sourcing, not by model goodwill.
2. **No-new-texture rule** — the generalized removed-diet-element precedent: unsourced sensory/procedural detail is absent, not hedged. This is the module's version of No Tier 5.
3. **Facilitator drift monitoring stays fully on**, with **Generating** treated as tour mode's primary drift signal (narration is the highest-temptation surface for invented texture the product will ever have). Temporal bleed and Smoothing also gain new surface area (a host walking a scene is one modern-idiom slip away from a museum docent).
4. **Q&A drops to ordinary mode:** a participant question inside a tour is answered with the standard conversational stack (full retrieval, all standing rules) — the tour never creates a *reduced-guardrail* state, only an *additional-structure* one.
5. **Tours end.** The mode has a defined exit; a session cannot be left ambiguously "in a scene."

### 4.4 Forward-looking technical integration note (`cic-poc`) — not a build task

If this were ever built, the touch points in the existing structure would be:

- **Backend:** a `tour_manifest.py` sibling to `world_manifest.py` (same single-source-of-truth pattern the manifest refactor already established — one entry per tour, keyed by world_id + tour_id); a tour-mode flag in conversation state; a prompt-assembly path that layers the mode overlay over the existing permanent prompt + capsule; retrieval scoping that pins the anchor chunk during narration beats while leaving Q&A retrieval unrestricted; the SSE stream gains a beat/mode annotation so the frontend can render the register banner and beat position. Facilitator monitoring pipeline unchanged in structure, extended with the tour-mode signal emphasis.
- **Frontend:** an invitation card component; a tour view (register banner persistent, beat position visible, exit affordance always on screen); the world-selection surface gains the tours-available / honest-refusal line per world.
- **Content/data:** Tour Manifests live alongside story chunks under each world's data dir; no change to lexicon/story chunk formats — the module reads them as-is.
- **Explicitly untouched:** the construction pipeline for worlds themselves; the existing encounter flow for participants who never accept a tour; Phase One testing.

---

## 5. What This Module Refuses, Restated Once

"We could imagine a plausible service based on general Christian custom of the era" is precisely the move this module exists to refuse — for a sentence, for a beat, and for an image alike. The per-world verdicts in §3 are not placeholders awaiting content: the Desert synaxis's interior, the Bethlehem horarium, and the whole Nicene-Cappadocian world are *closed* until their worlds' own records open them. "A generated story, however well-intentioned, is not witness."

---

## 6. Future Handoffs (named plainly, not started)

1. **L4 Tour Manifest Template** + review-cycle definition (construction-side; prerequisite to any tour existing).
2. **First Tour Manifest build: PAHC / Justin's Sunday gathering** (Class A flagship; strongest evidence, already-live world).
3. **Validation-suite extension:** scene-narration probe category (Generating-under-narration, register-persistence, refusal-list adherence) — tours do not ship on conversational validation alone.
4. **Visual-asset pipeline decision** (separate, funding-adjacent): confirm description-first default; scope option-2 rights/caption process for the Desert world's Kellia material if wanted.
5. **`cic-poc` build items per §4.4** — only after 1–3 exist and only when Phase Two is actually opened.
6. **Re-run §3.5 for Nicene-Cappadocian** when its Doc_09 is approved.
7. **Spoken-Syriac pronunciation research pass** (construction-side) — 4th-century pronunciation is itself a scholarly reconstruction with East/West disputes; required before any Tour Manifest claims recited Syriac aloud. Same pass should settle who sang refrain versus stanzas (§3.2, Sound findings).

---

## 7. Question Status (updated at V0.3 — project-lead rulings received 2026-07-16)

**Q1 — The Syriac boundary call — RESOLVED: "let the source make the call."** The Syriac tour proceeds on syrstory009's own license; the capsule's self-limit governs unscripted expansion, not the world's reviewed chunk. Adopted as the general rule for boundary tensions of this shape, with the corollary that more source-supported choice and variety per world is a good to pursue, never a risk to minimize — provided every added experience is source-licensed (§2.6).

**Q2 — Visual strategy default — STANDS.** Not separately re-confirmed, but the project lead's "whatever meets the need and is cheapest" ruling affirms it: description-first remains the launch shape, registry-licensed artifact imagery only where a world's own registry supports it, commissioned illustration deferred.

**Q3 — Paywall — RESOLVED: no paywall planned; everything accessible** (§2.5). If tiering is ever revisited, the evidentiary-absence-is-never-a-locked-feature commitment binds that conversation.

**Q4 — Sound layers — RESOLVED IN PART** (§2.7). Audio is licensed only for source-grounded performative moments (a teaching given, singing/recitation); the Syriac audio is decided as Syriac-language with English subtext/captions, other languages eventually. The Oxyrhynchus exhibit and the living-tradition comparison were not selected — **deferred, not planned**, consistent with cheapest-that-meets-the-need.

**Remaining open:**

1. **Confirm the "representative is voice only" interpretation (§2.7):** this document reads it as *the Representative is never audio-dubbed or visually depicted — its presence stays its written voice, with produced audio reserved for performative source moments.* If Mark meant something else (e.g., an audio-spoken Representative), §2.7's fourth bullet changes.
2. The construction-side prerequisites already in §6 (pronunciation pass; refrain-vs-stanza performance-role verification) before any Syriac audio is produced.
3. Mark's rulings list ended with an empty item 5 — held open in case a fifth thought was cut off.

---

## Document Log

- **2026-07-16 — V0.1 DRAFT created** in the dedicated Tour/Hosted Experience Module thread (Phase Two planning; no code touched). Grounded in direct reads of: all four live Doc_09 Story Inventories (PAHC 2026-07-07/08; Syriac 2026-07-08 incl. Validation Layer; Desert Doc_09a; HAL Doc_09a 2026-07-12); deployed capsules, permanent prompt (PAHC), and story chunks (`pahcstory006`, `syrstory009`, `desertstory008` read in full); `world_manifest.py`; L3D One-Representative Table Process V1.0; and verbatim extractions from Vision V1.1, Constitution V2.2 (Articles 6, 17, 19, 28, 30), and Construction Framework V7.3 (four tiers, No Tier 5, Story Inventory Requirement, Absent Stories). Companion decision-log entries recorded the same day in `CiC_Tour_Experience_Module_Decision_Log.md`.
- **Naming note:** the Framework's own name for Doc_09 is "Story Inventory"; "Story Repository" is the informal name used in some threads and the chunk-template title. This document uses the Framework's name except when citing files that use the other.
- **2026-07-16 — V0.2 DRAFT** (same day, after the project lead's exploration of the Syriac choir/sound question in-thread). Added: §2.6 (the experiential palette — "let the sources perform themselves" — and the refused composite-with-disclaimer move); §3.2 Sound findings (words/form/sound split; no period music exists within this world's horizon; Oxyrhynchus hymn barred by cross-contamination discipline; **decided:** voiced madrashe use multiple women's voices, per the attested bnat qyama choir, spoken not sung); §6 item 7 (pronunciation research pass); §7 Q4 (the three optional sound layers). Grounding added this pass: `syrlex004_madrasha.md` (Tier 1 lexicon chunk) read in full. All decisions and reasoning logged the same day in `CiC_Tour_Experience_Module_Decision_Log.md`.
- **2026-07-16 — V0.3 DRAFT** (same day, on the project lead's rulings). Q1 resolved ("let the source make the call" — Syriac tour proceeds; source-supported variety encouraged); Q3 resolved (no paywall planned, everything accessible — §2.5 rewritten); Q4 resolved in part (new §2.7 Audio policy: text default, audio only for source-performative moments, Syriac audio in Syriac with English captions, other languages eventually; Oxyrhynchus exhibit and living-tradition comparison deferred, not planned); Q2 stands via the cheapest-that-meets-the-need principle. §7 converted to a question-status section; one interpretation flagged for confirmation ("the representative is voice only" read as never audio-dubbed or visually depicted). File name retains V0_1 for link stability; the version of record is this log.
