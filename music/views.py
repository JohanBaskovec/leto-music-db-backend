from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from music.forms import AlbumReviewForm
from music.models import Album, AlbumReview


def index(request):
    return render(request, 'music/index.html')


class AlbumListView(generic.ListView):
    template_name = 'music/album/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        q = Album.objects.all()
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        albums = context['albums']
        for album in albums:
            album_review = AlbumReview.objects.filter(author=self.request.user, album=album).first()
            album.review = album_review
        return context


class AlbumDetailView(generic.DetailView):
    template_name = 'music/album/album_details.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = {}
        review = AlbumReview.objects.filter(album=self.object, author=self.request.user).first()
        context['review'] = review
        return super().get_context_data(**context)


class WriteAlbumReview(generic.CreateView):
    form_class = AlbumReviewForm
    template_name = 'music/album/write-review.html'

    def get_success_url(self):
        return reverse('music:update_review', args=[self.kwargs['pk']])

    def get_initial(self):
        return {'album': self.kwargs['pk']}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object = self.object.save()
        return super().form_valid(form)


class UpdateAlbumReview(generic.UpdateView):
    model = AlbumReview
    form_class = AlbumReviewForm
    template_name = 'music/album/update-review.html'

    def get_object(self, queryset=None):
        o = AlbumReview.objects.filter(author=self.request.user, album=self.kwargs['pk']).first()
        return o

    def get_success_url(self):
        return reverse('music:update_review', args=[self.kwargs['pk']])

    def get_initial(self):
        return {'album': self.kwargs['pk']}
