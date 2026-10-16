"""Rebuild the generated pages of the Hermes Wraps site.

index.html is edited by hand. This script:
  1. builds work.html, terms.html and 404.html from scripts/pages.py, reusing
     the header, closing band and footer from index.html;
  2. refreshes the type tiles in index.html (between <!--TYPE-TILES--> markers);
  3. gives every card photo a srcset (800px + 1600px) so phones get sharp images;
  4. adds ?v=<hash> to CSS/JS links so browsers never mix old and new files;
  5. writes a WebP copy of every card photo and serves it through <picture>,
     keeping the JPEG as the fallback.

Run:  python3 scripts/build.py
"""
import hashlib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(os.path.dirname(HERE), 'public')
os.chdir(PUBLIC)

src = open('index.html').read()
head = src[:src.index('  <script type="application/ld+json">')]
top = src[src.index('<body'):src.index('  <main id="main">')]
foot = src[src.index('  <!-- 10. Footer -->'):]
closing = src[src.index('    <!-- 9. Closing CTA band -->'):src.index('  </main>')]


def page(fn, title, desc, canon, main, extra_js=''):
    h = re.sub(r'<title>.*?</title>', '<title>' + title + '</title>', head)
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + desc + '">', h)
    h = h.replace('<link rel="canonical" href="https://hermeswraps.com/">', '<link rel="canonical" href="https://hermeswraps.com' + canon + '">')
    h = h.replace('<meta property="og:url" content="https://hermeswraps.com/">', '<meta property="og:url" content="https://hermeswraps.com' + canon + '">')
    h = h.replace('  <link rel="preload" as="image" href="/assets/hero-loop-poster.jpg">\n', '')
    if fn == '404.html':
        h = h.replace('<link rel="canonical" href="https://hermeswraps.com/404">', '<meta name="robots" content="noindex">')
    h += "  <script>document.documentElement.classList.add('js')</script>\n</head>\n"
    t = top
    if fn == 'work.html':
        t = t.replace('<a href="/work">Work</a>', '<a href="/work" aria-current="page">Work</a>')
    f = foot
    if extra_js:
        f = re.sub(r'(  <script src="/assets/site\.js[^"]*" defer></script>)', lambda m: m.group(1) + '\n' + extra_js, f)
    open(fn, 'w').write(h + t + '  <main id="main">\n' + main + closing + '  </main>\n\n' + f)


exec(open(os.path.join(HERE, 'pages.py')).read())

s = open('index.html').read()
a = s.index('<!--TYPE-TILES-->') + len('<!--TYPE-TILES-->')
b = s.index('        <!--/TYPE-TILES-->')
open('index.html', 'w').write(s[:a] + '\n        ' + TILES + '\n' + s[b:])

SIZES = '(max-width: 560px) calc(100vw - 32px), (max-width: 1100px) 50vw, 400px'


def responsive(m):
    tag = m.group(0)
    if 'srcset=' in tag:
        tag = re.sub(r'\s(srcset|sizes)="[^"]*"', '', tag)
    sm = re.search(r'src="/assets/([^"]+?)(-800)?\.jpg"', tag)
    if not sm:
        return tag
    base = sm.group(1)
    if not (os.path.exists('assets/' + base + '.jpg') and os.path.exists('assets/' + base + '-800.jpg')):
        return tag
    # Optional -1200 step (retouched photos from enhance.py) keeps 3x phones off the 1600w file
    steps = [('-800', 800)] + ([('-1200', 1200)] if os.path.exists('assets/' + base + '-1200.jpg') else []) + [('', 1600)]
    def srcset(ext):
        return ', '.join(f'/assets/{base}{s}.{ext} {w}w' for s, w in steps)
    tag = tag.replace(sm.group(0), f'src="/assets/{base}-800.jpg" srcset="{srcset("jpg")}" sizes="{SIZES}"')
    for s, _ in steps:
        webp(base + s)
    return (f'<picture><source type="image/webp" srcset="{srcset("webp")}" sizes="{SIZES}">'
            + tag + '</picture>')


def webp(name):
    src, out = 'assets/' + name + '.jpg', 'assets/' + name + '.webp'
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        Image.open(src).save(out, 'WEBP', quality=80, method=6)


def bust(html):
    def ver(m):
        path = m.group(2)
        h = hashlib.sha1(open(path.lstrip('/'), 'rb').read()).hexdigest()[:8]
        return f'{m.group(1)}{path}?v={h}"'
    return re.sub(r'((?:href|src)=")(/assets/[\w-]+\.(?:css|js))(?:\?v=\w+)?"', ver, html)


for fn in ['index.html', 'work.html', 'book.html', 'terms.html', '404.html']:
    html = open(fn).read()
    html = re.sub(r'<div class="media">(?:<picture><source [^>]+>)?(<img [^>]+>)(?:</picture>)?', lambda m: '<div class="media">' + responsive(re.match(r'.+', m.group(1))), html)
    html = bust(html)
    open(fn, 'w').write(html)
print('built', len(projects), 'projects')
