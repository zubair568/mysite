# Generated by Django 3.2.16 on 2023-01-17 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='user',
        ),
    ]