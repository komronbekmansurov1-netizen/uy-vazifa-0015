from django.contrib import admin
from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['name', 'is_active']
    search_fields = ['name', 'is_active']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'price', 'stock', 'is_active', 'created_at']
    list_filter = ['name', 'category', 'is_active']
    search_fields = ['name', 'category', 'is_active']

admin.site.register(Product, ProductAdmin)