# Generated by Django 4.0.5 on 2023-05-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidecc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
