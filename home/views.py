from django.shortcuts import render

from products.models import Product
from favorites.favorites import get_favorite_products, get_count_of_favorite_products

def index(request, filter_by_favorites=False):
    products = Product.objects.all()

    filter_text = request.GET.get("filter_search", "")
    selected_category = request.GET.get('category', 'all')
    
    if filter_by_favorites:
        fav_ids = get_favorite_products(request)
        products = products.filter(id__in=fav_ids)

    if filter_text:
        products = products.filter(name__icontains=filter_text)

    if selected_category != 'all' and selected_category:
        products = products.filter(category=selected_category)

    return render(request, 'home/index.html', {
        'products': products,
        'filter_by_favorites': filter_by_favorites,
        'selected_category': selected_category,  # Додано цей рядок
        'fav_ids': get_favorite_products(request),
    })