# Generated by Django 4.0.1 on 2022-05-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGeneral', '0008_imagenmascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='img',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='ImagenMascota',
        ),
    ]