from math import ceil
from django.shortcuts import render,redirect
from pythonbook.models import BookProduct
from django.http import JsonResponse
import json


def view_AddProduct(request, pageno=None):
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
        
            datax =  {
            'id': id, 
            'bookname': bookname, 
            'author':author,
            'price': price,
            'quantity': quantity,
            'unit' : unit,
            'instock' : instockword
            
            }
            return JsonResponse(datax,status=200)
            
        
    
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
        'pythonbook/addproduct.html',
        {
            'Books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
        }
    )
    
def view_PagingItem(request, pageno=None):
    # with open('static/pythonbook/data/books.json') as f:
    #     # '/home/ajaxjson/djangoEp2template/static/pythonbook/data/books.json
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
        'pythonbook/pagingitem.html',
        {
            'books':top10,
            'totalrecord':totalrecord,
            'totalpage':range(1,(totalpage+1)),
            'currentpage':currentpage,
            'previousPage':previousPage,
            'nextPage' : nextPage
        }
    )    
