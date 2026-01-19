from django.urls import path 
from . import views

app_name = 'petition'

urlpatterns = [
    path('', views.petition_view, name='petition'),
    path('liste/', views.liste_petitions, name='liste_petitions'),
]
