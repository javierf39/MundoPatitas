# Generated by Django 4.0.1 on 2022-05-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGeneral', '0006_veterinario_id_perfil_alter_veterinario_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinario',
            name='clave',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]