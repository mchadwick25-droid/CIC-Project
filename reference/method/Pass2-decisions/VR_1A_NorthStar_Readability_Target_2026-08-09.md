# Decision — 1A North Star and Readability Target (2026-08-09)

**Decided by:** Mark, in session, 2026-08-09.

## The north star (1A's definition, in Mark's words)

> 1A is our ultimate goal without compromising 1B, and word count is a
> minor piece of that. It is selecting words and sentence
> structure/length that is easy to read. It is keeping a flavor of the
> world, but not where it makes it a distraction or something that is
> not clear to a 10th grade English speaker. Our whole goal is making
> the rigor accessible to everyone, even not-English-first-language
> speakers. We make the wording easy, but still carry the uniqueness
> and truth of the world. People can understand the truth easily,
> without compromising the convictions and 1B and other things.

**Standing interpretation:** when this project says "1A" it means this
goal, everywhere it lives — records, capsules, demonstrations, the
shared block, the scorecard — NOT merely the Blueprint's Phase-1A task
(the `_HOW_YOU_ENGAGE` rewrite), which is one concrete piece of it. A
goal cannot be a phase: it must be load-bearing in every layer and
every checkpoint. No future session may re-narrow the term.

## The target

- **CEFR B2 / FK grade band 8–10, FRE ≥ 60, per emitted turn.**
- **Anchor register: BBC News / National Geographic prose** — serious,
  adult, vivid, clear; readable by a non-native speaker without
  simplifying the substance.
- The scored edge is the **upper bound only** (FK ≤ 10, FRE ≥ 60). The
  band floor of 8 is **reported, not failed** — the same philosophy the
  assembly gate has always documented ("too-simple is not the risk the
  floor guards"). FLATTENING, not FK, guards against emptiness.
- This extends the existing assembly-time floor (already FK ≤ 10 /
  FRE ≥ 60 on prompt and capsule text) to **per-turn output** as a
  scored checkpoint item. Same numbers the project already chose; new
  enforcement point.

## The both-sides frame (how 1A and 1B are scored together)

Success is a **triptych on the same transcript**, all three green:

| axis | instrument | failure mode it guards |
|---|---|---|
| accessible | per-turn FK/FRE (scored) + vocabulary reach vs top-5000 (reported) | a wall — held but unreadable |
| distinctive | FLATTENING watch, world imagery | a tour guide — accessible but flat |
| held | sustained-disagreement bar, fabrication 0 | a museum — distinctive but hollow, or worse, agreeable |

The world's uniqueness lives in its convictions, stories, images, and
rhythm — never in vocabulary density or syntax difficulty. A world term
earns its place when its meaning arrives with it (story first, term
after — the bridge). Flavor is never a toll the reader pays to reach
the truth.

## Instruments added on this decision (2026-08-09)

- `phase2_checkpoint.py` scorecard: **"readability B2 / FK 8-10 per
  emitted turn"** — scored; breaches listed per turn; band placement
  reported.
- **"vocabulary reach vs top-5000"** — report-only, built on the
  offline `wrs/gates/english_top5000_v1.txt` table already in the repo;
  world TECH_TERMS excluded (bridged flavor is counted by its own
  instrument, not as a vocabulary failure). No threshold invented;
  rates accumulate on the watchlist until a bar is set from data.

## First application — the item did real work immediately

All three committed artifacts re-scored (no new API calls):

| run | FK range | FRE min | verdict on the new item |
|---|---|---|---|
| Chloe run A | 3.21–7.35 | 73.7 | PASS (below band — reported) |
| Chloe run B | 5.19–8.03 | 71.6 | PASS |
| **Marius** | 6.8–9.75 | **52.9** | **FAIL — turn 1 breaches FRE 60** |

Marius's overall verdict flips from `PASS_PENDING_HUMAN_READ` to `FAIL`
on that one turn. His vocabulary reach also runs hottest in the fleet so
far (mean OOV 18.6%, max 30.9% — `athanasius`, `chalcedon`,
`constantinople`: the sees and councils that are his substance). The
chancery voice pushes on accessibility exactly where the world's flavor
is densest — which is precisely the tension this decision exists to
manage, caught by the instrument on first contact.

## RULED — hard edge (Mark, 2026-08-09)

> "hard edge, readability is the whole point"

Any single emitted turn breaching FK ≤ 10 / FRE ≥ 60 fails the world.
The periodic grace the measure got does NOT extend to readability. The
scored item covers **all** emitted turns — the sustained half's turns
are computed at scoring time with the same gate function, because a
voice that reads B2 in ordinary conversation but densifies under
pushback fails the same reader.

Marius's FAIL stands. His records fix (same session): a stacked-glosses
avoid_trait on `ijcvoice001` and the petitioner's-plain-speech clause in
his guard export — both derived from his OWN register rule ("plain for
petitions"), with the measurement on the record. The terms themselves
stay; density is what is refused. Checkpoint 2 re-run follows.
