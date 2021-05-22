from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Albam
from first_app import forms

# Create your views here.

def index(request):
    diction={'simple_text':'This is a simple text from view'}
    return render(request,'first_app/index.html',context= diction)

def form(request):
    new_form = forms.Musician_form()
    if request.method == 'POST':
        new_form= forms.Musician_form(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)

    diction={'test_form':new_form,'heading_1':'add new musician'}



    return render(request,'first_app/form.html',context=diction)
