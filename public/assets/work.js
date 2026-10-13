/* Work page: filters + native <dialog> image zoom */
(function () {
  'use strict';
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var cards = $$('#workGrid .project-card'), filters = $$('.filter'), prompt = document.querySelector('[data-prompt]');
  var empty = document.getElementById('emptyState'), status = document.getElementById('filterStatus');
  var LABELS = { all: 'All', commercial: 'Commercial & work vehicles', signs: 'Signs & storefronts', vinyl: 'Other vinyl', vehicle: 'Personal vehicles' };

  function apply(cat, fromHash) {
    if (!LABELS[cat]) cat = 'all';
    var n = 0;
    cards.forEach(function (c) { var on = cat === 'all' || c.getAttribute('data-cat') === cat; c.hidden = !on; if (on) n++; });
    filters.forEach(function (f) { f.setAttribute('aria-pressed', String(f.getAttribute('data-filter') === cat)); });
    if (prompt) prompt.hidden = cat !== 'all';
    empty.hidden = n > 0;
    status.textContent = LABELS[cat] + ': ' + n + (n === 1 ? ' project' : ' projects');
    if (!fromHash) history.replaceState(null, '', cat === 'all' ? location.pathname : '#' + cat);
  }
  filters.forEach(function (f) { f.addEventListener('click', function () { apply(f.getAttribute('data-filter')); }); });
  var reset = document.querySelector('[data-filter-reset]');
  if (reset) reset.addEventListener('click', function (e) { e.preventDefault(); apply('all'); });
  apply(location.hash.slice(1) || 'all', true);

  var dlg = document.getElementById('zoom');
  if (!dlg || typeof dlg.showModal !== 'function') {
    $$('[data-zoom]').forEach(function (b) { b.addEventListener('click', function () { window.open(b.getAttribute('data-zoom').split(',')[0], '_blank'); }); });
    return;
  }
  var img = dlg.querySelector('img'), cap = document.getElementById('zoomCap'), cnt = document.getElementById('zoomCount');
  var prev = dlg.querySelector('[data-zoom-prev]'), next = dlg.querySelector('[data-zoom-next]');
  var list = [], at = 0, title = '', alt = '';
  function show(n) {
    at = (n + list.length) % list.length;
    img.src = list[at];
    img.alt = alt + (list.length > 1 ? ' (photo ' + (at + 1) + ' of ' + list.length + ')' : '');
    cnt.textContent = list.length > 1 ? (at + 1) + ' / ' + list.length : '';
    prev.hidden = next.hidden = list.length < 2;
  }
  $$('[data-zoom]').forEach(function (b) {
    b.addEventListener('click', function () {
      var card = b.closest('.project-card');
      list = b.getAttribute('data-zoom').split(',');
      alt = card.querySelector('.media img').alt;
      cap.textContent = b.textContent + ' — ' + card.querySelector('p:last-of-type').textContent;
      show(0);
      dlg.showModal();
    });
  });
  prev.addEventListener('click', function () { show(at - 1); });
  next.addEventListener('click', function () { show(at + 1); });
  dlg.addEventListener('keydown', function (e) {
    if (list.length < 2) return;
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(at - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); show(at + 1); }
  });
  dlg.querySelector('[data-close-zoom]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();
