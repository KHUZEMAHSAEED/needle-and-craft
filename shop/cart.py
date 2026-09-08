from decimal import Decimal
from django.conf import settings
from .models import Product, ProductVariant, Coupon


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_data')
        if not cart:
            cart = self.session['cart_data'] = {}
        self.cart = cart
        self.coupon_code = self.session.get('cart_coupon')

    def _get_item_key(self, product_id, variant_id=None):
        return f"{product_id}_{variant_id or 0}"

    def add(self, product, variant=None, quantity=1, override_quantity=False):
        product_id = product.id
        variant_id = variant.id if variant else 0
        key = self._get_item_key(product_id, variant_id)

        unit_price = str(variant.final_price if variant else product.base_price)
        variant_name = variant.name if variant else ""

        if key not in self.cart:
            self.cart[key] = {
                'product_id': product.id,
                'variant_id': variant_id,
                'title': product.title,
                'variant_name': variant_name,
                'unit_price': unit_price,
                'quantity': 0,
                'image_url': product.image_url,
                'slug': product.slug,
            }

        if override_quantity:
            self.cart[key]['quantity'] = max(1, int(quantity))
        else:
            self.cart[key]['quantity'] += int(quantity)

        self.save()

    def update(self, key, quantity):
        if key in self.cart:
            qty = int(quantity)
            if qty > 0:
                self.cart[key]['quantity'] = qty
            else:
                del self.cart[key]
            self.save()

    def remove(self, key):
        if key in self.cart:
            del self.cart[key]
            self.save()

    def apply_coupon(self, code):
        clean_code = code.strip().upper()
        try:
            coupon = Coupon.objects.get(code__iexact=clean_code, active=True)
            self.session['cart_coupon'] = coupon.code
            self.coupon_code = coupon.code
            self.save()
            return True, f"Coupon '{coupon.code}' applied! ({coupon.discount_percent}% OFF)"
        except Coupon.DoesNotExist:
            return False, "Invalid or expired coupon code."

    def remove_coupon(self):
        if 'cart_coupon' in self.session:
            del self.session['cart_coupon']
            self.coupon_code = None
            self.save()

    def get_coupon(self):
        if self.coupon_code:
            try:
                return Coupon.objects.get(code=self.coupon_code, active=True)
            except Coupon.DoesNotExist:
                return None
        return None

    def __iter__(self):
        product_ids = [item['product_id'] for item in self.cart.values()]
        products = Product.objects.filter(id__in=product_ids).in_bulk()

        for key, item in self.cart.items():
            product = products.get(item['product_id'])
            item_copy = item.copy()
            item_copy['key'] = key
            item_copy['product'] = product
            item_copy['unit_price_decimal'] = Decimal(item['unit_price'])
            item_copy['total_price_decimal'] = item_copy['unit_price_decimal'] * item['quantity']
            yield item_copy

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    @property
    def total_count(self):
        return len(self)

    @property
    def is_empty(self):
        return len(self) == 0

    def get_subtotal(self):
        return sum(
            Decimal(item['unit_price']) * item['quantity']
            for item in self.cart.values()
        )

    def get_discount(self):
        coupon = self.get_coupon()
        subtotal = self.get_subtotal()
        if coupon and subtotal >= coupon.min_spend:
            discount = (subtotal * Decimal(coupon.discount_percent)) / Decimal(100)
            return discount.quantize(Decimal('0.01'))
        return Decimal('0.00')

    def get_shipping(self):
        # Free shipping if subtotal >= 50, otherwise flat 4.95
        subtotal = self.get_subtotal()
        if subtotal == 0 or subtotal >= Decimal('50.00'):
            return Decimal('0.00')
        return Decimal('4.95')

    def get_total(self):
        subtotal = self.get_subtotal()
        if subtotal == 0:
            return Decimal('0.00')
        discount = self.get_discount()
        shipping = self.get_shipping()
        total = subtotal - discount + shipping
        return max(Decimal('0.00'), total)

    def clear(self):
        self.session['cart_data'] = {}
        if 'cart_coupon' in self.session:
            del self.session['cart_coupon']
        self.save()

    def save(self):
        self.session.modified = True

    def to_json(self):
        coupon = self.get_coupon()
        items_list = []
        for key, item in self.cart.items():
            unit_p = Decimal(item['unit_price'])
            qty = item['quantity']
            items_list.append({
                'key': key,
                'product_id': item['product_id'],
                'variant_id': item['variant_id'],
                'title': item['title'],
                'variant_name': item['variant_name'],
                'unit_price': f"{unit_p:.2f}",
                'quantity': qty,
                'total_price': f"{(unit_p * qty):.2f}",
                'image_url': item['image_url'],
                'slug': item['slug'],
            })

        subtotal = self.get_subtotal()
        discount = self.get_discount()
        shipping = self.get_shipping()
        total = self.get_total()

        return {
            'items': items_list,
            'count': self.total_count,
            'subtotal': f"{subtotal:.2f}",
            'discount': f"{discount:.2f}",
            'shipping': f"{shipping:.2f}",
            'total': f"{total:.2f}",
            'free_shipping_eligible': subtotal >= Decimal('50.00'),
            'coupon_code': coupon.code if coupon else None,
            'coupon_percent': coupon.discount_percent if coupon else None,
        }
