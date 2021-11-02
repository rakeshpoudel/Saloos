from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    contactNo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email','password','password_2','contactNo',]


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        if password is not None and password!=password_2:
            raise ValueError("password doesnot match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Password")

