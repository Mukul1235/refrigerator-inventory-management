from django.urls import path
from .views import ProductView, ConsumeView, ExpiryAlertView, ShoppingListView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/consume/<int:pk>/', ConsumeView.as_view()),
    path('products/expiry-alerts/', ExpiryAlertView.as_view()),
    path('shopping-list/', ShoppingListView.as_view(), name='shopping_list'),

]