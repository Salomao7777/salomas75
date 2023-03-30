

# Create your views here.
from django.shortcuts import render
from .models import Animal, Categoria
# Create your views here.

def index(request):
    return render('index.html')

def Animal(request):
    return render()

def Categoria(request):
    return render()