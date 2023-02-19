from django.contrib import admin

from .models import Bank, Supplier, BankAccount


admin.site.register(Bank)
admin.site.register(Supplier)
admin.site.register(BankAccount)