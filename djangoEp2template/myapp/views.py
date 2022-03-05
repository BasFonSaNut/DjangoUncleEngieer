import datetime
from math import ceil
from itertools import product
from multiprocessing import context
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import LogMessageForm,GeeksForm
from .models import Allproduct,LogMessage
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage
import json
# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Django!")
    
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

def addproduct(request):
    if request.method == 'POST' and request.FILES['imageupload']:
        data = request.POST.copy()
        new = Allproduct()
        new.name = data.get('name')
        new.price = data.get('price')
        new.description = data.get('description')
        new.quantity = data.get('quantity')
        new.unit = data.get('unit')
        new.imageurl = data.get('imageurl')
        # new.image = data.get('image')
        if(data.get('instock') =='checked'):
            new.instock = 1
        else:
            new.instock = 0    
        #################image management ##########################
        file_image = request.FILES['imageupload']
        file_image_name = request.FILES['imageupload'].name.replace(' ','')
        print('file_image :',file_image)
        print('filename :',file_image_name)
        fs = FileSystemStorage()
        filename = fs.save(file_image_name,file_image)
        upload_file_url = fs.url(filename)
        upload_file_url = fs.url(filename)
        print('upload_file_url :',upload_file_url)
        new.image = upload_file_url[6:]
        #################end image management ##########################
        new.save()
        # new = Allproduct()
        # new.name = name
    product = Allproduct.objects.all().order_by('id').reverse() #get all
    # input last ,show first
    # .order_by('id').reverse()
    context ={'product':product} 
    return render(request, "myapp/addproduct.html",context)

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
 