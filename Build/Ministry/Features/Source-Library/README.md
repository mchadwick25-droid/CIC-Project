# Source Library — workstream

**Charter (Mark, 2026-10-14):** make every source a participant sees available by
link, so a reader can follow a citation into the passage itself, in our own Library of
vendored public-domain editions first and at the place we downloaded it from beside it.
Scholars study one of these worlds for years; the depth is in the primary texts.
Linking every answer to its passages turns a conversation into a doorway into the
texts, keeps it faithful by construction, and lets outside reviewers check us directly.

**Status:** Approved to proceed, 2026-10-14. Implementation is the first job after the
pilot launches, starting with desert. Nothing here is built yet.

## What is in this folder

- **`Design.md`** — the design of record: the seven decisions Mark converged on, the
  citation record shape, the anchor grammar, derivation and gate, the reader page, rights,
  hosting, the phased plan, and what is still unverified.
- **`Research.md`** — the four-stream research that preceded the decisions: how academic
  text programs address and link passages, free text databases and their licence terms,
  page-image and persistent-link infrastructure, and what a passage page must show to be
  trusted. Evidence grades are carried on every claim; most patristic and library hosts
  were blocked from the research sandbox, so licence wording is to be re-read live before
  it enters policy.
- **`Decision-Log.md`** — append-only, workstream-local. One entry per ruling and per PR.

The project-level record is the 2026-10-14 entry in
`Build/Ministry/Technology/CiC_FrontEnd_Decision_Log.md`.

## How the decisions were reached

Research first (Mark's instruction), then seven questions one at a time, each with
options and a recommendation, big picture first: what the Library is, where the link
lands, the CCEL posture, where the address lives, where the reader lives, the fallback
when a section cannot be pinpointed, and front door or links only. Mark took the
recommendation on each.

## Model routing

Fable did the design and the research coordination. The build is Sonnet work under the
build-cycle's own self-governance, with Haiku for the mechanical write-back pass. Any
ruling that turns out to need real back-and-forth goes back to Fable.

## Stage 1 prerequisites

Nothing is needed from Mark before the pilot launches. At the opening of Stage 1:

- Mark reads CCEL's copyright page live and sends the letter asking permission to
  republish the volumes. Passage display with credit does not wait on the answer.
- Root README map and `CiC_Repo_Structure_Tracking.md` updated before the new public
  directory on the site exists.
