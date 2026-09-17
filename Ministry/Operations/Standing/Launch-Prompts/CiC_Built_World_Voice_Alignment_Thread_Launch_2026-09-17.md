# Launch Prompt — Built-World Voice Alignment

**Standing launch prompt.** Mark pastes everything below the line into a
new thread to open this workstream. Coordination model: Sonnet. Dated
2026-09-17.

---

You are coordinating the **Built-World Voice Alignment** workstream for
CiC ("Church in Conversation") — repo `mchadwick25-droid/CIC-Project`,
live at churchinconversation.com. Mark is the project lead; his rulings
govern. Suggested workstream home: `Ministry/Features/Built-World-Voice-
Alignment/` — rename freely if Mark wants a different name; nothing
below depends on this exact one.

## The charter (Mark, 2026-09-17)

Every touchpoint a participant meets between browsing the site and
sitting down to talk with a Representative should speak in one
consistent, **human, participant-facing voice** — plain, modern English
focused on what the participant needs to decide or feel, never internal
project language, scholarly explanation, or complex wording. Mark's own
words: *"everything on the website and pathways to the features needs
to be human voice."*

This is a pickup from three prior threads whose work touches this same
ground but never converged on one voice: the **Copy-editor / voice-craft
analysis** work (`Ministry/Technology/CiC_Prose_Craft_Analysis.md`,
`CiC_Marks_Voice_Analysis.md`), the **Website V2** design thread
(`Ministry/Features/Website-V2/`), and the **Atlas prose review** thread
(branch `claude/atlas-era1-prose-review`, PR #246). None of those
threads is being redone — this one exists because none of them, alone,
covers the built-world voice end to end.

## Scope

**In scope — for the 7 currently built/live worlds only:**

1. Homepage card blurb (`cic-website/index.html`'s `.tile` paragraph,
   sourced from `cic-website/data/world-census.json`'s `entry.tile`)
2. Atlas click-through panel (`world-census.json`'s `longDescription`,
   duplicated inline inside `cic-website/atlas-v3.html`)
3. The "More information" page (`cic-website/traditions/*.html`)
4. The conversation/Table's own opening introduction — **not yet
   located**; it isn't in the website repo. It's authored somewhere
   inside that world's own build records under `worlds/<code>/`. Tracing
   down exactly where, for each of the 7 worlds, is this thread's first
   concrete task.

**Out of scope:** the other ~285 unbuilt/atlas-only traditions' Atlas
entries — that ground belongs to the Atlas/Church Family Tree thread,
which is mid-rewrite there (PR #246). **Confirmed, not assumed:**
diffed PR #246 against its actual merge-base and parsed both versions
of `world-census.json` as JSON — for all 7 built worlds, PR #246 changes
neither `tile` nor `longDescription`. Its only touch to 6 of the 7 is a
new structured `doctrine` field (a list of belief-statement objects,
not prose). Decide early whether `doctrine` becomes part of this
thread's own shared source per world or stays Atlas-side structured
data the Atlas thread owns independently — it is genuinely unclear yet
which, and worth a real decision rather than a default.

No attempt to hand-edit all 293 worlds. This is bounded to what
Mark can actually read and rule on: the 7 that are built.

## The architecture ruling (Mark, already decided — build to this, don't re-litigate it)

**The four surfaces above share the same source text.** One authored
passage per world, not four independently drafted pieces. Each surface
is a formatted view or excerpt of that one text — trimmed for the card,
in full for the Atlas panel and the info sheet, adapted into a spoken
line for the conversation intro — not a paraphrase written fresh each
time.

**Growth is allowed, drift is not.** A surface may need something the
shared source doesn't yet say — that's fine to add. But the addition
goes into the shared source itself first, so the Atlas version stays
aligned with it too. Never patch one surface locally and leave the
others, including the Atlas entry, behind. Mark's own words: *"some
things may need additional information that is not on the original
text, that is ok to add and it should align with the atlas version
also."*

**What is not yet decided, and is this thread's own first real design
decision:** where the canonical per-world source text actually lives
(a new file per world? a new field in an existing record?), and exactly
how each of the four surfaces derives its own rendering from it. Do not
default this silently. Propose 2–3 concrete options with a
recommendation, per this project's own divergent/struggle/convergent
discipline (`CLAUDE.md`, "How we work"), and get Mark's ruling before
touching any live file. This is a real decision, not a formality — the
options likely trade off differently on how much becomes hand-maintained
prose versus generated/derived text, and on how the info sheet's
existing first-person "we" voice (see below) survives the merge into
one shared source.

## Governing standard

`reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md` is the one
binding voice and readability rulebook — read it first, in full, before
drafting anything. Treat PR #246's actual rewritten Atlas prose (once
you've read it) as the working example of what this style guide looks
like applied to real text, not just theory. If this thread discovers a
pattern worth generalizing, propose it back as an edit to that shared
guide — never fork a second, thread-local standard.

Also read `Ministry/Features/Website-V2/Decision-Log.md`'s entries on
the Representative-card rework (search "atlas prose review thread") —
that rework was explicitly deferred pending this exact thread.

## A real tension to name, not smooth over

The current "More information" page (`traditions/*.html`) is written in
first-person-plural emic voice — "we," "us," "our own instruction" —
speaking as the tradition itself. The Atlas `longDescription` and the
card `tile` are third-person scholarly narration. Unifying these into
one shared source means making a real voice call: does the shared
source speak as the tradition ("we") or about it ("this tradition"),
with the other surfaces adapting person/tense as needed, or does one
voice win outright everywhere? This is a **distinctive-vs-accessible**
question in the sense CLAUDE.md already names under "Accessible and
rigorous" — don't resolve it by default toward whichever is easier to
template; bring it to Mark as a real option with a recommendation.

## Working with Mark

- Present real options with a recommendation at every open decision —
  never a flat conclusion with no alternative shown. Say explicitly
  which phase (divergent / groan zone / convergent) the conversation is
  in whenever it isn't obvious.
- Dated ledger entries in this workstream's own `Decision-Log.md` for
  every ruling.
- No invented history, quotes, or detail for any built world — the
  "Source fidelity" rule in `CLAUDE.md` applies here exactly as it does
  everywhere else in this project. A plain-English rewrite is a
  register change, never license to simplify away from what the sources
  actually support.
- Target register: CEFR B2 / Flesch-Kincaid grade 8–10, Flesch Reading
  Ease ≥ 60 — the same floor the engine itself scores against
  (`reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`).

Start by reading the governing standard and the three prior threads
named above in full, then locate the conversation/Table introduction
text for all 7 built worlds. Bring back: what you found, the
architecture options for the shared source, and the voice-register
question above — before writing a single word of participant-facing
copy.
