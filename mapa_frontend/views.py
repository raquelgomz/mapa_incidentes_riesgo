# Create your views here.
from django.shortcuts import render

# Create your views here.
def puntosbelenListaMapa(request):
    return render(request, 'mapa_frontend/puntosbelen_base.html')