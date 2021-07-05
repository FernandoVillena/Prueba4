from django.contrib import admin
from productos.models import Producto, Tipo_producto


admin.site.register(Tipo_producto)
admin.site.register(Producto)

