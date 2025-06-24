from django.db import models
from django.contrib.auth.models import User


class TourGuide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Tour(models.Model):
    place = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    duration_days = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.CASCADE, blank=True, null=True, related_name='tours')

    def __str__(self):
        return f'{self.place} | Duration: {self.duration_days}'



