# Generated by Django 4.0.1 on 2022-04-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGeneral', '0005_citamedica_publicacionadopcion_publicacionforo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioperfil',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
