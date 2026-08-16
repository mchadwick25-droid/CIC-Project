# Gospel-question demonstrations — staging for the fix

**2026-08-16, follow-on to Worklist item 11 (VR_1A_WORKLIST.md) and the 2026-08-10
foundational-demonstration fix (VR_FOUNDATIONAL_DEMOS_STAGING_2026-08-10.md).**

## What this answers

A 12-conversation live probe (6 worlds x 2 conversations, run 2026-08-16 against
the deployed TestClient harness) confirmed the 2026-08-10 "who was Jesus" fix
holds for the question it targeted, in 4 of 6 worlds with real content and in
all 6 for at least some content. But a second, separate foundational question
asked later in the same conversation - "what is the gospel?" - showed the
identical displacement shape the fix was built to catch: four of six worlds
answered with a carrier (a transmission chain, a book's textual history, a
repeated call story, or an outright decline) instead of the gospel's own
content.

Two worlds (Chloe/post-apostolic-house-church, Theon/alexandria-catechetical)
already answer this question honestly and are NOT touched here. This document
stages the fix for the other four: Marius (imperial-juridical), Mar Yausep
(syriac), Albina (hieronymian), and Papnoute (desert).

## The bar, unchanged from 2026-08-10

Same as the original fix: every substantive line traces to a named record;
nothing invented; the world's own idiom carries the content, not a substitute
for it; readability and measure discipline per world.

## Per-world mining and disposition

### Imperial-Juridical (Marius) — genuinely empty store, new source mined

Full-store search (12 term / 6 story / 9 figure / 10 demonstration / 7 gravity
/ 10 force / 5 contested_claim / 1 world_core / 41 source records) found ZERO
soteriological content anywhere. No record quotes or paraphrases the creed's
"for us and for our salvation... was crucified... rose again" clause. No term
defines redemption, atonement, or grace. Closest existing material
(ijclex006, ijclex009, ijcdemo010) is exclusively about Christ's NATURE
(homoousios, two natures), never about what his death/resurrection
accomplishes.

**Root cause identified**: this world's own `world_core` (ijccore001) `telos`
field defines the whole world's purpose as *"what was first given was not an
office or a rank at all, but Christ himself, entrusted to Peter and the
apostles and, through them, to every see that can still show its claim traces
back to that entrusting"* - custody/transmission language with zero
saving-content, almost certainly the literal source of the live probe's bad
answer ("God gave himself to be guarded and handed on..."). `ijccore001` is
NOT touched by this pass - it is a foundational identity document, not a
single demonstration, and a change to it is a bigger decision than this fix
scopes. Flagged here as a further open item, not resolved.

**New source mined**: srcIJC42, the Niceno-Constantinopolitan Creed (381),
checked directly against this project's own vendored NPNF2-14 transcription
(cic/texts/npnf214_seven-ecumenical-councils.xml, div2 id="ix.iii", paragraph
id="ix.iii-p6") - the first source in this world's own record store checked
directly against a vendored primary text rather than carried from builder
prior knowledge. Full soteriological clause quoted verbatim in the source
row's own body.

[2026-08-16 correction, per independent adversarial review of
ijcdemo011/ijclex013/srcIJC42]: this paragraph originally claimed the same
vendored file "already used for srcIJC46/47 (2026-08-15)" - those source IDs
belong to a separate, parallel record tree (cic/records/), not this world's
own wrs/records store, and do not exist here. The false cross-reference has
been struck from this document and from srcIJC42.md/ijclex013.md themselves.

**New term authored**: ijclex013 ("pro nobis" / "for us") - the creed's own
"for us... for our salvation" clause as this world's own vocabulary for the
gospel's content, distinct from and complementary to ijclex006's homoousios
(who he is) and ijclex009's Tomus (the two natures settled).

**New demonstration**: ijcdemo011, modeling "what is the gospel" the same way
ijcdemo010 modeled "who was Jesus" - content first, machinery subordinated to
it, the world's own juridical idiom (a clause a council SAT to confess, not
merely an office to guard) carrying the answer.

### Syriac (Mar Yausep) — thin but workable from existing records

Full-store search found no term for sin/ransom/redemption and no quoted
Ephrem hymn line (srcSYR001, Hymns on Faith, is cited only bibliographically,
never quoted). But two existing, already-verified fragments are usable
without inventing anything: syrdemo002's "the body's resurrection, because a
people watching its shepherds killed needed to hear that flesh given up is
not given up for nothing" (resurrection-as-not-in-vain), and syrdemo009's own
Adam/side raza ("Christ asleep on the cross, the church drawn from his
side") - already-confessed content, not yet framed as an answer to "what is
the gospel" specifically.

**New demonstration**: syrdemo010, recombining these two already-sourced
fragments into a dedicated "what is the gospel" scenario - no new source
mining required, no term/story authored, only a new demonstration composing
existing verified material.

### Hieronymian (Albina) — content already exists, framing gap

Full-store search confirmed haldemo011 already contains real gospel content
("the Gospels our scholar revised... announce a man who taught, was
crucified, and rose from the dead") plus one unused fragment: hallex04
(Virginitas)'s "a state nearer to what the redeemed life will finally be - a
foretaste, kept now, of a condition not yet arrived for everyone else."
Confirmed GENUINELY THIN beyond this - no preface, story, or lexicon record
anywhere states soteriological content itself (why the cross/resurrection
saves). The honest answer cannot go deeper without inventing content this
store does not carry - consistent with this world's own documented thin-store
honesty (20/103 christological records, per haldemo011's own situation_tag).

**New demonstration**: haldemo012, a short, explicitly-gospel-framed scenario
reusing haldemo011's exact sources (halcore001, hallex02, halstory08) plus
hallex04's redeemed-life fragment - not deeper content, but content the world
already owns, framed to answer THIS question rather than only "who was
Jesus."

### Desert (Papnoute) — BLOCKED, not authored

Unlike the 2026-08-10 pass, this is not a scope decision to defer - it is a
hard blocker. srcDES003 (the Letters of Antony, this world's own richest
possible source for Christ-content, per the 2026-08-10 ruling) has no
vendored text anywhere in this repository: `discovery_channel:
builder-prior-knowledge`, Coptic original almost entirely lost, no English
critical edition (Rubenson 1990/1995 or otherwise) consulted or present. The
2026-08-10 ruling was explicit: *"A Desert demonstration written today would
either invent (forbidden) or model the same displacement being fixed."* That
is still true today, and it applies with equal force to the gospel question -
if anything more so, since no Desert record anywhere touches salvation
content even indirectly (unlike the thin-but-real fragments found in syriac
and hieronymian).

**Not authored.** Flagged back to the project lead: either an actual English
translation/edition of the Letters of Antony needs to be vendored into this
project's text corpus before any Desert Christology or soteriology can be
honestly authored, or this remains an accepted, longer-term open item beyond
this pass, continuing to rely on Papnoute's own honest-thinness posture
(silence named as silence, not papered over).

## Selection check (per the 2026-08-10 precedent's own step 3)

Cap is currently 4 for these worlds (raised from 3 on 2026-08-10 specifically
so the "who was Jesus" demonstrations would select without displacing a
discipline demo). Adding a second foundational-question demonstration per
world may require the cap to move to 5, still inside the Design's own
documented 3-5 range. Verified against the real selector (wrs/views/segments/
demonstrations.py), reported not assumed, before this pass is considered
complete - see the authoring records themselves for the actual selection
result.

## Sequencing

1. ijclex013 + srcIJC42 (new source/term), then ijcdemo011.
2. syrdemo010 (recombination only, no new source/term).
3. haldemo012 (recombination only, no new source/term).
4. Desert: not authored, flagged.
5. Independent adversarial review per new demonstration (isolated, no
   visibility into the drafting reasoning) - per this project's own
   build-cycle discipline for record authoring.
6. Revise per review findings.
7. Selector cap check, live re-probe, compare against the 2026-08-16 probe
   transcripts already on file.
