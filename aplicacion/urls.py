"""
URL configuration for proyecto project.

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
from .views import (eliminar, index, ingresar, update,depart,ingresardepto,gastos,agregargasto,updepa,UpGasto,eliminarGasto,eliminardepa);
from django.urls import path

urlpatterns = [
   path('', index, name='index'),
   path('actualizar/<id>',update,name='actualizar'),
   path('ingresar/',ingresar,name='ingresar'),
    path('eliminar/<id>/', eliminar, name='eliminar'),
    path('departamentos',depart,name='departamentos'),
    path("IngresarDepartamento/", ingresardepto, name="IngresarDepto"),
    path("gastos/",gastos,name="Gastos"),
    path("ingresargasto/",agregargasto,name="ingresarGasto"),
    path("actualizardepartamento/<id>/",updepa,name="updepa"),
    path("actualizargasto/<id>/",UpGasto,name="UpGasto"),
    path('eliminardepa/<id>/', eliminardepa, name='eliminardepa'),
    path('eliminargasto/<id>/', eliminarGasto, name='eliminargasto'),
    
    
]
