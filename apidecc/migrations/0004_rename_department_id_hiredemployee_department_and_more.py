# Generated by Django 4.0.5 on 2023-05-22 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apidecc', '0003_alter_department_department_alter_job_job_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiredemployee',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='hiredemployee',
            old_name='job_id',
            new_name='job',
        ),
    ]
