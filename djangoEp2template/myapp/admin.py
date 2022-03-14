from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header ='BasSaFonNut Django'
admin.site.site_title ='Python Book'
admin.site.index_title = 'Main Admin'
class BookProductAdmin(admin.ModelAdmin):
    list_display=['id','bookname','instock','price','quantity']
    list_editable=['bookname','instock','price','quantity']
admin.site.register(BookProduct,BookProductAdmin)
admin.site.register(Profile)
admin.site.register(Cart)

class OrderListAdmin(admin.ModelAdmin):
    list_display = ['orderid','bookname','total']
admin.site.register(OrderList,OrderListAdmin)

class OrderPendingAdmin(admin.ModelAdmin):
    list_display=['orderid','payment','shipping','slipuploadstatus','slipuploadtime','totalquantity','goodsprice','codprice','shippingprice','totallyprice']
    list_editable=['slipuploadstatus','payment','shipping']
admin.site.register(OrderPending,OrderPendingAdmin)