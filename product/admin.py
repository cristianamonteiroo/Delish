from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)

class BrandModelAdmin(admin.ModelAdmin):
    list_display = ("brand", "model")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "description")

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Contact, ContactAdmin)