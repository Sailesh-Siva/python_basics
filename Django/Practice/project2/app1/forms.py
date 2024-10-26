from django import forms
from .models import Employee,Product

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

