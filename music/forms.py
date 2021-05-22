from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import models

from music.models import AlbumReview


class AlbumReviewForm(models.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ['rating', 'content', 'album']
        widgets = {'album': forms.HiddenInput()}
