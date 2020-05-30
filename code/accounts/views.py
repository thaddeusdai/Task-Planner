from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from .forms import  NewUserForm, ForgotPasswordForm, ResetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.core.mail import send_mail
import random as rd


# Create your views here.
def home(request):
    return render(request, 'index.html')

def logout_request(request):
    logout(request)
    return redirect("home")

def register(request):
# creates the user
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST or None)
        
        # must fill out the required form and the username must be unique
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, "User could not be created due to invalid information")
    
    
    return render(request, 'registration/register.html', {"form": form})



def forgot_password(request):
    # gets username, sends the email
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        
        if form.is_valid():
            try:
                user = Account.objects.get(username=form.cleaned_data["username"])
                temp_password = chr(rd.randint(97, 123)) + chr(rd.randint(97, 123)) + chr(rd.randint(97, 123)) + str(rd.randint(1000, 1000000))
                user.set_password(temp_password)
                user.save()
                send_mail(f'Password for {user.username}',
                            f'The temporary password for your account is {temp_password}',
                            'thaddeus.dai2000@gmail.com',
                            [f'{user.email}'],
                            fail_silently = False,
                                )
                messages.success(request, 'Your password was sent to your email')

                
            except:
                messages.error(request, 'That username does not exist')

                    

    return render(request, 'forgot_password.html')

@login_required
def reset_password(request, _username):
    user = Account.objects.get(username=_username)
    
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        
        if form.is_valid():
            if authenticate(username = _username, password = form.cleaned_data['current_pass']):
                user.set_password(form.cleaned_data['new_pass'])
                user.save()
                messages.success(request,"Password has been reset")
            else:
                messages.error(request,"The current password you entered is not the correct password for this account")
        else:
            messages.error(request,"Please fill out the form completely")
        
    

    return render(request, 'reset_password.html')

