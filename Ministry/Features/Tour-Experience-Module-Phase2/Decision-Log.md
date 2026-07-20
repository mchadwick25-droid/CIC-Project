# CiC Tour / Hosted Experience Module — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning —
including the "heart" reasoning, not just the design logic — and the specific next
action. A decision that only lives in conversation history is one that gets
re-litigated or lost by accident later.

Scope: a Phase Two, currently out-of-system product concept — a hosted "tour" mode
where a Representative walks a participant through a reconstructed communal experience
(worship service, shared meal, specific rite), grounded strictly in what the sources
allow, offered only for worlds where a real sourced scene exists. This thread does not
touch live `cic-poc` code and does not affect the current prototype or Phase One
testing.

---

## 2026-07-20 — Technical build spec written, explicitly for later implementation

**Mark's direction:** hold all Hosted Tour work — the one existing draft (Chloe's
Sunday-gathering demo) needs substantial content editing, and this is its own project
for after token reset (Friday 2026-07-24). In the meantime: "go ahead and design for
later implementation."

**Produced:** `CiC_Tour_Build_Spec_V0_1_DRAFT.md` — the engineering layer the strategy
doc's own §4.4 explicitly declined to be ("a forward-looking technical integration
note... not a build task"). Covers: the `TourManifest`/`TourBeat` data model
(mirroring `world_manifest.py`'s exact single-source-of-truth pattern), three new
`ConversationState` fields, why tour eligibility rides existing retrieval rather than
a new classifier (unlike the frame-breaker/modern-term/epistemology bridges), the new
`tour_mode.py` module and its three functions, the new `/tour/start`, `/tour/next`,
`/tour/exit` API surface, and the frontend components (invitation card, tour view,
world-selector honest-refusal line). Explicitly does not decide beat content,
validation-probe wording, or anything gated on the strategy doc's own Handoffs #2-#4.

**Gating restated:** Increment 1 + Increment 2 merged, a real first Tour Manifest
authored and reviewed (Handoff #2), and the validation-suite extension (Handoff #3) —
all still open, all still the reason nothing here gets built yet.

**Next action:** none until the gates above clear. Update this log again only once
actual build work starts.

---

## 2026-07-16 — Founding pass: strategy, evidentiary analysis, and architecture drafted (V0.1)

Full document: `Ministry/Technology/CiC_Tour_Experience_Module_Strategy_V0_1_DRAFT.md`.
The entries below record the real decisions and the open questions, so none of them
live only in the thread's conversation history.

### Decided: a tour is a presentation mode over approved Doc_09 story chunks — never a new content class

The module's evidentiary bar is not invented fresh; it already exists as the
Construction Framework's four-tier story classification and the No Tier 5 rule, and
each world's approved Story Inventory already is the licensing system. If a scene is
not a licensed story chunk, it cannot be toured — the tour adds a presentation layer
and guardrails, nothing upstream. **The heart of it:** a tour is a structurally
higher-stakes claim than a conversational answer ("this is what a morning gathering
looked like," not "here is what I can tell you"), so under Historical Responsibility
it must sit on *more* evidentiary weight, not less — and the safest way to guarantee
that forever is to make it architecturally impossible for a tour to say anything the
world's own signed record hasn't already licensed. "A generated story, however
well-intentioned, is not witness" (Framework V7.3, No Tier 5).

**Next action:** none until Phase Two opens; the future handoff list (§6 of the
strategy doc) starts with the L4 Tour Manifest Template.

### Decided: two tour classes, and no third

Class A (attested-scene, Tier 1 anchor — "here is what one witness tells us, in his
own words") and Class B (reconstruction, Tier 4 anchor — "a morning such as ours
might keep," with the reconstruction marking persistently visible for the tour's
whole duration, not just disclosed at the threshold). A world with neither gets no
tour, and the refusal is shown honestly — the "why is there no tour for this world"
answer is itself a mission surface, arguably the most Conviction-4-expressive screen
the product could have, because it is the exact point where any ordinary product
would fabricate.

### Recorded: per-world evidentiary verdicts (the lookup table a future builder needs)

- **The House-Churches — YES, strongest case.** Anchor `pahcstory006` (Justin's Sunday
  gathering, *First Apology* 65–67, **Tier 1** — the only Tier 1 narrated liturgical
  description in the whole live portfolio). Satellites available at Tier 4 (009, 010,
  011, 012). Constraints: Rome-only, never network-generalized, three eucharistic
  practices never blended, and no visual record exists (world archaeologically
  invisible; Dura-Europos and Abercius are Excluded registry rows).
- **Syriac Christianity — QUALIFIED YES, Class B only.** Anchor `syrstory009` (morning
  qyama gathering, **Tier 4**; the world has zero Tier 1 entries anywhere, per its own
  Doc_09 finding). Constraints: scene bound to pre-363 Nisibis; Mar Yausep is
  Persian-anchored; one genuine boundary call flagged for Mark (below, Open Q1).
- **Desert Fathers and Mothers — PARTIAL.** A daily-rhythm tour yes (`desertstory008`,
  Tier 4, Strand C only); a worship-service tour **no** — the synaxis is attested in
  one sourced sentence (shape and hour), its interior is not narratable, and the
  capsule says so in the world's own voice ("shape and its hour, not... its every
  phrase"). The honest-silence threshold at the synaxis door is itself a tour beat,
  and possibly the most formation-true moment this module could produce anywhere.
- **The Bethlehem Circle — PARTIAL/THIN.** Shared-life tour possible (`hal_story10`,
  Tier 4, explicitly no liturgical horarium — "which hours, which psalms" is not
  attested and not manufactured); `hal_story11` (translating a book) could ground a
  scholarly-practice tour but must never be narrated as a specific episode. No
  congregational/liturgical tour is possible at all (Absent Stories item 6: structural
  feature of the world, not a gap). Newest, least live-tested world — goes last.
- **Nicene-Cappadocian — NOT ASSESSABLE, no tour.** Build folder empty as of
  2026-07-16; no Doc_09 exists. Re-run the analysis when its Story Inventory is
  approved.

### Decided (as recommendation, pending Mark): description-first visual strategy

The project has no visual-asset pipeline of any kind, and the analysis found an
inversion worth stating plainly: **the most textually tourable world (PAHC) is the
least illustrable** — its own record excludes the famous visuals (Dura-Europos), so
the flagship tour cannot be illustrated from its own evidence at all, while the one
world with registry-licensed archaeology (Desert, Kellia excavations) has the thinner
tour. Recommendation carried in the strategy doc: description-first as the module's
launch shape; registry-licensed artifact imagery permitted only where a world's own
registry supports it; commissioned illustration deferred as a separately-resourced
"visual Tier 4" program with its own template and review cycle; generative-AI imagery
treated as presumptively prohibited (pictorial Tier 5 by construction). **The heart of
it:** an image is a claim that cannot hedge — a picture has no register for
Inferential/Thin — and the encounter is supposed to stay with the witness, not the
picture (Conviction 5).

### Open questions carried to Mark (not decided here)

1. **The Syriac boundary call.** Yausep's deployed capsule limits him to speaking
   "only briefly of the gathering itself," yet `syrstory009` is an approved,
   element-sourced scene built exactly for that territory. Leaning stated in the
   strategy doc: the licensed chunk is the world's own reviewed exception to the
   capsule's self-limit, which governs unscripted expansion. But this is a judgment
   about a live world's own self-understanding — Mark's call, not the thread's.
2. **Visual strategy default** — confirm the description-first recommendation above.
3. **The paywall/honesty seam.** If tours become a Level 2 paid offering, commit now
   that evidentiary absence is never presented as a locked feature: the "no tour
   exists for this world" screen stays identical and free everywhere. Worth logging
   as a standing commitment before any pricing work, because every off-the-shelf
   paywall pattern will get this wrong by default.

**Next action:** Mark reacts to the V0.1 draft (especially the three open questions);
on his reaction this either proceeds to the L4 Tour Manifest Template handoff spec or
parks cleanly as a Phase Two shelf item.

---

## 2026-07-16 — Mark's question: can the Syriac tour reproduce a choir or song?

Answered from the world's own record (`syrlex004_madrasha.md`, Tier 1;
`syrstory009`'s Source Identification; Source Registry rows #1–2), split three ways:

- **The words — yes.** Ephrem's madrashe survive as texts and are this world's own
  registered primary material (Registry #1 *Hymns on Faith*, #2 *Contra Haereses*).
  A tour beat can give an actual stanza-and-refrain, relayed and attributed ("words
  Ephrem set for the choirs"), with the translation named as translation — and with
  the honest note that the meter and acrostic, which the world's own lexicon entry
  identifies as part of the formation technology, are largely lost in English.
- **The form — yes, likely.** The stanzaic structure with refrains (ʿonyata) is
  attested in the lexicon entry itself; a participant could plausibly be shown, even
  handed, the refrain's role in performance. Exactly who sang refrain vs. stanzas
  needs a construction-side verification pass before a Tour Manifest states it.
- **The sound — no.** No musical notation survives from this world's window; melody
  titles survive in later manuscript rubrics, the melodies themselves do not. Any
  sung/audio reconstruction is invented music — audio Tier 5. Modern Syriac chant
  (Syriac Orthodox / Church of the East) is a living tradition's present voice, with
  centuries of unverifiable oral transmission between it and this world; presenting
  it as "what the bnat qyama sounded like" would cross the historical-witness vs.
  living-tradition line the Vision doc draws, on the exact world whose facilitator
  cautions already guard living-heritage sensitivity.

**The heart of it:** "the tune is lost; the words remain" — said by Yausep inside the
scene — is not a diminished version of the choir; it is the world telling the truth
about itself, and it is exactly the honest-silence beat the module was designed
around. The choir's silence is part of the tour.

**Open sub-question added (rides with Open Q1):** whether a clearly-labeled,
opt-in living-tradition comparison ("how communities descended from this world sing
madrashe today — a different claim than history") is wanted at all. It is defensible
under Three-Level Transparency but deliberately crosses the historical/living line,
so it is Mark's call, not the thread's.

---

## 2026-07-16 — Mark's follow-up: other period songs to composite from, labeled "it may have sounded like…"?

**The factual finding: no usable period music exists within this world's horizon.**
Nothing notated survives from Syriac Christianity's own window (200–410, Edessa/
Nisibis/Persia) — not for Ephrem, not for Bardaisan (whose hymn texts survive mostly
as fragments quoted by Ephrem to refute them, with no music). The nearest real
artifact anywhere in early Christianity is the Oxyrhynchus hymn (P.Oxy. 1786, Egypt,
late 3rd c.) — the earliest Christian hymn with surviving musical notation — but it
is Greek-language, Egyptian, a different tradition and genre, and **not Native to
this world's evidence base**. The project's own cross-contamination discipline
(applied explicitly in HAL Doc_09a §3: no borrowing from a neighboring world's
evidence) bars exactly this move. Beyond that: Greek pagan fragments (Seikilos
epitaph, Delphic hymns) are further afield still, and Jewish cantillation traditions
have no ancient notation. There is nothing to draw from that is this world's own.

**The governance finding: "put things together + say it may have sounded like" is
the disclaimed form of the move the module refuses.** The recommendation logged here
is no, on three grounds:

1. **It fails the Tier 4 test element-by-element.** Tier 4 licenses composites where
   "every element is traceable to attested evidence within the world's own horizon."
   For a melodic composite, the elements (scale, melody, vocal style, tempo) are
   precisely the things not attested — so it would not be assembling attested
   elements, it would be inventing all of them while borrowing authority from
   adjacent cultures. That is the Framework's own definition of generated material.
2. **A disclaimer does not neutralize a sensory claim.** Text can hedge mid-sentence;
   sound cannot. Whatever the label says, the participant leaves with *a* sound as
   the memory of "what the choir was like." The project's own precedent points the
   other way: the Desert world's unsourced diet element was removed, not
   retained-with-a-caveat, per the Template's explicit rule.
3. **The bar is constitutional, not thread-level.** Article 19: "free invention is
   prohibited at every stage of construction and deployment." No Tier 5's own text:
   "If the evidence does not support a story, the story does not exist for this
   world." A "may have sounded like" composite would need those rules amended, not a
   feature approved — named plainly so the real size of the decision is visible.

**What IS legitimately available instead** (recorded so the "no" doesn't read as
bare refusal): (a) the attested texts, refrain structure, and syllabic meter —
Ephrem's meters are in the texts themselves, so the *rhythm* of a madrasha is
attested even though the melody is not; (b) possibly the spoken Syriac words aloud —
with the flag that 4th-century pronunciation is itself a scholarly reconstruction
with East/West disputes, needing its own sourced research pass before any Tour
Manifest claims it; (c) an explicitly outside-this-world Level 3 exhibit of the
Oxyrhynchus hymn as "the only notated Christian music within a century of this
world — from a different place, language, and tradition; here is how little we
know" — honest as an artifact about the limits of evidence, permissible only if
never blended into the scene itself; (d) the living-tradition comparison already
logged above. Options (b), (c), (d) are all Mark's boundary calls.

**Next action:** Mark decides among (a)–(d); (a) is recommended as the default tour
content regardless of the rest.

---

## 2026-07-16 — Mark's creative resolution: women's voices, and the "sources perform themselves" palette

**Decided (Mark's own idea, endorsed by the thread): the spoken Syriac can be
multiple women's voices.** Checked element-by-element against the record: women —
attested (the bnat qyama choir, Harvey's scholarship in syrstory009's Source
Identification); multiple — attested (a choir is plural); the words — attested
(Ephrem's texts, Registry #1–2); spoken rather than sung — deliberately *withholds*
the one unattested element (melody) instead of inventing it. Once voiced at all,
women's voices are arguably required for fidelity: a lone male narrator would
misrepresent the attested performance context more than a women's ensemble does.
Guardrails: framing must present it as text-in-the-attested-voices, not performance
reconstruction (no unison/style/pacing claims); the contested-pronunciation research
pass still applies; and the tour carries the world's own Absent Stories truth — no
bnat qyama woman's own composed word survives, so women's voices carrying a man's
words is the record's own shape, said aloud rather than smoothed.

**The heart of it:** Mark went exploring for a way to give people *more* and landed
on a move that adds experiential richness by conforming to the evidence more
closely, not less — the withheld melody does the witnessing. This exchange is the
module's method in miniature.

**Principle adopted for the module: "let the sources perform themselves."** The
creative space is modal, not inventive: experiences are built only from attested
text (Justin's order of service; the Didache's Two Ways; Ephrem's stanzas; the
Psalter itself as the desert's own substrate; Jerome's prefaces), attested form
(meter, refrain, the sequence of a gathering, the shape of a week), attested roles
and voices (the letter read aloud to the gathering — PAHC's own network practice;
the catechumen being taught; the women's choir), and honest-silence beats. Every
world's tour palette is derived this way; nothing else is in the palette.

**Confirmed:** "no tour — nothing survives" remains a live outcome and is the rule
holding, not failing. Among the four live worlds the analysis found no total-zero;
the current zero (Nicene-Cappadocian) is unbuilt, not empty.

**Next action:** fold the palette and the women's-voices decision into V0.2 of the
strategy document once Mark settles the standing boundary calls (Syriac capsule
tension; spoken-Syriac pronunciation; Oxyrhynchus exhibit; living-tradition
comparison).

---

## 2026-07-16 — Project-lead rulings on the open questions (V0.3)

Mark answered the standing questions in-thread. Recorded as decided:

1. **Q1 resolved — "let the source make the call."** The Syriac tour proceeds on
   `syrstory009`'s own license: where a world's approved source material supports a
   scene, the tour exists; the capsule's self-limit governs unscripted expansion, not
   the reviewed chunk. Adopted as the general rule for every future boundary tension
   of this shape. **Corollary principle, Mark's own words in substance: more choice
   and more different experiences per world are good — but only when supported by
   the source material.** Tour families (e.g. PAHC's gathering / path-to-the-water /
   day-in-the-assembly) are encouraged wherever the sources license them.
2. **Q3 resolved — no paywall planning now.** The module is planned with everything
   accessible; tiering can be revisited later if the project goes that way. The
   standing commitment logged earlier (evidentiary absence is never presented as a
   locked feature) remains binding on any future revisit.
3. **Q4 partially resolved — audio policy: cheapest that meets the need.** No audio
   layers by default; audio only where the tour has a source-grounded performative
   reason — a teaching being given, singing/recitation (the women's-voices madrashe
   is the type case). **Decided: the Syriac audio is in Syriac with English subtext/
   captions, other languages eventually.** (Captions also serve accessibility, which
   fits the everything-accessible ruling.) The Oxyrhynchus exhibit and the
   living-tradition comparison were not selected — recorded as deferred, not
   planned, consistent with cheapest-that-meets-the-need.
4. **Q2 stands by the same principle.** Description-first visuals were not
   separately re-confirmed, but cheapest-that-meets-the-need affirms the
   recommendation; description-first remains the default.
5. **Interpretation flagged for confirmation:** Mark wrote "the representative is
   voice only." Read here as: the Representative is never audio-dubbed or visually
   depicted — its presence remains its written voice, with produced audio reserved
   for the source-performative moments above. Logged as an interpretation, not a
   settled ruling, until Mark confirms or corrects.
6. Mark's numbered list ended with an empty item 5 — noted so a dropped thought
   isn't lost; nothing invented for it.

**Next action:** fold rulings into strategy doc V0.3 (done same day); await Mark's
confirmation on item 5's interpretation and any content for his empty item.

---

## 2026-07-16 — Concept simulation built for Mark's demonstration video

**Decided and done:** at Mark's request, a standalone click-through simulation of the
PAHC/Chloe tour was built for him to screen-record as a demonstration of future
features. Published as a private artifact (Mark holds the link); source file kept in
the session scratchpad, deliberately NOT in `cic-poc` — it is a demonstration prop,
not product code, and touches nothing in the live prototype or Phase One testing.

**What it simulates**, matching the V0.3 architecture exactly: conversational
encounter → in-voice invitation card (with a working decline path — the open door is
demonstrated, not just claimed) → threshold screen (what this is / what it's built
from / what it will not claim) → seven hosted beats with a persistent Class A
register banner ("A witness's own account — Justin Martyr, First Apology 65–67") →
one scripted Q&A interruption (the who-presides question, answered with the world's
own unsettledness, tour paused not ended) → an honest-silence closing beat (no image
of any gathering place survives; Chloe declines to invent the room) → return to open
conversation. A "Step out" affordance is visible at every beat.

**Content discipline held:** every narrated line scripted only from licensed
material — pahcstory006 (Tier 1) for all seven beats and the two "Justin's own
words" pulls; the deployed capsule/permanent prompt for Chloe's voice (short plain
sentences, household's measure, two-paragraph cap respected); the closing
diversity-first references (Didache cup-before-bread, Ignatius one-table) are the
two practices the world's own chunks license and are named as distinct, per the
diversity-first rule. The simulation carries a visible "Concept simulation — not the
live product" footer naming its sources — the demo itself obeys Conviction 4.

**Verification note:** the page rendered in the session's browser pane, but the
automated browser driver was unresponsive, so the click-through was verified by
static inspection of the (deliberately simple) state machine rather than driven
end-to-end. Mark should click through once before recording; any glitch is a
one-line fix.

**Next action:** Mark clicks through, requests any script/voice adjustments, then
records. If the demo is shown outside the inner circle, the "concept simulation"
footer stays visible in the recording — same honesty rule as the product itself.

---

## 2026-07-20 — TR-4 and TR-5 built: the L4 Tour Manifest Template + review-cycle
## definition, and the Tour Eligibility Gate checklist

**What this is:** the strategy document's own first future handoff (§6, item 1 — "the
L4 Tour Manifest Template... prerequisite to any tour existing"), plus its natural
companion, both built as real, fillable planning artifacts: `CiC_L4_Tour_Manifest_
Template_V1_0.md` and `CiC_Tour_Eligibility_Gate_V1_0.md`, this same folder. Dispatched
against the Task Board's own DO NOW entries (TR-4, TR-5), which name these two items as
unblocked, no-code, no-live-system-risk work — text and process design only.

### Decided: both artifacts live here, not in `Hosted-Tour/`

Checked rather than assumed, per the dispatching instructions. `Hosted-Tour/`'s own
README names itself as "a self-contained immersive demo... built and verified for one
world" — a Phase One reference implementation, not a generalization thread. This
document's own founding entry (2026-07-16) already claims the generalization work as
this thread's own: "the future handoff list (§6 of the strategy doc) starts with the
L4 Tour Manifest Template." Neither `Integration-Notes.md` file states ownership in so
many words, but the strategy document's own §6 and this log's own prior "Next action"
lines are as explicit a claim of ownership as this project's documentation habit ever
makes without a dedicated line saying "X owns Y" — so followed that rather than the
weaker signal of silence in the other folder's Integration-Notes.md.

### Decided: "L4" names an artifact tier, not a folder claim

The dispatching brief guessed "L4" might mean an operational/deployed-experience tier.
Checked against the actual repo rather than trusting the guess: `L4-Templates/` at the
repo root is real, live, governed territory — a folder of fill-in-the-blank templates
for the Doc_01–Doc_10 world-build pipeline (Story Repository Chunk, World Capsule
Core, Voice Configuration, and others), each carrying the exact
builder-note/bracket/Final-Assembly-Instruction structure this new template also uses.
**The heart of it:** naming this "L4" is not decorative — it is a real claim that this
artifact is the *same species* of thing as those templates (a reusable construction
document subject to independent review), and that claim only holds if the new
document's actual shape matches theirs, which is why both new files were built to
mirror `Story_Repository_Chunk_Template.md`'s and `World_Capsule_Core_Template.md`'s
own conventions directly rather than inventing a new template shape. Filed under this
feature folder, not inside `L4-Templates/` itself, for two honest reasons named in the
template's own text: tours are not yet an approved part of the core pipeline (TR-14 is
still BLOCKED), and `L4-Templates/` is live, governed territory in its own right
(`CiC-L1L3-Foundation` branch work reconciled into it this same day, commit `2b86b8b`)
— not a place to add an unreviewed file uninvited. **Correction, System Hub review,
2026-07-20:** the original drafting pass claimed another thread "currently has active
uncommitted work" in `L4-Templates/` as part of this reasoning — checked directly via
`git status`/`git log` and that specific claim doesn't hold (the folder is clean,
nothing uncommitted there right now). The filing decision itself still stands on its
other, independently verified ground; only that one supporting detail was wrong, and
is corrected here rather than left standing uncorrected in the artifact's own text.

### Decided: the Tour Manifest's review cycle is the same rigor as every other
### construction document, narrower in scope, not lighter in standard

The strategy document had already answered the rigor question at its own founding
decision (§1.2) — a tour is a higher-stakes claim than a conversational answer, so it
needs *more* evidentiary weight, not less. What TR-4 actually still owed was the
mechanics: who reviews, against what, how many rounds. Landed on: independent
reviewer, no drafting involvement (this project's standing pattern, most recently run
in full on the Imperial-Juridical-Christianity build); a checklist that is narrower
than a Doc_09 review because a manifest may not cite anything outside its one already-
approved anchor chunk — so the review is a citation-fidelity and register-discipline
check, not a fresh evidentiary argument; and **minimum two rounds, a mandatory third
if Round 1 returns any HIGH finding** — not a flat "2–3," but the actual conditional
shape this project's own real review history shows (`Doc09_Round1_Review.md` found one
HIGH finding and the set needed a further round before it could be marked Cleared).
**The heart of it:** the temptation with a "smaller" artifact like a manifest is to
assume a smaller review will do. The reasoning that resists that here is Conviction
5's own logic turned toward images and sound specifically — a picture or a clip
"cannot hedge" the way a sentence can, so an error in a Tour Manifest's asset caption
or narration beat is *harder to walk back* once shown or played, not easier, even
though the manifest itself draws on less material than a whole Doc_09. Narrower input,
same consequence if the review misses something — so the same standard held, not a
lighter one.

### Decided: the Tour Eligibility Gate is the §3 method, made repeatable — not a
### fresh procedure

Every one of the Gate's eight steps was extracted from, and cited to, a real judgment
the strategy thread already made for one of its five worlds — Gate 1(b)'s
communal-vs.-biographical trap from the Desert world's three Tier-1 founding scenes;
Gate 2's narrated-vs.-thin-mention line from the Desert synaxis's own capsule wording;
Gate 5's four-part decline-stop check built directly from Chloe's own Stop 7 (the
room/the words/the people/the sound, each with its real citation); Gate 6's
visual/audio split from the PAHC/Desert imagery contrast and the Syriac sound findings.
Nothing in the Gate was invented fresh — the discipline this whole module runs on
("if the evidence does not support a story, the story does not exist for this world")
applies to the Gate's own construction as much as to any tour it will ever clear.
**One honest limit named in the Gate's own closing section, not smoothed over:** it has
only ever been reverse-engineered from a single pass across five worlds done by one
thread in one day. It has not yet been run fresh, end-to-end, by a different builder
against a new world — so whether its eight steps actually hold up under real second
use is still open, and the document says so rather than claiming a validation it
hasn't earned.

### Flagged, not resolved

1. **Neither new document has itself been through independent adversarial review.**
   Both are DRAFT V1.0, exactly as flagged in their own status lines — this thread
   built the artifacts TR-4/TR-5 ask for; running that review is separate work, not
   done here since it wasn't in scope.
2. **Who specifically staffs a Tour Manifest review** (a dedicated reviewer role vs.
   the existing rotating independent-agent pattern) is Mark's own staffing call,
   named as open in the template's own closing section rather than guessed at.
3. Confirmed via direct directory listing (2026-07-20) that `cic-poc/backend/app/`
   has `world_manifest.py` but no `tour_manifest.py` or any tour-related schema —
   TR-14 is genuinely future work, not something this pass could ground a manifest's
   field structure against beyond the strategy document's own §4.4 description of
   what that future file would need to look like.

**Next action:** these two artifacts unblock TR-7 (templated tour renderer) and TR-9
(scene-narration validation probe category) per the Task Board's own dependency chain,
and are themselves the prerequisite for TR-10 (formalizing the Chloe demo into a real,
reviewed Tour Manifest — the first real test of whether this template actually holds
up when filled in for the strongest, best-evidenced case in the portfolio).

---
