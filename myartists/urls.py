from django.conf.urls import patterns, url
from django.views.generic import UpdateView

from views import *


urlpatterns = patterns('',
    #URLS ARTISTS

    # List latest 5 artists: /myartists/
    url(r'^$',Inici.as_view(),name='artist_list'),

    # Artist details, ex.: /myartists/artists/1/
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetail.as_view(), name='artist_detail'),

    # Create a artist: /myartists/artists/create/
    url(r'^artists/create/$', ArtistCreate.as_view(), name='artist_create'),

    # Edit artist details, ex: /myartists/artists/1/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Artist, form_class=ArtistForm, template_name='myartists/form.html'),
        name='artist_edit'),

    # Artist album details, ex: /myartists/artists/1/albums/1/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/$',
        DetailView.as_view(model=Album, template_name='album_detail.html'),
        name='album_detail'),

    # Create a artist album, ex: /myartists/artists/1/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(),
        name='album_create'),

    # Edit artist album details, ex: /myartists/artists/1/albums/1/edit/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Album, form_class=AlbumForm, template_name='myartists/form.html'),
        name='album_edit'),

    # Create a artist review using function, ex: /myartists/artists/1/reviews/create/
    url(r'^artists/(?P<pk>\d+)/reviews/create/$', 'myartists.views.review',  name='review_create'),
    
    #URLS ALBUMS
    
        # List latest 5 albums: /myartists/
    url(r'^$',Inici.as_view(),name='album_list'),

    # Album details, ex.: /myartists/albums/1/
    url(r'^albums/(?P<pk>\d+)/$', AlbumDetail.as_view(), name='album_detail'),

    # Create a album: /myartists/albums/create/
    url(r'^albums/create/$', AlbumCreate.as_view(), name='album_create'),

    # Edit album details, ex: /myartists/albums/1/edit/
    url(r'^albums/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Album, form_class=AlbumForm, template_name='myartists/form.html'),
        name='album_edit'),

    # album album details, ex: /myartists/albums/1/albums/1/
    url(r'^albums/(?P<pkr>\d+)/albums/(?P<pk>\d+)/$',
        DetailView.as_view(model=Album, template_name='myartists/album_detail.html'),
        name='album_detail'),

    # Create a album album, ex: /myartists/albums/1/albums/create/
    url(r'^albums/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(),
        name='album_create'),

    # Edit album album details, ex: /myartists/albums/1/albums/1/edit/
    url(r'^albums/(?P<pkr>\d+)/albums/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Album, form_class=AlbumForm, template_name='myartists/form.html'),
        name='album_edit'),

    # Create a album review using function, ex: /myartists/albums/1/reviews/create/
    url(r'^albums/(?P<pk>\d+)/reviews/create/$', 'myartists.views.review',  name='review_create'),
    
    #URLS SONGS

    # List latest 5 songs: /myartists/
    url(r'^$',Inici.as_view(),name='song_list'),

    # Song details, ex.: /myartists/songs/1/
    url(r'^songs/(?P<pk>\d+)/$',  DetailView.as_view(model=Song, template_name='myartists/song_detail.html'),
        name='song_detail'),

    # Create a song: /myartists/songs/create/
    url(r'^songs/create/$', SongCreate.as_view(), name='song_create'),

    # Edit song details, ex: /myartists/songs/1/edit/
    url(r'^songs/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Song, form_class=SongForm, template_name='myartists/form.html'),
        name='song_edit'),

    # song song details, ex: /myartists/songs/1/songs/1/
    url(r'^songs/(?P<pkr>\d+)/songs/(?P<pk>\d+)/$',
        DetailView.as_view(model=Song, template_name='myartists/song_detail.html'),
        name='song_detail'),

    # Create a song song, ex: /myartists/songs/1/songs/create/
    url(r'^songs/(?P<pk>\d+)/songs/create/$',
        SongCreate.as_view(),
        name='song_create'),

    # Edit song song details, ex: /myartists/songs/1/songs/1/edit/
    url(r'^songs/(?P<pkr>\d+)/songs/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Song, form_class=SongForm, template_name='myartists/form.html'),
        name='song_edit'),

    # Create a song review using function, ex: /myartists/songs/1/reviews/create/
    url(r'^songs/(?P<pk>\d+)/reviews/create/$', 'myartists.views.review',  name='review_create'),
)