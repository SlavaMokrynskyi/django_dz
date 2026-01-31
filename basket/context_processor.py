from basket.basket import get_count_of_basket_products

def basket_list_count(request):
    return { 'basket_count': get_count_of_basket_products(request) }