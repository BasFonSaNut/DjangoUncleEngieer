from django import forms
from .models import LogMessage,Employee,Allproduct,GeeksModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = Allproduct
        fields = ['name', 'price','description','imageurl','instock','unit','quantity','image']  # NOTE: the trailing comma is required
        
    
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required
        
class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image']

class GeeksForm(forms.Form):
    model = GeeksModel 
    fields = ['title', 'img']           