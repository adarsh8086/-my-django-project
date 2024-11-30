# from django.contrib import admin
# from .models import CartItem,Purchase,Product

# Register your models here.


# admin.site.register(CartItem)
# admin.site.register(Purchase)
# admin.site.register(Product)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity', 'created_at')

# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'quantity', 'created_at')








# from django.contrib import admin
# from .models import Product, Purchase

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description')
#     search_fields = ('name',)

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'purchase_date')
#     search_fields = ('user__username', 'product__name')




# from django.contrib import admin
# from .models import CartItem, Purchase, Product

# # Register your models here.
# admin.site.register(CartItem)

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity')  # Customize this as needed

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description')
#     search_fields = ('name',)

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'purchase_date')
#     search_fields = ('user__username', 'product__name')





from django.contrib import admin
from .models import CartItem, Purchase, Product,OrderItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')  # Updated to correct field names

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description',)
    search_fields = ('name',)

   

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'purchase_date')
    search_fields = ('user__username', 'product__name')





class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal')

    

admin.site.register(OrderItem,OrderItemAdmin)