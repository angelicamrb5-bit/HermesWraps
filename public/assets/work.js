/* Work page: filters + native <dialog> image zoom */
(function () {
  'use strict';
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var cards = $$('#workGrid .project-card'), filters = $$('.filter'), prompt = document.querySelector('[data-prompt]');
  var empty = document.getElementById('emptyState'), status = document.getElementById('filterStatus');
  var LABELS = { all: 'All', fleet: 'Fleet', vehicle: 'Vehicle', signs: 'Signs', commercial: 'Commercial', vinyl: 'Other vinyl' };

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
    $$('[data-zoom]').forEach(function (b) { b.addEventListener('click', function () { window.open(b.getAttribute('data-zoom'), '_blank'); }); });
    return;
  }
  var img = dlg.querySelector('img'), cap = document.getElementById('zoomCap');
  $$('[data-zoom]').forEach(function (b) {
    b.addEventListener('click', function () {
      var card = b.closest('.project-card'), src = card.querySelector('.media img');
      img.src = b.getAttribute('data-zoom');
      img.alt = src.alt;
      cap.textContent = b.textContent + ' — ' + card.querySelector('p:last-of-type').textContent;
      dlg.showModal();
    });
  });
  dlg.querySelector('[data-close-zoom]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();
