from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from users.models import User
from users.models import Clients, Basket, Basket_items, Goods, Stock, Order_details, Orders

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Clients)
admin.site.register(Basket)
admin.site.register(Basket_items)
admin.site.register(Goods)
admin.site.register(Stock)
admin.site.register(Order_details)
admin.site.register(Orders)
