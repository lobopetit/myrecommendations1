# Create your views here.
from django.core import serializers
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from rest_framework import generics, permissions
from myartists import serializers
from rest_framework import viewsets

from myartists.serializers import ArtistSerializer, AlbumSerializer, ArtistReviewSerializer
from models import ArtistReview, AlbumReview, SongReview, Artist, Album, Song
from forms import ArtistForm, AlbumForm, SongForm

class ConneqResponseMixin(TemplateResponseMixin):
    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, concent_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, concent_type=u"application/xml")

    def render_to_response(self, context, **response_kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects = objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects = objects)
        else:
            return super (ConneqResponseMixin, self).render_to_response(context)

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

### RESTful API views ###

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = serializers.ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIAlbumList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIArtistReviewList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = ArtistReview
    queryset = ArtistReview.objects.all()
    serializer_class = ArtistReviewSerializer

class APIArtistReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = ArtistReview
    queryset = ArtistReview.objects.all()
    serializer_class = ArtistReviewSerializer

