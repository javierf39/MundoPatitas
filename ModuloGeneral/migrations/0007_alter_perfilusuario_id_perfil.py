# Generated by Django 4.0.1 on 2022-04-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGeneral', '0006_alter_usuarioperfil_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='id_perfil',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
