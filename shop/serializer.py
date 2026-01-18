from rest_framework.serializers import ModelSerializer
from .models import Product, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        fields = ['name', 'is_active', 'created_at']
        model = Category


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = ['name', 'category', 'description', 'price', 'stock', 'is_active', 'created_at']
        model = Product