"""Sentence-level fact check for the fabrication class R27
(`engine.m4.uncited_claims.find_uncited_claims`) and named_claim_grounding
(OG-16) each miss by construction - see Decision-Log.md Entries 76/77
(Conversation & Transparency Engine) for the live measurement this module
answers.

THE GAP THIS CLOSES. Two existing checks each cover part of the ground,
and the part neither covers is exactly where every fabrication found so
far has lived:

  - `find_uncited_claims` flags a sentence with no citation tag at all -
    but it is report-only and untouched by enforcement for a sentence
    that sits inside an otherwise well-cited paragraph (R27's own
    enforcement only regenerates on a WHOLE paragraph carrying no tag, or
    a `neighbour_named` offense - Entry 77's own rzg fixture: "Felix Manz
    was drowned in the Limmat River in January 1527" rides, untouched,
    inside a paragraph with four other genuinely tagged sentences).
  - `named_claim_grounding.find_named_claim_flags` only examines a
    sentence that ALREADY carries a tag and ALREADY passed
    `grounding_net`'s own ratio test - a sentence with no tag, or one
    whose tag's own verdict wasn't "ok", is out of its scope entirely by
    construction (its own module docstring; confirmed live, Entry 77's
    control-run finding: the Athanasius fabrication came from
    `find_uncited_claims`'s own untagged list, never from a tagged
    sentence `named_claim_grounding` could have looked at).

Every fabrication found in three separate live runs (Entry 61/#558/the
control run/Entry 77) was an UNTAGGED sentence naming a specific person,
place, date, or number with no support anywhere in the speaking world's
own compiled ground - not a near-miss of either check above, a
structurally different, wider-scoped question: "is this specific claim
supported ANYWHERE in what this world actually holds," asked of every
sentence a participant will read, independent of whether that sentence
carries a tag, and independent of which tag (if any) it carries.

REUSE, NOT DUPLICATION. This module is thin on purpose - every real piece
of machinery already exists and is reused unchanged:
  - `engine.prose.claim_markers` decides whether a sentence makes any
    checkable claim at all (a proper noun, or a number) - the same
    positive-detection gate `named_claim_grounding` and
    `find_uncited_claims` already both rest on.
  - `engine.m4.named_claim_grounding.record_ground`/`_source_ground` -
    OG-9's own per-record ground computation (a record's own text, plus
    its `sources[]`' resolved `work` field, truncated through
    `short_head` for the same reason that module's docstring gives) -
    reused via the new `repository_ground`, which sums it over EVERY
    record in the world's compiled repository rather than only a
    sentence's own tag(s). This is the one change in scope this module
    needed from the existing mechanism: ground the claim against
    everything the world holds, not only what the sentence happened to
    cite.
  - `engine.m4.named_claim_grounding.missing_markers` - the exact
    marker-vs-ground comparison `ungrounded_markers` already runs,
    factored out so both the tag-scoped check and this whole-repository
    one share one implementation of "is this name/number in the ground,"
    never two that could drift apart.
  - `engine.m4.uncited_claims._is_question`/`_is_honest_limit`/
    `_is_first_person_no_claim` - the same three allowed-uncited
    exemptions `find_uncited_claims` already uses, reused unchanged
    rather than re-decided here. This matters specifically for the
    honest-limit case: "Our record doesn't mention that Christian
    tradition... So if Alexandria held a bishop in our own years... we
    would have cared about that" NAMES Alexandria while denying
    knowledge of it, not asserting anything about it - exactly the shape
    R27's own `neighbour_named` class over-fired on live (Entry 77's
    `don` false trigger). A sentence exempted here makes no claim this
    module has any business grounding.

WHY EVERY SENTENCE, NOT ONLY UNTAGGED OR ONLY VERDICT-FAILING ONES.
`engine.m4.turn.apply_net`'s own docstring, and Program-Spec M4/
Artifact-5 SS2/SS5: "the checks gate decoration, never the text" - every
sentence a voice generates reaches the participant with only its own
citation tag stripped, regardless of that tag's own verdict. A
fabrication does not need to be untagged to reach a participant, so this
check runs over every sentence in `net_result["sentences"]`
unconditionally (after the three content exemptions above) - a tagged
sentence whose tag passed the ratio test can still name something absent
from the WHOLE repository, not just from its own tag's ground (that
narrower question is exactly what `named_claim_grounding` already
answers; this module answers the wider one on top of it, not instead of
it).

WHAT THIS CANNOT CATCH, NAMED PLAINLY RATHER THAN GLOSSED OVER: an
unsupported CHARACTERIZATION attached to an already-real, already-named
figure - Entry 76's own "[Eustathius] was a coward" fixture. Eustathius
of Sebaste is a real, grounded name in cappadocian's own repository;
"coward" is an ordinary lowercase adjective, not a proper noun or a
number, so `claim_markers` finds no checkable marker in that sentence at
all and this module has nothing to compare against ground. Catching an
invented QUALITY attached to a real name is a different, harder, fuzzier
problem than catching an invented NAME, DATE, or NUMBER - it would need
a genuinely different mechanism (comparing an attributed characterization
against what the cited/whole-repository text actually says about that
figure, not a marker-presence check), and is out of this module's own
scope by design, not by oversight. Measured recall against the known
fabrication set reflects this honestly (Decision-Log entry).

Report-only, additive, no participant-visible change: `find_unsupported_
named_claims` is meant to be called the same unconditional way
`find_uncited_claims`/`find_named_claim_flags` already are
(`engine.m4.turn._run_ordinary_voice_turn`), adding its own additive
`voice_event["fact_check_flags"]` key. No enforcement flag exists yet -
what a caught sentence's own regeneration/correction should say, and
under what flag it activates, is deliberately left to a later,
separately-ruled PR (Decision-Log entry's own recommendation: drop or
regenerate only the offending SENTENCE if this is ever enabled, never
blank the whole turn the way `r27_enforce`'s paragraph-level enforcement
does today - Entry 77 measured that shape wiping 5 of 22 turns entirely,
every one a false trigger on inspection; a sentence-scoped fix, if built,
should not repeat that failure mode).

A FOURTH EXEMPTION, found empirically rather than guessed in advance: a
counterfactual/hypothetical clause ("if [X] held..., we would have cared
about that") names a neighbour while explicitly NOT asserting anything
about them - the grammatical mirror of the honest-limit case above, and
missed by `_is_honest_limit`'s own fixed phrases/negation regex (that
check looks for an explicit absence claim - "not in our record,"
"nothing survives" - not a subjunctive mood). Traced directly to a real
false trigger Entry 77 measured live: `don`'s own "So if Alexandria held
a bishop in our own years, and that bishop's line ran clean or broken,
we would have cared about that. But no record of ours says we ever asked
the question" names Alexandria (which never otherwise appears anywhere
in `don`'s own compiled repository) inside a pure hypothetical, and
without this exemption this module would have reproduced the exact
`neighbour_named` false-positive shape it exists to improve on, on the
very same sentence. `_is_hypothetical_conditional` is narrow (an "if"
clause co-occurring with "would"/"would have" in the same sentence, not
a topic-specific phrase list) precisely so it generalizes to any
neighbour named this same honest, subjunctive way, not only this one
traced case."""
import re

from engine.m4.named_claim_grounding import missing_markers, repository_ground
from engine.m4.uncited_claims import _is_first_person_no_claim, _is_honest_limit, _is_question

_HYPOTHETICAL_CONDITIONAL = re.compile(r"\bif\b.*\bwould\b", re.IGNORECASE | re.DOTALL)


def _is_hypothetical_conditional(sentence: str) -> bool:
    return bool(_HYPOTHETICAL_CONDITIONAL.search(sentence))


def find_unsupported_named_claims(sentences: list[dict], *, repository_records: dict[str, dict]) -> list[dict]:
    """Report-only entry point, same calling shape as `find_uncited_claims`/
    `find_named_claim_flags`: takes `net_result["sentences"]` (no second
    sentence split), returns `[]` on a clean turn. Unlike both of those,
    examines every sentence regardless of its own tag/verdict (see module
    docstring) - the four content exemptions below are the only sentences
    skipped. Each flag: `{"sentence", "tags", "class":
    "unsupported_named_claim", "missing"}` - "missing" names the exact
    word(s)/number(s) not found anywhere in the world's whole compiled
    ground, the same shape `find_named_claim_flags` already uses for the
    identical reason (a flag naming no specifics is not auditable)."""
    ground_words, ground_digits = repository_ground(repository_records)
    flags = []
    for sent in sentences:
        text = sent["sentence"]
        if (
            _is_question(text) or _is_honest_limit(text.lower())
            or _is_first_person_no_claim(text) or _is_hypothetical_conditional(text)
        ):
            continue
        missing = missing_markers(text, ground_words, ground_digits, include_sentence_initial_proper_nouns=True)
        if missing:
            flags.append({
                "sentence": text, "tags": sent.get("tags") or [],
                "class": "unsupported_named_claim", "missing": missing,
            })
    return flags
