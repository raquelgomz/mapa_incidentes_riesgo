from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import PuntosBelen

puntosbelen_mapping = {
    'long': 'long',
    'lat': 'lat',
    'distrito': 'Distrito',
    'incidente': 'Incidente',
    'indicadorid': 'indicadorid',
    'geom': 'POINT',
}

PNT_BELEN_gpkg = Path(__file__).resolve().parent / 'datos' / 'PNT_BELEN.gpkg'

def run(verbose=True):
    lm = LayerMapping(PuntosBelen, PNT_BELEN_gpkg, puntosbelen_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)