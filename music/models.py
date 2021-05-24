from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Profile of ' + self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Instrument(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Artist(models.Model):
    name = models.CharField(max_length=1000)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Band(models.Model):
    name = models.CharField(max_length=1000)
    creation_date = models.DateField(null=True, blank=True)
    disbanding_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class ArtistBandMembership(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='band_memberships')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='artist_memberships')
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Membership of {} in the band {} from {} to {}'.format(self.artist.name, self.band.name,
                                                                      self.start_date, self.end_date)


class ContributionType(models.IntegerChoices):
    MUSICIAN = 1
    COVER_ARTIST = 2
    SOUND_ENGINEER = 3


class Album(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    recording_start = models.DateField(null=True, blank=True)
    recording_end = models.DateField(null=True, blank=True)
    picture = models.CharField(max_length=10000, blank=True)
    bands = models.ManyToManyField(Band, blank=True)
    artists = models.ManyToManyField(Artist, blank=True)

    def __str__(self):
        # creator_names = list(map(lambda b: b.name, self.bands.all())) + list(map(lambda m: m.name, self.artists.all()))
        creator_names = [b.name for b in self.bands.all()] + [m.name for m in self.artists.all()]
        creator_names_str = ', '.join(creator_names)
        return '{} by {} released on {}'.format(self.name,
                                                creator_names_str if creator_names_str else 'Unknown',
                                                self.release_date if self.release_date else 'unknown date')


class AlbumContribution(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ContributionType.choices)

    def __str__(self):
        return 'Contribution to {} by {}'.format(self.album.name, self.artist.name)


class Track(models.Model):
    order = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=1000, null=False, blank=False, )
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False, blank=False, )
    length = models.DurationField(null=False, blank=False)

    def __str__(self):
        return '{}, track {} on album {}'.format(self.title, self.order, self.album.name)


class TrackContribution(models.Model):
    track = models.ForeignKey(Track, null=False, blank=False, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, null=False, blank=False, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '"{}" playing the {} on track "{}" of album "{}"'.format(self.artist.name, self.instrument.name,
                                                                        self.track.title,
                                                                        self.track.album.name)


class AlbumReview(models.Model):
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(100)])
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='album_reviews')
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return 'Review by "{}" of the album "{}" made on {}'.format(self.author.username,
                                                                    self.album.name, self.publication_date)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'album'], name='one_review_per_user_per_album'),
        ]
