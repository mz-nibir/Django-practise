from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Albam
from first_app import forms

# Create your views here.

def index(request):
    musician_list= Musician.objects.order_by('first_name')
    diction={'title':'Home Page','musician_list':musician_list}
    return render(request,'first_app/index.html',context= diction)

def albam_list(request):
    diction={'title':'List of Albam'}
    return render(request,'first_app/albam_list.html',context= diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title':'Add Musician','musician_form':form}
    return render(request,'first_app/musician_form.html',context= diction)

def albam_form(request):
    form=forms.AlbamForm()

    if request.method == 'POST':
        form = forms.AlbamForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title':'Add Albam','albam_form':form}
    return render(request,'first_app/albam_form.html',context= diction)
