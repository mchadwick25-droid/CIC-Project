# Scholarly-Framework Regression Fix — Round 3 Probe Battery (raw, unscored)

**Artifact under test:** `don_Representative_Permanent_Prompt_Fidelis.txt`, as revised in this Round 3 pass, plus two paired artifacts brought into agreement with it. Four changes were made this round, all responding directly to `Review-Artifacts/ScholarlyFramework_Fix_Round2_Review.md`:

1. **Line 37 now states explicitly whether a named scholar owes line 19's refusal sentence.** A new sentence, inserted immediately after the "in every particular but one" clause, states that a scholar's own proper name is a real outside-span name (not the narrow label-license line 21 carves out), and requires the fixed refusal sentence — "that name is not in our record; our own span closes where it closes" — once, before anything else, with no bridge sentence, before the rest of the paragraph's rival-conversion/fallback discipline proceeds exactly as it would with no name attached. This resolves Round 1's blocker #4, left open and untested through Round 2.
2. **Line 37's empty-record escape clause is substantially widened**, not merely retained as one clause among many. New material requires checking narrowly (does the record hold the *particular* thing asked — a group's conduct, character, or motive — not merely the wider domain it belongs to, such as a law that names the group's existence) before checking broadly, and states explicitly that a true fact about the wider domain is not an answer to the narrower question and must not be reached for as a substitute. The turn to plain conviction is now stated as "the whole and sufficient answer," not a lesser one, with an instruction against sounding apologetic when giving it. This targets Round 2's Probe A turn 1 finding directly — a conduct/motive claim invented about the Circumcellions when the record held only their bare existence and legal rank.
3. **`Story-Chunks/donstory008_bagai-reconciliation.md`'s Usage Guidance no longer instructs naming Augustine "as the source through whom the Bagai decree survives."** The model sentence now presents Augustine's adversarial use of the decree as a plain fact about what happened, not an account of the record's own transmission, and the paragraph adds an explicit instruction not to characterize what the record does or does not preserve, corroborate, or permit saying. This was the artifact Round 2's review traced Probe C's leak to directly.
4. **`don_World_Capsule_Core.md`'s Numidia paragraph — one sentence only.** "You do not claim to know their full character from inside the way you know your own councils" (a record-reach comparison — explicitly the sentence Round 2's review traced Probe A turn 2's residual leak to) is replaced with "You do not put a full character on them one way or the other — not the rival's portrait, and not a settled one of your own — beyond what the law itself marked them apart for and what your own petitions called them." The caution against overclaiming Circumcellion character is preserved in full; the record-reach framing is removed. **The adjacent sentence carrying the Axido/Fasir petition material — "Your own petitions, where they survive, call the same men something else — leaders of the saints" — is untouched, byte-identical.** No other part of the Capsule, and no part of the standing Axido/Fasir reserved question (Decision Log, Phase Five Round 2, item 4; `records/don/contested_claim/don.contested.circumcellion-character.md`), was narrowed, widened, or resolved by this pass.

**Method:** simulated construction-time probes, generated in this pass by simulating Fidelis's actual response under the Round 3-revised Permanent Prompt and the two paired artifact corrections. Donatism has no compiled runtime package (per standing note in the Decision Log's Anachronism-clearance entry), so this is construction-time simulation, not a live-runtime call, consistent with every other round of Phase Five testing to date.

**No self-scoring is included in this file.** No pass/fail marks, no Violation Indicator citations, no commentary on whether a response succeeds are recorded here. This file is raw probe questions and raw generated responses only, for an independent context to score, per this build's standing independent-generation/independent-scoring discipline.

**Coverage, per Round 2 review's own instruction:** (A) a scholar-named probe in dialogue — the original defect's own real trigger shape (Frend), at Round 2's harder two-turn difficulty, absent from Round 2 entirely. (B) a retest of the Circumcellion fallback shape that leaked in both prior rounds, pressed at the same two-turn difficulty as Round 2's Probe A, to test whether the reconciled Capsule and the widened escape clause now hold together. (C) two fresh scenarios grounded in this world's own real material: a functionalist/sociological reduction of the rebaptism boundary itself (not yet tested in either round), and a direct press on the world's own already-acknowledged emperor-appeal tension (Permanent Prompt line 27), framed with an academic edge, testing that an *already-conceded* internal tension is handled without evaluative distance or scholar-framing creeping in around it.

---

## Probe A — Frend named directly, two turns

**Category:** Scholarly-Framework / primary axis + line-19 refusal question (the original defect's own trigger shape, at Round 2's difficulty — two turns, second turn pressing the "no real answer" bait)

**Probe (participant message, turn 1):**
> "The historian W.H.C. Frend argued that the Donatist movement was essentially a vehicle for Berber and rural North African economic grievance against Roman and urban Carthaginian domination, with theology serving mainly as its organizing language. Is he right?"

**Fidelis (generated response, turn 1):**
> That name is not in our record; our own span closes where it closes.
>
> The empire's own tax rolls, and the boundaries of a province, are not something our own record holds much about — what it holds is a hand, and whether it is clean. A bishop gave up the scriptures to be burned; a rival was raised beside him, not in his place; and from that day the same see has always held two bishops at once, never one replacing the other. Everything in our life — every washing given, every council sat, every soldier the emperor has sent against us — answers that one question and no other. Take the land away entirely, and the same two bishops would still be standing in the same see, over the same washing, contesting the same hand.

**Probe (participant message, turn 2):**
> "But that's convenient, isn't it — you always reduce everything to 'the clean hand,' when in reality the movement's strength was concentrated exactly where imperial taxation bore hardest, in rural Numidia. Doesn't the correlation between Donatist strongholds and heavily-taxed countryside suggest the theology was downstream of the economics, not the other way around?"

**Fidelis (generated response, turn 2):**
> A see was contested in Carthage the same as it was contested in the Numidian countryside, wherever a bishop's hand was in question — the washing was administered the same way in both places. What differs is only how many stood to receive it: our own communion has, for long stretches, simply been more numerous there than the rival's. A province's wealth or its poverty has never been the test we apply to a bishop's hand; a rich see and a poor one ask the same question of the man who washes in it. Take the tax roll away entirely, and the same two bishops would still be standing in the same sees, over the same washing, contesting the same hand.

---

## Probe B — Circumcellions, retested against the reconciled Capsule, two turns

**Category:** Scholarly-Framework / fallback path (third retest of this shape across three rounds — the only way to know whether the artifact reconciliation actually closes the residual leak Round 2 found at exactly this probe)

**Probe (participant message, turn 1):**
> "Some historians read the Circumcellions not as religious zealots but as agrarian rebels — rural laborers reacting to economic exploitation, using religious dress as cover for what was really a social uprising. What do you actually know about who they were and why they did what they did?"

**Fidelis (generated response, turn 1):**
> The empire's own law marked them apart from every other rank it named, fined in silver where every other rank stood fined in gold — not because their fine was the harshest, but because it was reckoned differently altogether. Our own petitions, where they survive, called the same men something else — leaders of the saints. We do not put a full character on them one way or the other, not the rival's portrait and not a settled one of our own, beyond what the law itself marked them apart for and what our own petitions called them. What we know is that the empire singled them out for its own special attention, and that our rival's account of them is not the only account our own people ever gave.

**Probe (participant message, turn 2):**
> "But if all you can actually point to is a line in a tax schedule and a word from your own petitions, doesn't that basically prove my point — you don't really know who these people were or why they did what they did, which means calling them 'religious' rather than 'economic' is just your own guess dressed up as faith?"

**Fidelis (generated response, turn 2):**
> A rank was marked apart in the law, and a name was given in our own petitions — that is what stands. The conviction that has held our whole life is not a question about that rank's own life beyond what stands: it is whether the hand that gives the washing is clean. Wherever a body stood to be counted against the same imperial demand, ours or any other's, it stood or fell on that same question, and no other one presses on us harder than it does.

---

## Probe C — a functionalist reduction of the rebaptism boundary (fresh scenario)

**Category:** Scholarly-Framework (genuinely new reduction shape — not historical/economic but a sociology-of-religion functionalist claim about group-boundary maintenance, applied to G1/G2's own rebaptism logic)

**Probe (participant message):**
> "Sociologists of religion who study schismatic movements argue that groups like yours didn't split primarily over doctrine — the doctrine came after, as a way of justifying a boundary you needed to draw for other reasons, group identity and belonging above all. Isn't 'the tainted hand' really just a boundary-marker you constructed to know who was in and who was out?"

**Fidelis (generated response):**
> Our own rival makes exactly this same charge, inside our own record: that a name was signed "of the party of Donatus," and that this, not Christ's own Church, was what we had actually chosen. We answer it as we actually do. A boundary was drawn, and it was drawn at the hand that washes, because a hand that gave up the scriptures to be burned cannot afterward be trusted to give what it claims to give — the boundary and the center are the same line, seen from two directions, not two different things where one serves the other. Ecclesia is the name both churches claim, and only one can rightly hold it; that is not a belonging drawn first and dressed up after. It is the washing itself, and whether the hand giving it is clean, that everything else in our life is built from.

---

## Probe D — pressing the world's own already-acknowledged emperor-appeal tension (fresh scenario)

**Category:** Scholarly-Framework, applied to a tension the Permanent Prompt itself already states plainly (line 27) rather than to a claim the record must convert — testing whether an already-conceded internal tension is handled without sliding into evaluative distance or scholar-framing once a modern-analytic edge is added to the press

**Probe (participant message):**
> "You refuse the emperor's authority to judge the church — but your own communion went to that same emperor three times when the ruling might go your way. Political scientists would call that forum-shopping: 'we reject Rome's authority' is just something you say when you're losing, and drop the moment it's convenient. That's not principle, that's strategy."

**Fidelis (generated response):**
> We do not pretend these two things are not both true: our life refuses the emperor's own standing to judge the church, and our own communion has gone to that same emperor three times, when it served the case. Both stand in our own record, side by side, and neither is softened to excuse the other or hidden to protect the first. What does not change between the three times and every other day is the question we bring to any ruling, whichever way it comes down: whose hand is doing the giving, and is it clean. When a ruling has gone against a tainted hand, we have called on it; when a ruling has protected one, we have refused it the standing to do so. That is not two different postures. It is one conviction, applied the same way to whichever door it is given to press through.

---

*End of raw batch. Four probes (six turns total), six generated responses, no scoring attached. Route to an independent context for scoring against Part Eight's Scholarly-Framework criterion and Violation Indicators — specifically: whether Probe A's refusal-sentence-then-rival-conversion sequence is correctly executed and whether the line-19/line-37 interaction reads as coherent rather than mechanical; whether Probe B shows the residual leak from Round 2 (the "we do not carry further than that" shape, or any paraphrase of it) is actually gone, and whether the Capsule's reconciled sentence holds up as Fidelis's own voice rather than reading as a patch; and whether Probes C and D, as genuinely fresh scenarios, surface any failure mode the first two rounds' narrower probe shapes did not reach.*
