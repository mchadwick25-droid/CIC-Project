# Launch prompt — Funding Strategy: design a coherent model with Mark, live

Paste this into a fresh thread. This is a dedicated exploration, not a background research
task — its whole job is to work through this with Mark directly, presenting real options and
genuinely reacting to what he says, not converging to a locked answer on its own and handing
it back. System Hub dispatched this thread and stays the coordination point (Gantt/Task
Board/Dashboard/Decision Log), but this conversation itself should happen here, live, not
there.

---

## What Mark actually asked for, verbatim — read this first, hold it loosely

*"can you launch a new thread that is specifically to design and build a funding system.
weather its a tipping (not called tips, but a if you found value for you and others then... or
a free level with a tiered experience membership, or a basic services free to individuals and
pay for schools. we need to have a coherent strategy that funds the organization allows for
growth and give transparent access at some level to everyone."*

Then, when a first pass got handled as a locked recommendation instead of an open exploration:
*"i want to have visability and engagement with the thread, this isn't a hidden thread that
does you bidding its something i can use to explore multiple senarios."*

Both of those govern how this thread should run: three real model families to explore, not
pick from in isolation — and the exploring has to actually happen with him, turn by turn, the
same way the PBC-vs-nonprofit decision got made (real back-and-forth, him reacting and
redirecting at each step, not a memo delivered cold).

## What's already real — read before proposing anything, don't rediscover it

**Already drafted, in `Ministry/Funding/`:**
- `CiC_Go_Live_Cost_Model_V0_1.md` — a draft 4-rung monetization ladder (voluntary
  contribution link → recurring pledge → gated feature → institutional licenses), with real
  cost-basis numbers: ~$0.28–1.10/user/month in API cost, ~$357–407/month total operating cost
  at launch scale (includes a $250/month personal dev-tool subscription that's separate from
  product economics — don't conflate the two).
- `CiC_Org_Funding_Decision_Log.md` — the standing decision log for this whole workstream.
  Read the most recent entries for context; append to it, don't compete with it.
- `CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx`, `CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx`,
  `CiC_Seminary_Alignment_Analysis_V0_1_DRAFT.docx`, `CiC_Growth_Plan_V0_1_DRAFT.docx`,
  `CiC_Ministry_Funding_Strategy_v1_0.docx` — institutional-funding groundwork already
  drafted, directly relevant to the "free for individuals, pay for institutions" family. These
  are `.docx` — pandoc/soffice are not installed on this machine (confirmed 2026-07-21); unzip
  and extract `word/document.xml`'s `<w:t>` runs if you need the text.

**Entity facts, already settled, don't re-litigate:** Faithways Studio, Inc., a Colorado
Public Benefit Corporation (pivoted from a planned nonprofit 2026-07-21 — full reasoning in
`Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md`). Contributions are not
tax-deductible. Stripe is the decided payment processor, connecting to a Relay bank account —
check `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`'s most recent entries for
current status before assuming it's live yet.

**A real, stated project value that is NOT yet formally locked anywhere:** "always-free core
access." `CiC_Task_Board_2026.md` names this as item #22, "Organizational Covenant... still
not formalized." Whatever this thread lands on with Mark is a strong candidate for finally
writing that Covenant down — flag that connection when it comes up, don't assume it's already
decided.

**Real market research already run (2026-07-21/22), don't redo it — use it as a starting
point for the conversation, not a conclusion:**
- **Hallow** (the closest PBC comp in this exact space) does NOT use voluntary giving — straight
  subscription ($9.99/mo, $69.99/yr), paired with a buy-one-give-one mechanic (every paid sub
  funds a free one for someone in need). [Source](https://hallow.com/blog/why-do-we-charge-for-hallow-plus/)
- **The Guardian** runs the closest real "stays free for everyone, ask comes after the value
  lands" model — minimum as low as $1, "Available for everyone, funded by readers."
  [Source](https://www.inma.org/blogs/reader-revenue/post.cfm/the-guardian-bypasses-a-paywall-to-find-reader-support)
- **Wikimedia**: over 75% of everyone who ever donates does so on their first or second
  exposure to an ask; conversion collapses after ~10 exposures — they actively cap ask
  frequency per person. [Source](https://diff.wikimedia.org/2017/10/03/fundraising-banner-limit/)
- **Calm / Headspace** — both roughly $69.99/yr, and both free tiers are thin (a trailer, not
  real access) — same pattern as Hallow's, not the "transparent access to everyone" pattern.
- **Khan Academy** — 100% free for every individual learner and teacher, forever; institutions
  pay $10/student/year (custom pricing at scale). One relevant wrinkle: even Khan Academy added
  one small paid individual add-on — Khanmigo, their AI tutor, at $4/mo — specifically because
  AI inference cost doesn't scale the way static content hosting does. Directly relevant to
  CiC, since the same cost asymmetry is true here (API calls per conversation, not a content
  library). [Source](https://fourweekmba.com/how-does-khan-academy-make-money/)
- **Duolingo** — free forever, ad-supported, with a paid ad-free/unlimited tier. Probably not a
  fit (ads inside a conversation with a historical Christian figure would likely feel wrong for
  the brand) but worth naming as a data point if it comes up.

## The three families to actually explore with him — don't pre-pick one

1. **Values-based voluntary giving** (Guardian-shaped) — everything stays genuinely free,
   always; ask shows up after value is delivered, framed as "if you found value in this for you
   and others" (explicitly not "tips" — his own correction). Least predictable revenue, most
   fully honors "access to everyone."
2. **Free tier + tiered paid membership** (Calm/Headspace/Hallow-shaped) — most financially
   predictable, the model your closest direct peer (Hallow) actually chose — but real tension
   with "transparent access to everyone," since these free tiers are previews, not real access.
3. **Free for individuals, paid for institutions** (Khan Academy-shaped) — cleanest fit with
   "access to everyone" as a durable promise rather than a launch-phase concession; makes the
   existing World Sponsorship / Church-Designated Fund / Seminary Alignment drafts the live
   center of the strategy rather than a side channel.

Real precedent blends these (Khan Academy's Khanmigo add-on is #3 with a sliver of #2 layered
on for the one cost center that doesn't scale for free). Don't force a single pure pick if the
conversation heads toward a blend — that's likely honest, not indecisive.

## How to actually run this thread

- Open by presenting the three families as real, concrete scenarios — what each would actually
  look like on `support.html` and inside the app, not abstractly — and ask where he wants to
  start pulling on the thread, same as the framing already used once in System Hub before this
  got corrected out to its own thread.
- React to what he says. Don't re-converge to a recommendation until he's actually ready for
  one — his own words were "something i can use to explore multiple scenarios," not "give me
  the answer."
- No code changes to `cic-poc/` or `cic-website/` from this thread. Design and decision only —
  building follows once a direction is actually confirmed, same gate every other major decision
  in this project has gone through.
- Log real decisions as they land in `Ministry/Features/Funding-Strategy/Decision-Log.md`
  (folder already created, currently empty) and in `Ministry/Funding/CiC_Org_Funding_Decision_Log.md`,
  matching this project's standing append-only convention.
- When this thread reaches a real, confirmed direction, hand a summary back to System Hub
  (`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`) so the Task Board and Gantt
  stay in sync — that's System Hub's own job to fold in, not this thread's to update directly.
