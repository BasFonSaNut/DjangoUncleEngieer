import datetime
from math import ceil
import datetime
# from itertools import product
from multiprocessing import context
from pickle import FALSE, TRUE
from statistics import quantiles
from django.forms import JSONField
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import LogMessageForm,GeeksForm,FriendForm
from .models import LogMessage,Friend,BookProduct
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage
import json

from django.shortcuts import HttpResponse
from django.views.generic.edit import CreateView
from django.http import JsonResponse,HttpRequest

from django.core import serializers

# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Django!")

# class SignUpView(CreateView):
#     template_name = 'myapp/signup.html'
#     form_class = Userregister

# def validate_username(request):
#     username = request.GET.get('username', None)
#     data = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     if data['is_taken']:
#         data['error_message'] = 'A user with this username already exists.'
#     return JsonResponse(data)


def testconvert(request):
    result = BookProduct.objects.all().order_by('id').reverse()[:1] 
    # print(type(result))
    for item in result.iterator():
        id = item.id
        bookname = item.bookname
        price = item.price
        # print(id,name,price)
    items = []
    data =  {
        'id': id, 
        'bookname': bookname, 
        'price': price
        }
    items.append(data)
    json_format = json.dumps(items)
    print(json_format)
    # print(type(items))
    
    
    # results = [obj.to_dict() for obj in items]
    # results.sort(key=lambda obj: obj["id"])
    # jsdata = json.dumps({"results": results})
    # print(jsdata)
    
    context={'data' : items }    
    return render(request, "myapp/testconvert.html",context)    
       
def checkNickName(request):
    # request should be ajax and method should be GET.
    # if is_ajax() and request.method == "GET":
    # if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
    nick_name = request.GET.get("nick_name", None)
    # check for the nick name in the database.
    if Friend.objects.filter(nick_name = nick_name).exists():
        # if nick_name found return not valid new friend
        return JsonResponse({"valid":False}, status = 200)
    else:
        # if nick_name not found, then user can create a new friend.
        return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)



def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "myapp/index.html", {"form": form, "friends": friends})


def postFriend(request):
    # request should be ajax and method should be POST.
    # if request.is_ajax and request.method == "POST":
        # get the form data
    form = FriendForm(request.POST)
    # save the data and after fetch the object in instance
    if form.is_valid():
        instance = form.save()
        # print(instance)
        # serialize in new friend object in json
        ser_instance = serializers.serialize('json', [ instance, ])
        # send to client side.
        print(ser_instance)
        return JsonResponse({"instance": ser_instance}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

    
def hello_there(request, name=None):
     return render(
        request,
        'myapp/hello_there.html',
        {
            'name': name,
            
        }
    )
     
def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")   



def displaylog(request):
     return render(request, "myapp/displaylog.html")
 
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.date
            message.save()
            return redirect("displaylog")
            # return redirect("home")
    else:
        return render(request, "myapp/log_message.html", {"form": form})

def greek_view(request):
    context = {}
    context['form'] = GeeksForm()
    return render( request, "myapp/greek.html", context)
    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context    
      
