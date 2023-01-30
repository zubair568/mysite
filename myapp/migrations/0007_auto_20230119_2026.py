# Generated by Django 3.2.16 on 2023-01-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_full_name_member_f_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='l_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default='', max_length=122),
        ),
        migrations.AlterField(
            model_name='member',
            name='f_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(default='', max_length=120),
        ),
    ]