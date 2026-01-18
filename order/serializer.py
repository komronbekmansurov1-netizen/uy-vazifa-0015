from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem

class OrderSerializer(ModelSerializer):
    class Meta:
        fields = ['user', 'status', 'total_price', 'created_at']
        model = Order

class OrderItemSerializer(ModelSerializer):
    class Meta:
        fields = ['order', 'product', 'quantity', 'price', 'total', 'created_at']
        model = OrderItem