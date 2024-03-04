from django.contrib import admin

# Register your models here.
from app.models import *

# class ProductAdminView(admin.ModelAdmin):
#     list_display=['product_category_name']

admin.site.register(ProductCategory)
admin.site.register(Product)

