from django.urls import path
from . import views

app_name = 'mapa_frontend'
urlpatterns = [
    path('', views.puntosbelenListaMapa, name='puntosbelen-lista-mapa')
]