from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import CustomUserCreationForm

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html')

def sobrenosotros(req):
  return render(req, 'sobrenosotros.html')

class AmigurumisList(ListView):

  model = Amigurumis
  template_name = 'lista_amigurumis.html'
  context_object_name = 'amigurumis'


class AmigurumisCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):

  model = Amigurumis
  template_name = 'amigurumi_create.html'
  fields = ['nombre', 'imagen', 'categoria', 'subcategoria', 'precio', 'stock', 'descripcion']
  success_url = '/pandora'

def login_view(req):
    if req.method == 'POST':
      
      mi_formulario= AuthenticationForm(req, data=req.POST)
      if mi_formulario.is_valid():

        data = mi_formulario.cleaned_data
        usuario = data['username']
        psw = data['password']

        user = authenticate(username=usuario, password=psw)

        if user:
          login(req, user)
          return render(req, "inicio.html", { "mensaje": f"Bienvenido {usuario}"})
        else:
          return render(req, "inicio.html", { "mensaje": f"Datos incorrectos!"})

      else:
        return render(req, "login.html", { "mi_formulario": mi_formulario })  

    else:
      mi_formulario = AuthenticationForm()
      return render(req, "login.html", { "mi_formulario": mi_formulario })  
  
def register(req):
    
    if req.method == "POST":
        mi_formulario = CustomUserCreationForm(req.POST)

        if mi_formulario.is_valid():
            mi_formulario.save()
            username = mi_formulario.cleaned_data.get("username")
            password = mi_formulario.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(req, user)
            return redirect("inicio")
        
    else:
        mi_formulario = CustomUserCreationForm()
        return render(req, "registro.html", {"mi_formulario": mi_formulario})