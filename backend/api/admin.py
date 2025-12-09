from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

'''
 personaliza como o modelo Order aparece no painel de administração
'''
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user", "createdAt", "totalPrice"
    ]