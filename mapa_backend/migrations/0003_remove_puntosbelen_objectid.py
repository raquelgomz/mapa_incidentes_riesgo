# Generated by Django 4.2.13 on 2024-07-15 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_backend', '0002_puntosbelen_objid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntosbelen',
            name='objectid',
        ),
    ]
