from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext as _

# Create your models here.
class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    tipo_producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=100,default='')
    precio = models.IntegerField(default=0)
    descripcion= models.CharField(max_length=600,default='')
    imagen = models.ImageField(upload_to="porductos", null= True)

    def __str__(self):
        return self.nombre
    class Meta: 
        permissions = (
            ('gerente', _('Es gerente')),
            ('cliente', _('Es cliente')),

        ) 