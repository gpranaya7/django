# Generated by Django 4.0 on 2024-09-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='sal',
            field=models.IntegerField(max_length=10),
        ),
    ]
