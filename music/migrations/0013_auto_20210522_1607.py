# Generated by Django 3.2.3 on 2021-05-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_albumreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='bands',
            field=models.ManyToManyField(blank=True, to='music.Band'),
        ),
    ]
