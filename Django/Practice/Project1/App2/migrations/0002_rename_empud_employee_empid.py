# Generated by Django 5.0.3 on 2024-05-01 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='empud',
            new_name='empid',
        ),
    ]
