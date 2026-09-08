# 🧵 Needle & Craft — Interactive E-Commerce Platform

> A modern, standalone single-store e-commerce application built in **Python & Django** for merchants selling needles, threads, notions, and haberdashery. Packaged with **10 distinct production-ready front-end design samples** and a live interactive theme switcher so clients can choose and customize their brand aesthetic.

---

## 🌟 16 Distinct Front-End Sample Archetypes & 4 Layout Systems

Clients can preview and switch between all 16 sample designs on the fly using the persistent **Live Demo Theme Switcher** bar at the top of the storefront, preview via clean canonical SEO URLs (e.g. `/demo/baroque/catalog/`), or select their permanent default theme in the **Merchant Control Panel** (`/store-admin/`) or Django admin (`/admin/`).

| # | Sample Theme | Focus & Niche | Layout Engine | Color Palette | Key Design Highlights |
|---|---|---|---|---|---|
| **1** | **Atelier Couture** | Haute Couture, French silk floss, 24k gold tambour hooks | **Boutique** | Velvet Obsidian (`#0B0D11`) & Brushed Gold (`#D4AF37`) | Editorial split hero, Playfair Display serif, gilded borders, gold foiled badges |
| **2** | **Wabi-Sabi Sashiko** | Japanese visible mending, indigo thread, palm thimbles | **Artisanal** | Rice Paper Ecru (`#F7F4EE`) & Japanese Indigo (`#1B3B6F`) | Zen asymmetrical banner with running stitch accents, dashed borders, terracotta stamps |
| **3** | **Modern Quilter Studio** | Contemporary sewing, machine needles, 50wt cotton | **Studio** | Living Coral (`#FF6B6B`), Fresh Seafoam Teal (`#2EC4B6`) | High-energy promotional studio hero, playful rounded cards, sale chips |
| **4** | **Heritage Leathercraft** | Heavy harness twine, sailmaker needles, cobbler awls | **Technical** | Burnished Cognac (`#8B4513`), Vintage Slate Steel (`#22252A`), Brass | Workbench hero, technical blueprint card styling, specification chips |
| **5** | **Botanical Dyehouse** | Plant-dyed wild silks, unbleached linen thread | **Artisanal** | Sage Leaf (`#4F772D`) & Madder Root Terracotta (`#BC4749`) | Soft organic curves, textured warm oat background, herbal divider motifs |
| **6** | **Nordic Wool & Crewel** | Scandinavian crewelwork, Gotland wool, hygge craft | **Studio** | Cloud Grey (`#F0F4F8`), Fjord Cobalt (`#2B4C7E`), Lingonberry | Ultra-clean Swiss minimalist layout, generous white space, borderless cards |
| **7** | **Victorian Haberdashery** | Antique needle cases, tatting shuttles, vintage lace | **Boutique** | Royal Burgundy (`#581825`) & Antique Parchment (`#F4ECD8`) | Ornate 19th-century framed hero, double etched borders, Cinzel serif |
| **8** | **Neon Tuft & Punch** | Gen-Z modern fiber art, rug tufting, punch needles | **Studio** | Cyber Jet Dark (`#101118`) & Electric Neon Lime (`#B4F82C`) | Neo-brutalist hero, angular drop shadows, high-voltage kinetic typography |
| **9** | **Precision Micro-Needle** | High-speed industrial embroidery, ballistic nylon thread | **Technical** | Titanium Slate (`#0F172A`) & Electric Cyan (`#06B6D4`) | Technical schematic grid, machine RPM badges, gauge charts |
| **10** | **Boho Tapestry & Weft** | Macramé cotton cords, tapestry warp, weaving shuttles | **Artisanal** | Warm Ochre (`#D9822B`) & Dusty Desert Rose (`#B3545A`) | Sun-drenched warm textured hero, artisanal badges, relaxed boho feel |
| **11** | **Baroque Goldwork** | Ecclesiastical vestment threads, passamenterie, metallic purl | **Boutique** | Midnight Obsidian (`#0A0612`), Imperial Gold (`#E6B800`), Royal Amethyst | Regal heraldic crest banner, filigree borders, illuminated manuscript styling |
| **12** | **Retro 70s Earth Weaver** | Macramé cord, burnt terracotta yarn, avocado crewel | **Artisanal** | Burnt Terracotta (`#C85A17`), Olive Gold (`#D4A017`), Avocado | Warm grooved psychedelic curves, 70s retro badges, earth-tone story cards |
| **13** | **Tactical Rigging & Mil-Spec** | Kevlar cords, bonded nylon V-69, titanium sailmaker needles | **Technical** | Tactical Drab (`#1B1E1B`), Cordura Olive (`#4B5320`), Safety Blaze Orange | Mil-Spec MIL-T-43435 HUD, tensile load meters (42 lbs test), ruggedized cards |
| **14** | **Kawaii Pastel Amigurumi** | Fluffy milk cotton, bent-tip tapestry needles, plush yarn | **Studio** | Blossom Pink (`#FFF0F5`), Sweet Lavender (`#E8D7FF`), Mint Cream | Squishy pill cards, sweet floating stickers, cute plush badge accents |
| **15** | **Dark Romantic Gothic** | Corsetry boning needles, blood-red silk floss, mourning lace | **Boutique** | Gothic Noir (`#0D0B10`), Crimson Rose (`#8B0000`), Burnished Pewter | Victorian velvet filigree, dramatic drop shadows, dark corsetry aesthetic |
| **16** | **Art Nouveau Stitched Lace** | Dragonfly motifs, Irish crochet hooks, flowing botanical lace | **Artisanal** | Sea Glass Sage (`#F2F7F4`), Whiplash Teal (`#1A535C`), Soft Gold | Sinuous organic curves, Mucha-inspired frames, botanical filigree |

---

## 📐 4 Distinct Catalog & Product Detail Layout Engines

Unlike typical themes that only change colors, each theme archetype dynamically switches between **4 structural layout engines** across both the Shop Catalog and Product Details views:

1. **Boutique Luxury (`layout-boutique`)**:
   - *Catalog*: Full-bleed luxury spotlight banners, curated editorial product cards with gold foiled borders and refined serif typography.
   - *Product Detail*: Magazine-style dual-column view, velvet swatch board, and antique heirloom accordion specifications.
2. **Studio Modern (`layout-studio`)**:
   - *Catalog*: Dynamic 4-column studio grid, category filter tabs, high-energy promotional ribbon with quick-dispatch highlights.
   - *Product Detail*: Clean studio showcase, interactive needle-to-thread pairing matrix, and quick-ship guarantee badge.
3. **Technical Precision (`layout-technical`)**:
   - *Catalog*: Industrial data-dense card strips, blueprint schematic headers, machine compatibility and ISO tolerance filters.
   - *Product Detail*: Technical blueprint specification card, live tensile strength gauge (42 lbs test rating), and high-speed machine RPM data.
4. **Artisanal Heritage (`layout-artisanal`)**:
   - *Catalog*: Asymmetrical 2-column storytelling cards, running-stitch dashed borders, and master artisan provenance markers.
   - *Product Detail*: Craft journey narrative, boro/visible mending instructions, and tactile plant-dyed material origin notes.

---

## 🔗 Clean Canonical SEO URL Routing

Say goodbye to messy query parameters (`?theme=...`). The platform features fully canonical SEO-optimized URL routing:

- **Demo Homepage**: `/demo/<theme_slug>/` (e.g. `/demo/baroque/`, `/demo/tactical/`)
- **Demo Catalog**: `/demo/<theme_slug>/catalog/`
- **Demo Category Filter**: `/demo/<theme_slug>/catalog/<category_slug>/` (e.g. `/demo/tactical/catalog/heavy-rigging-mil-spec-thread/`)
- **Demo Product Detail**: `/demo/<theme_slug>/product/<slug>/`
- **Standard Category SEO URLs**: `/catalog/<category_slug>/` (e.g. `/catalog/goldwork-ecclesiastical-threads/`)

## 🚀 Key Features

### 🎨 Live Theme Switcher Bar
- Sticky bar at the top of every page displaying theme number and color chips.
- Toggles CSS custom properties (`[data-theme="..."]`) instantaneously without page reload.
- Client selection is saved across sessions and query parameters (`?theme=<id>`).

### 🧵 Interactive Product Catalog & Search
- Live search filtering by title, description, and SKU.
- Category filter pills with product count indicators.
- "In Stock Only" toggle filter and multiple sort orders (Featured, Price: Low to High, Price: High to Low, Rating, Newest).

### 🔍 Product Details with Variant & Gauge Selectors
- **Color Swatch Selector**: Interactive clickable palette dots for thread spools with active ring highlight.
- **Needle Gauge Selector**: Interactive size options (e.g. Size 75/11 vs 90/14) with dynamic price updates.
- **Artisan Specifications Table**: Displays material, origin, tensile rating, and recommended fabrics.
- **Quantity Stepper**: Live +/- controls with instant price calculation.

### 🛍️ Slide-In Cart Drawer
- Animated slide-in drawer accessible from any page.
- AJAX-powered quantity adjustments (+/-) and instant item removal.
- Free shipping threshold tracker ($50 free delivery progress).
- Discount coupon code engine with real-time application.

### 💳 Express Checkout & Live Order Tracker
- Streamlined single-page checkout with contact and delivery forms.
- Simulated payment options: Credit Card, Cash on Delivery (COD), Direct Bank Transfer.
- Instant order creation with unique `#NT-XXXXXXXX` order number and `#TRK-XXXXXXXXXX` courier code.
- **4-Stage Live Order Stepper**: `Placed` → `Assembling` → `Dispatched` → `Delivered`.
- Printable order receipt.

### ⚙️ Merchant Control Panel (`/store-admin/`) & Django Admin (`/admin/`)
- Choose and lock the store's active default theme from all 16 samples.
- Edit store brand name, tagline, and announcement banner text.
- View incoming customer orders and update shipping fulfillment status.
- Real-time gross revenue and sales analytics.
- **Django Admin Superuser**:
  - URL: `http://127.0.0.1:8000/admin/`
  - Username: `admin`
  - Password: `admin123`

---

## 🛠️ Tech Stack

- **Backend**: Python 3.14, Django 6.1.1, SQLite3
- **Frontend**: Vanilla HTML5, Modern CSS3 with Custom Properties (CSS Tokens), Vanilla JavaScript (No heavy frameworks required)
- **Typography**: Google Fonts (`Playfair Display`, `Cinzel`, `Fraunces`, `Space Grotesk`, `Outfit`, `Plus Jakarta Sans`, `Syne`)

---

## ⚡ Quickstart Guide

### 1. Prerequisites
- Python 3.10+ installed
- Git installed

### 2. Setup Virtual Environment & Dependencies
```powershell
# Clone or navigate to the repository
cd needletravel

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 3. Run Database Migrations
```powershell
python manage.py migrate
```

### 4. Seed the Sample Catalog
Populate all 10 product categories, variants, coupons, and sample orders:
```powershell
python manage.py seed_catalog
```

### 5. Start the Local Server
```powershell
python manage.py runserver 8000
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser!

---

## 🧪 Running Automated Tests

Run the full Django test suite covering theme tokens, variant pricing, cart operations, coupons, checkout, and store admin:
```powershell
python manage.py test
```

---

## 🎟️ Demo Promo Codes

Test the cart drawer discount engine with these pre-seeded coupon codes:
- **`NEEDLE15`** — 15% OFF (Min. spend $30)
- **`SAVE10`** — 10% OFF (No min. spend)
- **`ARTISAN20`** — 20% OFF (Min. spend $60)

---

## 📂 Project Directory Structure

```text
needletravel/
├── config/                  # Django project configuration & settings
│   ├── settings.py          # App configuration, static/media paths, context processors
│   ├── urls.py              # Root URL routing
│   ├── wsgi.py
│   └── asgi.py
├── shop/                    # Core e-commerce application
│   ├── management/
│   │   └── commands/
│   │       └── seed_catalog.py  # Automated database seed command
│   ├── cart.py              # Session-based Cart manager
│   ├── context_processors.py# Injects 10 theme metadata and cart into all views
│   ├── models.py            # StoreConfig, Category, Product, Variant, Coupon, Order
│   ├── tests.py             # Full automated test suite
│   ├── urls.py              # Shop routing (home, catalog, product, cart API, checkout)
│   └── views.py             # View controllers and AJAX endpoints
├── static/
│   ├── css/
│   │   └── themes.css       # Complete design tokens and CSS for all 10 theme samples
│   └── js/
│       └── app.js           # Cart drawer, variant swatch selector, theme switcher
├── templates/
│   └── shop/
│       ├── base.html        # Main layout with live theme switcher bar & navigation
│       ├── home.html        # Dynamic hero sections for all 10 themes & featured grid
│       ├── catalog.html     # Instant search & category pill filtering
│       ├── product_detail.html # Swatch selector, gauge buttons, specs table
│       ├── cart_drawer.html # Slide-in cart drawer modal
│       ├── checkout.html    # Express checkout form & payment simulation
│       ├── order_success.html # Order receipt & 4-step live tracking stepper
│       └── store_admin.html # Merchant control panel & theme customizer
├── .gitignore               # Git ignore rules for Python, Django, and venv
├── requirements.txt         # Project dependencies
├── manage.py
└── README.md
```

---

## 📄 License
This project is open source and available under the MIT License.