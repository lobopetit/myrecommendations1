from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from models import Artist, Album
from forms import ArtistForm, AlbumForm
from views import ArtistCreate, AlbumCreate, ArtistDetail

urlpatterns = patterns('',
    # List latest 5 artists: /myartists/
    url(r'^$',
        ListView.as_view(
            queryset=Artist.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_artist_list',
            template_name='myartists/artist_list.html'),
        name='artist_list'),

    # Artist details, ex.: /myartists/artists/1/
    url(r'^artists/(?P<pk>\d+)/$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    # Create a artist: /myartists/artists/create/
    url(r'^artists/create/$',
        ArtistCreate.as_view(),
        name='artist_create'),

    # Edit artist details, ex: /myartists/artists/1/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Artist,
            form_class=ArtistForm,
            template_name='myartists/form.html'),
        name='artist_edit'),

    # Artist album details, ex: /myartists/artists/1/albums/1/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Album,
            template_name='myartists/album_detail.html'),
        name='album_detail'),

    # Create a artist album, ex: /myartists/artists/1/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(),
        name='album_create'),

    # Edit artist album details, ex: /myartists/artists/1/albums/1/edit/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Album,
            form_class=AlbumForm,
            template_name='myartists/form.html'),
        name='album_edit'),

    # Create a artist review using function, ex: /myartists/artists/1/reviews/create/
    url(r'^artists/(?P<pk>\d+)/reviews/create/$',
        'myartists.views.review',
        name='review_create'),
)