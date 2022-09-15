from django.contrib import admin

from apps.goods.models import PropertyObject, Category, Product, PropertyValue

admin.site.register(PropertyObject)
admin.site.register(PropertyValue)
admin.site.register(Product)
admin.site.register(Category)
