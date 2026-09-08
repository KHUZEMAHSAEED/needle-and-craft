from decimal import Decimal
import json
from django.test import TestCase, Client
from django.urls import reverse

from .models import StoreConfig, Category, Product, ProductVariant, Coupon, Order, OrderItem
from .context_processors import THEME_SAMPLES, THEME_MAP


class ShopEcommerceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.config = StoreConfig.get_solo()
        self.category = Category.objects.create(name="Fine Silk", slug="fine-silk", icon="🧵")
        self.product = Product.objects.create(
            category=self.category,
            title="French Mulberry Silk Floss",
            slug="french-mulberry-silk-floss",
            short_description="Divisible silk for couture embroidery.",
            description="Exquisite French silk spun in Lyon.",
            base_price=Decimal('15.00'),
            compare_price=Decimal('20.00'),
            image_url="https://example.com/silk.jpg",
            sku="SILK-TEST-01",
            theme_niche="couture",
        )
        self.variant = ProductVariant.objects.create(
            product=self.product,
            name="Champagne Gold",
            color_hex="#D4AF37",
            price_adjustment=Decimal('2.50'),
            stock=20,
        )
        self.coupon = Coupon.objects.create(
            code="TEST10",
            discount_percent=10,
            min_spend=Decimal('10.00'),
            active=True
        )

    def test_sixteen_sample_themes_configured(self):
        """Verify all 16 front-end sample archetypes are defined and available."""
        self.assertEqual(len(THEME_SAMPLES), 16)
        expected_keys = [
            'couture', 'sashiko', 'quilter', 'leathercraft', 'botanical',
            'nordic', 'victorian', 'neontuft', 'precision', 'boho',
            'baroque', 'retro70s', 'tactical', 'kawaii', 'gothic', 'artnouveau'
        ]
        for key in expected_keys:
            self.assertIn(key, THEME_MAP)
            self.assertIn(THEME_MAP[key]['layout_style'], ['boutique', 'studio', 'technical', 'artisanal'])

    def test_clean_seo_demo_routes(self):
        """Verify clean canonical SEO routes for demo storefronts."""
        # 1. Clean demo home route: /demo/<theme_id>/
        resp_baroque = self.client.get(reverse('demo_home', kwargs={'theme_id': 'baroque'}))
        self.assertEqual(resp_baroque.status_code, 200)
        self.assertEqual(resp_baroque.context['active_theme'], 'baroque')
        self.assertEqual(resp_baroque.context['layout_style'], 'boutique')

        # 2. Clean demo catalog route: /demo/<theme_id>/catalog/
        resp_tactical_cat = self.client.get(reverse('demo_catalog', kwargs={'theme_id': 'tactical'}))
        self.assertEqual(resp_tactical_cat.status_code, 200)
        self.assertEqual(resp_tactical_cat.context['active_theme'], 'tactical')
        self.assertEqual(resp_tactical_cat.context['layout_style'], 'technical')

        # 3. Clean demo catalog category route: /demo/<theme_id>/catalog/<category_slug>/
        resp_demo_cat = self.client.get(reverse('demo_catalog_category', kwargs={'theme_id': 'sashiko', 'category_slug': 'fine-silk'}))
        self.assertEqual(resp_demo_cat.status_code, 200)
        self.assertEqual(resp_demo_cat.context['active_theme'], 'sashiko')
        self.assertEqual(resp_demo_cat.context['layout_style'], 'artisanal')

        # 4. Clean demo product detail route: /demo/<theme_id>/product/<slug>/
        resp_demo_prod = self.client.get(reverse('demo_product_detail', kwargs={'theme_id': 'kawaii', 'slug': self.product.slug}))
        self.assertEqual(resp_demo_prod.status_code, 200)
        self.assertEqual(resp_demo_prod.context['active_theme'], 'kawaii')
        self.assertEqual(resp_demo_prod.context['layout_style'], 'studio')

    def test_clean_category_route(self):
        """Verify canonical category SEO route: /catalog/<category_slug>/"""
        response = self.client.get(reverse('catalog_category', kwargs={'category_slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "French Mulberry Silk Floss")

    def test_catalog_and_filters(self):
        """Verify product catalog search and category filtering."""
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "French Mulberry Silk Floss")

        # Search test
        search_resp = self.client.get(reverse('catalog') + '?q=Mulberry')
        self.assertContains(search_resp, "French Mulberry Silk Floss")

        search_empty = self.client.get(reverse('catalog') + '?q=NonExistentItemXYZ')
        self.assertContains(search_empty, "No products matched your criteria")

    def test_product_detail(self):
        """Verify product detail view with variants."""
        response = self.client.get(reverse('product_detail', kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "French Mulberry Silk Floss")
        self.assertContains(response, "Champagne Gold")

    def test_cart_ajax_operations(self):
        """Verify adding to cart, updating quantity, applying coupon, and removing items."""
        # 1. Add item with variant
        resp_add = self.client.post(
            reverse('cart_add'),
            data=json.dumps({
                'product_id': self.product.id,
                'variant_id': self.variant.id,
                'quantity': 2,
            }),
            content_type='application/json'
        )
        self.assertEqual(resp_add.status_code, 200)
        data = resp_add.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['cart']['count'], 2)
        # Unit price = 15.00 + 2.50 = 17.50, Total = 35.00
        self.assertEqual(data['cart']['subtotal'], '35.00')

        item_key = data['cart']['items'][0]['key']

        # 2. Apply coupon
        resp_coupon = self.client.post(
            reverse('cart_apply_coupon'),
            data=json.dumps({'code': 'TEST10'}),
            content_type='application/json'
        )
        self.assertEqual(resp_coupon.status_code, 200)
        data_coupon = resp_coupon.json()
        self.assertTrue(data_coupon['success'])
        # 10% of 35.00 = 3.50
        self.assertEqual(data_coupon['cart']['discount'], '3.50')

        # 3. Update quantity
        resp_update = self.client.post(
            reverse('cart_update'),
            data=json.dumps({'key': item_key, 'quantity': 3}),
            content_type='application/json'
        )
        self.assertEqual(resp_update.status_code, 200)
        data_update = resp_update.json()
        self.assertEqual(data_update['cart']['count'], 3)
        # 3 * 17.50 = 52.50
        self.assertEqual(data_update['cart']['subtotal'], '52.50')

        # 4. Remove item
        resp_remove = self.client.post(
            reverse('cart_remove'),
            data=json.dumps({'key': item_key}),
            content_type='application/json'
        )
        self.assertEqual(resp_remove.status_code, 200)
        data_remove = resp_remove.json()
        self.assertEqual(data_remove['cart']['count'], 0)

    def test_checkout_and_order_flow(self):
        """Verify checkout submission creates an Order and OrderItem records and redirects to success."""
        # Add product to cart first
        self.client.post(
            reverse('cart_add'),
            data=json.dumps({
                'product_id': self.product.id,
                'variant_id': self.variant.id,
                'quantity': 1,
            }),
            content_type='application/json'
        )

        checkout_data = {
            'customer_name': 'Madeleine Dupont',
            'customer_email': 'madeleine@couture.com',
            'customer_phone': '+1 (555) 789-0123',
            'shipping_address': '12 Silk Weaver Lane',
            'city': 'Boston',
            'postal_code': '02108',
            'country': 'United States',
            'payment_method': 'credit_card',
            'shipping_method': 'Standard Courier',
        }

        resp = self.client.post(reverse('checkout'), data=checkout_data)
        self.assertEqual(resp.status_code, 302)

        # Check Order was created
        order = Order.objects.filter(customer_name='Madeleine Dupont').first()
        self.assertIsNotNone(order)
        self.assertTrue(order.order_number.startswith("NT-"))
        self.assertEqual(order.items.count(), 1)
        item = order.items.first()
        self.assertEqual(item.product_title, self.product.title)
        self.assertEqual(item.unit_price, Decimal('17.50'))

        # Check order success view
        success_resp = self.client.get(reverse('order_success', kwargs={'order_number': order.order_number}))
        self.assertEqual(success_resp.status_code, 200)
        self.assertContains(success_resp, order.order_number)
        self.assertContains(success_resp, "Madeleine Dupont")

    def test_store_admin_settings_update(self):
        """Verify store owner can update active default theme and store branding."""
        post_data = {
            'action': 'update_settings',
            'store_name': 'Kyoto Sashiko Guild',
            'tagline': 'Authentic Japanese Visible Mending',
            'announcement_text': 'Free shipping on orders over $50',
            'active_theme': 'sashiko',
        }
        resp = self.client.post(reverse('store_admin'), data=post_data)
        self.assertEqual(resp.status_code, 302)

        config = StoreConfig.get_solo()
        self.assertEqual(config.store_name, 'Kyoto Sashiko Guild')
        self.assertEqual(config.active_theme, 'sashiko')

    def test_quick_search_api(self):
        """Verify the WoodMart-style live search autocomplete API endpoint."""
        # 1. Search with query matching product title
        resp = self.client.get(reverse('quick_search_api') + '?q=Mulberry')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertGreaterEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['title'], self.product.title)

        # 2. Search with category filter
        resp_cat = self.client.get(reverse('quick_search_api') + f'?q=Mulberry&category={self.category.slug}')
        self.assertEqual(resp_cat.status_code, 200)
        data_cat = resp_cat.json()
        self.assertGreaterEqual(data_cat['count'], 1)

        # 3. Search with non-matching query
        resp_empty = self.client.get(reverse('quick_search_api') + '?q=NonExistentZ99')
        self.assertEqual(resp_empty.status_code, 200)
        self.assertEqual(resp_empty.json()['count'], 0)

    def test_woodmart_headers_and_mega_menus(self):
        """Verify that WoodMart mega headers and home page catalog search render correctly."""
        # Theme 3: Modern Quilter uses header_style 'woodmart_mega'
        resp_quilter = self.client.get(reverse('demo_home', kwargs={'theme_id': 'quilter'}))
        self.assertEqual(resp_quilter.status_code, 200)
        self.assertContains(resp_quilter, "header-style-mega")
        self.assertContains(resp_quilter, "BROWSE CATEGORIES")
        self.assertContains(resp_quilter, "woodmart-search-form")
        self.assertContains(resp_quilter, "home-catalog-search-section")

        # Theme 1: Atelier Couture uses header_style 'boutique'
        resp_couture = self.client.get(reverse('demo_home', kwargs={'theme_id': 'couture'}))
        self.assertEqual(resp_couture.status_code, 200)
        self.assertContains(resp_couture, "header-style-boutique")
        self.assertContains(resp_couture, "HAUTE COLLECTIONS")

        # Theme 4: Heritage Leathercraft uses header_style 'technical'
        resp_leather = self.client.get(reverse('demo_home', kwargs={'theme_id': 'leathercraft'}))
        self.assertEqual(resp_leather.status_code, 200)
        self.assertContains(resp_leather, "header-style-technical")
        self.assertContains(resp_leather, "SPEC_CATALOG_INDEX")

