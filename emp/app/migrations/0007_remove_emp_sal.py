# Generated by Django 4.0 on 2024-09-26 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_emp_sal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='sal',
        ),
    ]
