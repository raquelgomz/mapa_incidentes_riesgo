from django.urls import path
from . import views

urlpatterns = [
    path("puntosbelen/", views.PuntosBelenLista.as_view(), name=views.PuntosBelenLista.name),
    path("puntosbelen/<int:pk>/", views.PuntosBelenDetalle.as_view(), name=views.PuntosBelenDetalle.name)
]