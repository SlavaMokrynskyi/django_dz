from django.shortcuts import render

from products.models import Product
from favorites.favorites import get_favorite_products, get_count_of_favorite_products

def index(request, filter_by_favorites=False):
    products = Product.objects.all()
    if filter_by_favorites:
        fav_ids = get_favorite_products(request)
        products = products.filter(id__in=fav_ids)

    return render(request, 'home/index.html', {
        'products': products,
        "fav_count": get_count_of_favorite_products(request),
        "fav_ids": get_favorite_products(request),
    })
