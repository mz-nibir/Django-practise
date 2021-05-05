from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello world!<h1>')

def home(request):
    return HttpResponse('<h2>Hello Nibir!<h2>')
