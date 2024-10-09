from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status

# Vista para listar y crear clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vista para obtener, actualizar y eliminar clientes por ID
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
