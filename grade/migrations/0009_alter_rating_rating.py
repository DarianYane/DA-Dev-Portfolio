# Generated by Django 4.0.5 on 2023-01-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0008_rename_url_delivery_rating_url_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('Óptimo', 'Óptimo'), ('Correcto', 'Correcto'), ('Bajo', 'Bajo')], default='Óptimo', max_length=50, verbose_name="Calificación final de la entrega: >= 80es 'Óptimo', entre 51 y 79 es 'Correcto', y menos o igual a 50 es 'Bajo'"),
        ),
    ]
