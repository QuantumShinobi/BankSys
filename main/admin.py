from django.contrib import admin
from .models import Transaction, User
# Register your models here.
admin.site.register(User)
admin.site.register(Transaction)
