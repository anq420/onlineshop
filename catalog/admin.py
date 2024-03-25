from django.contrib import admin
from catalog.models import Category, Product, Seller, ProductImage, Promo, Discount, Cashback, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'price')
    search_fields = ('article', 'name', 'category__name')


admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(ProductImage)
admin.site.register(Promo)
admin.site.register(Discount)
admin.site.register(Cashback)
admin.site.register(Order)
