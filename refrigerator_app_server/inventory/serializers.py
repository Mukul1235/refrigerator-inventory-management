from rest_framework import serializers
from .models import Product, PurchaseHistory, ConsumptionHistory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

class ConsumptionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionHistory
        fields = '__all__'