"""Generates NEEDS-RULING.md - every assignment the corpus run would not make
on its own authority, grouped so Mark can clear them in sweeps.

WHY GROUPED BY TARGET. 87 works carry `confidence: needs-ruling`, and read as a
flat list they look like 87 decisions. They are not. Ten workers, unable to see
each other, kept hitting the same small set of walls - most often *"this work is
real, and the census has no entry for its region and period."* One answer to
that clears five works, or seven. So the report leads with the count each
question clears, and the individual works sit under it as evidence.

The preface text for a recurring question is written here rather than derived,
because it comes from reading the workers' own reports. Everything else - which
works, which targets, the counts - is read from the map.

THAT SPLIT IS A HAZARD, and it has bitten twice. A preface claimed the Greek
apologists were among `pahc`'s flagged works; they were `provisional`. Another
claimed the church historians were among `imperial-juridical`'s; they are
`assigned`. Both came from a worker's report, both read plausibly, and both
were wrong about the pile they described - because prose written once does not
follow a generated list that keeps changing.

So every preface is now followed by the group's ACTUAL roster, generated: prose
and pile sit one line apart and disagreement is visible on sight. A sweep key
whose group has emptied is reported at the end of a run rather than silently
producing nothing.

    python world-build-docs/_cross-world/gen_needs_ruling.py
"""
import collections
import pathlib
import re
import textwrap

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
MAP = ROOT / "cic" / "corpus-map"

# The recurring questions, keyed by the entry the works were parked against.
# Each is a ruling that clears everything beneath it at once.
SWEEPS = {
    "post-apostolic-house-church":
        "**Answered.** `pahc` was the corpus's overflow shelf - the earliest entry there is, so "
        "everything early landed on it - and the pile has gone from 22 flagged works to 3. Three "
        "entries took it apart: `roman-church-third-century` (Hippolytus and Caius, who fell off "
        "the end of pahc's 200 CE window), `greek-apologists-second-century`, and "
        "`apocryphal-and-pseudepigraphal-literature`. What is left are three unrelated singles.",

    "imperial-juridical-christianity":
        "**Not the historians, and now down to one.** Eusebius, Socrates, Sozomen and Theodoret "
        "are all `assigned` here and always were; *Martyrs of Palestine* went to "
        "`palestinian-church-pre-constantinian`. What is left is the *Canonical Epistles of the Fathers*, where the question is granularity - a per-father "
        "split would send Basil and the Gregories to the Cappadocian entry and Athanasius and "
        "Peter to Alexandria, but would mint ten rows for seventeen thousand words of canons. "
        "(Lactantius' *Divine Institutes* is the third of this entry's questions and files under "
        "`latin-pastoral-congregational-christianity` below, where its other half sits: written "
        "during the Great Persecution by a Latin rhetor who became Constantine's court tutor, so "
        "neither side is a clean fit.)",

    "latin-pastoral-congregational-christianity":
        "**No entry for early Latin Christianity outside Carthage — and the last regional gap I "
        "declined to fill.** Every entry added in this series answered a *pile*: eight works for "
        "Gaul, seven for Anatolia, four across three entries for Palestine. This is two authors "
        "and two unrelated problems, which is below that bar, so it is left for a ruling rather "
        "than settled by a build thread. The entry runs from the 240s and is regionally North "
        "African, so four works are shelved here on language alone "
        "with the wrong region or the wrong century: Minucius Felix's *Octavius* (the earliest "
        "Latin apologetic dialogue), Commodian's verse (date disputed across three centuries), "
        "and both works of Victorinus of Pettau, the earliest Latin exegete, who was Pannonian. "
        "Worth knowing while you rule: the *Octavius*'s first half, Caecilius' speech, is one of "
        "the fullest surviving statements of the pagan case against Christianity anywhere.",
}


def load() -> dict:
    works: dict[tuple, dict] = {}
    for path in sorted(MAP.glob("*.yaml")):
        if path.name == "UNATTRIBUTED.yaml":
            continue
        for w in (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("works") or []:
            if w.get("confidence") != "needs-ruling":
                continue
            key = (w.get("author"), w.get("work"), w.get("source_file"))
            entry = works.setdefault(key, {"targets": [], "note": "", "role": w.get("role")})
            entry["targets"].append(path.stem)
            note = re.sub(r"\s+", " ", str(w.get("note") or "")).strip()
            if len(note) > len(entry["note"]):
                entry["note"] = note
    return works


def main() -> None:
    works = load()
    assignments = sum(len(v["targets"]) for v in works.values())

    # A work is filed under the target that most needs the ruling: the one with
    # the biggest pile, so a sweep answer clears as much as possible at once.
    weight = collections.Counter(t for v in works.values() for t in v["targets"])
    filed: dict[str, list] = collections.defaultdict(list)
    for key, v in works.items():
        home = max(v["targets"], key=lambda t: (weight[t], t))
        filed[home].append((key, v))

    out = [
        "# Needs-ruling — what the corpus assignment would not decide on its own\n",
        f"Generated by `gen_needs_ruling.py` from `cic/corpus-map/`. "
        f"**{len(works)} works, {assignments} assignments.**\n",
        "Every one of these was placed with a best guess and flagged, never forced and never "
        "dropped. The brief's instruction was that a flagged uncertainty is worth more than a "
        "confident wrong assignment, and ten workers took it seriously.\n",
        "**Read the group headings, not the list.** These are not 87 decisions. Ten workers who "
        "could not see each other kept hitting the same small set of walls, and the dominant one "
        "is not doubt about texts at all — it is *this work is real, and the census has no entry "
        "for its region and period.* One answer clears five or seven works at a time.\n",
        "Nothing here blocks anything. The map is valid and usable as it stands; a `needs-ruling` "
        "work is assigned, just not on the run's own authority.\n",
    ]

    out.append("\n## Answered since the run\n")
    out.append(
        "**Eleven entries added, 2026-08-26.** Fleet-wide flagged works have fallen from **87 to "
        "59** — a 32% reduction, and none of it by deciding anything a worker had refused to "
        "decide. Every entry answers the same complaint, raised independently by workers who "
        "could not see each other: *this material is real and the census has nowhere accurate to "
        "put it.*\n\n"
        "Seven are formation-world candidates, on record as *Possible Future World*:\n\n"
        "- **`gallic-monastic-ascetic-christianity`** (era 2, c. 360–450, *Possible Future World "
        "on record*). Closed the pre-Merovingian Gaul hole that two workers hit independently. "
        "**Seven works re-pointed**, six of them to `assigned`; the *Doubtful Letters of "
        "Sulpitius Severus* stay flagged because the editors' own attribution doubt is untouched "
        "by a new entry.\n"
        "- **`roman-church-third-century`** (era 1, c. 200–260). The decades `post-apostolic-"
        "house-church` (ends 200) and `novatianism` (begins 251) bracket without covering. Took "
        "the six Hippolytus works and Caius.\n"
        "- **`palestinian-ascetic-monasticism-early`** (era 2, c. 330–450). The same shape as "
        "Gaul: `chalcedonian-monasticism-judean-desert-and-gaza` does not begin until c. 450. "
        "Took Jerome's *Hilarion* and *Malchus*.\n"
        "- **`palestinian-church-pre-constantinian`** (era 1, c. 185–312). Caesarea and its "
        "library — where Origen went after Alexandria, where Pamphilus spent his life and money, "
        "and where Eusebius learned to work. **Works flagged in three separate piles turned out "
        "to be this one hole**: Alexander of Jerusalem and Julius Africanus under Alexandria, "
        "Maximus of Jerusalem under `pahc`, and Eusebius' *Martyrs of Palestine* under "
        "`imperial-juridical`, each noting that nothing covers pre-Constantinian Palestine. The "
        "Jerusalem entry does not begin until 325.\n"
        "- **`anatolian-church-third-century`** (era 1, c. 240–312). Gregory Thaumaturgus in "
        "Pontus and Methodius in Lycia. **The gap was regional, not per-author**, which is why it "
        "is one entry and not two: `post-apostolic-house-church` ends at 200, and between that "
        "line and Nicaea the only entries touching Asia Minor are Montanism and Modalist "
        "Monarchianism — both dissenting currents. The catholic church the Cappadocians came from "
        "was simply absent.\n"
        "- **`gallic-nicene-episcopate`** (era 2, c. 350–400). Hilary of Poitiers, whose three "
        "works stayed flagged through two rounds of entry-adding because the Gallic *monastic* "
        "entry had deliberately excluded him — its own case argued he is a controversialist whose "
        "Gallic location is incidental. That cut stands, so he got his own entry. Whether the two "
        "Gallic entries should be one is named there as the open question.\n"
        "- **`greek-apologists-second-century`** (era 1, c. 124–200). Fifteen works, and the "
        "argument that carried it is the one that carried Gaul: **Athens is not among `pahc`'s "
        "named regions**, and Quadratus, Aristides and Athenagoras all wrote from there. The "
        "entry's own record states the objection against it — that apologetic is a genre rather "
        "than a community — rather than hiding it.\n\n"
        "One is explicitly a shelf, and says so on its face:\n\n"
        "- **`apocryphal-and-pseudepigraphal-literature`** (era 1, c. 100–500). Fifteen works "
        "whose notes read, almost verbatim, *the census has no bucket for the class* — apocryphal "
        "Acts, the Protevangelium, the Gospel and Apocalypse of Peter, the Ignatian forgeries, "
        "and the Jewish pseudepigrapha that survive only because Christian scribes kept copying "
        "them. They had been filed by the century they DEPICT rather than the century they were "
        "written in. Its `why` field says a survey may reasonably rule it not a tradition at "
        "all.\n\n"
        "Five are shelves for material the corpus carries *about* a movement, registered as "
        "**Floor Question** rather than as exclusions — the creedal ground is not in doubt, but "
        "no Phase One record rules on any of them by name, and these entries do not invent one:\n\n"
        "- **`anomoean-eunomian-christianity`** — the gap **three** workers hit. Anti-Eunomian "
        "works were parked against `homoian-arian-christianity`, a different wing that split from "
        "it at Constantinople in 360.\n"
        "- **`pneumatomachian-current`** — Basil's and Nyssa's and Ambrose's *On the Holy Spirit* "
        "had no entry naming the party they answer. The only near-match by name, "
        "`byzantine-imperial-church-macedonian`, is a ninth-century imperial dynasty.\n"
        "- **`apollinarian-christianity`** — Gregory of Nazianzus' Cledonius letters, and not an "
        "Arian position at all.\n"
        "- **`modalist-monarchianism`** — Tertullian's *Against Praxeas* and Hippolytus' *Against "
        "Noetus*, two substantial heresiological works with nowhere to point.\n"
        "- **`bardaisanite-current`** — where the entry states the creedal question rather than "
        "settling it, because the evidence genuinely does not.\n\n"
        "**Two rulings by principle rather than one work at a time**, which is what took the "
        "remainder from 39 to 13. *The date-guess apocrypha*: thirteen works — the Byzantine "
        "apocalypses, the late apostolic martyrdom romances, the Latin Marian infancy gospels — "
        "had each been filed into whichever era bucket happened to be nearest, on dates their own "
        "notes call guesses spanning centuries. They went to "
        "`apocryphal-and-pseudepigraphal-literature`, whose window widened to c. 900 to cover its "
        "own material; an era guess is not a placement, the class is. Two kept a second id as "
        "`transmission` where the note stated real custody rather than a date. *The spurious "
        "corpora*: ten rows across six entries asking one question — does a spurious corpus file "
        "under the attributed name? It does, **and it also files as what it is**. The "
        "transmitted-author shelf stands (brief §6.2: derive from the markup, do not "
        "re-attribute), and the apocrypha entry is added, because a work circulating under a name "
        "that is not its author's is a pseudepigraphon by definition.\n\n"
        "**And a fourth relation, ruled the same day.** Three works in the Syriac pile said the "
        "same thing in different words — `syr` was marking *where a text was preserved*, not "
        "whose voice it is. `transmission` says custody: the Ambrose hypomnemata is a Greek "
        "apology that exists because Syriac scribes copied it, and the Testaments of the Twelve "
        "Patriarchs, the Life of Adam and Eve and the Narrative of Zosimus are Jewish works that "
        "survive only because Christian scribes went on copying them after Judaism let them go. "
        "**Seven rows**, and the boundary is what keeps it that small: an opponent quoted "
        "*inside* a work is not transmission (Celsus inside Origen — the book is Origen's), and "
        "neither is a lost work surviving as fragments in a later author. A re-scan after the "
        "rule was written returned nine candidates and every one was correctly excluded. A test "
        "pins the invariant that makes it mean anything: **every transmitted work has its voice "
        "assigned somewhere else** — custody of nothing is a mislabelled `tradition`.\n\n"
        "**And one ruling that added no entry at all.** The Donatists claimed Cyprian as their "
        "charter authority, and four of his works were flagged against `donatism` because "
        "neither existing role fitted: he is not a Donatist (`tradition` is false) and he died "
        "fifty years before the schism, so he is not describing it from outside (`context` is "
        "false). The answer was a third relation, **`antecedent`** — the authority an entry "
        "argued *from* — with a rule that stops it swallowing the map: **an antecedent "
        "assignment requires that the entry's own vendored sources argue from the text.** "
        "Measured, not asserted: Augustine's *On Baptism, Against the Donatists* names Cyprian "
        "306 times in 92,000 words. Cyprian is `antecedent` to `donatism` and `context` for "
        "`novatianism`, whose schism he lived through and argued against — one author, two "
        "relations, which is what the field is for. Four rows, and a test pins it narrow.\n\n"
        "**One invariant now holds across all nine floor entries and is worth knowing.** Of the "
        "70 works assigned to them, exactly **two** are a floor movement's own surviving voice — "
        "the *Excerpts of Theodotus* and Bardaisan's *Book of the Laws of Divers Countries*. "
        "Every other one is a refutation. The map says structurally what the corpus is: these "
        "movements reach us almost entirely through the people who argued with them.\n")
    out.append("\n## The sweeps — in order of how much each clears\n")
    out.append("| ruling | clears | the question |")
    out.append("|---|---:|---|")
    for target in sorted(filed, key=lambda t: -len(filed[t])):
        if target in SWEEPS:
            head = SWEEPS[target].split(".**")[0].replace("**", "").strip()
            out.append(f"| `{target}` | {len(filed[target])} | {textwrap.shorten(head, 96)} |")

    for target in sorted(filed, key=lambda t: (-len(filed[t]), t)):
        group = sorted(filed[target], key=lambda x: (str(x[0][2]), str(x[0][1])))
        out.append(f"\n## `{target}` — {len(group)} work(s)\n")
        if target in SWEEPS:
            out.append(SWEEPS[target] + "\n")
            # The roster, generated. See the note on drift above main().
            roster = ", ".join(sorted({str(k[0]) for k, _ in group}))
            out.append(f"*In this pile: {roster}.*\n")
        for (author, work, source), v in group:
            also = [t for t in sorted(set(v["targets"])) if t != target]
            out.append(f"**{work}** · `{author}` · `{str(source).split('_')[0]}`"
                       + (f" · also flagged against {', '.join(f'`{a}`' for a in also)}" if also else ""))
            out.append(f"> {v['note']}\n")

    out.append("\n---\n")
    out.append(
        "## Three questions that are not per-work\n\n"
        "These came out of the ten workers' reports rather than out of any single assignment, "
        "so they have no row above. Two are yours; one is a defect.\n\n"
        "**1. A duplicate census entry — this one is a defect, not a judgment.** The census "
        "carries `cyrilline-miaphysite-egyptian-tradition` (era 2, *Deferred by Step 0*) and "
        "`cyrilline-miaphysite-egyptian-christianity` (era 3, *Pre-Survey Candidate*). A worker "
        "used the Step-0 on-record one and flagged it; both now hold assignments. Duplicate "
        "census ids are the shape `engine/m1/cross_world.py` already polices, so this can become "
        "a standing check once you say which is real.\n\n"
        "**2. Outside voices embedded inside works assigned `tradition`.** Four workers hit this "
        "independently, and it is a real limit on what per-work assignment can express:\n\n"
        "- Celsus' *True Word* survives **only** inside Origen's refutation of it — the fullest "
        "pagan critique of Christianity in the corpus is, physically, a Christian book.\n"
        "- Basil's Letters carry eleven Libanius exchanges and letters of Julian.\n"
        "- Jerome's Letters carry Damasus, Augustine, Theophilus, Innocent.\n"
        "- Symmachus' pagan *Relatio* is printed inside Ambrose's letters — this one **was** "
        "split out and assigned `context` to `ijc`, which is the model for the rest if you want "
        "it applied.\n\n"
        "The question is whether embedded outside material earns its own assignment, or whether "
        "a note on the containing work is enough. Splitting is possible but only where the "
        "material sits in its own section; Celsus does not.\n\n"
        "**3. Movements the corpus documents that the census has no entry for at all.** Distinct "
        "from the sweeps above, which are works needing a shelf — these are *opponents* named "
        "throughout the corpus with nowhere to be described from: the Anomoeans/Eunomians (three "
        "workers), the Pneumatomachians/Macedonians, the Apollinarians, modalist Monarchianism "
        "(Noetus, Sabellius), Hermogenes, Bardaisan, and iconoclasm — where Nicaea II preserves, "
        "refracted through refutation, the 754 council's epitome, the iconoclasts' only words "
        "anywhere in the vendored corpus.\n\n"
        "---\n")
    out.append(
        "## How to answer one\n\n"
        "A ruling is a sentence, not a document. Either name the entry the work should go to, "
        "or say the census needs a new entry and roughly what it covers. The staging file for "
        "that source volume gets edited and `python cic/engine/corpus_map_merge.py` re-run; the "
        "work's `confidence` moves to `assigned` and it drops off this list.\n\n"
        "Where the answer is a **new census entry**, that is a change to "
        "`cic-website/data/world-census.json` and belongs to whoever owns the Atlas, not to a "
        "corpus thread. This report is the evidence that the entry is wanted: it names the "
        "material already in hand that would fill it.\n")

    orphans = sorted(set(SWEEPS) - set(filed))
    if orphans:
        print("NOTE: sweep prose with no remaining group (answered, or the key is stale):")
        for o in orphans:
            print(f"  {o}")

    target_file = pathlib.Path(__file__).resolve().parent / "NEEDS-RULING.md"
    target_file.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {target_file.relative_to(ROOT)} — {len(works)} works, {assignments} assignments, "
          f"{len(filed)} groups, {sum(len(filed[t]) for t in filed if t in SWEEPS)} covered by a sweep")


if __name__ == "__main__":
    main()
