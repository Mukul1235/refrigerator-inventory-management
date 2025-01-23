from celery import shared_task
from datetime import date
from .models import Product

@shared_task
def remove_expired_products():
    today = date.today()
    expired_products = Product.objects.filter(expiration_date__lt=today)
    for product in expired_products:
        product.quantity = 0
        product.save()
        print(f"Removed expired product: {product.name}")