from django.urls import path, include
from rest_framework import routers

from music.app_name import application_name
from music import views

# defines the namespace for the urls, so URL names can be
# prefixed by 'music:', for example 'music:index'
app_name = application_name

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'album-reviews', views.AlbumReviewSet, basename='album-review')
router.register(r'artists', views.ArtistSet)
router.register(r'bands', views.BandSet)
router.register(r'artist-band-membership', views.ArtistBandMembershipSet, basename='artist-band-membership')

urlpatterns = [
#    path('', views.index, name='index'),
#    path('album', views.AlbumListView.as_view(), name='album_list'),
#    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album_details'),
#    path('album/<int:pk>/write-review', views.WriteAlbumReview.as_view(), name='write_review'),
#    path('album/<int:pk>/update-review', views.UpdateAlbumReview.as_view(), name='update_review'),
    path('', include(router.urls)),
]
