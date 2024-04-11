from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def pago(request):
    return render(request,"pago.html")

def categorias(request):
    return render(request,"categorias.html")

def vista_previa_producto(request):
    return render(request,"vista_previa_producto.html")

def base(request):
    return render(request,"base.html")