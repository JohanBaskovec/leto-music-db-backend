# Generated by Django 3.2.3 on 2021-05-21 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210521_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='creation_year',
        ),
    ]
