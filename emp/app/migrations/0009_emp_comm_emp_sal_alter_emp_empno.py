# Generated by Django 4.0 on 2024-09-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_emp_comm'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='comm',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='emp',
            name='sal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='empno',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
