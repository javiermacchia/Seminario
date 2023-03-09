from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cartas(request):
    return render(request, 'cartas.html')

def padrinos(request):
    return render(request, 'padrinos.html')
