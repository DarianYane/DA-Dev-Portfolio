# Generated by Django 4.0.5 on 2022-10-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='year',
            field=models.IntegerField(default=2022, verbose_name='Year expected to be completed:'),
        ),
    ]
