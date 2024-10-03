from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html')

class AmigurumisList(ListView):

  model = Amigurumis
  template_name = 'lista_amigurumis.html'
  context_object_name = 'amigurumis'

class AmigurumisCreate(CreateView):

  model = Amigurumis
  template_name = 'amigurumi_create.html'
  fields = ['nombre', 'imagen', 'categoria', 'subcategoria', 'precio', 'stock', 'descripcion']
  success_url = '/pandora'