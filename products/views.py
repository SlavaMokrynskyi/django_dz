from django.shortcuts import get_object_or_404, render,redirect
from products.models import Product

from products.forms.product import ProductForm

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
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('admin_panel')


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('admin_panel')
    product_form = ProductForm()
    return render(request, 'products/add_product.html', {'form': product_form})

def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('admin_panel')
    product_form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': product_form})