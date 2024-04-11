"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from VGproject.views import inicio,categorias,pago,vista_previa_producto,base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base),
    path('inicio/',inicio),
    path('categorias/',categorias),
    path('pago/',pago),
    path('vista_previa_producto/',vista_previa_producto)
]

