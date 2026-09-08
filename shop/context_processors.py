from .models import StoreConfig
from .cart import Cart


THEME_SAMPLES = [
    {
        'id': 'couture',
        'number': 1,
        'name': 'Atelier Couture',
        'subtitle': 'Haute Couture French Haberdashery',
        'niche': 'Silk Floss, Goldwork, Tambour Needles',
        'tag': 'Luxury Dark Luxe',
        'layout_style': 'boutique',
        'primary_color': '#D4AF37',
        'accent_color': '#E5C158',
        'bg_preview': '#0D0F12',
        'font_family': 'Playfair Display, serif',
    },
    {
        'id': 'sashiko',
        'number': 2,
        'name': 'Wabi-Sabi Sashiko',
        'subtitle': 'Japanese Visible Mending & Boro',
        'niche': 'Indigo Heavy Thread, Palm Thimbles',
        'tag': 'Zen Organic Mending',
        'layout_style': 'artisanal',
        'primary_color': '#1B3B6F',
        'accent_color': '#D97757',
        'bg_preview': '#F7F4EE',
        'font_family': 'Outfit, sans-serif',
    },
    {
        'id': 'quilter',
        'number': 3,
        'name': 'Modern Quilter Studio',
        'subtitle': 'Contemporary Sewing & Notions Hub',
        'niche': 'Titanium Needles, 50wt Cotton, Rotary Cutters',
        'tag': 'Vibrant Maker Studio',
        'layout_style': 'studio',
        'primary_color': '#FF6B6B',
        'accent_color': '#2EC4B6',
        'bg_preview': '#FFFFFF',
        'font_family': 'Plus Jakarta Sans, sans-serif',
    },
    {
        'id': 'leathercraft',
        'number': 4,
        'name': 'Heritage Leathercraft',
        'subtitle': 'Heavy Industrial Workshop & Sailmaker',
        'niche': 'Waxed Harness Twine, Cobbler Awls',
        'tag': 'Rugged Industrial',
        'layout_style': 'technical',
        'primary_color': '#8B4513',
        'accent_color': '#C69214',
        'bg_preview': '#22252A',
        'font_family': 'Space Grotesk, sans-serif',
    },
    {
        'id': 'botanical',
        'number': 5,
        'name': 'Botanical Dyehouse',
        'subtitle': 'Organic Plant-Dyed Natural Fibers',
        'niche': 'Madder & Indigo Dyed Silks, Linen Thread',
        'tag': 'Earthy Natural Eco',
        'layout_style': 'artisanal',
        'primary_color': '#4F772D',
        'accent_color': '#BC4749',
        'bg_preview': '#FAF8F5',
        'font_family': 'Fraunces, serif',
    },
    {
        'id': 'nordic',
        'number': 6,
        'name': 'Nordic Wool & Crewel',
        'subtitle': 'Scandinavian Minimalist Hygge',
        'niche': 'Organic Crewel Wool, Tapestry Needles',
        'tag': 'Clean Scandi Hygge',
        'layout_style': 'studio',
        'primary_color': '#2B4C7E',
        'accent_color': '#D64550',
        'bg_preview': '#F0F4F8',
        'font_family': 'Plus Jakarta Sans, sans-serif',
    },
    {
        'id': 'victorian',
        'number': 7,
        'name': 'Victorian Haberdashery',
        'subtitle': '19th Century Antique Parlor & Lace',
        'niche': 'Filigree Needle Cases, Tatting Shuttles',
        'tag': 'Vintage Antique Etching',
        'layout_style': 'boutique',
        'primary_color': '#581825',
        'accent_color': '#B8860B',
        'bg_preview': '#F4ECD8',
        'font_family': 'Cinzel, serif',
    },
    {
        'id': 'neontuft',
        'number': 8,
        'name': 'Neon Tuft & Punch',
        'subtitle': 'Gen-Z Modern Fiber Art & Rug Punch',
        'niche': 'Punch Needles, Chunky Tufting Yarn',
        'tag': 'Cyber Neo-Brutalist',
        'layout_style': 'studio',
        'primary_color': '#B4F82C',
        'accent_color': '#8338EC',
        'bg_preview': '#12131C',
        'font_family': 'Syne, sans-serif',
    },
    {
        'id': 'precision',
        'number': 9,
        'name': 'Precision Micro-Needle',
        'subtitle': 'High-Tech Industrial & Machine Embroidery',
        'niche': 'Groz-Beckert DBx1, Kevlar & Bonded Nylon',
        'tag': 'High-Tech Technical',
        'layout_style': 'technical',
        'primary_color': '#06B6D4',
        'accent_color': '#3B82F6',
        'bg_preview': '#F8FAFC',
        'font_family': 'Space Grotesk, sans-serif',
    },
    {
        'id': 'boho',
        'number': 10,
        'name': 'Boho Tapestry & Weft',
        'subtitle': 'Artisan Fiber Weaving & Macramé',
        'niche': 'Unbleached Macramé Cord, Weaving Shuttles',
        'tag': 'Bohemian Warm Craft',
        'layout_style': 'artisanal',
        'primary_color': '#D9822B',
        'accent_color': '#B3545A',
        'bg_preview': '#FCF8F5',
        'font_family': 'Outfit, sans-serif',
    },
    {
        'id': 'baroque',
        'number': 11,
        'name': 'Baroque Ecclesiastical',
        'subtitle': 'Cathedral Goldwork & Vestment Thread',
        'niche': 'Real Gilt Passing Thread, Bullion Wire',
        'tag': 'Sacred Gilded Heraldry',
        'layout_style': 'boutique',
        'primary_color': '#C5A059',
        'accent_color': '#8B1E3F',
        'bg_preview': '#180B22',
        'font_family': 'Cinzel, serif',
    },
    {
        'id': 'retro70s',
        'number': 12,
        'name': 'Retro 70s Earth Weaver',
        'subtitle': 'Vintage Plant Hangers & Groovy Knotting',
        'niche': 'Rough Jute, Organic Hemp, Amber Beads',
        'tag': 'Warm Nostalgic Groovy',
        'layout_style': 'artisanal',
        'primary_color': '#E1AD01',
        'accent_color': '#B84A39',
        'bg_preview': '#FBF6EE',
        'font_family': 'Fraunces, serif',
    },
    {
        'id': 'tactical',
        'number': 13,
        'name': 'Tactical Rigging & Mil-Spec',
        'subtitle': 'Heavy Military-Grade Cordage & Awls',
        'niche': 'Bonded Kevlar 92, Heavy Webbing Needles',
        'tag': 'Mil-Spec Extreme Tensile',
        'layout_style': 'technical',
        'primary_color': '#9A7B4F',
        'accent_color': '#4B5320',
        'bg_preview': '#151719',
        'font_family': 'Space Grotesk, sans-serif',
    },
    {
        'id': 'kawaii',
        'number': 14,
        'name': 'Kawaii Pastel Amigurumi',
        'subtitle': 'Sweet Japanese Plush Crochet & Soft Fluff',
        'niche': 'Ergonomic Pastel Hooks, Milk Cotton Fluff',
        'tag': 'Playful Pastel Cute',
        'layout_style': 'studio',
        'primary_color': '#FF8FA3',
        'accent_color': '#70D6FF',
        'bg_preview': '#FFF5F7',
        'font_family': 'Outfit, sans-serif',
    },
    {
        'id': 'gothic',
        'number': 15,
        'name': 'Dark Romantic Corsetry',
        'subtitle': 'Victorian Corsetry & Velvet Millinery',
        'niche': 'Heavy Boning Needles, Waxed Lacing Cord',
        'tag': 'Dark Romance Velvet',
        'layout_style': 'boutique',
        'primary_color': '#9B1B30',
        'accent_color': '#4A0E17',
        'bg_preview': '#0F080C',
        'font_family': 'Playfair Display, serif',
    },
    {
        'id': 'artnouveau',
        'number': 16,
        'name': 'Art Nouveau Stitched Lace',
        'subtitle': 'Mucha-Inspired Filigree Silks & Tatting',
        'niche': 'Filigree Shuttles, Peacock Green Silks',
        'tag': 'Organic Whiplash Filigree',
        'layout_style': 'artisanal',
        'primary_color': '#7FA99B',
        'accent_color': '#DFB2B4',
        'bg_preview': '#F6FAF8',
        'font_family': 'Fraunces, serif',
    },
]

THEME_MAP = {t['id']: t for t in THEME_SAMPLES}


def shop_context(request):
    config = StoreConfig.get_solo()
    
    # Priority:
    # 1. URL kwargs from clean SEO route: /demo/<theme_id>/...
    # 2. Query param ?theme=... (backward compatibility)
    # 3. Session stored theme
    # 4. Store config default theme
    url_theme = None
    if request.resolver_match and 'theme_id' in request.resolver_match.kwargs:
        url_theme = request.resolver_match.kwargs['theme_id']

    query_theme = request.GET.get('theme')
    
    if url_theme and url_theme in THEME_MAP:
        active_theme_key = url_theme
        request.session['active_theme'] = active_theme_key
        is_demo_mode = True
    elif query_theme and query_theme in THEME_MAP:
        active_theme_key = query_theme
        request.session['active_theme'] = active_theme_key
        is_demo_mode = True
    else:
        active_theme_key = request.session.get('active_theme', config.active_theme)
        is_demo_mode = False

    if active_theme_key not in THEME_MAP:
        active_theme_key = 'couture'

    current_theme_info = THEME_MAP.get(active_theme_key, THEME_SAMPLES[0])
    layout_style = current_theme_info.get('layout_style', 'boutique')
    cart = Cart(request)

    # Clean URL prefix for demo mode
    demo_prefix = f"/demo/{active_theme_key}" if is_demo_mode else ""

    return {
        'store_config': config,
        'active_theme': active_theme_key,
        'current_theme': current_theme_info,
        'layout_style': layout_style,
        'theme_samples': THEME_SAMPLES,
        'is_demo_mode': is_demo_mode,
        'demo_prefix': demo_prefix,
        'cart': cart,
        'cart_count': cart.total_count,
    }
