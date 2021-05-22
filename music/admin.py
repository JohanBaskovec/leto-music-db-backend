from django.contrib import admin

# Register your models here.
from music.models import Artist, Album, Instrument, AlbumReview, Profile, Band, TrackContribution, AlbumContribution, \
    Track

admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(AlbumReview)
admin.site.register(Instrument)
admin.site.register(AlbumContribution)
admin.site.register(Track)
admin.site.register(TrackContribution)
