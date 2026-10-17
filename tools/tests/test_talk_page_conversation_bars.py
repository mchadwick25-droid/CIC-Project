"""cic-website/talk.html hides its own bars once the framed conversation starts, and fits the keyboard."""
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

TALK = Path(__file__).resolve().parents[2] / "cic-website" / "talk.html"

RUNNER = r"""
const [script, events, viewport] = JSON.parse(process.argv[1]);
const frame = { src: null, contentWindow: { name: 'frame' } };
const stranger = { name: 'other' };
const listeners = [];
const classes = new Set();
const body = { style: {}, classList: { toggle: (c, on) => (on ? classes.add(c) : classes.delete(c)) } };
const view = viewport ? { height: viewport[0], offsetTop: viewport[1], addEventListener: () => {} } : undefined;
global.window = {
  location: { search: '', hash: '', pathname: '/talk.html', hostname: 'churchinconversation.com', href: '' },
  history: { state: null, replaceState: () => {} },
  addEventListener: (type, fn) => { if (type === 'message') listeners.push(fn); },
  visualViewport: view,
};
global.document = {
  body,
  getElementById: (id) => (id === 'talk-frame' ? frame : { setAttribute: () => {}, getAttribute: () => '/' }),
};
new Function(script)();
for (const [fromFrame, data] of events) {
  listeners.forEach((fn) => fn({ source: fromFrame ? frame.contentWindow : stranger, data }));
}
process.stdout.write(JSON.stringify({ classes: [...classes], height: body.style.height || null, transform: body.style.transform || '' }));
"""


def _page_script() -> str:
    scripts = re.findall(r"<script>(.*?)</script>", TALK.read_text(encoding="utf-8"), re.S)
    return next(s for s in scripts if "talk-frame" in s)


def _run(events, viewport=None) -> dict:
    out = subprocess.run(
        ["node", "-e", RUNNER, json.dumps([_page_script(), events, viewport])],
        capture_output=True, text=True, check=True, timeout=30,
    )
    return json.loads(out.stdout)


pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")


def test_the_bars_hide_when_the_conversation_starts_and_return_when_it_does_not():
    assert _run([[True, {"type": "cic:started", "started": True}]])["classes"] == ["in-conversation"]
    events = [[True, {"type": "cic:started", "started": True}], [True, {"type": "cic:started", "started": False}]]
    assert _run(events)["classes"] == []


def test_only_the_framed_app_can_hide_the_bars():
    assert _run([[False, {"type": "cic:started", "started": True}]])["classes"] == []


def test_the_hidden_bars_rule_covers_both_bars():
    page = TALK.read_text(encoding="utf-8")
    assert "body.in-conversation .bar,body.in-conversation .feature-bar{display:none}" in page


def test_the_page_follows_the_visible_height_above_a_keyboard():
    result = _run([], viewport=[512.4, 0])
    assert result["height"] == "512px"
    assert result["transform"] == ""
    assert _run([], viewport=[500, 40])["transform"] == "translateY(40px)"
