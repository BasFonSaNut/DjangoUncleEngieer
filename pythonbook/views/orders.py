from datetime import datetime
from django.shortcuts import render,redirect
from pythonbook.models import Cart,Orders,OrderList,Profile
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
from django.http import JsonResponse

def view_OrderListPage(request):
    if request.method == 'POST' and request.FILES['slipupload']:
        data = request.POST.copy()
        rowindex = data.get('rowindex')
        slipdatetimekeyin = data.get('slipdatetimekeyin')
        transactionid = data.get('transactionid')
        orderid =  data.get('orderid')
        odp = Orders.objects.get(orderid=orderid)
        
        odp.slipdatetimekeyin = slipdatetimekeyin
        odp.transactionid = transactionid
        odp.slipuploadstatus = True
        odp.slipuploadtime = datetime.now()
        odp.image = request.FILES['slipupload']            
        
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
        odp.codprice =  codcost
        odp.shippingprice =  shipcost
        odp.totallyprice =  totalamount
        odp.save()
        
        # statustxt =  'ORDER :' + orderid +" WAS UPLOADSLIP"        
        datax={
                'orderid': orderid,
                'rowindex':rowindex
                }
        return JsonResponse(datax)
    
    
    username = request.user.username
    user = User.objects.get(username=username)
    order=Orders.objects.filter(user=user)
    for od in order:
        orderid = od.orderid
        odlist = OrderList.objects.filter(orderid=orderid)
        sumtotal = sum([c.total for c in odlist])
        sumquan = sum([c.quantity for c in odlist])
        od.total = sumtotal
        od.quantity = sumquan
            
    context = {'orderlists':order}
    return render(request,'pythonbook/orderlist.html',context)

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
            
            return render(request,'pythonbook/checkout2.html',context)
        
        if page =='confirmation':
            dt = datetime.now().strftime('%Y%m%d%H%M%S')
            genorderid = 'OD'+str(user.id).zfill(4)+dt
            
            orderpending = Orders()
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
            
           
            odp = Orders.objects.get(orderid=genorderid)
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
        
    return render(request,'pythonbook/checkout1.html')

def view_AllOrderListPage(request):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    
    statusupdate = ""
    if request.method == 'POST':
        data = request.POST.copy()
        orderid = data.get('orderid')
        updateWhat = data.get('updateWhat')
        odp = Orders.objects.get(orderid=orderid)
        if updateWhat == 'slipchecked':
            odp.slipcheckedstatus = True
            odp.save()
            statusupdate =  'status pass checked slip'
            data = {
            'statusupdate' : 'slip was check'
            }
            return JsonResponse(data)
        elif updateWhat == 'paymentchecked':
            odp.paymentstatus = True
            odp.save()
            statusupdate = "status Paid"
            data = {
            'statusupdate' : 'order was paid'
            }
            return JsonResponse(data)
        elif updateWhat == 'deliverychecked':
            # print("update delivery")
            odp.shippingstatus = True
            odp.save()
            statusupdate = "status  under delivery"
            data = {
            'statusupdate' : 'slip was check'
            }
            return JsonResponse(data)
        elif updateWhat == 'getTrackinnumber':
            trackingnumber = data.get('trackingnumber')
            rowindex = data.get('rowindex')
            odp = Orders.objects.get(orderid=orderid)
            odp.trackingnumber = trackingnumber
            odp.shippingstatus = True
            odp.save()
            data = {
            'orderid' : orderid,    
            'trackingNo' : trackingnumber,
            'rowindex' : rowindex            
            }
            return JsonResponse(data)
    
    order=Orders.objects.all()
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
    
    return render(request,'pythonbook/allorderlist.html',context)


def view_FRMtracking(request,orderid,rowindex):
    if request.user.profile.usertype != 'admin':
        return redirect('orderlist-page')
    
    context = {'orderid':orderid,
               'rowindex':rowindex
              }
    return render(request, "pythonbook/frmupdatetracking.html",context)

def view_FRMUploadSlip(request,orderid,rowindex):
    context = {'orderid':orderid,
               'rowindex':rowindex
              }
    return render(request, "pythonbook/frmuploadslip.html",context)

def view_OrderInfo(request,orderid):
    odp = Orders.objects.get(orderid=orderid)
    warningtxt = "<strong>ORDER นี้  upload slip แล้ว รอการเช็คสลิปเพื่อยืนยืนการชำระเงิน</strong>"
    context = {
            "odb":odp,
            "uploadslipwarning" : warningtxt
               
            }
    return render(request, "pythonbook/orderinfo.html",context)

