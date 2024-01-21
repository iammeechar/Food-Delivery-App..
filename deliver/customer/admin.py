from django.contrib import admin
from .models import MenuItems, Category, OrderModel

#added the menu items, categories and order model to the admin page.
admin.site.register(MenuItems)
admin.site.register(Category)
admin.site.register(OrderModel)
