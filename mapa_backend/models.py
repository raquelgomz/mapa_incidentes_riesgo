from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class PuntosBelen(models.Model):
    long = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    distrito = models.CharField(max_length=254, null=True)
    incidente = models.CharField(max_length=254, null=True)
    indicadorid = models.BigIntegerField(null=True)
    geom = models.PointField()

    def __int__(self): return self.indicadorid