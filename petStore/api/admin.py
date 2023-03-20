from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Pet)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderStatus)