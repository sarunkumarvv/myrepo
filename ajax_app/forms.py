from dataclasses import field
import email
from pyexpat import model
from django import forms
from .models import studentmodel

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = ['name','age']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'age':forms.NumberInput(attrs={'class':'form-control','id':'ageid'}),
        }