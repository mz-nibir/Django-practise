from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Albam
from first_app import forms

# Create your views here.

def index(request):
    musician_list= Musician.objects.order_by('first_name')
    diction={'text_1': 'The list of Musician','musician': musician_list}
    return render(request,'first_app/index.html',context= diction)

def form(request):
    new_form = forms.user_form()
    diction={'text_form': new_form, 'heading_1': 'this is from django form'}

    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            dob = new_form.cleaned_data['dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name': user_name})
            diction.update({'user_dob': dob})
            diction.update({'user_email': user_email})

            diction.update({'form_submitted': 'yes'})


    return render(request,'first_app/form.html',context= diction)
