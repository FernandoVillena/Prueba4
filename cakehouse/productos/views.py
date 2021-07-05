from productos.models import Producto
from django.http import HttpResponse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse



def index(request):
    listado_clientes =Producto.objects.all()
    clientes ={'listado_clientes':listado_clientes }
    return render(request, 'productos/index.html',clientes)

def mostrar_productos(request):

    if request.POST['Buscar']:
        buscado= request.POST['Buscar']
        producto = Producto.objects.filter(nombre__icontains=buscado)
        return render(request,'productos/mostrar_productos.html',{"producto":producto,"query":buscado})
    else:
        return HttpResponse("No has introducido nada")


def mostrado(request,id):
    producto= Producto.objects.get(pk=id)
    return render(request,'productos/mostrado.html',{'producto':producto})

def pago(request,id):
    producto= Producto.objects.get(pk=id)
    return render(request,'productos/pago.html',{'producto':producto})

