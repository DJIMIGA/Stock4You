from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SupplierOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'En attente'),
        ('validated', 'Validée'),
        ('delivered', 'Livré'),
        ('cancelled', 'Annulée')
    ])

    def __str__(self):
        return f"Order {self.order_number} - {self.supplier.name}"
