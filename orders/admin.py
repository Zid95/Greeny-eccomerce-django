from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(OrderDetail)

admin.site.register(Cart)
admin.site.register(CartDetail)
