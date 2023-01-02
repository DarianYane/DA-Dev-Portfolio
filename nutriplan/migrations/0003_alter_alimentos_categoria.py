# Generated by Django 4.0.5 on 2023-01-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriplan', '0002_alter_alimentos_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='categoria',
            field=models.CharField(choices=[('Grasas', 'Grasas'), ('Frutas', 'Frutas'), ('Verduras', 'Verduras'), ('Cereales_Legumbres', 'Cereales y Legumbres'), ('Proteínas', 'Proteínas'), ('Lacteos', 'Lacteos'), ('Otros', 'Otros')], default='Otros', max_length=50),
        ),
    ]
