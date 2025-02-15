# Generated by Django 5.1.4 on 2025-02-10 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumbre', '0011_rename_cabaña_cabana_alter_usuario_activation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kumbre.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='activation_token',
            field=models.CharField(default='a913f08259fa4afd977c941a2b4173cd', max_length=64, unique=True),
        ),
    ]
