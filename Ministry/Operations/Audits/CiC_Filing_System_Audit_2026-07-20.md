# CiC Filing System Audit — 2026-07-20

**Status: EXECUTED, same day, on Mark's approval.** Six parallel read-only
investigations mapped the repo (nothing moved during the audit itself);
the target structure and migration sequence below were then carried out
in full — see the System Hub Decision Log's 2026-07-20 execution entry
for the exact commits and one live collision found and reconciled
mid-migration. Left as originally written below for the record of what
was proposed and why; this document was not rewritten after the fact.

---

## Why this audit

Mark asked for a full audit of the filing system and a proposal for
reorganizing it so the same problems stop recurring — specifically:
keep separate projects (the Atlas, the 4-role "Representative Modes" setup,
and everything being added to the core conversation experience) in their
own protected file structures, and bring them together only at a
deliberate implementation point.

## The pattern behind "the same things happen again"

This project has already lived through real incidents — the file-loss
scare, the Bethlehem Circle prompt drift, the false "Alexandria is the
fifth live world" claim, a near-miss duplicate Change-Orders filing, three
self-certified compliance numbers that didn't hold up on independent
check, and (see below) two more found during this very audit. None of
these trace to carelessness in one instance. They trace to five structural
gaps that recur everywhere:

1. **The same fact lives in two or more places with nothing forcing them
   to agree.** World-Builds vs. deployed runtime data vs. two hardcoded
   frontend files vs. the manifest — four places, zero automated checks
   between any of them.
2. **A feature's own output has no single home**, so nobody — including
   the people who built it — can list everywhere it lives without
   searching. The Atlas exists in 8 different locations; Representative
   Modes in 6.
3. **A decision recorded in a log is not the same as a decision executed
   on disk.** Facilitator-Governance V3.4 was ruled "safe to archive" in
   this project's own Decision Log on 2026-07-19. It is still sitting in
   the live folder today.
4. **Superseded content is marked in prose, not in location.** A document
   says "SUPERSEDED" in its own first line, but sits in the same folder,
   same tier, as the current version — a folder listing can't tell them
   apart.
5. **Tooling drifts the same way content does.** The one script that
   exists to keep two locations in sync (`extract_source_registries.py`)
   has itself gone stale — its hardcoded path points at a directory that
   no longer exists after a prior reorg.

---

## Findings, by area

### A. `Ministry/Technology/` — 75 files, 14 feature threads, no index

No file anywhere in this tree says what threads exist or where each one's
output lives. Even the three threads with their own subfolder
(`Hosted-Tour/`, `Representative-Modes/`, `World-Orientation-Map/`) keep
their own Decision Log *outside* that subfolder, as a loose sibling file —
so even the best-organized threads split across two locations.

Specific problems found:
- **Near-duplicate thread names causing real confusion:** "Messaging &amp;
  Branding Kit" and "Branding &amp; Messaging Analysis" are two entirely
  separate threads — separate decision logs, separate launch prompts, both
  dated the same day — distinguishable only by reading closely enough to
  notice the swapped word order.
- **"Tour" name collision:** "Hosted Tour" (a built, working demo) and
  "Tour Experience Module" (an unbuilt Phase Two concept) are used almost
  interchangeably in prose despite being different scopes.
- **Version staircases with no archival step:** Engineering Specification
  exists at V1_0/V1_1/V1_2 side by side with no marker on which is current;
  the World Map's census data has 12 sequential spreadsheet versions kept
  side by side.
- **Explicitly-superseded content left undifferentiated:** two Guided
  Questions files each open with "⚠ SUPERSEDED" in their own text, but sit
  in the same folder as the live curriculum with no filename signal.
- **Broken version chains:** Full UX Design V1.0 references a V0.1 draft
  that no longer exists anywhere in the repo (lost on a squashed branch).
- **One split thread with two unrelated filename prefixes:** Guided
  Questions' own follow-on work (`CiC_QuestionFirst_Entry_Design_V0_1.md`,
  `CiC_World_Coverage_Cards_V0_1.md`) doesn't carry the `Guided_Questions_`
  prefix, so a search for that prefix misses real pieces of the thread.
- **Debris:** a 0-byte `_permtest.txt` sitting among real files.

### B. Atlas / World Orientation Map — 8 locations, including a live-tested integration branch checked out *outside the repo entirely*

The single worst-scattered feature found. Its content spans:
1. Live production (`cic-website/atlas.html`, `world-map.html`,
   `world-atlas-list.html`) — current, but self-disclosed as stale on two
   worlds' status as of today.
2. A dedicated draft folder (`Ministry/Technology/World-Orientation-Map/`,
   24 files) already labeled "superseded scratch drafts" in its own commit
   history, but still sitting in the live tree.
3. Governing decision log + launch doc, one level up from that folder.
4. Real, live-tested integration code wiring the map into the actual
   conversational app — on a branch (`claude/world-map-merge-into-main`)
   checked out in **its own separate sibling directory outside the repo
   root** (`C:\Users\mchad\Documents\CiC-Project-worldmap-merge`), never
   merged, gated on an undecided Tier A/B scope question.
5. A second, earlier exploration branch.
6. ~30 other documents across Operations, Technology, Communication, and
   World-Builds that reference the feature without containing its content.

A reader needs to open roughly three dozen files across 5 top-level
directories and 2 branches to reconstruct this one feature's actual
current status.

### C. Representative Modes ("4-role setup") — 6 locations, not live at all

- Design docs + decision log: `Ministry/Technology/Representative-Modes/`
  and a sibling log file — clean internally, but not live in the app.
- The actual code exists only on a local, **unpushed** branch
  (`claude/representative-modes-exploration`) that is one commit ahead of
  what the tracking docs cite (the Dashboard and Task Board reference an
  older commit than the branch's real tip).
- Its governance root lives in `L3D-Encounter-Methodology/` (a third
  location), including a Syriac-specific duplicate copy.
- Its origin/charter decision lives in a *different* thread's decision log
  (`CiC_FrontEnd_Decision_Log.md`), not its own.
- A stray compiled `.pyc` file for the branch's `role_modes.py` sits in the
  main working tree's `__pycache__` — physical evidence someone ran the
  branch locally and switched back without cleaning up.
- At least 14 other documents (Task Board, Gantt, Dashboard, multiple
  readiness assessments) carry their own RM-1..RM-15 task references that
  must be cross-checked to know current status.

### D. World-Builds vs. deployed data — 57 sync points per world, zero automated checks, real drift found, plus a live bug

Every deployed world has a **per-file**, not per-folder, manual sync
requirement: permanent prompt, world capsule core, every lexicon chunk,
every story chunk — confirmed at 57 individual file-pairs for Alexandria
alone. `world_manifest.py` is a real single-source-of-truth *within the
backend*, but is itself a fifth manually-maintained list, which is exactly
why a fully-built world (Imperial and Juridical Christianity) currently has
zero footprint in the running app.

**No automated check exists anywhere in the repo** — no CI, no test
comparing the two copies, no sync script. The one script that touches this
area (`extract_source_registries.py`) has a hardcoded path to a directory
that no longer exists after a prior reorg.

**Real, current drift found** (not hypothetical):
- Syriac: one deployed lexicon file has no source counterpart at all;
  4 deployed files carry a "Quick Meaning" section absent from source.
- Hieronymian: all 15 deployed lexicon chunks have frontmatter the source
  lacks; one has a substantive wording rewrite present only downstream.
- House-Church: two story chunks have genuinely different prose between
  source and deployed copies.
- Alexandria and Desert-Monasticism: fully clean, byte-identical — proof
  the pattern is fixable, not inherent.

**Live production bug found, unrelated to filing but caused by exactly
this dual-hardcoding pattern:** `MessageBubble.tsx`'s `REPRESENTATIVE_INFO`
dict correctly lists Theon, but the adjacent `getSpeakerInfo` switch
statement has no `case` for `'theon'` — his messages in the deployed
Alexandria world currently fall through to the `default` case and render
labeled and styled as the Facilitator, not as Theon. Two hardcoded
structures inside the *same file* fell out of sync with each other.

### E. Rest of `Ministry/` — Operations overloaded, cross-thread authorship untracked by location

- **`Ministry/Operations/`** (28 files) mixes three genuinely different
  things with no separation: 5 standing tracking artifacts (Decision Log,
  Task Board, Dashboard, two Gantt files), ~16 one-off dated audits/status
  reports, and 6 launch prompts for threads whose actual deliverables live
  entirely elsewhere — most strikingly, the Imperial-Juridical world-build
  launch prompt sits here while all 57+ real deliverable files sit under
  `World-Builds/`.
- **Orphaned/misfiled files in Operations:** `w1brief_h.md`, a full
  reviewer-orientation brief for World 1, cryptically abbreviated and
  filed here instead of alongside its four siblings in
  `Ministry/Scholarly-Review/`; a bare `.ico` icon file with no
  explanation; `lexicon_compliance_checker.py`, a script sitting among
  prose documents.
- **A second, currently-unresolved data loss, found during this audit:**
  five `Ministry/Marketplace/` files (the Landscape Scan, the
  Differentiation and Lessons brief, that thread's own decision log and
  launch doc, plus a Funder Landscape doc) were recovered into `main` this
  same session (commit `e536bd0`) — but are **not present in the current
  tree**. The recovery commit is a real ancestor of `main`; the files it
  added are gone from `main`'s tip regardless. This needs the same
  git-archaeology recovery already used once this session, not a filing
  fix.
- **Cross-thread authorship with no location-based ownership signal:**
  the Funding thread writes documents that live in `Organization/`; the
  Branding thread edits Funding's own donor `.docx` files and logs it in a
  file that lives in `Technology/`. Each case is disclosed in the
  document's own header prose — but nothing about *where a file sits*
  tells you who actually owns it.
- **`Ministry/Communication/`** otherwise holds one coherent, well-run
  `Brand-Assets/` subtree (36 files) with a heavy but legitimate
  versioning pattern (per-world icon lock history) — the one place a
  version staircase is arguably working as intended, since each lock is a
  real, named checkpoint.

### F. Archive / Syriac-Build / worktree debris

- **The Archive convention exists, is written down clearly**
  (`CiC_L2A_Clean_File_Structure_V1.1.docx`: *"Only the latest ratified
  version stays in a live folder... nothing is deleted without explicit
  instruction"*), and is mostly followed. Two live gaps: the governing
  document's own category list is stale (missing two real Archive
  categories that already exist on disk), and the one already-decided
  archival action from yesterday (move Facilitator-Governance V3.4) was
  never physically executed.
- **`Syriac-Build/`** is a real, intentional, git-tracked clean-build
  sandbox (confirmed via the Decision Log) — but has **zero internal
  self-documentation**. It reuses the exact same folder names as the real
  L1-L4 root (`L1-Foundation/`, `L4-Templates/`, etc.) with no README, no
  suffix, nothing marking it as a sandbox rather than an accidental
  duplicate — a direct instance of the exact thing the project's own
  filing rule warns against ("a copy of a template appearing anywhere
  else is a filing defect, not a second canonical copy"), tolerated here
  as an undocumented special case.
- **Worktree debris:** one local worktree (`cool-hofstadter-61cab6`) is
  carrying 1.3GB of untracked `.venv`/build artifacts from an old
  dependency install — pure disk weight, safe to reclaim. Two other local
  worktrees are fully merged (0 commits ahead of `main`) and never cleaned
  up. The Atlas integration branch's sibling directory (found in section
  B) is the one worktree in this whole audit holding real, undelivered
  value — everything else found is either intentional-but-undocumented or
  safe-to-reclaim clutter.

---

## Two things to fix regardless of any reorganization decision

These aren't filing problems — they're a live bug and a live data gap,
found along the way. Recommend fixing both now, independent of whether/how
the reorg proceeds:

1. **Fix `MessageBubble.tsx`'s missing `'theon'` case** in
   `getSpeakerInfo` — a one-line addition, currently causing Theon's
   messages to render as the Facilitator in a deployed, live-tested world.
2. **Recover the 5 missing Marketplace files** the same way the earlier
   file-loss incident was resolved this session — via git history, not
   reconstruction from memory.

---

## The natural breakdown

Looking at everything that actually exists, the project has eight natural
domains, not one undifferentiated `Ministry/` folder:

| Domain | What it is | Current state |
|---|---|---|
| **Foundation** (L1-L4) | The build methodology itself | Already well-organized; protected by Mark's own standing rule; not part of this reorg |
| **World Content** (`World-Builds/`) | Per-world construction records | Already well-organized internally; the problem is at its deployment *boundary*, not its own structure |
| **The Core App** (`cic-poc/`) | The actual running conversational product | The integration destination — features land here only when deliberately merged |
| **The Public Website** (`cic-website/`) | Marketing/orientation site, separate deployable | A second, distinct integration destination |
| **Feature Workstreams** | Everything being *added* that isn't world content and isn't yet core-app code: Atlas, Representative Modes, Guided Questions, Hosted Tour, Facilitator Upgrade, Front-End Strategy, Backend, Website changes | Currently scattered ad hoc under `Ministry/Technology/` — **this is where the reorg actually needs to happen** |
| **Cross-cutting Ministry domains** | Communication/Branding, Marketplace, Organization, Funding, Scholarly-Review | Fine as top-level domains; need light internal hygiene only |
| **Operations / System Hub** | The project's own control tower | Overloaded — needs to hold only what's actually its own |
| **Archive** | Superseded/historical record | Working convention; needs 2 small fixes, not a redesign |

---

## Proposed target structure

```
CiC-Project/
├── L1-Foundation/ .. L4-Templates/        UNCHANGED — protected core methodology
├── World-Builds/<world>/                   UNCHANGED — per-world source of record
├── cic-poc/                                 UNCHANGED — the live app; features land here only at integration
├── cic-website/                              UNCHANGED — the live site; same rule
├── Project-Reference/                        UNCHANGED
├── Archive/                                   convention kept; category list corrected; V3.4 actually moved in
│
└── Ministry/
    ├── Features/                             NEW — every in-development, not-yet-core feature gets exactly one folder
    │   ├── Atlas-World-Map/
    │   │   ├── README.md                     one-page index: what it is, current state, what's live vs. integrated, open decisions
    │   │   ├── Decision-Log.md
    │   │   ├── Launch-Prompts/
    │   │   ├── Design/                       current specs/architecture only
    │   │   ├── Drafts-Archive/                dated, superseded scratch material — moved here, not left beside the live version
    │   │   └── Integration-Notes.md          branch names, worktree paths, exact merge status, the Tier A/B decision record
    │   ├── Representative-Modes/              same shape
    │   ├── Guided-Questions/
    │   ├── Hosted-Tour/
    │   ├── Tour-Experience-Module-Phase2/     renamed to stop colliding with Hosted-Tour
    │   ├── Front-End-Integration-Strategy/
    │   ├── Facilitator-Upgrade/
    │   ├── Backend/
    │   └── Website/
    │
    ├── Communication/                         unchanged domain; Brand-Assets/ untouched; near-duplicate threads disambiguated in-place
    ├── Marketplace/                            5 missing files recovered first
    ├── Organization/
    ├── Funding/
    ├── Scholarly-Review/                       World 1's orphaned brief moves in here, alongside its 4 siblings
    │
    └── Operations/
        ├── Standing/                           Decision Log, Task Board, Dashboard, both Gantt files — the durable artifacts only
        └── Audits/                              dated one-off audits/status-reports/handoffs (this document included)
            (feature launch prompts move OUT to Ministry/Features/<name>/Launch-Prompts/;
             world-build launch prompts move to World-Builds/<world>/)
```

**The rule that actually answers "bring it together only at the
implementation point":** a Feature folder holds *everything* about that
feature — design, decisions, exploration code references, branch names —
right up until a deliberate, logged step merges specific files into
`cic-poc/`, `cic-website/`, or `World-Builds/`. That folder's own
`Integration-Notes.md` is the single place recording exactly what has and
hasn't crossed that line, so "is this actually live" becomes a one-file
answer instead of the current cross-reference hunt across 5-8 locations.

**Separately, a tooling recommendation, not a filing change:** the
World-Builds ↔ deployed-data drift (section D) isn't fixed by moving
files — both locations are already correctly placed. It needs a small
sync-checker script (diff each world's `World-Builds/` copy against its
`cic-poc/backend/data/` copy, report drift) wired into the Coach Standard
Review Checklist's existing Section H. Worth building as a follow-up, not
blocking on this reorg.

---

## Recommended sequence, if approved

1. Fix the two concrete items above (Theon bug, Marketplace recovery) —
   independent of the reorg decision, low-risk, already fully diagnosed.
2. Create `Ministry/Features/` and move each thread's files in via `git mv`
   (preserves history), one commit per feature — reviewable and revertable
   individually rather than one large sweep.
3. Split `Ministry/Operations/` into `Standing/` and `Audits/`; move the
   feature/world-build launch prompts out to their new homes.
4. Fix the two live Archive gaps (update the category list; move V3.4 in).
5. Leave `L1-Foundation/` through `L4-Templates/`, `World-Builds/`,
   `cic-poc/`, and `cic-website/` untouched — they don't need to move, and
   moving them would touch the protected build-process territory this
   project has an explicit standing rule against disturbing.
6. Build the sync-checker script as a separate, later task.

Not done automatically: any of the above. This is the proposal for your
review.
