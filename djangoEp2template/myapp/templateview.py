from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import EmployeeForm
from .models import Employee
class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)  
   
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)    


class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'