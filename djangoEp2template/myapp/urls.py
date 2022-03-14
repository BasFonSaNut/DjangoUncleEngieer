from django.urls import path
from myapp import views
   

urlpatterns =[
    path('', views.home, name="home-page"),
    path("register/", views.register, name="register"),
    
    path("pagingitem/<int:pageno>",views.pagingitem,name="pagingitem"),
    path("addproductpaging/<int:pageno>",views.addproductpaging,name="addproductpaging"),
    path("productpage/", views.productpage, name="productpage"),
    path("post/ajax/addproduct/", views.addproduct, name="addproduct"),
    
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contact/", views.contact, name="contact"),
    path('AddtoCart/<int:bid>', views.AddtoCart , name='addtocart'),
    path('MyCart/', views.MyCart, name='mycart-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('orderlist/', views.OrderListPage, name='orderlist-page'),
    path('allorderlist/', views.AllOrderListPage, name='allorderlist-page'),
    path('uploadslip/<str:orderid>', views.UploadSlip, name='uploadslip-page')
    
    
    # path('addfriend', fortestviews.indexView,name="indexView"),
    # path('post/ajax/friend', fortestviews.postFriend, name = "post_friend"),
    # path('get/ajax/validate/nickname', fortestviews.checkNickName, name = "validate_nickname"),
    # path("testconvert/",fortestviews.testconvert,name='testconvert')
    # re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    # re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username')
    # path("log/", views.log_message, name="log"),
    #path("displaylog/", home_list_view, name="displaylog")
    # path("displaylog/", views.displaylog, name="displaylog")
    #path("greek/", views.form.greek_view,name="greek"),
    #path("hello_there/<str:name>",views.hello_there,name="hello_there"),
]