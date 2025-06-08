from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category


# Home
def home(request):
    return render(request, 'shop/home.html')


# Entry point – lets the user choose between individual and B2B view
def product_entry_point(request):
    return render(request, 'shop/products/entry.html')


# Product list for B2B customers (requires login)
@login_required
def product_list_b2b(request):
    # TODO: Add B2B account verification if needed
    return render(request, 'shop/products/product_list.html', {
        'client_type': 'b2b'
    })

# Product detail view based on SEO-friendly slug
def product_detail(request, slug):
    client_type = request.GET.get('typ', 'individual')  # defaults to individual
    return render(request, 'shop/products/detail.html', {
        'slug': slug,
        'client_type': client_type
    })

# Shopping cart
def cart(request):
    return render(request, 'shop/cart.html')

# Checkout process
def checkout(request):
    return render(request, 'shop/checkout.html')

# Contact page
def contact(request):
    return render(request, 'shop/contact.html')

# About us page
def about(request):
    return render(request, 'shop/about.html')

# Business offer page
def for_business(request):
    return render(request, 'shop/for_business.html')

# B2B account panel (requires login)
@login_required
def b2b_account(request):
    return render(request, 'shop/b2b_account.html')

# Store terms and conditions
def terms(request):
    return render(request, 'shop/legal/terms.html')

# Privacy policy
def privacy_policy(request):
    return render(request, 'shop/legal/privacy.html')

def product_list(request):
    category_id = request.GET.get('kategoria')  # ID kategorii z adresu URL
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category__id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    })