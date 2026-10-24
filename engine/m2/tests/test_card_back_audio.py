import hashlib
import json
from pathlib import Path

SITE = Path(__file__).resolve().parents[3] / "cic-website"
AUDIO = SITE / "audio" / "cards"


def _summaries():
    census = json.loads((SITE / "data" / "world-census.json").read_text())
    return {
        m["id"]: " ".join(m["entry"]["summary"].split())
        for m in census["movements"]
        if m["status"] == "Built & Live" and (m.get("entry") or {}).get("representativeName") and m["entry"].get("summary")
    }


def test_every_card_back_has_audio_made_from_its_current_summary():
    manifest = json.loads((AUDIO / "manifest.json").read_text())
    summaries = _summaries()
    assert set(manifest) == set(summaries)
    for key, text in summaries.items():
        assert manifest[key]["hash"] == hashlib.sha256(text.encode()).hexdigest()[:16], key
        assert manifest[key]["chars"] == len(text), key
        assert (AUDIO / f"{key}.mp3").stat().st_size > 10_000, key


def test_every_card_back_clip_was_made_with_one_voice_and_one_set_of_settings():
    manifest = json.loads((AUDIO / "manifest.json").read_text())
    made_with = {json.dumps({k: v for k, v in e.items() if k not in ("hash", "chars")}, sort_keys=True) for e in manifest.values()}
    assert len(made_with) == 1
