/* Hermes Wraps — shared site behaviour (no dependencies) */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduced = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* Data saver on: keep the poster, let the visitor start the video */
  var saveData = !!(navigator.connection && navigator.connection.saveData);

  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* Analytics hook: Cloudflare Web Analytics records page views; this
     forwards named clicks to any tracker that is added later. */
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-track]');
    if (!t) return;
    var name = t.getAttribute('data-track');
    if (typeof window.hwTrack === 'function') window.hwTrack(name);
  });

  /* Sticky header shadow */
  var header = $('#siteHeader');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* Mobile menu sheet: Escape closes, focus stays inside */
  var sheet = $('#mobileSheet');
  var openBtn = $('.site-header .menu-btn');
  if (sheet && openBtn) {
    var focusables = function () { return $$('a[href], button:not([disabled])', sheet); };
    var openSheet = function () {
      sheet.hidden = false;
      document.body.style.overflow = 'hidden';
      openBtn.setAttribute('aria-expanded', 'true');
      var f = focusables(); if (f.length) f[f.length > 1 ? 1 : 0].focus();
    };
    var closeSheet = function (restore) {
      sheet.hidden = true;
      document.body.style.overflow = '';
      openBtn.setAttribute('aria-expanded', 'false');
      if (restore !== false) openBtn.focus();
    };
    openBtn.addEventListener('click', openSheet);
    $('[data-close]', sheet).addEventListener('click', function () { closeSheet(); });
    $$('a', sheet).forEach(function (a) { a.addEventListener('click', function () { closeSheet(false); }); });
    sheet.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeSheet(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    window.addEventListener('resize', function () { if (!sheet.hidden && window.innerWidth > 960) closeSheet(false); });
  }

  /* Hero background video: plays muted unless reduced motion; always pausable */
  var hv = $('#heroVideo'), toggle = $('#heroVideoToggle');
  if (hv && toggle) {
    var label = $('span', toggle);
    var icon = $('svg', toggle);
    var pauseIcon = icon.innerHTML;
    var playIcon = '<path d="M4 2.5v11a.5.5 0 0 0 .77.42l8.5-5.5a.5.5 0 0 0 0-.84l-8.5-5.5A.5.5 0 0 0 4 2.5z"/>';
    var setState = function (playing) {
      toggle.setAttribute('aria-pressed', String(!playing));
      label.textContent = playing ? 'Pause background video' : 'Play background video';
      icon.innerHTML = playing ? pauseIcon : playIcon;
    };
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      if (hv.paused) { var p = hv.play(); if (p && p.catch) p.catch(function () {}); setState(true); }
      else { hv.pause(); setState(false); }
    });
    if (reduced || saveData) { setState(false); }
    else {
      var p = hv.play();
      if (p && p.then) p.then(function () { setState(true); }).catch(function () { setState(false); });
      else setState(true);
    }
    /* Save battery: pause while off screen, resume if it was playing */
    var heroVisible = true;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        heroVisible = en[0].isIntersecting;
        if (toggle.getAttribute('aria-pressed') === 'true') return;
        if (en[0].isIntersecting) { var q = hv.play(); if (q && q.catch) q.catch(function () {}); }
        else hv.pause();
      }, { threshold: 0.1 }).observe(hv);
    }
  }

  /* Header CTA steps back while the hero (with its own CTA) is on screen */
  var heroEl = $('#hero');
  if (heroEl && 'IntersectionObserver' in window) {
    document.body.classList.add('hero-in-view');
    new IntersectionObserver(function (en) { document.body.classList.toggle('hero-in-view', en[0].isIntersecting); }, { threshold: 0.35 }).observe(heroEl);
  }

  /* Sticky mobile CTA: after the hero, hidden near the closing band */
  var sticky = $('#stickyCta');
  if (sticky && 'IntersectionObserver' in window) {
    var hero = $('#hero') || $('.page-hero'), closing = $('#closing'), footer = $('.site-footer');
    var pastHero = false, nearEnd = false;
    var update = function () {
      var show = pastHero && !nearEnd;
      sticky.classList.toggle('is-visible', show);
      sticky.setAttribute('aria-hidden', String(!show));
      $('a', sticky).tabIndex = show ? 0 : -1;
    };
    if (hero) new IntersectionObserver(function (en) { pastHero = !en[0].isIntersecting && en[0].boundingClientRect.top < 0; update(); }).observe(hero);
    var ends = [closing, footer].filter(Boolean), seen = new Map();
    var endObs = new IntersectionObserver(function (en) {
      en.forEach(function (x) { seen.set(x.target, x.isIntersecting); });
      nearEnd = Array.from(seen.values()).some(Boolean); update();
    });
    ends.forEach(function (el) { endObs.observe(el); });
  }

  /* Videos with sound (home before-and-after): the background video pauses while
     one plays, and they stop when scrolled out of view, so sound never keeps playing */
  var clips = $$('.story-photo video');
  clips.forEach(function (v) {
    v.addEventListener('play', function () {
      clips.forEach(function (o) { if (o !== v && !o.paused) o.pause(); });
      if (hv && !hv.paused) hv.pause();
    });
    v.addEventListener('pause', function () {
      if (hv && toggle && heroVisible && toggle.getAttribute('aria-pressed') !== 'true' && !reduced && !saveData && !clips.some(function (o) { return !o.paused; })) {
        var q = hv.play(); if (q && q.catch) q.catch(function () {});
      }
    });
  });
  if (clips.length && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (!x.isIntersecting && !x.target.paused) x.target.pause(); });
    }, { threshold: 0.25 });
    clips.forEach(function (v) { co.observe(v); });
  }
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) clips.forEach(function (v) { if (!v.paused) v.pause(); });
  });

  /* Active nav link for in-page sections */
  var navLinks = $$('.main-nav ul a[href^="/#"]');
  if (navLinks.length && location.pathname === '/' && 'IntersectionObserver' in window) {
    var map = {};
    navLinks.forEach(function (a) { var id = a.getAttribute('href').slice(2); var s = document.getElementById(id); if (s) map[id] = a; });
    var so = new IntersectionObserver(function (en) {
      en.forEach(function (x) {
        var a = map[x.target.id]; if (!a) return;
        if (x.isIntersecting) { navLinks.forEach(function (l) { l.classList.remove('is-active'); }); a.classList.add('is-active'); }
        else a.classList.remove('is-active');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(map).forEach(function (id) { so.observe(document.getElementById(id)); });
  }
})();
