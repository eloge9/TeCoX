from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'pages/events.html')

def poste(request):
    return render(request, 'pages/poste.html')