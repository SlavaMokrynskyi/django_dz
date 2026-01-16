from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from products.forms.product import ProductForm
from products.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {"products": products})


def product_details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, "products/product_details.html", {"product": product})


def admin_panel(request):
    products = Product.objects.all()
    return render(request, "products/admin-panel.html", {"products": products})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    messages.success(request, "Product deleted successfully")
    return redirect("admin_panel")


def add_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product added successfully")
            return redirect("admin_panel")
    product_form = ProductForm()
    return render(request, "products/add_product.html", {"form": product_form})


def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product updated successfully")
            return redirect("admin_panel")
    product_form = ProductForm(instance=product)
    return render(request, "products/update_product.html", {"form": product_form})
