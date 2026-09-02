# Website V2 — D0 Inheritance Note

**What this is:** the close of D0 immersion. What the prior website thread, the
icon/graphics thread, the brand system, and the UX design constitution already
settled — what V2 keeps without re-deciding — and where the seams show: places
the record disagrees with itself, or the live site has moved past what the
governing documents describe. Read alongside `Decision-Log.md`'s entry for
today. Sandbox artifact — not a deliverable, not final.

---

## 1. What's already settled, and V2 keeps it

**Identity is closed.** The "Arriving" mark (the C-as-table, madder dot at the
threshold) is the approved, final logo — art approved by Mark 2026-07-18, no
open items on the mark itself. Manuscript palette (parchment/vellum/iron-gall/
madder/gold-leaf/lapis/Tyrian/graphite), Alegreya + Alegreya Sans, and the
voice (scholar-host at a table; witness-but-not-recruiting; the five pairs in
the Brand Guidelines) are all FINAL, not open for D1 re-litigation. The
table-and-chair glyph is companion illustration only, never the logo, never
adjacent to the mark. **The live site already implements this correctly** —
`cic-website/assets/style.css` carries the exact brand tokens, and the four
core marketing pages (home, about, support, what's-next) read as one system.

**Six locked Representative portraits**, painterly/fine-art style (not
photorealistic — Mark's explicit call), one per live world, each with its own
documented historical-research trail. These are already in production use on
the homepage's Representative carousel. A **seventh, Cappadocian**, has
apparently since landed (present in the live carousel's portrait map and
`world-census.json`, per `git log` — the Icons/Graphics Decision-Log itself
never mentions this world, so that thread's record is behind what's actually
shipped).

**The disclosure grammar is real, not just designed.** Level-2 hover/tap
popover → Level-3 click/full-entry panel-or-sheet, first-occurrence-only
lexicon terms, the ✲ citation marker — this is built and working in
`cic-poc/frontend` (`Level2Card.tsx`, `Level3Panel.tsx`, `GlossMark.tsx`,
`StoryMark.tsx`), including the mobile popover-before-full-entry fix
(Level2-Mobile-Popover thread, merged). Any website surface that echoes
in-app content (lexicon terms, citations) should reuse this exact grammar,
not invent a second one.

**The business entity and its constraints are locked and load-bearing for
copy.** Faithways Studio, Inc. — a Colorado Public Benefit Corporation, **not
a nonprofit**, no 501(c)(3), contributions not tax-deductible. `.com` is
primary (`.org` redirects) specifically because ".org read as nonprofit-coded"
for a for-profit PBC. This governs every word of any Support/Give surface a
redesign touches.

**Six "protected lines" and a locked vocabulary rule are already live,
corpus-wide** (Brand-Messaging-Rework thread): the doorway line, the
measurement/"yours to own" line, the record/silence line, the hero hook, the
testimony line, and — functionally load-bearing for IA and copy — a
**"world" → "Christian tradition"** rename applied across site pages and
`world-census.json`. D1 authors should write "tradition," not "world," in any
visitor-facing copy they draft.

---

## 2. Where the seams show

**A. The charter's own deploy assumption is wrong — flag for Mark before D4.**
The launch prompt's open item asks whether to add "a Render preview
environment or manual deploys" for the build window. But `cic-website/`
deploys via **Cloudflare Pages** (confirmed in its own README and in the V1
Decision-Log's 2026-08-06 entry about a Cloudflare Worker misconfiguration
that was fixed). Render hosts the **conversation engine**
(`cic-engine.onrender.com`), a separate service. Cloudflare Pages already
supports per-branch preview deployments natively — the D4 open item is
probably "confirm/configure a Pages preview build for `claude/website-v2-
sandbox`," not a Render question at all. Worth a direct correction to Mark
rather than carrying the charter's assumption forward.

**B. A real, unresolved conflict on the six world-site photos.** The Website
V1 thread's 2026-07-24 log entry describes six architectural/artifact photos
(Ephesus, Kom el-Shoqafa, Dura-Europos, Hagia Irene, the Macarius monastery,
the Grotto of St. Jerome) as available for site use, five of them requiring
only visible attribution (CC BY-SA). The icon/graphics thread's own **later**
2026-07-24 entry records that Mark was separately told 5 of the 6 "need
permission and payment" — and pulled all six from live use as a precaution,
explicitly **not resolving** which account is right. The `World-Media/README.md`
still carries a "PULLED FROM LIVE USE — do not use" banner today. **Net: these
photos are not cleared for D1 or D3 use.** If a direction wants real
historical photography rather than the portraits/icons, that rights question
needs Mark's resolution first, not an assumption either way.

**C. The Atlas/map surface hasn't converged onto the brand system yet.** The
public "Church in History" map (`atlas-v3.html`, nav-labeled "Map," the site's
secondary primary CTA) runs its **own separate palette** (`--bg:#f3ecdc`,
gold accents) — not the site-wide parchment/madder tokens the rest of the
marketing pages use. This is a known, named debt (Full-UX-Design §2.5c: "when
the map is next edited it adopts the era-ground palette") that has not
happened. A V2 direction that treats the Atlas as central needs to either
inherit this debt explicitly or pay it down as part of the redesign — it
can't be ignored, since the Atlas is genuinely load-bearing site IA today
(nav-anchored, the homepage's secondary CTA, linked from the Representative
carousel).

**D. The governing UX constitution targets the *app*, not this site — and even
there, it's ahead of what's shipped.** `CiC_Full_UX_Design_V1_0.md` is binding
for `cic-poc/frontend` (the conversation experience), not `cic-website/` — the
Website README says so explicitly ("distinct from the conversational app").
But several of its FINAL, designed pieces are **not yet live** in the actual
app frontend, verified directly against `cic-poc/frontend/src`: no
`LivingTableScene`, no role/mode selector (`RoleSelector`/`role_modes`), no
guided-onboarding three-door threshold. `whats-next.html` says this plainly —
Representative Modes haven't shipped, and "the multi-voice Table experience
does not yet exist on the new [engine] architecture." **Implication for V2
copy and CTAs:** don't let marketing language promise an in-app experience
(seated Living Table, multiple voices at once, mode-adjusted pacing) that
isn't actually there yet. The homepage's current "Bring \[Name\] to the
Table" link is honest about this (it seats a field, never auto-starts), which
is the right posture to keep.

**E. Two same-named, unrelated "Tour" concepts — a naming collision risk, not
yet a live one.** `cic-website/tour.html` is a slide-deck preview of the
*designed app experience itself* (arriving → choosing a tradition → the
Table) — pulled from live nav 2026-07-20, reachable only by direct URL today,
no page actually links to it. The **separate** Hosted-Tour /
Tour-Experience-Module-Phase2 feature — a Representative-adjacent, curated
historical walkthrough — was fully re-scoped 2026-08-03 to launch **from the
Atlas**, Facilitator-narrated, and is unbuilt. Not a live contradiction, but
if V2 gives the Atlas a real "Tour" entry point, `tour.html`'s URL and title
need to not collide with it.

**F. Cost/support copy is genuinely volatile — design for that, don't hardcode
it.** `support.html`'s own header comment records **six** successive reframes
of the cost section in a single week (per-hour vs. per-conversation figures,
itemized vs. qualitative, "we rebuilt" vs. ongoing-work framing), ending back
at simple $1/$2-per-hour editorial figures. This isn't settled; it's actively
still moving. A V2 direction should treat the cost/ask copy as a content slot
the current draft-and-approve discipline keeps rewriting, not something to
bake into a fixed layout or a specific number.

**G. The business-model gate on multi-Representative tables may have already
loosened, unconfirmed.** The V1 log records a hard rule (2026-07-24): "the
multi-select picker" must never be exposed from the free interview entry
point, since multi-Representative tables were a planned paid tier. The
**current live homepage** offers a quiet "Bring \[Name\] to the Table" link
next to every free interview link (dated in-code to a 2026-08-28 ruling),
which seats — doesn't gate — the Table field. This may be an intentional,
later loosening of the old rule, or it may be an oversight. Worth confirming
with Mark rather than assuming either way before D1 designs entry points
around it.

**H. Docs can lag shipped code — including one live, public, user-facing
instance.** `whats-next.html` (live today) lists **"Cappadocian Nicene
Pastoral-Monastic Tradition"** under "Three new traditions are in
development." It isn't in development — it's a seventh live world: built,
merged (`PR #73`, "complete record-native world build, admitted"), its
portrait shipped (`assets/portraits/cappadocian.jpg`), and its status in
`world-census.json` is `"Built & Live"` — already appearing in the homepage's
own Representative carousel. This isn't a planning-doc curiosity; it's the
current live public site telling visitors a shipped tradition is still
upcoming. Worth a same-day content fix independent of V2 (remove Cappadocian
from `whats-next.html`'s "in development" list), not something to wait on the
redesign for. Smaller version of the same pattern: the Icons/Graphics
Decision-Log's own "all six Representatives" framing predates this seventh
world entirely, and `atlas-v3.html`'s header comment still says "not yet
linked from the site" though it's been the primary Atlas nav page since the
2026-08-03 ship flip. Treat any status line in a planning doc — or a page
copy block — as a claim to verify against the actual data, not a fact to
cite directly.

---

## 3. Skim-context findings (lower depth, per the launch prompt)

- **Atlas-World-Map:** the interactive map is real, shipped, load-bearing site
  IA (see §2.C above for its palette debt). Three-view consolidation (Story /
  Wall Chart / Research Table) happened under "Blueprint B5.g" 2026-08-03;
  `atlas.html` and `world-atlas.html` are now redirect stubs into
  `atlas-v3.html`, kept only so old links resolve.
- **Increment-1-Build:** executed the constitution's budget-floor spec
  against the app conversation screen — app-side only, confirms (doesn't
  change) what's summarized in §1 above.
- **Front-End-Integration-Strategy:** the disclosure-tier / clutter-budget
  precursor Full-UX-Design extends; superseded for anything screen-level.
  App-facing, not website IA.
- **Hosted-Tour / Tour-Experience-Module-Phase2:** both superseded 2026-08-03;
  see §2.E above for the live naming-collision risk this creates.
- **Brand-Messaging-Rework:** see §1 — the six protected lines and the
  tradition-not-world rule are locked, live, corpus-wide inputs for D1. One
  open tail: five more "will never try to convert you" instances and some
  doorway phrasing remain in *draft*, not-yet-public documents (FAQ,
  elevator speeches) — a named backlog, not a website blocker.
- **Level2-Mobile-Popover:** small, merged, app-side fix confirming tap→
  popover→full-entry parity with desktop hover→click. No website action.

---

## 4. Proposed for D1 (pending Mark's go)

**Accessibility floor:** WCAG 2.2 AA, as the launch prompt suggests as the
default. Nothing in this immersion pass argues for AAA — but AA needs to be a
standing practice, not a late audit: the live site's own history already
shows two real dark-mode contrast bugs caught and fixed after the fact
(the homepage's access-note text, and inline `--muted` colors on
`support.html` that silently defeated a dark-mode override already sitting in
the shared stylesheet). Each D1 direction should state its floor and show its
contrast math for its own accent choices, not assume the existing tokens are
safe by inheritance.

**Proposed five directions**, chosen from what's actually true about this
project rather than the launch prompt's illustrative list verbatim — each
serves the four charter goals differently, and each has a real, nameable
weakness:

1. **Editorial / long-form storytelling** — pushes the "trade book on
   parchment" register further: the site reads like a literary quarterly,
   Representative stories as feature essays, slow reveal, generous
   whitespace. Strong on storytelling; weakest on "easy access to features"
   and "cutting-edge."
2. **Atlas-first spatial** — makes the interactive map the site's spine, not
   a nav item — visitors explore twenty centuries spatially, with Table entry
   points as stops along the way. Strong on discovery and differentiation;
   risks overwhelming a first-time visitor and competing with the
   constitution's Table-primacy rule.
3. **Institutional-professional / scholarly authority** — modeled on serious
   digital-humanities archives; foregrounds the ten-step build process and
   the sourcing/confidence apparatus up front, restrained grid, minimal
   ornament. Strong on "professional design" and clarity; risks reading cold,
   underserving the "life-changing journey" heart goal.
4. **Quiet-liturgical** — treats the site itself as a small threshold-crossing,
   extending the Living Table's stillness/anti-ghost posture into the
   marketing surface itself — slow pacing, real silence, no motion for its
   own sake. Strong on the heart goal; risks underserving task-oriented and
   returning visitors.
5. **Product-led feature clarity** — modeled on the clearest modern product
   marketing (fast task completion, strong hierarchy, mobile-first). Strongest
   on "easy access to features"; the real risk is the brand's own explicit
   refusal of "tech-forward" — this direction has to prove it can stay warm
   and specific rather than reading as generic SaaS, and D2 should attack it
   hardest on exactly that point.

Recommendation: commission all five — the charter asks for rigor over
economy, and these five pull in genuinely different, non-adjacent
directions rather than five variations on one idea.
