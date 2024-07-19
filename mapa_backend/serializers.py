from .models import PuntosBelen
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class PuntosBelenSerializador(GeoFeatureModelSerializer):
    class Meta:
        model = PuntosBelen
        geo_field = 'geom'

        fields = (
            'id',
            'long',
            'lat',
            'distrito',
            'incidente',
            'indicadorid'
        )