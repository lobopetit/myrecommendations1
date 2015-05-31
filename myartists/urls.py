from django.conf.urls import patterns, url
from django.views.generic import UpdateView
from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from models import Album, Artist, Song
from forms import ArtistForm, AlbumForm
from views import *
from myartists import views

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

    # Delete a artist
    url(r'^artists/(?P<pk>\d+)/delete/$',ArtistDelete.as_view(), name='artist_delete'),


    # Artist album details, ex: /myartists/artists/1/albums/1/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/$',
        DetailView.as_view(model=Album, template_name='album_detail.html'),
        name='album_detail'),

    # Create a artist album, ex: /myartists/artists/1/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(),
        name='album_create'),

    # Delete an album
    url(r'^artists/(?P<pk>\d+)/delete/$',AlbumDelete.as_view(), name='album_delete'),


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

#RESTful API

router = routers.DefaultRouter()
router.register(r'artists', views.AlbumViewSet)
router.register(r'albums', views.AlbumViewSet)


urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
	url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/artists/$', APIArtistList.as_view(), name='artist-list'),
	url(r'^api/artists/(?P<pk>\d+)/$', APIAlbumDetail.as_view(), name='artist-detail'),
	url(r'^api/albums/$', login_required(APIAlbumList.as_view()), name='album-list'),
	url(r'^api/albums/(?P<pk>\d+)/$', APIArtistDetail.as_view(), name='album-detail'),
	url(r'^api/artistreviews/$', APIArtistReviewList.as_view(), name='artistreview-list'),
	url(r'^api/artistreviews/(?P<pk>\d+)/$', APIArtistReviewDetail.as_view(), name='artistreview-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])