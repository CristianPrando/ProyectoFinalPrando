from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserEditForm, AvatarFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
import os
# Create your views here.

def inicio(req):
    return render(req, 'inicio.html')

def sobrenosotros(req):
  return render(req, 'sobrenosotros.html')

class AmigurumisList(ListView):

  model = Amigurumis
  template_name = 'lista_amigurumis.html'
  context_object_name = 'amigurumis'

class AmigurumisListAdmin(ListView):

  model = Amigurumis
  template_name = 'lista_amigurumis_admin.html'
  context_object_name = 'amigurumis'

class AmigurumisCreate(LoginRequiredMixin, CreateView):

  model = Amigurumis
  template_name = 'amigurumi_create.html'
  fields = ['nombre', 'imagen', 'categoria', 'subcategoria', 'precio', 'stock', 'descripcion']
  success_url = reverse_lazy('creacionexitosa')

def creacionexitosa(req):
   return render(req, 'creacionexitosa.html')

class AmigurumiUpdate(LoginRequiredMixin, UpdateView):
   model = Amigurumis
   template_name = 'actualizaamigurumi.html'
   fields = ['nombre', 'imagen', 'categoria', 'subcategoria', 'precio', 'stock', 'descripcion']
   success_url = reverse_lazy('actualizacionexitosa')
   context_object_name = 'amigurumi'
   
   def test_func(self):
      return self.request.user.is_superuser

def actualizacionexitosa(req):
   return render(req, 'actualizacionexitosa.html')

class AmigurumiDetail(DetailView):

  model = Amigurumis
  template_name = 'detalleamigurumi.html'
  context_object_name = 'amigurumis'

class AmigurumiDelete(DeleteView):

  model = Amigurumis
  template_name = 'amigurumidelete.html'
  success_url = reverse_lazy('eliminacionexitosa')
  context_object_name = 'amigurumi'

  def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.imagen:
            if os.path.isfile(self.object.imagen.path):
                os.remove(self.object.imagen.path)

        return super().delete(request, *args, **kwargs)

def eliminacionexitosa(req):
   return render(req, 'eliminacionexitosa.html')

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
    
@login_required()
def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':
    
    mi_formulario= UserEditForm(req.POST, instance=req.user)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario.first_name = data['first_name']
      usuario.last_name = data['last_name']
      usuario.email = data['email']
      usuario.set_password(data["password1"])
      usuario.save()

      return render(req, "inicio.html", { "mensaje": f"Datos actualizados exitosamente!"})

    else:
      return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = UserEditForm(instance=req.user)
    return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })  
  

@login_required()
def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':
    
    mi_formulario= UserEditForm(req.POST, instance=req.user)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario.first_name = data['first_name']
      usuario.last_name = data['last_name']
      usuario.email = data['email']
      usuario.set_password(data["password1"])
      usuario.save()

      return render(req, "inicio.html", { "mensaje": f"Datos actualizados exitosamente!"})

    else:
      return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = UserEditForm(instance=req.user)
    return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })  
  
def agregar_avatar(req):

  if req.method == 'POST':
    
    mi_formulario= AvatarFormulario(req.POST, req.FILES)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save()

      return render(req, "inicio.html", { "mensaje": f"Avatar creado correctamente!"})

    else:
      return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = AvatarFormulario()
    return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })
  
def carrito_view(request):
    # Asegúrate de que el usuario esté autenticado
    if request.user.is_authenticated:
        carrito_items = Carrito.objects.filter(user=request.user)
        total = sum(item.amigurumi.precio * item.cantidad for item in carrito_items)
        return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})
    else:
        return redirect('Login')  # Redirige al usuario si no está autenticado

def agregar_al_carrito(req, amigurumi_id):
    if not req.user.is_authenticated:
        return redirect('Login')  

    amigurumi = Amigurumis.objects.get(id=amigurumi_id)
    
    carrito_item, created = Carrito.objects.get_or_create(
        amigurumi=amigurumi,
        user=req.user  
    )

    if not created:
        carrito_item.cantidad += 1  
        carrito_item.save()

    return redirect('carrito')  

def eliminar_producto(request, id):
    if request.user.is_authenticated:
        item = Carrito.objects.get(id=id, user=request.user)
        item.delete()
    return redirect('carrito')  

def actualizar_cantidad(request, id):
    if request.method == "POST":
        nueva_cantidad = request.POST.get('cantidad')
        item = Carrito.objects.get(id=id, user=request.user)
        item.cantidad = nueva_cantidad
        item.save()
    return redirect('carrito') 

def navbar_context(request):
    total_items = Carrito.objects.filter(user=request.user).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    return {'total_items': total_items}