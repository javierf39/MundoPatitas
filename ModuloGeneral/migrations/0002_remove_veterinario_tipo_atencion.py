# Generated by Django 4.0.3 on 2022-06-14 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGeneral', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veterinario',
            name='tipo_atencion',
        ),
    ]
