/* "Tell us what you think": opens a card from the button with id
   feedback-toggle and posts the comment to the engine.

   The card is added to the page when the script runs. With JavaScript off the
   button does nothing and the Contact link in the footer still works. The
   engine address follows the same local-or-live rule as go-deeper-config.js,
   worked out here so the script stands alone. */
(function () {
  'use strict';

  var toggle = document.getElementById('feedback-toggle');
  if (!toggle) { return; }

  var isLocal = ['localhost', '127.0.0.1'].indexOf(window.location.hostname) !== -1;
  var API = isLocal ? 'http://localhost:8000' : 'https://cic-engine.onrender.com';

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
