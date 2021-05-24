from django.contrib.auth.models import User
from rest_framework import serializers, permissions

from music.models import AlbumReview


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'album_reviews']
