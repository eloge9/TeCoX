from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("",views.home , name="home" ),
    path("events/",views.events,name="events"),
    path("poste/",views.poste,name="poste"),
]
