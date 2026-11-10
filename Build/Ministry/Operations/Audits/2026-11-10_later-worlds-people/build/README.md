# P2-G3b build: data release 31 — 2026-11-10

Mark ruled "take every recommendation" on the later-worlds list (Decision-Log, "The later-worlds
people ruled (P2-G3b)"). Pamphilus was then held by a correction to ruling B's premise (same
entry): the Library holds no undisputed words of his. This release adds the other 13.

## What the release holds

**13 person entries** (kind "person", status Within Another World (A5)), each told within the
tradition whose shelf holds them, hidden from the map until P2-P like release 29's:

| atlasId | id | told within |
|---|---|---|
| I.58 | `polycarp-of-smyrna` | post-apostolic-house-church |
| I.59 | `methodius-of-olympus` | anatolian-church-third-century |
| I.60 | `lactantius` | latin-apologists |
| I.61 | `paula-of-rome` | hieronymian-ascetic-literary |
| I.62 | `constantine-the-great` | imperial-juridical-christianity |
| I.63 | `basil-of-caesarea` | cappadocian-nicene-pastoral-monastic-tradition |
| I.64 | `gregory-of-nazianzus` | cappadocian-nicene-pastoral-monastic-tradition |
| II.23 | `patrick-of-ireland` | insular-irish-monastic-christianity |
| II.24 | `justinian-i` | byzantine-imperial-church-justinianic |
| III.26 | `bede-of-jarrow` | anglo-saxon-christianity |
| IV.28 | `gregory-vii` | latin-papal-church-gregorian |
| IV.29 | `innocent-iii` | latin-papal-church-gregorian |
| VI.37 | `hugo-grotius` | the-remonstrants-and-dort |

Each `legacy` says which later traditions name the person, from the passages the clean count
verified; it claims no influence the sources do not show.

**People rows.** Each home row now points at the person entry (12 replaced, Paula added to the
Hieronymian row). **concerns.** 21 existing links now name the person entry their note or quotes
are about (`apply_log.json`). None was overwritten. The Dictatus Papae link
(`latin-papal-church-gregorian--latin-papal-church-avignon-to-lateran-v`) is left without
`concerns`: Mirbt's heading reports the view that Cardinal Deusdedit wrote it, so it is not
counted as Gregory VII's own words. No new links.

## How it was drafted and reviewed

Sonnet drafted in four slices (`p1` to `p4`, `Draft_r0.json`) to `Person_Drafting_Brief.md`.
Each draft carries a fact table tying every factual sentence to a vendored file, lines and quote.

| round | reviewer | findings | outcome |
|---|---|---|---|
| 1 | two Opus, full review (`reviews/Review_Round1_A.json`, `_B.json`) | 2 blocking, 9 substantial, 17 minor | revised (`Draft_r1.json`) |
| 2 | Opus, targeted recheck (`reviews/Review_Round2.json`) | 1 substantial, 4 minor | revised (`Draft_r2.json`) |
| 3 | Opus, targeted recheck (`reviews/Review_Round3.json`) | 1 substantial, fact table only | fixed with the reviewer's text (`p2/Draft_r3.json`) |

Round 1's blocking findings were the Paula and Pamphilus entries saying they had no words of their
own, against ruling B. Its substantial finding that the Library lacks the Apology's text led to
Pamphilus being held. Round 3's one finding was two swapped sentence fields in Basil's fact table,
the drafting record. No census field depended on it. The coordinator applied the reviewer's exact
text and checked it; see the coordinator's report for the cap. Renderings of non-English lines are
Opus's (round 1 fixes, used verbatim).

`apply_g3b.py` merged the drafts (`decisions.json`: the skipped `concerns` link and five spelling
fixes to American spelling in our own prose). `check_draft.py` from release 29 ran clean on every
final draft.

## Checks

- `node tools/validate-census.mjs --base <release 30> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors (2 old shortName warnings).
- `python -m engine.m6.cli atlas-sync`, then `atlas-check` and `check`: no changes left.
- `node Build/tools/generate_tree_pages.mjs`; `node tools/build_tree_site.mjs`: 0 mismatched.
- Node tests: the validator suites, with `validate_census_people.test.mjs` fixed. Its fixture home,
  the Latin apologists, now tells Lactantius as well, and its cases now detach him before emptying
  the home's row. Also `cic-worker/worker.test.mjs` and `generate_tree_pages.test.mjs`.
  `pytest engine/m6/tests`: 45 passed.
- Paths, commentary (`--enforce`) and spelling: clean.

## Recording batch (no recording made)

The tree narration dry run counts 13 new pages, 11,077 characters, for the one recording batch.
No sample was prepared and no paid call made.

# Data release 32 — 2026-11-10

The Library's first wants batch (PR #1577) vendored the words three held people lacked, and the
coordinator brought them in under Mark's ruling (Decision-Log, "Three held people come in once the
Library holds their words").

| atlasId | id | told within | own words now held |
|---|---|---|---|
| I.65 | `pamphilus-of-caesarea` | alexandria-catechetical | the Apology for Origen, Book I, in Rufinus's Latin (joint with Eusebius; Jerome's denial named) |
| III.27 | `heraclius` | byzantine-imperial-church-heraclian-iconoclast | the Ecthesis, issued and signed in his name (Mansi X) |
| IV.30 | `bonaventure` | the-franciscan-movement | the Legenda maior (Salter 1904) and the Tria opuscula (Quaracchi 1911) |

Also: one link gains `concerns` (`canons-regular-victorine-school--the-franciscan-movement`, to
Bonaventure); Pamphilus and Heraclius are added to their homes' people rows and Bonaventure's row
item points at his entry; Nikodemos the Hagiorite leaves the 1453-1650 Ottoman row (out of window;
he stays in the Kollyvades row). `decisions_r32.json` holds the row drop and one field override:
Bonaventure's place label becomes "Italy · Paris and beyond", since the validator requires every
modern-country place on a label of at most two places.

Drafted on Sonnet (`p5/Draft_r0.json`), reviewed by Opus: round 1, 0 blocking, 4 substantial, 11
minor (`reviews/R32_Review_Round1.json`), revised (`p5/Draft_r1.json`); round 2, approve with no
findings (`reviews/R32_Review_Round2.json`). The review judged that the Ecthesis still counts as
Heraclius's own words under answer C: the Lateran acts and his own later letter both say it went out
in his name with his signature. `check_draft.py` ran clean against main's texts after #1577 merged.
Apply log: `apply_log_r32.json`. Checks as for release 31.
