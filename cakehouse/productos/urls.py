from django.urls import path

from . import views
app_name= 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('mostrar_productos',views.mostrar_productos,name='mostrar_productos'),
    path('mostrado/<id>/',views.mostrado,name='mostrado'),
    path('pago/<id>/',views.pago,name='pago'),
    path('administracion',views.administracion,name='administracion'),
    path('modificar/<id>/',views.modificar,name='modificar'),
    path('eliminar/<id>/',views.eliminar,name='eliminar'),
    path('modificar_producto',views.modificar_producto,name='modificar_producto'),
    path('agregar_producto',views.agregar_producto,name='agregar_producto'),
    path('agregar',views.agregar,name='agregar'),

    
    
]