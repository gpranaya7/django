# Generated by Django 4.2.5 on 2024-12-13 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_bank_id_alter_bank_bank_name_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='branch',
            new_name='branch_name',
        ),
    ]