"""
URL configuration for MiEjProyectoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from MiEjProyectoDjango.views import saludo
from MiEjProyectoDjango import views2





urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),  # Añadir nueva ruta
    path('saludo2/', views2.saludo2, name='saludo2'),  # Ruta para la vista2 saludo
    path('fecha/', views2.fecha, name='fecha'),  # Ruta para la vista2 de fecha
    path('calcEdad/<int:year>/', views2.calcEdad, name='calcEdad'),  # Ruta para la vista2 de cálculo de edad
]