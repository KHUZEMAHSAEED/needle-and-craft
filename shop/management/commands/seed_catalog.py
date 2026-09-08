from decimal import Decimal
from django.core.management.base import BaseCommand
from shop.models import StoreConfig, Category, Product, ProductVariant, Coupon, Order, OrderItem


class Command(BaseCommand):
    help = 'Seeds database with realistic needle & thread catalog spanning 10 front-end sample themes'

    def handle(self, *args, **options):
        self.stdout.write("Starting needle & thread catalog seed...")

        # 1. Store Config
        config = StoreConfig.get_solo()
        config.store_name = "Fil & Pointe Haberdashery"
        config.tagline = "Fine Artisan Threads, Hand-Forged Needles & Haute Notions"
        config.announcement_text = "✨ Atelier Spring Release: Enjoy 15% off orders over $40 with code NEEDLE15 | Complimentary worldwide courier"
        config.active_theme = "couture"
        config.save()

        # 2. Categories
        categories_data = [
            {
                'name': 'Haute Couture & Silk',
                'slug': 'couture-silk',
                'icon': '🧵',
                'description': 'Pure mulberry silk threads, metallic bouillon wires, and French tambour embroidery needles.',
                'order': 1,
            },
            {
                'name': 'Sashiko & Visible Mending',
                'slug': 'sashiko-mending',
                'icon': '🪡',
                'description': 'Heavy Japanese indigo-dyed cotton skeins, tempered steel mending needles, and palm thimbles.',
                'order': 2,
            },
            {
                'name': 'Quilting & Precision Sewing',
                'slug': 'quilting-notions',
                'icon': '📐',
                'description': 'Titanium-coated machine quilting needles, 50wt Egyptian cotton spools, and precision cutting tools.',
                'order': 3,
            },
            {
                'name': 'Leathercraft & Heavy Twine',
                'slug': 'leather-rigging',
                'icon': '🔨',
                'description': 'Waxed braided sailmaker twine, harness needles size 00, and hand-ground diamond cobbler awls.',
                'order': 4,
            },
            {
                'name': 'Botanical & Naturally Dyed',
                'slug': 'botanical-fibers',
                'icon': '🌿',
                'description': 'Madder root, indigo, and walnut hull plant-dyed organic silks and Belgian unbleached linen thread.',
                'order': 5,
            },
            {
                'name': 'Nordic Wool & Crewel',
                'slug': 'nordic-wool',
                'icon': '🧶',
                'description': '100% Scandinavian organic crewelwork wool, blunt tapestry needles, and Swedish linen twill.',
                'order': 6,
            },
            {
                'name': 'Victorian Antiques & Notions',
                'slug': 'victorian-notions',
                'icon': '🗝️',
                'description': 'Antique brass chatelaine needle cases, bone tatting shuttles, and gold filigree stork scissors.',
                'order': 7,
            },
            {
                'name': 'Tufting & Modern Punch Needle',
                'slug': 'punch-needle',
                'icon': '⚡',
                'description': 'Ergonomic wooden Oxford punch needles, chunky rug tufting yarn spools, and monk cloth canvas.',
                'order': 8,
            },
            {
                'name': 'Industrial & Micro-Engineering',
                'slug': 'industrial-precision',
                'icon': '⚙️',
                'description': 'Groz-Beckert industrial DBx1 machine needles, bonded nylon 69, and Kevlar high-tensile threads.',
                'order': 9,
            },
            {
                'name': 'Boho Tapestry & Macramé',
                'slug': 'boho-weaving',
                'icon': '☀️',
                'description': 'Natural 4mm combed macramé cord, warped tapestry warp thread, and hand-carved maple shuttles.',
                'order': 10,
            },
            {
                'name': 'Baroque Goldwork & Liturgical',
                'slug': 'baroque-goldwork',
                'icon': '👑',
                'description': 'Real silver-gilt passing threads, gold bullion purl wires, and liturgical vestment needles.',
                'order': 11,
            },
            {
                'name': 'Retro 70s Earth Weaver',
                'slug': 'retro-earth',
                'icon': '🌻',
                'description': 'Rough golden jute twine, raw unbleached hemp cordage, and vintage turned hardwood beads.',
                'order': 12,
            },
            {
                'name': 'Tactical Rigging & Mil-Spec',
                'slug': 'tactical-milspec',
                'icon': '🛡️',
                'description': 'Bonded Kevlar 92 high-tensile threads, field repair awls, and heavy ballistic webbing needles.',
                'order': 13,
            },
            {
                'name': 'Kawaii Pastel Amigurumi',
                'slug': 'kawaii-plush',
                'icon': '🌸',
                'description': 'Soft-touch pastel ergonomic hooks, milk cotton fluff yarn, and safety locking stitch markers.',
                'order': 14,
            },
            {
                'name': 'Dark Romantic Corsetry',
                'slug': 'gothic-corsetry',
                'icon': '🥀',
                'description': 'Heavy-duty steel boning needles, ultra-waxed corset lacing twine, and midnight velvet floss.',
                'order': 15,
            },
            {
                'name': 'Art Nouveau Stitched Lace',
                'slug': 'art-nouveau',
                'icon': '🦚',
                'description': 'Mucha-inspired peacock green silks, sterling filigree tatting shuttles, and picot lace needles.',
                'order': 16,
            },
        ]

        cat_map = {}
        for cdata in categories_data:
            cat, _ = Category.objects.update_or_create(
                slug=cdata['slug'],
                defaults=cdata
            )
            cat_map[cdata['slug']] = cat

        # 3. Products
        products_data = [
            # 1. Couture
            {
                'category': cat_map['couture-silk'],
                'title': "Soie d'Or 100% Pure French Silk Floss Skein",
                'slug': 'soie-dor-pure-french-silk-floss',
                'short_description': "Lustrous 7-strand divisible filament silk spun in Lyon, ideal for goldwork and haute couture embroidery.",
                'description': "Crafted in historic workshops near Lyon, Soie d'Or is renowned among Paris ateliers for its unmatched sheen, tensile purity, and resistance to fraying. Divisible into 7 micro-strands, it glides through fine organza and velvet like liquid light.",
                'base_price': Decimal('18.50'),
                'compare_price': Decimal('24.00'),
                'image_url': 'https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?auto=format&fit=crop&w=800&q=80',
                'badge': 'Haute Atelier Choice',
                'in_stock': True,
                'sku': 'COUT-SILK-001',
                'rating': Decimal('5.0'),
                'reviews_count': 64,
                'specs': {
                    'Material': '100% Mulberry Filament Silk',
                    'Length': '25 meters (27.3 yds)',
                    'Origin': 'Lyon, France',
                    'Recommended Needle': 'Couture Hand Embroidery Size 9/10',
                },
                'theme_niche': 'couture',
                'is_featured': True,
                'variants': [
                    {'name': 'Champagne Gold (Dore)', 'color_hex': '#D4AF37', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Imperial Obsidian Black', 'color_hex': '#1A1A1A', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': 'Royal Garnet Crimson', 'color_hex': '#7A0019', 'price_adjustment': Decimal('1.50'), 'stock': 20},
                    {'name': 'Opalescent Ivory', 'color_hex': '#FDFBF7', 'price_adjustment': Decimal('0.00'), 'stock': 50},
                ]
            },
            {
                'category': cat_map['couture-silk'],
                'title': '24K Gold-Plated Tambour Hook & Luneville Needle Set',
                'slug': 'gold-plated-tambour-luneville-needle-set',
                'short_description': 'Precision French beading tambour hook with interchangeable hardened micro-needles #70, #80, and #90.',
                'description': 'Master the exquisite art of Lunéville embroidery with our heirloom 24k gold-plated brass tambour handle. Ergonomically weighted for effortless chain-stitching and bead application on delicate tulle and silk gazar.',
                'base_price': Decimal('48.00'),
                'compare_price': Decimal('58.00'),
                'image_url': 'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=800&q=80',
                'badge': 'Limited Edition',
                'in_stock': True,
                'sku': 'COUT-NEEDLE-002',
                'rating': Decimal('4.9'),
                'reviews_count': 42,
                'specs': {
                    'Handle Material': '24K Gold Plated Brass & Rosewood',
                    'Needle Sizes': '#70 (Ultra-fine), #80 (Standard), #90 (Heavy Bead)',
                    'Length': '11.5 cm',
                    'Origin': 'Paris, France',
                },
                'theme_niche': 'couture',
                'is_featured': True,
                'variants': [
                    {'name': 'Classic Trio Set (#70, #80, #90)', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                    {'name': 'Master Guild Set (Trio + 5 Extra Needles)', 'price_adjustment': Decimal('14.00'), 'stock': 15},
                ]
            },

            # 2. Sashiko
            {
                'category': cat_map['sashiko-mending'],
                'title': 'Olympus Authentic Heavy Indigo Sashiko Cotton Spool (100m)',
                'slug': 'olympus-heavy-indigo-sashiko-cotton-spool',
                'short_description': 'Unmercerized, tightly spun matte Japanese cotton thread for visible mending, boro repair, and geometric stitching.',
                'description': 'Produced in Japan using non-mercerized long-staple cotton, this authentic sashiko thread creates the signature raised stitch tactile relief. Deeply dyed in rich indigo tones that soften and gain unique patina with time and washing.',
                'base_price': Decimal('11.50'),
                'compare_price': Decimal('14.00'),
                'image_url': 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80',
                'badge': 'Traditional Wabi-Sabi',
                'in_stock': True,
                'sku': 'SASH-THREAD-001',
                'rating': Decimal('4.9'),
                'reviews_count': 53,
                'specs': {
                    'Material': '100% Unmercerized Japanese Cotton',
                    'Length': '100 meters (109 yds)',
                    'Weight': 'Heavyweight (6-ply tight twist)',
                    'Origin': 'Nagano, Japan',
                },
                'theme_niche': 'sashiko',
                'is_featured': True,
                'variants': [
                    {'name': 'Deep Midnight Indigo', 'color_hex': '#1B3B6F', 'price_adjustment': Decimal('0.00'), 'stock': 45},
                    {'name': 'Washed Chambray Blue', 'color_hex': '#4A7C9D', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                    {'name': 'Natural Ecru Unbleached', 'color_hex': '#F2EBD9', 'price_adjustment': Decimal('0.00'), 'stock': 60},
                    {'name': 'Persimmon Terracotta', 'color_hex': '#C85A32', 'price_adjustment': Decimal('1.00'), 'stock': 25},
                ]
            },
            {
                'category': cat_map['sashiko-mending'],
                'title': 'Hiroshima Hand-Polished Sashiko Needles & Palm Thimble Kit',
                'slug': 'hiroshima-sashiko-needles-palm-thimble-kit',
                'short_description': 'Set of 6 high-carbon tempered steel needles made in Hiroshima with authentic adjustable leather palm thimble.',
                'description': 'Hiroshima needles undergo more than 30 artisanal manufacturing steps, resulting in microscopic lengthwise polish lines that minimize resistance through multi-layered denim and linen. Includes an adjustable cowhide palm thimble for unibody rhythmic stitching.',
                'base_price': Decimal('22.00'),
                'compare_price': Decimal('28.00'),
                'image_url': 'https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?auto=format&fit=crop&w=800&q=80',
                'badge': 'Artisan Forged',
                'in_stock': True,
                'sku': 'SASH-NEEDLE-002',
                'rating': Decimal('5.0'),
                'reviews_count': 78,
                'specs': {
                    'Material': 'High-Carbon Tempered Spring Steel',
                    'Pack Quantity': '6 needles (3 Long 65mm + 3 Short 48mm)',
                    'Thimble': 'Natural vegetable tanned leather with brass coin',
                    'Origin': 'Hiroshima, Japan',
                },
                'theme_niche': 'sashiko',
                'is_featured': True,
                'variants': [
                    {'name': 'Standard Kit (6 Needles + Leather Thimble)', 'price_adjustment': Decimal('0.00'), 'stock': 50},
                    {'name': 'Deluxe Set (+ Japanese Boro Fabric Bundle)', 'price_adjustment': Decimal('16.00'), 'stock': 20},
                ]
            },

            # 3. Quilter
            {
                'category': cat_map['quilting-notions'],
                'title': 'Schmetz Titanium-Coated Quilting Machine Needles (Pack of 10)',
                'slug': 'schmetz-titanium-quilting-machine-needles',
                'short_description': 'Titanium Nitride (TiN) coating extends needle life by 5x, reducing heat buildup through batting and dense piecing.',
                'description': 'Engineered specifically for machine piecing and free-motion quilting, the slightly rounded special taper point easily penetrates dense woven cotton without needle deflection or skipped stitches.',
                'base_price': Decimal('16.90'),
                'compare_price': Decimal('21.50'),
                'image_url': 'https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?auto=format&fit=crop&w=800&q=80',
                'badge': 'Top Rated Quilting',
                'in_stock': True,
                'sku': 'QUILT-NEEDLE-001',
                'rating': Decimal('4.9'),
                'reviews_count': 92,
                'specs': {
                    'Coating': 'Titanium Nitride Golden Hard-Coat',
                    'System': '130/705 H-Q',
                    'Compatibility': 'Universal Home Sewing & Quilting Machines',
                    'Origin': 'Germany',
                },
                'theme_niche': 'quilter',
                'is_featured': True,
                'variants': [
                    {'name': 'Assorted Sizes 75/11 & 90/14', 'price_adjustment': Decimal('0.00'), 'stock': 65},
                    {'name': 'Size 75/11 (Fine Cotton Piecing)', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Size 90/14 (Heavy Batting & Free-Motion)', 'price_adjustment': Decimal('0.00'), 'stock': 55},
                ]
            },
            {
                'category': cat_map['quilting-notions'],
                'title': 'Aurifil Mako 50wt Egyptian Long-Staple Cotton Spool (1300m)',
                'slug': 'aurifil-mako-50wt-cotton-spool',
                'short_description': 'The gold standard for modern quilters: ultra-low lint, high tensile strength, and virtually flat seam allowances.',
                'description': 'Produced from 100% Long Staple Egyptian Cotton in Milan, Italy. Mercerized to perfection, Aurifil 50wt is celebrated worldwide for crisp, flat patchwork seams and flawless free-motion quilting.',
                'base_price': Decimal('14.95'),
                'compare_price': Decimal('18.00'),
                'image_url': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff?auto=format&fit=crop&w=800&q=80',
                'badge': 'Quilter Essential',
                'in_stock': True,
                'sku': 'QUILT-THREAD-002',
                'rating': Decimal('4.9'),
                'reviews_count': 110,
                'specs': {
                    'Fiber': '100% Giza Long-Staple Egyptian Cotton',
                    'Weight': '50wt (2-ply)',
                    'Length': '1,300 meters (1,422 yds)',
                    'Origin': 'Milan, Italy',
                },
                'theme_niche': 'quilter',
                'is_featured': True,
                'variants': [
                    {'name': 'Coral Living', 'color_hex': '#FF6B6B', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': 'Seafoam Teal', 'color_hex': '#2EC4B6', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Dove White #2024', 'color_hex': '#FFFFFF', 'price_adjustment': Decimal('0.00'), 'stock': 80},
                    {'name': 'Soft Charcoal Slate #2605', 'color_hex': '#4A4E69', 'price_adjustment': Decimal('0.00'), 'stock': 45},
                ]
            },

            # 4. Leathercraft
            {
                'category': cat_map['leather-rigging'],
                'title': 'Barbour Braided Waxed Linen Cord 5-Cord Spool',
                'slug': 'barbour-braided-waxed-linen-cord',
                'short_description': 'Traditional Irish wet-spun flax thread with pure beeswax impregnation for saddle-stitching and heavy leatherwork.',
                'description': 'Trusted by master saddlers, bootmakers, and sailmakers for over a century. The heavy beeswax coating locks stitches permanently into awl holes and shields fiber against moisture, salt water, and abrasive tension.',
                'base_price': Decimal('24.50'),
                'compare_price': Decimal('32.00'),
                'image_url': 'https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=800&q=80',
                'badge': 'Heavy Duty Artisan',
                'in_stock': True,
                'sku': 'LEATH-CORD-001',
                'rating': Decimal('4.9'),
                'reviews_count': 49,
                'specs': {
                    'Material': '100% Wet-Spun Irish Flax with Natural Beeswax',
                    'Cord Size': '5-Cord (0.85mm diameter)',
                    'Tensile Strength': '42 lbs test',
                    'Origin': 'Northern Ireland',
                },
                'theme_niche': 'leathercraft',
                'is_featured': True,
                'variants': [
                    {'name': 'Cognac Havana Brown', 'color_hex': '#8B4513', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                    {'name': 'Coal Black', 'color_hex': '#1B1B1B', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Natural Honey Wax', 'color_hex': '#E9C46A', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                ]
            },
            {
                'category': cat_map['leather-rigging'],
                'title': 'John James English Harness Needles (Size 000 / Size 00)',
                'slug': 'john-james-english-harness-needles',
                'short_description': 'Round blunt point needles forged from high-tensile carbon steel, designed specifically not to split leather fibers.',
                'description': 'Manufactured in Redditch, Worcestershire—the traditional needle-making capital of England. The rounded blunt point glides smoothly through pre-punched awl holes without piercing or fraying the companion thread during saddle stitching.',
                'base_price': Decimal('12.50'),
                'compare_price': Decimal('16.00'),
                'image_url': 'https://images.unsplash.com/photo-1509281373149-e957c6296406?auto=format&fit=crop&w=800&q=80',
                'badge': 'Redditch English Steel',
                'in_stock': True,
                'sku': 'LEATH-NEEDLE-002',
                'rating': Decimal('5.0'),
                'reviews_count': 61,
                'specs': {
                    'Steel Type': 'Hardened Carbon Spring Steel',
                    'Tip': 'Blunt Round Point for Saddle Stitching',
                    'Pack Size': 'Pack of 25 Needles',
                    'Origin': 'Redditch, England',
                },
                'theme_niche': 'leathercraft',
                'is_featured': True,
                'variants': [
                    {'name': 'Size 00 (Heavy Holsters & Saddles)', 'price_adjustment': Decimal('0.00'), 'stock': 45},
                    {'name': 'Size 000 (Wallets & Watch Straps)', 'price_adjustment': Decimal('0.00'), 'stock': 50},
                ]
            },

            # 5. Botanical
            {
                'category': cat_map['botanical-fibers'],
                'title': 'Plant-Dyed Wild Tussah Silk Skein Bundle (Set of 4)',
                'slug': 'plant-dyed-wild-tussah-silk-bundle',
                'short_description': 'Dyed by hand using madder root, indigo, marigold flowers, and black walnut husks with zero synthetic mordants.',
                'description': 'Each skein is naturally kettle-dyed in small artisan batches in Vermont. The unrefined wild Tussah silk offers organic texture, subtle earth tones, and a gentle woodsy scent.',
                'base_price': Decimal('36.00'),
                'compare_price': Decimal('44.00'),
                'image_url': 'https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80',
                'badge': '100% Botanical Dye',
                'in_stock': True,
                'sku': 'BOTA-SILK-001',
                'rating': Decimal('4.9'),
                'reviews_count': 38,
                'specs': {
                    'Dye Sources': 'Madder Root, Japanese Indigo, Marigold, Walnut',
                    'Fiber': 'Non-Violent Wild Tussah Peace Silk',
                    'Total Length': '80 meters across 4 skeins',
                    'Origin': 'Vermont, USA',
                },
                'theme_niche': 'botanical',
                'is_featured': True,
                'variants': [
                    {'name': 'Autumn Forest Palette (Madder, Sage, Rust, Sand)', 'price_adjustment': Decimal('0.00'), 'stock': 20},
                    {'name': 'Spring Flora Palette (Indigo, Blush, Olive, Clay)', 'price_adjustment': Decimal('0.00'), 'stock': 18},
                ]
            },

            # 6. Nordic Wool
            {
                'category': cat_map['nordic-wool'],
                'title': 'ScanFil Nordic Organic Crewelwork Wool Skeins (2-Ply)',
                'slug': 'scanfil-nordic-crewelwork-wool-skeins',
                'short_description': 'Spun from virgin Scandinavian sheep fleece, providing rich loft, matte visual warmth, and exceptional longevity.',
                'description': 'Designed for Swedish embroidery, traditional folk motifs, and textured knit mending. The 2-ply twist ensures consistent stitch definition without flattening over time.',
                'base_price': Decimal('15.50'),
                'compare_price': Decimal('19.00'),
                'image_url': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff?auto=format&fit=crop&w=800&q=80',
                'badge': 'Nordic Pure Fleece',
                'in_stock': True,
                'sku': 'NORD-WOOL-001',
                'rating': Decimal('4.8'),
                'reviews_count': 29,
                'specs': {
                    'Composition': '100% Scandinavian Virgin Wool',
                    'Skein Length': '25 meters',
                    'Weight': 'Crewel 2-Ply',
                    'Origin': 'Gotland, Sweden',
                },
                'theme_niche': 'nordic',
                'is_featured': False,
                'variants': [
                    {'name': 'Fjord Cobalt Blue', 'color_hex': '#2B4C7E', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': 'Lingonberry Red', 'color_hex': '#D64550', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                    {'name': 'Cloud Heather Grey', 'color_hex': '#A0AAB2', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                ]
            },

            # 7. Victorian
            {
                'category': cat_map['victorian-notions'],
                'title': 'Victorian Filigree Chatelaine Needle Case & Stork Shears Set',
                'slug': 'victorian-filigree-needle-case-stork-shears',
                'short_description': 'Replica 1880s antique brass chatelaine case with airtight friction cap and hand-tuned precision embroidery scissors.',
                'description': 'Cast from authentic 19th-century Victorian jeweler dies, this ornate brass needle case protects hand-sewing needles with antique charm. Paired with razor-sharp stork embroidery shears with fine needlepoint tips.',
                'base_price': Decimal('38.00'),
                'compare_price': Decimal('48.00'),
                'image_url': 'https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=800&q=80',
                'badge': 'Antique Parlor Replica',
                'in_stock': True,
                'sku': 'VICT-NOTION-001',
                'rating': Decimal('4.9'),
                'reviews_count': 55,
                'specs': {
                    'Material': 'Antique Brushed Brass & Forged Steel',
                    'Case Length': '9 cm (Accommodates needles up to 75mm)',
                    'Shears Length': '11.5 cm with hand-ground blade',
                    'Origin': 'Sheffield, England',
                },
                'theme_niche': 'victorian',
                'is_featured': True,
                'variants': [
                    {'name': 'Antique Burnished Brass', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                    {'name': 'Silver Patina Pewter Finish', 'price_adjustment': Decimal('3.00'), 'stock': 15},
                ]
            },

            # 8. Neon Tuft
            {
                'category': cat_map['punch-needle'],
                'title': 'Oxford Ergonomic Maple Punch Needle (#10 Regular)',
                'slug': 'oxford-ergonomic-punch-needle-10',
                'short_description': 'The premier wooden punch needle for rug tufting, fiber wall hangings, and chunky contemporary punch art.',
                'description': 'Crafted in Vermont with a turned solid American maple handle and electropolished stainless steel needle tube. Creates even, plush 1/4" yarn loops effortlessly through monk cloth without cramping wrists.',
                'base_price': Decimal('34.00'),
                'compare_price': Decimal('40.00'),
                'image_url': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
                'badge': 'Fiber Art Favorite',
                'in_stock': True,
                'sku': 'TUFT-PUNCH-001',
                'rating': Decimal('5.0'),
                'reviews_count': 84,
                'specs': {
                    'Handle': 'Turned Hard American Maple',
                    'Loop Height': '1/4 inch (6.3mm)',
                    'Yarn Weight': 'Heavy Worsted, Bulky Rug Yarn, Strips',
                    'Origin': 'Vermont, USA',
                },
                'theme_niche': 'neontuft',
                'is_featured': True,
                'variants': [
                    {'name': '#10 Regular (Heavy Rug Yarn)', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': '#14 Fine (Worsted & Floss)', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                ]
            },

            # 9. Precision Industrial
            {
                'category': cat_map['industrial-precision'],
                'title': 'Groz-Beckert Titanium DBx1 Industrial Needles (Box of 50)',
                'slug': 'groz-beckert-titanium-dbx1-needles-50',
                'short_description': 'GEBEDUR titanium nitride coated needles rated for up to 6,000 stitches/min on automated commercial machines.',
                'description': 'Manufactured in Germany with ultra-precise eye geometry and GEBEDUR titanium coating that prevents deflection, skip-stitching, and needle breakage when sewing heavy canvas, automotive upholstery, and technical outerwear.',
                'base_price': Decimal('29.50'),
                'compare_price': Decimal('38.00'),
                'image_url': 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80',
                'badge': 'Commercial High-Speed',
                'in_stock': True,
                'sku': 'PREC-INDUS-001',
                'rating': Decimal('4.9'),
                'reviews_count': 67,
                'specs': {
                    'Shank Type': 'Round Shank (DBx1 / 16x231 / 287WH)',
                    'Coating': 'GEBEDUR Titanium Nitride (Gold)',
                    'Speed Rating': 'Up to 6,000 SPM',
                    'Origin': 'Albstadt, Germany',
                },
                'theme_niche': 'precision',
                'is_featured': True,
                'variants': [
                    {'name': 'Size 90/14 (General Industrial)', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Size 110/18 (Heavy Canvas & Upholstery)', 'price_adjustment': Decimal('2.00'), 'stock': 30},
                    {'name': 'Size 130/21 (Extra Heavy Cordura)', 'price_adjustment': Decimal('4.00'), 'stock': 25},
                ]
            },

            # 10. Boho Tapestry
            {
                'category': cat_map['boho-weaving'],
                'title': 'Artisan 4mm Single Strand Organic Cotton Macramé Rope (250m)',
                'slug': 'artisan-4mm-organic-cotton-macrame-rope',
                'short_description': 'Zero chemical bleaching, buttery soft single-twist combed cotton rope for fringed wall hangings and fiber tapestries.',
                'description': 'Spun from virgin unbleached Turkish cotton fibers, this 4mm single-twist cord brushes out into ultra-fluffy feathery tassels effortlessly while retaining strong tensile structure for intricate knotting.',
                'base_price': Decimal('21.00'),
                'compare_price': Decimal('27.00'),
                'image_url': 'https://images.unsplash.com/photo-1590736969955-71cc94801759?auto=format&fit=crop&w=800&q=80',
                'badge': 'Natural Bohemian',
                'in_stock': True,
                'sku': 'BOHO-CORD-001',
                'rating': Decimal('4.9'),
                'reviews_count': 44,
                'specs': {
                    'Diameter': '4.0 mm',
                    'Length': '250 meters (820 ft / ~1.1 kg spool)',
                    'Twist': 'Single Strand Combed Rope',
                    'Origin': 'Izmir, Turkey',
                },
                'theme_niche': 'boho',
                'is_featured': True,
                'variants': [
                    {'name': 'Warm Natural Cream', 'color_hex': '#F7EFE3', 'price_adjustment': Decimal('0.00'), 'stock': 45},
                    {'name': 'Sunbaked Ochre Mustard', 'color_hex': '#D9822B', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                    {'name': 'Dusty Desert Rose', 'color_hex': '#B3545A', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                ]
            },

            # 11. Baroque Goldwork
            {
                'category': cat_map['baroque-goldwork'],
                'title': 'Real Silver-Gilt Passing Thread & Gold Bullion Purl Skein',
                'slug': 'real-silver-gilt-passing-thread-gold-bullion',
                'short_description': 'Authentic metallic thread wound over silk core for sacred liturgical vestments and royal heraldry embroidery.',
                'description': 'Handcrafted using centuries-old techniques. Real silver-gilt foil is wound in a continuous microscopic helix over a yellow silk core, creating blinding radiance without tarnishing.',
                'base_price': Decimal('42.00'),
                'compare_price': Decimal('55.00'),
                'image_url': 'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=800&q=80',
                'badge': 'Ecclesiastical Guild',
                'in_stock': True,
                'sku': 'BARO-GOLD-001',
                'rating': Decimal('5.0'),
                'reviews_count': 33,
                'specs': {
                    'Foil Composition': '2% Silver-Gilt on Pure Silk Core',
                    'Length': '20 meters',
                    'Origin': 'Lyon & Florence',
                },
                'theme_niche': 'baroque',
                'is_featured': True,
                'variants': [
                    {'name': 'Imperial Gold Passing #4', 'color_hex': '#C5A059', 'price_adjustment': Decimal('0.00'), 'stock': 20},
                    {'name': 'Bright Silver Gilt #4', 'color_hex': '#E0E0E0', 'price_adjustment': Decimal('0.00'), 'stock': 15},
                ]
            },

            # 12. Retro 70s
            {
                'category': cat_map['retro-earth'],
                'title': 'Raw Golden Jute Craft Twine & Turned Hardwood Bead Set',
                'slug': 'raw-golden-jute-craft-twine-hardwood-bead-set',
                'short_description': '3-ply natural unrefined jute cord paired with 50 hand-turned walnut beads for retro macramé wall hangings.',
                'description': 'A love letter to 1970s fiber arts. The golden jute fiber is completely unprocessed, offering that rustic earthy scent, textured hand-feel, and robust knot holding power.',
                'base_price': Decimal('19.50'),
                'compare_price': Decimal('25.00'),
                'image_url': 'https://images.unsplash.com/photo-1590736969955-71cc94801759?auto=format&fit=crop&w=800&q=80',
                'badge': '70s Earth Revival',
                'in_stock': True,
                'sku': 'RETR-JUTE-001',
                'rating': Decimal('4.8'),
                'reviews_count': 41,
                'specs': {
                    'Material': '100% Golden Bengal Jute',
                    'Length': '150 meters (492 ft)',
                    'Origin': 'Bengal / Vermont',
                },
                'theme_niche': 'retro70s',
                'is_featured': True,
                'variants': [
                    {'name': 'Raw Natural Golden Jute', 'color_hex': '#E1AD01', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': 'Rust Terracotta Dip', 'color_hex': '#B84A39', 'price_adjustment': Decimal('2.00'), 'stock': 25},
                ]
            },

            # 13. Tactical Rigging
            {
                'category': cat_map['tactical-milspec'],
                'title': 'Bonded Kevlar 92 High-Tensile Rigging Thread & Diamond Awl',
                'slug': 'bonded-kevlar-92-rigging-thread-diamond-awl',
                'short_description': 'Commercial Mil-Spec DuPont Kevlar thread with 50 lbs break test strength and high-carbon ground diamond point awl.',
                'description': 'Engineered for extreme duty: military webbing, ballistic nylon packs, paraglider rigging, and mountaineering harness repairs. Impervious to rot, saltwater, and temperatures up to 800°F.',
                'base_price': Decimal('32.00'),
                'compare_price': Decimal('40.00'),
                'image_url': 'https://images.unsplash.com/photo-1509281373149-e957c6296406?auto=format&fit=crop&w=800&q=80',
                'badge': 'Mil-Spec Extreme Tensile',
                'in_stock': True,
                'sku': 'TACT-KEVL-001',
                'rating': Decimal('5.0'),
                'reviews_count': 58,
                'specs': {
                    'Fiber': '100% Virgin DuPont Kevlar',
                    'Tensile Test': '50 lbs Break Strength',
                    'Temperature Rating': 'Heat resistant to 800°F',
                    'Origin': 'USA',
                },
                'theme_niche': 'tactical',
                'is_featured': True,
                'variants': [
                    {'name': 'Coyote Brown (Size 92)', 'color_hex': '#9A7B4F', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Tactical Matte Black', 'color_hex': '#1C1F22', 'price_adjustment': Decimal('0.00'), 'stock': 45},
                    {'name': 'Ranger Green (OD)', 'color_hex': '#4B5320', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                ]
            },

            # 14. Kawaii Amigurumi
            {
                'category': cat_map['kawaii-plush'],
                'title': 'Pastel Ergonomic Soft-Grip Hook & 5-Ply Milk Cotton Fluff Set',
                'slug': 'pastel-ergonomic-hook-milk-cotton-fluff-set',
                'short_description': 'Buttery smooth aluminum hook with pastel silicone ergonomic grip and 4 skeins of anti-pilling milk cotton.',
                'description': 'Craft plush amigurumi bunnies, cats, and cute keychains effortlessly. The gentle ergonomic grip cushions the palm, while the combed milk cotton glides with zero splitting.',
                'base_price': Decimal('22.50'),
                'compare_price': Decimal('28.00'),
                'image_url': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff?auto=format&fit=crop&w=800&q=80',
                'badge': 'Kawaii Cute Favorite',
                'in_stock': True,
                'sku': 'KAWA-HOOK-001',
                'rating': Decimal('4.9'),
                'reviews_count': 72,
                'specs': {
                    'Hook Material': 'Lightweight Anodized Aluminum with Pastel Silicone Handle',
                    'Yarn Composition': '80% Combed Cotton, 20% Milk Fiber',
                    'Origin': 'Japan / Korea',
                },
                'theme_niche': 'kawaii',
                'is_featured': True,
                'variants': [
                    {'name': 'Baby Blossom Set (Pink, Lavender, Mint, Cream)', 'price_adjustment': Decimal('0.00'), 'stock': 40},
                    {'name': 'Ocean Sweets Set (Sky Blue, Seafoam, Coral, Vanilla)', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                ]
            },

            # 15. Dark Gothic Corsetry
            {
                'category': cat_map['gothic-corsetry'],
                'title': 'Heavy Waxed Corset Lacing Cord & Spring Steel Boning Needles',
                'slug': 'heavy-waxed-corset-lacing-boning-needles',
                'short_description': 'High-density braided tubular corsetry cord with reinforced metal aglets and blunt curved boning channel needles.',
                'description': 'Designed specifically for tight-lacing historical corsets, stays, and dark romantic evening gowns. Won’t roll, snap, or stretch under extreme cinch tension.',
                'base_price': Decimal('26.00'),
                'compare_price': Decimal('34.00'),
                'image_url': 'https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?auto=format&fit=crop&w=800&q=80',
                'badge': 'Dark Romance Atelier',
                'in_stock': True,
                'sku': 'GOTH-CORSET-001',
                'rating': Decimal('5.0'),
                'reviews_count': 39,
                'specs': {
                    'Cord Type': 'High-Density Waxed Tubular Braided Poly-Flax',
                    'Length': '8 meters (with solid brass aglets)',
                    'Origin': 'Sheffield, England',
                },
                'theme_niche': 'gothic',
                'is_featured': True,
                'variants': [
                    {'name': 'Midnight Raven Black', 'color_hex': '#0D080C', 'price_adjustment': Decimal('0.00'), 'stock': 35},
                    {'name': 'Blood Crimson Wine', 'color_hex': '#9B1B30', 'price_adjustment': Decimal('1.50'), 'stock': 25},
                ]
            },

            # 16. Art Nouveau
            {
                'category': cat_map['art-nouveau'],
                'title': 'Alphonse Peacock Filigree Silk & Sterling Lace Tatting Shuttle',
                'slug': 'alphonse-peacock-filigree-silk-tatting-shuttle',
                'short_description': 'Inspired by Mucha whip-lash motifs: high-sheen peacock gradient silk floss with etched vintage tatting shuttle.',
                'description': 'Echoing the flowing organic curves of 1900s Paris. The iridescent peacock silk floss shifts between emerald, teal, and bronze in natural light, making delicate lace collars and picot motifs sing.',
                'base_price': Decimal('35.00'),
                'compare_price': Decimal('44.00'),
                'image_url': 'https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80',
                'badge': 'Art Nouveau Filigree',
                'in_stock': True,
                'sku': 'ARTN-LACE-001',
                'rating': Decimal('4.9'),
                'reviews_count': 47,
                'specs': {
                    'Fiber': '100% Pure Mulberry Silk with Iridescent Gradient Dye',
                    'Shuttle': 'Polished Antique Pewter / Silver Finish with Picot Hook',
                    'Origin': 'Paris / Vienna',
                },
                'theme_niche': 'artnouveau',
                'is_featured': True,
                'variants': [
                    {'name': 'Peacock Emerald Gradient', 'color_hex': '#518576', 'price_adjustment': Decimal('0.00'), 'stock': 30},
                    {'name': 'Dusty Orchid Rose Gradient', 'color_hex': '#DFB2B4', 'price_adjustment': Decimal('0.00'), 'stock': 25},
                ]
            },
        ]

        for pdata in products_data:
            variants_list = pdata.pop('variants', [])
            product, _ = Product.objects.update_or_create(
                slug=pdata['slug'],
                defaults=pdata
            )
            for vdata in variants_list:
                ProductVariant.objects.update_or_create(
                    product=product,
                    name=vdata['name'],
                    defaults={
                        'color_hex': vdata.get('color_hex'),
                        'price_adjustment': vdata.get('price_adjustment', Decimal('0.00')),
                        'stock': vdata.get('stock', 30),
                        'sku_suffix': vdata.get('sku_suffix', ''),
                    }
                )

        # 4. Coupons
        coupons = [
            {'code': 'NEEDLE15', 'discount_percent': 15, 'min_spend': Decimal('30.00')},
            {'code': 'SAVE10', 'discount_percent': 10, 'min_spend': Decimal('0.00')},
            {'code': 'ARTISAN20', 'discount_percent': 20, 'min_spend': Decimal('60.00')},
        ]
        for c in coupons:
            Coupon.objects.update_or_create(
                code=c['code'],
                defaults=c
            )

        # 5. Initial Sample Order for demonstration
        sample_prod = Product.objects.filter(slug='soie-dor-pure-french-silk-floss').first()
        if sample_prod and not Order.objects.exists():
            order = Order.objects.create(
                customer_name="Geneviève Moreau",
                customer_email="g.moreau@atelier-couture.fr",
                customer_phone="+33 1 42 68 55 00",
                shipping_address="14 Rue du Faubourg Saint-Honoré",
                city="Paris",
                postal_code="75008",
                country="France",
                payment_method="credit_card",
                shipping_method="Express Atelier Courier",
                shipping_cost=Decimal('0.00'),
                subtotal=Decimal('37.00'),
                discount_amount=Decimal('5.55'),
                total_amount=Decimal('31.45'),
                status='confirmed',
            )
            OrderItem.objects.create(
                order=order,
                product=sample_prod,
                product_title=sample_prod.title,
                variant_name="Champagne Gold (Dore)",
                unit_price=Decimal('18.50'),
                quantity=2,
                total_price=Decimal('37.00')
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded needle & thread catalog spanning all 10 sample styles!"))
