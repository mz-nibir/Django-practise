from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Albam
from first_app import forms

# Create your views here.

def index(request):
    diction={'title':'Home Page'}
    return render(request,'first_app/index.html',context= diction)

def albam_list(request):
    diction={'title':'List of Albam'}
    return render(request,'first_app/albam_list.html',context= diction)

def musician_form(request):
    diction={'title':'Add Musician'}
    return render(request,'first_app/musician_form.html',context= diction)

def albam_form(request):
    diction={'title':'Add Albam'}
    return render(request,'first_app/albam_form.html',context= diction)
