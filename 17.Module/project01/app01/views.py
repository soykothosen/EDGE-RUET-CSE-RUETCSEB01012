from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello World")

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def newhome(request):
    return render(request,'home.html')

def dynamic(request):
    return render(request,'base.html',{'name': 'RUET'})

def other(request):
    return render(request,'other.html',{'name': 'RUET'})

def index(request):
    return render(request,'index.html')
