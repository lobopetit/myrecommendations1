from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Artist, Album, ArtistReview


class ArtistSerializer(HyperlinkedModelSerializer):
	#url = HyperlinkedIdentityField(view_name='myartists:artist-detail')
	#albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='myartists:album-detail')
	#artistreview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='myartists:artistreview-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Artist
		#fields = ('url', 'name', 'city', 'country', 'style', 'web', 'user', 'date', 'albums', 'artistreview_set')
        fields = ('name', 'city', 'country', 'style', 'web')

class AlbumSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='myartists:album-detail')
	artist = HyperlinkedRelatedField(view_name='myartists:artist-detail', read_only=True)
	user = CharField(read_only=True)

	class Meta:
		model = Album
		fields = ('url', 'name', 'description', 'price', 'image', 'user', 'date', 'artist')


class ArtistReviewSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='myartists:artistreview-detail')
	artist = HyperlinkedRelatedField(view_name='myartists:artist-detail', read_only=True)
	user = CharField(read_only=True)

	class Meta:
		model = ArtistReview
		fields = ('url', 'rating', 'comment', 'user', 'date', 'artist')