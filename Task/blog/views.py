import datetime
from django.http import HttpResponse
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "add.html")

def newyear(request):
    now = datetime.datetime.now()
    return render(request, "newyear.html", {
        "newyear": now.month == 1 and now.day == 1
    })

def greet(request, name):
    return render(request, "greet.html", {
        "name": name.capitalize()
    })