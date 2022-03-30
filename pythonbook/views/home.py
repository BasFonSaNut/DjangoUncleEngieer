from math import ceil
from django.shortcuts import render
from pythonbook.models import BookProduct
# from django.contrib.auth.models import User

def view_Home(request):
   
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
    return render(request,"pythonbook/home.html",context)