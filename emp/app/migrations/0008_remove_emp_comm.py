# Generated by Django 4.0 on 2024-09-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_emp_sal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='comm',
        ),
    ]
