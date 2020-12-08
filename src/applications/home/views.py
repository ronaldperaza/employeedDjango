from django.db import models
from applications.home.models import Prueba
from django.shortcuts import render

from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView,
)
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    template_name = "home/prueba.html"



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    #query siempre hace referencia a una lista
    queryset = ['0','10','20','30','40',] 
 

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = "lista"

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'