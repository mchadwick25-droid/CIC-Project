/* "Tell us what you think": opens a card from the button with id
   feedback-toggle and posts the comment to the engine. On Church Family Tree
   pages and the interactive tree it also adds a quiet row at the foot of the
   page: a like, and a link that opens a small card to report a problem.

   The card is added to the page when the script runs. With JavaScript off the
   button does nothing and the Contact link in the footer still works. The
   engine address follows the same local-or-live rule as go-deeper-config.js,
   worked out here so the script stands alone. */
(function () {
  'use strict';

  var toggle = document.getElementById('feedback-toggle');
  if (!toggle) { return; }

  var isLocal = ['localhost', '127.0.0.1'].indexOf(window.location.hostname) !== -1;
  var API = isLocal ? 'http://localhost:8000' : 'https://app.churchinconversation.com';

  var segment = window.location.pathname.split('/').pop() || 'index.html';
  var PAGE = segment.indexOf('.') === -1 ? segment + '.html' : segment;

  var MARKUP =
    '<h2 id="feedback-title">Tell us what you think</h2>' +
    '<form id="feedback-form" novalidate>' +
      '<div class="fb-field">' +
        '<label for="feedback-text">What was this like for you? What should we do better?</label>' +
        '<textarea id="feedback-text" name="text" required maxlength="2000"></textarea>' +
      '</div>' +
      '<fieldset>' +
        '<legend>May we quote you?</legend>' +
        '<div class="fb-radio">' +
          '<input type="radio" id="feedback-quote-no" name="quote_consent" value="no" checked>' +
          '<label for="feedback-quote-no">No</label>' +
        '</div>' +
        '<div class="fb-radio">' +
          '<input type="radio" id="feedback-quote-anonymous" name="quote_consent" value="anonymous">' +
          '<label for="feedback-quote-anonymous">Yes, without my name</label>' +
        '</div>' +
        '<div class="fb-radio fb-name">' +
          '<input type="radio" id="feedback-quote-first-name" name="quote_consent" value="first_name">' +
          '<label for="feedback-quote-first-name">Yes, with my first name:</label>' +
          '<label class="fb-vh" for="feedback-first-name">First name</label>' +
          '<input type="text" id="feedback-first-name" name="first_name" maxlength="60" autocomplete="given-name" disabled>' +
        '</div>' +
      '</fieldset>' +
      '<p class="fb-note" id="feedback-safety">A person reads these, usually within a week. No one reads them live. If you need help now, please reach out to someone real: a person you trust, a crisis line, or emergency services where you are.</p>' +
      '<div class="fb-field">' +
        '<label for="feedback-email">Email, if you would like a reply (optional)</label>' +
        '<input type="email" id="feedback-email" name="email" maxlength="200" autocomplete="email">' +
      '</div>' +
      '<p class="fb-error" id="feedback-error" role="alert"></p>' +
      '<div class="fb-actions">' +
        '<button type="submit" class="btn primary" id="feedback-send">Send</button>' +
        '<button type="button" class="btn secondary" id="feedback-cancel">Cancel</button>' +
      '</div>' +
    '</form>' +
    '<p class="fb-done" id="feedback-done" role="status"></p>' +
    '<div class="fb-actions"><button type="button" class="btn secondary" id="feedback-close" hidden>Close</button></div>';

  var card = document.createElement('section');
  card.className = 'feedback-card';
  card.id = 'feedback-card';
  card.setAttribute('role', 'dialog');
  card.setAttribute('aria-modal', 'false');
  card.setAttribute('aria-labelledby', 'feedback-title');
  card.hidden = true;
  card.innerHTML = MARKUP;

  var bar = toggle.closest('header, .topbar, .bar') || toggle.parentNode;
  bar.insertAdjacentElement('afterend', card);
  toggle.setAttribute('aria-controls', 'feedback-card');

  var form = card.querySelector('#feedback-form');
  var text = card.querySelector('#feedback-text');
  var firstName = card.querySelector('#feedback-first-name');
  var email = card.querySelector('#feedback-email');
  var send = card.querySelector('#feedback-send');
  var errorLine = card.querySelector('#feedback-error');
  var doneLine = card.querySelector('#feedback-done');
  var closeBtn = card.querySelector('#feedback-close');
  var radios = card.querySelectorAll('input[name="quote_consent"]');

  var sent = false;

  function consent() {
    for (var i = 0; i < radios.length; i++) {
      if (radios[i].checked) { return radios[i].value; }
    }
    return 'no';
  }

  function syncName() {
    var wantsName = consent() === 'first_name';
    firstName.disabled = !wantsName;
    firstName.required = wantsName;
  }

  function place() {
    var rect = bar.getBoundingClientRect();
    var top = Math.max(8, rect.bottom + 8);
    card.style.top = top + 'px';
    card.style.maxHeight = Math.max(160, window.innerHeight - top - 8) + 'px';
  }

  function resetForm() {
    form.reset();
    syncName();
    form.hidden = false;
    errorLine.textContent = '';
    doneLine.textContent = '';
    closeBtn.hidden = true;
    send.disabled = false;
    sent = false;
  }

  function open() {
    if (sent) { resetForm(); }
    card.hidden = false;
    toggle.setAttribute('aria-expanded', 'true');
    place();
    text.focus();
  }

  function close() {
    card.hidden = true;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.focus();
  }

  toggle.addEventListener('click', function () {
    if (card.hidden) { open(); } else { close(); }
  });

  card.querySelector('#feedback-cancel').addEventListener('click', close);
  closeBtn.addEventListener('click', close);

  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && !card.hidden) { close(); }
  });

  window.addEventListener('resize', function () { if (!card.hidden) { place(); } });
  window.addEventListener('scroll', function () { if (!card.hidden) { place(); } }, { passive: true });

  for (var i = 0; i < radios.length; i++) {
    radios[i].addEventListener('change', function () {
      syncName();
      if (consent() === 'first_name') { firstName.focus(); }
    });
  }
  syncName();

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (sent) { return; }

    var comment = text.value.trim();
    if (!comment) { text.value = ''; }
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    var choice = consent();
    var body = {
      kind: 'comment',
      page: PAGE,
      text: comment,
      quote_consent: choice,
      first_name: choice === 'first_name' ? firstName.value.trim() : null,
      email: email.value.trim() || null
    };

    errorLine.textContent = '';
    send.disabled = true;

    fetch(API + '/api/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      credentials: 'omit',
      referrerPolicy: 'no-referrer'
    }).then(function (res) {
      if (res.status !== 201) { throw new Error('status ' + res.status); }
      sent = true;
      form.hidden = true;
      doneLine.textContent = 'Thank you. A person reads these each week.';
      closeBtn.hidden = false;
      closeBtn.focus();
    }).catch(function () {
      errorLine.textContent = "That didn't go through. Try again in a moment, or email info@churchinconversation.com.";
      send.disabled = false;
    });
  });
})();

(function () {
  'use strict';

  var id = window.location.pathname.replace(/^\/+/, '').replace(/\.html$/, '');
  var onTree = id.indexOf('tree/') === 0 && id.length > 5;
  var onAtlas = id === 'atlas-v3';
  if (!onTree && !onAtlas) { return; }

  var PAGE = id.replace(/[^A-Za-z0-9\/_.:-]/g, '-').slice(0, 120);
  var LIKE_KEY = 'cic-page-like:' + PAGE;
  var MAX_NOTE = 600;

  var isLocal = ['localhost', '127.0.0.1'].indexOf(window.location.hostname) !== -1;
  var API = isLocal ? 'http://localhost:8000' : 'https://app.churchinconversation.com';

  var HEART =
    '<svg class="pf-heart" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
      '<path d="M12 20.5 4.2 12.9a4.7 4.7 0 0 1 0-6.7 4.8 4.8 0 0 1 6.8 0l1 1 1-1a4.8 4.8 0 0 1 6.8 0 4.7 4.7 0 0 1 0 6.7L12 20.5Z" ' +
      'fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>' +
    '</svg>';

  var MARKUP =
    '<div class="pf-row">' +
      '<button type="button" class="pf-like" id="pf-like" aria-pressed="false">' + HEART + 'This helped</button>' +
      '<button type="button" class="pf-report" id="pf-report" aria-expanded="false" aria-controls="pf-card">Report a problem</button>' +
    '</div>' +
    '<p class="pf-status" id="pf-status" role="status"></p>' +
    '<form class="pf-card" id="pf-card" role="dialog" aria-labelledby="pf-title" novalidate hidden>' +
      '<p class="pf-title" id="pf-title">Tell us what is wrong</p>' +
      '<fieldset>' +
        '<legend>What kind of problem?</legend>' +
        '<div class="pf-chips">' +
          '<span class="pf-chip"><input type="radio" id="pf-reason-accuracy" name="reason" value="accuracy"><label for="pf-reason-accuracy">Accuracy</label></span>' +
          '<span class="pf-chip"><input type="radio" id="pf-reason-craft" name="reason" value="craft"><label for="pf-reason-craft">Craft</label></span>' +
        '</div>' +
      '</fieldset>' +
      '<div class="pf-field">' +
        '<label for="pf-note">What did you see?</label>' +
        '<textarea id="pf-note" name="text" required maxlength="' + MAX_NOTE + '" aria-describedby="pf-count"></textarea>' +
        '<p class="pf-fine" id="pf-count"></p>' +
      '</div>' +
      '<p class="pf-fine">A person reads these, usually within a week. No one reads them live. If you need help now, please reach out to someone real: a person you trust, a crisis line, or emergency services where you are.</p>' +
      '<div class="pf-field">' +
        '<label for="pf-email">Email (only if you want a reply)</label>' +
        '<input type="email" id="pf-email" name="email" maxlength="200" autocomplete="email">' +
      '</div>' +
      '<p class="pf-error" id="pf-error" role="alert"></p>' +
      '<div class="pf-actions">' +
        '<button type="submit" class="pf-send" id="pf-send" disabled>Send</button>' +
        '<button type="button" class="pf-cancel" id="pf-cancel">Cancel</button>' +
      '</div>' +
    '</form>';

  var root = document.createElement('div');
  root.className = 'page-feedback' + (onAtlas ? ' page-feedback--fixed' : '');
  root.innerHTML = MARKUP;

  var footer = document.querySelector('.site-footer');
  if (onTree && footer) {
    footer.parentNode.insertBefore(root, footer);
  } else {
    (document.querySelector('main') || document.body).appendChild(root);
  }

  var likeBtn = root.querySelector('#pf-like');
  var reportBtn = root.querySelector('#pf-report');
  var status = root.querySelector('#pf-status');
  var card = root.querySelector('#pf-card');
  var note = root.querySelector('#pf-note');
  var email = root.querySelector('#pf-email');
  var count = root.querySelector('#pf-count');
  var sendBtn = root.querySelector('#pf-send');
  var errorLine = root.querySelector('#pf-error');
  var radios = root.querySelectorAll('input[name="reason"]');

  function post(body) {
    return fetch(API + '/api/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      credentials: 'omit',
      referrerPolicy: 'no-referrer'
    }).then(function (res) {
      if (res.status !== 201) { throw new Error('status ' + res.status); }
    });
  }

  function setLiked() {
    likeBtn.setAttribute('aria-pressed', 'true');
    likeBtn.disabled = true;
  }

  try {
    if (window.localStorage.getItem(LIKE_KEY) === '1') { setLiked(); }
  } catch (e) { /* storage blocked: the like still works for this visit */ }

  likeBtn.addEventListener('click', function () {
    if (likeBtn.disabled) { return; }
    likeBtn.disabled = true;
    post({ kind: 'like', page: PAGE }).then(function () {
      setLiked();
      try { window.localStorage.setItem(LIKE_KEY, '1'); } catch (e) { /* remembering is a convenience */ }
    }).catch(function () {
      likeBtn.disabled = false;
    });
  });

  function reason() {
    for (var i = 0; i < radios.length; i++) {
      if (radios[i].checked) { return radios[i].value; }
    }
    return '';
  }

  function sync() {
    count.textContent = (MAX_NOTE - note.value.length) + ' characters left';
    sendBtn.disabled = !reason() || !note.value.trim();
  }

  function open() {
    status.textContent = '';
    card.hidden = false;
    reportBtn.setAttribute('aria-expanded', 'true');
    sync();
    radios[0].focus();
  }

  function close() {
    card.hidden = true;
    reportBtn.setAttribute('aria-expanded', 'false');
    reportBtn.focus();
  }

  reportBtn.addEventListener('click', function () {
    if (card.hidden) { open(); } else { close(); }
  });
  root.querySelector('#pf-cancel').addEventListener('click', close);
  card.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape') { ev.stopPropagation(); close(); }
  });
  note.addEventListener('input', sync);
  for (var i = 0; i < radios.length; i++) { radios[i].addEventListener('change', sync); }

  card.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var text = note.value.trim();
    var kind = reason();
    if (!kind || !text || sendBtn.disabled) { return; }
    errorLine.textContent = '';
    sendBtn.disabled = true;
    post({ kind: 'report', page: PAGE, reason: kind, text: text, email: email.value.trim() || null }).then(function () {
      card.reset();
      errorLine.textContent = '';
      close();
      status.textContent = 'Thank you. A person will read it.';
    }).catch(function () {
      errorLine.textContent = "That didn't go through. Try again in a moment, or email info@churchinconversation.com.";
      sendBtn.disabled = false;
    });
  });
})();
