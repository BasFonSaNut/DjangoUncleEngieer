from django.shortcuts import render

def view_Aboutus(request):
    return render(request,'pythonbook/aboutus.html')

def view_Contactus(request):
    return render(request,'pythonbook/contact.html')