# 🧵 Needle & Craft — Interactive E-Commerce Platform

> A modern, standalone single-store e-commerce application built in **Python & Django** for merchants selling needles, threads, notions, and haberdashery. Packaged with **10 distinct production-ready front-end design samples** and a live interactive theme switcher so clients can choose and customize their brand aesthetic.

---

## 🌟 10 Distinct Front-End Sample Archetypes

Clients can preview and switch between all 10 sample designs on the fly using the persistent **Live Demo Theme Switcher** bar at the top of the storefront, or select their permanent default theme in the **Merchant Control Panel** (`/store-admin/`).

| # | Sample Theme | Focus & Niche | Color Palette | Key Design Highlights |
|---|---|---|---|---|
| **1** | **Atelier Couture** | Haute Couture, French silk floss, 24k gold tambour hooks | Velvet Obsidian (`#0B0D11`) & Brushed Gold (`#D4AF37`) | Editorial split hero, Playfair Display serif, gilded borders, gold foiled badges |
| **2** | **Wabi-Sabi Sashiko** | Japanese visible mending, indigo thread, palm thimbles | Rice Paper Ecru (`#F7F4EE`) & Japanese Indigo (`#1B3B6F`) | Zen asymmetrical banner with running stitch accents, dashed borders, terracotta stamps |
| **3** | **Modern Quilter Studio** | Contemporary sewing, machine needles, 50wt cotton | Living Coral (`#FF6B6B`), Fresh Seafoam Teal (`#2EC4B6`) | High-energy promotional studio hero, playful rounded cards, sale chips |
| **4** | **Heritage Leathercraft** | Heavy harness twine, sailmaker needles, cobbler awls | Burnished Cognac (`#8B4513`), Vintage Slate Steel (`#22252A`), Brass | Workbench hero, technical blueprint card styling, specification chips |
| **5** | **Botanical Dyehouse** | Plant-dyed wild silks, unbleached linen thread | Sage Leaf (`#4F772D`) & Madder Root Terracotta (`#BC4749`) | Soft organic curves, textured warm oat background, herbal divider motifs |
| **6** | **Nordic Wool & Crewel** | Scandinavian crewelwork, Gotland wool, hygge craft | Cloud Grey (`#F0F4F8`), Fjord Cobalt (`#2B4C7E`), Lingonberry | Ultra-clean Swiss minimalist layout, generous white space, borderless cards |
| **7** | **Victorian Haberdashery** | Antique needle cases, tatting shuttles, vintage lace | Royal Burgundy (`#581825`) & Antique Parchment (`#F4ECD8`) | Ornate 19th-century framed hero, double etched borders, Cinzel serif |
| **8** | **Neon Tuft & Punch** | Gen-Z modern fiber art, rug tufting, punch needles | Cyber Jet Dark (`#101118`) & Electric Neon Lime (`#B4F82C`) | Neo-brutalist hero, angular drop shadows, high-voltage kinetic typography |
| **9** | **Precision Micro-Needle** | High-speed industrial embroidery, ballistic nylon thread | Titanium Slate (`#0F172A`) & Electric Cyan (`#06B6D4`) | Technical schematic grid, machine RPM badges, gauge charts |
| **10** | **Boho Tapestry & Weft** | Macramé cotton cords, tapestry warp, weaving shuttles | Warm Ochre (`#D9822B`) & Dusty Desert Rose (`#B3545A`) | Sun-drenched warm textured hero, artisanal badges, relaxed boho feel |

---

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

### ⚙️ Merchant Control Panel (`/store-admin/`)
- Choose and lock the store's active default theme from all 10 samples.
- Edit store brand name, tagline, and announcement banner text.
- View incoming customer orders and update shipping fulfillment status.
- Real-time gross revenue and sales analytics.

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