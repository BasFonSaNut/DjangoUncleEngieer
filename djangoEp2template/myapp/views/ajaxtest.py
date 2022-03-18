from myapp.models import Orders
from django.http import JsonResponse
# for ajax
from django.views.generic import ListView
from django.views.generic import View
#===============================Ajax===========
class view_OrderCrudView(ListView):
    model = Orders
    template_name = 'myapp/allorderlistajax.html'
    order=Orders.objects.all()
    context_object_name = 'orderlists'
    
class view_OrderCrudSlipChecked(View):
    def post(self, request):
        orderid = request.POST.get('orderid', None)
        updateWhat = request.POST.get('updateWhat', None)
        csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)


        print(updateWhat)
        obj = Orders.objects.get(orderid=orderid)
        obj.slipcheckedstatus = True
        obj.save()
        data = {
            'statusupdate' : 'slip was check'
        }
        return JsonResponse(data)
    
class OrderCrudPaidChecked(View):
    def post(self, request):
        orderid = request.POST.get('orderid', None)
        updateWhat = request.POST.get('updateWhat', None)
        csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)
        print(updateWhat)
       
        obj = Orders.objects.get(orderid=orderid)
        obj.paymentstatus = True
        obj.save()
        
        data = {
            'statusupdate': 'slip was paid'
        }
        return JsonResponse(data)
#==============================