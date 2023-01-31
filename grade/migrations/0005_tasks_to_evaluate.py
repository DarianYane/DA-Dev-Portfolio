# Generated by Django 4.0.5 on 2023-01-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0004_alter_commission_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks_to_Evaluate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Task to evaluate',
                'verbose_name_plural': 'Tasks to evaluate',
            },
        ),
    ]