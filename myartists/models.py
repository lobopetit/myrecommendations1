# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Artist(models.Model):
    name = models.TextField()
    city = models.TextField(default="")
    country = models.TextField(blank=True, null=True)
    style = models.TextField(blank=False)
    web = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myartists:artist_detail', kwargs={'pk': self.pk})


class Album(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="myartists", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    artist = models.ForeignKey(Artist, null=True, related_name='albums')

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myartists:album_detail', kwargs={'pkr': self.artist.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class ArtistReview(Review):
    artist = models.ForeignKey(Artist)