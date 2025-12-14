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

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            image_url=request.POST['image_url'],
            description=request.POST.get('description', ''),
            price=request.POST['price'],
            stock=request.POST['stock'],
            category=request.POST['category'],
            discount=request.POST.get('discount', 0)
        )
        return render(request, 'admin_panel/index.html', {'products': Product.objects.all()})
    return render(request, 'admin_panel/index.html', {'products': Product.objects.all()})