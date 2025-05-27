from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import *


@receiver(pre_save, sender=Property)
def assign_agent_sold_property(sender, instance, **kwargs):
    old_property = Property.objects.filter(id=instance.id).first()
    if old_property and old_property.is_sold is False and instance.is_sold is True:
        for agent_prop in PropertyAgent.objects.filter(property_id=instance.id).all():
            agent = agent_prop.agent
            agent.sold_properties += 1
            agent.save()
