from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'tittle': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'tittle': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
