from django.conf.urls import url
from django.urls import path
from another_app import views

app_name= 'another_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),

]
