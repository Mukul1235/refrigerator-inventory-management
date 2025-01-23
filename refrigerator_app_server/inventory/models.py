from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, choices=[('liter', 'Liter'), ('gram', 'Gram')])
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class PurchaseHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    purchase_date = models.DateField(auto_now_add=True)

class ConsumptionHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    consumption_date = models.DateField(auto_now_add=True)