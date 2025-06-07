from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Product entry point (choose individual or B2B)
    path('produkty/', views.product_entry_point, name='product_entry'),

    # Cart & checkout
    path('koszyk/', views.cart, name='cart'),
    path('zamowienie/', views.checkout, name='checkout'),

    # Static info pages
    path('kontakt/', views.contact, name='contact'),
    path('o-nas/', views.about, name='about'),
    path('dla-firm/', views.for_business, name='for_business'),
    path('konto-b2b/', views.b2b_account, name='b2b_account'),

    # Legal
    path('regulamin/', views.terms, name='terms'),
    path('polityka-prywatnosci/', views.privacy_policy, name='privacy_policy'),

    # Product lists
    path('produkty/detaliczny/', views.product_list_individual, name='product_list_individual'),
    path('produkty/biznesowy/', views.product_list_b2b, name='product_list_b2b'),

    # Product detail (SEO-friendly slug)
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
