# Generated by Django 3.2.3 on 2021-05-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_albumcontribution_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='length',
            field=models.DurationField(),
            preserve_default=False,
        ),
    ]
