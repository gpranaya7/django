# Generated by Django 4.0 on 2024-09-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_emp_sal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='sal',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]