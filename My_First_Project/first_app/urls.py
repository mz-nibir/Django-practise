from django.conf.urls import url
from django.urls import path
from first_app import views

app_name= "First_app"

urlpatterns= [
    path('',views.index,name='index'),
    path('form/',views.form,name='form'),
]
