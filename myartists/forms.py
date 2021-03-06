from django.forms import ModelForm
from myartists.models import Artist, Album, Song

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user', 'date',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('Artist', 'user', 'date',)

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ('Artist', 'user', 'date',)