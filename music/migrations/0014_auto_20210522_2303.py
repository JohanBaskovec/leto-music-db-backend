# Generated by Django 3.2.3 on 2021-05-22 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0013_auto_20210522_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='bands', to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='music.album'),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
