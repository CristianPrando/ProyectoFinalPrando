"""
URL configuration for Proyecto_Final_Prando project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobrenosotros', sobrenosotros, name='sobrenosotros'),
    path('listaamigurumis/', AmigurumisList.as_view(), name='listaamigurumis'),
    path('listaamigurumisadmin/', AmigurumisListAdmin.as_view(), name='listaamigurumisadmin'),
    path('creaamigurumi/', AmigurumisCreate.as_view(), name='creaamigurumi'),
    path('creacionexitosa/', creacionexitosa, name='creacionexitosa'),
    path('actualizaamigurumi/<pk>', AmigurumiUpdate.as_view(), name='actualizaamigurumi'),
    path('actualizacionexitosa/', actualizacionexitosa, name='actualizacionexitosa'),
    path('detalleamigurumi/<pk>', AmigurumiDetail.as_view(), name='detalleamigurumi'),
    path('eliminaramigurumi/<pk>', AmigurumiDelete.as_view(), name='eliminaramigurumi'),
    path('eliminacionexitosa/', eliminacionexitosa, name='eliminacionexitosa'),
    path('registro/', register, name='Registro'),
    path('login/', login_view, name='Login'),
    path('logout/', LogoutView.as_view(template_name="Logout.html"), name='Logout'),
    path('editarperfil/', editar_perfil, name='editarperfil'),
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
    path('eliminar-avatar/', eliminar_avatar, name='eliminar_avatar'),
    path('confirmar-eliminario-avatar/', confirmar_eliminacion_avatar, name='confirmar_eliminacion_avatar'),
    path('carrito/', carrito_view, name='carrito'),
    path('agregar_al_carrito/<int:amigurumi_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('carrito/actualizar/<int:id>/', actualizar_cantidad, name='actualizar_cantidad'),
    path('finalizar-pedido/', finalizar_pedido, name='finalizar_pedido'),
    path('ropa', ropa, name='ropa'),
    path('insumos', insumos, name='insumos'),
    path('busqueda-amigurumi', busqueda_amigurumi, name='busqueda_amigurumi'),
    path('contacto/', contacto, name='contacto'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
