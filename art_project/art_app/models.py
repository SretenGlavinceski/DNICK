from django.db import models
from django.contrib.auth.models import User


# Изложба: наслов, датум на почеток, датум на завршување, опис, локација.

class Exhibition(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_finish = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='art_works/', blank=True, null=True)

    def num_of_artist_at_exhibition(self):
        return Artist.objects.filter(artwork__exhibition__id=self.id).distinct().count()

    def num_of_artworks_at_exhibition(self):
        return ArtWork.objects.filter(exhibition__id=self.id).count()

    def list_artworks_text(self):
        artworks_text = ''

        for artwork in ArtWork.objects.filter(exhibition__id=self.id).all():
            artworks_text += artwork.title
            artworks_text += ', '

        return artworks_text[:-2]

    def __str__(self):
        return f'{self.title} in {self.location}'


# Уметник: име (и презиме), уметнички стил (impressionism, pop art, graffiti).

class Artist(models.Model):
    TYPE_OF_ART = [
        ('I', 'impressionism'),
        ('P', 'pop art'),
        ('G', 'graffiti')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    art_type = models.CharField(max_length=1, choices=TYPE_OF_ART, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.get_art_type_display()}'


# Уметничко дело: наслов, датум на создавање, слика.

class ArtWork(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date_creation = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='art_works/', blank=True, null=True)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
