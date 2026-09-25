"""Sentence-level fact check: for every sentence a voice turn produces,
does each proper noun and number it names appear somewhere in the
speaking world's own compiled repository (every record, not only the
sentence's own citation tag)?

A sentence can name something absent from the world's own ground while
sitting inside an otherwise well-cited paragraph, and while carrying a
tag whose own ratio-based grounding check passed - `find_uncited_claims`
only examines untagged (or withheld) sentences, and `named_claim_grounding`
only examines a sentence that already carries a tag with an "ok" verdict.
Neither check reaches a sentence whose specific named/numbered claim has
no support anywhere in the world's own repository if that sentence
happens to be otherwise well-formed. This module closes that gap: it
runs over every sentence unconditionally, grounded against the whole
repository rather than a sentence's own tag(s).

GROUND: `engine.m4.named_claim_grounding.repository_ground` - every
record's own text, plus each record's own `sources[]` resolved through
`work`/`short_head`, unioned across the entire repository. Same
marker-vs-ground comparison as `named_claim_grounding.ungrounded_markers`
(`missing_markers`, shared between both).

MARKERS: `engine.prose.claim_markers`'s own proper-noun/number detection,
with sentence-initial proper nouns included (`include_sentence_initial_
proper_nouns=True`) - unlike `claim_markers`'s own default, which excludes
a sentence's first word. That default is right for grounding a marker
against a single tagged record (a narrow ground, where an ordinary
capitalized sentence-opener risks a false flag); against a whole
compiled repository, an ordinary word that opens a sentence without being
a real name either falls into the stopword/doctrinal-vocabulary
exclusions below, or - being ordinary vocabulary - is overwhelmingly
likely to also occur elsewhere in the same repository, so it grounds
itself rather than false-flagging.

EXEMPTIONS: a sentence makes no claim this module checks when it is a
question, an honest-limit statement, or first-person framing with no
checkable content (`engine.m4.uncited_claims`'s own three exemptions,
reused unchanged). A fourth, local exemption covers a counterfactual
clause: "if X held..., we would have cared" names X without asserting
anything about it. Only the conditional clause's own span (from "if" to
the following "would"/"would have") is stripped before checking - a
name or number elsewhere in the same sentence, outside that span, is
still checked normally.

KNOWN LIMITS:
  - A claim built from words that are each individually grounded, but
    combined into a specific relationship no single record states, is
    not caught - this checks whether a name/number appears anywhere in
    the ground, not whether the sentence's own composed claim is true.
  - An unsupported CHARACTERIZATION of an already-grounded, real name
    (an invented quality or opinion attributed to a real figure) carries
    no proper-noun or number marker of its own, so there is nothing here
    to compare against ground - a different, harder problem than an
    absent name or number.
  - A different derivational form of a grounded name (an adjective where
    the ground has the noun, or similar) is not recognized as the same
    word - `missing_markers`' own documented limit, shared unchanged.
  - The same fact stated in a different surface form than the ground
    uses (a digit where the ground spells the number out, or vice
    versa) is not recognized as the same value.
  - A flag here means a specific name or number is not found anywhere in
    the world's own compiled ground - not that the named thing is
    fictional, and not that the sentence is false. Real people, places,
    and events are flagged exactly the same way an invented one would
    be, whenever this particular world's own repository happens not to
    hold them.

Report-only and additive: `find_unsupported_named_claims` is called the
same unconditional way `find_uncited_claims`/`find_named_claim_flags`
already are, adding `voice_event["fact_check_flags"]`. No enforcement
exists yet."""
import re

from engine.m4.named_claim_grounding import missing_markers, repository_ground
from engine.m4.uncited_claims import _is_first_person_no_claim, _is_honest_limit, _is_question

# Non-greedy so a later, unrelated "would" elsewhere in the sentence does
# not pull everything between "if" and it into the stripped span.
_HYPOTHETICAL_CLAUSE = re.compile(r"\bif\b.*?\bwould(?:\s+have)?\b", re.IGNORECASE | re.DOTALL)


def _strip_hypothetical_clauses(sentence: str) -> str:
    return _HYPOTHETICAL_CLAUSE.sub(" ", sentence)


def find_unsupported_named_claims(sentences: list[dict], *, repository_records: dict[str, dict]) -> list[dict]:
    """Every sentence's own proper nouns and numbers, checked against
    `repository_ground`. Takes `net_result["sentences"]` (no second
    sentence split), returns `[]` on a clean turn. Examines every
    sentence regardless of its own tag or verdict - see module docstring.
    Each flag: `{"sentence", "tags", "class": "unsupported_named_claim",
    "missing"}` - "missing" names the specific word(s)/number(s) not
    found anywhere in the world's own ground."""
    ground_words, ground_digits = repository_ground(repository_records)
    flags = []
    for sent in sentences:
        text = sent["sentence"]
        if _is_question(text) or _is_honest_limit(text.lower()) or _is_first_person_no_claim(text):
            continue
        checkable = _strip_hypothetical_clauses(text)
        missing = missing_markers(checkable, ground_words, ground_digits, include_sentence_initial_proper_nouns=True)
        if missing:
            flags.append({
                "sentence": text, "tags": sent.get("tags") or [],
                "class": "unsupported_named_claim", "missing": missing,
            })
    return flags
