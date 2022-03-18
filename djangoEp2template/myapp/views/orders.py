from datetime import datetime
from django.shortcuts import render,redirect
from myapp.models import Cart,OrderPending,OrderList,Profile
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
from django.http import JsonResponse

def view_OrderListPage(request):
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

def view_Checkout(request): 
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
            
           
            odp = OrderPending.objects.get(orderid=genorderid)
            mycart = Cart.objects.filter(user=user) 
            sumtotal = sum([c.total for c in mycart])
            sumquan = sum([c.quantity for c in mycart])
            odp.goodsprice = sumtotal
            odp.totalquantity = sumquan
            odp.save()
            
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


def view_UploadSlip(request,orderid):
    uploadstatus = ""
    if request.method == 'POST' and request.FILES['slipupload']:
        # print(data)
        data = request.POST.copy()
        codprice = data.get('codprice')
        shippingprice = data.get('shippingprice')
        totallyprice = data.get('totallyprice')
        slipdatetimekeyin = data.get('slipdatetimekeyin')
        transactionid = data.get('transactionid')
        orderid =  data.get('orderid')
        # print(data)
        odp = OrderPending.objects.get(orderid=orderid)
        odp.codprice =  codprice
        odp.shippingprice =  shippingprice
        odp.totallyprice =  totallyprice
        odp.slipdatetimekeyin = slipdatetimekeyin
        odp.transactionid = transactionid
        odp.slipuploadstatus = True
        odp.slipuploadtime = datetime.now()
        odp.image = request.FILES['slipupload']            
        odp.save()
        uploadstatus = 'uploadslip'
        
    
    
    odp=OrderPending.objects.get(orderid=orderid)
    sumquan = odp.totalquantity
    
    # calculate shipping cost
    shipcost = 0
    if odp.shipping == 'ems':
        shipcost = sum([50 if i == 0 else 10 for i in range(sumquan)])
    else:
        shipcost = sum([30 if i == 0 else 10 for i in range(sumquan)])
    
    codcost = 0
    if odp.payment == 'cod':
        codcost = 20
            
    totalamount =  odp.goodsprice + shipcost + codcost           
    context={
            'orderid':orderid,
            'totalamount':totalamount,
            'shipingcost':shipcost,
            'codcost':codcost,
            'status' : uploadstatus,
            'odb':odp
            }
    return render(request,'myapp/uploadslip.html',context)


def view_AllOrderListPage(request):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    
    statusupdate = ""
    if request.method == 'POST':
        data = request.POST.copy()
        orderid = data.get('orderid')
        updateWhat = data.get('updateWhat')
        # print(updateWhat)
        # orderid =request.POST.get('orderid', None)
        # updateWhat =request.POST.get('updateWhat', None)
        odp = OrderPending.objects.get(orderid=orderid)
        if updateWhat == 'slipchecked':
            # print("update checked slip")
            odp.slipcheckedstatus = True
            odp.save()
            statusupdate =  'status pass checked slip'
            # datax= {'statusupdate': 'status pass checked slip'}
            # json_format = json.dumps(datax)
            # return JsonResponse({"instance":json_format}, status=200)
            # return render(request,'myapp/allorderlist.html',context)
            data = {
            'statusupdate' : 'slip was check'
            }
            return JsonResponse(data)
        elif updateWhat == 'paymentchecked':
            # print("update payment")
            odp.paymentstatus = True
            odp.save()
            statusupdate = "status Paid"
            # datax= {"statusupdate": "status Paid"}
            # json_format = json.dumps(datax)
            # return JsonResponse({"instance":json_format}, status=200)
            # return render(request,'myapp/allorderlist.html',context)
            data = {
            'statusupdate' : 'order was paid'
            }
            return JsonResponse(data)
        elif updateWhat == 'deliverychecked':
            # print("update delivery")
            odp.shippingstatus = True
            odp.save()
            statusupdate = "status  under delivery"
            # datax= {"statusupdate": "status  under delivery"}  
            # json_format = json.dumps(datax)
            # return JsonResponse({"instance":json_format}, status=200)  
            # return render(request,'myapp/allorderlist.html',context)
            data = {
            'statusupdate' : 'slip was check'
            }
            return JsonResponse(data)
    order=OrderPending.objects.all()
    for od in order:
        orderid = od.orderid
        odlist = OrderList.objects.filter(orderid=orderid)
        sumtotal = sum([c.total for c in odlist])
        sumquan = sum([c.quantity for c in odlist])
        od.total = sumtotal
        od.quantity = sumquan
            
    context = {
               'orderlists':order,
               'updatestatus':statusupdate
              }
    
    return render(request,'myapp/allorderlist.html',context)


def view_UpdateTracking(request,orderid):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    
    if request.method == 'POST':
        data = request.POST.copy()
        trackingnumber = data.get('trackingnumber')
        odp = OrderPending.objects.get(orderid=orderid)
        odp.trackingnumber = trackingnumber
        odp.shippingstatus = True
        odp.save()
        return redirect('allorderlist-page')
    
    context = {'orderid':orderid}
    return render(request, "myapp/updatetracking.html",context)



def view_FRMtracking(request,orderid):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    
    context = {'orderid':orderid}
    return render(request, "myapp/frmuploadtracking.html",context)
