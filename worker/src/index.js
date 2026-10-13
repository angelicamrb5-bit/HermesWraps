/* Hermes Wraps — consultation request endpoint.
   POST /api/consult (JSON) → validates → emails the request to env.TO.
   book.js falls back to WhatsApp / email when this endpoint is unavailable. */

const TYPES = { vehicle: 'Vehicle / fleet wraps', signs: 'Signs', commercial: 'Commercial graphics', vinyl: 'Other vinyl' };
const LIMITS = { name: 120, company: 120, email: 200, type: 20, requirements: 4000, phone: 40, quantity: 60, timeline: 120 };
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') return json({ ok: false, error: 'method' }, 405);

    // Same-site posts only
    const origin = request.headers.get('origin');
    if (origin && new URL(origin).hostname.replace(/^www\./, '') !== 'hermeswraps.com') return json({ ok: false, error: 'origin' }, 403);

    let d;
    try { d = await request.json(); } catch { return json({ ok: false, error: 'body' }, 400); }
    if (!d || typeof d !== 'object') return json({ ok: false, error: 'body' }, 400);

    // Honeypot: real visitors never fill this hidden field
    if (d.website) return json({ ok: true });

    const v = {};
    for (const k of Object.keys(LIMITS)) v[k] = String(d[k] || '').trim().slice(0, LIMITS[k]);
    if (!v.name || !EMAIL_RE.test(v.email) || !TYPES[v.type] || !v.requirements) return json({ ok: false, error: 'fields' }, 422);

    const lines = [
      'Free consultation request — hermeswraps.com',
      '',
      'Name: ' + v.name,
      v.company ? 'Company: ' + v.company : null,
      'Email: ' + v.email,
      v.phone ? 'Phone: ' + v.phone : null,
      'Project type: ' + TYPES[v.type],
      v.quantity ? 'Quantity / fleet size: ' + v.quantity : null,
      v.timeline ? 'Timeline: ' + v.timeline : null,
      '',
      'Requirements:',
      v.requirements,
      '',
      'Reply to this email to answer ' + v.name + ' directly.'
    ].filter((l) => l !== null);

    try {
      await env.EMAIL.send({
        to: env.TO,
        from: { name: 'Hermes Wraps website', email: env.FROM },
        replyTo: v.email,
        subject: 'Consultation request — ' + (v.company || v.name) + ' · ' + TYPES[v.type],
        text: lines.join('\n')
      });
    } catch (err) {
      console.error('send failed', err && err.code, err && err.message);
      return json({ ok: false, error: 'send' }, 502);
    }
    return json({ ok: true });
  }
};
