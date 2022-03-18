from django.contrib.auth.models import User
from myapp.models import BookProduct,Cart,Profile
from django.shortcuts import render,redirect

def view_AddtoCart(request,bid):
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
        
def view_MyCart(request):
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