from django.urls import path
from . import views
from .models import LogMessage
#from .views import home,about,contact,log_message,hello_there,addproduct
from myapp import views
# from myapp.views import (
#     indexView,
#     postFriend, 
# )
    
home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="myapp/displaylog.html",
)

urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    
    path("register/", views.register, name="register"),
    path("pagingitem/<int:pageno>",views.pagingitem,name="pagingitem"),
    path("addproductpaging/<int:pageno>",views.addproductpaging,name="addproductpaging"),
    
    path('addfriend', views.indexView,name="indexView"),
    path('post/ajax/friend', views.postFriend, name = "post_friend"),
    path('get/ajax/validate/nickname', views.checkNickName, name = "validate_nickname"),
    
    path("productpage/", views.productpage, name="productpage"),
    path("post/ajax/addproduct/", views.addproduct, name="addproduct"),
    path("testconvert/",views.testconvert,name='testconvert')
    # re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    # re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username')
    # path("log/", views.log_message, name="log"),
    #path("displaylog/", home_list_view, name="displaylog")
    # path("displaylog/", views.displaylog, name="displaylog")
    #path("greek/", views.form.greek_view,name="greek"),
    #path("hello_there/<str:name>",views.hello_there,name="hello_there"),
]