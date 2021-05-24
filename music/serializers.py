from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from rest_framework.utils.field_mapping import get_url_kwargs, get_detail_view_name

from music.app_name import application_name
from music.models import AlbumReview, Album, Band, Artist, ArtistBandMembership


#class NamespaceHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
#    def build_url_field(self, field_name, model_class):
#        """
#        Create a field representing the object's own URL.
#        """
#        field_class = self.serializer_url_field
#        field_kwargs = {
#            'view_name': application_name + ':' + get_detail_view_name(model_class)
#        }
#
#        return field_class, field_kwargs


class ArtistSerializer(serializers.ModelSerializer):
    #band_memberships = serializers.HyperlinkedRelatedField(many=True,
    #                                                       view_name=application_name + ':artist-band-membership-detail',
    #                                                       queryset=ArtistBandMembership.objects.all())

    class Meta:
        model = Artist
        fields = ['id', 'name', 'band_memberships']


class AlbumArtistReverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    #bands = serializers.HyperlinkedRelatedField(many=True,
    #                                            view_name=application_name + ':band-detail',
    #                                            queryset=Band.objects.all())
    #artists = serializers.HyperlinkedRelatedField(many=True,
    #                                              view_name=application_name + ':artist-detail',
    #                                              queryset=Artist.objects.all())
    #reviews = serializers.HyperlinkedRelatedField(many=True,
    #                                              view_name=application_name + ':album-review-detail',
    #                                              queryset=AlbumReview.objects.all())

    class Meta:
        model = Album
        fields = ['id', 'name', 'release_date', 'bands', 'artists', 'reviews']


# class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
#    bands = serializers.HyperlinkedRelatedField(many=True,
#                                                view_name=application_name + ':band-detail',
#                                                queryset=Band.objects.all())
#    artists = serializers.HyperlinkedRelatedField(many=True,
#                                                  view_name=application_name + ':artist-detail',
#                                                  queryset=Artist.objects.all())
#
#    class Meta:
#        model = Album
#        fields = ['id', 'name', 'release_date', 'bands', 'artists', 'url']
#
#
# class AlbumReviewReverseSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = AlbumReview
#        fields = ['id', 'rating', 'url']
#
#
# class AlbumViewSerializer(serializers.ModelSerializer):
#    bands = serializers.HyperlinkedRelatedField(many=True,
#                                                view_name=application_name + ':band-detail',
#                                                queryset=Band.objects.all())
#    artists = AlbumArtistReverseSerializer(many=True)
#    reviews = AlbumReviewReverseSerializer(many=True)
#
#    class Meta:
#        model = Album
#        fields = ['id', 'name', 'release_date', 'bands', 'artists', 'url', 'reviews']


class AlbumReviewSerializer(serializers.ModelSerializer):
    #author = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    #album = serializers.HyperlinkedRelatedField(view_name=application_name + ':album-detail',
    #                                            queryset=Album.objects.all())

    class Meta:
        model = AlbumReview
        fields = ['id', 'content', 'rating', 'album', 'author']
        #extra_kwargs = {
        #    'url': {'view_name': application_name + ':album-review-detail'},
        #}


class ArtistBandMembershipSerializer(serializers.ModelSerializer):
    #band = serializers.HyperlinkedRelatedField(view_name=application_name + ':band-detail',
    #                                           queryset=Band.objects.all())
    #artist = serializers.HyperlinkedRelatedField(view_name=application_name + ':artist-detail',
    #                                             queryset=Artist.objects.all())

    class Meta:
        model = ArtistBandMembership
        fields = ['id', 'band', 'artist', 'start_date', 'end_date']
        extra_kwargs = {
            'url': {'view_name': application_name + ':artist-band-membership-detail'},
        }


class BandSerializer(serializers.ModelSerializer):
    #artist_memberships = serializers.HyperlinkedRelatedField(many=True,
    #                                                         view_name=application_name + ':artist-band-membership-detail',
    #                                                         queryset=ArtistBandMembership.objects.all())

    class Meta:
        model = Band
        fields = ['id', 'name', 'artist_memberships']
