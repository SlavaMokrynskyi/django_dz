from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from basket.basket import add_product_to_basket, remove_product_from_basket, get_basket_products
from products.models import Product


def index(request):
    basket = get_basket_products(request)
    product_ids = [int(k) for k in basket.keys()]
    products = Product.objects.filter(id__in=product_ids)
    items = []
    total = 0
    for product in products:
        qty = int(basket.get(str(product.id), 0))
        items.append({'product': product, 'qty': qty, 'subtotal': product.price * qty})
        total += product.price * qty
    return render(request, 'basket/index.html', {'items': items, 'total': total})


def add_product(request, product_id):
    qty = int(request.GET.get('qty', 1))
    success = add_product_to_basket(request, product_id, qty)
    if success:
        messages.success(request, 'Товар додано в кошик')
    else:
        messages.warning(request, 'Не вистачає товару на складі або неправильно вказана кількість')
    referrer = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/'
    return HttpResponseRedirect(referrer)


def remove_product(request, product_id):
    remove_product_from_basket(request, product_id)
    referrer = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/basket'
    return HttpResponseRedirect(referrer)
