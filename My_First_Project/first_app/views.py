from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Albam
from first_app import forms
from django.db.models import Avg

# Create your views here.

def index(request):
    musician_list= Musician.objects.order_by('first_name')
    diction={'title':'Home Page','musician_list':musician_list}
    return render(request,'first_app/index.html',context= diction)

def albam_list(request, artist_id):
    artist_info= Musician.objects.get(pk=artist_id)
    albam_list= Albam.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating= Albam.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    diction={'title':'List of Albam','artist_info':artist_info,'albam_list':albam_list,'artist_rating':artist_rating}
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

def edit_artist(request,artist_id):
     artist_info=Musician.objects.get(pk=artist_id)
     form= forms.MusicianForm(instance=artist_info)

     if request.method == 'POST':
         form=forms.MusicianForm(request.POST,instance=artist_info)

         if form.is_valid():
             form.save(commit=True)
             return albam_list(request,artist_id)

     diction={'edit_form':form,'title':'Edit Artist'}
     return render(request,'first_app/edit_artist.html',context= diction)
