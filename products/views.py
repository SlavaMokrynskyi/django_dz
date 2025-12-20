from django.shortcuts import render,redirect
from products.models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_details(request, id):
    product = Product.objects.get(pk=id)
    return render(request,'products/product_details.html', {'product': product})

def admin_panel(request):
    products = Product.objects.all()
    return render(request, 'products/admin-panel.html', {'products': products})

def delete_product(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        if product:
            product.delete()
        else:
            return redirect('admin_panel')
    return redirect('admin_panel')

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
        return redirect('admin_panel')
    return redirect('admin_panel')