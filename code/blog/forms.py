from django import forms
from .models import Customer


class MyForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ["firstname", "lastname","dob","file",]
    labels = {'firstname':"Name", 'lastname':"Surname",'dob':"Date of birth",'file':"Excel file",}