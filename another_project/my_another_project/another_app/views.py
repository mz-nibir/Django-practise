from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View,TemplateView

# Create your views here.

# def index(request):
#     return HttpResponse('Hellow world')

class IndexView(TemplateView):
    # def get(self,request):
    #     return HttpResponse('Hello World!!!!')
    template_name= 'another_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_text_1']= 'sample text 1'
        context['sample_text_2']= 'sample text 2'

        return context
