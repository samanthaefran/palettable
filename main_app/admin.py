from django.contrib import admin
from .models import Product, Color, Looks
# Register your models here.
admin.site.register(Product)

admin.site.register(Color)

admin.site.register(Looks)