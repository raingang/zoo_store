from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    '''
    Модель отображения категории в админке
    '''
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    '''
    Модель отображения товара в админке
    '''
    list_display = ['name', 'slug', 'price', 'copies',
                    'discount', 'created', 'updated', 'category']
    list_filter = ['category', 'created', 'updated']
    list_editable = ['price', 'copies', 'discount']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
