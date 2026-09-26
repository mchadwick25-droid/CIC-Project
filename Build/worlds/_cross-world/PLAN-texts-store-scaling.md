# Plan: `cic/texts/` past the size where plain git stops being free

**Status:** planning only. Nothing here is executed — the recommendation below
is what to do *when the trigger fires*, not now. Hand-written, not generated.
Answers the blueprint's own A3 item ("plan git-lfs or a
texts submodule before the store passes ~1 GB — not urgent").

## Measured state, today

`cic/texts/` holds 64 vendored files, 188.8 MB, git-tracked. `.git` itself
packs to ~129 MB. Neither is close to the blueprint's ~1 GB estimate for
100+ worlds' worth of TCP/TEI and 19th-century OCR. `git lfs` is not
installed in this sandbox — checked directly, not assumed.

## The two real options, and the one this project should NOT default to

The blueprint named git-lfs and a separate `cic-texts` repository/submodule
as "the standard answer, either works, not urgent." That's true as generic
advice. It is not true for this project specifically, for two reasons this
plan checked rather than assumed:

**1. GitHub LFS is now metered, and this project clones unusually often.**
GitHub retired prepaid LFS data packs; LFS billing today is 10 GiB/month
free storage + bandwidth on Free/Pro plans, then ~$0.07/GiB-month to store
and ~$0.0875/GiB every time an LFS file is *downloaded* — and every
historical revision of a tracked file counts toward stored size, not just
the current one ([GitHub LFS billing docs](https://docs.github.com/billing/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage);
[StorageBites on the post-data-pack pricing](https://storagebites.com/git-lfs)).
Plain git object storage carries no such metering — GitHub's constraint
there is soft (recommends repos stay under ~1 GB, warns above ~5 GB, and
hard-blocks individual files over 100 MB), not billed per gigabyte moved.

That distinction matters more here than in a typical repo because **this
project's own environment clones the whole repository fresh into a new
ephemeral container for every session** (see this environment's own
"Environment configuration" note: "the repository was cloned fresh when
the container started"). A typical developer clones a repo once and pulls
small deltas after that; this project re-pays the full clone cost every
session, across however many sessions run. Under LFS, every one of those
clones (that touches an LFS-tracked file) draws down the metered bandwidth
allowance. Under plain git, it doesn't — the "cost" of a bigger `cic/texts/`
is purely slower clones, which is unpleasant but never a bill.

**2. This project's own immutability rule already blunts LFS's actual
selling point.** LFS earns its keep on repos where the *same* large file
gets overwritten repeatedly — every revision bloats plain git's packed
history forever, because git never forgets a blob it once held. `A2` (the
blueprint's own recommendation, already practiced) says a vendored file is
never edited after it gets an `ENTRIES` row, only superseded by a new file.
So `cic/texts/`'s history growth is already close to *linear* in its
current content size, not a multiple of it from edit churn. The problem LFS
is built to solve barely exists here.

**Recommendation, for when the trigger below fires: prefer a separate
`cic-texts` repository over git-lfs**, specifically because of (1) and (2)
above — not because a submodule is generically better, but because this
project's own clone-per-session pattern makes LFS's metered bandwidth a real
recurring cost, and its own append-only discipline removes the one thing LFS
is genuinely good at. A separate repository (referenced by URL in acquisition
docs, or as a git submodule for tooling that wants it checked out
automatically) also does something LFS cannot: let sessions that don't need
raw texts skip the clone/checkout entirely, shrinking the *routine* case
instead of just making the large case faster. See "what has to be true
first," below — that benefit isn't free either.

## The trigger

Not "when it hits 1 GB." Re-open this plan at **700 MB** in `cic/texts/`
(check with `python cic/engine/texts_registry.py`, which now prints this
figure every run — see "the mechanical check," below) — early enough that
the migration itself can be unhurried, the way this project prefers to
handle anything with a real cost to getting it wrong. 1 GB is treated as
the point where it's overdue, not the point to start thinking about it.

## What has to be true before a split actually happens (NEEDS SIGN-OFF, later)

Splitting `cic/texts/` into its own repository is not just a `git mv` +
submodule add. Two things read the raw store today in ways a split would
break, and both would need to change first:

- **`gate_edition_rights_consistency`** (`engine/m1/gates.py`)
  hard-fails a compile if a `source.edition` names a
  `cic/texts/<file>` path that doesn't exist on disk. If most sessions
  stopped checking out `cic/texts/`, every world's compile would fail this
  gate every time, which is exactly backwards — the gate exists to catch a
  *real* missing file, not "the submodule wasn't initialized here." The gate
  would need a third state — "the store isn't checked out in this
  workspace at all" — that prints advisory and skips, not a defect, the
  same advisory/defect split C1 already names for this same gate's rights
  check.
- **`corpus_structure.py`, `corpus_authors.py`, `corpus_index.py`,
  `corpus_probe.py`** all read file contents directly and would simply not
  run without the store present — acceptable, since they're already
  builder-facing tools invoked deliberately, not part of any gate battery,
  but worth naming so "why did STRUCTURE.md stop regenerating" isn't a
  mystery later.

Neither of these is done by this plan. They're the concrete precondition
for actually executing the recommendation above, and they touch gate
behavior — a project-level call, when the trigger fires, not before.

## The mechanical check

`python cic/engine/texts_registry.py` now prints the live total size of
`cic/texts/` on every run, with a note once it passes 700 MB and again past
1 GB, naming this file. Advisory only — same "derived, not asserted"
discipline as the rest of this layer, and deliberately not a gate: crossing
either number is a planning cue, not a defect.

## Re-verify before acting, not just before reading

GitHub's LFS billing model changed once already between this research pass
and whenever it's read again — the numbers above were current as of
2026-09-02 ([sources: GitHub LFS billing](https://docs.github.com/billing/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage),
[LFS-to-metered-billing discussion](https://github.com/orgs/community/discussions/61362)).
Whoever acts on this plan when the trigger fires should re-check current
pricing before assuming the recommendation still holds, not re-run this
research from scratch — the reasoning (clone-per-session pattern,
immutability blunting LFS's advantage) is durable even if the exact
dollar figures move.
