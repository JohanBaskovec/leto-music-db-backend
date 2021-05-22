from django.urls import path

from music import views

# defines the namespace for the urls, so URL names can be
# prefixed by 'music:', for example 'music:index'
app_name='music'

urlpatterns = [
    path('', views.index, name='index'),
    path('album', views.AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album_details'),
    path('album/<int:pk>/write-review', views.WriteAlbumReview.as_view(), name='write_review'),
    path('album/<int:pk>/update-review', views.UpdateAlbumReview.as_view(), name='update_review'),
]
