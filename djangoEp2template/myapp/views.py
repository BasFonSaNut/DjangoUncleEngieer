from math import ceil
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BookProduct,Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import json
def aboutus(request):
    return render(request,'myapp/aboutus.html')

def contact(request):
    return render(request,'myapp/contact.html')
    
def productpage(request):
    Books = BookProduct.objects.all().order_by('id').reverse() #get all
    top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    totalrecord = len(Books)
    totalpage = ceil(totalrecord/10)
    currentpage = 1
    previousPage = totalpage
    nextPage = 2
    
    
    return render(
        request,
        'myapp/productpage.html',
        {
            'Books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
        }
    )
    

def home(request):
    # with open('static/myapp/data/books.json') as f:
        # ขึ้นระบบจริงใช้ real path '/home/ajaxjson/djangoEp2template/static/myapp/data/books.json
        # jsondata = json.load(f)
        # # output_dict = [x for x in jsondata if x['quantity'] > '10']  json filter
        # top10 = jsondata[:10]
        # totalrecord = len(jsondata)
        # totalpage = ceil(totalrecord/10)
    # top10 = BookProduct.objects.filter(instock=False)
    # preorder = BookProduct.objects.filter(quantity__lt=0)#less than ,gt greater than
    # preorder = BookProduct.objects.filter(quantity__lte=0) #less than or equal
    top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    totalrecord = BookProduct.objects.all().count()
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

def addproductpaging(request, pageno=None):
    if request.user.profile.usertype != 'admin':
        redirect('home')
    # input last ,show first
    # .order_by('id').reverse()
    Books = BookProduct.objects.all().order_by('id').reverse() #get all
    top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    totalrecord = len(Books)
    totalpage = ceil(totalrecord/10)
    currentpage = pageno
    previousPage = 1
    nextPage = 1
    startrecord = 1
    endrecord = 10
    
    if(pageno == 1):
        top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    else:
        startrecord = (pageno-1) * 10
        endrecord = startrecord+10
        top10 = BookProduct.objects.all().order_by('id').reverse()[startrecord:endrecord]   
                    
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
        'myapp/addproductpaging.html',
        {
            'Books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
        }
    )
    
def pagingitem(request, pageno=None):
    # with open('static/myapp/data/books.json') as f:
    #     # '/home/ajaxjson/djangoEp2template/static/myapp/data/books.json
    #     jsondata = json.load(f)
    #     top10 = jsondata[:10]
    #     totalrecord = len(jsondata)
    top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    totalrecord = BookProduct.objects.all().count()
    totalpage = ceil(totalrecord/10)
    currentpage = pageno
    previousPage = 1
    nextPage = 1
    startrecord = 1
    endrecord = 10
    
    if(pageno == 1):
        # top10 = jsondata[:10]
        top10 = BookProduct.objects.all().order_by('id').reverse()[:10]
    else:
        startrecord = (pageno-1) * 10
        endrecord = startrecord+10
        # top10 = jsondata[startrecord:endrecord]   
        top10 = BookProduct.objects.all().order_by('id').reverse()[startrecord:endrecord]            
    if(pageno>1):
        previousPage = pageno-1
    else:
        previousPage = totalpage
        
    if(pageno<totalpage):
        nextPage = pageno+1
    else:
        nextPage = 1    
   
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

def register(request):
    
    if request.method == 'POST':
        data = request.POST.copy()
        newuser = User()
        newuser.username = data.get('username')
        newuser.email = data.get('email')
        newuser.first_name = data.get('first_name')
        newuser.last_name = data.get('last_name')
        newuser.set_password(data.get('password'))
        newuser.save()
        
        profile = Profile()
        profile.user = User.objects.get(username=data.get('username'))
        profile.save()
        
        # from django.contrib.auth import authenticate,login ,for auto login after register
        user = authenticate(username=data.get('username'),password=data.get('password'))
        login(request,user)
        # home(request)
        # users = User.objects.all().order_by('id').reverse() #get all
        # input last ,show first
        # .order_by('id').reverse()
        # context ={'users':users} 
    return render(request, "myapp/register.html")
 
def addproduct(request):
    if request.user.profile.usertype != 'admin':
        redirect('home')
    if request.method == 'POST' and request.FILES['imageupload']:
        # print(data)
        data = request.POST.copy()
        new = BookProduct()
        new.bookname = data.get('bookname')
        new.author = data.get('author')
        new.price = data.get('price')
        new.description = data.get('description')
        new.quantity = data.get('quantity')
        new.unit = data.get('unit')
        # new.instock = data.get('instock')
        instockword = ''
        if data.get('instock') != None:
             new.instock = True
             instockword = 'มีสินค้า'
        else:  
            new.instock = False 
            instockword = 'สินค้าหมด'
            
        new.image = request.FILES['imageupload']            
        new.save()
        result = BookProduct.objects.all().order_by('id').reverse()[:1] #get one
        
        # items = [] use later in case multiple record
        # convert list to dict
        for item in result.iterator():
            id = item.id
            bookname = item.bookname
            author = item.author
            price = item.price
            quantity = item.quantity
            unit = item.unit
            
            # print(id,name,price)
        
            data =  {
            'id': id, 
            'bookname': bookname, 
            'author':author,
            'price': price,
            'quantity': quantity,
            'unit' : unit,
            'instock' : instockword
            
            }
        # items.append(data) use later in case multiple records
        
        #convert dict to json    
        json_format = json.dumps(data)
        # print(json_format)
        return JsonResponse({"instance": json_format}, status=200)
       
    # except:
    #     return JsonResponse({"error": 'Error'}, status=400)
        
    return JsonResponse({"error": ""}, status=400)
  
    # product = BookProduct.objects.all().order_by('id').reverse() #get all
    
    
    # input last ,show first
    # .order_by('id').reverse()
    # context ={'product':product} 
    # return render(request, "myapp/addproduct.html",context)