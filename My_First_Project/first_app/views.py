from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diction={'text_1': 'i am from views.py page'}
    return render(request,'first_app/index.html',context= diction)
