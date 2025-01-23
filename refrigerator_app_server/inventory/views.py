from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, PurchaseHistory, ConsumptionHistory
from .serializers import ProductSerializer, PurchaseHistorySerializer, ConsumptionHistorySerializer
from datetime import date, timedelta

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsumeView(APIView):
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            quantity_to_consume = float(request.data.get('quantity'))
            if product.quantity >= quantity_to_consume:
                product.quantity -= quantity_to_consume
                product.save()
                ConsumptionHistory.objects.create(
                    product=product,
                    quantity=quantity_to_consume
                )
                return Response({'message': 'Quantity consumed successfully'})
            return Response({'error': 'Insufficient quantity'}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

class ExpiryAlertView(APIView):
    def get(self, request):
        today = date.today()
        products = Product.objects.filter(expiration_date__lte=today + timedelta(days=2))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)