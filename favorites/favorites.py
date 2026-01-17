FAVORITE_PRODUCTS_KEY = 'favorite_list'

def get_favorite_products(request):
    return request.session.get(FAVORITE_PRODUCTS_KEY, [])

def get_count_of_favorite_products(request):
    return len(get_favorite_products(request))

def add_product_to_favorites(request, product_id):
    favoriteIds = get_favorite_products(request)
    if product_id not in favoriteIds:
        favoriteIds.append(product_id)
        request.session[FAVORITE_PRODUCTS_KEY] = favoriteIds
    request.session.modified = True

def remove_product_from_favorites(request, product_id):
    favoriteIds = get_favorite_products(request)
    if product_id in favoriteIds:
        favoriteIds.remove(product_id)
        request.session[FAVORITE_PRODUCTS_KEY] = favoriteIds
    request.session.modified = True
