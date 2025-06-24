from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import *
import random


@receiver(pre_delete, sender=TourGuide)
def add_tour_guide_to_tours(sender, instance, **kwargs):
    tours_by_guide = Tour.objects.filter(tour_guide=instance).all()

    for tour in tours_by_guide:
        tour.tour_guide = random.choice(TourGuide.objects.exclude(id=instance.id).all())
        tour.save()
