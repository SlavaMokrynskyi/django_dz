from products.models import Product

BASKET_PRODUCTS_KEY = 'basket'

def get_basket_products(request):
    """Return dict mapping product_id (str) -> qty (int)."""
    return request.session.get(BASKET_PRODUCTS_KEY, {})

def get_count_of_basket_products(request):
    return sum(int(q) for q in get_basket_products(request).values())


def add_product_to_basket(request, product_id, qty=1):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return False
    qty = int(qty)
    if qty < 1:
        return False
    # ensure enough stock
    if product.stock < qty:
        return False
    basket = get_basket_products(request).copy()
    key = str(product_id)
    current = int(basket.get(key, 0))
    basket[key] = current + qty
    request.session[BASKET_PRODUCTS_KEY] = basket
    # decrease product stock
    product.stock = product.stock - qty
    product.save()
    request.session.modified = True
    return True


def remove_product_from_basket(request, product_id):
    basket = get_basket_products(request).copy()
    key = str(product_id)
    qty = int(basket.get(key, 0))
    if key in basket:
        del basket[key]
        request.session[BASKET_PRODUCTS_KEY] = basket
        try:
            product = Product.objects.get(pk=product_id)
            product.stock = product.stock + qty
            product.save()
        except Product.DoesNotExist:
            pass
    request.session.modified = True
