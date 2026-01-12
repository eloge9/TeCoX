from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('utilisateur/', views.dashboard_user, name='dashboard_user'),
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('super_admin/', views.dashboard_super_admin, name='dashboard_super_admin'),
]
