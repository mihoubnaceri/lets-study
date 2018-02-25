from django.shortcuts import render
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.
# from django.contrib.auth import authenticate, login
#
# def login(request):
#     form_error = None
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             userObj = form.cleaned_data
#             username = userObj['username']
#             password = userObj['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
#                 return HttpResponseRedirect("/")
#             else:
#                 form_error = "alread exists choose other !"
#     else:
#         if request.user.is_authenticated:
#             return HttpResponseRedirect("/")
#         else:
#             form = UserLoginForm()
#     return render(request,"accounts/login.html",{"form_error":form_error})
from django.contrib.auth.views import login

def custom_login(request): # overriding the deault login view from django.contrib.auth.views
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return login(request)

@login_required
def profile(request,username):
    user = User.objects.get(username=username)
    return render(request,"accounts/profile.html",{"user":user})

def register(request):
    form_error = None
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj["username"]
            email = userObj["email"]
            password = userObj["password"]
            confirm_password = request.POST.get("confirm-password")
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()) and password == confirm_password :
                User.objects.create_user(username,email,password)
                user = authenticate(username=username,password=password)
                login(request,user)
                return HttpResponseRedirect("/")

            else:
                form_error = "alread exists choose other !"

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            form = UserRegistrationForm()

    return render(request,"accounts/register.html",{"form":form,"form_error":form_error})
