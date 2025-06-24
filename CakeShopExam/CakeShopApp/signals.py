from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import *

import random


@receiver(pre_delete, sender=Baker)
def assign_cake_baker(sender, instance, **kwargs):
    for cake in Cake.objects.filter(baker_id=instance.id).all():
        cake.baker = random.choice(Baker.objects.exclude(id=instance.id).all())
        cake.save()
