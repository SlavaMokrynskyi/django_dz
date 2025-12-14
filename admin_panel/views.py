from django.shortcuts import render
from products.models import Product

# Create your views here.
def admin_panel(request):
    products = Product.objects.all()
    return render(request, 'admin_panel/index.html', {'products': products})

def delete_product(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        if product:
            product.delete()
        else:
            return render(request, 'admin_panel/index.html', {'error': 'Product not found.'})
    return render(request, 'admin_panel/index.html', {'products': Product.objects.all()})