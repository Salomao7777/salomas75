from django.urls import path
from .views import index, Animal, Categoria

urlpatterns = [
    path('index.html', index, name='index'),
    path('', Animal, name='Animal'),
    path('', Categoria, name='Categoria'),
]