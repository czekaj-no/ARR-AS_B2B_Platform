from django.contrib import admin
from .models import Category, Product, ProductVariant, UserProfile, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vat_rate')
    list_filter = ('category',)

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'weight', 'price_b2c_brutto', 'price_b2b_netto')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_b2b', 'activated', 'company_name', 'nip')
    list_filter = ('is_b2b', 'activated')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'status', 'created_at')
    list_filter = ('status', 'delivery_method')
    search_fields = ('full_name', 'email', 'company_name')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'variant', 'quantity')