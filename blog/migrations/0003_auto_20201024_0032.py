# Generated by Django 2.2.1 on 2020-10-24 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201023_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
    ]
