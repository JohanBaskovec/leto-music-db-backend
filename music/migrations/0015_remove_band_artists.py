# Generated by Django 3.2.3 on 2021-05-22 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20210522_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='artists',
        ),
    ]