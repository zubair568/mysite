# Generated by Django 3.2.16 on 2023-01-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230117_2227'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='member',
        ),
    ]