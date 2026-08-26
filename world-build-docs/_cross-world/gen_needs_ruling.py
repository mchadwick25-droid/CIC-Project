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
works, which targets, the counts - is read from the map, so this cannot drift
from what was actually assigned.

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
        "**`pahc` is the corpus's overflow shelf, and that is the finding.** Its window is "
        "70-200 CE, and it collected 22 needs-ruling works because it is the only early entry "
        "there is. Three distinct questions sit inside this one pile: (a) *the Greek apologists* "
        "have no entry of their own - Athenagoras, Mathetes, the dubious Justiniana; (b) *early "
        "third-century Rome* has no entry, so Hippolytus (c. 170-236) and Caius fall off the end "
        "of pahc's window; (c) *later pseudepigrapha* impersonating first-century figures - the "
        "Spurious Epistles of Ignatius are 4th-century forgeries sitting in a 70-200 entry. "
        "Splitting even one of these off pahc would clear most of the pile.",
    "alexandria-catechetical":
        "Mostly Origen's reception and the third-century Alexandrian controversy - works whose "
        "Alexandrian connection is real but whose own home entry does not exist (Dionysius of "
        "Rome, Julius Africanus' correspondence, Methodius arguing against Origen).",
    "imperial-juridical-christianity":
        "**No entry exists for the church historians as such**, so Eusebius, Socrates, Sozomen "
        "and Theodoret were parked here on the reading that they document the imperial "
        "settlement. Also here: whether official conciliar acta and imperial rescripts count as "
        "`ijc`'s *own voice* or as `context` - a question about what that world is.",
    "cappadocian-nicene-pastoral-monastic-tradition":
        "**No entries for third-century Pontus, Palestine or Antioch.** Gregory Thaumaturgus is "
        "shelved with the Cappadocian entry he is forerunner to; the Trullan appendix's "
        "Canonical Epistles of the Fathers would split per-father into this entry and the "
        "Alexandrian one if you want them split at all.",
    "merovingian-gallic-christianity":
        "**No entry for pre-Merovingian Gaul.** `merovingian-gallic-christianity` starts c. 480, "
        "and Martin of Tours, Sulpitius Severus, Vincent of Lerins and Cassian's Marseilles all "
        "sit c. 360-450. Two independent workers hit this hole - it is also where Hilary of "
        "Poitiers falls. One entry, or one ruling that this material files forward, clears all "
        "of it.",
    "donatism":
        "**The Cyprian antecedent question**, raised once per work the Donatists actually "
        "invoked. Cyprian died in 258 and the Donatists claimed him; whether his Epistles, "
        "*De Unitate*, *De Lapsis* and the 256 rebaptism council belong to `donatism` as "
        "antecedents, or only to his own entry, is a judgment about what an entry's corpus is "
        "for. The workers refused to decide it and flagged it four times.",
    "homoian-arian-christianity":
        "**No entry for the Anomoeans / Eunomians**, hit by three separate workers. "
        "`homoian-arian-christianity` is named for a different Arian party, so anti-Eunomian "
        "works (Nyssa's *Against Eunomius*, Nazianzen's Theological Orations, Chrysostom on the "
        "Paralytic) are parked against the nearest Arian bucket rather than a right one.",
    "syriac-edessa-nisibis":
        "**The Clementine literature, and what `syr` is for.** Recognitions and Homilies sit "
        "between `ebionite-nazoraean-current` (the Jewish-Christian source theory) and this "
        "entry (Syrian provenance) - one ruling covers the whole Pseudo-Clementine corpus, the "
        "Two Epistles on Virginity with it. The deeper question underneath all four works here "
        "is whether `syr` means *Edessene* or means *transmitted in Syriac*: the Ambrose "
        "hypomnemata is Greek apologetic that survives only in Syriac, which is a fact about "
        "transmission, not about the tradition.",
    "latin-pastoral-congregational-christianity":
        "**No entry for early Latin Christianity outside Carthage.** This entry runs from the "
        "240s and is regionally North African, so four works are shelved here on language alone "
        "with the wrong region or the wrong century: Minucius Felix's *Octavius* (the earliest "
        "Latin apologetic dialogue), Commodian's verse (date disputed across three centuries), "
        "and both works of Victorinus of Pettau, the earliest Latin exegete, who was Pannonian. "
        "Worth knowing while you rule: the *Octavius*'s first half, Caecilius' speech, is one of "
        "the fullest surviving statements of the pagan case against Christianity anywhere.",
    "byzantine-imperial-church-macedonian":
        "Ante-Nicene volumes housing much later works: Byzantine-era apocalypses (the Virgin, "
        "Sedrach, Esdras, apocryphal John) printed in ANF and placed here by date-guess alone.",
    "jerusalem-liturgical-pilgrimage-christianity":
        "**No entry for Palestinian or Syrian monasticism before c. 450**, so Jerome's "
        "*Hilarion* and *Malchus* have nowhere that fits; `desert-monasticism` is regionally "
        "Egypt. A second worker hit the same hole from Chrysostom's ascetic treatises.",
    "valentinian-and-other-gnostic-christianities":
        "**Bardaisan has no census entry.** Two of Ephraim's Prose Refutations are purely "
        "anti-Bardaisan and are parked here as a best guess - the Chronicle of Edessa's own "
        "notes call him a promulgator of Valentinus' doctrine, but the classification is "
        "contested. Own entry, file under other-Gnostic, or Syriac-only?",
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

    target_file = pathlib.Path(__file__).resolve().parent / "NEEDS-RULING.md"
    target_file.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {target_file.relative_to(ROOT)} — {len(works)} works, {assignments} assignments, "
          f"{len(filed)} groups, {sum(len(filed[t]) for t in filed if t in SWEEPS)} covered by a sweep")


if __name__ == "__main__":
    main()
