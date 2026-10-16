import os
CHEV = '<svg viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M7 4l5 5-5 5"/></svg>'

# (category, [images], title, meta, line, alt) — images under /assets/ ; work/ ones have an -800 version
W = 'work/'
projects = [
  ("commercial", [W+"cargo-van-construction-side", W+"cargo-van-construction-rear"], "Cargo van | full wrap for a construction company", "FULL WRAP · CARGO VAN", "Black and gold full wrap with logo, phone and QR code.", "Black cargo van with a gold and black construction company wrap"),
  ("vehicle", ["tucson-pink-front", "tucson-pink-rear"], "Hyundai Tucson | full color change", "FULL COLOR CHANGE · SUV", "Full color change, front to rear.", "Hyundai Tucson after a full pink color-change wrap"),
  ("vehicle", ["silverado-hood-angle", "silverado-hood-close"], "Chevrolet Silverado | hood wrap", "PARTIAL WRAP · PICKUP", "Hood wrap, with a close view of the edges.", "Chevrolet Silverado with a wrapped hood"),
  ("commercial", [W+"wrecker-towing-front", W+"wrecker-towing-side"], "Ford F-Series wrecker | towing company wrap", "FULL WRAP · TOW TRUCK", "Bold printed graphics carried across the cab and the wrecker body.", "Ford wrecker tow truck with an orange and white towing company wrap"),
  ("vehicle", ["corvette-front", "corvette-side"], "Chevrolet Corvette C8 | gloss black roof & mirrors", "PARTIAL WRAP · SPORTS CAR", "Gloss black roof and mirrors.", "White Chevrolet Corvette C8 with a gloss black roof and mirrors"),
  ("commercial", [W+"box-truck-tire-shop-side", W+"box-truck-tire-shop-rear"], "Box truck | full box graphics", "COMMERCIAL GRAPHICS · BOX TRUCK", "Printed graphics on both sides and the rear door of the box.", "Box truck with full printed graphics for a tire shop"),
  ("commercial", [W+"cybertruck-electric"], "Tesla Cybertruck | matte black with brand graphics", "COMMERCIAL GRAPHICS · PICKUP", "Matte black finish with the company logo on the doors.", "Matte black Tesla Cybertruck with an electrical company logo on the doors"),
  ("commercial", [W+"dump-truck-front", W+"dump-truck-rear"], "Dump truck | cab and body graphics", "COMMERCIAL GRAPHICS · DUMP TRUCK", "Logo and phone number matched across the cab and dump body.", "Red dump truck with company logo and phone number graphics"),
  ("signs", [W+"storefront-windows-pet-store", W+"storefront-doors-pet-store"], "Pet store | storefront window & door graphics", "WINDOW GRAPHICS · STOREFRONT", "Full-color printed graphics across the windows and entry doors.", "Pet store storefront with full-color parrot and bird window graphics"),
  ("commercial", [W+"transit-van-hvac-front", W+"transit-van-hvac-rear"], "Ford Transit | heating & cooling van graphics", "COMMERCIAL GRAPHICS · CARGO VAN", "Services, phone numbers and brand partners laid out across the van.", "White Ford Transit van with heating and cooling company graphics"),
  ("commercial", [W+"wrecker-junk-cars-front", W+"wrecker-junk-cars-side"], "Wrecker | cash-for-cars graphics", "FULL WRAP · TOW TRUCK", "Red, white and black printed wrap with logo and phone number.", "Red wrecker tow truck with printed graphics for a junk car buyer"),
  ("commercial", [W+"express-van-electrical-side", W+"express-van-electrical-rear"], "Chevrolet Express | electrical contractor graphics", "COMMERCIAL GRAPHICS · CARGO VAN", "Logo, services, phone and QR code applied to the sides and rear.", "White and blue Chevrolet Express van with electrical services graphics"),
  ("commercial", [W+"promaster-van-electric"], "Ram ProMaster | electrical company wrap", "FULL WRAP · CARGO VAN", "Purple full wrap with logo and phone number.", "Purple Ram ProMaster van wrapped for an electrical company"),
  ("commercial", [W+"vacuum-truck-side", W+"vacuum-truck-rear"], "Vacuum truck | tank and cab graphics", "COMMERCIAL GRAPHICS · TANK TRUCK", "Printed graphics applied around the tank and onto the cab.", "Vacuum tank truck with printed graphics on the tank and cab"),
  ("commercial", [W+"isuzu-truck-landscape-side", W+"isuzu-truck-landscape-front"], "Isuzu truck | landscaping company graphics", "COMMERCIAL GRAPHICS · WORK TRUCK", "Yellow cab and body with logo and phone number.", "Yellow Isuzu work truck with landscaping company graphics"),
  ("commercial", [W+"transit-van-mechanical-front", W+"transit-van-mechanical-rear"], "Ford Transit | mechanical services graphics", "COMMERCIAL GRAPHICS · CARGO VAN", "Brand graphics wrapped from the sides around to the rear doors.", "White Ford Transit van with teal and orange mechanical services graphics"),
  ("commercial", [W+"cybertruck-realty-side", W+"cybertruck-realty-rear"], "Tesla Cybertruck | gold brand accents", "COMMERCIAL GRAPHICS · PICKUP", "Gold logo and pinstripe accents on a dark finish.", "Dark Tesla Cybertruck with gold logo and pinstripe accents"),
  ("commercial", [W+"express-van-full-wrap"], "Chevrolet Express | full printed wrap", "FULL WRAP · CARGO VAN", "Purple and gold full wrap with logo and phone number.", "Chevrolet Express van with a purple and gold full printed wrap"),
  ("commercial", [W+"promaster-van-front", W+"promaster-van-side"], "Ram ProMaster | full printed wrap", "FULL WRAP · CARGO VAN", "Black, gold and white graphics with logo and phone number.", "White Ram ProMaster van with black and gold printed wrap"),
  ("commercial", [W+"transit-van-decor"], "Ford Transit | home decor company wrap", "FULL WRAP · CARGO VAN", "Black and green wrap with services and phone number.", "Black Ford Transit van with green home decor company graphics"),
  ("commercial", [W+"transit-van-yellow"], "Ford Transit | yellow brand wrap", "FULL WRAP · CARGO VAN", "Yellow and black wrap with logo, services and phone.", "Ford Transit van with a yellow and black company wrap"),
  ("commercial", [W+"minivan-cleaning"], "Minivan | cleaning company graphics", "COMMERCIAL GRAPHICS · MINIVAN", "Teal printed wrap with a portrait, logo and phone number.", "Minivan with teal printed graphics for a cleaning company"),
  ("commercial", [W+"utility-cart-brand-side", W+"utility-cart-brand-rear"], "Utility cart | brand graphics", "COMMERCIAL GRAPHICS · UTILITY CART", "Logo and web address on the cargo box and body.", "White utility cart with red and black brand graphics on the cargo box"),
  ("signs", [W+"storefront-door-flooring"], "Flooring store | entry door graphics", "DOOR GRAPHICS · STOREFRONT", "Logo, address, hours and contact details on the glass doors.", "Storefront glass doors with a flooring company's logo and contact graphics"),
  ("signs", [W+"display-fridge-desserts-1", W+"display-fridge-desserts-2", W+"display-fridge-desserts-3"], "Display fridges | dessert brand wraps", "APPLIANCE WRAP · 3 UNITS", "Branded wraps on display fridges and freezers in a store.", "Display fridges wrapped with a dessert brand's logo pattern"),
  ("vehicle", [W+"utv-custom-wrap"], "Off-road UTV | custom graphic wrap", "CUSTOM WRAP · UTV", "Full-color custom graphics across the body panels.", "Off-road UTV with a full-color custom graphic wrap"),
  ("commercial", ["commercial-suv-side", "commercial-suv-hood"], "Business SUV | printed side & hood graphics", "COMMERCIAL GRAPHICS · SUV", "Logo and web address matched across side and hood.", "Compact SUV with printed commercial side graphics showing the logo, services and phone number"),
  ("vehicle", ["corolla-roof-angle", "corolla-roof-front"], "Toyota Corolla | gloss black roof", "PARTIAL WRAP · SEDAN", "Gloss black roof.", "White Toyota Corolla with a gloss black roof wrap"),
  ("vehicle", ["sedan-roof-black"], "Sedan | gloss black roof", "PARTIAL WRAP · SEDAN", "Gloss black roof.", "Gloss black roof wrap on a gray sedan"),
  # Silverado: hood story to be confirmed by the client — captions kept neutral
  ("vehicle", ["bmw-x1-hood-front", "bmw-x1-hood-roof-close"], "BMW X1 | gloss black hood & roof", "PARTIAL WRAP · SUV", "Gloss black hood and roof.", "BMW X1 with a gloss black hood and roof"),
]
from PIL import Image
ROOT = os.path.join(PUBLIC, 'assets') + '/'
def thumb(p):
    # Card photo: the retouched original from scripts/enhance.py when one exists, then the
    # background-free cutout from scripts/cutouts.py; otherwise the original.
    # The viewer always gets originals.
    for d in ('edit/', 'cutout/'):
        alt = d + p.split('/')[-1]
        if os.path.exists(ROOT + alt + '-800.jpg'):
            return alt + '-800.jpg'
    return p + ('-800' if p.startswith(W) else '') + '.jpg'

cards = []
for i, (cat, imgs, title, meta, line, alt) in enumerate(projects):
    t = title.replace('&', '&amp;')
    w, h = Image.open(ROOT + thumb(imgs[0])).size
    full = ','.join('/assets/' + p + '.jpg' for p in imgs)
    count = f' <span class="count">· {len(imgs)} photos</span>' if len(imgs) > 1 else ''
    cards.append(f'''          <article class="project-card" data-cat="{cat}">
            <div class="media"><img src="/assets/{thumb(imgs[0])}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>
            <h3><button type="button" data-zoom="{full}" aria-haspopup="dialog">{t}</button></h3>
            <span class="meta mono">{meta}{count}</span>
            <p>{line}</p>
          </article>''')


TYPES = [
  ("commercial", "Business &amp; fleet vehicles", "Vans, box trucks, tow trucks, dump trucks and company cars.", "cutout/cargo-van-construction-side-800.jpg", "Black cargo van with a gold and black construction company wrap"),
  ("vehicle", "Personal vehicles", "Full color changes and partial wraps: roofs, hoods, mirrors and chrome delete.", "cutout/tucson-pink-front-800.jpg", "Hyundai Tucson after a full pink color-change wrap"),
  ("signs", "Signs &amp; storefronts", "Window, door and in-store graphics for businesses.", W+"storefront-windows-pet-store-800.jpg", "Pet store storefront with full-color window graphics"),
]
def type_tiles(level='h3'):
    out = []
    for key, name, desc, img, alt in TYPES:
        n = sum(1 for p in projects if p[0] == key)
        w, h = Image.open(ROOT + img).size
        out.append(f"""          <article class="type-card">
            <div class="media"><img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>
            <{level}><a href="/work#{key}" data-type-link="{key}">{name}</a></{level}>
            <p>{desc}</p>
            <span class="text-link" aria-hidden="true">View catalog · {n} {"project" if n == 1 else "projects"} <span class="arrow">→</span></span>
          </article>""")
    return '<div class="type-grid type-grid-3">\n' + '\n'.join(out) + '\n        </div>'
# Home highlights: the three strongest photos, one full wrap, one partial, one business vehicle.
# They use background-free cutouts from scripts/cutouts.py; the catalog keeps the original photos.
HIGHLIGHTS = [
  ("vehicle", "Full color change", "Hyundai Tucson, wrapped front to rear in a new color.", "cutout/tucson-pink-front-800.jpg", "Hyundai Tucson after a full pink color-change wrap"),
  ("vehicle", "Partial wrap", "Chevrolet Silverado with a wrapped hood.", "cutout/silverado-hood-angle-800.jpg", "White Chevrolet Silverado with a black wrapped hood"),
  ("commercial", "Business vehicle", "Cargo van in a black and gold full wrap with logo, phone and QR code.", "cutout/cargo-van-construction-side-800.jpg", "Black cargo van with a gold and black construction company wrap"),
]
def highlight_tiles():
    out = []
    for key, name, desc, img, alt in HIGHLIGHTS:
        w, h = Image.open(ROOT + img).size
        out.append(f"""          <article class="type-card">
            <div class="media"><img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>
            <h3><a href="/work#{key}" data-type-link="{key}">{name}</a></h3>
            <p>{desc}</p>
            <span class="text-link" aria-hidden="true">See more like this <span class="arrow">→</span></span>
          </article>""")
    return '<div class="type-grid type-grid-3">\n' + '\n'.join(out) + '\n        </div>'
TILES = highlight_tiles()

work_main = f'''    <section class="page-hero page-top" aria-labelledby="workTitle">
      <div class="wrap">
        <span class="eyebrow">Selected work</span>
        <h1 id="workTitle">Work measured against our clients' standards.</h1>
        <p class="lead" id="workLead">Real Hermes Wraps projects in Tampa Bay: business and fleet vehicles, personal vehicles, signs and storefronts. Choose a type of work to open its catalog.</p>
      </div>
    </section>

    <section class="section flush-top" id="types" aria-label="Types of work">
      <div class="wrap">
        {type_tiles('h2')}
      </div>
    </section>

    <section class="section flush-top" id="catalog" aria-labelledby="catalogTitle" hidden>
      <div class="wrap">
        <a class="text-link" href="/work" data-type-reset><span class="arrow" aria-hidden="true">←</span> All types of work</a>
        <h2 id="catalogTitle" tabindex="-1">Catalog</h2>
        <ul class="filters" aria-label="Type of work">
          <li><button class="filter" type="button" data-filter="commercial" aria-pressed="false">Business &amp; fleet vehicles</button></li>
          <li><button class="filter" type="button" data-filter="vehicle" aria-pressed="false">Personal vehicles</button></li>
          <li><button class="filter" type="button" data-filter="signs" aria-pressed="false">Signs &amp; storefronts</button></li>
        </ul>
        <p class="sr-only" id="filterStatus" role="status" aria-live="polite"></p>
        <div class="card-grid" id="workGrid">
{chr(10).join(cards)}
          <p class="inline-prompt" id="midPrompt">Want one like this? <a href="/book" data-track="cta-work-mid">Book a free consultation.</a></p>
        </div>
        <p class="catalog-next" id="catalogNext"></p>
        <p class="inline-prompt">Have a standard we should meet? <a href="/book" data-track="cta-work-inline">Book a free consultation.</a></p>
      </div>
    </section>

    <section class="section bg-alt" id="social" aria-labelledby="socialTitle">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">The process on video</span>
          <h2 id="socialTitle">Watch the work on Instagram and TikTok.</h2>
          <p>Installations, removals and finished vehicles, filmed by Hermes Wraps.</p>
        </div>
        <ul class="social-links">
          <li><a class="btn btn-secondary" href="https://www.instagram.com/hermeswraps/" target="_blank" rel="noopener" data-track="instagram-work">Instagram<span class="sr-only"> (opens in a new tab)</span> <span class="arrow" aria-hidden="true">→</span></a></li>
          <li><a class="btn btn-secondary" href="https://www.tiktok.com/@hermeswraps" target="_blank" rel="noopener" data-track="tiktok-work">TikTok<span class="sr-only"> (opens in a new tab)</span> <span class="arrow" aria-hidden="true">→</span></a></li>
        </ul>
      </div>
    </section>

    <dialog class="zoom" id="zoom" aria-label="Project image">
      <img alt="">
      <div class="zoom-bar">
        <p id="zoomCap"></p>
        <div class="zoom-nav">
          <button class="btn btn-secondary-dark btn-s" type="button" data-zoom-prev aria-label="Previous photo">←</button>
          <span class="mono" id="zoomCount" aria-live="polite"></span>
          <button class="btn btn-secondary-dark btn-s" type="button" data-zoom-next aria-label="Next photo">→</button>
          <button class="btn btn-dark btn-s" type="button" data-close-zoom>Close</button>
        </div>
        <p class="zoom-cta"><a href="/book" id="zoomBook" data-track="cta-zoom">Want one like this? Book a free consultation →</a></p>
      </div>
    </dialog>

'''

terms = [
  ("Written quote", "Only the written quote defines the scope of work. Quotes cover exterior surfaces unless stated otherwise. Door jambs, chrome delete and other extras are quoted separately."),
  ("Deposit &amp; payment", "A 50% deposit, paid once the written quote is approved, reserves the installation date and covers the material order. The balance is due before the vehicle is released. Business accounts receive payment terms in writing."),
  ("Vehicle condition", "The paint must be in sound condition. Chips, dents and scratches can show through the film. Existing damage is noted and photographed at drop-off."),
  ("Installation warranty", "Installation defects such as lifting or peeling, reported within the period stated on the quote, are inspected and repaired. Accidents, normal wear and improper care are not covered."),
  ("Care of the film", "Hand wash with pH-neutral soap. Avoid automatic car washes, pressure washing near edges, wax and harsh chemicals on the film."),
  ("Timeline", "An estimated timeline comes with the quote. Film availability and added services can extend it."),
  ("Photos &amp; video", "The process may be filmed and photographed for the portfolio. Let us know before work starts if you prefer your vehicle not to appear."),
  ("Fleet projects", "Fleet work follows an approved layout per vehicle type. Scheduling, pricing per vehicle and payment terms are set out in a written agreement."),
]
terms_html = "\n".join(f'          <li><h2>{t}</h2><p>{p}</p></li>' for t, p in terms)
terms_main = f'''    <section class="page-hero page-top" aria-labelledby="termsTitle">
      <div class="wrap prose">
        <span class="eyebrow">Terms of service</span>
        <h1 id="termsTitle">Clear terms before work begins.</h1>
        <p class="lead">Every project starts with a written quote. These are the main terms; the complete terms are included with each quote. Nothing is scheduled until the written quote is approved.</p>
      </div>
    </section>
    <section class="section flush-top" aria-label="Terms">
      <div class="wrap prose">
        <ol class="terms-list">
{terms_html}
        </ol>
        <p class="muted">Questions about these terms? Ask during your free consultation.</p>
      </div>
    </section>
    <section class="section bg-alt" id="privacy" aria-labelledby="privacyTitle">
      <div class="wrap prose">
        <span class="eyebrow">Privacy</span>
        <h2 id="privacyTitle">How we use your details.</h2>
        <p>We use the details you send us only to answer your request and prepare your quote. We don't sell or share them.</p>
        <p>The consultation form on this website sends your request by email to our inbox; the website itself doesn't store it. If you choose WhatsApp instead, your request opens in your own WhatsApp app, ready to send. Messages then live in email or WhatsApp like any other conversation with us.</p>
        <p>This site uses cookie-free analytics to count visits. No advertising cookies are used.</p>
        <p>To ask us to delete your details, email <a href="mailto:hermeswraps@gmail.com">hermeswraps@gmail.com</a> or call <a href="tel:+18134751311">(813) 475-1311</a>.</p>
      </div>
    </section>

'''

nf_main = '''    <section class="section page-top" aria-labelledby="nfTitle">
      <div class="wrap prose">
        <img class="logo-plate" src="/assets/logo.jpg" alt="Hermes Wraps — Vinyl Specialists logo" width="96" height="96">
        <span class="eyebrow">404 · Page not found</span>
        <h1 id="nfTitle">This page isn't here.</h1>
        <p class="lead muted">The link may be old or mistyped. Here's where to go next.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="/book">Book a free consultation</a>
          <a class="text-link" href="/work">See our work <span class="arrow" aria-hidden="true">→</span></a>
        </div>
        <p class="reassure">Free · No obligation · We review your specs before quoting.</p>
      </div>
    </section>

'''

page('work.html', 'Our Work: Vehicle Wraps &amp; Commercial Graphics in Tampa Bay | Hermes Wraps',
     'Hermes Wraps projects in Tampa Bay, labeled by vehicle, finish and service: commercial graphics, partial wraps and color changes.',
     '/work', work_main, '  <script src="/assets/work.js" defer></script>')
page('terms.html', 'Terms of Service &amp; Privacy | Hermes Wraps',
     'Hermes Wraps terms of service: written quotes, deposits, vehicle condition, installation warranty, film care, timelines and privacy.',
     '/terms', terms_main)
page('404.html', 'Page Not Found | Hermes Wraps',
     'This page could not be found. Book a free consultation or see Hermes Wraps work.',
     '/404', nf_main)
