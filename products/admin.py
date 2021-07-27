
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(category)
admin.site.register(product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(ProductImages)

