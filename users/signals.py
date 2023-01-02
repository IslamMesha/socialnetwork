from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from users.tasks import enrich_geolocation_data


@receiver(post_save, sender=User)
def enrich_user_geolocation_data(sender, instance, created, **kwargs):
    if created:
        # enrich_geolocation_data.delay(user_pk=instance.pk)
        enrich_geolocation_data(user_pk=instance.pk)
