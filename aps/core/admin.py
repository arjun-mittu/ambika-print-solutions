from django.contrib import admin
from .models import Item,OrderItem,Order,BillingAddress,Payment,contactme
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(contactme)
