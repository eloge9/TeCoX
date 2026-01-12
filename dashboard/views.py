from django.shortcuts import render

# Create your views here.

def dashboard_user(request):
    return render(request, "utilisateurs/dashboard_utilisateur.html")

def dashboard_admin(request):
    return render(request, "admin/dashboard_admin.html")

def dashboard_super_admin(request):
    return render(request, "super_admin/dashboard_super_admin.html")