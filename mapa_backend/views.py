from .models import PuntosBelen
from .serializers import PuntosBelenSerializador
from rest_framework import generics

# Create your views here.
class PuntosBelenLista(generics.ListAPIView):
    queryset = PuntosBelen.objects.all()
    serializer_class = PuntosBelenSerializador
    name = 'PuntosBelen-lista'

class PuntosBelenDetalle(generics.RetrieveAPIView):
    queryset = PuntosBelen.objects.all()
    serializer_class = PuntosBelenSerializador
    name = 'puntosbelen-detalle'