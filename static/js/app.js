/**
 * Needletravel Interactive E-Commerce & Multi-Theme Front-End Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initCartDrawer();
  initVariantSelectors();
  initThemeSwitcher();
  initCatalogFilters();
});

// ==========================================
// CSRF Helper
// ==========================================
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// ==========================================
// TOAST NOTIFICATIONS
// ==========================================
function showToast(message, isError = false) {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  if (isError) {
    toast.style.borderColor = '#ef4444';
  }

  const icon = isError ? '⚠️' : '✨';
  toast.innerHTML = `<span>${icon}</span> <div>${message}</div>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3200);
}

// ==========================================
// CART DRAWER CONTROLLER
// ==========================================
function initCartDrawer() {
  const overlay = document.getElementById('cartOverlay');
  const openButtons = document.querySelectorAll('[data-cart-open]');
  const closeButton = document.getElementById('cartCloseBtn');

  if (!overlay) return;

  function openCart() {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    refreshCartDrawer();
  }

  function closeCart() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  openButtons.forEach(btn => btn.addEventListener('click', (e) => {
    e.preventDefault();
    openCart();
  }));

  if (closeButton) {
    closeButton.addEventListener('click', closeCart);
  }

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      closeCart();
    }
  });

  // Global Quick-Add Button Handler
  document.addEventListener('click', async (e) => {
    const quickAdd = e.target.closest('[data-quick-add]');
    if (quickAdd) {
      e.preventDefault();
      const productId = quickAdd.dataset.productId;
      const variantId = quickAdd.dataset.variantId || null;

      try {
        quickAdd.disabled = true;
        const resp = await fetch('/api/cart/add/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify({ product_id: productId, variant_id: variantId, quantity: 1 })
        });
        const data = await resp.json();
        quickAdd.disabled = false;

        if (data.success) {
          updateCartBadges(data.cart.count);
          renderCartDrawerHTML(data.cart);
          showToast(data.message);
          openCart();
        } else {
          showToast(data.error || 'Failed to add item', true);
        }
      } catch (err) {
        quickAdd.disabled = false;
        showToast('Network error while adding to bag', true);
      }
    }
  });

  // Coupon apply
  const couponBtn = document.getElementById('cartApplyCouponBtn');
  const couponInput = document.getElementById('cartCouponInput');
  if (couponBtn && couponInput) {
    couponBtn.addEventListener('click', async (e) => {
      e.preventDefault();
      const code = couponInput.value.trim();
      if (!code) return;

      try {
        couponBtn.disabled = true;
        const resp = await fetch('/api/cart/coupon/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify({ code })
        });
        const data = await resp.json();
        couponBtn.disabled = false;

        if (data.success) {
          showToast(data.message);
          renderCartDrawerHTML(data.cart);
        } else {
          showToast(data.message || 'Invalid coupon', true);
        }
      } catch (err) {
        couponBtn.disabled = false;
        showToast('Error applying coupon', true);
      }
    });
  }
}

async function refreshCartDrawer() {
  try {
    const resp = await fetch('/api/cart/');
    const cartData = await resp.json();
    updateCartBadges(cartData.count);
    renderCartDrawerHTML(cartData);
  } catch (err) {
    console.error('Error fetching cart data:', err);
  }
}

function updateCartBadges(count) {
  const badges = document.querySelectorAll('.cart-count-badge');
  badges.forEach(b => {
    b.textContent = count;
  });
}

function renderCartDrawerHTML(cart) {
  const itemsContainer = document.getElementById('cartDrawerItems');
  const subtotalElem = document.getElementById('cartSubtotal');
  const discountRow = document.getElementById('cartDiscountRow');
  const discountElem = document.getElementById('cartDiscount');
  const shippingElem = document.getElementById('cartShipping');
  const totalElem = document.getElementById('cartTotal');
  const emptyMessage = document.getElementById('cartEmptyMessage');
  const footerElem = document.getElementById('cartDrawerFooter');

  if (!itemsContainer) return;

  if (cart.items.length === 0) {
    itemsContainer.innerHTML = '';
    if (emptyMessage) emptyMessage.style.display = 'block';
    if (footerElem) footerElem.style.display = 'none';
    return;
  }

  if (emptyMessage) emptyMessage.style.display = 'none';
  if (footerElem) footerElem.style.display = 'flex';

  let html = '';
  cart.items.forEach(item => {
    html += `
      <div class="cart-item-row" data-key="${item.key}">
        <img src="${item.image_url}" alt="${item.title}" class="cart-item-thumb">
        <div class="cart-item-details">
          <a href="/product/${item.slug}/" class="cart-item-title">${item.title}</a>
          ${item.variant_name ? `<span class="cart-item-variant">${item.variant_name}</span>` : ''}
          <div class="cart-item-price">$${item.unit_price}</div>
          <div class="cart-item-bottom">
            <div class="quantity-stepper" style="transform: scale(0.9); transform-origin: left;">
              <button type="button" class="qty-btn" onclick="updateItemQuantity('${item.key}', ${item.quantity - 1})">-</button>
              <span class="qty-input" style="line-height: 38px;">${item.quantity}</span>
              <button type="button" class="qty-btn" onclick="updateItemQuantity('${item.key}', ${item.quantity + 1})">+</button>
            </div>
            <button type="button" class="cart-item-remove-btn" onclick="removeItemFromCart('${item.key}')">Remove</button>
          </div>
        </div>
      </div>
    `;
  });

  itemsContainer.innerHTML = html;

  if (subtotalElem) subtotalElem.textContent = `$${cart.subtotal}`;
  if (shippingElem) shippingElem.textContent = cart.shipping === '0.00' ? 'FREE' : `$${cart.shipping}`;
  if (totalElem) totalElem.textContent = `$${cart.total}`;

  if (discountRow && discountElem) {
    if (parseFloat(cart.discount) > 0) {
      discountRow.style.display = 'flex';
      discountElem.textContent = `-$${cart.discount} (${cart.coupon_code})`;
    } else {
      discountRow.style.display = 'none';
    }
  }
}

window.updateItemQuantity = async function(key, newQty) {
  try {
    const resp = await fetch('/api/cart/update/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({ key, quantity: newQty })
    });
    const data = await resp.json();
    if (data.success) {
      updateCartBadges(data.cart.count);
      renderCartDrawerHTML(data.cart);
    }
  } catch (err) {
    showToast('Failed to update quantity', true);
  }
};

window.removeItemFromCart = async function(key) {
  try {
    const resp = await fetch('/api/cart/remove/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({ key })
    });
    const data = await resp.json();
    if (data.success) {
      updateCartBadges(data.cart.count);
      renderCartDrawerHTML(data.cart);
      showToast('Item removed from cart');
    }
  } catch (err) {
    showToast('Failed to remove item', true);
  }
};

// ==========================================
// VARIANT & SWATCH SELECTOR (PRODUCT DETAIL)
// ==========================================
function initVariantSelectors() {
  const detailForm = document.getElementById('productDetailForm');
  if (!detailForm) return;

  const priceElem = document.getElementById('detailDynamicPrice');
  const basePrice = parseFloat(detailForm.dataset.basePrice || '0');
  const variantInput = document.getElementById('selectedVariantId');
  const variantNameLabel = document.getElementById('selectedVariantNameLabel');

  const swatches = document.querySelectorAll('[data-variant-swatch]');
  const gaugeBtns = document.querySelectorAll('[data-variant-gauge]');

  function selectVariant(elem) {
    const variantId = elem.dataset.variantId;
    const variantName = elem.dataset.variantName;
    const priceAdjustment = parseFloat(elem.dataset.priceAdjustment || '0');

    // Update active class
    if (elem.dataset.variantSwatch !== undefined) {
      swatches.forEach(s => s.classList.remove('active'));
    } else if (elem.dataset.variantGauge !== undefined) {
      gaugeBtns.forEach(g => g.classList.remove('active'));
    }
    elem.classList.add('active');

    // Update hidden field & label
    if (variantInput) variantInput.value = variantId;
    if (variantNameLabel) variantNameLabel.textContent = variantName;

    // Recalculate price
    const finalPrice = basePrice + priceAdjustment;
    if (priceElem) {
      priceElem.textContent = `$${finalPrice.toFixed(2)}`;
    }
  }

  swatches.forEach(s => s.addEventListener('click', () => selectVariant(s)));
  gaugeBtns.forEach(g => g.addEventListener('click', () => selectVariant(g)));

  // Detail page Add to Cart submit
  detailForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const productId = detailForm.dataset.productId;
    const variantId = variantInput ? variantInput.value : null;
    const qtyInput = document.getElementById('detailQuantity');
    const quantity = qtyInput ? parseInt(qtyInput.value) : 1;
    const submitBtn = detailForm.querySelector('button[type="submit"]');

    try {
      if (submitBtn) submitBtn.disabled = true;
      const resp = await fetch('/api/cart/add/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ product_id: productId, variant_id: variantId, quantity })
      });
      const data = await resp.json();
      if (submitBtn) submitBtn.disabled = false;

      if (data.success) {
        updateCartBadges(data.cart.count);
        renderCartDrawerHTML(data.cart);
        showToast(data.message);
        const overlay = document.getElementById('cartOverlay');
        if (overlay) overlay.classList.add('open');
      } else {
        showToast(data.error || 'Failed to add item', true);
      }
    } catch (err) {
      if (submitBtn) submitBtn.disabled = false;
      showToast('Error adding to bag', true);
    }
  });

  // Quantity adjusters on detail page
  const minusBtn = document.getElementById('qtyMinus');
  const plusBtn = document.getElementById('qtyPlus');
  const qtyInput = document.getElementById('detailQuantity');
  if (minusBtn && plusBtn && qtyInput) {
    minusBtn.addEventListener('click', () => {
      let val = parseInt(qtyInput.value) || 1;
      if (val > 1) qtyInput.value = val - 1;
    });
    plusBtn.addEventListener('click', () => {
      let val = parseInt(qtyInput.value) || 1;
      qtyInput.value = val + 1;
    });
  }
}

// ==========================================
// INTERACTIVE THEME SWITCHER
// ==========================================
function initThemeSwitcher() {
  const chips = document.querySelectorAll('.theme-chip');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const themeId = chip.dataset.theme;
      if (!themeId) return;

      // Update active theme in UI immediately
      document.documentElement.setAttribute('data-theme', themeId);
      chips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');

      // Update URL without page reload or navigate
      const url = new URL(window.location);
      url.searchParams.set('theme', themeId);
      window.history.replaceState({}, '', url);

      // Save to server session
      fetch(`/set-theme/${themeId}/`);

      showToast(`Sample theme switched to "${chip.dataset.name || themeId}"`);
    });
  });
}

// ==========================================
// CATALOG INSTANT FILTER
// ==========================================
function initCatalogFilters() {
  const searchInput = document.getElementById('catalogLiveSearch');
  const inStockCheck = document.getElementById('catalogInStock');
  const sortSelect = document.getElementById('catalogSort');

  if (!searchInput && !inStockCheck && !sortSelect) return;

  function applyFilters() {
    const params = new URLSearchParams(window.location.search);
    if (searchInput && searchInput.value.trim()) {
      params.set('q', searchInput.value.trim());
    } else {
      params.delete('q');
    }

    if (inStockCheck) {
      if (inStockCheck.checked) {
        params.set('in_stock', 'true');
      } else {
        params.delete('in_stock');
      }
    }

    if (sortSelect) {
      params.set('sort', sortSelect.value);
    }

    window.location.search = params.toString();
  }

  let searchTimeout;
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        applyFilters();
      }
    });
  }

  if (inStockCheck) {
    inStockCheck.addEventListener('change', applyFilters);
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', applyFilters);
  }
}
