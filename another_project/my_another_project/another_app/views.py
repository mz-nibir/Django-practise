from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from another_app import models

# Create your views here.


class IndexView(ListView):

    context_object_name = 'musician_list'

    model = models.Musician

    template_name= 'another_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_text_1']= 'sample text 1'
        context['sample_text_2']= 'sample text 2'

        return context


class MusicianDetails(DetailView):
    context_object_name= 'musician'
    model = models.Musician
    template_name = 'another_app/musician_details.html'

class AddMusician(CreateView):
    fields= ('first_name','last_name', 'instrument')
    model= models.Musician
    template_name = 'another_app/musician_form.html'

class UpdateMusician(UpdateView):
    fields= ('first_name', 'instrument')
    model= models.Musician
    template_name = 'another_app/musician_form.html'
