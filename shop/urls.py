from django.urls import path
from . import views

urlpatterns = [
    # Clean SEO Demo Storefront Routes
    path('demo/<slug:theme_id>/', views.home_view, name='demo_home'),
    path('demo/<slug:theme_id>/catalog/', views.catalog_view, name='demo_catalog'),
    path('demo/<slug:theme_id>/catalog/<slug:category_slug>/', views.catalog_view, name='demo_catalog_category'),
    path('demo/<slug:theme_id>/product/<slug:slug>/', views.product_detail_view, name='demo_product_detail'),

    # Standard Storefront Routes (SEO Clean)
    path('', views.home_view, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('catalog/<slug:category_slug>/', views.catalog_view, name='catalog_category'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    
    # Cart AJAX API
    path('api/cart/', views.cart_data, name='cart_data'),
    path('api/cart/add/', views.cart_add, name='cart_add'),
    path('api/cart/update/', views.cart_update, name='cart_update'),
    path('api/cart/remove/', views.cart_remove, name='cart_remove'),
    path('api/cart/coupon/', views.cart_apply_coupon, name='cart_apply_coupon'),
    path('api/cart/coupon/remove/', views.cart_remove_coupon, name='cart_remove_coupon'),
    
    # Checkout & Confirmation
    path('checkout/', views.checkout_view, name='checkout'),
    path('order/<str:order_number>/', views.order_success_view, name='order_success'),
    
    # Theme Switcher & Admin
    path('set-theme/<str:theme_id>/', views.set_theme_view, name='set_theme'),
    path('store-admin/', views.store_admin_view, name='store_admin'),
]
