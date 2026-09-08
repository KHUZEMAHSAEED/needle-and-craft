import json
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.db.models import Q

from .models import StoreConfig, Category, Product, ProductVariant, Coupon, Order, OrderItem
from .cart import Cart
from .context_processors import THEME_MAP, THEME_SAMPLES


def home_view(request, theme_id=None):
    if theme_id and theme_id in THEME_MAP:
        request.session['active_theme'] = theme_id

    featured_products = Product.objects.filter(is_featured=True, in_stock=True)[:8]
    if not featured_products.exists():
        featured_products = Product.objects.all()[:8]
    
    categories = Category.objects.all()
    latest_products = Product.objects.all().order_by('-created_at')[:6]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'shop/home.html', context)


def catalog_view(request, theme_id=None, category_slug=None):
    if theme_id and theme_id in THEME_MAP:
        request.session['active_theme'] = theme_id

    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Category filter (supports clean SEO route /catalog/<category_slug>/ or ?category=...)
    slug_to_check = category_slug or request.GET.get('category', '').strip()
    selected_category = None
    if slug_to_check:
        selected_category = get_object_or_404(Category, slug=slug_to_check)
        products = products.filter(category=selected_category)

    # Search filter
    search_query = request.GET.get('q', '').strip()
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(sku__icontains=search_query)
        )

    # In-stock filter
    in_stock_only = request.GET.get('in_stock') == 'true'
    if in_stock_only:
        products = products.filter(in_stock=True)

    # Niche filter (matches theme sample)
    niche_filter = request.GET.get('niche', '').strip()
    if niche_filter:
        products = products.filter(theme_niche=niche_filter)

    # Sorting
    sort = request.GET.get('sort', 'featured')
    if sort == 'price_asc':
        products = products.order_by('base_price')
    elif sort == 'price_desc':
        products = products.order_by('-base_price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('-is_featured', 'title')

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'in_stock_only': in_stock_only,
        'sort': sort,
        'total_count': products.count(),
    }
    return render(request, 'shop/catalog.html', context)


def product_detail_view(request, slug, theme_id=None):
    if theme_id and theme_id in THEME_MAP:
        request.session['active_theme'] = theme_id

    product = get_object_or_404(Product, slug=slug)
    variants = product.variants.all()
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'variants': variants,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)


# ==========================================
# CART AJAX ENDPOINTS
# ==========================================

@require_POST
def cart_add(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        variant_id = data.get('variant_id')
        quantity = int(data.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id)
        variant = None
        if variant_id:
            variant = get_object_or_404(ProductVariant, id=variant_id, product=product)

        cart = Cart(request)
        cart.add(product=product, variant=variant, quantity=quantity)

        return JsonResponse({
            'success': True,
            'message': f"Added '{product.title}' to your cart.",
            'cart': cart.to_json(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@require_POST
def cart_update(request):
    try:
        data = json.loads(request.body)
        key = data.get('key')
        quantity = int(data.get('quantity', 1))

        cart = Cart(request)
        cart.update(key=key, quantity=quantity)

        return JsonResponse({
            'success': True,
            'cart': cart.to_json(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@require_POST
def cart_remove(request):
    try:
        data = json.loads(request.body)
        key = data.get('key')

        cart = Cart(request)
        cart.remove(key=key)

        return JsonResponse({
            'success': True,
            'cart': cart.to_json(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@require_POST
def cart_apply_coupon(request):
    try:
        data = json.loads(request.body)
        code = data.get('code', '')
        cart = Cart(request)
        success, message = cart.apply_coupon(code)
        return JsonResponse({
            'success': success,
            'message': message,
            'cart': cart.to_json(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@require_POST
def cart_remove_coupon(request):
    cart = Cart(request)
    cart.remove_coupon()
    return JsonResponse({
        'success': True,
        'message': "Coupon removed.",
        'cart': cart.to_json(),
    })


@require_GET
def cart_data(request):
    cart = Cart(request)
    return JsonResponse(cart.to_json())


# ==========================================
# CHECKOUT & ORDER CONFIRMATION
# ==========================================

def checkout_view(request):
    cart = Cart(request)
    if cart.is_empty:
        messages.warning(request, "Your bag is currently empty. Please select needles or threads to purchase.")
        return redirect('catalog')

    if request.method == 'POST':
        name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('customer_email', '').strip()
        phone = request.POST.get('customer_phone', '').strip()
        address = request.POST.get('shipping_address', '').strip()
        city = request.POST.get('city', '').strip()
        postal_code = request.POST.get('postal_code', '').strip()
        country = request.POST.get('country', 'United States').strip()
        payment_method = request.POST.get('payment_method', 'credit_card')
        shipping_method = request.POST.get('shipping_method', 'Standard Courier')

        if not (name and email and phone and address and city and postal_code):
            messages.error(request, "Please fill in all required shipping and contact details.")
            return render(request, 'shop/checkout.html', {'cart': cart})

        subtotal = cart.get_subtotal()
        discount = cart.get_discount()
        shipping_cost = cart.get_shipping()
        total = cart.get_total()

        # Create Order
        order = Order.objects.create(
            customer_name=name,
            customer_email=email,
            customer_phone=phone,
            shipping_address=address,
            city=city,
            postal_code=postal_code,
            country=country,
            payment_method=payment_method,
            shipping_method=shipping_method,
            shipping_cost=shipping_cost,
            subtotal=subtotal,
            discount_amount=discount,
            total_amount=total,
            status='confirmed',
        )

        # Create Order Items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item.get('product'),
                product_title=item['title'],
                variant_name=item.get('variant_name', ''),
                unit_price=item['unit_price_decimal'],
                quantity=item['quantity'],
                total_price=item['total_price_decimal'],
            )

        # Clear cart
        cart.clear()
        messages.success(request, f"Order #{order.order_number} successfully placed!")
        return redirect('order_success', order_number=order.order_number)

    return render(request, 'shop/checkout.html', {'cart': cart})


def order_success_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'shop/order_success.html', {'order': order})


# ==========================================
# THEME SWITCHER & STORE ADMIN
# ==========================================

def set_theme_view(request, theme_id):
    if theme_id in THEME_MAP:
        request.session['active_theme'] = theme_id
        return redirect('demo_home', theme_id=theme_id)
    return redirect('home')


def store_admin_view(request):
    config = StoreConfig.get_solo()
    orders = Order.objects.all()[:20]
    total_revenue = sum(o.total_amount for o in Order.objects.all())
    total_orders = Order.objects.count()
    total_products = Product.objects.count()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update_settings':
            config.store_name = request.POST.get('store_name', config.store_name)
            config.tagline = request.POST.get('tagline', config.tagline)
            config.announcement_text = request.POST.get('announcement_text', config.announcement_text)
            new_theme = request.POST.get('active_theme')
            if new_theme in THEME_MAP:
                config.active_theme = new_theme
                request.session['active_theme'] = new_theme
            config.save()
            messages.success(request, "Store configuration and active default theme updated successfully!")
            return redirect('store_admin')

        elif action == 'update_order_status':
            order_id = request.POST.get('order_id')
            new_status = request.POST.get('status')
            order = get_object_or_404(Order, id=order_id)
            if new_status in dict(Order.STATUS_CHOICES):
                order.status = new_status
                order.save()
                messages.success(request, f"Order #{order.order_number} status changed to '{order.get_status_display()}'.")
            return redirect('store_admin')

    context = {
        'config': config,
        'orders': orders,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'total_products': total_products,
        'theme_choices': THEME_SAMPLES,
    }
    return render(request, 'shop/store_admin.html', context)


@require_GET
def quick_search_api(request):
    """
    Live autocomplete search API for WoodMart-style header search bar.
    Returns matching products with title, category, price, thumbnail, and demo-aware URL.
    """
    q = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()
    
    if not q and not category_slug:
        return JsonResponse({'results': [], 'count': 0})
        
    products = Product.objects.filter(in_stock=True)
    if category_slug:
        products = products.filter(category__slug=category_slug)
        
    if q:
        products = products.filter(
            Q(title__icontains=q) |
            Q(short_description__icontains=q) |
            Q(description__icontains=q) |
            Q(sku__icontains=q) |
            Q(theme_niche__icontains=q)
        )
        
    results = []
    active_theme = request.session.get('active_theme')
    
    for p in products[:10]:
        if active_theme:
            product_url = f"/demo/{active_theme}/product/{p.slug}/"
        else:
            product_url = f"/product/{p.slug}/"

        results.append({
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'url': product_url,
            'category': p.category.name,
            'category_slug': p.category.slug,
            'price': str(p.base_price),
            'image_url': p.image_url,
            'rating': str(p.rating),
            'theme_niche': p.theme_niche,
            'in_stock': p.in_stock,
        })
        
    return JsonResponse({'results': results, 'count': len(results)})

