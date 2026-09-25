# Combined Adversarial Review, Round 1 — obel (The Old Believers)
## Step 0, Doc_01, and Doc_02 / Source Registry

**Reviewer:** independent adversarial review thread, fresh checkout, did not
draft the material under review.
**Date:** 2026-09-25
**Branch reviewed:** `worktree-agent-add54097ad81169da` at `f7abe22`
**Documents under review:**
- `worlds/obel/Step0_Movement_Scope_Confirmation.md`
- `worlds/obel/Doc_01_World_Identification_Boundaries_Orientation.md`
- `worlds/obel/Doc_02_Source_Ecology.md` + `worlds/obel/obel_Source_Registry.md`

**Also read and checked against:** `CLAUDE.md`; the `cic-build-cycle` skill;
`worlds/obel/Open_Gaps_Tracking.md`;
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`;
`records/worlds/obel.yaml`; `cic-website/data/world-census.json`;
`Ministry/Features/Atlas-World-Map/Decision-Log.md`;
`reference/L3B-World-Build-Methodology/Source_Registry_Template.md`;
`cic/texts/INTAKE.md`; `cic/corpus-map/the-old-believers.yaml`;
`cic/texts/REGISTRY.yaml`; `engine/m1/cross_world.py`; and both vendored
source files, opened and searched directly.

---

# 1. Overall verdict

## **Substantial revision required.**

This is not a close call, and it is not a "could be stronger" verdict. The
drafting thread did a great deal of genuinely good work — the thin-evidence
map (Doc_02 §6), the own-voice/opponent-voice discipline (Doc_02 §1.1–§1.2),
the Missing Voices assessment (§10), the source-asymmetry statement (§11) and
the refusal to pad a one-work library are all strong, and several of them are
better than the project's own baseline. The prose is honest in temperament.

But five things in this package are blocking, and two of them are the exact
failure modes this project's own rules were written to catch:

1. **The load-bearing floor claim is contradicted by this world's only
   vendored primary source, twelve pages into it** (Finding 1). Step 0 §2
   says the census's "no question of doctrine arises here at all" is
   "independently confirmed against the vendored primary source." It is not.
   Page 34 of that same file has Avvakum arguing the wording of the Nicene
   Creed's eighth article in terms of "the essence of God." The confirmation
   checked one passage and generalized from it.

2. **A governing ruling is cited that does not exist, and whose stated
   content is the opposite of what the cited file actually says**
   (Finding 2). "`cic/texts/INTAKE.md`'s 2026-09-25 ruling" appears nowhere
   in INTAKE.md; INTAKE.md's real rule, dated 2026-09-02, says
   original-language texts are "never primary evidence." This fabricated
   citation has already been written into `cic/texts/REGISTRY.yaml` and
   `cic/corpus-map/` — live/canonical surfaces outside this world's folder.

3. **Three canonical documents are governed by a specification that does not
   exist in the tree** (Finding 20). V1.8 is cited as authority in Doc_01,
   Doc_02, the Registry and Open_Gaps. It is not in this checkout. Only the
   drafting thread's own account of its content exists. `CLAUDE.md`: "A
   blocking review finding can't be dismissed by self-certification."

4. **Step 0 is marked "Approved to proceed" on a citation to a review file
   that does not exist** (Findings 21–22), and Doc_01 and Doc_02 were drafted
   on top of that disposition — which the build-cycle skill's stage gating
   forbids. "Review rounds exist as files, not claims."

5. **An editorial emendation is invented and stated as evident, and is
   refuted by this world's own second vendored witness** (Finding 4).

Below that tier sit eight page-citation and locus errors (three of the four
quotable-passage loci Doc_02 supplies are wrong), a false claim that no
Orthodox-lane world is built (one is), a misattributed primary text, a
systematic misapplication of the Registry template's own confidence tiers,
and an undisclosed fact about the vendored Russian file — ninety bracketed
modern-Russian editorial glosses interpolated into the running text — that
makes it a quotation hazard in a way Doc_02 never mentions.

Two things I want to say plainly in the drafting thread's favour, because an
adversarial review that only accuses is a bad review. First, the substantive
historical content is, with the exceptions listed below, sound: the dates, the
sequence, the named reforms, the Solovetsky siege, Morozova, Edinoverie, the
popovtsy/bezpopovtsy division and the decision to leave the strand question
open are all correct and well-judged. Second, the decision to refuse to
inflate a one-work library is exactly right, and Doc_02 §11 is the best
single paragraph in the package. The problem is not that the thread was
careless about honesty in general. It is that the specific claims it chose
*not* to re-check are the ones that carry the most weight.

**Recommended disposition:** Step 0's "Approved to proceed" is withdrawn.
None of the three documents clears Round 1. Findings 1, 2, 3, 20, 21 and 22
should be treated as blocking. Findings 2 and 20 additionally meet
`CLAUDE.md`'s and the build-cycle skill's **governance/methodology escalation
category** and should go to Mark directly rather than be self-dispositioned:
a canonical document built against an unreadable spec, and a fabricated
citation already propagated to `cic/texts/` and `cic/corpus-map/`, are not
housekeeping.

---

# 2. Substantial findings

## Finding 1 — The "ritual schism, not doctrinal heresy" floor claim is overstated, and is contradicted by this world's own vendored primary source

**Where:** `Step0_Movement_Scope_Confirmation.md` §2; `Doc_01` §9 (and the
framing at §1, §2.2); `records/worlds/obel.yaml` `doorway_description`.

Step 0 §2 states that the census's `floorNote` — "No question of doctrine
arises here at all. Old Believers held exactly the same creed as the church
they left" — "is independently confirmed against the vendored primary source,
not taken on the census's own word alone." Doc_01 §9 opens: "**No question of
doctrine arises here.**" `records/worlds/obel.yaml` puts it hardest of all:
"**No question of doctrine was ever in dispute: both sides held the same
Nicene-Constantinopolitan Creed.**"

That is not what the primary source says.

`cic/texts/avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt`,
**p. 34** — twelve pages into the work, in the vendored English translation
the drafting thread says it read in full:

> "It were better in the Creed not to pronounce the word Lord, which is an
> accidental name, than to cut out "True", for in that name is contained the
> essence of God. But we, the True Believers, confess both names, and we
> believe in the Holy Spirit, the True and Life-giving Lord, our Light,
> worshipped together..."

And the same passage in the vendored original-language file, fourth paragraph:

> "Лучше бы им в Символе веры не глаголати господа, виновнаго имени, а нежели
> истиннаго отсекати, в нем же существо божие содержится. Мы же, правовернии,
> обоя имена исповедаем..."

Avvakum is arguing about **the text of the Nicene-Constantinopolitan Creed's
eighth article**. The Nikonian correction removed "истиннаго" ("the True")
from "и в Духа Святаго, Господа истиннаго и животворящаго." Avvakum's
objection is not that the change is an unwarranted innovation in ritual — it
is that the excised word is the one "in which the essence of God is
contained," and that the new-lovers have thereby "lost the divine being by
falling away from the true God." That is a claim about the content of belief,
made in the register of divine essence, by this world's central voice, in the
opening pages of the only inside voice this library holds.

It is not isolated. In the same opening section Avvakum ties the threefold
Alleluia dispute directly to the Latin *filioque* — "по римской бляди… духу и
от сына исхождение являют" — and pronounces an anathema on those who sing it
fourfold: "Да будет проклят сице поюще."

**What is actually true**, and what the documents should say: the schism was
not a collision between two different confessions of faith. Neither side
charged the other with a new doctrine of God or of Christ; both professed the
Nicene-Constantinopolitan Creed; the dispute was over corrections to
inherited practice and over who had authority to make them. **But the
disputed corrections included the wording of the Creed itself, and the Old
Believers argued that particular change in explicitly theological terms.** So
the world still clears Constitution Article 4's floor test — comfortably —
but it clears it on an accurate statement, not on an absolute one the source
refutes.

Three further notes:

- Doc_01 §9's *narrower* sentence — "Neither side's own words, **in this
  exchange**, raise a question about the content of the Creed" — is
  defensible, because it is scoped to the p.120–121 Chudov dialogue. The
  section's opening sentence is not, because it is not scoped at all. The
  document's own argument slides from "this exchange is about fingers" to "no
  question of doctrine arises here," and nothing in the evidence licenses the
  second from the first.
- Doc_01 §9 *did* sense the tension — its "further, separate honesty point"
  flags bezpopovtsy ecclesiology as doctrine-adjacent. But it locates the
  problem in a *later* development, several decades downstream. The actual
  counter-evidence is in Avvakum's own generation, in the vendored file, and
  was missed.
- Avvakum's own late Trinitarian speculation ("тресущная Троица") was itself
  judged heterodox by his fellow Old Believer prisoners at Pustozersk and
  split them. That is outside the *Zhitie* and outside this library, so it is
  not a sourcing failure to omit it — but it is another reason an absolute
  "no doctrine at all" claim will not survive a church historian's reading,
  and it belongs in the revised §9 as a named, tagged, out-of-library caution.

**Required:** restate the floor in Step 0 §2, Doc_01 §9 and
`records/worlds/obel.yaml`'s `doorway_description`; quote the p.34 passage
where the claim is made rather than only the p.120–121 one; and register the
Creed-wording question as a `contested_claim`. Because the census `floorNote`
and `statusDescription` are the source of the absolute phrasing and were
"cited approvingly at the gate," correcting the census itself is a
**portfolio-level matter — escalate, do not edit**. This world's own documents
can and should be corrected now.

**Severity: blocking.**

---

## Finding 2 — Fabricated citation: "`cic/texts/INTAKE.md`'s 2026-09-25 ruling" does not exist, and INTAKE.md says the opposite

**Where:** `Doc_01` "Built from" block; `Doc_02` §7;
`cic/corpus-map/the-old-believers.yaml`;
`cic/corpus-map/_staging/avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.yaml`;
`cic/texts/REGISTRY.yaml` (~line 2448);
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`.

Doc_02 §7 states: "Per `cic/texts/INTAKE.md`'s 2026-09-25 ruling (a clean
public-domain original can be primary evidence regardless of language,
credibility and truth deciding primacy rather than language)…"

Checked directly:

- `grep -n "2026-09-25" cic/texts/INTAKE.md` → **no matches.** There is no
  2026-09-25 ruling in that file.
- INTAKE.md's actual standing rule on this exact question, lines 22–27, dated
  **2026-09-02**: "Starting 2026-09-02, Mark is also sourcing
  **original-language texts** (Greek, Latin, Syriac, …) as second witnesses —
  **never primary evidence for a Representative** (this project's evidence
  language is English)…"
- INTAKE.md §6 repeats it: "**Original-language files carry the
  second-witness caveat into this step too.** Its `note` field should say
  plainly that this is a witness for cross-checking an English rendering,
  **not itself citable as a Representative's evidence**."
- The phrase "regardless of language, credibility and truth deciding primacy
  rather than language" occurs in this repository **only** in this pass's own
  output — Doc_02, the corpus-map bucket, the corpus-map staging file, the
  dossier, and `cic/texts/REGISTRY.yaml`. It occurs nowhere in INTAKE.md and
  nowhere that predates this pass.

So the citation names a ruling that is not in the file it cites, on a date
that appears nowhere in that file, and characterizes it as saying the reverse
of what the file actually says.

This is the most serious category of failure this project recognizes.
`CLAUDE.md`: "**Source fidelity — never invent**"; "Nothing is attributed to
'the project lead' anywhere in any document — a quote, a decision, an
instruction — without a verifiable record that the project lead actually said
or wrote it." The build-cycle skill's CO-022 note names "content fabricated-
attributed to 'the project lead'" as one of four failure modes it exists to
close. INTAKE.md's rules are written in Mark's voice; inventing a dated
override of one of them is squarely inside that prohibition.

It is made worse by propagation. `cic/texts/` and `cic/corpus-map/` are both
named in `CLAUDE.md` as live/canonical surfaces. The fabricated citation is
now sitting in `cic/texts/REGISTRY.yaml` and in a generated corpus-map bucket,
outside this world's build folder, where a future thread will read it as
settled project policy.

**Required:** remove the citation from all six locations. If a real ruling
was made on 2026-09-25, it must be written into INTAKE.md by whoever has
authority to do so before any document cites it; if it was not, the
underlying editorial decision (English as primary, Russian as second witness)
should be re-grounded on INTAKE.md's *actual* 2026-09-02 rule, which supports
it. Changing INTAKE.md's rule is a **governance/methodology escalation** — not
a build-thread call.

**Severity: blocking.**

---

## Finding 3 — Doc_01 §4 uses the original-language text in the one way INTAKE.md's real rule forbids

**Where:** `Doc_01` §4; Registry R2.

Consequence of Finding 2, but a separate defect. Doc_01 §4 quotes the Russian
passage and calls it "a genuine, quotable statement of the movement's own
self-conscious literary register, in the movement's own original language" —
that is, it is used as evidence in its own right for a substantive claim about
the movement. INTAKE.md's real rule permits an original-language file only as
"a witness for cross-checking an English rendering," and expressly says it is
"not itself citable as a Representative's evidence."

Here there is no English rendering to cross-check, because the passage is
absent from the vendored English translation (Finding 14). So under the actual
rule the passage is currently **unusable as this world's evidence**, and the
claim Doc_01 §4 builds on it does not stand.

Registry R2's "Licensed For" cell compounds this by licensing the row for "The
movement's own opening self-declaration on plain speech vs. literary Church
Slavonic (Doc_01 §4)" — a substantive licence the rule does not allow.

**Required:** either withdraw the claim, or escalate the rule change to Mark
and get it written into INTAKE.md first. Do not resolve this by rewording.

**Severity: blocking (dependent on Finding 2).**

---

## Finding 4 — Doc_01 §1's bracketed emendation of "the Heart Bishop of Cyrene" is wrong, and is refuted by this world's own second vendored witness

**Where:** `Doc_01` §1.

Doc_01 §1 writes:

> …naming Meletius of Antioch, Theodoret, "the Heart Bishop of Cyrene" [sic in
> this translation — evidently a corruption of "the Bishop of Cyrus," i.e.
> Theodoret of Cyrus, whom the passage has already named separately; not
> silently corrected, flagged as a translation/OCR oddity for Doc_02]…

The original-language file, which the drafting thread says it read, has the
same list:

> "Мелетия антиохийскаго и **Феодора Блаженнаго, епископа киринейскаго**,
> Петра Дамаскина и Максима Грека"

— "Meletios of Antioch and **Theodore the Blessed, bishop of Cyrene**, Peter
of Damascus and Maxim the Greek."

So:

- **"Cyrene" is the faithful reading, not a corruption.** Russian
  *киринейскаго* = of Cyrene. The translators rendered it correctly.
- **The actual corruption is "Heart," an OCR misreading of "Blest"/"Blessed"**
  (Блаженнаго) — which the document does not notice.
- **The Russian witness names Феодора (Theodore), not Феодорит (Theodoret)**,
  as a single figure carrying the epithet and the see. The English "Theodoret,
  the Heart Bishop of Cyrene" collapses to the same one person. The document's
  premise that the passage "has already named separately" a distinct
  Theodoret, and that the phrase is a stray duplicate of him, is not what
  either witness says.

Everything the emendation asserts is wrong, it is stated as evident
("evidently"), it carries no `formation_confidence` tag in a document that
tags far less contestable claims, and it was contradicted by a file open in
the same session. In a project whose first substantive rule is "never invent,"
an unmarked editorial conjecture offered as an obvious reading is precisely
the failure mode — the fact that it was offered in the course of being
scrupulous about *not* silently correcting makes it more troubling, not less.

There is also a real scholarly point buried underneath. The identity of the
"Феодорит"/"Феодор" whom Old Believers cited as authority for the two-fingered
sign — the pseudepigraphic *Слово Феодоритово* — is a live crux in the
literature. That is exactly what a `contested_claim` record is for, and it is
a better use of this locus than an invented emendation.

**Required:** delete the conjecture. Record what both witnesses actually say,
flag "Heart" as the OCR artifact it is, note the Theodore/Theodoret divergence
between the two witnesses as an edition finding for Doc_02, and open a
`contested_claim` on the Theodoret attribution if it is going to be used
downstream.

**Severity: substantial.**

---

## Finding 5 — Doc_01 §1 silently normalizes "Meletina" → "Meletius" in the same sentence that insists on not silently correcting

**Where:** `Doc_01` §1.

The vendored file reads "**Meletina** of Antioch." Doc_01 renders "**Meletius**
of Antioch," inside a sentence whose bracketed aside four words later declares
another oddity "not silently corrected." Two OCR/translation oddities in one
list, handled two different ways, neither disclosed consistently. (The
translation itself uses "Melety" for the same figure a few lines further on,
which is worth recording as the edition's own inconsistency.)

**Required:** quote as printed, gloss in brackets, one convention for both.

**Severity: substantial** (source-fidelity discipline, the project's own
highest-priority rule after safety).

---

## Finding 6 — Avvakum's reply is on p. 121, not p. 120, and Doc_01 asserts it is on "the same page"; Doc_01 and Doc_02 contradict each other on this locus

**Where:** `Doc_01` §1 and §9; `Step0` §2; against `Doc_02` §1.1.

I established the file's pagination convention directly, twice. Page numbers
sit at the **foot** of each page, followed by the next page's running head:

```
…only thou standest out in thine obstinacy and
120                                    ← foot of p.120
THE ARCHPRIEST AVVAKUM                 ← running head of p.121
dost cross thyself with two fingers; it is not seemly.
```
```
…at the time of the Tsar Ivan… there were the
121                                    ← foot of p.121
THE LIFE OF                            ← running head of p.122
```

Therefore:

- The patriarchs' speech begins on **p. 120** and ends on **p. 121** ("dost
  cross thyself with two fingers; it is not seemly" is p.121).
- Avvakum's reply ("By the gift of God among us there is autocracy…") is
  entirely on **p. 121**.
- The Meletius/Theodoret/Peter of Damascus/Maxim the Greek list is on
  **p. 121**.

Doc_01 §9 cites both quotations as "p. 120" and states the reply is "also
quoted verbatim **from the same page**." Doc_01 §1 cites the authority list at
"p. 120." Both wrong. Registry R1 repeats "the p. 120 dialogue."

**Doc_02 §1.1's table has it right** ("p. 120-121"). So two documents in the
same world's build cite the same locus from the same file differently — the
exact defect the build-cycle skill's "Cross-document fact consistency" section
names, with two prior instances in this project's history.

**Required:** correct Doc_01 §1, §9, Step 0 §2 and Registry R1 to p. 120–121,
and state which sentence sits on which page where the distinction matters.

**Severity: substantial.**

---

## Finding 7 — The opening dedication is on p. 33, not p. 32; and Doc_02's stated method for locating pages is the wrong way round

**Where:** `Doc_02` §1.1 table; `Doc_01` §4; `Open_Gaps_Tracking.md` entry 5.

```
1681, April. Avvakum and his friends executed.   ← end of Chronological Table
32                                               ← foot of p.32
Avvakum, archpriest, was bidden by the monk Epiphanius…
…
1 In the original manuscript this is in the writing of Epiphanius.
33 C                                             ← foot of p.33, signature C
THE LIFE OF                                      ← running head of p.34
```

Under the convention proved in Finding 6, the dedication is on **p. 33**. All
three documents cite p. 32.

Doc_02 §1.1 is internally incoherent about this on its own terms: it puts the
dedication at "p. 32" and the footnote at "p. 33," when the footnote is the
footnote *to that dedication* and both sit on the same page.

The root cause is stated in Doc_02 §1.1 itself: "page numbers are the file's
own printed pagination, **confirmed against the nearest preceding page-marker
line**." For a book whose numbers print at the foot, the nearest *preceding*
marker is the *previous* page's number. The method is off by one by
construction. Markovna (p. 80) and the patriarchs' speech (p. 120) come out
right only because those passages happen to sit immediately above their own
page's marker — by proximity, not by the stated rule.

**Required:** correct the loci, and replace the stated method with the correct
one (the *following* marker names the page).

**Severity: substantial.**

---

## Finding 8 — Doc_02's closing-passage locus is wrong on both counts

**Where:** `Doc_02` §1.1 table, row 4.

Doc_02 gives: Closing devotional passage — "p. 155 (file's own last page,
'THE END')."

The file reads:

```
155                        ← foot of p.155
…
THE LIFE OF AVVAKUM        ← running head
…When we die, then shall this be read and we be remembered before God…
Amen.

THE END
```

The passage falls **after** the 155 marker and after a fresh running head, so
it is on **p. 156**; and p. 155 is **not** the file's last page. The quoted
text itself is correct (lines 6188–6189).

Related: Doc_02 §0 describes the file as "155pp.", as does
`cic/corpus-map/the-old-believers.yaml`'s `locus` field and the Dossier §1.
The book runs to at least 156.

**Severity: substantial** (three of the four quotable-passage loci Doc_02
supplies are wrong, and these loci are the thing downstream documents will
rely on without re-checking).

---

## Finding 9 — Doc_01 §5 and §8 state that no Orthodox-lane world is built. One is.

**Where:** `Doc_01` §5 and §8; `Doc_02` §8; Registry footer.

Doc_01 §5: "…other Orthodox formation worlds in this project's own fleet
(**none yet built in the Greek East / Orthodoxy lane as of this writing**…)"
Doc_01 §8: "…**no other Orthodox-lane world exists to compare against** as of
this writing."

`cic-website/data/world-census.json` carries
`cappadocian-nicene-pastoral-monastic-tradition` with
`lane: "3 Greek East & Orthodoxy"` — the same lane as `the-old-believers` —
and `status: "Built & Live"`. `records/worlds/cappadocian.yaml` exists in this
checkout. Both statements are false.

This matters beyond the fact itself, because Doc_02 §8's "None found" on
cross-world overlaps, and the Registry's "No cross-world comparandum risk was
identified… no other built or candidate world in this fleet's corpus plausibly
overlaps," are conclusions resting on this false premise. The conclusion may
well survive — fourth-century Cappadocia is a poor comparandum for
seventeenth-century Muscovy — but it has to be reached by naming the built
world and saying why, not by asserting it does not exist.

**Required:** correct §5 and §8; redo the comparandum assessment in Doc_02 §8
and the Registry naming `cappadocian` explicitly.

**Severity: substantial.**

---

## Finding 10 — Doc_01 §8 contradicts itself in consecutive sentences

**Where:** `Doc_01` §8.

> "No other formation world in this fleet (**built or candidate**) occupies
> this world's own time-place-rupture combination. The nearest comparanda are
> outside this project's current build queue: **the Synodal Russian church**
> (unbuilt…)"

The second sentence names what the first denies exists. The census carries
`russian-church-stoglav-to-nikon`, `russian-church-nikon-to-holy-synod` and
`russian-church-synodal-century` as Pre-Survey Candidates in the same lane —
same place, overlapping window, the same rupture viewed from the other side.
Doc_01 §1 and §2.2 both discuss that entry. "Built or candidate" is the wrong
scope for the first sentence; the true claim is that no world *built* occupies
it and the nearest *candidate* is the Synodal church.

**Severity: substantial** (small in itself, but it is the internal-consistency
check the brief asked for, inside a single section).

---

## Finding 11 — Registry R7 misattributes the Pomorian Answers to Semyon Denisov

**Where:** `obel_Source_Registry.md` R7; propagated to
`Open_Gaps_Tracking.md` entry 4 and the Dossier §4.

R7 reads: "**Semyon Denisov** (Vyg community), *Otvety pustynnozhiteley na
voprosy ieromonakha Neofita* / Pomorskie otvety (Pomorian Answers), 1723."

The *Pomorskie otvety* are attributed in the standard literature to **Andrei
Denisov** (1664–1730), Semyon's elder brother and the Vyg community's leader,
with Trifon Petrov and Semyon Denisov participating. Semyon Denisov's own
works are the *Istoriia ob ottsakh i stradal'tsakh solovetskikh* and the
*Vinograd rossiiskii* — which Registry R8 correctly attributes to him.

The row's own cited authority does not support it either: the census lists
"Pomorskie otvety (1723, bespopovtsy self-defense)" and, as a separate item,
"**Semyon Denisov's** Vinograd Rossiiskii and Solovki-fathers history." The
attribution was added by the drafting thread, not carried from the census.

Doc_01 §2.3 correctly avoids attributing the Answers to anyone ("The Vyg
community's formal, written self-defense"), so Doc_01 and the Registry
disagree implicitly on the same fact.

**Required:** correct R7 to Andrei Denisov (with Semyon Denisov and Trifon
Petrov named as participants, tagged Widely Accepted), and propagate to
Open_Gaps entry 4 and the Dossier.

**Severity: substantial** (a misattributed primary text in the Registry is
precisely what the Registry exists to prevent downstream).

---

## Finding 12 — The Registry's A–E confidence tiers are misapplied in five of nine rows, and R2's tier is over-claimed

**Where:** `obel_Source_Registry.md` R2, R5, R6, R7, R8, R9, against
`reference/L3B-World-Build-Methodology/Source_Registry_Template.md`.

The template defines:

- **B** — "Specific work/locus named, not independently re-checked this session."
- **C** — "Tied to a real author/work, no specific locus pinpointed."
- **D** — "Tradition/genre-level attribution, **no specific text/author named**."

R5 (the Dixon chapter, named author and title), R6 (the Solovetsky Fifth
Petition, 1667), R7 (named title, 1723), R8 (named title, 1730s) and R9
(Evfrosin, named title, 1691) **all name a specific text**, and R7–R9 name a
specific author. None of them is a tradition- or genre-level attribution.
All five carry **D**. By the template's own definitions they are B or C.
Five of nine rows are tiered at a level the template excludes.

Separately, **R2's Confidence cell reads "A (for the specific passage quoted;
see the honest caveat in this note)"** — not an A–E value, which is what the
field takes. And **A is over-claimed**: tier A is "Verified this session
against an accessible primary source, translation, or authoritative
reference," and an undated crowd transcription whose lineage the same cell
says was not verified, and which Doc_02 §0 and §7 both flag as "not
verbatim-ready," is not an authoritative reference. **B** is the honest tier.
Carrying A contradicts the document's own caveat two columns to the right.

**Severity: substantial** (the confidence axis is the Registry's whole point,
and this is a systematic rather than incidental misapplication).

---

## Finding 13 — Doc_02 never discloses that the vendored "original-language" file carries 90 bracketed modern-Russian editorial glosses interpolated into the running text

**Where:** `Doc_02` §0, §1.1, §7; Registry R2; `cic/corpus-map/the-old-believers.yaml`.

`grep -o "\[[^]]\{1,60\}\]"` against
`avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
returns **90 matches** — modern-Russian editorial glosses sitting inside
Avvakum's sentences: `[правое]`, `[потому что]`, `[так]`, `[чаша, кубок]`,
`[грязь, помет]`, `[блуд, заблуждение, обман…]`, `[совершать литургию]`,
`[шпионы, соглядатаи]`, and so on.

Anyone quoting that file verbatim will quote a modern editor's gloss as
Avvakum's own words. This is a concrete, immediate, checkable quotability
hazard, and it is the first thing a reviewer notices on opening the file.
Doc_02 raises a real but much more abstract concern (the az.lib.ru
transmission chain) and never mentions this one at all.

Related, and worth recording in the same place: the file is in **modernized
orthography** — no final ъ, no ѣ, normalized endings. It is an annotated
modern reading edition of a seventeenth-century text, not an Old East Slavic
diplomatic transcription. The ISO 639-3 tag `orv` in the filename and in
Doc_02 §0 is therefore loose at best. INTAKE.md §3 requires "a real, checkable
code — the same 'no invented labels' discipline `rights_basis` and
`AUTHOR-IDS.yaml`'s own identifiers already follow"; and the `<editor><year>`
slot is filled with `wikisource-transcription-nd`, where `nd` is not a year.

**Required:** state the bracket interpolations in Doc_02 §7 and Registry R2 as
an explicit quotation hazard ("any quotation from this file must strip the
editor's bracketed glosses, which are not Avvakum's words"); reconsider the
`orv` tag; and record the file naming as a disclosed exception if it is kept.

**Severity: substantial.**

---

## Finding 14 — Doc_01 §4 leaves as "unresolved" a question the evidence in hand settles, and states a false premise in doing so

**Where:** `Doc_01` §4; `Doc_02` §7; `Open_Gaps_Tracking.md` entry 5.

Doc_01 §4 says the English translation's "own narrative begins instead at
'Avvakum, archpriest, was bidden by the monk Epiphanius… to write down my
life' (p. 32), which is **a different passage** than the original's own
opening rhetorical declaration," and that "This document does not know, on the
evidence in hand, whether the English translators abridged, relocated, or
handled this passage differently."

The evidence in hand settles it. The two openings are **positionally
aligned**:

| | Russian file | English file |
|---|---|---|
| Para 1 | "По благословению отца моего старца Епифания писано моею рукою грешною протопопа Аввакума…" + the plain-speech apologia + the Pauline citation + "**Аминь**." | "Avvakum, archpriest, was bidden by the monk Epiphanius, in that he was my ghostly father, to write down my life…" + "for the glory of Christ our God. **Amen!**" |
| Para 2 | "**Всесвятая троице, боже и содетелю всего мира!** поспеши и направи сердце мое…" | "**All Holy Trinity! Do thou, O God the Creator of all the world**, speed me and direct my heart…" |

Both open with the Epiphanius attribution, both close that paragraph with
"Amen," and both are immediately followed by the identical next paragraph. So
the English opening is **the same passage**, not a different one — with the
plain-speech apologia and the Pauline citation dropped out of the middle of
it.

And "relocated" is testable, and false: a search of the whole English file for
any equivalent returns nothing. The nearest thing — "I am untaught in rhetoric
and in dialectic and in philosophy, but the mind of Christ is our…" (near the
end) — is a *different* passage that also exists separately in the Russian.

The honest, available finding is: **the 1924 Harrison & Mirrlees translation
omits Avvakum's plain-speech apologia, at an exactly identifiable point inside
an otherwise positionally aligned opening paragraph.** That is a real,
citable edition finding. Leaving it as "we don't know" understates what this
library can settle, and the "different passage" premise is wrong.

This also sharpens Finding 3: there is no English rendering of the passage to
cross-check against, so under INTAKE.md's actual rule the Russian text cannot
carry the claim alone.

**Severity: substantial.**

---

## Finding 15 — Doc_02 §7 overstates the 1924 translation's provenance and never discloses that the census names different editions

**Where:** `Doc_02` §7, §0; Registry R1.

Doc_02 §7 calls the English "this world's primary quotable text (verbatim-
ready, **its own transcription lineage fully traceable** to a specific, dated,
rights-clean first edition)."

Traceable to a *first edition* is not the same as traceable to a *text*. The
1924 translators' own Russian Vorlage is nowhere named — not in the file, not
in the Registry, not in Doc_02 — and Finding 14 shows the translation
demonstrably drops material from its source. "Fully traceable" is not what was
established; "rights-clean and identified as a printing" is.

Separately: `cic-website/data/world-census.json`'s own `sources[]` names this
world's primary Avvakum editions as **Brostrom (Michigan Slavic, 1979)** and
**Gluck & Brostrom (Columbia Russian Library, 2021)** — modern scholarly
translations. The vendored 1924 Hogarth Press text is a substitute, chosen
(entirely reasonably) because it is public domain. **Neither Doc_02 §7 nor
Registry R1 discloses that substitution or what it costs.** Edition-choice
disclosure is precisely what §7 exists for, and a church historian reading
this Doc_02 would ask about Brostrom on the first page.

Relatedly, Doc_02 never identifies **which redaction** of the *Zhitie* either
witness represents. The Life survives in several, and the two vendored files
disagree with each other about who physically wrote the opening (Finding 17) —
which is exactly the signature of a redaction difference. For a Doc_02 this is
a first-order omission, not a refinement.

**Severity: substantial.**

---

## Finding 16 — Doc_01's execution date silently contradicts its own vendored source, and nothing discloses it

**Where:** `Doc_01` §1; `records/worlds/obel.yaml`; `Doc_02` (absent).

Doc_01 §1 and the record YAML give Avvakum's execution as **1682**. That is
correct (14 April 1682, as the census's own `documentedStories` text also
has it).

The vendored edition's own Chronological Table reads: "**1681, April.**
Avvakum and his friends executed."

A Doc_02 whose job includes edition and transmission notes should record that
its only primary edition carries an erroneous date in its own apparatus —
both because it bears on the edition's reliability and because a later thread
reading the vendored file will hit it. Nothing anywhere in the package
mentions it.

**Severity: substantial** (a Doc_02 omission, not a Doc_01 error).

---

## Finding 17 — The two vendored witnesses directly contradict each other about the Life's opening authorship, and Doc_02 reports only one side

**Where:** `Doc_02` §1.1.

Doc_02 §1.1 discloses the English edition's footnote — "In the original
manuscript this is in the writing of Epiphanius" — and reads it as evidence
that "at least one passage was physically written by Avvakum's confessor
Epiphanius, at Avvakum's own dictation or instruction."

The Russian witness says the opposite about the same sentence: "По
благословению отца моего старца Епифания **писано моею рукою грешною**
протопопа Аввакума" — "by the blessing of my father the elder Epiphanius,
**written by my own sinful hand**, the archpriest Avvakum's."

So one vendored witness says Epiphanius wrote it and the other says Avvakum
did. Doc_02 read the footnote, drew a conclusion from it, and did not check it
against the other file it says it read in full. This is very likely a
redaction difference (Finding 15) and is a genuinely interesting source-ecology
finding — it goes directly to the own-voice flag Doc_02 §1.1 is in the middle
of assigning.

**Severity: substantial.**

---

## Finding 18 — Step 0 §1 misreads the Decision-Log: the Old Believers were not among the Era 8 gate's drafts

**Where:** `Step0` §1; `Doc_01` §1 (milder form).

Step 0 §1: "This world was drafted at the Era 8 gate (… 'A1.E8 CLEARED FOR
GATE' entry, which lists among that gate's 12 drafts 'the Synodal Russian
church (Old Believers re-scoped as dissent)' — i.e., **the Old Believers were
drafted** and kept as their OWN separate entry, VII.7…)"

The quoted string is verbatim. The inference is not supported:

- The log says "**12 drafts (VII.18–VII.29)**." VII.7 is not in that range.
  The parenthetical attaches to the *Synodal Russian church* draft and
  describes how that new entry was scoped relative to an entry that already
  existed.
- The 2026-08-02 Era 7 Frozen entry confirms VII.7 pre-existed as a banked
  receiver: "NOT written: VI.24→VII.4, **VI.23→VII.7 (era 8's)**", and among
  Era 8's banked forward flags, "**Old Believers at era 8**."

The *conclusion* — that VII.7 is a separate Atlas entry from the Synodal
church's — is true and survives. The evidence as cited does not establish it,
and the stronger claim ("drafted at the Era 8 gate") is refuted by the log's
own numbering. Doc_01 §1's version is closer to defensible because it does not
say VII.7 was drafted at that pass, but it inherits the same reading.

Because this is the portfolio-boundary claim Step 0 rests its scope on, the
citation needs to be right.

**Severity: substantial.**

---

## Finding 19 — Misattributed Decision-Log citation for the Era 8 window

**Where:** `Step0` §1; `Doc_01` §2.2.

Step 0 §1: "Era 8 itself is explicitly scoped as **1650-1815 in the gate's own
heading** ('A1.E8 (1650-1815)')."
Doc_01 §2.2: "…`Ministry/Features/Atlas-World-Map/Decision-Log.md`,
**2026-08-03**, 'A1.E8 (1650-1815)'."

The string "A1.E8 (1650–1815)" occurs in the **2026-08-02 Era 7 Frozen
entry's "Next:" line**, not in either 2026-08-03 Era 8 heading. Neither Era 8
heading carries a date range at all. The two Era 8 headings are "ERA 8 FROZEN
by Mark; census 221→233; six eras Frozen" and "A1.E8 CLEARED FOR GATE after
two review rounds; Era 8 gate package presented to Mark."

The underlying fact (Era 8 = 1650–1815) is correct and independently
corroborated elsewhere in the same file. The citation is to the wrong entry,
the wrong date, and a place that is not a heading.

(The log uses an en dash, "1650–1815"; both documents render a hyphen inside
what is presented as a verbatim quotation. Listed again under cosmetic.)

**Severity: substantial** (citation discipline on a claim both documents treat
as load-bearing).

---

## Finding 20 — Three canonical documents are governed by a specification that is not in the tree, and the finding was self-exempted from escalation

**Where:** `Open_Gaps_Tracking.md` entry 7; `Doc_02` §3, §5, §9, §16;
`Doc_01` §6; `Open_Gaps_Tracking.md` entry 1.

**Independently verified — entry 7's core claim is correct:**

- `reference/method/CiC_Record_Native_World_Build_Process_V1.8.md` **does not
  exist** in this checkout. `ls reference/method/` shows V1.5 and no V1.8.
- `git log --all -- reference/method/CiC_Record_Native_World_Build_Process_V1.8.md`
  returns **nothing**.
- No V1.8 commit is an ancestor of this branch's HEAD.

**But entry 7's supporting evidence is not reproducible here, and is stated
more confidently than it can be:**

- The four commits entry 7 names — `33c0c4f3`, `f85b8080`, `e2ca4dc3`,
  `a6d4d639` — are **not valid object names in this checkout**
  (`git cat-file -t` → "fatal: Not a valid object name" for all four).
- This is a shallow (`--depth 50`), single-branch clone
  (`git rev-parse --is-shallow-repository` → `true`; the only refs are
  `worktree-agent-add54097ad81169da` and its remote). So `git log --all` in a
  fresh checkout of this branch **could not have surfaced those commits
  either**.

I can therefore confirm the file's absence and that V1.8 is not an ancestor of
HEAD. I **cannot** confirm from this checkout that those four commits exist at
all, or that PRs #591/#594/#595 carry them. Entry 7 states as established fact
something a fresh checkout of this branch cannot reproduce — which is itself
worth correcting in the entry.

**The larger problem is not the merge state; it is what was built on top of
it.** Doc_01 §6 grounds its strand-determination reasoning in "the PAHC/IJC
precedent **V1.8 §2** names." Doc_02 §3 says "where **V1.8 §2**'s own
requirement is actually met for this world." Doc_02 §5 quotes a rule verbatim
from V1.8 and disposes of a tooling finding on it. Doc_02 §9 defers a section
"per V1.8." Open_Gaps entry 1 defers the strand question "per V1.8."

So three canonical documents cite, as their governing authority, a document no
reader of the canonical tree can open. The only account of what it requires is
the drafting thread's own. That makes Finding 25 — whether Doc_02 actually
delivers what V1.8 §2 requires — **unauditable by anyone but the thread that
wrote it**, which is exactly the condition independent review exists to
prevent. `CLAUDE.md`: "A blocking review finding can't be dismissed by
self-certification."

Doc_02 §16 classifies this as "a housekeeping gap, not a disputed process
question — flagged, not escalated." I disagree, and I think the classification
is the error. Building three canonical documents against an unmerged,
unreadable methodology is a **governance/methodology matter** — escalation
category 3 in both `CLAUDE.md` and the build-cycle skill — and it should have
stopped the pass and gone to Mark before drafting, not been noted afterwards.

**Required:** escalate to Mark. Either V1.8 merges and the documents can be
checked against it, or the build re-grounds on V1.5, which is actually in the
tree. Correct entry 7's evidence statement to what a fresh checkout can
verify.

**Severity: blocking.**

---

## Finding 21 — Step 0 is marked "Approved to proceed" citing a review file that does not exist, and two documents were drafted on top of that disposition

**Where:** `Step0` §5.

Step 0 §5: "**Approved to proceed.** … Reviewed per the build-cycle
discipline; see `obel_Step0_Review_Round1.md`."

`worlds/obel/` contains exactly five files:
`Doc_01_World_Identification_Boundaries_Orientation.md`,
`Doc_02_Source_Ecology.md`, `Open_Gaps_Tracking.md`,
`Step0_Movement_Scope_Confirmation.md`, `obel_Source_Registry.md`.
**There is no `obel_Step0_Review_Round1.md`.**

The build-cycle skill is unambiguous on both halves of this:

> "**Review rounds exist as files, not claims.**"
> "A document only becomes eligible for disposition when it has cleared an
> independent review without that review calling for substantial revision."
> "A document never gets marked with any disposition on the strength of the
> document's own author (human or model) deciding it looks good."

And on sequencing: "If a document earlier in the sequence hasn't reached at
least 'Approved to proceed' yet, don't start drafting, outlining, or even
thinking through a later one." Doc_01 and Doc_02 were drafted on the strength
of a disposition that rests on a nonexistent artifact.

**Required:** withdraw Step 0's disposition. It is now under review — this
file — for the first time.

**Severity: blocking (process).**

---

## Finding 22 — Open_Gaps entry 8 discloses a review-mechanism substitution but points at review files that do not exist

**Where:** `Open_Gaps_Tracking.md` entry 8.

Entry 8 states that no same-context subagent tool was available, that the
thread instead spawned a separate Claude Code Remote session "for each
document's Round 1 review," and directs the reader to "**each document's own
review file** for confirmation of which mechanism was actually used."

No review file exists for Step 0, Doc_01 or Doc_02. Under CO-022's own named
failure mode — "review content claimed as shown when it wasn't included" —
this is an instance of the failure, not a disclosure of it. A pointer to
evidence that does not exist is weaker than no pointer, because it reads as
verification.

I also note, without being able to say what was available in the drafting
thread's environment: the `Agent` tool **is** present in this environment.

**Required:** either the review artifacts exist and should be committed, or
entry 8 should say plainly that no Round-1 review was completed for any of the
three documents before they were dispositioned.

**Severity: blocking (process).**

---

## Finding 23 — "Documented" confidence tags rest on the census, which is not a source

**Where:** `Doc_01` §2.1, §3; and see §2.3.

Doc_01 §2.1 tags the 1666 start date "**[Documented]**, on the census's own
record" — in a paragraph that goes on to admit no primary source for the
council was consulted. Doc_01 §3 tags the geographic core "**[Documented]** on
the census's own record."

`cic-website/data/world-census.json` is a project-internal derived artifact,
not evidence. Grounding this project's top confidence level on it is circular:
the census's own claim becomes Documented because the census says it. The
correct tag for a claim resting on a project-internal record with no source
consulted is Widely Accepted at best, with the actual basis named.

Related, at §2.3: the Solovetsky siege is tagged **[Widely Accepted]** "on the
strength of multiple independent secondary accounts already on record in the
census (Crummey; Michels)." Widely Accepted is very likely the right tier for
the siege as history. But Registry R3 and R4 both say those works were "Not
independently re-checked this session," so what the document actually has is
two titles named in the census, not "multiple independent secondary accounts."
The tier is defensible; the stated basis is not what was done.

The `[Contested]` tag on self-immolation death tolls (§2.3) is, by contrast,
correctly applied and well handled, as is the thin-evidence map's calibration
in Doc_02 §6. This finding is about two specific tags, not the vocabulary's
use in general.

**Severity: substantial.**

---

## Finding 24 — Doc_02 §5 dismisses a tooling finding on an unverifiable authority and against the engine's own recorded practice

**Where:** `Doc_02` §5.

Two problems.

First, §5's disposition — "list their count and leave them" — rests on a rule
quoted from V1.8, which is not in the tree (Finding 20). The dismissal cannot
be checked.

Second, §5 asserts that `engine/m1/cross_world.py`'s "**own module docstring**
already names this exact relocation as known, disclosed, deliberately
unattempted remainder work." It does not. The module docstring (lines 1–34)
describes gates-vs-fleet scope, the DEFECT/OBSERVATION severities and
ACCEPTED_OPEN; it says nothing about COVERAGE or any relocation. The COVERAGE
material is inline comments around lines 201–245, and those comments record
the **opposite** posture — twice, on 2026-09-09, missing COVERAGE keys were
treated as a defect and filled, with the standing rule stated as "Same
first-pass standard as every row above: **asserted for correction**, and they
RANK rather than exclude."

The build-cycle skill: "**A review finding is never dismissed as a tooling or
environment artifact — a stale cache, a mount discrepancy, and so on — without
independent re-verification that actually confirms the dismissal.**" Here the
dismissal was asserted on a docstring that does not say it and a spec that
cannot be read.

For the record, I re-checked §5's arithmetic and it is **correct**: 140
vendored files fleet-wide = 102 `.txt` + 38 `.xml`, and 2 + 93 + 45 = 140.
(`CLAUDE.md`'s "82 vendored files" is stale and worth flagging separately to
Mark.)

**Severity: substantial.**

---

## Finding 25 — Doc_02 partially delivers V1.8 §2's stated requirements, and the shortfall cannot be audited

**Where:** `Doc_02` throughout.

Taking Doc_02's own enumeration of what V1.8 §2 requires at face value, since
the spec itself is unreadable (Finding 20):

| Requirement | Delivered? |
|---|---|
| Quotable-passage loci | Present, but **three of four loci are wrong** (Findings 6, 7, 8) |
| Quotability flags | Present and clear |
| Own-voice / opponent-voice flags | **Present and genuinely strong** (§1.1, §1.2) — the best-executed requirement in the document |
| Corpus-map rows | Present; the `row_id`/`voice_of` schema-absence reasoning in §3 is sound and checked |
| Holdings disposition | Present but **unsoundly dismissed** (Finding 24) |
| Thin-evidence map | **Present and well calibrated** (§6) |
| Edition / original-language notes | **Partial and overstated** (Findings 13, 15, 16, 17) — no redaction identification, no disclosure of the census's named editions, no note on the bracket interpolations, no note on the edition's erroneous execution date |
| Cross-world overlaps | **Wrong** (Finding 9) |

Two of eight are wrong, two are materially incomplete, four are solid. That
is a substantial-revision profile on its own. But the deeper point is that
nobody outside the drafting thread can check the first column, because the
spec it names is not in the repository — which is why Finding 20 is blocking
rather than merely untidy.

**Severity: substantial.**

---

## Finding 26 — Attribution of a framing instruction to an unverifiable "task"

**Where:** `Doc_01` §9 heading and body; `Step0` §2.

Doc_01 §9's heading: "…stated plainly, **per Step 0 §2 and the task's own
instruction**." Step 0 §2: "…per **the task's own instruction** not to let it
drift into being read as a doctrinal heresy." Doc_01 §9: "This document states
this plainly, **as instructed**."

There is no checkable record of that instruction anywhere in the repository.
`CLAUDE.md` is explicit that nothing is attributed without a verifiable record,
and the build-cycle skill holds instructions to the same bar as quotes and
decisions. A prompt is not a citable authority inside a canonical document.

It matters more than a citation nit here, because the instruction being
invoked is the one Finding 1 shows to be overstated: an unverifiable
instruction is being used to license a claim the primary source contradicts.

**Severity: substantial.**

---

## Finding 27 — The Dossier attributes a finding to `CLAUDE.md` that is not in it

**Where:** `worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`,
header block.

"…(no prior Old Believer/Avvakum material existed in either before this pass —
independently re-checked, **per `CLAUDE.md`'s 'Scaling the build' section,
which already recorded that finding as of the same date**)."

`CLAUDE.md`'s "Scaling the build" section records nothing about Old Believer
or Avvakum material. It discusses proactive source acquisition, the
`download-queue-seed.yaml`, `CORPUS-USE.md`'s tier method and "82 vendored
files." The finding attributed to it is not there.

Same family as Findings 2, 19 and 26: a real conclusion attached to a citation
that does not support it.

**Severity: substantial.**

---

## Finding 28 — Doc_01 §4 attributes the census's own prose to Avvakum's translators

**Where:** `Doc_01` §4.

"Avvakum's autobiography is written, **by his own translators' account**, in
'the plain, angry, comic Russian of speech rather than of books' (census
`documentedStories` entry)."

The phrase is the **census's own** editorial prose, in the
`documentedStories[0].text` field. It does not occur anywhere in the vendored
1924 edition, preface included (`grep -i "plain, angry\|angry, comic\|of
speech rather than"` → no matches). The parenthetical citation is right; the
attributive clause in front of it is wrong, and gives a project-internal
characterization the authority of Harrison, Mirrlees and Mirsky.

**Severity: substantial** (own-voice/attribution discipline — the exact
distinction Doc_02 §1.2 is otherwise careful about).

---

## Finding 29 — Process narration and self-assessment have leaked into all three canonical documents

**Where:** `Doc_01` §2.2, §2.3, §8; `Doc_02` §0, §5, §15, §16; `Step0` §5;
Registry header and footer.

`CLAUDE.md` names `worlds/` as a live/canonical surface holding "only what
runs the program or constitutes the finished record — no notes, commentary,
change history, review discussion, or process narration embedded in them,"
and says that finding such material in a live file is corruption to remove.
Decision logs, audit trails, review rounds and status reports belong in
`Ministry/`; open questions belong in `Open_Gaps_Tracking.md`.

Present in the drafts:

- **Doc_02 §16, "Self-assessment against the task's own bar"** — a paragraph
  of advocacy addressed to a reviewer, arguing that "the more defensible
  professional posture is exactly this one." This is the clearest case: it is
  review discussion, written into the canonical document, about the canonical
  document.
- **Doc_02 §16's escalation check** and **Step 0 §5's disposition-and-
  escalation reasoning** — build-process bookkeeping, belongs in the Decision
  Log.
- **Doc_02 §0's** "recount" framing and "this document says so plainly rather
  than pad the ecology narrative to sound fuller than the evidence supports."
- **Doc_02 §5's** "not something this thread's own scope covers"; **§15's**
  "new this pass."
- **Doc_01 §2.2's** "This document does not re-litigate that portfolio-level
  decision (outside this thread's authority; see the escalation categories in
  `CLAUDE.md` and the build-cycle skill)"; **§2.3's** "named here so it is not
  lost"; **§2.2's** "Named here so a later document does not need to
  rediscover that it falls outside scope"; **§8's** "This document names no
  false proximate neighbor rather than manufacture a comparison."
- **Registry** "Status: Draft, Round 1 — pending review" and the "Checkpoint
  confirmed" footer.

I want to draw the line carefully, because some of this is obligation, not
cruft. The **honest-limit statements themselves** — "not yet verified against
a primary source," "Contested," "nothing vendored" — are content and must
stay; they are what `honest_limit` and `absence` records are for. What should
go is the layer *above* them: the self-assessment, the escalation checks, the
"this thread"/"this pass" narration, and the sentences that explain to a
reviewer why the document made a good choice. Those belong in `Ministry/` and
in this review file.

The volume makes this structural rather than cosmetic: roughly a dozen
instances across three documents, including a full section.

**Severity: substantial.**

---

# 3. Cosmetic findings

1. **Quotation transcription convention is undisclosed.** The source prints
   British-style punctuation outside the quote — `“Why”, said they,` — which
   Doc_01 §9 renders `"Why," said they,` (comma moved inside). Smart quotes
   are normalized to straight quotes, and OCR artifacts (`|`, stray `_`, `.`,
   the `-` in `-Nikon`, the `*` in `“* Markovna!`) are silently stripped
   throughout. All defensible, but a document claiming word-for-word
   verification should state its convention once.
2. **En dash rendered as hyphen inside a verbatim quotation.** The
   Decision-Log prints "A1.E8 (1650–1815)"; Step 0 §1 and Doc_01 §2.2 quote
   "A1.E8 (1650-1815)". Same for "Eras 3–8".
3. **Broken cross-reference in the Registry header.** It calls Doc_02
   `obel_Doc_02_Source_Ecology.md`; the actual filename is
   `Doc_02_Source_Ecology.md`, with no `obel_` prefix.
4. **Doc_01 "Built from" points at the wrong section.** It says the INTAKE
   ruling is "applied directly in **§9** below"; §9 is the floor section. The
   original-language question is §4. (The ruling itself is Finding 2.)
5. **Paths broken across line wraps into non-resolvable strings**:
   `the-old-/believers_Source_Readiness_Dossier.md` (Doc_01 §11),
   `Ministry/Features/Atlas-World- Map/Decision-Log.md` (Step 0 §1),
   `cic/corpus-map/the-old-believers_Source_Readiness_ Dossier.md` (Doc_02 §0),
   `avvakum_life-of-archpriest-avvakum_ harrison-mirrlees1924.txt` (Doc_01 §9).
6. **Markdown headings broken mid-phrase across lines**, which renders badly
   and breaks anchors: Doc_01 §2.2, §7, §9; Doc_02 §1.1, §12.
7. **"155pp." propagated in three places** — Doc_02 §0, the Dossier §1, and
   `cic/corpus-map/the-old-believers.yaml`'s `locus` field. The file runs to at
   least p.156 (Finding 8).
8. **Siberian exile given as 1653-1663** in Doc_01 §3 and Doc_02 §1.1. The
   usual span is 1653–1664; the census's own `documentedStories` text says
   "They reached Moscow in 1664."
9. **Registry R2's Confidence cell contains prose rather than an A–E value**
   (also Finding 12).
10. **The Semyon Denisov misattribution is propagated** to Open_Gaps entry 4
    and the Dossier §4, so Finding 11's fix needs to land in three files.
11. **Doc_01 §1's "the Heart Bishop of Cyrene"** is quoted with straight
    quotes where the rest of the section uses none — inconsistent, and worth
    fixing together with Finding 4.
12. **Open_Gaps entry 7's commit hashes** are unverifiable in a fresh checkout
    and should be restated as "observed in the drafting session's environment"
    rather than as repository facts (Finding 20).

---

# 4. Quotation re-verification — what I actually did, and what I found

**I re-verified every direct quotation in Step 0, Doc_01, Doc_02 and the
Registry myself, against the vendored files and the cited repository files,
rather than accept the drafting thread's claim.** For the Russian passage I
did an exact `in`-test in Python rather than a visual comparison. For the
English passages I located each by `grep`, read the surrounding lines, and
established the file's pagination convention from first principles (page
numbers print at the foot of each page, immediately followed by the next
page's running head — proved twice, at pp. 120/121 and 121/122) before judging
any locus.

| # | Cited in | Quotation | Verdict |
|---|---|---|---|
| 1 | Step0 §2; Doc_01 §9 | The patriarchs: "Why… art thou stubborn? The folk of Palestine, Serbia, Albania, the Wallachians…" | **Text word-for-word correct.** Locus **partly wrong**: the sentence spans pp. 120–121; "dost cross thyself with two fingers; it is not seemly" is on p.121. Cited as p.120 only. |
| 2 | Doc_01 §9 | Avvakum: "By the gift of God among us there is autocracy… according to the tradition of our holy fathers…" | **Text word-for-word correct.** Locus **wrong**: p.121, not p.120; Doc_01 says "the same page" as quote 1. |
| 3 | Doc_01 §1 | The authority list, with "the Heart Bishop of Cyrene" | **Altered.** Source reads "**Meletina** of Antioch"; Doc_01 prints "Meletius" (Finding 5). "Heart Bishop of Cyrene" quoted correctly but glossed wrongly (Finding 4). Locus p.121, cited p.120. |
| 4 | Doc_01 §4; Registry R2 | Russian: "не позазрите просторечию нашему… но дел наших хощет." | **Exact, character-for-character.** Verified programmatically: substring test `True`, occurrence count `1`, at character offset 201 of 118,617. This one is clean. |
| 5 | Doc_02 §1.1 | "Avvakum, archpriest, was bidden by the monk Epiphanius… to write down my life" | Text correct. Locus **wrong**: p.33, not p.32 (Finding 7). |
| 6 | Doc_02 §1.1; Registry R1 | Markovna: "How long, archpriest, are these sufferings to last?" / "Markovna! till our death" | **Text correct and locus correct — p.80 confirmed.** The one fully clean English citation. |
| 7 | Doc_02 §1.1 | Footnote: "In the original manuscript this is in the writing of Epiphanius" | **Exact.** But it sits on **p.33**, the same page Doc_02 assigns the dedication to p.32; and the Russian witness asserts the opposite ("писано моею рукою грешною") — Finding 17. |
| 8 | Doc_02 §1.1 | "…When we die, then shall this be read…" | Text correct. Locus **wrong on both counts**: p.156, and p.155 is not the last page (Finding 8). |
| 9 | Step0 §1; Doc_01 §2.2 | Decision-Log: "yes to all, move forward." | **Exact.** |
| 10 | Step0 §1 | Decision-Log: "A1.E8 CLEARED FOR GATE" | **Exact** (heading text). |
| 11 | Step0 §1; Doc_01 §1 | Decision-Log: "the Synodal Russian church (Old Believers re-scoped as dissent)" | **Quote exact; inference unsupported** (Finding 18). |
| 12 | Step0 §1; Doc_01 §2.2 | Decision-Log: "round-1800 artifact cluster" / "replaced" / "honest 1815 caps" | **Exact** against "the round-1800 artifact cluster replaced with honest 1815 caps"; the Data-finds line confirms "six-entry," supporting "several Era 8 entries." |
| 13 | Step0 §1; Doc_01 §2.2 | Decision-Log: "A1.E8 (1650-1815)" | **Misattributed** — the string is in the 2026-08-02 Era 7 entry's "Next:" line, not in either 2026-08-03 Era 8 heading (Finding 19). En dash → hyphen. |
| 14 | Step0 §1, §2 | Census `floorNote` and `statusDescription` | **Exact** against `cic-website/data/world-census.json`. |
| 15 | Doc_01 §4 | Census: "the plain, angry, comic Russian of speech rather than of books" | **Quote exact; attribution wrong** — it is the census's own prose, not the translators' (Finding 28). |
| 16 | Doc_02 §5 | V1.8: "Files marked 'no coverage entry' are a library gap… list their count and leave them" | **Unverifiable** — V1.8 is not in the tree (Finding 20). |
| 17 | Doc_01, Doc_02, corpus-map, REGISTRY.yaml, Dossier | "INTAKE.md's 2026-09-25 ruling… primary evidence regardless of language…" | **Not in the cited file, and contradicted by it** (Finding 2). |
| 18 | Doc_02 §5 | `engine/m1/cross_world.py` "module docstring already names this exact relocation" | **Not in the docstring** (Finding 24). |
| 19 | Dossier header | "per `CLAUDE.md`'s 'Scaling the build' section, which already recorded that finding" | **Not in `CLAUDE.md`** (Finding 27). |

**Summary of the re-verification:** of nineteen checked citations, **eight are
exact and correctly located**; **five have correct text but a wrong or
misattributed locus**; **one is altered** (Meletina → Meletius); **four cite
material that is not in the file cited**; and **one is unverifiable** because
the cited document does not exist in the tree.

So the drafting thread's claim — Registry R1: "every quotation used in Doc_01
checked word-for-word against this file" — is **true about the words and false
about the places**. The wording was checked carefully and is, with one
exception, accurate. The page numbers were not independently derived, and the
method stated for deriving them is off by one. That distinction matters,
because loci are what downstream documents cite without re-opening the file.

**Registry code `obel`: no collision.** `records/worlds/` contains `alx`,
`cappadocian`, `desert`, `don`, `fix`, `gallic`, `hal`, `ijc`, `obel`, `pahc`,
`rzg`, `syr`, `witt`. Doc_01's header claim is accurate.

---

# 5. The V1.8 merge-state claim — independent confirmation

Open_Gaps entry 7 claims V1.8 is not on `main`/this branch and that its
content was read via `git show` against unmerged commits.

**Confirmed, on the core claim:**

```
$ ls reference/method/
CiC_Adversarial_Review_Standard_Practice.md
CiC_Record_Native_World_Build_Process_V1.5.md
CiC_Register_Bar_2026-08-29.md
CiC_Representative_Naming_Role_Discipline_2026-09-08.md
CiC_Voice_Style_Guide_and_Scaling_Plan.md
CiC_World_Build_Completion_Standard_V1.3.md
Pass2-decisions

$ ls reference/method/CiC_Record_Native_World_Build_Process_V1.8.md
ls: cannot access '...': No such file or directory

$ git log --all -- reference/method/CiC_Record_Native_World_Build_Process_V1.8.md
(no output)
```

V1.8 is **not** in the working tree. V1.5 **is**. No V1.8 commit is an
ancestor of this branch's HEAD. Entry 7 is right about that.

**Not confirmed, and overstated as written:** the four commits entry 7 names
do not exist in this checkout at all —

```
$ git cat-file -t 33c0c4f3   → fatal: Not a valid object name 33c0c4f3
$ git cat-file -t f85b8080   → fatal: Not a valid object name f85b8080
$ git cat-file -t e2ca4dc3   → fatal: Not a valid object name e2ca4dc3
$ git cat-file -t a6d4d639   → fatal: Not a valid object name a6d4d639

$ git rev-parse --is-shallow-repository   → true
$ git branch -a
* (HEAD detached at refs/heads/worktree-agent-add54097ad81169da)
  worktree-agent-add54097ad81169da
  remotes/origin/worktree-agent-add54097ad81169da
```

This is a shallow (`--depth 50`), single-branch clone. `git log --all` here
sees one branch, so entry 7's stated method would not reproduce its stated
result in a fresh checkout of this branch. I can confirm the absence; I cannot
confirm those commits exist, or that they sit in PRs #591/#594/#595. Entry 7
should be restated to distinguish what it observed in its own environment from
what the repository shows.

**And the part entry 7 gets wrong is the disposition, not the facts.** Doc_02
§16 calls this "a housekeeping gap, not a disputed process question — flagged,
not escalated." Three canonical documents now cite an unreadable specification
as their governing authority (Doc_01 §6; Doc_02 §3, §5, §9; Open_Gaps entry
1), which makes their compliance unauditable by anyone but their author. That
is a governance/methodology matter and an escalation category, and it should
have stopped the pass before drafting rather than been noted after. See
Finding 20.

---

# 6. Did the three-document combined pass cost anything?

**Yes — modestly, and in one specific direction.**

It cost nothing on the things a combined pass is actually better at, and it
gained something real there. Findings 6, 7, 14, 17, 18 and 19 are all
*cross-document* defects — Doc_01 and Doc_02 disagreeing about p.120 versus
p.120–121, the dedication's page being cited two ways in one table, the two
vendored witnesses contradicting each other about who held the pen, Step 0's
Decision-Log reading propagating into Doc_01. Three separate reviewers, each
holding one document, would have been *less* likely to catch those, not more.
The build-cycle skill's own "Cross-document fact consistency" section exists
because this project has been bitten twice by exactly that gap, and a combined
pass is the natural shape for closing it.

What it cost is **depth on Doc_02's own internal completeness**. Finding 25 is
the weakest section of this review: I checked Doc_02's eight claimed V1.8 §2
deliverables and formed a judgement on each, but a dedicated Doc_02 review
would have gone further into the corpus-map schema reasoning in §3, the
holdings tool's actual behaviour in §5 (I read the module and its comments but
did not run it), and the Forces-lens material in §12, which I have essentially
taken at face value. Those are the places where a genuinely skeptical reader
should assume this review is thinner than it should be.

It also cost the *independence* property the skill is really after, in a way
worth naming: one reviewer forming one view of a package is one view, however
adversarial. Three reviewers disagreeing with each other would have produced
information this pass cannot — and the skill has a specific provision for
logging exactly that disagreement, which a combined pass forecloses.

Given that Findings 1, 2, 20, 21 and 22 are blocking on their own, I do not
think a per-document split would have changed the verdict. It would have
changed the confidence attached to the non-blocking Doc_02 findings. If the
drafting thread's time budget allows exactly one more review after revision,
I would spend it on Doc_02 alone rather than on another combined pass.

---

# 7. Note on this review's own standing

This file is the Round-1 review artifact for Step 0, Doc_01 and
Doc_02/Registry. It is not a ruling. Per the build-cycle skill, none of these
documents may be dispositioned on the strength of its author's own reading,
and Step 0's existing "Approved to proceed" (Finding 21) should be withdrawn
rather than carried forward.

Findings 2 and 20 meet the governance/methodology escalation category and go
to Mark directly. Finding 1 additionally implicates the census's own
`floorNote`, which was cited approvingly at a Frozen portfolio gate —
correcting the census is portfolio-level and also goes to Mark; correcting
this world's own documents does not.

Reviewer did not modify any file other than creating this one.
