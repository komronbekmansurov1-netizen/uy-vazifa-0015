from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
# Create your views here.

class CategoryApiView(APIView):
    def get(self):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True)
        return Response(data.data)

    def post(self, request):
        new_category = CategorySerializer(data=request.data)
        if new_category.is_valid():
            new_category.save()
            return Response(
                {
                    'message': "Category qo'shildi"
                }
            )
        return Response(
            {
                'message': 'ok'
            }
        )
    

class ProductApiView(APIView):
    def get(self):
        products = Product.objects.all()
        data = ProductSerializer(products, many=True)
        return Response(data.data)
    
    def post(self, request):
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(
                {
                    'message': "Product qo'shildi"
                }
            )
        return Response(
            {
                'message': 'ok'
            }
        )