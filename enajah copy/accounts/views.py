from django.shortcuts import render,get_object_or_404
from .forms import UserRegistrationForm,UserLoginForm,ProfileForm
from .models import StudentProfile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import login
from django import forms
from django.conf import settings
from courses.models import Palier
# Create your views here.
# from django.contrib.auth import authenticate, login
#

@login_required
def edit_profile(request,username):
    user = User.objects.get(username=username)
    user_form = ProfileForm(instance=user)
    create_user =None
    ProfileInlineFormset = inlineformset_factory(User,StudentProfile,fields=("bio","facebook","school_name","palier","age","photo"))
    formset = ProfileInlineFormset(instance=user)
    if request.user.is_authenticated and request.user.username == user.username:
        if request.method == "POST":
            user_form = ProfileForm(request.POST,request.FILES,instance=user)
            formset = ProfileInlineFormset(request.POST,request.FILES,instance=user)
            if user_form.is_valid():
                created_user = user_form.save()
                formset = ProfileInlineFormset(request.POST,request.FILES,instance =created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect("/")
        return render(request,"accounts/update_profile.html",{
            "username": username,
            "profile_form":user_form,
            "formset":formset,
        })
    else:
        return PermissionDenied


def enroll_student(request,username,palier_slug):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    button = "Enroll"
    palier = get_object_or_404(Palier,palier_slug=palier_slug)
    enrolled = user.enrolled_palier.all()

    print(enrolled)
    if request.method=="POST":
        print(user.enrolled_palier.all())
        palier.student.add(user)
        
        palier.save()
        return HttpResponseRedirect("/")
    return render(request,"accounts/pay.html",{})


def custom_login(request): # overriding the deault login view from django.contrib.auth.views
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return login(request)
def users(request):
    users = User.objects.all()
    return render(request,"accounts/users.html",{"users":users})


@login_required
def profile(request,username):
    amine = User.objects.get(username=username)

    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    args = {'user': user}

    return render(request,"accounts/profile.html",args)

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
