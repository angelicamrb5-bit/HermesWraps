/* Consultation form: validates, then opens WhatsApp or email with the request ready to send.
   Replace with a real submission (Worker → business inbox, with uploads) once decision D5 is made. */
(function () {
  'use strict';
  var WHATSAPP = '18134751311';
  var EMAIL = 'hermeswraps@gmail.com';
  var $ = function (s, r) { return (r || document).querySelector(s); };

  var form = $('#consultForm'), done = $('#formDone'), alertBox = $('#formAlert');
  if (!form) return;

  var TYPES = { vehicle: 'Vehicle / fleet wraps', signs: 'Signs', commercial: 'Commercial graphics', vinyl: 'Other vinyl' };
  var fromUrl = new URLSearchParams(location.search).get('type');
  if (fromUrl && TYPES[fromUrl]) form.elements.type.value = fromUrl;

  var ERRORS = {
    name: 'Enter your name.',
    company: 'Enter your company name.',
    email: 'Enter a work email so we can send your consultation details.',
    type: 'Choose a project type.',
    requirements: 'Tell us the standards this project must meet.'
  };
  var ICON = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="8" cy="8" r="6.5"/><path d="M8 4.5v4M8 11h.01"/></svg>';

  function check(el) {
    var err = document.getElementById('e-' + el.id.slice(2));
    if (!err) return true;
    var v = el.value.trim();
    var ok = !!v && (el.type !== 'email' || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
    el.setAttribute('aria-invalid', String(!ok));
    err.hidden = ok;
    err.innerHTML = ok ? '' : ICON + '<span>' + ERRORS[el.name] + '</span>';
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
      'Company: ' + d.company,
      'Work email: ' + d.email,
      'Project type: ' + TYPES[d.type],
      'Requirements: ' + d.requirements
    ];
    if (d.phone) lines.push('Phone: ' + d.phone);
    if (d.quantity) lines.push('Quantity / fleet size: ' + d.quantity);
    if (d.timeline) lines.push('Timeline: ' + d.timeline);
    lines.push('', 'I can send brand files and photos in this conversation.');
    return lines.join('\n');
  }

  var lastText = '';
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var mode = (e.submitter && e.submitter.getAttribute('data-send')) || 'whatsapp';
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
    var text = message(d);
    lastText = text;

    if (mode === 'email') {
      location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Free consultation request — ' + (d.company || d.name)) + '&body=' + encodeURIComponent(text);
      $('#doneText').textContent = 'Your request is ready in your email app. Press send there so it reaches us.';
    } else {
      var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(text);
      var w = window.open(url, '_blank');
      if (w) { try { w.opener = null; } catch (err) {} } else { location.href = url; }
      $('#doneText').textContent = 'Your request is ready in WhatsApp. Press send there so it reaches us.';
    }
    form.hidden = true;
    done.hidden = false;
    done.focus();
  });

  /* Backup when WhatsApp or the email app doesn't open: copy the request */
  var copyBtn = $('#copyRequest'), copyStatus = $('#copyStatus');
  if (copyBtn) copyBtn.addEventListener('click', function () {
    var ok = function () { copyStatus.textContent = 'Copied. Paste it into WhatsApp or an email to hermeswraps@gmail.com.'; };
    var fail = function () { copyStatus.textContent = 'Copy failed. Select the text from your form and send it to (813) 475-1311.'; };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(lastText).then(ok, fail);
    else {
      var t = document.createElement('textarea'); t.value = lastText; t.setAttribute('readonly', ''); t.style.position = 'absolute'; t.style.left = '-9999px';
      document.body.appendChild(t); t.select();
      try { document.execCommand('copy') ? ok() : fail(); } catch (err) { fail(); }
      document.body.removeChild(t);
    }
  });

  $('#editAgain').addEventListener('click', function () {
    copyStatus && (copyStatus.textContent = '');
    done.hidden = true;
    form.hidden = false;
    form.elements.name.focus();
  });
})();
