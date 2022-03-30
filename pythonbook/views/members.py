from django.shortcuts import redirect,render
from pythonbook.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def view_Register(request):
    
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
        return redirect('home-page')    
    
    return render(request, "pythonbook/register.html")