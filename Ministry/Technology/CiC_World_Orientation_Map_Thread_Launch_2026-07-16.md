# Launch prompt — World Orientation & Selection Map thread

Paste this into a fresh thread. This is a **new, currently-out-of-system product
concept** — an interactive visual map letting a participant orient themselves across
two thousand years of Christian history before choosing who to talk to. It is deliberately
scoped as its own project, separate from the live `cic-poc` front-end and separate from
the general front-end-strategy thread, because it is not being built into the running
app yet. It may eventually integrate into the live world-selection flow — that
integration decision, and its timing, belongs to the front-end thread when this project
is mature enough to hand off, not to this thread to decide or implement unilaterally.

**Scope note, read this first:** this thread designs and specifies the map — its data
model, its content (which historical movements appear, where, and why), its interaction
design, and the honest "what's built vs. not yet built" transparency layer. It does not
touch `cic-poc` code. Where this thread's work implies a concrete build item for the
live app, name that plainly as a future handoff, the same discipline every other thread
in this project already follows.

---

## The core idea, stated exactly as given

An interactive **World Orientation and Selection Map**: a scrolling, interlinear
timeline (think the "who lived in relationship to whom" visual style used in Bible-
history timelines) that visually presents Christian worlds across history — their
development, relationships, influences, and historical context — so a participant can
confidently choose which world(s) to enter and converse with.

**The specific five-step workflow this map exists to serve:**
1. Introduce the world.
2. Orient the user within Christian history.
3. Show relationships to other worlds.
4. Help them decide where to go.
5. Launch them into conversation.

**The transparency requirement, stated exactly as given:** the map spans all of
Christian history, past and present — not just the worlds currently built. It
highlights which worlds exist today, which are intended/in progress, and — critically —
gives an honest, clickable explanation for real historical movements that are **not**
in the conversation set: naming plainly that a movement is real and important, and that
the reason it isn't here yet is usually that the project doesn't yet have the source
ecology to build a genuine living-ecology world from it (not that it was judged
unimportant). This is the same honesty-over-simplification posture the project already
applies everywhere else, extended to the map of the whole landscape itself.

**Interaction model, stated exactly as given:**
- **Hover** on a world/movement → lightweight options: add to conversation, get more
  information, take a tour, etc.
- **Click** → the deeper service/product (full description, source-ecology status, and —
  for live worlds — the actual entry point into conversation).

---

## What already governs this, read in this order

1. **`Ministry/Communication/Vision, Mission, Convictions, and Foundational
   Commitments V1.1.docx`** — the Why. Two convictions are directly load-bearing for
   this specific product:
   - **Conviction 1** (no single movement exhausts the richness of Christ — together
     they form a vast testimony) is the entire reason a *landscape* view, not just a
     picker, is worth building at all. The map's job is to make that testimony visible
     as a testimony, not just a menu.
   - **Conviction 4** (authentic encounter requires trustworthy transparency — nothing
     essential hidden) is the direct justification for showing real movements that
     aren't built yet, honestly, rather than only showing what's ready to sell.
   - **Foundational Value: Historical Responsibility** — the map itself must hold the
     same discipline the world-builds do: not overselling thin coverage, not silently
     omitting movements whose absence might read as a judgment on their importance.

2. **`L1-Foundation/CiC_L1_Constitution_V2_2.docx`** — the What. Article 6's Encounter-
   Success Standard applies to the map's role in the encounter too: does the map help a
   participant arrive at a world with real, honest expectations (informed consent about
   what they're about to meet), or does it oversell/undersell any world relative to what
   it actually is.

3. **`L3B-World-Build-Methodology/CiC_L3B_Formation_World_Blueprint_V7.3.docx`** and
   **`CiC_L3B_Formation_World_Construction_Framework_V7.3.docx`** — the How. This
   thread's "why isn't X built yet" explanations must be grounded in the actual
   construction pipeline's own criteria — specifically **Source Ecology assessment**
   (Doc_02) and **Gravity Discovery** (Doc_04, see `anthropic-skills:cic-gravity-index`)
   — not an invented or vague "we haven't gotten to it yet." If a movement genuinely
   lacks the source density/attestation to pass Source Ecology, that is the honest,
   specific reason to give a curious participant who clicks on it — not a placeholder.

4. **Current world-build status, so this thread doesn't have to rediscover it:**
   - **Built and live** (all four in `cic-poc`): The House-Churches (Chloe, 70-200 CE),
     Syriac Christianity (Mar Yausep, 200-410 CE), Desert Fathers and Mothers (Papnoute,
     c. 320-430 CE), The Bethlehem Circle (Albina, c. 382-420 CE).
   - **Started, not yet built:** `World-Builds/Nicene-Cappadocian/` exists as a folder
     but is currently empty — no construction has begun.
   - **Substantial prior work exists outside the active build tree:** an earlier
     "Alexandria" world build (Logos-centered catechetical tradition) exists in
     `OneDrive/Desktop/Church in Conversation/Former Versions/` (V6 and V7 tracks) —
     real prior construction documents, previously discussed as a strong candidate for
     a future world alongside Nicene-Cappadocian, not yet formally resumed.
   - **Not started at all, but real and worth the map naming honestly:** the map's
     "why not yet" content will need real Source Ecology judgment calls for movements
     spanning the rest of Christian history — e.g. Nicene/Chalcedonian councils'
     surrounding communities, Byzantine/Eastern Orthodox monasticism, Coptic and
     Ethiopian Christianity, medieval Western monasticism, the Reformation-era
     movements, Anabaptist/Radical Reformation communities, Pentecostal/Charismatic
     origins, and contemporary living traditions. This thread should not assume any of
     these are automatically buildable — some may fail Source Ecology for a
     conversational-community voice even where ample *institutional* history exists.

5. **`Ministry/Technology/CiC_FrontEnd_Decision_Log.md`** — read in full, so this
   thread's map design doesn't contradict or duplicate existing front-end decisions
   about world selection, the "Deep Interview" vs. "Compare Worlds" entry framing, or
   the four-role onboarding model already planned there.

## What to produce

1. **A landscape data model.** For every candidate movement/era across two thousand
   years (not just the four live worlds), capture: approximate time span, region,
   relationships/influences to other movements (who formed whom, who reacted against
   whom, shared vs. divergent lineage), and a build-status field: *Live*, *In
   Construction*, *Identified Candidate* (real prior work exists, e.g. Alexandria), or
   *Not Yet Assessed / Source Ecology Uncertain*. This is the map's actual content
   spine — get this right before any visual design work.

2. **Honest "not yet" content.** For movements that have been through even an informal
   Source Ecology look and found wanting, draft the actual clickable explanation text a
   curious participant would read — modeled on the honesty already established in the
   four live worlds' own tile-copy sourcing-richness disclosures (see
   `backend/app/world_manifest.py` in `cic-poc` for that precedent and its tone). Don't
   invent evidentiary judgments here that haven't actually been made — where a real
   Source Ecology assessment hasn't happened yet for a movement, say that plainly too
   ("we haven't yet assessed whether the sources exist to build this honestly") rather
   than fabricating a verdict.

3. **The five-step interaction flow, designed concretely.** Work through what each of
   the five steps (introduce → orient in history → show relationships → help decide →
   launch into conversation) actually looks like as a UI sequence, and what the
   hover-vs-click distinction surfaces at each stage (hover: lightweight options; click:
   the deeper product). Reference existing visual patterns for interlinear/relational
   historical timelines to ground the "scrolling timeline" concept concretely rather
   than describing it abstractly.

4. **A future-integration note, not an integration.** Once the above is drafted,
   produce a short handoff describing how this map *could* eventually connect to the
   live app's world-selection flow (e.g. replacing or supplementing the current
   "Single Representative / Multiple Representatives" toggle) — as a proposal for the
   front-end thread to evaluate on its own timeline, not a mandate or a build task for
   this thread to execute.

## Coordination boundary, stated plainly

This thread designs the map — its content, its honesty about what's built and what
isn't, its interaction model. It does not:
- Touch `cic-poc` frontend or backend code.
- Decide when or whether this gets integrated into the live world-selection flow —
  that's the front-end thread's call, once this thread hands off a mature proposal.
- Make Source Ecology or Gravity Discovery determinations informally — if this thread
  needs to know whether a movement is genuinely buildable, that assessment should be
  requested from (or run using) the actual Construction Framework methodology, not
  guessed at for the sake of map content.

## Logging

Log real decisions and open questions in
`Ministry/Technology/CiC_World_Orientation_Map_Decision_Log.md` as they happen — same
dated-entry discipline (what was decided, the reasoning including the heart of it, the
next action) already in use in the other threads. Don't let a real decision live only
in this thread's own conversation history.
