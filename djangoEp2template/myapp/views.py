import datetime
from math import ceil
# from itertools import product
from multiprocessing import context
from pickle import FALSE, TRUE
from django.forms import JSONField
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import LogMessageForm,GeeksForm,FriendForm
from .models import Allproduct,LogMessage,Friend,BookProduct
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage
import json

from django.shortcuts import HttpResponse
# from django.views.generic.edit import CreateView
from django.http import JsonResponse,HttpRequest

from django.core import serializers

class Needed(object):
    def __init__(self, name, number):
      self.name = name
      self.number = number

    def to_dict(self):
      return {"name": self.name, "number": self.number}
        
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

def productpage(request):
    return render(request, "myapp/productpage.html")

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
        
def home(request):
    with open('static/myapp/data/books.json') as f:
        jsondata = json.load(f)
        top10 = jsondata[:10]
        totalrecord = len(jsondata)
        totalpage = ceil(totalrecord/10)
        currentpage = 1
        previousPage = 1
        nextPage = 1
    context = {
            'books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
            }     
    return render(request,"myapp/home.html",context)


def pagingitem(request, pageno=None):
    with open('static/myapp/data/books.json') as f:
        jsondata = json.load(f)
        top10 = jsondata[:10]
        totalrecord = len(jsondata)
        totalpage = ceil(totalrecord/10)
        currentpage = pageno
        previousPage = 1
        nextPage = 1
        startrecord = 1
        endrecord = 10
        
        if(pageno == 1):
            top10 = jsondata[:10]
        else:
            startrecord = (pageno-1) * 10
            endrecord = startrecord+10
            top10 = jsondata[startrecord:endrecord]   
                     
        if(pageno>1):
            previousPage = pageno-1
        else:
            previousPage = totalpage
            
        if(pageno<totalpage):
            nextPage = pageno+1
        else:
            nextPage = 1    

    # context ={'books':top10,'totalrecord':totalrecord,'totalpage':range(1,(totalpage+1)),'currentpage':currentpage}     
    return render(
        request,
        'myapp/pagingitem.html',
        {
            'books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
        }
    )


def login(request):
    return render(request,"myapp/login.html")
    
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

def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        newuser = User()
        newuser.username = data.get('email')
        newuser.email = data.get('email')
        newuser.first_name = data.get('first_name')
        newuser.last_name = data.get('last_name')
        newuser.set_password(data.get('password'))
        newuser.save()
        
    users = User.objects.all().order_by('id').reverse() #get all
    # input last ,show first
    # .order_by('id').reverse()
    context ={'users':users} 
    return render(request, "myapp/register.html",context)

def testconvert(request):
    result = BookProduct.objects.all().order_by('id').reverse()[:1] 
    # print(type(result))
    for item in result.iterator():
        id = item.id
        name = item.name
        price = item.price
        # print(id,name,price)
    items = []
    data =  {
        'id': id, 
        'name': name, 
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
        
def addproduct(request):
    if request.method == 'POST' and request.FILES['imageupload']:
        # print(data)
        data = request.POST.copy()
        new = BookProduct()
        new.name = data.get('name')
        new.author = data.get('author')
        new.price = data.get('price')
        new.description = data.get('description')
        new.quantity = data.get('quantity')
        new.unit = data.get('unit')
        
        if data.get('instock') != None:
            new.instock = 1
        else:  
            new.instock = 0         
        # #################image management ##########################
        file_image = request.FILES['imageupload']
        file_image_name = request.FILES['imageupload'].name.replace(' ','')
        new.imagefilename = file_image_name
        new.imageurl = '../static/myapp/images/book/icon/'+file_image_name
        # print('file_image :',file_image)
        # print('filename :',file_image_name)
        fs = FileSystemStorage()
        filename = fs.save(file_image_name,file_image)
        upload_file_url = fs.url(filename)
        # print('upload_file_url :',upload_file_url)
        new.image = upload_file_url[6:]
        
        # #################end image management ##########################
        new.save()
        result = BookProduct.objects.all().order_by('id').reverse()[:1] #get one
        
        items = []
        for item in result.iterator():
            id = item.id
            name = item.name
            price = item.price
            # print(id,name,price)
        
            data =  {
            'id': id, 
            'name': name, 
            'price': price
            }
            # items.append(data)
            
        json_format = json.dumps(data)
        print(json_format)
       
       
        return JsonResponse({"instance": json_format}, status=200)
       
    # except:
    #     return JsonResponse({"error": 'Error'}, status=400)
        
    return JsonResponse({"error": ""}, status=400)
  
    # product = BookProduct.objects.all().order_by('id').reverse() #get all
    
    
    # input last ,show first
    # .order_by('id').reverse()
    # context ={'product':product} 
    # return render(request, "myapp/addproduct.html",context)

def getAllproduct(request):
    product = Allproduct.objects.all() #get all
    context ={'product':product} #dictionary
    return render(request,'myapp/allproduct.html',context)


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
 