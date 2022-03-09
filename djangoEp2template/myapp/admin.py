from django.contrib import admin
from .models import BookProduct, Cart,Profile
# Register your models here.
admin.site.register(BookProduct)
admin.site.register(Profile)
admin.site.register(Cart)