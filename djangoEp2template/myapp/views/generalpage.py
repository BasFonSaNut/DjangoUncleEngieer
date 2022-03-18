from django.shortcuts import render

def view_Aboutus(request):
    return render(request,'myapp/aboutus.html')

def view_Contactus(request):
    return render(request,'myapp/contact.html')