from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>I am from first app</h1>')

def contact(request):
    return HttpResponse("contact page")
