from cakehouse.serializers import ProductoSerializer
from productos.models import Producto,Tipo_producto
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from cakehouse.serializers import UserSerializer, GroupSerializer, ProductoSerializer, Tipo_productoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]   

class Tipo_productoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tipo_producto.objects.all()
    serializer_class = Tipo_productoSerializer
    permission_classes = [permissions.IsAuthenticated]      