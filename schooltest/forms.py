from django import forms 
from .models import PersonalRecord

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib import admin


class PersonalRecordForm(forms.ModelForm):
    class Meta :
        model = PersonalRecord
        fields = ['username','firstname_lastname','idcard_citizen', 'birthday', 'level', 'school_name','last_grade', 'phone_number', 'father_name',
        'father_occupation','father_phone', 'mother_name','mother_occupation', 'mother_phone2', 'address'] #ไม่เอาfieldนี้มาแสดงมาทำ
  
    