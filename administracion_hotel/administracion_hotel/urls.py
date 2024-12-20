"""
URL configuration for administracion_hotel project.

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
from hotel import views

urlpatterns = [
       path('admin/', admin.site.urls),
    path('clientesDB/', views.lista_clientes_base_datos, name='clientesDB'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('habitacionesDB/', views.habitacion_disponible_base_datos, name='habitacionesDB'),
    path('habitaciones/', views.habitacion_disponible, name='habitacion'),
]
