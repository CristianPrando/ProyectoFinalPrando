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
    path('creaamigurumi/', AmigurumisCreate.as_view(), name='creaamigurumi'),
    path('registro/', register, name='Registro'),
    path('login/', login_view, name='Login'),
    path('logout/', LogoutView.as_view(template_name="Logout.html"), name='Logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
