from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'total_price', 'created_at']
    list_filter = ['user', 'status']
    search_fields = ['user', 'status']

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'total']
    list_filter = ['order', 'product']
    search_fields = ['order', 'product']

admin.site.register(OrderItem, OrderItemAdmin)