# Generated by Django 5.1.4 on 2025-02-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumbre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sugerencia',
            name='mensaje',
            field=models.TextField(default='sin mensaje'),
        ),
    ]
