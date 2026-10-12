#!/usr/bin/env node
// Read-only evidence capture for the website-audit skill.
// Visits pages with Playwright, takes screenshots at 3 viewports and records
// page signals (meta, headings, links, images, forms, console errors, failed
// requests, basic a11y hints). Never fills or submits forms.
//
// Usage: node capture.mjs <url|file> [more...] [--out dir] [--max 15] [--crawl]
// Env:   CHROMIUM_PATH=/path/to/chromium (optional)

import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

function loadPlaywright() {
  const bases = [process.cwd(), ...(process.env.NODE_PATH || '').split(path.delimiter).filter(Boolean)];
  try { bases.push(execSync('npm root -g', { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim()); } catch {}
  for (const base of bases) {
    try { return createRequire(path.join(base, 'noop.js'))('playwright'); } catch {}
  }
  console.error('Playwright not found. Install it (npm i -g playwright) or fall back to fetch-based evidence.');
  process.exit(2);
}

const args = process.argv.slice(2);
const opts = { out: 'website-audit-evidence', max: 15, crawl: false };
const targets = [];
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === '--out') opts.out = args[++i];
  else if (a === '--max') opts.max = Number(args[++i]);
  else if (a === '--crawl') opts.crawl = true;
  else targets.push(fs.existsSync(a) ? pathToFileURL(path.resolve(a)).href : a);
}
if (!targets.length) {
  console.error('Usage: node capture.mjs <url|file> [more...] [--out dir] [--max 15] [--crawl]');
  process.exit(1);
}

const VIEWPORTS = {
  mobile: { width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
  tablet: { width: 768, height: 1024, isMobile: true, hasTouch: true, deviceScaleFactor: 1 },
  desktop: { width: 1440, height: 900, isMobile: false, hasTouch: false, deviceScaleFactor: 1 },
};

const slug = (u, n) => {
  const { hostname, pathname } = new URL(u);
  const tail = (hostname + pathname).replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').slice(-60) || 'page';
  return `${String(n).padStart(2, '0')}-${tail.replace(/^-/, '')}`;
};

// Runs in the page. Plain DOM reads only.
function collectSignals() {
  const q = (s) => [...document.querySelectorAll(s)];
  const meta = (sel) => document.querySelector(sel)?.getAttribute('content') ?? null;
  const text = (el) => (el.innerText || el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 160);
  const labelFor = (el) => {
    if (el.id && document.querySelector(`label[for="${CSS.escape(el.id)}"]`)) return 'label[for]';
    if (el.closest('label')) return 'wrapping label';
    if (el.getAttribute('aria-label')) return 'aria-label';
    if (el.getAttribute('aria-labelledby')) return 'aria-labelledby';
    if (el.getAttribute('title')) return 'title';
    return null;
  };
  const docWidth = document.documentElement.scrollWidth;
  return {
    title: document.title,
    lang: document.documentElement.getAttribute('lang'),
    metaDescription: meta('meta[name="description"]'),
    viewport: meta('meta[name="viewport"]'),
    robots: meta('meta[name="robots"]'),
    canonical: document.querySelector('link[rel="canonical"]')?.href ?? null,
    og: Object.fromEntries(q('meta[property^="og:"]').map((m) => [m.getAttribute('property'), m.getAttribute('content')])),
    twitter: Object.fromEntries(q('meta[name^="twitter:"]').map((m) => [m.getAttribute('name'), m.getAttribute('content')])),
    hreflang: q('link[rel="alternate"][hreflang]').map((l) => ({ lang: l.hreflang, href: l.href })),
    jsonLdTypes: q('script[type="application/ld+json"]').map((s) => {
      try { const j = JSON.parse(s.textContent); return [].concat(j).map((x) => x['@type'] || (x['@graph'] ? 'graph' : '?')); }
      catch { return ['INVALID JSON']; }
    }).flat(),
    headings: q('h1,h2,h3,h4,h5,h6').map((h) => `${h.tagName}: ${text(h)}`),
    h1Count: q('h1').length,
    landmarks: Object.fromEntries(['header', 'nav', 'main', 'footer', 'aside'].map((t) => [t, q(`${t},[role="${t === 'header' ? 'banner' : t === 'footer' ? 'contentinfo' : t === 'aside' ? 'complementary' : t === 'nav' ? 'navigation' : t}"]`).length])),
    skipLink: q('a[href^="#"]').slice(0, 3).some((a) => /skip|saltar/i.test(text(a))),
    links: q('a').map((a) => ({
      text: text(a) || a.getAttribute('aria-label') || a.querySelector('img')?.alt || '',
      href: a.getAttribute('href'),
      abs: a.href,
      targetBlank: a.target === '_blank',
      rel: a.rel || null,
    })),
    buttons: q('button,[role="button"],input[type="submit"],input[type="button"]').map((b) => ({
      text: text(b) || b.value || b.getAttribute('aria-label') || '', tag: b.tagName.toLowerCase(), type: b.getAttribute('type'),
    })),
    clickableNonInteractive: q('div[onclick],span[onclick]').length,
    images: q('img').map((i) => ({
      src: i.currentSrc || i.src, alt: i.getAttribute('alt'), loading: i.getAttribute('loading'),
      natural: `${i.naturalWidth}x${i.naturalHeight}`, rendered: `${i.clientWidth}x${i.clientHeight}`,
      broken: i.complete && i.naturalWidth === 0,
    })),
    forms: q('form').map((f) => ({
      action: f.getAttribute('action'), method: f.getAttribute('method'),
      fields: [...f.querySelectorAll('input,select,textarea')].filter((e) => e.type !== 'hidden').map((e) => ({
        tag: e.tagName.toLowerCase(), type: e.getAttribute('type'), name: e.name || null,
        required: e.required, autocomplete: e.getAttribute('autocomplete'), placeholder: e.getAttribute('placeholder'),
        label: labelFor(e),
      })),
    })),
    unlabeledInputsOutsideForms: q('input,select,textarea').filter((e) => !e.closest('form') && e.type !== 'hidden' && !labelFor(e)).length,
    iframes: q('iframe').map((f) => ({ src: f.src, title: f.title || null })),
    videos: q('video').map((v) => ({ autoplay: v.autoplay, muted: v.muted, controls: v.controls })),
    scripts: q('script[src]').map((s) => s.src),
    stylesheets: q('link[rel="stylesheet"]').map((l) => l.href),
    fonts: [...new Set(q('body *').slice(0, 2000).map((e) => getComputedStyle(e).fontFamily))],
    horizontalOverflow: docWidth > window.innerWidth ? `${docWidth}px > ${window.innerWidth}px` : null,
    smallTapTargets: q('a,button,input,select,textarea,[role="button"]').filter((e) => {
      const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && (r.width < 24 || r.height < 24);
    }).slice(0, 30).map((e) => `${e.tagName.toLowerCase()} "${text(e).slice(0, 40)}"`),
    wordCount: (document.body?.innerText || '').split(/\s+/).filter(Boolean).length,
  };
}

const { chromium } = loadPlaywright();
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
fs.mkdirSync(opts.out, { recursive: true });

const queue = [...targets];
const seen = new Set();
const results = [];
const origin = new URL(targets[0]).origin;

while (queue.length && results.length < opts.max) {
  const url = queue.shift().split('#')[0];
  if (seen.has(url)) continue;
  seen.add(url);
  const page = { url, slug: slug(url, results.length + 1), viewports: {} };
  for (const [name, vp] of Object.entries(VIEWPORTS)) {
    const { width, height, ...rest } = vp;
    const ctx = await browser.newContext({ viewport: { width, height }, ...rest });
    const p = await ctx.newPage();
    const consoleMsgs = [];
    const failed = [];
    const requests = [];
    p.on('console', (m) => ['error', 'warning'].includes(m.type()) && consoleMsgs.push(`${m.type()}: ${m.text()}`.slice(0, 300)));
    p.on('pageerror', (e) => consoleMsgs.push(`pageerror: ${e.message}`.slice(0, 300)));
    p.on('requestfailed', (r) => failed.push(`${r.failure()?.errorText} ${r.url()}`));
    p.on('response', (r) => {
      requests.push({ url: r.url(), status: r.status(), type: r.request().resourceType(), size: Number(r.headers()['content-length'] || 0) });
      if (r.status() >= 400) failed.push(`${r.status()} ${r.url()}`);
    });
    const vr = { consoleMsgs, failed };
    try {
      const t0 = Date.now();
      const resp = await p.goto(url, { waitUntil: 'load', timeout: 45000 });
      await p.waitForLoadState('networkidle', { timeout: 10000 }).catch(() => {});
      vr.loadMs = Date.now() - t0;
      vr.status = resp?.status() ?? null;
      vr.finalUrl = p.url();
      if (name === 'desktop') vr.headers = resp?.headers() ?? null;
      vr.signals = await p.evaluate(collectSignals);
      vr.requestCount = requests.length;
      vr.bytesByType = requests.reduce((acc, r) => ((acc[r.type] = (acc[r.type] || 0) + r.size), acc), {});
      vr.largestRequests = requests.sort((a, b) => b.size - a.size).slice(0, 10);
      vr.screenshotFold = path.join(opts.out, `${page.slug}-${name}.png`);
      await p.screenshot({ path: vr.screenshotFold });
      vr.screenshotFull = path.join(opts.out, `${page.slug}-${name}-full.png`);
      await p.screenshot({ path: vr.screenshotFull, fullPage: true });
      if (name === 'desktop') {
        // Keyboard: where does focus land in the first few tabs, and is it visible?
        await p.mouse.click(1, 1).catch(() => {});
        vr.firstTabStops = [];
        for (let i = 0; i < 8; i++) {
          await p.keyboard.press('Tab');
          vr.firstTabStops.push(await p.evaluate(() => {
            const el = document.activeElement;
            if (!el || el === document.body) return 'body';
            const s = getComputedStyle(el);
            const visible = s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0 || s.boxShadow !== 'none';
            return `${el.tagName.toLowerCase()} "${(el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 40)}" focusStyle=${visible ? 'yes' : 'maybe-none'}`;
          }));
        }
      }
    } catch (e) {
      vr.error = e.message;
    }
    page.viewports[name] = vr;
    await ctx.close();
  }
  results.push(page);
  console.log(`captured ${url}`);
  if (opts.crawl) {
    for (const l of page.viewports.desktop?.signals?.links ?? []) {
      try {
        const u = new URL(l.abs);
        if (u.origin === origin && /^https?:|^file:/.test(u.protocol) && !/\.(pdf|jpe?g|png|gif|webp|svg|zip|mp4)$/i.test(u.pathname)) {
          const clean = u.href.split('#')[0];
          if (!seen.has(clean) && !queue.includes(clean)) queue.push(clean);
        }
      } catch {}
    }
  }
}

await browser.close();
const summaryPath = path.join(opts.out, 'summary.json');
fs.writeFileSync(summaryPath, JSON.stringify({ capturedAt: new Date().toISOString(), viewports: VIEWPORTS, pages: results, notCaptured: queue }, null, 2));
console.log(`wrote ${summaryPath} (${results.length} pages${queue.length ? `, ${queue.length} queued but not captured (--max)` : ''})`);
