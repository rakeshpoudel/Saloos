from django import forms
from .models import Customer


class CustomerCreateform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Name")
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Address")
    contactNo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="ContactNo")

    class Meta:
        model = Customer
        exclude = ['user']
