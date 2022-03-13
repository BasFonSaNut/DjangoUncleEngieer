from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BookProduct)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(OrderList)
admin.site.register(OrderPending)