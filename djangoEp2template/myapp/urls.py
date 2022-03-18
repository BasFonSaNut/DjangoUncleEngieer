from django.urls import path
from . import views

urlpatterns =[
   
    path('', views.view_Home, name="home-page"),
    path("pagingitem/<int:pageno>",views.view_PagingItem,name="pagingitem"),
    path("aboutus/", views.view_Aboutus, name="aboutus"),
    path("contact/", views.view_Contactus, name="contact"),
    
    path("register/", views.view_Register, name="register"),

    path("addproduct/<int:pageno>",views.view_AddProduct,name="addproduct-page"),
        
    path('AddtoCart/<int:bid>', views.view_AddtoCart , name='addtocart'),
    path('mycart/', views.view_MyCart, name='mycart-page'),
    path('checkout/', views.view_Checkout, name='checkout-page'),
    path('orderlist/', views.view_OrderListPage, name='orderlist-page'),
    path('allorderlist/', views.view_AllOrderListPage, name='allorderlist-page'),
    path('uploadslip/<str:orderid>', views.view_UploadSlip, name='uploadslip-page'),
    path('updatetracking/<str:orderid>', views.view_UpdateTracking, name='updatetracking'),
    path('frmupdatetracking/<str:orderid>', views.view_FRMtracking, name='frmupdatetracking'),
    
    # ================Ajax=========================
    path('updatecheckslip/',  views.view_OrderCrudSlipChecked.as_view(), name='updatecheckslip_ajax'),
    path('updatepayment/',  views.OrderCrudPaidChecked.as_view(), name='updatepayment_ajax'),
    path('orderlistajax/',  views.view_OrderCrudView.as_view(), name='orderlistajax')
]