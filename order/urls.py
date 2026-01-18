from django.urls import path
from .views import OrderItemApiView, OrderApiView

urlpatterns = [
    path('orders/', OrderApiView.as_view()),
    path('orderitems/', OrderItemApiView.as_view())
]