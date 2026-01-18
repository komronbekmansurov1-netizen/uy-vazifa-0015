from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer
# Create your views here.

class OrderApiView(APIView):
    def get(self):
        orders = Order.objects.all()
        data = OrderSerializer(orders, many=True)
        return Response(data.data)
    
    def post(self, request):
        new_order = OrderSerializer(data=request.data)
        if new_order.is_valid():
            new_order.save()
            return Response(
                {
                    'message': "Order qo'shildi"
                }
            )
        return Response(
            {
                'message': 'ok'
            }
        )
    

class OrderItemApiView(APIView):
    def get(self):
        orders = Order.objects.all()
        data = OrderItemSerializer(orders, many=True)
        return Response(data.data)
    
    def post(self, request):
        new_orderitem = OrderItemSerializer(data=request.data)
        if new_orderitem.is_valid():
            new_orderitem.save()
            return Response(
                {
                    'message': "OrderItem qo'shildi"
                }
            )
        return Response(
            {
                'message': 'ok'
            }
        )