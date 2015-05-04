# Create your views here.

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from models import ArtistReview, AlbumReview, SongReview, Artist, Album, Song
from forms import ArtistForm, AlbumForm, SongForm

class ArtistDetail(DetailView):
    model = Artist
    template_name = 'myartists/artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = ArtistReview.RATING_CHOICES
        return context

class ArtistCreate(CreateView):
    model = Artist
    template_name = 'myartists/form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

class AlbumDetail(DetailView):
    model = Album
    template_name = 'myartists/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = AlbumReview.RATING_CHOICES
        return context

class AlbumCreate(CreateView):
    model = Album
    template_name = 'myartists/form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

class SongDetail(DetailView):
    model = Artist
    template_name = 'myartists/song_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SongDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = SongReview.RATING_CHOICES
        return context

class SongCreate(CreateView):
    model = Song
    template_name = 'myartists/form.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)

def review(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    new_review = ArtistReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        artist=artist)
    new_review.save()
    return HttpResponseRedirect(urlresolvers.reverse('myartists:artist_detail', args=(artist.id,)))

class Inici(ListView):
    model =  Artist
    template_name = 'myartists/artist_list.html'
    queryset = Artist.objects.all()
    context_object_name='artists_list'