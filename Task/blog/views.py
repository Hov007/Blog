from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Create your views here
from .models import *
from .forms import CreateUserForm
from django.utils.translation import gettext as _


def index(request):
    return render(request, "index.html")

def register(request):
    form = CreateUserForm() # Now form is equal to the form we created in forms.py

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid(): # checking is form is valid
            form.save()
            _(messages.success(request, "Account was created!"))

            return redirect('login')


    context = {"form":form}
    return render(request, "register.html", context)

def loginPage(request):
    if request.method == "POST":
        # Taking username and password from user (from login.html)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checking if the username and password are correct
        user = authenticate(request, username=username, password=password)
        # If there is a user loging in if not poping up an error message
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {}
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')

# Decorator that bans home page without loging in
@login_required(login_url='login')
def home(request):
    # Showing all posts from db
    post = Post.objects.all()
    context = {"post": post}
    return render(request, "home.html", context)

@login_required(login_url='login')
def viewPost(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    return render(request, "view.html", context)

@login_required(login_url='login')
def addPost(request):
    if request.method == 'POST':
        post = Post()
        # taking loged in user
        user = User.objects.get(username=request.user.username)
        # adding post under the user's name
        post.title = request.POST.get('title')
        post.user = user
        post.body = request.POST.get('content')
        post.save()
        messages.success(request, "Post is added!")
        return redirect('home')
    context = {}
    return render(request, "add.html", context)

@login_required(login_url='login')
def myPost(request):
    # Showing only post of the logged in user
    user = User.objects.get(username = request.user.username)
    post = Post.objects.filter(user=user)
    context = {"post": post}
    return render(request, "myposts.html", context)

@login_required(login_url='login')
def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.body = request.POST.get('content')
        post.save()
        messages.success(request, "Post is updated!")
        return redirect('myposts')
    context = {"post": post}
    return render(request, "edit.html", context)

@login_required(login_url='login')
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        messages.success(request, "Post is deleted!")
        return redirect("myposts")
    context = {"post": post}
    return render(request, "deletePost.html", context)