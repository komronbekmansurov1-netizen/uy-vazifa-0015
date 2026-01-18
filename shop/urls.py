from django.urls import path
from .views import CategoryApiView, ProductApiView

urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('products/', ProductApiView.as_view())
]