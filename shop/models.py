import uuid
from decimal import Decimal
from django.db import models
from django.utils.text import slugify


THEME_CHOICES = [
    ('couture', '1. Atelier Couture (Haute Couture & Goldwork)'),
    ('sashiko', '2. Wabi-Sabi Sashiko (Japanese Mending & Indigo)'),
    ('quilter', '3. Modern Quilter Studio (Contemporary Craft & Sewing)'),
    ('leathercraft', '4. Heritage Leathercraft (Industrial Workshop & Rigging)'),
    ('botanical', '5. Botanical Dyehouse (Organic Plant-Dyed Silk & Linen)'),
    ('nordic', '6. Nordic Wool & Crewel (Scandinavian Minimalist Hygge)'),
    ('victorian', '7. Victorian Haberdashery (Antique Parlor & Filigree)'),
    ('neontuft', '8. Neon Tuft & Punch (Gen-Z Fiber Art & Modern Rug Punch)'),
    ('precision', '9. Precision Micro-Needle (High-Tech Industrial & Embroidery)'),
    ('boho', '10. Boho Tapestry & Weft (Artisan Weaving & Macramé)'),
]


class StoreConfig(models.Model):
    store_name = models.CharField(max_length=150, default="Needle & Thread Merchant Co.")
    tagline = models.CharField(max_length=255, default="Fine Haberdashery, Artisan Threads & Precision Needles")
    announcement_text = models.CharField(
        max_length=255, 
        default="✨ Handcrafted Spring Release: Free worldwide shipping on orders over $50 | Use code NEEDLE15"
    )
    active_theme = models.CharField(max_length=30, choices=THEME_CHOICES, default='couture')
    contact_email = models.EmailField(default="concierge@needletravel.com")
    contact_phone = models.CharField(max_length=50, default="+1 (800) 555-SEWN")
    currency_symbol = models.CharField(max_length=5, default="$")
    instagram_handle = models.CharField(max_length=100, default="@needletravel_official")

    class Meta:
        verbose_name = "Store Configuration"
        verbose_name_plural = "Store Configuration"

    def __str__(self):
        return f"{self.store_name} ({self.get_active_theme_display()})"

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji or icon identifier")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.CharField(max_length=500)
    badge = models.CharField(max_length=50, blank=True, help_text="e.g. Artisan Made, Best Seller, Limited")
    in_stock = models.BooleanField(default=True)
    sku = models.CharField(max_length=50, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=Decimal('4.9'))
    reviews_count = models.PositiveIntegerField(default=28)
    specs = models.JSONField(default=dict, blank=True, help_text="Key-value pairs for technical specifications")
    theme_niche = models.CharField(max_length=30, blank=True, help_text="Sample theme archetype this best represents")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def discount_percent(self):
        if self.compare_price and self.compare_price > self.base_price:
            diff = self.compare_price - self.base_price
            return int((diff / self.compare_price) * 100)
        return None


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    variant_type = models.CharField(max_length=50, default="standard", help_text="e.g. color, gauge, spool_weight")
    name = models.CharField(max_length=150)
    color_hex = models.CharField(max_length=20, blank=True, null=True, help_text="e.g. #D4AF37 for color swatches")
    gauge_size = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. Size 10 / 0.45mm")
    price_adjustment = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    stock = models.PositiveIntegerField(default=35)
    sku_suffix = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.product.title} - {self.name}"

    @property
    def final_price(self):
        return self.product.base_price + self.price_adjustment


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    discount_percent = models.PositiveIntegerField(default=10)
    min_spend = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percent}% OFF)"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Payment Pending'),
        ('confirmed', 'Order Confirmed & Assembling'),
        ('shipped', 'Dispatched / In Transit'),
        ('delivered', 'Delivered'),
    ]

    PAYMENT_CHOICES = [
        ('credit_card', 'Credit / Debit Card'),
        ('cod', 'Cash on Delivery (COD)'),
        ('bank_transfer', 'Direct Bank Transfer / Wire'),
    ]

    order_number = models.CharField(max_length=50, unique=True, editable=False)
    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=50)
    shipping_address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=30)
    country = models.CharField(max_length=100, default="United States")
    
    payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default='credit_card')
    shipping_method = models.CharField(max_length=50, default="Standard Atelier Courier")
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='confirmed')
    tracking_number = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.order_number} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"NT-{uuid.uuid4().hex[:8].upper()}"
        if not self.tracking_number:
            self.tracking_number = f"TRK-{uuid.uuid4().hex[:10].upper()}"
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_title = models.CharField(max_length=200)
    variant_name = models.CharField(max_length=150, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product_title} ({self.variant_name})"
