from django import forms
from .models import Barber,Service


class BarberCreateform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Name")
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Address")
    contactNo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="ContactNo")

    class Meta:
        model = Barber
        exclude = ['user']

class AddServiceForm(forms.ModelForm):
    servicetitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label="Description")
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),label="price")


    class Meta:
        model = Service
        exclude = ['barber']

class ChangeProfileImageform(forms.ModelForm):
    class Meta:
        model = Barber
        fields = ['profile']


