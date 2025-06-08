from django.db import models
from django.conf import settings

# 🟫 Kategorie produktów: pierogi, naleśniki, kluski, krokiety
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 🛍️ Produkt (główne dane)
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    image_main = models.ImageField(upload_to='products/')
    vat_rate = models.DecimalField(max_digits=4, decimal_places=2, default=8.0)  # np. 8%

    def __str__(self):
        return self.name

# 📦 Wariant wagowy (każdy produkt ma różne wagi i ceny)
class ProductVariant(models.Model):
    GRAM_CHOICES = [
        (500, '500g'),
        (1000, '1kg'),
        (2000, '2kg'),
        (3000, '3kg'),
        (5000, '5kg'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    weight = models.PositiveIntegerField(choices=GRAM_CHOICES)
    price_b2c_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    price_b2b_netto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.weight}g"

    def price_b2b_brutto(self):
        return round(self.price_b2b_netto * (1 + (self.product.vat_rate / 100)), 2)

# 👤 Profil użytkownika (czy to klient b2b)
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_b2b = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)  # aktywacja przez admina
    company_name = models.CharField(max_length=255, blank=True, null=True)
    nip = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

# 🧾 Zamówienie
class Order(models.Model):
    ORDER_STATUS = [
        ('new', 'Nowe'),
        ('ready', 'Gotowe do odbioru'),
        ('completed', 'Zrealizowane'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    nip = models.CharField(max_length=20, blank=True, null=True)
    delivery_method = models.CharField(max_length=20, choices=[('pickup', 'Odbiór osobisty'), ('delivery', 'Dostawa')])
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='new')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zamówienie #{self.id}"

# 🧺 Elementy zamówienia
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.variant} x {self.quantity}"
