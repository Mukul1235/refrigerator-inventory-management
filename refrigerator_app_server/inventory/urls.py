from django.urls import path
from .views import ProductView, ConsumeView, ExpiryAlertView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/consume/<int:pk>/', ConsumeView.as_view()),
    path('products/expiry-alerts/', ExpiryAlertView.as_view()),
]