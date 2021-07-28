from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def hov(request):
    return HttpResponse("Hello Hov!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")