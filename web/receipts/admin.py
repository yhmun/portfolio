from django.contrib import admin
from .models import Receipt, Item

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass