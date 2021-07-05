from django.urls import path

from . import views
app_name= 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('mostrar_productos',views.mostrar_productos,name='mostrar_productos'),
    path('mostrado/<id>/',views.mostrado,name='mostrado'),
    path('pago/<id>/',views.pago,name='pago'),

]