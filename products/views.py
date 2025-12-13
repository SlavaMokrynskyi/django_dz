from django.shortcuts import render

products = [
    {
        "id" : 1,
        "name" : "Wireless Headphones",
        "image_url" : "https://www.cornellstore.com/site/Product_images/11041317_media-Midnight-01.jpg",
        "description" : "High-quality wireless headphones with noise cancellation.",
        "price" : 199.99,
        "stock" : 25,
        "category" : "electronics",
        "discount" : 10
    },
    {
        "id" : 2,
        "name" : "Smartwatch",
        "image_url" : "https://www.lapcare.com/cdn/shop/files/Fitso_3_black.jpg?v=1757325785&width=2048",
        "description" : "Feature-packed smartwatch with fitness tracking.",
        "price" : 149.99,
        "stock" : 40,
        "category" : "electronics",
        "discount" : 15
    },
    {
        "id" : 3,
        "name" : "Leather Jacket",
        "image_url" : "https://m.media-amazon.com/images/I/815BFpsSAHL._AC_UY1100_.jpg",
        "description" : "Stylish leather jacket for all seasons.",
        "price" : 249.99,
        "stock" : 10,
        "category" : "clothing",
        "discount" : 20
    },
]

# Create your views here.
def product_list(request):
    return render(request, 'product_list/index.html', {'products': products})

def product_details(request, id):
    return render(request,'product_details/index.html', {'product': products[id - 1]})