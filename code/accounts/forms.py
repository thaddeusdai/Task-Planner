from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Account
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

        
class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length = 100)

class ResetPasswordForm(forms.Form):
    new_pass = forms.CharField(max_length=100, widget=forms.PasswordInput())
    current_pass = forms.CharField(max_length=100, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    
        


        