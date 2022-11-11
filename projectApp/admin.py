from django.contrib import admin
from .models import ProductMain,ProductColor,productImage


# Register your models here.

admin.site.register(ProductMain)
admin.site.register(productImage)
admin.site.register(ProductColor)
