

from productos.models import Tipo_producto
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


def administracion(request):
    listado_clientes =Producto.objects.all()
    clientes ={'listado_clientes':listado_clientes }
    return render(request, 'productos/administracion.html',clientes)



def modificar(request,id):
    producto= Producto.objects.get(pk=id)
    tipo_producto= Tipo_producto.objects.all()
    producto_t=producto.tipo_producto
    return render(request,'productos/modificar.html',{'producto':producto,'tipo_producto':tipo_producto,'producto_t':producto_t })


def modificar_producto(request):
    id_producto=request.POST['id_producto']
    Nombre_p=request.POST['Nombre'].strip()
    precio_p=request.POST['precio'].strip()
    descripcion_p=request.POST['descripcion'].strip()
    imagen_p=request.FILES.get('imagen')
    tipoproducto_p=request.POST['tipoproducto']
    
    tipo=Tipo_producto.objects.get(id=tipoproducto_p)

    producto= Producto(id=id_producto,nombre=Nombre_p,
    precio=precio_p,descripcion=descripcion_p,imagen =imagen_p,
    tipo_producto= tipo)

    producto.save()
    return HttpResponseRedirect(reverse('productos:administracion'))


def eliminar(request,id):
    producto= Producto.objects.get(pk=id)
    producto.delete()
    return HttpResponseRedirect(reverse('productos:administracion'))

def agregar_producto(request):
    tipo_producto= Tipo_producto.objects.all()
    return render(request,'productos/agregar_producto.html',{'tipo_producto':tipo_producto})

def agregar(request):
    Nombre_p=request.POST['Nombre'].strip()
    precio_p=request.POST['precio'].strip()
    descripcion_p=request.POST['descripcion'].strip()
    imagen_p=request.FILES.get('imagen')
    tipoproducto_p=request.POST['tipoproducto']
    
    tipo=Tipo_producto.objects.get(id=tipoproducto_p)

    producto= Producto(nombre=Nombre_p,
    precio=precio_p,descripcion=descripcion_p,imagen =imagen_p,
    tipo_producto= tipo)

    producto.save()
    return HttpResponseRedirect(reverse('productos:administracion'))