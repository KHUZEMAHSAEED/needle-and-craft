from django.contrib import admin
from .models import StoreConfig, Category, Product, ProductVariant, Coupon, Order, OrderItem


@admin.register(StoreConfig)
class StoreConfigAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'active_theme', 'contact_email', 'contact_phone')


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'base_price', 'compare_price', 'in_stock', 'is_featured', 'sku', 'theme_niche')
    list_filter = ('category', 'in_stock', 'is_featured', 'theme_niche')
    search_fields = ('title', 'sku', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductVariantInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'color_hex', 'gauge_size', 'price_adjustment', 'stock')
    list_filter = ('product__category',)
    search_fields = ('name', 'product__title')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'min_spend', 'active')
    list_filter = ('active',)
    search_fields = ('code',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_title', 'variant_name', 'unit_price', 'quantity', 'total_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'customer_email', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'customer_name', 'customer_email', 'tracking_number')
    readonly_fields = ('order_number', 'tracking_number', 'created_at')
    inlines = [OrderItemInline]
