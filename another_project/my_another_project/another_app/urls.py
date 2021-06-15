from django.conf.urls import url
from django.urls import path
from another_app import views

app_name= 'another_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='musician_update'),

]
