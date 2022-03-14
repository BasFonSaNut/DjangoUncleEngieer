from datetime import datetime
from math import ceil
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

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
        redirect('home-page')
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
        
    return JsonResponse({"error": ""}, status=400)
  
def AddtoCart(request,bid):
    username = request.user.username
    user = User.objects.get(username=username)
    check = BookProduct.objects.get(id=bid)
    
    try:
        # if Cart.objects.filter(user=user,bookid=bid).exists():
        #case mycart exist
        newcart = Cart.objects.get(user=user,bookid=bid)
        newquan = newcart.quantity+1
        calculate = newcart.price * newquan
        newcart.quantity = newquan
        newcart.total = calculate
        newcart.save()
        
        sumtotal=0
        sumquan =0
        cartRec = Cart.objects.filter(user=user)
        sumquan = sum([c.quantity for c in cartRec]) 
        # sumtotal = sum([c.total for c in count]) 
        
        cartRec = Cart.objects.filter(user=user)
        sumtotal = sum([c.total for c in cartRec])
         
        updateprofile = Profile.objects.get(user=user)
        updateprofile.cartquan = sumquan
        updateprofile.sumtotal = sumtotal
            
        return redirect('home-page')
       
           
    except:
        newcart = Cart()
        newcart.user = user
        newcart.bookid = bid
        newcart.bookname = check.bookname
        newcart.quantity = 1
        newcart.price = check.price
        calculate = check.price * 1
        newcart.total = calculate
        newcart.save()
        
        sumtotal=0
        sumquan =0
        cartRec = Cart.objects.filter(user=user)
        sumquan = sum([c.quantity for c in cartRec]) 
        # sumtotal = sum([c.total for c in count]) 
        
        cartRec = Cart.objects.filter(user=user)
        sumtotal = sum([c.total for c in cartRec])
         
        updateprofile = Profile.objects.get(user=user)
        updateprofile.cartquan = sumquan
        updateprofile.sumtotal = sumtotal
        updateprofile.save()
        return redirect('home-page')
        
def MyCart(request):
    username = request.user.username
    user = User.objects.get(username=username)
    status = ''
    if request.method == 'POST':
        data = request.POST.copy()
        print(data.get('state'))
        if data.get('state') == 'dodelete':
        
            bookid = data.get('bookid')
            item = Cart.objects.get(user=user,bookid=bookid)
            item.delete()
            
            # update total,count at profile
            cartRec = Cart.objects.filter(user=user)
            sumtotal = sum([c.total for c in cartRec])
            sumquan = sum([c.quantity for c in cartRec])
            
            updateprofile = Profile.objects.get(user=user)
            updateprofile.cartquan = sumquan
            updateprofile.sumtotal = sumtotal
            updateprofile.save()
            status='deleted'
            
        if data.get('state') == 'doupdate':
            
            bookid = data.get('bookid')
            quantity = int(data.get('quantity'))
            item = Cart.objects.get(user=user,bookid=bookid)
            item.quantity = quantity
            calculate = item.price * quantity
            item.total = calculate
            item.save()
            
            # update total,count at profile
            cartRec = Cart.objects.filter(user=user)
            sumtotal = sum([c.total for c in cartRec])
            sumquan = sum([c.quantity for c in cartRec])
            
            updateprofile = Profile.objects.get(user=user)
            updateprofile.cartquan = sumquan
            updateprofile.sumtotal = sumtotal
            updateprofile.save()
            status='updated'
        if data.get('state') == 'dodeleteall':
            Cart.objects.filter(user=user).delete()
            updateprofile = Profile.objects.get(user=user)
            updateprofile.cartquan = 0
            updateprofile.sumtotal = 0
            updateprofile.save()
            status='deletedall'
                
    mycart = Cart.objects.filter(user=user)
    context = {'mycart': mycart,'status':status} 
    
    return render(request,'myapp/mycart.html',context)

def checkout(request): 
    username = request.user.username
    user = User.objects.get(username=username)
    if request.method == 'POST':
        data = request.POST.copy()
        fullname = data.get('fullname')
        tel = data.get('tel')
        address = data.get('address')
        shipping = data.get('shipping')
        payment = data.get('payment')
        note = data.get('note')
        page = data.get('page')
        if page =='information':
            orderaddress ={}
            orderaddress['fullname'] = fullname
            orderaddress['tel'] = tel
            orderaddress['address'] = address
            orderaddress['shipping'] = shipping
            orderaddress['payment'] = payment
            orderaddress['note'] = note
            orderaddress['email'] = user.email
            
            mycart = Cart.objects.filter(user=user)
            context = {'mycart': mycart,'address':orderaddress} 
            
            return render(request,'myapp/checkout2.html',context)
        
        if page =='confirmation':
            # print('confirmation')
            # print(data)
            dt = datetime.now().strftime('%Y%m%d%H%M%S')
            genorderid = 'OD'+str(user.id).zfill(4)+dt
            
            orderpending = OrderPending()
            orderpending.orderid = genorderid
            orderpending.user = user
            orderpending.fullname = fullname
            orderpending.tel = tel
            orderpending.address = address
            orderpending.shipping = shipping
            orderpending.payment = payment
            orderpending.note = note
            orderpending.shippingstatus = False
            orderpending.paymentstatus = False
            orderpending.save()
            
            mycart = Cart.objects.filter(user=user)
            for cartitem in mycart:
                itempending= OrderList()
                itempending.orderid = genorderid
                itempending.bookid = cartitem.bookid
                itempending.bookname = cartitem.bookname
                itempending.price = cartitem.price
                itempending.quantity = cartitem.quantity
                itempending.total = cartitem.total
            
                itempending.shippingstatus = False
                itempending.orderdate = cartitem.stamp
                itempending.save()
            
            
            updateprofile = Profile.objects.get(user=user)
            updateprofile.cartquan = 0
            updateprofile.sumtotal = 0
            updateprofile.save()
            
            Cart.objects.filter(user=user).delete()
           
            return redirect('mycart-page')
        
    return render(request,'myapp/checkout1.html')

def OrderListPage(request):
    username = request.user.username
    user = User.objects.get(username=username)
    order=OrderPending.objects.filter(user=user)
    for od in order:
        orderid = od.orderid
        odlist = OrderList.objects.filter(orderid=orderid)
        sumtotal = sum([c.total for c in odlist])
        sumquan = sum([c.quantity for c in odlist])
        od.total = sumtotal
        od.quantity = sumquan
            
    context = {'orderlists':order}
    return render(request,'myapp/orderlist.html',context)


def AllOrderListPage(request):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    order=OrderPending.objects.all()
    for od in order:
        orderid = od.orderid
        odlist = OrderList.objects.filter(orderid=orderid)
        sumtotal = sum([c.total for c in odlist])
        sumquan = sum([c.quantity for c in odlist])
        od.total = sumtotal
        od.quantity = sumquan
            
    context = {'orderlists':order}
    return render(request,'myapp/allorderlist.html',context)

def UploadSlip(request,orderid):
    odlist = OrderList.objects.filter(orderid=orderid)
    sumtotal = sum([c.total for c in odlist])
    count = len(odlist)
    odp=OrderPending.objects.get(orderid=orderid)
    paymenttype = odp.payment
    shippingtype = odp.shipping
    
    # enympa
    shipcost = 0
    if odp.shipping == 'ems':
        shipcost = sum([50 if i == 0 else 10 for i in range(count)])
    else:
        shipcost = sum([30 if i == 0 else 10 for i in range(count)])
    
    codcost = 0
    if odp.payment == 'cod':
        codcost = 20
              
    totalamount =  sumtotal + shipcost + codcost           
    context={'orderid':orderid,
             'slipamount':sumtotal,
             'shipingcost':shipcost,
             
             'totalamount':totalamount,
             'codcost':codcost,
             'bookcount':count,
             'paymenttype':paymenttype,
             'shippingtype':shippingtype
             
             }
    return render(request,'myapp/uploadslip.html',context)

    # new.image = request.FILES['imageupload']            
    # new.save()
    