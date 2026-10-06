/* Narration player: a typographic play control, a seekable rail, the time and
   a speed choice, drawn over each page's own <audio> element.

   The <audio> stays in the page and does all the playing, so anything that
   already starts, stops or reads it (the Atlas panel's autoplay, the pause-the-
   others rule) keeps working, and a browser without JavaScript keeps the
   ordinary controls. The speed is one setting for the whole site, remembered in
   this browser. */
(function () {
  'use strict';

  var RATE_KEY = 'cic.narration.rate';
  var RATES = [1, 1.25, 1.5, 2];
  var CSS = [
    '.cicp{--c-acc:#A13E2B;--c-fg:#2A2521;--c-mute:#6B6259;--c-rule:rgba(42,37,33,.18);',
    'flex:1 1 100%;display:flex;flex-wrap:wrap;align-items:center;gap:.3rem 1.1rem;padding:.4rem 0;',
    'border-top:1px solid var(--c-rule);border-bottom:1px solid var(--c-rule);',
    "font-family:'Alegreya Sans','Trebuchet MS',sans-serif;color:var(--c-fg)}",
    '.cicp[data-tone=dark]{--c-acc:#E08C74;--c-fg:#F1E9DD;--c-mute:#B8AEA1;--c-rule:rgba(241,233,221,.18)}',
    '.cicp button{font:inherit;cursor:pointer;background:none;border:0;padding:0;color:inherit}',
    '.cicp button:focus-visible,.cicp-rail:focus-visible{outline:2px solid var(--c-acc);outline-offset:3px;border-radius:2px}',
    '.cicp-play{display:inline-flex;align-items:center;gap:.5rem;min-height:36px;color:var(--c-acc)!important;',
    'font-weight:700;font-size:.95rem;letter-spacing:.07em;text-transform:uppercase}',
    '.cicp-play:hover{filter:brightness(1.12)}',
    '.cicp-play svg{width:13px;height:13px;fill:currentColor;flex:none}',
    '.cicp-rail{position:relative;flex:1 1 140px;min-width:120px;height:28px;cursor:pointer;touch-action:none}',
    '.cicp-rail::before{content:"";position:absolute;left:0;right:0;top:13px;height:2px;background:var(--c-rule)}',
    '.cicp-fill{position:absolute;left:0;top:13px;height:2px;width:0;background:var(--c-acc)}',
    '.cicp-dot{position:absolute;left:0;top:9px;width:10px;height:10px;margin-left:-5px;border-radius:50%;background:var(--c-acc)}',
    '.cicp-time{font-weight:600;font-size:.82rem;color:var(--c-mute);font-variant-numeric:tabular-nums;white-space:nowrap}',
    '.cicp-speeds{display:flex;gap:.2rem .75rem}',
    '.cicp-speeds button{min-height:32px;padding:0 .05rem;font-weight:600;font-size:.85rem;color:var(--c-mute);',
    'border-bottom:2px solid transparent}',
    '.cicp-speeds button:hover{color:var(--c-fg)}',
    '.cicp-speeds button[aria-pressed=true]{color:var(--c-acc);border-bottom-color:var(--c-acc)}',
    '@media (max-width:30rem){.cicp-rail{order:3;flex-basis:100%}.cicp-time{order:2}.cicp-speeds{order:4}}'
  ].join('');
  var PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>';
  var PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>';

  var players = [];

  function getRate() {
    try {
      var r = parseFloat(localStorage.getItem(RATE_KEY));
      return RATES.indexOf(r) >= 0 ? r : 1;
    } catch (e) {
      return 1;
    }
  }

  function applyRate(audio) {
    var r = getRate();
    audio.defaultPlaybackRate = r;
    audio.playbackRate = r;
    audio.preservesPitch = true;
    audio.webkitPreservesPitch = true;
  }

  function setRate(r) {
    try {
      localStorage.setItem(RATE_KEY, String(r));
    } catch (e) { /* the choice then lasts for this page only */ }
    Array.prototype.forEach.call(document.querySelectorAll('audio'), applyRate);
    players.forEach(function (p) { p.syncSpeed(); });
  }

  function clock(s) {
    s = Math.max(0, Math.floor(s || 0));
    return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2);
  }

  function toneOf(el) {
    for (var n = el; n && n.nodeType === 1; n = n.parentElement) {
      var m = /rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/.exec(getComputedStyle(n).backgroundColor);
      if (m && (m[4] === undefined || parseFloat(m[4]) > 0.5)) {
        return (0.299 * m[1] + 0.587 * m[2] + 0.114 * m[3]) / 255 < 0.5 ? 'dark' : 'light';
      }
    }
    return 'light';
  }

  function enhance(audio) {
    if (audio.dataset.cicPlayer) return;
    var host = audio.closest('.narration');
    if (!host) return;
    audio.dataset.cicPlayer = '1';
    audio.controls = false;
    audio.style.display = 'none';

    var ui = document.createElement('div');
    ui.className = 'cicp';
    ui.setAttribute('data-tone', toneOf(host));
    ui.innerHTML =
      '<button type="button" class="cicp-play"></button>' +
      '<div class="cicp-rail" role="slider" tabindex="0" aria-label="Position in the narration" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">' +
      '<span class="cicp-fill"></span><span class="cicp-dot"></span></div>' +
      '<span class="cicp-time" aria-hidden="true">0:00</span>' +
      '<div class="cicp-speeds" role="group" aria-label="Narration speed"></div>';
    audio.insertAdjacentElement('afterend', ui);

    var play = ui.querySelector('.cicp-play');
    var rail = ui.querySelector('.cicp-rail');
    var fill = ui.querySelector('.cicp-fill');
    var dot = ui.querySelector('.cicp-dot');
    var time = ui.querySelector('.cicp-time');
    var speeds = ui.querySelector('.cicp-speeds');

    var buttons = RATES.map(function (r) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = r + '×';
      b.dataset.rate = String(r);
      b.addEventListener('click', function () { setRate(r); });
      speeds.appendChild(b);
      return b;
    });

    function draw() {
      var d = audio.duration, t = audio.currentTime || 0;
      var f = d > 0 ? Math.min(100, (t / d) * 100) : 0;
      fill.style.width = f + '%';
      dot.style.left = f + '%';
      rail.setAttribute('aria-valuenow', String(Math.round(f)));
      rail.setAttribute('aria-valuetext', d > 0 ? clock(t) + ' of ' + clock(d) : clock(t));
      time.textContent = d > 0 ? clock(t) + ' / ' + clock(d) : clock(t);
      var playing = !audio.paused && !audio.ended;
      play.innerHTML = (playing ? PAUSE : PLAY) + '<span>' + (playing ? 'Pause' : (t > 0 && !audio.ended ? 'Resume' : 'Listen')) + '</span>';
      play.setAttribute('aria-label', playing ? 'Pause narration' : 'Play narration');
    }

    play.addEventListener('click', function () {
      if (audio.paused) {
        var go = audio.play();
        if (go && go.catch) go.catch(function () { /* the browser refused; the button stays as it was */ });
      } else {
        audio.pause();
      }
    });

    function seekTo(clientX) {
      var d = audio.duration;
      if (!(d > 0)) return;
      var box = rail.getBoundingClientRect();
      audio.currentTime = Math.min(1, Math.max(0, (clientX - box.left) / box.width)) * d;
    }
    rail.addEventListener('pointerdown', function (e) {
      rail.setPointerCapture(e.pointerId);
      seekTo(e.clientX);
      rail.onpointermove = function (m) { seekTo(m.clientX); };
    });
    rail.addEventListener('pointerup', function () { rail.onpointermove = null; });
    rail.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 5); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { audio.currentTime = Math.max(0, audio.currentTime - 5); e.preventDefault(); }
      else if (e.key === ' ' || e.key === 'Enter') { play.click(); e.preventDefault(); }
    });

    ['play', 'pause', 'ended', 'timeupdate', 'loadedmetadata', 'durationchange', 'emptied'].forEach(function (ev) {
      audio.addEventListener(ev, draw);
    });
    audio.addEventListener('loadedmetadata', function () { applyRate(audio); });

    players.push({
      syncSpeed: function () {
        var cur = getRate();
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(parseFloat(b.dataset.rate) === cur)); });
      }
    });
    players[players.length - 1].syncSpeed();
    applyRate(audio);
    draw();
  }

  // One voice at a time across the page.
  document.addEventListener('play', function (e) {
    if (!e.target || e.target.tagName !== 'AUDIO') return;
    applyRate(e.target);
    Array.prototype.forEach.call(document.querySelectorAll('audio'), function (a) {
      if (a !== e.target && !a.paused) a.pause();
    });
  }, true);

  function scan(root) {
    Array.prototype.forEach.call((root || document).querySelectorAll('.narration audio'), enhance);
  }

  function start() {
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);
    scan();
    new MutationObserver(function (records) {
      records.forEach(function (r) {
        Array.prototype.forEach.call(r.addedNodes, function (n) {
          if (n.nodeType !== 1) return;
          if (n.matches && n.matches('.narration audio')) enhance(n);
          else if (n.querySelectorAll) scan(n);
        });
      });
    }).observe(document.documentElement, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
