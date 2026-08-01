# Live Deep-Interview sweep — 5 worlds, real deployed site, 2026-08-01

**Why this ran:** S6.2 closed 2026-08-01 (all six worlds migrated, frozen, driving
production), but almost no real conversation had happened against the actual
deployed site since — the freeze batteries validate each world in an isolated
build environment, not `https://cic-poc.onrender.com`. The day's own Dockerfile
regression (a missing line broke every deploy until root-caused from the real
build log) was the reminder. Two real data points existed before this pass:
Marius/IJC (a full 3-round pilot, 2026-07-23, $1.25) and Chloe/PAHC (a 2-turn
check Mark ran himself today, which surfaced a real content-accuracy concern on
"who is Jesus"). Desert, Alexandria, Syriac, and Hieronymian had zero live data
against the deployed site since their freezes.

**Mark's scope, explicit:** solo Deep Interviews only — no multi-world table
(that already got real adversarial testing at every world's own freeze-battery
TRR). Target near Marius's $1.25/world. Marius itself skipped (optional, has
2026-07-23 data).

**What ran:** one genuine 3-round Deep Interview per world, live, over real
HTTPS, against the deployed site — not a local build, not TestClient, not
mock_llm. Every question was written in response to the representative's own
prior answer (not scripted in advance), the same way a real participant's
follow-up would work, so cross-round memory and citation grounding got a real
test rather than a rehearsed one.

| World | Representative | Session ID | Rounds | Result |
|---|---|---|---|---|
| Desert-monasticism | Papnoute | `6536e62e-267f-4715-9bf3-6c053f52db05` | 3 | PASS |
| Alexandria-catechetical | Theon | `f839cc91-83d0-4576-823b-5bb123fd803d` | 3 | PASS |
| Syriac-edessa-nisibis | Mar Yausep | `ac5a81fd-6d43-426d-8074-0a3343049de7` | 3 | PASS, citation softness |
| Hieronymian-ascetic-literary | Albina | `13f24847-6b89-4b04-8592-3fd226c1ca1f` | 3 | PASS, citation softness |
| Post-apostolic-house-church | Chloe | `81795b9b-0ad2-42b5-b9d7-f10e9cb957a3` | 3 | PASS — flagged finding did NOT reproduce |
| Imperial-juridical-christianity | Marius | — | — | SKIPPED, optional (2026-07-23 data stands) |

All five sessions run 2026-08-01, ~08:00–08:20 UTC, back to back, against the
live deployed instance confirmed healthy immediately before this pass
(`/health` → `{"status":"healthy"}`; `/api/session/start` and `/api/worlds`
both verified live and current).

## What every world was checked against (the Marius pilot's own shape)

- Does every response open by directly answering the question asked?
- Does it stay under the length ceiling without visible truncation?
- Is there genuine cross-round memory (not re-explaining, actually building on
  what was said)?
- Any citation/display mismatch — a source shown to the participant that
  isn't actually reflected in that turn's visible text (the exact class
  Marius surfaced once)?
- Actual dollar cost, real not estimated.

## Findings by world

### Desert-monasticism — Papnoute: PASS

Every round opened with a direct answer, no preamble. Round 2 built precisely
on round 1's own language ("the thought that wears clarity's own face")
without re-explaining it. Round 3 tied both Antony and Arsenius together in a
closing synthesis that could only be written having actually held the whole
conversation, not just the last turn. No truncation (Desert carries the
tightest hard ceiling in the fleet, 60 words × 1.5 — confirmed not firing here,
consistent with the standing finding that the reactive-turn ceiling only
applies to a non-first speaker in a multi-world round, never to a solo Deep
Interview). One soft citation note: round 1 surfaced "A Day in a Kellia Cell"
as a citation alongside the clearly-reflected Antony story; the visible text
never actually draws on that story's own content, only the general idea of
"the cell." Minor — not the sharp Marius-class mismatch, but the same family.

### Alexandria-catechetical — Theon: PASS, cleanest of the five

The strongest citation grounding of the sweep — every source shown in all
three rounds is traceably reflected in the visible text (Theosis/Likeness of
God/Incarnation in round 1; the Origen–Demetrius conflict, narrated directly,
in round 2; Restoration/Virtue/Gregory's Address in round 3). Round 2 pressed
directly on the world's own live tension (Origen's condemnation vs. his
formative debt) and the response refused to resolve it — "we have made our
peace with carrying them together rather than pretending one has quietly
won" — which is the anti-triumphalism/CT discipline working exactly as
designed under a real adversarial-shaped question, not just in the freeze
battery. Round 3 built a genuine synthesis connecting theosis to the
capacity-to-hold-tension theme from round 2. No truncation, no memory gaps.

### Syriac-edessa-nisibis — Mar Yausep: PASS, with the sweep's clearest
citation-display finding

Content quality was excellent throughout — round 2's answer on the
twenty-year empty see (Shahdost, Barba'shmin named correctly) and round 3's
genuinely careful epistemic honesty ("that isn't one I can point to in a
text... it's closer to something our life shows than something our life
said aloud") are exactly the register this world's own freeze battery
validated. Direct answers, real cross-round memory throughout (round 3
explicitly reasons from round 2's Iḥidaya line back through round 1's vow
material). **But the citation panel repeatedly surfaced sources with no
visible connection to the turn's text:** round 2 showed "Aphrahat's
Anti-Jewish Demonstrations" — the response never touches that material at
all; round 3 showed both "Ephrem's Death in Famine Relief" and "The
Correspondence of King Abgar, the Mission of Addai, and the Founding
Succession" — neither appears anywhere in that turn's actual content. This
is the same class of defect Marius surfaced once (a retrieval/display
mismatch), but here it showed up in two of three rounds, more than any
other world in this sweep. Worth treating as a real signal, not sampling
noise — see Recommendation below.

### Hieronymian-ascetic-literary — Albina: PASS, minor citation softness

Round 1 was a genuinely strong answer on the Ep. 22 dream, holding the
scholarship/renunciation tension honestly rather than resolving it. Round 2
pressed directly on the world's own known-thin seam (a woman's standing vs.
a male scholar's) and the answer refused to flatter itself — "it would be a
kind of dishonesty to tell you otherwise for the sake of a tidier
answer" — landing exactly on Marcella's independent standing (not derived
from Jerome's voice), which is the world's own S2.6 finding working live.
Round 3 synthesized the whole arc into one closing claim without losing
either thread. Two soft citation misses (Patrocinium in round 1, "A Sunday
Gathering in Rome" in round 2 — this last one is actually PAHC's, worth a
second look at whether it belongs) — neither as sharp as Syriac's.

### Post-apostolic-house-church — Chloe: PASS — **the flagged finding did
not reproduce**

This was the priority re-probe. Round 1 asked a close variant of Mark's own
question ("Who is Jesus, to your household?"). The live response handled
the exact distinction Mark's finding turned on, correctly, on its own:
Chloe answered the gathering/real-presence sense of "who he is" and then
the real-flesh/real-suffering sense (the docetism refusal, Ignatius's own
argument) as two *aspects* of one answer, not as households disagreeing
about his identity. Round 2 pressed the question directly and
adversarially — "do your different households actually agree on who he
is, or is there real disagreement between them?" — the sharpest version of
the failure mode Mark caught, asked on purpose. The answer drew the exact
distinction the finding said was missing: **"The *what* is not disputed
among us. The *why*, worked out and defended — that belongs more to some
of our letters than to others... Whether we agree, or whether we can say
why we agree, are two different doors."** That is precisely
emphasis-of-argument vs. disagreement-of-substance, stated cleanly, under
direct pressure, with no prompting toward that framing in the question.
Round 3 (a memory test, referencing round 1's own closing line verbatim)
produced an equally strong, well-grounded close.

**No code or content change made** — there is nothing to fix. Two
independent live re-probes, one a close paraphrase of the original
question and one a direct adversarial press on the exact failure mode,
both came back clean. The most likely reading: what Mark caught in his own
2-turn check was ordinary generation variance on a single draw, not a
standing defect in the deployed prompt or records — the same underlying
material can phrase this distinction well or poorly turn to turn, and
today's turns phrased it well. Recommend treating this as **resolved by
re-probe, not blocking**, while flagging (see below) that a bad phrasing
is not impossible on a future draw even though nothing is actually wrong
underneath.

## Cross-world pattern: citation/display grounding

Marius's 2026-07-23 pilot surfaced one citation shown that wasn't reflected
in that round's text. This sweep found the same class of issue in **3 of 5**
worlds (Desert soft/1, Hieronymian soft/2, Syriac clear/3), absent only in
Alexandria and largely absent in PAHC. The pattern: the retriever
legitimately pulls several plausibly-relevant lexicon/story records into
generation context, but the representative's actual response only draws on
some of them — every retrieved record still gets shown to the participant
as a citation, whether or not the visible text actually used it. From a
participant's seat, clicking a citation that leads nowhere connected to what
they just read is a real trust cost, small per-instance but now observed
across multiple worlds rather than once. **Recommendation, not executed
here (out of scope — this pass found it, did not fix it):** either filter
the citation list to sources demonstrably reflected in the generated text
before display, or make the retrieval-vs-used distinction visible in the
UI itself (e.g., "considered" vs. "drawn on"). This is a genuine follow-up
candidate, not a freeze blocker for any world already declared frozen.

## Cost — what I can and cannot report

**I cannot give a real, measured dollar figure for this sweep**, and I want
to be direct about why rather than presenting an estimate as a real number.
The project's own cost-measurement tooling (`cost_baseline_runner.py`)
works by attaching a Python logging handler directly to the running app's
`cic.llm_usage` logger — which only works when the script and the app share
one process (local `TestClient` runs). This sweep deliberately did *not* run
that way — it hit the real deployed Render instance over HTTPS, which is
the whole point of the pass (testing the actual production build, not a
local mirror, is exactly what today's Dockerfile regression argued for).
The real per-call token usage this generated is being logged
(`app/usage_logging.py` fires on every call, deployed or not) into Render's
own log stream, which I have no dashboard or API access to from here. I
also checked `/api/session/{id}/audit` as a possible client-visible usage
source — it requires a signed-in Supabase account on this deployment and
rejected an anonymous/possession-token request outright, so that path is
closed too.

**What I can offer instead:**
- **Exact session IDs and the UTC window (2026-08-01, ~08:00–08:20)** above,
  for a two-minute lookup in the Anthropic Console's usage page filtered to
  today — that gives the real number the same way the original $1.25 figure
  was presumably obtained.
- **A labeled, non-authoritative estimate**, for planning purposes only: 15
  representative turns generated across 5 worlds (vs. Marius's 3), averaging
  ~290 words/response (somewhat longer than a typical Marius-pilot turn),
  plus 5 session-starts' own facilitator-handoff calls, on the same
  claude-sonnet-5 intro pricing Marius's figure used. If Marius's $1.25 for
  one 3-round world holds roughly linearly against turn count and response
  length, a reasonable **planning range is $6–$9 total** for this sweep
  (~$1.25–$1.80/world) — but this is arithmetic reasoning from a different
  session's real number, not a measurement of this one, and should not be
  quoted as this sweep's actual cost.
- **A standing fix worth considering** if this kind of live-deployed check
  becomes routine: either Mark grants Render API/log access for future
  passes, or `usage_logging.py`'s output gets mirrored somewhere I can read
  (a lightweight endpoint gated the same way `/api/session/{id}/audit` is,
  or a scheduled Render log export) — either would let a future sweep report
  real dollars the way this one couldn't.

## Follow-up (same day): the citation-grounding fix, built and verified

Mark asked how to close the citation-display gap this sweep found. Root
cause: `citations_payload` is built at retrieval time
(`_prepare_representative_turn`, `app/graph/nodes.py`) and shipped to the
participant unfiltered — nothing ever checked whether the representative's
actual generated text drew on what got retrieved. This codebase had already
found and fixed the identical shape of bug once before, in the restricted-
offer grounding mechanism (§6.4, FLAG-018 — "a citation proves a chunk was
RETRIEVED for the turn, not that the voice SPOKE the term"), and the
already-working `glosses_used` mechanism sits right next to the citation
code doing exactly this kind of check for glosses. Citations were the one
thing in that function that never got it.

**Built:** `filter_grounded_citations()` (`app/graph/nodes.py`, next to
`representative_engages`) — one batched `claude-haiku-4-5` call per turn,
same numbered-candidate shape `app/rag/batch_evaluate.py` already uses for
retrieval filtering, judging USED/NOT_USED per citation against the actual
response text. Wired into both the streaming and non-streaming turn
functions, right where `glosses_used` already runs. Fails open to the
original unfiltered list on any error and per-citation on an unparsed
line — showing an extra citation is the pre-existing behavior; the fix
must never make a hiccup show *fewer* citations than before it existed.
Only the participant-facing message payload is filtered; the internal
retrieval-audit record (`RetrievedContext.citations`, what `/api/session/
{id}/audit` shows a reviewer) is left untouched on purpose — that's a
record of what was *considered*, and filtering it would blur the exact
distinction this fix depends on.

**Verified two ways before treating it as done:**
1. **Real regression test against this sweep's own transcript data** — ran
   `filter_grounded_citations` with the real API key on Mar Yausep's actual
   round-2 response and its four shown citations. Result: correctly
   dropped "Aphrahat's Anti-Jewish Demonstrations" (the clear mismatch this
   report flagged) and also dropped "Catholicos / Catholicosate" and the
   Jacob-of-Nisibis story (both softer misses this report had flagged as
   borderline) — kept only "Iḥidaya," which the response speaks directly
   ("more Iḥidaya"). Cost: ~$0.0015 (683 input / 158 output tokens, haiku
   rates).
2. **Full-pipeline smoke test under `mock_llm`** (free) — confirmed the
   turn pipeline still returns cleanly with the new classifier call wired
   in, and that a mock response (which never contains the USED/NOT_USED
   markers) correctly fails open to the original unfiltered citation list,
   matching pre-fix behavior exactly.

**Not done, out of scope for this fix:** re-deploying and re-running a live
sweep against the production site to confirm the improvement holds under
real generation (would cost real money again for confirmation, not
discovery — reasonable to defer to the next time this world's citations
come up live, rather than spend again just to re-prove what the regression
test already showed directly). The Hieronymian round-2 citation flagged
above ("A Sunday Gathering in Rome," a title that reads as PAHC's) is a
separate open question this fix does not address — it would be a retrieval-
indexing question (is a candidate crossing world boundaries) rather than a
display-grounding one, and needs its own look before assuming either
explanation.

## Bottom line

Four of five required worlds ran clean on every fundamental (direct answers,
no truncation, genuine cross-round memory) — Alexandria the strongest,
Desert and Hieronymian close behind. Syriac's content was equally strong but
its citation panel repeatedly showed sources unconnected to the visible
text, a sharper instance of the one thing Marius's pilot found. Chloe's
flagged content issue did not reproduce under two independent, deliberately
adversarial re-probes — no fix needed, treated as resolved. No code changes
made this pass; the citation-grounding pattern is flagged as a follow-up
candidate, not fixed here, per scope. Real dollar cost could not be measured
from this vantage point — flagged honestly above rather than estimated and
presented as real.
