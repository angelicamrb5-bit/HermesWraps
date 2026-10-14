/* Consultation form: validates, then sends the request straight to the business inbox
   (POST /api/consult, see worker/). If the visitor picks WhatsApp, it opens WhatsApp with
   the request written out. If the direct send fails, it says so and lets the visitor send
   the same request by email or WhatsApp, or copy it. */
(function () {
  'use strict';
  var WHATSAPP = '18134751311';
  var EMAIL = 'hermeswraps@gmail.com';
  var $ = function (s, r) { return (r || document).querySelector(s); };

  var form = $('#consultForm'), done = $('#formDone'), alertBox = $('#formAlert');
  if (!form) return;

  var TYPES = { commercial: 'Business & fleet vehicles', vehicle: 'Personal vehicles', signs: 'Signs & storefronts' };
  var fromUrl = new URLSearchParams(location.search).get('type');
  if (fromUrl && TYPES[fromUrl]) form.elements.type.value = fromUrl;

  var ERRORS = {
    name: 'Enter your name.',
    email: 'Enter an email address so we can send your consultation details.',
    emailFormat: 'Check the email address. It should look like name@example.com.',
    type: 'Choose a project type.',
    requirements: 'Tell us about the project: the vehicle or space and what you want done.'
  };
  var ICON = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="8" cy="8" r="6.5"/><path d="M8 4.5v4M8 11h.01"/></svg>';

  function check(el) {
    var err = document.getElementById('e-' + el.id.slice(2));
    if (!err) return true;
    var v = el.value.trim();
    var badFormat = !!v && el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
    var ok = !!v && !badFormat;
    el.setAttribute('aria-invalid', String(!ok));
    err.hidden = ok;
    err.innerHTML = ok ? '' : ICON + '<span>' + (badFormat ? ERRORS.emailFormat : ERRORS[el.name]) + '</span>';
    return ok;
  }

  Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) {
    el.addEventListener('blur', function () { if (el.getAttribute('aria-invalid') !== null) check(el); });
    el.addEventListener('change', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); });
  });

  function message(d) {
    var lines = [
      'Free consultation request — Hermes Wraps',
      '',
      'Name: ' + d.name,
      'Email: ' + d.email,
      'Project type: ' + TYPES[d.type],
      'About the project: ' + d.requirements
    ];
    if (d.company) lines.splice(3, 0, 'Company: ' + d.company);
    if (d.phone) lines.push('Phone: ' + d.phone);
    if (d.quantity) lines.push('Quantity / fleet size: ' + d.quantity);
    if (d.timeline) lines.push('Timeline: ' + d.timeline);
    lines.push('', 'I can send brand files and photos in this conversation.');
    return lines.join('\n');
  }

  var submitBtn = form.querySelector('[data-send="direct"]');
  var submitLabel = submitBtn ? submitBtn.textContent : '';
  var aside = $('.book-aside');
  var current = null;

  function openEmail(d) {
    location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Free consultation request — ' + (d.company || d.name)) + '&body=' + encodeURIComponent(message(d));
  }
  function openWhatsApp(d) {
    var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(message(d));
    var w = window.open(url, '_blank');
    if (w) { try { w.opener = null; } catch (err) {} } else { location.href = url; }
  }

  /* state: 'sent' (in our inbox), 'whatsapp' (visitor chose WhatsApp), 'failed' (direct send failed) */
  function show(state, d) {
    var first = d.name.split(' ')[0];
    var copy = {
      sent: ['Request sent.', 'Thanks, ' + first + '. Your request is in our inbox. We will reply to ' + d.email + '. You can send brand files and photos by replying to our email or on WhatsApp.'],
      whatsapp: ['Almost done - press send.', 'Your request is ready in WhatsApp. Press send there so it reaches us.'],
      failed: ['We couldn\'t send it from here.', 'Your request is written out and ready. Send it by email or WhatsApp instead, or copy it.']
    }[state];
    $('#doneTitle').textContent = copy[0];
    $('#doneText').textContent = copy[1];
    $('#doneSteps').hidden = state !== 'sent';
    $('#doneChoose').hidden = state !== 'failed';
    $('#doneFallback').hidden = state !== 'whatsapp';
    $('#editAgain').hidden = state === 'sent';
    if (aside) aside.hidden = state === 'sent';
    form.hidden = true;
    done.hidden = false;
    done.focus();
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var mode = (e.submitter && e.submitter.getAttribute('data-send')) || 'direct';
    var bad = [];
    Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) { if (!check(el)) bad.push(el); });
    if (bad.length) {
      alertBox.hidden = false;
      bad[0].focus();
      return;
    }
    alertBox.hidden = true;

    var d = {};
    Array.prototype.forEach.call(form.elements, function (el) { if (el.name) d[el.name] = el.value.trim(); });
    current = d;

    if (mode === 'whatsapp') { openWhatsApp(d); show('whatsapp', d); return; }
    if (!window.fetch) { show('failed', d); return; }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending…';
    fetch('/api/consult', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(d) })
      .then(function (r) { return r.ok ? r.json() : { ok: false }; })
      .catch(function () { return { ok: false }; })
      .then(function (res) {
        submitBtn.disabled = false;
        submitBtn.textContent = submitLabel;
        show(res && res.ok ? 'sent' : 'failed', d);
      });
  });

  $('#chooseEmail').addEventListener('click', function () { if (current) openEmail(current); });
  $('#chooseWhatsApp').addEventListener('click', function () { if (current) openWhatsApp(current); });
  $('#copyRequest').addEventListener('click', function () {
    var btn = this;
    if (!current || !navigator.clipboard) return;
    navigator.clipboard.writeText(message(current)).then(function () {
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy request'; }, 2000);
    });
  });

  $('#editAgain').addEventListener('click', function () {
    done.hidden = true;
    form.hidden = false;
    if (aside) aside.hidden = false;
    form.elements.name.focus();
  });
})();
