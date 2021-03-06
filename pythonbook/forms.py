from django import forms
from .models import Employee,BookProduct,Userregister,Friend
import datetime
        
class BookProductForm(forms.ModelForm):
    class Meta:
        model = BookProduct
        fields = ['bookname', 'price','author','description','imageurl','imagefilename','instock','unit','quantity','image']  # NOTE: the trailing comma is required
    
class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image']


class UserCreationForm(forms.ModelForm):
    
    model = Userregister 
    fields = ['username', 'password'] 

class FriendForm(forms.ModelForm):
    ## change the widget of the date field.
    dob = forms.DateField(
        label='What is your birth date?', 
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )
    
    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Friend
        fields = ("__all__")   
        # fields = ['nick_name','first_name','likes','dob','lives_in']