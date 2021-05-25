from django.conf.urls import url
from django.urls import path
from first_app import views

app_name= "First_app"

urlpatterns= [
    path('',views.index,name='index'),
    path('add_albam/',views.albam_form,name='albam_form'),
    path('add_musician/',views.musician_form,name='musician_form'),
    path('albam_list/<int:artist_id>/',views.albam_list,name='albam_list'),
    path('edit_artist/<int:artist_id>/',views.edit_artist,name='edit_artist'),
    path('edit_albam/<int:albam_id>/',views.edit_albam,name='edit_albam'),



]
