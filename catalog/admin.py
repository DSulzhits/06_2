from django.contrib import admin
from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'sign_of_current_version')
